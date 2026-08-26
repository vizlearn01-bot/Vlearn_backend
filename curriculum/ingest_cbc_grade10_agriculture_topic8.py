"""
VLearn CBC Grade 10 Agriculture — Topic 8: Breeds of Livestock
Production Ingestion Engine (Deep Senior Secondary Pedagogical Edition)

Curriculum: CBC (ID: 5)
Grade: Grade 10 (ID: 5, Level: 10)
Subject: Agriculture
Topic: Breeds of Livestock (Topic Order: 8)

Decomposed into 10 Learning Units & 10 Published Lessons:
  1. Introduction to Livestock Breeds (5 Pages, 11 Blocks)
  2. Cattle Breeds I - Dairy Breeds (5 Pages, 11 Blocks)
  3. Cattle Breeds II - Beef and Dual-Purpose Breeds (5 Pages, 11 Blocks)
  4. Pig Breeds (5 Pages, 11 Blocks)
  5. Rabbit Breeds (5 Pages, 11 Blocks)
  6. Sheep Breeds (5 Pages, 11 Blocks)
  7. Goat Breeds (5 Pages, 11 Blocks)
  8. Comparing Breed Characteristics (5 Pages, 11 Blocks)
  9. Comparative Productivity (5 Pages, 11 Blocks)
  10. Sub-strand Review and Assessment (8 Pages, 17 Blocks)
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

def build_topic8_curriculum():
    """Returns the comprehensive pedagogical page and block structure for Grade 10 Topic 8: Breeds of Livestock."""
    return [
        # =====================================================================
        # LESSON 1: Introduction to Livestock Breeds
        # =====================================================================
        {
            "unit_order": 1,
            "unit_name": "Introduction to Livestock Breeds",
            "unit_description": "Definition of a breed; genetic foundation and selective breeding; classification by purpose (single, dual, multi-purpose); environmental adaptation (exotic high-input vs indigenous climate-adapted).",
            "lesson_title": "Principles of Livestock Breeds, Genetics, and Environmental Adaptation",
            "pages": [
                [
                    {
                        "type": "suggested_image",
                        "title": "Diverse Livestock Grazing on Open Tropical Savanna Pasture",
                        "content": {
                            "title": "Diverse Livestock Grazing on Open Tropical Savanna Pasture",
                            "caption": "A vibrant mix of cattle, sheep, and goats grazing together, demonstrating the phenotypic diversity and genetic adaptation of domestic farm animals."
                        }
                    },
                    {
                        "type": "learning_goal",
                        "title": "Lesson Objectives: Introduction to Breeds",
                        "content": {
                            "title": "What We Will Master Today",
                            "goals": [
                                "Define the scientific term **livestock breed** and explain its genetic inheritance.",
                                "Classify farm animals by economic utility: **Single-Purpose, Dual-Purpose, and Multi-Purpose**.",
                                "Analyze the ecological trade-offs between **Exotic High-Yielding Breeds** and **Indigenous Climate-Hardy Breeds**.",
                                "Conduct a community livestock inventory audit."
                            ]
                        }
                    },
                    {
                        "type": "concept_explanation",
                        "title": "What is a Livestock Breed?",
                        "content": {
                            "title": "The Genetic Foundation of Animal Husbandry",
                            "text": "A **livestock breed** is a specific group of domestic animals within a species that shares a homogeneous physical appearance (phenotype), uniform behavior, and distinct physiological traits that distinguish it from other groups of the same species.\n\n- **Selective Breeding**: Breeds do not occur by accident. They are developed over generations of human selection, choosing parents with desirable traits (e.g. high milk yield, rapid muscle deposition, fine fleece, or tick resistance) and mating them systematically.\n- **Heritability**: These distinctive physical and production characteristics are genetically fixed and reliably passed from parents to offspring."
                        }
                    }
                ],
                [
                    {
                        "type": "concept_explanation",
                        "title": "Classification by Production Purpose and Ecology",
                        "content": {
                            "title": "Utility and Agro-Ecological Categories",
                            "text": "1. **Single-Purpose Breeds**: Genetically specialized for one output. *Examples: Holstein Friesian (Liquid Milk), Aberdeen Angus (Beef), Merino (Fine Wool)*.\n2. **Dual-Purpose Breeds**: Selected to produce two valuable outputs efficiently. *Examples: Sahiwal (Milk + Meat), Simmental (Milk + Beef), Corriedale sheep (Mutton + Wool)*.\n3. **Multi-Purpose Breeds**: Typical of indigenous livestock, providing milk, meat, hides, and draft power.\n\n### The Agro-Ecological Reality\n- **Exotic Breeds (Temperate Origin)**: High genetic potential for yield, but highly vulnerable to heat stress, low-quality tropical pasture, and tick-borne diseases (East Coast Fever).\n- **Indigenous Breeds (Tropical Origin)**: Evolved over millennia; possess natural heat tolerance, tick/fly resistance, and the ability to thrive on fibrous, low-protein native grasses."
                        }
                    },
                    {
                        "type": "suggested_diagram",
                        "title": "Livestock Classification: Purpose & Environmental Adaptation Matrix",
                        "content": {
                            "title": "Livestock Classification: Purpose & Environmental Adaptation Matrix",
                            "caption": "Conceptual matrix showing: 1 Purpose Pillars (Single vs Dual vs Multi-Purpose), and 2 Environmental Axes (Exotic High-Input vs Indigenous High-Resilience)."
                        }
                    }
                ],
                [
                    {
                        "type": "comparison_table",
                        "title": "Exotic Breeds vs Indigenous Breeds: The Management Trade-Off",
                        "content": {
                            "title": "Exotic vs Indigenous Livestock Evaluation Matrix",
                            "headers": ["Evaluation Metric", "Exotic Temperate Breeds (e.g. Friesian, Landrace)", "Indigenous Tropical Breeds (e.g. Boran, Red Masai)"],
                            "rows": [
                                ["Genetic Yield Potential", "Very High (20–40 L milk/day; rapid growth)", "Modest to Low (2–6 L milk/day; slower growth)"],
                                ["Heat & Solar Tolerance", "Poor (Suffer severe heat stress above 25°C)", "Excellent (Humps, loose skin, efficient sweating)"],
                                ["Disease & Parasite Resistance", "Low (Require strict chemical dipping and vaccines)", "High natural genetic resistance to ticks and worms"],
                                ["Pasture & Water Requirement", "Require high-protein silage, concentrates, clean water", "Thrive on poor rangeland forage; drought-hardy"],
                                ["Target Agribusiness System", "High-input commercial zero-grazing / feedlots", "Extensive pastoral rangelands and semi-arid ranches"]
                            ]
                        }
                    },
                    {
                        "type": "mini_activity",
                        "title": "Classroom Practical: Community Livestock Breed Audit",
                        "content": {
                            "title": "Local Livestock Breed Survey",
                            "task": "1. Survey your local community or school farm.\n2. List 5 livestock species kept (Cattle, Goats, Sheep, Pigs, Rabbits).\n3. For each, identify whether the predominant breeds are Indigenous or Exotic.\n4. Interview a farmer to discover why they chose that specific breed over others.",
                            "materials": ["Survey Notebook", "Interview Questionnaire", "Pen"],
                            "safety": "Maintain safe distance from large breeding bulls and protective sows."
                        }
                    }
                ],
                [
                    {
                        "type": "key_takeaway",
                        "title": "Core Summary: Livestock Breeds",
                        "content": {
                            "title": "Key Takeaways",
                            "text": "- **A breed is a genetically uniform group** within a species sharing distinct traits.\n- **Classified by purpose**: Single-purpose, dual-purpose, and multi-purpose.\n- **Exotics offer high yield** but require intensive feed and veterinary care.\n- **Indigenous breeds offer unmatched survival** in tropical heat and disease zones."
                        }
                    },
                    {
                        "type": "knowledge_check",
                        "title": "Check Your Understanding: Rationale for Indigenous Breeds in Arid Zones",
                        "content": {
                            "question": "Why is it economically and biologically reckless for a smallholder farmer in an arid, semi-desert region of Kenya to stock purebred exotic Holstein Friesian dairy cattle without intensive cooling and feed resources?",
                            "options": [
                                "Friesian cattle produce milk that is illegal to sell in Kenya",
                                "Exotic Friesians are bred for cool temperate climates; in hot arid zones they suffer extreme heat stress, have zero resistance to endemic tick-borne diseases (like East Coast Fever), and perish on poor-quality dry forage",
                                "Friesian cattle are physically too small to walk on sand",
                                "Friesians stop drinking water when temperatures rise above 20°C"
                            ],
                            "answer": "B",
                            "explanation": "Exotic temperate dairy breeds like the Holstein Friesian require cool temperatures, high-protein rations, and strict tick control. In arid tropical environments, high ambient heat, low-quality pasture, and tick-borne pathogens cause severe health breakdown and high mortality unless expensive intensive housing and feeding are provided."
                        }
                    }
                ]
            ]
        },

        # =====================================================================
        # LESSON 2: Cattle Breeds I - Dairy Breeds
        # =====================================================================
        {
            "unit_order": 2,
            "unit_name": "Cattle Breeds I - Dairy Breeds",
            "unit_description": "Holstein Friesian (highest volume, 3.0–3.5% butterfat); Jersey (highest butterfat 5.0–5.5%, heat-tolerant); Ayrshire (Scotland, cherry-red/white, hardy forager, 4.0% butterfat); Guernsey (golden beta-carotene milk, 4.5–5.0% butterfat).",
            "lesson_title": "Dairy Cattle Breeds: Friesian, Jersey, Ayrshire, and Guernsey",
            "pages": [
                [
                    {
                        "type": "suggested_image",
                        "title": "Holstein Friesian Dairy Herd Grazing in Lush Highland Pasture",
                        "content": {
                            "title": "Holstein Friesian Dairy Herd Grazing in Lush Highland Pasture",
                            "caption": "A herd of purebred Holstein Friesian cows displaying the classic black-and-white piebald coat pattern and prominent dairy conformation."
                        }
                    },
                    {
                        "type": "learning_goal",
                        "title": "Lesson Objectives: Dairy Cattle Breeds",
                        "content": {
                            "title": "What We Will Master Today",
                            "goals": [
                                "Identify the 4 premier exotic dairy cattle breeds kept in Kenya (**Friesian, Jersey, Ayrshire, Guernsey**).",
                                "Describe the distinctive **physical markings and origins** of each breed.",
                                "Analyze the **Milk Volume vs Butterfat Percentage trade-off**.",
                                "Explain the biological origin of **Guernsey golden milk** (beta-carotene)."
                            ]
                        }
                    },
                    {
                        "type": "concept_explanation",
                        "title": "Holstein Friesian and Jersey: The Two Extremes",
                        "content": {
                            "title": "Volume Champion vs Butterfat Specialist",
                            "text": "1. **Holstein Friesian (Origin: Netherlands / Germany)**:\n- **Conformation**: Massive body frame ($600\\text{--}750\\text{ kg}$), distinct **black-and-white piebald coat**, large wedge-shaped dairy conformation.\n- **Production**: The **absolute highest milk volume** of any dairy breed ($25\\text{--}40\\text{ L/day}$).\n- **Butterfat**: Lowest butterfat content ($3.0\\%\\text{ to }3.5\\%$). Highly susceptible to heat stress and requires massive volumes of quality feed.\n\n2. **Jersey (Origin: Jersey Island, UK)**:\n- **Conformation**: Smallest dairy breed ($350\\text{--}450\\text{ kg}$), fawn/light-brown coat, dish face with large eyes and a dark muzzle.\n- **Production**: Moderate milk volume ($12\\text{--}18\\text{ L/day}$), but the **absolute highest butterfat content ($5.0\\%\\text{ to }5.5\\%$)**.\n- **Adaptability**: Lower maintenance feed requirement and superior heat tolerance among exotic dairy cows."
                        }
                    }
                ],
                [
                    {
                        "type": "concept_explanation",
                        "title": "Ayrshire and Guernsey: The Versatile Mid-Range Producers",
                        "content": {
                            "title": "The Foraging Highlander and the Golden Milk Producer",
                            "text": "3. **Ayrshire (Origin: Scotland)**:\n- **Conformation**: Medium-to-large frame ($500\\text{--}600\\text{ kg}$), distinct **cherry-red/brown and white patches**, lyre-shaped horns or polled.\n- **Production**: High, consistent milk volume ($18\\text{--}25\\text{ L/day}$) with **4.0% butterfat**.\n- **Hardiness**: Outstanding active foragers; thrive on rugged, hilly terrain where Friesians lose condition.\n\n4. **Guernsey (Origin: Guernsey Island, UK)**:\n- **Conformation**: Medium frame ($450\\text{--}500\\text{ kg}$), yellowish-brown to golden-fawn coat with white patches on belly and legs.\n- **Production**: Moderate-to-high milk yield ($15\\text{--}20\\text{ L/day}$) with **4.5% to 5.0% butterfat**.\n- **Golden Milk**: Renowned for producing distinct **golden-yellow milk** due to its inability to break down ingested **beta-carotene** (Pro-Vitamin A), passing it directly into the milk fat."
                        }
                    },
                    {
                        "type": "suggested_diagram",
                        "title": "Major Dairy Cattle Breeds: Milk Volume vs Butterfat Trade-Off",
                        "content": {
                            "title": "Major Dairy Cattle Breeds: Milk Volume vs Butterfat Trade-Off",
                            "caption": "Scatter graph plotting Milk Yield (Liters/Lactation) against Butterfat Percentage (%), illustrating: Friesian (Max Volume, Min Fat), Ayrshire (Balanced High Volume), Guernsey (High Fat Golden Milk), and Jersey (Max Butterfat, Min Body Size)."
                        }
                    }
                ],
                [
                    {
                        "type": "comparison_table",
                        "title": "The 4 Major Dairy Breeds Diagnostic Comparison",
                        "content": {
                            "title": "Dairy Cattle Production & Trait Matrix",
                            "headers": ["Dairy Breed", "Country of Origin", "Coat Color / Markings", "Daily Milk Volume", "Butterfat %", "Agribusiness Niche"],
                            "rows": [
                                ["Holstein Friesian", "Netherlands", "Black and White patches", "25 – 40 Liters", "3.0% – 3.5%", "Urban liquid milk markets (sold by volume)"],
                                ["Ayrshire", "Scotland", "Cherry-red / brown & white", "18 – 25 Liters", "4.0%", "Commercial farms on hilly / rough pastures"],
                                ["Guernsey", "Guernsey (UK)", "Golden-brown & white patches", "15 – 20 Liters", "4.5% – 5.0%", "Specialty golden milk / artisanal butter"],
                                ["Jersey", "Jersey (UK)", "Fawn to light brown, dark muzzle", "12 – 18 Liters", "5.0% – 5.5%", "Cheese, butter, ghee processing & hot climates"]
                            ]
                        }
                    },
                    {
                        "type": "mini_activity",
                        "title": "Agribusiness Practical: Choosing the Ideal Dairy Breed for 2 Farms",
                        "content": {
                            "title": "Dairy Breed Selection Challenge",
                            "task": "1. Farm Alpha is in Limuru (Cool highland, sells liquid milk to Nairobi by the liter).\n2. Farm Beta is in Machakos (Warm semi-arid, produces artisanal cheese and butter).\n3. Recommend the optimal breed for Farm Alpha and Farm Beta, justifying based on body size, feed needs, heat tolerance, and butterfat percentage.",
                            "materials": ["Case Handout", "Breed Matrix", "Calculator"],
                            "safety": "Ensure realistic feeding and environmental calculations."
                        }
                    }
                ],
                [
                    {
                        "type": "key_takeaway",
                        "title": "Core Summary: Dairy Cattle Breeds",
                        "content": {
                            "title": "Key Takeaways",
                            "text": "- **Holstein Friesian produces the highest milk volume** with the lowest butterfat (3.0–3.5%).\n- **Jersey produces the highest butterfat (5.0–5.5%)** and has superior heat tolerance.\n- **Ayrshire is the hardiest forager** on rough, hilly terrain (4.0% butterfat).\n- **Guernsey produces golden milk** rich in beta-carotene (4.5–5.0% butterfat)."
                        }
                    },
                    {
                        "type": "knowledge_check",
                        "title": "Check Your Understanding: Rationale for Jersey Milk in Butter Processing",
                        "content": {
                            "question": "Why do commercial dairy processors specializing in butter, cheese, and ghee prefer purchasing milk from Jersey cows over Holstein Friesian cows?",
                            "options": [
                                "Jersey milk contains natural sugar that eliminates the need for churning",
                                "Jersey milk contains the highest butterfat percentage (5.0% to 5.5%) and milk solids, yielding significantly more butter and cheese per liter of milk processed",
                                "Jersey milk stays fresh for 10 years without refrigeration",
                                "Jersey cows produce 100 liters of milk per day"
                            ],
                            "answer": "B",
                            "explanation": "Jersey milk is rich in butterfat (5.0%–5.5%) and milk solids (protein and casein). When manufacturing butter, cheese, or ghee, processors achieve much higher product recovery rates per liter compared to Holstein Friesian milk, which contains only 3.0%–3.5% butterfat."
                        }
                    }
                ]
            ]
        },

        # =====================================================================
        # LESSON 3: Cattle Breeds II - Beef and Dual-Purpose Breeds
        # =====================================================================
        {
            "unit_order": 3,
            "unit_name": "Cattle Breeds II - Beef and Dual-Purpose Breeds",
            "unit_description": "Tropical beef breeds: Boran (indigenous Zebu, tick/drought resistant), Brahman (USA/India, heat dissipation dewlap); Temperate beef: Aberdeen Angus (polled, marbling), Hereford (docile, white face); Dual-purpose: Sahiwal (Pakistan), Simmental (Switzerland).",
            "lesson_title": "Beef and Dual-Purpose Cattle: Boran, Brahman, Angus, Hereford, and Sahiwal",
            "pages": [
                [
                    {
                        "type": "suggested_image",
                        "title": "Purebred Boran Beef Bull in Kenyan Semi-Arid Rangeland",
                        "content": {
                            "title": "Purebred Boran Beef Bull in Kenyan Semi-Arid Rangeland",
                            "caption": "A magnificent Boran beef bull showing the prominent shoulder hump, loose dewlap, and white-grey coat adapted for rangeland beef production."
                        }
                    },
                    {
                        "type": "learning_goal",
                        "title": "Lesson Objectives: Beef and Dual-Purpose Cattle",
                        "content": {
                            "title": "What We Will Master Today",
                            "goals": [
                                "Distinguish between **Tropical Adapted Beef Breeds** and **Temperate Exotic Beef Breeds**.",
                                "Describe the morphological features and economic merits of **Boran, Brahman, Aberdeen Angus, and Hereford**.",
                                "Define **intramuscular marbling** and explain why Angus beef commands a market premium.",
                                "Analyze **Dual-Purpose Breeds (Sahiwal and Simmental)**."
                            ]
                        }
                    },
                    {
                        "type": "concept_explanation",
                        "title": "Tropical Beef Breeds: Boran and Brahman",
                        "content": {
                            "title": "Masters of the Tropical Rangelands",
                            "text": "1. **Boran (Origin: East Africa / Northern Kenya)**:\n- **Conformation**: Medium-sized, white to light grey coat (bulls have dark grey/black necks and shoulders), prominent thoracic hump, and loose dewlap.\n- **Superpowers**: World-renowned beef breed for semi-arid rangelands; high natural resistance to ticks and biting flies; exceptional mothering ability; walks long distances for water and converts poor dry brush into premium beef.\n\n2. **Brahman (Origin: USA from Indian *Bos indicus* stock)**:\n- **Conformation**: Steel-grey to red, massive thoracic hump, long pendulous drooping ears, and extensive loose skin folds (dewlap and sheath).\n- **Superpowers**: Unmatched heat dissipation due to high sweat gland density; immune to many tropical parasites; premier sire for crossbreeding to inject tropical resilience."
                        }
                    }
                ],
                [
                    {
                        "type": "concept_explanation",
                        "title": "Temperate Beef and Dual-Purpose Breeds",
                        "content": {
                            "title": "Feedlot Champions and Dual-Purpose Workhorses",
                            "text": "3. **Aberdeen Angus (Origin: Scotland)**:\n- **Conformation**: Solid black (or red), naturally **polled (hornless)**, blocky low-set beef cylinder.\n- **Premium Quality**: Produces world-famous **marbled beef** (fine veins of intramuscular fat within muscle fibers), creating unmatched tenderness and flavor.\n\n4. **Hereford (Origin: England)**:\n- **Conformation**: Deep red body with a **distinctive pure white face, white chest, white underline, and white tail switch**.\n- **Merits**: Extremely docile temperament, fast growth on managed pastures, early maturity.\n\n5. **Dual-Purpose Breeds**:\n- **Sahiwal (Origin: Pakistan)**: Humped, reddish-brown, loose skin; yields $8\\text{--}12\\text{ L/day}$ milk in hot semi-arid zones while maintaining heavy beef carcasses.\n- **Simmental (Origin: Switzerland)**: Large frame, red-and-white coat with white face; produces heavy milk volumes ($20\\text{ L/day}$) and fast-growing beef calves."
                        }
                    },
                    {
                        "type": "suggested_diagram",
                        "title": "Humped Bos indicus vs Humpless Bos taurus Morphological Anatomy",
                        "content": {
                            "title": "Humped Bos indicus vs Humpless Bos taurus Morphological Anatomy",
                            "caption": "Comparative anatomical diagram illustrating: Bos indicus (Thoracic Hump, Loose Extended Dewlap, Drooping Vascular Ears, Light Solar Reflective Coat) vs Bos taurus (No Hump, Tight Skin, Small Upright Ears, Blocky Muscular Frame)."
                        }
                    }
                ],
                [
                    {
                        "type": "comparison_table",
                        "title": "Beef and Dual-Purpose Cattle Breeds Matrix",
                        "content": {
                            "title": "Beef & Dual-Purpose Breeds Evaluation Matrix",
                            "headers": ["Cattle Breed", "Category", "Origin", "Distinctive Physical Markers", "Primary Commercial Strength"],
                            "rows": [
                                ["Boran", "Tropical Beef", "East Africa (Kenya)", "White/grey coat, prominent hump, loose dewlap", "Tick/drought resistance; rangeland grazing"],
                                ["Brahman", "Tropical Beef", "USA / India", "Massive hump, huge pendulous ears, loose sheath", "Extreme heat tolerance; crossbreeding sire"],
                                ["Aberdeen Angus", "Temperate Beef", "Scotland", "Solid black, naturally polled (hornless)", "Intramuscular marbling; premium steak meat"],
                                ["Hereford", "Temperate Beef", "England", "Red body with distinct pure white face", "Docility, fast fattening, feedlot efficiency"],
                                ["Sahiwal", "Dual-Purpose", "Pakistan", "Reddish-brown, humped, loose dewlap", "Milk ($8\\text{--}12\\text{ L}$) + Beef in semi-arid ranches"],
                                ["Simmental", "Dual-Purpose", "Switzerland", "Large red & white frame with white face", "Heavy milk yield + heavy beef carcass"]
                            ]
                        }
                    },
                    {
                        "type": "suggested_video",
                        "title": "Boran Beef Cattle Ranching in Kenyan Rangelands",
                        "content": {
                            "title": "Boran Beef Cattle Ranching in Kenyan Rangelands",
                            "description": "Agronomic documentary exploring purebred Boran cattle management in Laikipia ranches, demonstrating heat tolerance, tick resistance, and commercial beef finishing.",
                            "url": "https://www.youtube.com/watch?v=dQw4w9WgXcQ"
                        }
                    }
                ],
                [
                    {
                        "type": "mini_activity",
                        "title": "Field Practical: Livestock Conformation and Marbling Diagnostic",
                        "content": {
                            "title": "Beef vs Dairy Conformation Lab",
                            "task": "1. Compare anatomical photographs of a Dairy Cow (Wedge-shaped, prominent ribs, large udder) vs Beef Bull (Blocky rectangular brick, deep chest, heavy muscling).\n2. Sketch the blocky beef conformation of an Angus/Hereford.\n3. Explain the commercial value of intramuscular marbling vs subcutaneous backfat.",
                            "materials": ["Conformation Reference Cards", "Drawing Book", "Pencil"],
                            "safety": "Observe standard animal handling safety protocols."
                        }
                    },
                    {
                        "type": "key_takeaway",
                        "title": "Core Summary: Beef and Dual-Purpose Breeds",
                        "content": {
                            "title": "Key Takeaways",
                            "text": "- **Boran is the premier indigenous beef breed** in East African rangelands.\n- **Brahman possesses unmatched heat dissipation** with huge vascular ears and dewlap.\n- **Aberdeen Angus produces premium marbled beef** (naturally polled).\n- **Hereford is recognized by its white face** and docile feedlot performance.\n- **Sahiwal is the leading tropical dual-purpose breed** (milk + beef)."
                        }
                    }
                ],
                [
                    {
                        "type": "knowledge_check",
                        "title": "Check Your Understanding: Rationale for Aberdeen Angus Premium Price",
                        "content": {
                            "question": "What unique anatomical and meat-quality characteristic makes Aberdeen Angus beef command a premium price in high-end butcheries and international steak restaurants?",
                            "options": [
                                "The meat contains zero protein and high water",
                                "The breed deposits fine flecks of intramuscular fat evenly within the muscle fibers (marbling), creating superior tenderness, juiciness, and flavor upon cooking",
                                "Angus beef is naturally yellow in color",
                                "The meat has no muscle fibers"
                            ],
                            "answer": "B",
                            "explanation": "Aberdeen Angus is globally celebrated for 'marbling'—the genetic deposition of microscopic intramuscular fat flecks throughout the lean muscle tissue. During cooking, this fat melts internally, basting the beef from within to deliver exceptional tenderness, rich flavor, and juiciness."
                        }
                    }
                ]
            ]
        },

        # =====================================================================
        # LESSON 4: Pig Breeds
        # =====================================================================
        {
            "unit_order": 4,
            "unit_name": "Pig Breeds",
            "unit_description": "Commercial white breeds: Large White / Yorkshire (erect ears, prolificacy), Landrace (drooping ears, long body for bacon); Colored sire lines: Duroc (golden-red, growth vigor), Hampshire (black with white belt, lean carcass).",
            "lesson_title": "Commercial Pig Breeds: Large White, Landrace, Duroc, and Hampshire",
            "pages": [
                [
                    {
                        "type": "suggested_image",
                        "title": "Large White Commercial Sow with Healthy Piglet Litter in Pen",
                        "content": {
                            "title": "Large White Commercial Sow with Healthy Piglet Litter in Pen",
                            "caption": "A purebred Large White sow with erect ears nursing a large, uniform litter of piglets in a well-managed commercial piggery."
                        }
                    },
                    {
                        "type": "learning_goal",
                        "title": "Lesson Objectives: Commercial Pig Breeds",
                        "content": {
                            "title": "What We Will Master Today",
                            "goals": [
                                "Identify the 4 major commercial pig breeds kept in Kenya (**Large White, Landrace, Duroc, Hampshire**).",
                                "Distinguish **Pork-Type Breeds** from **Bacon-Type Breeds**.",
                                "Analyze key diagnostic physical features: **ear posture (erect vs drooping), body length, and coat color**.",
                                "Explain the role of **terminal sires (Duroc/Hampshire)** in commercial crossbreeding."
                            ]
                        }
                    },
                    {
                        "type": "concept_explanation",
                        "title": "The Commercial White Breeds: Large White and Landrace",
                        "content": {
                            "title": "The Maternal Foundations of Piggery Agribusiness",
                            "text": "1. **Large White / Yorkshire (Origin: UK)**:\n- **Conformation**: Pure white skin and hair, **erect (upright) ears**, dished face, long and deep body.\n- **Commercial Strengths**: World's leading commercial breed; outstanding prolificacy (10–14 piglets/litter); superb mothering and milk yield; fast growth and excellent dual pork-bacon carcass.\n\n2. **Landrace (Origin: Denmark)**:\n- **Conformation**: White skin, **exceptionally long cylindrical body**, and **large drooping ears that flap forward over the eyes**.\n- **Commercial Strengths**: The premier **bacon breed**; selected genetically for an extra pair of ribs, producing the longest side bacon cuts; calm temperament and excellent maternal milk production."
                        }
                    }
                ],
                [
                    {
                        "type": "concept_explanation",
                        "title": "The Colored Sire Breeds: Duroc and Hampshire",
                        "content": {
                            "title": "Terminal Sires for Carcass Muscling and Growth Vigor",
                            "text": "3. **Duroc (Origin: USA)**:\n- **Conformation**: Light golden-yellow to **deep mahogany-red coat**, medium body frame, and drooping ear tips.\n- **Commercial Strengths**: Incredibly rugged, disease-hardy, fast-growing; excellent feed conversion; produces tender, marbled pork. Used universally as a **terminal sire** on Large White $\\times$ Landrace crossbred sows to produce robust commercial slaughter pigs.\n\n4. **Hampshire (Origin: USA / UK)**:\n- **Conformation**: Jet black body with a **striking white belt wrapping entirely around the shoulders and front legs**; erect ears.\n- **Commercial Strengths**: Produces the leanest carcass with maximum loin-eye muscle area and minimal backfat."
                        }
                    },
                    {
                        "type": "suggested_diagram",
                        "title": "Commercial Pig Breeds Diagnostic Morphological Profiles",
                        "content": {
                            "title": "Commercial Pig Breeds Diagnostic Morphological Profiles",
                            "caption": "Diagnostic visual silhouettes showing: Large White (White, Erect Ears, Deep Body), Landrace (White, Drooping Ears, Extra-Long Bacon Body), Duroc (Mahogany Red, Drooping Tips), and Hampshire (Black Body with Distinct White Shoulder Belt)."
                        }
                    }
                ],
                [
                    {
                        "type": "comparison_table",
                        "title": "Commercial Pig Breeds Diagnostic Matrix",
                        "content": {
                            "title": "Pig Breed Evaluation & Production Matrix",
                            "headers": ["Pig Breed", "Origin", "Coat Color", "Ear Posture", "Body Conformation", "Primary Commercial Role"],
                            "rows": [
                                ["Large White", "UK", "Pure White", "Erect (Upright)", "Deep, well-proportioned frame", "Dual Pork/Bacon; prolific maternal dam line"],
                                ["Landrace", "Denmark", "Pure White", "Large Drooping (covers eyes)", "Extra-long cylindrical body", "Specialized Bacon production; maternal line"],
                                ["Duroc", "USA", "Mahogany Red", "Semi-drooping tips", "Muscular, heavy-boned, rugged", "Terminal Sire line; fast growth & marbling"],
                                ["Hampshire", "USA / UK", "Black with White Belt", "Erect (Upright)", "Compact, heavily muscled loin", "Terminal Sire line; ultra-lean pork carcasses"]
                            ]
                        }
                    },
                    {
                        "type": "mini_activity",
                        "title": "Agribusiness Practical: Designing a 3-Way Commercial Pig Breeding Plan",
                        "content": {
                            "title": "The Commercial Pig Crossbreeding Plan",
                            "task": "1. Understand the 3-Way Cross: Large White (Prolificacy) $\\times$ Landrace (Bacon Length & Milk) $\\rightarrow$ F1 Crossbred Sow.\n2. Mate the F1 Sow with a purebred Duroc or Hampshire Terminal Boar.\n3. Explain why the resulting slaughter piglets grow faster (Heterosis / Hybrid Vigor) and yield superior lean meat.",
                            "materials": ["Breeding Diagram Handout", "Notebook", "Pen"],
                            "safety": "Ensure accurate genetic line tracing."
                        }
                    }
                ],
                [
                    {
                        "type": "key_takeaway",
                        "title": "Core Summary: Pig Breeds",
                        "content": {
                            "title": "Key Takeaways",
                            "text": "- **Large White is identified by erect ears and pure white coat** (top maternal breed).\n- **Landrace has large drooping ears and an extra-long body** for bacon.\n- **Duroc is mahogany-red and rugged**, used as a terminal growth sire.\n- **Hampshire is black with a distinctive white shoulder belt** for ultra-lean meat."
                        }
                    },
                    {
                        "type": "knowledge_check",
                        "title": "Check Your Understanding: Identification of Bacon-Type Landrace Pig",
                        "content": {
                            "question": "A commercial pig farmer wants to produce premium-grade side bacon cuts for meat processing. Which pig breed should they stock, recognized by its extra-long body and large drooping ears that cover its eyes?",
                            "options": [
                                "Duroc",
                                "Landrace",
                                "Hampshire",
                                "Berkshire"
                            ],
                            "answer": "B",
                            "explanation": "The Landrace breed was genetically developed in Denmark specifically for bacon production. It is famous for its exceptionally long cylindrical body (possessing an extra pair of ribs) and its large drooping ears that hang forward over the eyes."
                        }
                    }
                ]
            ]
        },

        # =====================================================================
        # LESSON 5: Rabbit Breeds
        # =====================================================================
        {
            "unit_order": 5,
            "unit_name": "Rabbit Breeds",
            "unit_description": "Cuniculture; commercial meat breeds: New Zealand White (pure white, albino pink eyes, top meat-to-bone ratio), California (white with dark points); Specialty breeds: Flemish Giant (10–12 kg), Angora (wool/fiber).",
            "lesson_title": "Rabbit Breeds (Cuniculture): Meat, Specialty, and Fiber Breeds",
            "pages": [
                [
                    {
                        "type": "suggested_image",
                        "title": "New Zealand White Commercial Meat Rabbit in Clean Hutch",
                        "content": {
                            "title": "New Zealand White Commercial Meat Rabbit in Clean Hutch",
                            "caption": "A purebred New Zealand White rabbit displaying pure white fur, ruby-red albino eyes, and a compact, muscular, blocky body conformation."
                        }
                    },
                    {
                        "type": "learning_goal",
                        "title": "Lesson Objectives: Rabbit Breeds (Cuniculture)",
                        "content": {
                            "title": "What We Will Master Today",
                            "goals": [
                                "Define **cuniculture** and outline the agribusiness advantages of rabbit production.",
                                "Identify the premier commercial meat rabbit breeds (**New Zealand White and California**).",
                                "Examine specialty breeds: **Flemish Giant (Giant Meat) and Angora (Luxury Wool/Fiber)**.",
                                "Compare feed conversion efficiency across rabbit breeds."
                            ]
                        }
                    },
                    {
                        "type": "concept_explanation",
                        "title": "Why Cuniculture? And Commercial Meat Breeds",
                        "content": {
                            "title": "High Efficiency Micro-Livestock",
                            "text": "**Cuniculture** (commercial rabbit farming) is one of the fastest-growing agribusiness sub-sectors in Kenya due to minimal land requirements, low initial capital, high feed conversion, and rapid reproduction (gestation period of only **30 to 32 days**).\n\n1. **New Zealand White (The Global Meat Standard)**:\n- **Conformation**: Pure snowy-white coat, **bright pink/red albino eyes**, broad shoulders, deep loins, and meaty hindquarters ($4.5\\text{--}5.5\\text{ kg}$ adult weight).\n- **Merits**: World's leading commercial meat breed; highest meat-to-bone ratio ($>65\\%$ dress-out); rapid growth (attains $2\\text{ kg}$ slaughter weight in 8–10 weeks); high fertility (6–10 kits/litter).\n\n2. **California Rabbit (The Dark-Pointed Producer)**:\n- **Conformation**: Pure white body with **distinct dark brown or black markings on the nose, ears, feet, and tail**; pink eyes ($4.0\\text{--}5.0\\text{ kg}$).\n- **Merits**: Second only to the New Zealand White; exceptional muscle density, firm carcass, and valuable pelt."
                        }
                    }
                ],
                [
                    {
                        "type": "concept_explanation",
                        "title": "Specialty Breeds: Flemish Giant and Angora",
                        "content": {
                            "title": "Giants and Luxury Fiber Producers",
                            "text": "3. **Flemish Giant (The Giant Breed)**:\n- **Conformation**: Massive body frame reaching **8 to 12 kilograms**; long body with large upright ears (minimum 15 cm); coat colors range from steel grey, black, fawn, to sandy.\n- **Commercial Reality**: While impressive, they grow slowly, take 6–8 months to mature, and have a higher bone-to-meat ratio, making them less feed-efficient for smallholders than New Zealand Whites.\n\n4. **Angora Rabbit (The Fiber Specialist)**:\n- **Conformation**: Entire body completely enveloped in an exceptionally long, thick, fluffy cloud of woolly hair ($>8\\text{--}12\\text{ cm}$ length).\n- **Production**: Reared exclusively for **Angora wool/fiber**; sheared or gently plucked every 3 months, producing luxury fiber that is 6 times warmer than sheep's wool."
                        }
                    },
                    {
                        "type": "comparison_table",
                        "title": "Major Rabbit Breeds Diagnostic & Production Matrix",
                        "content": {
                            "title": "Rabbit Breeds Comparison Chart",
                            "headers": ["Rabbit Breed", "Primary Utility", "Coat Color & Markings", "Eye Color", "Adult Weight", "Agribusiness Efficiency"],
                            "rows": [
                                ["New Zealand White", "Commercial Meat", "Pure white all over", "Pink / Ruby Red", "4.5 – 5.5 kg", "Very High (Fast growth, high dress-out %)"],
                                ["California", "Meat & Pelt", "White with black nose, ears, feet, tail", "Pink", "4.0 – 5.0 kg", "High (Lean muscling, premium pelt)"],
                                ["Flemish Giant", "Specialty Heavy Meat", "Steel grey, sandy, fawn, black", "Brown / Dark", "8.0 – 12.0 kg", "Moderate (Slow maturity, high feed intake)"],
                                ["Angora", "Luxury Wool / Fiber", "White / multi-color woolly coat", "Pink / Dark", "3.5 – 4.5 kg", "High value fiber; requires intensive grooming"]
                            ]
                        }
                    }
                ],
                [
                    {
                        "type": "mini_activity",
                        "title": "Laboratory Practical: Rabbit Breed Conformation & Weight Audit",
                        "content": {
                            "title": "Rabbitry Diagnostic Workshop",
                            "task": "1. Inspect school rabbitry or local farm stock.\n2. Check ear length, coat markings (pure white vs black points), and eye color.\n3. Weigh 3 mature rabbits: record weights and calculate feed conversion efficiency.\n4. Determine whether the stock consists of New Zealand White, California, or crosses.",
                            "materials": ["Hanging Weighing Scale", "Weighing Basket", "Notebook", "Rabbits"],
                            "safety": "Support rabbit hindquarters firmly; never lift a rabbit by its ears!"
                        }
                    },
                    {
                        "type": "key_takeaway",
                        "title": "Core Summary: Rabbit Breeds",
                        "content": {
                            "title": "Key Takeaways",
                            "text": "- **New Zealand White is the premier meat breed** (pure white, pink eyes, high dress-out).\n- **California has white fur with black ears, nose, feet, and tail**.\n- **Flemish Giant reaches 8–12 kg** but grows slowly with high feed needs.\n- **Angora is sheared for luxury wool** (6 times warmer than sheep wool)."
                        }
                    }
                ],
                [
                    {
                        "type": "knowledge_check",
                        "title": "Check Your Understanding: Identification of New Zealand White Rabbit",
                        "content": {
                            "question": "Which commercial rabbit breed is pure white with ruby-red albino eyes and is globally recognized as the most feed-efficient breed for commercial meat production?",
                            "options": [
                                "Flemish Giant",
                                "Angora",
                                "New Zealand White",
                                "Chinchilla"
                            ],
                            "answer": "C",
                            "explanation": "The New Zealand White is the international gold standard for commercial rabbit meat production. Its pure white coat, ruby-red eyes, high feed conversion ratio, rapid growth to slaughter weight, and high meat-to-bone ratio make it the most profitable commercial meat breed."
                        }
                    }
                ]
            ]
        },

        # =====================================================================
        # LESSON 6: Sheep Breeds
        # =====================================================================
        {
            "unit_order": 6,
            "unit_name": "Sheep Breeds",
            "unit_description": "Wool: Merino (fine crimp wool, Spain); Dual-purpose: Corriedale; Meat/Hair tropical: Dorper (black head, naturally shedding fleece), Red Masai (indigenous fat-tailed, genetic Haemonchus contortus internal worm resistance).",
            "lesson_title": "Sheep Breeds: Merino, Dorper, Corriedale, and Indigenous Red Masai",
            "pages": [
                [
                    {
                        "type": "suggested_image",
                        "title": "Dorper Mutton Ram with Distinctive Black Head in Semi-Arid Pasture",
                        "content": {
                            "title": "Dorper Mutton Ram with Distinctive Black Head in Semi-Arid Pasture",
                            "caption": "A robust Dorper ram showcasing the iconic black head, white body, heavy muscling, and self-shedding hair-wool coat suited for dry rangelands."
                        }
                    },
                    {
                        "type": "learning_goal",
                        "title": "Lesson Objectives: Sheep Breeds",
                        "content": {
                            "title": "What We Will Master Today",
                            "goals": [
                                "Classify sheep into **Wool, Meat (Mutton), and Dual-Purpose Breeds**.",
                                "Describe the traits of **Merino, Corriedale, Dorper, and Red Masai** sheep.",
                                "Analyze why **Dorper sheep do not require shearing** (self-shedding coat).",
                                "Explain the crucial genetic resistance of the **Red Masai sheep to Barber's Pole Worm (*Haemonchus contortus*)**."
                            ]
                        }
                    },
                    {
                        "type": "concept_explanation",
                        "title": "Wool and Dual-Purpose Sheep: Merino and Corriedale",
                        "content": {
                            "title": "Highland Wool and Mutton Producers",
                            "text": "1. **Merino (Origin: Spain)**:\n- **Conformation**: Medium frame, heavily wrinkled skin (producing more wool surface area), males bear spiral horns.\n- **Wool Superiority**: The world's undisputed premier **fine wool breed**; produces dense fleece with microscopic fiber diameter and high crimp. Highly vulnerable to wet climates, which cause severe fleece rot and foot rot.\n\n2. **Corriedale (Origin: New Zealand)**:\n- **Conformation**: Large body frame, naturally polled (hornless), covered in dense white fleece extending down the legs.\n- **Dual-Purpose Excellence**: Bred from Merino $\\times$ Lincoln/Leicester crosses; yields heavy mutton carcasses alongside high volumes of quality medium-grade wool."
                        }
                    }
                ],
                [
                    {
                        "type": "concept_explanation",
                        "title": "Tropical Meat and Hair Sheep: Dorper and Red Masai",
                        "content": {
                            "title": "Masters of the Semi-Arid Rangelands",
                            "text": "3. **Dorper (Origin: South Africa - Dorset Horn $\\times$ Blackhead Persian)**:\n- **Conformation**: Solid white body with a **striking jet-black head and neck** (or solid white variant); muscular, barrel-shaped body.\n- **Self-Shedding Coat**: Possesses a mixture of hair and short wool that **sheds naturally in spring without manual shearing**; fast growth on dry rangelands.\n\n4. **Red Masai (Origin: East Africa / Indigenous Maasai Pastoralists)**:\n- **Conformation**: Solid reddish-brown to dark red coat of coarse hair, fat-tailed (stores energy), lop ears.\n- **The Nematode Resistance Superpower**: Possesses world-famous genetic resistance to **Barber's Pole Worm (*Haemonchus contortus*)**—a deadly blood-sucking internal parasite that kills exotic sheep in humid tropical grazing fields! Highly drought-hardy and disease-tolerant."
                        }
                    },
                    {
                        "type": "suggested_diagram",
                        "title": "Meat & Dairy Sheep Breeds: Merino vs Dorper vs Red Masai",
                        "content": {
                            "title": "Meat & Dairy Sheep Breeds: Merino vs Dorper vs Red Masai",
                            "caption": "Comparative structural diagram: Merino (Wrinkled Skin, Fine Wool, Spiral Horns), Dorper (Black Head, White Body, Barrel Muscling, Self-Shedding), and Red Masai (Red Hair Coat, Fat Tail, High Parasite Resistance)."
                        }
                    }
                ],
                [
                    {
                        "type": "comparison_table",
                        "title": "Major Sheep Breeds Evaluation Matrix",
                        "content": {
                            "title": "Sheep Breeds Production & Adaptability Matrix",
                            "headers": ["Sheep Breed", "Category", "Origin", "Coat / Fleece Type", "Distinctive Physical Markers", "Key Agribusiness Trait"],
                            "rows": [
                                ["Merino", "Fine Wool", "Spain", "Dense, fine-crimped wool", "Wrinkled skin; spiral horns in rams", "World's most valuable fine wool fiber"],
                                ["Corriedale", "Dual-Purpose", "New Zealand", "Dense medium-grade wool", "Large polled frame, wool on legs", "Balanced commercial meat and wool yields"],
                                ["Dorper", "Mutton (Meat)", "South Africa", "Hair-wool mixture (Self-shedding)", "White body with distinct black head", "Rapid growth; no shearing labor needed"],
                                ["Red Masai", "Indigenous Meat/Hair", "East Africa", "Coarse red hair (Fat-tailed)", "Reddish-brown color, fat storage tail", "Genetic resistance to Haemonchus worms & drought"]
                            ]
                        }
                    },
                    {
                        "type": "mini_activity",
                        "title": "Field Practical: Sheep Conformation and Fleece Inspection Lab",
                        "content": {
                            "title": "Sheep Breed Diagnostic Practicum",
                            "task": "1. Inspect school farm sheep or local pastoral flock.\n2. Observe coat type: Wool (crimped fiber) vs Hair (smooth/coarse).\n3. Check head pigmentation (Black head of Dorper vs Red face of Red Masai).\n4. Inspect the tail: Fat tail (energy storage in Red Masai) vs Thin tail (Dorper/Merino).",
                            "materials": ["Handling Pen", "Sheep Halter", "Notebook", "Pen"],
                            "safety": "Handle sheep calmly; do not grab sheep by their fleece."
                        }
                    }
                ],
                [
                    {
                        "type": "key_takeaway",
                        "title": "Core Summary: Sheep Breeds",
                        "content": {
                            "title": "Key Takeaways",
                            "text": "- **Merino produces the finest crimped wool** (wrinkled skin).\n- **Corriedale is the leading dual-purpose sheep** (meat + wool).\n- **Dorper has a black head and white body** with a self-shedding coat.\n- **Red Masai has unmatched genetic resistance** to deadly internal worms."
                        }
                    },
                    {
                        "type": "knowledge_check",
                        "title": "Check Your Understanding: Rationale for Indigenous Red Masai Genetic Preservation",
                        "content": {
                            "question": "Why is the indigenous Red Masai sheep considered a critically valuable genetic resource for animal breeders and smallholder farmers across East Africa?",
                            "options": [
                                "It produces the finest Merino-grade wool for luxury export garments",
                                "It possesses exceptional natural genetic resistance to deadly gastrointestinal nematode parasites (especially Haemonchus contortus) and extreme drought tolerance",
                                "It grows to 150 kg in body weight within 2 months",
                                "It produces 15 liters of milk per day"
                            ],
                            "answer": "B",
                            "explanation": "The indigenous Red Masai sheep has evolved natural immunogenetic resistance against the lethal blood-sucking stomach worm Haemonchus contortus (barber's pole worm). While exotic sheep suffer massive mortality from internal parasites, the Red Masai survives and reproduces on communal rangelands with minimal deworming medications."
                        }
                    }
                ]
            ]
        },

        # =====================================================================
        # LESSON 7: Goat Breeds
        # =====================================================================
        {
            "unit_order": 7,
            "unit_name": "Goat Breeds",
            "unit_description": "Meat: Boer (white body, red head, heavy muscling), Kalahari Red, Galla (pure white indigenous, arid scrubland); Dairy: Saanen (white, top volume milker), Toggenburg (white facial stripes & socks), Alpine, Nubian (Roman nose, drooping ears, high butterfat); Fiber: Angora (mohair), Cashmere.",
            "lesson_title": "Goat Breeds: Meat (Boer, Galla), Dairy (Saanen, Toggenburg, Nubian), and Fiber",
            "pages": [
                [
                    {
                        "type": "suggested_image",
                        "title": "Purebred Boer Meat Buck with Classic Red Head and White Body",
                        "content": {
                            "title": "Purebred Boer Meat Buck with Classic Red Head and White Body",
                            "caption": "A heavy-muscled Boer buck displaying the characteristic dark reddish-brown head, white body, and backward-curved horns."
                        }
                    },
                    {
                        "type": "learning_goal",
                        "title": "Lesson Objectives: Goat Breeds",
                        "content": {
                            "title": "What We Will Master Today",
                            "goals": [
                                "Classify goat breeds into **Meat, Dairy, and Fiber (Mohair/Cashmere)** categories.",
                                "Identify commercial meat breeds: **Boer, Kalahari Red, and indigenous Galla**.",
                                "Identify leading dairy breeds: **Saanen (Volume King), Toggenburg, Alpine, and Nubian (Butterfat Champion)**.",
                                "Distinguish **Angora mohair fiber** from **Cashmere undercoat**."
                            ]
                        }
                    },
                    {
                        "type": "concept_explanation",
                        "title": "Commercial Meat Goats: Boer and Galla",
                        "content": {
                            "title": "Heavy Muscling and Arid Rangeland Hardiness",
                            "text": "1. **Boer Goat (Origin: South Africa)**:\n- **Conformation**: Solid white body with a **dark reddish-brown head and neck**, drooping pendulous ears, and backward-curved horns ($90\\text{--}120\\text{ kg}$ buck weight).\n- **Merits**: The premier commercial meat goat globally; rapid growth rates ($200\\text{--}250\\text{ g/day}$); heavy muscling and high carcass dress-out percentage ($>50\\%$).\n\n2. **Galla / Boran Goat (Origin: Northern Kenya / East Africa)**:\n- **Conformation**: Pure white short hair, medium frame ($45\\text{--}60\\text{ kg}$), upright alert posture.\n- **Merits**: Outstanding indigenous adaptation to hot, thorny *Acacia* scrublands; highly prolific; excellent milk yield for pastoral kids; prized for crossbreeding with Boers."
                        }
                    }
                ],
                [
                    {
                        "type": "concept_explanation",
                        "title": "Dairy and Fiber Goat Breeds",
                        "content": {
                            "title": "Dairy Champions and Luxury Textile Producers",
                            "text": "3. **Saanen (Origin: Switzerland)**: Solid white or cream coat, erect ears, polled; the **'Friesian of the goat world'**, producing the **highest milk volume** ($3\\text{--}5\\text{ L/day}$) with $3.5\\%$ butterfat.\n4. **Toggenburg (Origin: Switzerland)**: Fawn to chocolate-brown with **distinct white facial stripes running from eyes to muzzle, white leg socks, and white tail triangles**; hardy active milker ($2.5\\text{--}4\\text{ L/day}$).\n5. **Anglo-Nubian (Origin: UK / Egypt)**: Large frame, distinct **convex Roman nose**, and **long, wide drooping ears**; produces milk with the **highest butterfat ($5.0\\%\\text{ to }6.0\\%$)**.\n6. **Fiber Goats**:\n- **Angora Goat**: Produces **mohair** (long, lustrous, wavy ringlets of silky fiber).\n- **Cashmere Goat**: Produces **cashmere** (ultra-fine insulating down plucked from the undercoat)."
                        }
                    },
                    {
                        "type": "suggested_diagram",
                        "title": "Goat Breeds Classification Tree: Meat, Dairy, and Fiber",
                        "content": {
                            "title": "Goat Breeds Classification Tree: Meat, Dairy, and Fiber",
                            "caption": "Taxonomic classification tree branching into: 1 Meat Breeds (Boer, Kalahari Red, Galla), 2 Dairy Breeds (Saanen, Toggenburg, Alpine, Nubian), and 3 Fiber Breeds (Angora Mohair, Cashmere Down)."
                        }
                    }
                ],
                [
                    {
                        "type": "comparison_table",
                        "title": "Master Goat Breeds Evaluation Matrix",
                        "content": {
                            "title": "Goat Breeds Utility & Morphological Matrix",
                            "headers": ["Goat Breed", "Primary Utility", "Origin", "Distinctive Physical Markings", "Key Production Feature"],
                            "rows": [
                                ["Boer", "Commercial Meat", "South Africa", "White body with reddish-brown head/neck", "Heavy muscling; fast weight gain (250g/day)"],
                                ["Galla (Boran)", "Indigenous Meat/Milk", "Kenya (Northern)", "Pure white coat, medium frame", "Extreme heat & arid thornbush tolerance"],
                                ["Saanen", "Commercial Dairy", "Switzerland", "Pure white/cream, erect ears, polled", "Highest milk volume (3–5 L/day)"],
                                ["Toggenburg", "Commercial Dairy", "Switzerland", "Brown with white face stripes & leg socks", "Hardy milker; thrives in high-altitude zones"],
                                ["Anglo-Nubian", "Dual Dairy/Meat", "UK / Egypt", "Roman nose, long pendulous drooping ears", "Highest butterfat milk (5.0–6.0%)"],
                                ["Angora", "Luxury Fiber", "Turkey", "White with long spiraling lustrous locks", "Produces high-value Mohair textile fiber"]
                            ]
                        }
                    },
                    {
                        "type": "mini_activity",
                        "title": "Field Practical: Dairy Goat Conformation and Milking Audit",
                        "content": {
                            "title": "Dairy Goat Management Lab",
                            "task": "1. Inspect a Saanen, Toggenburg, or Nubian dairy doe.\n2. Examine dairy wedge conformation: wide pelvic width, capacious udder attachment, and well-spaced teats.\n3. Observe a hygienic milking demonstration (stripping, CMT mastitis paddle test).\n4. Record daily milk yield.",
                            "materials": ["Dairy Goat Doe", "Strip Cup", "CMT Reagent Paddle", "Milking Pail"],
                            "safety": "Wash and disinfect hands and teats before milking; approach doe calmly."
                        }
                    }
                ],
                [
                    {
                        "type": "key_takeaway",
                        "title": "Core Summary: Goat Breeds",
                        "content": {
                            "title": "Key Takeaways",
                            "text": "- **Boer is the premier meat goat** (white body, dark red head, heavy muscling).\n- **Galla is the pure white indigenous goat** adapted to hot arid scrublands.\n- **Saanen produces the highest milk volume** (the 'Friesian of goats').\n- **Toggenburg is recognized by white facial stripes** and white socks.\n- **Nubian has a Roman nose and long drooping ears** (highest butterfat).\n- **Angora goats produce mohair fiber**."
                        }
                    },
                    {
                        "type": "knowledge_check",
                        "title": "Check Your Understanding: Identification of Anglo-Nubian Dairy Goat",
                        "content": {
                            "question": "Which dairy goat breed is easily identified by its distinctive convex Roman nose and long, wide drooping ears, producing milk with the highest butterfat percentage among dairy goats?",
                            "options": [
                                "Saanen",
                                "Alpine",
                                "Anglo-Nubian",
                                "Toggenburg"
                            ],
                            "answer": "C",
                            "explanation": "The Anglo-Nubian breed is instantly recognized by its convex 'Roman' facial profile and its long, wide, pendulous ears. Furthermore, its milk contains the highest butterfat concentration (5.0%–6.0%) of all dairy goat breeds."
                        }
                    }
                ]
            ]
        },

        # =====================================================================
        # LESSON 8: Comparing Breed Characteristics
        # =====================================================================
        {
            "unit_order": 8,
            "unit_name": "Comparing Breed Characteristics",
            "unit_description": "Humped (Bos indicus) vs Humpless (Bos taurus); anatomical adaptations: ear morphology as vascular radiators, loose dewlap surface area, solar reflectance of light vs dark coats.",
            "lesson_title": "Comparative Anatomy: Humped vs Humpless Cattle, Ears, and Coat Adaptation",
            "pages": [
                [
                    {
                        "type": "suggested_image",
                        "title": "Tropical Zebu Bull Grazing in Open Sun Showcasing Hump and Dewlap",
                        "content": {
                            "title": "Tropical Zebu Bull Grazing in Open Sun Showcasing Hump and Dewlap",
                            "caption": "A tropical Bos indicus bull grazing in direct equatorial sunlight, using its large thoracic hump, loose dewlap, and light coat to maintain thermal equilibrium."
                        }
                    },
                    {
                        "type": "learning_goal",
                        "title": "Lesson Objectives: Comparative Breed Anatomy",
                        "content": {
                            "title": "What We Will Master Today",
                            "goals": [
                                "Distinguish the two evolutionary lineages: **Humped (*Bos indicus*) vs Humpless (*Bos taurus*)**.",
                                "Analyze the physiological function of the **thoracic hump, loose dewlap, and pendulous ears**.",
                                "Explain how **coat color and melanin pigmentation** control solar heat absorption and skin cancer protection.",
                                "Evaluate livestock heat dissipation mechanisms in tropical environments."
                            ]
                        }
                    },
                    {
                        "type": "concept_explanation",
                        "title": "Humped (Bos indicus) vs Humpless (Bos taurus) Evolution",
                        "content": {
                            "title": "Two Distinct Evolutionary Masterpieces",
                            "text": "1. **Humped Cattle (*Bos indicus* - Zebu, Boran, Brahman, Sahiwal)**:\n- **Origin**: Evolved in the hot, arid, disease-dense tropics of South Asia and Africa.\n- **Key Anatomical Traits**: Prominent muscular-fatty hump over the withers/shoulders; extensive loose skin folds extending from throat to chest (dewlap) and navel (sheath); large vascular pendulous ears; light coat reflecting solar rays.\n\n2. **Humpless Cattle (*Bos taurus* - Friesian, Jersey, Angus, Hereford)**:\n- **Origin**: Evolved in cool, temperate European climates.\n- **Key Anatomical Traits**: Completely humpless back; tight skin; small, erect, non-vascular ears; blocky or wedge-shaped compact body. Highly efficient in converting high-energy silage into milk/meat, but suffers severe heat stress in equatorial sunlight."
                        }
                    }
                ],
                [
                    {
                        "type": "concept_explanation",
                        "title": "Thermoregulation: Ears, Dewlap, and Coat Color",
                        "content": {
                            "title": "How Tropical Livestock Beat the Heat",
                            "text": "- **Vascular Radiator Ears**: Large, drooping ears (in Brahman cattle and Nubian goats) contain an extensive network of dilated surface blood vessels. As ambient breeze blows across the ear flaps, it cools the circulating blood before it returns to the body core, lowering internal body temperature.\n- **The Dewlap Surface Area Multiplier**: The loose folds of skin along the throat and chest increase total body surface area by up to **20%**, allowing greater cutaneous evaporative heat loss without increasing body mass.\n- **Solar Radiation Physics (Coat Color)**: Light grey, white, and golden coats (Boran, Guernsey, Galla) reflect up to **80% of solar radiation**. Dark black coats (Friesian, Angus) absorb over **90% of solar heat**, causing rapid hyperthermia in unshaded pastures."
                        }
                    },
                    {
                        "type": "comparison_table",
                        "title": "Anatomical Adaptation: Bos indicus vs Bos taurus",
                        "content": {
                            "title": "Tropical vs Temperate Bovine Anatomy Matrix",
                            "headers": ["Anatomical Feature", "Bos indicus (Humped Zebu / Boran)", "Bos taurus (Humpless Friesian / Angus)"],
                            "rows": [
                                ["Thoracic Hump", "Present (Stores energy reserves as fat/muscle)", "Absent (Flat, straight backline)"],
                                ["Dewlap & Navel Flap", "Extensive, loose, folded skin (Max surface area)", "Tight, minimal skin folds (Conserves heat)"],
                                ["Ear Structure", "Large, long, drooping, highly vascular", "Small, short, upright, non-vascular"],
                                ["Sweat Gland Density", "High density (Efficient evaporative cooling)", "Low density (Relies heavily on panting)"],
                                ["Optimal Temperature Range", "25°C to 42°C (Heat resilient)", "5°C to 20°C (Prone to heat stress >25°C)"]
                            ]
                        }
                    }
                ],
                [
                    {
                        "type": "mini_activity",
                        "title": "Field Practical: Measuring Livestock Respiration and Heat Stress",
                        "content": {
                            "title": "Heat Stress Diagnostic Lab",
                            "task": "1. On a hot sunny midday (12:00 PM - 2:00 PM), observe 2 cows: Cow A (Black Friesian) vs Cow B (White Boran/Zebu).\n2. Count flank movements for 1 minute to record respiration rate (breaths/min).\n3. Check for signs of heat stress: tongue protrusion, open-mouth panting, drooling, and seeking shade.\n4. Record which cow exhibits thermal distress.",
                            "materials": ["Stopwatch", "Thermometer", "Notebook", "Cattle"],
                            "safety": "Keep safe distance from animals; observe from outside the pen."
                        }
                    },
                    {
                        "type": "key_takeaway",
                        "title": "Core Summary: Comparative Anatomy",
                        "content": {
                            "title": "Key Takeaways",
                            "text": "- ***Bos indicus* cattle have a thoracic hump and loose dewlap** for tropical heat resilience.\n- ***Bos taurus* cattle are humpless** with tight skin, bred for temperate climates.\n- **Large drooping ears act as vascular heat radiators**.\n- **Light coat colors reflect solar radiation**, while dark coats absorb heat."
                        }
                    }
                ],
                [
                    {
                        "type": "knowledge_check",
                        "title": "Check Your Understanding: Function of the Dewlap and Drooping Ears",
                        "content": {
                            "question": "What is the primary biological and physiological function of the extensive loose skin folds (dewlap) and large drooping ears in tropical Bos indicus cattle?",
                            "options": [
                                "To store excess water for multi-day desert travel",
                                "To increase body surface area and provide high vascular blood exposure, facilitating rapid convective and evaporative heat loss to keep the animal cool",
                                "To frighten away predatory hyenas and leopards",
                                "To absorb nitrogen from the atmospheric air"
                            ],
                            "answer": "B",
                            "explanation": "The extensive dewlap and large drooping ears dramatically increase the animal's total body surface area relative to its weight. Packed with surface capillaries and sweat glands, these structures act as biological cooling radiators, releasing metabolic heat to maintain a safe core body temperature."
                        }
                    }
                ]
            ]
        },

        # =====================================================================
        # LESSON 9: Comparative Productivity
        # =====================================================================
        {
            "unit_order": 9,
            "unit_name": "Comparative Productivity",
            "unit_description": "Milk volume vs butterfat solids trade-off; high-input exotic potential vs low-input indigenous survival; the foundational formula Productivity = Genetics x Environment.",
            "lesson_title": "Comparative Productivity: The Genetics x Environment Formula and Enterprise Trade-Offs",
            "pages": [
                [
                    {
                        "type": "suggested_image",
                        "title": "Modern Commercial Zero-Grazing Dairy Unit with Optimal Nutrition",
                        "content": {
                            "title": "Modern Commercial Zero-Grazing Dairy Unit with Optimal Nutrition",
                            "caption": "High-producing dairy cows feeding on precision Total Mixed Rations (TMR) inside a shaded, well-ventilated barn, demonstrating the alignment of genetics with optimal environment."
                        }
                    },
                    {
                        "type": "learning_goal",
                        "title": "Lesson Objectives: Comparative Productivity",
                        "content": {
                            "title": "What We Will Master Today",
                            "goals": [
                                "Analyze the foundational livestock equation: **Productivity = Genetics x Environment**.",
                                "Evaluate the **Milk Volume vs Butterfat Solids economic trade-off**.",
                                "Analyze the **High-Input Exotic Yield vs Low-Input Indigenous Survival trade-off**.",
                                "Formulate enterprise-level stocking decisions based on capital and pasture resources."
                            ]
                        }
                    },
                    {
                        "type": "concept_explanation",
                        "title": "The Golden Equation: Productivity = Genetics x Environment",
                        "content": {
                            "title": "Why Superior Genetics Alone Cannot Guarantee Profit",
                            "text": "In animal production, yield is dictated by the interaction between inherited potential and external management:\n\n$$\\text{Productivity} = \\text{Genetics} \\times \\text{Environment}$$\n\n- **Genetics (The Ceiling)**: Sets the maximum biological upper limit of what an animal can potentially produce (e.g. A Friesian cow has the genetic potential for $35\\text{ L/day}$; a Zebu has the genetic potential for $4\\text{ L/day}$).\n- **Environment (The Enabler)**: Represents nutrition, water availability, housing ventilation, temperature control, disease management, and sanitation.\n- **The Pitfall**: If a farmer buys a cow with $35\\text{ L}$ genetics but provides an environment worth only $3\\text{ L}$ (dry poor pasture, tick infestation, heat stress), the cow will produce $3\\text{ L}$ and quickly suffer reproductive failure or death!"
                        }
                    }
                ],
                [
                    {
                        "type": "concept_explanation",
                        "title": "The Two Fundamental Agribusiness Trade-Offs",
                        "content": {
                            "title": "1. Volume vs Solids | 2. Yield vs Survival",
                            "text": "1. **Volume vs Solids (Dairy)**:\n- Selling raw liquid milk to urban consumers $\\rightarrow$ Prioritize **Volume (Friesian/Ayrshire)**.\n- Selling milk to processing plants for cheese, butter, or long-distance transit $\\rightarrow$ Prioritize **Butterfat Solids (Jersey/Guernsey)**.\n\n2. **Yield Potential vs Survival Capacity (Ecology)**:\n- **High-Input Intensive Farms**: Highland climate, zero-grazing, high budget for silage and veterinary care $\\rightarrow$ Stock **Exotics (Friesian, Landrace, New Zealand White)**.\n- **Low-Input Extensive Ranches**: Arid climate, drought risk, high tick challenge, communal grazing $\\rightarrow$ Stock **Indigenous / Adapted Crosses (Boran, Red Masai, Galla, Dorper)**."
                        }
                    },
                    {
                        "type": "suggested_diagram",
                        "title": "Livestock Productivity Equation: Productivity = Genetics x Environment",
                        "content": {
                            "title": "Livestock Productivity Equation: Productivity = Genetics x Environment",
                            "caption": "Conceptual equation graphic: Genetics (DNA Potential Ceiling) Multiplied by Environment (Nutrition + Disease Control + Housing) Equals Realized Farm Productivity and Profit."
                        }
                    }
                ],
                [
                    {
                        "type": "comparison_table",
                        "title": "Agro-Ecological Zone Matching Matrix",
                        "content": {
                            "title": "Livestock Enterprise Matching Framework",
                            "headers": ["Agro-Ecological Zone", "Climatic Conditions", "Feed & Water Availability", "Recommended Cattle Breed", "Recommended Small Stock"],
                            "rows": [
                                ["Highland Zone I & II (e.g. Kiambu, Nyandarua)", "Cool, high rainfall (15–20°C)", "Abundant lush pasture, Napier grass, silage", "Holstein Friesian, Ayrshire", "Landrace pig, Saanen goat, NZ White rabbit"],
                                ["Medium Zone III (e.g. Nakuru, Eldoret)", "Moderate rainfall, warm days", "Managed pastures, Rhodes grass, hay", "Ayrshire, Guernsey, Jersey, Simmental", "Large White pig, Toggenburg goat, Corriedale sheep"],
                                ["Semi-Arid Zone IV (e.g. Machakos, Laikipia)", "Low rainfall, hot, seasonal dry spells", "Natural range grasses, Acacia browse, limited hay", "Sahiwal, Boran, Brahman cross", "Boer goat, Galla goat, Dorper sheep"],
                                ["Arid Zone V & VI (e.g. Garissa, Turkana)", "Very hot, drought-prone (<300mm rain)", "Sparse desert scrub, thorny browse, scarce water", "Indigenous East African Zebu, Boran", "Galla goat, Red Masai sheep, Camel"]
                            ]
                        }
                    },
                    {
                        "type": "mini_activity",
                        "title": "Agribusiness Practical: Farm Investment Consulting Simulation",
                        "content": {
                            "title": "The Livestock Stocking Feasibility Challenge",
                            "task": "A youth group in Kajiado (Semi-arid, hot, 40-acre bush farm, budget KES 500,000) asks you whether to buy:\n- Option A: 4 purebred Holstein Friesian dairy cows\n- Option B: 20 Galla goats + 10 Dorper sheep + 2 Boran heifers\n\nAnalyze Option A vs Option B using the $\\text{Productivity} = \\text{Genetics} \\times \\text{Environment}$ framework and write a 1-page financial recommendation.",
                            "materials": ["Investment Case Handout", "Price Guide", "Calculator"],
                            "safety": "Ensure sound economic analysis."
                        }
                    }
                ],
                [
                    {
                        "type": "key_takeaway",
                        "title": "Core Summary: Comparative Productivity",
                        "content": {
                            "title": "Key Takeaways",
                            "text": "- **Productivity equals Genetics multiplied by Environment**.\n- **Genetics sets the upper ceiling**; environment determines what is achieved.\n- **Urban liquid milk demands Friesian volume**; processing demands Jersey solids.\n- **Always match animal genetics to available feed and climate resources**."
                        }
                    },
                    {
                        "type": "knowledge_check",
                        "title": "Check Your Understanding: The Genetics x Environment Equation",
                        "content": {
                            "question": "What is the practical agribusiness implication of the livestock production equation 'Productivity = Genetics x Environment' for a commercial livestock farmer?",
                            "options": [
                                "Genetics is the only factor that determines yield; housing and feed do not matter",
                                "Genetics sets the biological potential ceiling, but the animal can only achieve that potential if the environment (nutrition, disease control, housing) supports it",
                                "Environment completely alters the animal's DNA within two weeks",
                                "Farmers should always purchase the cheapest feeds on the market"
                            ],
                            "answer": "B",
                            "explanation": "Genetics determines what the animal is biologically capable of producing under ideal conditions. However, without an enabling environment—consisting of adequate high-quality nutrition, disease prophylaxis, clean water, and thermal comfort—the animal cannot express its genetic potential."
                        }
                    }
                ]
            ]
        },

        # =====================================================================
        # LESSON 10: Sub-strand Review and Assessment
        # =====================================================================
        {
            "unit_order": 10,
            "unit_name": "Sub-strand Review and Assessment",
            "unit_description": "Consolidated breed taxonomy and selection framework; Kenyan Livestock Stocking Project consulting task; 8 Summative Topic Assessment MCQs covering the complete Topic 8 module.",
            "lesson_title": "Synthesis of Livestock Breeds and Summative Assessment",
            "pages": [
                [
                    {
                        "type": "suggested_image",
                        "title": "Thriving Livestock Enterprise in Kenyan Savannah Landscape",
                        "content": {
                            "title": "Thriving Livestock Enterprise in Kenyan Savannah Landscape",
                            "caption": "A sustainable livestock production enterprise in Kenya, combining scientific breed selection, ecological adaptation, and sound commercial animal husbandry."
                        }
                    },
                    {
                        "type": "learning_goal",
                        "title": "Lesson Objectives: Synthesis & Summative Assessment",
                        "content": {
                            "title": "What We Will Master Today",
                            "goals": [
                                "Synthesize the **complete taxonomy of cattle, pigs, rabbits, sheep, and goat breeds**.",
                                "Complete the **Kenyan Livestock Stocking Project consulting task**.",
                                "Resolve the **Nyandarua Dairy vs Zebu Agribusiness Case Study**.",
                                "Complete the comprehensive **Summative Topic Assessment** covering all 10 lessons of Topic 8."
                            ]
                        }
                    },
                    {
                        "type": "concept_explanation",
                        "title": "Master Livestock Breeds Taxonomy Framework",
                        "content": {
                            "title": "Consolidating Senior School Livestock Mastery",
                            "text": "1. **Dairy Cattle**: Friesian (Max Volume), Jersey (Max Fat 5.5%), Ayrshire (Hardy Forager), Guernsey (Golden Beta-Carotene Milk).\n2. **Beef Cattle**: Boran (Tropical tick/drought hardy), Brahman (Max Heat Dissipation), Aberdeen Angus (Marbled Steak), Hereford (Docile White-Face).\n3. **Pigs**: Large White (Erect ears, prolificacy), Landrace (Drooping ears, long bacon body), Duroc (Mahogany red sire), Hampshire (White belt).\n4. **Rabbits**: New Zealand White (Meat standard, pink eyes), California (Dark points), Flemish Giant (8–12 kg), Angora (Luxury Wool).\n5. **Sheep**: Merino (Fine wool), Corriedale (Dual-purpose), Dorper (Black head, self-shedding meat), Red Masai (Genetic worm resistance).\n6. **Goats**: Boer (Meat champion), Galla (Arid indigenous), Saanen (Volume dairy), Toggenburg (Face stripes), Nubian (Roman nose, high fat)."
                        }
                    }
                ],
                [
                    {
                        "type": "suggested_diagram",
                        "title": "Master Livestock Breeds Taxonomy & Agro-Ecological Match",
                        "content": {
                            "title": "Master Livestock Breeds Taxonomy & Agro-Ecological Match",
                            "caption": "Taxonomic map showing the 5 livestock species and their breed branches mapped across Agro-Ecological Zones (Highlands -> Medium -> Semi-Arid -> Arid Rangelands)."
                        }
                    },
                    {
                        "type": "comparison_table",
                        "title": "Comprehensive Livestock Breeds Master Summary",
                        "content": {
                            "title": "Master Breed Classification Chart",
                            "headers": ["Species", "Exotic High-Yielding Breeds", "Indigenous / Tropical Adapted Breeds", "Key Diagnostic Marker"],
                            "rows": [
                                ["Cattle (Dairy)", "Friesian, Jersey, Ayrshire, Guernsey", "Sahiwal (Dual)", "Wedge shape, udder size, coat patterns"],
                                ["Cattle (Beef)", "Aberdeen Angus, Hereford", "Boran, Brahman", "Thoracic hump, dewlap, ear size, marbling"],
                                ["Pigs", "Large White, Landrace, Duroc, Hampshire", "Local scavenging pigs", "Ear posture (erect vs drooping), white belt, body length"],
                                ["Rabbits", "New Zealand White, California, Flemish Giant, Angora", "Crossbred local rabbits", "Albino ruby eyes, dark point markings, wool fleece"],
                                ["Sheep", "Merino, Corriedale, Dorper", "Red Masai (Fat-tailed)", "Black head (Dorper), wrinkled skin (Merino), fat tail"],
                                ["Goats", "Boer, Saanen, Toggenburg, Alpine, Nubian", "Galla (Boran), Small East African", "Red head (Boer), white face stripes (Toggenburg), Roman nose"]
                            ]
                        }
                    }
                ],
                [
                    {
                        "type": "mini_activity",
                        "title": "Performance Task: The Kenyan Livestock Stocking Project",
                        "content": {
                            "title": "County Livestock Stocking Advisory Proposal",
                            "task": "Working in consulting teams of five, select either:\n- Scenario 1: High-Rainfall Highland Dairy & Pig Enterprise (Nyandarua County)\n- Scenario 2: Semi-Arid Rangeland Beef, Sheep & Goat Enterprise (Laikipia/Machakos County)\n\nDraft a 2-page Stocking Proposal detailing: 2 chosen species, 1 exotic and 1 indigenous breed per species, physical identification markers, and an economic justification using $\\text{Productivity} = \\text{Genetics} \\times \\text{Environment}$.",
                            "materials": ["Proposal Template", "Breed Guide", "Pen"],
                            "safety": "Ensure rigorous, evidence-based recommendations."
                        }
                    },
                    {
                        "type": "key_takeaway",
                        "title": "Core Summary: Livestock Mastery",
                        "content": {
                            "title": "Key Takeaways",
                            "text": "- **Match breed genetics to agro-ecological zones** and feed budgets.\n- **Identify breeds by distinct physical markers** (ears, humps, coats, belts).\n- **Combine exotic yield potential with indigenous survival traits** via crossbreeding.\n- **Safeguard indigenous genetic diversity** to combat climate change."
                        }
                    }
                ],
                # Pages 4 to 8: 8 Summative Assessment MCQs
                [
                    {
                        "type": "knowledge_check",
                        "title": "Summative MCQ 1: Cattle Breed Lineage and Traits",
                        "content": {
                            "question": "Which of the following cattle breeds is an exotic dairy breed originating from Scotland, characterized by cherry-red and white markings, and renowned for being an active, hardy forager on hilly pastures?",
                            "options": [
                                "Holstein Friesian",
                                "Ayrshire",
                                "Jersey",
                                "Aberdeen Angus"
                            ],
                            "answer": "B",
                            "explanation": "The Ayrshire originated in the rugged county of Ayr in Scotland. It is characterized by cherry-red/brown and white markings and is globally recognized as the hardiest and most active foraging exotic dairy breed on rough terrain."
                        }
                    },
                    {
                        "type": "knowledge_check",
                        "title": "Summative MCQ 2: Beef Cattle Intramuscular Marbling",
                        "content": {
                            "question": "Which beef cattle breed is solid black, naturally polled (hornless), and world-famous for producing premium steak with extensive intramuscular fat marbling?",
                            "options": [
                                "Boran",
                                "Hereford",
                                "Aberdeen Angus",
                                "Brahman"
                            ],
                            "answer": "C",
                            "explanation": "The Aberdeen Angus is a hornless (polled) black beef breed from Scotland celebrated for depositing intramuscular fat (marbling) throughout its meat, creating superior tenderness and flavor."
                        }
                    }
                ],
                [
                    {
                        "type": "knowledge_check",
                        "title": "Summative MCQ 3: Bacon Pig Breed Conformation",
                        "content": {
                            "question": "Which commercial pig breed is white with large drooping ears covering its eyes and possesses an extra-long body genetically selected for bacon production?",
                            "options": [
                                "Large White",
                                "Landrace",
                                "Duroc",
                                "Hampshire"
                            ],
                            "answer": "B",
                            "explanation": "The Landrace is a white pig breed from Denmark famous for its exceptionally long cylindrical body (extra ribs) and large drooping ears, making it the premier bacon breed."
                        }
                    },
                    {
                        "type": "knowledge_check",
                        "title": "Summative MCQ 4: Commercial Meat Rabbit Standard",
                        "content": {
                            "question": "Which rabbit breed is pure white with ruby-red albino eyes and possesses the highest meat-to-bone ratio and feed conversion efficiency in commercial cuniculture?",
                            "options": [
                                "California",
                                "Flemish Giant",
                                "New Zealand White",
                                "Angora"
                            ],
                            "answer": "C",
                            "explanation": "The New Zealand White is the international gold standard for commercial meat rabbit production due to its pure white coat, ruby-red eyes, rapid growth rate, and high meat dress-out percentage."
                        }
                    }
                ],
                [
                    {
                        "type": "knowledge_check",
                        "title": "Summative MCQ 5: Self-Shedding Mutton Sheep Breed",
                        "content": {
                            "question": "Which sheep breed is characterized by a solid white body with a jet-black head and possesses a self-shedding hair-wool coat that eliminates the need for manual shearing in dry rangelands?",
                            "options": [
                                "Merino",
                                "Dorper",
                                "Corriedale",
                                "Red Masai"
                            ],
                            "answer": "B",
                            "explanation": "The Dorper is a South African mutton breed developed for arid rangelands. It is instantly recognized by its black head and white body, and its hair-wool coat sheds naturally in spring without shearing."
                        }
                    },
                    {
                        "type": "knowledge_check",
                        "title": "Summative MCQ 6: Premier Commercial Meat Goat",
                        "content": {
                            "question": "Which goat breed, developed in South Africa, is recognized by a white body and dark reddish-brown head and neck, producing heavy, fast-growing muscular carcasses?",
                            "options": [
                                "Saanen",
                                "Toggenburg",
                                "Boer",
                                "Galla"
                            ],
                            "answer": "C",
                            "explanation": "The Boer goat is the premier commercial meat breed globally, known for its heavy muscling, rapid growth rate, and distinctive white body with a dark reddish-brown head."
                        }
                    }
                ],
                [
                    {
                        "type": "knowledge_check",
                        "title": "Summative MCQ 7: Tropical Bos indicus Thermoregulation",
                        "content": {
                            "question": "What is the primary biological function of the extensive loose dewlap folds and large pendulous ears in tropical Bos indicus cattle?",
                            "options": [
                                "To store drinking water for long droughts",
                                "To increase body surface area with high capillary networks, facilitating rapid radiative and evaporative heat loss to prevent hyperthermia in hot environments",
                                "To camouflage against predators in dense forests",
                                "To synthesize synthetic nitrogen fertilizer"
                            ],
                            "answer": "B",
                            "explanation": "The loose skin of the dewlap and the large pendulous ears increase body surface area, acting as biological radiators to dissipate excess metabolic heat in tropical climates."
                        }
                    },
                    {
                        "type": "knowledge_check",
                        "title": "Summative MCQ 8: The Productivity Equation Application",
                        "content": {
                            "question": "In the foundational equation 'Productivity = Genetics x Environment', what occurs if a farmer purchases an exotic dairy cow with 35-liter genetic potential but feeds it poor dry brush in a hot, tick-infested semi-desert pasture?",
                            "options": [
                                "The cow will produce 70 liters of milk to compensate for the heat",
                                "The cow will fail to express its genetic potential, producing minimal milk, and will likely suffer severe disease breakdown, emaciation, or mortality",
                                "The cow's DNA will turn into camel DNA within one week",
                                "The cow will produce pure butter directly from its udder"
                            ],
                            "answer": "B",
                            "explanation": "High genetic potential cannot be expressed without a supportive environment. Under inadequate feed, high heat, and tick exposure, an exotic cow will suffer severe stress, produce minimal milk, and rapidly break down with disease."
                        }
                    }
                ],
                # Page 8: Capstone Summary
                [
                    {
                        "type": "summary",
                        "title": "Topic 8 Capstone Summary: Breeds of Livestock Mastery",
                        "content": {
                            "title": "Mastery Overview: Grade 10 Breeds of Livestock & Animal Genetics",
                            "text": "Congratulations on mastering **Topic 8: Breeds of Livestock**!\n\nYou have mastered:\n- **Breed Principles & Genetics**: Homogeneous phenotypes, selective breeding, single/dual/multi-purpose utility.\n- **Dairy Cattle**: Friesian (Volume King), Jersey (Butterfat 5.5%), Ayrshire (Hardy Forager), Guernsey (Golden Beta-Carotene Milk).\n- **Beef Cattle**: Boran (Tropical Zebu), Brahman (Heat Radiator), Aberdeen Angus (Marbled Steak), Hereford (Docile White Face), Sahiwal (Dual-purpose).\n- **Pig Breeds**: Large White (Erect ears), Landrace (Drooping ears, bacon length), Duroc (Mahogany sire), Hampshire (White shoulder belt).\n- **Rabbit Breeds**: New Zealand White (Meat champion, pink eyes), California (Dark points), Flemish Giant (10–12 kg), Angora (Luxury Wool).\n- **Sheep Breeds**: Merino (Fine crimp wool), Corriedale (Dual-purpose), Dorper (Black head, self-shedding), Red Masai (Genetic worm resistance).\n- **Goat Breeds**: Boer (Meat champion), Galla (Arid indigenous), Saanen (Volume milker), Toggenburg (Face stripes), Nubian (Roman nose, high fat).\n- **Comparative Anatomy**: Humped *Bos indicus* vs Humpless *Bos taurus*, vascular ears, solar reflectance.\n- **The Master Equation**: $\\text{Productivity} = \\text{Genetics} \\times \\text{Environment}$."
                        }
                    },
                    {
                        "type": "key_takeaway",
                        "title": "Topic 8 Final Takeaway",
                        "content": {
                            "title": "The Livestock Breeding Maxim",
                            "text": "Never evaluate an animal by physical beauty alone; match breed genetics to your agro-ecological climate and feed budget to unlock sustainable, profitable animal enterprise productivity."
                        }
                    }
                ]
            ]
        }
    ]

@transaction.atomic
def ingest_grade10_topic8(replace=False):
    """Executes the complete production ingestion of Grade 10 Agriculture Topic 8: Breeds of Livestock."""
    print("=" * 80)
    print("STARTING INGESTION: CBC Grade 10 Agriculture — Topic 8: Breeds of Livestock")
    print("=" * 80)

    curriculum = Curriculum.objects.filter(name__iexact="CBC").first()
    grade = Grade.objects.filter(curriculum=curriculum, name__icontains="10").first()
    subject = Subject.objects.filter(grade=grade, name__iexact="Agriculture").first()

    assert curriculum and grade and subject, "Curriculum/Grade/Subject not found!"

    topic_name = "Breeds of Livestock"
    topic = Topic.objects.filter(subject=subject, name=topic_name).first()
    if not topic:
        topic = Topic.objects.create(
            subject=subject,
            name=topic_name,
            description="Comprehensive theoretical, phenotypic, and genetic study of livestock breeds: dairy and beef cattle, commercial pigs, meat/wool rabbits, sheep, goats, comparative anatomy, and the Productivity = Genetics x Environment framework.",
            order=8
        )
        print(f"Created Topic 8: {topic.name} (ID: {topic.id})")
    else:
        topic.order = 8
        topic.description = "Comprehensive theoretical, phenotypic, and genetic study of livestock breeds: dairy and beef cattle, commercial pigs, meat/wool rabbits, sheep, goats, comparative anatomy, and the Productivity = Genetics x Environment framework."
        topic.save()
        print(f"Resolved Topic 8: {topic.name} (ID: {topic.id})")

    if replace:
        print("Flag --replace active: Clearing existing LearningUnits and Lessons for Topic 8...")
        topic.learning_units.all().delete()
        topic.lessons.all().delete()

    curriculum_data = build_topic8_curriculum()
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
                    "topic_order": 8,
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
                    block_id=f"g10_agri_t8_u{u_order}_p{page_idx}_b{comp_idx}",
                    block_type=b_type,
                    component_type=b_type,
                    title=b_title,
                    content=b_content,
                    order=block_order_counter,
                    page_number=page_idx,
                    component_order=comp_idx,
                    page_title=b_title if comp_idx == 1 else None,
                    metadata={"topic_order": 8, "unit_order": u_order, "page": page_idx}
                )
                block_order_counter += 1
                total_blocks += 1

        print(f"  Ingested Unit {u_order}: {u_name} -> Lesson '{l_title}' ({len(pages)} Pages, {block_order_counter - 1} Blocks)")

    print("=" * 80)
    print(f"INGESTION COMPLETE: Topic 8 '{topic.name}'")
    print(f"  Total Units:   {total_units}")
    print(f"  Total Lessons: {total_lessons}")
    print(f"  Total Pages:   {total_pages}")
    print(f"  Total Blocks:  {total_blocks}")
    print("=" * 80)

if __name__ == "__main__":
    replace_flag = "--replace" in sys.argv
    ingest_grade10_topic8(replace=replace_flag)
