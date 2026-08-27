"""
VLearn CBC Grade 10 Geography — Topic 3: Statistical Methods
Direct Programmatic Source-Driven Ingestion Engine

Subject: Geography (Grade 10, CBC)
Topic 3: Statistical Methods
Source: Grade 10 Geography/03_statistical_methods.md

Usage:
  ./venv/bin/python curriculum/ingest_cbc_grade10_geography_topic3.py
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
# TOPIC 3 LESSON DEFINITIONS (12 LESSONS)
# =============================================================================
LESSONS_DATA = [
    # Lesson 1: Meaning and Role of Statistics in Geography
    {
        "unit_order": 1,
        "unit_name": "Meaning and Role of Statistics in Geography",
        "lesson_title": "Meaning and Role of Statistics in Geography",
        "pages": [
            {
                "page_number": 1,
                "page_title": "Introduction to Geographical Statistics",
                "blocks": [
                    {
                        "block_type": "suggested_image",
                        "component_type": "suggested_image",
                        "title": "Meteorological Weather Station and Data Collection",
                        "content": {"text": "A standard meteorological station recording quantitative daily weather measurements such as temperature, rainfall, and atmospheric pressure."}
                    },
                    {
                        "block_type": "learning_goal",
                        "component_type": "learning_goal",
                        "title": "Lesson Objectives: Meaning and Role of Statistics",
                        "content": {
                            "text": (
                                "By the end of this lesson, you will be able to:\n\n"
                                "- Explain the meaning of statistics as applied in geographical studies\n"
                                "- Examine how statistical data simplifies complex spatial phenomena\n"
                                "- Use statistical figures to make objective regional comparisons across Kenya"
                            )
                        }
                    },
                    {
                        "block_type": "concept_explanation",
                        "component_type": "concept_explanation",
                        "title": "Prerequisite Spark: The Power of Averages",
                        "content": {
                            "text": (
                                "Think about a local marketplace in your county. If you wanted to describe how much maize is sold every day, "
                                "you could list every single bag sold by every individual seller over the year. However, saying 'On average, our market sells "
                                "250 bags of maize per day' communicates the reality immediately and clearly. Statistics transform overwhelming piles of raw numbers into actionable knowledge."
                            )
                        }
                    }
                ]
            },
            {
                "page_number": 2,
                "page_title": "Definitions & Nature of Statistics",
                "blocks": [
                    {
                        "block_type": "definition_card",
                        "component_type": "definition_card",
                        "title": "Key Statistical Terminology",
                        "content": {
                            "definitions": [
                                {
                                    "term": "Statistics",
                                    "definition": "The scientific discipline and systematic process of collecting, organizing, analyzing, interpreting, and presenting numerical data.",
                                    "simple": "The science of turning messy, raw numbers into clear, meaningful information."
                                },
                                {
                                    "term": "Geographical Statistics",
                                    "definition": "Quantitative (numerical) data representing physical and human geographical phenomena, such as daily temperatures, annual rainfall, population density, crop yields, and traffic volumes.",
                                    "simple": "'Geography in numbers'—measurable figures that describe our world."
                                }
                            ]
                        }
                    },
                    {
                        "block_type": "concept_explanation",
                        "component_type": "concept_explanation",
                        "title": "The Dual Role of Statistics in Geography",
                        "content": {
                            "text": (
                                "In geographical inquiry, statistics serve two fundamental functions:\n\n"
                                "1. **Simplifying Complex Data**: Geographers observe massive volumes of continuous information. Rather than reviewing 365 daily temperature logs for Nairobi, calculating an annual average temperature condenses the records into a single representative figure.\n\n"
                                "2. **Facilitating Regional Comparisons**: Numerical indicators allow objective spatial comparisons. Comparing Lodwar's average annual rainfall (150 mm) with Kericho's (1,800 mm) immediately demonstrates stark differences in climate and agricultural potential."
                            )
                        }
                    },
                    {
                        "block_type": "suggested_diagram",
                        "component_type": "suggested_diagram",
                        "title": "Statistics as a Data Condensation Mechanism",
                        "content": {"text": "Dual-panel infographic contrasting a disorganized cloud of 30 daily temperature figures with a clean single summary indicator of 22°C mean temperature."}
                    }
                ]
            },
            {
                "page_number": 3,
                "page_title": "Kenyan Case Study & Agricultural Planning",
                "blocks": [
                    {
                        "block_type": "real_world_case",
                        "component_type": "real_world_case",
                        "title": "Case Study: Rainfall Statistics in Nairobi & Crop Calendars",
                        "content": {
                            "title": "Bimodal Rainfall Patterns and Farming Decisions in Kenya",
                            "description": (
                                "Nairobi experiences a bimodal rainfall regime with two distinct wet seasons: the long rains from March to May "
                                "and the short rains from October to December. By analyzing historical monthly rainfall statistics (such as 120 mm in April "
                                "versus 30 mm in July), Kenyan agricultural extension officers can advise farmers on the exact planting dates for maize and beans to maximize yields and avoid crop failure."
                            )
                        }
                    },
                    {
                        "block_type": "concept_explanation",
                        "component_type": "concept_explanation",
                        "title": "Why Geographers Rely on Quantitative Evidence",
                        "content": {
                            "text": (
                                "Descriptive words like 'wet' or 'dry' are subjective and imprecise. When economic planners allocate national funds for irrigation "
                                "or famine relief, they require exact millimeters of precipitation, cubic meters of river discharge, and demographic counts. "
                                "Statistical data forms the backbone of modern geographic planning and policy formulation."
                            )
                        }
                    }
                ]
            },
            {
                "page_number": 4,
                "page_title": "Formative Assessment",
                "blocks": [
                    {
                        "block_type": "knowledge_check",
                        "component_type": "knowledge_check",
                        "title": "Knowledge Check: Role of Statistics",
                        "content": {
                            "question": "Why is statistical data valuable to a geographer?",
                            "options": [
                                "A) It replaces the need for field observations.",
                                "B) It simplifies complex raw data and enables precise regional comparisons.",
                                "C) It is always 100% accurate and never contains errors.",
                                "D) It only measures qualitative experiences like feelings."
                            ],
                            "correct_answer": "B",
                            "explanation": "Statistics condense large volumes of raw observations into clear summary figures and enable objective comparisons between different geographical regions."
                        }
                    },
                    {
                        "block_type": "knowledge_check",
                        "component_type": "knowledge_check",
                        "title": "Knowledge Check: Identifying Geographical Statistics",
                        "content": {
                            "question": "Which of the following is an example of a geographical statistic?",
                            "options": [
                                "A) A verbal description of a scenic landscape.",
                                "B) A list of historical national holidays.",
                                "C) The average annual tea production of Kericho County in metric tonnes.",
                                "D) A sketch map of Mt. Kenya drawn without a scale."
                            ],
                            "correct_answer": "C",
                            "explanation": "Annual tea yield measured in metric tonnes is a quantitative, numerical data point representing an agricultural and geographical phenomenon."
                        }
                    }
                ]
            }
        ]
    },

    # Lesson 2: Limitations of Statistics in Geographical Studies
    {
        "unit_order": 2,
        "unit_name": "Limitations of Statistics in Geographical Studies",
        "lesson_title": "Limitations of Statistics in Geographical Studies",
        "pages": [
            {
                "page_number": 1,
                "page_title": "Introduction to Statistical Limitations",
                "blocks": [
                    {
                        "block_type": "suggested_image",
                        "component_type": "suggested_image",
                        "title": "Drought Impact and Livestock Pastoralism in ASAL Kenya",
                        "content": {"text": "Pastoralist communities navigating arid land during severe drought, illustrating the human and environmental realities behind food insecurity statistics."}
                    },
                    {
                        "block_type": "learning_goal",
                        "component_type": "learning_goal",
                        "title": "Lesson Objectives: Statistical Limitations",
                        "content": {
                            "text": (
                                "By the end of this lesson, you will be able to:\n\n"
                                "- Analyze the inherent limitations of relying solely on numerical data in geographical studies\n"
                                "- Explain why statistical figures cannot uncover the underlying causes of spatial phenomena\n"
                                "- Justify the necessity of combining quantitative data with qualitative geographical analysis"
                            )
                        }
                    },
                    {
                        "block_type": "concept_explanation",
                        "component_type": "concept_explanation",
                        "title": "Prerequisite Spark: The Story Behind the Numbers",
                        "content": {
                            "text": (
                                "Suppose you read a report stating: 'Counties in the Arid and Semi-Arid Lands (ASAL) of Kenya experienced a 45% drop in livestock productivity.' "
                                "Does that single percentage capture the cultural attachment of pastoralist families to their herds, the emotional toll of drought, or the historical land tenure policies that created this vulnerability? "
                                "Numbers provide patterns, but humans live the reality."
                            )
                        }
                    }
                ]
            },
            {
                "page_number": 2,
                "page_title": "Core Limitations of Geographical Statistics",
                "blocks": [
                    {
                        "block_type": "concept_explanation",
                        "component_type": "concept_explanation",
                        "title": "Major Constraints in Statistical Analysis",
                        "content": {
                            "text": (
                                "While statistics are indispensable, geographers must be mindful of their critical constraints:\n\n"
                                "1. **Inability to Explain Underlying Causes**: Statistics show *what* is happening, but rarely *why*. A statistic showing a 40% reduction in maize yield does not reveal whether the root cause was fertilizer failure, armyworm pests, unpredictable rainfall, or high diesel prices for tractors.\n\n"
                                "2. **Outdated and Incomplete Records**: Censuses and large-scale agricultural surveys occur infrequently (e.g. once every 10 years in Kenya). Resource allocation decisions risk being based on stale figures.\n\n"
                                "3. **Omission of Qualitative Realities**: Numbers cannot measure emotions, cultural beliefs, indigenous ecological wisdom, or land disputes.\n\n"
                                "4. **Vulnerability to Bias and Manipulation**: If sample groups are selected carelessly (such as interviewing only wealthy commercial landowners), results will be severely distorted."
                            )
                        }
                    },
                    {
                        "block_type": "suggested_diagram",
                        "component_type": "suggested_diagram",
                        "title": "The Qualitative-Quantitative Analytical Balance",
                        "content": {"text": "Conceptual diagram showing how quantitative metrics (what, how much) combine with qualitative field interviews and observations (why, how) to form complete geographical understanding."}
                    }
                ]
            },
            {
                "page_number": 3,
                "page_title": "The Fallacy of Simple Averages & Misconceptions",
                "blocks": [
                    {
                        "block_type": "concept_explanation",
                        "component_type": "concept_explanation",
                        "title": "Misconception Alert: The 'Objective Number' Myth",
                        "content": {
                            "text": (
                                "Learners often assume that because something is expressed as a number, it represents absolute truth. "
                                "In reality, statistical summaries can mask extreme local disparities.\n\n"
                                "**The Farm Size Paradox**:\n"
                                "Consider a village where the reported average landholding is 5 acres per household. "
                                "This might sound equitable, yet it could arise because one large commercial rancher owns 100 acres while 20 smallholder families survive on just 0.25 acres each! "
                                "Without examining distributions and qualitative ground conditions, statistics can be profoundly misleading."
                            )
                        }
                    }
                ]
            },
            {
                "page_number": 4,
                "page_title": "Formative Assessment",
                "blocks": [
                    {
                        "block_type": "knowledge_check",
                        "component_type": "knowledge_check",
                        "title": "Knowledge Check: Explanatory Power of Statistics",
                        "content": {
                            "question": "Why are statistics alone insufficient for understanding complex geographical phenomena?",
                            "options": [
                                "A) Because numbers are too difficult to calculate.",
                                "B) Because statistics demonstrate patterns but do not explain the underlying causes or qualitative human experiences.",
                                "C) Because quantitative data is never accepted in modern geography.",
                                "D) Because qualitative data is always superior to quantitative measurements."
                            ],
                            "correct_answer": "B",
                            "explanation": "Statistics show trends and quantities but lack causal explanations and exclude crucial qualitative, social, and cultural contexts."
                        }
                    },
                    {
                        "block_type": "knowledge_check",
                        "component_type": "knowledge_check",
                        "title": "Knowledge Check: Interpreting Summary Averages",
                        "content": {
                            "question": "A researcher calculates that the average farm size in a rural village is 5 acres. What critical reality might this statistic conceal?",
                            "options": [
                                "A) The exact mathematical average of the farm sizes.",
                                "B) Severe inequality in land ownership, such as one wealthy farmer owning 100 acres while 20 families own 0.25 acres each.",
                                "C) The total acreage of the village.",
                                "D) The geographic coordinate boundaries of the area."
                            ],
                            "correct_answer": "B",
                            "explanation": "Summary averages can hide extreme inequality and skewness, illustrating a primary limitation of relying exclusively on central values."
                        }
                    }
                ]
            }
        ]
    },

    # Lesson 3: Types of Geographical Data
    {
        "unit_order": 3,
        "unit_name": "Types of Geographical Data",
        "lesson_title": "Types of Geographical Data",
        "pages": [
            {
                "page_number": 1,
                "page_title": "Introduction to Data Classification",
                "blocks": [
                    {
                        "block_type": "suggested_image",
                        "component_type": "suggested_image",
                        "title": "Plastic Rain Gauge for Primary Meteorological Data Collection",
                        "content": {"text": "A standard rain gauge cylinder used to collect first-hand quantitative continuous precipitation data in the field."}
                    },
                    {
                        "block_type": "learning_goal",
                        "component_type": "learning_goal",
                        "title": "Lesson Objectives: Types of Geographical Data",
                        "content": {
                            "text": (
                                "By the end of this lesson, you will be able to:\n\n"
                                "- Distinguish clearly between primary and secondary geographical data sources\n"
                                "- Contrast quantitative (numerical) and qualitative (descriptive) data types\n"
                                "- Classify quantitative variables into discrete (countable) and continuous (measurable) scales"
                            )
                        }
                    },
                    {
                        "block_type": "concept_explanation",
                        "component_type": "concept_explanation",
                        "title": "Prerequisite Spark: First-Hand vs Published Evidence",
                        "content": {
                            "text": (
                                "If you step outside with a thermometer and record the current air temperature on your school field, you have gathered primary data. "
                                "If you search an atlas or Kenya National Bureau of Statistics (KNBS) report to look up the long-term mean temperature of Nairobi, "
                                "you are utilizing secondary data. Both types have distinct strengths and applications."
                            )
                        }
                    }
                ]
            },
            {
                "page_number": 2,
                "page_title": "Primary vs Secondary & Quantitative vs Qualitative",
                "blocks": [
                    {
                        "block_type": "definition_card",
                        "component_type": "definition_card",
                        "title": "Fundamental Data Categories",
                        "content": {
                            "definitions": [
                                {
                                    "term": "Primary Data",
                                    "definition": "Raw, first-hand information collected directly from the field by the researcher for a specific purpose.",
                                    "simple": "Data you collected yourself in the field."
                                },
                                {
                                    "term": "Secondary Data",
                                    "definition": "Data that has already been collected, organized, compiled, and published by other agencies or researchers.",
                                    "simple": "Information obtained from books, reports, or existing databases."
                                },
                                {
                                    "term": "Quantitative Data",
                                    "definition": "Numerical measurements or counts that answer questions like 'how much', 'how many', or 'how frequently'.",
                                    "simple": "Information expressed as numbers (e.g., 1,200 mm of rain, 45 cars per minute)."
                                },
                                {
                                    "term": "Qualitative Data",
                                    "definition": "Descriptive, non-numerical observations representing qualities, opinions, visual textures, or perceptions.",
                                    "simple": "Information expressed as words or descriptions (e.g., 'the soil is dark, loose, and crumbly')."
                                }
                            ]
                        }
                    }
                ]
            },
            {
                "page_number": 3,
                "page_title": "Discrete vs Continuous Numerical Variables",
                "blocks": [
                    {
                        "block_type": "concept_explanation",
                        "component_type": "concept_explanation",
                        "title": "Classifying Quantitative Geographical Data",
                        "content": {
                            "text": (
                                "Quantitative data splits into two mathematical categories based on how it is measured:\n\n"
                                "1. **Discrete Data**:\n"
                                "- Can only take distinct, separate, whole values obtained by counting.\n"
                                "- Examples: Number of tractors on a farm (3, not 3.4), count of matatus at a junction, number of boreholes in a sub-county.\n\n"
                                "2. **Continuous Data**:\n"
                                "- Can take any value along an unbroken, continuous scale and is obtained by measuring with instruments.\n"
                                "- Examples: Atmospheric temperature (22.65°C), rainfall depth (14.2 mm), elevation (2,150.4 m), wind speed (18.7 km/h)."
                            )
                        }
                    },
                    {
                        "block_type": "suggested_diagram",
                        "component_type": "suggested_diagram",
                        "title": "Geographical Data Classification Hierarchy",
                        "content": {"text": "A comprehensive classification tree diagram organizing geographical data by source (Primary vs Secondary), nature (Quantitative vs Qualitative), and mathematical scale (Discrete vs Continuous)."}
                    }
                ]
            },
            {
                "page_number": 4,
                "page_title": "Comparing Primary and Secondary Sources",
                "blocks": [
                    {
                        "block_type": "concept_explanation",
                        "component_type": "concept_explanation",
                        "title": "Practical Trade-Offs in Data Sourcing",
                        "content": {
                            "text": (
                                "| Characteristic | Primary Data | Secondary Data |\n"
                                "| :--- | :--- | :--- |\n"
                                "| **Source** | Direct field investigation | Published books, KNBS, journals |\n"
                                "| **Timeliness** | Fresh, current, and customized | May be outdated or generalized |\n"
                                "| **Cost & Time** | High cost, labor-intensive | Cheap, quick to acquire |\n"
                                "| **Coverage** | Usually localized or small sample | Broad regional or national scale |\n"
                                "| **Reliability** | Controlled directly by investigator | Dependent on original author's integrity |"
                            )
                        }
                    }
                ]
            },
            {
                "page_number": 5,
                "page_title": "Formative Assessment",
                "blocks": [
                    {
                        "block_type": "knowledge_check",
                        "component_type": "knowledge_check",
                        "title": "Knowledge Check: Classifying Rainfall Measurements",
                        "content": {
                            "question": "A Grade 10 student uses a rain gauge to record daily rainfall at their school weather station. What type of data are they collecting?",
                            "options": [
                                "A) Primary, quantitative, and continuous data.",
                                "B) Secondary, qualitative, and discrete data.",
                                "C) Primary, qualitative, and continuous data.",
                                "D) Secondary, quantitative, and discrete data."
                            ],
                            "correct_answer": "A",
                            "explanation": "The data is primary because it is measured directly by the student; quantitative because it is numerical; and continuous because precipitation depth is measured on an unbroken physical scale."
                        }
                    },
                    {
                        "block_type": "knowledge_check",
                        "component_type": "knowledge_check",
                        "title": "Knowledge Check: Identifying Secondary Qualitative Data",
                        "content": {
                            "question": "Which of the following is an example of secondary qualitative geographical data?",
                            "options": [
                                "A) Counting the number of commercial shops along Moi Avenue in Mombasa.",
                                "B) Reading a 1920 colonial explorer's diary describing the dense indigenous forests of the Aberdare Ranges.",
                                "C) Measuring the pH acidity level of soil samples in a school farm.",
                                "D) Downloading 2024 population figures from the Kenya National Bureau of Statistics."
                            ],
                            "correct_answer": "B",
                            "explanation": "A historical diary is an already existing written source (secondary) that contains descriptive, non-numerical text (qualitative)."
                        }
                    }
                ]
            }
        ]
    },

    # Lesson 4: Sampling and Ethical Considerations
    {
        "unit_order": 4,
        "unit_name": "Sampling and Ethical Considerations",
        "lesson_title": "Sampling and Ethical Considerations",
        "pages": [
            {
                "page_number": 1,
                "page_title": "Introduction to Sampling & Ethics",
                "blocks": [
                    {
                        "block_type": "suggested_image",
                        "component_type": "suggested_image",
                        "title": "Fieldwork Interview with Local Farmer in Agricultural Community",
                        "content": {"text": "A field researcher conducting an ethical survey interview with a smallholder farmer in an African agricultural setting."}
                    },
                    {
                        "block_type": "learning_goal",
                        "component_type": "learning_goal",
                        "title": "Lesson Objectives: Sampling & Research Ethics",
                        "content": {
                            "text": (
                                "By the end of this lesson, you will be able to:\n\n"
                                "- Explain the importance and practical rationale of sampling in geographical fieldwork\n"
                                "- Differentiate between random, systematic, and stratified sampling methods\n"
                                "- Apply essential ethical protocols including informed consent, anonymity, and honesty"
                            )
                        }
                    },
                    {
                        "block_type": "concept_explanation",
                        "component_type": "concept_explanation",
                        "title": "Prerequisite Spark: The Feasibility Dilemma",
                        "content": {
                            "text": (
                                "Suppose you want to investigate the daily domestic water consumption of households in a sub-county with 10,000 families. "
                                "Would you interview every single family? Visiting 10,000 households would take months and require immense financial resources. "
                                "Sampling allows geographers to inspect a carefully selected, representative subset that accurately reflects the entire community."
                            )
                        }
                    }
                ]
            },
            {
                "page_number": 2,
                "page_title": "Sampling Terminology & Rationale",
                "blocks": [
                    {
                        "block_type": "definition_card",
                        "component_type": "definition_card",
                        "title": "Essential Sampling Terms",
                        "content": {
                            "definitions": [
                                {
                                    "term": "Population (Target Universe)",
                                    "definition": "The entire group of individuals, households, farms, or physical objects that the geographical inquiry focuses upon.",
                                    "simple": "The total group you want to understand."
                                },
                                {
                                    "term": "Sample",
                                    "definition": "A smaller, manageable subset of the population selected for actual measurement, counting, or surveying.",
                                    "simple": "The specific portion chosen to represent the whole."
                                },
                                {
                                    "term": "Sampling Bias",
                                    "definition": "A systematic distortion in data that occurs when certain members of the population are more likely to be selected than others, yielding misleading results.",
                                    "simple": "An unfair selection that skews the true picture."
                                }
                            ]
                        }
                    }
                ]
            },
            {
                "page_number": 3,
                "page_title": "Scientific Sampling Methods",
                "blocks": [
                    {
                        "block_type": "concept_explanation",
                        "component_type": "concept_explanation",
                        "title": "The Three Core Sampling Techniques",
                        "content": {
                            "text": (
                                "Geographers apply structured sampling frameworks to eliminate bias:\n\n"
                                "1. **Random Sampling**:\n"
                                "- Every member of the population has an equal and independent chance of being chosen.\n"
                                "- Example: Using a random number generator or pulling household numbers from a lottery container.\n\n"
                                "2. **Systematic Sampling**:\n"
                                "- Samples are chosen at regular mathematical intervals along a transect, grid, or register.\n"
                                "- Example: Surveying every 10th house along a road, or taking soil samples every 50 meters.\n\n"
                                "3. **Stratified Sampling**:\n"
                                "- The population is divided into distinct subgroups (strata) based on specific characteristics, and samples are drawn proportionally from each group.\n"
                                "- Example: Dividing farmers into small-scale (<2 acres), medium-scale (2–10 acres), and large-scale (>10 acres) to ensure all economic strata are fairly represented."
                            )
                        }
                    },
                    {
                        "block_type": "suggested_diagram",
                        "component_type": "suggested_diagram",
                        "title": "Comparison of Random, Systematic, and Stratified Sampling",
                        "content": {"text": "A clear multi-panel diagram illustrating the visual mechanics of Simple Random Sampling, Systematic Transect Sampling, and Stratified Subgroup Sampling."}
                    }
                ]
            },
            {
                "page_number": 4,
                "page_title": "Ethical Standards in Geographical Research",
                "blocks": [
                    {
                        "block_type": "concept_explanation",
                        "component_type": "concept_explanation",
                        "title": "Core Ethical Principles for Fieldwork",
                        "content": {
                            "text": (
                                "Fieldwork brings researchers into direct contact with people and ecosystems. Ethical inquiry demands:\n\n"
                                "1. **Informed Consent**: Clearly explain the study's purpose and obtain voluntary agreement before questioning respondents or recording data.\n"
                                "2. **Anonymity & Confidentiality**: Never disclose or publish respondents' personal names, mobile phone numbers, or private domestic details.\n"
                                "3. **Respect & Non-Coercion**: Respect respondents' right to decline questions. Respect local cultural norms and community leadership protocols.\n"
                                "4. **Scientific Honesty**: Never falsify, fabricate, or manipulate raw data to force a preferred hypothesis."
                            )
                        }
                    }
                ]
            },
            {
                "page_number": 5,
                "page_title": "Formative Assessment",
                "blocks": [
                    {
                        "block_type": "knowledge_check",
                        "component_type": "knowledge_check",
                        "title": "Knowledge Check: Importance of Sampling",
                        "content": {
                            "question": "Why is sampling widely utilized in geographical fieldwork?",
                            "options": [
                                "A) It guarantees that zero mathematical error will ever occur.",
                                "B) It is a practical, cost-effective method to obtain representative conclusions without examining every single member of a large population.",
                                "C) It enables researchers to deliberately exclude difficult respondents.",
                                "D) It is an administrative rule enforced only in urban areas."
                            ],
                            "correct_answer": "B",
                            "explanation": "Sampling makes data collection manageable, fast, and affordable while providing a statistically representative snapshot of the target universe."
                        }
                    },
                    {
                        "block_type": "knowledge_check",
                        "component_type": "knowledge_check",
                        "title": "Knowledge Check: Identifying Sampling Bias",
                        "content": {
                            "question": "A student investigating market waste management only interviews sellers positioned right next to the main gate because they are quickest to reach. What does this practice demonstrate?",
                            "options": [
                                "A) Stratified random sampling.",
                                "B) Sampling bias (convenience sampling).",
                                "C) Systematic spatial sampling.",
                                "D) Standard ethical protocol."
                            ],
                            "correct_answer": "B",
                            "explanation": "Interviewing only easily accessible sellers introduces convenience sampling bias because gate vendors may experience vastly different waste disposal realities than those deep inside the market."
                        }
                    }
                ]
            }
        ]
    },

    # Lesson 5: Methods of Data Collection: Observations and Measurements
    {
        "unit_order": 5,
        "unit_name": "Methods of Data Collection: Observations and Measurements",
        "lesson_title": "Methods of Data Collection: Observations and Measurements",
        "pages": [
            {
                "page_number": 1,
                "page_title": "Introduction to Field Observations",
                "blocks": [
                    {
                        "block_type": "suggested_image",
                        "component_type": "suggested_image",
                        "title": "Urban Road Traffic Flow and Vehicle Observation",
                        "content": {"text": "Road transport observation showing busy multi-vehicle traffic flow suitable for manual vehicle tallying and count recording."}
                    },
                    {
                        "block_type": "learning_goal",
                        "component_type": "learning_goal",
                        "title": "Lesson Objectives: Observations & Measurements",
                        "content": {
                            "text": (
                                "By the end of this lesson, you will be able to:\n\n"
                                "- Collect geographical data through systematic direct observation and structured counting\n"
                                "- Apply the standard five-bar tally system to record real-time discrete field counts\n"
                                "- Identify and utilize standardized instruments for measuring continuous environmental variables"
                            )
                        }
                    },
                    {
                        "block_type": "concept_explanation",
                        "component_type": "concept_explanation",
                        "title": "Prerequisite Spark: Real-Time Traffic Counting",
                        "content": {
                            "text": (
                                "Imagine standing at a busy roundabout during morning rush hour. Vehicles are speeding past every few seconds—buses, private cars, "
                                "motorbikes (bodabodas), and heavy trucks. If you tried writing numbers down on blank paper, you would quickly lose count. "
                                "Field geographers use the tally recording matrix to capture rapid discrete data without missing a beat."
                            )
                        }
                    }
                ]
            },
            {
                "page_number": 2,
                "page_title": "The Tally Recording System",
                "blocks": [
                    {
                        "block_type": "concept_explanation",
                        "component_type": "concept_explanation",
                        "title": "The Five-Bar Tally System",
                        "content": {
                            "text": (
                                "The tally system is the universal standard for recording counts in real time. Items are recorded in groups of five:\n\n"
                                "- Four vertical strokes are drawn for the first four items: `| | | |`\n"
                                "- The fifth item is marked by drawing a diagonal stroke across the four vertical lines: `||||` with diagonal strike\n"
                                "- Subsequent items start a new group of five\n\n"
                                "**Why use tallies?**\n"
                                "Tallies prevent errors because researchers do not need to perform mental arithmetic while observing. At the conclusion of the session, "
                                "calculating totals is as easy as counting in multiples of five."
                            )
                        }
                    },
                    {
                        "block_type": "suggested_diagram",
                        "component_type": "suggested_diagram",
                        "title": "Standard Tally Counting and Grouping Mechanism",
                        "content": {"text": "Vector diagram illustrating the progression of tally marks from 1 to 5, showing 4 vertical strokes crossed by a 5th diagonal strike, grouped into neat blocks."}
                    },
                    {
                        "block_type": "suggested_video",
                        "component_type": "suggested_video",
                        "title": "Manual Traffic Counting and Tally Sheet Construction",
                        "content": {
                            "resolved_video_id": "d1r5p8Z8l_Y",
                            "youtube_url": "https://www.youtube.com/watch?v=d1r5p8Z8l_Y",
                            "description": "Educational demonstration showing how urban transport planners set up lane-by-lane tally sheets and systematically categorize vehicle counts."
                        }
                    }
                ]
            },
            {
                "page_number": 3,
                "page_title": "Mechanical Measurements & Field Instruments",
                "blocks": [
                    {
                        "block_type": "concept_explanation",
                        "component_type": "concept_explanation",
                        "title": "Standardized Physical Measurement Tools",
                        "content": {
                            "text": (
                                "When gathering continuous physical data, geographers use calibrated scientific tools:\n\n"
                                "1. **Rain Gauge**:\n"
                                "- Measures liquid precipitation depth in millimeters (mm).\n"
                                "- Placed in an open area away from tall trees and buildings to prevent interception or splash errors.\n\n"
                                "2. **Thermometer (Six's Maximum & Minimum)**:\n"
                                "- Measures maximum and minimum daily atmospheric temperatures in degrees Celsius (°C).\n"
                                "- Housed inside a louvered Stevenson screen to shield the bulb from direct sunlight and artificial radiation.\n\n"
                                "3. **Surveyor's Tape Measure**:\n"
                                "- Measures horizontal distances, river channel widths, and transect intervals in meters (m) and centimeters (cm)."
                            )
                        }
                    }
                ]
            },
            {
                "page_number": 4,
                "page_title": "Formative Assessment",
                "blocks": [
                    {
                        "block_type": "knowledge_check",
                        "component_type": "knowledge_check",
                        "title": "Knowledge Check: Tally Count Interpretation",
                        "content": {
                            "question": "If you observe and count 24 cars during a 15-minute roadside survey, how should this total be represented using standard tally blocks?",
                            "options": [
                                "A) 24 individual vertical strokes without grouping.",
                                "B) Four complete groups of five tallies, plus four single vertical strokes.",
                                "C) Five complete groups of five tallies.",
                                "D) Three groups of five tallies, plus nine single strokes."
                            ],
                            "correct_answer": "B",
                            "explanation": "Four complete bundles of five equal 20, plus 4 single vertical strokes equals 24."
                        }
                    },
                    {
                        "block_type": "knowledge_check",
                        "component_type": "knowledge_check",
                        "title": "Knowledge Check: Matching Instruments with Variables",
                        "content": {
                            "question": "Which field instrument is accurately paired with the geographical variable it measures?",
                            "options": [
                                "A) Thermometer → Wind direction.",
                                "B) Rain Gauge → Liquid precipitation depth in millimeters (mm).",
                                "C) Tape Measure → Soil chemical acidity (pH).",
                                "D) Prismatic Compass → Atmospheric air pressure."
                            ],
                            "correct_answer": "B",
                            "explanation": "A rain gauge is the calibrated instrument used internationally to measure rainfall depth in millimeters."
                        }
                    }
                ]
            }
        ]
    },

    # Lesson 6: Methods of Data Collection: Questionnaires, Interviews, and Photography
    {
        "unit_order": 6,
        "unit_name": "Methods of Data Collection: Questionnaires, Interviews, and Photography",
        "lesson_title": "Methods of Data Collection: Questionnaires, Interviews, and Photography",
        "pages": [
            {
                "page_number": 1,
                "page_title": "Introduction to Questionnaires & Visual Records",
                "blocks": [
                    {
                        "block_type": "suggested_image",
                        "component_type": "suggested_image",
                        "title": "Severe Gully Erosion and Landscape Degradation",
                        "content": {"text": "Ground photograph of deep gully erosion carving through topsoil, demonstrating how photography captures environmental evidence."}
                    },
                    {
                        "block_type": "learning_goal",
                        "component_type": "learning_goal",
                        "title": "Lesson Objectives: Questionnaires, Interviews & Photography",
                        "content": {
                            "text": (
                                "By the end of this lesson, you will be able to:\n\n"
                                "- Formulate effective closed and open questions for geographical questionnaires\n"
                                "- Compare the advantages and limitations of personal interviews versus questionnaires\n"
                                "- Explain how ground photography provides objective qualitative and spatial evidence"
                            )
                        }
                    },
                    {
                        "block_type": "concept_explanation",
                        "component_type": "concept_explanation",
                        "title": "Prerequisite Spark: Capturing Landscape Evidence",
                        "content": {
                            "text": (
                                "Look at a photograph of an active gully slicing through a hillside. A table of numbers might record 'soil depth = 12 cm', "
                                "but the photograph reveals the exposed tree roots, the steep vertical sidewalls, and the nearby homestead under threat. "
                                "Ground photographs, combined with structured questions and spoken interviews, bring human and environmental realities to life."
                            )
                        }
                    }
                ]
            },
            {
                "page_number": 2,
                "page_title": "Questionnaire Design: Closed vs Open Questions",
                "blocks": [
                    {
                        "block_type": "concept_explanation",
                        "component_type": "concept_explanation",
                        "title": "Crafting Effective Questionnaire Items",
                        "content": {
                            "text": (
                                "A questionnaire is a formulated series of written questions administered to respondents.\n\n"
                                "1. **Closed (Structured) Questions**:\n"
                                "- Respondents choose from predetermined options (e.g. Yes/No, multiple-choice, or rating scales).\n"
                                "- *Example*: 'Do you apply terracing on your hillside farm? [ ] Yes  [ ] No'\n"
                                "- *Advantage*: Very fast to administer, easy to code numerically, and simple to present in bar charts or tables.\n\n"
                                "2. **Open (Unstructured) Questions**:\n"
                                "- Respondents reply in their own words without restriction.\n"
                                "- *Example*: 'Explain how erratic rainfall has impacted your household income over the past three seasons.'\n"
                                "- *Advantage*: Captures deep qualitative context, personal insights, and unexpected explanations."
                            )
                        }
                    },
                    {
                        "block_type": "suggested_diagram",
                        "component_type": "suggested_diagram",
                        "title": "Field Data Collection Toolkit Comparison",
                        "content": {"text": "Comparative diagram illustrating the three major field methods: Questionnaires (structured data), Face-to-Face Interviews (in-depth responses), and Ground Photography (visual proof)."}
                    }
                ]
            },
            {
                "page_number": 3,
                "page_title": "Interviews & Ground Photography in Fieldwork",
                "blocks": [
                    {
                        "block_type": "concept_explanation",
                        "component_type": "concept_explanation",
                        "title": "Deep Dialogues and Visual Ground Proof",
                        "content": {
                            "text": (
                                "**Personal Interviews**:\n"
                                "- Direct dialogue between researcher and respondent.\n"
                                "- Allows the researcher to clarify confusing points, ask follow-up questions, and gauge non-verbal responses.\n"
                                "- *Limitation*: Can be time-consuming and expensive across wide areas.\n\n"
                                "**Ground Photography**:\n"
                                "- Captures exact visual conditions of landforms, agricultural practices, vegetation degradation, and human settlements at a specific point in time.\n"
                                "- Serves as indisputable permanent evidence to support statistical tables in a formal geographical inquiry report."
                            )
                        }
                    }
                ]
            },
            {
                "page_number": 4,
                "page_title": "Formative Assessment",
                "blocks": [
                    {
                        "block_type": "knowledge_check",
                        "component_type": "knowledge_check",
                        "title": "Knowledge Check: Questionnaire Design",
                        "content": {
                            "question": "What is the primary advantage of utilizing closed questions in a geographical survey questionnaire?",
                            "options": [
                                "A) They encourage respondents to write lengthy essays.",
                                "B) They produce standardized responses that are quick to code, calculate, and analyze statistically.",
                                "C) They guarantee that all respondents are telling the complete truth.",
                                "D) They do not require any preparation or testing."
                            ],
                            "correct_answer": "B",
                            "explanation": "Closed questions provide fixed categories, making the resulting data clean, standardized, and easily quantifiable into tables and charts."
                        }
                    },
                    {
                        "block_type": "knowledge_check",
                        "component_type": "knowledge_check",
                        "title": "Knowledge Check: Role of Ground Photography",
                        "content": {
                            "question": "How does ground photography support numerical measurements in a soil erosion study?",
                            "options": [
                                "A) It makes the research paper visually decorative.",
                                "B) It eliminates the need for taking any physical measurements in the field.",
                                "C) It provides direct, visible visual evidence of soil erosion severity, landscape features, and crop health to contextualize numerical figures.",
                                "D) It automatically converts qualitative descriptions into GPS coordinates."
                            ],
                            "correct_answer": "C",
                            "explanation": "Photography provides authentic visual documentation of physical and human conditions that numerical figures alone cannot convey."
                        }
                    }
                ]
            }
        ]
    },

    # Lesson 7: Organizing Raw Geographical Data
    {
        "unit_order": 7,
        "unit_name": "Organizing Raw Geographical Data",
        "lesson_title": "Organizing Raw Geographical Data",
        "pages": [
            {
                "page_number": 1,
                "page_title": "Introduction to Data Organization",
                "blocks": [
                    {
                        "block_type": "suggested_image",
                        "component_type": "suggested_image",
                        "title": "Agricultural Market Produce Sorting and Inventory",
                        "content": {"text": "Produce sorting in an open-air African marketplace, representing raw goods being categorized into structured quantities."}
                    },
                    {
                        "block_type": "learning_goal",
                        "component_type": "learning_goal",
                        "title": "Lesson Objectives: Organizing Raw Data",
                        "content": {
                            "text": (
                                "By the end of this lesson, you will be able to:\n\n"
                                "- Process raw, unstructured numerical observations collected from the field\n"
                                "- Construct structured frequency tables with categories, tallies, and frequencies\n"
                                "- Audit datasets to guarantee mathematical integrity and total consistency"
                            )
                        }
                    },
                    {
                        "block_type": "concept_explanation",
                        "component_type": "concept_explanation",
                        "title": "Prerequisite Spark: The Chaos of Raw Data",
                        "content": {
                            "text": (
                                "Suppose you recorded the ages of 20 farmers attending an agricultural training session in your sub-county: "
                                "45, 23, 61, 34, 45, 52, 23, 34, 45, 61, 34, 52, 45, 23, 34, 52, 45, 61, 34, 45. "
                                "In its raw form, this list is chaotic and hard to interpret. "
                                "How do we organize these values so an agricultural extension officer can instantly identify the most active age group?"
                            )
                        }
                    }
                ]
            },
            {
                "page_number": 2,
                "page_title": "Frequency Distribution Tables",
                "blocks": [
                    {
                        "block_type": "concept_explanation",
                        "component_type": "concept_explanation",
                        "title": "Constructing a Standard Frequency Table",
                        "content": {
                            "text": (
                                "**Raw Data**: Unorganized observations directly from the field. It is difficult to detect patterns in raw data at a glance.\n\n"
                                "**Frequency Table**: A structured grid showing each distinct category or value alongside the number of times it occurs (its frequency).\n\n"
                                "**5-Step Construction Guide**:\n"
                                "1. Identify all unique categories or values in the raw dataset.\n"
                                "2. Create a table with three distinct columns: *Category / Value*, *Tally*, and *Frequency ($f$)*.\n"
                                "3. Process the raw dataset entry by entry, entering a tally stroke in the appropriate category row.\n"
                                "4. Sum the tallies for each category and write the numerical total in the Frequency column.\n"
                                "5. Calculate the overall total ($\sum f$) and verify that it matches the exact sample size."
                            )
                        }
                    },
                    {
                        "block_type": "suggested_diagram",
                        "component_type": "suggested_diagram",
                        "title": "Data Pipeline: From Raw Field Records to Frequency Table",
                        "content": {"text": "Step-by-step pipeline diagram showing raw chaotic field counts flowing through tally grouping into a clean summary frequency distribution table."}
                    }
                ]
            },
            {
                "page_number": 3,
                "page_title": "Worked Example & Data Audit",
                "blocks": [
                    {
                        "block_type": "concept_explanation",
                        "component_type": "concept_explanation",
                        "title": "Worked Example: 15-Minute Vehicle Count",
                        "content": {
                            "text": (
                                "Let us summarize a 15-minute vehicle observation dataset recorded outside a school gate:\n\n"
                                "| Vehicle Category | Tally Marks | Frequency ($f$) |\n"
                                "| :--- | :--- | :---: |\n"
                                "| **Buses** | `| |` | 2 |\n"
                                "| **Cars** | `||||` `||||` `||||` `||||` `| | | |` | 24 |\n"
                                "| **Lorries / Trucks** | `| | |` | 3 |\n"
                                "| **Motorbikes (Bodabodas)** | `||||` `|` | 6 |\n"
                                "| **Bicycles** | `| |` | 2 |\n"
                                "| **Total Sum ($\sum f$)** | | **37** |\n\n"
                                "**Data Audit Rule**:\n"
                                "Always check that the sum of the frequency column equals the total number of recorded observations ($2 + 24 + 3 + 6 + 2 = 37$). "
                                "If the totals do not match, re-audit your survey sheets to locate omitted records."
                            )
                        }
                    }
                ]
            },
            {
                "page_number": 4,
                "page_title": "Formative Assessment",
                "blocks": [
                    {
                        "block_type": "knowledge_check",
                        "component_type": "knowledge_check",
                        "title": "Knowledge Check: Purpose of Frequency Tables",
                        "content": {
                            "question": "What is the primary objective of converting raw field data into a frequency table?",
                            "options": [
                                "A) To conceal recording mistakes made during field observation.",
                                "B) To make numerical data look complex and technical.",
                                "C) To condense unorganized observations into a clear, structured format that reveals distributions and patterns at a glance.",
                                "D) To automatically convert discrete numbers into satellite coordinates."
                            ],
                            "correct_answer": "C",
                            "explanation": "Frequency tables organize raw observations into clean categories, allowing analysts to identify dominant patterns and calculate summary statistics."
                        }
                    },
                    {
                        "block_type": "knowledge_check",
                        "component_type": "knowledge_check",
                        "title": "Knowledge Check: Resolving Data Mismatches",
                        "content": {
                            "question": "If your completed frequency table sums to 35 observations, but your field logging sheet registered 38 surveyed households, what is the correct scientific action?",
                            "options": [
                                "A) Change the recorded sample size to 35 without checking.",
                                "B) Audit your raw field records line-by-line to find the 3 missing entries and correct the tally counts.",
                                "C) Discard the entire study and abandon the project.",
                                "D) Invent 3 fictitious numbers to make the total 38."
                            ],
                            "correct_answer": "B",
                            "explanation": "Scientific integrity requires auditing raw records to correct omission errors and ensure total consistency."
                        }
                    }
                ]
            }
        ]
    },

    # Lesson 8: Measures of Central Tendency: Mean, Median, and Mode
    {
        "unit_order": 8,
        "unit_name": "Measures of Central Tendency: Mean, Median, and Mode",
        "lesson_title": "Measures of Central Tendency: Mean, Median, and Mode",
        "pages": [
            {
                "page_number": 1,
                "page_title": "Introduction to Central Tendency",
                "blocks": [
                    {
                        "block_type": "suggested_image",
                        "component_type": "suggested_image",
                        "title": "Tea Estate Worker and Tea Farm Harvest in Kericho",
                        "content": {"text": "A lush tea plantation in Kericho County, representing commercial agricultural yields analyzed using statistical measures of central tendency."}
                    },
                    {
                        "block_type": "learning_goal",
                        "component_type": "learning_goal",
                        "title": "Lesson Objectives: Central Tendency",
                        "content": {
                            "text": (
                                "By the end of this lesson, you will be able to:\n\n"
                                "- Calculate the arithmetic mean, median, and mode for geographical datasets\n"
                                "- Interpret the geographical meaning and appropriate application of each measure\n"
                                "- Evaluate how extreme outlier values distort the arithmetic mean versus the median"
                            )
                        }
                    },
                    {
                        "block_type": "concept_explanation",
                        "component_type": "concept_explanation",
                        "title": "Prerequisite Spark: Finding the Typical Value",
                        "content": {
                            "text": (
                                "If a foreign tea buyer asks, 'What is the typical annual harvest of tea farms in Kericho?', "
                                "you cannot list the exact figures for all hundreds of farms. You need a single representative number that captures the center of the data. "
                                "Measures of central tendency—Mean, Median, and Mode—provide mathematical ways to summarize the 'middle' of a dataset."
                            )
                        }
                    }
                ]
            },
            {
                "page_number": 2,
                "page_title": "Definitions & Mathematical Formulas",
                "blocks": [
                    {
                        "block_type": "definition_card",
                        "component_type": "definition_card",
                        "title": "The Three Measures of Central Tendency",
                        "content": {
                            "definitions": [
                                {
                                    "term": "Arithmetic Mean",
                                    "definition": "The mathematical average calculated by dividing the sum of all values by the total number of observations: Mean = (Sum of x) / n.",
                                    "simple": "The balance point if everything was shared out equally."
                                },
                                {
                                    "term": "Median",
                                    "definition": "The exact middle value when a dataset is arranged in ascending or descending numerical order. For an even number of values, it is the average of the two middle numbers.",
                                    "simple": "The middle score that splits the top 50% from the bottom 50%."
                                },
                                {
                                    "term": "Mode",
                                    "definition": "The specific value or category that appears most frequently in a dataset.",
                                    "simple": "The most common or popular value."
                                }
                            ]
                        }
                    }
                ]
            },
            {
                "page_number": 3,
                "page_title": "Step-by-Step Mathematical Walkthrough",
                "blocks": [
                    {
                        "block_type": "concept_explanation",
                        "component_type": "concept_explanation",
                        "title": "Worked Example: Kericho Tea Farm Harvests",
                        "content": {
                            "text": (
                                "Let us analyze the annual tea harvest (in thousands of tonnes) of a sample of 7 farms in Kericho County:\n"
                                "**12, 15, 12, 18, 25, 12, 32**\n\n"
                                "**Step 1: Calculate the Mean ($\bar{x}$)**\n"
                                "- Sum of all harvests: $12 + 15 + 12 + 18 + 25 + 12 + 32 = 126$ thousand tonnes.\n"
                                "- Total number of farms ($n$): $7$.\n"
                                "- $\text{Mean} = \frac{126}{7} = 18$ thousand tonnes.\n"
                                "- *Geographical Meaning*: If total tea production were shared equally across all sampled farms, each would produce 18,000 tonnes.\n\n"
                                "**Step 2: Calculate the Median**\n"
                                "- Sort values in ascending order: **12, 12, 12, 15, 18, 25, 32**.\n"
                                "- Identify the middle item ($4^{\text{th}}$ position): **15** thousand tonnes.\n"
                                "- *Geographical Meaning*: Exactly half of the farms produce less than 15,000 tonnes, while half produce more.\n\n"
                                "**Step 3: Identify the Mode**\n"
                                "- The value **12** appears three times (more than any other).\n"
                                "- *Mode* = **12** thousand tonnes (the most common harvest size)."
                            )
                        }
                    }
                ]
            },
            {
                "page_number": 4,
                "page_title": "Outlier Distortion & Misconception Alert",
                "blocks": [
                    {
                        "block_type": "concept_explanation",
                        "component_type": "concept_explanation",
                        "title": "Misconception Alert: The Vulnerability of the Mean",
                        "content": {
                            "text": (
                                "Students frequently assume the arithmetic mean is always the best measure of central tendency. "
                                "However, the mean is heavily distorted by extreme values (outliers).\n\n"
                                "**The Outlier Impact**:\n"
                                "In a survey of 5 households' weekly water usage: **200 L, 220 L, 210 L, 250 L, 920 L** (where one home filled a commercial tanker).\n"
                                "- The Mean is $\frac{1800}{5} = 360$ L (higher than 4 out of 5 households!).\n"
                                "- The Median is **220 L**, which accurately reflects what typical families consume.\n"
                                "When extreme outliers exist, the **median** is a much more robust measure."
                            )
                        }
                    },
                    {
                        "block_type": "suggested_diagram",
                        "component_type": "suggested_diagram",
                        "title": "Central Tendency Skew and Outlier Distribution Visualizer",
                        "content": {"text": "A comparative balance beam diagram demonstrating how an extreme outlier pulls the Mean far to the right, while the Median remains stably anchored at the true middle."}
                    }
                ]
            },
            {
                "page_number": 5,
                "page_title": "Formative Assessment",
                "blocks": [
                    {
                        "block_type": "knowledge_check",
                        "component_type": "knowledge_check",
                        "title": "Knowledge Check: Outlier Effects on Measures",
                        "content": {
                            "question": "Given the weekly water consumption of 5 households: 200 L, 220 L, 210 L, 250 L, 920 L. Why is the median (220 L) a superior representative measure compared to the mean (360 L)?",
                            "options": [
                                "A) The median is easier to calculate.",
                                "B) The mean is distorted by the extreme outlier (920 L), which is uncharacteristic of typical households.",
                                "C) The mean can never be calculated for liquid volumes.",
                                "D) Outliers always make the median mathematically incorrect."
                            ],
                            "correct_answer": "B",
                            "explanation": "Outliers heavily pull the mean away from the true cluster of data, making the median a much more representative indicator of typical conditions."
                        }
                    },
                    {
                        "block_type": "knowledge_check",
                        "component_type": "knowledge_check",
                        "title": "Knowledge Check: Calculating the Mode",
                        "content": {
                            "question": "A five-day temperature recording log registers: 24°C, 26°C, 24°C, 28°C, 30°C. What is the mode?",
                            "options": [
                                "A) 26.4°C",
                                "B) 26°C",
                                "C) 24°C",
                                "D) 30°C"
                            ],
                            "correct_answer": "C",
                            "explanation": "24°C is the mode because it appears twice, having a higher frequency than any other recorded temperature."
                        }
                    }
                ]
            }
        ]
    },

    # Lesson 9: Data Presentation: Simple and Grouped Bar Graphs
    {
        "unit_order": 9,
        "unit_name": "Data Presentation: Simple and Grouped Bar Graphs",
        "lesson_title": "Data Presentation: Simple and Grouped Bar Graphs",
        "pages": [
            {
                "page_number": 1,
                "page_title": "Introduction to Bar Graphs",
                "blocks": [
                    {
                        "block_type": "suggested_image",
                        "component_type": "suggested_image",
                        "title": "Nairobi Highway Traffic and Matatu Public Transport Flow",
                        "content": {"text": "Busy urban transport corridor in Nairobi with commercial buses, cars, and matatus, illustrating categorical transport data."}
                    },
                    {
                        "block_type": "learning_goal",
                        "component_type": "learning_goal",
                        "title": "Lesson Objectives: Bar Graphs",
                        "content": {
                            "text": (
                                "By the end of this lesson, you will be able to:\n\n"
                                "- Construct accurate simple and grouped (comparative) bar graphs with appropriate scales and labels\n"
                                "- Apply cartographic rules including equal bar widths and equal spacing between discrete bars\n"
                                "- Evaluate the advantages and limitations of bar graphs in geographical communication"
                            )
                        }
                    },
                    {
                        "block_type": "concept_explanation",
                        "component_type": "concept_explanation",
                        "title": "Prerequisite Spark: Visualizing Quantities",
                        "content": {
                            "text": (
                                "Tables of numbers require mental effort to scan and compare. But when those numbers become colored rectangular bars, "
                                "the tallest bar immediately grabs your attention. Bar graphs translate abstract numbers into immediate visual heights."
                            )
                        }
                    }
                ]
            },
            {
                "page_number": 2,
                "page_title": "Bar Graph Types & Construction Guidelines",
                "blocks": [
                    {
                        "block_type": "concept_explanation",
                        "component_type": "concept_explanation",
                        "title": "Simple vs Grouped Bar Graphs",
                        "content": {
                            "text": (
                                "1. **Simple Bar Graph**:\n"
                                "- Uses rectangular bars of equal width to show values for distinct discrete categories.\n"
                                "- Height or length of each bar is directly proportional to the value it represents.\n\n"
                                "2. **Grouped (Comparative) Bar Graph**:\n"
                                "- Places multiple bars side-by-side for each category to compare two or more variables simultaneously (e.g. comparing Nairobi vs Mombasa monthly rainfall).\n\n"
                                "**Cartographic Construction Rules**:\n"
                                "1. Draw vertical Y-axis (dependent variable/frequency) and horizontal X-axis (independent categorical variable).\n"
                                "2. Choose a uniform, easy-to-read scale for the Y-axis (e.g. 1 cm = 5 units).\n"
                                "3. Maintain **equal widths** for all bars.\n"
                                "4. Leave **equal spaces** between bars to indicate discrete categories.\n"
                                "5. Label both axes clearly and provide a comprehensive title."
                            )
                        }
                    }
                ]
            },
            {
                "page_number": 3,
                "page_title": "Worked Construction & Vector Visual",
                "blocks": [
                    {
                        "block_type": "concept_explanation",
                        "component_type": "concept_explanation",
                        "title": "Worked Example: Plotting School Gate Traffic",
                        "content": {
                            "text": (
                                "Let us plot our 15-minute traffic count data (Buses: 2, Cars: 24, Lorries: 3, Motorbikes: 6, Bicycles: 2):\n\n"
                                "- **X-axis**: Categorical vehicle classes.\n"
                                "- **Y-axis**: Number of vehicles (scale 0 to 30).\n"
                                "- **Visual Pattern**: The 'Cars' bar towers over all other categories at 24 units, making private cars the dominant transport mode at a glance."
                            )
                        }
                    },
                    {
                        "block_type": "suggested_diagram",
                        "component_type": "suggested_diagram",
                        "title": "Publication-Quality Simple Bar Graph of Traffic Volume",
                        "content": {"text": "A precision-drawn simple bar graph displaying vehicle counts with scaled Y-axis, labeled X-axis categories, distinct bar heights, and equal discrete spacing."}
                    }
                ]
            },
            {
                "page_number": 4,
                "page_title": "Formative Assessment",
                "blocks": [
                    {
                        "block_type": "knowledge_check",
                        "component_type": "knowledge_check",
                        "title": "Knowledge Check: Best Use of Bar Graphs",
                        "content": {
                            "question": "Which type of geographical data is most appropriately presented using a simple bar graph?",
                            "options": [
                                "A) Continuous temperature variations over a 100-year timescale.",
                                "B) Discrete, categorical data, such as crop yields across different Kenyan counties.",
                                "C) Continuous elevation profiles along a mountain hiking path.",
                                "D) Qualitative diary entries about climate perceptions."
                            ],
                            "correct_answer": "B",
                            "explanation": "Bar graphs are specifically suited for discrete, categorical data where distinct classes or regions are compared."
                        }
                    },
                    {
                        "block_type": "knowledge_check",
                        "component_type": "knowledge_check",
                        "title": "Knowledge Check: Cartographic Spacing Rule",
                        "content": {
                            "question": "Why is it mandatory to leave uniform spaces between adjacent bars on a standard simple bar graph?",
                            "options": [
                                "A) To make the graph look decorative and colorful.",
                                "B) To emphasize that the categories are discrete and distinct, unlike continuous data which flows without gaps.",
                                "C) To save ink during printing.",
                                "D) To match the horizontal scale of a topographical map."
                            ],
                            "correct_answer": "B",
                            "explanation": "Spaces between bars signify discrete, distinct categories, clearly separating bar graphs from continuous histograms."
                        }
                    }
                ]
            }
        ]
    },

    # Lesson 10: Data Presentation: Histograms, Pictograms, and Pie Charts
    {
        "unit_order": 10,
        "unit_name": "Data Presentation: Histograms, Pictograms, and Pie Charts",
        "lesson_title": "Data Presentation: Histograms, Pictograms, and Pie Charts",
        "pages": [
            {
                "page_number": 1,
                "page_title": "Introduction to Proportional Presentation",
                "blocks": [
                    {
                        "block_type": "suggested_image",
                        "component_type": "suggested_image",
                        "title": "Agricultural Land Use Parcels and Crop Fields in Kenya",
                        "content": {"text": "Farmland showing distinct parcel divisions of maize and cash crops, illustrating proportional land-use distributions."}
                    },
                    {
                        "block_type": "learning_goal",
                        "component_type": "learning_goal",
                        "title": "Lesson Objectives: Histograms & Pie Charts",
                        "content": {
                            "text": (
                                "By the end of this lesson, you will be able to:\n\n"
                                "- Distinguish clearly between bar graphs (discrete) and histograms (continuous)\n"
                                "- Interpret and construct pictograms using standard symbolic keys\n"
                                "- Calculate sector angles and draw precision pie charts representing proportions and percentages"
                            )
                        }
                    },
                    {
                        "block_type": "concept_explanation",
                        "component_type": "concept_explanation",
                        "title": "Prerequisite Spark: Slicing the Land",
                        "content": {
                            "text": (
                                "If a school farm covers 100 hectares, how can we show at a glance what fraction is devoted to maize, beans, and coffee? "
                                "A pie chart turns the full circle (360°) into a proportional representation of the whole farm."
                            )
                        }
                    }
                ]
            },
            {
                "page_number": 2,
                "page_title": "Histograms vs Bar Graphs & Pictograms",
                "blocks": [
                    {
                        "block_type": "concept_explanation",
                        "component_type": "concept_explanation",
                        "title": "Presentation Formats for Different Data Types",
                        "content": {
                            "text": (
                                "1. **Histograms**:\n"
                                "- Designed specifically for **continuous numerical data** divided into class intervals (e.g. temperature ranges: 10–15°C, 15–20°C, 20–25°C).\n"
                                "- Unlike bar graphs, there are **NO spaces between the bars** because the data forms an unbroken continuum.\n\n"
                                "2. **Pictograms**:\n"
                                "- Utilize repetitive graphic symbols or icons to represent fixed quantities (e.g. 1 sack icon = 100 bags of maize).\n"
                                "- Highly engaging for public displays, though less precise for fine mathematical analysis."
                            )
                        }
                    }
                ]
            },
            {
                "page_number": 3,
                "page_title": "Pie Charts: Mathematical Calculation & Construction",
                "blocks": [
                    {
                        "block_type": "concept_explanation",
                        "component_type": "concept_explanation",
                        "title": "Calculating Sector Angles for Pie Charts",
                        "content": {
                            "text": (
                                "A pie chart is a circular statistical graphic where each sector's angle is directly proportional to its share of the total.\n\n"
                                "**Angle Formula**:\n"
                                "$$\text{Sector Angle} = \left(\frac{\text{Component Value}}{\text{Total Value}}\right) \times 360^\circ$$\n\n"
                                "**Worked Example: School Farm Land Use (100 Hectares Total)**:\n"
                                "- **Maize** (50 ha): $\left(\frac{50}{100}\right) \times 360^\circ = 180^\circ$ (exactly half the circle / 50%)\n"
                                "- **Beans** (30 ha): $\left(\frac{30}{100}\right) \times 360^\circ = 108^\circ$ (30%)\n"
                                "- **Coffee** (20 ha): $\left(\frac{20}{100}\right) \times 360^\circ = 72^\circ$ (20%)\n"
                                "- **Sum Check**: $180^\circ + 108^\circ + 72^\circ = 360^\circ$ (100%)."
                            )
                        }
                    },
                    {
                        "block_type": "suggested_diagram",
                        "component_type": "suggested_diagram",
                        "title": "Proportional Pie Chart of Agricultural Land Allocation",
                        "content": {"text": "A precision vector pie chart with labeled sectors for Maize (180° / 50%), Beans (108° / 30%), and Coffee (72° / 20%) with high-contrast color shading and key."}
                    }
                ]
            },
            {
                "page_number": 4,
                "page_title": "Formative Assessment",
                "blocks": [
                    {
                        "block_type": "knowledge_check",
                        "component_type": "knowledge_check",
                        "title": "Knowledge Check: Histogram vs Bar Chart",
                        "content": {
                            "question": "What is the primary structural difference between a simple bar chart and a histogram?",
                            "options": [
                                "A) Bar charts are drawn horizontally, while histograms are always drawn vertically.",
                                "B) Bar charts represent discrete categories with spaces between bars, whereas histograms represent continuous data with no spaces between bars.",
                                "C) Histograms use pictorial icons, while bar charts use lines.",
                                "D) Bar charts are used in human geography, while histograms are only used in physical geography."
                            ],
                            "correct_answer": "B",
                            "explanation": "Histograms display continuous grouped data without gaps between adjacent bars, whereas bar charts display distinct discrete categories with gaps."
                        }
                    },
                    {
                        "block_type": "knowledge_check",
                        "component_type": "knowledge_check",
                        "title": "Knowledge Check: Calculating Pie Chart Sector Angles",
                        "content": {
                            "question": "A student constructs a pie chart showing energy sources in a town: Hydroelectric (60%), Geothermal (30%), and Diesel (10%). What is the correct sector angle for Geothermal energy?",
                            "options": [
                                "A) 30°",
                                "B) 60°",
                                "C) 108°",
                                "D) 120°"
                            ],
                            "correct_answer": "C",
                            "explanation": "Sector Angle = 30% of 360° = 0.30 × 360° = 108°."
                        }
                    }
                ]
            }
        ]
    },

    # Lesson 11: Data Presentation: Combined Bar and Line Graphs (Climographs)
    {
        "unit_order": 11,
        "unit_name": "Data Presentation: Combined Bar and Line Graphs (Climographs)",
        "lesson_title": "Data Presentation: Combined Bar and Line Graphs (Climographs)",
        "pages": [
            {
                "page_number": 1,
                "page_title": "Introduction to Combined Climatic Graphs",
                "blocks": [
                    {
                        "block_type": "suggested_image",
                        "component_type": "suggested_image",
                        "title": "Seasonal Weather and Rain Clouds over Kenyan Landscape",
                        "content": {"text": "A panoramic landscape showing shifting seasonal cloud cover and precipitation patterns over Kenya."}
                    },
                    {
                        "block_type": "learning_goal",
                        "component_type": "learning_goal",
                        "title": "Lesson Objectives: Combined Climatic Graphs",
                        "content": {
                            "text": (
                                "By the end of this lesson, you will be able to:\n\n"
                                "- Construct a dual-axis combined bar and line graph representing rainfall and temperature\n"
                                "- Follow standard cartographic conventions (bars for rainfall totals, line for temperature averages)\n"
                                "- Interpret climographs to deduce seasonal regimes, bimodal rainfall, and agricultural viability"
                            )
                        }
                    },
                    {
                        "block_type": "concept_explanation",
                        "component_type": "concept_explanation",
                        "title": "Prerequisite Spark: Two Climate Variables on One Grid",
                        "content": {
                            "text": (
                                "Temperature and rainfall operate together to create climate. Plotting them on two separate graphs makes it difficult "
                                "to see if the hottest months coincide with the wettest periods. A combined climograph unifies both variables on a single dual-axis chart."
                            )
                        }
                    }
                ]
            },
            {
                "page_number": 2,
                "page_title": "Dual-Axis Graph Architecture & Conventions",
                "blocks": [
                    {
                        "block_type": "concept_explanation",
                        "component_type": "concept_explanation",
                        "title": "Standard Rules for Combined Climographs",
                        "content": {
                            "text": (
                                "A combined climograph uses two vertical Y-axes sharing a common horizontal X-axis (12 months, Jan–Dec):\n\n"
                                "1. **Rainfall (Left Y-Axis)**:\n"
                                "- Scaled in millimeters (mm).\n"
                                "- Represented by **vertical blue bars** because monthly rainfall is a discrete total sum.\n\n"
                                "2. **Temperature (Right Y-Axis)**:\n"
                                "- Scaled in degrees Celsius (°C).\n"
                                "- Represented by a **continuous red line** connecting monthly average points, because temperature changes continuously across the year."
                            )
                        }
                    },
                    {
                        "block_type": "suggested_video",
                        "component_type": "suggested_video",
                        "title": "Constructing and Interpreting a Dual-Axis Climate Graph",
                        "content": {
                            "resolved_video_id": "x1Y_9uO9e28",
                            "youtube_url": "https://www.youtube.com/watch?v=x1Y_9uO9e28",
                            "description": "Step-by-step video tutorial demonstrating the dual-axis setup, plotting rainfall bars, and drawing the temperature curve."
                        }
                    }
                ]
            },
            {
                "page_number": 3,
                "page_title": "Worked Climatic Analysis: Nairobi",
                "blocks": [
                    {
                        "block_type": "concept_explanation",
                        "component_type": "concept_explanation",
                        "title": "Nairobi 12-Month Climate Data & Deduction",
                        "content": {
                            "text": (
                                "| Month | Jan | Feb | Mar | Apr | May | Jun | Jul | Aug | Sep | Oct | Nov | Dec |\n"
                                "| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |\n"
                                "| **Rainfall (mm)** | 50 | 40 | 80 | 120 | 100 | 60 | 30 | 40 | 50 | 90 | 130 | 110 |\n"
                                "| **Temp (°C)** | 21 | 22 | 22 | 21 | 20 | 18 | 17 | 18 | 19 | 20 | 20 | 21 |\n\n"
                                "**Climatic Deductions**:\n"
                                "- **Wettest Peak**: November (130 mm) and April (120 mm).\n"
                                "- **Driest Month**: July (30 mm).\n"
                                "- **Rainfall Pattern**: Classic **bimodal rainfall regime** with two distinct peaks (March–May long rains and Oct–Dec short rains).\n"
                                "- **Temperature Range**: Mild equatorial highland temperatures ranging from 17°C in July to 22°C in February/March."
                            )
                        }
                    },
                    {
                        "block_type": "suggested_diagram",
                        "component_type": "suggested_diagram",
                        "title": "Nairobi Combined Climatograph Dual-Axis Graph",
                        "content": {"text": "Dual-axis vector climograph of Nairobi showing monthly rainfall blue bars (left axis) and monthly temperature red line curve (right axis) across 12 months."}
                    }
                ]
            },
            {
                "page_number": 4,
                "page_title": "Formative Assessment",
                "blocks": [
                    {
                        "block_type": "knowledge_check",
                        "component_type": "knowledge_check",
                        "title": "Knowledge Check: Cartographic Climate Graph Conventions",
                        "content": {
                            "question": "On a standard dual-axis combined climate graph, how are rainfall and temperature conventionally represented?",
                            "options": [
                                "A) Rainfall is drawn as a line, and temperature as vertical bars.",
                                "B) Both variables are drawn as lines of different colors.",
                                "C) Rainfall is represented by vertical bars, and temperature is represented by a continuous line.",
                                "D) Both variables are represented using pictograms."
                            ],
                            "correct_answer": "C",
                            "explanation": "Standard international cartographic convention requires discrete monthly precipitation totals to be plotted as vertical bars and continuous temperature averages as a continuous line."
                        }
                    },
                    {
                        "block_type": "knowledge_check",
                        "component_type": "knowledge_check",
                        "title": "Knowledge Check: Identifying Rainfall Regimes",
                        "content": {
                            "question": "Based on Nairobi's monthly climate data showing peaks in April (120 mm) and November (130 mm), how is its rainfall regime classified?",
                            "options": [
                                "A) Unimodal rainfall (single wet season).",
                                "B) Arid desert regime.",
                                "C) Bimodal rainfall (two distinct wet seasons during the year).",
                                "D) Completely uniform rainfall throughout all 12 months."
                            ],
                            "correct_answer": "C",
                            "explanation": "Two distinct seasonal precipitation peaks in a year constitute a classic bimodal rainfall regime."
                        }
                    }
                ]
            }
        ]
    },

    # Lesson 12: School-Based Geographical Inquiry Project
    {
        "unit_order": 12,
        "unit_name": "School-Based Geographical Inquiry Project",
        "lesson_title": "School-Based Geographical Inquiry Project",
        "pages": [
            {
                "page_number": 1,
                "page_title": "Introduction to the Inquiry Project",
                "blocks": [
                    {
                        "block_type": "suggested_image",
                        "component_type": "suggested_image",
                        "title": "Students Conducting Fieldwork and Environmental Survey",
                        "content": {"text": "Secondary school students collaborating in the field to collect and record environmental geographical data."}
                    },
                    {
                        "block_type": "learning_goal",
                        "component_type": "learning_goal",
                        "title": "Lesson Objectives: Inquiry Project",
                        "content": {
                            "text": (
                                "By the end of this lesson, you will be able to:\n\n"
                                "- Design and execute a simple, ethical school-based geographical statistical inquiry\n"
                                "- Synthesize data collection, tallying, central tendency calculations, and graphing into a formal report\n"
                                "- Formulate evidence-based geographical conclusions and actionable recommendations"
                            )
                        }
                    },
                    {
                        "block_type": "concept_explanation",
                        "component_type": "concept_explanation",
                        "title": "Prerequisite Spark: Becoming the Geographer",
                        "content": {
                            "text": (
                                "You have mastered data types, sampling, instruments, tables, averages, and charts. "
                                "Now it is time to put these tools together to solve a real problem in your school or local community through a hands-on inquiry project."
                            )
                        }
                    }
                ]
            },
            {
                "page_number": 2,
                "page_title": "The Inquiry Cycle & Topic Selection",
                "blocks": [
                    {
                        "block_type": "concept_explanation",
                        "component_type": "concept_explanation",
                        "title": "The 6-Stage Geographical Inquiry Cycle",
                        "content": {
                            "text": (
                                "Every scientific geographical investigation follows six sequential phases:\n\n"
                                "1. **Define Question**: Formulate a clear, testable research problem.\n"
                                "2. **Design Plan**: Select sampling method, tools, and ethical consent protocols.\n"
                                "3. **Collect Data**: Gather field observations, tallies, measurements, or questionnaire responses.\n"
                                "4. **Organize & Calculate**: Compile frequency tables and calculate Mean, Median, and Mode.\n"
                                "5. **Present & Interpret**: Draw bar charts, pie charts, or climographs and explain the spatial patterns.\n"
                                "6. **Conclude & Recommend**: Summarize findings, state limitations, and propose solutions.\n\n"
                                "**Manageable School Project Topics**:\n"
                                "- *Topic A (Weather)*: Monitor daily school temperatures and rainfall over 14 days.\n"
                                "- *Topic B (Waste Audit)*: Sort and weigh plastic, organic, and paper waste produced by classes daily.\n"
                                "- *Topic C (Mobility)*: Survey student transport modes and daily travel distances."
                            )
                        }
                    },
                    {
                        "block_type": "suggested_diagram",
                        "component_type": "suggested_diagram",
                        "title": "The 6-Stage Geographical Inquiry Framework",
                        "content": {"text": "A cyclical flowchart diagram detailing the 6 phases of geographical inquiry from problem definition to data collection, analysis, and final reporting."}
                    }
                ]
            },
            {
                "page_number": 3,
                "page_title": "Report Structure & Safety Precautions",
                "blocks": [
                    {
                        "block_type": "concept_explanation",
                        "component_type": "concept_explanation",
                        "title": "Scientific Report Format & Field Safety",
                        "content": {
                            "text": (
                                "**Formal Inquiry Report Structure**:\n"
                                "1. *Title Page*: Title, student names, admission numbers, date.\n"
                                "2. *Introduction*: Problem statement and geographical objectives.\n"
                                "3. *Methodology*: Tools used, sampling technique, and sample size.\n"
                                "4. *Data Presentation & Analysis*: Tables, graphs, and central tendency calculations.\n"
                                "5. *Discussion*: Explaining patterns and geographical meaning.\n"
                                "6. *Conclusion & Recommendations*: Key discoveries and proposed practical solutions.\n"
                                "7. *Limitations*: Honest disclosure of data gaps, sample constraints, or measurement errors.\n\n"
                                "**Field Safety Protocols**:\n"
                                "- *Waste Audit*: Always wear thick protective rubber gloves and face masks. Never touch broken glass or biohazardous medical waste.\n"
                                "- *Weather Station*: Never collect data during active thunderstorms or lightning."
                            )
                        }
                    }
                ]
            },
            {
                "page_number": 4,
                "page_title": "Formative Assessment",
                "blocks": [
                    {
                        "block_type": "knowledge_check",
                        "component_type": "knowledge_check",
                        "title": "Knowledge Check: Starting an Inquiry",
                        "content": {
                            "question": "What is the essential first stage when embarking on a school-based geographical inquiry project?",
                            "options": [
                                "A) Drawing final conclusion charts.",
                                "B) Formulating a clear, researchable geographical question or problem statement.",
                                "C) Writing the final recommendations.",
                                "D) Publishing results online."
                            ],
                            "correct_answer": "B",
                            "explanation": "Every valid scientific inquiry begins by clearly defining the research problem and specific questions to guide data collection."
                        }
                    },
                    {
                        "block_type": "knowledge_check",
                        "component_type": "knowledge_check",
                        "title": "Knowledge Check: Rationale for Limitations Section",
                        "content": {
                            "question": "Why is it vital to include an honest 'Limitations' section in a geographical research report?",
                            "options": [
                                "A) To make the report appear longer.",
                                "B) To identify potential error sources and data constraints, enabling others to evaluate conclusions honestly.",
                                "C) It is a required qualification for publishing.",
                                "D) It proves that no errors occurred during fieldwork."
                            ],
                            "correct_answer": "B",
                            "explanation": "Acknowledging limitations maintains scientific honesty and allows readers to understand the boundaries and precision of the findings."
                        }
                    }
                ]
            }
        ]
    }
]

def run_ingestion():
    print("=" * 70)
    print("VLearn CBC Grade 10 Geography — Topic 3: Statistical Methods Ingestion")
    print("=" * 70)

    curriculum = Curriculum.objects.filter(name__iexact="CBC").first()
    if not curriculum:
        print("ERROR: Curriculum 'CBC' not found.")
        sys.exit(1)

    grade = Grade.objects.filter(curriculum=curriculum, name__icontains="10").first()
    if not grade:
        print("ERROR: Grade 10 not found under CBC.")
        sys.exit(1)

    subject = Subject.objects.filter(grade=grade, name="Geography").first()
    if not subject:
        print("ERROR: Subject 'Geography' not found under Grade 10.")
        sys.exit(1)

    print(f"Target: Curriculum={curriculum.name}, Grade={grade.name}, Subject={subject.name} (ID: {subject.id})")

    with transaction.atomic():
        topic, created = Topic.objects.get_or_create(
            subject=subject,
            order=3,
            defaults={
                "name": "Statistical Methods",
                "description": (
                    "Collection, organization, analysis, interpretation, and presentation of numerical geographical data. "
                    "Covers data types, sampling, tally systems, measures of central tendency, bar graphs, pie charts, "
                    "climographs, and school-based inquiry projects."
                )
            }
        )
        if not created and topic.name != "Statistical Methods":
            topic.name = "Statistical Methods"
            topic.description = (
                "Collection, organization, analysis, interpretation, and presentation of numerical geographical data. "
                "Covers data types, sampling, tally systems, measures of central tendency, bar graphs, pie charts, "
                "climographs, and school-based inquiry projects."
            )
            topic.save()

        print(f"Topic 3: '{topic.name}' (ID: {topic.id}) - {'Created' if created else 'Ready'}")

        total_units = 0
        total_lessons = 0
        total_blocks = 0

        for l_data in LESSONS_DATA:
            u_order = l_data["unit_order"]
            u_name = l_data["unit_name"]
            l_title = l_data["lesson_title"]

            unit, u_created = LearningUnit.objects.get_or_create(
                topic=topic,
                order=u_order,
                defaults={
                    "name": u_name,
                    "description": f"Unit {u_order}: {u_name} in Grade 10 Geography."
                }
            )
            if not u_created and unit.name != u_name:
                unit.name = u_name
                unit.description = f"Unit {u_order}: {u_name} in Grade 10 Geography."
                unit.save()

            total_units += 1

            lesson, l_created = Lesson.objects.get_or_create(
                learning_unit=unit,
                defaults={
                    "topic": topic,
                    "title": l_title,
                    "status": "published",
                    "version": 1
                }
            )
            if not l_created:
                lesson.title = l_title
                lesson.topic = topic
                lesson.status = "published"
                lesson.version = 1
                lesson.save()

            total_lessons += 1

            # Remove existing blocks to ensure clean idempotent rebuild
            LessonBlock.objects.filter(lesson=lesson).delete()

            block_count = 0
            for page in l_data["pages"]:
                p_num = page["page_number"]
                p_title = clean_text(page.get("page_title", ""))

                for comp_idx, block_def in enumerate(page["blocks"], start=1):
                    b_type = block_def["block_type"]
                    c_type = block_def.get("component_type", b_type)
                    b_title = clean_text(block_def["title"])
                    b_content = clean_content_dict(block_def["content"])

                    LessonBlock.objects.create(
                        lesson=lesson,
                        page_number=p_num,
                        component_order=comp_idx,
                        block_type=b_type,
                        component_type=c_type,
                        title=b_title,
                        content=b_content
                    )
                    block_count += 1
                    total_blocks += 1

            print(f"  ✓ Unit {u_order}: Lesson '{l_title}' -> {len(l_data['pages'])} pages, {block_count} blocks")

    print("=" * 70)
    print(f"INGESTION COMPLETE: {total_units} Units, {total_lessons} Lessons, {total_blocks} Blocks.")
    print("=" * 70)

if __name__ == "__main__":
    run_ingestion()
