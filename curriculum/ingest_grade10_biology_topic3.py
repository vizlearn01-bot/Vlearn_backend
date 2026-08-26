"""
VLearn Grade 10 Biology — Topic 3: Cell Structure and Specialization
Production Ingestion Engine (5 Comprehensive Lessons)

Curriculum: CBC (Curriculum ID: 5)
Grade: Grade 10 (Grade ID: 5, Level: 10)
Subject: Biology (Grade 10 CBC)
Topic: Cell Structure and Specialization (Topic Order: 3)

Structured into 5 Comprehensive Learning Units & 5 Published Lessons (47 Concept Cards):
  1. Microscopy: Light and Electron Microscopes (10 Pages)
  2. Temporary Slides and Microscopic Observation (10 Pages)
  3. Plant and Animal Cell Structure and Functions (10 Pages)
  4. Specialized Cells and Adaptation to Function (9 Pages)
  5. Levels of Organization in Living Organisms (9 Pages)

Usage:
  ./venv/bin/python curriculum/ingest_grade10_biology_topic3.py [--replace]
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
    """Removes bracket citations [184, 185], visual prompt text, and cleans double spaces."""
    if not text:
        return ""
    # Remove bracket citations like [184], [184, 185], [image_1]
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

def build_topic3_curriculum():
    """Returns the comprehensive pedagogical page and block structure for Grade 10 Biology Topic 3."""
    return [
        # =====================================================================
        # LESSON 3.1: Microscopy: Light and Electron Microscopes
        # =====================================================================
        {
            "unit_order": 1,
            "unit_name": "Microscopy: Light and Electron Microscopes",
            "unit_description": "Principles of microscopy, magnification vs resolution, comparative mechanics of light and electron microscopes, and high vacuum specimen constraints.",
            "lesson_title": "Microscopy: Light and Electron Microscopes",
            "pages": [
                # Page 1: Introduction & Learning Focus
                [
                    {
                        "type": "learning_goal",
                        "title": "Learning Focus: Principles of Microscopy",
                        "content": {
                            "title": "Learning Focus: Principles of Microscopy",
                            "goals": [
                                "Differentiate between magnifying power and resolving power in biological microscopy.",
                                "Compare the structure, working principles, capabilities, and limitations of light and electron microscopes.",
                                "Explain why high vacuum conditions are required for electron microscopy and how this dictates biological specimen preparation."
                            ]
                        }
                    },
                    {
                        "type": "concept_explanation",
                        "title": "Opening the Window into the Microscopic Realm",
                        "content": {
                            "title": "Opening the Window into the Microscopic Realm",
                            "text": "If you look at your hand, you see smooth skin. But if you could zoom in ten thousand times, you would see a bustling city of trillions of living, working cells.\n\nFor thousands of years, humans had no idea cells existed because our eyes cannot see anything smaller than 0.1 millimeters ($100\\ \\mu\\text{m}$). The invention of the microscope changed everything, opening a window into the invisible world of microscopic life."
                        }
                    }
                ],
                # Page 2: Key Terms
                [
                    {
                        "type": "definition_card",
                        "title": "Microscopy & Optical Physics Vocabulary",
                        "content": {
                            "term": "Essential Microscopy Terminology",
                            "definition": "Key concepts governing optical and electronic magnification instruments.",
                            "key_points": [
                                "Microscope: An optical or electronic instrument used to produce enlarged, resolved images of structures too small to be seen with the naked human eye.",
                                "Magnification: The number of times larger an image appears compared to the actual physical size of the specimen.",
                                "Resolution (Resolving Power): The minimum distance by which two separate points must be separated for an optical system to distinguish them as two distinct entities.",
                                "Photomicrograph: A photograph of a microscopic specimen captured through an optical or electron microscope.",
                                "Vacuum: A space completely devoid of air and matter, required in electron microscopes to prevent air molecules from deflecting electron beams."
                            ]
                        }
                    }
                ],
                # Page 3: Magnification vs Resolution
                [
                    {
                        "type": "concept_explanation",
                        "title": "Magnification versus Resolution: Mathematical vs Physical Limits",
                        "content": {
                            "title": "Magnification versus Resolution: Mathematical vs Physical Limits",
                            "text": "Microscopes are foundational to cytology. However, making an object look bigger (**magnification**) is scientifically useless unless we can also see the fine sub-cellular details clearly (**resolution**):\n\n1. **Magnification** is purely mathematical:\n$$\\text{Total Magnification} = \\text{Eyepiece Lens Magnification} \\times \\text{Objective Lens Magnification}$$\n\n2. **Resolution** is governed by the physical wavelength of the illumination source. Radiation with shorter wavelengths can pass between closer adjacent structures, resolving them as separate points. If two structures are closer than a microscope's resolution threshold, they blur together into a single blob regardless of how much magnification is increased."
                        }
                    }
                ],
                # Page 4: Visualizing Resolution: Low vs High Resolution SVG
                [
                    {
                        "type": "suggested_diagram",
                        "title": "Visualizing Optical Physics: Magnification vs. Resolving Power",
                        "content": {
                            "description": "Comparative diagram illustrating magnification vs resolution. Left panel: Two adjacent points magnified 100x but blurred together as a single indistinct oval (High Magnification, Low Resolution). Right panel: The same two points magnified 100x and clearly resolved as two distinct sharp circles (High Magnification, High Resolution).",
                            "caption": "Comparison of empty magnification (blurred points) vs high resolving power (crisply separated points)."
                        }
                    }
                ],
                # Page 5: Comparing Light and Electron Microscopes
                [
                    {
                        "type": "comparison_table",
                        "title": "Compound Light Microscope vs Transmission/Scanning Electron Microscope",
                        "content": {
                            "headers": ["Characteristic / Parameter", "Compound Light Microscope (LM)", "Electron Microscope (TEM / SEM)"],
                            "rows": [
                                ["Radiation Source", "Visible light rays (~400 to 700 nm wavelength)", "High-velocity electron beam (~0.005 nm wavelength)"],
                                ["Lenses Used", "Curved optical glass lenses", "Electromagnetic coils (solenoids)"],
                                ["Maximum Useful Magnification", "Up to approximately 1,500×", "Up to 500,000× to 2,000,000×"],
                                ["Resolving Limit", "~200 nm (0.2 µm) — limited by light wavelength", "~0.2 nm to 0.5 nm (reveals molecular & organelle ultrastructure)"],
                                ["Specimen State", "Can examine living moving cells or stained dead tissues", "Dead, dehydrated, and heavy-metal stained specimens only"],
                                ["Operating Medium", "Air at atmospheric pressure", "High vacuum chamber (to prevent electron scattering)"],
                                ["Image Produced", "True color (natural or dyed)", "Monochrome black and white (electron density map)"],
                                ["Cost & Portability", "Affordable, lightweight, portable, simple preparation", "Extremely expensive floor-standing units requiring specialized facilities"]
                            ]
                        }
                    }
                ],
                # Page 6: Research Transmission Electron Microscope Image
                [
                    {
                        "type": "suggested_image",
                        "title": "Modern Research Transmission Electron Microscope (TEM) Laboratory Unit",
                        "content": {
                            "description": "High-resolution photograph of a modern floor-standing Transmission Electron Microscope (TEM) showing the vertical electromagnetic column, electron gun chamber, vacuum pumps, and digital imaging monitor workstation.",
                            "caption": "A research-grade Transmission Electron Microscope utilizing high-velocity electron beams in a vacuum column to resolve sub-cellular organelles down to 0.2 nanometers."
                        }
                    }
                ],
                # Page 7: The Vacuum Constraint & Empty Magnification Misconception
                [
                    {
                        "type": "concept_explanation",
                        "title": "The Vacuum Constraint & Empty Magnification",
                        "content": {
                            "title": "The Vacuum Constraint & Empty Magnification",
                            "text": "Because electrons are subatomic particles with tiny mass, they are easily deflected by atmospheric nitrogen and oxygen molecules. To maintain a straight, focused beam, electron microscopes must maintain a **high vacuum**.\n\n**Biological Implications**:\n- Living cells burst and dehydrate instantly in a vacuum; thus, electron microscopy can **only view dead, preserved specimens**.\n- Specimens must be sliced into ultra-thin sections and stained with heavy metals (gold, lead, osmium) to create contrast."
                        }
                    },
                    {
                        "type": "common_misconception",
                        "title": "Misconception: Stronger Glass Lenses Can Magnify 100,000x",
                        "content": {
                            "misconception": "If we build a light microscope with stronger, thicker glass lenses, we can magnify objects 100,000x and see individual viruses clearly.",
                            "correction": "No matter how perfect or thick glass lenses are, light microscopes can NEVER resolve structures smaller than 200 nanometers. This is a fundamental physical barrier dictated by the wavelength of visible light (~400–700 nm). Any magnification beyond 1,500x under a light microscope is 'empty magnification'—the image gets larger but remains completely blurry."
                        }
                    }
                ],
                # Page 8: Deep Dive Educational Video
                [
                    {
                        "type": "suggested_video",
                        "title": "Deep Dive: Microscopy — Light vs. Electron Microscopes",
                        "content": {
                            "description": "Educational video exploring optical light microscopy, transmission and scanning electron microscopes, magnification formulas, and resolving power limits."
                        }
                    }
                ],
                # Page 9: Knowledge Check
                [
                    {
                        "type": "knowledge_check",
                        "title": "Check Your Understanding: Choosing Microscopes for Phagocytosis",
                        "content": {
                            "question": "A medical researcher wants to observe how a living human white blood cell moves and engulfs a live bacterium in real time. Which microscope must they choose, and why?",
                            "options": [
                                "An electron microscope, because its high magnification of 500,000x allows the researcher to see the bacterium's cell wall clearly.",
                                "A light microscope, because it can view live, moving specimens in real time, whereas the high vacuum inside an electron microscope kills cells instantly.",
                                "An electron microscope, because its resolution is high enough to display the engulfing process in natural live colors.",
                                "A dissecting electron microscope with glass objective lenses."
                            ],
                            "correct_answer": "B",
                            "explanation": "Active physiological processes like phagocytosis can only be observed in living cells using a light microscope. Because electron microscopes require a strict high vacuum, all specimens must be dead, dehydrated, and chemically fixed."
                        }
                    }
                ],
                # Page 10: Summary
                [
                    {
                        "type": "summary",
                        "title": "Lesson Summary: Principles of Microscopy",
                        "content": {
                            "title": "Lesson Summary: Principles of Microscopy",
                            "points": [
                                "Magnification enlarges image dimensions; resolution provides visual clarity by separating adjacent points.",
                                "Light microscopes use glass lenses and visible light to examine live or dead cells up to ~1,500× magnification with a 200 nm resolution limit.",
                                "Electron microscopes utilize electromagnetic coils and electron beams in a vacuum to achieve up to 500,000× magnification and 0.2 nm resolution on dead specimens.",
                                "Magnification beyond the resolving limit is empty magnification."
                            ]
                        }
                    }
                ]
            ]
        },

        # =====================================================================
        # LESSON 3.2: Temporary Slides and Microscopic Observation
        # =====================================================================
        {
            "unit_order": 2,
            "unit_name": "Temporary Slides and Microscopic Observation",
            "unit_description": "Slide preparation procedures (sectioning, staining, 45° coverslip mounting), Field of View (FOV) calibration, cell size estimation in micrometers, and laboratory safety.",
            "lesson_title": "Temporary Slides and Microscopic Observation",
            "pages": [
                # Page 1: Introduction & Learning Focus
                [
                    {
                        "type": "learning_goal",
                        "title": "Learning Focus: Slide Preparation & Micro-Measurement",
                        "content": {
                            "title": "Learning Focus: Slide Preparation & Micro-Measurement",
                            "goals": [
                                "Explain the purpose of sectioning, staining, and mounting in temporary slide preparation.",
                                "Prepare a temporary wet mount slide of an onion epidermis safely and procedurally.",
                                "Calibrate the microscope's Field of View (FOV) and estimate actual cell sizes in micrometers (µm)."
                            ]
                        }
                    },
                    {
                        "type": "concept_explanation",
                        "title": "Preparing Cells for Microscopic Investigation",
                        "content": {
                            "title": "Preparing Cells for Microscopic Investigation",
                            "text": "How do biologists observe the internal cellular organization of living tissues? They don't just guess; they prepare ultra-thin slices of tissues, stain them with diagnostic biological dyes, and mount them as **temporary slides**.\n\nIn this lesson, we master the techniques for preparing plant wet mounts and calculate the actual physical dimensions of single microscopic cells."
                        }
                    }
                ],
                # Page 2: Key Terms
                [
                    {
                        "type": "definition_card",
                        "title": "Slide Preparation & Measurement Vocabulary",
                        "content": {
                            "term": "Essential Cytological Techniques",
                            "definition": "Key concepts in laboratory slide preparation and micro-metrology.",
                            "key_points": [
                                "Temporary Slide (Wet Mount): A slide prepared for immediate observation using a liquid medium and coverslip, meant for short-term study.",
                                "Sectioning: Slicing specimen tissues into extremely thin layers (1–2 cells thick) to allow light rays to pass freely.",
                                "Staining: Applying chemical dyes (e.g. Iodine solution, Methylene blue) to selectively color specific cell components like nuclei or cell walls.",
                                "Mounting: Placing the specimen on a glass slide in liquid under a thin coverslip to keep it flat and protect objective lenses.",
                                "Field of View (FOV): The circular lighted area visible when looking through the eyepiece lens.",
                                "Micrometer (µm): Metric unit of length equal to one-thousandth of a millimeter ($1\\text{ mm} = 1,000\\ \\mu\\text{m}$)."
                            ]
                        }
                    }
                ],
                # Page 3: The 4 Stages of Slide Preparation
                [
                    {
                        "type": "step_process",
                        "title": "The Four Standard Stages of Temporary Slide Preparation",
                        "content": {
                            "title": "The Four Standard Stages of Temporary Slide Preparation",
                            "steps": [
                                {
                                    "step_number": 1,
                                    "title": "Thin Sectioning",
                                    "description": "Thick tissues block light completely, appearing black under transmitted light. Tissues must be sliced or peeled into single-cell-thick layers so light passes freely."
                                },
                                {
                                    "step_number": 2,
                                    "title": "Fixation & Hydration",
                                    "description": "Mounting the specimen immediately in a drop of clean water preserves cell turgor, prevents dehydration, and keeps tissue flat."
                                },
                                {
                                    "step_number": 3,
                                    "title": "Diagnostic Staining",
                                    "description": "Transparent cell parts are made visible using diagnostic dyes: Iodine Solution binds to starch and turns nuclei dark brown/orange; Methylene Blue stains animal cell nuclei bright blue."
                                },
                                {
                                    "step_number": 4,
                                    "title": "45° Coverslip Mounting",
                                    "description": "Lowering a clean coverslip slowly at a 45-degree angle with a mounted needle forces air outwards, preventing obstructive air bubbles."
                                }
                            ]
                        }
                    }
                ],
                # Page 4: Calculating Cell Size Using Field of View (FOV)
                [
                    {
                        "type": "concept_explanation",
                        "title": "Method: Calculating Cell Size Using Field of View (FOV)",
                        "content": {
                            "title": "Method: Calculating Cell Size Using Field of View (FOV)",
                            "text": "A microscope serves as a precision micro-measuring tool through a two-step calculation:\n\n**Step 1: Determine the Diameter of the Field of View (FOV)**\n1. Place a clear plastic millimeter ruler on the stage under low power.\n2. Count the millimeter intervals visible across the diameter of the circular lighted field (e.g. 3 mm).\n3. Convert millimeters to micrometers by multiplying by 1,000:\n$$\\text{FOV Diameter} = 3\\text{ mm} \\times 1,000 = 3,000\\ \\mu\\text{m}$$\n\n**Step 2: Estimate the Actual Size of a Single Cell**\n1. Place your prepared specimen slide on the stage.\n2. Count how many cells lie end-to-end lengthwise across the diameter (e.g. 15 cells).\n3. Apply the cell size formula:\n$$\\text{Actual Cell Size} = \\frac{\\text{Diameter of Field of View (FOV)}}{\\text{Number of Cells Aligned Across Diameter}} = \\frac{3,000\\ \\mu\\text{m}}{15\\text{ cells}} = 200\\ \\mu\\text{m}$$"
                        }
                    }
                ],
                # Page 5: Field of View Calibration SVG
                [
                    {
                        "type": "suggested_diagram",
                        "title": "Microscope Field of View (FOV) Calibration & Cell Size Calculation",
                        "content": {
                            "description": "Two-panel vector diagram. Panel 1: Circular low-power Field of View with a millimeter ruler scale aligned across diameter, showing 3 mm = 3,000 micrometers. Panel 2: The same circular field with 15 rectangular onion epidermal cells aligned end-to-end across diameter, showing the calculation 3,000 um / 15 cells = 200 um per cell.",
                            "caption": "Step-by-step microscopic metrology: converting millimeter ruler markings into micrometers and dividing by cell count."
                        }
                    }
                ],
                # Page 6: Practical Investigation: Onion Epidermis Slide Preparation
                [
                    {
                        "type": "step_process",
                        "title": "Practical Protocol: Onion Epidermal Wet Mount Preparation",
                        "content": {
                            "title": "Practical Protocol: Onion Epidermal Wet Mount Preparation",
                            "steps": [
                                {
                                    "step_number": 1,
                                    "title": "Peel Transparent Epidermis",
                                    "description": "Use forceps to gently peel a thin, transparent single-cell-thick epidermal layer from the inner concave scale of an onion bulb."
                                },
                                {
                                    "step_number": 2,
                                    "title": "Mount Flat in Water Droplet",
                                    "description": "Place the peel flat in a water droplet on a clean glass slide without folds or creases."
                                },
                                {
                                    "step_number": 3,
                                    "title": "Stain with Iodine",
                                    "description": "Add one drop of brown-yellow Iodine solution. Let stand 1 minute to stain nuclei and cell walls."
                                },
                                {
                                    "step_number": 4,
                                    "title": "Lower Coverslip at 45°",
                                    "description": "Rest coverslip on liquid edge at 45° and lower slowly with a needle to eliminate air bubbles. Blot excess stain."
                                }
                            ]
                        }
                    },
                    {
                        "type": "callout",
                        "title": "KICD Biological Safety Mandate",
                        "content": {
                            "title": "KICD Biological Safety Mandate",
                            "text": "**CRITICAL SAFETY RULE**: Never use human cheek cells or blood samples in school laboratories. This strict curriculum safety rule prevents the potential transmission of blood-borne viral pathogens (such as HIV and Hepatitis). Use only safe plant tissues (onion, Tradescantia) or baker's yeast."
                        }
                    }
                ],
                # Page 7: Light Micrograph: Stained Onion Epidermal Cells at 400x
                [
                    {
                        "type": "suggested_image",
                        "title": "Light Micrograph of Stained Onion Epidermal Cells at 400x",
                        "content": {
                            "description": "High-clarity light micrograph of Allium cepa (onion) epidermal cells stained with iodine at 400x magnification, displaying regular rectangular cell walls, cytoplasm, and distinct stained nuclei.",
                            "caption": "Light micrograph of onion epidermal cells at 400x magnification revealing rigid rectangular cellulose walls, cytoplasm, and dark stained nuclei."
                        }
                    }
                ],
                # Page 8: Deep Dive Educational Video
                [
                    {
                        "type": "suggested_video",
                        "title": "Deep Dive: Step-by-Step Slide Preparation and Field of View Calculation",
                        "content": {
                            "description": "Laboratory demonstration showing onion epidermal peeling, iodine staining, bubble-free coverslip mounting, and field of view calibration formulas."
                        }
                    }
                ],
                # Page 9: Knowledge Check
                [
                    {
                        "type": "knowledge_check",
                        "title": "Check Your Understanding: Calculating Cell Size",
                        "content": {
                            "question": "A student measures their microscope's field of view diameter under low power and finds it is 2.5 millimeters. They switch to their prepared kale slide and count approximately 20 cells lined up side-by-side across this diameter. What is the estimated actual width of an individual cell in micrometers?",
                            "options": [
                                "125 µm",
                                "12.5 µm",
                                "8 µm",
                                "800 µm"
                            ],
                            "correct_answer": "A",
                            "explanation": "First, convert the FOV diameter from millimeters to micrometers: 2.5 mm × 1,000 = 2,500 µm. Next, divide the FOV diameter by the cell count: 2,500 µm / 20 cells = 125 µm."
                        }
                    }
                ],
                # Page 10: Summary
                [
                    {
                        "type": "summary",
                        "title": "Lesson Summary: Slide Preparation & Micro-Measurement",
                        "content": {
                            "title": "Lesson Summary: Slide Preparation & Micro-Measurement",
                            "points": [
                                "Temporary slide preparation requires thin sectioning, water mounting, diagnostic staining, and 45° coverslip lowering.",
                                "Iodine solution selectively stains cell walls and nuclei brown-yellow for optical contrast.",
                                "Field of View diameter divided by cell count provides accurate microscopic cell size in micrometers ($1\\text{ mm} = 1,000\\ \\mu\\text{m}$).",
                                "School laboratory safety strictly bans human tissue sampling to eliminate pathogen transmission."
                            ]
                        }
                    }
                ]
            ]
        },

        # =====================================================================
        # LESSON 3.3: Plant and Animal Cell Structure and Functions
        # =====================================================================
        {
            "unit_order": 3,
            "unit_name": "Plant and Animal Cell Structure and Functions",
            "unit_description": "Organelles under electron microscope (mitochondria cristae, chloroplast grana/stroma, ER, Golgi, lysosomes, vacuoles, centrioles), and detailed plant vs animal cell comparison.",
            "lesson_title": "Plant and Animal Cell Structure and Functions",
            "pages": [
                # Page 1: Introduction & Learning Focus
                [
                    {
                        "type": "learning_goal",
                        "title": "Learning Focus: Eukaryotic Cell Ultrastructure",
                        "content": {
                            "title": "Learning Focus: Eukaryotic Cell Ultrastructure",
                            "goals": [
                                "Describe the fine structure and functions of plant and animal cell organelles as revealed by electron microscopy.",
                                "Relate the physical ultrastructure of organelles (mitochondria cristae, chloroplast grana/stroma) to their biological metabolic roles.",
                                "Compare plant and animal cells, identifying key structural similarities and differences."
                            ]
                        }
                    },
                    {
                        "type": "concept_explanation",
                        "title": "The Microscopic Automated Factory: The Cell",
                        "content": {
                            "title": "The Microscopic Automated Factory: The Cell",
                            "text": "Think of a single living cell not as a simple bag of jelly, but as a highly automated, ultra-modern biochemical factory. It contains its own protective outer walls, a central genetic database (nucleus), energy generators, protein synthesis assembly lines, packaging departments, and internal transport highways.\n\nIn this lesson, we explore the internal compartments—called **organelles**—that coordinate eukaryotic cellular life."
                        }
                    }
                ],
                # Page 2: Key Terms
                [
                    {
                        "type": "definition_card",
                        "title": "Cellular Organelles Vocabulary",
                        "content": {
                            "term": "Essential Eukaryotic Organelles",
                            "definition": "Specialized sub-cellular membrane-bound structures performing discrete biochemical functions.",
                            "key_points": [
                                "Organelle: A specialized membrane-bound sub-cellular structure suspended in cytoplasm performing specific biochemical tasks.",
                                "Cell Membrane: A semi-permeable phospholipid bilayer with embedded proteins controlling the passage of substances.",
                                "Nucleus: The double-membrane-bound control center containing genetic chromatin DNA and nucleolus.",
                                "Mitochondrion: The double-membrane 'powerhouse' where aerobic respiration occurs to synthesize ATP energy.",
                                "Chloroplast: The double-membrane photosynthetic organelle containing chlorophyll in thylakoid grana stacks.",
                                "Ribosome: A tiny non-membrane-bound particle composed of RNA and protein that synthesizes polypeptide chains.",
                                "Endoplasmic Reticulum (ER): Membrane network: Rough ER transports proteins; Smooth ER synthesizes lipids and steroids.",
                                "Golgi Apparatus: Flattened membrane sacs that modify, sort, package, and secrete cellular proteins into vesicles.",
                                "Lysosome: A membrane-bound vesicle containing hydrolytic digestive enzymes that break down worn organelles and pathogens.",
                                "Cell Wall: A rigid outer layer made of cellulose in plant cells providing mechanical support and turgor resistance."
                            ]
                        }
                    }
                ],
                # Page 3: Detailed Eukaryotic Ultrastructure SVG Diagram
                [
                    {
                        "type": "suggested_diagram",
                        "title": "Detailed Ultrastructure: Plant Cell vs. Animal Cell",
                        "content": {
                            "description": "Comparative side-by-side vector diagram of Plant Cell vs Animal Cell under electron microscopy. Plant Cell: Thick cellulose wall, plasma membrane, large central vacuole with tonoplast, chloroplasts with grana stacks, mitochondria with cristae, nucleus, rough/smooth ER, Golgi. Animal Cell: Flexible membrane, central nucleus, multiple mitochondria, centriole pair at 90 degrees, lysosomes, small vacuoles.",
                            "caption": "Comparative electron micrograph diagrams of eukaryotic plant and animal cell ultrastructure."
                        }
                    }
                ],
                # Page 4: Energy & Control Organelles
                [
                    {
                        "type": "concept_explanation",
                        "title": "The Powerhouses & Control Centers of the Cell",
                        "content": {
                            "title": "The Powerhouses & Control Centers of the Cell",
                            "text": "1. **Mitochondrion (Plural: Mitochondria)**:\n- *Structure*: Sausage-shaped double membrane. The inner membrane is extensively folded into **cristae**, enclosing a fluid **matrix** with respiratory enzymes.\n- *Adaptation & Function*: The site of aerobic cellular respiration. Folded cristae provide a massive surface area for electron transport enzymes, maximizing **ATP** energy generation.\n\n2. **Chloroplast (Plants Only)**:\n- *Structure*: Double-membrane organelle containing disc-like **thylakoids** stacked into **grana**, suspended in a fluid **stroma**.\n- *Adaptation & Function*: The site of photosynthesis. Thylakoid grana contain **chlorophyll** to trap light energy for photolysis; stroma fixes $CO_2$ into glucose.\n\n3. **Nucleus**:\n- *Structure*: Enclosed by a double nuclear membrane with pores, containing **chromatin** (coiled DNA) and a **nucleolus** (which manufactures ribosomes).\n- *Function*: Directs all metabolic and developmental cellular activities."
                        }
                    }
                ],
                # Page 5: Synthesis, Secretion, and Structural Organelles
                [
                    {
                        "type": "comparison_table",
                        "title": "Endomembrane, Secretory, and Structural Organelles",
                        "content": {
                            "headers": ["Organelle", "Structural Characteristics", "Metabolic Function & Adaptation"],
                            "rows": [
                                ["Rough Endoplasmic Reticulum (RER)", "Membrane network studded with ribosomes", "Folds and transports newly synthesized proteins to the Golgi apparatus"],
                                ["Smooth Endoplasmic Reticulum (SER)", "Tubular membrane channels lacking ribosomes", "Synthesizes lipids, phospholipids, and steroid hormones; detoxifies chemicals"],
                                ["Golgi Apparatus", "Stacks of flattened cisternae producing vesicles", "Modifies, packages, sorts, and secretes cellular proteins and enzymes"],
                                ["Lysosomes", "Spherical vesicles with hydrolytic enzymes", "Digests worn-out organelles, cellular debris, and engulfed pathogens ('cell suicide' if burst)"],
                                ["Vacuoles", "Membrane-bound sacs with cell sap", "Plants: One large permanent central vacuole maintaining turgor; Animals: Small temporary vacuoles"],
                                ["Centrioles (Animals Only)", "Pair of cylindrical structures at 90°", "Organizes spindle fibers during chromosome separation in cell division"],
                                ["Cellulose Cell Wall (Plants Only)", "Rigid outer layer of cellulose fibers", "Provides mechanical rigidity, maintains fixed shape, and prevents osmotic bursting"]
                            ]
                        }
                    }
                ],
                # Page 6: TEM Micrograph: Organelle Ultrastructure
                [
                    {
                        "type": "suggested_image",
                        "title": "Transmission Electron Micrograph (TEM) of Mitochondria and Organelles",
                        "content": {
                            "description": "High-resolution Transmission Electron Micrograph (TEM) showing a mammalian cell cross-section detailing a mitochondrion with distinct folded inner cristae and dense matrix, adjacent to rough endoplasmic reticulum studded with ribosomes.",
                            "caption": "Transmission electron micrograph (TEM) revealing the internal cristae folds of a mitochondrion and surrounding rough endoplasmic reticulum."
                        }
                    }
                ],
                # Page 7: Comprehensive Plant vs Animal Comparison & Misconception
                [
                    {
                        "type": "comparison_table",
                        "title": "Structural Differences: Plant vs Animal Cells",
                        "content": {
                            "headers": ["Feature / Organelle", "Plant Cell", "Animal Cell"],
                            "rows": [
                                ["Cell Wall", "Present; rigid outer layer made of cellulose", "Completely absent"],
                                ["Chloroplasts & Plastids", "Present in photosynthetic cells (leaves/stems)", "Completely absent"],
                                ["Vacuoles", "One large, permanent central vacuole filled with cell sap", "Small, temporary, scattered vacuoles (or absent)"],
                                ["Centrioles", "Absent in higher plants", "Present (organizes mitotic spindle fibers)"],
                                ["Cell Shape", "Regular, fixed, and rigid (rectangular/polygonal)", "Irregular, flexible, and variable"],
                                ["Storage Carbohydrate", "Starch granules and oils", "Glycogen granules and fats"],
                                ["Nucleus Position", "Peripheral (pushed to side by central vacuole)", "Centrally located"]
                            ]
                        }
                    },
                    {
                        "type": "common_misconception",
                        "title": "Misconception: Plant Cells Do Not Need Mitochondria",
                        "content": {
                            "misconception": "Because plant cells have chloroplasts to make food, they do not need mitochondria.",
                            "correction": "Plant cells contain BOTH chloroplasts and mitochondria! Chloroplasts act purely as solar panels to manufacture glucose. However, cells cannot use raw glucose directly; they must break it down to release usable ATP energy. Mitochondria perform this essential cellular respiration day and night in all living plant cells."
                        }
                    }
                ],
                # Page 8: Deep Dive Educational Video
                [
                    {
                        "type": "suggested_video",
                        "title": "Deep Dive: Eukaryotic Cell Structure, Organelles, and Ultrastructure",
                        "content": {
                            "description": "Detailed video exploration of eukaryotic organelle ultrastructure, mitochondria cristae, chloroplast thylakoids, and comparative plant vs animal cytology."
                        }
                    }
                ],
                # Page 9: Knowledge Check
                [
                    {
                        "type": "knowledge_check",
                        "title": "Check Your Understanding: Organelle Density in Active Tissues",
                        "content": {
                            "question": "Cells that line human kidney tubules constantly pump mineral ions back into the bloodstream against concentration gradients—a process requiring massive amounts of chemical ATP energy (active transport). Which organelle would you expect to find in exceptionally high concentrations inside these kidney tubule cells?",
                            "options": [
                                "Lysosomes",
                                "Rough Endoplasmic Reticulum",
                                "Mitochondria",
                                "Chloroplasts"
                            ],
                            "correct_answer": "C",
                            "explanation": "Mitochondria are the respiratory powerhouses of the cell, responsible for synthesizing ATP through aerobic respiration. Cells with heavy active transport demands (such as kidney tubules, root hair cells, and active muscle fibers) are densely packed with mitochondria."
                        }
                    }
                ],
                # Page 10: Summary
                [
                    {
                        "type": "summary",
                        "title": "Lesson Summary: Cell Ultrastructure & Organelles",
                        "content": {
                            "title": "Lesson Summary: Cell Ultrastructure & Organelles",
                            "points": [
                                "Electron microscopy reveals membrane-bound organelles with structure-to-function specialization.",
                                "Mitochondria have folded cristae for ATP respiration; chloroplasts possess thylakoid grana for photosynthesis.",
                                "The nucleus, ribosomes, ER, and Golgi apparatus cooperate in protein synthesis and secretion.",
                                "Plant cells are distinguished by rigid cellulose walls, large central vacuoles, and chloroplasts."
                            ]
                        }
                    }
                ]
            ]
        },

        # =====================================================================
        # LESSON 3.4: Specialized Cells and Adaptation to Function
        # =====================================================================
        {
            "unit_order": 4,
            "unit_name": "Specialized Cells and Adaptation to Function",
            "unit_description": "Cell differentiation, division of labor, and structure-to-function adaptations in plant cells (root hair, palisade, guard, pollen) and animal cells (RBC, sperm, neuron).",
            "lesson_title": "Specialized Cells and Adaptation to Function",
            "pages": [
                # Page 1: Introduction & Learning Focus
                [
                    {
                        "type": "learning_goal",
                        "title": "Learning Focus: Cell Specialization & Adaptations",
                        "content": {
                            "title": "Learning Focus: Cell Specialization & Adaptations",
                            "goals": [
                                "Define cell differentiation and cell specialization in multicellular organisms.",
                                "Relate the physical structural adaptations of specialized plant cells (root hair, palisade, guard, pollen) to their functions.",
                                "Relate the physical structural adaptations of specialized animal cells (erythrocytes, sperm cells, motor neurons) to their functions."
                            ]
                        }
                    },
                    {
                        "type": "concept_explanation",
                        "title": "Division of Labor: Cellular Differentiation",
                        "content": {
                            "title": "Division of Labor: Cellular Differentiation",
                            "text": "A multicellular organism is like a modern society. If every person tried to do every job—farming, medicine, engineering, transport—nothing would be done efficiently. Multicellular life works because of **division of labor**.\n\nInstead of all cells remaining identical, they undergo **differentiation** to become structurally modified to execute specific physiological jobs with maximum efficiency."
                        }
                    }
                ],
                # Page 2: Key Terms
                [
                    {
                        "type": "definition_card",
                        "title": "Differentiation & Specialization Vocabulary",
                        "content": {
                            "term": "Essential Developmental Terminology",
                            "definition": "Key concepts in cell modification and physiological division of labor.",
                            "key_points": [
                                "Cell Differentiation: The developmental process by which unspecialized stem cells undergo structural and functional modifications to become specialized.",
                                "Cell Specialization: The condition of a cell being structurally modified to carry out a particular physiological role within a multicellular organism.",
                                "Adaptation: Any physical or biochemical modification that enhances a cell's efficiency in performing its dedicated function."
                            ]
                        }
                    }
                ],
                # Page 3: Specialized Cell Adaptations Matrix SVG
                [
                    {
                        "type": "suggested_diagram",
                        "title": "Specialized Plant and Animal Cell Adaptations Matrix",
                        "content": {
                            "description": "Six-panel visual matrix showing specialized cell adaptations. Plant side: Root hair cell (elongated lateral extension), Palisade mesophyll cell (columnar with dense chloroplasts), Guard cell pair (thick inner wall and pore). Animal side: Red blood cell (biconcave disc without nucleus), Sperm cell (acrosome, midpiece mitochondria, flagellum), Motor neuron (long axon with myelin sheath).",
                            "caption": "Structure-to-function adaptations across six major specialized eukaryotic cells."
                        }
                    }
                ],
                # Page 4: Specialized Plant Cells and Adaptations
                [
                    {
                        "type": "comparison_table",
                        "title": "Specialized Plant Cells: Structure-to-Function Adaptations",
                        "content": {
                            "headers": ["Specialized Plant Cell", "Anatomical Location", "Major Structural Adaptations", "Dedicated Physiological Function"],
                            "rows": [
                                ["Root Hair Cell", "Root epidermis", "Long, thin lateral cytoplasmic extension; thin cell wall; lack of chloroplasts; high solute vacuole", "Vastly increases surface area for rapid absorption of water by osmosis and mineral ions by active transport"],
                                ["Palisade Mesophyll Cell", "Upper leaf mesophyll", "Columnar shape; tightly packed vertically; contains the highest density of chloroplasts", "Maximizes sunlight capture for photosynthesis; columnar shape allows deep light penetration"],
                                ["Guard Cell", "Leaf epidermis", "Crescent-shaped pairs; thick inelastic inner wall; thin elastic outer wall", "Regulates stomatal pore aperture: turgor stretching opens pore for gas exchange; flaccidity closes pore to conserve water"],
                                ["Pollen Grain", "Flower anther", "Thick, tough resistant outer wall (exine); light aerodynamic or spiky sticky surface", "Protects male genetic gametes during transport by wind or insect pollinators to stigma"]
                            ]
                        }
                    }
                ],
                # Page 5: Specialized Animal Cells and Adaptations
                [
                    {
                        "type": "comparison_table",
                        "title": "Specialized Animal Cells: Structure-to-Function Adaptations",
                        "content": {
                            "headers": ["Specialized Animal Cell", "Location / Tissue", "Major Structural Adaptations", "Dedicated Physiological Function"],
                            "rows": [
                                ["Red Blood Cell (Erythrocyte)", "Bloodstream", "Biconcave disc shape; lacks nucleus and mitochondria when mature; flexible membrane; packed with hemoglobin", "Maximizes surface-area-to-volume ratio for rapid $O_2$ diffusion; lack of nucleus provides maximum space for oxygen-carrying hemoglobin"],
                                ["Sperm Cell (Male Gamete)", "Testes / Semen", "Streamlined head with acrosome enzymes; midpiece packed with mitochondria; long flagellum tail", "Acrosome digests outer egg coat; mitochondria generate ATP to power flagellar swimming to ovum for fertilization"],
                                ["Motor Neuron (Nerve Cell)", "Nervous system", "Extremely elongated axon (up to 1 meter); fatty myelin sheath insulation; branched dendrites", "Conducts high-speed electrical nerve impulses across long bodily distances without signal dissipation"]
                            ]
                        }
                    }
                ],
                # Page 6: SEM Micrograph: Human Red Blood Cells
                [
                    {
                        "type": "suggested_image",
                        "title": "Scanning Electron Micrograph (SEM) of Human Red Blood Cells",
                        "content": {
                            "description": "High-resolution Scanning Electron Micrograph (SEM) showing the characteristic biconcave disc shape of human erythrocytes, displaying the indented central surfaces optimized for oxygen diffusion.",
                            "caption": "Scanning electron micrograph (SEM) of mammalian red blood cells revealing the biconcave disc geometry that maximizes surface-area-to-volume ratio for oxygen transport."
                        }
                    }
                ],
                # Page 7: Deep Dive Educational Video
                [
                    {
                        "type": "suggested_video",
                        "title": "Deep Dive: Specialized Cells and Adaptations to Function",
                        "content": {
                            "description": "Video presentation exploring cellular differentiation, plant cell adaptations (root hairs, palisade, guard cells), and animal cell specializations (erythrocytes, neurons, sperm)."
                        }
                    }
                ],
                # Page 8: Knowledge Check
                [
                    {
                        "type": "knowledge_check",
                        "title": "Check Your Understanding: Consequences of RBC Nucleus Retention",
                        "content": {
                            "question": "A mutant animal is born with red blood cells that fail to lose their nuclei during maturation. Which physiological consequence will this animal most likely suffer from?",
                            "options": [
                                "Its red blood cells will divide uncontrollably, forming tumors.",
                                "The cells will carry significantly less oxygen, causing the animal to suffer chronic fatigue during exertion, because the nucleus occupies valuable internal space that should be packed with hemoglobin.",
                                "The cells will be too small to squeeze through capillaries, blocking blood flow.",
                                "The cells will consume all the oxygen they transport because the nucleus contains chloroplasts."
                            ],
                            "correct_answer": "B",
                            "explanation": "The biconcave, anucleate (nucleus-free) structure of mature mammalian red blood cells is an adaptation to dedicate maximum internal volume to packing hemoglobin. Retaining the nucleus severely reduces hemoglobin capacity, leading to poor oxygen delivery and rapid fatigue."
                        }
                    }
                ],
                # Page 9: Summary
                [
                    {
                        "type": "summary",
                        "title": "Lesson Summary: Specialized Cells & Adaptations",
                        "content": {
                            "title": "Lesson Summary: Specialized Cells & Adaptations",
                            "points": [
                                "Cell differentiation modifies unspecialized cells into specialized shapes with dedicated organelle distributions.",
                                "Root hair cells maximize surface area for water/mineral absorption; palisade cells maximize chloroplast density for photosynthesis.",
                                "Red blood cells lose nuclei to maximize hemoglobin space; sperm cells use midpiece mitochondria and flagella for motility.",
                                "In every specialized cell, physical structure directly dictates biological function."
                            ]
                        }
                    }
                ]
            ]
        },

        # =====================================================================
        # LESSON 3.5: Levels of Organization in Living Organisms
        # =====================================================================
        {
            "unit_order": 5,
            "unit_name": "Levels of Organization in Living Organisms",
            "unit_description": "The 6 hierarchical tiers of biological organization (organelle, cell, tissue, organ, organ system, organism) in plants and animals, and the advantages of division of labor.",
            "lesson_title": "Levels of Organization in Living Organisms",
            "pages": [
                # Page 1: Introduction & Learning Focus
                [
                    {
                        "type": "learning_goal",
                        "title": "Learning Focus: Hierarchy of Biological Organization",
                        "content": {
                            "title": "Learning Focus: Hierarchy of Biological Organization",
                            "goals": [
                                "Describe the nested hierarchy of biological organization: Organelle → Cell → Tissue → Organ → Organ System → Organism.",
                                "Identify representative examples of tissues, organs, and organ systems in both plants and animals.",
                                "Explain the evolutionary and physiological advantages of division of labor in multicellular organisms."
                            ]
                        }
                    },
                    {
                        "type": "concept_explanation",
                        "title": "Nature's Hierarchical Architecture",
                        "content": {
                            "title": "Nature's Hierarchical Architecture",
                            "text": "You cannot build a car by throwing metal, rubber, and glass into a heap. First, you forge pistons and cylinders (parts). You assemble them into an engine (component). You connect the engine to fuel and electrical lines to form the drive system (system). Finally, you assemble the complete car.\n\nNature builds multicellular organisms in the exact same nested hierarchical manner—bridging sub-cellular organelles to complete living entities."
                        }
                    }
                ],
                # Page 2: Key Terms
                [
                    {
                        "type": "definition_card",
                        "title": "Biological Hierarchy Vocabulary",
                        "content": {
                            "term": "Essential Architectural Levels",
                            "definition": "The progressive structural tiers of living systems.",
                            "key_points": [
                                "Tissue: A group of similar specialized cells integrated to perform a specific common function.",
                                "Organ: A distinct structural unit composed of two or more different tissues working cooperatively to carry out a major physiological role.",
                                "Organ System: A group of organs cooperating sequentially to carry out a comprehensive bodily life process.",
                                "Division of Labour: The allocation of specific physiological tasks to specialized cells, tissues, and organs, maximizing efficiency and survivability."
                            ]
                        }
                    }
                ],
                # Page 3: Nested Concentric Hierarchy SVG Diagram
                [
                    {
                        "type": "suggested_diagram",
                        "title": "Nested Hierarchy of Biological Organization",
                        "content": {
                            "description": "Concentric nested circular diagram showing the 6 ascending levels of biological organization: Organelle -> Cell -> Tissue -> Organ -> Organ System -> Organism. Beside it, dual parallel pathways for plants (Chloroplast -> Palisade Cell -> Mesophyll Tissue -> Leaf -> Shoot System -> Whole Plant) and animals (Mitochondrion -> Muscle Cell -> Cardiac Tissue -> Heart -> Circulatory System -> Human).",
                            "caption": "Nested structural hierarchy bridging sub-cellular organelles to complete multicellular organisms."
                        }
                    }
                ],
                # Page 4: The 6 Levels of Biological Hierarchy
                [
                    {
                        "type": "step_process",
                        "title": "The Six Tiers of Biological Organization",
                        "content": {
                            "title": "The Six Tiers of Biological Organization",
                            "steps": [
                                {
                                    "step_number": 1,
                                    "title": "Organelle Level",
                                    "description": "Specialized sub-cellular structures (e.g. Mitochondrion, Chloroplast) performing discrete metabolic tasks within a cell."
                                },
                                {
                                    "step_number": 2,
                                    "title": "Cell Level",
                                    "description": "The fundamental structural and functional unit of life (e.g. Red blood cell, Root hair cell)."
                                },
                                {
                                    "step_number": 3,
                                    "title": "Tissue Level",
                                    "description": "A group of similar specialized cells working together. Plant: Epidermal, Mesophyll, Vascular (Xylem/Phloem). Animal: Epithelial, Muscular, Nervous, Connective (Blood/Bone)."
                                },
                                {
                                    "step_number": 4,
                                    "title": "Organ Level",
                                    "description": "Different coordinated tissues performing a major physiological function. Plant: Leaf, Stem, Root, Flower. Animal: Heart, Brain, Lungs, Stomach, Kidneys."
                                },
                                {
                                    "step_number": 5,
                                    "title": "Organ System Level",
                                    "description": "A group of cooperative organs carrying out comprehensive processes. Plant: Shoot system, Root system. Animal: Digestive, Circulatory, Respiratory, Nervous systems."
                                },
                                {
                                    "step_number": 6,
                                    "title": "Organism Level",
                                    "description": "The complete individual living entity capable of independent life and reproduction (e.g. Maize plant, Human being)."
                                }
                            ]
                        }
                    }
                ],
                # Page 5: Organism Ecosystem Image
                [
                    {
                        "type": "suggested_image",
                        "title": "Biological Organization: From Cells to Multicellular Organisms",
                        "content": {
                            "description": "High-resolution photograph of a diverse Kenyan ecosystem showcasing multicellular plants and mammals, illustrating the culmination of biological organization into complete living organisms.",
                            "caption": "Multicellular organisms represent the integrated coordination of trillions of cells organized into tissues, organs, and organ systems."
                        }
                    }
                ],
                # Page 6: Advantages of Division of Labor
                [
                    {
                        "type": "concept_explanation",
                        "title": "Why Division of Labor Drives Multicellular Evolution",
                        "content": {
                            "title": "Why Division of Labor Drives Multicellular Evolution",
                            "text": "Unicellular organisms must carry out every life process—feeding, waste excretion, movement, defense—within a single microscopic cell. If that single cell is damaged, the organism dies.\n\nMulticellular organisms escape this bottleneck through the **division of labor**:\n- **Maximum Efficiency**: Specialized tissues and organs perform one function with extraordinary speed and precision.\n- **Large Size & Complexity**: Organ systems (like circulatory and vascular tracks) allow organisms to grow large without diffusion limitations.\n- **Damage Resilience**: Injury to one cell or tissue does not cause immediate organism death; specialized cells can divide to regenerate and repair damaged parts."
                        }
                    }
                ],
                # Page 7: Deep Dive Educational Video
                [
                    {
                        "type": "suggested_video",
                        "title": "Deep Dive: Levels of Biological Organization — From Organelles to Organisms",
                        "content": {
                            "description": "Video guide exploring the hierarchy of life: organelle, cell, tissue, organ, organ system, and multicellular organism integration."
                        }
                    }
                ],
                # Page 8: Knowledge Check
                [
                    {
                        "type": "knowledge_check",
                        "title": "Check Your Understanding: Classifying Plant Structures",
                        "content": {
                            "question": "Under which level of biological organization should a student classify a fresh celery stalk, and why?",
                            "options": [
                                "Tissue, because it is composed of uniform xylem cells that transport water.",
                                "Organelle, because it contains chloroplasts.",
                                "Organ, because it is a stem structure composed of multiple tissues (epidermis, vascular bundles, and parenchyma) working together to support the plant and transport materials.",
                                "Organ System, because it contains both root and leaf structures."
                            ],
                            "correct_answer": "C",
                            "explanation": "A stem (the celery stalk) is a plant organ. It is composed of different tissues—including epidermal tissue for protection, vascular tissue (xylem and phloem) for fluid transport, and ground parenchyma tissue for support and storage—integrated to carry out stem functions."
                        }
                    }
                ],
                # Page 9: Summary
                [
                    {
                        "type": "summary",
                        "title": "Lesson Summary: Levels of Biological Organization",
                        "content": {
                            "title": "Lesson Summary: Levels of Biological Organization",
                            "points": [
                                "Living things are organized into a nested hierarchy: Organelle → Cell → Tissue → Organ → Organ System → Organism.",
                                "Tissues combine similar cells; organs integrate diverse tissues for complex physiological functions.",
                                "In plants, roots, stems, leaves, and flowers are organs; in animals, heart, lungs, and brain form systems.",
                                "The division of labor enables multicellular organisms to attain large body sizes, high efficiency, and environmental resilience."
                            ]
                        }
                    }
                ]
            ]
        }
    ]

def ingest_grade10_biology_topic3(replace=False):
    """Executes the database ingestion for Grade 10 Biology Topic 3."""
    print("=" * 80)
    print("VLearn Grade 10 Biology — Ingestion Engine")
    print("Topic 3: Cell Structure and Specialization (CBC Curriculum ID: 5)")
    print("=" * 80)

    # 1. Resolve Curriculum
    curriculum = Curriculum.objects.filter(name="CBC").first() or Curriculum.objects.filter(id=5).first()
    if not curriculum:
        print("[!] Fatal: Curriculum 'CBC' (ID: 5) not found in database!")
        return

    print(f"[*] Curriculum: {curriculum.name} (ID: {curriculum.id})")

    # 2. Resolve Grade
    grade = Grade.objects.filter(curriculum=curriculum, name="Grade 10").first() or Grade.objects.filter(curriculum=curriculum, level=10).first()
    if not grade:
        print("[!] Fatal: Grade 'Grade 10' under CBC not found in database!")
        return

    print(f"[*] Grade: {grade.name} (ID: {grade.id}, Level: {grade.level})")

    # 3. Resolve Subject under Grade 10 CBC (Strict Scope Isolation)
    subject, created = Subject.objects.get_or_create(
        grade=grade,
        name="Biology",
        defaults={"description": "Grade 10 Biology Curriculum under CBC senior secondary science pathway."}
    )
    print(f"[*] Subject: {subject.name} under {grade.name} (ID: {subject.id})")

    # 4. Resolve Topic 3
    topic_name = "Cell Structure and Specialization"
    topic = Topic.objects.filter(subject=subject, name=topic_name).first()

    if topic and replace:
        print(f"[*] Found existing Topic '{topic_name}' (ID: {topic.id}). Performing clean replacement of child units/lessons...")
        topic.learning_units.all().delete()
        topic.lessons.all().delete()
    elif not topic:
        topic = Topic.objects.create(
            subject=subject,
            name=topic_name,
            order=3,
            description="Comprehensive syllabus on microscopy (light and electron), temporary slide preparation, cell size calculation, organelle ultrastructure, specialized cells, and levels of biological organization."
        )
        print(f"[+] Created Topic: {topic.name} (ID: {topic.id})")
    else:
        print(f"[*] Using existing Topic: {topic.name} (ID: {topic.id})")

    curriculum_data = build_topic3_curriculum()
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

            learning_unit.name = unit_name
            learning_unit.description = unit_desc
            learning_unit.save()

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
            print(f"  [+] Ingesting Lesson {unit_order}: {lesson.title} (Lesson ID: {lesson.id})")

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
            print(f"      [OK] Ingested {lesson_page_count} Concept Cards for Lesson {unit_order}.")

    print("=" * 80)
    print("[SUCCESS] Grade 10 Biology Topic 3 Ingestion Complete!")
    print(f"[*] Total Lessons Ingested: {total_lessons}")
    print(f"[*] Total Pages/Cards:      {total_pages}")
    print(f"[*] Total Blocks Created:   {total_blocks}")
    print("=" * 80)

if __name__ == "__main__":
    replace_flag = "--replace" in sys.argv
    ingest_grade10_biology_topic3(replace=replace_flag)
