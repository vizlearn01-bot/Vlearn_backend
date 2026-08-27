"""
VLearn CBC Grade 10 Geography — Topic 2: Map Reading and Interpretation
Direct Programmatic Source-Driven Ingestion Engine

Subject: Geography (Grade 10, CBC)
Topic 2: Map Reading and Interpretation
Source: Grade 10 Geography/02_map_reading_and_interpretation.md

Usage:
  ./venv/bin/python curriculum/ingest_cbc_grade10_geography_topic2.py
"""

import os
import sys
import re
import json
import django

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "Nexus_backend.settings")
django.setup()

from django.db import transaction
from curriculum.models import (
    Curriculum, Grade, Subject, Topic,
    LearningUnit, Lesson, LessonBlock
)

def clean_text(raw_str):
    """Remove citation brackets ([1], [37], [S1, p. 1]) and normalize whitespace."""
    if not isinstance(raw_str, str):
        return raw_str
    cleaned = re.sub(r'\[(?:\d+|image_\d+|S\d+.*?|[\d,\s]+)\]', '', raw_str)
    cleaned = re.sub(r'[ \t]+', ' ', cleaned)
    return cleaned.strip()

def clean_content_dict(data):
    if isinstance(data, str):
        return clean_text(data)
    elif isinstance(data, list):
        return [clean_content_dict(item) for item in data]
    elif isinstance(data, dict):
        return {k: clean_content_dict(v) for k, v in data.items()}
    return data

# =============================================================================
# TOPIC 2 LESSON DEFINITIONS (13 LESSONS)
# =============================================================================
LESSONS_DATA = [
    # Lesson 1: Understanding Topographical Maps
    {
        "unit_order": 1,
        "unit_name": "Understanding Topographical Maps",
        "lesson_title": "Understanding Topographical Maps",
        "pages": [
            {
                "page_number": 1,
                "page_title": "Introduction to Topographical Maps",
                "blocks": [
                    {
                        "block_type": "suggested_image",
                        "component_type": "suggested_image",
                        "title": "Topographical Map Sheet with Relief and Cultural Details",
                        "content": {"text": "A standard topographical survey map sheet showing elevation contour lines, grid coordinates, drainage systems, and human infrastructure."}
                    },
                    {
                        "block_type": "learning_goal",
                        "component_type": "learning_goal",
                        "title": "Lesson Objectives: Topographical Maps",
                        "content": {
                            "text": (
                                "By the end of this lesson, you will be able to:\n\n"
                                "- Define the term 'map' and classify maps into Topographical, Thematic, and Sketch types\n"
                                "- Identify the six essential marginal components on a standard topographical sheet\n"
                                "- Explain how Survey of Kenya 1:50,000 series maps are structured for spatial reading"
                            )
                        }
                    },
                    {
                        "block_type": "concept_explanation",
                        "component_type": "concept_explanation",
                        "title": "Prerequisite Spark: The Bird's-Eye View",
                        "content": {
                            "text": (
                                "Imagine floating in an airplane directly above your hometown. From above, houses look like small rectangles, "
                                "rivers look like winding silver ribbons, and roads connect towns like a spider's web. "
                                "A map is a scaled, stylized mathematical drawing of this bird's-eye view."
                            )
                        }
                    }
                ]
            },
            {
                "page_number": 2,
                "page_title": "Map Types and Marginal Information",
                "blocks": [
                    {
                        "block_type": "definition_card",
                        "component_type": "definition_card",
                        "title": "Essential Map Definitions",
                        "content": {
                            "definitions": [
                                {
                                    "term": "Topographical Map",
                                    "definition": "A general-purpose map at medium to large scale showing both natural physical relief (elevation, drainage, vegetation) and artificial cultural features (roads, buildings, administrative boundaries).",
                                    "simple": "A detailed drawing that reveals the exact shape of the terrain and everything constructed on it."
                                },
                                {
                                    "term": "Thematic Map",
                                    "definition": "A specialized map designed to emphasize a specific spatial theme or topic (e.g. annual rainfall distribution, population density, geology).",
                                    "simple": "A map dedicated to a single topic, such as weather or soil type."
                                }
                            ]
                        }
                    },
                    {
                        "block_type": "concept_explanation",
                        "component_type": "concept_explanation",
                        "title": "The Six Marginal Reference Elements",
                        "content": {
                            "text": (
                                "Standard Survey of Kenya topographical sheets feature six critical reference components on their margins:\n\n"
                                "1. **Sheet Title & Series Number**: Identifies the locality (e.g., 'NYERI, Sheet 120/4, Series Y731').\n"
                                "2. **Key / Legend**: Decodes all conventional signs, colors, and line types used across the sheet.\n"
                                "3. **Scale (RF, Statement, Linear)**: Establishes the mathematical ratio between map distance and ground distance.\n"
                                "4. **North Arrow Box**: Shows True North, Grid North, and Magnetic North with annual magnetic variation.\n"
                                "5. **Grid Reference Frame**: A network of numbered Eastings and Northings for precise location referencing.\n"
                                "6. **Sheet History & Edition**: Documents compilation dates, aerial photography flight years, and publisher metadata."
                            )
                        }
                    },
                    {
                        "block_type": "suggested_diagram",
                        "component_type": "suggested_diagram",
                        "title": "Marginal Information Layout of a Standard Topographical Sheet",
                        "content": {"text": "Vector diagram illustrating the margin layout of a 1:50,000 topographical map sheet showing title, key, scale bar, north arrows, and grid frame."}
                    }
                ]
            },
            {
                "page_number": 3,
                "page_title": "Video Demonstration & Walkthrough",
                "blocks": [
                    {
                        "block_type": "suggested_video",
                        "component_type": "suggested_video",
                        "title": "Reading Marginal Information on Topographical Maps",
                        "content": {
                            "resolved_video_id": "z9d9qL_v_aI",
                            "youtube_url": "https://www.youtube.com/watch?v=z9d9qL_v_aI",
                            "description": "Video walkthrough showing how to locate the title, scale, magnetic declination, and legend on a topographical map sheet."
                        }
                    }
                ]
            },
            {
                "page_number": 4,
                "page_title": "Knowledge Check",
                "blocks": [
                    {
                        "block_type": "knowledge_check",
                        "component_type": "knowledge_check",
                        "title": "Question 1: The Function of the Map Key",
                        "content": {
                            "question": "Which marginal component of a topographical map serves as the dictionary that translates symbols, colors, and line types into real-world features?",
                            "options": [
                                "A. The Sheet History",
                                "B. The Key / Legend",
                                "C. The Linear Scale",
                                "D. The Sheet Index"
                            ],
                            "correct_answer": "B",
                            "explanation": "The Key (or Legend) defines and decodes all symbols, abbreviations, and conventional signs shown on the map."
                        }
                    },
                    {
                        "block_type": "knowledge_check",
                        "component_type": "knowledge_check",
                        "title": "Question 2: Topographical vs Thematic Maps",
                        "content": {
                            "question": "What is the key distinguishing characteristic of a topographical map compared to a thematic map?",
                            "options": [
                                "A. Topographical maps never use scales or grid lines",
                                "B. Topographical maps depict both physical relief (elevation) and man-made cultural features simultaneously",
                                "C. Topographical maps only display administrative boundary lines",
                                "D. Topographical maps are always drawn freehand"
                            ],
                            "correct_answer": "B",
                            "explanation": "Topographical maps provide comprehensive multi-purpose spatial coverage of terrain elevation, drainage, vegetation, and human infrastructure."
                        }
                    }
                ]
            }
        ]
    },

    # Lesson 2: Direction, Compass Bearings, and Location
    {
        "unit_order": 2,
        "unit_name": "Direction, Compass Bearings, and Location",
        "lesson_title": "Direction, Compass Bearings, and Location",
        "pages": [
            {
                "page_number": 1,
                "page_title": "Direction and Bearing Fundamentals",
                "blocks": [
                    {
                        "block_type": "suggested_image",
                        "component_type": "suggested_image",
                        "title": "Prismatic Compass and Navigational Geometry",
                        "content": {"text": "A magnetic prismatic compass aligned with map grid lines for taking directional bearings in the field."}
                    },
                    {
                        "block_type": "learning_goal",
                        "component_type": "learning_goal",
                        "title": "Lesson Objectives: Direction and Bearing",
                        "content": {
                            "text": (
                                "By the end of this lesson, you will be able to:\n\n"
                                "- Identify and construct the 16 points of the compass card\n"
                                "- Differentiate with precision between Direction and Compass Bearing\n"
                                "- Measure forward grid bearings using a protractor and calculate reciprocal back bearings\n"
                                "- Adjust for magnetic declination to convert grid bearings to magnetic bearings"
                            )
                        }
                    }
                ]
            },
            {
                "page_number": 2,
                "page_title": "The 16-Point Compass & Bearing Measurement",
                "blocks": [
                    {
                        "block_type": "definition_card",
                        "component_type": "definition_card",
                        "title": "Direction vs Bearing Defined",
                        "content": {
                            "definitions": [
                                {
                                    "term": "Direction",
                                    "definition": "The general heading along which a feature lies relative to a reference point, expressed using compass points (e.g. North-East, South-South-West).",
                                    "simple": "A general compass heading."
                                },
                                {
                                    "term": "Bearing",
                                    "definition": "The precise horizontal angle measured clockwise from True, Grid, or Magnetic North to a target line, expressed in three digits from 000° to 360°.",
                                    "simple": "An exact angle in degrees measured clockwise starting from North."
                                }
                            ]
                        }
                    },
                    {
                        "block_type": "step_process",
                        "component_type": "step_process",
                        "title": "How to Measure a Grid Bearing (Step-by-Step)",
                        "content": {
                            "steps": [
                                {"step_number": 1, "title": "Identify Reference Point", "description": "For 'Bearing of B from A', start at point A (the 'from' point)."},
                                {"step_number": 2, "title": "Draw North Grid Line", "description": "Draw a thin vertical pencil line through Point A parallel to the map's vertical grid lines (Eastings)."},
                                {"step_number": 3, "title": "Connect Target Line", "description": "Draw a straight line connecting Point A to Point B."},
                                {"step_number": 4, "title": "Position Protractor", "description": "Center your 360°/180° protractor over Point A, aligning 000° with the upward North line."},
                                {"step_number": 5, "title": "Read Clockwise Angle", "description": "Read the angle clockwise from 000° North to the target line AB and record as three digits (e.g. 065°, 142°, 285°)."}
                            ]
                        }
                    },
                    {
                        "block_type": "suggested_diagram",
                        "component_type": "suggested_diagram",
                        "title": "Protractor Alignment and Bearing Measurement Diagram",
                        "content": {"text": "Vector diagram illustrating how to align the center and 0-degree mark of a protractor on Point A to measure the clockwise angle to Point B."}
                    }
                ]
            },
            {
                "page_number": 3,
                "page_title": "Back Bearing & Magnetic Declination",
                "blocks": [
                    {
                        "block_type": "formula_breakdown",
                        "component_type": "formula_breakdown",
                        "title": "Back Bearing Calculation Formula",
                        "content": {
                            "text": (
                                "The **Back Bearing** (the reverse bearing of A from B) is opposite by 180°:\n\n"
                                "- If Forward Bearing is **< 180°**: `Back Bearing = Forward Bearing + 180°`\n"
                                "- If Forward Bearing is **>= 180°**: `Back Bearing = Forward Bearing - 180°`\n\n"
                                "*Example*: Forward bearing = 075° -> Back bearing = 075° + 180° = **255°**."
                            )
                        }
                    },
                    {
                        "block_type": "common_misconception",
                        "component_type": "common_misconception",
                        "title": "Common Exam Trap: Measuring from the Wrong End",
                        "content": {
                            "misconception": "Placing the protractor at Point B when asked for the 'bearing of B from A'.",
                            "reality": "Always place the center of the protractor on the starting point designated after the word 'from'."
                        }
                    }
                ]
            },
            {
                "page_number": 4,
                "page_title": "Formative Knowledge Check",
                "blocks": [
                    {
                        "block_type": "knowledge_check",
                        "component_type": "knowledge_check",
                        "title": "Question 1: Starting Position for Bearing",
                        "content": {
                            "question": "A student is asked to calculate the bearing of a church from a cattle dip. Where should the center of the protractor be placed?",
                            "options": [
                                "A. Halfway between the church and cattle dip",
                                "B. At the church",
                                "C. At the cattle dip",
                                "D. At the bottom edge of the map"
                            ],
                            "correct_answer": "C",
                            "explanation": "The question specifies 'from the cattle dip', making the cattle dip the reference vertex where the north line and protractor center must be situated."
                        }
                    },
                    {
                        "block_type": "knowledge_check",
                        "component_type": "knowledge_check",
                        "title": "Question 2: Calculating Back Bearing",
                        "content": {
                            "question": "If the forward grid bearing of a bridge from a school is measured as 130°, what is the reciprocal back bearing?",
                            "options": [
                                "A. 050°",
                                "B. 310°",
                                "C. 220°",
                                "D. 080°",
                            ],
                            "correct_answer": "B",
                            "explanation": "Because 130° is less than 180°, add 180°: 130° + 180° = 310°."
                        }
                    }
                ]
            }
        ]
    },

    # Lesson 3: Map Scales and Distance Calculations
    {
        "unit_order": 3,
        "unit_name": "Map Scales and Distance Calculations",
        "lesson_title": "Map Scales and Distance Calculations",
        "pages": [
            {
                "page_number": 1,
                "page_title": "The Geometry of Map Scales",
                "blocks": [
                    {
                        "block_type": "suggested_image",
                        "component_type": "suggested_image",
                        "title": "Linear Scale Bar on Cartographic Charts",
                        "content": {"text": "A divided linear scale bar showing primary kilometer divisions and secondary meter subdivisions."}
                    },
                    {
                        "block_type": "learning_goal",
                        "component_type": "learning_goal",
                        "title": "Lesson Objectives: Scales & Distances",
                        "content": {
                            "text": (
                                "By the end of this lesson, you will be able to:\n\n"
                                "- Define map scale and differentiate between Statement, Linear, and Representative Fraction (RF) forms\n"
                                "- Convert seamlessly between RF and Statement scales\n"
                                "- Measure straight-line distances and winding routes (rivers/roads) using the string/thread method"
                            )
                        }
                    }
                ]
            },
            {
                "page_number": 2,
                "page_title": "Three Forms of Map Scale",
                "blocks": [
                    {
                        "block_type": "comparison_table",
                        "component_type": "comparison_table",
                        "title": "Classification of Scale Formats",
                        "content": {
                            "headers": ["Scale Type", "Format Example", "Interpretation / Usage"],
                            "rows": [
                                ["Statement Scale", "1 cm represents 0.5 km", "Direct verbal expression of map-to-ground relationship"],
                                ["Representative Fraction (RF)", "1:50,000 or 1/50,000", "Unitless ratio; 1 unit on map = 50,000 identical units on ground"],
                                ["Linear Scale", "Graduated bar line", "Visual bar subdivided into primary (km) and secondary (m) intervals"]
                            ]
                        }
                    },
                    {
                        "block_type": "formula_breakdown",
                        "component_type": "formula_breakdown",
                        "title": "Worked Example: Converting RF to Statement Scale",
                        "content": {
                            "text": (
                                "Convert RF **1:50,000** to a statement scale in centimeters to kilometers:\n\n"
                                "1. `1 cm on map = 50,000 cm on ground`\n"
                                "2. `Convert cm to meters`: `50,000 / 100 = 500 meters`\n"
                                "3. `Convert meters to kilometers`: `500 / 1,000 = 0.5 kilometers`\n"
                                "4. Statement: **'1 cm represents 0.5 km'** (or **'2 cm represents 1 km'**)."
                            )
                        }
                    }
                ]
            },
            {
                "page_number": 3,
                "page_title": "Measuring Curved and Winding Distances",
                "blocks": [
                    {
                        "block_type": "step_process",
                        "component_type": "step_process",
                        "title": "The Thread Method for Winding Routes",
                        "content": {
                            "steps": [
                                {"step_number": 1, "title": "Prepare Thread", "description": "Tie a knot at one end of a thin, non-stretch sewing thread to serve as the start mark."},
                                {"step_number": 2, "title": "Align and Pivot", "description": "Place the knot at the starting landmark and pivot the thread along every curve of the road or river using a pencil tip."},
                                {"step_number": 3, "title": "Mark Terminal Point", "description": "Mark the final destination on the thread with a sharp pen."},
                                {"step_number": 4, "title": "Measure Against Ruler / Scale", "description": "Straighten the thread along a centimeter ruler or directly on the map's linear scale bar to find the exact ground distance."}
                            ]
                        }
                    },
                    {
                        "block_type": "suggested_diagram",
                        "component_type": "suggested_diagram",
                        "title": "The Thread Method Visualized on a Meandering River",
                        "content": {"text": "Vector diagram illustrating thread placement along winding curves of a river and its subsequent measurement against a linear scale."}
                    }
                ]
            },
            {
                "page_number": 4,
                "page_title": "Formative Knowledge Check",
                "blocks": [
                    {
                        "block_type": "knowledge_check",
                        "component_type": "knowledge_check",
                        "title": "Question 1: Distance Calculation on 1:50,000 Scale",
                        "content": {
                            "question": "A straight road measures exactly 12.4 cm on a 1:50,000 topographical map. What is the actual ground distance in kilometers?",
                            "options": [
                                "A. 12.4 km",
                                "B. 6.2 km",
                                "C. 24.8 km",
                                "D. 3.1 km"
                            ],
                            "correct_answer": "B",
                            "explanation": "On a 1:50,000 map, 1 cm represents 0.5 km. Therefore, 12.4 cm * 0.5 km/cm = 6.2 km."
                        }
                    },
                    {
                        "block_type": "knowledge_check",
                        "component_type": "knowledge_check",
                        "title": "Question 2: Scale Conversion",
                        "content": {
                            "question": "What is the Representative Fraction (RF) for a statement scale of '1 cm represents 2.5 kilometers'?",
                            "options": [
                                "A. 1:25,000",
                                "B. 1:250,000",
                                "C. 1:2,500",
                                "D. 1:500,000"
                            ],
                            "correct_answer": "B",
                            "explanation": "2.5 km = 2,500 m = 250,000 cm. Thus, the RF scale is 1:250,000."
                        }
                    }
                ]
            }
        ]
    },

    # Lesson 4: Conventional Signs and Symbols
    {
        "unit_order": 4,
        "unit_name": "Conventional Signs and Symbols",
        "lesson_title": "Conventional Signs and Symbols",
        "pages": [
            {
                "page_number": 1,
                "page_title": "The Visual Language of Maps",
                "blocks": [
                    {
                        "block_type": "suggested_image",
                        "component_type": "suggested_image",
                        "title": "Standard Cartographic Conventional Signs",
                        "content": {"text": "A standard topographic legend displaying conventional signs for vegetation, hydrography, communication, and human settlements."}
                    },
                    {
                        "block_type": "learning_goal",
                        "component_type": "learning_goal",
                        "title": "Lesson Objectives: Signs & Symbols",
                        "content": {
                            "text": (
                                "By the end of this lesson, you will be able to:\n\n"
                                "- Identify and interpret standard international conventional signs on Survey of Kenya maps\n"
                                "- Decode standard cartographic color conventions (Blue, Green, Brown, Red, Black)\n"
                                "- Extract social and economic data (schools, dispensaries, factories, plantations) from map symbols"
                            )
                        }
                    }
                ]
            },
            {
                "page_number": 2,
                "page_title": "Cartographic Color Conventions",
                "blocks": [
                    {
                        "block_type": "comparison_table",
                        "component_type": "comparison_table",
                        "title": "Standard Color Codes on Topographical Maps",
                        "content": {
                            "headers": ["Color", "Geographical Category", "Standard Features Represented"],
                            "rows": [
                                ["Blue", "Hydrography & Water", "Rivers, lakes, swamps, boreholes, dams, seasonal streams"],
                                ["Green", "Vegetation & Land Cover", "Forests, plantations, scrub, bamboo, thickets, mangroves"],
                                ["Brown", "Relief & Landforms", "Contour lines, spot heights, sand dunes, trigonometric stations"],
                                ["Red / Orange", "Human Infrastructure", "All-weather bound surface roads, principal highways, urban zones"],
                                ["Black", "Man-Made / Cultural", "Loose-surface roads, footpaths, railways, buildings, churches, boundaries"]
                            ]
                        }
                    },
                    {
                        "block_type": "suggested_diagram",
                        "component_type": "suggested_diagram",
                        "title": "Topographical Conventional Signs and Color Matrix",
                        "content": {"text": "Vector chart displaying standard conventional symbols categorized by color: blue water, green vegetation, brown relief, and black/red cultural infrastructure."}
                    }
                ]
            },
            {
                "page_number": 3,
                "page_title": "Formative Knowledge Check",
                "blocks": [
                    {
                        "block_type": "knowledge_check",
                        "component_type": "knowledge_check",
                        "title": "Question 1: Interpreting Map Colors",
                        "content": {
                            "question": "On a standard Survey of Kenya 1:50,000 sheet, which color is universally used to depict contour lines, relief elevation, and spot heights?",
                            "options": [
                                "A. Green",
                                "B. Black",
                                "C. Brown",
                                "D. Blue"
                            ],
                            "correct_answer": "C",
                            "explanation": "Brown is the standardized international cartographic color used for relief, contour lines, and physical terrain elevation."
                        }
                    },
                    {
                        "block_type": "knowledge_check",
                        "component_type": "knowledge_check",
                        "title": "Question 2: Evidence of Social Services",
                        "content": {
                            "question": "Which combination of conventional symbols provides direct evidence of social and administrative services in a settlement?",
                            "options": [
                                "A. Papyrus swamp and seasonal marsh symbols",
                                "B. Letters 'Sch' (School), 'Disp' (Dispensary), and cross symbol (Church)",
                                "C. Broken black lines representing footpaths",
                                "D. Closely packed brown contour rings"
                            ],
                            "correct_answer": "B",
                            "explanation": "Standard abbreviations like 'Sch', 'Disp', 'PO' (Post Office), and religious symbols indicate educational, healthcare, and community services."
                        }
                    }
                ]
            }
        ]
    },

    # Lesson 5: Finding Your Place: Grid References
    {
        "unit_order": 5,
        "unit_name": "Finding Your Place: Grid References",
        "lesson_title": "Finding Your Place: Grid References",
        "pages": [
            {
                "page_number": 1,
                "page_title": "Cartographic Grid Coordinates",
                "blocks": [
                    {
                        "block_type": "suggested_image",
                        "component_type": "suggested_image",
                        "title": "Grid Reference System on Topographic Sheets",
                        "content": {"text": "A detailed close-up of intersecting Eastings and Northings forming a 1 km national grid square."}
                    },
                    {
                        "block_type": "learning_goal",
                        "component_type": "learning_goal",
                        "title": "Lesson Objectives: Grid References",
                        "content": {
                            "text": (
                                "By the end of this lesson, you will be able to:\n\n"
                                "- Distinguish between Eastings (vertical grid lines) and Northings (horizontal grid lines)\n"
                                "- State the fundamental rule of grid referencing: 'Eastings before Northings' (along the corridor, up the stairs)\n"
                                "- Give and locate features using 4-figure grid references (1 km square) and 6-figure grid references (100 m precision)"
                            )
                        }
                    }
                ]
            },
            {
                "page_number": 2,
                "page_title": "4-Figure and 6-Figure Grid Referencing",
                "blocks": [
                    {
                        "block_type": "concept_explanation",
                        "component_type": "concept_explanation",
                        "title": "The Golden Rule: Eastings Then Northings",
                        "content": {
                            "text": (
                                "A topographical map grid is composed of:\n\n"
                                "- **Eastings**: Vertical lines numbered from West to East (numbers increase eastward).\n"
                                "- **Northings**: Horizontal lines numbered from South to North (numbers increase northward).\n\n"
                                "### 1. 4-Figure Grid Reference (Locating a Grid Square)\n"
                                "Identifies the entire 1 km² square by stating the **bottom-left (South-West) corner** lines:\n"
                                "1. Read the Easting line to the left of the square (e.g. `34`).\n"
                                "2. Read the Northing line below the square (e.g. `78`).\n"
                                "3. Combine: **`3478`**.\n\n"
                                "### 2. 6-Figure Grid Reference (Point Precision to 100m)\n"
                                "Subdivides the 1 km grid square into tenths (0–9):\n"
                                "1. State the Easting (`34`) and estimate tenths east toward the target (`6`) -> `346`.\n"
                                "2. State the Northing (`78`) and estimate tenths north toward the target (`3`) -> `783`.\n"
                                "3. Combine: **`346783`**."
                            )
                        }
                    },
                    {
                        "block_type": "suggested_diagram",
                        "component_type": "suggested_diagram",
                        "title": "4-Figure vs 6-Figure Grid Reference Subdivisions",
                        "content": {"text": "Vector diagram showing a 1km by 1km grid square with tenths subdivisions for Eastings (X-axis) and Northings (Y-axis) pinpointing a target feature."}
                    }
                ]
            },
            {
                "page_number": 3,
                "page_title": "Formative Knowledge Check",
                "blocks": [
                    {
                        "block_type": "knowledge_check",
                        "component_type": "knowledge_check",
                        "title": "Question 1: 4-Figure Grid Corner Rule",
                        "content": {
                            "question": "When stating a 4-figure grid reference for a square, which intersection corner must always be read?",
                            "options": [
                                "A. The North-East corner (top-right)",
                                "B. The South-West corner (bottom-left)",
                                "C. The North-West corner (top-left)",
                                "D. The South-East corner (bottom-right)"
                            ],
                            "correct_answer": "B",
                            "explanation": "Standard 4-figure grid referencing requires taking the coordinates of the South-West (bottom-left) corner of the designated grid square."
                        }
                    },
                    {
                        "block_type": "knowledge_check",
                        "component_type": "knowledge_check",
                        "title": "Question 2: 6-Figure Grid Coordinate Order",
                        "content": {
                            "question": "A borehole is located at Easting 45 (6 tenths across) and Northing 82 (4 tenths up). What is its correct 6-figure grid reference?",
                            "options": [
                                "A. 824456",
                                "B. 456824",
                                "C. 458264",
                                "D. 645482"
                            ],
                            "correct_answer": "B",
                            "explanation": "Eastings come first (45 + 6 = 456) followed by Northings (82 + 4 = 824), yielding 456824."
                        }
                    }
                ]
            }
        ]
    },

    # Lesson 6: Representing Relief
    {
        "unit_order": 6,
        "unit_name": "Representing Relief",
        "lesson_title": "Representing Relief",
        "pages": [
            {
                "page_number": 1,
                "page_title": "Methods of Depicting Terrain Elevation",
                "blocks": [
                    {
                        "block_type": "suggested_image",
                        "component_type": "suggested_image",
                        "title": "Triangulation Pillar and Survey Benchmark on a Mountain Peak",
                        "content": {"text": "A concrete trigonometric station pillar on a mountain summit, representing accurate primary geodetic elevation points."}
                    },
                    {
                        "block_type": "learning_goal",
                        "component_type": "learning_goal",
                        "title": "Lesson Objectives: Relief Representation",
                        "content": {
                            "text": (
                                "By the end of this lesson, you will be able to:\n\n"
                                "- Define 'relief' and understand how a flat 2D map conveys 3D vertical elevation\n"
                                "- Compare methods of representing relief: Contours, Spot Heights, Trigonometric Stations, Benchmarks, Layer Tinting, and Hachures\n"
                                "- Calculate the Vertical Interval (V.I.) and determine height values on contour maps"
                            )
                        }
                    }
                ]
            },
            {
                "page_number": 2,
                "page_title": "Relief Depiction Methods Compared",
                "blocks": [
                    {
                        "block_type": "comparison_table",
                        "component_type": "comparison_table",
                        "title": "Methods of Depicting Relief on Maps",
                        "content": {
                            "headers": ["Method", "Symbol / Description", "Accuracy & Pedagogical Utility"],
                            "rows": [
                                ["Contour Lines", "Brown isarithmic lines joining points of equal elevation above sea level", "Most accurate and scientific method; allows slope and gradient calculation"],
                                ["Spot Heights", "A small black dot with a number (e.g. .1840)", "Provides exact pinpoint altitude for specific points (road junctions, hilltops)"],
                                ["Trigonometrical Stations", "Triangle with dot and height (e.g. △ 2150)", "High-accuracy geodetic pillars on prominent summits"],
                                ["Benchmarks (BM)", "Arrow symbol with letters 'BM' (e.g. BM 1620)", "Permanent altitude marks carved on stone along highways and railways"],
                                ["Layer Tinting", "Graduated color shading (green lowlands -> brown highlands)", "Gives instant visual overview of regional relief zones"],
                                ["Hachures", "Short, drawn lines pointing in the direction of steepest slope", "Historical method; shows steepness but gives no exact height numbers"]
                            ]
                        }
                    },
                    {
                        "block_type": "definition_card",
                        "component_type": "definition_card",
                        "title": "Vertical Interval (V.I.)",
                        "content": {
                            "definitions": [
                                {
                                    "term": "Vertical Interval (V.I.)",
                                    "definition": "The constant difference in vertical elevation between two consecutive contour lines on a topographical map (commonly 20 meters on Survey of Kenya 1:50,000 maps).",
                                    "simple": "The height jump from one contour line to the next."
                                }
                            ]
                        }
                    },
                    {
                        "block_type": "suggested_diagram",
                        "component_type": "suggested_diagram",
                        "title": "Comparison of Spot Heights, Trigonometrical Stations, Benchmarks, and Contours",
                        "content": {"text": "Vector diagram illustrating the distinct symbols for Spot Heights, Trig Stations (Primary/Secondary), Benchmarks, and brown Contour Lines."}
                    }
                ]
            },
            {
                "page_number": 3,
                "page_title": "Formative Knowledge Check",
                "blocks": [
                    {
                        "block_type": "knowledge_check",
                        "component_type": "knowledge_check",
                        "title": "Question 1: Defining Contour Lines",
                        "content": {
                            "question": "What is a contour line?",
                            "options": [
                                "A. A line connecting places with equal atmospheric pressure",
                                "B. An imaginary line on a map joining all points that have the same height above mean sea level",
                                "C. A line marking administrative county boundaries",
                                "D. A line connecting points with equal annual rainfall"
                            ],
                            "correct_answer": "B",
                            "explanation": "Contour lines join points of identical elevation above mean sea level, revealing the 3D relief of the land."
                        }
                    },
                    {
                        "block_type": "knowledge_check",
                        "component_type": "knowledge_check",
                        "title": "Question 2: Vertical Interval Calculation",
                        "content": {
                            "question": "On a map, consecutive index contours are labeled 1,400m and 1,500m, with 4 intermediate contour intervals between them. What is the Vertical Interval (V.I.)?",
                            "options": [
                                "A. 50 m",
                                "B. 20 m",
                                "C. 10 m",
                                "D. 100 m"
                            ],
                            "correct_answer": "B",
                            "explanation": "The difference between 1,500m and 1,400m is 100m. Divided across 5 intervals gives a Vertical Interval of 20 meters (100 / 5 = 20m)."
                        }
                    }
                ]
            }
        ]
    },

    # Lesson 7: Contour Interpretation: Slope Types and Landforms
    {
        "unit_order": 7,
        "unit_name": "Contour Interpretation: Slope Types and Landforms",
        "lesson_title": "Contour Interpretation: Slope Types and Landforms",
        "pages": [
            {
                "page_number": 1,
                "page_title": "Reading Landforms from Contours",
                "blocks": [
                    {
                        "block_type": "suggested_image",
                        "component_type": "suggested_image",
                        "title": "Topographic Mountain Relief and Contour Slopes",
                        "content": {"text": "A 3D topographical relief model of steep mountain slopes, valleys, and ridges compared with 2D contour drawings."}
                    },
                    {
                        "block_type": "learning_goal",
                        "component_type": "learning_goal",
                        "title": "Lesson Objectives: Slopes & Landforms",
                        "content": {
                            "text": (
                                "By the end of this lesson, you will be able to:\n\n"
                                "- Identify slope types: Gentle, Steep, Even, Uneven, Convex, and Concave\n"
                                "- Interpret major topographical landforms: Valleys, Spurs, Ridges, Hills, Plateaus, Cols, Saddles, Passes, and Cliffs\n"
                                "- Calculate slope gradient using the formula `Gradient = Vertical Interval (VI) / Horizontal Equivalent (HE)`"
                            )
                        }
                    }
                ]
            },
            {
                "page_number": 2,
                "page_title": "Slope Types and Contour Spacing",
                "blocks": [
                    {
                        "block_type": "concept_explanation",
                        "component_type": "concept_explanation",
                        "title": "Slope Types and Contour Patterns",
                        "content": {
                            "text": (
                                "1. **Gentle Slope**: Contours are **widely spaced** apart.\n"
                                "2. **Steep Slope**: Contours are **closely packed** together.\n"
                                "3. **Even / Regular Slope**: Contours are **uniformly and equally spaced**.\n"
                                "4. **Convex Slope**: Contours are **closely packed at the base** and **widely spaced at the top** (bulges outwards).\n"
                                "5. **Concave Slope**: Contours are **closely packed at the top** and **widely spaced at the base** (curves inward like a bowl)."
                            )
                        }
                    },
                    {
                        "block_type": "suggested_diagram",
                        "component_type": "suggested_diagram",
                        "title": "Six Fundamental Slope Types in Contour Profile",
                        "content": {"text": "Vector diagram illustrating contour spacing and side-profile views for Gentle, Steep, Even, Convex, Concave, and Terraced slopes."}
                    }
                ]
            },
            {
                "page_number": 3,
                "page_title": "Topographical Landforms Decoded",
                "blocks": [
                    {
                        "block_type": "comparison_table",
                        "component_type": "comparison_table",
                        "title": "Contour Characteristics of Major Landforms",
                        "content": {
                            "headers": ["Landform", "Contour Pattern / Shape", "V-Shape / U-Shape Direction"],
                            "rows": [
                                ["River Valley", "V-shaped contours", "V-apex points **upstream** (towards higher ground)"],
                                ["Spur (Ridge projection)", "V-shaped or U-shaped contours", "V-apex points **downstream** (towards lower ground)"],
                                ["Ridge", "Elongated, parallel contour bands", "Forms a long, narrow crest with steep side slopes"],
                                ["Col / Saddle", "Gap or dip between two hilltops", "Col is a narrow steep gap; Saddle is a broader, gentler dip"],
                                ["Plateau", "Closely packed contours at edges, flat open space on top", "Elevated upland with a broad, flat summit"],
                                ["Cliff", "Contour lines merge or touch each other", "Represents a near-vertical rock face"]
                            ]
                        }
                    }
                ]
            },
            {
                "page_number": 4,
                "page_title": "Formative Knowledge Check",
                "blocks": [
                    {
                        "block_type": "knowledge_check",
                        "component_type": "knowledge_check",
                        "title": "Question 1: Valley vs Spur V-Apex",
                        "content": {
                            "question": "How do you distinguish a river valley from a spur when inspecting V-shaped contour lines?",
                            "options": [
                                "A. Valley contours are green while spur contours are blue",
                                "B. In a valley, the apex of the V points upstream towards higher elevation; in a spur, the apex points towards lower elevation",
                                "C. Spurs are always flat plateaus with no contours",
                                "D. Valley contours never cross each other"
                            ],
                            "correct_answer": "B",
                            "explanation": "In a valley, V-shaped contours point toward higher ground (upstream), whereas in a spur (a land projection), they point toward lower ground."
                        }
                    },
                    {
                        "block_type": "knowledge_check",
                        "component_type": "knowledge_check",
                        "title": "Question 2: Convex Slope Contours",
                        "content": {
                            "question": "Which contour pattern characterizes a convex slope?",
                            "options": [
                                "A. Contours are widely spaced at the base and close together at the top",
                                "B. Contours are closely packed at the base and widely spaced towards the top",
                                "C. Contours are completely circular and concentric",
                                "D. Contours overlap and touch each other"
                            ],
                            "correct_answer": "B",
                            "explanation": "A convex slope is steep at the bottom (closely spaced contours) and gentle at the summit (widely spaced contours)."
                        }
                    }
                ]
            }
        ]
    },

    # Lesson 8: Drainage and Water Systems
    {
        "unit_order": 8,
        "unit_name": "Drainage and Water Systems",
        "lesson_title": "Drainage and Water Systems",
        "pages": [
            {
                "page_number": 1,
                "page_title": "Hydrological Patterns on Maps",
                "blocks": [
                    {
                        "block_type": "suggested_image",
                        "component_type": "suggested_image",
                        "title": "Aerial View of a River Drainage Basin",
                        "content": {"text": "Aerial photograph of a branching dendritic river network flowing across a drainage basin."}
                    },
                    {
                        "block_type": "learning_goal",
                        "component_type": "learning_goal",
                        "title": "Lesson Objectives: Drainage Patterns",
                        "content": {
                            "text": (
                                "By the end of this lesson, you will be able to:\n\n"
                                "- Identify river drainage features: Source, Tributaries, Confluence, Main stream, Distributaries, Delta/Mouth\n"
                                "- Classify the five major drainage patterns: Dendritic, Trellis, Radial, Parallel, and Centripetal\n"
                                "- Determine river flow direction using contour intersections and spot height gradients"
                            )
                        }
                    }
                ]
            },
            {
                "page_number": 2,
                "page_title": "The Five Major Drainage Patterns",
                "blocks": [
                    {
                        "block_type": "comparison_table",
                        "component_type": "comparison_table",
                        "title": "Characteristics of Drainage Patterns",
                        "content": {
                            "headers": ["Drainage Pattern", "Visual Geometry", "Geological / Relief Control"],
                            "rows": [
                                ["Dendritic", "Tree-branch like network", "Develops on rocks of uniform resistance (homogenous geology)"],
                                ["Trellis", "Rectangular geometry; tributaries join main river at **near right angles (90°)**", "Develops in folded or faulted terrain with alternating hard and soft rock strata"],
                                ["Radial", "Rivers flow outwards in all directions like spokes of a bicycle wheel", "Originates from a central isolated volcanic dome or mountain peak (e.g. Mt. Kenya)"],
                                ["Parallel", "Rivers flow side-by-side in the same direction with few bends", "Develops on steep, uniformly inclined fault escarpments"],
                                ["Centripetal", "Rivers converge inwards from all directions into a central depression or lake", "Flows into an inland basin or caldera lake (e.g. Lake Victoria / Lake Nakuru)"]
                            ]
                        }
                    },
                    {
                        "block_type": "suggested_diagram",
                        "component_type": "suggested_diagram",
                        "title": "The Five Classic Drainage Patterns Visualized",
                        "content": {"text": "Vector diagram illustrating Dendritic (tree-like), Trellis (right-angled), Radial (spokes), Parallel, and Centripetal drainage patterns."}
                    }
                ]
            },
            {
                "page_number": 3,
                "page_title": "Determining River Flow Direction",
                "blocks": [
                    {
                        "block_type": "step_process",
                        "component_type": "step_process",
                        "title": "Three Methods to Deduce River Flow Direction",
                        "content": {
                            "steps": [
                                {"step_number": 1, "title": "Contour V-Apex Rule", "description": "Contour lines form V-shapes pointing upstream. Rivers always flow in the opposite direction (away from the apex)."},
                                {"step_number": 2, "title": "Spot Height Gradient", "description": "Check spot heights along the river valley. Water flows from high elevation numbers to lower elevation numbers."},
                                {"step_number": 3, "title": "Tributary Junction Angle", "description": "Tributaries typically join the main stream at acute angles pointing downstream in the direction of flow."}
                            ]
                        }
                    }
                ]
            },
            {
                "page_number": 4,
                "page_title": "Formative Knowledge Check",
                "blocks": [
                    {
                        "block_type": "knowledge_check",
                        "component_type": "knowledge_check",
                        "title": "Question 1: Radial Drainage Pattern",
                        "content": {
                            "question": "A series of streams originate near the summit of Mount Kenya and flow outward in all directions like wheel spokes. What drainage pattern is this?",
                            "options": [
                                "A. Trellis",
                                "B. Dendritic",
                                "C. Radial",
                                "D. Centripetal"
                            ],
                            "correct_answer": "C",
                            "explanation": "Radial drainage occurs when streams flow outward down the flanks of a central elevated dome or volcanic peak."
                        }
                    },
                    {
                        "block_type": "knowledge_check",
                        "component_type": "knowledge_check",
                        "title": "Question 2: Trellis Pattern Geometry",
                        "content": {
                            "question": "What is the defining geometric feature of a trellis drainage pattern?",
                            "options": [
                                "A. Tributaries flow in circular loops",
                                "B. Tributaries join the main river at approximately right angles (90°)",
                                "C. All streams disappear underground",
                                "D. The main river splits into multiple braided channels"
                            ],
                            "correct_answer": "B",
                            "explanation": "In trellis drainage, tributaries follow parallel structural strike valleys and join the main consequent river at near right angles."
                        }
                    }
                ]
            }
        ]
    },

    # Lesson 9: Vegetation and Land Cover
    {
        "unit_order": 9,
        "unit_name": "Vegetation and Land Cover",
        "lesson_title": "Vegetation and Land Cover",
        "pages": [
            {
                "page_number": 1,
                "page_title": "Vegetation Communities on Maps",
                "blocks": [
                    {
                        "block_type": "suggested_image",
                        "component_type": "suggested_image",
                        "title": "Savanna Woodland and Forest Canopy Distribution",
                        "content": {"text": "An aerial land-cover map showing the spatial transition from tropical montane forest to savanna grassland."}
                    },
                    {
                        "block_type": "learning_goal",
                        "component_type": "learning_goal",
                        "title": "Lesson Objectives: Vegetation Interpretation",
                        "content": {
                            "text": (
                                "By the end of this lesson, you will be able to:\n\n"
                                "- Identify natural vegetation types on topographical maps (Forest, Woodland, Scrub, Thicket, Bamboo, Papyrus swamp, Mangrove)\n"
                                "- Deduce climate, altitude, and drainage conditions from vegetation symbols\n"
                                "- Differentiate between natural vegetation and planted agricultural crops/plantations"
                            )
                        }
                    }
                ]
            },
            {
                "page_number": 2,
                "page_title": "Vegetation Symbols as Environmental Indicators",
                "blocks": [
                    {
                        "block_type": "comparison_table",
                        "component_type": "comparison_table",
                        "title": "Vegetation Types and Inferred Environmental Conditions",
                        "content": {
                            "headers": ["Vegetation Symbol", "Cartographic Appearance", "Environmental & Climatic Inference"],
                            "rows": [
                                ["Dense Forest", "Solid green shading with tree icons", "High rainfall (> 1,200 mm), cool-to-warm highland altitude, fertile soils"],
                                ["Bamboo", "Bamboo cluster icons", "High-altitude montane zone (2,500m - 3,000m), cold, mist-prone slopes"],
                                ["Woodland / Scrub", "Scattered tree and bush symbols", "Semi-arid to sub-humid climate, moderate rainfall (500 - 800 mm)"],
                                ["Papyrus Swamp", "Blue-green marsh grass icons", "Poorly drained, waterlogged, flat floodplain or lake fringe"],
                                ["Mangrove Swamp", "Coastal marsh symbols along tidewater", "Saline, brackish intertidal mudflats along the Indian Ocean coast"]
                            ]
                        }
                    }
                ]
            },
            {
                "page_number": 3,
                "page_title": "Formative Knowledge Check",
                "blocks": [
                    {
                        "block_type": "knowledge_check",
                        "component_type": "knowledge_check",
                        "title": "Question 1: Environmental Indicators of Mangrove",
                        "content": {
                            "question": "The presence of mangrove swamp symbols along a river estuary indicates which environmental condition?",
                            "options": [
                                "A. Glaciated high-altitude alpine climate",
                                "B. Brackish, saline waterlogged mudflats in tropical coastal intertidal zones",
                                "C. Deep volcanic soils in arid inland plains",
                                "D. Desert sand dunes"
                            ],
                            "correct_answer": "B",
                            "explanation": "Mangrove trees thrive exclusively in saline, brackish intertidal mudflats along tropical marine coastlines."
                        }
                    }
                ]
            }
        ]
    },

    # Lesson 10: Synthesizing Relief, Drainage, and Vegetation
    {
        "unit_order": 10,
        "unit_name": "Synthesizing Relief, Drainage, and Vegetation",
        "lesson_title": "Synthesizing Relief, Drainage, and Vegetation",
        "pages": [
            {
                "page_number": 1,
                "page_title": "Holistic Landscape Analysis",
                "blocks": [
                    {
                        "block_type": "suggested_image",
                        "component_type": "suggested_image",
                        "title": "Highland Terrain, River Catchment, and Forest Cover",
                        "content": {"text": "A comprehensive satellite and topographical view showing the interrelationship between relief altitude, drainage networks, and forest cover."}
                    },
                    {
                        "block_type": "learning_goal",
                        "component_type": "learning_goal",
                        "title": "Lesson Objectives: Landscape Synthesis",
                        "content": {
                            "text": (
                                "By the end of this lesson, you will be able to:\n\n"
                                "- Synthesize relief, drainage, and vegetation into a unified ecological assessment\n"
                                "- Explain how altitude influences temperature and vegetation zonation\n"
                                "- Deduce human settlement and farming patterns from combined physical factors"
                            )
                        }
                    }
                ]
            },
            {
                "page_number": 2,
                "page_title": "The Triad of Physical Geography on Maps",
                "blocks": [
                    {
                        "block_type": "concept_explanation",
                        "component_type": "concept_explanation",
                        "title": "How Relief, Drainage, and Vegetation Interlock",
                        "content": {
                            "text": (
                                "When reading a topographical map, always analyze the **Physical Triad** together:\n\n"
                                "1. **Relief controls Drainage**: Rivers originate on high, steep ridges and flow toward gentle lowlands. Steep slopes produce fast-flowing, straight streams with radial or trellis patterns; flat plains produce meandering rivers and swamps.\n"
                                "2. **Relief controls Vegetation**: Highland slopes receive orographic rainfall, supporting dense forests (e.g. above 1,800m). Arid rain-shadow lowlands support only scrub and thornbush.\n"
                                "3. **Drainage shapes Relief**: River erosion cuts deep V-shaped valleys and gorges, shaping escarpments over geological time."
                            )
                        }
                    },
                    {
                        "block_type": "suggested_diagram",
                        "component_type": "suggested_diagram",
                        "title": "The Interlocking Triad: Relief, Drainage, and Vegetation",
                        "content": {"text": "Vector diagram illustrating the three-way interaction between topography, hydrology, and ecological vegetation cover."}
                    }
                ]
            },
            {
                "page_number": 3,
                "page_title": "Formative Knowledge Check",
                "blocks": [
                    {
                        "block_type": "knowledge_check",
                        "component_type": "knowledge_check",
                        "title": "Question 1: Altitude and Vegetation Correlation",
                        "content": {
                            "question": "A topographical map shows dense forest on western highland slopes between 2,000m and 2,600m, but dry scrub on eastern lowland plains below 1,000m. What explains this distribution?",
                            "options": [
                                "A. The lowlands receive higher rainfall than the highlands",
                                "B. Orographic rainfall and cool temperatures on highland windward slopes support forest growth, while lowlands lie in rain shadow",
                                "C. Forests are only planted in towns",
                                "D. Soil erosion is highest in the forests"
                            ],
                            "correct_answer": "B",
                            "explanation": "Highland windward slopes receive high orographic precipitation supporting dense forests, while leeward lowlands experience rain shadow aridity."
                        }
                    }
                ]
            }
        ]
    },

    # Lesson 11: Drawing a Cross-Section / Relief Profile
    {
        "unit_order": 11,
        "unit_name": "Drawing a Cross-Section / Relief Profile",
        "lesson_title": "Drawing a Cross-Section / Relief Profile",
        "pages": [
            {
                "page_number": 1,
                "page_title": "Constructing Cross-Sections",
                "blocks": [
                    {
                        "block_type": "suggested_image",
                        "component_type": "suggested_image",
                        "title": "Topographical Cross-Section and Relief Profile",
                        "content": {"text": "A technical relief profile illustrating the step-by-step projection of contour lines onto a cross-sectional graph."}
                    },
                    {
                        "block_type": "learning_goal",
                        "component_type": "learning_goal",
                        "title": "Lesson Objectives: Cross-Sections",
                        "content": {
                            "text": (
                                "By the end of this lesson, you will be able to:\n\n"
                                "- Draw an accurate topographical cross-section between two given grid coordinates\n"
                                "- Label physical and human features (rivers, hills, roads) on the cross-section\n"
                                "- Calculate Vertical Exaggeration (VE) using `VE = Vertical Scale / Horizontal Scale`\n"
                                "- Determine intervisibility between two points on a cross-section profile"
                            )
                        }
                    }
                ]
            },
            {
                "page_number": 2,
                "page_title": "Step-by-Step Cross-Section Construction",
                "blocks": [
                    {
                        "block_type": "step_process",
                        "component_type": "step_process",
                        "title": "The 6 Steps to Draw a Cross-Section",
                        "content": {
                            "steps": [
                                {"step_number": 1, "title": "Draw Section Line", "description": "Join Point A and Point B on your map with a straight, sharp pencil line."},
                                {"step_number": 2, "title": "Place Paper Strip", "description": "Lay a straight strip of blank paper along line AB and mark points A and B."},
                                {"step_number": 3, "title": "Tick & Label Contours", "description": "Mark every contour line that crosses the paper edge and write its exact height (e.g. 1400, 1420, 1440). Also tick rivers and roads."},
                                {"step_number": 4, "title": "Set Up Graph Axes", "description": "Draw a graph on paper. Horizontal scale equals map scale (1:50,000). Vertical scale is chosen (e.g. 1 cm rep 20 m)."},
                                {"step_number": 5, "title": "Plot Points & Curve", "description": "Transfer the ticked heights onto the graph as points and connect them with a smooth, continuous freehand curve."},
                                {"step_number": 6, "title": "Label Features & VE", "description": "Annotate hills, rivers, and roads with arrows, add a clear title, and calculate Vertical Exaggeration."}
                            ]
                        }
                    },
                    {
                        "block_type": "formula_breakdown",
                        "component_type": "formula_breakdown",
                        "title": "Calculating Vertical Exaggeration (VE)",
                        "content": {
                            "text": (
                                "Vertical Exaggeration measures how much the vertical scale has been enlarged relative to the horizontal scale:\n\n"
                                "$$\\text{Vertical Exaggeration (VE)} = \\frac{\\text{Vertical Scale (VS)}}{\\text{Horizontal Scale (HS)}}$$\n\n"
                                "*Example*: If HS = 1:50,000 and VS = 1 cm rep 20 m (1:2,000):\n"
                                "$$\\text{VE} = \\frac{1/2000}{1/50000} = \\frac{50000}{2000} = 25\\text{ times}$$"
                            )
                        }
                    },
                    {
                        "block_type": "suggested_diagram",
                        "component_type": "suggested_diagram",
                        "title": "Step-by-Step Cross-Section Construction and Intervisibility Guide",
                        "content": {"text": "Vector diagram illustrating the paper strip contour ticking method and the resulting smooth topographic profile graph."}
                    }
                ]
            },
            {
                "page_number": 3,
                "page_title": "Intervisibility Analysis",
                "blocks": [
                    {
                        "block_type": "concept_explanation",
                        "component_type": "concept_explanation",
                        "title": "What is Intervisibility?",
                        "content": {
                            "text": (
                                "Two points are **intervisible** if an observer standing at Point A can see Point B without any intervening high ground (hill, ridge, spur) blocking the line of sight.\n\n"
                                "- To test on a cross-section: Draw a straight pencil line of sight from the top of Point A to Point B. If the terrain profile rises above this line at any point, the features are **NOT intervisible**."
                            )
                        }
                    }
                ]
            },
            {
                "page_number": 4,
                "page_title": "Formative Knowledge Check",
                "blocks": [
                    {
                        "block_type": "knowledge_check",
                        "component_type": "knowledge_check",
                        "title": "Question 1: Vertical Exaggeration Calculation",
                        "content": {
                            "question": "A student constructs a cross-section using a horizontal scale of 1:50,000 and a vertical scale of 1 cm represents 50 meters (1:5,000). What is the Vertical Exaggeration?",
                            "options": [
                                "A. 5 times",
                                "B. 10 times",
                                "C. 50 times",
                                "D. 2.5 times"
                            ],
                            "correct_answer": "B",
                            "explanation": "VE = HS denominator / VS denominator = 50,000 / 5,000 = 10 times."
                        }
                    }
                ]
            }
        ]
    },

    # Lesson 12: Resource Suitability Analysis and Route Selection
    {
        "unit_order": 12,
        "unit_name": "Resource Suitability Analysis and Route Selection",
        "lesson_title": "Resource Suitability Analysis and Route Selection",
        "pages": [
            {
                "page_number": 1,
                "page_title": "Spatial Route & Site Planning",
                "blocks": [
                    {
                        "block_type": "suggested_image",
                        "component_type": "suggested_image",
                        "title": "Mountain Highway Route Planning Across Alpine Passes",
                        "content": {"text": "A mountain highway navigating winding terrain along gentle slope contours, avoiding steep cliffs and marshy river valleys."}
                    },
                    {
                        "block_type": "learning_goal",
                        "component_type": "learning_goal",
                        "title": "Lesson Objectives: Site & Route Suitability",
                        "content": {
                            "text": (
                                "By the end of this lesson, you will be able to:\n\n"
                                "- Select optimal alignment routes for roads, railways, and pipelines on a topographical map\n"
                                "- Evaluate site suitability for human settlements, schools, coffee/tea factories, and airstrips\n"
                                "- Apply slope gradient, drainage stability, and environmental constraint criteria"
                            )
                        }
                    }
                ]
            },
            {
                "page_number": 2,
                "page_title": "Cartographic Criteria for Route & Site Selection",
                "blocks": [
                    {
                        "block_type": "comparison_table",
                        "component_type": "comparison_table",
                        "title": "Site Selection Decision Matrix",
                        "content": {
                            "headers": ["Project / Feature", "Optimal Terrain & Relief", "Essential Environmental Factors to Avoid"],
                            "rows": [
                                ["Road / Highway Route", "Gentle, uniform slopes following contour valleys or mountain passes", "Steep cliffs (landslides), marshy swamps, wide river crossings"],
                                ["Airstrip / Airport", "Broad, flat plain with widely spaced contours", "High hills along flight paths, foggy river valleys, marshy ground"],
                                ["Tea / Coffee Processing Factory", "Gentle slope near raw crop plantations", "Steep escarpments lacking road access; near reliable water supply"],
                                ["Residential Settlement", "Gentle, well-drained sunny ridge or terrace", "Flood-prone river floodplains, poorly drained papyrus swamps"]
                            ]
                        }
                    },
                    {
                        "block_type": "suggested_diagram",
                        "component_type": "suggested_diagram",
                        "title": "Route Alignment and Site Suitability Decision Matrix",
                        "content": {"text": "Vector diagram illustrating how engineers choose optimal highway alignments along contour valleys while avoiding cliffs, swamps, and floodplains."}
                    }
                ]
            },
            {
                "page_number": 3,
                "page_title": "Formative Knowledge Check",
                "blocks": [
                    {
                        "block_type": "knowledge_check",
                        "component_type": "knowledge_check",
                        "title": "Question 1: Selecting an Airstrip Site",
                        "content": {
                            "question": "Which combination of terrain characteristics on a topographical map is most suitable for locating an airstrip?",
                            "options": [
                                "A. A narrow mountain gorge with closely packed contours",
                                "B. A broad, flat plain with widely spaced contours and clear approach lines free of high hills",
                                "C. A permanent papyrus swamp adjacent to a lake",
                                "D. A steep volcanic cone"
                            ],
                            "correct_answer": "B",
                            "explanation": "Airstrips require flat, well-drained terrain with minimal gradient and unobstructed flight approach corridors free of surrounding high hills."
                        }
                    }
                ]
            }
        ]
    },

    # Lesson 13: Map Skills Assessment and Error Correction
    {
        "unit_order": 13,
        "unit_name": "Map Skills Assessment and Error Correction",
        "lesson_title": "Map Skills Assessment and Error Correction",
        "pages": [
            {
                "page_number": 1,
                "page_title": "Comprehensive Topic Review",
                "blocks": [
                    {
                        "block_type": "suggested_image",
                        "component_type": "suggested_image",
                        "title": "Cartographic Analysis and Survey Examination",
                        "content": {"text": "A student geographer analyzing a topographical map with dividers, protractor, and magnifier for integrated examination questions."}
                    },
                    {
                        "block_type": "learning_goal",
                        "component_type": "learning_goal",
                        "title": "Topic 2 Final Mastery Goals",
                        "content": {
                            "text": (
                                "By completing this review, you will:\n\n"
                                "- Review the complete toolkit: Marginal info, Bearings, Scales, Grid references, Relief, Contours, Drainage, Vegetation, Cross-sections, and Route planning\n"
                                "- Avoid standard KCSE map-work errors\n"
                                "- Complete the summative examination checkpoint with at least 80% accuracy"
                            )
                        }
                    }
                ]
            },
            {
                "page_number": 2,
                "page_title": "The Master Map Interpretation Checklist",
                "blocks": [
                    {
                        "block_type": "step_process",
                        "component_type": "step_process",
                        "title": "Step-by-Step Map Exam Protocol",
                        "content": {
                            "steps": [
                                {"step_number": 1, "title": "Check Marginal Information First", "description": "Always confirm the sheet name, series number, RF scale (e.g. 1:50,000), and vertical interval (20m)."},
                                {"step_number": 2, "title": "Orient Grid Coordinates", "description": "Read Eastings first (X-axis) then Northings (Y-axis). Double-check whether 4-figure or 6-figure is required."},
                                {"step_number": 3, "title": "Protractor Alignment", "description": "Ensure protractor is centered on the 'from' point and measured clockwise from 000° Grid North."},
                                {"step_number": 4, "title": "Scale Unit Conversions", "description": "State distance answers in the requested units (kilometers or meters). 1 cm on 1:50,000 = 0.5 km = 500 m."},
                                {"step_number": 5, "title": "Cross-Section Accuracy", "description": "Use a fresh paper strip, mark every contour, plot smooth curves, and calculate VE using identical units."}
                            ]
                        }
                    },
                    {
                        "block_type": "suggested_diagram",
                        "component_type": "suggested_diagram",
                        "title": "Map Work Mastery Summary Diagram",
                        "content": {"text": "Vector diagram summarizing the complete map-reading workflow from marginal decoding to 3D relief synthesis."}
                    }
                ]
            },
            {
                "page_number": 3,
                "page_title": "Summative Examination Checkpoint",
                "blocks": [
                    {
                        "block_type": "knowledge_check",
                        "component_type": "knowledge_check",
                        "title": "Checkpoint Question 1: Reciprocal Bearing",
                        "content": {
                            "question": "If the forward grid bearing from a market to a church is 245°, what is the bearing of the market from the church?",
                            "options": [
                                "A. 425°",
                                "B. 065°",
                                "C. 115°",
                                "D. 245°"
                            ],
                            "correct_answer": "B",
                            "explanation": "Because 245° is greater than 180°, subtract 180°: 245° - 180° = 065°."
                        }
                    },
                    {
                        "block_type": "knowledge_check",
                        "component_type": "knowledge_check",
                        "title": "Checkpoint Question 2: Drainage Recognition",
                        "content": {
                            "question": "A river network shows tributaries joining the main stream at sharp 90-degree right angles in a folded valley. Which drainage pattern is this?",
                            "options": [
                                "A. Radial",
                                "B. Trellis",
                                "C. Centripetal",
                                "D. Dendritic"
                            ],
                            "correct_answer": "B",
                            "explanation": "Trellis drainage is characterized by right-angled tributary confluences formed in folded or faulted rock strata."
                        }
                    },
                    {
                        "block_type": "knowledge_check",
                        "component_type": "knowledge_check",
                        "title": "Checkpoint Question 3: 6-Figure Grid Precision",
                        "content": {
                            "question": "A trigonometrical station is located in grid square 6789, exactly 8 tenths east and 2 tenths north. What is its 6-figure grid reference?",
                            "options": [
                                "A. 892678",
                                "B. 678892",
                                "C. 672898",
                                "D. 898672"
                            ],
                            "correct_answer": "B",
                            "explanation": "Eastings first (67 + 8 = 678) followed by Northings (89 + 2 = 892) gives 678892."
                        }
                    }
                ]
            }
        ]
    }
]

def ingest_topic_2():
    print("=== Starting Ingestion for Grade 10 Geography — Topic 2: Map Reading and Interpretation ===")
    
    cbc = Curriculum.objects.filter(name__iexact="CBC").first()
    grade10 = Grade.objects.filter(curriculum=cbc, name__icontains="10").first()
    subject = Subject.objects.filter(grade=grade10, name="Geography").first()
    
    with transaction.atomic():
        topic, _ = Topic.objects.get_or_create(
            subject=subject,
            order=2,
            defaults={"name": "Map Reading and Interpretation", "description": "Topographical map analysis, scales, bearings, grid references, relief, drainage, vegetation, cross-sections, and site selection."}
        )
        topic.name = "Map Reading and Interpretation"
        topic.description = "Topographical map analysis, scales, bearings, grid references, relief, drainage, vegetation, cross-sections, and site selection."
        topic.save()
        print(f"Topic configured: {topic.name} (ID: {topic.id})")

        total_blocks_created = 0

        for lesson_data in LESSONS_DATA:
            u_order = lesson_data["unit_order"]
            u_name = lesson_data["unit_name"]
            l_title = lesson_data["lesson_title"]

            unit, _ = LearningUnit.objects.get_or_create(
                topic=topic,
                order=u_order,
                defaults={"name": u_name, "description": f"Learning unit for {u_name}"}
            )
            unit.name = u_name
            unit.save()

            lesson, _ = Lesson.objects.get_or_create(
                topic=topic,
                learning_unit=unit,
                defaults={"title": l_title, "status": "published", "version": 1}
            )
            lesson.title = l_title
            lesson.status = "published"
            lesson.version = 1
            lesson.save()

            # Clean existing blocks for idempotent ingestion
            lesson.blocks.all().delete()

            block_seq = 1
            for page in lesson_data["pages"]:
                p_num = page["page_number"]
                p_title = page["page_title"]

                for c_order, block_dict in enumerate(page["blocks"], start=1):
                    cleaned_content = clean_content_dict(block_dict.get("content", {}))
                    LessonBlock.objects.create(
                        lesson=lesson,
                        block_type=block_dict["block_type"],
                        component_type=block_dict.get("component_type", block_dict["block_type"]),
                        title=clean_text(block_dict.get("title", "")),
                        content=cleaned_content,
                        page_number=p_num,
                        page_title=p_title,
                        order=block_seq,
                        component_order=c_order
                    )
                    block_seq += 1
                    total_blocks_created += 1

            print(f"  Ingested Unit {u_order}: {u_name} ({len(lesson_data['pages'])} pages, {block_seq-1} blocks)")

        print(f"\nSuccessfully ingested Topic 2: 13 Lessons, {total_blocks_created} Blocks.")

if __name__ == "__main__":
    ingest_topic_2()
