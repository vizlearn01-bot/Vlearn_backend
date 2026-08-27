"""
VLearn CBC Grade 10 Geography — Topic 10: Agriculture
Direct Programmatic Source-Driven Ingestion Engine

Subject: Geography (Grade 10 CBC, Subject ID: 37)
Topic 10: Agriculture
Source: Grade 10 Geography/10_agriculture.md

Lessons:
  1. Introduction to Agriculture: Classification & Subsistence Farming
  2. Commercial, Urban, Intensive, and Extensive Agricultural Systems
  3. Physical and Human Factors Influencing Agriculture
  4. Agricultural Systems as Open Cycles: Inputs, Processes, and Outputs
  5. Agricultural Value Chains: From Farm to Fork
  6. The Importance of Agriculture in Society
  7. Agricultural Regions and Spatial Patterns in Africa
  8. Key Trends in African Agriculture
  9. Challenges Facing Kenyan Agriculture: Climatic & Biological Threats
  10. Challenges Facing Kenyan Agriculture: Socio-Economic Hurdles
  11. Sustainable and Climate-Smart Agricultural Strategies
  12. The Critical Role of Agriculture in Food Security
  13. Local Field Study: Researching Agricultural Strategies
  14. Communicating Agricultural Strategies: Designing a Policy Brief
  15. Topic Review, Synthesis, and Unit Assessment

Usage:
  ./venv/bin/python curriculum/ingest_cbc_grade10_geography_topic10.py
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
# TOPIC 10 LESSON DEFINITIONS (15 LESSONS)
# =============================================================================
LESSONS_DATA = [
    # Lesson 1: Introduction to Agriculture: Classification & Subsistence Farming
    {
        "unit_order": 1,
        "unit_name": "Introduction to Agriculture: Classification & Subsistence Farming",
        "lesson_title": "Introduction to Agriculture: Classification & Subsistence Farming",
        "pages": [
            {
                "page_number": 1,
                "page_title": "Introduction & Learning Objectives",
                "blocks": [
                    {
                        "block_type": "suggested_image",
                        "component_type": "suggested_image",
                        "title": "Smallholder Farming in Rural Kenya",
                        "content": {"text": "A photograph showing a smallholder family farming in a subsistence maize and bean plot in Western Kenya using hand tools."}
                    },
                    {
                        "block_type": "learning_goal",
                        "component_type": "learning_goal",
                        "title": "Lesson Objectives: Classification & Subsistence Farming",
                        "content": {
                            "text": (
                                "By the end of this lesson, you will be able to:\n\n"
                                "- Define agriculture and classify agricultural activities into crop cultivation, livestock rearing, and mixed farming\n"
                                "- Describe the primary characteristics of subsistence farming (shifting cultivation, pastoral nomadism, and intensive subsistence)\n"
                                "- Analyze the socio-economic and structural conditions that lead to subsistence farming in East Africa"
                            )
                        }
                    },
                    {
                        "block_type": "concept_explanation",
                        "component_type": "concept_explanation",
                        "title": "Prerequisite Spark: The Farm Behind Breakfast",
                        "content": {
                            "text": (
                                "Think about what you ate for breakfast this morning. Whether it was sweet potatoes, a slice of bread, or a cup of tea, "
                                "every single ingredient came from a farm. Some of these farms are small family gardens, while others are massive commercial "
                                "fields stretching as far as the eye can see. Agriculture is the dynamic engine that keeps human society nourished and functioning!"
                            )
                        }
                    }
                ]
            },
            {
                "page_number": 2,
                "page_title": "Definitions & Agricultural Classification",
                "blocks": [
                    {
                        "block_type": "definition_card",
                        "component_type": "definition_card",
                        "title": "Core Agricultural Terminology",
                        "content": {
                            "definitions": [
                                {
                                    "term": "Agriculture",
                                    "definition": "The science, art, and business of cultivating plants and rearing livestock animals to produce food, fiber, fuel, and raw materials for human use.",
                                    "simple": "Farming plants and raising animals for human consumption and economic survival."
                                },
                                {
                                    "term": "Subsistence Agriculture",
                                    "definition": "A farming system where crops are grown and livestock reared primarily for the farmer's household consumption, leaving minimal or no surplus for commercial sale.",
                                    "simple": "Farming to feed your own family rather than selling to make a profit."
                                },
                                {
                                    "term": "Pastoral Nomadism",
                                    "definition": "An extensive subsistence livestock system where pastoralists migrate periodically with their herds in search of pasture and water.",
                                    "simple": "Moving continuously with animals across arid lands to find grass and water."
                                }
                            ]
                        }
                    },
                    {
                        "block_type": "concept_explanation",
                        "component_type": "concept_explanation",
                        "title": "The Three Main Branches of Agriculture",
                        "content": {
                            "text": (
                                "Agriculture is broadly classified into three major branches:\n\n"
                                "1. **Arable Farming (Crop Cultivation):** Growing annual or perennial crops for food, medicine, or industrial raw materials (e.g., maize, beans, wheat).\n"
                                "2. **Livestock Farming (Animal Husbandry):** Rearing animals for milk, meat, wool, hides, draft power, or breeding (e.g., cattle, camels, goats).\n"
                                "3. **Mixed Farming:** Integrating crop cultivation and animal husbandry on the same farm unit, allowing waste products like manure to fertilize crops."
                            )
                        }
                    }
                ]
            },
            {
                "page_number": 3,
                "page_title": "Subsistence Systems & Classification Tree",
                "blocks": [
                    {
                        "block_type": "diagram",
                        "component_type": "diagram",
                        "title": "Agricultural Systems Classification Tree",
                        "content": {
                            "caption": "Taxonomy of global agricultural systems: Subsistence vs Commercial systems."
                        }
                    },
                    {
                        "block_type": "concept_explanation",
                        "component_type": "concept_explanation",
                        "title": "Socio-Economic Profile of Subsistence Farming",
                        "content": {
                            "text": (
                                "Subsistence farming is widespread across sub-Saharan Africa. Key structural characteristics include:\n\n"
                                "- **Small, Fragmented Plots:** Average landholding is often less than 1-2 hectares.\n"
                                "- **Family Labor:** Dependent on household manual labor rather than hired workers or heavy machinery.\n"
                                "- **Low Technology:** Utilization of simple hand tools such as jembes (hoes) and pangas (machetes).\n"
                                "- **Low Capital Input:** Minimal use of hybrid seeds, synthetic fertilizers, or mechanization due to financial constraints.\n"
                                "- **High Crop Diversity:** Intercropping multiple food staples (maize, beans, cassava) to reduce the risk of total crop failure."
                            )
                        }
                    }
                ]
            },
            {
                "page_number": 4,
                "page_title": "Types of Subsistence Agriculture & Kenyan Relevance",
                "blocks": [
                    {
                        "block_type": "concept_explanation",
                        "component_type": "concept_explanation",
                        "title": "Major Subsistence Systems",
                        "content": {
                            "text": (
                                "Global subsistence farming manifests in three distinct forms:\n\n"
                                "1. **Shifting Cultivation (Slash-and-Burn):** Farmers clear a forest patch, burn the slash to enrich soil ash, cultivate for 2-3 seasons until fertility drops, then abandon the plot to fallow while clearing a new patch.\n"
                                "2. **Pastoral Nomadism:** Practiced in arid/semi-arid regions where herders move camels, cattle, and goats across communal rangelands.\n"
                                "3. **Intensive Subsistence Farming:** Maximizing food output per square meter using high human labor inputs (characteristic of Asian wet-rice paddies and dense East African highland valleys)."
                            )
                        }
                    },
                    {
                        "block_type": "case_study",
                        "component_type": "case_study",
                        "title": "Kenyan ASALs and Pastoral Nomadism",
                        "content": {
                            "text": (
                                "In Kenya's Arid and Semi-Arid Lands (ASALs), including Turkana, Marsabit, Wajir, and Garissa counties, "
                                "pastoral nomadism is the principal livelihood strategy. Because rainfall is sparse (<300 mm/year) and highly erratic, "
                                "crop cultivation is unviable. Pastoralists migrate seasonally along established grazing corridors to access boreholes, "
                                "oasis wells, and dry-season highland pastures."
                            )
                        }
                    },
                    {
                        "block_type": "misconception_alert",
                        "component_type": "misconception_alert",
                        "title": "Misconceptions Around Subsistence Farmers",
                        "content": {
                            "misconception": "Subsistence farmers produce low yields because they are lazy or lack farming knowledge.",
                            "correction": "Subsistence farmers possess deep indigenous ecological knowledge. Their low commercial surplus results from systemic structural barriers: lack of capital, absence of rural feeder roads, unaffordable agricultural inputs, and climate volatility."
                        }
                    }
                ]
            },
            {
                "page_number": 5,
                "page_title": "Formative Assessment: Classification & Subsistence",
                "blocks": [
                    {
                        "block_type": "multiple_choice_question",
                        "component_type": "multiple_choice_question",
                        "title": "Question 1: Shifting Cultivation Characteristics",
                        "content": {
                            "question": "Which agricultural system is characterized by clearing a forest plot, farming it for a few seasons, and then abandoning it to allow natural regeneration once soil fertility declines?",
                            "options": [
                                "Pastoral Nomadism",
                                "Commercial Plantation Farming",
                                "Shifting Cultivation",
                                "Intensive Wet-Rice Farming"
                            ],
                            "correct_answer": "Shifting Cultivation",
                            "explanation": "Shifting cultivation (slash-and-burn) relies on plot rotation and long fallow periods to restore depleted soil fertility naturally."
                        }
                    },
                    {
                        "block_type": "multiple_choice_question",
                        "component_type": "multiple_choice_question",
                        "title": "Question 2: Subsistence Farming Characteristics",
                        "content": {
                            "question": "What is a primary characteristic of subsistence farming in East Africa?",
                            "options": [
                                "High levels of mechanization using combine harvesters",
                                "Large-scale export of cash crops to European commodity markets",
                                "Heavy reliance on family labor and traditional hand tools",
                                "Extensive use of automated center-pivot irrigation systems"
                            ],
                            "correct_answer": "Heavy reliance on family labor and traditional hand tools",
                            "explanation": "Subsistence agriculture is characterized by low capital input, utilizing family labor and simple manual tools like hoes and machetes to meet household dietary needs."
                        }
                    }
                ]
            }
        ]
    },

    # Lesson 2: Commercial, Urban, Intensive, and Extensive Agricultural Systems
    {
        "unit_order": 2,
        "unit_name": "Commercial, Urban, Intensive, and Extensive Agricultural Systems",
        "lesson_title": "Commercial, Urban, Intensive, and Extensive Agricultural Systems",
        "pages": [
            {
                "page_number": 1,
                "page_title": "Introduction & Learning Objectives",
                "blocks": [
                    {
                        "block_type": "suggested_image",
                        "component_type": "suggested_image",
                        "title": "Commercial Floriculture Greenhouses in Naivasha",
                        "content": {"text": "A satellite and landscape photograph showing extensive high-tech greenhouse flower farms along the shores of Lake Naivasha, Kenya."}
                    },
                    {
                        "block_type": "learning_goal",
                        "component_type": "learning_goal",
                        "title": "Lesson Objectives: Farming Systems",
                        "content": {
                            "text": (
                                "By the end of this lesson, you will be able to:\n\n"
                                "- Contrast commercial agriculture with subsistence farming systems\n"
                                "- Define intensive versus extensive farming based on input density and spatial scale\n"
                                "- Evaluate the growing role of urban agriculture, vertical farming, and hydroponics in modern cities"
                            )
                        }
                    },
                    {
                        "block_type": "concept_explanation",
                        "component_type": "concept_explanation",
                        "title": "Prerequisite Spark: Farming on Rooftops and Warehouses",
                        "content": {
                            "text": (
                                "Have you ever seen lush leafy vegetables growing on an urban rooftop, inside vertical PVC pipes, or in climate-controlled warehouses? "
                                "In rapidly expanding cities where open land is scarce and expensive, urban agriculture and hydroponics are transforming how food is grown "
                                "right where consumers live!"
                            )
                        }
                    }
                ]
            },
            {
                "page_number": 2,
                "page_title": "Definitions & Comparative Systems",
                "blocks": [
                    {
                        "block_type": "definition_card",
                        "component_type": "definition_card",
                        "title": "Key Agricultural System Definitions",
                        "content": {
                            "definitions": [
                                {
                                    "term": "Commercial Agriculture",
                                    "definition": "Large-scale agricultural production undertaken primarily for market sale and financial profit.",
                                    "simple": "Farming focused on producing cash crops or livestock for commercial profit."
                                },
                                {
                                    "term": "Intensive Agriculture",
                                    "definition": "A farming system that maximizes crop yield per unit area through high applications of capital, labor, fertilizer, and technology on relatively small landholdings.",
                                    "simple": "Using lots of money, labor, and technology to get high yields from small land."
                                },
                                {
                                    "term": "Extensive Agriculture",
                                    "definition": "A farming system characterized by large land areas with relatively low inputs of labor, capital, and agrochemicals per unit area.",
                                    "simple": "Farming huge areas of land with low labor and input density per hectare."
                                },
                                {
                                    "term": "Urban Agriculture",
                                    "definition": "The cultivation, processing, and distribution of food crops and livestock within and around urban areas.",
                                    "simple": "Growing food in cities using balconies, rooftops, and small open urban spaces."
                                }
                            ]
                        }
                    },
                    {
                        "block_type": "concept_explanation",
                        "component_type": "concept_explanation",
                        "title": "Commercial vs Subsistence Farming Matrix",
                        "content": {
                            "text": (
                                "Commercial agriculture is distinguished by:\n\n"
                                "- **Large Capital Investment:** Significant expenditure on machinery, hybrid seeds, and automated irrigation.\n"
                                "- **Specialization (Monoculture):** Devoting large tracts of land to a single high-value crop (e.g., tea, coffee, wheat, sugarcane).\n"
                                "- **High Mechanization:** Replacement of manual labor with tractors, combine harvesters, and aerial sprayers.\n"
                                "- **Market Orientation:** Production targeted at domestic urban centers or international export markets."
                            )
                        }
                    }
                ]
            },
            {
                "page_number": 3,
                "page_title": "Intensive vs Extensive Farming Systems",
                "blocks": [
                    {
                        "block_type": "diagram",
                        "component_type": "diagram",
                        "title": "Intensive vs Extensive Agricultural Systems Matrix",
                        "content": {
                            "caption": "Comparison of input density, land footprint, labor, capital, and yield per hectare."
                        }
                    },
                    {
                        "block_type": "concept_explanation",
                        "component_type": "concept_explanation",
                        "title": "Input Density vs Land Scale",
                        "content": {
                            "text": (
                                "The distinction between intensive and extensive agriculture depends on input concentration:\n\n"
                                "- **Intensive Farming:** Focuses on yield per hectare (kg/ha). Common in densely populated highlands (e.g., Kiambu tea smallholdings, Naivasha cut flowers, Dutch horticulture).\n"
                                "- **Extensive Farming:** Focuses on total volume across vast land areas. Yield per hectare is modest, but total production is large (e.g., Laikipia commercial beef ranches, Australian sheep stations, Canadian wheat prairies)."
                            )
                        }
                    }
                ]
            },
            {
                "page_number": 4,
                "page_title": "Urban High-Tech Farming & Kenyan Floriculture",
                "blocks": [
                    {
                        "block_type": "concept_explanation",
                        "component_type": "concept_explanation",
                        "title": "Hydroponics and Vertical Farming Innovations",
                        "content": {
                            "text": (
                                "Modern urban agriculture leverages advanced soil-less and controlled environments:\n\n"
                                "- **Hydroponics:** Growing plants in nutrient-enriched water solutions without soil, reducing water usage by up to 90%.\n"
                                "- **Vertical Farming:** Stacking growing trays vertically under LED grow lights inside controlled indoor spaces.\n"
                                "- **Benefits:** Drastically slashes transport emissions (food miles), provides fresh greens to city dwellers, and operates year-round regardless of weather."
                            )
                        }
                    },
                    {
                        "block_type": "case_study",
                        "component_type": "case_study",
                        "title": "Lake Naivasha Intensive Floriculture Hub",
                        "content": {
                            "text": (
                                "Kenya is the world's leading exporter of cut flowers to the European Union. Around Lake Naivasha, "
                                "intensive commercial greenhouses utilize computerized drip fertigation, precise humidity control, and "
                                "specialized cold-chain logistics to harvest, package, and fly millions of roses to Amsterdam within 24 hours of cutting."
                            )
                        }
                    }
                ]
            },
            {
                "page_number": 5,
                "page_title": "Formative Assessment: Commercial & Urban Systems",
                "blocks": [
                    {
                        "block_type": "multiple_choice_question",
                        "component_type": "multiple_choice_question",
                        "title": "Question 1: Classifying Naivasha Flower Farms",
                        "content": {
                            "question": "A commercial flower farm in Naivasha uses computerized greenhouses, high chemical fertilizers, and automated drip irrigation on a small lakeshore parcel to export roses. How is this system classified?",
                            "options": [
                                "Extensive Subsistence Farming",
                                "Intensive Commercial Agriculture",
                                "Shifting Cultivation",
                                "Extensive Pastoral Ranching"
                            ],
                            "correct_answer": "Intensive Commercial Agriculture",
                            "explanation": "The flower farm is commercial (farming for export profit) and intensive (maximizing yield per hectare on a small parcel using high capital and technology inputs)."
                        }
                    },
                    {
                        "block_type": "multiple_choice_question",
                        "component_type": "multiple_choice_question",
                        "title": "Question 2: Urban Hydroponics Advantage",
                        "content": {
                            "question": "What is the primary operational advantage of hydroponic farming in densely populated urban centers like Nairobi?",
                            "options": [
                                "It requires hundreds of hectares of cheap rural land",
                                "It grows crops in nutrient-enriched water without soil, saving space and conserving water",
                                "It depends completely on seasonal monsoonal rains",
                                "It is exclusively suited for low-value cereal crops like sorghum"
                            ],
                            "correct_answer": "It grows crops in nutrient-enriched water without soil, saving space and conserving water",
                            "explanation": "Hydroponics uses water enriched with dissolved nutrients instead of soil, enabling space-efficient vertical farming and up to 90% water savings in urban environments."
                        }
                    }
                ]
            }
        ]
    },

    # Lesson 3: Physical and Human Factors Influencing Agriculture
    {
        "unit_order": 3,
        "unit_name": "Physical and Human Factors Influencing Agriculture",
        "lesson_title": "Physical and Human Factors Influencing Agriculture",
        "pages": [
            {
                "page_number": 1,
                "page_title": "Introduction & Learning Objectives",
                "blocks": [
                    {
                        "block_type": "suggested_image",
                        "component_type": "suggested_image",
                        "title": "Lush Tea Plantations on the Kericho Slopes",
                        "content": {"text": "A photograph showing undulating green tea plantations in the cool, volcanic highlands of Kericho, Kenya."}
                    },
                    {
                        "block_type": "learning_goal",
                        "component_type": "learning_goal",
                        "title": "Lesson Objectives: Agricultural Determinants",
                        "content": {
                            "text": (
                                "By the end of this lesson, you will be able to:\n\n"
                                "- Analyze how climatic factors (temperature, rainfall, sunshine, frost) determine crop distribution\n"
                                "- Explain the role of relief (slope, aspect, altitude) and edaphic factors (soil depth, pH, drainage) in farming suitability\n"
                                "- Evaluate the influence of human variables: capital, labor, transport infrastructure, and government policies"
                            )
                        }
                    },
                    {
                        "block_type": "concept_explanation",
                        "component_type": "concept_explanation",
                        "title": "Prerequisite Spark: Why Tea in Kericho, Camels in Garissa?",
                        "content": {
                            "text": (
                                "Why do we find vast, emerald tea bushes thriving across the cool highlands of Kericho, while herds of dromedary camels graze across the hot, "
                                "semi-arid plains of Garissa? Crops and livestock have strict physiological tolerance limits. Farmers cannot choose what to produce without "
                                "first consulting the environmental constraints of climate, terrain, and soil!"
                            )
                        }
                    }
                ]
            },
            {
                "page_number": 2,
                "page_title": "Physical Determinants: Climate & Soil",
                "blocks": [
                    {
                        "block_type": "definition_card",
                        "component_type": "definition_card",
                        "title": "Physical & Human Agricultural Factors",
                        "content": {
                            "definitions": [
                                {
                                    "term": "Physical Factors",
                                    "definition": "Natural abiotic conditions—climate, relief, and soil properties—that establish the biological boundaries of crop and livestock survival.",
                                    "simple": "Natural environmental conditions like rainfall, temperature, terrain, and soil quality."
                                },
                                {
                                    "term": "Edaphic Factors",
                                    "definition": "Soil-related physical and chemical characteristics, including texture, depth, structure, organic content, and pH, that dictate root growth and nutrient availability.",
                                    "simple": "The properties and fertility of the soil where crops grow."
                                },
                                {
                                    "term": "Relief (Topography)",
                                    "definition": "The elevation, slope gradient, and terrain orientation of the land surface.",
                                    "simple": "The shape, height, and slope of the landscape."
                                }
                            ]
                        }
                    },
                    {
                        "block_type": "concept_explanation",
                        "component_type": "concept_explanation",
                        "title": "Climatic & Edaphic Constraints",
                        "content": {
                            "text": (
                                "Physical constraints dictate what crops can thrive:\n\n"
                                "- **Rainfall Requirements:** Tea and coffee need >1,200 mm of well-distributed annual rainfall. Drought-hardy cereals (sorghum, millet) survive in areas with <500 mm.\n"
                                "- **Temperature & Altitude:** High temperatures accelerate cocoa and sugarcane growth, while tea and pyrethrum require cool highland temperatures (15°C to 21°C).\n"
                                "- **Soil Chemistry:** Tea requires deep, well-drained, acidic volcanic soils (pH 4.5-5.5). Sugarcane and cotton prefer heavy, nutrient-rich clay and alluvial soils."
                            )
                        }
                    }
                ]
            },
            {
                "page_number": 3,
                "page_title": "Relief, Slope, & Altitude Zonation",
                "blocks": [
                    {
                        "block_type": "diagram",
                        "component_type": "diagram",
                        "title": "Physical & Human Factors Influencing Agriculture Matrix",
                        "content": {
                            "caption": "Interactive matrix linking physical environmental drivers with human socio-economic variables."
                        }
                    },
                    {
                        "block_type": "concept_explanation",
                        "component_type": "concept_explanation",
                        "title": "Relief and Agro-Ecological Zonation",
                        "content": {
                            "text": (
                                "Topography strongly influences agricultural practices:\n\n"
                                "- **Steep Slopes:** Suffer from high water runoff and soil erosion; unsuited for heavy machinery, but well-drained slopes are ideal for tea when terraced.\n"
                                "- **Flat Plains:** Ideal for mechanized wheat and maize cultivation (e.g., Uasin Gishu plateau), though vulnerable to waterlogging if subsoil drainage is poor.\n"
                                "- **Altitudinal Zonation:** Ascending Mount Kenya transitions land use from semi-arid pastoralism at the base, to coffee (1,400-1,800m), tea (1,800-2,400m), pyrethrum and potatoes (>2,400m)."
                            )
                        }
                    }
                ]
            },
            {
                "page_number": 4,
                "page_title": "Human Variables & Kericho Case Study",
                "blocks": [
                    {
                        "block_type": "concept_explanation",
                        "component_type": "concept_explanation",
                        "title": "Socio-Economic and Political Drivers",
                        "content": {
                            "text": (
                                "Human factors determine whether farming potential is realized:\n\n"
                                "- **Capital:** Financial liquidity to purchase certified seeds, chemical inputs, drip equipment, and hire machinery.\n"
                                "- **Labor Supply:** Labor-intensive crops like tea and coffee require large, skilled seasonal plucking workforces.\n"
                                "- **Transport & Cold Chains:** Perishable milk and horticulture require tarmac roads and refrigerated transport to prevent spoilage.\n"
                                "- **Government Policy:** Subsidies on fertilizer, price floors, export tariffs, and trade pacts directly shape agricultural profitability."
                            )
                        }
                    },
                    {
                        "block_type": "case_study",
                        "component_type": "case_study",
                        "title": "The Kericho Tea Phenomenon",
                        "content": {
                            "text": (
                                "The Kericho Highlands represent the optimal convergence of physical and human geography: "
                                "deep, acidic volcanic soils, bimodal rainfall exceeding 1,800 mm annually, cool highland temperatures, "
                                "well-drained slopes, proximity to the Kisumu-Nakuru transport corridor, and substantial multinational and smallholder capital."
                            )
                        }
                    }
                ]
            },
            {
                "page_number": 5,
                "page_title": "Formative Assessment: Factors Influencing Agriculture",
                "blocks": [
                    {
                        "block_type": "multiple_choice_question",
                        "component_type": "multiple_choice_question",
                        "title": "Question 1: Wheat Farming Terrain Suitability",
                        "content": {
                            "question": "Which combination of soil and terrain characteristics is most suitable for large-scale, mechanized commercial wheat farming?",
                            "options": [
                                "Deep, waterlogged clays on steep mountain cliffs",
                                "Fertile, well-drained loamy volcanic soils on flat to gently undulating plains",
                                "Coarse desert sands on rocky escarpments",
                                "Acidic peat soils in coastal mangroves"
                            ],
                            "correct_answer": "Fertile, well-drained loamy volcanic soils on flat to gently undulating plains",
                            "explanation": "Gentle plains allow efficient operation of tractors and combine harvesters, while well-drained fertile volcanic loams supply vital nutrients and prevent waterlogging."
                        }
                    },
                    {
                        "block_type": "multiple_choice_question",
                        "component_type": "multiple_choice_question",
                        "title": "Question 2: Kericho Tea Concentration",
                        "content": {
                            "question": "Why is commercial tea cultivation concentrated along highland slopes in Kericho and Nyeri counties?",
                            "options": [
                                "Tea bushes require stagnant swamps to germinate",
                                "Highland slopes provide well-drained soils, cool temperatures, and reliable high rainfall",
                                "Tractors can only operate on steep cliffs",
                                "Tea is an arid crop that dies under regular rainfall"
                            ],
                            "correct_answer": "Highland slopes provide well-drained soils, cool temperatures, and reliable high rainfall",
                            "explanation": "Tea roots decay in waterlogged soils, making well-drained slopes essential. Highland altitudes supply the cool temperatures and heavy bimodal rainfall tea requires."
                        }
                    }
                ]
            }
        ]
    },

    # Lesson 4: Agricultural Systems as Open Cycles: Inputs, Processes, and Outputs
    {
        "unit_order": 4,
        "unit_name": "Agricultural Systems as Open Cycles: Inputs, Processes, and Outputs",
        "lesson_title": "Agricultural Systems as Open Cycles: Inputs, Processes, and Outputs",
        "pages": [
            {
                "page_number": 1,
                "page_title": "Introduction & Learning Objectives",
                "blocks": [
                    {
                        "block_type": "suggested_image",
                        "component_type": "suggested_image",
                        "title": "Smallholder Dairy & Crop Mixed Farm",
                        "content": {"text": "A photograph of a Kenyan smallholder dairy farmer with zero-grazing cattle, utilizing crop residue for feed and dung for farm biogas and manure."}
                    },
                    {
                        "block_type": "learning_goal",
                        "component_type": "learning_goal",
                        "title": "Lesson Objectives: Agricultural Systems Analysis",
                        "content": {
                            "text": (
                                "By the end of this lesson, you will be able to:\n\n"
                                "- Conceptualize a farm as an open thermodynamic and biological system\n"
                                "- Classify farm components into physical/human inputs, agricultural processes, and primary/secondary outputs\n"
                                "- Construct and evaluate system flowcharts incorporating closed-loop feedback mechanisms"
                            )
                        }
                    },
                    {
                        "block_type": "concept_explanation",
                        "component_type": "concept_explanation",
                        "title": "Prerequisite Spark: The Farm as a Food Factory",
                        "content": {
                            "text": (
                                "Think of an artisanal bakery: flour, yeast, and water go in (inputs), dough is kneaded and baked (processes), "
                                "and fresh bread comes out (outputs). A farm works on the exact same systems principles! It absorbs sunlight, rain, seeds, and labor, "
                                "transforms them through biological processes, and yields crops, livestock, and waste products."
                            )
                        }
                    }
                ]
            },
            {
                "page_number": 2,
                "page_title": "Definitions & Systems Theory in Farming",
                "blocks": [
                    {
                        "block_type": "definition_card",
                        "component_type": "definition_card",
                        "title": "Systems Geography Terminology",
                        "content": {
                            "definitions": [
                                {
                                    "term": "Open System",
                                    "definition": "A functional entity that continually exchanges matter, energy, and information across its boundaries with the surrounding external environment.",
                                    "simple": "A system where energy and materials flow freely in and out."
                                },
                                {
                                    "term": "Farm Inputs",
                                    "definition": "The physical resources (solar energy, rain, soil) and human/capital assets (seeds, machinery, labor, fertilizer) introduced into a farming operation.",
                                    "simple": "Everything put into a farm to make crops grow and animals thrive."
                                },
                                {
                                    "term": "Farm Processes",
                                    "definition": "The sequence of operational, mechanical, and biological activities executed on a farm to convert inputs into usable outputs.",
                                    "simple": "The physical farming tasks: plowing, planting, weeding, spraying, milking, and harvesting."
                                },
                                {
                                    "term": "Farm Outputs",
                                    "definition": "The resultant commodities, by-products, and waste materials generated by the farm system.",
                                    "simple": "The final products produced, such as food, milk, crop stalks, manure, and runoff."
                                }
                            ]
                        }
                    },
                    {
                        "block_type": "concept_explanation",
                        "component_type": "concept_explanation",
                        "title": "The Dynamic Open Cycle",
                        "content": {
                            "text": (
                                "Every farm operates as an open system characterized by continuous flows:\n\n"
                                "- **Inputs:** Solar radiation, precipitation, parent soil nutrients, hybrid seeds, pesticides, tractor fuel, and human labor.\n"
                                "- **Processes:** Land preparation, drilling, irrigation, weeding, fertilizer application, pest spraying, veterinary dipping, milking, and harvesting.\n"
                                "- **Outputs:** Marketable yield (maize grain, milk, tea leaves, eggs) and non-commercial by-products (stubble, dung, chemical runoff, greenhouse gas emissions)."
                            )
                        }
                    }
                ]
            },
            {
                "page_number": 3,
                "page_title": "The Farm System Flowchart & Feedback Loops",
                "blocks": [
                    {
                        "block_type": "diagram",
                        "component_type": "diagram",
                        "title": "Agricultural System Open Cycle: Inputs -> Processes -> Outputs",
                        "content": {
                            "caption": "Flowchart showing energy and matter flows, transformation processes, outputs, and internal feedback loops."
                        }
                    },
                    {
                        "block_type": "concept_explanation",
                        "component_type": "concept_explanation",
                        "title": "Closed-Loop Feedback Cycles",
                        "content": {
                            "text": (
                                "In sustainable mixed farming systems, outputs are recycled back as valuable inputs:\n\n"
                                "- **Manure Recycling:** Cow dung (output) is composted and applied to vegetable garden plots as organic fertilizer (input).\n"
                                "- **Crop Stubble Feed:** Harvested maize stalks and bean haulms (outputs) are chopped into silage to feed zero-grazed dairy cows (input).\n"
                                "- **Biogas Digestion:** Fermenting animal dung produces methane gas for household cooking and slurry fertilizer for crop fields."
                            )
                        }
                    }
                ]
            },
            {
                "page_number": 4,
                "page_title": "Kenyan Zero-Grazing Case & System Boundaries",
                "blocks": [
                    {
                        "block_type": "case_study",
                        "component_type": "case_study",
                        "title": "Zero-Grazing Mixed Farming in Central Kenya",
                        "content": {
                            "text": (
                                "In high-density counties like Kiambu and Nyeri, smallholder farmers operate highly efficient closed-loop 1-acre systems. "
                                "Napier grass is cultivated on field borders and fed to Friesian cows in sheds. The cows produce daily milk for sale, "
                                "while their slurry is channeled directly into kitchen gardens and banana groves, eliminating the need for expensive chemical fertilizers."
                            )
                        }
                    },
                    {
                        "block_type": "misconception_alert",
                        "component_type": "misconception_alert",
                        "title": "Outputs Are Not Just Market Goods",
                        "content": {
                            "misconception": "Farm outputs only include the profitable crops and livestock that the farmer sells at market.",
                            "correction": "Systems theory recognizes all generated materials as outputs, including negative externalities such as eroded topsoil runoff, pesticide leaching into groundwater, and methane emissions."
                        }
                    }
                ]
            },
            {
                "page_number": 5,
                "page_title": "Formative Assessment: Agricultural Systems",
                "blocks": [
                    {
                        "block_type": "multiple_choice_question",
                        "component_type": "multiple_choice_question",
                        "title": "Question 1: Classifying Farm Operations",
                        "content": {
                            "question": "On a dairy farm, which of the following activities is classified as a *process*?",
                            "options": [
                                "Dairy cows and pasture grass seeds",
                                "Milking and veterinary treatment",
                                "Fresh pasteurized milk and cow manure",
                                "Solar radiation and tractor diesel"
                            ],
                            "correct_answer": "Milking and veterinary treatment",
                            "explanation": "Milking and veterinary care are operational activities (processes) that convert inputs (cows, fodder) into primary outputs (milk)."
                        }
                    },
                    {
                        "block_type": "multiple_choice_question",
                        "component_type": "multiple_choice_question",
                        "title": "Question 2: Open System Mechanics",
                        "content": {
                            "question": "Why is an agricultural farm scientifically classified as an *open system*?",
                            "options": [
                                "It prohibits any materials from crossing its physical boundaries",
                                "It operates completely without human management or intervention",
                                "It continually exchanges energy and matter (solar radiation, rain, crops, waste) with the external environment",
                                "It can only function in open fields without greenhouses or barns"
                            ],
                            "correct_answer": "It continually exchanges energy and matter (solar radiation, rain, crops, waste) with the external environment",
                            "explanation": "An open system interacts dynamically with external surroundings, absorbing inputs (rain, sunlight, fertilizer) and discharging outputs (market crops, runoff, stubble)."
                        }
                    }
                ]
            }
        ]
    },

    # Lesson 5: Agricultural Value Chains: From Farm to Fork
    {
        "unit_order": 5,
        "unit_name": "Agricultural Value Chains: From Farm to Fork",
        "lesson_title": "Agricultural Value Chains: From Farm to Fork",
        "pages": [
            {
                "page_number": 1,
                "page_title": "Introduction & Learning Objectives",
                "blocks": [
                    {
                        "block_type": "suggested_image",
                        "component_type": "suggested_image",
                        "title": "Tea Withering and Processing in Embu Factory",
                        "content": {"text": "A photograph showing workers in Rukuriri Tea Factory in Embu, Kenya, processing green tea leaves through withering and CTC cutting."}
                    },
                    {
                        "block_type": "learning_goal",
                        "component_type": "learning_goal",
                        "title": "Lesson Objectives: Value Chains",
                        "content": {
                            "text": (
                                "By the end of this lesson, you will be able to:\n\n"
                                "- Define an agricultural value chain and describe value addition mechanisms\n"
                                "- Trace an agricultural product (e.g., tea, dairy, coffee) step-by-step from farm production to retail consumption\n"
                                "- Identify critical post-harvest loss points and analyze strategies to capture economic value locally"
                            )
                        }
                    },
                    {
                        "block_type": "concept_explanation",
                        "component_type": "concept_explanation",
                        "title": "Prerequisite Spark: Why Does Tea Cost More in the Supermarket?",
                        "content": {
                            "text": (
                                "When a smallholder plucks green tea leaves, they sell them for a modest price per kilogram at a rural buying center. "
                                "Yet a packaged carton of branded tea in a Nairobi supermarket or London tea shop sells for ten times that price! Why? "
                                "Because the product was withering, fermented, dried, graded, blended, packaged, and transported across an intricate value chain!"
                            )
                        }
                    }
                ]
            },
            {
                "page_number": 2,
                "page_title": "Definitions & Value Chain Architecture",
                "blocks": [
                    {
                        "block_type": "definition_card",
                        "component_type": "definition_card",
                        "title": "Value Chain Terminology",
                        "content": {
                            "definitions": [
                                {
                                    "term": "Agricultural Value Chain",
                                    "definition": "The entire connected sequence of activities required to bring an agricultural commodity from initial input supply, through on-farm production, bulking, processing, and distribution, to the final consumer.",
                                    "simple": "The complete journey of food from the farm to the customer's plate."
                                },
                                {
                                    "term": "Value Addition",
                                    "definition": "The process of altering the physical state, form, quality, or packaging of a raw agricultural good to increase its market value and shelf life.",
                                    "simple": "Transforming raw produce into higher-priced processed goods (e.g., milk into cheese)."
                                },
                                {
                                    "term": "Post-Harvest Loss (PHL)",
                                    "definition": "The measurable reduction in edible food quantity or nutritional/economic quality between harvesting and final retail consumption.",
                                    "simple": "Food that spoils, rots, or is eaten by pests before it reaches the buyer."
                                }
                            ]
                        }
                    },
                    {
                        "block_type": "concept_explanation",
                        "component_type": "concept_explanation",
                        "title": "The Five Stages of the Agribusiness Chain",
                        "content": {
                            "text": (
                                "Every agricultural value chain consists of five foundational nodes:\n\n"
                                "1. **Input Provision:** Certified seed breeders, agrochemical suppliers, livestock hatcheries, and financial credit.\n"
                                "2. **On-Farm Production:** Planting, cultivating, animal husbandry, and harvesting by farmers.\n"
                                "3. **Aggregating & Logistics:** Bulking produce at cooperative collection hubs, grading, and refrigerated transport.\n"
                                "4. **Industrial Processing & Packaging (Value Addition):** Pasteurization, milling, canning, drying, and retail branding.\n"
                                "5. **Wholesale & Retail Marketing:** Supermarkets, urban open-air markets, food service institutions, and export terminals."
                            )
                        }
                    }
                ]
            },
            {
                "page_number": 3,
                "page_title": "Tracing Value Chains: Coffee & Dairy",
                "blocks": [
                    {
                        "block_type": "diagram",
                        "component_type": "diagram",
                        "title": "Farm to Fork Agribusiness Value Chain",
                        "content": {
                            "caption": "Step-by-step value addition stages from input supply to supermarket retail."
                        }
                    },
                    {
                        "block_type": "concept_explanation",
                        "component_type": "concept_explanation",
                        "title": "Economic Multipliers of Value Addition",
                        "content": {
                            "text": (
                                "Processing raw farm produce delivers massive socio-economic benefits:\n\n"
                                "- **Extended Shelf Life:** Fresh tomatoes spoil within days; tomato paste and sauce keep for over a year.\n"
                                "- **Rural Industrialization:** Establishing processing plants (tea factories, creameries) creates non-farm manufacturing jobs in rural counties.\n"
                                "- **Price Stability:** Processed goods protect farmers from seasonal glut price crashes at harvest."
                            )
                        }
                    }
                ]
            },
            {
                "page_number": 4,
                "page_title": "Kenyan Tea Value Addition & Policy",
                "blocks": [
                    {
                        "block_type": "case_study",
                        "component_type": "case_study",
                        "title": "Capturing Value in the Kenyan Tea Sector",
                        "content": {
                            "text": (
                                "Kenya is the world's leading exporter of black CTC tea, yet over 85% is exported in bulk 50 kg sacks "
                                "to be blended and packaged abroad in Europe and the Middle East. Kenyan national policy is actively encouraging "
                                "local value addition—packaging branded tea bags and flavored teas domestically—to retain billions of shillings "
                                "in retail profits within Kenya."
                            )
                        }
                    },
                    {
                        "block_type": "misconception_alert",
                        "component_type": "misconception_alert",
                        "title": "Who Captures the Profits?",
                        "content": {
                            "misconception": "Primary farmers earn the largest profit margin because they do the hardest physical labor.",
                            "correction": "Primary crop production is typically the lowest-margin stage. The highest profits and markups are captured downstream by processors, packagers, brand owners, and retail supermarket chains."
                        }
                    }
                ]
            },
            {
                "page_number": 5,
                "page_title": "Formative Assessment: Agricultural Value Chains",
                "blocks": [
                    {
                        "block_type": "multiple_choice_question",
                        "component_type": "multiple_choice_question",
                        "title": "Question 1: Identifying Value Addition",
                        "content": {
                            "question": "Which of the following operations represents an example of *value addition* in the agricultural sector?",
                            "options": [
                                "Harvesting raw sugarcane and leaving it uncovered in the field",
                                "Processing fresh cow milk into strawberry yogurt and packaging it into retail tubs",
                                "Transporting bruised, unwashed tomatoes in open wooden crates",
                                "Selling freshly dug potatoes directly from the mud without cleaning"
                            ],
                            "correct_answer": "Processing fresh cow milk into strawberry yogurt and packaging it into retail tubs",
                            "explanation": "Value addition transforms raw agricultural goods into processed, packaged commodities (like yogurt), dramatically enhancing shelf life and market value."
                        }
                    },
                    {
                        "block_type": "multiple_choice_question",
                        "component_type": "multiple_choice_question",
                        "title": "Question 2: Processing Node in the Value Chain",
                        "content": {
                            "question": "At which node of the agricultural value chain does a raw food crop undergo pasteurization, refining, milling, or canning?",
                            "options": [
                                "Input Provision",
                                "On-Farm Primary Production",
                                "Industrial Processing and Packaging",
                                "Direct Consumer Consumption"
                            ],
                            "correct_answer": "Industrial Processing and Packaging",
                            "explanation": "Processing and packaging is the industrial stage where raw commodities are mechanically or chemically altered, sanitized, and packaged for commercial distribution."
                        }
                    }
                ]
            }
        ]
    },

    # Lesson 6: The Importance of Agriculture in Society
    {
        "unit_order": 6,
        "unit_name": "The Importance of Agriculture in Society",
        "lesson_title": "The Importance of Agriculture in Society",
        "pages": [
            {
                "page_number": 1,
                "page_title": "Introduction & Learning Objectives",
                "blocks": [
                    {
                        "block_type": "suggested_image",
                        "component_type": "suggested_image",
                        "title": "Grain Traders and Agro-Processing in Kenya",
                        "content": {"text": "A photograph showing agricultural commercial traders and grain processing hubs supporting employment and food distribution in Kenya."}
                    },
                    {
                        "block_type": "learning_goal",
                        "component_type": "learning_goal",
                        "title": "Lesson Objectives: Socio-Economic Significance",
                        "content": {
                            "text": (
                                "By the end of this lesson, you will be able to:\n\n"
                                "- Explain how agriculture provides foundational food security and nutrition\n"
                                "- Quantify the contribution of agriculture to national GDP, direct employment, and foreign exchange earnings\n"
                                "- Evaluate backward and forward linkages between agriculture and manufacturing industries"
                            )
                        }
                    },
                    {
                        "block_type": "concept_explanation",
                        "component_type": "concept_explanation",
                        "title": "Prerequisite Spark: What If Agriculture Stopped for One Week?",
                        "content": {
                            "text": (
                                "Imagine if all agricultural activities across Kenya ceased completely for just seven days. Urban supermarkets would empty, "
                                "flour mills and textile factories would shut down, and foreign exchange inflows from tea and flowers would vanish. "
                                "Agriculture is not merely a rural livelihood; it is the fundamental economic bedrock supporting modern urban civilization!"
                            )
                        }
                    }
                ]
            },
            {
                "page_number": 2,
                "page_title": "Definitions & National Economic Contributions",
                "blocks": [
                    {
                        "block_type": "definition_card",
                        "component_type": "definition_card",
                        "title": "Economic & Macro-Development Terminology",
                        "content": {
                            "definitions": [
                                {
                                    "term": "Gross Domestic Product (GDP)",
                                    "definition": "The total monetary market value of all finished goods and services produced within a country over a specific time period (usually one year).",
                                    "simple": "The total monetary value of everything produced inside a nation in a year."
                                },
                                {
                                    "term": "Foreign Exchange Earnings",
                                    "definition": "Monetary revenue acquired by a nation through exporting domestic products and commodities to international trading partners.",
                                    "simple": "Money earned in foreign currencies by selling export goods to other nations."
                                },
                                {
                                    "term": "Agro-Processing Linkages",
                                    "definition": "Interdependent economic connections where agricultural outputs serve as raw material inputs for industrial manufacturing (forward linkages) while industries supply farm tools and chemicals (backward linkages).",
                                    "simple": "How farms and factories support each other by buying and selling materials."
                                }
                            ]
                        }
                    },
                    {
                        "block_type": "concept_explanation",
                        "component_type": "concept_explanation",
                        "title": "The Economic Engine: GDP, Jobs, and Forex",
                        "content": {
                            "text": (
                                "Agriculture drives national economic stability in three major dimensions:\n\n"
                                "- **Direct Contribution to GDP:** Agriculture accounts directly for over 20-25% of Kenya's annual GDP, and another 25% indirectly through manufacturing and services.\n"
                                "- **Employment Creation:** Employs more than 40% of the total national workforce and upwards of 70% of rural Kenyans.\n"
                                "- **Foreign Exchange Reserves:** Major cash crop exports (tea, cut flowers, coffee, fresh vegetables) generate crucial foreign currency needed to purchase energy, transport fuel, medicines, and technology."
                            )
                        }
                    }
                ]
            },
            {
                "page_number": 3,
                "page_title": "Industrial Raw Materials & Industrial Linkages",
                "blocks": [
                    {
                        "block_type": "diagram",
                        "component_type": "diagram",
                        "title": "Agricultural Economic Multiplier & Industrial Linkages",
                        "content": {
                            "caption": "Interdependent links connecting primary agriculture, processing, manufacturing, employment, and export revenues."
                        }
                    },
                    {
                        "block_type": "concept_explanation",
                        "component_type": "concept_explanation",
                        "title": "Feeding Secondary Manufacturing",
                        "content": {
                            "text": (
                                "Agricultural outputs serve as essential raw materials for diverse manufacturing industries:\n\n"
                                "- **Textiles & Apparel:** Cotton lint spun into yarn, fabric, and garments.\n"
                                "- **Edible Oil Refineries:** Sunflowers, palm nuts, coconuts, and soybeans pressed into cooking oils and margarines.\n"
                                "- **Leather & Tanning:** Cattle hides and goat skins tanned into footwear, handbags, and industrial belts.\n"
                                "- **Sugar & Beverages:** Sugarcane crushed into refined sugar and molasses for ethanol production."
                            )
                        }
                    }
                ]
            },
            {
                "page_number": 4,
                "page_title": "The Backbone of Kenya's Economy",
                "blocks": [
                    {
                        "block_type": "case_study",
                        "component_type": "case_study",
                        "title": "Why Kenya Calls Agriculture its 'Backbone'",
                        "content": {
                            "text": (
                                "In Kenya, when agriculture performs well due to favorable rainfall, national GDP growth accelerates. "
                                "Conversely, when severe droughts hit rural counties, food inflation surges, manufacturing output dips, and national economic growth stalls. "
                                "Rural prosperity directly determines the purchasing power of the entire Kenyan consumer market."
                            )
                        }
                    },
                    {
                        "block_type": "misconception_alert",
                        "component_type": "misconception_alert",
                        "title": "Does Modernization Make Agriculture Obsolete?",
                        "content": {
                            "misconception": "As developing countries industrialize and grow tech sectors, agriculture becomes unimportant.",
                            "correction": "Even the most technologically advanced economies (such as the USA, the Netherlands, and Japan) maintain highly subsidized, high-tech agricultural sectors to guarantee food security and secure high-value exports."
                        }
                    }
                ]
            },
            {
                "page_number": 5,
                "page_title": "Formative Assessment: Agricultural Importance",
                "blocks": [
                    {
                        "block_type": "multiple_choice_question",
                        "component_type": "multiple_choice_question",
                        "title": "Question 1: Economic Significance of Agriculture",
                        "content": {
                            "question": "Why is agriculture widely recognized as the 'backbone' of Kenya's national economy?",
                            "options": [
                                "It is the only industry in the country that utilizes digital mobile phones",
                                "It employs over 70% of the rural workforce and generates a major share of GDP and foreign currency",
                                "All Kenyan citizens exclusively live on commercial plantation estates",
                                "Kenya does not possess any manufacturing, mining, or service industries"
                            ],
                            "correct_answer": "It employs over 70% of the rural workforce and generates a major share of GDP and foreign currency",
                            "explanation": "Agriculture is the backbone because it underpins rural livelihoods, food security, national GDP, industrial raw materials, and foreign exchange reserves."
                        }
                    },
                    {
                        "block_type": "multiple_choice_question",
                        "component_type": "multiple_choice_question",
                        "title": "Question 2: Agro-Processing Definition",
                        "content": {
                            "question": "Which manufacturing sector relies directly on raw agricultural outputs to produce textiles, refined cooking oil, leather shoes, and canned fruit juices?",
                            "options": [
                                "Heavy Metallurgical Smelting",
                                "Telecommunications Hardware Assembly",
                                "Agro-Processing and Food Manufacturing",
                                "Petroleum Cracking and Petrochemicals"
                            ],
                            "correct_answer": "Agro-Processing and Food Manufacturing",
                            "explanation": "Agro-processing is the industrial manufacturing branch that refines, transforms, and packages raw agricultural commodities into commercial goods."
                        }
                    }
                ]
            }
        ]
    },

    # Lesson 7: Agricultural Regions and Spatial Patterns in Africa
    {
        "unit_order": 7,
        "unit_name": "Agricultural Regions and Spatial Patterns in Africa",
        "lesson_title": "Agricultural Regions and Spatial Patterns in Africa",
        "pages": [
            {
                "page_number": 1,
                "page_title": "Introduction & Learning Objectives",
                "blocks": [
                    {
                        "block_type": "suggested_image",
                        "component_type": "suggested_image",
                        "title": "Tropical Cocoa Plantation in West Africa",
                        "content": {"text": "A photograph showing lush tropical cocoa trees bearing ripe orange cocoa pods in a West African equatorial plantation."}
                    },
                    {
                        "block_type": "learning_goal",
                        "component_type": "learning_goal",
                        "title": "Lesson Objectives: Spatial Patterns in Africa",
                        "content": {
                            "text": (
                                "By the end of this lesson, you will be able to:\n\n"
                                "- Map and characterize the major agricultural zones of Africa (Equatorial, Savannah, Mediterranean, Temperate Grasslands)\n"
                                "- Explain how continental climate belts determine the spatial distribution of cash crops and pastoralism\n"
                                "- Analyze the relationship between population density, land scarcity, and land-use intensity across Africa"
                            )
                        }
                    },
                    {
                        "block_type": "concept_explanation",
                        "component_type": "concept_explanation",
                        "title": "Prerequisite Spark: Africa's Continental Farming Quilt",
                        "content": {
                            "text": (
                                "Across the immense African continent, farming styles change dramatically. In the northern and southern extremes, "
                                "orchards produce wine grapes, olives, and citrus. Along the equator, humid rainforests host cocoa, rubber, and oil palm plantations. "
                                "Across the sweeping savannahs, pastoral cattle and drought-hardy grains dominate. This continental tapestry is governed by Africa's distinct climate zones!"
                            )
                        }
                    }
                ]
            },
            {
                "page_number": 2,
                "page_title": "Definitions & African Agricultural Zones",
                "blocks": [
                    {
                        "block_type": "definition_card",
                        "component_type": "definition_card",
                        "title": "Spatial Agricultural Geography",
                        "content": {
                            "definitions": [
                                {
                                    "term": "Spatial Distribution",
                                    "definition": "The geographical arrangement, clustering, or dispersion of physical and human phenomena across the Earth's surface.",
                                    "simple": "The pattern of where things are located across a map or region."
                                },
                                {
                                    "term": "Agricultural Region",
                                    "definition": "A continuous geographical territory exhibiting relatively homogeneous climatic conditions, soil types, crop combinations, and farming methods.",
                                    "simple": "An area sharing similar climate, soils, and typical farm types."
                                },
                                {
                                    "term": "Rainfed Agriculture",
                                    "definition": "Agricultural production systems that rely exclusively on natural precipitation rather than artificial canal or groundwater irrigation.",
                                    "simple": "Farming that depends entirely on natural rain."
                                }
                            ]
                        }
                    },
                    {
                        "block_type": "concept_explanation",
                        "component_type": "concept_explanation",
                        "title": "The Four Major African Agro-Climatic Zones",
                        "content": {
                            "text": (
                                "Continental farming systems align with major bioclimatic zones:\n\n"
                                "1. **Equatorial Wet Zone (West & Central Africa):** Year-round high temperatures and heavy rainfall (>1,600 mm). Dominant crops: cocoa, oil palm, rubber, cassava, plantains.\n"
                                "2. **Tropical Savannah Zone (East, West & Southern Africa):** Distinct wet and dry seasons. Dominant activities: mixed grain cultivation (maize, sorghum, millet), pulses, and pastoral livestock.\n"
                                "3. **Mediterranean Zones (North African coast & South African Cape):** Mild, wet winters and hot, dry summers. Dominant crops: citrus fruits, olives, viticulture (grapes), and winter wheat.\n"
                                "4. **Temperate Grasslands (South African Highveld):** Moderate rainfall and cooler temperatures. Dominant systems: commercial mechanized grain (maize, wheat) and commercial livestock ranching."
                            )
                        }
                    }
                ]
            },
            {
                "page_number": 3,
                "page_title": "Spatial Distribution Map & Land-Use Intensity",
                "blocks": [
                    {
                        "block_type": "diagram",
                        "component_type": "diagram",
                        "title": "African Agricultural Eco-zones Map",
                        "content": {
                            "caption": "Continental distribution of Mediterranean, Saharan/Oases, Sahelian pastoral, Savannah mixed, and Equatorial plantation zones."
                        }
                    },
                    {
                        "block_type": "concept_explanation",
                        "component_type": "concept_explanation",
                        "title": "Population Density and Land-Use Intensity",
                        "content": {
                            "text": (
                                "Agricultural intensity is closely correlated with rural population density:\n\n"
                                "- **High-Density Regions (Ethiopian Highlands, East African Rift Highlands, Nile Valley):** Extreme land scarcity forces continuous cultivation, intercropping, and multi-tier agroforestry on tiny smallholder plots.\n"
                                "- **Low-Density Regions (Sahel, Kalahari, Miombo Woodlands):** Abundant land allows extensive pastoral grazing and traditional shifting bush fallowing."
                            )
                        }
                    }
                ]
            },
            {
                "page_number": 4,
                "page_title": "Regional Case: West African Cocoa Belt",
                "blocks": [
                    {
                        "block_type": "case_study",
                        "component_type": "case_study",
                        "title": "The West African Cocoa Dominance",
                        "content": {
                            "text": (
                                "Côte d'Ivoire and Ghana together produce nearly 60% of the world's total cocoa supply. "
                                "This spatial concentration is enabled by the equatorial forest environment: high year-round humidity, "
                                "temperatures consistently between 22°C and 30°C, and rich canopy shade provided by remnant rainforest trees."
                            )
                        }
                    },
                    {
                        "block_type": "misconception_alert",
                        "component_type": "misconception_alert",
                        "title": "Is the Sahara Completely Devoid of Agriculture?",
                        "content": {
                            "misconception": "The Sahara Desert is an empty wasteland where no agriculture can ever occur.",
                            "correction": "The Sahara contains fertile oases fed by artesian aquifers, where intensive tiered irrigation produces high-value date palms, figs, pomegranates, and vegetables."
                        }
                    }
                ]
            },
            {
                "page_number": 5,
                "page_title": "Formative Assessment: African Agricultural Regions",
                "blocks": [
                    {
                        "block_type": "multiple_choice_question",
                        "component_type": "multiple_choice_question",
                        "title": "Question 1: Mediterranean Agriculture Characteristics",
                        "content": {
                            "question": "Which African agricultural zone features mild, wet winters and hot, dry summers, making it ideal for specialized orchards of olives, citrus, and wine grapes?",
                            "options": [
                                "Equatorial Rainforest Belt",
                                "Tropical Savannah Zone",
                                "Mediterranean Coastal Zone",
                                "Sahelian Pastoral Rangeland"
                            ],
                            "correct_answer": "Mediterranean Coastal Zone",
                            "explanation": "The Mediterranean climate zones in North Africa and the Western Cape of South Africa support orchard viticulture and citrus due to their winter rain patterns."
                        }
                    },
                    {
                        "block_type": "multiple_choice_question",
                        "component_type": "multiple_choice_question",
                        "title": "Question 2: West African Cash Crop Concentration",
                        "content": {
                            "question": "In the humid equatorial rainforest belt of West Africa (Côte d'Ivoire and Ghana), which cash crop is the dominant export commodity?",
                            "options": [
                                "Temperate Wheat",
                                "Cocoa",
                                "Drought-Resistant Sorghum",
                                "Pyrethrum"
                            ],
                            "correct_answer": "Cocoa",
                            "explanation": "Cocoa requires high year-round temperatures, high humidity, and heavy rainfall typical of West Africa's equatorial belt. Côte d'Ivoire and Ghana are the global leaders in cocoa exports."
                        }
                    }
                ]
            }
        ]
    },

    # Lesson 8: Key Trends in African Agriculture
    {
        "unit_order": 8,
        "unit_name": "Key Trends in African Agriculture",
        "lesson_title": "Key Trends in African Agriculture",
        "pages": [
            {
                "page_number": 1,
                "page_title": "Introduction & Learning Objectives",
                "blocks": [
                    {
                        "block_type": "suggested_image",
                        "component_type": "suggested_image",
                        "title": "African Farmer Accessing Mobile Digital Agronomy",
                        "content": {"text": "A photograph showing a smallholder farmer in an African field using a smartphone app to check weather alerts and market commodity prices."}
                    },
                    {
                        "block_type": "learning_goal",
                        "component_type": "learning_goal",
                        "title": "Lesson Objectives: Modern Trends in African Agriculture",
                        "content": {
                            "text": (
                                "By the end of this lesson, you will be able to:\n\n"
                                "- Explain how mobile digital technology (ICT) and FinTech are empowering smallholder farmers\n"
                                "- Analyze the transition from traditional subsistence to commercial agribusiness models\n"
                                "- Evaluate changing demographic trends, including youth agripreneurship and women's land tenure rights"
                            )
                        }
                    },
                    {
                        "block_type": "concept_explanation",
                        "component_type": "concept_explanation",
                        "title": "Prerequisite Spark: The Connected Farmer",
                        "content": {
                            "text": (
                                "Visit a rural Kenyan farm today, and you are likely to see a farmer holding a smartphone, checking real-time potato prices in Nairobi, "
                                "receiving instant mobile money payments for milk, and studying a localized 7-day rainfall forecast. Technology is transforming African farming "
                                "from a manual struggle into a connected, data-driven business!"
                            )
                        }
                    }
                ]
            },
            {
                "page_number": 2,
                "page_title": "Definitions & The Digital Agricultural Revolution",
                "blocks": [
                    {
                        "block_type": "definition_card",
                        "component_type": "definition_card",
                        "title": "Modern Agritech Terminology",
                        "content": {
                            "definitions": [
                                {
                                    "term": "Agribusiness",
                                    "definition": "The comprehensive commercial sector encompassing farming operations, processing, input manufacturing, logistics, and retail marketing conducted on corporate business principles.",
                                    "simple": "Treating the entire farming and food production process as a commercial business."
                                },
                                {
                                    "term": "Precision Agriculture",
                                    "definition": "A farming management concept that uses satellite GPS mapping, drone imagery, and IoT soil sensors to optimize fertilizer and water applications to specific field zones.",
                                    "simple": "Using sensors, drones, and digital data to give crops the exact water and fertilizer they need."
                                },
                                {
                                    "term": "Mobile FinTech Inclusion",
                                    "definition": "The provision of affordable digital micro-credit, crop insurance, and payment systems to unbanked rural farmers via mobile phone networks.",
                                    "simple": "Using mobile phones to borrow money, buy crop insurance, and receive payments."
                                }
                            ]
                        }
                    },
                    {
                        "block_type": "concept_explanation",
                        "component_type": "concept_explanation",
                        "title": "Four Transformative Continental Trends",
                        "content": {
                            "text": (
                                "African agriculture is experiencing fundamental structural shifts:\n\n"
                                "1. **Digital Agronomy & Mobile Platforms:** SMS and smartphone apps (e.g., DigiFarm, iShamba) deliver extension advice, pest diagnostics, and transparent market pricing.\n"
                                "2. **FinTech & Parametric Insurance:** Satellite-indexed crop insurance policies trigger automatic mobile payouts when regional rainfall falls below drought thresholds.\n"
                                "3. **Irrigation Expansion:** Shifting from vulnerable rainfed farming toward solar-powered drip kits and rainwater retention dams.\n"
                                "4. **Youth and Gender Inclusivity:** Increasing legal reforms securing female land ownership and young 'agripreneurs' deploying greenhouse and poultry ventures."
                            )
                        }
                    }
                ]
            },
            {
                "page_number": 3,
                "page_title": "Agri-Tech Solutions & Solar Cold Storage",
                "blocks": [
                    {
                        "block_type": "diagram",
                        "component_type": "diagram",
                        "title": "Digital Agriculture & Agribusiness Ecosystem",
                        "content": {
                            "caption": "Integration of satellite weather data, mobile finance, solar cold-chains, and direct-to-consumer e-commerce."
                        }
                    },
                    {
                        "block_type": "concept_explanation",
                        "component_type": "concept_explanation",
                        "title": "Solar Cold-Storage Revolution",
                        "content": {
                            "text": (
                                "A critical technological breakthrough across East Africa is off-grid solar-powered cold storage. "
                                "Pay-as-you-store solar cold rooms established at rural markets allow vegetable and dairy farmers to preserve "
                                "perishable produce for weeks, eliminating the pressure to dump harvests at throwaway prices to opportunistic brokers."
                            )
                        }
                    }
                ]
            },
            {
                "page_number": 4,
                "page_title": "Kenyan Agritech Leadership",
                "blocks": [
                    {
                        "block_type": "case_study",
                        "component_type": "case_study",
                        "title": "Kenya as the Silicon Savannah of Agritech",
                        "content": {
                            "text": (
                                "Kenya is the global hub for African digital agriculture innovation. Platforms like Twiga Foods connect "
                                "tens of thousands of rural vegetable farmers directly to urban kiosk retailers using mobile ordering, "
                                "bypassing predatory cartels and reducing post-harvest supply chain losses from 40% down to under 5%."
                            )
                        }
                    },
                    {
                        "block_type": "misconception_alert",
                        "component_type": "misconception_alert",
                        "title": "Is Modernization Only for Large Estates?",
                        "content": {
                            "misconception": "Modern agricultural technologies only benefit large multinational commercial plantations.",
                            "correction": "Digital mobile advisory, solar drip kits, improved seed varieties, and micro-insurance are designed specifically to scale smallholder farms operating on 1-2 acres."
                        }
                    }
                ]
            },
            {
                "page_number": 5,
                "page_title": "Formative Assessment: Key Trends in African Agriculture",
                "blocks": [
                    {
                        "block_type": "multiple_choice_question",
                        "component_type": "multiple_choice_question",
                        "title": "Question 1: Mobile Technology Impact",
                        "content": {
                            "question": "How are mobile phone applications primarily helping smallholder farmers in rural Kenya improve their agricultural profitability?",
                            "options": [
                                "By physically tilling and plowing fields automatically",
                                "By providing direct access to transparent market commodity prices, localized weather forecasts, and mobile payments",
                                "By chemically increasing seasonal cloud cover and monsoonal rainfall",
                                "By replacing all human labor across tea plantations"
                            ],
                            "correct_answer": "By providing direct access to transparent market commodity prices, localized weather forecasts, and mobile payments",
                            "explanation": "Mobile phones bridge the rural information divide, giving farmers real-time pricing data, weather forecasts, and instant financial transaction tools."
                        }
                    },
                    {
                        "block_type": "multiple_choice_question",
                        "component_type": "multiple_choice_question",
                        "title": "Question 2: Commercial Agribusiness Definition",
                        "content": {
                            "question": "What term describes the comprehensive integration of farming with commercial business practices, corporate value chains, and modern agro-processing?",
                            "options": [
                                "Nomadic Pastoralism",
                                "Shifting Cultivation",
                                "Agribusiness",
                                "Extensive Bush Fallowing"
                            ],
                            "correct_answer": "Agribusiness",
                            "explanation": "Agribusiness refers to treating the entire agricultural sector—from input supply to consumer retail—as a commercially organized, profit-driven enterprise."
                        }
                    }
                ]
            }
        ]
    },

    # Lesson 9: Challenges Facing Kenyan Agriculture: Climatic & Biological Threats
    {
        "unit_order": 9,
        "unit_name": "Challenges Facing Kenyan Agriculture: Climatic & Biological Threats",
        "lesson_title": "Challenges Facing Kenyan Agriculture: Climatic & Biological Threats",
        "pages": [
            {
                "page_number": 1,
                "page_title": "Introduction & Learning Objectives",
                "blocks": [
                    {
                        "block_type": "suggested_image",
                        "component_type": "suggested_image",
                        "title": "Locust Swarms and Crop Damage in East Africa",
                        "content": {"text": "A photograph showing a dense migratory desert locust swarm descending upon agricultural fields and destroying crops in East Africa."}
                    },
                    {
                        "block_type": "learning_goal",
                        "component_type": "learning_goal",
                        "title": "Lesson Objectives: Climatic & Biological Threats",
                        "content": {
                            "text": (
                                "By the end of this lesson, you will be able to:\n\n"
                                "- Analyze the extreme vulnerability of rainfed agriculture to climate variability, droughts, and flash floods\n"
                                "- Identify major biological threats: invasive insect pests (Fall Armyworm, Desert Locusts) and fungal/viral diseases\n"
                                "- Explain the causes and catastrophic impacts of soil erosion, nutrient exhaustion, and land degradation"
                            )
                        }
                    },
                    {
                        "block_type": "concept_explanation",
                        "component_type": "concept_explanation",
                        "title": "Prerequisite Spark: The Farmer's Gamble with Rain and Pests",
                        "content": {
                            "text": (
                                "Imagine a farmer who has invested their life savings to lease land, purchase certified seeds, and hire planting labor. "
                                "The first rains trigger germination, but then the rains abruptly cease for months. If the dry spell doesn't kill the young maize, "
                                "a swarm of Fall Armyworms invades the field overnight. This illustrates the acute biological and climatic risks Kenyan farmers navigate daily!"
                            )
                        }
                    }
                ]
            },
            {
                "page_number": 2,
                "page_title": "Definitions & Environmental Hazards",
                "blocks": [
                    {
                        "block_type": "definition_card",
                        "component_type": "definition_card",
                        "title": "Agricultural Risk Terminology",
                        "content": {
                            "definitions": [
                                {
                                    "term": "Climate Variability",
                                    "definition": "Short-term deviations and fluctuations in meteorological conditions (e.g., delayed rains, mid-season dry spells, torrential deluges) around long-term climatic averages.",
                                    "simple": "Unpredictable changes in weather patterns, such as sudden droughts or heavy storms."
                                },
                                {
                                    "term": "Soil Degradation",
                                    "definition": "The physical, chemical, and biological decline in soil productivity caused by topsoil erosion, organic matter depletion, acidification, or salinization.",
                                    "simple": "The loss of soil quality, fertility, and depth due to poor farming and erosion."
                                },
                                {
                                    "term": "Desert Locust Swarms",
                                    "definition": "Highly destructive, migratory insect pests (Schistocerca gregaria) that aggregate into dense flying swarms capable of consuming their body weight in green vegetation daily.",
                                    "simple": "Massive swarms of flying insects that strip crops and pastures clean in hours."
                                }
                            ]
                        }
                    },
                    {
                        "block_type": "concept_explanation",
                        "component_type": "concept_explanation",
                        "title": "Climatic Vulnerability: Over-Reliance on Rain",
                        "content": {
                            "text": (
                                "Over 80% of Kenyan agriculture is strictly rainfed, exposing it to extreme climate hazards:\n\n"
                                "- **Severe Recurrent Droughts:** Delayed or failed seasonal rains cause catastrophic crop failures in breadbasket counties and trigger massive livestock mortality across pastoral ASALs.\n"
                                "- **Flash Flooding & Soil Loss:** Torrential downpours wash away fertile topsoil, trigger mudslides on steep highland slopes, drown livestock, and wash out rural access bridges."
                            )
                        }
                    }
                ]
            },
            {
                "page_number": 3,
                "page_title": "Biological Threats: Pests & Diseases",
                "blocks": [
                    {
                        "block_type": "diagram",
                        "component_type": "diagram",
                        "title": "Kenya Agro-Ecological Zones & Climate Hazard Vulnerability",
                        "content": {
                            "caption": "Spatial distribution of high-potential agricultural zones versus drought-prone ASALs and pest migration corridors."
                        }
                    },
                    {
                        "block_type": "concept_explanation",
                        "component_type": "concept_explanation",
                        "title": "Major Crop & Livestock Pathogens",
                        "content": {
                            "text": (
                                "Kenyan producers face relentless biological hazards:\n\n"
                                "- **Fall Armyworm (Spodoptera frugiperda):** Invasive caterpillar that burrows deep into maize whorls and cobs, wiping out up to 30-50% of harvests.\n"
                                "- **Maize Lethal Necrosis (MLN):** Devastating synergistic viral disease causing complete crop chlorosis and zero grain yield.\n"
                                "- **Coffee Berry Disease (CBD):** Fungal infection turning green berries black, causing premature berry drop.\n"
                                "- **Livestock Epidemics:** East Coast Fever (tick-borne), Foot-and-Mouth Disease (FMD), and Peste des Petits Ruminants (PPR)."
                            )
                        }
                    }
                ]
            },
            {
                "page_number": 4,
                "page_title": "Case Study: 2019-2020 Locust Invasion",
                "blocks": [
                    {
                        "block_type": "case_study",
                        "component_type": "case_study",
                        "title": "The 2019-2020 Desert Locust Crisis in Northern Kenya",
                        "content": {
                            "text": (
                                "In 2019-2020, unusual cyclone activity over the Arabian Peninsula triggered the worst desert locust upsurge "
                                "in East Africa in 70 years. Swarms spanning hundreds of square kilometers invaded Mandera, Wajir, Marsabit, Isiolo, "
                                "and Samburu, consuming tens of thousands of hectares of pastures and food crops, precipitating severe food insecurity."
                            )
                        }
                    },
                    {
                        "block_type": "misconception_alert",
                        "component_type": "misconception_alert",
                        "title": "Is Blanket Chemical Spraying the Best Fix?",
                        "content": {
                            "misconception": "When pest outbreaks occur, the most effective response is spraying massive quantities of synthetic chemical pesticides everywhere.",
                            "correction": "Blanket spraying kills vital pollinators (bees), contaminates water sources, and creates pesticide-resistant super-pests. Sustainable farming relies on Integrated Pest Management (IPM), combining biological predators, pheromone traps, and botanical sprays."
                        }
                    }
                ]
            },
            {
                "page_number": 5,
                "page_title": "Formative Assessment: Climatic & Biological Hazards",
                "blocks": [
                    {
                        "block_type": "multiple_choice_question",
                        "component_type": "multiple_choice_question",
                        "title": "Question 1: Rainfed Farming Vulnerability",
                        "content": {
                            "question": "Why is Kenya's agricultural production highly vulnerable to climate variability, such as delayed seasonal rains and mid-season dry spells?",
                            "options": [
                                "Over 80% of Kenyan farming is rainfed, relying completely on natural seasonal precipitation",
                                "Most Kenyan farms are located inside underground geothermal chambers",
                                "Kenyan smallholders do not plant crop seeds",
                                "Droughts only occur in coastal mangrove swamps"
                            ],
                            "correct_answer": "Over 80% of Kenyan farming is rainfed, relying completely on natural seasonal precipitation",
                            "explanation": "Because more than four-fifths of Kenyan agricultural land relies strictly on rainfall rather than irrigation, any irregularity in seasonal rain directly harms crop yields."
                        }
                    },
                    {
                        "block_type": "multiple_choice_question",
                        "component_type": "multiple_choice_question",
                        "title": "Question 2: Destructive Cereal Pest",
                        "content": {
                            "question": "Which invasive caterpillar pest burrows deep into the growing whorl and cobs of Kenyan maize plants, causing catastrophic leaf and grain damage?",
                            "options": [
                                "Desert Locust",
                                "Fall Armyworm",
                                "Tsetse Fly",
                                "Quelea Bird"
                            ],
                            "correct_answer": "Fall Armyworm",
                            "explanation": "The Fall Armyworm is an aggressive invasive caterpillar that feeds on maize leaves, stems, and cobs, causing massive yield losses across sub-Saharan Africa."
                        }
                    }
                ]
            }
        ]
    },

    # Lesson 10: Challenges Facing Kenyan Agriculture: Socio-Economic Hurdles
    {
        "unit_order": 10,
        "unit_name": "Challenges Facing Kenyan Agriculture: Socio-Economic Hurdles",
        "lesson_title": "Challenges Facing Kenyan Agriculture: Socio-Economic Hurdles",
        "pages": [
            {
                "page_number": 1,
                "page_title": "Introduction & Learning Objectives",
                "blocks": [
                    {
                        "block_type": "suggested_image",
                        "component_type": "suggested_image",
                        "title": "Transport Challenges on Rural Muddy Feeder Roads",
                        "content": {"text": "A photograph showing a vehicle stuck in deep mud on an unpaved rural road in Vihiga, Kenya, hindering transport of agricultural produce."}
                    },
                    {
                        "block_type": "learning_goal",
                        "component_type": "learning_goal",
                        "title": "Lesson Objectives: Socio-Economic Constraints",
                        "content": {
                            "text": (
                                "By the end of this lesson, you will be able to:\n\n"
                                "- Explain how generational land subdivision and fragmentation undermines agricultural viability\n"
                                "- Analyze the impact of poor rural road infrastructure and lack of cold chains on post-harvest losses\n"
                                "- Evaluate credit constraints, exorbitant input costs, and middleman price exploitation"
                            )
                        }
                    },
                    {
                        "block_type": "concept_explanation",
                        "component_type": "concept_explanation",
                        "title": "Prerequisite Spark: The Rotting Harvest",
                        "content": {
                            "text": (
                                "A farmer in Nyandarua harvests a bumper crop of fresh cabbages and potatoes. But heavy rains turn the unpaved feeder road into impassable mud. "
                                "Trucks cannot reach the farm. The farmer must either watch the harvest rot in the field or sell it for pennies to an exploitative broker with a tractor. "
                                "This highlights the devastating socio-economic hurdles confronting rural agriculture!"
                            )
                        }
                    }
                ]
            },
            {
                "page_number": 2,
                "page_title": "Definitions & Structural Constraints",
                "blocks": [
                    {
                        "block_type": "definition_card",
                        "component_type": "definition_card",
                        "title": "Socio-Economic Agrarian Terminology",
                        "content": {
                            "definitions": [
                                {
                                    "term": "Land Fragmentation",
                                    "definition": "The progressive subdivision of agricultural landholdings into smaller, geographically scattered parcels across successive generations due to customary inheritance laws.",
                                    "simple": "Dividing family land into smaller and smaller tiny plots among children."
                                },
                                {
                                    "term": "Post-Harvest Losses (PHL)",
                                    "definition": "The quantifiable loss of agricultural produce occurring between harvesting and retail sale due to poor storage, insect infestation, rot, or transport delays.",
                                    "simple": "Crops that spoil or are wasted after harvesting because of bad roads or poor storage."
                                },
                                {
                                    "term": "Agricultural Input Costs",
                                    "definition": "The financial expenditures required to purchase farming supplies, including certified seeds, basal fertilizers, agrochemicals, fuel, and tractor hire.",
                                    "simple": "The cost of buying seeds, fertilizers, and equipment needed to farm."
                                }
                            ]
                        }
                    },
                    {
                        "block_type": "concept_explanation",
                        "component_type": "concept_explanation",
                        "title": "The Three Core Socio-Economic Bottlenecks",
                        "content": {
                            "text": (
                                "Kenyan agriculture is constrained by three major structural barriers:\n\n"
                                "1. **Land Fragmentation:** In fertile highlands (Kiambu, Kisii, Murang'a), average plots have shrunk to <0.5 acres, preventing mechanization and economies of scale.\n"
                                "2. **Inadequate Feeder Road Infrastructure:** Muddy rural roads during harvest seasons leave fresh tomatoes, mangoes, and milk stranded, causing 30-40% post-harvest losses.\n"
                                "3. **High Input Prices & Credit Barriers:** Commercial banks demand land title deeds as collateral, which most smallholders and women lack, preventing investment in irrigation and machinery."
                            )
                        }
                    }
                ]
            },
            {
                "page_number": 3,
                "page_title": "Post-Harvest Loss Interventions & Storage",
                "blocks": [
                    {
                        "block_type": "diagram",
                        "component_type": "diagram",
                        "title": "Post-Harvest Loss Interventions & Storage Solutions",
                        "content": {
                            "caption": "Comparison of traditional loss points versus modern hermetic bags, solar dryers, and metal silos."
                        }
                    },
                    {
                        "block_type": "concept_explanation",
                        "component_type": "concept_explanation",
                        "title": "Hermetic Storage and Metal Silos",
                        "content": {
                            "text": (
                                "Post-harvest grain loss to weevils and rodents traditionally consumes 20-30% of harvested maize. "
                                "Adopting modern hermetic storage bags (e.g., PICS bags) creates an oxygen-free environment that suffocates insects "
                                "without requiring dangerous chemical dusts, allowing farmers to store grain safely for over a year."
                            )
                        }
                    }
                ]
            },
            {
                "page_number": 4,
                "page_title": "Land Fragmentation & Cooperative Power",
                "blocks": [
                    {
                        "block_type": "case_study",
                        "component_type": "case_study",
                        "title": "Extreme Fragmentation in Kisii and Central Highlands",
                        "content": {
                            "text": (
                                "In Kisii, Vihiga, and Kiambu counties, population pressure has subdivided farm plots into narrow strips "
                                "barely large enough for a homestead and a few banana mats. To overcome this, farmers are forming producer cooperatives "
                                "to bulk their produce together, negotiate directly with supermarket buyers, and access input subsidies."
                            )
                        }
                    },
                    {
                        "block_type": "misconception_alert",
                        "component_type": "misconception_alert",
                        "title": "Are Middlemen Purely Evil?",
                        "content": {
                            "misconception": "Agricultural brokers (middlemen) provide zero value and exist purely to exploit defenseless farmers.",
                            "correction": "While unscrupulous cartels exploit price asymmetries, brokers provide essential logistics: supplying cash at farm gate, bearing spoilage risk during transit, and bulking small yields from hundreds of tiny plots to fill trucks for distant urban markets."
                        }
                    }
                ]
            },
            {
                "page_number": 5,
                "page_title": "Formative Assessment: Socio-Economic Hurdles",
                "blocks": [
                    {
                        "block_type": "multiple_choice_question",
                        "component_type": "multiple_choice_question",
                        "title": "Question 1: Land Fragmentation Challenge",
                        "content": {
                            "question": "Why does continuous generational land fragmentation present a major barrier to modern agricultural modernization in Kenya?",
                            "options": [
                                "It makes the underlying volcanic soil permanently toxic to crops",
                                "Plots become too small and scattered to practice mechanization or achieve economies of scale",
                                "It prevents atmospheric rainfall from reaching the ground",
                                "It legally obligates all smallholders to become nomadic pastoralists"
                            ],
                            "correct_answer": "Plots become too small and scattered to practice mechanization or achieve economies of scale",
                            "explanation": "Generational subdivision breaks arable land into micro-plots where operating tractors or achieving commercial production efficiencies becomes economically impossible."
                        }
                    },
                    {
                        "block_type": "multiple_choice_question",
                        "component_type": "multiple_choice_question",
                        "title": "Question 2: Post-Harvest Loss Identification",
                        "content": {
                            "question": "A farmer harvests 100 bags of maize but loses 30 bags in storage because rats and weevils infest the unsealed wooden granary. What is this loss scientifically called?",
                            "options": [
                                "Tectonic Fracturing",
                                "Edaphic Salinization",
                                "Post-Harvest Loss",
                                "Input Depletion"
                            ],
                            "correct_answer": "Post-Harvest Loss",
                            "explanation": "Post-harvest loss refers to the destruction or spoilage of harvested food along the value chain prior to consumer utilization."
                        }
                    }
                ]
            }
        ]
    },

    # Lesson 11: Sustainable and Climate-Smart Agricultural Strategies
    {
        "unit_order": 11,
        "unit_name": "Sustainable and Climate-Smart Agricultural Strategies",
        "lesson_title": "Sustainable and Climate-Smart Agricultural Strategies",
        "pages": [
            {
                "page_number": 1,
                "page_title": "Introduction & Learning Objectives",
                "blocks": [
                    {
                        "block_type": "suggested_image",
                        "component_type": "suggested_image",
                        "title": "Agroforestry and Fanya Juu Terraces in Kenya",
                        "content": {"text": "A photograph showing agroforestry trees integrated with crops on terraced hillsides around Mount Kenya."}
                    },
                    {
                        "block_type": "learning_goal",
                        "component_type": "learning_goal",
                        "title": "Lesson Objectives: Climate-Smart Strategies",
                        "content": {
                            "text": (
                                "By the end of this lesson, you will be able to:\n\n"
                                "- Define Climate-Smart Agriculture (CSA) and evaluate its three core pillars (productivity, adaptation, mitigation)\n"
                                "- Explain soil and water conservation techniques: Fanya Juu terracing, mulching, contour bunds, and agroforestry\n"
                                "- Analyze the ecological benefits of crop diversification, organic composting, and minimum tillage"
                            )
                        }
                    },
                    {
                        "block_type": "concept_explanation",
                        "component_type": "concept_explanation",
                        "title": "Prerequisite Spark: Taming the Hillside",
                        "content": {
                            "text": (
                                "Imagine standing on a dry, degraded hillside in Machakos county. During the rains, water rushes down the slope, carving gullies "
                                "and stripping fertile topsoil. During the dry season, crops wither and die. What can a farmer do? By digging stepped terraces, "
                                "planting deep-rooted trees, and mulching the soil with dry grass, the runoff is trapped, moisture is preserved, and the hill becomes a lush green oasis!"
                            )
                        }
                    }
                ]
            },
            {
                "page_number": 2,
                "page_title": "Definitions & The Three Pillars of CSA",
                "blocks": [
                    {
                        "block_type": "definition_card",
                        "component_type": "definition_card",
                        "title": "Sustainable Agriculture Terminology",
                        "content": {
                            "definitions": [
                                {
                                    "term": "Climate-Smart Agriculture (CSA)",
                                    "definition": "An integrated agrarian landscape approach that sustainably increases productivity, enhances climate resilience (adaptation), and reduces greenhouse gas emissions (mitigation).",
                                    "simple": "Farming methods that boost food production while coping with climate change and protecting the environment."
                                },
                                {
                                    "term": "Agroforestry",
                                    "definition": "The deliberate integration of woody perennials (trees and shrubs) with agricultural crops and/or livestock on the same land-management unit.",
                                    "simple": "Growing beneficial trees alongside crops and farm animals on the same plot."
                                },
                                {
                                    "term": "Mulching",
                                    "definition": "The agronomic practice of applying a protective layer of organic residues (straw, leaves, grass) over bare soil to conserve moisture and suppress weeds.",
                                    "simple": "Covering the ground with dry grass or leaves to keep moisture in the soil and stop weeds."
                                }
                            ]
                        }
                    },
                    {
                        "block_type": "concept_explanation",
                        "component_type": "concept_explanation",
                        "title": "The Three Pillars of CSA",
                        "content": {
                            "text": (
                                "Climate-Smart Agriculture addresses food security and climate change simultaneously:\n\n"
                                "1. **Sustainably Increase Productivity:** Enhance crop and livestock yields and farm incomes to support food security.\n"
                                "2. **Build Resilience (Adaptation):** Fortify smallholder farming systems against climate shocks, droughts, floods, and invasive pests.\n"
                                "3. **Reduce Greenhouse Gas Emissions (Mitigation):** Sequester carbon in soil organic matter and trees while minimizing nitrous oxide and methane emissions."
                            )
                        }
                    }
                ]
            },
            {
                "page_number": 3,
                "page_title": "Conservation Engineering: Terraces & Agroforestry",
                "blocks": [
                    {
                        "block_type": "diagram",
                        "component_type": "diagram",
                        "title": "Climate-Smart Agriculture Matrix: Drip Irrigation / Agroforestry / Terracing",
                        "content": {
                            "caption": "Engineering mechanics of Fanya Juu terracing, agroforestry canopy layers, and water-saving drip fertigation."
                        }
                    },
                    {
                        "block_type": "concept_explanation",
                        "component_type": "concept_explanation",
                        "title": "Fanya Juu Terracing Mechanics",
                        "content": {
                            "text": (
                                "The legendary Kenyan **Fanya Juu** ('throw upward' in Swahili) terracing technique:\n\n"
                                "- **Excavation:** A trench is dug along the contour line, and the excavated soil is thrown uphill to form a ridge.\n"
                                "- **Vegetative Stabilization:** The ridge is planted with fodder grass (e.g., Napier grass) to bind the soil with root networks.\n"
                                "- **Natural Leveling:** Over several seasons, eroding soil washes down into the trench, naturally leveling the slope into flat, stepped benches that capture 100% of rainfall runoff."
                            )
                        }
                    }
                ]
            },
            {
                "page_number": 4,
                "page_title": "Agroforestry Benefits & Machakos Transformation",
                "blocks": [
                    {
                        "block_type": "case_study",
                        "component_type": "case_study",
                        "title": "The Machakos Miracle: From Wasteland to Terraced Eden",
                        "content": {
                            "text": (
                                "In the 1930s, British colonial reports condemned Machakos as an environmental disaster doomed by severe gully erosion. "
                                "Over subsequent decades, Akamba smallholders mobilized community groups to terrace over 85% of arable hillsides "
                                "using Fanya Juu terraces, integrating Grevillea trees and fruit orchards, proving that community-led CSA can reverse desertification."
                            )
                        }
                    },
                    {
                        "block_type": "misconception_alert",
                        "component_type": "misconception_alert",
                        "title": "Do Trees Compete with Crops?",
                        "content": {
                            "misconception": "Planting trees among food crops always stunts crop yields because trees steal sunlight and water.",
                            "correction": "When deep-rooted agroforestry species (such as Grevillea robusta or nitrogen-fixing Calliandra) are selected, their roots draw water from deep subterranean layers, while their canopy fixes nitrogen and provides windbreak protection, enhancing crop yields."
                        }
                    }
                ]
            },
            {
                "page_number": 5,
                "page_title": "Formative Assessment: Sustainable & CSA Strategies",
                "blocks": [
                    {
                        "block_type": "multiple_choice_question",
                        "component_type": "multiple_choice_question",
                        "title": "Question 1: Fanya Juu Terracing Technique",
                        "content": {
                            "question": "Which soil and water conservation technique involves digging a trench along a contour line and throwing the excavated soil uphill to form a water-trapping ridge?",
                            "options": [
                                "Continuous Overgrazing",
                                "Fanya Juu Terracing",
                                "Slash-and-Burn Shifting Cultivation",
                                "Deep Mechanical Downhill Plowing"
                            ],
                            "correct_answer": "Fanya Juu Terracing",
                            "explanation": "'Fanya juu' means 'do upward' in Swahili. Throwing soil uphill creates a contour ridge that prevents water runoff, traps eroding topsoil, and creates flat farming benches over time."
                        }
                    },
                    {
                        "block_type": "multiple_choice_question",
                        "component_type": "multiple_choice_question",
                        "title": "Question 2: Function of Mulching",
                        "content": {
                            "question": "What is the primary agronomic benefit of spreading dry maize stalks and grass as mulch over bare soil around vegetable crops?",
                            "options": [
                                "It accelerates soil water evaporation and drying",
                                "It forms a physical barrier that conserves soil moisture and suppresses weed germination",
                                "It attracts desert locust swarms to feed on vegetable leaves",
                                "It compacts the soil into hard stone to prevent root growth"
                            ],
                            "correct_answer": "It forms a physical barrier that conserves soil moisture and suppresses weed germination",
                            "explanation": "Mulch protects bare soil from direct solar radiation, drastically reducing water evaporation, lowering soil temperatures, and suppressing weed growth."
                        }
                    }
                ]
            }
        ]
    },

    # Lesson 12: The Critical Role of Agriculture in Food Security
    {
        "unit_order": 12,
        "unit_name": "The Critical Role of Agriculture in Food Security",
        "lesson_title": "The Critical Role of Agriculture in Food Security",
        "pages": [
            {
                "page_number": 1,
                "page_title": "Introduction & Learning Objectives",
                "blocks": [
                    {
                        "block_type": "suggested_image",
                        "component_type": "suggested_image",
                        "title": "Food Production and Market Abundance in Kenya",
                        "content": {"text": "A photograph showing a vibrant Kenyan open-air food market overflowing with fresh vegetables, maize, beans, and fruits, symbolizing food availability and access."}
                    },
                    {
                        "block_type": "learning_goal",
                        "component_type": "learning_goal",
                        "title": "Lesson Objectives: Food Security",
                        "content": {
                            "text": (
                                "By the end of this lesson, you will be able to:\n\n"
                                "- Define food security according to the FAO framework\n"
                                "- Analyze the Four Pillars of Food Security: Availability, Access, Utilization, and Stability\n"
                                "- Evaluate the link between smallholder agricultural productivity, poverty alleviation, and national dietary diversity"
                            )
                        }
                    },
                    {
                        "block_type": "concept_explanation",
                        "component_type": "concept_explanation",
                        "title": "Prerequisite Spark: A Hungry Nation Cannot Prosper",
                        "content": {
                            "text": (
                                "Have you ever heard the saying, 'A hungry nation is a weak nation'? If a society cannot reliably feed its citizens, "
                                "children suffer malnutrition and cognitive stunting, workforce productivity collapses, and national development stalls. "
                                "Food security is humanity's most fundamental requirement!"
                            )
                        }
                    }
                ]
            },
            {
                "page_number": 2,
                "page_title": "Definitions & The Four Pillars Framework",
                "blocks": [
                    {
                        "block_type": "definition_card",
                        "component_type": "definition_card",
                        "title": "Food Security Terminology",
                        "content": {
                            "definitions": [
                                {
                                    "term": "Food Security",
                                    "definition": "A situation that exists when all people, at all times, have physical, social, and economic access to sufficient, safe, and nutritious food that meets their dietary needs for an active and healthy life.",
                                    "simple": "When everyone always has enough safe, healthy, and affordable food to eat."
                                },
                                {
                                    "term": "Food Availability",
                                    "definition": "The physical presence of food stocks in sufficient quantities through domestic agricultural production, commercial food imports, or emergency food reserves.",
                                    "simple": "Having enough food physically present in the markets and granaries."
                                },
                                {
                                    "term": "Food Access",
                                    "definition": "The economic and physical capacity of households to acquire adequate nutritious food, governed by household income, commodity prices, and market transport.",
                                    "simple": "Having enough money and transport access to buy healthy food."
                                },
                                {
                                    "term": "Food Utilization",
                                    "definition": "The body's physiological absorption and biological use of nutrients from consumed food, supported by clean drinking water, adequate sanitation, and dietary diversity.",
                                    "simple": "How the human body uses nutrients from safe, balanced, and clean food."
                                }
                            ]
                        }
                    },
                    {
                        "block_type": "concept_explanation",
                        "component_type": "concept_explanation",
                        "title": "The Fourth Pillar: Food Stability",
                        "content": {
                            "text": (
                                "A food system is only secure when the final pillar—**Stability**—is achieved:\n\n"
                                "- **Stability:** Ensuring that food availability, access, and utilization are maintained consistently over time without periodic disruptions caused by seasonal dry spells, price spikes, or supply chain shocks."
                            )
                        }
                    }
                ]
            },
            {
                "page_number": 3,
                "page_title": "Food Security Pillars Model & Multimedia Analysis",
                "blocks": [
                    {
                        "block_type": "diagram",
                        "component_type": "diagram",
                        "title": "Food Security 4-Pillars Pillar Model",
                        "content": {
                            "caption": "Four-pillar structural model: Availability, Access, Utilization, and Stability supporting National Well-Being."
                        }
                    },
                    {
                        "block_type": "video",
                        "component_type": "video",
                        "title": "Educational Video: Understanding Food Security and Nutrition in Africa",
                        "content": {
                            "url": "https://www.youtube.com/watch?v=D-w_iUvBvQk",
                            "caption": "Video exploring food security pillars, post-harvest losses, and climate-smart agricultural interventions."
                        }
                    }
                ]
            },
            {
                "page_number": 4,
                "page_title": "Poverty Reduction, Hidden Hunger, & Case Insights",
                "blocks": [
                    {
                        "block_type": "concept_explanation",
                        "component_type": "concept_explanation",
                        "title": "Hidden Hunger vs Caloric Sufficiency",
                        "content": {
                            "text": (
                                "True food security requires more than just carbohydrates:\n\n"
                                "- **Caloric Sufficiency:** Simply eating enough energy (e.g., maize ugali daily) satisfies hunger but leads to **hidden hunger** (micronutrient deficiencies in iron, zinc, and vitamin A).\n"
                                "- **Dietary Diversity:** Cultivating indigenous African leafy vegetables (managu, terere), beans, orange-fleshed sweet potatoes, and keeping poultry supplies essential vitamins, iron, and proteins for child development."
                            )
                        }
                    },
                    {
                        "block_type": "case_study",
                        "component_type": "case_study",
                        "title": "Smallholder Productivity as a Poverty Cure",
                        "content": {
                            "text": (
                                "In Kenya, agricultural growth is estimated to be more than two to three times more effective at reducing poverty "
                                "than growth in any non-agricultural sector. When smallholder yields rise, families feed themselves, generate cash income, "
                                "and expand food supply in urban markets, lowering food prices for urban poor families."
                            )
                        }
                    }
                ]
            },
            {
                "page_number": 5,
                "page_title": "Formative Assessment: Food Security",
                "blocks": [
                    {
                        "block_type": "multiple_choice_question",
                        "component_type": "multiple_choice_question",
                        "title": "Question 1: Diagnosing Food Security Pillars",
                        "content": {
                            "question": "A nation has warehouses overflowing with imported wheat, but low-income slum residents cannot buy food due to unemployment and high prices. Which food security pillar is compromised?",
                            "options": [
                                "Food Availability",
                                "Food Access",
                                "Food Utilization",
                                "Atmospheric Stability"
                            ],
                            "correct_answer": "Food Access",
                            "explanation": "Food is physically available in the country (Availability), but poor families lack the economic purchasing power (income) to acquire it (Access)."
                        }
                    },
                    {
                        "block_type": "multiple_choice_question",
                        "component_type": "multiple_choice_question",
                        "title": "Question 2: Micronutrient Diversity",
                        "content": {
                            "question": "Why is cultivating a diverse combination of crops (sweet potatoes, indigenous greens, beans, maize) superior for household food security compared to growing maize alone?",
                            "options": [
                                "It requires full tractor mechanization across all fields",
                                "It provides a balanced spectrum of proteins, vitamins, and minerals, preventing malnutrition and hidden hunger",
                                "It stops any rain from falling onto the farm plots",
                                "It forces farmers to export all produce to foreign markets"
                            ],
                            "correct_answer": "It provides a balanced spectrum of proteins, vitamins, and minerals, preventing malnutrition and hidden hunger",
                            "explanation": "Dietary diversity addresses the food utilization pillar by supplying essential micronutrients, vitamins, and proteins needed for complete health."
                        }
                    }
                ]
            }
        ]
    },

    # Lesson 13: Local Field Study: Researching Agricultural Strategies
    {
        "unit_order": 13,
        "unit_name": "Local Field Study: Researching Agricultural Strategies",
        "lesson_title": "Local Field Study: Researching Agricultural Strategies",
        "pages": [
            {
                "page_number": 1,
                "page_title": "Introduction & Learning Objectives",
                "blocks": [
                    {
                        "block_type": "suggested_image",
                        "component_type": "suggested_image",
                        "title": "Fieldwork Students Conducting Agricultural Research",
                        "content": {"text": "A photograph showing geography and agriculture students in field gear conducting an outdoor farm investigation, mapping plots and recording data."}
                    },
                    {
                        "block_type": "learning_goal",
                        "component_type": "learning_goal",
                        "title": "Lesson Objectives: Field Study Design",
                        "content": {
                            "text": (
                                "By the end of this lesson, you will be able to:\n\n"
                                "- Formulate clear, focused research objectives and investigative hypotheses for a local farm field study\n"
                                "- Design primary data collection instruments: observation checklists, structured interview schedules, and soil sampling guides\n"
                                "- Implement fieldwork safety, logistics, and research ethics protocols"
                            )
                        }
                    },
                    {
                        "block_type": "concept_explanation",
                        "component_type": "concept_explanation",
                        "title": "Prerequisite Spark: Geography Beyond the Classroom",
                        "content": {
                            "text": (
                                "Rather than solely reading about farming in textbooks, imagine visiting an active smallholder farm in your locality. "
                                "You walk the furrows, inspect drip emitters, test soil pH, and interview the farmer about pest pressures and market margins. "
                                "This is geographical fieldwork—scientific inquiry in action!"
                            )
                        }
                    }
                ]
            },
            {
                "page_number": 2,
                "page_title": "Definitions & Fieldwork Methodology",
                "blocks": [
                    {
                        "block_type": "definition_card",
                        "component_type": "definition_card",
                        "title": "Field Inquiry Terminology",
                        "content": {
                            "definitions": [
                                {
                                    "term": "Geographical Fieldwork",
                                    "definition": "A structured experiential research investigation wherein students collect original primary spatial and empirical data directly from the real-world environment.",
                                    "simple": "Leaving the classroom to collect real data and observations in the field."
                                },
                                {
                                    "term": "Observation Checklist",
                                    "definition": "A systematic data collection rubric used to record the presence, frequency, physical condition, and spatial arrangement of observed agricultural features.",
                                    "simple": "A prepared list to tick off what crops, tools, and erosion signs are seen on the farm."
                                },
                                {
                                    "term": "Primary Data",
                                    "definition": "Original, first-hand qualitative and quantitative data gathered directly by the researcher at the study site.",
                                    "simple": "Brand-new data collected by you directly during the field study."
                                }
                            ]
                        }
                    },
                    {
                        "block_type": "concept_explanation",
                        "component_type": "concept_explanation",
                        "title": "The Four-Stage Fieldwork Lifecycle",
                        "content": {
                            "text": (
                                "A rigorous agricultural field inquiry executes four sequential phases:\n\n"
                                "1. **Pre-Field Preparation:** Formulate specific research objectives (e.g., 'To evaluate soil conservation methods on Kamau's farm'), obtain administrative clearance, and design question schedules.\n"
                                "2. **Field Execution:** Conduct transect walks, administer farmer questionnaires, record GPS coordinates, and complete observation matrices.\n"
                                "3. **Post-Field Analysis:** Transcribe interview notes, calculate crop yield statistics, and draw farm layout sketches.\n"
                                "4. **Synthesis & Reporting:** Compile an evidence-based report linking field observations to geographic principles."
                            )
                        }
                    }
                ]
            },
            {
                "page_number": 3,
                "page_title": "Data Collection Instruments & Workflow",
                "blocks": [
                    {
                        "block_type": "diagram",
                        "component_type": "diagram",
                        "title": "Fieldwork Agricultural Data Collection Flow",
                        "content": {
                            "caption": "Step-by-step scientific fieldwork protocol: Pre-visit planning, on-site transect walks, data synthesis, and report compilation."
                        }
                    },
                    {
                        "block_type": "concept_explanation",
                        "component_type": "concept_explanation",
                        "title": "Safety Protocols and Research Ethics",
                        "content": {
                            "text": (
                                "Rigorous fieldwork demands strict ethical and safety standards:\n\n"
                                "- **Safety First:** Wear sturdy closed-toe boots, sunscreen, and sunhats; bring safe drinking water; avoid handling agrochemicals or unauthorized farm machinery.\n"
                                "- **Ethical Compliance:** Always secure informed consent before entering private fields or taking photographs; treat farmers with dignity; respect indigenous knowledge."
                            )
                        }
                    }
                ]
            },
            {
                "page_number": 4,
                "page_title": "Field Observation Guides & Transect Mapping",
                "blocks": [
                    {
                        "block_type": "case_study",
                        "component_type": "case_study",
                        "title": "Designing a Farm Transect Walk",
                        "content": {
                            "text": (
                                "A transect walk involves walking a straight line across a farm from the highest elevation to the lowest valley bottom. "
                                "Students map how land use transitions from agroforestry trees on upper ridges, to terraced maize on mid-slopes, "
                                "down to irrigated vegetable beds and fish ponds in the fertile valley depression."
                            )
                        }
                    },
                    {
                        "block_type": "misconception_alert",
                        "component_type": "misconception_alert",
                        "title": "Fieldwork Is Not Manual Farm Labor",
                        "content": {
                            "misconception": "During an agricultural field trip, students should spend their time weeding or harvesting crops for the host farmer.",
                            "correction": "While respectful assistance is valued, fieldwork is an academic scientific research activity centered on data collection, interviews, spatial mapping, and analytical reporting."
                        }
                    }
                ]
            },
            {
                "page_number": 5,
                "page_title": "Formative Assessment: Agricultural Fieldwork",
                "blocks": [
                    {
                        "block_type": "multiple_choice_question",
                        "component_type": "multiple_choice_question",
                        "title": "Question 1: Formulating Research Objectives",
                        "content": {
                            "question": "You are organizing a geographical field inquiry on a local smallholder farm. Which of the following represents a scientifically sound *research objective*?",
                            "options": [
                                "To plow the farmer's two-acre plot using a rented tractor",
                                "To identify and evaluate the soil-water conservation strategies utilized by the farmer",
                                "To purchase fresh vegetables to cook dinner at school",
                                "To write a creative poem about the beauty of green countryside landscapes"
                            ],
                            "correct_answer": "To identify and evaluate the soil-water conservation strategies utilized by the farmer",
                            "explanation": "A scientific research objective must be clear, measurable, and focused on discovering specific geographical knowledge."
                        }
                    },
                    {
                        "block_type": "multiple_choice_question",
                        "component_type": "multiple_choice_question",
                        "title": "Question 2: Field Research Ethics",
                        "content": {
                            "question": "Why must geography students always obtain explicit permission from landowners before entering private farm plots and photographing crops during fieldwork?",
                            "options": [
                                "It is a legal requirement to pay cash entrance fees for all open fields",
                                "It protects students from wild carnivores in tea bushes",
                                "It upholds research ethics, respecting property rights, privacy, and informed consent",
                                "It physically accelerates crop growth rates"
                            ],
                            "correct_answer": "It upholds research ethics, respecting property rights, privacy, and informed consent",
                            "explanation": "Ethical research requires informed consent, respecting the rights, property, and privacy of participating community members."
                        }
                    }
                ]
            }
        ]
    },

    # Lesson 14: Communicating Agricultural Strategies: Designing a Policy Brief
    {
        "unit_order": 14,
        "unit_name": "Communicating Agricultural Strategies: Designing a Policy Brief",
        "lesson_title": "Communicating Agricultural Strategies: Designing a Policy Brief",
        "pages": [
            {
                "page_number": 1,
                "page_title": "Introduction & Learning Objectives",
                "blocks": [
                    {
                        "block_type": "suggested_image",
                        "component_type": "suggested_image",
                        "title": "Agricultural Extension Officer Engaging Rural Farmers",
                        "content": {"text": "A photograph showing an agricultural extension officer presenting an infographic strategy poster to a rural farmer cooperative."}
                    },
                    {
                        "block_type": "learning_goal",
                        "component_type": "learning_goal",
                        "title": "Lesson Objectives: Policy Briefs & Extension Posters",
                        "content": {
                            "text": (
                                "By the end of this lesson, you will be able to:\n\n"
                                "- Explain the structure, purpose, and audience targeting of an agricultural policy brief\n"
                                "- Synthesize empirical field research data into concise, persuasive, evidence-based policy recommendations\n"
                                "- Design an accessible visual extension poster for rural farming communities"
                            )
                        }
                    },
                    {
                        "block_type": "concept_explanation",
                        "component_type": "concept_explanation",
                        "title": "Prerequisite Spark: Translating Science into Action",
                        "content": {
                            "text": (
                                "Suppose your field study discovers a revolutionary low-cost solar cooling method that eliminates potato rot. "
                                "If you write a 100-page academic thesis filled with technical jargon, busy county agricultural ministers and farmers will never read it. "
                                "But if you condense your findings into a 2-page visual policy brief with clear action points, you can transform agricultural policy across the county!"
                            )
                        }
                    }
                ]
            },
            {
                "page_number": 2,
                "page_title": "Definitions & Policy Brief Architecture",
                "blocks": [
                    {
                        "block_type": "definition_card",
                        "component_type": "definition_card",
                        "title": "Strategic Communication Terminology",
                        "content": {
                            "definitions": [
                                {
                                    "term": "Policy Brief",
                                    "definition": "A concise, targeted document that synthesizes complex research evidence into practical, actionable recommendations for non-specialist decision-makers and government officials.",
                                    "simple": "A short, easy-to-read report that explains a problem and tells leaders how to fix it."
                                },
                                {
                                    "term": "Target Audience",
                                    "definition": "The specific group of stakeholders, policymakers, or community leaders whom a communication product is deliberately crafted to inform and influence.",
                                    "simple": "The exact people you are trying to convince or inform."
                                },
                                {
                                    "term": "Evidence-Based Recommendation",
                                    "definition": "A policy or agronomic proposal derived directly from empirical data, rigorous field observation, and proven scientific outcomes.",
                                    "simple": "A recommendation backed up by real facts, data, and field findings."
                                }
                            ]
                        }
                    },
                    {
                        "block_type": "concept_explanation",
                        "component_type": "concept_explanation",
                        "title": "The Five Essential Sections of a Policy Brief",
                        "content": {
                            "text": (
                                "An effective agricultural policy brief contains five clear components:\n\n"
                                "1. **Compelling Title:** Focused and urgent (e.g., 'Beating Drought: Scaling Up Solar Drip Irrigation in Machakos County').\n"
                                "2. **Executive Summary:** A concise 3-sentence summary of the crisis, key findings, and recommended action.\n"
                                "3. **Problem Statement:** Defining the agricultural challenge backed by verifiable statistics.\n"
                                "4. **Evidence & Field Findings:** Data visualizations, infographics, and empirical proof showing why current practices fail.\n"
                                "5. **Actionable Recommendations:** A numbered, prioritized checklist of concrete steps for policymakers."
                            )
                        }
                    }
                ]
            },
            {
                "page_number": 3,
                "page_title": "Policy Brief Layout & Infographics",
                "blocks": [
                    {
                        "block_type": "diagram",
                        "component_type": "diagram",
                        "title": "Policy Brief Infographic Layout",
                        "content": {
                            "caption": "Professional layout architecture for an agricultural policy brief: Header, problem matrix, visual data evidence, and policy recommendations."
                        }
                    },
                    {
                        "block_type": "concept_explanation",
                        "component_type": "concept_explanation",
                        "title": "Designing Farmer Extension Posters",
                        "content": {
                            "text": (
                                "When communicating directly with grassroots farming communities:\n\n"
                                "- **Visual Dominance:** Use step-by-step illustrations (e.g., 'Before' vs 'After' terracing).\n"
                                "- **Language Accessibility:** Utilize clear national languages (Swahili or local languages) and avoid dense statistical equations.\n"
                                "- **Clear Call to Action:** Provide simple, numbered instructions (e.g., 'Step 1: Dig trench along contour. Step 2: Plant Napier grass on ridge')."
                            )
                        }
                    }
                ]
            },
            {
                "page_number": 4,
                "page_title": "Case Study: Scaling Solar Cold Rooms",
                "blocks": [
                    {
                        "block_type": "case_study",
                        "component_type": "case_study",
                        "title": "Policy Brief in Action: Dairy Cooling in Nyandarua",
                        "content": {
                            "text": (
                                "In Nyandarua, a student policy brief titled 'Halting Milk Spoilage: Subsidizing Solar Chillers for Smallholder Cooperatives' "
                                "demonstrated that 35% of morning milk spoiled before reaching collection hubs. The county government adopted the recommendations, "
                                "allocating matching funds to install solar-powered milk cooling stations across 5 sub-counties."
                            )
                        }
                    },
                    {
                        "block_type": "misconception_alert",
                        "component_type": "misconception_alert",
                        "title": "Complexity Does Not Equal Credibility",
                        "content": {
                            "misconception": "A policy brief must be filled with complicated scientific jargon and dense mathematical proofs to look professional.",
                            "correction": "Decision-makers value clarity, speed, and actionable brevity. The greatest policy skill is translating complex geographical science into clear, persuasive, plain-language action points."
                        }
                    }
                ]
            },
            {
                "page_number": 5,
                "page_title": "Formative Assessment: Designing a Policy Brief",
                "blocks": [
                    {
                        "block_type": "multiple_choice_question",
                        "component_type": "multiple_choice_question",
                        "title": "Question 1: Purpose of an Agricultural Policy Brief",
                        "content": {
                            "question": "What is the primary function and purpose of writing an agricultural policy brief?",
                            "options": [
                                "To write a lengthy fictional novel about life on an estate",
                                "To synthesize research findings into a clear, concise document providing evidence-based recommendations for decision-makers",
                                "To calculate the exact quantum atomic mass of nitrogen atoms in fertilizer",
                                "To sell combine harvesters directly to foreign buyers"
                            ],
                            "correct_answer": "To synthesize research findings into a clear, concise document providing evidence-based recommendations for decision-makers",
                            "explanation": "A policy brief translates scientific data into an accessible, high-impact summary that guides busy leaders and community officers to make informed decisions."
                        }
                    },
                    {
                        "block_type": "multiple_choice_question",
                        "component_type": "multiple_choice_question",
                        "title": "Question 2: Crafting Evidence-Based Recommendations",
                        "content": {
                            "question": "Which of the following statements represents a concrete, *evidence-based policy recommendation*?",
                            "options": [
                                "Farming is a very nice and pleasant way of spending time in the countryside",
                                "The county should allocate 15% of its budget to fund three solar milk cooling hubs, which our data shows will reduce post-harvest losses by 80%",
                                "All farmers should immediately stop keeping cows and only plant wheat",
                                "The national government should distribute free video games to rural youth"
                            ],
                            "correct_answer": "The county should allocate 15% of its budget to fund three solar milk cooling hubs, which our data shows will reduce post-harvest losses by 80%",
                            "explanation": "This recommendation is specific, actionable, budgeted, and backed by measurable empirical evidence ('reduce post-harvest losses by 80%')."
                        }
                    }
                ]
            }
        ]
    },

    # Lesson 15: Topic Review, Synthesis, and Unit Assessment
    {
        "unit_order": 15,
        "unit_name": "Topic Review, Synthesis, and Unit Assessment",
        "lesson_title": "Topic Review, Synthesis, and Unit Assessment",
        "pages": [
            {
                "page_number": 1,
                "page_title": "Introduction & Learning Objectives",
                "blocks": [
                    {
                        "block_type": "suggested_image",
                        "component_type": "suggested_image",
                        "title": "Agricultural Landscape of Central Highlands Kenya",
                        "content": {"text": "A panoramic photograph showing the agricultural mosaic of the Central Highlands of Kenya with tea, maize, agroforestry, and terracing."}
                    },
                    {
                        "block_type": "learning_goal",
                        "component_type": "learning_goal",
                        "title": "Lesson Objectives: Topic Synthesis & Final Assessment",
                        "content": {
                            "text": (
                                "By the end of this lesson, you will be able to:\n\n"
                                "- Synthesize the complete topic: agricultural classification, physical/human drivers, open system cycles, value chains, and trends\n"
                                "- Evaluate Kenya's climatic, biological, and socio-economic hurdles alongside Climate-Smart Agriculture solutions\n"
                                "- Complete the comprehensive summative unit checkpoint demonstrating mastery of Grade 10 Geography Topic 10"
                            )
                        }
                    },
                    {
                        "block_type": "concept_explanation",
                        "component_type": "concept_explanation",
                        "title": "Prerequisite Spark: Unifying the Agricultural Landscape",
                        "content": {
                            "text": (
                                "Over 14 lessons, we have traversed the entire agricultural landscape: from smallholder subsistence plots in arid savannahs "
                                "to automated rose greenhouses in Naivasha. We analyzed farming as an open thermodynamic system, traced value chains from farm to fork, "
                                "investigated climate hazards, and designed climate-smart terracing and policy briefs. Let's unite all these concepts into a master synthesis!"
                            )
                        }
                    }
                ]
            },
            {
                "page_number": 2,
                "page_title": "The Master Agricultural Systems Matrix",
                "blocks": [
                    {
                        "block_type": "concept_explanation",
                        "component_type": "concept_explanation",
                        "title": "The Unified Agricultural Systems Equation",
                        "content": {
                            "text": (
                                "The entire subject of agricultural geography can be summarized by a unifying systems model:\n\n"
                                "$$\\text{Physical Constraints (Climate, Soil, Slope)} + \\text{Human Inputs (Capital, Labor, Tech)} \\rightarrow \\text{Farm Processes} \\rightarrow \\text{Outputs \\& Value Chains} \\rightarrow \\text{Food Security \\& GDP Growth}$$\n\n"
                                "- **Environmental Boundaries:** Climate, relief, and soil determine the biological feasibility of crops.\n"
                                "- **Human Systems:** Capital, labor, technology, and transport dictate whether farming reaches commercial scale.\n"
                                "- **Sustainable CSA:** Terracing, agroforestry, and mobile technology overcome climatic and soil degradation barriers."
                            )
                        }
                    },
                    {
                        "block_type": "definition_card",
                        "component_type": "definition_card",
                        "title": "Master Synthesis Glossary",
                        "content": {
                            "definitions": [
                                {
                                    "term": "Agricultural System",
                                    "definition": "An integrated, open biophysical and economic cycle transforming natural resources and human inputs into food, fiber, and raw materials.",
                                    "simple": "The complete interconnected system of farming inputs, tasks, and outputs."
                                },
                                {
                                    "term": "Climate-Smart Resilience",
                                    "definition": "The capacity of an agrarian system to absorb climatic shocks (droughts, floods) and sustain productivity through conservation practices.",
                                    "simple": "The ability of a farm to survive droughts and floods without losing its crops."
                                }
                            ]
                        }
                    }
                ]
            },
            {
                "page_number": 3,
                "page_title": "Master Synthesis Infographic",
                "blocks": [
                    {
                        "block_type": "diagram",
                        "component_type": "diagram",
                        "title": "Master Agriculture Synthesis & Decision Tree",
                        "content": {
                            "caption": "Comprehensive synthesis mind map linking agricultural challenges, climate-smart interventions, value chains, and national food security outcomes."
                        }
                    },
                    {
                        "block_type": "concept_explanation",
                        "component_type": "concept_explanation",
                        "title": "Comprehensive Topic Review Checklist",
                        "content": {
                            "text": (
                                "Before attempting the final checkpoint, ensure you can:\n\n"
                                "1. Differentiate subsistence from commercial, and intensive from extensive agriculture.\n"
                                "2. Identify physical constraints (rainfall, temperature, slope, soil) and human variables (capital, transport, policy).\n"
                                "3. Trace the open cycle of inputs, processes, and outputs including feedback loops (manure, stubble).\n"
                                "4. Map the five nodes of agricultural value chains and calculate value addition benefits.\n"
                                "5. Explain the Four Pillars of Food Security (Availability, Access, Utilization, Stability).\n"
                                "6. Detail Climate-Smart Agriculture techniques (Fanya Juu terraces, mulching, agroforestry, solar drip kits)."
                            )
                        }
                    }
                ]
            },
            {
                "page_number": 4,
                "page_title": "Unit Review Checkpoint & Key Insights",
                "blocks": [
                    {
                        "block_type": "case_study",
                        "component_type": "case_study",
                        "title": "Transforming Kenya's Agricultural Horizon",
                        "content": {
                            "text": (
                                "Kenya's vision for agricultural transformation balances high-tech agribusiness innovation (digital apps, solar cold chains, floriculture) "
                                "with grassroots climate-smart conservation (terracing, agroforestry, rainwater harvesting). "
                                "Securing the future of agriculture guarantees national prosperity, food sovereignty, and ecological resilience for generations to come."
                            )
                        }
                    }
                ]
            },
            {
                "page_number": 5,
                "page_title": "Summative Unit Assessment",
                "blocks": [
                    {
                        "block_type": "multiple_choice_question",
                        "component_type": "multiple_choice_question",
                        "title": "Question 1: Mixed Farm Feedback Loop",
                        "content": {
                            "question": "On a sustainable mixed farm, which of the following operations represents a *closed feedback loop* where an output is recycled back as an internal input?",
                            "options": [
                                "Exporting raw tea leaves in bulk to foreign auction markets",
                                "Collecting cattle manure and applying it as organic compost on vegetable garden plots",
                                "Purchasing imported chemical fertilizer from a commercial dealer",
                                "Transporting maize to an urban commercial grain miller"
                            ],
                            "correct_answer": "Collecting cattle manure and applying it as organic compost on vegetable garden plots",
                            "explanation": "A feedback loop recycles a system output (cattle manure) directly back into the farm as an input (organic fertilizer), reducing costs and enhancing sustainability."
                        }
                    },
                    {
                        "block_type": "multiple_choice_question",
                        "component_type": "multiple_choice_question",
                        "title": "Question 2: Climate-Smart Hillside Soil Conservation",
                        "content": {
                            "question": "Which climate-smart agronomic strategy is most effective for preventing steep hillside erosion, conserving soil moisture, and restoring nitrogen nutrients?",
                            "options": [
                                "Continuous monoculture maize farming with complete residue removal",
                                "Overgrazing a dense herd of goats on the bare slope",
                                "Practicing agroforestry by planting nitrogen-fixing trees on terraced contour food crops",
                                "Applying heavy doses of chemical weedkillers across the hill"
                            ],
                            "correct_answer": "Practicing agroforestry by planting nitrogen-fixing trees on terraced contour food crops",
                            "explanation": "Agroforestry on terraces combines deep root soil stabilization, leaf litter mulching for moisture retention, and biological nitrogen fixation."
                        }
                    },
                    {
                        "block_type": "multiple_choice_question",
                        "component_type": "multiple_choice_question",
                        "title": "Question 3: Defining Food Utilization",
                        "content": {
                            "question": "Which statement accurately defines *food utilization*, one of the four essential pillars of food security?",
                            "options": [
                                "The physical presence of cereal grain stocks in national warehouses",
                                "A household's financial earnings and purchasing power in local retail shops",
                                "The physiological absorption and nutritional use of food, supported by balanced diets, safe water, and hygienic preparation",
                                "The transport of agricultural harvests along paved highways"
                            ],
                            "correct_answer": "The physiological absorption and nutritional use of food, supported by balanced diets, safe water, and hygienic preparation",
                            "explanation": "Food utilization relates to the biological assimilation of nutrients, requiring clean drinking water, sanitation, proper food hygiene, and balanced dietary diversity."
                        }
                    }
                ]
            }
        ]
    }
]

def run_ingestion():
    print("=" * 80)
    print("Starting Ingestion: CBC Grade 10 Geography — Topic 10: Agriculture")
    print("=" * 80)

    with transaction.atomic():
        # 1. Target Curriculum
        curriculum = Curriculum.objects.filter(name__iexact="CBC").first()
        if not curriculum:
            raise ValueError("Curriculum 'CBC' not found in database!")

        # 2. Target Grade 10
        grade = Grade.objects.filter(curriculum=curriculum, name__icontains="10").first()
        if not grade:
            raise ValueError("Grade 10 not found under CBC curriculum!")

        # 3. Target Subject: Geography (Subject ID: 37)
        subject = Subject.objects.filter(id=37).first() or Subject.objects.filter(grade=grade, name="Geography").first()
        if not subject:
            raise ValueError("Subject 'Geography' (ID: 37) not found under Grade 10 CBC!")

        # 4. Target Topic: Topic 10 Agriculture
        topic, created = Topic.objects.get_or_create(
            subject=subject,
            order=10,
            defaults={
                "name": "Agriculture",
                "description": "Strand 3.0: Human and Economic Activities - Topic 10: Agriculture (15 Lessons)"
            }
        )
        topic.name = "Agriculture"
        topic.description = "Strand 3.0: Human and Economic Activities - Topic 10: Agriculture (15 Lessons)"
        topic.save()

        print(f"Target Topic: [{topic.id}] Order {topic.order}: {topic.name} under Subject: {subject.name} (Grade 10 CBC)")

        total_blocks_created = 0

        for les_data in LESSONS_DATA:
            u_order = les_data["unit_order"]
            u_name = clean_text(les_data["unit_name"])
            les_title = clean_text(les_data["lesson_title"])

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

            # Clear existing blocks for idempotency
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
    print(f"Ingestion completed successfully for Grade 10 Geography Topic 10! (Total Blocks: {total_blocks_created})")
    print("=" * 80)

if __name__ == "__main__":
    run_ingestion()
