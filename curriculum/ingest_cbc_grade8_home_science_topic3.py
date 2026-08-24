"""
VLearn CBC Grade 8 Home Science — Topic 3: Textile and Clothing
Production Ingestion Engine (Phase 1: Content & Card Architecture)

Curriculum: CBC (Curriculum ID: 5)
Grade: Grade 8 (Level: 8)
Subject: Home Science (ID: 28)
Topic: Textile and Clothing (Topic Order: 3)

Decomposed into 3 Learning Units & 3 Published Lessons (24 Total Structured Pages):
  1. Artificial Textile Fibres (8 Pages)
  2. Seams in Garment Construction (8 Pages)
  3. Methods of Controlling Fullness (8 Pages)

Features:
  - Rich typography with bold key terms, phrases, and structured bullets.
  - Step-by-step process workflows, lab testing protocols, and garment assembly.
  - Formatted comparison tables and practical callouts.

Usage:
  ./venv/bin/python curriculum/ingest_cbc_grade8_home_science_topic3.py [--replace]
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

def build_topic3_curriculum():
    """Returns the comprehensive pedagogical page and block structure for Topic 3: Textile and Clothing."""
    return [
        # =====================================================================
        # LESSON 1: Artificial Textile Fibres
        # =====================================================================
        {
            "unit_order": 1,
            "unit_name": "Artificial Textile Fibres",
            "unit_description": "Fibre classification (Synthetic vs. Regenerated), physical & chemical properties of nylon, polyester, acrylic, viscose & acetate, identification tests (burning, chemical, microscopic), lab safety PPE, and non-biodegradable waste disposal.",
            "lesson_title": "Artificial Textile Fibres",
            "pages": [
                # Page 1: Topic Introduction & Visual Hook
                [
                    {
                        "type": "suggested_image",
                        "title": "Solve the Sweater Mystery: Real Wool vs. Acrylic",
                        "content": {
                            "title": "Solve the Sweater Mystery: Real Wool vs. Acrylic",
                            "caption": "A traditional textile loom where delicate yarns are spun and woven into durable everyday clothing."
                        }
                    },
                    {
                        "type": "learning_goal",
                        "title": "Learning Objectives: Artificial Textile Fibres",
                        "content": {
                            "title": "What We Will Learn Today",
                            "goals": [
                                "Classify textile fibres based on origins, distinguishing between **regenerated fibres** and **fully synthetic fibres**.",
                                "Analyze the distinct properties and applications of **nylon**, **polyester**, **acrylic**, **viscose rayon**, and **acetate rayon**.",
                                "Perform scientific **fabric identification tests**: burning reaction, chemical solubility, and microscopic cross-section analysis.",
                                "Apply mandatory **laboratory PPE protocols** and evaluate the environmental impacts of **non-biodegradable synthetic waste**."
                            ]
                        }
                    },
                    {
                        "type": "concept_explanation",
                        "title": "What Are Artificial Fibres?",
                        "content": {
                            "title": "From Nature to the Laboratory",
                            "text": "Every piece of cloth starts as tiny, hair-like strands called **fibres** spun into yarn. While natural fibres come directly from plants (cotton, linen) or animals (wool, silk), **artificial fibres** are manufactured by humans through industrial and chemical engineering:\n\n• **Regenerated Fibres (Semi-Synthetic)**: Made by chemically dissolving and reforming natural plant materials like **wood cellulose** (e.g. **viscose rayon**, **acetate rayon**).\n• **Synthetic Fibres (Fully Synthetic)**: Made entirely from petrochemical polymers synthesized from petroleum oils, coal, and chemicals (e.g. **nylon**, **polyester**, **acrylic**)."
                        }
                    }
                ],
                # Page 2: The Textile Family Tree
                [
                    {
                        "type": "suggested_diagram",
                        "title": "The Textile Family Tree: Natural vs. Artificial Fibres",
                        "content": {
                            "title": "The Textile Family Tree: Natural vs. Artificial Fibres",
                            "caption": "Conceptual tree diagram showing the branches of Natural, Regenerated, and Synthetic textile fibres."
                        }
                    },
                    {
                        "type": "comparison_table",
                        "title": "Regenerated vs. Synthetic Textile Fibres",
                        "content": {
                            "title": "Classification of Artificial Textile Fibres",
                            "headers": ["Classification", "Raw Material Source", "Key Examples", "Distinctive Characteristic"],
                            "rows": [
                                ["Regenerated (Semi-Synthetic)", "Natural wood pulp cellulose & cotton linters treated with chemicals", "Viscose Rayon, Acetate Rayon", "Soft, absorbent, breathable, and drapes elegantly with a silk-like sheen"],
                                ["Synthetic: Polyamide", "Petroleum chemicals (polymerized diamines + dicarboxylic acids)", "Nylon", "Exceptional tensile strength, high elasticity, lightweight, and waterproof"],
                                ["Synthetic: Polyester", "Petrochemical polymers (ethylene glycol + terephthalic acid)", "Polyester (Terylene, Dacron)", "Supreme crease resistance, hydrophobic (quick drying), and extreme durability"],
                                ["Synthetic: Polyacrylic", "Acrylonitrile petrochemical monomers", "Acrylic (Orlon, Cashmilon)", "Fluffy, light, holds heat exceptionally well, mimicking natural sheep's wool"]
                            ]
                        }
                    },
                    {
                        "type": "callout",
                        "title": "Important Clarification",
                        "content": {
                            "title": "Is Viscose Rayon a Natural Fibre?",
                            "text": "No! Although viscose rayon starts with natural wood pulp, wood cannot be spun into threads naturally. It must be dissolved in sodium hydroxide and carbon disulfide, then extruded through tiny spinneret holes into an acid bath to 'regenerate' as a fibre."
                        }
                    }
                ],
                # Page 3: Properties and Everyday Applications of Synthetics
                [
                    {
                        "type": "suggested_diagram",
                        "title": "Properties and Everyday Applications of Synthetics (Nylon, Polyester, Acrylic)",
                        "content": {
                            "title": "Properties and Everyday Applications of Synthetics",
                            "caption": "Bento infographic matching Nylon (waterproof backpacks), Polyester (wrinkle-free jerseys), and Acrylic (warm sweaters)."
                        }
                    },
                    {
                        "type": "concept_explanation",
                        "title": "Understanding Synthetic Material Superpowers",
                        "content": {
                            "title": "Thermoplasticity and Hydrophobicity",
                            "text": "Synthetic fibres dominate modern clothing in Kenya because of two core physical properties:\n\n• **1. Thermoplasticity (Heat Sensitivity)**: Synthetics soften and melt when exposed to high temperatures. This allows permanent pleating in skirts, but means they will **melt and burn** if ironed with a hot iron!\n• **2. Hydrophobicity (Water Repellency)**: Synthetics absorb almost no water. Polyester sports jerseys and nylon umbrellas dry in minutes because moisture stays on the surface rather than soaking into the fibre core."
                        }
                    }
                ],
                # Page 4: Scientific Fibre Identification Tests
                [
                    {
                        "type": "suggested_diagram",
                        "title": "The Scientific Burning Test and Microscopic Analysis Matrix",
                        "content": {
                            "title": "The Scientific Burning Test and Microscopic Analysis Matrix",
                            "caption": "Visual identification guide showing flame behavior, smoke scent, residue beads, and smooth rod microscopic cross-sections."
                        }
                    },
                    {
                        "type": "comparison_table",
                        "title": "Burning Test Diagnostic Indicators",
                        "content": {
                            "title": "How Fibres React to Heat and Flame",
                            "headers": ["Fibre", "Approaching Flame", "In Flame & Smoke", "Smoke Odor", "Residue / Ash"],
                            "rows": [
                                ["Nylon", "Melts and curls away from heat", "Burns slowly with melting; white smoke", "Distinct **celery-like** chemical smell", "Hard, round, gray-brown uncrushable bead"],
                                ["Polyester", "Melts and curls rapidly", "Burns slowly with dark gray/black smoke", "Distinct **sweet aromatic** chemical smell", "Hard, round, dark black uncrushable bead"],
                                ["Acrylic", "Shrinks and fuses instantly", "Burns rapidly and flares with thick black soot", "Pungent, **acrid sour** chemical smell", "Hard, black, irregular crusty residue"],
                                ["Viscose Rayon", "Catches fire immediately", "Burns rapidly with bright steady yellow flame", "Smells like **burning paper/wood**", "Light, soft, feathery gray ash"],
                                ["Natural Cotton", "Does not melt; catches fire easily", "Burns quickly with steady glowing flame", "Smells like **burning leaves/paper**", "Soft, fine gray ash with no hard bead"],
                                ["Natural Wool", "Burns slowly with sizzling", "Self-extinguishes when removed from flame", "Strong **burning hair/feathers** smell", "Dark, irregular, crisp ash that crushes easily"]
                            ]
                        }
                    }
                ],
                # Page 5: Worked Example — Laboratory Burning Test Procedure
                [
                    {
                        "type": "step_process",
                        "title": "Worked Example: Conducting a Supervised Burning Test on a Mystery Thread",
                        "content": {
                            "title": "Step-by-Step Laboratory Procedure",
                            "steps": [
                                {
                                    "step_number": 1,
                                    "title": "Put On Mandatory PPE",
                                    "description": "Wear a **cotton dust coat**, **safety goggles**, and heat-resistant gloves. Ensure the laboratory has open windows for good cross-ventilation."
                                },
                                {
                                    "step_number": 2,
                                    "title": "Extract Yarn & Grip with Metal Forceps",
                                    "description": "Unravel a 5 cm thread from the fabric swatch. **Grip one end tightly with long metal forceps (tweezers)**—never use bare fingers!"
                                },
                                {
                                    "step_number": 3,
                                    "title": "Approach Flame Slowly",
                                    "description": "Hold the thread near the edge of a candle flame. Observe whether the thread curls away, melts into a drop, or catches fire immediately."
                                },
                                {
                                    "step_number": 4,
                                    "title": "Ignite & Fan Fumes for Smell Check",
                                    "description": "Move the thread into the flame for 2 seconds, remove, blow out, and gently **fan the smoke towards your nose** to identify the smell (celery, sweet, or acrid)."
                                },
                                {
                                    "step_number": 5,
                                    "title": "Cool and Inspect Residue",
                                    "description": "Allow the residue to cool completely. Press it between your fingers to check whether it forms a **hard, uncrushable plastic bead** (synthetic) or **soft, fine ash** (natural)."
                                }
                            ]
                        }
                    }
                ],
                # Page 6: Lab Safety and the Non-Biodegradable Crisis
                [
                    {
                        "type": "suggested_diagram",
                        "title": "Lab Safety PPE and The Non-Biodegradable Synthetic Environmental Crisis",
                        "content": {
                            "title": "Lab Safety PPE and The Environmental Decomposition Timeline",
                            "caption": "Infographic showing mandatory lab safety gear on the left alongside the decomposition timeline of cotton (months) vs synthetic polyester (200+ years)."
                        }
                    },
                    {
                        "type": "concept_explanation",
                        "title": "The Ecological Impact of Synthetic Fabrics",
                        "content": {
                            "title": "Why Synthetics Must Never Be Dumped in Soil",
                            "text": "• **Non-Biodegradable Waste**: Synthetic fibres are forms of plastic made from petrochemicals. While a cotton sock decomposes into soil nutrients within 5 months, a polyester shirt or nylon bag takes **200 to 500 years** to break down in landfills!\n• **Toxic Open-Air Burning**: Burning discarded synthetic clothes releases toxic fumes and carcinogenic chemicals into our air.\n• **The Sustainable Solution**: Instead of throwing away old synthetic garments, **repurpose** them into cleaning cloths, tote bags, or cushion fillings, or donate them for textile recycling."
                        }
                    },
                    {
                        "type": "callout",
                        "title": "Safety Alert",
                        "content": {
                            "title": "Never Burn Synthetics with Bare Hands!",
                            "text": "When synthetic fibres ignite, they melt into molten plastic exceeding 250°C. If molten nylon drops onto bare skin, it sticks and causes severe, painful second-degree chemical burns. Always use long metal forceps!"
                        }
                    }
                ],
                # Page 7: Key Takeaways & Recall Helper
                [
                    {
                        "type": "key_takeaway",
                        "title": "Key Takeaways: Artificial Textile Fibres",
                        "content": {
                            "title": "Core Ideas to Remember",
                            "takeaways": [
                                "**Regenerated fibres** (Viscose, Acetate) originate from chemically processed wood cellulose; **synthetics** (Nylon, Polyester, Acrylic) originate from petrochemical oils.",
                                "**Synthetics are thermoplastic** (melt under high heat) and **hydrophobic** (water-repellent, quick-drying).",
                                "The **burning test** identifies synthetics by their melting behavior, distinctive chemical odors, and hard, uncrushable residue beads.",
                                "Synthetics are **non-biodegradable** and must be repurposed or recycled to protect soils, rivers, and wildlife."
                            ]
                        }
                    },
                    {
                        "type": "memory_tip",
                        "title": "Synthetic Fibre Recall Helper",
                        "content": {
                            "title": "Remember 'N-P-A'",
                            "tip": "**N**ylon (strong & waterproof), **P**olyester (crease-resistant & quick-dry), **A**crylic (warm & wool-like)!"
                        }
                    }
                ],
                # Page 8: Knowledge Check
                [
                    {
                        "type": "knowledge_check",
                        "title": "Knowledge Check: Identifying Artificial Fibres",
                        "content": {
                            "question": "A student unpicks a thread from a mystery sports windbreaker jacket and tests it with a candle flame using forceps. The thread melts and curls away from the heat, burns slowly with a distinct celery-like chemical smell, and leaves a hard, round, uncrushable gray bead. Which fibre is this?",
                            "options": [
                                "Natural Cotton, because it burns with a steady flame.",
                                "Nylon, because melting, a celery-like odor, and a hard uncrushable bead are the unique diagnostic characteristics of nylon.",
                                "Viscose Rayon, because it leaves soft gray ash.",
                                "Natural Wool, because it smells like burning feathers."
                            ],
                            "correct_index": 1,
                            "explanation": "Nylon is a synthetic polyamide fibre that uniquely melts and curls away from flame, produces a characteristic celery-like chemical scent, and hardens into an uncrushable round bead upon cooling."
                        }
                    }
                ]
            ]
        },

        # =====================================================================
        # LESSON 2: Seams in Garment Construction
        # =====================================================================
        {
            "unit_order": 2,
            "unit_name": "Seams in Garment Construction",
            "unit_description": "Classification of seams into inconspicuous (French, plain, open) and conspicuous (overlaid/lapped, machine-fell), factors influencing seam selection, technical construction of French & machine-fell seams, and qualities of well-made seams.",
            "lesson_title": "Seams in Garment Construction",
            "pages": [
                # Page 1: Topic Introduction & Visual Hook
                [
                    {
                        "type": "suggested_image",
                        "title": "Why Do Seams Tear? The Power of Sewing Joins",
                        "content": {
                            "title": "Why Do Seams Tear? The Power of Sewing Joins",
                            "caption": "A precision sewing machine creating durable, even stitching to securely join garment fabric pieces."
                        }
                    },
                    {
                        "type": "learning_goal",
                        "title": "Learning Objectives: Seams in Clothing Construction",
                        "content": {
                            "title": "What We Will Learn Today",
                            "goals": [
                                "Define a **seam** and classify seams into **inconspicuous** (hidden) and **conspicuous** (visible) categories.",
                                "Analyze the **5 critical factors** that govern seam selection (fabric weight, position, wear and tear, design effect).",
                                "Master the step-by-step technical construction of a self-finished **French seam** and a durable **Machine-fell seam**.",
                                "Identify the technical qualities of **well-made seams** and troubleshoot common sewing machine tension faults."
                            ]
                        }
                    },
                    {
                        "type": "concept_explanation",
                        "title": "What is a Seam and Why Does it Matter?",
                        "content": {
                            "title": "The Structural Backbone of Clothing",
                            "text": "A **seam** is a permanent line of stitching that securely joins two or more pieces of fabric together to construct garments and household articles.\n\n• **Durability**: A well-chosen seam withstands daily body movements, sitting tension, and laundry friction.\n• **Comfort & Skin Protection**: Enclosed seams prevent raw fabric threads from fraying, scratching the skin, or causing itchiness.\n• **Aesthetic Appeal**: Neatly executed seams create clean, professional garment style lines."
                        }
                    }
                ],
                # Page 2: Seam Classification (Inconspicuous vs Conspicuous)
                [
                    {
                        "type": "suggested_diagram",
                        "title": "Cross-Section Schematics of Inconspicuous and Conspicuous Seams",
                        "content": {
                            "title": "Cross-Section Schematics of Inconspicuous and Conspicuous Seams",
                            "caption": "Technical layer diagrams showing French seam double fold, Machine-fell flat double-stitch, and Overlaid/Lapped seam."
                        }
                    },
                    {
                        "type": "comparison_table",
                        "title": "Classification of Clothing Seams",
                        "content": {
                            "title": "Inconspicuous vs. Conspicuous Seams",
                            "headers": ["Seam Category", "Appearance on Right Side", "Key Construction Examples", "Primary Uses in Garments"],
                            "rows": [
                                ["Inconspicuous (Hidden)", "Invisible; only a single, flat join line shows on the outside of the garment", "French Seam, Plain Open Seam", "Lightweight fabrics, baby dresses, sheer blouses, side seams of delicate cotton shirts"],
                                ["Conspicuous (Visible)", "Visible; one or two parallel rows of topstitching show prominently on the outside", "Machine-Fell (Double-Stitched) Seam, Overlaid (Lapped) Seam", "Heavy-duty garments, jeans, overalls, sports shorts, decorative bodice yokes"]
                            ]
                        }
                    },
                    {
                        "type": "callout",
                        "title": "Why the French Seam is Special",
                        "content": {
                            "title": "A Self-Finished Seam",
                            "text": "A French seam is called a **self-finished seam** because its double-stitching completely encases all raw fabric edges inside a neat cloth envelope. It requires zero edge-neatening or zig-zag stitching!"
                        }
                    }
                ],
                # Page 3: Factors Influencing Seam Selection
                [
                    {
                        "type": "concept_explanation",
                        "title": "The 5 Factors Governing Seam Selection",
                        "content": {
                            "title": "Choosing the Right Seam for the Job",
                            "text": "You cannot use the same seam on every fabric. Before cutting and sewing, professional tailors evaluate:\n\n• **1. Fabric Weight & Texture**: Lightweight fabrics (silk, chiffon, voile) need narrow **French seams**; heavy fabrics (denim, canvas) need flat, double-stitched **machine-fell seams**.\n• **2. Garment Use & Strain**: Garments exposed to heavy wear and washing (jeans, work overalls) need the immense strength of machine-fell seams.\n• **3. Position of the Seam**: Straight side seams suit French seams; curved armholes and neckline joins require flat **plain seams** that can be notched.\n• **4. Garment Style & Design**: Decorative yokes on jackets and blouses call for the styled topstitching of **overlaid seams**.\n• **5. Laundering Frequency**: Articles washed frequently require fully enclosed seams that will not fray during machine washing."
                        }
                    },
                    {
                        "type": "callout",
                        "title": "Fabric Weight Rule",
                        "content": {
                            "title": "Why You Never Use French Seams on Denim!",
                            "text": "Sewing a French seam on thick denim creates four heavy layers of folded canvas. This produces a huge, rigid lump of cloth that chafes the skin and will instantly snap the sewing machine needle!"
                        }
                    }
                ],
                # Page 4: Worked Example — Constructing a French Seam
                [
                    {
                        "type": "step_process",
                        "title": "Worked Example: Step-by-Step Construction of a French Seam",
                        "content": {
                            "title": "The 5-Step French Seam Method",
                            "steps": [
                                {
                                    "step_number": 1,
                                    "title": "Pin WRONG Sides Together",
                                    "description": "Align fabric pieces with **wrong sides facing each other** (right sides facing out). Pin and stitch **1 cm (3/8 inch)** from the raw edge."
                                },
                                {
                                    "step_number": 2,
                                    "title": "Trim Raw Seam Allowance to 3 mm",
                                    "description": "Using sharp shears, carefully trim the raw seam allowance down to **3 mm (1/8 inch)**. (Trimming close prevents raw thread 'whiskers' from poking through!)."
                                },
                                {
                                    "step_number": 3,
                                    "title": "Press Seam Open",
                                    "description": "Open out the fabric pieces and press the stitching line flat with a warm iron to set the stitches."
                                },
                                {
                                    "step_number": 4,
                                    "title": "Fold RIGHT Sides Together",
                                    "description": "Fold the fabric with **right sides facing each other**, rolling the seam right onto the folded edge. Press the fold sharp."
                                },
                                {
                                    "step_number": 5,
                                    "title": "Stitch Second Line to Encase",
                                    "description": "Stitch a second line **6 mm (1/4 inch)** from the folded edge, completely enclosing the trimmed raw edges inside the neat seam casing."
                                }
                            ]
                        }
                    }
                ],
                # Page 5: Qualities of Well-Made Seams vs Common Faults
                [
                    {
                        "type": "suggested_diagram",
                        "title": "Qualities of Well-Made Seams vs. Common Tailoring Faults",
                        "content": {
                            "title": "Qualities of Well-Made Seams vs. Common Tailoring Faults",
                            "caption": "Diagnostic diagram comparing balanced machine tension, uniform width, and flat pressing against puckering, loose thread loops, and raw whiskers."
                        }
                    },
                    {
                        "type": "concept_explanation",
                        "title": "The Tailor's Quality Checklist",
                        "content": {
                            "title": "4 Marks of Professional Seammanship",
                            "text": "• **1. Uniform Width**: The seam must maintain a perfectly consistent width from top to bottom without wavy wandering.\n• **2. Completely Flat & Unpuckered**: The fabric must lie smooth. Puckering occurs when upper thread tension is too tight or the fabric is pulled forcefully while sewing.\n• **3. Balanced Stitch Tension**: Upper and lower bobbin threads must lock perfectly in the middle of the fabric without loops.\n• **4. Zero Raw 'Whiskers'**: No loose fraying threads should poke through the finished seam."
                        }
                    }
                ],
                # Page 6: Hands-On Seam Troubleshooting Activity
                [
                    {
                        "type": "mini_activity",
                        "title": "Hands-On: Garment Seam Audit & Fault Diagnosis",
                        "content": {
                            "title": "Activity: Audit 3 Household Garments",
                            "instructions": "Inspect three different garments at home or school (e.g. a school shirt, a pair of jeans, and a bedsheet):\n\n1. **Identify the Seam Type**: Is it a French seam, plain seam, machine-fell seam, or overlaid seam?\n2. **Classify**: Inconspicuous (hidden) vs Conspicuous (visible)?\n3. **Quality Check**: Run your finger along the seam. Is it flat, unpuckered, and free of thread whiskers?\n\nRecord your observations in your Home Science notebook."
                        }
                    }
                ],
                # Page 7: Key Takeaways & Recall Helper
                [
                    {
                        "type": "key_takeaway",
                        "title": "Key Takeaways: Seams in Clothing Construction",
                        "content": {
                            "title": "Core Ideas to Remember",
                            "takeaways": [
                                "**Inconspicuous seams** (French, plain) hide on the inside; **conspicuous seams** (machine-fell, overlaid) show visible topstitching on the outside.",
                                "A **French seam** is self-finished through a 2-step stitch that encloses raw edges, ideal for delicate, fraying fabrics.",
                                "**Machine-fell seams** lie flat with double topstitching, providing extreme strength for heavy fabrics like denim.",
                                "Always trim raw edges to **3 mm** before sewing the second row of a French seam to prevent unsightly thread **whiskers**."
                            ]
                        }
                    },
                    {
                        "type": "memory_tip",
                        "title": "Seam Selection Helper",
                        "content": {
                            "title": "Light vs Heavy Seam Rule",
                            "tip": "**French for Fine & Fraying** (Silk, Voile, Chiffon); **Fell for Firm & Heavy** (Denim, Jeans, Overalls)!"
                        }
                    }
                ],
                # Page 8: Knowledge Check
                [
                    {
                        "type": "knowledge_check",
                        "title": "Knowledge Check: Seam Construction & Selection",
                        "content": {
                            "question": "You are making a pair of heavy cotton school play shorts that will experience frequent friction, vigorous sports activity, and repeated washing. Which seam is the most appropriate, and why?",
                            "options": [
                                "A delicate French seam, because it hides raw threads on the inside.",
                                "A Machine-fell (double-stitched) seam, because it lies completely flat, encloses all edges, and provides exceptional double-stitched strength for heavy wear.",
                                "A loose open seam with no edge finishing.",
                                "Gluing the fabric edges together with fabric adhesive."
                            ],
                            "correct_index": 1,
                            "explanation": "Machine-fell seams feature two parallel rows of permanent topstitching that securely lock flat fabric layers, making them the most durable and flat choice for sportswear, work overalls, and play shorts."
                        }
                    }
                ]
            ]
        },

        # =====================================================================
        # LESSON 3: Methods of Controlling Fullness
        # =====================================================================
        {
            "unit_order": 3,
            "unit_name": "Methods of Controlling Fullness",
            "unit_description": "Purpose of controlling fullness, technical anatomy of single & double darts, pleats (box vs inverted), tucks (plain vs decorative), gathers (dual gathering threads), easing, and assembling a child's sleeveless, collarless garment.",
            "lesson_title": "Methods of Controlling Fullness",
            "pages": [
                # Page 1: Topic Introduction & Visual Hook
                [
                    {
                        "type": "suggested_image",
                        "title": "From Flat Fabric to 3D Fit: The Art of Fullness Control",
                        "content": {
                            "title": "From Flat Fabric to 3D Fit: The Art of Fullness Control",
                            "caption": "Skilled garment tailoring where flat fabric is folded, pleated, and darted to create comfortable 3D body contours."
                        }
                    },
                    {
                        "type": "learning_goal",
                        "title": "Learning Objectives: Controlling Fullness",
                        "content": {
                            "title": "What We Will Learn Today",
                            "goals": [
                                "Explain why **controlling fullness** is necessary to transform 2D flat cloth into 3D ergonomic garments.",
                                "Construct and press **single-pointed** and **double-pointed darts** with hand-tied thread tips.",
                                "Compare **box pleats**, **inverted pleats**, and **tucks** (plain and decorative pin tucks).",
                                "Master the mechanics of **gathers** (using 2 parallel basting lines) and invisible **easing**."
                            ]
                        }
                    },
                    {
                        "type": "concept_explanation",
                        "title": "Why Do We Control Fullness?",
                        "content": {
                            "title": "Flat Cloth vs. Curved Human Bodies",
                            "text": "Fabric is manufactured as a flat, two-dimensional sheet. However, the human body is three-dimensional with curves around the bust, waist, hips, and shoulders:\n\n• **Ergonomic Fit**: Removes excess baggy fabric where the body is narrow (such as the waist).\n• **Freedom of Movement**: Adds extra room and expansion where joints bend and muscles move (such as pleated skirts).\n• **Aesthetic Styling**: Creates flattering visual features, textures, and decorative accents (such as gathers, ruffles, and pin tucks)."
                        }
                    }
                ],
                # Page 2: Darts: Single-Pointed and Double-Pointed
                [
                    {
                        "type": "suggested_diagram",
                        "title": "Anatomy and Stitching Procedure of Single and Double-Pointed Darts",
                        "content": {
                            "title": "Anatomy and Stitching Procedure of Darts",
                            "caption": "Technical diagram showing single-pointed dart tapering from wide intake to point, and double-pointed dart tapering at both ends."
                        }
                    },
                    {
                        "type": "concept_explanation",
                        "title": "The Anatomy of Darts",
                        "content": {
                            "title": "Shaping the Waist, Bust, and Hips",
                            "text": "A **dart** is a tapered triangular fold stitched into fabric to shape flat cloth to body contours:\n\n• **Single-Pointed Dart**: Starts wide at a seam line (the **intake**) and tapers smoothly down to a sharp single point. Used at the bust, waist, and shoulder.\n• **Double-Pointed Dart (Fish Dart)**: Widest in the middle and tapers to sharp points at both ends. Used vertically on fitted shirts, blouses, and dresses at the waistline.\n• **The Golden Tailoring Rule**: Always stitch a dart **from the wide end toward the point**. Never backstitch on the sewing machine at the tip; leave long thread tails and **tie a secure square knot by hand** to prevent an unsightly bubble pucker!"
                        }
                    },
                    {
                        "type": "callout",
                        "title": "Common Sewing Mistake",
                        "content": {
                            "title": "Why You Never Backstitch at a Dart Tip",
                            "text": "Machine backstitching at a dart point creates a hard, bulky knot of thread that produces a permanent, unsightly cone or 'bubble' on the outside of the garment."
                        }
                    }
                ],
                # Page 3: Pleats (Box vs. Inverted) and Tucks
                [
                    {
                        "type": "suggested_diagram",
                        "title": "3D Folding Schematics: Box Pleats, Inverted Pleats, and Stitched Tucks",
                        "content": {
                            "title": "3D Folding Schematics: Pleats and Tucks",
                            "caption": "Diagram showing how Box Pleats (folds facing away on right side) are the exact reverse of Inverted Pleats (folds meeting in center), alongside pin tucks."
                        }
                    },
                    {
                        "type": "comparison_table",
                        "title": "Comparing Methods of Fullness Control",
                        "content": {
                            "title": "Pleats vs. Tucks Comparison Guide",
                            "headers": ["Method", "Structural Design", "Everyday Example", "Key Advantage"],
                            "rows": [
                                ["Box Pleat", "Two folds turned in opposite directions, facing away from each other on the right side", "Back of boys' shirts, pleated curtains", "Adds sharp, geometric volume and shoulder movement"],
                                ["Inverted Pleat", "Two folds turned toward each other, meeting exactly in the center on the right side", "Girls' school uniform skirts, tennis skirts", "Lies completely flat when standing; expands widely when walking or running"],
                                ["Plain Tucks", "Narrow parallel folds of fabric stitched along their entire length", "Yokes of children's rompers, shirts", "Provides gentle structural shaping and body fit"],
                                ["Decorative Pin Tucks", "Very narrow (1–2 mm) stitched folds arranged in parallel clusters", "Formal dress shirts, christening gowns", "Creates exquisite linear texture and visual elegance"]
                            ]
                        }
                    }
                ],
                # Page 4: Gathers vs. Easing: Soft Ripples and Smooth Sleeves
                [
                    {
                        "type": "concept_explanation",
                        "title": "Gathers and Easing: Controlling Soft Fullness",
                        "content": {
                            "title": "Soft Ripples vs. Invisible Control",
                            "text": "• **Gathers**: Multiple tiny, uniform soft folds created by drawing up **two parallel rows of long basting stitches**. Used to draw a wide skirt piece into a narrow waistband or a puffed sleeve into a cuff.\n  • *Why Two Rows?* Sewing two parallel rows (one just above the seamline and one just below) prevents the thread from snapping and keeps all gathers standing upright and evenly spaced!\n\n• **Easing**: Drawing in slightly extra fabric (1–2 cm) along a curved seam **without creating any visible pleats or wrinkles**. Used to set sleeve heads smoothly into armhole joins."
                        }
                    },
                    {
                        "type": "callout",
                        "title": "Master Tailor Tip",
                        "content": {
                            "title": "Always Pull the Bobbin (Lower) Threads Together!",
                            "text": "When gathering, always pull the two **bobbin (lower) threads simultaneously** from both ends towards the center. Bobbin threads slide freely through the fabric, ensuring smooth, even gathers."
                        }
                    }
                ],
                # Page 5: Worked Example — Constructing a Child's Sleeveless Top
                [
                    {
                        "type": "step_process",
                        "title": "Worked Example: Constructing a Child's Sleeveless, Collarless Garment",
                        "content": {
                            "title": "Integrated Garment Construction Workflow",
                            "steps": [
                                {
                                    "step_number": 1,
                                    "title": "Transfer Markings & Sew Waist Darts",
                                    "description": "Mark single-pointed darts on front and back bodice pieces. Stitch from the wide edge to the point and tie thread ends by hand."
                                },
                                {
                                    "step_number": 2,
                                    "title": "Join Shoulder Seams with French Seams",
                                    "description": "Join front and back bodice at the shoulders using delicate, self-finished **French seams**."
                                },
                                {
                                    "step_number": 3,
                                    "title": "Neaten Collarless Neckline",
                                    "description": "Apply a fitted crossway bias strip (facing) to the curved neckline, turn to the inside, and topstitch neatly."
                                },
                                {
                                    "step_number": 4,
                                    "title": "Gather Peplum Skirt to Bodice",
                                    "description": "Sew **two rows of gathering stitches** across the skirt top. Draw threads to match the bodice waistline, distribute ruffles evenly, and stitch securely."
                                },
                                {
                                    "step_number": 5,
                                    "title": "Join Side Seams & Hem",
                                    "description": "Close side seams using continuous French seams from armhole to lower edge. Turn and stitch a clean 1 cm hem; press thoroughly."
                                }
                            ]
                        }
                    }
                ],
                # Page 6: Hands-On Sewing Sampler Activity
                [
                    {
                        "type": "mini_activity",
                        "title": "Hands-On: Stitching a Dart and Gathers Practice Sampler",
                        "content": {
                            "title": "Activity: Create Your Needlework Sampler",
                            "instructions": "Using a 15 cm x 15 cm scrap of cotton fabric:\n\n1. **Stitch a Single-Pointed Dart**: Fold along center, stitch from 2 cm wide intake down to the point, run off fold, and tie a square knot by hand.\n2. **Sew Gathers**: On another scrap, stitch two parallel rows of long basting stitches 6 mm apart. Pull both bobbin threads to create 5 cm of dense, uniform gathers.\n3. **Press**: Press the dart to one side and steam the gathers flat at the seamline.\n\nMount your finished samples in your Home Science needlework portfolio!"
                        }
                    }
                ],
                # Page 7: Key Takeaways & Recall Helper
                [
                    {
                        "type": "key_takeaway",
                        "title": "Key Takeaways: Methods of Controlling Fullness",
                        "content": {
                            "title": "Core Ideas to Remember",
                            "takeaways": [
                                "Controlling fullness transforms flat **2D fabric** to fit curved **3D human bodies**.",
                                "**Darts** shape body curves; always stitch from the wide end to the tip and knot thread ends by hand (no machine backstitching!).",
                                "**Box pleats** (folds facing away on the right side) are the reverse of **inverted pleats** (folds meeting in the center).",
                                "**Gathers** require **two parallel rows** of basting stitches to prevent snapping and produce even, upright ruffles."
                            ]
                        }
                    },
                    {
                        "type": "memory_tip",
                        "title": "The 5 Fullness Control Methods Helper",
                        "content": {
                            "title": "Remember 'D-P-T-G-E'",
                            "tip": "**D**arts (shaping), **P**leats (expansion), **T**ucks (structure/style), **G**athers (soft ruffles), **E**asing (smooth curve joins)!"
                        }
                    }
                ],
                # Page 8: Knowledge Check
                [
                    {
                        "type": "knowledge_check",
                        "title": "Knowledge Check: Methods of Controlling Fullness",
                        "content": {
                            "question": "A student is sewing gathers on a cotton skirt to join it to a waistband. Why must the student sew two parallel rows of loose basting stitches instead of just a single row?",
                            "options": [
                                "Because a single row of thread is illegal in tailoring exams.",
                                "Because two parallel rows distribute the soft ruffles evenly, keep gathers standing upright, and prevent thread breakage when pulling.",
                                "Because the second row of stitching is always unpicked and thrown away before wearing.",
                                "To double the thickness of the fabric so it cannot bend."
                            ],
                            "correct_index": 1,
                            "explanation": "Sewing two parallel rows of gathering stitches supports the fabric ripples uniformly across the seam line and shares the tension, preventing the thread from snapping when drawn up."
                        }
                    }
                ]
            ]
        }
    ]

def ingest_cbc_grade8_home_science_topic3(replace=False):
    """Executes the atomic ingestion of CBC Grade 8 Home Science Topic 3."""
    print("=" * 80)
    print("STARTING INGESTION: CBC GRADE 8 HOME SCIENCE — TOPIC 3: TEXTILE AND CLOTHING")
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

    # 4. Resolve Topic: Textile and Clothing (Order: 3)
    topic_name = "Textile and Clothing"
    topic = Topic.objects.filter(subject=subject, name=topic_name).first()

    if topic and replace:
        print(f"[*] Found existing Topic '{topic_name}' (ID: {topic.id}). Removing for clean replace...")
        topic.delete()
        topic = None

    if not topic:
        topic = Topic.objects.create(
            subject=subject,
            name=topic_name,
            order=3,
            description="Comprehensive CBC Grade 8 module on artificial textile fibres (regenerated vs synthetic), seam classification and construction (French & machine-fell), and methods of controlling fullness (darts, pleats, tucks, gathers, easing)."
        )
        print(f"[+] Created Topic: {topic.name} (ID: {topic.id}, Order: {topic.order})")
    else:
        print(f"[*] Using existing Topic: {topic.name} (ID: {topic.id}, Order: {topic.order})")

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
    print("[SUCCESS] CBC Grade 8 Home Science Topic 3 Ingestion Complete!")
    print(f"[*] Total Lessons Ingested: {total_lessons}")
    print(f"[*] Total Pages Ingested:   {total_pages}")
    print(f"[*] Total Blocks Ingested:  {total_blocks}")
    print("=" * 80)

if __name__ == "__main__":
    replace_flag = "--replace" in sys.argv
    ingest_cbc_grade8_home_science_topic3(replace=replace_flag)
