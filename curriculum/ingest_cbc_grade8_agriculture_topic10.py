"""
VLearn CBC Grade 8 Agriculture — Topic 10: Sewing and Production Techniques
Production Ingestion Engine (Phase 1: Content & Card Architecture - Deep Pedagogical Edition)

Curriculum: CBC (Curriculum ID: 5)
Grade: Grade 8 (ID: 15, Level: 8)
Subject: Agriculture
Topic: Sewing and Production Techniques (Topic Order: 10)

Decomposed into 5 Learning Units & 5 Published Lessons:
  1. Introduction to Sewing Skills and Types of Seams (7 Pages, 12 Blocks)
  2. Practical: Making Samples of Seams — The Plain Seam (7 Pages, 12 Blocks)
  3. Practical: Making Samples of Seams — The Open Seam (7 Pages, 12 Blocks)
  4. Practical Activity: Constructing a Simple Household Item — Making a Pocket Pouch (7 Pages, 13 Blocks)
  5. Sewing Tool Safety and Care of Sewing Equipment & Capstone (10 Pages, 22 Blocks)

Deep Pedagogical Enhancements:
  - Strict 1 Card = 1 Understandable Idea progression.
  - Zero citation leaks ([Topic 4], [2]), zero developer meta-tags, zero raw unrendered LaTeX in student text.
  - Formative scenario MCQs and 10 Topic Summative MCQs with comprehensive educational explanations.
  - Multi-video integrations embedded across individual practical lessons.

Usage:
  ./venv/bin/python curriculum/ingest_cbc_grade8_agriculture_topic10.py [--replace]
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
    """Removes bracket citations, LaTeX leak artifacts, and normalizes unicode bullets into standard markdown list items."""
    if not text:
        return ""
    text = re.sub(r'\[(?:\d+|image_\d+|S\d+.*?|[\d,\s]{2,}|Topic \d+|Week \d+: Lesson \d+)\]', '', text)
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
    """Returns the comprehensive pedagogical page and block structure for Grade 8 Topic 10: Sewing and Production Techniques."""
    return [
        # =====================================================================
        # LESSON 1: Introduction to Sewing Skills and Types of Seams
        # =====================================================================
        {
            "unit_order": 1,
            "unit_name": "Introduction to Sewing Skills and Types of Seams",
            "unit_description": "Foundational textile construction: defining seams (joining, shaping, decorating), raw edge fraying mechanisms, the 1.0 cm to 1.5 cm seam allowance buffer, and contrasting Plain Seams (lightweight cotton) vs. Open Seams (heavy denim/canvas).",
            "lesson_title": "Introduction to Sewing Skills and Types of Seams",
            "pages": [
                # Page 1: Visual Hook & Learning Objectives
                [
                    {
                        "type": "suggested_image",
                        "title": "Textile Anatomy: Garment Seam Construction",
                        "content": {
                            "title": "Textile Anatomy: Garment Seam Construction",
                            "caption": "Inside view of a denim garment showing two fabric panels joined by a neat straight stitch line and the protective raw edge seam allowances."
                        }
                    },
                    {
                        "type": "learning_goal",
                        "title": "Learning Objectives: The Architecture of Seams",
                        "content": {
                            "title": "What We Will Accomplish Today",
                            "goals": [
                                "Define a **seam** and explain its three primary purposes in garment construction.",
                                "Explain why leaving a **1.0 cm to 1.5 cm seam allowance** prevents fabric fraying.",
                                "Compare the structural differences between a **Plain Seam** and an **Open Seam**.",
                                "Select the appropriate seam for lightweight cotton versus heavy denim fabrics."
                            ]
                        }
                    },
                    {
                        "type": "concept_explanation",
                        "title": "The Strength of the Stitched Joint",
                        "content": {
                            "title": "How Flat Fabric Becomes 3D Articles",
                            "text": "Every shirt, pair of trousers, curtain, and pillowcase in your home is held together by seams! A seam is a strong structural bridge joining separate pieces of fabric. Without properly constructed seams with adequate seam allowances, our clothes would split and unravel under the slightest tension or during washing."
                        }
                    }
                ],
                # Page 2: Plain vs. Open Seam Characteristics
                [
                    {
                        "type": "concept_explanation",
                        "title": "Plain Seams vs. Open Seams",
                        "content": {
                            "title": "Two Fundamental Seam Types",
                            "text": "- **1. The Plain Seam**:\n  * *Structure*: Two pieces of fabric are placed with right sides facing each other, and sewn along the seam allowance line. Both raw edges lie together on one side of the stitching.\n  * *Ideal Fabrics*: Lightweight to medium woven cotton, calico, poplin, and linen.\n  * *Best Uses*: Pillowcases, lightweight curtains, simple aprons, pocket pouches.\n- **2. The Open Seam**:\n  * *Structure*: A plain seam whose two seam allowances have been parted and pressed flat against opposite sides of the stitch line.\n  * *Ideal Fabrics*: Heavy fabrics like denim, canvas, corduroy, and wool.\n  * *Best Uses*: Heavy trousers, schoolbags, winter coats, table runners (eliminates bulky ridges)."
                        }
                    },
                    {
                        "type": "suggested_diagram",
                        "title": "Seam Anatomy & Classification: Plain Seam vs. Open Seam Structural Mechanics",
                        "content": {
                            "title": "Seam Anatomy & Classification: Plain Seam vs. Open Seam Structural Mechanics",
                            "caption": "Structural comparison: 1. Plain Seam (Both raw edges lie together on one side, fast, strong for light cotton) • 2. Open Seam (Seam allowances parted and pressed flat in opposite directions, splits bulk for heavy denim/canvas)."
                        }
                    }
                ],
                # Page 3: Plain vs. Open Seam Comparison Matrix
                [
                    {
                        "type": "comparison_table",
                        "title": "Seam Types & Fabric Application Matrix",
                        "content": {
                            "title": "Technical Evaluation of Plain and Open Seams",
                            "headers": ["Seam Type", "Internal Appearance", "Primary Advantage", "Ideal Fabric Weight", "Typical Household Uses"],
                            "rows": [
                                ["Plain Seam", "Two raw edges lie together on one side of stitch line", "Fast to sew, strong joint, needs minimal ironing", "Lightweight cotton, linen, poplin, calico", "Pillowcases, lightweight curtains, aprons, pocket pouches"],
                                ["Open Seam", "Two seam allowances parted and pressed flat in opposite directions", "Splits bulk, makes joint completely flat and smooth against skin", "Heavy denim, canvas, wool, corduroy", "Denim trousers, heavy canvas schoolbags, winter jackets"]
                            ]
                        }
                    }
                ],
                # Page 4: Interactive Seam Matching Challenge
                [
                    {
                        "type": "interactive_scenario",
                        "title": "Seam & Fabric Application Matching Challenge",
                        "content": {
                            "title": "Selecting the Right Seam for the Job",
                            "instructions": "Match the fabric and item to its optimal seam type:",
                            "scenario": "A student tailor is sewing two items: a lightweight cotton pillowcase, and a heavy denim school backpack.",
                            "question": "Which seam construction is best for the heavy denim backpack to prevent bulky ridges?",
                            "options": [
                                "Open Seam (splits the thick seam allowances and presses them flat on opposite sides).",
                                "Plain Seam with 0.1 cm seam allowance",
                                "Glue the fabric together without stitching",
                                "Leave raw cut edges completely exposed without pressing"
                            ],
                            "correct_feedback": "Correct! Thick fabrics like denim create heavy ridges if both edges lie together. An Open Seam parts and presses the allowances flat, eliminating bulk.",
                            "incorrect_feedback": "Incorrect. Heavy fabrics require an Open Seam to part the seam allowances and press them flat, reducing joint bulkiness."
                        }
                    }
                ],
                # Page 5: Formative Knowledge Check
                [
                    {
                        "type": "knowledge_check",
                        "title": "Knowledge Check: Seam Allowance Function",
                        "content": {
                            "question": "What is the primary technical purpose of leaving a 'seam allowance' of 1.0 cm to 1.5 cm when sewing fabric pieces together?",
                            "options": [
                                "It provides a safety buffer that prevents stitches from tearing through the raw woven edges when the garment is pulled or washed.",
                                "It gives space to attach heavy metal buttons.",
                                "It keeps the sewing needle cool during high-speed stitching.",
                                "It reduces the amount of thread used by half."
                            ],
                            "answer": "A",
                            "explanation": "Cut edges of woven fabrics fray easily. If stitches are placed directly on the cut edge, threads slip out and the seam splits. A 1.0–1.5 cm seam allowance provides a strong structural buffer."
                        }
                    }
                ],
                # Page 6: Summary & Connection Forward
                [
                    {
                        "type": "key_takeaway",
                        "title": "Lesson Summary",
                        "content": {
                            "text": "- A **seam** joins, shapes, and decorates fabric pieces in clothing and household items.\n- The **1.0 cm to 1.5 cm seam allowance** is essential to stop stitches from tearing out of fraying raw edges.\n- **Plain seams** keep raw edges together (best for light cottons).\n- **Open seams** press allowances flat on opposite sides (best for heavy fabrics to split bulk)."
                        }
                    },
                    {
                        "type": "transition",
                        "title": "Looking Ahead",
                        "content": {
                            "text": "How do we prepare and hand-sew a perfect plain seam sample? In Lesson 2, we learn about sharp-tool safety, pinning, basting, and stitching!"
                        }
                    }
                ],
                # Page 7: Economic Value of Sewing
                [
                    {
                        "type": "concept_explanation",
                        "title": "Financial Self-Reliance in the Home",
                        "content": {
                            "title": "Why Hand Sewing is an Essential Life Skill",
                            "text": "Knowing how to sew saves household money! Instead of discarding a school uniform with a split seam or paying a tailor for minor alterations, you can fix and create items like aprons and shopping bags from local scrap fabric."
                        }
                    }
                ]
            ]
        },

        # =====================================================================
        # LESSON 2: Practical: Making Samples of Seams — The Plain Seam
        # =====================================================================
        {
            "unit_order": 2,
            "unit_name": "Practical: Making Samples of Seams — The Plain Seam",
            "unit_description": "Hand-sewing laboratory: sharp tool safety (thimbles, pincushions, passing shears), step-by-step plain seam construction (right sides together, marking 1.2 cm line, right-angle pinning, basting tacking, permanent backstitch, fastening off double knot).",
            "lesson_title": "Practical: Making Samples of Seams — The Plain Seam",
            "pages": [
                # Page 1: Visual Hook & Learning Objectives
                [
                    {
                        "type": "suggested_image",
                        "title": "Hand Stitching Craft: Safe Needle & Thimble Technique",
                        "content": {
                            "title": "Hand Stitching Craft: Safe Needle & Thimble Technique",
                            "caption": "A close-up of hands sewing cotton cloth with a needle and thread, with a protective metal thimble worn on the middle finger to prevent needle pricks."
                        }
                    },
                    {
                        "type": "learning_goal",
                        "title": "Learning Objectives: Plain Seam Craftsmanship",
                        "content": {
                            "title": "What We Will Accomplish Today",
                            "goals": [
                                "Demonstrate strict sharp-tool safety using **thimbles and pincushions**.",
                                "Describe the chronological steps to construct a **hand-sewn plain seam**.",
                                "Execute accurate **right-angle pinning and temporary basting (tacking)**.",
                                "Sew a clean plain seam sample on cotton cloth using strong **permanent backstitches**."
                            ]
                        }
                    },
                    {
                        "type": "concept_explanation",
                        "title": "The Secret of Accurate Stitching: Basting",
                        "content": {
                            "title": "Why We Baste Before Permanent Stitching",
                            "text": "If you try to hold two loose pieces of fabric with your fingers while making tiny permanent stitches, the fabric will slip and slide, creating a crooked seam! Basting (temporary, loose running stitches) locks the layers in place so your final stitches are straight and strong."
                        }
                    }
                ],
                # Page 2: Step-by-Step Plain Seam Construction Workflow
                [
                    {
                        "type": "concept_explanation",
                        "title": "Standard Operating Procedure: Plain Seam Sample",
                        "content": {
                            "title": "Five Steps to a Perfect Plain Seam",
                            "text": "- **Step 1: Right Sides Together**: Place two cotton specimens (10 cm × 15 cm) with printed right sides facing each other, cut edges aligned.\n- **Step 2: Mark & Pin**: Draw a straight line exactly **1.2 cm** from the edge using tailor's chalk and a ruler. Insert straight pins at **right angles** to the edge.\n- **Step 3: Basting (Tacking)**: Sew long, temporary running stitches along the line. Remove pins.\n- **Step 4: Permanent Stitching**: Sew tight, small **backstitches** along the basted line. Fasten off with a secure double knot.\n- **Step 5: Finish**: Gently pull out the temporary basting thread and inspect the seam."
                        }
                    },
                    {
                        "type": "suggested_diagram",
                        "title": "Step-by-Step Plain Seam Construction Workflow",
                        "content": {
                            "title": "Step-by-Step Plain Seam Construction Workflow",
                            "caption": "Hand-sewing operational sequence: 1. Right sides facing together -> 2. Draw 1.2 cm chalk line -> 3. Insert pins at right angles -> 4. Sew temporary basting thread -> 5. Permanent tight backstitch & double knot."
                        }
                    }
                ],
                # Page 3: Hand Sewing Tools & Safety Standards
                [
                    {
                        "type": "comparison_table",
                        "title": "Hand Sewing Tools & Safety Protocol Matrix",
                        "content": {
                            "title": "Studio Equipment & Safety Management",
                            "headers": ["Sewing Tool", "Primary Tailoring Function", "Major Safety Hazard", "Mandatory Safety Protocol"],
                            "rows": [
                                ["Hand Needle", "Pushes thread through fabric layers to form stitches", "Puncture wounds, swallowing if held in mouth", "Never put in mouth; store in pincushion when not in hand"],
                                ["Thimble", "Protective metal/plastic cap for middle pushing finger", "Finger pricks from eye-end of needle", "Always wear on middle finger when pushing needles through cloth"],
                                ["Fabric Shears", "Cuts clean, unfrayed fabric edges", "Deep cuts, stabbing if passed blade-first", "Pass handle-first with blades closed; never cut paper/cardboard"],
                                ["Tailor's Chalk", "Draws removable chalk guideline for seam allowances", "Breaking chalk into powder", "Store flat in box; sharpen edge for fine, crisp lines"]
                            ]
                        }
                    }
                ],
                # Page 4: Video Resource — Hand Sewing a Plain Seam
                [
                    {
                        "type": "suggested_video",
                        "title": "Instructional Video: How to Hand Sew a Plain Seam & Master Basting",
                        "content": {
                            "title": "Instructional Video: How to Hand Sew a Plain Seam & Master Basting",
                            "url": "https://www.youtube.com/watch?v=TXJPk-QfhDU",
                            "resolved_video_id": "TXJPk-QfhDU",
                            "caption": "Watch this practical hand-sewing demonstration showing fabric alignment, right-angle pinning, basting technique, backstitching, and neat thread knotting."
                        }
                    },
                    {
                        "type": "concept_explanation",
                        "title": "Key Workshop Takeaways from the Video",
                        "content": {
                            "title": "Practical Sewing Insights",
                            "text": "- **1. Right-Angle Pinning**: Notice how pins placed perpendicular (at 90 degrees) to the edge keep fabric flat without buckling.\n- **2. Thread Length**: Observe why sewing thread should be no longer than your arm's length (about 50 cm) to prevent tangles.\n- **3. Tension Control**: Watch how pulling thread too tightly puckers the cloth, while pulling too loosely leaves weak loops."
                        }
                    }
                ],
                # Page 5: Interactive Plain Seam Ordering Challenge
                [
                    {
                        "type": "interactive_scenario",
                        "title": "Plain Seam Chronological Sequencing Challenge",
                        "content": {
                            "title": "Ordering Practical Hand-Sewing Steps",
                            "instructions": "Place the plain seam steps in the correct chronological order:",
                            "scenario": "A student is preparing to sew a plain seam sample in the home science studio.",
                            "question": "What is the correct logical workflow from start to finish?",
                            "options": [
                                "1. Right sides together -> 2. Draw 1.2 cm chalk line -> 3. Pin at right angles -> 4. Baste with long stitches -> 5. Sew permanent backstitches & knot",
                                "1. Sew permanent stitches -> 2. Cut fabric after sewing -> 3. Draw chalk lines",
                                "1. Put needles in mouth -> 2. Cut paper with fabric shears -> 3. Sew without pinning",
                                "1. Pull out stitches -> 2. Throw fabric on floor"
                            ],
                            "correct_feedback": "Correct! Align right sides, measure/mark 1.2 cm, pin at right angles, baste temporarily, and sew permanent backstitches.",
                            "incorrect_feedback": "Incorrect. Follow the chronological sequence: Align -> Mark -> Pin -> Baste -> Sew permanent stitches."
                        }
                    }
                ],
                # Page 6: Formative Knowledge Check
                [
                    {
                        "type": "knowledge_check",
                        "title": "Knowledge Check: The Function of Basting",
                        "content": {
                            "question": "Why is 'basting' (tacking) considered a mandatory step before sewing permanent stitches on a plain seam?",
                            "options": [
                                "Basting temporarily locks the fabric layers in place, preventing them from slipping or wrinkling while you sew permanent stitches.",
                                "Basting permanently glues the raw edges together.",
                                "Basting makes the thread waterproof.",
                                "Basting replaces the need for cutting fabric."
                            ],
                            "answer": "A",
                            "explanation": "Hand-sewing requires stability. Temporary basting stitches hold fabric layers securely together, ensuring the final stitch line is straight and even."
                        }
                    }
                ],
                # Page 7: Summary & Connection Forward
                [
                    {
                        "type": "key_takeaway",
                        "title": "Lesson Summary",
                        "content": {
                            "text": "- Always wear a **thimble** on your middle finger and store needles in **pincushions**.\n- Construct plain seams with **right sides facing together** and a **1.2 cm seam allowance**.\n- **Pin at right angles** and **baste** to prevent fabric slippage.\n- Sew permanent **backstitches** for strength and fasten off with a double knot."
                        }
                    },
                    {
                        "type": "transition",
                        "title": "Looking Ahead",
                        "content": {
                            "text": "How do we transform a plain seam into a completely flat, non-bulky open seam? In Lesson 3, we master finger-parting, damp pressing, and iron safety!"
                        }
                    }
                ]
            ]
        },

        # =====================================================================
        # LESSON 3: Practical: Making Samples of Seams — The Open Seam
        # =====================================================================
        {
            "unit_order": 3,
            "unit_name": "Practical: Making Samples of Seams — The Open Seam",
            "unit_description": "Constructing open seams: stitching a 1.5 cm plain seam, removing basting, finger-parting seam allowances, damp press cloth application, flat iron pressing technique, edge-finishing with pinking shears or hand overcasting, and iron safety.",
            "lesson_title": "Practical: Making Samples of Seams — The Open Seam",
            "pages": [
                # Page 1: Visual Hook & Learning Objectives
                [
                    {
                        "type": "suggested_image",
                        "title": "Tailoring Precision: Open Seam with Pinked Edges",
                        "content": {
                            "title": "Tailoring Precision: Open Seam with Pinked Edges",
                            "caption": "Inside of a garment showing two seam allowances parted and pressed flat against opposite sides of a central stitch line, with neat pinked zigzag edges."
                        }
                    },
                    {
                        "type": "learning_goal",
                        "title": "Learning Objectives: Open Seam Pressing & Finishing",
                        "content": {
                            "title": "What We Will Accomplish Today",
                            "goals": [
                                "Explain why open seams are essential for **heavy, bulky fabrics**.",
                                "Demonstrate how to **finger-part and press seam allowances flat**.",
                                "Apply **iron safety rules** (standing on heel, heat-resistant surfaces, never leaving unattended).",
                                "Finish raw edges using **pinking shears or hand overcasting stitches**."
                            ]
                        }
                    },
                    {
                        "type": "concept_explanation",
                        "title": "Splitting the Bulk for Smooth Comfort",
                        "content": {
                            "title": "Why Garment Inners Must Lie Flat",
                            "text": "If you sew a pair of heavy jeans or a canvas bag using a plain seam, both thick raw edges bundle together into a hard, rigid ridge that chafes against your skin. By parting the seam allowances and pressing them flat in opposite directions, an **open seam** eliminates bulk completely!"
                        }
                    }
                ],
                # Page 2: Step-by-Step Open Seam Construction Workflow
                [
                    {
                        "type": "concept_explanation",
                        "title": "Standard Operating Procedure: Open Seam Sample",
                        "content": {
                            "title": "Five Steps to an Open Pressed Seam",
                            "text": "- **Step 1: Sew Plain Seam Base**: Stitch two specimens right-sides together with a **1.5 cm seam allowance**. Fasten off with a double knot.\n- **Step 2: Remove Basting**: Gently pull out the temporary basting thread.\n- **Step 3: Finger-Part Allowances**: Lay fabric wrong-side up on the pressing board. Use your fingers to open and part the two seam allowances.\n- **Step 4: Press Flat with Iron**: Place a damp pressing cloth over the parted allowances. Press a warm iron flat down for 3-5 seconds along the seam line (do not slide roughly).\n- **Step 5: Finish Edges**: Trim raw edges with pinking shears (zigzag) or sew light hand overcasting to stop fraying."
                        }
                    },
                    {
                        "type": "suggested_diagram",
                        "title": "Open Seam Splitting & Iron Pressing Protocol",
                        "content": {
                            "title": "Open Seam Splitting & Iron Pressing Protocol",
                            "caption": "Open seam workflow: 1. Stitch plain seam base (1.5 cm allowance) -> 2. Finger-part allowances on pressing board -> 3. Damp pressing cloth protection -> 4. Flat iron pressing (stand iron on heel) -> 5. Pinked zigzag edge finishing."
                        }
                    }
                ],
                # Page 3: Iron Safety & Edge Finishing Comparison
                [
                    {
                        "type": "comparison_table",
                        "title": "Edge Finishing Techniques & Iron Safety Standards",
                        "content": {
                            "title": "Finishing Open Seams and Safety Rules",
                            "headers": ["Technique / Safety Rule", "Operational Procedure", "Primary Function / Rationale", "Best Applied On"],
                            "rows": [
                                ["Pinking (Pinking Shears)", "Cut raw edges with specialized zigzag saw-tooth shears", "Zigzag cuts break thread alignment, stopping long fraying threads", "Crisp woven cotton, linen, wool"],
                                ["Hand Overcasting", "Sew loose, diagonal loop stitches around the raw cut edge", "Encloses raw thread ends to prevent unraveling during washing", "Loosely woven fabrics that fray heavily"],
                                ["Damp Press Cloth", "Place clean, damp cotton cloth between iron and garment", "Prevents hot iron from scorching or creating shiny burn marks", "Delicate cottons, dark fabrics, wool"],
                                ["Iron Heel Stand", "Always stand iron upright on its base heel when pausing", "Prevents hot metal plate from scorching ironing board or causing fires", "All pressing sessions"]
                            ]
                        }
                    }
                ],
                # Page 4: Interactive Seam Comparison Challenge
                [
                    {
                        "type": "interactive_scenario",
                        "title": "Plain vs. Open Seam Structural Matching Challenge",
                        "content": {
                            "title": "Comparing Seam Structures",
                            "instructions": "Match the seam characteristic to the correct seam type:",
                            "scenario": "A student is inspecting the inside of two garments: a lightweight cotton apron and a heavy denim jacket.",
                            "question": "Which seam structure is found on the inside of the heavy denim jacket?",
                            "options": [
                                "Open Seam: the two seam allowances are split and pressed flat on opposite sides to eliminate bulk.",
                                "Plain Seam: both raw edges stick up together as a thick ridge.",
                                "No seams at all: fabric is held by tape.",
                                "Raw unstitched cut fabric."
                            ],
                            "correct_feedback": "Correct! Denim jackets use open seams so the thick seam allowances are split and pressed flat, preventing bulky, uncomfortable ridges.",
                            "incorrect_feedback": "Incorrect. Heavy denim garments require Open Seams to split the seam allowances and press them flat."
                        }
                    }
                ],
                # Page 5: Formative Knowledge Check
                [
                    {
                        "type": "knowledge_check",
                        "title": "Knowledge Check: Safe Iron Handling in Sewing Studios",
                        "content": {
                            "question": "What is the correct, safe procedure for handling a household iron when pressing open seams during a practical session?",
                            "options": [
                                "Always stand the iron upright on its heel when not in hand, use a damp press cloth, and unplug it immediately when finished.",
                                "Slide the iron back and forth as fast as possible across the table.",
                                "Test the iron's heat by touching the hot metal plate with wet bare fingers.",
                                "Leave the hot iron face-down on a pile of dry newspapers."
                            ],
                            "answer": "A",
                            "explanation": "Hot irons are fire and burn hazards. Always stand the iron on its heel, use pressing cloths, and disconnect power the moment you are finished."
                        }
                    }
                ],
                # Page 6: Summary & Connection Forward
                [
                    {
                        "type": "key_takeaway",
                        "title": "Lesson Summary",
                        "content": {
                            "text": "- **Open seams** split the seam allowances and press them flat on opposite sides.\n- Pressing flat **eliminates bulky ridges** on heavy fabrics like denim and canvas.\n- Always use a **damp pressing cloth** and **stand the iron on its heel**.\n- Finish split raw edges with **pinking shears** or **hand overcasting** to prevent fraying."
                        }
                    },
                    {
                        "type": "transition",
                        "title": "Looking Ahead",
                        "content": {
                            "text": "Let's put our seaming skills to practical use! In Lesson 4, we measure, cut, double-hem, and hand-sew a functional VLearn Pocket Pouch!"
                        }
                    }
                ],
                # Page 7: Pressing Technique Pro-Tip
                [
                    {
                        "type": "concept_explanation",
                        "title": "Pressing vs. Ironing: A Critical Distinction",
                        "content": {
                            "title": "Why We Press Down Rather Than Slide",
                            "text": "In clothing construction, 'ironing' means sliding the iron back and forth, which stretches damp bias seams out of shape. 'Pressing' means lifting the iron and placing it firmly down onto the seam for 3-5 seconds without sliding. This flattens the seam allowances crisp and flat without distorting the garment."
                        }
                    }
                ]
            ]
        },

        # =====================================================================
        # LESSON 4: Practical Activity: Constructing a Simple Household Item — Making a Pocket Pouch
        # =====================================================================
        {
            "unit_order": 4,
            "unit_name": "Practical Activity: Constructing a Simple Household Item — Making a Pocket Pouch",
            "unit_description": "Project-based production lab: pattern layout (15 cm × 30 cm), smooth fabric cutting, double-fold hemming of raw ends, pocket folding (10 cm body + 5 cm flap), pinning and basting side seams, permanent backstitching, turning right-side out, and button fastener attachment.",
            "lesson_title": "Practical Activity: Constructing a Simple Household Item — Making a Pocket Pouch",
            "pages": [
                # Page 1: Visual Hook & Project Objectives
                [
                    {
                        "type": "suggested_image",
                        "title": "Functional Craft: Hand-Sewn Cotton Pocket Pouch",
                        "content": {
                            "title": "Functional Craft: Hand-Sewn Cotton Pocket Pouch",
                            "caption": "A finished rectangular pocket pouch made from colorful African print cotton fabric, featuring neat side seams, a folded top flap, and a wooden button fastener."
                        }
                    },
                    {
                        "type": "learning_goal",
                        "title": "Learning Objectives: Household Item Construction",
                        "content": {
                            "title": "What We Will Accomplish Today",
                            "goals": [
                                "Measure and cut a **15 cm × 30 cm fabric rectangle** accurately using tailor's chalk.",
                                "Construct a **double-fold hem (0.5 cm × 0.5 cm)** on short raw ends.",
                                "Fold and sew **strong plain side seams** using the interlocking backstitch.",
                                "Turn the pouch inside out, press corners neatly, and attach a **button fastener**."
                            ]
                        }
                    },
                    {
                        "type": "concept_explanation",
                        "title": "From Scrap Cloth to Useful Article",
                        "content": {
                            "title": "The Joy of Practical Creation",
                            "text": "Today, you become a textile creator! Using a single piece of cotton fabric, your needle, thread, and scissors, you will construct a durable pocket pouch to hold your pens, sewing tools, or pocket money."
                        }
                    }
                ],
                # Page 2: Step-by-Step Pocket Pouch Construction Blueprint
                [
                    {
                        "type": "concept_explanation",
                        "title": "Step-by-Step Pocket Pouch Construction SOP",
                        "content": {
                            "title": "Five Steps to Build Your Pocket Pouch",
                            "text": "- **Step 1: Measure & Cut**: Trace a **15 cm wide × 30 cm long** rectangle on the wrong side with chalk. Cut smoothly with fabric shears.\n- **Step 2: Double-Hem Short Ends**: Fold raw short ends by 0.5 cm, then 0.5 cm again. Stitch down to completely seal the raw edges.\n- **Step 3: Fold Pouch Body**: With right sides together, fold the bottom up by **10 cm**, leaving a **5 cm flap** exposed at the top.\n- **Step 4: Pin, Baste & Backstitch**: Pin side edges at right angles. Baste 1.0 cm from edges. Sew permanent, tight **backstitches** on both sides. Knot securely.\n- **Step 5: Turn, Press & Fasten**: Turn pouch inside out, gently push out corners with a blunt pencil, press flat with a warm iron, and sew a button or snap onto the flap."
                        }
                    },
                    {
                        "type": "suggested_diagram",
                        "title": "Pocket Pouch Construction Blueprint: 15cm x 30cm Pattern, Double-Hem & Backstitched Sides",
                        "content": {
                            "title": "Pocket Pouch Construction Blueprint: 15cm x 30cm Pattern, Double-Hem & Backstitched Sides",
                            "caption": "Project blueprint: 1. 15cm x 30cm cotton pattern -> 2. Double-fold hem on short ends -> 3. 10cm pocket body fold (right sides facing) -> 4. Backstitched side plain seams (1.0 cm allowance) -> 5. Turned pouch with top flap & button."
                        }
                    }
                ],
                # Page 3: Hand Stitches Comparison for Project Work
                [
                    {
                        "type": "comparison_table",
                        "title": "Hand Stitches Applied in Pouch Construction",
                        "content": {
                            "title": "Stitch Selection & Functional Roles",
                            "headers": ["Stitch Name", "Stitch Appearance", "Strength Level", "Role in Pouch Construction"],
                            "rows": [
                                ["Running Stitch", "Even, dashed straight line with equal spaces", "Moderate", "Used for hemming the short edges and preliminary basting"],
                                ["Backstitch", "Continuous unbroken line of stitches overlapping backwards", "Maximum (Mimics machine stitch)", "Used for side seams to withstand pressure from stored items"],
                                ["Overcasting Stitch", "Diagonal looped stitches wrapping over raw edges", "Moderate", "Used to finish raw seam allowances inside the pouch"],
                                ["Fastening-Off Double Knot", "Two tight overlapping knots at the end of stitch line", "High Security", "Locks threads permanently so seams never unravel"]
                            ]
                        }
                    }
                ],
                # Page 4: Video Resource — How to Sew a Pocket Pouch Project
                [
                    {
                        "type": "suggested_video",
                        "title": "Instructional Video: How to Sew a Pocket Pouch / Simple Household Project",
                        "content": {
                            "title": "Instructional Video: How to Sew a Pocket Pouch / Simple Household Project",
                            "url": "https://www.youtube.com/watch?v=6ZjkLwQt_YE",
                            "resolved_video_id": "6ZjkLwQt_YE",
                            "caption": "Watch this step-by-step practical craft video showing fabric measurement, double-hemming, pocket folding, backstitching sides, and attaching a wooden button."
                        }
                    },
                    {
                        "type": "concept_explanation",
                        "title": "Key Project Insights from the Video",
                        "content": {
                            "title": "Craftsmanship Tips",
                            "text": "- **1. Double Hemming**: Notice how folding raw edges twice (0.5 cm + 0.5 cm) locks all loose threads inside the fold.\n- **2. Corner Poking**: Observe how using a blunt pencil pushes the corner points out sharply without piercing through the fabric.\n- **3. Button Shank**: Watch how creating a small thread shank under the button allows the flap to close smoothly without pulling."
                        }
                    }
                ],
                # Page 5: Interactive Pouch Construction Ordering Challenge
                [
                    {
                        "type": "interactive_scenario",
                        "title": "Pocket Pouch Assembly Sequencing Challenge",
                        "content": {
                            "title": "Ordering Project Construction Steps",
                            "instructions": "Place the pouch construction steps in the correct chronological sequence:",
                            "scenario": "Your home science group is constructing cotton pocket pouches.",
                            "question": "What is the correct chronological sequence of operations?",
                            "options": [
                                "1. Trace 15x30 cm rectangle & cut -> 2. Double-hem short raw ends -> 3. Fold bottom up 10 cm right-sides together -> 4. Baste & backstitch side seams -> 5. Turn inside out & press flat",
                                "1. Turn inside out -> 2. Sew side seams -> 3. Cut fabric after sewing",
                                "1. Sew button on loose thread -> 2. Leave raw edges unhemmed",
                                "1. Cut fabric with teeth -> 2. Glue with cooking oil"
                            ],
                            "correct_feedback": "Correct! Always cut accurately, double-hem raw short ends, fold right-sides together, backstitch side seams, turn inside out, and press flat.",
                            "incorrect_feedback": "Incorrect. Follow the chronological order: Cut -> Double-hem short ends -> Fold -> Backstitch sides -> Turn & Press."
                        }
                    }
                ],
                # Page 6: Formative Knowledge Check
                [
                    {
                        "type": "knowledge_check",
                        "title": "Knowledge Check: Backstitch Superiority for Side Seams",
                        "content": {
                            "question": "Why is the 'backstitch' strictly preferred over the 'running stitch' when hand-sewing the side seams of a pocket pouch?",
                            "options": [
                                "The backstitch forms an interlocking, continuous line that mimics machine stitching, preventing the side seams from splitting under tension.",
                                "The backstitch uses half as much thread.",
                                "The backstitch dissolves in water.",
                                "The backstitch is invisible from both sides."
                            ],
                            "answer": "A",
                            "explanation": "Pouches hold heavy objects like pens and coins that exert pressure on side joints. The backstitch locks backwards with each stitch, creating an extremely strong, durable seam."
                        }
                    }
                ],
                # Page 7: Summary & Connection Forward
                [
                    {
                        "type": "key_takeaway",
                        "title": "Lesson Summary",
                        "content": {
                            "text": "- **Pouch pattern**: Measure and cut a clean **15 cm × 30 cm cotton rectangle**.\n- Always **double-hem short raw ends** (0.5 cm + 0.5 cm) before folding the pouch body.\n- Fold **10 cm up** right-sides together, leaving a **5 cm top flap**.\n- Sew side seams with **interlocking backstitches** and press flat with a warm iron."
                        }
                    },
                    {
                        "type": "transition",
                        "title": "Looking Ahead",
                        "content": {
                            "text": "How do we care for our sewing studio equipment and maintain manual sewing machines? In Lesson 5, we master studio safety, lint removal, and gear lubrication!"
                        }
                    }
                ]
            ]
        },

        # =====================================================================
        # LESSON 5: Sewing Tool Safety and Care of Sewing Equipment & Capstone
        # =====================================================================
        {
            "unit_order": 5,
            "unit_name": "Sewing Tool Safety and Care of Sewing Equipment",
            "unit_description": "Studio maintenance & safety protocols: Four Safe Sewing Habits (accountability, passing shears handle-first, mouth hazard prevention, safe metal disposal), fabric shears preservation (never cut paper), manual sewing machine maintenance (lint removal with soft brush, specialized mineral oil lubrication, test scrap stitching), topic video review, and 10 topic summative MCQs.",
            "lesson_title": "Sewing Tool Safety and Care of Sewing Equipment & Capstone",
            "pages": [
                # Page 1: Visual Hook & Capstone Objectives
                [
                    {
                        "type": "suggested_image",
                        "title": "Studio Safety: Dedicated Tool Organization & Pincushion",
                        "content": {
                            "title": "Studio Safety: Dedicated Tool Organization & Pincushion",
                            "caption": "A classic tomato-shaped red fabric pincushion filled with straight steel pins, sitting alongside a tape measure and closed fabric shears."
                        }
                    },
                    {
                        "type": "learning_goal",
                        "title": "Learning Objectives: Studio Safety & Topic Mastery",
                        "content": {
                            "title": "What We Will Accomplish Today",
                            "goals": [
                                "Practice the **Four Safe Sewing Habits** in the textile studio.",
                                "Explain why fabric shears must **never be used to cut paper or cardboard**.",
                                "Execute routine **lint brushing and mineral oil lubrication** on a manual sewing machine.",
                                "Review the Topic Video and achieve 100% mastery on the **10 Topic Summative Assessment Questions**."
                            ]
                        }
                    },
                    {
                        "type": "concept_explanation",
                        "title": "The Discipline of the Sewing Studio",
                        "content": {
                            "title": "Protecting Hands and Preserving Machines",
                            "text": "A great textile artisan respects their tools! Dropping a needle on the floor can injure a barefoot classmate, and using cooking oil on a sewing machine will ruin its gears forever. Mastering tool care and studio safety ensures our equipment lasts for generations."
                        }
                    }
                ],
                # Page 2: Studio Safety & Sewing Machine Care Architecture
                [
                    {
                        "type": "concept_explanation",
                        "title": "The Four Safe Habits & Sewing Machine Maintenance",
                        "content": {
                            "title": "Safety Protocols and Machine Servicing",
                            "text": "- **The Four Safe Sewing Habits**:\n  * 1. *Pin Accountability*: Count pins before and after; always store in a **pincushion** (never in clothes or mouth).\n  * 2. *Passing Shears*: Close blades firmly, hold blades in your hand, and pass **handle-first**.\n  * 3. *The Mouth Rule*: Never hold needles, pins, or buttons between your lips (swallowing/choking hazard).\n  * 4. *Safe Disposal*: Place bent pins or broken needles in a dedicated metal disposal tin.\n- **Sewing Machine Care**:\n  * 1. *Sweep Lint*: Use a small lint brush to sweep dust out of bobbin cases (lint absorbs oil and dries gears).\n  * 2. *Mineral Oil Only*: Apply 1-2 drops of clear, specialized **sewing machine oil** (never vegetable cooking oil which turns gummy).\n  * 3. *Absorb Excess*: Stitch on scrap cotton to absorb excess oil before sewing garments."
                        }
                    },
                    {
                        "type": "suggested_diagram",
                        "title": "Sewing Studio Safety Protocol & Manual Sewing Machine Maintenance Cycle",
                        "content": {
                            "title": "Sewing Studio Safety Protocol & Manual Sewing Machine Maintenance Cycle",
                            "caption": "Studio safety & machine maintenance: 1. Pincushion accountability -> 2. Pass shears handle-first -> 3. Power off & sweep lint from bobbin case -> 4. Apply 1 drop mineral sewing machine oil -> 5. Test stitch on scrap fabric."
                        }
                    }
                ],
                # Page 3: Sewing Machine Maintenance Matrix
                [
                    {
                        "type": "comparison_table",
                        "title": "Sewing Machine Maintenance Operations Matrix",
                        "content": {
                            "title": "Servicing Procedures & Common Errors",
                            "headers": ["Maintenance Step", "Correct Procedure", "Common Dangerous Error", "Consequence of Error"],
                            "rows": [
                                ["Dust & Lint Removal", "Use a soft lint brush to sweep lint from bobbin area", "Blowing breath into bobbin case", "Moisture from breath causes steel gears to rust"],
                                ["Lubrication (Oiling)", "Apply 1 drop of clear mineral sewing machine oil to oiling holes", "Using vegetable or cooking oil", "Vegetable oil oxidizes into sticky gum that permanently jams gears"],
                                ["Needle Inspection", "Replace bent or blunt needles immediately", "Continuing to sew with a bent needle", "Breaks needle, scratches needle plate, skips stitches"],
                                ["Post-Oiling Run", "Sew rows of blank stitches on scrap cotton cloth", "Sewing expensive final garment immediately", "Stray oil droplets stain and ruin the garment fabric"]
                            ]
                        }
                    }
                ],
                # Page 4: Interactive Studio Habits Challenge
                [
                    {
                        "type": "interactive_scenario",
                        "title": "Studio Safety Habits Classification",
                        "content": {
                            "title": "Sorting Studio Practices into Safe vs. Dangerous",
                            "instructions": "Classify the following studio practices:",
                            "scenario": "A student is observing classmates working during a practical sewing session.",
                            "question": "Which of these practices is strictly safe and professional?",
                            "options": [
                                "Counting pins before and after sewing, storing them in a pincushion, and passing shears handle-first with closed blades.",
                                "Holding three steel pins between your lips while folding a hem.",
                                "Cutting cardboard boxes and wire with specialized fabric shears.",
                                "Leaving loose needles on chair cushions while searching for scissors."
                            ],
                            "correct_feedback": "Correct! Storing pins in pincushions, keeping needles out of mouths, and passing shears handle-first ensures 100% studio safety.",
                            "incorrect_feedback": "Incorrect. Never hold pins in your mouth, never leave needles on chairs, and never cut cardboard with fabric shears!"
                        }
                    }
                ],
                # Page 5: Formative Knowledge Check & Master Summary
                [
                    {
                        "type": "knowledge_check",
                        "title": "Knowledge Check: Cooking Oil Danger on Machines",
                        "content": {
                            "question": "Why is it strictly forbidden to use vegetable cooking oil to lubricate a manual sewing machine?",
                            "options": [
                                "Vegetable oil oxidizes over time, turning into a sticky, gummy paste that traps dust and permanently jams the moving metal gears.",
                                "Vegetable oil makes the machine sew 10 times too fast.",
                                "Vegetable oil chemically dissolves the steel needle instantly.",
                                "Vegetable oil makes the thread turn into plastic."
                            ],
                            "answer": "A",
                            "explanation": "Cooking oils are organic and dry into a sticky gum when exposed to air. This gummy residue cements the gears, destroying the machine. Always use clear, refined mineral sewing machine oil."
                        }
                    },
                    {
                        "type": "key_takeaway",
                        "title": "Topic 10 Master Summary: Sewing and Production Techniques",
                        "content": {
                            "text": "- **Seam Types**: **Plain seams** (two edges together for light cottons) vs. **Open seams** (allowances parted and pressed flat to split bulk on heavy fabrics).\n- **Seam Allowance**: Always leave **1.0 cm to 1.5 cm** to prevent fraying and stitch failure.\n- **Studio Safety**: Use **thimbles**, store pins in **pincushions**, pass shears **handle-first**, and never put pins in your mouth.\n- **Pouch Project**: 15x30 cm cotton pattern, double-hemmed short ends, 10 cm fold, **interlocking backstitched side seams**.\n- **Machine Care**: Sweep lint with brushes, lubricate with **mineral sewing machine oil only**, and test-stitch on scrap cloth."
                        }
                    }
                ],
                # Page 6: Topic Video Review
                [
                    {
                        "type": "suggested_video",
                        "title": "Topic Video Review: Hand Sewing Craftsmanship, Seam Science & Studio Safety",
                        "content": {
                            "title": "Topic Video Review: Hand Sewing Craftsmanship, Seam Science & Studio Safety",
                            "url": "https://www.youtube.com/watch?v=Ei5z_0Lxmic",
                            "resolved_video_id": "Ei5z_0Lxmic",
                            "caption": "Watch this comprehensive educational review covering seam classification, plain and open seam construction, pocket pouch assembly, and sewing studio safety protocols."
                        }
                    },
                    {
                        "type": "concept_explanation",
                        "title": "Key Review Highlights for Video Analysis",
                        "content": {
                            "title": "Final Review Highlights",
                            "text": "- **1. Seam Selection**: Notice how fabric thickness dictates whether you should sew a plain or open seam.\n- **2. Hand Stitch Durability**: Observe how the backstitch creates an interlocking joint as strong as a machine stitch.\n- **3. Tool Discipline**: See how proper tool care preserves scissors and sewing machines for decades."
                        }
                    }
                ],
                # Page 7: Topic Assessment Part 1 (Questions 1 to 2)
                [
                    {
                        "type": "knowledge_check",
                        "title": "Topic Assessment - Question 1: Mouth Hazard with Needles",
                        "content": {
                            "question": "Why must a sewing needle or straight pin never be held between the lips or teeth while organizing fabric?",
                            "options": [
                                "You could easily swallow or inhale the sharp needle if you cough, laugh, or are accidentally bumped, causing severe internal injuries.",
                                "Moisture from lips causes the needle to rust within minutes.",
                                "It makes the needle tip turn blunt.",
                                "It transfers bacteria that rots the cotton fabric."
                            ],
                            "answer": "A",
                            "explanation": "Holding sharp pins in the mouth is extremely hazardous. An unexpected cough or bump can cause accidental swallowing, leading to life-threatening internal injury."
                        }
                    },
                    {
                        "type": "knowledge_check",
                        "title": "Topic Assessment - Question 2: Plain vs. Open Seam Structural Difference",
                        "content": {
                            "question": "What is the structural difference between a Plain Seam and an Open Seam?",
                            "options": [
                                "In a plain seam, both raw edges lie together on one side of the stitching; in an open seam, the two seam allowances are split and pressed flat on opposite sides.",
                                "A plain seam is hand sewn, while an open seam is only sewn with electric machines.",
                                "A plain seam has a 5.0 cm allowance, while an open seam has zero allowance.",
                                "A plain seam uses elastic thread, while an open seam uses wire."
                            ],
                            "answer": "A",
                            "explanation": "Plain seams keep both raw edges together on one side (fast and strong for light fabrics). Open seams part the allowances and press them flat on opposite sides to eliminate bulk on heavy fabrics."
                        }
                    }
                ],
                # Page 8: Topic Assessment Part 2 (Questions 3 to 5)
                [
                    {
                        "type": "knowledge_check",
                        "title": "Topic Assessment - Question 3: Fabric Suitability for Plain Seams",
                        "content": {
                            "question": "Which fabric choice is most suitable for sewing a standard Plain Seam sample?",
                            "options": [
                                "Lightweight woven cotton fabric (e.g., poplin or calico).",
                                "Thick, heavy wool blanketing.",
                                "Rigid, heavy canvas backpack sheets.",
                                "Heavy knitted winter sweaters."
                            ],
                            "answer": "A",
                            "explanation": "Plain seams are simplest and most effective on lightweight woven cottons (calico/poplin), where having both edges lie together does not create excessive bulk."
                        }
                    },
                    {
                        "type": "knowledge_check",
                        "title": "Topic Assessment - Question 4: Fabric Shears Preservation Rule",
                        "content": {
                            "question": "Why should specialized fabric shears never be used to cut paper patterns or cardboard boxes?",
                            "options": [
                                "Paper contains dense fibers and abrasive minerals that quickly dull the fine cutting edge of fabric shears, making them chew and tear fabric.",
                                "Fabric shears cut paper too quickly, leading to crooked lines.",
                                "Paper fibers chemically dissolve steel blades.",
                                "It is culturally disrespectful to use tailoring tools on school paper."
                            ],
                            "answer": "A",
                            "explanation": "Paper fibers are abrasive. Cutting paper or cardboard rapidly dulls the razor-sharp edge of fabric shears, ruining their ability to cut clean, unfrayed fabric edges."
                        }
                    },
                    {
                        "type": "knowledge_check",
                        "title": "Topic Assessment - Question 5: Strongest Hand Stitch for Side Seams",
                        "content": {
                            "question": "Which hand stitch provides the strongest, most durable joint for sewing the side seams of a pocket pouch?",
                            "options": [
                                "The small, interlocking hand backstitch.",
                                "Long, loose temporary basting stitches.",
                                "A simple, loose running stitch.",
                                "A wide overcasting stitch."
                            ],
                            "answer": "A",
                            "explanation": "The hand backstitch overlaps backward with every stitch, creating a tight, interlocking continuous thread line that mimics a sewing machine stitch, offering maximum joint strength."
                        }
                    }
                ],
                # Page 9: Topic Assessment Part 3 (Questions 6 to 8)
                [
                    {
                        "type": "knowledge_check",
                        "title": "Topic Assessment - Question 6: Plain Seam Preparation Sequence",
                        "content": {
                            "question": "What is the correct logical sequence of steps to prepare and hand-sew a straight plain seam?",
                            "options": [
                                "Match right sides together -> Mark seam allowance -> Pin at right angles -> Baste -> Sew permanent stitches -> Remove basting.",
                                "Permanent stitching -> Basting -> Pinning -> Pressing -> Cutting.",
                                "Sew permanent stitches -> Press open -> Pull fabric apart -> Match raw edges.",
                                "Cut raw edges -> Sew backstitches -> Draw chalk lines -> Pin -> Baste."
                            ],
                            "answer": "A",
                            "explanation": "Matching right sides, measuring/marking, pinning at right angles, and basting lock fabric layers in place so permanent stitches can be sewn straight and accurately."
                        }
                    },
                    {
                        "type": "knowledge_check",
                        "title": "Topic Assessment - Question 7: Function of a Thimble",
                        "content": {
                            "question": "How does wearing a 'thimble' on your middle finger protect you during hand-sewing practicals?",
                            "options": [
                                "It provides a hard protective surface to push the needle's eye-end through thick fabric layers, preventing painful skin puncture wounds.",
                                "It holds fabric pieces tightly together.",
                                "It acts as a magnet that holds pins.",
                                "It stops thread from tangling."
                            ],
                            "answer": "A",
                            "explanation": "A thimble worn on the middle finger acts as a protective shield, allowing the sewer to push the blunt eye-end of the needle through tough cloth without puncturing their skin."
                        }
                    },
                    {
                        "type": "knowledge_check",
                        "title": "Topic Assessment - Question 8: Rationale for Pressing Open Seams",
                        "content": {
                            "question": "What is the primary technical purpose of 'pressing' the seam allowances of an open seam with a hot iron?",
                            "options": [
                                "To flatten the joint completely, removing bulky ridges so the seam looks smooth and professional and does not chafe the skin.",
                                "To dry the fabric after washing.",
                                "To shrink the thread fibers to make them stronger.",
                                "To fuse the fabric layers together without thread."
                            ],
                            "answer": "A",
                            "explanation": "Pressing parts the seam allowances and flattens them flat against the garment inner, eliminating bulky ridges and making the exterior joint smooth and neat."
                        }
                    }
                ],
                # Page 10: Topic Assessment Part 4 (Questions 9 to 10)
                [
                    {
                        "type": "knowledge_check",
                        "title": "Topic Assessment - Question 9: Lint Cleaning Before Oiling",
                        "content": {
                            "question": "Why must manual sewing machines be regularly brushed free of lint and dust before applying oil?",
                            "options": [
                                "Lint absorbs oil like a sponge, drying out the gears and forming a thick, abrasive paste that accelerates machine wear and jams parts.",
                                "Dust turns the thread black.",
                                "Dust catches fire at high speeds.",
                                "Lint causes needles to bend."
                            ],
                            "answer": "A",
                            "explanation": "Fabric lint traps oil and turns into a gritty sludge that accelerates mechanical friction and gear wear. Always brush away lint before applying fresh mineral oil."
                        }
                    },
                    {
                        "type": "knowledge_check",
                        "title": "Topic Assessment - Question 10: Economic Self-Reliance of Sewing",
                        "content": {
                            "question": "What is the primary economic benefit of mastering hand-sewing and production skills in a household context?",
                            "options": [
                                "It enables household members to repair torn garments and construct simple functional articles from fabric scraps, saving money and reducing waste.",
                                "It allows households to open large industrial garment factories overnight.",
                                "It guarantees you never have to wash clothes.",
                                "It eliminates the need to purchase food."
                            ],
                            "answer": "A",
                            "explanation": "Sewing promotes financial self-reliance by allowing families to mend split seams, alter clothing, and repurpose scrap cloth into useful household items instead of buying new ones."
                        }
                    }
                ]
            ]
        }
    ]

def ingest_cbc_grade8_agriculture_topic10(replace: bool = True):
    """Executes the database transaction to ingest Topic 10 into CBC Grade 8 Agriculture."""
    print("=" * 80)
    print("STARTING CONTENT INGESTION: CBC GRADE 8 AGRICULTURE — TOPIC 10 (FINAL TOPIC)")
    print("=" * 80)

    with transaction.atomic():
        curriculum, _ = Curriculum.objects.get_or_create(
            name="CBC",
            defaults={"description": "Competency Based Curriculum"}
        )
        grade, _ = Grade.objects.get_or_create(
            curriculum=curriculum,
            name="Grade 8",
            defaults={"level": 8, "description": "Junior Secondary School Grade 8"}
        )
        subject, _ = Subject.objects.get_or_create(
            grade=grade,
            name="Agriculture",
            defaults={"description": "Grade 8 Agriculture (CBC)"}
        )

        print(f"[*] Hierarchy Resolved: {curriculum.name} -> {grade.name} -> {subject.name}")

        topic_name = "Sewing and Production Techniques"
        if replace:
            existing_topics = Topic.objects.filter(subject=subject, name=topic_name)
            if existing_topics.exists():
                print(f"[*] Found existing topic '{topic_name}' (ID: {existing_topics.first().id}). Deleting for clean replace...")
                existing_topics.delete()

        topic, created = Topic.objects.get_or_create(
            subject=subject,
            name=topic_name,
            defaults={
                "order": 10,
                "description": "Comprehensive hand-sewing skills, textile construction, and studio safety: understanding seams (joining, shaping, decorating); seam allowance buffers (1.0 cm to 1.5 cm); structural mechanics and applications of Plain Seams vs. Open Seams; hand-sewing practicals (pinning, basting, permanent backstitch); flat iron pressing and edge finishing (pinking shears and overcasting); project construction of a functional cotton Pocket Pouch; studio safety (thimbles, pincushions, passing shears handle-first); and manual sewing machine maintenance (lint brushing and mineral oil lubrication)."
            }
        )
        print(f"[*] Topic: '{topic.name}' (ID: {topic.id}, Created: {created})")

        curriculum_data = build_topic10_curriculum()
        total_units = len(curriculum_data)
        total_lessons = 0
        total_pages = 0
        total_blocks = 0

        for unit_data in curriculum_data:
            u_order = unit_data["unit_order"]
            u_name = clean_text(unit_data["unit_name"])
            u_desc = clean_text(unit_data["unit_description"])
            l_title = clean_text(unit_data["lesson_title"])
            pages_data = unit_data["pages"]

            unit = LearningUnit.objects.create(
                topic=topic,
                name=u_name,
                order=u_order,
                description=u_desc
            )

            lesson = Lesson.objects.create(
                topic=topic,
                learning_unit=unit,
                title=l_title,
                status="published",
                version=1
            )
            total_lessons += 1

            block_order = 0
            for page_idx, page_blocks in enumerate(pages_data, start=1):
                total_pages += 1
                page_title = None

                for comp_idx, b_data in enumerate(page_blocks, start=1):
                    b_type = b_data["type"]
                    b_title = clean_text(b_data.get("title", ""))
                    b_content = clean_dict(b_data.get("content", {}))

                    if not page_title and b_title:
                        page_title = b_title

                    LessonBlock.objects.create(
                        lesson=lesson,
                        block_id=f"g8_agri_t10_u{u_order}_p{page_idx}_b{comp_idx}",
                        block_type=b_type,
                        component_type=b_type,
                        title=b_title,
                        content=b_content,
                        page_number=page_idx,
                        page_title=page_title,
                        component_order=comp_idx,
                        order=block_order
                    )
                    block_order += 1
                    total_blocks += 1

            print(f"  [+] Ingested Unit {u_order}: '{u_name}' -> Lesson ID {lesson.id} ({len(pages_data)} Pages, {block_order} Blocks)")

        print("\n" + "=" * 80)
        print(f"[SUCCESS] Ingestion Complete for Grade 8 Topic 10: '{topic.name}'")
        print(f"[*] Units Created:   {total_units}")
        print(f"[*] Lessons Created: {total_lessons}")
        print(f"[*] Total Pages:     {total_pages}")
        print(f"[*] Total Blocks:    {total_blocks}")
        print("=" * 80)

if __name__ == "__main__":
    replace_flag = "--replace" in sys.argv or True
    ingest_cbc_grade8_agriculture_topic10(replace=replace_flag)
