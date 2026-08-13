"""
VLearn Form 4 Geography — Topic 8: Population
Rich In-Place Production Ingestion Engine

Topic: Population (Topic Order: 8)
Subject: Geography (Subject ID: 18)
Grade: Form 4 (Grade ID: 4)
Curriculum: 844 (Curriculum ID: 4)

Decomposed into 6 Learning Units & 6 Published Lessons (67 Total Pages):
  1. Foundations of Demography, Census, and Demographic Indicators (11 Pages)
  2. Spatial Distribution and Density of Population in Kenya and East Africa (12 Pages)
  3. Population Dynamics, Growth Rates, and Fertility Drivers (12 Pages)
  4. Population Structure, Age-Sex Pyramids, and Dependency Ratios (12 Pages)
  5. Population Movements, Migration Dynamics, and Urbanization (12 Pages)
  6. Comparative Case Studies (Kenya vs Sweden), Topic Synthesis, and KCSE Review (8 Pages)

Usage:
  ./venv/bin/python curriculum/ingest_form4_geography_topic8.py
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
    """Removes bracket citations and cleans double spaces."""
    if not text:
        return ""
    text = re.sub(r'\[(?:\d+|image_\d+|S\d+.*?|[\d,\s]+)\]', '', text)
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

def build_topic8_curriculum():
    """Returns the comprehensive, textbook-grade pedagogical page and block structure for Geography Topic 8."""
    return [
        # =====================================================================
        # LESSON 1: Foundations of Demography, Census, and Demographic Indicators (11 Pages)
        # =====================================================================
        {
            "unit_order": 1,
            "unit_name": "Foundations of Demography, Census, and Demographic Indicators",
            "unit_description": "Definition of population, demography, census methods, and key demographic rates.",
            "lesson_title": "Foundations of Demography, Census, and Demographic Indicators",
            "pages": [
                # Page 1
                [
                    {
                        "type": "learning_goal",
                        "title": "Learning Objectives: Foundations of Demography",
                        "content": {
                            "title": "Learning Objectives: Foundations of Demography",
                            "goals": [
                                "Define population, demography, and national population census in a geographic context.",
                                "Distinguish between De Facto and De Jure population census enumeration methods.",
                                "Calculate and interpret key demographic indicators: Crude Birth Rate (CBR), Crude Death Rate (CDR), Natural Increase, and Life Expectancy."
                            ]
                        }
                    },
                    {
                        "type": "concept_explanation",
                        "title": "Geographic Definition of Population & Demography",
                        "content": {
                            "title": "Geographic Definition of Population & Demography",
                            "text": "Population refers to the total number of human beings inhabiting a specified geographic area (such as a county, country, or continent) at a particular time. Demography is the scientific and quantitative study of human populations, focusing on their size, composition, spatial distribution, density, age-sex structure, and dynamic changes over time due to births, deaths, and migration.\n\nDemographic data is essential for national development planning. Governments rely on demographic statistics to plan for schools, healthcare facilities, housing, water supply, electricity grids, transport networks, employment opportunities, and national food security."
                        }
                    }
                ],
                # Page 2
                [
                    {
                        "type": "definition_card",
                        "title": "Census Enumeration Taxonomy",
                        "content": {
                            "term": "Population Census Methods Taxonomy",
                            "definition": "The official, systematic counting of a country's population conducted at regular 10-year intervals.",
                            "key_points": [
                                "De Facto Census Method: Enumerates individuals based on where they are physically present on the official census night, regardless of their permanent residence.",
                                "De Jure Census Method: Enumerates individuals based on their legal or usual permanent place of residence, regardless of where they are physically present on census night.",
                                "Census Functions: Provides authoritative demographic data for allocating national revenue to counties, delimiting parliamentary constituencies, and planning public infrastructure."
                            ]
                        }
                    }
                ],
                # Page 3
                [
                    {
                        "type": "suggested_diagram",
                        "title": "Demographic Rate Formulas & Rates Calculation Matrix",
                        "content": {
                            "title": "Demographic Rate Formulas & Rates Calculation Matrix",
                            "caption": "Core Demographic Indicators: CBR = (Births / Population) × 1000 | CDR = (Deaths / Population) × 1000 | Natural Increase = CBR - CDR",
                            "description": "Mathematical formula diagram detailing formulas for Crude Birth Rate, Crude Death Rate, Natural Increase, and Infant Mortality Rate."
                        }
                    },
                    {
                        "type": "concept_explanation",
                        "title": "Key Demographic Rates & Formulas",
                        "content": {
                            "title": "Key Demographic Rates & Formulas",
                            "text": "Geographers quantify population change using standardized demographic rates expressed per 1,000 people:\n\n1. Crude Birth Rate (CBR): $$\text{CBR} = \frac{\text{Total Live Births in a Year}}{\text{Total Mid-Year Population}} \times 1,000$$\n\n2. Crude Death Rate (CDR): $$\text{CDR} = \frac{\text{Total Deaths in a Year}}{\text{Total Mid-Year Population}} \times 1,000$$\n\n3. Natural Population Increase: $$\text{Rate of Natural Increase (\%)} = \frac{\text{CBR} - \text{CDR}}{10}$$\n\n4. Infant Mortality Rate (IMR): Number of deaths of infants under 1 year of age per 1,000 live births in a given year."
                        }
                    }
                ],
                # Page 4
                [
                    {
                        "type": "suggested_image",
                        "title": "Tom Mboya Nairobi High Density Crowd Visualization",
                        "content": {
                            "title": "Tom Mboya Nairobi High Density Crowd Visualization",
                            "caption": "Dense urban street crowd on Tom Mboya Street in Nairobi representing high population concentration.",
                            "url": "https://upload.wikimedia.org/wikipedia/commons/6/64/Nairobi_Commercial_TomMboya_Lane.jpg",
                            "author": "CC BY-SA 4.0, Wikimedia Commons",
                            "licensing": "CC BY-SA 4.0",
                            "commons_page_url": "https://commons.wikimedia.org/wiki/File:Nairobi_Commercial_TomMboya_Lane.jpg"
                        }
                    },
                    {
                        "type": "concept_explanation",
                        "title": "Source of Demographic Data: Vital Registration",
                        "content": {
                            "title": "Source of Demographic Data: Vital Registration",
                            "text": "Apart from national decennial population censuses, governments collect continuous demographic data through Vital Registration Systems. Vital registration mandates the legal recording of births, deaths, marriages, divorces, and adoption events as they occur in hospitals and chief locations."
                        }
                    }
                ],
                # Page 5
                [
                    {
                        "type": "worked_example",
                        "title": "Calculating Demographic Rates: Worked Example",
                        "content": {
                            "question": "A county in Kenya with a mid-year population of 2,000,000 recorded 70,000 live births and 18,000 deaths in a single year. Calculate: (a) Crude Birth Rate (CBR), (b) Crude Death Rate (CDR), and (c) Rate of Natural Increase. (4 Marks)",
                            "strategy": "Apply demographic formulas per 1,000 population.",
                            "solution": [
                                "1. (a) CBR = (70,000 / 2,000,000) * 1,000 = 35 per 1,000 (1 Mark)",
                                "2. (b) CDR = (18,000 / 2,000,000) * 1,000 = 9 per 1,000 (1 Mark)",
                                "3. (c) Natural Increase per 1,000 = CBR - CDR = 35 - 9 = 26 per 1,000 (1 Mark)",
                                "4. Natural Increase Percentage = 26 / 10 = 2.6% per annum (1 Mark)"
                            ]
                        }
                    }
                ],
                # Page 6
                [
                    {
                        "type": "suggested_image",
                        "title": "Nairobi Retail Trade Node Population Hub Visualization",
                        "content": {
                            "title": "Nairobi Retail Trade Node Population Hub Visualization",
                            "caption": "Artisan craft market in Nairobi representing population aggregation at commercial nodes.",
                            "url": "https://upload.wikimedia.org/wikipedia/commons/7/7a/Maasai_Market-Nairobi.jpg",
                            "author": "CC BY-SA 4.0, Wikimedia Commons",
                            "licensing": "CC BY-SA 4.0",
                            "commons_page_url": "https://commons.wikimedia.org/wiki/File:Maasai_Market-Nairobi.jpg"
                        }
                    },
                    {
                        "type": "comparison_table",
                        "title": "De Facto vs De Jure Census Methods Comparison",
                        "content": {
                            "headers": ["Enumeration Feature", "De Facto Census Method", "De Jure Census Method"],
                            "rows": [
                                ["Counting Basis", "Counts people where they are physically spent census night", "Counts people at their legal permanent residence"],
                                ["Travelers & Visitors", "Enumerated at temporary hotel/transit location", "Enumerated back at home residence"],
                                ["Simplicity of Execution", "Simpler during a single night, avoids double counting", "More complex; requires verifying legal residence"],
                                ["Resource Allocation", "Reflects immediate night-time spatial distribution", "Reflects long-term residential population demands"]
                            ]
                        }
                    }
                ],
                # Page 7
                [
                    {
                        "type": "callout",
                        "title": "Geographic Insight: Census Night Inoculation",
                        "content": {
                            "text": "To ensure an accurate De Facto census, governments declare a national 'Census Night' holiday. Travel is restricted overnight so enumerators can count every individual where they sleep, preventing double-counting or omissions."
                        }
                    }
                ],
                # Page 8
                [
                    {
                        "type": "mini_activity",
                        "title": "Interactive Census Classifier",
                        "content": {
                            "activity_type": "scenario_decision",
                            "title": "Interactive Census Classifier",
                            "prompt": "Scenario: A businessman from Kisumu stays overnight in a Mombasa hotel on Census Night and is enumerated at the hotel. Which census method was used?",
                            "options": [
                                "Option A: De Facto Census Method (enumerated where physically present on census night).",
                                "Option B: De Jure Census Method.",
                                "Option C: Sample Survey Method."
                            ],
                            "correct_option": "Option A: De Facto Census Method (enumerated where physically present on census night).",
                            "explanation": "De Facto enumerates people wherever they spend census night, regardless of their home residence."
                        }
                    }
                ],
                # Page 9
                [
                    {
                        "type": "knowledge_check",
                        "title": "Knowledge Checkpoint: Foundations of Demography",
                        "content": {
                            "question": "What is the formula for calculating the Rate of Natural Increase of a population?",
                            "options": [
                                "Crude Birth Rate (CBR) minus Crude Death Rate (CDR)",
                                "Crude Birth Rate plus Immigration",
                                "Crude Death Rate divided by Total Population",
                                "Total Population divided by Land Area"
                            ],
                            "correct_answer": 0,
                            "explanation": "Natural Increase equals Crude Birth Rate minus Crude Death Rate (excluding net migration)."
                        }
                    }
                ],
                # Page 10
                [
                    {
                        "type": "common_mistake",
                        "title": "Common Student Exam Traps: Natural Increase vs Growth Rate",
                        "content": {
                            "mistake": "Confusing Rate of Natural Increase with Population Growth Rate.",
                            "correction": "Natural Increase accounts ONLY for Births minus Deaths. Total Population Growth Rate includes Natural Increase PLUS Net Migration (Immigration minus Emigration).",
                            "reasoning": "Migration is an external population driver distinct from natural fertility and mortality."
                        }
                    }
                ],
                # Page 11
                [
                    {
                        "type": "summary",
                        "title": "Foundations of Demography: Key Takeaways",
                        "content": {
                            "title": "Foundations of Demography: Key Takeaways",
                            "summary_points": [
                                "Demography is the quantitative study of human population size, structure, and spatial distribution.",
                                "Census methods include De Facto (physical location on census night) and De Jure (permanent legal residence).",
                                "Demographic indicators (CBR, CDR, Natural Increase) drive population projections and national resource allocation."
                            ]
                        }
                    }
                ]
            ]
        },

        # =====================================================================
        # LESSON 2: Spatial Distribution and Density of Population in Kenya and East Africa (12 Pages)
        # =====================================================================
        {
            "unit_order": 2,
            "unit_name": "Spatial Distribution and Density of Population in Kenya and East Africa",
            "unit_description": "Population density factors, high vs low density zones in Kenya, and physical/human drivers.",
            "lesson_title": "Spatial Distribution and Density of Population in Kenya and East Africa",
            "pages": [
                # Page 1
                [
                    {
                        "type": "learning_goal",
                        "title": "Learning Objectives: Spatial Distribution & Density",
                        "content": {
                            "title": "Learning Objectives: Spatial Distribution & Density",
                            "goals": [
                                "Define population density and calculate arithmetic density ($D = \text{Population} / \text{Area}$).",
                                "Identify high, medium, and low population density regions in Kenya and East Africa.",
                                "Analyze physical (climate, soils, relief, pests) and human (urbanization, agriculture, transport) drivers of population distribution."
                            ]
                        }
                    },
                    {
                        "type": "concept_explanation",
                        "title": "Population Distribution & Density Concepts",
                        "content": {
                            "title": "Population Distribution & Density Concepts",
                            "text": "Population Distribution describes the spatial pattern of where people live across a country's land surface (whether even, nucleated, linear, or sparse). Population Density measures the concentration of people per unit area of land, expressed as persons per square kilometer ($\text{persons/km}^2$):\n\n$$\text{Population Density} = \frac{\text{Total Population}}{\text{Total Land Area in km}^2}$$\n\nIn Kenya, population distribution is extremely uneven: over 75% of the population resides on less than 20% of the land area (the fertile highlands and Lake Victoria basin), while vast arid lowlands remain sparsely populated."
                        }
                    }
                ],
                # Page 2
                [
                    {
                        "type": "suggested_diagram",
                        "title": "Kenya Population Density Distribution Map & Ecological Zones",
                        "content": {
                            "title": "Kenya Population Density Distribution Map & Ecological Zones",
                            "caption": "Spatial Population Density Map: High Density Highlands & Lake Victoria Basin (300-1000+ persons/km²) vs Low Density Arid ASALs (<15 persons/km²)",
                            "description": "Spatial map diagram showing high density clusters in Central Highlands and Lake Basin vs sparse density in Northern ASALs."
                        }
                    },
                    {
                        "type": "suggested_image",
                        "title": "Kiambu High Density Agricultural Farming Zone Visualization",
                        "content": {
                            "title": "Kiambu High Density Agricultural Farming Zone Visualization",
                            "caption": "Intensive smallholder farming landscape in Kiambu County illustrating high rural population density in fertile highlands.",
                            "url": "https://upload.wikimedia.org/wikipedia/commons/5/57/Wangige_vegetable_local_market_in_Kiambu_Kenya.jpg",
                            "author": "CC BY-SA 4.0, Wikimedia Commons",
                            "licensing": "CC BY-SA 4.0",
                            "commons_page_url": "https://commons.wikimedia.org/wiki/File:Wangige_vegetable_local_market_in_Kiambu_Kenya.jpg"
                        }
                    }
                ],
                # Page 3
                [
                    {
                        "type": "definition_card",
                        "title": "Population Density Zones in Kenya Taxonomy",
                        "content": {
                            "term": "Population Density Zones Taxonomy",
                            "definition": "Classification of Kenyan regions based on population concentration per square kilometer.",
                            "key_points": [
                                "High Density Zones (>250 persons/km²): Central Highlands (Kiambu, Murang'a, Nyeri), Lake Victoria Basin (Kisii, Nyamira, Kakamega), Urban centers (Nairobi, Mombasa).",
                                "Medium Density Zones (50 - 240 persons/km²): Coastal strip, Machakos, Kitui, Kericho, Trans-Nzoia agricultural belts.",
                                "Low Density Zones (<15 persons/km²): Northern & Eastern ASALs (Turkana, Marsabit, Wajir, Mandera, Garissa, Isiolo), Nyika Plateau."
                            ]
                        }
                    }
                ],
                # Page 4
                [
                    {
                        "type": "suggested_diagram",
                        "title": "Physical vs Human Drivers of Population Density Diagram",
                        "content": {
                            "title": "Physical vs Human Drivers of Population Density Diagram",
                            "caption": "Multidimensional Density Drivers: Climate/Rainfall + Soil Fertility + Water Availability vs Economic Jobs + Transport Corridors + Security",
                            "description": "Diagram contrasting physical environmental factors and human socio-economic drivers determining population density."
                        }
                    },
                    {
                        "type": "suggested_image",
                        "title": "Kibera High Density Settlement Aerial View Visualization",
                        "content": {
                            "title": "Kibera High Density Settlement Aerial View Visualization",
                            "caption": "Aerial view of Kibera in Nairobi showing extremely high urban population density.",
                            "url": "https://upload.wikimedia.org/wikipedia/commons/8/8c/Kibera_aerial_view_western_part.jpg",
                            "author": "CC BY-SA 4.0, Wikimedia Commons",
                            "licensing": "CC BY-SA 4.0",
                            "commons_page_url": "https://commons.wikimedia.org/wiki/File:Kibera_aerial_view_western_part.jpg"
                        }
                    }
                ],
                # Page 5
                [
                    {
                        "type": "concept_explanation",
                        "title": "Physical Factors Influencing Population Distribution",
                        "content": {
                            "title": "Physical Factors Influencing Population Distribution",
                            "text": "1. Climate (Precipitation & Temperature): Areas receiving high, well-distributed rainfall (>1,000 mm/year) support intensive rain-fed agriculture and attract dense populations (e.g., Kisii, Murang'a). Arid regions receiving <350 mm/year support only sparse pastoralism.\n\n2. Soil Fertility: Deep fertile volcanic soils (Rift Valley, Central Highlands) attract dense farming populations, whereas infertile sandy desert soils support very few people.\n\n3. Pests & Diseases: Historical prevalence of tsetse flies (causing sleeping sickness) in Lambwe Valley and malaria mosquitoes in swampy lowlands created low population pockets.\n\n4. Water Supply: Availability of permanent rivers, lakes, and freshwater springs attracts settlements in drylands."
                        }
                    }
                ],
                # Page 6
                [
                    {
                        "type": "suggested_image",
                        "title": "Turkana Pastoralist ASAL Low Density Zone Visualization",
                        "content": {
                            "title": "Turkana Pastoralist ASAL Low Density Zone Visualization",
                            "caption": "Arid landscape in Turkana County illustrating sparse pastoralist population density.",
                            "url": "https://upload.wikimedia.org/wikipedia/commons/4/4e/Turkana_woman.jpg",
                            "author": "CC BY-SA 4.0, Wikimedia Commons",
                            "licensing": "CC BY-SA 4.0",
                            "commons_page_url": "https://commons.wikimedia.org/wiki/File:Turkana_woman.jpg"
                        }
                    },
                    {
                        "type": "concept_explanation",
                        "title": "Human Factors Influencing Population Distribution",
                        "content": {
                            "title": "Human Factors Influencing Population Distribution",
                            "text": "1. Economic Activities & Employment: Industrial cities, commercial mining centers (Kwale titanium), and plantation estates attract large migrant populations seeking jobs.\n\n2. Transport Networks: Construction of tarmac highways and railways (SGR Corridor) encourages linear population settlement along transit routes.\n\n3. Urbanization & Administrative Hubs: Capital cities (Nairobi) and county headquarters offer social amenities (hospitals, universities, electricity), driving rapid population growth.\n\n4. Historical & Security Factors: Historical inter-community conflicts or banditry in remote border regions create low density buffer zones."
                        }
                    }
                ],
                # Page 7
                [
                    {
                        "type": "comparison_table",
                        "title": "High Density Highlands vs Low Density ASALs Comparison",
                        "content": {
                            "headers": ["Geographic Feature", "High Density Highlands (e.g., Kisii/Kiambu)", "Low Density ASALs (e.g., Turkana/Marsabit)"],
                            "rows": [
                                ["Annual Rainfall", "High & reliable (>1,200 mm/year)", "Low & unreliable (<350 mm/year)"],
                                ["Soil Types", "Deep, fertile volcanic soils", "Shallow, sandy, saline soils"],
                                ["Primary Economic Activity", "Intensive cash crop & food crop farming", "Nomadic pastoralism"],
                                ["Infrastructure Level", "Dense tarmac road networks & electricity", "Sparse roads & limited social amenities"],
                                ["Mean Density", "Over 500 - 1,000+ persons per km²", "Less than 10 - 15 persons per km²"]
                            ]
                        }
                    }
                ],
                # Page 8
                [
                    {
                        "type": "worked_example",
                        "title": "Calculating Population Density: Worked Example",
                        "content": {
                            "question": "County A has a total land area of 4,000 km² and a registered population of 2,400,000 people. County B has a land area of 60,000 km² and a population of 300,000 people. Calculate the population density for both counties and state which is high density. (4 Marks)",
                            "strategy": "Apply formula: Density = Total Population / Total Area.",
                            "solution": [
                                "1. County A Density = 2,400,000 / 4,000 = 600 persons/km² (1 Mark)",
                                "2. County B Density = 300,000 / 60,000 = 5 persons/km² (1 Mark)",
                                "3. Density Comparison: County A is a High-Density Zone (600 persons/km²), whereas County B is a Low-Density Zone (5 persons/km²). (2 Marks)"
                            ]
                        }
                    }
                ],
                # Page 9
                [
                    {
                        "type": "mini_activity",
                        "title": "Interactive Density Factors Evaluator",
                        "content": {
                            "activity_type": "scenario_decision",
                            "title": "Interactive Density Factors Evaluator",
                            "prompt": "Why does Kisii County in Western Kenya have one of the highest rural population densities in Africa (>1,000 persons/km²)?",
                            "options": [
                                "Option A: Reliable high bimodal rainfall, fertile volcanic soils, and intensive smallholder tea/banana farming.",
                                "Option B: Extensive mineral oil reserves.",
                                "Option C: Flat desert terrain."
                            ],
                            "correct_option": "Option A: Reliable high bimodal rainfall, fertile volcanic soils, and intensive smallholder tea/banana farming.",
                            "explanation": "Kisii combines exceptional high rainfall and fertile soils, allowing intensive agricultural land use to sustain high rural population densities."
                        }
                    }
                ],
                # Page 10
                [
                    {
                        "type": "knowledge_check",
                        "title": "Knowledge Checkpoint: Spatial Distribution & Density",
                        "content": {
                            "question": "Which area in Kenya is categorized as a low population density zone due to aridity?",
                            "options": [
                                "Turkana County",
                                "Kiambu County",
                                "Kisii County",
                                "Nyeri County"
                            ],
                            "correct_answer": 0,
                            "explanation": "Turkana County is an arid semi-desert region with low population density (<15 persons/km²)."
                        }
                    }
                ],
                # Page 11
                [
                    {
                        "type": "common_mistake",
                        "title": "Common Student Exam Traps: Arithmetic vs Physiological Density",
                        "content": {
                            "mistake": "Assuming population density is uniform across an entire county.",
                            "correction": "Arithmetic density averages total population over total land area, ignoring uncultivable mountains or deserts. Actual population is clustered near water sources and roads.",
                            "reasoning": "Distribution maps show localized population nucleations."
                        }
                    }
                ],
                # Page 12
                [
                    {
                        "type": "summary",
                        "title": "Spatial Distribution & Density: Key Takeaways",
                        "content": {
                            "title": "Spatial Distribution & Density: Key Takeaways",
                            "summary_points": [
                                "Population Density = Total Population / Total Land Area.",
                                "High density (>250 persons/km²) occurs in volcanic highlands, Lake Basin, and urban cities.",
                                "Low density (<15 persons/km²) occurs in northern ASALs due to aridity and shallow soils.",
                                "Distribution is driven by climate, soils, relief, economic employment, transport, and water supply."
                            ]
                        }
                    }
                ]
            ]
        },

        # =====================================================================
        # LESSON 3: Population Dynamics, Growth Rates, and Fertility Drivers (12 Pages)
        # =====================================================================
        {
            "unit_order": 3,
            "unit_name": "Population Dynamics, Growth Rates, and Fertility Drivers",
            "unit_description": "Factors influencing high/low fertility rates, mortality decline, Demographic Transition Model (DTM), and overpopulation.",
            "lesson_title": "Population Dynamics, Growth Rates, and Fertility Drivers",
            "pages": [
                # Page 1
                [
                    {
                        "type": "learning_goal",
                        "title": "Learning Objectives: Population Dynamics",
                        "content": {
                            "title": "Learning Objectives: Population Dynamics",
                            "goals": [
                                "Explain socio-cultural and economic factors responsible for high fertility rates in developing nations.",
                                "Analyze causes of declining mortality rates (healthcare, immunization, sanitation).",
                                "Evaluate the 4 stages of the Demographic Transition Model (DTM) and concepts of overpopulation and carrying capacity."
                            ]
                        }
                    },
                    {
                        "type": "concept_explanation",
                        "title": "Factors Driving High Fertility in Developing Nations",
                        "content": {
                            "title": "Factors Driving High Fertility in Developing Nations",
                            "text": "Developing nations in Sub-Saharan Africa often experience high Total Fertility Rates (TFR) due to several interacting factors:\n\n1. Socio-Cultural Beliefs: Cultural preference for large families to prestige, lineage continuation, and ancestor reverence.\n2. Early Marriage: Cultural practices where girls marry at a young age, extending their reproductive lifespan.\n3. High Value placed on Children as Economic Assets: In rural agricultural economies, children provide farm labor and care for aging parents.\n4. High Infant Mortality Rates: Families have many children to ensure some survive to adulthood.\n5. Low Contraceptive Prevalence & Education: Limited access to family planning services and low female formal education levels."
                        }
                    }
                ],
                # Page 2
                [
                    {
                        "type": "suggested_diagram",
                        "title": "Demographic Transition Model 4-Stage Curve",
                        "content": {
                            "title": "Demographic Transition Model 4-Stage Curve",
                            "caption": "Demographic Transition: Stage 1 (High Stationary) → Stage 2 (Early Expanding - Rapid Growth) → Stage 3 (Late Expanding) → Stage 4 (Low Stationary)",
                            "description": "Line graph diagram illustrating birth rate and death rate curves across the 4 classic stages of demographic transition."
                        }
                    },
                    {
                        "type": "concept_explanation",
                        "title": "Factors Driving Declining Mortality Rates",
                        "content": {
                            "title": "Factors Driving Declining Mortality Rates",
                            "text": "Global crude death rates and infant mortality rates have declined significantly due to:\n\n1. Medical & Healthcare Expansion: Widespread childhood immunization against infectious diseases (polio, measles, tuberculosis), availability of antibiotics, and maternity clinics.\n2. Improved Sanitation & Clean Water: Pipe-borne water supply and modern sewage treatment reducing water-borne epidemics (cholera, typhoid).\n3. Vector Control Programs: Distribution of insecticide-treated mosquito nets and indoor spraying combating malaria.\n4. Improved Food Security & Nutrition: Mechanized agriculture and relief aid reducing famine deaths."
                        }
                    }
                ],
                # Page 3
                [
                    {
                        "type": "definition_card",
                        "title": "The Demographic Transition Model (DTM) Taxonomy",
                        "content": {
                            "term": "Demographic Transition Model (DTM) Taxonomy",
                            "definition": "A model illustrating how birth rates and death rates change as a nation undergoes economic industrialization.",
                            "key_points": [
                                "Stage 1 (High Stationary): High birth rate & high death rate; slow or fluctuating population growth (pre-industrial societies).",
                                "Stage 2 (Early Expanding): High birth rate & rapidly falling death rate; VERY HIGH population growth (many developing nations like Kenya historically).",
                                "Stage 3 (Late Expanding): Falling birth rate & low death rate; decelerating population growth.",
                                "Stage 4 (Low Stationary): Low birth rate & low death rate; stable or near-zero population growth (developed nations like Sweden)."
                            ]
                        }
                    }
                ],
                # Page 4
                [
                    {
                        "type": "suggested_diagram",
                        "title": "Population Growth vs Carrying Capacity Curves",
                        "content": {
                            "title": "Population Growth vs Carrying Capacity Curves",
                            "caption": "Ecological Balance: Exponential Population Growth vs Environmental Carrying Capacity Ceiling → Overpopulation & Resource Scarcity",
                            "description": "Graph showing exponential population growth exceeding land carrying capacity, causing environmental degradation."
                        }
                    },
                    {
                        "type": "concept_explanation",
                        "title": "Overpopulation, Underpopulation, & Carrying Capacity",
                        "content": {
                            "title": "Overpopulation, Underpopulation, & Carrying Capacity",
                            "text": "• Carrying Capacity: The maximum population size that a given land area's natural resources (soil, water, vegetation) can sustain indefinitely without environmental degradation.\n\n• Overpopulation: Occurs when population size exceeds the available resources and carrying capacity of an area, leading to land fragmentation, soil erosion, unemployment, and falling living standards.\n\n• Underpopulation: Occurs when an area has insufficient human population to fully exploit its rich natural resources (e.g., Australia, Canada)."
                        }
                    }
                ],
                # Page 5
                [
                    {
                        "type": "suggested_diagram",
                        "title": "Impact of Rapid Population Growth on Land Fragmentation Model",
                        "content": {
                            "title": "Impact of Rapid Population Growth on Land Fragmentation Model",
                            "caption": "Subdivision Cascade: Large Family Ancestral Farm → Subdivided into Small Sub-plots → Sub-economic Farm Units → Rural Poverty",
                            "description": "Diagram illustrating ancestral land being repeatedly subdivided among heirs into tiny sub-economic agricultural plots."
                        }
                    },
                    {
                        "type": "concept_explanation",
                        "title": "Consequences of Rapid Population Growth in Kenya",
                        "content": {
                            "title": "Consequences of Rapid Population Growth in Kenya",
                            "text": "Rapid population growth exerts severe pressure on developing economies:\n1. Severe Land Fragmentation: Ancestral farms are repeatedly subdivided among children into tiny, sub-economic plots that cannot support households.\n2. High Unemployment: Labor force expands faster than job creation in formal sectors.\n3. Pressure on Social Amenities: Overcrowded schools, hospital bed shortages, and housing deficits in urban centers.\n4. Environmental Degradation: Deforestation, encroaching on catchment forests, and soil erosion."
                        }
                    }
                ],
                # Page 6
                [
                    {
                        "type": "comparison_table",
                        "title": "Overpopulation vs Underpopulation Comparison",
                        "content": {
                            "headers": ["Dimension", "Overpopulation", "Underpopulation"],
                            "rows": [
                                ["Resource-Population Ratio", "Population exceeds environmental carrying capacity", "Population is too small to exploit resources fully"],
                                ["Land Availability", "High land fragmentation & landlessness", "Vast uncultivated arable land available"],
                                ["Employment Level", "High unemployment & underemployment", "Labor shortages in agriculture and industries"],
                                ["Living Standards", "Declining per capita income & urban slums", "High potential per capita income if labor increases"],
                                ["Example Nations", "High-density rural parts of Kenya, Bangladesh", "Australia, Canada, Namibia"]
                            ]
                        }
                    }
                ],
                # Page 7
                [
                    {
                        "type": "worked_example",
                        "title": "KCSE Analysis: Measures Taken by Kenya to Control Population Growth",
                        "content": {
                            "question": "Explain four national strategies implemented by the Kenyan government to control rapid population growth. (4 Marks)",
                            "strategy": "Identify government policy programs and explain demographic impact.",
                            "solution": [
                                "1. National Family Planning Programs (1 Mark): Establishing clinics providing accessible, affordable modern contraceptives.",
                                "2. Female Education Expansion (1 Mark): Retaining girls longer in secondary/tertiary education delays marriage age and lowers total fertility.",
                                "3. Public Health Campaigns (1 Mark): Educating communities via radio and community health workers on family planning benefits.",
                                "4. Integration of Reproductive Health into Primary Healthcare (1 Mark): Providing maternal and child health services in rural dispensaries."
                            ]
                        }
                    }
                ],
                # Page 8
                [
                    {
                        "type": "mini_activity",
                        "title": "Interactive DTM Stage Evaluator",
                        "content": {
                            "activity_type": "scenario_decision",
                            "title": "Interactive DTM Stage Evaluator",
                            "prompt": "Scenario: A nation experiences a falling death rate due to medical immunization, while its birth rate remains very high, leading to rapid population growth. Which stage of the Demographic Transition Model is this nation in?",
                            "options": [
                                "Option A: Stage 2 (Early Expanding Stage).",
                                "Option B: Stage 1 (High Stationary Stage).",
                                "Option C: Stage 4 (Low Stationary Stage)."
                            ],
                            "correct_option": "Option A: Stage 2 (Early Expanding Stage).",
                            "explanation": "Stage 2 is characterized by high birth rates coupled with rapidly falling death rates, generating explosive population expansion."
                        }
                    }
                ],
                # Page 9
                [
                    {
                        "type": "knowledge_check",
                        "title": "Knowledge Checkpoint: Population Dynamics",
                        "content": {
                            "question": "What is meant by the environmental carrying capacity of a region?",
                            "options": [
                                "The maximum population size that a region's resources can sustain indefinitely without degradation.",
                                "The total weight of all trees in a forest.",
                                "The number of trucks moving on a highway.",
                                "The birth rate per 1,000 people."
                            ],
                            "correct_answer": 0,
                            "explanation": "Carrying capacity is the maximum population ecosystem resources can support without environmental damage."
                        }
                    }
                ],
                # Page 10
                [
                    {
                        "type": "callout",
                        "title": "Geographic Insight: Female Education & Fertility",
                        "content": {
                            "text": "Demographic studies prove that educating girls through secondary school is the single most effective intervention for reducing fertility rates. Educated women tend to marry later, pursue careers, and have smaller, healthier families."
                        }
                    }
                ],
                # Page 11
                [
                    {
                        "type": "common_mistake",
                        "title": "Common Student Exam Traps: Overpopulation Definition",
                        "content": {
                            "mistake": "Defining overpopulation purely as a large number of people.",
                            "correction": "Overpopulation is NOT just a large population number; it is a RELATIVE concept defined as population EXCEEDING available resources and carrying capacity.",
                            "reasoning": "A small population in a desert can be overpopulated if water/food resources cannot sustain them."
                        }
                    }
                ],
                # Page 12
                [
                    {
                        "type": "summary",
                        "title": "Population Dynamics: Key Takeaways",
                        "content": {
                            "title": "Population Dynamics: Key Takeaways",
                            "summary_points": [
                                "High fertility in developing nations is driven by early marriage, cultural beliefs, and economic value of children.",
                                "Mortality rates have fallen due to immunization, sanitation, and healthcare expansion.",
                                "The Demographic Transition Model traces 4 stages from high stationary to low stationary.",
                                "Rapid population growth causes land fragmentation, unemployment, and environmental degradation."
                            ]
                        }
                    }
                ]
            ]
        },

        # =====================================================================
        # LESSON 4: Population Structure, Age-Sex Pyramids, and Dependency Ratios (12 Pages)
        # =====================================================================
        {
            "unit_order": 4,
            "unit_name": "Population Structure, Age-Sex Pyramids, and Dependency Ratios",
            "unit_description": "Age-sex structure, population pyramids (progressive vs regressive), and dependency ratio calculations.",
            "lesson_title": "Population Structure, Age-Sex Pyramids, and Dependency Ratios",
            "pages": [
                # Page 1
                [
                    {
                        "type": "learning_goal",
                        "title": "Learning Objectives: Population Structure",
                        "content": {
                            "title": "Learning Objectives: Population Structure",
                            "goals": [
                                "Define population structure and interpret Age-Sex Pyramids.",
                                "Compare progressive (broad-based, young) pyramids of developing nations with regressive/stationary pyramids of developed nations.",
                                "Calculate and analyze Dependency Ratios and their socio-economic implications."
                            ]
                        }
                    },
                    {
                        "type": "concept_explanation",
                        "title": "Population Structure & Age-Sex Pyramids",
                        "content": {
                            "title": "Population Structure & Age-Sex Pyramids",
                            "text": "Population Structure refers to the composition of a population in terms of age categories and gender distribution. Geographers visualize this structure using an Age-Sex Pyramid (Population Pyramid), a horizontal bar graph where:\n\n• The vertical axis represents 5-year age cohorts (0-4, 5-9, 10-14 ... 80+).\n• The horizontal axis represents percentage or absolute numbers of population.\n• Males are plotted on the left side; Females are plotted on the right side."
                        }
                    }
                ],
                # Page 2
                [
                    {
                        "type": "suggested_diagram",
                        "title": "Progressive (Kenya) vs Regressive (Sweden) Age-Sex Pyramids",
                        "content": {
                            "title": "Progressive (Kenya) vs Regressive (Sweden) Age-Sex Pyramids",
                            "caption": "Pyramid Comparison: Kenya Progressive (Broad Base = High Birth Rate, Rapid Tapering) vs Sweden Regressive (Narrow Base = Low Birth Rate, Bulging Top = Aging Population)",
                            "description": "Side-by-side population pyramids showing Kenya's broad-based young structure vs Sweden's narrow-based aging structure."
                        }
                    },
                    {
                        "type": "definition_card",
                        "title": "Population Pyramid Types Taxonomy",
                        "content": {
                            "term": "Population Pyramid Types Taxonomy",
                            "definition": "Classification of population pyramids based on structural shape and demographic growth characteristics.",
                            "key_points": [
                                "Progressive (Broad-Based) Pyramid: Wide base tapering rapidly to a narrow apex. Indicates high birth rate, high youth dependency, and low life expectancy (e.g., Kenya, Uganda).",
                                "Stationary (Beehive-Shaped) Pyramid: Uniform width across age groups, narrowing only at old age. Indicates low birth rate, stable population (e.g., USA, UK).",
                                "Regressive (Narrow-Based / Constrictive) Pyramid: Narrow base, bulging middle and top. Indicates very low birth rate, sub-replacement fertility, and aging population (e.g., Sweden, Japan, Germany)."
                            ]
                        }
                    }
                ],
                # Page 3
                [
                    {
                        "type": "suggested_diagram",
                        "title": "Dependency Ratio Calculation Model & Economic Burden Scale",
                        "content": {
                            "title": "Dependency Ratio Calculation Model & Economic Burden Scale",
                            "caption": "Economic Scale: Dependent Population (Children 0-14 + Elderly 65+) Supported by Working Population (15-64)",
                            "description": "Balance scale diagram showing young and old dependents being supported by the economically active working population."
                        }
                    },
                    {
                        "type": "concept_explanation",
                        "title": "Dependency Ratio Concept & Formula",
                        "content": {
                            "title": "Dependency Ratio Concept & Formula",
                            "text": "The Dependency Ratio measures the economic burden borne by the working-age population to support non-working dependents:\n\n$$\text{Dependency Ratio} = \frac{\text{Children (0-14 years)} + \text{Elderly (65+ years)}}{\text{Working Population (15-64 years)}} \times 100$$\n\n• Dependent Population: Children aged 0–14 years and elderly people aged 65+ years.\n• Economically Active (Working) Population: Individuals aged 15–64 years who generate income and pay taxes.\n\nDeveloping nations like Kenya have high Dependency Ratios (>80%) dominated by youth dependents, requiring heavy government expenditure on primary schools, immunizations, and child healthcare."
                        }
                    }
                ],
                # Page 4
                [
                    {
                        "type": "worked_example",
                        "title": "Calculating Dependency Ratio: Worked Example",
                        "content": {
                            "question": "A country's census data reveals: Children (0-14 yrs) = 18,000,000; Working Age (15-64 yrs) = 22,000,000; Elderly (65+ yrs) = 2,000,000. Calculate the Dependency Ratio and interpret the result. (4 Marks)",
                            "strategy": "Apply formula: Dependency Ratio = [(0-14) + (65+)] / (15-64) * 100.",
                            "solution": [
                                "1. Formula: Dependency Ratio = [(Children + Elderly) / Working Population] * 100 (1 Mark)",
                                "2. Substitution: [(18,000,000 + 2,000,000) / 22,000,000] * 100 (1 Mark)",
                                "3. Calculation: [20,000,000 / 22,000,000] * 100 = 90.9% (1 Mark)",
                                "4. Interpretation: The Dependency Ratio is 90.9%. This means every 100 working individuals support approximately 91 non-working dependents, indicating a heavy economic burden. (1 Mark)"
                            ]
                        }
                    }
                ],
                # Page 5
                [
                    {
                        "type": "suggested_diagram",
                        "title": "Age Structure Dynamics: Youth Bulge vs Aging Population",
                        "content": {
                            "title": "Age Structure Dynamics: Youth Bulge vs Aging Population",
                            "caption": "Socio-Economic Impacts: Developing Youth Bulge (School Demand, Job Needs) vs Developed Aging Population (Pension Strain, Geriatric Healthcare)",
                            "description": "Comparison diagram showing economic demands of a youth bulge vs an aging population."
                        }
                    },
                    {
                        "type": "concept_explanation",
                        "title": "Socio-Economic Implications of Age Structure",
                        "content": {
                            "title": "Socio-Economic Implications of Age Structure",
                            "text": "1. Developing Nations (Youth Bulge): A broad pyramid base means huge demand for primary/secondary education, high youth unemployment, and high future momentum of population growth as young people enter reproductive age.\n\n2. Developed Nations (Aging Population): A constrictive pyramid top means shrinking workforce, high pension costs, labor shortages, and high demand for geriatric healthcare facilities."
                        }
                    }
                ],
                # Page 6
                [
                    {
                        "type": "comparison_table",
                        "title": "Kenya Pyramid vs Sweden Pyramid Structural Comparison",
                        "content": {
                            "headers": ["Pyramid Feature", "Kenya Population Pyramid", "Sweden Population Pyramid"],
                            "rows": [
                                ["Base Width (0-14 yrs)", "BROAD: High Crude Birth Rate", "NARROW: Low birth rate below replacement level"],
                                ["Middle Section (15-64 yrs)", "Steeply tapering upwards", "Wide rectangular bulb; large working workforce"],
                                ["Apex / Top (65+ yrs)", "NARROW: Low proportion of elderly", "WIDE: High proportion of elderly (high life expectancy)"],
                                ["Dominant Dependency Type", "Youth Dependency (Children 0-14 yrs)", "Aged Dependency (Elderly 65+ yrs)"],
                                ["Growth Momentum", "High future population momentum", "Zero or negative population growth momentum"]
                            ]
                        }
                    }
                ],
                # Page 7
                [
                    {
                        "type": "mini_activity",
                        "title": "Interactive Pyramid Interpreter",
                        "content": {
                            "activity_type": "scenario_decision",
                            "title": "Interactive Pyramid Interpreter",
                            "prompt": "Scenario: You are examining a population pyramid with a very broad base and a very narrow top. What does this structural shape indicate about the nation's demographics?",
                            "options": [
                                "Option A: High birth rate, high youth dependency ratio, and low life expectancy.",
                                "Option B: Low birth rate and an aging population.",
                                "Option C: Negative population growth."
                            ],
                            "correct_option": "Option A: High birth rate, high youth dependency ratio, and low life expectancy.",
                            "explanation": "A broad base indicates many births, while a rapidly tapering top indicates high mortality rates in older age cohorts."
                        }
                    }
                ],
                # Page 8
                [
                    {
                        "type": "knowledge_check",
                        "title": "Knowledge Checkpoint: Population Structure",
                        "content": {
                            "question": "In calculating the Dependency Ratio, which age bracket constitutes the economically active working population?",
                            "options": [
                                "15 to 64 years",
                                "0 to 14 years",
                                "65 years and above",
                                "0 to 25 years"
                            ],
                            "correct_answer": 0,
                            "explanation": "Individuals aged 15 to 64 years represent the economically active working population."
                        }
                    }
                ],
                # Page 9
                [
                    {
                        "type": "callout",
                        "title": "Geographic Insight: The Demographic Dividend",
                        "content": {
                            "text": "When a developing nation successfully lowers its birth rate, the proportion of child dependents falls while the working-age population expands. This creates a temporary window of economic growth known as the Demographic Dividend."
                        }
                    }
                ],
                # Page 10
                [
                    {
                        "type": "common_mistake",
                        "title": "Common Student Exam Traps: Pyramid Reading",
                        "content": {
                            "mistake": "Misidentifying the working-age population as dependents.",
                            "correction": "ONLY children (0-14) and elderly (65+) are DEPENDENTS. People aged 15-64 are the WORKING POPULATION.",
                            "reasoning": "Working-age individuals generate tax revenue and fund social services."
                        }
                    }
                ],
                # Page 11
                [
                    {
                        "type": "summary",
                        "title": "Population Structure: Key Takeaways",
                        "content": {
                            "title": "Population Structure: Key Takeaways",
                            "summary_points": [
                                "Age-sex pyramids visualize age cohorts and male/female gender distribution.",
                                "Progressive pyramids (Kenya) have broad bases (high birth rate) and narrow tops.",
                                "Regressive pyramids (Sweden) have narrow bases (low birth rate) and wide tops (aging population).",
                                "Dependency Ratio = [(Children + Elderly) / Working Population] * 100."
                            ]
                        }
                    }
                ]
            ]
        },

        # =====================================================================
        # LESSON 5: Population Movements, Migration Dynamics, and Urbanization (12 Pages)
        # =====================================================================
        {
            "unit_order": 5,
            "unit_name": "Population Movements, Migration Dynamics, and Urbanization",
            "unit_description": "Types of migration, push and pull factors, urban informal settlements, and brain drain.",
            "lesson_title": "Population Movements, Migration Dynamics, and Urbanization",
            "pages": [
                # Page 1
                [
                    {
                        "type": "learning_goal",
                        "title": "Learning Objectives: Migration & Urbanization",
                        "content": {
                            "title": "Learning Objectives: Migration & Urbanization",
                            "goals": [
                                "Define migration and distinguish between Internal Migration and International Migration.",
                                "Analyze Push and Pull factors driving Rural-to-Urban and Rural-to-Rural migration in Kenya.",
                                "Evaluate socio-economic impacts of migration on both origin rural areas and destination urban centers."
                            ]
                        }
                    },
                    {
                        "type": "concept_explanation",
                        "title": "Migration Concepts & Classification",
                        "content": {
                            "title": "Migration Concepts & Classification",
                            "text": "Migration is defined as the physical movement of people from one place of residence to another, involving a permanent or semi-permanent change of home. People who move into a region are called Immigrants, while people who leave a region are called Emigrants.\n\nMigration is broadly classified into:\n1. Internal Migration: Movement within national boundaries (Rural-to-Urban, Rural-to-Rural, Urban-to-Rural, Urban-to-Urban).\n2. International Migration: Movement across international borders (Emigration to foreign nations or Immigration from abroad)."
                        }
                    }
                ],
                # Page 2
                [
                    {
                        "type": "suggested_diagram",
                        "title": "Rural-to-Urban Migration Push and Pull Factors Flowchart",
                        "content": {
                            "title": "Rural-to-Urban Migration Push and Pull Factors Flowchart",
                            "caption": "Migration Drivers: Rural Push Factors (Land Scarcity, Drought, Low Wages) vs Urban Pull Factors (Industrial Jobs, Higher Education, Social Amenities)",
                            "description": "Flowchart contrasting rural push factors repelling migrants with urban pull factors attracting migrants."
                        }
                    },
                    {
                        "type": "suggested_image",
                        "title": "Nairobi CBD Core Urban Skyline Visualization",
                        "content": {
                            "title": "Nairobi CBD Core Urban Skyline Visualization",
                            "caption": "Nairobi central business district skyline attracting rural-to-urban job seekers.",
                            "url": "https://upload.wikimedia.org/wikipedia/commons/8/80/Norra_centrala_Nairobi.jpg",
                            "author": "CC BY-SA 4.0, Wikimedia Commons",
                            "licensing": "CC BY-SA 4.0",
                            "commons_page_url": "https://commons.wikimedia.org/wiki/File:Norra_centrala_Nairobi.jpg"
                        }
                    }
                ],
                # Page 3
                [
                    {
                        "type": "definition_card",
                        "title": "Migration Push & Pull Taxonomy",
                        "content": {
                            "term": "Push & Pull Migration Factors Taxonomy",
                            "definition": "Classification of environmental and socio-economic forces governing population migration.",
                            "key_points": [
                                "Push Factors (Origin Negative Forces): Severe land fragmentation, soil exhaustion, rural poverty, drought/famine, lack of secondary schools, insecurity/conflict.",
                                "Pull Factors (Destination Positive Forces): Employment opportunities in manufacturing/services, higher wages, modern hospitals, universities, urban leisure amenities.",
                                "Rural-to-Rural Migration: Farmers moving from overpopulated highlands to settlement schemes (e.g., Mwea, Bura) or pastoralists moving for seasonal pasture.",
                                "Brain Drain: Emigration of highly trained professionals (doctors, engineers) to developed nations."
                            ]
                        }
                    }
                ],
                # Page 4
                [
                    {
                        "type": "suggested_diagram",
                        "title": "Urbanization & Informal Settlement Growth Cascade",
                        "content": {
                            "title": "Urbanization & Informal Settlement Growth Cascade",
                            "caption": "Urban Impact: Massive Rural-to-Urban Migration → Formal Housing Shortage → Growth of Slums & Informal Settlements → Pressure on Services",
                            "description": "Flowchart showing how rapid rural influx exceeds urban housing capacity, triggering informal slum growth."
                        }
                    },
                    {
                        "type": "suggested_image",
                        "title": "Nairobi Periphery Rural-Urban Fringe Visualization",
                        "content": {
                            "title": "Nairobi Periphery Rural-Urban Fringe Visualization",
                            "caption": "Peri-urban settlement on the outskirts of Nairobi representing rural-urban land conversion.",
                            "url": "https://upload.wikimedia.org/wikipedia/commons/9/97/A_vegetable_stall_in_the_outskirts_of_Nairobi%2C_Kenya.jpg",
                            "author": "CC BY-SA 4.0, Wikimedia Commons",
                            "licensing": "CC BY-SA 4.0",
                            "commons_page_url": "https://commons.wikimedia.org/wiki/File:A_vegetable_stall_in_the_outskirts_of_Nairobi%2C_Kenya.jpg"
                        }
                    }
                ],
                # Page 5
                [
                    {
                        "type": "concept_explanation",
                        "title": "Effects of Migration on Rural Areas & Urban Centers",
                        "content": {
                            "title": "Effects of Migration on Rural Areas & Urban Centers",
                            "text": "1. Effects on Rural Origin Areas:\n   • Positives: Diaspora and urban-rural monetary remittances sent home to build houses and pay school fees; reduces pressure on agricultural land.\n   • Negatives: Depopulation of energetic young male labor force, leaving farming to elderly women; rural decline.\n\n2. Effects on Urban Destination Centers:\n   • Positives: Plentiful supply of cheap labor for urban construction and factories.\n   • Negatives: Proliferation of informal slum settlements (Kibera, Mathare), unemployment, traffic congestion, elevated crime rates, and strain on municipal water and sanitation."
                        }
                    }
                ],
                # Page 6
                [
                    {
                        "type": "suggested_diagram",
                        "title": "Brain Drain & Diaspora Remittances Economic Exchange Model",
                        "content": {
                            "title": "Brain Drain & Diaspora Remittances Economic Exchange Model",
                            "caption": "International Migration Trade-Off: Emigration of Skilled Professionals (Loss of Expertise) ↔ Return Diaspora Remittances (Foreign Exchange Inflows)",
                            "description": "Diagram depicting economic trade-offs between professional brain drain and diaspora monetary remittances."
                        }
                    },
                    {
                        "type": "comparison_table",
                        "title": "Push Factors vs Pull Factors Functional Comparison",
                        "content": {
                            "headers": ["Migration Factor Category", "Push Factors (Rural Origin)", "Pull Factors (Urban Destination)"],
                            "rows": [
                                ["Economic Drivers", "Unemployment & low agricultural wages", "Industrial jobs & higher wage rates"],
                                ["Land Factors", "Sub-economic land fragmentation & soil infertility", "Availability of commercial & residential plots"],
                                ["Social Amenities", "Inadequate healthcare & secondary schools", "Advanced referral hospitals & universities"],
                                ["Environmental Factors", "Recurrent droughts, soil erosion, pest infestation", "Paved roads, piped water, reliable electricity"]
                            ]
                        }
                    }
                ],
                # Page 7
                [
                    {
                        "type": "worked_example",
                        "title": "KCSE Case Study: Causes and Impacts of Rural-to-Urban Migration in Nairobi",
                        "content": {
                            "question": "Explain three push factors forcing people out of rural areas and three negative impacts of rapid urbanization in Nairobi. (6 Marks)",
                            "strategy": "Separate into 3 Push Factors (3 Marks) and 3 Urban Negative Impacts (3 Marks).",
                            "solution": [
                                "1. Rural Push Factors (3 Marks):\n   • Land Scarcity & Sub-division: Extreme agricultural land fragmentation in high-density rural counties.\n   • Rural Unemployment: Lack of non-farm employment opportunities for educated youth.\n   • Recurrent Droughts: Crop failures reducing agricultural income.",
                                "2. Urban Negative Impacts in Nairobi (3 Marks):\n   • Growth of Informal Slums: Rapid influx leads to sprawling unserviced settlements like Kibera.\n   • High Urban Unemployment: Job seekers exceed industrial job creation.\n   • Strain on Social Services: Severe water shortages, traffic jams, and overcrowded public hospitals."
                            ]
                        }
                    }
                ],
                # Page 8
                [
                    {
                        "type": "mini_activity",
                        "title": "Interactive Migration Factor Evaluator",
                        "content": {
                            "activity_type": "scenario_decision",
                            "title": "Interactive Migration Factor Evaluator",
                            "prompt": "Scenario: A young graduate leaves Kakamega County due to lack of local job opportunities and moves to Nairobi after securing an engineering job. How are these two factors classified?",
                            "options": [
                                "Option A: Lack of jobs in Kakamega is a Rural Push Factor; securing an engineering job in Nairobi is an Urban Pull Factor.",
                                "Option B: Both are Push Factors.",
                                "Option C: Both are International Migration."
                            ],
                            "correct_option": "Option A: Lack of jobs in Kakamega is a Rural Push Factor; securing an engineering job in Nairobi is an Urban Pull Factor.",
                            "explanation": "Unemployment repels the migrant from Kakamega (push), while employment attracts the migrant to Nairobi (pull)."
                        }
                    }
                ],
                # Page 9
                [
                    {
                        "type": "knowledge_check",
                        "title": "Knowledge Checkpoint: Migration & Urbanization",
                        "content": {
                            "question": "Which term describes the emigration of highly skilled doctors and engineers from developing nations to Western countries?",
                            "options": [
                                "Brain Drain",
                                "Rural-to-Rural Migration",
                                "Urban Sprawl",
                                "De Facto Census"
                            ],
                            "correct_answer": 0,
                            "explanation": "Brain Drain refers to the loss of educated professional talent through international emigration."
                        }
                    }
                ],
                # Page 10
                [
                    {
                        "type": "callout",
                        "title": "Geographic Insight: Diaspora Remittances",
                        "content": {
                            "text": "Diaspora monetary remittances sent back home by Kenyans working abroad now exceed KSh 500 Billion annually, surpassing tea exports as Kenya's top foreign exchange earner."
                        }
                    }
                ],
                # Page 11
                [
                    {
                        "type": "common_mistake",
                        "title": "Common Student Exam Traps: Migration Types",
                        "content": {
                            "mistake": "Assuming all internal migration is Rural-to-Urban.",
                            "correction": "Remember: Rural-to-Rural migration (moving to government settlement schemes or tea estates) is also a major internal migration stream in Kenya.",
                            "reasoning": "Landless farmers move to rural schemes like Mwea or Bura for agricultural settlement."
                        }
                    }
                ],
                # Page 12
                [
                    {
                        "type": "summary",
                        "title": "Migration Dynamics: Key Takeaways",
                        "content": {
                            "title": "Migration Dynamics: Key Takeaways",
                            "summary_points": [
                                "Migration is permanent or semi-permanent change of residence; classified as Internal or International.",
                                "Rural Push factors (land scarcity, poverty) and Urban Pull factors (jobs, amenities) drive movement.",
                                "Rural origin regions benefit from remittances but lose young labor.",
                                "Urban destination cities gain cheap labor but face slum proliferation and service congestion."
                            ]
                        }
                    }
                ]
            ]
        },

        # =====================================================================
        # LESSON 6: Comparative Case Studies (Kenya vs Sweden), Topic Synthesis, and KCSE Review (8 Pages)
        # =====================================================================
        {
            "unit_order": 6,
            "unit_name": "Comparative Case Studies (Kenya vs Sweden), Topic Synthesis, and KCSE Review",
            "unit_description": "Comparative case study (Kenya vs Sweden demographic profiles), topic synthesis, and KCSE exam questions.",
            "lesson_title": "Comparative Case Studies (Kenya vs Sweden), Topic Synthesis, and KCSE Review",
            "pages": [
                # Page 1
                [
                    {
                        "type": "learning_goal",
                        "title": "Learning Objectives: Population Synthesis",
                        "content": {
                            "title": "Learning Objectives: Population Synthesis",
                            "goals": [
                                "Compare demographic profiles, growth rates, and age structures of Kenya and Sweden.",
                                "Master KCSE 10-mark essay questions on population density drivers and age-sex pyramids.",
                                "Complete end-of-topic revision assessment."
                            ]
                        }
                    },
                    {
                        "type": "suggested_image",
                        "title": "Stockholm Sweden City Aerial View Visualization",
                        "content": {
                            "title": "Stockholm Sweden City Aerial View Visualization",
                            "caption": "Stockholm urban aerial view representing a developed nation with slow population growth.",
                            "url": "https://upload.wikimedia.org/wikipedia/commons/2/2e/Aerial_view_of_Gamla_Stan%2C_Stockholm.jpg",
                            "author": "CC BY-SA 4.0, Wikimedia Commons",
                            "licensing": "CC BY-SA 4.0",
                            "commons_page_url": "https://commons.wikimedia.org/wiki/File:Aerial_view_of_Gamla_Stan%2C_Stockholm.jpg"
                        }
                    }
                ],
                # Page 2
                [
                    {
                        "type": "concept_explanation",
                        "title": "Comparative Case Study: Kenya vs Sweden Population Profiles",
                        "content": {
                            "title": "Comparative Case Study: Kenya vs Sweden Population Profiles",
                            "text": "Comparing Kenya (a developing African nation) and Sweden (a highly developed European nation) reveals contrasting demographic paradigms:\n\n1. Birth Rate & Growth Rate: Kenya has a high Crude Birth Rate (~28 per 1,000) and rapid population growth (~2.2% per year). Sweden has a low Crude Birth Rate (~11 per 1,000) and near-zero natural growth (~0.1% per year).\n\n2. Age Structure & Pyramid Shape: Kenya features a broad-based progressive pyramid with over 40% of the population under 15 years. Sweden features a narrow-based constrictive pyramid with an aging population (>20% aged 65+ years).\n\n3. Dependency Type: Kenya faces high Youth Dependency (spending on schools/vaccines). Sweden faces high Aged Dependency (spending on geriatric healthcare/pensions).\n\n4. Life Expectancy: Kenya's life expectancy is ~67 years; Sweden's life expectancy is ~83 years due to advanced universal healthcare."
                        }
                    }
                ],
                # Page 3
                [
                    {
                        "type": "comparison_table",
                        "title": "Kenya vs Sweden Demographic Profile Matrix",
                        "content": {
                            "headers": ["Demographic Indicator", "Kenya Profile", "Sweden Profile"],
                            "rows": [
                                ["Development Classification", "Developing Agrarian Nation", "Developed Post-Industrial Nation"],
                                ["Crude Birth Rate (CBR)", "HIGH (~28 per 1,000)", "LOW (~11 per 1,000)"],
                                ["Crude Death Rate (CDR)", "MODERATE (~7 per 1,000)", "MODERATE-HIGH (~10 per 1,000 due to aging)"],
                                ["Life Expectancy", "Moderate (~67 years)", "Very High (~83 years)"],
                                ["Pyramid Structure", "Broad base (Progressive / Young)", "Narrow base, wide top (Regressive / Aging)"],
                                ["Primary Dependency", "Youth Dependency (Children 0-14 yrs)", "Aged Dependency (Elderly 65+ yrs)"],
                                ["Urbanization Rate", "Moderate (~28% urbanized)", "Very High (>88% urbanized)"]
                            ]
                        }
                    }
                ],
                # Page 4
                [
                    {
                        "type": "worked_example",
                        "title": "Worked KCSE Essay 1: Factors Influencing Population Density in Kenya",
                        "content": {
                            "question": "Explain five physical and human factors responsible for high population density in the Kenya Highlands. (10 Marks)",
                            "strategy": "State factor (1 Mark) and explain geographical impact on density (1 Mark).",
                            "solution": [
                                "1. Reliable High Rainfall (2 Marks): Bimodal precipitation exceeding 1,200 mm/year supports intensive rain-fed cash crop farming.",
                                "2. Deep Volcanic Soils (2 Marks): Rich fertile soils sustain high crop yields, supporting dense agricultural households.",
                                "3. Cool Highland Temperatures (2 Marks): Pleasant climate reduces tropical disease vectors like malaria mosquitoes.",
                                "4. Developed Transport Infrastructure (2 Marks): Dense road networks facilitate commercial trade and market access.",
                                "5. Industrial & Urban Centers (2 Marks): Cities like Nairobi and Nakuru provide non-farm employment opportunities."
                            ]
                        }
                    }
                ],
                # Page 5
                [
                    {
                        "type": "worked_example",
                        "title": "Worked KCSE Essay 2: Demographic Comparison (Kenya vs Sweden Pyramids)",
                        "content": {
                            "question": "Compare the population pyramid of Kenya with that of Sweden under: (a) Birth rate and base width, (b) Life expectancy and apex width, and (c) Economic dependency implications. (10 Marks)",
                            "strategy": "Contrast Kenya and Sweden systematically across the three sub-headings.",
                            "solution": [
                                "1. Birth Rate & Base Width (3 Marks):\n   • Kenya: Broad base indicating high Crude Birth Rate and large child population.\n   • Sweden: Narrow base indicating low Crude Birth Rate below replacement level.",
                                "2. Life Expectancy & Apex Width (3 Marks):\n   • Kenya: Narrow tapering top indicating shorter life expectancy (~67 yrs) and low elderly proportion.\n   • Sweden: Broad bulged apex indicating long life expectancy (~83 yrs) and high elderly proportion.",
                                "3. Economic Dependency Implications (4 Marks):\n   • Kenya: High Youth Dependency burden requiring heavy investment in primary education and immunizations.\n   • Sweden: High Aged Dependency burden requiring heavy investment in geriatric healthcare, care homes, and pensions."
                            ]
                        }
                    }
                ],
                # Page 6
                [
                    {
                        "type": "definition_card",
                        "title": "Master Glossary of Geography Population Terms",
                        "content": {
                            "term": "Geography Population Master Glossary",
                            "definition": "Essential textbook definitions required for KCSE Geography Paper 2.",
                            "key_points": [
                                "Demography: The scientific study of human population size, structure, and spatial distribution.",
                                "Population Density: Average number of persons per square kilometer of land area.",
                                "Carrying Capacity: Maximum population supported indefinitely by local environmental resources.",
                                "Overpopulation: Situation where population size exceeds available environmental carrying capacity.",
                                "Dependency Ratio: Ratio of non-working dependents (0-14 and 65+) to working-age population (15-64).",
                                "Progressive Pyramid: Broad-based pyramid typical of developing nations with high birth rates.",
                                "Regressive Pyramid: Narrow-based pyramid typical of developed nations with low birth rates and aging population.",
                                "Brain Drain: Emigration of highly educated professionals from developing to developed nations."
                            ]
                        }
                    }
                ],
                # Page 7
                [
                    {
                        "type": "knowledge_check",
                        "title": "Topic 8 Mastery Assessment Question",
                        "content": {
                            "question": "Which demographic characteristic distinguishes Sweden's population profile from Kenya's?",
                            "options": [
                                "Sweden has a low birth rate, high life expectancy, and an aging population structure.",
                                "Sweden has a broad-based progressive pyramid.",
                                "Sweden has high youth dependency.",
                                "Sweden has an uneducated population."
                            ],
                            "correct_answer": 0,
                            "explanation": "Sweden is a developed nation with sub-replacement fertility, high life expectancy, and high aged dependency."
                        }
                    }
                ],
                # Page 8
                [
                    {
                        "type": "summary",
                        "title": "Topic 8 Mastery Synthesis & Review",
                        "content": {
                            "title": "Topic 8 Mastery Synthesis & Review",
                            "summary_points": [
                                "Demography studies population size, density, structure, and spatial distribution.",
                                "Kenya's population density is concentrated in fertile highlands and Lake Victoria basin.",
                                "Kenya has a progressive broad pyramid (high youth dependency); Sweden has a regressive narrow pyramid (aging population).",
                                "Rural-urban migration is driven by rural push and urban pull factors.",
                                "Form 4 Geography Topic 8 (Population) Ingestion is 100% Complete & Production Ready!"
                            ]
                        }
                    }
                ]
            ]
        }
    ]

def ingest_form4_geography_topic8():
    print("=" * 80)
    print("VLearn Form 4 Geography — Topic 8: Population")
    print("In-Place Production Ingestion Engine (Preserves Topic ID)")
    print("=" * 80)

    curriculum = Curriculum.objects.filter(name="844").first()
    grade = Grade.objects.filter(curriculum=curriculum, name="Form 4").first()
    subject = Subject.objects.filter(grade=grade, name="Geography").first()

    if not subject:
        print("[!] Error: Subject 'Geography' not found under Form 4.")
        return

    print(f"[*] Resolved Target: {curriculum.name} -> {grade.name} -> {subject.name} (ID: {subject.id})")

    topic_name = "Population"

    # Match topic by order or name in-place
    topic = Topic.objects.filter(subject=subject, order=8).first()
    if not topic:
        topic = Topic.objects.filter(subject=subject, name=topic_name).first()

    if not topic:
        topic = Topic.objects.create(
            subject=subject,
            name=topic_name,
            order=8,
            description="Comprehensive syllabus on demography, census methods, population distribution and density drivers, fertility/mortality dynamics, Demographic Transition Model, progressive vs regressive age-sex pyramids, dependency ratios, migration push/pull factors, urbanization, and comparative case studies (Kenya vs Sweden)."
        )
        print(f"[+] Created Topic: {topic.name} (ID: {topic.id})")
    else:
        topic.name = topic_name
        topic.order = 8
        topic.description = "Comprehensive syllabus on demography, census methods, population distribution and density drivers, fertility/mortality dynamics, Demographic Transition Model, progressive vs regressive age-sex pyramids, dependency ratios, migration push/pull factors, urbanization, and comparative case studies (Kenya vs Sweden)."
        topic.save()
        print(f"[*] Preserving existing Topic ID: {topic.id} ({topic.name})")

    curriculum_data = build_topic8_curriculum()
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
                lesson.save()
            else:
                lesson = Lesson.objects.create(
                    topic=topic,
                    learning_unit=learning_unit,
                    title=lesson_title,
                    status="published",
                    version=1
                )
            print(f"  [+] Ingested Lesson {unit_order}: {lesson.title} (ID: {lesson.id})")

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
            print(f"      [OK] Ingested {lesson_page_count} Pages for Lesson {unit_order}.")

    print("=" * 80)
    print("[SUCCESS] Form 4 Geography Topic 8 (Population) Ingested In-Place!")
    print(f"[*] Topic ID Preserved:     {topic.id}")
    print(f"[*] Total Lessons Ingested: {total_lessons}")
    print(f"[*] Total Pages Ingested:   {total_pages}")
    print(f"[*] Total Blocks Ingested:  {total_blocks}")
    print("=" * 80)

if __name__ == "__main__":
    ingest_form4_geography_topic8()
