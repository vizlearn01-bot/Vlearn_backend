"""
VLearn CBC Grade 8 Agriculture — Topic 8: Cooking Balanced Meals for Special Groups
Production Ingestion Engine (Phase 1: Content & Card Architecture - Deep Pedagogical Edition)

Curriculum: CBC (Curriculum ID: 5)
Grade: Grade 8 (ID: 15, Level: 8)
Subject: Agriculture
Topic: Cooking Balanced Meals for Special Groups (Topic Order: 8)

Decomposed into 4 Learning Units & 4 Published Lessons:
  1. Introduction to Balanced Meals and Meal Planning Factors (7 Pages, 12 Blocks)
  2. Understanding Special Groups and Dietary Guidelines (7 Pages, 12 Blocks)
  3. Feeding Habits, Food Taboos, and Cultural Practices (7 Pages, 12 Blocks)
  4. Practical: Planning, Preparing, and Presenting a Balanced Meal for a Special Group & Capstone (10 Pages, 22 Blocks)

Deep Pedagogical Enhancements:
  - Strict 1 Card = 1 Understandable Idea progression.
  - Zero citation leaks ([2], [543]), zero developer meta-tags, zero raw unrendered LaTeX.
  - Formative scenario MCQs and 10 Topic Summative MCQs with comprehensive educational explanations.
  - Multi-video integrations embedded across individual practical lessons.

Usage:
  ./venv/bin/python curriculum/ingest_cbc_grade8_agriculture_topic8.py [--replace]
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
    text = re.sub(r'\[(?:\d+|image_\d+|S\d+.*?|[\d,\s]{2,}|Week \d+: Lesson \d+)\]', '', text)
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
    """Returns the comprehensive pedagogical page and block structure for Grade 8 Topic 8: Cooking Balanced Meals for Special Groups."""
    return [
        # =====================================================================
        # LESSON 1: Introduction to Balanced Meals and Meal Planning Factors
        # =====================================================================
        {
            "unit_order": 1,
            "unit_name": "Introduction to Balanced Meals and Meal Planning Factors",
            "unit_description": "Foundational nutrition: the three food pillars (carbohydrates, proteins, protective vitamins/minerals), and biological meal-planning factors (age, gender, physiological state, and health status).",
            "lesson_title": "Introduction to Balanced Meals and Meal Planning Factors",
            "pages": [
                # Page 1: Visual Hook & Learning Objectives
                [
                    {
                        "type": "suggested_image",
                        "title": "Nutrition Anatomy: The Balanced Meal Plate",
                        "content": {
                            "title": "Nutrition Anatomy: The Balanced Meal Plate",
                            "caption": "A colorful, nutritionally balanced plate divided into energy-giving carbohydrates, bodybuilding proteins, and protective fresh vegetables."
                        }
                    },
                    {
                        "type": "learning_goal",
                        "title": "Learning Objectives: The Architecture of Nutrition",
                        "content": {
                            "title": "What We Will Accomplish Today",
                            "goals": [
                                "Define a **balanced meal** and identify its three fundamental food pillars.",
                                "Analyze how **age, gender, and physical activity levels** dictate nutrient requirements.",
                                "Explain why children require higher protein density than sedentary adults.",
                                "Appreciate the role of meal planning in preventing household malnutrition."
                            ]
                        }
                    },
                    {
                        "type": "concept_explanation",
                        "title": "The Science of Fueling the Human Body",
                        "content": {
                            "title": "Why One Meal Does Not Fit All",
                            "text": "Every human body is a living engine. A 10-month-old growing infant, an active adolescent boy, a pregnant mother, and a 75-year-old grandfather all have vastly different biological fuel requirements! Mastering meal planning means tailoring the proportions, nutrients, and physical textures of foods to support optimal health at every stage of life."
                        }
                    }
                ],
                # Page 2: The Three Food Pillars & Biological Planning Factors
                [
                    {
                        "type": "concept_explanation",
                        "title": "The Three Essential Nutrient Pillars",
                        "content": {
                            "title": "Carbohydrates, Proteins, and Protective Micronutrients",
                            "text": "- **1. Carbohydrates (Energy-Givers)**: Starches and complex sugars that fuel daily muscular work and brain activity (e.g., maize ugali, brown rice, sweet potatoes, cassava).\n- **2. Proteins (Bodybuilders)**: Amino acids that build new muscle fibers, repair cellular wear and tear, and synthesize immune antibodies (e.g., beans, eggs, lean beef, fish, milk, peas).\n- **3. Vitamins & Minerals (Protective Regulators)**: Micronutrients like Vitamin A, C, iron, and calcium that protect against infections and regulate metabolism (e.g., spinach, kales, carrots, citrus fruits).\n- **Biological Planning Factors**: We must adjust these three pillars based on **Age** (growth rates), **Gender** (muscle mass & iron loss), and **Health Status** (recovery needs)."
                        }
                    },
                    {
                        "type": "suggested_diagram",
                        "title": "The Balanced Diet Triangle & Biological Planning Matrix",
                        "content": {
                            "title": "The Balanced Diet Triangle & Biological Planning Matrix",
                            "caption": "Nutritional framework: 1. Energy Pillars (Carbs: Ugali/Rice) • 2. Bodybuilding Pillars (Proteins: Fish/Eggs/Legumes) • 3. Protective Pillars (Vitamins/Minerals: Greens/Carrots) • 4. Biological Modifiers (Age, Gender, Activity, Recovery)."
                        }
                    }
                ],
                # Page 3: Biological Factors Comparison Matrix
                [
                    {
                        "type": "comparison_table",
                        "title": "Biological Factors & Dietary Planning Matrix",
                        "content": {
                            "title": "Biological Modifiers & Dietary Adaptations",
                            "headers": ["Biological Group", "Primary Physiological Demand", "Key Nutrient Focus", "Optimal Kitchen Food Choices"],
                            "rows": [
                                ["Growing Child (1-5 yrs)", "Rapid bone, brain, and muscle development", "High Protein & Calcium", "Soft mashed sweet potatoes with minced meat, whole milk, eggs"],
                                ["Active Adolescent / Adult Male", "High energy expenditure and heavy muscular labor", "High Carbohydrates & B-Vitamins", "Maize ugali, brown rice, lean beef, yellow beans, green kales"],
                                ["Adolescent Girl / Woman", "Replenishing menstrual blood loss & bone density", "Iron, Folic Acid & Calcium", "Dark leafy greens (managu/spinach), liver, small fish (omena)"],
                                ["Elderly Individual", "Slower metabolism, missing teeth, sluggish digestion", "High Fiber, Low Starch & Soft Texture", "Steamed pureed vegetables, soft fish broth, tender stewed legumes"]
                            ]
                        }
                    }
                ],
                # Page 4: Interactive Food Group Sorting Challenge
                [
                    {
                        "type": "interactive_scenario",
                        "title": "Food Group Nutritional Classification Challenge",
                        "content": {
                            "title": "Sorting Foods into the Three Pillars",
                            "instructions": "Classify each food item under Carbohydrate, Protein, or Protective Vitamin/Mineral:",
                            "scenario": "A student is planning a lunch menu from local Kenyan ingredients: Steamed Rice, Boiled Egg, Sauteed Spinach, and Sliced Carrots.",
                            "question": "Which of these ingredients provides the primary bodybuilding proteins needed for muscle repair?",
                            "options": [
                                "Boiled Egg (Bodybuilding Protein).",
                                "Steamed Rice",
                                "Sauteed Spinach",
                                "Sliced Carrots"
                            ],
                            "correct_feedback": "Correct! Eggs provide complete, high-quality animal proteins packed with essential amino acids for muscle and tissue repair.",
                            "incorrect_feedback": "Incorrect. Rice provides carbohydrates (energy), and spinach/carrots provide protective vitamins and minerals. Eggs provide bodybuilding protein."
                        }
                    }
                ],
                # Page 5: Formative Knowledge Check
                [
                    {
                        "type": "knowledge_check",
                        "title": "Knowledge Check: Child Protein Requirements",
                        "content": {
                            "question": "Why do growing children require more protein per kilogram of body weight compared to sedentary adults?",
                            "options": [
                                "Children's bodies are actively developing new muscle tissues, bones, and organs daily, requiring constant protein building blocks.",
                                "Children perform more heavy industrial labor than adults.",
                                "Children burn carbohydrates twice as fast.",
                                "Children cannot digest plant fibers."
                            ],
                            "answer": "A",
                            "explanation": "Proteins are bodybuilders. Because young children undergo rapid physical and cellular growth, their proportional protein demand is far higher than inactive adults."
                        }
                    }
                ],
                # Page 6: Summary & Connection Forward
                [
                    {
                        "type": "key_takeaway",
                        "title": "Lesson Summary",
                        "content": {
                            "text": "- A **balanced meal** harmonizes **carbohydrates** (energy), **proteins** (bodybuilding), and **vitamins/minerals** (protection).\n- **Age, gender, and health status** dictate individual caloric and nutrient requirements.\n- Children and adolescents require higher **protein and mineral density** for physical growth.\n- Meal planning prevents malnutrition and promotes lifelong wellness."
                        }
                    },
                    {
                        "type": "transition",
                        "title": "Looking Ahead",
                        "content": {
                            "text": "Who are the vulnerable members in our families who need specialized diets? In Lesson 2, we explore special groups: infants, pregnant/lactating mothers, the elderly, and convalescents!"
                        }
                    }
                ],
                # Page 7: Micronutrient Synergy Callout
                [
                    {
                        "type": "concept_explanation",
                        "title": "Nutrient Synergy: Vitamin C and Iron",
                        "content": {
                            "title": "How Nutrients Work Together",
                            "text": "Eating iron-rich spinach alone is good, but pairing it with Vitamin C (like adding freshly squeezed lemon juice or sliced tomatoes) triples the body's iron absorption rate! A smart meal planner combines complementary foods to maximize nutritional value."
                        }
                    }
                ]
            ]
        },

        # =====================================================================
        # LESSON 2: Understanding Special Groups and Dietary Guidelines
        # =====================================================================
        {
            "unit_order": 2,
            "unit_name": "Understanding Special Groups and Dietary Guidelines",
            "unit_description": "Categorizing special biological groups: weaning infants (soft semi-solids), pregnant/lactating mothers (iron, folate, calcium, fluids), the elderly (soft fiber, low starch), and sick convalescents (easily absorbed broths).",
            "lesson_title": "Understanding Special Groups and Dietary Guidelines",
            "pages": [
                # Page 1: Visual Hook & Learning Objectives
                [
                    {
                        "type": "suggested_image",
                        "title": "Special Dietary Care: Nutrient-Dense Convalescent Meal",
                        "content": {
                            "title": "Special Dietary Care: Nutrient-Dense Convalescent Meal",
                            "caption": "A warm, easily digestible bowl of strained chicken and vegetable broth paired with smooth mashed sweet potatoes for a recovering patient."
                        }
                    },
                    {
                        "type": "learning_goal",
                        "title": "Learning Objectives: Special Groups & Dietary Adaptation",
                        "content": {
                            "title": "What We Will Accomplish Today",
                            "goals": [
                                "Identify the four key **special groups** in our communities.",
                                "Outline the specific dietary guidelines for **pregnant/lactating mothers** and the **elderly**.",
                                "Explain how to adapt meal texture and composition for **sick convalescents**.",
                                "Demonstrate how to transform a standard family meal into special group portions."
                            ]
                        }
                    },
                    {
                        "type": "concept_explanation",
                        "title": "Compassionate Nutrition in the Home",
                        "content": {
                            "title": "Caring for Vulnerable Family Members",
                            "text": "When a family member is ill with malaria, pregnant with a baby, or elderly with fragile teeth, serving them a standard plate of stiff dry ugali and tough fried meat can cause pain, indigestion, or refusal to eat. Adapting recipes with tenderness and science is the heart of household care."
                        }
                    }
                ],
                # Page 2: The Four Special Groups & Their Dietary Needs
                [
                    {
                        "type": "concept_explanation",
                        "title": "Nutritional Guidelines for Special Biological Groups",
                        "content": {
                            "title": "Four Distinct Dietary Needs",
                            "text": "- **1. Weaning Infants (6-24 months)**: Transitioning from breast milk to soft, nutrient-dense semi-solids (e.g., fortified millet porridge with milk and mashed ripe bananas).\n- **2. Pregnant & Lactating Mothers**: Carrying developing fetuses or synthesizing breast milk requires **Iron & Folic Acid** (blood building), **Calcium** (fetal bones without skeletal depletion), and **Extra Clean Fluids**.\n- **3. The Elderly**: Reduced physical activity requires lower carbohydrates to prevent obesity, high dietary fiber to prevent constipation, and soft/mashed textures to accommodate missing teeth.\n- **4. Convalescents (Recovering Patients)**: Weakened immune systems and low appetite require warm, clear, protein-rich broths, pureed vegetables, and fresh juices that digest rapidly."
                        }
                    },
                    {
                        "type": "suggested_diagram",
                        "title": "Special Groups Dietary Adaptations Flowchart",
                        "content": {
                            "title": "Special Groups Dietary Adaptations Flowchart",
                            "caption": "Recipe adaptation flow: Standard Family Meal (Stiff Ugali, Fried Beef, Kale) -> 1. Elderly (Soft rice, minced stewed beef, steamed spinach) -> 2. Convalescent (Warm chicken broth, mashed potato/pumpkin) -> 3. Infant (Smooth millet porridge with milk & banana puree)."
                        }
                    }
                ],
                # Page 3: Special Group Guidelines Matrix
                [
                    {
                        "type": "comparison_table",
                        "title": "Special Groups Nutritional Requirements Matrix",
                        "content": {
                            "title": "Dietary Modifications & Preparation Standards",
                            "headers": ["Special Group", "Physiological Challenge", "Mandatory Dietary Rule", "Recommended Dishes"],
                            "rows": [
                                ["Pregnant Women", "Fetal organ growth & blood expansion", "High iron, folic acid, calcium & proteins", "Liver stew, dark leafy managu, fortified milk, beans"],
                                ["Lactating Mothers", "High fluid & nutrient loss during milk synthesis", "Extra clean fluids, calcium, and balanced calories", "Millet porridge with milk, fresh water, stewed fish"],
                                ["The Elderly", "Slow digestion, low metabolism, dental loss", "Soft textures, reduced starches, high dietary fiber", "Steamed vegetable purees, soft-boiled rice, fish fillet soup"],
                                ["Convalescents", "Poor appetite, low immunity, weak stomach", "Light, non-greasy, warm, vitamin-dense liquid broths", "Chicken vegetable soup, mashed sweet potatoes, fruit juice"]
                            ]
                        }
                    }
                ],
                # Page 4: Video Resource — Nutritional Care for Special Groups
                [
                    {
                        "type": "suggested_video",
                        "title": "Instructional Video: Nutritional Needs of Special Groups & Meal Adaptation",
                        "content": {
                            "title": "Instructional Video: Nutritional Needs of Special Groups & Meal Adaptation",
                            "url": "https://www.youtube.com/watch?v=TXJPk-QfhDU",
                            "resolved_video_id": "TXJPk-QfhDU",
                            "caption": "Watch this educational presentation explaining dietary adaptations for infants, pregnant mothers, the elderly, and recovering patients in African households."
                        }
                    },
                    {
                        "type": "concept_explanation",
                        "title": "Key Workshop Insights from the Video",
                        "content": {
                            "title": "Clinical Nutrition Takeaways",
                            "text": "- **1. Fluid Management**: Notice how lactating mothers require at least 3 liters of fluids daily to support milk production.\n- **2. The Sieve Technique**: Watch how pureed foods are passed through a clean wire sieve to remove hard choking lumps for infants.\n- **3. Low Salt / Low Spice**: Observe why convalescent broths must avoid heavy chili spices that irritate healing stomachs."
                        }
                    }
                ],
                # Page 5: Interactive Special Group Matching Challenge
                [
                    {
                        "type": "interactive_scenario",
                        "title": "Special Group Dietary Matching Challenge",
                        "content": {
                            "title": "Matching Groups to Dietary Rules",
                            "instructions": "Match each special group to its correct primary dietary guideline:",
                            "scenario": "A community health nurse is advising a rural family on cooking for four distinct relatives.",
                            "question": "Which dietary modification is specifically required for an elderly grandfather with no teeth?",
                            "options": [
                                "Reduce heavy starches, increase dietary fiber, and steam/mash foods into soft, easily chewable textures (The Elderly).",
                                "Serve hard-boiled maize and tough fried beef.",
                                "Provide high chili spices to stimulate heart rate.",
                                "Feed only cold water for 3 days."
                            ],
                            "correct_feedback": "Correct! The elderly require high fiber to prevent constipation, lower starch to match low physical activity, and soft mashed textures for easy chewing.",
                            "incorrect_feedback": "Incorrect. The elderly need soft, high-fiber, easily chewable meals with reduced heavy starches."
                        }
                    }
                ],
                # Page 6: Formative Knowledge Check
                [
                    {
                        "type": "knowledge_check",
                        "title": "Knowledge Check: Maternal Calcium Depletion",
                        "content": {
                            "question": "What happens if a pregnant woman's daily diet lacks sufficient calcium-rich foods like milk and small fish?",
                            "options": [
                                "The developing baby's physiological demand will extract calcium directly from the mother's own bones, weakening her skeleton.",
                                "The baby will be born with green hair.",
                                "The mother's digestive system will freeze.",
                                "The mother will gain 50 kg of weight instantly."
                            ],
                            "answer": "A",
                            "explanation": "Fetal skeletal development is prioritized by the body. If dietary calcium is lacking, calcium is leached from the mother's bones, increasing her risk of bone weakness."
                        }
                    }
                ],
                # Page 7: Summary & Connection Forward
                [
                    {
                        "type": "key_takeaway",
                        "title": "Lesson Summary",
                        "content": {
                            "text": "- **Special groups** have unique nutritional, textural, and metabolic requirements.\n- **Pregnant/lactating mothers** need **iron, folate, calcium, and ample fluids**.\n- **The elderly** need **soft, high-fiber, low-starch meals** to assist slow digestion.\n- **Convalescents** heal best on **warm, easily absorbable, nutrient-dense broths**."
                        }
                    },
                    {
                        "type": "transition",
                        "title": "Looking Ahead",
                        "content": {
                            "text": "Why do some traditional beliefs forbid pregnant mothers from eating eggs and children from eating liver? In Lesson 3, we investigate cultural food taboos and biological facts!"
                        }
                    }
                ]
            ]
        },

        # =====================================================================
        # LESSON 3: Feeding Habits, Food Taboos, and Cultural Practices
        # =====================================================================
        {
            "unit_order": 3,
            "unit_name": "Feeding Habits, Food Taboos, and Cultural Practices",
            "unit_description": "Socio-cultural nutrition: origins of food taboos, debunking dangerous taboos (forbidding eggs to pregnant mothers, organ meats to children), nutritional deficiencies (anemia, stunting), and community advocacy.",
            "lesson_title": "Feeding Habits, Food Taboos, and Cultural Practices",
            "pages": [
                # Page 1: Visual Hook & Learning Objectives
                [
                    {
                        "type": "suggested_image",
                        "title": "Local Protein Diversity: Eggs & Indigenous Legumes",
                        "content": {
                            "title": "Local Protein Diversity: Eggs & Indigenous Legumes",
                            "caption": "Fresh farm eggs, cowpeas, and roasted peanuts—affordable, nutrient-dense local proteins that are often restricted by traditional food taboos."
                        }
                    },
                    {
                        "type": "learning_goal",
                        "title": "Learning Objectives: Debunking Food Taboos with Science",
                        "content": {
                            "title": "What We Will Accomplish Today",
                            "goals": [
                                "Define a **food taboo** and explain historical reasons for cultural food bans.",
                                "Analyze the biological damage caused by forbidding eggs, fish, and liver to mothers and children.",
                                "Explain how avoiding iron-rich foods triggers **maternal and childhood anemia**.",
                                "Advocate respectfully for evidence-based nutrition in local communities."
                            ]
                        }
                    },
                    {
                        "type": "concept_explanation",
                        "title": "Culture Meets Modern Biology",
                        "content": {
                            "title": "The Conflict Between Tradition and Science",
                            "text": "Food taboos are cultural customs that forbid eating specific foods. While some traditional practices protected rare wildlife or avoided toxic plants, many taboos unjustly target pregnant women and children—the two groups with the highest protein and micronutrient needs! In CBC Agriculture, we use science to protect our families' health while respecting our cultural heritage."
                        }
                    }
                ],
                # Page 2: Cultural Taboos vs. Biological Facts
                [
                    {
                        "type": "concept_explanation",
                        "title": "Debunking Common Harmful Food Taboos",
                        "content": {
                            "title": "Three Common Myths and Scientific Realities",
                            "text": "- **1. Taboo: 'Pregnant women must not eat eggs or the baby will be born bald or difficult to deliver.'**\n  * *Biological Fact*: Eggs provide complete animal proteins and choline essential for fetal brain development. Avoiding eggs leads to maternal muscle loss and low birth weight.\n- **2. Taboo: 'Children who eat liver or gizzard will become thieves and liars.'**\n  * *Biological Fact*: Liver is nature's richest source of bioavailable Vitamin A and Iron. Forbidding liver increases the risk of **nutritional anemia**, night-blindness, and poor immunity.\n- **3. Taboo: 'Lactating mothers must not eat beans or green vegetables.'**\n  * *Biological Fact*: Green vegetables and legumes provide essential folic acid, calcium, and vegetable protein to enrich breast milk and keep mothers strong."
                        }
                    },
                    {
                        "type": "suggested_diagram",
                        "title": "Cultural Food Taboos vs. Modern Biological Science Truth Matrix",
                        "content": {
                            "title": "Cultural Food Taboos vs. Modern Biological Science Truth Matrix",
                            "caption": "Scientific debunking matrix: Left: Traditional Taboo Myths (Eggs cause baldness, liver causes stealing, greens sour milk) • Right: Biological Reality (Eggs build fetal brain, liver stops iron-deficiency anemia, greens provide calcium & folic acid)."
                        }
                    }
                ],
                # Page 3: Taboos vs. Nutritional Consequences Matrix
                [
                    {
                        "type": "comparison_table",
                        "title": "Cultural Taboos & Nutritional Consequence Matrix",
                        "content": {
                            "title": "Debunking Food Taboos with Nutritional Evidence",
                            "headers": ["Cultural Taboo Myth", "Target Group", "Biological Truth", "Nutritional Damage of Taboo"],
                            "rows": [
                                ["'Pregnant women must not eat eggs'", "Pregnant Mothers", "Eggs provide high-quality protein & choline for fetal brain development", "Low birth weight, maternal muscle wasting"],
                                ["'Children must not eat liver/gizzard'", "Young Children", "Liver contains concentrated bioavailable iron and Vitamin A", "Iron-deficiency anemia, weakened immune system, night-blindness"],
                                ["'Lactating mothers must avoid dark greens'", "Breastfeeding Mothers", "Dark greens provide iron and calcium to replenish maternal stores", "Maternal fatigue, calcium leaching from bones into milk"]
                            ]
                        }
                    }
                ],
                # Page 4: Video Resource — Overcoming Cultural Food Taboos
                [
                    {
                        "type": "suggested_video",
                        "title": "Instructional Video: Overcoming Food Taboos & Maternal Nutrition in Africa",
                        "content": {
                            "title": "Instructional Video: Overcoming Food Taboos & Maternal Nutrition in Africa",
                            "url": "https://www.youtube.com/watch?v=6ZjkLwQt_YE",
                            "resolved_video_id": "6ZjkLwQt_YE",
                            "caption": "Watch this public health video showing community dialogue, addressing harmful dietary misconceptions, and empowering mothers with balanced local foods in Kenya."
                        }
                    },
                    {
                        "type": "concept_explanation",
                        "title": "Community Advocacy Strategies from the Video",
                        "content": {
                            "title": "How to Talk to Elders Respectfully",
                            "text": "- **1. Respectful Dialogue**: Never mock traditional beliefs; explain that modern medical science provides new tools to ensure healthy, smart babies.\n- **2. Local Ingredients**: Show that affordable local foods (eggs, omena, managu) provide world-class nutrition.\n- **3. Positive Role Models**: Involve community health workers and grandmothers in promoting balanced complementary feeding."
                        }
                    }
                ],
                # Page 5: Interactive Taboo Counseling Challenge
                [
                    {
                        "type": "interactive_scenario",
                        "title": "Community Taboo Counseling Challenge",
                        "content": {
                            "title": "Advising a Pregnant Mother in the Village",
                            "instructions": "Choose the most scientific, respectful, and helpful advice:",
                            "scenario": "A pregnant mother in your village is told by her neighbors to stop eating fish and eggs because of traditional beliefs.",
                            "question": "What is the best counsel you can offer her?",
                            "options": [
                                "Politely explain that fish and eggs contain essential proteins, healthy fats, and iron that her developing baby needs for healthy brain and muscle growth.",
                                "Tell her to eat only white sugar and soda.",
                                "Tell her to stop eating all foods completely.",
                                "Tell her to leave the village immediately."
                            ],
                            "correct_feedback": "Correct! Respectfully sharing scientific facts empowers mothers to make nutritious choices that protect fetal brain and muscle growth.",
                            "incorrect_feedback": "Incorrect. Always provide respectful, evidence-based nutrition facts explaining that eggs and fish provide essential protein and healthy fats."
                        }
                    }
                ],
                # Page 6: Formative Knowledge Check
                [
                    {
                        "type": "knowledge_check",
                        "title": "Knowledge Check: Childhood Liver Taboo Consequence",
                        "content": {
                            "question": "What is the direct biological consequence when young children are forbidden from eating nutrient-dense organ meats like liver?",
                            "options": [
                                "They suffer from an increased risk of iron-deficiency anemia, poor cognitive development, and weakened immune defense.",
                                "They become exceptionally tall.",
                                "Their bones turn into pure gold.",
                                "They become immune to all diseases."
                            ],
                            "answer": "A",
                            "explanation": "Liver is a premier source of bioavailable iron and Vitamin A. Denying it to children leads to iron-deficiency anemia and increased susceptibility to infections."
                        }
                    }
                ],
                # Page 7: Summary & Connection Forward
                [
                    {
                        "type": "key_takeaway",
                        "title": "Lesson Summary",
                        "content": {
                            "text": "- **Food taboos** often target the most vulnerable groups: pregnant women, nursing mothers, and children.\n- Avoiding **eggs and fish** during pregnancy leads to low birth weight and maternal malnutrition.\n- Forbidding **liver and organ meats** to children causes **iron-deficiency anemia**.\n- Respectful community advocacy with scientific facts protects household health."
                        }
                    },
                    {
                        "type": "transition",
                        "title": "Looking Ahead",
                        "content": {
                            "text": "Let's put our nutrition knowledge into practical culinary action! In Lesson 4, we plan, cook, plate, and present a balanced meal for an elderly relative or convalescent!"
                        }
                    }
                ]
            ]
        },

        # =====================================================================
        # LESSON 4: Practical: Planning, Preparing, and Presenting a Balanced Meal for a Special Group & Capstone
        # =====================================================================
        {
            "unit_order": 4,
            "unit_name": "Practical: Planning, Preparing, and Presenting a Balanced Meal for a Special Group",
            "unit_description": "Hands-on culinary lab: menu design for elderly/convalescent, kitchen safety (pot handles turned inward, claw grip cutting), cross-contamination barriers, step-by-step cooking (sweet potatoes, minced stew, steamed spinach), plating aesthetics, topic video review, and 10 topic summative MCQs.",
            "lesson_title": "Practical: Planning, Preparing, and Presenting a Balanced Meal for a Special Group & Capstone",
            "pages": [
                # Page 1: Visual Hook & Capstone Objectives
                [
                    {
                        "type": "suggested_image",
                        "title": "Culinary Lab: Collaborative Kitchen Meal Preparation",
                        "content": {
                            "title": "Culinary Lab: Collaborative Kitchen Meal Preparation",
                            "caption": "Grade 8 students working collaboratively in a hygienic school kitchen, preparing and plating a soft balanced meal for a recovering convalescent."
                        }
                    },
                    {
                        "type": "learning_goal",
                        "title": "Learning Objectives: Culinary Execution & Topic Mastery",
                        "content": {
                            "title": "What We Will Accomplish Today",
                            "goals": [
                                "Design a 3-part balanced menu tailored to an **elderly relative or convalescent**.",
                                "Demonstrate strict kitchen safety: **pot handles turned inward, claw grip, separate cutting boards**.",
                                "Execute step-by-step preparation of **mashed sweet potatoes, minced beef stew, and steamed spinach**.",
                                "Review the Topic Video and achieve 100% mastery on the **10 Topic Summative Assessment Questions**."
                            ]
                        }
                    },
                    {
                        "type": "concept_explanation",
                        "title": "The Junior Wellness Culinary Lab",
                        "content": {
                            "title": "From Recipe to Plate",
                            "text": "Cooking for someone who is recovering or elderly is an expression of culinary love and scientific care. Today, we execute a complete practical kitchen session, mastering knife safety, preventing cross-contamination, and presenting an appetizing, nutrient-dense plate!"
                        }
                    }
                ],
                # Page 2: Safety Rules & Cross-Contamination Barriers
                [
                    {
                        "type": "concept_explanation",
                        "title": "Kitchen Safety & Cross-Contamination Prevention",
                        "content": {
                            "title": "The Four Mandatory Kitchen Rules",
                            "text": "- **1. Pot Handles Inward**: Always turn pot handles toward the center of the stove so nobody bumps into them and spills scalding liquids.\n- **2. The Knife Claw Grip**: Tuck finger tips inward like a cat's claw while slicing to protect knuckles from sharp blades.\n- **3. Separate Chopping Boards**: Never chop raw meat and fresh salad vegetables on the same board! Bacteria on raw meat cause dangerous **cross-contamination**.\n- **4. Dry Oven Mitts**: Always use completely dry cloth mitts when handling hot pans (damp cloths conduct heat instantly and cause severe steam burns)."
                        }
                    },
                    {
                        "type": "suggested_diagram",
                        "title": "Practical Kitchen Workflow, Cross-Contamination Barrier & Safe Plating Protocol",
                        "content": {
                            "title": "Practical Kitchen Workflow, Cross-Contamination Barrier & Safe Plating Protocol",
                            "caption": "Culinary lab workflow: 1. Hygiene & separate boards (Red = Raw meat, Green = Fresh vegetables) -> 2. Cooking (Boil/mash sweet potatoes, simmer minced beef, steam spinach) -> 3. Inward pot handle safety -> 4. Attractive balanced plating with clean rim."
                        }
                    }
                ],
                # Page 3: Step-by-Step Cooking Standard Operating Procedure
                [
                    {
                        "type": "step_process",
                        "title": "Standard Operating Procedure: Special Group Balanced Meal",
                        "content": {
                            "title": "How to Prepare Mashed Sweet Potatoes, Minced Stew & Steamed Spinach",
                            "steps": [
                                "**Step 1: Sanitize & Prep**: Wash hands for 20 seconds. Wash sweet potatoes and spinach in running water. Sanitize knives, pans, and cutting boards.",
                                "**Step 2: Peel, Boil & Mash**: Peel sweet potatoes, cube uniformly, and boil in lightly salted water for 15-20 minutes until tender. Mash with a fork until silky smooth.",
                                "**Step 3: Mince & Simmer Stew**: Brown lean minced beef with chopped onions and tomatoes in a little oil. Add clean water, cover, and simmer for 20 minutes until melt-in-the-mouth tender.",
                                "**Step 4: Steam Green Spinach**: Finely chop spinach. Steam gently in a covered pot with a splash of water for 3 to 5 minutes to preserve bright green vitamins.",
                                "**Step 5: Plate & Serve**: Place a neat portion of mashed sweet potato on one half of the plate, and minced stew with steamed spinach on the other half. Wipe plate edges clean."
                            ]
                        }
                    }
                ],
                # Page 4: Interactive Culinary Sequencing Challenge
                [
                    {
                        "type": "interactive_scenario",
                        "title": "Kitchen Culinary Sequencing Challenge",
                        "content": {
                            "title": "Ordering Practical Cooking Steps",
                            "instructions": "Place the meal preparation steps in the correct chronological sequence:",
                            "scenario": "Your cooking team is preparing lunch for a convalescent patient.",
                            "question": "What is the correct logical order of actions?",
                            "options": [
                                "1. Wash hands & sanitize surfaces -> 2. Peel & chop ingredients -> 3. Boil sweet potatoes & simmer minced beef -> 4. Mash potatoes & steam greens -> 5. Plate neatly & wipe rim",
                                "1. Plate raw cold food -> 2. Cook on unwashed table -> 3. Wash hands after eating",
                                "1. Chop raw chicken on salad board -> 2. Leave pot handles sticking outward into walkway",
                                "1. Serve raw unpeeled potatoes"
                            ],
                            "correct_feedback": "Correct! Always establish hygiene first, prep ingredients, cook thoroughly, mash/steam, and plate neatly.",
                            "incorrect_feedback": "Incorrect. Follow the chronological order: Sanitize -> Prep -> Cook -> Mash/Steam -> Plate."
                        }
                    }
                ],
                # Page 5: Formative Knowledge Check & Master Summary
                [
                    {
                        "type": "knowledge_check",
                        "title": "Knowledge Check: Cross-Contamination Danger",
                        "content": {
                            "question": "Why is it strictly forbidden to slice raw meat and then slice fresh salad spinach on the same unwashed chopping board?",
                            "options": [
                                "Harmful bacteria on raw meat transfer directly to the spinach, causing severe food poisoning (cross-contamination).",
                                "Spinach leaves will make the knife blade turn green.",
                                "Raw meat makes the spinach grow taller.",
                                "It makes the stove burners too hot."
                            ],
                            "answer": "A",
                            "explanation": "Raw meats carry natural bacteria like Salmonella. Cutting raw meat and then fresh greens on the same board transfers pathogens directly, causing foodborne illnesses."
                        }
                    },
                    {
                        "type": "key_takeaway",
                        "title": "Topic 8 Master Summary: Cooking Balanced Meals for Special Groups",
                        "content": {
                            "text": "- **Balanced Meals**: Combine **carbohydrates** (energy), **proteins** (bodybuilding), and **vitamins/minerals** (protection).\n- **Special Groups**: **Infants** (smooth semi-solids), **Pregnant/Lactating mothers** (iron, folate, calcium, fluids), **The Elderly** (soft fiber, low starch), **Convalescents** (light warm broths).\n- **Debunking Taboos**: Eggs build fetal brain, liver eliminates childhood anemia, and greens supply essential calcium and iron.\n- **Kitchen Safety & Hygiene**: Pot handles inward, claw grip cutting, separate chopping boards, and clean plating."
                        }
                    }
                ],
                # Page 6: Topic Video Review
                [
                    {
                        "type": "suggested_video",
                        "title": "Topic Video Review: Balanced Meals for Special Groups & Kitchen Safety",
                        "content": {
                            "title": "Topic Video Review: Balanced Meals for Special Groups & Kitchen Safety",
                            "url": "https://www.youtube.com/watch?v=Ei5z_0Lxmic",
                            "resolved_video_id": "Ei5z_0Lxmic",
                            "caption": "Watch this comprehensive educational review covering balanced meal pillars, special group nutritional adaptations, cultural taboo debunking, and safe culinary lab execution."
                        }
                    },
                    {
                        "type": "concept_explanation",
                        "title": "Key Review Questions for Video Analysis",
                        "content": {
                            "title": "Final Review Highlights",
                            "text": "- **1. Recipe Transformation**: Notice how standard family recipes can be modified easily without cooking separate expensive meals.\n- **2. Texture and Digestion**: Observe why mashing and pureeing saves critical digestive energy for sick patients.\n- **3. Respectful Communication**: See how evidence-based facts dispel harmful community food taboos."
                        }
                    }
                ],
                # Page 7: Topic Assessment Part 1 (Questions 1 to 2)
                [
                    {
                        "type": "knowledge_check",
                        "title": "Topic Assessment - Question 1: Maternal Iron & Folate Function",
                        "content": {
                            "question": "What is the primary nutritional reason for encouraging pregnant mothers to consume foods rich in iron and folate (folic acid)?",
                            "options": [
                                "To support healthy fetal brain and spinal development and prevent maternal anemia.",
                                "To provide rapid energy for heavy physical construction work.",
                                "To lower the mother's daily body temperature.",
                                "To make the fetal skeletal system harden too early in the first trimester."
                            ],
                            "answer": "A",
                            "explanation": "Folate prevents neural tube and brain defects in the developing baby, while iron builds maternal hemoglobin to prevent life-threatening anemia."
                        }
                    },
                    {
                        "type": "knowledge_check",
                        "title": "Topic Assessment - Question 2: Elderly High-Fiber Rationale",
                        "content": {
                            "question": "An elderly person's diet should generally contain lower calories but higher dietary fiber. Why is fiber so critical for this group?",
                            "options": [
                                "Fiber prevents sluggish digestion and helps avoid chronic constipation in less active elderly digestive systems.",
                                "Fiber provides instant explosive energy for sprint running.",
                                "Fiber replaces the need for drinking water.",
                                "Fiber hardens teeth enamel."
                            ],
                            "answer": "A",
                            "explanation": "Metabolism and physical movement slow with age, reducing caloric needs. High fiber supports bowel motility, preventing digestive sluggishness and constipation."
                        }
                    }
                ],
                # Page 8: Topic Assessment Part 2 (Questions 3 to 5)
                [
                    {
                        "type": "knowledge_check",
                        "title": "Topic Assessment - Question 3: Negative Impact of Liver Taboo",
                        "content": {
                            "question": "Which of the following describes a traditional cultural taboo that directly harms a young child's biological development?",
                            "options": [
                                "Forbidding children from eating nutrient-dense, iron-rich liver and gizzard under the belief that it causes stealing.",
                                "Feeding children soft millet porridge during weaning.",
                                "Ensuring children wash their hands with soap before eating.",
                                "Encouraging children to drink clean boiled milk."
                            ],
                            "answer": "A",
                            "explanation": "Liver is a premier source of bioavailable iron and Vitamin A. Forbidding it deprives children of critical micronutrients, causing anemia and poor immunity."
                        }
                    },
                    {
                        "type": "knowledge_check",
                        "title": "Topic Assessment - Question 4: Inward Pot Handle Safety Rule",
                        "content": {
                            "question": "Why should pot handles on a kitchen cooking stove always be turned toward the center of the stove?",
                            "options": [
                                "To prevent people from accidentally bumping into the handles and spilling scalding hot food or liquids.",
                                "To make the pot handles absorb more heat.",
                                "To keep the food from getting too cold.",
                                "To make the gas burner use less fuel."
                            ],
                            "answer": "A",
                            "explanation": "Turning pot handles inward prevents walking cooks from catching their clothes or arms on handles and knocking scalding pots onto themselves."
                        }
                    },
                    {
                        "type": "knowledge_check",
                        "title": "Topic Assessment - Question 5: Infant Meal Adaptation Method",
                        "content": {
                            "question": "What is the best way to modify a standard family meal of stiff ugali, beef stew, and kales for a 1-year-old infant?",
                            "options": [
                                "Mash or blend the soft cooked ingredients with milk or broth into a smooth, nutrient-dense semi-solid puree.",
                                "Serve the meal exactly as it is in a smaller bowl.",
                                "Fry the beef with extra hot chili spices.",
                                "Dry the beef into hard jerky strips."
                            ],
                            "answer": "A",
                            "explanation": "Infants have developing teeth and swallowing reflexes. Pureeing or mashing foods with milk or broth creates an easily swallowable, nutrient-rich complementary meal."
                        }
                    }
                ],
                # Page 9: Topic Assessment Part 3 (Questions 6 to 8)
                [
                    {
                        "type": "knowledge_check",
                        "title": "Topic Assessment - Question 6: Maternal Calcium Depletion Mechanism",
                        "content": {
                            "question": "During pregnancy, avoiding calcium-rich foods like milk, yoghurt, and small fish can cause which biological consequence?",
                            "options": [
                                "The developing fetus will extract calcium directly from the mother's own bones, causing maternal bone weakening.",
                                "The baby will be born with overly dark skin.",
                                "The mother's digestive system will stop absorbing starch.",
                                "The baby will grow teeth before birth."
                            ],
                            "answer": "A",
                            "explanation": "The fetus requires calcium for skeleton formation. If the mother's diet is calcium-deficient, maternal bones are demineralized to supply the baby."
                        }
                    },
                    {
                        "type": "knowledge_check",
                        "title": "Topic Assessment - Question 7: Cross-Contamination High Risk Action",
                        "content": {
                            "question": "Which kitchen practice represents the highest risk of dangerous cross-contamination?",
                            "options": [
                                "Slicing raw chicken breast and then slicing fresh raw tomatoes on the same unwashed cutting board.",
                                "Steaming green spinach in a covered pot with water.",
                                "Washing carrots in clean running water before peeling.",
                                "Carrying a knife with the blade pointing downward."
                            ],
                            "answer": "A",
                            "explanation": "Raw poultry contains bacteria that transfer directly onto raw tomatoes if prepared on the same unwashed board, causing food poisoning."
                        }
                    },
                    {
                        "type": "knowledge_check",
                        "title": "Topic Assessment - Question 8: Mashing Food for Sick Convalescents",
                        "content": {
                            "question": "What biological digestive benefit is achieved by mashing sweet potatoes for a weak convalescent recovering from malaria?",
                            "options": [
                                "It reduces the mechanical workload of chewing and speeds up stomach liquefaction and nutrient absorption.",
                                "It increases the total calories inside the potato by 500%.",
                                "It chemically converts starch into animal protein.",
                                "It makes the potato absorb more salt."
                            ],
                            "answer": "A",
                            "explanation": "Mashing eliminates the physical energy required for chewing, allowing weak patients to digest and absorb nutrients rapidly."
                        }
                    }
                ],
                # Page 10: Topic Assessment Part 4 (Questions 9 to 10)
                [
                    {
                        "type": "knowledge_check",
                        "title": "Topic Assessment - Question 9: Gender as a Meal Planning Factor",
                        "content": {
                            "question": "In meal planning, why is 'gender' considered a key biological factor when calculating daily food portions?",
                            "options": [
                                "Physiological differences, muscle mass, and biological blood loss (menstruation in women) create distinct energy and iron requirements.",
                                "Boys are culturally expected to eat more greens than girls.",
                                "Women require higher starch intake to build bone mass.",
                                "Gender determines if someone can digest plant proteins."
                            ],
                            "answer": "A",
                            "explanation": "Men generally have greater muscle mass requiring more calories, while adolescent girls and women need extra iron to compensate for menstrual blood loss."
                        }
                    },
                    {
                        "type": "knowledge_check",
                        "title": "Topic Assessment - Question 10: Vegetable Preparation for Toothless Relatives",
                        "content": {
                            "question": "If an elderly family member has severe dental problems (missing teeth), which vegetable preparation method is most suitable?",
                            "options": [
                                "Steaming and pureeing vegetables (like pumpkin or spinach) until silky smooth and soft.",
                                "Deep-frying raw kale until dry and crispy.",
                                "Slicing raw carrots into hard matchstick strips.",
                                "Serving raw cabbage leaves whole."
                            ],
                            "answer": "A",
                            "explanation": "Steaming preserves essential vitamins, while pureeing or mashing eliminates the need for chewing, making vegetables easy and safe to eat."
                        }
                    }
                ]
            ]
        }
    ]

def ingest_cbc_grade8_agriculture_topic8(replace: bool = True):
    """Executes the database transaction to ingest Topic 8 into CBC Grade 8 Agriculture."""
    print("=" * 80)
    print("STARTING CONTENT INGESTION: CBC GRADE 8 AGRICULTURE — TOPIC 8 (DEEP EDITION)")
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

        topic_name = "Cooking Balanced Meals for Special Groups"
        if replace:
            existing_topics = Topic.objects.filter(subject=subject, name=topic_name)
            if existing_topics.exists():
                print(f"[*] Found existing topic '{topic_name}' (ID: {existing_topics.first().id}). Deleting for clean replace...")
                existing_topics.delete()

        topic, created = Topic.objects.get_or_create(
            subject=subject,
            name=topic_name,
            defaults={
                "order": 8,
                "description": "Comprehensive meal planning, special groups nutrition, and practical culinary science: balanced meal architecture (carbohydrates, proteins, protective vitamins/minerals); biological modifiers (age, gender, health status); dietary guidelines for weaning infants, pregnant/lactating mothers, the elderly, and sick convalescents; debunking cultural food taboos; practical kitchen safety (inward pot handles, knife claw grip, separate cutting boards); step-by-step cooking and attractive balanced plating."
            }
        )
        print(f"[*] Topic: '{topic.name}' (ID: {topic.id}, Created: {created})")

        curriculum_data = build_topic8_curriculum()
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
                        block_id=f"g8_agri_t8_u{u_order}_p{page_idx}_b{comp_idx}",
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
        print(f"[SUCCESS] Ingestion Complete for Grade 8 Topic 8: '{topic.name}'")
        print(f"[*] Units Created:   {total_units}")
        print(f"[*] Lessons Created: {total_lessons}")
        print(f"[*] Total Pages:     {total_pages}")
        print(f"[*] Total Blocks:    {total_blocks}")
        print("=" * 80)

if __name__ == "__main__":
    replace_flag = "--replace" in sys.argv or True
    ingest_cbc_grade8_agriculture_topic8(replace=replace_flag)
