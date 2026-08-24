"""
VLearn CBC Grade 8 Agriculture — Topic 9: Cooking Balanced Meals for Special Occasions
Production Ingestion Engine (Phase 1: Content & Card Architecture - Deep Pedagogical Edition)

Curriculum: CBC (Curriculum ID: 5)
Grade: Grade 8 (ID: 15, Level: 8)
Subject: Agriculture
Topic: Cooking Balanced Meals for Special Occasions (Topic Order: 9)

Decomposed into 5 Learning Units & 5 Published Lessons:
  1. Menu Planning and Factors for Special Occasions (7 Pages, 12 Blocks)
  2. Comparing Serving Styles: Family-Style vs. Blue-Plate Service (7 Pages, 12 Blocks)
  3. Designing and Preparing Menus for Special Occasions (7 Pages, 12 Blocks)
  4. Practical: Preparing, Cooking, and Serving a Special Occasion Meal (7 Pages, 13 Blocks)
  5. Financial Management and Waste Reduction in Event Catering & Capstone (10 Pages, 22 Blocks)

Deep Pedagogical Enhancements:
  - Strict 1 Card = 1 Understandable Idea progression.
  - Zero citation leaks ([Topic 4], [KES]), zero developer meta-tags, zero raw unrendered LaTeX in student text.
  - Formative scenario MCQs and 10 Topic Summative MCQs with comprehensive educational explanations.
  - Multi-video integrations embedded across individual practical lessons.

Usage:
  ./venv/bin/python curriculum/ingest_cbc_grade8_agriculture_topic9.py [--replace]
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
    # Sanitize math text leaks
    text = text.replace(r'\text{', '').replace(r'\times', '×')
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

def build_topic9_curriculum():
    """Returns the comprehensive pedagogical page and block structure for Grade 8 Topic 9: Cooking Balanced Meals for Special Occasions."""
    return [
        # =====================================================================
        # LESSON 1: Menu Planning and Factors for Special Occasions
        # =====================================================================
        {
            "unit_order": 1,
            "unit_name": "Menu Planning and Factors for Special Occasions",
            "unit_description": "Cultural, social, and nutritional dimensions of catering for special events (weddings, graduations, community holidays); key logistical factors: guest count, budget limits, kitchen equipment, and dietary diversity.",
            "lesson_title": "Menu Planning and Factors for Special Occasions",
            "pages": [
                # Page 1: Visual Hook & Learning Objectives
                [
                    {
                        "type": "suggested_image",
                        "title": "Hospitality in Action: Festive Communal Banquet",
                        "content": {
                            "title": "Hospitality in Action: Festive Communal Banquet",
                            "caption": "A festive outdoor dining table with steaming platters of roasted meats, spiced rice, fresh salads, and fruit skewers shared among community members."
                        }
                    },
                    {
                        "type": "learning_goal",
                        "title": "Learning Objectives: The Logistics of Celebration",
                        "content": {
                            "title": "What We Will Accomplish Today",
                            "goals": [
                                "Explain the cultural and social role of **food in community celebrations**.",
                                "Analyze the five key **logistical factors** in large-scale menu planning.",
                                "Formulate cost-effective, balanced menus utilizing **local seasonal ingredients**.",
                                "Evaluate demographic needs to prevent expensive event food waste."
                            ]
                        }
                    },
                    {
                        "type": "concept_explanation",
                        "title": "The Power of Communal Dining",
                        "content": {
                            "title": "Why Celebrations Center Around Food",
                            "text": "Sharing a meal during special occasions—like school prize-giving days, weddings, and cultural festivals—builds unity, expresses gratitude, and preserves agricultural traditions. But feeding a large crowd requires master coordination: running out of food leaves guests hungry, while overcooking wastes valuable money!"
                        }
                    }
                ],
                # Page 2: Logistical Planning Factors
                [
                    {
                        "type": "concept_explanation",
                        "title": "Five Critical Menu Planning Factors",
                        "content": {
                            "title": "Catering Logistics for Large Crowds",
                            "text": "- **1. Guest Count (Demographics)**: Knowing the exact number of toddlers, teens, adults, and elderly guests determines portion sizes and textures.\n- **2. Nutritional Balance (Golden Ratio)**: Every plate must supply 1/2 vegetables, 1/4 bodybuilding proteins, and 1/4 energy carbohydrates.\n- **3. Budget Limits & Local Sourcing**: Prioritize affordable local, seasonal crops (sweet potatoes, beans, spinach) over expensive imported foods.\n- **4. Kitchen Equipment & Space**: Ensure enough large cooking pots (sufurias), burners, and serving plates are available.\n- **5. Dietary Restrictions**: Provide vegetarian and health-friendly options (like green gram stews) for guests with dietary restrictions."
                        }
                    },
                    {
                        "type": "suggested_diagram",
                        "title": "Special Occasion Event Menu Logistics & Demographic Balancing Framework",
                        "content": {
                            "title": "Special Occasion Event Menu Logistics & Demographic Balancing Framework",
                            "caption": "Event catering workflow: 1. Guest Demographics & Confirmed RSVP -> 2. Budget & Local Sourcing Matrix -> 3. Golden Ratio Plate (1/2 Greens, 1/4 Protein, 1/4 Starch) -> 4. Kitchen Equipment & Safety Capacity."
                        }
                    }
                ],
                # Page 3: Event Scale Comparison Matrix
                [
                    {
                        "type": "comparison_table",
                        "title": "Event Scale & Planning Strategy Matrix",
                        "content": {
                            "title": "Menu Logistics Across Different Gathering Scales",
                            "headers": ["Event Scale", "Key Planning Challenge", "Smart Ingredient Strategy", "Recommended Serving Style"],
                            "rows": [
                                ["Family Gathering (5-10 people)", "Varied personal tastes, intimate atmosphere", "High-quality fresh cuts, homemade vegetable sides", "Blue-Plate (Plated) Service for personal touch"],
                                ["School Club Party (20-40 students)", "Fast-paced, tight student budget, limited pots", "Bulk starches (rice/potatoes), bean stews, slaw", "Family-Style Service to encourage sharing"],
                                ["Community Festival (100+ guests)", "High volume, unpredictable arrivals, food cooling", "Slow-cooked stews, roasted tubers, bulk greens", "Buffet stations or trained student servers"]
                            ]
                        }
                    }
                ],
                # Page 4: Interactive Budgeting & Ingredient Classification
                [
                    {
                        "type": "interactive_scenario",
                        "title": "Event Budgeting Ingredient Classification",
                        "content": {
                            "title": "Choosing Cost-Effective Celebration Ingredients",
                            "instructions": "Classify each ingredient choice for a school graduation party on a tight budget:",
                            "scenario": "A student catering committee is selecting ingredients for a 40-person school celebration.",
                            "question": "Which ingredient choice is most cost-effective and nutritionally practical?",
                            "options": [
                                "Locally grown cowpeas, beans, seasonal spinach, and bulk local maize flour.",
                                "Imported canned luxury seafood and out-of-season berries.",
                                "Packaged commercial frozen beef patties from an expensive supermarket.",
                                "Imported processed soda bottles for every guest."
                            ],
                            "correct_feedback": "Correct! Sourcing bulk local staples, legumes, and in-season greens keeps meals highly nutritious, fresh, and budget-friendly.",
                            "incorrect_feedback": "Incorrect. Sourcing out-of-season or imported processed foods drives up costs and reduces freshness. Always choose local, seasonal foods!"
                        }
                    }
                ],
                # Page 5: Formative Knowledge Check
                [
                    {
                        "type": "knowledge_check",
                        "title": "Knowledge Check: Demographic Portion Planning",
                        "content": {
                            "question": "Why is knowing guest demographics (e.g., number of toddlers versus active young adults) crucial when planning an event menu?",
                            "options": [
                                "It allows the caterer to adjust both food texture (soft vs. firm) and portion sizes to eliminate food waste.",
                                "It determines what kind of music should be played.",
                                "It tells the cook how many gas burners to buy.",
                                "Toddlers always eat twice as much starch as adults."
                            ],
                            "answer": "A",
                            "explanation": "Demographic planning tailors food texture and portions accurately: young children need small, soft portions, while active youth require higher energy starches, minimizing leftover waste."
                        }
                    }
                ],
                # Page 6: Summary & Connection Forward
                [
                    {
                        "type": "key_takeaway",
                        "title": "Lesson Summary",
                        "content": {
                            "text": "- **Special occasion dining** fosters community bonding and celebrates shared achievements.\n- Successful catering balances **guest count, budget, nutrition, equipment, and dietary diversity**.\n- Sourcing **local seasonal crops** lowers costs while maximizing freshness and nutritional density.\n- Demographic planning prevents both food shortages and wasteful surpluses."
                        }
                    },
                    {
                        "type": "transition",
                        "title": "Looking Ahead",
                        "content": {
                            "text": "How should food be delivered to tables during a celebration? In Lesson 2, we compare Family-Style shared platters with Blue-Plate individual service!"
                        }
                    }
                ],
                # Page 7: Agricultural Integration Spotlight
                [
                    {
                        "type": "concept_explanation",
                        "title": "School Farm to Banquet Table",
                        "content": {
                            "title": "Connecting Agriculture with Hospitality",
                            "text": "The smartest school caterers harvest fresh greens, eggs, and sweet potatoes directly from their school garden! Using produce from organic school gardens slashes catering costs to near zero while serving the freshest, chemical-free food possible."
                        }
                    }
                ]
            ]
        },

        # =====================================================================
        # LESSON 2: Comparing Serving Styles: Family-Style vs. Blue-Plate Service
        # =====================================================================
        {
            "unit_order": 2,
            "unit_name": "Comparing Serving Styles: Family-Style vs. Blue-Plate Service",
            "unit_description": "Comparative food service systems: Family-Style (communal shared platters, casual, low labor, high social interaction) vs. Blue-Plate Service (kitchen portioned, strict portion control, superior hygiene, aesthetic plating).",
            "lesson_title": "Comparing Serving Styles: Family-Style vs. Blue-Plate Service",
            "pages": [
                # Page 1: Visual Hook & Learning Objectives
                [
                    {
                        "type": "suggested_image",
                        "title": "Communal Dining: Family-Style Shared Platters",
                        "content": {
                            "title": "Communal Dining: Family-Style Shared Platters",
                            "caption": "A round dining table with diners passing large communal bowls of potatoes, stew, and fresh vegetables to serve themselves."
                        }
                    },
                    {
                        "type": "learning_goal",
                        "title": "Learning Objectives: Mastering Food Service Systems",
                        "content": {
                            "title": "What We Will Accomplish Today",
                            "goals": [
                                "Define **Family-Style service** and **Blue-Plate (plated) service**.",
                                "Compare both styles regarding **labor, portion control, hygiene, and table space**.",
                                "Explain why Blue-Plate service guarantees nutritional balance.",
                                "Select the optimal service style for various social and institutional scenarios."
                            ]
                        }
                    },
                    {
                        "type": "concept_explanation",
                        "title": "How Service Style Shapes the Meal Experience",
                        "content": {
                            "title": "Platters vs. Individual Plates",
                            "text": "The way food arrives at the table changes everything! Passing large platters creates a warm, lively atmosphere of sharing, while receiving an individually arranged plate provides elegance, strict hygiene, and precise nutritional balance."
                        }
                    }
                ],
                # Page 2: Detailed Service Comparison
                [
                    {
                        "type": "concept_explanation",
                        "title": "Family-Style vs. Blue-Plate Service Mechanics",
                        "content": {
                            "title": "Operational Differences",
                            "text": "- **1. Family-Style Service (Shared Platters)**:\n  * *How it works*: Large serving bowls and platters are placed in the center of the table; guests serve themselves.\n  * *Pros*: Highly social, encourages sharing, requires fewer serving staff.\n  * *Cons*: Risk of unequal food distribution (first guest takes all meat), higher risk of germ spread on shared spoons, and plate waste if guests take too much.\n- **2. Blue-Plate Service (Kitchen Plated)**:\n  * *How it works*: Chefs portion and arrange starch, protein, and vegetables onto individual plates in the kitchen before waiters deliver them.\n  * *Pros*: Perfect portion control, ensures 1/2-1/4-1/4 nutritional balance, beautiful presentation, superior hygiene.\n  * *Cons*: Requires more kitchen plates and active servers; food can cool if not served quickly."
                        }
                    },
                    {
                        "type": "suggested_diagram",
                        "title": "Family-Style vs. Blue-Plate (Plated) Service Comparison Matrix",
                        "content": {
                            "title": "Family-Style vs. Blue-Plate (Plated) Service Comparison Matrix",
                            "caption": "Detailed comparison: Left: Family-Style (Communal platters, high social sharing, low labor, risk of uneven portions) • Right: Blue-Plate (Kitchen portioning, 1/2 greens golden ratio, maximum hygiene, higher labor/plates)."
                        }
                    }
                ],
                # Page 3: Side-by-Side Evaluation Table
                [
                    {
                        "type": "comparison_table",
                        "title": "Food Service Systems Feature Comparison",
                        "content": {
                            "title": "Technical Evaluation of Serving Styles",
                            "headers": ["Feature", "Family-Style Service", "Blue-Plate (Plated) Service"],
                            "rows": [
                                ["Labor & Staffing", "Low (Guests serve themselves from table platters)", "High (Kitchen plating crew + table delivery servers)"],
                                ["Portion Control", "Low (Unregulated; early diners may take extra meat)", "High (Strict uniform portions set by the chef)"],
                                ["Hygiene & Sanitation", "Moderate (Shared serving spoons, hand contact)", "High (Food untouched by other guests)"],
                                ["Table Space Required", "High (Must fit large, heavy bowls and hot platters)", "Low (Only needs space for individual guest plates)"],
                                ["Nutritional Balance", "Variable (Guests may skip vegetables entirely)", "Guaranteed (Golden ratio plated by the chef)"]
                            ]
                        }
                    }
                ],
                # Page 4: Video Resource — Professional Food Service Styles
                [
                    {
                        "type": "suggested_video",
                        "title": "Instructional Video: Food Service Styles: Family-Style vs. Plated Service",
                        "content": {
                            "title": "Instructional Video: Food Service Styles: Family-Style vs. Plated Service",
                            "url": "https://www.youtube.com/watch?v=TXJPk-QfhDU",
                            "resolved_video_id": "TXJPk-QfhDU",
                            "caption": "Watch this hospitality demonstration highlighting table setup, serving mechanics, and portion control differences between communal family service and plated banqueting."
                        }
                    },
                    {
                        "type": "concept_explanation",
                        "title": "Key Professional Takeaways from the Video",
                        "content": {
                            "title": "Hospitality Insights",
                            "text": "- **1. Serving Spoon Etiquette**: In family-style, notice that each platter has a designated serving spoon to prevent personal utensil contamination.\n- **2. Plating Rims**: In blue-plate service, observe how chefs keep the plate rim completely spotless.\n- **3. Flow of Delivery**: Watch how plated meals are served simultaneously to ensure food stays hot."
                        }
                    }
                ],
                # Page 5: Interactive Event Matching Challenge
                [
                    {
                        "type": "interactive_scenario",
                        "title": "Event Service Style Matching Challenge",
                        "content": {
                            "title": "Selecting the Right Service Style",
                            "instructions": "Match each event scenario to its ideal serving style:",
                            "scenario": "You are directing the food committee for two events: a formal wedding reception with 150 guests, and an informal Sunday family lunch.",
                            "question": "Which serving style should you choose for the formal 150-guest wedding?",
                            "options": [
                                "Blue-Plate (Plated) Service for strict portion control, professional presentation, and high hygiene.",
                                "Family-Style Service with massive open bowls on each table.",
                                "Tell guests to cook their own food in the kitchen.",
                                "Serve cold raw ingredients directly."
                            ],
                            "correct_feedback": "Correct! Large formal events like weddings require Blue-Plate service for elegance, fair portioning, and strict hygiene.",
                            "incorrect_feedback": "Incorrect. Large formal banquets require Blue-Plate service to ensure portion fairness and rapid, elegant service."
                        }
                    }
                ],
                # Page 6: Formative Knowledge Check
                [
                    {
                        "type": "knowledge_check",
                        "title": "Knowledge Check: Nutritional Benefit of Blue-Plate Service",
                        "content": {
                            "question": "What is the primary nutritional advantage of Blue-Plate service over Family-Style service in a public dining setting?",
                            "options": [
                                "It ensures every guest receives a scientifically balanced plate (1/2 vegetables, 1/4 protein, 1/4 starch) portioned by the kitchen.",
                                "It allows guests to eat unlimited amounts of fried starches.",
                                "It makes the food cook twice as fast in the pots.",
                                "It requires no dishwashing after the event."
                            ],
                            "answer": "A",
                            "explanation": "In Blue-Plate service, the kitchen controls the portions of each food group, ensuring everyone receives the proper ratio of protective greens, protein, and starch."
                        }
                    }
                ],
                # Page 7: Summary & Connection Forward
                [
                    {
                        "type": "key_takeaway",
                        "title": "Lesson Summary",
                        "content": {
                            "text": "- **Family-Style Service** uses central platters: highly social and low labor, but harder to control portions and hygiene.\n- **Blue-Plate Service** is plated in the kitchen: ensures strict portion control, beautiful aesthetics, and superior hygiene.\n- Formal events, hospital wards, and young child feeding benefit most from **Blue-Plate service**.\n- Informal family and club meals thrive on **Family-Style sharing**."
                        }
                    },
                    {
                        "type": "transition",
                        "title": "Looking Ahead",
                        "content": {
                            "text": "How do we design an exciting menu that looks beautiful and tastes delicious? In Lesson 3, we master color balance, texture contrast, and flavor harmony!"
                        }
                    }
                ]
            ]
        },

        # =====================================================================
        # LESSON 3: Designing and Preparing Menus for Special Occasions
        # =====================================================================
        {
            "unit_order": 3,
            "unit_name": "Designing and Preparing Menus for Special Occasions",
            "unit_description": "Sensory menu engineering: color balance (vibrant greens, reds, yellows vs. monochrome plates), texture contrast (soft stews, crunchy slaws, fluffy grains), flavor harmony, and sustainable local sourcing.",
            "lesson_title": "Designing and Preparing Menus for Special Occasions",
            "pages": [
                # Page 1: Visual Hook & Learning Objectives
                [
                    {
                        "type": "suggested_image",
                        "title": "Visual Harmony: Colorful Balanced Banquet Plate",
                        "content": {
                            "title": "Visual Harmony: Colorful Balanced Banquet Plate",
                            "caption": "A golden roasted chicken leg, vibrant green steamed broccoli, and bright orange carrot sticks arranged neatly next to fluffy spiced yellow rice."
                        }
                    },
                    {
                        "type": "learning_goal",
                        "title": "Learning Objectives: Sensory Menu Engineering",
                        "content": {
                            "title": "What We Will Accomplish Today",
                            "goals": [
                                "Explain how **color, texture, and flavor** stimulate appetite and enjoyment.",
                                "Avoid unappetizing monochrome menus by incorporating **rainbow vegetables**.",
                                "Design a complete 3-part balanced event menu using **local, seasonal ingredients**.",
                                "Connect crop intercropping on farms with low-cost, balanced event dishes."
                            ]
                        }
                    },
                    {
                        "type": "concept_explanation",
                        "title": "We Eat With Our Eyes First!",
                        "content": {
                            "title": "The Art of Sensory Plating",
                            "text": "Imagine being served a plate with white rice, boiled white potatoes, and steamed white cauliflower. Even though it contains nutrients, it looks pale and unappetizing! Combining vibrant colors, crispy and tender textures, and complementary flavors transforms simple food into an unforgettable celebration feast."
                        }
                    }
                ],
                # Page 2: The Three Pillars of Menu Aesthetics
                [
                    {
                        "type": "concept_explanation",
                        "title": "Color, Texture, and Flavor Harmonization",
                        "content": {
                            "title": "Three Rules of Culinary Aesthetics",
                            "text": "- **1. Color Balance (The Visual Rainbow)**: Combine naturally colorful vegetables—deep green kales/spinach, bright orange carrots/pumpkins, and ruby red tomatoes/kachumbari.\n- **2. Texture Contrast (Mouthfeel Variety)**: Balance soft elements (mashed sweet potatoes, tender stewed meat) with crunchy elements (raw cabbage slaw, roasted groundnuts) and fluffy grains (spiced pilau).\n- **3. Flavor Harmony (Taste Balance)**: Pair rich savory stews with tangy, acidic sides (tomato-lemon kachumbari) to cut through richness and cleanse the palate."
                        }
                    },
                    {
                        "type": "suggested_diagram",
                        "title": "Event Menu Design Architecture: Color Harmony, Texture Contrast & Local Sourcing Flowchart",
                        "content": {
                            "title": "Event Menu Design Architecture: Color Harmony, Texture Contrast & Local Sourcing Flowchart",
                            "caption": "Menu design sequence: 1. Budget & Guest Count -> 2. Energy Base (Local Starch: Pilau/Sweet Potato) -> 3. Bodybuilding Protein (Chicken/Beans/Fish) -> 4. Protective Colors (Spinach + Tomato Kachumbari) -> 5. Sensory Harmony Review."
                        }
                    }
                ],
                # Page 3: Menu Appeal Analysis Matrix
                [
                    {
                        "type": "comparison_table",
                        "title": "Celebration Menu Sensory Appeal Evaluation",
                        "content": {
                            "title": "Evaluating Event Menus for Color and Texture",
                            "headers": ["Proposed Menu", "Color Palette", "Textural Profile", "Overall Appeal Rating & Rationale"],
                            "rows": [
                                ["White rice, boiled potatoes, steamed cauliflower", "Monochrome (White/Pale)", "All soft/mushy; no crunch", "Poor (Bland, visually uninviting, unexciting)"],
                                ["Spiced yellow pilau, beef stew, kales, red kachumbari", "Vibrant (Yellow, Brown, Green, Red)", "Fluffy grain, tender meat, crunchy salsa", "High (Appetizing, colorful, perfectly balanced)"],
                                ["Mashed sweet potato, stewed lentils, carrot-cabbage slaw", "Rich (Orange, Brown, Green, Gold)", "Smooth mash, tender beans, crisp raw slaw", "High (Cost-effective, highly nutritious, beautiful)"],
                                ["Boiled cassava, white beans, boiled white cabbage", "Pale / Monochrome", "Uniformly soft and fibrous", "Poor (Lacks visual appeal and textural contrast)"]
                            ]
                        }
                    }
                ],
                # Page 4: Interactive Menu Design Challenge
                [
                    {
                        "type": "interactive_scenario",
                        "title": "Menu Sensory Appeal Classification",
                        "content": {
                            "title": "Evaluating School Celebration Menus",
                            "instructions": "Classify the following menu proposals based on visual and sensory appeal:",
                            "scenario": "A student group presents two menu ideas for a school award banquet.",
                            "question": "Which menu has the highest sensory, textural, and visual appeal?",
                            "options": [
                                "Spiced yellow turmeric rice, savory beef stew, steamed dark greens, and crunchy red kachumbari.",
                                "Plain white boiled rice, boiled white cassava, and steamed white cauliflower.",
                                "Fried white dough balls with plain white sugar syrup.",
                                "Raw unpeeled white potatoes."
                            ],
                            "correct_feedback": "Correct! Yellow rice, rich brown stew, dark green kales, and bright red crunchy kachumbari offer maximum color and texture contrast.",
                            "incorrect_feedback": "Incorrect. Avoid pale monochrome menus. Choose meals that combine multiple vibrant colors and crunchy textures!"
                        }
                    }
                ],
                # Page 5: Formative Knowledge Check
                [
                    {
                        "type": "knowledge_check",
                        "title": "Knowledge Check: Agricultural Nitrogen Synergy",
                        "content": {
                            "question": "Why is it economically and agriculturally smart to intercrop cowpeas with maize, and then serve them together (githeri) at a community celebration?",
                            "options": [
                                "Cowpeas fix atmospheric nitrogen to naturally fertilize companion maize, and serving them together creates an affordable, complete protein-carbohydrate balanced meal.",
                                "It makes the crops grow without needing any water.",
                                "It turns the maize kernels into pure sugar.",
                                "It makes both crops resistant to all plant diseases."
                            ],
                            "answer": "A",
                            "explanation": "Intercropping legumes enriches farm soil with natural nitrogen, while combining maize and legumes in the kitchen yields a complete, highly nutritious, low-cost balanced dish."
                        }
                    }
                ],
                # Page 6: Summary & Connection Forward
                [
                    {
                        "type": "key_takeaway",
                        "title": "Lesson Summary",
                        "content": {
                            "text": "- **Appealing celebration menus** balance **color, texture, and flavor** to stimulate appetite.\n- Avoid **monochrome plates** by incorporating vibrant green, orange, and red seasonal vegetables.\n- Pair **soft stews** with **crispy, crunchy raw salads** (slaw or kachumbari).\n- Sourcing **farm-intercropped staples** (maize + legumes) delivers world-class nutrition at minimal cost."
                        }
                    },
                    {
                        "type": "transition",
                        "title": "Looking Ahead",
                        "content": {
                            "text": "Time to enter the kitchen! In Lesson 4, we execute our practical cooking lab: spiced rice, savory beef stew, steamed crunchy cabbage, and clean Blue-Plate presentation!"
                        }
                    }
                ],
                # Page 7: Culinary Pro-Tip: Seasonal Sourcing
                [
                    {
                        "type": "concept_explanation",
                        "title": "The Seasonal Sourcing Advantage",
                        "content": {
                            "title": "Why Seasonality Wins in Catering",
                            "text": "When vegetables are in peak harvest season, their flavor and vitamin levels are at their maximum, and market prices drop by up to 60%! A great caterer designs menus around whatever crops are currently flooding local farmers' markets."
                        }
                    }
                ]
            ]
        },

        # =====================================================================
        # LESSON 4: Practical: Preparing, Cooking, and Serving a Special Occasion Meal
        # =====================================================================
        {
            "unit_order": 4,
            "unit_name": "Practical: Preparing, Cooking, and Serving a Special Occasion Meal",
            "unit_description": "Hands-on culinary lab: team division of labor, 3-basin sanitation station, mise en place preparation, step-by-step cooking (spiced turmeric rice, savory beef stew, short-steamed green cabbage), and Blue-Plate presentation.",
            "lesson_title": "Practical: Preparing, Cooking, and Serving a Special Occasion Meal",
            "pages": [
                # Page 1: Visual Hook & Practical Objectives
                [
                    {
                        "type": "suggested_image",
                        "title": "Kitchen Organization: Professional Mise en Place",
                        "content": {
                            "title": "Kitchen Organization: Professional Mise en Place",
                            "caption": "A tidy kitchen workstation with pre-measured raw rice, cubed beef, diced onions, chopped tomatoes, and shredded cabbage in individual prep bowls."
                        }
                    },
                    {
                        "type": "learning_goal",
                        "title": "Learning Objectives: Banqueting Culinary Execution",
                        "content": {
                            "title": "What We Will Accomplish Today",
                            "goals": [
                                "Organize a collaborative kitchen team with clear **role assignments**.",
                                "Establish a **3-basin sanitation station** and color-coded chopping boards.",
                                "Execute step-by-step cooking of **spiced yellow rice, beef stew, and short-steamed cabbage**.",
                                "Plate and present a balanced meal using professional **Blue-Plate standards**."
                            ]
                        }
                    },
                    {
                        "type": "concept_explanation",
                        "title": "The Secret of Professional Kitchens: Mise en Place",
                        "content": {
                            "title": "Everything in Its Place Before Cooking",
                            "text": "In professional culinary arts, 'Mise en Place' means having all ingredients washed, chopped, measured, and tools arranged before turning on any heat! This eliminates panic, prevents burning food, and keeps the kitchen safe and organized."
                        }
                    }
                ],
                # Page 2: Team Roles & Sanitation Station Setup
                [
                    {
                        "type": "concept_explanation",
                        "title": "Division of Labor and Sanitation Station SOP",
                        "content": {
                            "title": "Kitchen Team Organization & 3-Basin Sanitation",
                            "text": "- **Team Roles**: Group Leader (timing & safety), Prep Team (washing & chopping), Cook Team (heat & stirring), Plating Team (hygienic serving & rim wiping).\n- **3-Basin Sanitation Station**:\n  * *Basin 1*: Warm soapy water for handwashing and washing raw root crops.\n  * *Basin 2*: Clean running water for rinsing.\n  * *Basin 3*: Mild sanitizing solution for wiping countertops and cutting boards.\n- **Cutting Board Safety**: Red/blue board for raw beef, green board for cabbage to stop **cross-contamination**."
                        }
                    },
                    {
                        "type": "suggested_diagram",
                        "title": "Banqueting Kitchen Operation: Division of Labor, Sanitation Station & Inward Pot Handles",
                        "content": {
                            "title": "Banqueting Kitchen Operation: Division of Labor, Sanitation Station & Inward Pot Handles",
                            "caption": "Operational kitchen floorplan: 1. 3-Basin Sanitation Station -> 2. Color-coded cutting boards -> 3. Stoves with inward-facing pot handles -> 4. Blue-Plate assembly line with clean plate rims."
                        }
                    }
                ],
                # Page 3: Step-by-Step Practical Cooking SOP
                [
                    {
                        "type": "step_process",
                        "title": "Standard Operating Procedure: Banquet Main Course",
                        "content": {
                            "title": "Cooking Spiced Rice, Beef Stew, and Steamed Cabbage",
                            "steps": [
                                "**Step 1: Mise en Place**: Wash cabbage and tomatoes in Basin 1/2. Finely shred cabbage, dice onions, cube beef on separate boards.",
                                "**Step 2: Cook Spiced Rice**: Sauté onions with a pinch of turmeric in 1 tbsp oil. Add washed rice and water (1:2 ratio). Boil, cover, and simmer for 15-20 min.",
                                "**Step 3: Simmer Beef Stew**: Brown beef cubes in a pot. Add onions, garlic, and tomatoes. Add 1 cup broth/water, cover, and simmer for 25 min until tender.",
                                "**Step 4: Steam Green Cabbage**: Place shredded cabbage in a pot with 2 tbsp water and a pinch of salt. Cover tightly and steam for 3 to 5 minutes so it stays bright green and crisp.",
                                "**Step 5: Blue-Plate Presentation**: Portion 1/4 plate spiced rice, 1/4 plate beef stew, and 1/2 plate steamed cabbage. Wipe plate rim clean before serving."
                            ]
                        }
                    }
                ],
                # Page 4: Video Resource — Banqueting Cookery & Mise en Place
                [
                    {
                        "type": "suggested_video",
                        "title": "Instructional Video: Practical Banquet Cookery & Mise en Place",
                        "content": {
                            "title": "Instructional Video: Practical Banquet Cookery & Mise en Place",
                            "url": "https://www.youtube.com/watch?v=6ZjkLwQt_YE",
                            "resolved_video_id": "6ZjkLwQt_YE",
                            "caption": "Watch this practical kitchen demonstration showing team prep, vegetable steaming techniques, stove safety, and uniform banquet plating."
                        }
                    },
                    {
                        "type": "concept_explanation",
                        "title": "Key Lab Insights from the Video",
                        "content": {
                            "title": "Culinary Technique Highlights",
                            "text": "- **1. Short Steaming**: Notice why steaming cabbage for only 3-5 minutes keeps it bright green and loaded with Vitamin C.\n- **2. Inward Handles**: Observe how every saucepan handle is turned inward to prevent catastrophic spills.\n- **3. Plate Rim Inspection**: Watch the plating team wipe every plate edge with a clean towel before delivery."
                        }
                    }
                ],
                # Page 5: Interactive Culinary Sequencing Challenge
                [
                    {
                        "type": "interactive_scenario",
                        "title": "Kitchen Banqueting Workflow Challenge",
                        "content": {
                            "title": "Chronological Culinary Execution",
                            "instructions": "Place the banqueting steps in the correct chronological order:",
                            "scenario": "Your school cooking group is preparing food for 30 guest parents.",
                            "question": "What is the correct logical workflow from start to finish?",
                            "options": [
                                "1. Sanitize hands & setup 3 basins -> 2. Chop beef and veggies on separate boards -> 3. Cook rice & simmer stew -> 4. Steam cabbage 3-5 min -> 5. Blue-plate with 1/2 greens ratio",
                                "1. Plate cold food -> 2. Turn on stove -> 3. Wash hands after eating",
                                "1. Leave pot handles sticking into walkway -> 2. Chop raw meat on salad board",
                                "1. Boil cabbage for 1 hour until brown -> 2. Throw raw meat on dirty tables"
                            ],
                            "correct_feedback": "Correct! Always establish sanitation first, prep ingredients, cook thoroughly, steam greens briefly, and plate with the golden ratio.",
                            "incorrect_feedback": "Incorrect. Follow the chronological order: Sanitize -> Prep -> Cook -> Steam -> Plate."
                        }
                    }
                ],
                # Page 6: Formative Knowledge Check
                [
                    {
                        "type": "knowledge_check",
                        "title": "Knowledge Check: Short Steaming vs. Long Boiling",
                        "content": {
                            "question": "Why is steaming shredded cabbage for 3 to 5 minutes far superior to boiling it in excess water for 20 minutes?",
                            "options": [
                                "Short steaming preserves heat-sensitive Vitamin C and maintains bright green color and crisp texture, whereas long boiling leaches nutrients and turns leaves yellow-brown.",
                                "Short steaming makes the cabbage absorb 5 times more cooking oil.",
                                "Long boiling makes the cabbage taste like sugar.",
                                "Short steaming destroys all beneficial dietary fibers."
                            ],
                            "answer": "A",
                            "explanation": "Excessive boiling leaches water-soluble vitamins (Vitamin C, B-complex) into the discarded cooking water and breaks down chlorophyll, turning vegetables yellow-brown."
                        }
                    }
                ],
                # Page 7: Summary & Connection Forward
                [
                    {
                        "type": "key_takeaway",
                        "title": "Lesson Summary",
                        "content": {
                            "text": "- **Mise en place** organizes all chopped ingredients and tools before heat is turned on.\n- The **3-basin sanitation system** and color-coded boards eliminate pathogen transfer.\n- Steaming vegetables for **3-5 minutes** locks in vitamins, crunchy texture, and vibrant color.\n- **Blue-Plate service** delivers a balanced 1/2 vegetable, 1/4 protein, 1/4 starch meal with clean presentation."
                        }
                    },
                    {
                        "type": "transition",
                        "title": "Looking Ahead",
                        "content": {
                            "text": "How do caterers manage event finances, calculate exact ingredient quantities, and recycle food leftovers? In Lesson 5, we master financial management, portion math, and the circular compost loop!"
                        }
                    }
                ]
            ]
        },

        # =====================================================================
        # LESSON 5: Financial Management and Waste Reduction in Event Catering & Capstone
        # =====================================================================
        {
            "unit_order": 5,
            "unit_name": "Financial Management and Waste Reduction in Event Catering",
            "unit_description": "Event budgeting math: portion formula (Total = Portion × Guests), RSVP attendance management, food loss prevention, behavioral portioning (smaller plates), circular agricultural loops (compost heaps & poultry feed), topic video review, and 10 topic summative MCQs.",
            "lesson_title": "Financial Management and Waste Reduction in Event Catering & Capstone",
            "pages": [
                # Page 1: Visual Hook & Capstone Objectives
                [
                    {
                        "type": "suggested_image",
                        "title": "Circular Sustainability: School Garden Composting Setup",
                        "content": {
                            "title": "Circular Sustainability: School Garden Composting Setup",
                            "caption": "A student emptying a container of raw organic vegetable kitchen scraps (cabbage cores, potato skins, onion ends) into a school garden compost bin."
                        }
                    },
                    {
                        "type": "learning_goal",
                        "title": "Learning Objectives: Catering Economics & Topic Mastery",
                        "content": {
                            "title": "What We Will Accomplish Today",
                            "goals": [
                                "Calculate exact ingredient quantities using the **Portion Formula**.",
                                "Apply financial management and **RSVP tracking** to prevent event losses.",
                                "Design a **circular waste management plan** recycling kitchen scraps into compost manure.",
                                "Review the Topic Video and achieve 100% mastery on the **10 Topic Summative Assessment Questions**."
                            ]
                        }
                    },
                    {
                        "type": "concept_explanation",
                        "title": "The Economics and Ecology of Catering",
                        "content": {
                            "title": "Smart Math and Zero Waste",
                            "text": "Catering without mathematical planning is a recipe for financial disaster! Buying too much food wastes money, while throwing away leftovers harms the environment. Today, we master event budgeting math and connect kitchen waste directly back into the school farm's compost and animal feed loops."
                        }
                    }
                ],
                # Page 2: The Portion Formula & Budgeting Mathematics
                [
                    {
                        "type": "concept_explanation",
                        "title": "Event Budgeting and Quantity Calculation",
                        "content": {
                            "title": "The Portion Formula in Action",
                            "text": "- **The Core Formula**: Total Ingredient Required = Portion Size per Guest × Expected Guest Count.\n- **Example Calculation**:\n  * Standard beef portion = 0.15 kg (150 g) per guest.\n  * For 40 confirmed guests: 0.15 kg × 40 = 6.0 kg of beef required.\n- **Planners Procurement Rules**:\n  * 1. Always enforce an **RSVP** (confirmed guest list) before buying.\n  * 2. Purchase from wholesale farm markets rather than expensive retail stores.\n  * 3. Add a small 5% safety buffer for unexpected visitors, but never double recipes blindly."
                        }
                    },
                    {
                        "type": "suggested_diagram",
                        "title": "Event Catering Financial Math, Portion Formulas & Circular Agricultural Waste Loops",
                        "content": {
                            "title": "Event Catering Financial Math, Portion Formulas & Circular Agricultural Waste Loops",
                            "caption": "Catering economics & circular loop: 1. Confirmed RSVP -> 2. Portion Formula Math -> 3. Behavioral Portioning (Smaller plates) -> 4. Clean surplus donation -> 5. Raw crop scrap composting -> 6. Soil enrichment for next crop harvest."
                        }
                    }
                ],
                # Page 3: Circular Event Waste Management Matrix
                [
                    {
                        "type": "comparison_table",
                        "title": "Event Waste Categories & Sustainable Agricultural Solutions",
                        "content": {
                            "title": "Managing Waste Streams in School Event Catering",
                            "headers": ["Waste Category", "Immediate Consequence", "Financial Impact", "Sustainable Farm Solution"],
                            "rows": [
                                ["Uncooked Crop Residues (Cabbage cores, peels, onion skins)", "Flies, kitchen odors", "Minor (paid for prep scraps)", "Chop and add to the school compost pile to generate rich organic manure"],
                                ["Untouched Cooked Leftovers (Clean pilau, bean stew)", "Bacterial spoilage within 12h if uncooled", "Major (lost fuel, oil, labor, food costs)", "Cool immediately; package hygienically and distribute to local needy families"],
                                ["Plate Waste (Half-eaten food from guest plates)", "Saliva contamination; unfit for humans", "Total financial loss", "Feed to school poultry/pigs (if low salt) or mix into deep compost pits"]
                            ]
                        }
                    }
                ],
                # Page 4: Interactive Catering Math Challenge
                [
                    {
                        "type": "interactive_scenario",
                        "title": "Event Catering Mathematics Challenge",
                        "content": {
                            "title": "Calculating Rice for a School Meeting",
                            "instructions": "Apply the portion formula to calculate quantity and cost:",
                            "scenario": "You are catering for a Parent-Teacher meeting with 30 confirmed guests. Rice portion is 0.1 kg (100 g) per person, and bulk rice costs 150 KES per kg.",
                            "question": "How much rice should you purchase, and what will it cost?",
                            "options": [
                                "Purchase 3 kg of rice, costing 450 KES (0.1 kg × 30 = 3 kg; 3 kg × 150 KES = 450 KES).",
                                "Purchase 30 kg of rice, costing 4,500 KES.",
                                "Purchase 10 kg of rice, costing 1,500 KES.",
                                "Purchase 1 kg of rice, costing 150 KES."
                            ],
                            "correct_feedback": "Correct! 0.1 kg × 30 guests = 3 kg of rice; 3 kg × 150 KES/kg = 450 KES total cost. Precise calculations prevent financial loss and food surplus!",
                            "incorrect_feedback": "Incorrect. Use the formula: Portion (0.1 kg) × Guests (30) = 3 kg. Total cost = 3 kg × 150 KES = 450 KES."
                        }
                    }
                ],
                # Page 5: Formative Knowledge Check & Master Summary
                [
                    {
                        "type": "knowledge_check",
                        "title": "Knowledge Check: Closed-Loop Farm Recycling",
                        "content": {
                            "question": "Which practice demonstrates a closed-loop agricultural recycling system for event waste on a school farm?",
                            "options": [
                                "Collecting cabbage cores and potato peels from food preparation and adding them to the compost heap to enrich school farm soil.",
                                "Burning paper napkins and dumping plastic bottles in dry gullies.",
                                "Pouring leftover hot cooking oil into clean water streams.",
                                "Burying half-eaten salted plates in cattle grazing paddocks."
                            ],
                            "answer": "A",
                            "explanation": "Kitchen crop residues contain organic matter and minerals. Composting them recycles nutrients back to the soil, providing free organic manure for future crops."
                        }
                    },
                    {
                        "type": "key_takeaway",
                        "title": "Topic 9 Master Summary: Cooking Balanced Meals for Special Occasions",
                        "content": {
                            "text": "- **Menu Planning Logistics**: Balance **guest count, budget, nutrition, equipment, and dietary diversity**.\n- **Serving Systems**: **Family-Style** (communal, social, low labor) vs. **Blue-Plate** (kitchen portioned, strict portion control, maximum hygiene).\n- **Sensory Aesthetics**: Harmonize **colors** (rainbow greens/reds), **textures** (soft stews + crispy slaws), and **flavors**.\n- **Practical Execution**: Division of labor, 3-basin sanitation station, inward pot handles, and short steaming.\n- **Catering Economics**: Apply the **Portion Formula**, get RSVP counts, and recycle crop scraps into **compost manure**."
                        }
                    }
                ],
                # Page 6: Topic Video Review
                [
                    {
                        "type": "suggested_video",
                        "title": "Topic Video Review: Special Occasions Catering & Zero-Waste Hospitality",
                        "content": {
                            "title": "Topic Video Review: Special Occasions Catering & Zero-Waste Hospitality",
                            "url": "https://www.youtube.com/watch?v=Ei5z_0Lxmic",
                            "resolved_video_id": "Ei5z_0Lxmic",
                            "caption": "Watch this comprehensive educational review covering event menu logistics, serving style comparisons, sensory aesthetics, kitchen safety, and catering financial management."
                        }
                    },
                    {
                        "type": "concept_explanation",
                        "title": "Key Review Highlights for Video Analysis",
                        "content": {
                            "title": "Final Review Takeaways",
                            "text": "- **1. Portion Accuracy**: Notice how mathematical portion planning prevents massive leftover spoilage.\n- **2. Hospitality Standards**: Observe why wiping plate rims creates an unforgettable impression of hygiene and care.\n- **3. Composting Connections**: See how catering scraps become tomorrow's rich garden manure."
                        }
                    }
                ],
                # Page 7: Topic Assessment Part 1 (Questions 1 to 2)
                [
                    {
                        "type": "knowledge_check",
                        "title": "Topic Assessment - Question 1: Family-Style Hygiene Limitation",
                        "content": {
                            "question": "Why is Family-Style service generally considered less hygienic than Blue-Plate service for a large community gathering?",
                            "options": [
                                "Multiple guests handle the same communal serving spoons, increasing the risk of cross-contamination and pathogen transmission.",
                                "Food in Family-Style service is cooked at lower temperatures.",
                                "Blue-Plate food is treated with chemical preservatives in the kitchen.",
                                "Family-Style service requires disposable plastic cups."
                            ],
                            "answer": "A",
                            "explanation": "Because guests pass shared platters and use common utensils, pathogens can easily transfer from hands to spoons and into the food, raising cross-contamination risks."
                        }
                    },
                    {
                        "type": "knowledge_check",
                        "title": "Topic Assessment - Question 2: Color and Texture Contrast in Vegetables",
                        "content": {
                            "question": "You are planning a menu for a community holiday celebration. Which vegetable combination provides the best sensory color and textural contrast?",
                            "options": [
                                "Steamed green spinach and a crispy red tomato-onion salad (kachumbari).",
                                "Steamed white cabbage and boiled white potatoes.",
                                "Boiled cauliflower and mashed turnips.",
                                "Deep-fried kales and stewed green peas."
                            ],
                            "answer": "A",
                            "explanation": "Deep green spinach (soft texture) paired with bright red kachumbari (crunchy, tangy) provides superior visual color contrast and mouthfeel variety."
                        }
                    }
                ],
                # Page 8: Topic Assessment Part 2 (Questions 3 to 5)
                [
                    {
                        "type": "knowledge_check",
                        "title": "Topic Assessment - Question 3: 3-Basin Sanitation Station Purpose",
                        "content": {
                            "question": "What is the primary purpose of setting up a 'Sanitation Station' with three basins in a practical school kitchen?",
                            "options": [
                                "To establish a clean, sequential workflow for handwashing, raw crop rinsing, and tool sanitization to prevent foodborne illness.",
                                "To provide separate water reservoirs for boiling beef and rice.",
                                "To cool down hot pots and pans quickly after cooking.",
                                "To store dry spices away from rodents."
                            ],
                            "answer": "A",
                            "explanation": "The 3-basin setup ensures hands are washed, crops are clean, and tools/counters are sanitized, preventing bacterial contamination during high-volume cooking."
                        }
                    },
                    {
                        "type": "knowledge_check",
                        "title": "Topic Assessment - Question 4: Catering Portion Formula Calculation",
                        "content": {
                            "question": "A caterer expects 80 guests for a wedding. The portion size for sweet potatoes is 200 grams (0.2 kg) per person. How many kilograms of sweet potatoes should be purchased?",
                            "options": [
                                "16 kg (0.2 kg × 80 guests = 16 kg).",
                                "8 kg",
                                "80 kg",
                                "20 kg"
                            ],
                            "answer": "A",
                            "explanation": "Using the Portion Formula: Total Quantity = Portion (0.2 kg) × Guests (80) = 16 kg of sweet potatoes."
                        }
                    },
                    {
                        "type": "knowledge_check",
                        "title": "Topic Assessment - Question 5: School Farm Compost Loop",
                        "content": {
                            "question": "Which agricultural practice describes a closed-loop recycling system for event catering waste on a school farm?",
                            "options": [
                                "Collecting cabbage cores and potato peels from food prep and adding them to the school's compost pile to enrich farm soil.",
                                "Burning paper decorations and throwing plastic into dry gullies.",
                                "Burying salted plate leftovers deep in pasture soil where cattle graze.",
                                "Pouring hot leftover cooking oil directly into clean water wells."
                            ],
                            "answer": "A",
                            "explanation": "Kitchen crop scraps decompose into high-grade organic humus, replenishing soil nutrients for subsequent school garden crops without synthetic inputs."
                        }
                    }
                ],
                # Page 9: Topic Assessment Part 3 (Questions 6 to 8)
                [
                    {
                        "type": "knowledge_check",
                        "title": "Topic Assessment - Question 6: Meaning of Mise en Place",
                        "content": {
                            "question": "What is the exact meaning of 'Mise en Place' in professional culinary and kitchen management?",
                            "options": [
                                "Having all ingredients washed, chopped, measured, and tools arranged before cooking begins.",
                                "Washing all dirty pots after guests leave.",
                                "Calculating the event budget and cost per plate.",
                                "Plating individual portions artistically in the kitchen."
                            ],
                            "answer": "A",
                            "explanation": "'Mise en place' means 'everything in its place.' Pre-measuring and prepping ingredients before lighting stoves prevents kitchen chaos and burning food."
                        }
                    },
                    {
                        "type": "knowledge_check",
                        "title": "Topic Assessment - Question 7: Blue-Plate Budget Control Mechanism",
                        "content": {
                            "question": "How does Blue-Plate service assist an event planner in managing a tight catering budget?",
                            "options": [
                                "It provides strict portion control, ensuring the kitchen prepares exactly the right amount of food without costly overproduction.",
                                "It allows guests to serve themselves unlimited food.",
                                "It eliminates the need for dishwashing.",
                                "It requires purchasing expensive imported serving platters."
                            ],
                            "answer": "A",
                            "explanation": "Blue-Plate service allows kitchen staff to distribute food uniformly, preventing early diners from over-serving and eliminating expensive surplus preparation."
                        }
                    },
                    {
                        "type": "knowledge_check",
                        "title": "Topic Assessment - Question 8: Severe Kitchen Knife Safety Hazard",
                        "content": {
                            "question": "Which of the following represents an extreme safety hazard when handling kitchen knives in a cooking lab?",
                            "options": [
                                "Walking rapidly through a busy kitchen while gesturing and pointing with a chef's knife.",
                                "Holding the knife by the handle with the blade pointing down when walking.",
                                "Tucking fingers inward like a claw when slicing raw crops on a stable board.",
                                "Keeping eyes focused on fingers and the knife blade while cutting."
                            ],
                            "answer": "A",
                            "explanation": "Gesturing or pointing with an exposed blade in a busy kitchen creates an extreme risk of accidental cuts and puncture injuries. Knives must always be handled with discipline."
                        }
                    }
                ],
                # Page 10: Topic Assessment Part 4 (Questions 9 to 10)
                [
                    {
                        "type": "knowledge_check",
                        "title": "Topic Assessment - Question 9: RSVP Importance in Event Catering",
                        "content": {
                            "question": "In event catering, why is obtaining an RSVP (confirmed guest count) so critical?",
                            "options": [
                                "It allows the planner to calculate exact ingredient quantities, reducing both food waste and unnecessary financial spending.",
                                "It determines what music will be played.",
                                "It decides whether to use gas or charcoal burners.",
                                "It is a government requirement for crop trading."
                            ],
                            "answer": "A",
                            "explanation": "Confirmed attendance numbers allow caterers to buy precise ingredient amounts using the portion formula, avoiding expensive leftovers and budget overruns."
                        }
                    },
                    {
                        "type": "knowledge_check",
                        "title": "Topic Assessment - Question 10: Vegetarian Protein Alternative on Event Menus",
                        "content": {
                            "question": "If a guest at your celebration is a strict vegetarian, which menu item represents a high-protein, balanced alternative to beef stew?",
                            "options": [
                                "A rich, savory stew made of local brown beans and green cowpeas.",
                                "Soft boiled yellow rice spiced with turmeric.",
                                "Steamed cabbage and boiled white potatoes.",
                                "Sliced raw tomatoes and sweet bananas."
                            ],
                            "answer": "A",
                            "explanation": "Legumes like beans and cowpeas are rich in bodybuilding plant proteins, making them an excellent, nutritious, and balanced protein replacement for beef stew."
                        }
                    }
                ]
            ]
        }
    ]

def ingest_cbc_grade8_agriculture_topic9(replace: bool = True):
    """Executes the database transaction to ingest Topic 9 into CBC Grade 8 Agriculture."""
    print("=" * 80)
    print("STARTING CONTENT INGESTION: CBC GRADE 8 AGRICULTURE — TOPIC 9 (DEEP EDITION)")
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

        topic_name = "Cooking Balanced Meals for Special Occasions"
        if replace:
            existing_topics = Topic.objects.filter(subject=subject, name=topic_name)
            if existing_topics.exists():
                print(f"[*] Found existing topic '{topic_name}' (ID: {existing_topics.first().id}). Deleting for clean replace...")
                existing_topics.delete()

        topic, created = Topic.objects.get_or_create(
            subject=subject,
            name=topic_name,
            defaults={
                "order": 9,
                "description": "Comprehensive event catering, food service systems, and culinary economics: cultural role of special occasions; five logistical planning factors (demographics, golden ratio nutrition, budget, equipment, dietary diversity); comparing Family-Style communal platters vs. Blue-Plate kitchen plated service; sensory menu aesthetics (color harmony, texture contrast, flavor balance); practical banqueting cookery (division of labor, 3-basin sanitation station, mise en place, inward pot handles, short steaming); catering mathematics (portion formula, RSVP tracking); and circular agricultural waste recycling (composting and animal feed loops)."
            }
        )
        print(f"[*] Topic: '{topic.name}' (ID: {topic.id}, Created: {created})")

        curriculum_data = build_topic9_curriculum()
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
                        block_id=f"g8_agri_t9_u{u_order}_p{page_idx}_b{comp_idx}",
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
        print(f"[SUCCESS] Ingestion Complete for Grade 8 Topic 9: '{topic.name}'")
        print(f"[*] Units Created:   {total_units}")
        print(f"[*] Lessons Created: {total_lessons}")
        print(f"[*] Total Pages:     {total_pages}")
        print(f"[*] Total Blocks:    {total_blocks}")
        print("=" * 80)

if __name__ == "__main__":
    replace_flag = "--replace" in sys.argv or True
    ingest_cbc_grade8_agriculture_topic9(replace=replace_flag)
