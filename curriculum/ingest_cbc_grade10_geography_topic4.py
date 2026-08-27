"""
VLearn CBC Grade 10 Geography — Topic 4: Geographic Information System (GIS)
Direct Programmatic Source-Driven Ingestion Engine

Subject: Geography (Grade 10 CBC, Subject ID: 37)
Topic 4: Geographic Information System (GIS)
Source: Grade 10 Geography/04_geographic_information_system.md

Usage:
  ./venv/bin/python curriculum/ingest_cbc_grade10_geography_topic4.py
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
    """Remove citation brackets ([1], [48], [S1, p. 1]) and normalize whitespace."""
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
# TOPIC 4 LESSON DEFINITIONS (13 LESSONS)
# =============================================================================
LESSONS_DATA = [
    # Lesson 1: Introduction to Geospatial Technologies
    {
        "unit_order": 1,
        "unit_name": "Introduction to Geospatial Technologies",
        "lesson_title": "Introduction to Geospatial Technologies",
        "pages": [
            {
                "page_number": 1,
                "page_title": "Geospatial Revolution & Learning Goals",
                "blocks": [
                    {
                        "block_type": "suggested_image",
                        "component_type": "suggested_image",
                        "title": "Satellite Earth Observation and Geospatial Technologies",
                        "content": {"text": "An Earth observation satellite orbiting high above the planet capturing continuous geospatial data of terrain, oceans, and atmospheric conditions."}
                    },
                    {
                        "block_type": "learning_goal",
                        "component_type": "learning_goal",
                        "title": "Lesson Objectives: Geospatial Technologies",
                        "content": {
                            "text": (
                                "By the end of this lesson, you will be able to:\n\n"
                                "- Explain GIS, GPS, and Remote Sensing (RS) as modern geospatial technologies\n"
                                "- Compare the different spatial questions each technology is designed to answer\n"
                                "- Trace how Remote Sensing, GPS, and GIS connect into an integrated spatial pipeline"
                            )
                        }
                    },
                    {
                        "block_type": "concept_explanation",
                        "component_type": "concept_explanation",
                        "title": "Prerequisite Spark: Everyday Spatial Tech",
                        "content": {
                            "text": (
                                "When you open Google Maps on a smartphone to find the fastest route to a shop or school, "
                                "you are using three distinct spatial technologies working together in harmony:\n\n"
                                "1. Satellite sensors capturing aerial photographs from space (Remote Sensing).\n"
                                "2. Orbiting satellite constellations pinpointing your phone's blue dot (GPS).\n"
                                "3. Computer software overlaying your dot onto roads and calculating route traffic (GIS)."
                            )
                        }
                    }
                ]
            },
            {
                "page_number": 2,
                "page_title": "Core Definitions: The Geospatial Trio",
                "blocks": [
                    {
                        "block_type": "definition_card",
                        "component_type": "definition_card",
                        "title": "Essential Geospatial Definitions",
                        "content": {
                            "definitions": [
                                {
                                    "term": "Geographic Information System (GIS)",
                                    "definition": "A computer-based technology used to capture, store, analyze, manage, and display geographically referenced data.",
                                    "simple": "The computational brain that organizes, layers, and solves spatial problems on a digital map."
                                },
                                {
                                    "term": "Global Positioning System (GPS)",
                                    "definition": "A satellite-based navigation system that provides precise location coordinates (latitude, longitude, and altitude) anywhere on Earth.",
                                    "simple": "A space-based positioning tool that answers: 'Where exactly am I right now?'"
                                },
                                {
                                    "term": "Remote Sensing (RS)",
                                    "definition": "The process of collecting data and capturing images of the Earth's surface from a distance, typically using sensors mounted on satellites, airplanes, or drones.",
                                    "simple": "Taking high-tech photos and measurements from high above without touching the ground."
                                }
                            ]
                        }
                    }
                ]
            },
            {
                "page_number": 3,
                "page_title": "The Spatial Workflow Pipeline",
                "blocks": [
                    {
                        "block_type": "diagram",
                        "component_type": "diagram",
                        "title": "The Three-Stage Geospatial Pipeline",
                        "content": {
                            "caption": "Workflow connecting Remote Sensing (Observation), GPS (Location Coordinates), and GIS (Integration & Spatial Decision-Making)."
                        }
                    },
                    {
                        "block_type": "concept_explanation",
                        "component_type": "concept_explanation",
                        "title": "Case Study: Managing Flood Disasters in Kisumu",
                        "content": {
                            "text": (
                                "Consider how Kenyan emergency agencies coordinate disaster management during floods:\n\n"
                                "- **Stage 1: Observation (Remote Sensing)**: A satellite photographs developing floodwaters spreading across lowlands in Kisumu County.\n"
                                "- **Stage 2: Location (GPS)**: Ground emergency teams use handheld GPS devices to record precise coordinates of marooned homesteads and damaged bridges.\n"
                                "- **Stage 3: Analysis (GIS)**: GIS software combines the satellite flood image, GPS victim coordinates, and road elevation layers to plot the safest, fastest evacuation routes."
                            )
                        }
                    }
                ]
            },
            {
                "page_number": 4,
                "page_title": "Check Your Understanding",
                "blocks": [
                    {
                        "block_type": "multiple_choice_question",
                        "component_type": "multiple_choice_question",
                        "title": "Formative Assessment: Deforestation Monitoring",
                        "content": {
                            "question": "Which geospatial technology is best suited for taking real-time aerial photographs of deforestation in the Mau Forest?",
                            "options": [
                                "Geographic Information System (GIS)",
                                "Global Positioning System (GPS)",
                                "Remote Sensing (RS)",
                                "Statistical frequency tables"
                            ],
                            "correct_answer": "Remote Sensing (RS)",
                            "explanation": "Remote Sensing captures physical and visual data from a distance using sensors on satellites, airplanes, or drones."
                        }
                    },
                    {
                        "block_type": "multiple_choice_question",
                        "component_type": "multiple_choice_question",
                        "title": "Formative Assessment: Core Function of GIS",
                        "content": {
                            "question": "What is the primary role of a Geographic Information System (GIS)?",
                            "options": [
                                "To transmit radio signals from space to ground receivers",
                                "To capture, store, analyze, manage, and display spatial data to support decision-making",
                                "To calculate the exact time it takes for a signal to travel to space",
                                "To replace all paper maps in schools"
                            ],
                            "correct_answer": "To capture, store, analyze, manage, and display spatial data to support decision-making",
                            "explanation": "GIS acts as the integrative computing platform that synthesizes imagery, coordinates, and database attributes into actionable models."
                        }
                    }
                ]
            }
        ]
    },

    # Lesson 2: Core Concepts of GIS: Spatial vs. Attribute Data and Layers
    {
        "unit_order": 2,
        "unit_name": "Core Concepts of GIS: Spatial vs. Attribute Data and Layers",
        "lesson_title": "Core Concepts of GIS: Spatial vs. Attribute Data and Layers",
        "pages": [
            {
                "page_number": 1,
                "page_title": "Introduction to Spatial vs. Attribute Data",
                "blocks": [
                    {
                        "block_type": "suggested_image",
                        "component_type": "suggested_image",
                        "title": "Thematic GIS Map Overlay and Layer Stacking",
                        "content": {"text": "A multi-layered thematic map displaying overlapping spatial layers of terrain, hydrology, and crop cover."}
                    },
                    {
                        "block_type": "learning_goal",
                        "component_type": "learning_goal",
                        "title": "Lesson Objectives: Data Types & Layers",
                        "content": {
                            "text": (
                                "By the end of this lesson, you will be able to:\n\n"
                                "- Distinguish between spatial data and attribute data in GIS\n"
                                "- Classify vector geographic features into points, lines, and polygons\n"
                                "- Explain how layers are geo-referenced and stacked to create comprehensive digital maps"
                            )
                        }
                    },
                    {
                        "block_type": "concept_explanation",
                        "component_type": "concept_explanation",
                        "title": "Prerequisite Spark: The Transparent Overlay Sheet Analogy",
                        "content": {
                            "text": (
                                "Imagine drawing three separate maps on clear, transparent plastic sheets:\n"
                                "- Sheet 1: Rivers and streams only\n"
                                "- Sheet 2: Road networks and railways only\n"
                                "- Sheet 3: Towns and market centres only\n\n"
                                "When you stack these transparent sheets on top of each other, an integrated map appears! "
                                "This is the foundational logic behind GIS layers."
                            )
                        }
                    }
                ]
            },
            {
                "page_number": 2,
                "page_title": "Spatial Data vs Attribute Data",
                "blocks": [
                    {
                        "block_type": "definition_card",
                        "component_type": "definition_card",
                        "title": "Key Terminology: Spatial vs Attribute",
                        "content": {
                            "definitions": [
                                {
                                    "term": "Spatial Data",
                                    "definition": "Numerical information representing the exact geographical location and geometric shape of a feature on Earth's surface (e.g. coordinates, boundaries).",
                                    "simple": "The 'Where' of a feature: coordinates, points, lines, and shapes."
                                },
                                {
                                    "term": "Attribute Data",
                                    "definition": "Descriptive, non-spatial characteristics and tabular properties linked to a geographical feature.",
                                    "simple": "The 'What' of a feature: names, depths, population numbers, and road conditions."
                                },
                                {
                                    "term": "Layer (GIS)",
                                    "definition": "A digital overlay containing geographic features of a single theme or dataset, perfectly geo-referenced to a common coordinate system.",
                                    "simple": "A separate thematic map layer (e.g. Soils, Roads, Rivers) stacked in a digital map."
                                }
                            ]
                        }
                    },
                    {
                        "block_type": "concept_explanation",
                        "component_type": "concept_explanation",
                        "title": "Vector Geometry: Points, Lines, and Polygons",
                        "content": {
                            "text": (
                                "In vector GIS, all real-world objects are modeled as one of three geometric primitives:\n\n"
                                "- **Points (0D)**: Single (X, Y) coordinate pairs representing discrete, small features (e.g. boreholes, weather stations, school gates, mountain peaks).\n"
                                "- **Lines / Polylines (1D)**: Connected ordered sequences of coordinate vertices representing linear networks (e.g. rivers, paved roads, transmission lines, railway tracks).\n"
                                "- **Polygons (2D)**: Closed contiguous boundaries enclosing an area representing regional continuous zones (e.g. national parks, lakes, administrative counties, farm parcels)."
                            )
                        }
                    }
                ]
            },
            {
                "page_number": 3,
                "page_title": "The Layer Stacking Model",
                "blocks": [
                    {
                        "block_type": "diagram",
                        "component_type": "diagram",
                        "title": "Exploded 3D GIS Layer Stack",
                        "content": {
                            "caption": "Vertical alignment of Points (schools/wells), Lines (rivers/roads), Polygons (land parcels), and Base Imagery (satellite raster)."
                        }
                    },
                    {
                        "block_type": "concept_explanation",
                        "component_type": "concept_explanation",
                        "title": "Spatial Alignment Through Shared Coordinates",
                        "content": {
                            "text": (
                                "Why don't layers get mixed up when stacked? Because every layer is **geo-referenced** to the exact same "
                                "spatial coordinate system (e.g. UTM or WGS84).\n\n"
                                "When layers align, GIS can perform powerful relational queries like: *'Which health clinics (points) "
                                "are located within 500 metres of a paved highway (line) on fertile volcanic soil (polygon)?'*"
                            )
                        }
                    }
                ]
            },
            {
                "page_number": 4,
                "page_title": "Check Your Understanding",
                "blocks": [
                    {
                        "block_type": "multiple_choice_question",
                        "component_type": "multiple_choice_question",
                        "title": "Formative Assessment: Data Classification",
                        "content": {
                            "question": "In a school GIS project, the location of a water tap is recorded as coordinates (-1.285, 36.821), while its operational state is listed as 'Functional'. How are these categorized?",
                            "options": [
                                "Both are spatial data",
                                "Both are attribute data",
                                "The coordinates are spatial data; the functional status is attribute data",
                                "The coordinates are attribute data; the functional status is spatial data"
                            ],
                            "correct_answer": "The coordinates are spatial data; the functional status is attribute data",
                            "explanation": "Coordinates locate the point in physical space (spatial), whereas condition descriptions are stored in tabular databases (attribute)."
                        }
                    },
                    {
                        "block_type": "multiple_choice_question",
                        "component_type": "multiple_choice_question",
                        "title": "Formative Assessment: Vector Shape Selection",
                        "content": {
                            "question": "Which vector shape is most appropriate for representing the Athi River on a 1:50,000 scale GIS map?",
                            "options": [
                                "Point",
                                "Line",
                                "Polygon",
                                "Raster pixel"
                            ],
                            "correct_answer": "Line",
                            "explanation": "Rivers are continuous, linear natural features best represented as connected vector lines."
                        }
                    }
                ]
            }
        ]
    },

    # Lesson 3: Components of GIS
    {
        "unit_order": 3,
        "unit_name": "Components of GIS",
        "lesson_title": "Components of GIS",
        "pages": [
            {
                "page_number": 1,
                "page_title": "The GIS System Architecture",
                "blocks": [
                    {
                        "block_type": "suggested_image",
                        "component_type": "suggested_image",
                        "title": "Modern GIS Workstation and Computer Laboratory",
                        "content": {"text": "A specialized GIS computing workstation equipped with high-resolution monitors, analysis software, and spatial database interfaces."}
                    },
                    {
                        "block_type": "learning_goal",
                        "component_type": "learning_goal",
                        "title": "Lesson Objectives: Five Components of GIS",
                        "content": {
                            "text": (
                                "By the end of this lesson, you will be able to:\n\n"
                                "- Describe the five essential interacting components of a Geographic Information System\n"
                                "- Explain the role of Hardware, Software, Data, People, and Methods\n"
                                "- Evaluate why GIS is an integrated socio-technical framework rather than just computer software"
                            )
                        }
                    },
                    {
                        "block_type": "concept_explanation",
                        "component_type": "concept_explanation",
                        "title": "Prerequisite Spark: Software is Not Enough",
                        "content": {
                            "text": (
                                "If an organization purchases expensive GIS mapping software but has no field coordinates, "
                                "no high-performance computers to process satellite images, and no staff trained in spatial modeling, "
                                "can they create a map or make a spatial decision? "
                                "A GIS requires five tightly linked components to function."
                            )
                        }
                    }
                ]
            },
            {
                "page_number": 2,
                "page_title": "The Five Essential GIS Components",
                "blocks": [
                    {
                        "block_type": "diagram",
                        "component_type": "diagram",
                        "title": "The Five Interacting Components of GIS",
                        "content": {
                            "caption": "Hardware, Software, Data, People, and Methods interacting to form a functional Geographic Information System."
                        }
                    },
                    {
                        "block_type": "concept_explanation",
                        "component_type": "concept_explanation",
                        "title": "Component Breakdown",
                        "content": {
                            "text": (
                                "1. **Hardware**: Physical computing infrastructure, including multicore CPUs, GPUs, high-resolution screens, GPS receivers, digitizing tablets, and cloud storage servers.\n\n"
                                "2. **Software**: Programs providing tools to capture, store, query, analyze, and display spatial data (e.g. QGIS, ArcGIS Pro, Google Earth Engine, PostGIS).\n\n"
                                "3. **Data**: The core fuel of GIS, combining geo-referenced spatial coordinates/imagery and rich tabular attribute datasets.\n\n"
                                "4. **People**: Trained spatial professionals (GIS analysts, cartographers, urban planners, surveyors) and end users who design models, query data, and interpret results.\n\n"
                                "5. **Methods**: Standardized procedures, mathematical algorithms, spatial analysis models, and institutional workflows used to solve real-world problems."
                            )
                        }
                    }
                ]
            },
            {
                "page_number": 3,
                "page_title": "Check Your Understanding",
                "blocks": [
                    {
                        "block_type": "multiple_choice_question",
                        "component_type": "multiple_choice_question",
                        "title": "Formative Assessment: GIS Components Role",
                        "content": {
                            "question": "Which component of GIS represents the specialized algorithms used to calculate the shortest emergency delivery route in Nairobi?",
                            "options": [
                                "Hardware",
                                "Software",
                                "Methods",
                                "People"
                            ],
                            "correct_answer": "Methods",
                            "explanation": "Methods encompass the mathematical procedures, spatial algorithms, rules, and workflows applied to solve geographic problems."
                        }
                    },
                    {
                        "block_type": "multiple_choice_question",
                        "component_type": "multiple_choice_question",
                        "title": "Formative Assessment: Why People Matter",
                        "content": {
                            "question": "Why are 'People' considered a critical component of a Geographic Information System?",
                            "options": [
                                "Because computers cannot run without manual hand-cranking",
                                "Because trained professionals must design, manage, analyze, and geographically interpret the results of a GIS model",
                                "Because people represent spatial points on a map",
                                "Because people are the main source of hardware failures"
                            ],
                            "correct_answer": "Because trained professionals must design, manage, analyze, and geographically interpret the results of a GIS model",
                            "explanation": "Even the most advanced software and hardware cannot generate value without skilled analysts to formulate queries and make informed spatial decisions."
                        }
                    }
                ]
            }
        ]
    },

    # Lesson 4: Geographical Coordinates and Geo-Referencing
    {
        "unit_order": 4,
        "unit_name": "Geographical Coordinates and Geo-Referencing",
        "lesson_title": "Geographical Coordinates and Geo-Referencing",
        "pages": [
            {
                "page_number": 1,
                "page_title": "The Global Coordinate Grid",
                "blocks": [
                    {
                        "block_type": "suggested_image",
                        "component_type": "suggested_image",
                        "title": "Global Coordinate Grid of Latitude and Longitude",
                        "content": {"text": "A three-dimensional globe showing the graticule of parallels of latitude and meridians of longitude intersecting across the continents."}
                    },
                    {
                        "block_type": "learning_goal",
                        "component_type": "learning_goal",
                        "title": "Lesson Objectives: Coordinates & Geo-Referencing",
                        "content": {
                            "text": (
                                "By the end of this lesson, you will be able to:\n\n"
                                "- Explain the angular concepts of latitude and longitude on the Earth's sphere\n"
                                "- Understand how the global graticule creates unique coordinate addresses\n"
                                "- Analyze the importance of geo-referencing in pinning scanned maps to the Earth's surface"
                            )
                        }
                    },
                    {
                        "block_type": "video",
                        "component_type": "video",
                        "title": "Visualizing Latitude and Longitude Grids",
                        "content": {
                            "url": "https://www.youtube.com/watch?v=swKBi6hHHMA",
                            "caption": "Educational 3D demonstration of the Equator, Prime Meridian, and intersecting latitude/longitude coordinate lines."
                        }
                    }
                ]
            },
            {
                "page_number": 2,
                "page_title": "Latitude, Longitude & Geo-Referencing",
                "blocks": [
                    {
                        "block_type": "definition_card",
                        "component_type": "definition_card",
                        "title": "Coordinate Grid Definitions",
                        "content": {
                            "definitions": [
                                {
                                    "term": "Latitude (Parallels)",
                                    "definition": "Horizontal angular distance measured in degrees north or south of the Equator (0° at Equator to 90° N/S at the Poles).",
                                    "simple": "Horizontal grid lines measuring distance north or south."
                                },
                                {
                                    "term": "Longitude (Meridians)",
                                    "definition": "Vertical angular distance measured in degrees east or west of the Prime Meridian (0° at Greenwich to 180° E/W).",
                                    "simple": "Vertical grid lines measuring distance east or west."
                                },
                                {
                                    "term": "Geo-referencing",
                                    "definition": "The process of assigning real-world geographic coordinates (latitude/longitude or projected UTM) to digital raster images or scanned paper maps.",
                                    "simple": "Anchoring an image to its true physical location on the globe."
                                }
                            ]
                        }
                    },
                    {
                        "block_type": "diagram",
                        "component_type": "diagram",
                        "title": "Global Graticule: Latitude and Longitude Angles",
                        "content": {
                            "caption": "Diagram illustrating the Equator, Prime Meridian, Parallels of Latitude, and Meridians of Longitude."
                        }
                    }
                ]
            },
            {
                "page_number": 3,
                "page_title": "Why Geo-Referencing is Essential",
                "blocks": [
                    {
                        "block_type": "concept_explanation",
                        "component_type": "concept_explanation",
                        "title": "Transforming Raw Pixels into Geographic Data",
                        "content": {
                            "text": (
                                "When you scan an old paper map or take an aerial photo with a drone, the computer initially sees "
                                "only raw image pixels (rows and columns) with no spatial awareness.\n\n"
                                "To make it useful in GIS:\n"
                                "1. You identify **Ground Control Points (GCPs)**—clear landmarks like road junctions, bridges, or survey pillars.\n"
                                "2. You link those pixel locations to their true GPS coordinates.\n"
                                "3. The GIS warps and stretches the image mathematically so that every single pixel matches its true physical spot on Earth."
                            )
                        }
                    }
                ]
            },
            {
                "page_number": 4,
                "page_title": "Check Your Understanding",
                "blocks": [
                    {
                        "block_type": "multiple_choice_question",
                        "component_type": "multiple_choice_question",
                        "title": "Formative Assessment: Geo-Referencing Concept",
                        "content": {
                            "question": "What is the primary objective of 'geo-referencing' a scanned map?",
                            "options": [
                                "The process of giving a map a colorful decorative border",
                                "Assigning real-world spatial coordinates (latitude and longitude) to map features or scanned images",
                                "Translating map labels into multiple languages",
                                "Converting vector shapes into a statistical bar graph"
                            ],
                            "correct_answer": "Assigning real-world spatial coordinates (latitude and longitude) to map features or scanned images",
                            "explanation": "Geo-referencing pins an image or dataset to real ground locations so it aligns with other spatial layers."
                        }
                    },
                    {
                        "block_type": "multiple_choice_question",
                        "component_type": "multiple_choice_question",
                        "title": "Formative Assessment: Reference Latitude",
                        "content": {
                            "question": "Which line of latitude divides the Earth into Northern and Southern Hemispheres?",
                            "options": [
                                "Prime Meridian",
                                "Greenwich Meridian",
                                "The Equator (0°)",
                                "Tropic of Capricorn"
                            ],
                            "correct_answer": "The Equator (0°)",
                            "explanation": "The Equator (0° latitude) is the central parallel dividing the globe into Northern and Southern Hemispheres."
                        }
                    }
                ]
            }
        ]
    },

    # Lesson 5: Coordinate Conversion: Decimal Degrees to DMS
    {
        "unit_order": 5,
        "unit_name": "Coordinate Conversion: Decimal Degrees to DMS",
        "lesson_title": "Coordinate Conversion: Decimal Degrees to DMS",
        "pages": [
            {
                "page_number": 1,
                "page_title": "Coordinate Systems & Units",
                "blocks": [
                    {
                        "block_type": "suggested_image",
                        "component_type": "suggested_image",
                        "title": "GPS Digital Screen Displaying Coordinates",
                        "content": {"text": "A digital navigation screen showing exact numerical coordinates in degrees, minutes, and decimal notation."}
                    },
                    {
                        "block_type": "learning_goal",
                        "component_type": "learning_goal",
                        "title": "Lesson Objectives: Coordinate Math",
                        "content": {
                            "text": (
                                "By the end of this lesson, you will be able to:\n\n"
                                "- Convert coordinates from Decimal Degrees (DD) to Degrees, Minutes, Seconds (DMS)\n"
                                "- Convert coordinates from DMS format back to Decimal Degrees (DD) with mathematical precision\n"
                                "- Apply the base-60 sexagesimal subdivision rules to spatial coordinates"
                            )
                        }
                    },
                    {
                        "block_type": "concept_explanation",
                        "component_type": "concept_explanation",
                        "title": "The Sexagesimal System (Base-60)",
                        "content": {
                            "text": (
                                "Geographical coordinates use the base-60 system just like time:\n\n"
                                "- **1 Degree (°)** = 60 Minutes (′)\n"
                                "- **1 Minute (′)** = 60 Seconds (″)\n"
                                "- **1 Degree (°)** = 3,600 Seconds (″)\n\n"
                                "GPS devices often output Decimal Degrees (DD, e.g. 36.8245°), while traditional topographical maps use Degrees, Minutes, Seconds (DMS, e.g. 36° 49′ 28.2″)."
                            )
                        }
                    }
                ]
            },
            {
                "page_number": 2,
                "page_title": "Converting Decimal Degrees (DD) to DMS",
                "blocks": [
                    {
                        "block_type": "diagram",
                        "component_type": "diagram",
                        "title": "Coordinate Conversion Workflow: Decimal Degrees to DMS",
                        "content": {
                            "caption": "Mathematical pipeline: Base-60 integer extraction for Degrees, Minutes (*60), and Seconds (*60)."
                        }
                    },
                    {
                        "block_type": "concept_explanation",
                        "component_type": "concept_explanation",
                        "title": "Step-by-Step Conversion: DD to DMS",
                        "content": {
                            "text": (
                                "To convert **36.8245°** to DMS:\n\n"
                                "1. **Whole Degrees**: Keep the whole integer part -> **36°**\n"
                                "2. **Calculate Minutes**: Take decimal part $0.8245$ and multiply by 60:\n"
                                "   $$0.8245 \\times 60 = 49.47'$$\n"
                                "   Keep the whole number -> **49'**\n"
                                "3. **Calculate Seconds**: Take remaining decimal $0.47$ and multiply by 60:\n"
                                "   $$0.47 \\times 60 = 28.2''$$\n"
                                "   Keep the seconds -> **28.2''**\n\n"
                                "**Final DMS Coordinate**: **36° 49' 28.2'' E**"
                            )
                        }
                    }
                ]
            },
            {
                "page_number": 3,
                "page_title": "Converting DMS to Decimal Degrees (DD)",
                "blocks": [
                    {
                        "block_type": "concept_explanation",
                        "component_type": "concept_explanation",
                        "title": "Step-by-Step Conversion: DMS to DD",
                        "content": {
                            "text": (
                                "Formula:\n"
                                "$$\\text{Decimal Degrees (DD)} = \\text{Degrees} + \\frac{\\text{Minutes}}{60} + \\frac{\\text{Seconds}}{3600}$$\n\n"
                                "Let's convert **1° 15' 36'' S** into Decimal Degrees:\n\n"
                                "1. Divide minutes: $\\frac{15}{60} = 0.25$\n"
                                "2. Divide seconds: $\\frac{36}{3600} = 0.01$\n"
                                "3. Sum together: $1 + 0.25 + 0.01 = 1.26^\\circ$\n\n"
                                "**Final Decimal Coordinate**: **1.26° S** (or $-1.26^\\circ$ in GIS software)"
                            )
                        }
                    }
                ]
            },
            {
                "page_number": 4,
                "page_title": "Check Your Understanding",
                "blocks": [
                    {
                        "block_type": "multiple_choice_question",
                        "component_type": "multiple_choice_question",
                        "title": "Formative Assessment: Decimal Minutes Calculation",
                        "content": {
                            "question": "Convert 0.45 degrees into minutes of arc.",
                            "options": [
                                "4.5 minutes",
                                "45 minutes",
                                "27 minutes",
                                "30 minutes"
                            ],
                            "correct_answer": "27 minutes",
                            "explanation": "Multiply the decimal degree fraction by 60: 0.45 * 60 = 27 minutes."
                        }
                    },
                    {
                        "block_type": "multiple_choice_question",
                        "component_type": "multiple_choice_question",
                        "title": "Formative Assessment: DMS to DD Calculation",
                        "content": {
                            "question": "Convert 1° 30' into Decimal Degrees (DD).",
                            "options": [
                                "1.30°",
                                "1.50°",
                                "1.75°",
                                "1.05°"
                            ],
                            "correct_answer": "1.50°",
                            "explanation": "30 minutes equals 30/60 = 0.5 degrees. Adding 1 whole degree gives 1.50°."
                        }
                    }
                ]
            }
        ]
    },

    # Lesson 6: Global Positioning System (GPS) in Practice
    {
        "unit_order": 6,
        "unit_name": "Global Positioning System (GPS) in Practice",
        "lesson_title": "Global Positioning System (GPS) in Practice",
        "pages": [
            {
                "page_number": 1,
                "page_title": "Satellite Positioning Principles",
                "blocks": [
                    {
                        "block_type": "suggested_image",
                        "component_type": "suggested_image",
                        "title": "Handheld Rugged GPS Receiver for Field Mapping",
                        "content": {"text": "A handheld GPS receiver used in field geography surveys to record real-time coordinates, waypoints, and tracks."}
                    },
                    {
                        "block_type": "learning_goal",
                        "component_type": "learning_goal",
                        "title": "Lesson Objectives: GPS in Practice",
                        "content": {
                            "text": (
                                "By the end of this lesson, you will be able to:\n\n"
                                "- Explain how GPS receivers calculate ground positions using satellite trilateration\n"
                                "- State the minimum satellite constellation requirements for 2D and 3D positioning\n"
                                "- Analyze factors causing positioning error and explain the GPS uncertainty circle"
                            )
                        }
                    },
                    {
                        "block_type": "concept_explanation",
                        "component_type": "concept_explanation",
                        "title": "How GPS Works: Satellite Constellations",
                        "content": {
                            "text": (
                                "The Global Positioning System consists of a constellation of 24+ satellites orbiting Earth "
                                "at an altitude of approximately 20,200 km. Each satellite transmits atomic-clock timed radio signals "
                                "giving its orbital position and transmission timestamp."
                            )
                        }
                    }
                ]
            },
            {
                "page_number": 2,
                "page_title": "Satellite Trilateration",
                "blocks": [
                    {
                        "block_type": "diagram",
                        "component_type": "diagram",
                        "title": "GPS Satellite Trilateration Geometry",
                        "content": {
                            "caption": "Intersecting signal spheres from four satellites determining an exact ground position (Latitude, Longitude, Altitude, Time)."
                        }
                    },
                    {
                        "block_type": "concept_explanation",
                        "component_type": "concept_explanation",
                        "title": "The Physics of Trilateration",
                        "content": {
                            "text": (
                                "- Distance formula: $\\text{Distance} = \\text{Speed of Light } (c) \\times \\text{Time Delay } (\\Delta t)$\n"
                                "- **1 Satellite**: Receiver is somewhere on a vast spherical sphere surface.\n"
                                "- **2 Satellites**: The two spheres intersect, narrowing the location to a circular ring.\n"
                                "- **3 Satellites**: The three spheres intersect at two points (one on Earth, one in outer space), giving a **2D Position** (Latitude & Longitude).\n"
                                "- **4 Satellites**: Eliminates receiver clock errors and provides a complete **3D Position** (Latitude, Longitude, Altitude)."
                            )
                        }
                    }
                ]
            },
            {
                "page_number": 3,
                "page_title": "GPS Accuracy and Uncertainty Circles",
                "blocks": [
                    {
                        "block_type": "concept_explanation",
                        "component_type": "concept_explanation",
                        "title": "Why Coordinates Have Error Margins",
                        "content": {
                            "text": (
                                "Satellite signals travel through the atmosphere and can be delayed by the ionosphere, deflected "
                                "by tall city skyscrapers (multipath error), or blocked by dense forest canopies.\n\n"
                                "Because of this, digital mapping apps display your position inside a translucent **uncertainty circle** "
                                "(e.g. 'Accuracy ±5m'). Your true physical coordinate lies somewhere inside that circle."
                            )
                        }
                    }
                ]
            },
            {
                "page_number": 4,
                "page_title": "Check Your Understanding",
                "blocks": [
                    {
                        "block_type": "multiple_choice_question",
                        "component_type": "multiple_choice_question",
                        "title": "Formative Assessment: Satellites Needed for 3D Fix",
                        "content": {
                            "question": "What is the minimum number of satellites required for a GPS receiver to calculate a highly accurate 3D position (including altitude)?",
                            "options": [
                                "1 satellite",
                                "2 satellites",
                                "3 satellites",
                                "4 satellites"
                            ],
                            "correct_answer": "4 satellites",
                            "explanation": "While 3 satellites yield a 2D fix (lat/long), a minimum of 4 is required to solve for altitude and correct receiver clock bias."
                        }
                    },
                    {
                        "block_type": "multiple_choice_question",
                        "component_type": "multiple_choice_question",
                        "title": "Formative Assessment: The Uncertainty Circle",
                        "content": {
                            "question": "Why does a smartphone mapping app show a translucent blue circle around your location pin when you are in a dense forest or among high-rise buildings?",
                            "options": [
                                "To indicate nearby tourist points of interest",
                                "It represents the uncertainty circle, showing that signal deflection/obstruction is reducing coordinate accuracy",
                                "It is a decorative cartographic symbol representing water bodies",
                                "To signal that your smartphone battery is low"
                            ],
                            "correct_answer": "It represents the uncertainty circle, showing that signal deflection/obstruction is reducing coordinate accuracy",
                            "explanation": "Obstacles interfere with satellite signals, expanding the positioning uncertainty margin around the user's estimated location."
                        }
                    }
                ]
            }
        ]
    },

    # Lesson 7: Remote Sensing and Image Interpretation
    {
        "unit_order": 7,
        "unit_name": "Remote Sensing and Image Interpretation",
        "lesson_title": "Remote Sensing and Image Interpretation",
        "pages": [
            {
                "page_number": 1,
                "page_title": "Principles of Remote Sensing",
                "blocks": [
                    {
                        "block_type": "suggested_image",
                        "component_type": "suggested_image",
                        "title": "Multispectral Remote Sensing Satellite Imagery",
                        "content": {"text": "A multispectral satellite scene capturing terrain, water bodies, and vegetation across distinct electromagnetic wavebands."}
                    },
                    {
                        "block_type": "learning_goal",
                        "component_type": "learning_goal",
                        "title": "Lesson Objectives: Remote Sensing",
                        "content": {
                            "text": (
                                "By the end of this lesson, you will be able to:\n\n"
                                "- Explain how remote sensing sensors capture electromagnetic radiation from Earth's surface\n"
                                "- Distinguish between True-Colour and False-Colour (Near-Infrared) composite images\n"
                                "- Identify forests, water bodies, agricultural crops, and urban centers on satellite imagery"
                            )
                        }
                    },
                    {
                        "block_type": "concept_explanation",
                        "component_type": "concept_explanation",
                        "title": "Prerequisite Spark: Beyond Human Vision",
                        "content": {
                            "text": (
                                "Human eyes can only see visible light (Red, Green, Blue). But satellite sensors can detect "
                                "invisible Near-Infrared (NIR) and thermal radiation. "
                                "Why do scientists convert infrared light into bright red imagery? "
                                "Because healthy plant chlorophyll reflects infrared radiation like a bright mirror!"
                            )
                        }
                    }
                ]
            },
            {
                "page_number": 2,
                "page_title": "True-Colour vs False-Colour Imagery",
                "blocks": [
                    {
                        "block_type": "diagram",
                        "component_type": "diagram",
                        "title": "True-Colour vs False-Colour (NIR) Satellite Comparison",
                        "content": {
                            "caption": "Comparison of True-Colour (RGB) and False-Colour Infrared composites highlighting healthy vegetation in bright red."
                        }
                    },
                    {
                        "block_type": "concept_explanation",
                        "component_type": "concept_explanation",
                        "title": "Interpreting Spectral Signatures",
                        "content": {
                            "text": (
                                "- **True-Colour Composite**: Renders features as seen by the human eye. Healthy vegetation is green, clear water is dark blue/black, bare soil is tan/brown, and concrete/asphalt is gray.\n\n"
                                "- **False-Colour (Standard NIR Composite)**: Maps invisible Near-Infrared light to the Red display channel. Healthy crops and forests appear **vibrant bright red**, clear water absorbs infrared and appears **jet black**, while urban built-up areas appear **cyan/grey-blue**."
                            )
                        }
                    }
                ]
            },
            {
                "page_number": 3,
                "page_title": "Check Your Understanding",
                "blocks": [
                    {
                        "block_type": "multiple_choice_question",
                        "component_type": "multiple_choice_question",
                        "title": "Formative Assessment: False-Colour Vegetation",
                        "content": {
                            "question": "Why does healthy vegetation appear bright red in near-infrared (false-colour) satellite imagery?",
                            "options": [
                                "Because leaves are affected by acidic pollution",
                                "Healthy plant chlorophyll reflects near-infrared radiation extremely strongly, which is mapped to the red visual channel",
                                "Satellites can only take photos during dry, hot seasons",
                                "Red is the international symbol for environmental danger"
                            ],
                            "correct_answer": "Healthy plant chlorophyll reflects near-infrared radiation extremely strongly, which is mapped to the red visual channel",
                            "explanation": "Plant cellular structure strongly reflects NIR radiation; displaying this band in red makes vegetation stand out sharply from soil and concrete."
                        }
                    },
                    {
                        "block_type": "multiple_choice_question",
                        "component_type": "multiple_choice_question",
                        "title": "Formative Assessment: True-Colour Water Signature",
                        "content": {
                            "question": "Which feature is correctly paired with its typical appearance in a true-colour satellite image?",
                            "options": [
                                "Asphalt roads -> Bright green",
                                "Deep, clean water -> Very dark blue or black",
                                "Dense forest -> Bright yellow",
                                "Exposed soil -> Bright neon red"
                            ],
                            "correct_answer": "Deep, clean water -> Very dark blue or black",
                            "explanation": "Clean deep water absorbs almost all incoming solar radiation, reflecting minimal light and appearing dark blue or black."
                        }
                    }
                ]
            }
        ]
    },

    # Lesson 8: Data Sources and Data Input in GIS
    {
        "unit_order": 8,
        "unit_name": "Data Sources and Data Input in GIS",
        "lesson_title": "Data Sources and Data Input in GIS",
        "pages": [
            {
                "page_number": 1,
                "page_title": "Sources of Spatial Data",
                "blocks": [
                    {
                        "block_type": "suggested_image",
                        "component_type": "suggested_image",
                        "title": "Land Surveyor Using Modern Field Equipment",
                        "content": {"text": "A land surveyor collecting high-precision spatial coordinates using a total station and GPS receiver in the field."}
                    },
                    {
                        "block_type": "learning_goal",
                        "component_type": "learning_goal",
                        "title": "Lesson Objectives: Data Sources & Input",
                        "content": {
                            "text": (
                                "By the end of this lesson, you will be able to:\n\n"
                                "- Identify primary and secondary sources of GIS data\n"
                                "- Describe the methods of spatial data input: manual entry, GPS import, and digitization\n"
                                "- Compare raster scanning with on-screen vector heads-up digitizing"
                            )
                        }
                    },
                    {
                        "block_type": "concept_explanation",
                        "component_type": "concept_explanation",
                        "title": "Where Does GIS Data Come From?",
                        "content": {
                            "text": (
                                "A GIS is only as good as the data entered into it. Spatial data originates from four main sources:\n\n"
                                "1. **Satellite Imagery & Aerial Photography**: Continuous raster coverage of landscapes.\n"
                                "2. **Direct Field Surveys**: Fieldworkers recording coordinates with GPS handsets or mobile survey apps (e.g. KoboToolbox, ODK).\n"
                                "3. **Existing Hardcopy Paper Maps**: Scanned topographical and cadastral map sheets.\n"
                                "4. **Online Open Databases & Portals**: OpenStreetMap, government open data portals, and national survey databases."
                            )
                        }
                    }
                ]
            },
            {
                "page_number": 2,
                "page_title": "Methods of Data Input: Digitization",
                "blocks": [
                    {
                        "block_type": "diagram",
                        "component_type": "diagram",
                        "title": "On-Screen Heads-Up Vector Digitizing",
                        "content": {
                            "caption": "Tracing point landmarks, road polylines, and parcel boundary polygons over a geo-referenced raster background."
                        }
                    },
                    {
                        "block_type": "concept_explanation",
                        "component_type": "concept_explanation",
                        "title": "Three Primary Data Input Workflows",
                        "content": {
                            "text": (
                                "- **Manual Coordinate Entry**: Typing coordinate pairs directly into an attribute table.\n"
                                "- **Importing GPS Files**: Directly loading structured waypoint and track files (`.gpx`, `.kml`, `.geojson`, `.shp`) from GPS devices into GIS software.\n"
                                "- **Heads-Up Digitization**: The cartographer loads a geo-referenced raster image as a background and uses a computer mouse to trace features into digital vector layers (clicking points for wells, dragging polylines for rivers, and closing polygons for forests)."
                            )
                        }
                    }
                ]
            },
            {
                "page_number": 3,
                "page_title": "Check Your Understanding",
                "blocks": [
                    {
                        "block_type": "multiple_choice_question",
                        "component_type": "multiple_choice_question",
                        "title": "Formative Assessment: GPS File Import",
                        "content": {
                            "question": "A student imports a `.gpx` file containing coordinate waypoints from their smartphone into a GIS application. What is this method of data input called?",
                            "options": [
                                "Manual digitization",
                                "Geo-referencing",
                                "Importing GPS data files",
                                "Secondary literature review"
                            ],
                            "correct_answer": "Importing GPS data files",
                            "explanation": "GPX (GPS Exchange Format) is the open standard format for transferring GPS waypoints and track data into GIS programs."
                        }
                    },
                    {
                        "block_type": "multiple_choice_question",
                        "component_type": "multiple_choice_question",
                        "title": "Formative Assessment: Digitization Definition",
                        "content": {
                            "question": "What is 'digitization' in a Geographic Information System?",
                            "options": [
                                "Printing a digital map onto paper",
                                "Tracing physical features on top of a geo-referenced background image to create digital vector points, lines, or polygons",
                                "Calculating coordinates using multiplication formulas",
                                "Taking photographs with a smartphone camera"
                            ],
                            "correct_answer": "Tracing physical features on top of a geo-referenced background image to create digital vector points, lines, or polygons",
                            "explanation": "Digitization converts visual raster imagery into structured, queryable vector geometric layers."
                        }
                    }
                ]
            }
        ]
    },

    # Lesson 9: Styling and Displaying GIS Data
    {
        "unit_order": 9,
        "unit_name": "Styling and Displaying GIS Data",
        "lesson_title": "Styling and Displaying GIS Data",
        "pages": [
            {
                "page_number": 1,
                "page_title": "Cartographic Symbology & Design",
                "blocks": [
                    {
                        "block_type": "suggested_image",
                        "component_type": "suggested_image",
                        "title": "Styled Thematic Map with Cartographic Symbology",
                        "content": {"text": "A professionally styled thematic choropleth map displaying regional categories with clear legend, scale, and north orientation."}
                    },
                    {
                        "block_type": "learning_goal",
                        "component_type": "learning_goal",
                        "title": "Lesson Objectives: Styling GIS Data",
                        "content": {
                            "text": (
                                "By the end of this lesson, you will be able to:\n\n"
                                "- Apply cartographic symbology rules to point, line, and polygon layers\n"
                                "- Differentiate between qualitative and quantitative thematic maps\n"
                                "- Verify map layouts against the standard six essential marginal elements"
                            )
                        }
                    },
                    {
                        "block_type": "concept_explanation",
                        "component_type": "concept_explanation",
                        "title": "The Art and Science of Cartography",
                        "content": {
                            "text": (
                                "Raw GIS data looks like a jumble of random lines and dots until a cartographer styles it. "
                                "Symbology translates abstract computer coordinates into intuitive visual language that human readers "
                                "can understand in seconds."
                            )
                        }
                    }
                ]
            },
            {
                "page_number": 2,
                "page_title": "Symbology Rules & The Essential Elements Checklist",
                "blocks": [
                    {
                        "block_type": "diagram",
                        "component_type": "diagram",
                        "title": "Complete Thematic Map Layout and Marginal Elements",
                        "content": {
                            "caption": "Map composition showing Title, Map Body, Legend/Key, Scale Bar, North Arrow, and Source attribution."
                        }
                    },
                    {
                        "block_type": "concept_explanation",
                        "component_type": "concept_explanation",
                        "title": "The Six Essential Marginal Components",
                        "content": {
                            "text": (
                                "Every completed GIS map layout must include the **KICD Cartographic Standards Checklist**:\n\n"
                                "1. **Title**: Clearly states WHAT is shown, WHERE it is located, and WHEN the data was collected.\n"
                                "2. **Key / Legend**: Explains all visual symbols, line styles, and color ramps.\n"
                                "3. **Scale**: Shows ground distance conversion via a linear scale bar and representative fraction (e.g. 1:50,000).\n"
                                "4. **North Arrow / Orientation**: Indicates geographic True North.\n"
                                "5. **Coordinate Frame / Grid**: Shows latitude/longitude or UTM grid reference lines.\n"
                                "6. **Source Attribution**: Acknowledges where the raw data originated (e.g. Survey of Kenya, KFS, Landsat)."
                            )
                        }
                    }
                ]
            },
            {
                "page_number": 3,
                "page_title": "Check Your Understanding",
                "blocks": [
                    {
                        "block_type": "multiple_choice_question",
                        "component_type": "multiple_choice_question",
                        "title": "Formative Assessment: Cartographic Symbology",
                        "content": {
                            "question": "You are styling a land-use map for your school locality. Which styling choice is most intuitive and cartographically correct?",
                            "options": [
                                "Shading lakes bright red and forests yellow",
                                "Using standard green for forests, blue for water bodies, and light brown for agricultural soils",
                                "Using the same black circle symbol for both roads and wells",
                                "Deleting the map legend to keep the layout uncluttered"
                            ],
                            "correct_answer": "Using standard green for forests, blue for water bodies, and light brown for agricultural soils",
                            "explanation": "Maps must follow conventional color associations (green for flora, blue for water) to ensure immediate legibility."
                        }
                    },
                    {
                        "block_type": "multiple_choice_question",
                        "component_type": "multiple_choice_question",
                        "title": "Formative Assessment: Purpose of a Legend",
                        "content": {
                            "question": "Why is a Legend (Key) mandatory on a styled GIS thematic map?",
                            "options": [
                                "It is used directly to calculate ground distances",
                                "It translates abstract symbols and colors into real-world geographic meanings",
                                "It indicates the magnetic orientation of the map",
                                "It lists the biographical background of the cartographer"
                            ],
                            "correct_answer": "It translates abstract symbols and colors into real-world geographic meanings",
                            "explanation": "Without a key, visual colors and icons cannot be decoded by the reader, rendering the map meaningless."
                        }
                    }
                ]
            }
        ]
    },

    # Lesson 10: Querying and Analyzing Spatial Data
    {
        "unit_order": 10,
        "unit_name": "Querying and Analyzing Spatial Data",
        "lesson_title": "Querying and Analyzing Spatial Data",
        "pages": [
            {
                "page_number": 1,
                "page_title": "Spatial Analysis Capabilities",
                "blocks": [
                    {
                        "block_type": "suggested_image",
                        "component_type": "suggested_image",
                        "title": "GIS Spatial Analysis and Proximity Buffering",
                        "content": {"text": "A spatial analysis map display showing concentric buffer rings and overlay zones around critical infrastructure."}
                    },
                    {
                        "block_type": "learning_goal",
                        "component_type": "learning_goal",
                        "title": "Lesson Objectives: Spatial Query & Analysis",
                        "content": {
                            "text": (
                                "By the end of this lesson, you will be able to:\n\n"
                                "- Formulate attribute and spatial queries in a GIS\n"
                                "- Explain proximity analysis (buffering) and overlay analysis\n"
                                "- Apply network analysis to solve optimal routing and transportation problems"
                            )
                        }
                    },
                    {
                        "block_type": "concept_explanation",
                        "component_type": "concept_explanation",
                        "title": "Beyond Map Making: Spatial Analysis",
                        "content": {
                            "text": (
                                "While graphics software can draw pretty maps, only a GIS can perform **spatial analysis**—asking "
                                "complex mathematical 'Where' questions to uncover patterns, calculate distances, and model scenarios."
                            )
                        }
                    }
                ]
            },
            {
                "page_number": 2,
                "page_title": "Core Analytical Methods in GIS",
                "blocks": [
                    {
                        "block_type": "diagram",
                        "component_type": "diagram",
                        "title": "Spatial Analysis: Buffering, Overlay, and Network Routing",
                        "content": {
                            "caption": "Visual representation of Buffer Proximity Zones, Multi-Layer Overlay Suitability, and Network Shortest-Path Routing."
                        }
                    },
                    {
                        "block_type": "concept_explanation",
                        "component_type": "concept_explanation",
                        "title": "Four Pillars of Spatial Analysis",
                        "content": {
                            "text": (
                                "1. **Spatial Queries**: Filtering data based on location and attributes (e.g. `SELECT * FROM Clinics WHERE Distance_To_Road < 100m`).\n\n"
                                "2. **Proximity Analysis (Buffering)**: Generating a boundary zone of a specific distance around a feature (e.g. creating a 50-meter riparian protection buffer along the Nairobi River).\n\n"
                                "3. **Overlay Analysis**: Stacking multiple independent layers (e.g. slope, soil type, annual rainfall) to find overlapping zones that satisfy all criteria for tea farming suitability.\n\n"
                                "4. **Network Analysis**: Analyzing interconnected line networks (roads, pipes, power grids) to find the shortest or fastest route for emergency vehicles."
                            )
                        }
                    }
                ]
            },
            {
                "page_number": 3,
                "page_title": "Check Your Understanding",
                "blocks": [
                    {
                        "block_type": "multiple_choice_question",
                        "component_type": "multiple_choice_question",
                        "title": "Formative Assessment: Proximity Buffering",
                        "content": {
                            "question": "An environmental protection agency needs to identify all industrial factories located within 100 meters of the Nairobi River. Which GIS tool should they use?",
                            "options": [
                                "Scale conversion",
                                "Proximity analysis (Buffering)",
                                "Coordinate conversion from DD to DMS",
                                "Ground photography"
                            ],
                            "correct_answer": "Proximity analysis (Buffering)",
                            "explanation": "Buffering generates a perimeter boundary of specified distance around linear river features to detect nearby structures."
                        }
                    },
                    {
                        "block_type": "multiple_choice_question",
                        "component_type": "multiple_choice_question",
                        "title": "Formative Assessment: Overlay Analysis",
                        "content": {
                            "question": "What does 'Overlay Analysis' involve in a GIS workflow?",
                            "options": [
                                "Accidentally printing one paper map over another",
                                "Combining multiple thematic layers on a common grid to identify areas meeting intersecting spatial criteria",
                                "Drawing a geological cross-section through a mountain",
                                "Collecting socioeconomic data using paper questionnaires"
                            ],
                            "correct_answer": "Combining multiple thematic layers on a common grid to identify areas meeting intersecting spatial criteria",
                            "explanation": "Overlay analysis integrates multiple spatial themes (e.g. slope, soil, rainfall) to identify suitable target zones."
                        }
                    }
                ]
            }
        ]
    },

    # Lesson 11: Applications of GIS: Urban Planning and Disaster Management
    {
        "unit_order": 11,
        "unit_name": "Applications of GIS: Urban Planning and Disaster Management",
        "lesson_title": "Applications of GIS: Urban Planning and Disaster Management",
        "pages": [
            {
                "page_number": 1,
                "page_title": "Urban Planning & Disaster Management",
                "blocks": [
                    {
                        "block_type": "suggested_image",
                        "component_type": "suggested_image",
                        "title": "Emergency Disaster Response and Evacuation Operations",
                        "content": {"text": "Emergency response personnel conducting flood rescue operations and coordinating relief logistics in flood-affected lowlands."}
                    },
                    {
                        "block_type": "learning_goal",
                        "component_type": "learning_goal",
                        "title": "Lesson Objectives: Urban & Disaster GIS",
                        "content": {
                            "text": (
                                "By the end of this lesson, you will be able to:\n\n"
                                "- Evaluate how GIS supports sustainable urban development, zoning, and transport routing\n"
                                "- Design GIS-based disaster preparedness and flood evacuation strategies\n"
                                "- Analyze the Kenyan case study of flood mitigation and early warning in Budalangi"
                            )
                        }
                    },
                    {
                        "block_type": "concept_explanation",
                        "component_type": "concept_explanation",
                        "title": "Prerequisite Spark: Planning a Growing City",
                        "content": {
                            "text": (
                                "Imagine you are the chief town planner for Nairobi or Mombasa. Where would you site a new municipal "
                                "solid waste landfill? You must ensure it is:\n"
                                "- At least 2 km away from residential neighborhoods (Buffering)\n"
                                "- Located on impermeable clay soils to protect groundwater (Overlay)\n"
                                "- Directly connected to major arterial roads (Network Analysis)\n\n"
                                "GIS makes this multi-criteria spatial decision fast, objective, and accurate."
                            )
                        }
                    }
                ]
            },
            {
                "page_number": 2,
                "page_title": "Disaster Management & The Budalangi Flood Model",
                "blocks": [
                    {
                        "block_type": "diagram",
                        "component_type": "diagram",
                        "title": "Disaster Management GIS: Flood Inundation & Evacuation Routing",
                        "content": {
                            "caption": "Digital Elevation Model (DEM) showing River Nzoia flood risk zones, marooned villages, and high-ground evacuation shelters."
                        }
                    },
                    {
                        "block_type": "concept_explanation",
                        "component_type": "concept_explanation",
                        "title": "Kenyan Case Study: Budalangi Flood Early Warning",
                        "content": {
                            "text": (
                                "Budalangi in Busia County has historically suffered severe seasonal flooding when the River Nzoia bursts its banks.\n\n"
                                "Kenyan disaster agencies deploy GIS models by combining:\n"
                                "1. **Digital Elevation Models (DEM)**: Identifies low-lying depressions below river flood levels.\n"
                                "2. **Hydrological Drainage Layers**: Models runoff velocity and water accumulation rates.\n"
                                "3. **Settlement & Road Layers**: Identifies vulnerable homesteads and charts safe, elevated evacuation corridors to highland shelters."
                            )
                        }
                    }
                ]
            },
            {
                "page_number": 3,
                "page_title": "Check Your Understanding",
                "blocks": [
                    {
                        "block_type": "multiple_choice_question",
                        "component_type": "multiple_choice_question",
                        "title": "Formative Assessment: Disaster GIS Support",
                        "content": {
                            "question": "How does GIS assist emergency rescue teams during active flood disasters?",
                            "options": [
                                "It physically prevents heavy rainfall from occurring",
                                "It maps flooded lowlands and overlays road networks to navigate safe evacuation corridors",
                                "It replaces the need for first-aid medical supplies",
                                "It converts qualitative interviews into statistical tables"
                            ],
                            "correct_answer": "It maps flooded lowlands and overlays road networks to navigate safe evacuation corridors",
                            "explanation": "GIS combines elevation, flood extent, and transport layers to route rescue teams and identify stranded populations."
                        }
                    },
                    {
                        "block_type": "multiple_choice_question",
                        "component_type": "multiple_choice_question",
                        "title": "Formative Assessment: Site Suitability Layers",
                        "content": {
                            "question": "Which data layers are most critical for an urban planner identifying safe zones for new residential housing?",
                            "options": [
                                "Mineral export trends and historic tourism statistics",
                                "Terrain slope (topography), soil stability, and flood hazard zone layers",
                                "Colonial border histories and local political party offices",
                                "Total annual maize production per county"
                            ],
                            "correct_answer": "Terrain slope (topography), soil stability, and flood hazard zone layers",
                            "explanation": "Topography, soil mechanics, and flood hazard boundaries directly determine physical construction safety."
                        }
                    }
                ]
            }
        ]
    },

    # Lesson 12: Applications of GIS: Agriculture, Health, and Conservation
    {
        "unit_order": 12,
        "unit_name": "Applications of GIS: Agriculture, Health, and Conservation",
        "lesson_title": "Applications of GIS: Agriculture, Health, and Conservation",
        "pages": [
            {
                "page_number": 1,
                "page_title": "Agriculture, Health & Environmental GIS",
                "blocks": [
                    {
                        "block_type": "suggested_image",
                        "component_type": "suggested_image",
                        "title": "Agricultural Drone Aerial Monitoring and Crop Health",
                        "content": {"text": "A multispectral sensor drone surveying agricultural crop health and vegetative index variations across farm parcels."}
                    },
                    {
                        "block_type": "learning_goal",
                        "component_type": "learning_goal",
                        "title": "Lesson Objectives: Agri, Health & Ecology",
                        "content": {
                            "text": (
                                "By the end of this lesson, you will be able to:\n\n"
                                "- Explain the role of GIS and GPS in precision agriculture and variable-rate fertilizing\n"
                                "- Analyze how public health agencies track disease outbreaks and map health facility access\n"
                                "- Evaluate GIS applications in monitoring deforestation and wildlife corridors in Kenya"
                            )
                        }
                    },
                    {
                        "block_type": "concept_explanation",
                        "component_type": "concept_explanation",
                        "title": "Transforming Vital Sectors",
                        "content": {
                            "text": (
                                "GIS is transforming modern life beyond traditional cartography. In Kenya, precision agriculture "
                                "maximizes crop harvest, epidemiological mapping battles malaria and cholera, and conservationists "
                                "protect vital water towers like the Mau Forest Complex."
                            )
                        }
                    }
                ]
            },
            {
                "page_number": 2,
                "page_title": "Precision Agriculture & Environmental Protection",
                "blocks": [
                    {
                        "block_type": "diagram",
                        "component_type": "diagram",
                        "title": "Precision Agriculture NDVI Workflow & Forest Conservation",
                        "content": {
                            "caption": "Precision agriculture workflow: Drone multispectral imaging, NDVI crop stress zoning, and targeted variable-rate fertilizer delivery."
                        }
                    },
                    {
                        "block_type": "concept_explanation",
                        "component_type": "concept_explanation",
                        "title": "Three Major Application Domains",
                        "content": {
                            "text": (
                                "- **Precision Agriculture**: Farmers use Normalized Difference Vegetation Index (NDVI) imagery from drones/satellites to map crop vigour. GPS-guided tractors apply fertilizer and irrigation strictly to underperforming patches, slashing costs and runoff.\n\n"
                                "- **Environmental Conservation**: Kenya Forest Service (KFS) monitors deforestation in the Mau Forest Complex by analyzing multi-temporal satellite imagery to detect illegal logging clearings in real time.\n\n"
                                "- **Public Health & Epidemiology**: Health agencies map disease incidence (e.g. malaria or cholera) to identify environmental clusters (stagnant water pools, contaminated boreholes) and dispatch targeted medical supplies."
                            )
                        }
                    }
                ]
            },
            {
                "page_number": 3,
                "page_title": "Check Your Understanding",
                "blocks": [
                    {
                        "block_type": "multiple_choice_question",
                        "component_type": "multiple_choice_question",
                        "title": "Formative Assessment: Deforestation Tracking",
                        "content": {
                            "question": "How does GIS assist authorities in combating deforestation in Kenya's primary water catchment towers?",
                            "options": [
                                "It physically plants trees automatically",
                                "It analyzes multi-temporal satellite imagery to detect changes in canopy cover and pinpoint illegal logging",
                                "It calculates the average height of trees in centimetres",
                                "It conducts door-to-door interviews with local timber traders"
                            ],
                            "correct_answer": "It analyzes multi-temporal satellite imagery to detect changes in canopy cover and pinpoint illegal logging",
                            "explanation": "Multi-date satellite imagery comparison allows GIS systems to highlight loss of forest canopy with high temporal precision."
                        }
                    },
                    {
                        "block_type": "multiple_choice_question",
                        "component_type": "multiple_choice_question",
                        "title": "Formative Assessment: Precision Agriculture Benefits",
                        "content": {
                            "question": "What is a primary advantage of 'precision agriculture' powered by GIS and GPS?",
                            "options": [
                                "It eliminates the need for any human farm workers",
                                "It allows targeted application of fertilizer and water based on micro-level crop health maps, maximizing efficiency",
                                "It allows crops to grow without soil or sunlight",
                                "It replaces the need for seasonal rainfall forecasts"
                            ],
                            "correct_answer": "It allows targeted application of fertilizer and water based on micro-level crop health maps, maximizing efficiency",
                            "explanation": "Precision agriculture applies inputs selectively based on spatial need, reducing waste and optimizing crop yields."
                        }
                    }
                ]
            }
        ]
    },

    # Lesson 13: Locality Mapping Project and Quality Control
    {
        "unit_order": 13,
        "unit_name": "Locality Mapping Project and Quality Control",
        "lesson_title": "Locality Mapping Project and Quality Control",
        "pages": [
            {
                "page_number": 1,
                "page_title": "The Community Locality Mapping Project",
                "blocks": [
                    {
                        "block_type": "suggested_image",
                        "component_type": "suggested_image",
                        "title": "Participatory Community Mapping and Field Surveying",
                        "content": {"text": "Students and community members collaborating around a shared locality map to record local assets and environmental hazards."}
                    },
                    {
                        "block_type": "learning_goal",
                        "component_type": "learning_goal",
                        "title": "Lesson Objectives: Locality Project & QA",
                        "content": {
                            "text": (
                                "By the end of this lesson, you will be able to:\n\n"
                                "- Design and execute an end-to-end community asset or hazard mapping project\n"
                                "- Collect, digitize, style, and compile field spatial data into a finished map\n"
                                "- Evaluate map outputs against cartographic quality control and positional accuracy standards"
                            )
                        }
                    },
                    {
                        "block_type": "concept_explanation",
                        "component_type": "concept_explanation",
                        "title": "Putting Theory Into Practice",
                        "content": {
                            "text": (
                                "In this culminating project, you will work in small teams to map your school or community. "
                                "You will map physical assets (water taps, health clinics, sports fields) or local hazards "
                                "(flood zones, open quarries, waste dumps), following the full professional GIS workflow."
                            )
                        }
                    }
                ]
            },
            {
                "page_number": 2,
                "page_title": "The 5-Step Project Workflow & QA Checklist",
                "blocks": [
                    {
                        "block_type": "diagram",
                        "component_type": "diagram",
                        "title": "Locality Mapping 5-Step Project Workflow & QA Checklist",
                        "content": {
                            "caption": "Project workflow from Planning, Field Data Collection, Data Entry, Cartographic Styling, to Final Quality Control Audit."
                        }
                    },
                    {
                        "block_type": "concept_explanation",
                        "component_type": "concept_explanation",
                        "title": "Cartographic Quality Control Audit",
                        "content": {
                            "text": (
                                "Before presenting your community map, audit it against the **KICD Quality Standards Checklist**:\n\n"
                                "1. **Positional Accuracy**: Do GPS points match their true physical ground positions?\n"
                                "2. **Completeness**: Are all six essential map elements (Title, Key, Scale, North Arrow, Coordinates, Source) present?\n"
                                "3. **Cartographic Clarity**: Are symbols unambiguous, uncluttered, and easy to read?\n"
                                "4. **Source & Date Attribution**: Is the data origin clearly stated with author and survey date?"
                            )
                        }
                    }
                ]
            },
            {
                "page_number": 3,
                "page_title": "Check Your Understanding",
                "blocks": [
                    {
                        "block_type": "multiple_choice_question",
                        "component_type": "multiple_choice_question",
                        "title": "Formative Assessment: Positional Accuracy Check",
                        "content": {
                            "question": "During your locality mapping audit, you discover that the school borehole is plotted 2 kilometres away from its true ground position. Which quality control standard has been violated?",
                            "options": [
                                "Aesthetic coloring",
                                "Legend completeness",
                                "Positional accuracy",
                                "Title description"
                            ],
                            "correct_answer": "Positional accuracy",
                            "explanation": "Positional accuracy measures how closely coordinate coordinates on the map match true physical locations on Earth."
                        }
                    },
                    {
                        "block_type": "multiple_choice_question",
                        "component_type": "multiple_choice_question",
                        "title": "Formative Assessment: Essential Map Checklist",
                        "content": {
                            "question": "Before submitting your final locality map, you check it against the cartographic standards checklist. Which of the following is an unnecessary decoration rather than an essential element?",
                            "options": [
                                "A clear scale bar and complete legend",
                                "A North Arrow and coordinate grid",
                                "A decorative hand-drawn portrait of the cartographer",
                                "A descriptive title and data source attribution"
                            ],
                            "correct_answer": "A decorative hand-drawn portrait of the cartographer",
                            "explanation": "Standard cartographic layouts require Title, Key, Scale, Orientation, Grid, and Source; personal portraits are non-standard decorative elements."
                        }
                    }
                ]
            }
        ]
    }
]

def run_ingestion():
    print("=" * 80)
    print("VLearn Ingestion Engine: Grade 10 Geography — Topic 4: GIS")
    print("=" * 80)

    with transaction.atomic():
        # 1. Verify Hierarchy
        curriculum = Curriculum.objects.filter(name__iexact="CBC").first()
        if not curriculum:
            raise RuntimeError("Curriculum 'CBC' not found!")

        grade = Grade.objects.filter(curriculum=curriculum, name__icontains="10").first()
        if not grade:
            raise RuntimeError("Grade 10 not found under CBC!")

        subject = Subject.objects.filter(grade=grade, name="Geography").first()
        if not subject:
            raise RuntimeError("Subject 'Geography' (ID 37) not found under Grade 10 CBC!")

        topic, created = Topic.objects.get_or_create(
            subject=subject,
            order=4,
            defaults={
                "name": "Geographic Information System (GIS)",
                "description": "Introduction to geospatial technologies, spatial vs attribute data, components of GIS, coordinates, GPS, remote sensing, spatial queries, and applications."
            }
        )
        topic.name = "Geographic Information System (GIS)"
        topic.description = "Introduction to geospatial technologies, spatial vs attribute data, components of GIS, coordinates, GPS, remote sensing, spatial queries, and applications."
        topic.save()

        print(f"Target Topic: [{topic.id}] Grade 10 Geography - Topic 4: {topic.name}")

        # 2. Ingest 13 Lessons & Units
        total_blocks_created = 0
        for les_data in LESSONS_DATA:
            u_order = les_data["unit_order"]
            u_name = clean_text(les_data["unit_name"])
            les_title = clean_text(les_data["lesson_title"])

            unit, u_created = LearningUnit.objects.get_or_create(
                topic=topic,
                order=u_order,
                defaults={"name": u_name, "description": f"Learning unit for {u_name}"}
            )
            unit.name = u_name
            unit.save()

            lesson, l_created = Lesson.objects.get_or_create(
                topic=topic,
                learning_unit=unit,
                defaults={
                    "title": les_title,
                    "status": "published",
                    "version": 1
                }
            )
            lesson.title = les_title
            lesson.status = "published"
            lesson.version = 1
            lesson.save()

            # Clean previous blocks for idempotency
            lesson.blocks.all().delete()

            block_seq = 1
            for page in les_data["pages"]:
                p_num = page["page_number"]
                p_title = clean_text(page["page_title"])

                for comp_order, blk in enumerate(page["blocks"], start=1):
                    b_type = blk["block_type"]
                    c_type = blk.get("component_type", b_type)
                    b_title = clean_text(blk.get("title", p_title))
                    b_content = clean_content_dict(blk.get("content", {}))

                    LessonBlock.objects.create(
                        lesson=lesson,
                        page_number=p_num,
                        page_title=p_title,
                        order=block_seq,
                        component_order=comp_order,
                        block_type=b_type,
                        component_type=c_type,
                        title=b_title,
                        content=b_content
                    )
                    block_seq += 1
                    total_blocks_created += 1

            print(f" -> Ingested Unit {u_order}: {les_title} ({len(les_data['pages'])} pages, {block_seq - 1} blocks)")

    print("=" * 80)
    print(f"Ingestion completed successfully for Grade 10 Geography Topic 4! (Total Blocks: {total_blocks_created})")
    print("=" * 80)

if __name__ == "__main__":
    run_ingestion()
