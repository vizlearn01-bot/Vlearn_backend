"""
VLearn CBC Grade 8 Agriculture — Topic 6: Preparation of Animal Products
Production Ingestion Engine (Phase 1: Content & Card Architecture - Deep Pedagogical Edition)

Curriculum: CBC (Curriculum ID: 5)
Grade: Grade 8 (ID: 15, Level: 8)
Subject: Agriculture
Topic: Preparation of Animal Products (Topic Order: 6)

Decomposed into 9 Learning Units & 9 Published Lessons:
  1. Fish Scaling and Gutting (7 Pages, 12 Blocks)
  2. Cleaning, Salting, and Frying Fish (7 Pages, 12 Blocks)
  3. Poultry Slaughtering and Defeathering (7 Pages, 12 Blocks)
  4. Gutting, Cleaning, and Draining Chicken (7 Pages, 13 Blocks)
  5. Preserving Meat by Salting and Boiling (7 Pages, 12 Blocks)
  6. Preserving Meat by Drying and Smoking (7 Pages, 12 Blocks)
  7. Preserving Milk by Boiling (7 Pages, 12 Blocks)
  8. Preserving Milk by Fermentation and Cooling (7 Pages, 12 Blocks)
  9. Importance of Milk and Meat Preservation & Capstone (10 Pages, 22 Blocks)

Deep Pedagogical Enhancements:
  - Strict 1 Card = 1 Understandable Idea progression.
  - Zero citation leaks ([1], [421]), zero developer meta-tags, zero raw unrendered LaTeX.
  - Formative scenario MCQs and Topic Summative MCQs with comprehensive educational explanations.
  - Multi-video integrations embedded across individual practical lessons.

Usage:
  ./venv/bin/python curriculum/ingest_cbc_grade8_agriculture_topic6.py [--replace]
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

def build_topic6_curriculum():
    """Returns the comprehensive pedagogical page and block structure for Grade 8 Topic 6: Preparation of Animal Products."""
    return [
        # =====================================================================
        # LESSON 1: Fish Scaling and Gutting
        # =====================================================================
        {
            "unit_order": 1,
            "unit_name": "Fish Scaling and Gutting",
            "unit_description": "Fish freshness indicators (clear eyes, bright red gills, firm skin), purpose of scaling and gutting, descaling technique (tail to head), and shallow belly slitting to extract viscera safely.",
            "lesson_title": "Fish Scaling and Gutting",
            "pages": [
                # Page 1: Visual Hook & Learning Objectives
                [
                    {
                        "type": "suggested_image",
                        "title": "Freshness Quality: Fresh Harvested Tilapia",
                        "content": {
                            "title": "Freshness Quality: Fresh Harvested Tilapia",
                            "caption": "A fresh, high-quality tilapia showing shiny intact scales, clear bulging eyes, and clean skin ready for kitchen processing."
                        }
                    },
                    {
                        "type": "learning_goal",
                        "title": "Learning Objectives: Fresh Fish Processing",
                        "content": {
                            "title": "What We Will Accomplish Today",
                            "goals": [
                                "Identify 4 key sensory signs of **fresh, high-quality fish** (eyes, gills, skin, smell).",
                                "Explain why **scaling and gutting** are essential biological food-safety procedures.",
                                "Demonstrate descaling technique from **tail toward head at 45 degrees**.",
                                "Execute a shallow **belly incision from the vent forward** without puncturing internal organs."
                            ]
                        }
                    },
                    {
                        "type": "concept_explanation",
                        "title": "The Art of Fish Processing",
                        "content": {
                            "title": "From Harvest to Kitchen",
                            "text": "Fresh fish is a premier source of high-quality protein, omega-3 fats, and essential minerals like calcium and phosphorus. However, fresh fish spoils faster than almost any other meat! To make fish pleasant to eat and prevent rapid microbial decay, we must master two foundational skills: **scaling** (removing calcium armor) and **gutting** (removing bacteria-laden internal organs)."
                        }
                    }
                ],
                # Page 2: Evaluating Fish Freshness
                [
                    {
                        "type": "concept_explanation",
                        "title": "Sensory Indicators of Fish Quality",
                        "content": {
                            "title": "How to Inspect Raw Fish",
                            "text": "Before processing, you must verify that the fish is fresh and safe for human consumption:\n\n- **1. The Eyes**: Must be clear, bright, and bulging outward (decaying fish have sunken, cloudy, grey eyes).\n- **2. The Gills**: Lift the gill cover (operculum); gills must be bright red or pink and free of slimy brown mucus.\n- **3. The Flesh & Skin**: Flesh must be firm and elastic, springing back immediately when pressed with a thumb; scales must adhere tightly to the skin.\n- **4. The Odor**: Fresh fish smells like clean lake or ocean water—never sour, ammonia-like, or rotten."
                        }
                    },
                    {
                        "type": "suggested_diagram",
                        "title": "Fish Anatomy & 4-Step Scaling/Gutting Workflow",
                        "content": {
                            "title": "Fish Anatomy & 4-Step Scaling/Gutting Workflow",
                            "caption": "Fish anatomy & processing flowchart: 1. Grip tail firmly with cloth -> 2. Scrape scales tail-to-head at 45° -> 3. Shallow slit from vent to under-jaw -> 4. Extract entire viscera mass intact & rinse cavity under running water."
                        }
                    }
                ],
                # Page 3: Biological Importance of Scaling & Gutting
                [
                    {
                        "type": "comparison_table",
                        "title": "Scaling vs. Gutting: Biological & Culinary Functions",
                        "content": {
                            "title": "Fish Preparation Functions Matrix",
                            "headers": ["Processing Step", "Anatomical Target", "Culinary Purpose", "Food Safety & Biological Reason"],
                            "rows": [
                                ["Fish Scaling", "Outer epidermis & calcium scales", "Removes hard, indigestible plates for pleasant texture", "Eliminates surface slime, dirt, and trapped algae"],
                                ["Fish Gutting", "Internal viscera (stomach, intestines, liver, gills)", "Prevents foul bitter tastes and stomach acid leakage", "Removes digestive enzymes and millions of rot-causing microbes that cause rapid decomposition"],
                                ["Cavity Washing", "Inner peritoneal lining & kidney bloodline", "Produces clean, appetizing white/pink flesh", "Washes away residual blood, gall residues, and microscopic bacteria"]
                            ]
                        }
                    }
                ],
                # Page 4: Interactive Scaling & Gutting Sequencing
                [
                    {
                        "type": "interactive_scenario",
                        "title": "Fish Processing Sequencing Challenge",
                        "content": {
                            "title": "Ordering Fish Processing Steps",
                            "instructions": "Arrange the practical fish dressing steps in the correct chronological order:",
                            "scenario": "You have a fresh tilapia on a clean cutting board ready to prepare for cooking.",
                            "question": "What is the correct sequence of actions?",
                            "options": [
                                "1. Hold tail with clean cloth -> 2. Scrape scales tail to head -> 3. Shallow slit from vent to under-jaw -> 4. Pull out guts and gills -> 5. Rinse cavity under cold tap water",
                                "1. Slit belly deep into intestines -> 2. Fry with scales on -> 3. Scrape scales off cooked fish",
                                "1. Leave fish in hot sun for 2 days -> 2. Cut off head -> 3. Wash intestines with oil",
                                "1. Dip live fish in hot boiling grease"
                            ],
                            "correct_feedback": "Correct! Always secure the tail first, scrape scales tail-to-head, make a shallow belly slit from the vent, pull the viscera mass intact, and rinse the cavity thoroughly.",
                            "incorrect_feedback": "Incorrect. Follow the hygienic order: Grip tail -> Descale tail-to-head -> Shallow vent slit -> Extract guts intact -> Rinse cavity."
                        }
                    }
                ],
                # Page 5: Formative Knowledge Check
                [
                    {
                        "type": "knowledge_check",
                        "title": "Knowledge Check: Shallow Belly Incision Logic",
                        "content": {
                            "question": "Why must a chef make a very shallow slit along the belly midline rather than pushing the knife blade deep into the abdominal cavity?",
                            "options": [
                                "To prevent puncturing the intestines and stomach, which would spill digestive juices and waste onto the meat, contaminating it with bacteria and foul flavors.",
                                "To prevent the knife blade from becoming dull.",
                                "To make the scales fall off faster.",
                                "To allow the fish to swim again."
                            ],
                            "answer": "A",
                            "explanation": "A shallow cut slices only the outer abdominal skin wall, keeping the delicate digestive intestines intact so that fecal waste and digestive enzymes do not contaminate the meat."
                        }
                    }
                ],
                # Page 6: Summary & Connection Forward
                [
                    {
                        "type": "key_takeaway",
                        "title": "Lesson Summary",
                        "content": {
                            "text": "- Inspect fish freshness using **clear eyes, bright red gills, and firm elastic flesh**.\n- **Scaling** removes indigestible calcium plates; always scrape **from tail toward head at 45 degrees**.\n- **Gutting** removes digestive organs to prevent rapid microbial decay and bad odors.\n- Make a **shallow belly incision** starting at the anal vent running forward to the jaw."
                        }
                    },
                    {
                        "type": "transition",
                        "title": "Looking Ahead",
                        "content": {
                            "text": "Now that our fish is scaled, gutted, and clean, how do we season and cook it safely? In Lesson 2, we learn how to score, salt, and safely pan-fry fish without hot oil splatters!"
                        }
                    }
                ],
                # Page 7: Operculum & Gill Removal Callout
                [
                    {
                        "type": "concept_explanation",
                        "title": "Why Gills Must Be Removed",
                        "content": {
                            "title": "The Dirty Filter of the Fish",
                            "text": "Fish gills act as water filters, trapping mud, parasites, and bacteria while absorbing oxygen from pond water. When gutting fish, always reach under the operculum (gill flap) and pull the feathery red gills out along with the digestive viscera. Leaving gills in place imparts a muddy, bitter flavor to soup or fried fish."
                        }
                    }
                ]
            ]
        },

        # =====================================================================
        # LESSON 2: Cleaning, Salting, and Frying Fish
        # =====================================================================
        {
            "unit_order": 2,
            "unit_name": "Cleaning, Salting, and Frying Fish",
            "unit_description": "Final cavity sanitation, deep muscle scoring (slits), moisture control (pat-drying to stop grease splatters), salt curing mechanics, and safe pan-frying techniques.",
            "lesson_title": "Cleaning, Salting, and Frying Fish",
            "pages": [
                # Page 1: Visual Hook & Learning Objectives
                [
                    {
                        "type": "suggested_image",
                        "title": "Culinary Preparation: Scored & Salt-Cured Tilapia",
                        "content": {
                            "title": "Culinary Preparation: Scored & Salt-Cured Tilapia",
                            "caption": "Freshly prepared tilapia with diagonal scores on its thick muscles, seasoned with coarse salt and dried ready for safe pan-frying."
                        }
                    },
                    {
                        "type": "learning_goal",
                        "title": "Learning Objectives: Scoring, Seasoning & Safe Frying",
                        "content": {
                            "title": "What We Will Accomplish Today",
                            "goals": [
                                "Demonstrate how to **score (make diagonal cuts on) thick fish muscles** for even heat and seasoning penetration.",
                                "Explain how **dry salt acts as a moisture extractor and temporary preservative**.",
                                "Perform **pat-drying** to eliminate surface water and prevent explosive hot oil splattering.",
                                "Execute safe **pan-frying protocol**: sliding food away from the body using long tongs."
                            ]
                        }
                    },
                    {
                        "type": "concept_explanation",
                        "title": "The Physics and Safety of Frying",
                        "content": {
                            "title": "Why Water and Hot Oil Do Not Mix",
                            "text": "When water contacts hot cooking oil (180°C), it instantly vaporizes into expanding steam. This rapid steam explosion throws microscopic droplets of scalding oil into the air! Mastering pat-drying and gentle tongs placement ensures cooking is crispy, golden, and 100% safe from burn injuries."
                        }
                    }
                ],
                # Page 2: Scoring & Pat-Drying Dynamics
                [
                    {
                        "type": "concept_explanation",
                        "title": "Scoring Muscles & Surface Moisture Control",
                        "content": {
                            "title": "The 3 Pre-Frying Steps",
                            "text": "- **1. Diagonal Muscle Scoring**: Make 2 to 3 shallow, angled cuts across the thickest part of the fish body on both sides. This allows hot oil, heat, and salt to penetrate deep into the dense spine muscles, preventing raw undercooked centers.\n- **2. Cavity Inspection**: Check that the black kidney bloodline along the inner spine is scraped clean with a teaspoon under cold water.\n- **3. Thorough Pat-Drying**: Use clean paper towels or a dry kitchen cloth to press firmly over the skin and inside the belly cavity until zero surface water remains."
                        }
                    },
                    {
                        "type": "suggested_diagram",
                        "title": "Fish Scoring, Pat-Drying & Safe Pan-Frying Safety Dynamics",
                        "content": {
                            "title": "Fish Scoring, Pat-Drying & Safe Pan-Frying Safety Dynamics",
                            "caption": "Culinary physics diagram: 1. Diagonal scores (even heat & salt penetration) -> 2. Pat-drying with cloth (zero water = zero grease splattering) -> 3. Long tongs laying fish gently AWAY from chef into 180°C oil."
                        }
                    }
                ],
                # Page 3: The Science of Salt-Curing & Safe Frying Protocol
                [
                    {
                        "type": "step_process",
                        "title": "Standard Operating Procedure: Salting & Frying",
                        "content": {
                            "title": "How to Season and Fry Fish Safely",
                            "steps": [
                                "**Step 1: Rub Salt**: Rub fine salt into the diagonal scores, over the skin, and inside the belly cavity. Let rest for 5-10 minutes to draw out excess moisture.",
                                "**Step 2: Heat Oil to Medium**: Pour clean vegetable oil 2 cm deep into a dry pan. Heat on medium until a test onion slice sizzles gently (175°C to 185°C).",
                                "**Step 3: Lay Fish Away from Body**: Grip the dried fish with long tongs. Lower it gently into the pan sliding **away from your body** so grease splashes hit the back wall.",
                                "**Step 4: Avoid Overcrowding**: Fry 1 or 2 fish at a time to keep oil temperature high and prevent greasy, soggy fish.",
                                "**Step 5: Flip Once & Drain**: Fry for 5 to 7 minutes until golden brown; flip gently once. Drain on paper towels before serving."
                            ]
                        }
                    }
                ],
                # Page 4: Video Resource — Fish Processing & Cooking
                [
                    {
                        "type": "suggested_video",
                        "title": "Instructional Video: Tilapia Processing, Salting, and Deep-Frying",
                        "content": {
                            "title": "Instructional Video: Tilapia Processing, Salting, and Deep-Frying",
                            "url": "https://www.youtube.com/watch?v=TXJPk-QfhDU",
                            "resolved_video_id": "TXJPk-QfhDU",
                            "caption": "Watch this culinary demonstration showing fresh fish scaling, diagonal scoring, salting, pat-drying, and safe pan-frying techniques in Kenya."
                        }
                    },
                    {
                        "type": "concept_explanation",
                        "title": "Practical Culinary Takeaways from the Video",
                        "content": {
                            "title": "Chef's Workshop Notes",
                            "text": "- **1. Crisp Skin**: Notice how thorough pat-drying creates a crisp, blistered skin without sticking to the pan.\n- **2. Tongs Angle**: Watch how the chef holds tongs at a low angle and slides the fish into the oil smoothly.\n- **3. Bone Heat**: See how the diagonal cuts allow steam to escape from the deep backbone."
                        }
                    }
                ],
                # Page 5: Interactive Kitchen Safety Matching
                [
                    {
                        "type": "interactive_scenario",
                        "title": "Fish Frying Safety Matching Challenge",
                        "content": {
                            "title": "Matching Actions to Safety Reasons",
                            "instructions": "Match the kitchen action to its critical safety rationale:",
                            "scenario": "A student is getting ready to fry a wet, freshly washed whole fish in a pan of smoking oil.",
                            "question": "What is the primary danger if the student drops the wet fish directly toward their chest?",
                            "options": [
                                "The water will cause explosive hot oil spattering directly onto the student's chest and arms, causing severe burns.",
                                "The fish will turn into solid ice.",
                                "The stove will run out of gas instantly.",
                                "The fish scales will grow back."
                            ],
                            "correct_feedback": "Correct! Wet food dropped toward the cook causes violent oil spattering and severe burn injuries. Always pat-dry food and slide it away from your body!",
                            "incorrect_feedback": "Incorrect. Water in hot oil vaporizes explosively, throwing hot oil droplets. Always pat-dry and slide food away from yourself."
                        }
                    }
                ],
                # Page 6: Formative Knowledge Check
                [
                    {
                        "type": "knowledge_check",
                        "title": "Knowledge Check: Purpose of Pat-Drying",
                        "content": {
                            "question": "What is the scientific and safety purpose of pat-drying a raw fish with a clean cloth before lowering it into hot cooking oil?",
                            "options": [
                                "To eliminate surface moisture so water droplets do not vaporize explosively into steam and spatter scalding oil onto the cook.",
                                "To make the fish lighter so it floats on oil.",
                                "To wipe away the fish bones.",
                                "To cool the frying pan down."
                            ],
                            "answer": "A",
                            "explanation": "Water contacting 180°C oil turns to steam instantly, causing violent spitting and spattering. Drying the surface guarantees clean, safe, splatter-free frying."
                        }
                    }
                ],
                # Page 7: Summary & Connection Forward
                [
                    {
                        "type": "key_takeaway",
                        "title": "Lesson Summary",
                        "content": {
                            "text": "- **Score thick muscles diagonally** to ensure uniform cooking and deep salt penetration.\n- **Pat-dry fish thoroughly** to eliminate water and prevent explosive grease splattering.\n- **Salting** draws out tissue moisture, firms the flesh, and provides temporary preservation.\n- Use **long tongs and slide food away from you** into medium-hot cooking oil."
                        }
                    },
                    {
                        "type": "transition",
                        "title": "Looking Ahead",
                        "content": {
                            "text": "We have mastered fish preparation! In Lesson 3, we transition to livestock processing: studying the ethical, humane, and sanitary methods of slaughtering and defeathering poultry!"
                        }
                    }
                ]
            ]
        },

        # =====================================================================
        # LESSON 3: Poultry Slaughtering and Defeathering
        # =====================================================================
        {
            "unit_order": 3,
            "unit_name": "Poultry Slaughtering and Defeathering",
            "unit_description": "Animal welfare ethics, humane stunning principles, rapid neck jugular cut for complete bleeding, hot-water scalding temperature control (60°C to 65°C), and tear-free plucking techniques.",
            "lesson_title": "Poultry Slaughtering and Defeathering",
            "pages": [
                # Page 1: Visual Hook & Learning Objectives
                [
                    {
                        "type": "suggested_image",
                        "title": "Ethical Processing: Hygienic Poultry Restraining Cone",
                        "content": {
                            "title": "Ethical Processing: Hygienic Poultry Restraining Cone",
                            "caption": "A clean, stainless-steel poultry restraining cone setup designed for humane, stress-free slaughter and rapid bleeding."
                        }
                    },
                    {
                        "type": "learning_goal",
                        "title": "Learning Objectives: Humane Slaughter & Scalding",
                        "content": {
                            "title": "What We Will Accomplish Today",
                            "goals": [
                                "Explain the **animal welfare and ethical principles** of humane poultry handling.",
                                "Describe the **stunning and rapid bleeding protocol** to prevent animal suffering and meat spoilage.",
                                "Control hot-water scalding temperature precisely at **60°C to 65°C for 45 to 60 seconds**.",
                                "Demonstrate clean **plucking technique pulling in the direction of feather growth** to avoid tearing skin."
                            ]
                        }
                    },
                    {
                        "type": "concept_explanation",
                        "title": "Compassion in Agricultural Education",
                        "content": {
                            "title": "Respecting Farm Animals",
                            "text": "Livestock birds feel fear and pain. In CBC Agriculture, we treat animals with dignity and compassion throughout their lives. When preparing poultry for food, slaughter must be swift, painless, stress-free, and executed in a clinical, sanitary environment."
                        }
                    }
                ],
                # Page 2: Humane Stunning & Complete Bleeding
                [
                    {
                        "type": "concept_explanation",
                        "title": "The Stunning Principle & Bleeding Dynamics",
                        "content": {
                            "title": "Why Complete Bleeding is Critical",
                            "text": "- **Humane Stunning**: A swift, precise mechanical blow to the back of the head renders the bird instantly unconscious so it feels zero pain during the cut.\n- **The Jugular Incision**: Using a razor-sharp knife, cut the jugular vein and carotid artery on the side of the neck just behind the jaw. Do not sever the windpipe completely.\n- **Complete Bleeding**: Place the bird head-down in a restraining cone for 2 to 3 minutes. Residual blood in muscle tissues acts as a breeding ground for bacteria, turning meat dark, bloody, and sour within hours."
                        }
                    },
                    {
                        "type": "suggested_diagram",
                        "title": "Humane Poultry Stunning, Rapid Bleeding & 60-65°C Scalding Temperature Matrix",
                        "content": {
                            "title": "Humane Poultry Stunning, Rapid Bleeding & 60-65°C Scalding Temperature Matrix",
                            "caption": "Poultry dressing workflow: 1. Humane stunning & head-down cone placement -> 2. Rapid jugular bleed (2-3 mins) -> 3. Scald in 60°C-65°C water (45-60s) -> 4. Wet plucking pulling with feather grain -> 5. Blue flame singeing of hair feathers."
                        }
                    }
                ],
                # Page 3: Hot-Water Scalding Science (60°C - 65°C)
                [
                    {
                        "type": "comparison_table",
                        "title": "Scalding Water Temperature Comparison",
                        "content": {
                            "title": "Scalding Temperature Control Matrix",
                            "headers": ["Water Temperature", "Physical Effect on Feather Follicles", "Physical Effect on Skin & Meat Quality", "Recommendation"],
                            "rows": [
                                ["Below 55°C (Too Cold)", "Follicle muscles remain tight & constricted", "Feathers extremely difficult to pull; tears skin", "Unacceptable (Ineffective)"],
                                ["60°C to 65°C (Optimum)", "Relaxes feather follicle muscles smoothly", "Skin remains intact, smooth, and elastic; easy plucking", "Recommended Standard (45-60s dip)"],
                                ["Above 75°C - 100°C (Boiling)", "Follicles overcook immediately", "Outer epidermal skin cooks, blisters, and tears off completely, exposing raw meat to bacterial contamination", "Strictly Forbidden (Ruint Carcass)"]
                            ]
                        }
                    }
                ],
                # Page 4: Defeathering (Plucking) & Singeing Technique
                [
                    {
                        "type": "step_process",
                        "title": "Standard Operating Procedure: Defeathering",
                        "content": {
                            "title": "Step-by-Step Defeathering Workflow",
                            "steps": [
                                "**Step 1: Submerge in Scald Pot**: Hold bird by feet and submerge in 60°C-65°C water for 45-60 seconds, swirling gently so water penetrates under wings.",
                                "**Step 2: Pluck Immediately**: Remove from water and pluck while follicles are warm and dilated.",
                                "**Step 3: Pull Large Feathers First**: Strip large flight feathers from wings and tail first (hardest to remove).",
                                "**Step 4: Pluck with the Grain**: Pull breast, back, and neck feathers in the natural direction they grow to avoid ripping delicate skin.",
                                "**Step 5: Singeing**: Pass the carcass quickly over a clean blue gas flame to burn off tiny hair-like pinfeathers (filoplumes)."
                            ]
                        }
                    }
                ],
                # Page 5: Formative Knowledge Check
                [
                    {
                        "type": "knowledge_check",
                        "title": "Knowledge Check: Water Temperature in Poultry Scalding",
                        "content": {
                            "question": "What happens if a slaughtered chicken is dipped into 100°C boiling water instead of 60°C to 65°C warm water during scalding?",
                            "options": [
                                "The boiling water cooks and softens the outer skin, causing it to tear and rip away during plucking, exposing meat to dirt and bacteria.",
                                "The feathers become impossible to pull.",
                                "The chicken bones dissolve into liquid.",
                                "The chicken turns into a live bird."
                            ],
                            "answer": "A",
                            "explanation": "Boiling water cooks the delicate epidermal skin, causing it to tear into shreds during plucking. Optimum warm water (60°C–65°C) relaxes follicles without cooking the skin."
                        }
                    }
                ],
                # Page 6: Summary & Connection Forward
                [
                    {
                        "type": "key_takeaway",
                        "title": "Lesson Summary",
                        "content": {
                            "text": "- **Humane slaughter** requires swift, painless stunning and rapid jugular vein bleeding.\n- Complete **head-down bleeding** prevents meat spoilage and off-flavors.\n- **Scald in 60°C to 65°C water for 45 to 60 seconds** to relax feather follicles smoothly.\n- **Pluck in the direction of feather growth** and singe filoplumes over a clean flame."
                        }
                    },
                    {
                        "type": "transition",
                        "title": "Looking Ahead",
                        "content": {
                            "text": "The outside of the chicken is clean and plucked. In Lesson 4, we enter the abdominal cavity: mastering the delicate procedure of gutting, giblet cleaning, and carcass draining!"
                        }
                    }
                ],
                # Page 7: Restraining Cone Biosecurity Callout
                [
                    {
                        "type": "concept_explanation",
                        "title": "Restraining Cone Hygiene",
                        "content": {
                            "title": "Why Cones Prevent Bruising",
                            "text": "Holding a flapping chicken by hand during bleeding causes severe muscle wing flapping, which ruptures capillaries and creates dark red blood bruises on breast meat. A restraining cone gently holds the bird's wings in place, preventing wing fractures and ensuring premium, unbruised white meat."
                        }
                    }
                ]
            ]
        },

        # =====================================================================
        # LESSON 4: Gutting, Cleaning, and Draining Chicken
        # =====================================================================
        {
            "unit_order": 4,
            "unit_name": "Gutting, Cleaning, and Draining Chicken",
            "unit_description": "Poultry evisceration anatomy, vent isolation cut, edible giblets (gizzard, liver, heart), gallbladder bile hazard, neck crop extraction, and upside-down carcass drainage.",
            "lesson_title": "Gutting, Cleaning, and Draining Chicken",
            "pages": [
                # Page 1: Visual Hook & Learning Objectives
                [
                    {
                        "type": "suggested_image",
                        "title": "Giblets Identification: Clean Liver, Heart & Gizzard",
                        "content": {
                            "title": "Giblets Identification: Clean Liver, Heart & Gizzard",
                            "caption": "Cleaned, high-value edible poultry offal (liver, heart, and gizzard) arranged neatly on a sanitized prep tray."
                        }
                    },
                    {
                        "type": "learning_goal",
                        "title": "Learning Objectives: Evisceration & Cavity Drainage",
                        "content": {
                            "title": "What We Will Accomplish Today",
                            "goals": [
                                "Execute a clean **horizontal vent incision** to access the abdominal cavity safely.",
                                "Classify internal organs into **edible giblets (gizzard, liver, heart)** vs **inedible waste (intestines, lungs)**.",
                                "Safely excise the green **gallbladder from the liver without puncturing bitter bile**.",
                                "Extract the **neck crop** and demonstrate **upside-down carcass suspension for complete drainage**."
                            ]
                        }
                    },
                    {
                        "type": "concept_explanation",
                        "title": "Surgical Precision in the Kitchen",
                        "content": {
                            "title": "The Delicate Anatomy of Evisceration",
                            "text": "Evisceration (gutting) requires careful attention to anatomy. Inside the bird lies the digestive tract filled with feed, bacteria, and concentrated green bile. Puncturing the gallbladder or crop ruins the taste and safety of the entire carcass, while proper evisceration yields delicious meat and valuable giblets!"
                        }
                    }
                ],
                # Page 2: Internal Organ Anatomy & The Gallbladder Hazard
                [
                    {
                        "type": "concept_explanation",
                        "title": "Anatomy of Poultry Organs & The Bile Hazard",
                        "content": {
                            "title": "Recognizing Organs & Hazards",
                            "text": "- **1. The Gallbladder Hazard**: Attached to the underside of the liver is a small, dark green sac called the **gallbladder**, containing bitter green bile. You must gently slice the gallbladder away from the liver without puncturing it. If punctured, bile permanently stains breast and liver meat green, giving it an intolerable bitter taste.\n- **2. The Gizzard (Muscular Stomach)**: Cut the gizzard free from intestines. Slit it open down the center, wash out the gravel stones and feed particles, and peel away the tough yellow inner keratin lining.\n- **3. The Neck Crop**: Reach into the neck opening to locate the crop (the food storage pouch). Loosen it from the skin and pull it out intact with the windpipe."
                        }
                    },
                    {
                        "type": "suggested_diagram",
                        "title": "Poultry Evisceration Anatomy, Gallbladder Hazard & Upside-Down Drainage Rig",
                        "content": {
                            "title": "Poultry Evisceration Anatomy, Gallbladder Hazard & Upside-Down Drainage Rig",
                            "caption": "Evisceration anatomy guide: 1. Horizontal vent incision -> 2. Gallbladder excising warning (green bile sac attached to liver) -> 3. Gizzard peeling -> 4. Neck crop extraction -> 5. Upside-down carcass suspension (draining moisture to prevent rot)."
                        }
                    }
                ],
                # Page 3: Organ Classification Matrix
                [
                    {
                        "type": "comparison_table",
                        "title": "Poultry Organ Classification & Utilization",
                        "content": {
                            "title": "Poultry Viscera Classification Matrix",
                            "headers": ["Organ Name", "Anatomical Function", "Classification", "Preparation & Disposal Protocol"],
                            "rows": [
                                ["Liver", "Blood filtration & nutrient storage", "Edible Giblet (High Value)", "Cut away gallbladder cleanly; wash in cold water"],
                                ["Gizzard", "Muscular grinding stomach (uses stones)", "Edible Giblet (High Value)", "Slice open, wash out stones, peel yellow inner lining"],
                                ["Heart", "Blood circulation pump", "Edible Giblet", "Trim major blood vessels and rinse inner blood clots"],
                                ["Gallbladder", "Bile storage sac (bitter digestive juice)", "Hazardous Waste (Inedible)", "Excise carefully without puncturing; discard in waste bin"],
                                ["Crop & Windpipe", "Swallowed food storage & respiration", "Waste / High Risk", "Pull out from neck opening intact without tearing"],
                                ["Intestines", "Nutrient digestion & fecal waste", "Inedible Waste", "Discard immediately in covered bin (never leave on board)"]
                            ]
                        }
                    }
                ],
                # Page 4: Practical Video — Poultry Dressing & Evisceration
                [
                    {
                        "type": "suggested_video",
                        "title": "Practical Video: Grade 8 Agriculture Poultry Dressing & Gutting",
                        "content": {
                            "title": "Practical Video: Grade 8 Agriculture Poultry Dressing & Gutting",
                            "url": "https://www.youtube.com/watch?v=6ZjkLwQt_YE",
                            "resolved_video_id": "6ZjkLwQt_YE",
                            "caption": "Watch this step-by-step practical demonstration on poultry evisceration, safe gallbladder removal, gizzard peeling, and carcass drainage in Kenya."
                        }
                    },
                    {
                        "type": "concept_explanation",
                        "title": "Field Workshop Reminders from the Video",
                        "content": {
                            "title": "Hygiene & Drainage Rules",
                            "text": "- **1. Two Chopping Boards**: Notice how the instructor uses one board for raw carcass cutting and a separate sterilized board for edible giblets.\n- **2. The Drainage Hook**: Observe how carcasses are suspended upside down for 15 to 20 minutes so all cavity wash water drips away.\n- **3. Waste Disposal**: Watch how all inedible viscera are placed directly into a sealed bin to prevent attracting houseflies."
                        }
                    }
                ],
                # Page 5: Interactive Organ Classification Challenge
                [
                    {
                        "type": "interactive_scenario",
                        "title": "Poultry Organ Classification Challenge",
                        "content": {
                            "title": "Sorting Edible Giblets from Hazardous Waste",
                            "instructions": "Determine the correct category for each organ:",
                            "scenario": "You have extracted the internal viscera mass from a dressed chicken carcass.",
                            "question": "Which organ must be handled with extreme care and discarded because puncturing it will ruin the meat with bitter green liquid?",
                            "options": [
                                "The Gallbladder (contains bitter green bile that permanently stains and spoils meat flavor).",
                                "The Gizzard.",
                                "The Heart.",
                                "The Liver."
                            ],
                            "correct_feedback": "Correct! The gallbladder contains bitter green bile. Puncturing it stains the meat green and imparts a permanent, intolerable bitter flavor.",
                            "incorrect_feedback": "Incorrect. The gizzard, heart, and liver are edible giblets. The gallbladder contains bitter green bile and is hazardous waste."
                        }
                    }
                ],
                # Page 6: Formative Knowledge Check
                [
                    {
                        "type": "knowledge_check",
                        "title": "Knowledge Check: Carcass Suspension Drainage",
                        "content": {
                            "question": "Why must a freshly gutted and washed poultry carcass be hung upside down by its legs for 15 to 20 minutes before refrigeration or cooking?",
                            "options": [
                                "To allow all internal wash water and residual blood to drain out completely, preventing stagnant moisture pools where rot-causing bacteria multiply.",
                                "To make the chicken feathers grow back.",
                                "To stretch the bird's neck bones.",
                                "To cool the stove burners."
                            ],
                            "answer": "A",
                            "explanation": "Hanging the carcass upside down drains trapped cavity wash water and residual blood. Stagnant moisture pools inside the cavity breed spoilage bacteria rapidly."
                        }
                    }
                ],
                # Page 7: Summary & Connection Forward
                [
                    {
                        "type": "key_takeaway",
                        "title": "Lesson Summary",
                        "content": {
                            "text": "- Make a shallow **horizontal vent incision** to access the abdominal cavity.\n- Excise the green **gallbladder carefully without puncturing bitter bile**.\n- Clean the **gizzard by washing out stones and peeling the yellow keratin lining**.\n- Extract the **neck crop intact** and hang the carcass **upside down to drain moisture**."
                        }
                    },
                    {
                        "type": "transition",
                        "title": "Looking Ahead",
                        "content": {
                            "text": "Now that our meat is processed, how do we keep it fresh for weeks without electricity? In Lesson 5, we explore the science of preserving meat by salting and boiling!"
                        }
                    }
                ]
            ]
        },

        # =====================================================================
        # LESSON 5: Preserving Meat by Salting and Boiling
        # =====================================================================
        {
            "unit_order": 5,
            "unit_name": "Preserving Meat by Salting and Boiling",
            "unit_description": "Principles of meat preservation without refrigeration, osmotic dehydration via dry-salting, thermal pathogen destruction via boiling (parboiling), and comparative shelf-life.",
            "lesson_title": "Preserving Meat by Salting and Boiling",
            "pages": [
                # Page 1: Visual Hook & Learning Objectives
                [
                    {
                        "type": "suggested_image",
                        "title": "Traditional Food Security: Salt-Cured Beef Strips",
                        "content": {
                            "title": "Traditional Food Security: Salt-Cured Beef Strips",
                            "caption": "Lean strips of beef heavily coated in coarse dry salt crystals on a wooden board, drawing out moisture to prevent bacterial decay."
                        }
                    },
                    {
                        "type": "learning_goal",
                        "title": "Learning Objectives: Salting & Boiling Preservation",
                        "content": {
                            "title": "What We Will Accomplish Today",
                            "goals": [
                                "Explain how **osmosis in dry-salting** draws out cellular water to dehydrate and destroy bacteria.",
                                "Describe how **boiling at 100°C** destroys active pathogens and denatures tissue enzymes.",
                                "Execute safe **parboiling of meat cubes** in salted water for 15 to 20 minutes.",
                                "Compare the **shelf life, fuel requirements, and pre-cooking preparation** of salting versus boiling."
                            ]
                        }
                    },
                    {
                        "type": "concept_explanation",
                        "title": "Preservation Without Electricity",
                        "content": {
                            "title": "Saving Food for the Future",
                            "text": "In many rural communities across Kenya, households live off-grid without electrical refrigeration. When large livestock is slaughtered, fresh meat must be preserved immediately to prevent fly strikes, bacterial rot, and food poisoning. Salting and boiling are two low-cost, highly effective household preservation techniques."
                        }
                    }
                ],
                # Page 2: The Osmotic Science of Dry-Salting
                [
                    {
                        "type": "concept_explanation",
                        "title": "The Biological Mechanism of Salt Dehydration",
                        "content": {
                            "title": "How Salt Kills Rot-Causing Bacteria",
                            "text": "- **Water Activity ($$a_w$$)**: Bacteria require available free water in meat tissue to metabolize, divide, and rot food.\n- **Osmosis**: When raw meat strips (1 cm thick) are coated in coarse dry salt, the high salt concentration outside bacterial cells pulls water out through their cell membranes.\n- **Plasmolysis & Death**: The bacterial cells lose their internal water, shrink (plasmolyze), and die or become completely dormant!\n- **Slanted Drainage Board**: Always place salted meat on a slanted wooden board so the extracted cellular wastewater drains away safely."
                        }
                    },
                    {
                        "type": "suggested_diagram",
                        "title": "Meat Dehydration via Osmotic Dry-Salting & Thermal Pathogen Destruction Matrix",
                        "content": {
                            "title": "Meat Dehydration via Osmotic Dry-Salting & Thermal Pathogen Destruction Matrix",
                            "caption": "Preservation science diagram: 1. Osmosis (salt draws moisture out of meat & bacteria cells) -> 2. Slanted drainage board -> 3. Thermal boiling at 100°C (denaturing enzymes & killing active germs) -> 4. Soaking salted meat in water before cooking."
                        }
                    }
                ],
                # Page 3: The Thermal Science of Boiling (Parboiling)
                [
                    {
                        "type": "concept_explanation",
                        "title": "Thermal Pathogen Destruction by Boiling",
                        "content": {
                            "title": "How Parboiling Extends Meat Shelf Life",
                            "text": "- **High-Temperature Sterilization**: Submerging cubed meat in salted boiling water at 100°C for 15 to 20 minutes destroys surface vegetative bacteria, mold spores, and parasitic cysts.\n- **Enzyme Inactivation**: Heat denatures natural muscle enzymes that would otherwise break down proteins and cause meat tissue to soften and rot.\n- **Draining & Clean Air Storage**: After boiling, drain all water completely and store the cooked meat in a clean, dust-free wire mesh basket in a cool, ventilated larder."
                        }
                    },
                    {
                        "type": "comparison_table",
                        "title": "Dry-Salting vs. Boiling Comparison Matrix",
                        "content": {
                            "title": "Meat Preservation Trade-Off Matrix",
                            "headers": ["Preservation Method", "Primary Mechanism", "Estimated Shelf Life", "Fuel / Energy Needed", "Pre-Cooking Requirement"],
                            "rows": [
                                ["Dry-Salting", "Osmotic moisture extraction; cellular dehydration", "2 to 4 Weeks", "Zero fuel / Zero fire needed", "Must soak in clean water to wash out excess salt before cooking"],
                                ["Boiling (Parboiling)", "Thermal destruction of microbes & enzymes at 100°C", "2 to 4 Days (Short term)", "Requires firewood, charcoal, or gas fuel", "Ready to fry or stew directly without soaking"]
                            ]
                        }
                    }
                ],
                # Page 4: Interactive Method Selection Challenge
                [
                    {
                        "type": "interactive_scenario",
                        "title": "Off-Grid Preservation Selection Challenge",
                        "content": {
                            "title": "Choosing Between Salting and Boiling",
                            "instructions": "Select the best preservation method based on household resources:",
                            "scenario": "A rural homestead has just received 10 kg of raw beef, but they have completely run out of cooking gas, charcoal, and firewood, and have no refrigerator.",
                            "question": "Which preservation method must the family use to save their beef from rotting?",
                            "options": [
                                "Dry-Salting: Cut into thin strips and rub heavily with coarse dry salt on a slanted board (requires zero fire or fuel).",
                                "Boiling in a cold pot with no fire.",
                                "Leaving raw meat in a plastic bag on the floor.",
                                "Washing meat with mud."
                            ],
                            "correct_feedback": "Correct! Dry-salting requires zero firewood or electricity, making it the premier emergency preservation method when fuel is unavailable.",
                            "incorrect_feedback": "Incorrect. Without fire or fuel, boiling is impossible. Dry-salting preserves meat via osmosis without needing any heat."
                        }
                    }
                ],
                # Page 5: Formative Knowledge Check
                [
                    {
                        "type": "knowledge_check",
                        "title": "Knowledge Check: Pre-Cooking Salt Soaking",
                        "content": {
                            "question": "Why must dry-salted meat strips always be soaked in fresh clean water for 30 to 60 minutes before being cooked and eaten?",
                            "options": [
                                "To leach out and wash away the heavy excess salt concentration, making the meat healthy, palatable, and pleasant to taste.",
                                "To make the meat turn into fish.",
                                "To wash away the meat protein.",
                                "To cool down the cooking fire."
                            ],
                            "answer": "A",
                            "explanation": "Preservation requires a heavy coat of salt that makes raw cured meat far too salty to consume directly. Soaking in fresh water removes excess salt before cooking."
                        }
                    }
                ],
                # Page 6: Summary & Connection Forward
                [
                    {
                        "type": "key_takeaway",
                        "title": "Lesson Summary",
                        "content": {
                            "text": "- **Dry-salting** preserves meat via **osmosis**, pulling out moisture to dehydrate bacteria.\n- Salted meat lasts **2 to 4 weeks** without fire or electricity; soak in water before cooking.\n- **Boiling at 100°C** destroys active pathogens and extends shelf life for **2 to 4 days**.\n- Always use **slanted boards** for salting to let extracted wastewater drain away safely."
                        }
                    },
                    {
                        "type": "transition",
                        "title": "Looking Ahead",
                        "content": {
                            "text": "What if we want meat to last for months instead of weeks? In Lesson 6, we master the traditional arts of sun-drying (biltong/nyirinyiri) and aromatic hardwood smoking!"
                        }
                    }
                ],
                # Page 7: Fly Screen Sanitation Callout
                [
                    {
                        "type": "concept_explanation",
                        "title": "Biosecurity Against Blowflies",
                        "content": {
                            "title": "Protecting Cured Meat from Maggots",
                            "text": "Bluebottle blowflies are attracted to the scent of curing meat. If a fly lands on salted meat, it lays hundreds of microscopic eggs that hatch into maggots within 12 hours. Always cure and drain meat beneath a clean, tightly secured mosquito net or wire mesh food safe."
                        }
                    }
                ]
            ]
        },

        # =====================================================================
        # LESSON 6: Preserving Meat by Drying and Smoking
        # =====================================================================
        {
            "unit_order": 6,
            "unit_name": "Preserving Meat by Drying and Smoking",
            "unit_description": "Solar radiation dehydration (sun-drying thin strips, moisture drop <10%), chemistry of wood smoke (phenols and organic acids), hardwood vs toxic softwood resins, and traditional African smoke chambers.",
            "lesson_title": "Preserving Meat by Drying and Smoking",
            "pages": [
                # Page 1: Visual Hook & Learning Objectives
                [
                    {
                        "type": "suggested_image",
                        "title": "Traditional Preservation: Solar Drying Meat Lines",
                        "content": {
                            "title": "Traditional Preservation: Solar Drying Meat Lines",
                            "caption": "Thin strips of lean beef hanging on wire lines under intense equatorial sunlight, dehydrating into shelf-stable dry meat (nyirinyiri/biltong)."
                        }
                    },
                    {
                        "type": "learning_goal",
                        "title": "Learning Objectives: Solar Drying & Wood Smoking",
                        "content": {
                            "title": "What We Will Accomplish Today",
                            "goals": [
                                "Explain how **solar heat and wind currents** evaporate water to drop meat moisture below 10%.",
                                "Describe how **hardwood smoke deposits antimicrobial phenols and organic acids** onto meat.",
                                "Distinguish **safe burning hardwoods (acacia, fruitwoods)** from **toxic resinous softwoods (pine, cypress)**.",
                                "Demonstrate clean **thin slicing (5 mm)** and fly netting protection."
                            ]
                        }
                    },
                    {
                        "type": "concept_explanation",
                        "title": "Solar Energy & Smoke Chemistry",
                        "content": {
                            "title": "Ancient Indigenous Food Technology",
                            "text": "For centuries, pastoralist communities across Kenya (like the Maasai, Turkana, and Borana) have utilized natural sunlight and aromatic wood smoke to create shelf-stable meat (nyirinyiri). Solar drying physically removes water, while wood smoking coats meat in natural chemical shields that repel insects and kill microbes for months!"
                        }
                    }
                ],
                # Page 2: The Physical Science of Solar Drying
                [
                    {
                        "type": "concept_explanation",
                        "title": "Solar Evaporation Dynamics",
                        "content": {
                            "title": "Dehydrating Meat to Below 10% Moisture",
                            "text": "- **Microbial Moisture Limit**: Bacteria cannot reproduce or survive when meat moisture falls below 15%.\n- **Thin Slicing**: Slice lean meat along muscle fibers into thin strips (5 mm thick). Thin cuts allow solar heat and breezes to penetrate to the core quickly.\n- **Solar Wire Lines**: Hang strips on wire lines in direct hot sun for 3 to 5 days. Cover with light mesh netting to block blowflies and dust.\n- **Result**: Meat turns dark, stiff, and snaps when bent, remaining edible for up to 6 months without refrigeration!"
                        }
                    },
                    {
                        "type": "suggested_diagram",
                        "title": "Solar Radiation Dehydration vs Hardwood Phenol Wood-Smoking Comparison",
                        "content": {
                            "title": "Solar Radiation Dehydration vs Hardwood Phenol Wood-Smoking Comparison",
                            "caption": "Comparative diagram: Left: Solar Drying (UV rays + wind reduce moisture to <10%) • Right: Wood Smoking (Acacia hardwood coals produce phenols & organic acids that kill bacteria & prevent fat rancidity. Warning: NO resinous pine!)."
                        }
                    }
                ],
                # Page 3: The Chemical Science of Wood-Smoking
                [
                    {
                        "type": "concept_explanation",
                        "title": "Antimicrobial Chemistry of Wood Smoke",
                        "content": {
                            "title": "How Hardwood Smoke Preserves Meat",
                            "text": "- **1. Natural Phenols**: Burning hardwood releases **phenolic compounds** that act as powerful natural germicides, destroying surface bacteria and fungi.\n- **2. Organic Acids**: Smoke deposits acetic and formic acids, creating a thin acidic shield that halts bacterial multiplication.\n- **3. Anti-Rancidity Antioxidants**: Smoke chemicals prevent meat fats from reacting with oxygen (oxidative rancidity), stopping foul sour smells.\n- **4. Hardwood vs. Toxic Softwoods**: Always use seasoned **hardwood** (acacia, mango, guava). **NEVER use pine, cypress, or cedar**—softwoods contain sticky sap and toxic resins that coat meat in bitter black soot and poisonous chemical residues!"
                        }
                    },
                    {
                        "type": "comparison_table",
                        "title": "Sun-Drying vs. Wood-Smoking Comparison",
                        "content": {
                            "title": "Preservation Technology Matrix",
                            "headers": ["Feature", "Sun-Drying (Solar Dehydration)", "Wood-Smoking (Chemical & Thermal)"],
                            "rows": [
                                ["Primary Energy Source", "Solar thermal radiation and atmospheric wind", "Slow-burning hardwood embers (40°C - 50°C)"],
                                ["Active Preservation Agent", "Physical water evaporation (Moisture < 10%)", "Natural chemical phenols, organic acids, and gentle heat"],
                                ["Finished Flavor", "Mild, natural concentrated meat flavor", "Rich, smoky, aromatic woody flavor"],
                                ["Fuel Type Required", "Zero fuel (100% renewable solar power)", "Hardwoods only (Acacia, fruitwoods; NO pine/cypress)"],
                                ["Shelf Life", "3 to 6 Months in dry containers", "2 to 4 Months in ventilated larders"]
                            ]
                        }
                    }
                ],
                # Page 4: Interactive Wood Selection Challenge
                [
                    {
                        "type": "interactive_scenario",
                        "title": "Wood Selection for Smoking Challenge",
                        "content": {
                            "title": "Selecting Safe Firewood for Meat Smoking",
                            "instructions": "Evaluate the firewood choices for smoking meat:",
                            "scenario": "A student finds three types of wood offcuts near a workshop: dry acacia hardwood branch, seasoned guava wood, and fresh pine timber dripping with sticky resin.",
                            "question": "Which wood MUST BE STRICTLY AVOIDED for smoking food, and why?",
                            "options": [
                                "Pine wood: It contains sticky resins that produce toxic, bitter black soot that ruins food flavor and is unsafe to eat.",
                                "Acacia wood: It burns too clean.",
                                "Guava wood: It produces a pleasant aroma.",
                                "All woods are identical."
                            ],
                            "correct_feedback": "Correct! Softwoods like pine and cypress contain resinous sap that releases toxic, bitter soot and tar compounds, ruining meat safety and flavor.",
                            "incorrect_feedback": "Incorrect. Pine wood contains sticky resin that produces bitter, toxic smoke. Always use hardwoods like acacia or guava."
                        }
                    }
                ],
                # Page 5: Formative Knowledge Check
                [
                    {
                        "type": "knowledge_check",
                        "title": "Knowledge Check: Role of Phenols in Wood Smoke",
                        "content": {
                            "question": "What is the scientific function of phenolic chemical compounds deposited onto meat during hardwood smoking?",
                            "options": [
                                "They act as powerful natural germicides that kill surface bacteria and prevent fats from turning rancid.",
                                "They turn the meat into sweet sugar candy.",
                                "They make the meat absorb rainwater.",
                                "They dissolve the meat bones."
                            ],
                            "answer": "A",
                            "explanation": "Natural phenols in hardwood smoke act as germicides (killing bacteria and molds) and antioxidants (preventing fat oxidation and rancidity)."
                        }
                    }
                ],
                # Page 6: Summary & Connection Forward
                [
                    {
                        "type": "key_takeaway",
                        "title": "Lesson Summary",
                        "content": {
                            "text": "- **Sun-drying** evaporates moisture below 10%, stopping all microbial activity for months.\n- Slice meat into **thin 5 mm strips** and hang under **protective fly netting**.\n- **Wood-smoking** deposits **antimicrobial phenols and acids** that preserve meat and prevent rancidity.\n- **Burn hardwoods (acacia/fruitwoods) only**; strictly avoid resinous softwoods (pine/cypress)."
                        }
                    },
                    {
                        "type": "transition",
                        "title": "Looking Ahead",
                        "content": {
                            "text": "We have mastered meat preservation. Now, let's explore another vital livestock product: raw fresh milk! In Lesson 7, we explore the science and kitchen safety of preserving milk by boiling!"
                        }
                    }
                ],
                # Page 7: Hermetic Container Storage Callout
                [
                    {
                        "type": "concept_explanation",
                        "title": "Storing Dried Meat in Humid Weather",
                        "content": {
                            "title": "Preventing Re-Hydration",
                            "text": "Dried meat (biltong/nyirinyiri) is a sponge for atmospheric moisture! If left in humid air, it absorbs water vapor and molds will grow within days. Always store completely dry meat in clean, airtight (hermetic) glass jars or sealed tins with tight lids."
                        }
                    }
                ]
            ]
        },

        # =====================================================================
        # LESSON 7: Preserving Milk by Boiling
        # =====================================================================
        {
            "unit_order": 7,
            "unit_name": "Preserving Milk by Boiling",
            "unit_description": "Dairy microbiology, rapid lactose-to-lactic acid souring, milk pasteurization at 100°C for 2-3 minutes, pathogen destruction (Tuberculosis & Brucellosis), stir-aeration to break protein skin, and container scalding.",
            "lesson_title": "Preserving Milk by Boiling",
            "pages": [
                # Page 1: Visual Hook & Learning Objectives
                [
                    {
                        "type": "suggested_image",
                        "title": "Kitchen Thermal Processing: Boiling Fresh Cow's Milk",
                        "content": {
                            "title": "Kitchen Thermal Processing: Boiling Fresh Cow's Milk",
                            "caption": "Fresh raw cow's milk heating in a stainless steel pot on a clean kitchen stove, being stirred to prevent protein skin formation."
                        }
                    },
                    {
                        "type": "learning_goal",
                        "title": "Learning Objectives: Milk Pasteurization & Hygiene",
                        "content": {
                            "title": "What We Will Accomplish Today",
                            "goals": [
                                "Explain why raw milk spoils rapidly due to **lactic acid bacterial fermentation**.",
                                "Describe how **boiling at 100°C for 2 to 3 minutes** destroys pathogens like Tuberculosis and Brucellosis.",
                                "Demonstrate **stir-aeration** to prevent protein skin formation and boil-overs.",
                                "Sanitize storage containers using **scalding boiling water** to prevent re-contamination."
                            ]
                        }
                    },
                    {
                        "type": "concept_explanation",
                        "title": "The Perfect Nutrient Liquid",
                        "content": {
                            "title": "Why Raw Milk is Vulnerable",
                            "text": "Milk is nature's complete food: rich in water (87%), protein (casein), fat, calcium, and milk sugar (**lactose**). Unfortunately, this rich nutrient broth makes raw milk an ideal habitat for bacteria! Left unheated, millions of bacteria consume lactose, produce sour acid, and curdle the milk within hours."
                        }
                    }
                ],
                # Page 2: Microscopic Souring & Thermal Pathogen Destruction
                [
                    {
                        "type": "concept_explanation",
                        "title": "Microbiology of Raw Milk & Disease Risks",
                        "content": {
                            "title": "Zoonotic Disease Risks of Raw Milk",
                            "text": "- **Lactic Acid Bacteria**: Wild bacteria eat lactose ($$\\text{C}_{12}\\text{H}_{22}\\text{O}_{11}$$) and convert it into lactic acid ($$\\text{C}_3\\text{H}_6\\text{O}_3$$). The rising acid drops milk pH, causing milk proteins to clump into sour lumps.\n- **Dangerous Pathogens**: Raw unboiled milk from cows can transmit deadly zoonotic diseases to humans: *Mycobacterium bovis* (Bovine Tuberculosis) and *Brucella abortus* (Brucellosis / Undulant Fever).\n- **Boiling Destruction**: Heating milk to an active rolling boil (100°C) for 2 to 3 minutes pasteurizes the liquid, killing 99.9% of active pathogens and extending room-temperature shelf life to 24-48 hours!"
                        }
                    },
                    {
                        "type": "suggested_diagram",
                        "title": "Milk Pasteurization Thermodynamics, Protein Skin Stir-Aeration & Sterilization Flow",
                        "content": {
                            "title": "Milk Pasteurization Thermodynamics, Protein Skin Stir-Aeration & Sterilization Flow",
                            "caption": "Dairy science flowchart: 1. Raw milk (bacteria eat lactose -> lactic acid) -> 2. Boiling at 100°C (destroys TB & Brucella) -> 3. Stir-aeration (breaks casein skin to stop boil-overs) -> 4. Scalding storage bottle with boiling water -> 5. Cool rapidly & cover."
                        }
                    }
                ],
                # Page 3: Stir-Aeration & Protein Skin Physics
                [
                    {
                        "type": "concept_explanation",
                        "title": "The Physics of Boiling Over & Stir-Aeration",
                        "content": {
                            "title": "Why Milk Boils Over and How to Stop It",
                            "text": "- **Casein Protein Skin**: As milk heats above 60°C, whey and casein proteins denature and float to the surface, forming a tough, rubbery skin across the top of the liquid.\n- **Steam Pressure Explosion**: Steam bubbles rising from the hot pot bottom get trapped beneath this protein skin. Pressure builds rapidly until the steam pushes the entire foaming skin up and over the pot rim, creating a dangerous kitchen mess!\n- **The Stir-Aeration Solution**: Stirring continuously with a clean wooden spoon breaks the surface skin, allowing steam to vent safely. Placing a clean wooden spoon across the pot rim also pops rising foam bubbles."
                        }
                    },
                    {
                        "type": "step_process",
                        "title": "Standard Operating Procedure: Milk Boiling & Storage",
                        "content": {
                            "title": "How to Boil and Store Milk Cleanly",
                            "steps": [
                                "**Step 1: Scald Storage Bottles**: Wash glass or food-grade plastic bottles with hot soapy water, then pour boiling water inside to sterilize them completely.",
                                "**Step 2: Heat with Constant Stirring**: Pour fresh raw milk into a clean pot and heat on medium, stirring continuously to break surface skin.",
                                "**Step 3: Active Boil for 2-3 Minutes**: When milk rises, lower heat slightly and let bubble actively for 2 to 3 minutes.",
                                "**Step 4: Rapid Cooling**: Place the hot pot in a basin of cold tap water to cool down quickly (prevents slow cooked off-flavors).",
                                "**Step 5: Sealed Sterile Storage**: Pour into the scalded bottle, seal tightly with a clean lid, and store in a cool shaded larder."
                            ]
                        }
                    }
                ],
                # Page 4: Interactive Milk Boiling Sequencing Challenge
                [
                    {
                        "type": "interactive_scenario",
                        "title": "Milk Boiling & Sterilization Sequencing Challenge",
                        "content": {
                            "title": "Ordering Milk Boiling Steps",
                            "instructions": "Place the milk handling steps in the correct chronological order:",
                            "scenario": "You have received 3 liters of fresh morning milk directly from the milking shed.",
                            "question": "What is the correct hygienic procedure to preserve this milk?",
                            "options": [
                                "1. Scald storage bottles with boiling water -> 2. Heat milk with constant stirring -> 3. Active boil for 2-3 minutes -> 4. Cool rapidly in cold water bath -> 5. Pour into sterilized bottle and seal",
                                "1. Pour hot boiling milk into dirty unwashed bottles -> 2. Leave pot open in sun for flies",
                                "1. Mix raw unboiled milk with boiled milk -> 2. Drink raw milk directly from cow",
                                "1. Freeze raw unwashed milk with cow hair inside"
                            ],
                            "correct_feedback": "Correct! Always sanitize storage bottles first, stir continuously while boiling for 2-3 minutes, cool rapidly, and seal in sterile containers.",
                            "incorrect_feedback": "Incorrect. Follow the chronological order: Scald bottles -> Heat & stir -> Boil 2-3 mins -> Rapid cool -> Seal in sterile bottle."
                        }
                    }
                ],
                # Page 5: Formative Knowledge Check
                [
                    {
                        "type": "knowledge_check",
                        "title": "Knowledge Check: Reason for Stirring Milk",
                        "content": {
                            "question": "Why must milk be stirred continuously while being heated on a stove?",
                            "options": [
                                "To break the surface protein skin, allowing steam bubbles to escape safely and preventing the milk from boiling over the rim.",
                                "To turn the milk into cheese instantly.",
                                "To make the milk turn blue.",
                                "To add salt to the milk."
                            ],
                            "answer": "A",
                            "explanation": "Stirring prevents a tough casein protein skin from forming over the surface. Without a skin to trap rising steam, the milk will not boil over."
                        }
                    }
                ],
                # Page 6: Summary & Connection Forward
                [
                    {
                        "type": "key_takeaway",
                        "title": "Lesson Summary",
                        "content": {
                            "text": "- Raw milk spoils when bacteria convert **lactose sugar into sour lactic acid**.\n- **Boiling at 100°C for 2 to 3 minutes** pasteurizes milk and destroys TB and Brucellosis.\n- **Stir-aeration** breaks surface protein skin, venting steam and preventing boil-overs.\n- **Scald storage containers with boiling water** before bottling to prevent re-infection."
                        }
                    },
                    {
                        "type": "transition",
                        "title": "Looking Ahead",
                        "content": {
                            "text": "What if you don't have a stove or fuel to boil milk daily? In Lesson 8, we explore natural lactic acid fermentation (making mala/mursik) and low-cost charcoal cooling cabinets!"
                        }
                    }
                ],
                # Page 7: Brucellosis Prevention Callout
                [
                    {
                        "type": "concept_explanation",
                        "title": "Health Warning: Never Drink Raw Milk",
                        "content": {
                            "title": "The Threat of Undulant Fever",
                            "text": "Brucellosis (*Brucella abortus*) is a bacterial infection transmitted through unpasteurized milk. In humans, it causes severe fluctuating fevers, debilitating joint pain, night sweats, and chronic fatigue that lasts for months. Boiling milk thoroughly is a simple, lifesaving habit that eliminates 100% of Brucella bacteria."
                        }
                    }
                ]
            ]
        },

        # =====================================================================
        # LESSON 8: Preserving Milk by Fermentation and Cooling
        # =====================================================================
        {
            "unit_order": 8,
            "unit_name": "Preserving Milk by Fermentation and Cooling",
            "unit_description": "Controlled biological preservation via lactic acid fermentation (sour milk/mala/mursik, drop in pH, crowding out rot microbes), and physical evaporative cooling mechanics of off-grid charcoal coolers (5-10°C drop).",
            "lesson_title": "Preserving Milk by Fermentation and Cooling",
            "pages": [
                # Page 1: Visual Hook & Learning Objectives
                [
                    {
                        "type": "suggested_image",
                        "title": "Traditional Fermentation: Kenyan Milk Calabash Gourds",
                        "content": {
                            "title": "Traditional Fermentation: Kenyan Milk Calabash Gourds",
                            "caption": "Traditional Kenyan gourd calabashes (sotet) sterilized with charcoal embers, used for safe natural lactic acid milk fermentation."
                        }
                    },
                    {
                        "type": "learning_goal",
                        "title": "Learning Objectives: Fermentation & Charcoal Cooling",
                        "content": {
                            "title": "What We Will Accomplish Today",
                            "goals": [
                                "Explain the biological science of **lactic acid fermentation (making mala/mursik)**.",
                                "Describe how low pH (acidity) prevents rot-causing bacteria from multiplying.",
                                "Explain the physical mechanics of **evaporative charcoal coolers (5°C to 10°C drop)**.",
                                "Analyze why low-cost traditional technologies support **rural food security without electricity**."
                            ]
                        }
                    },
                    {
                        "type": "concept_explanation",
                        "title": "Harnessing Biology and Physics",
                        "content": {
                            "title": "Off-Grid Dairy Technologies",
                            "text": "Preserving milk without electricity is one of humanity's greatest agricultural achievements. By utilizing **beneficial bacteria (fermentation)** to create an acidic shield, or using **water evaporation (charcoal coolers)** to absorb ambient heat, rural households can keep dairy nutritious and safe for weeks!"
                        }
                    }
                ],
                # Page 2: The Biological Science of Milk Fermentation
                [
                    {
                        "type": "concept_explanation",
                        "title": "How Lactic Acid Bacteria Protect Milk",
                        "content": {
                            "title": "Biological Warfare in the Gourd",
                            "text": "- **Good Bacteria vs. Bad Bacteria**: When boiled milk is cooled to lukewarm (35°C to 40°C) and poured into a sterilized gourd or clay pot, beneficial lactic acid bacteria (*Lactobacillus bulgaricus* and *Streptococcus thermophilus*) flourish.\n- **The Acid Shield**: These friendly bacteria consume lactose and produce large quantities of **lactic acid**, dropping the milk pH below 4.5. Harmful rot-causing bacteria and food-poisoning germs cannot survive in this acidic environment!\n- **Mala & Mursik**: The milk thickens into a delicious, tangy, protein-dense curd that stays fresh and safe to drink for 2 to 3 weeks at room temperature."
                        }
                    },
                    {
                        "type": "suggested_diagram",
                        "title": "Lactic Acid Fermentation (Mala/Mursik) & Evaporative Charcoal Cooler Architecture",
                        "content": {
                            "title": "Lactic Acid Fermentation (Mala/Mursik) & Evaporative Charcoal Cooler Architecture",
                            "caption": "Dairy tech diagram: Left: Fermentation in Calabash (Lactobacillus turns lactose to lactic acid -> pH drops <4.5 -> rot bacteria die) • Right: Charcoal Cooler (Water tank drips on charcoal mesh walls -> breeze evaporates water -> absorbs heat -> drops internal temp by 5-10°C)."
                        }
                    }
                ],
                # Page 3: The Physics of Evaporative Charcoal Coolers
                [
                    {
                        "type": "concept_explanation",
                        "title": "Off-Grid Charcoal Cooler Engineering",
                        "content": {
                            "title": "How Evaporative Cooling Works Without Electricity",
                            "text": "- **Structure**: A wooden cabinet framed with double wire mesh walls packed with coarse chunks of charcoal.\n- **Drip Irrigation**: A small water reservoir on the roof drips water slowly onto the charcoal walls, keeping them constantly soaked.\n- **Evaporative Physics**: When warm, dry breeze passes through the wet charcoal, water molecules absorb heat energy (latent heat of vaporization) and evaporate into the air.\n- **Temperature Drop**: This evaporation absorbs thermal energy from inside the cabinet, dropping the interior temperature by **5°C to 10°C** below ambient air!\n- **Application**: Perfect for storing boiled milk, eggs, and leafy vegetables fresh for 3 to 5 days in hot, dry regions."
                        }
                    },
                    {
                        "type": "comparison_table",
                        "title": "Milk Preservation Methods Comparison",
                        "content": {
                            "title": "Dairy Preservation Technology Matrix",
                            "headers": ["Method", "Preservation Principle", "Storage Container", "Estimated Shelf Life", "Operating Requirements"],
                            "rows": [
                                ["Boiling", "Thermal sterilization destroys pathogens at 100°C", "Scalded glass/plastic bottle", "1 to 2 Days", "Requires stove & firewood/gas fuel"],
                                ["Fermentation (Mala)", "Lactic acid lowers pH < 4.5; biological crowding", "Sterilized calabash gourd / clay pot", "2 to 3 Weeks", "Warm ambient room (25°C - 35°C)"],
                                ["Charcoal Cooler", "Evaporative cooling drops temp by 5°C - 10°C", "Wet charcoal wire cabinet", "3 to 5 Days", "Dry breeze & continuous clean water drip"]
                            ]
                        }
                    }
                ],
                # Page 4: Video Resource — Off-Grid Dairy Technologies
                [
                    {
                        "type": "suggested_video",
                        "title": "Instructional Video: Milk Fermentation & Low-Cost Charcoal Cooling",
                        "content": {
                            "title": "Instructional Video: Milk Fermentation & Low-Cost Charcoal Cooling",
                            "url": "https://www.youtube.com/watch?v=uFnDdYWgkV8",
                            "resolved_video_id": "uFnDdYWgkV8",
                            "caption": "Watch this field demonstration on traditional milk fermentation in gourds and constructing low-cost evaporative charcoal coolers in Kenya."
                        }
                    },
                    {
                        "type": "concept_explanation",
                        "title": "Key Field Takeaways from the Video",
                        "content": {
                            "title": "Workshop Notes",
                            "text": "- **1. Gourd Sterilization**: Watch how glowing embers from senetwet wood are swirled inside traditional gourds to sterilize the inner walls and impart a smoky aroma.\n- **2. Charcoal Mesh**: Observe how coarse charcoal is packed tightly between wire mesh layers.\n- **3. Wind Placement**: Notice how the cooler is positioned in an open, breezy corridor to maximize evaporation rates."
                        }
                    }
                ],
                # Page 5: Interactive Classification Challenge
                [
                    {
                        "type": "interactive_scenario",
                        "title": "Dairy Technology Classification Challenge",
                        "content": {
                            "title": "Classifying Preservation Principles",
                            "instructions": "Determine whether the statement describes Fermentation or Charcoal Cooling:",
                            "scenario": "A rural school farm is setting up two milk preservation systems.",
                            "question": "Which technology relies on the physical latent heat of water evaporation rather than bacterial biological acid production?",
                            "options": [
                                "Evaporative Charcoal Cooler (uses water evaporation from wet charcoal to absorb heat energy).",
                                "Lactic Acid Fermentation (Mala)",
                                "Both are identical biological reactions",
                                "Neither"
                            ],
                            "correct_feedback": "Correct! Charcoal cooling is a physical process based on the evaporation of water absorbing heat energy. Fermentation is a biological process using bacteria.",
                            "incorrect_feedback": "Incorrect. Charcoal cooling relies on the physical evaporation of water to cool the cabinet. Fermentation relies on biological lactic acid production."
                        }
                    }
                ],
                # Page 6: Formative Knowledge Check
                [
                    {
                        "type": "knowledge_check",
                        "title": "Knowledge Check: Charcoal Cooler Climatic Requirements",
                        "content": {
                            "question": "Why does an evaporative charcoal cooler operate with maximum cooling efficiency in a hot, dry, windy semi-arid area but poorly in a damp, rainy, humid forest?",
                            "options": [
                                "Dry air and wind speed up water evaporation, absorbing large amounts of heat energy; in humid air, water cannot evaporate quickly.",
                                "Charcoal turns to stone in dry weather.",
                                "Wind blows the milk away.",
                                "Humid air causes the wood to catch fire."
                            ],
                            "answer": "A",
                            "explanation": "Evaporation requires unsaturated (dry) air and airflow. In hot, dry, breezy climates, water evaporates rapidly, absorbing maximum heat and dropping cabinet temperatures."
                        }
                    }
                ],
                # Page 7: Summary & Connection Forward
                [
                    {
                        "type": "key_takeaway",
                        "title": "Lesson Summary",
                        "content": {
                            "text": "- **Fermentation** uses *Lactobacillus* to convert lactose into **lactic acid (pH < 4.5)**.\n- Acidic environments destroy rot-causing bacteria, keeping mala safe for **2 to 3 weeks**.\n- **Charcoal coolers** utilize **evaporative cooling** to drop cabinet temperatures by **5°C to 10°C**.\n- Charcoal coolers require **zero electricity**, relying only on water drips and dry breezes."
                        }
                    },
                    {
                        "type": "transition",
                        "title": "Looking Ahead",
                        "content": {
                            "text": "Why is food preservation so vital for our households, communities, and nation? In our final lesson, we analyze food security, conduct a household audit, and take our Topic Summative Assessment!"
                        }
                    }
                ]
            ]
        },

        # =====================================================================
        # LESSON 9: Importance of Milk and Meat Preservation & Capstone
        # =====================================================================
        {
            "unit_order": 9,
            "unit_name": "Importance of Milk and Meat Preservation",
            "unit_description": "Socio-economic impact of preservation: cutting post-harvest losses (up to 30%), household protein security, drought disaster shields, household kitchen audits, topic video review, and 10 topic summative MCQs.",
            "lesson_title": "Importance of Milk and Meat Preservation & Capstone",
            "pages": [
                # Page 1: Visual Hook & Capstone Objectives
                [
                    {
                        "type": "suggested_image",
                        "title": "Family Food Security: Nutritious Household Dinner",
                        "content": {
                            "title": "Family Food Security: Nutritious Household Dinner",
                            "caption": "A healthy African family enjoying a balanced, protein-rich meal supported by preserved milk and meat products in a clean kitchen."
                        }
                    },
                    {
                        "type": "learning_goal",
                        "title": "Learning Objectives: Food Security & Topic Mastery",
                        "content": {
                            "title": "What We Will Accomplish Today",
                            "goals": [
                                "Explain how animal product preservation slashes **national post-harvest loss (30% waste)**.",
                                "Analyze how preserved food reserves act as a **drought and disaster shield**.",
                                "Conduct a structured **Household Food Preservation Audit** in your home kitchen.",
                                "Review the Topic Video and demonstrate 100% mastery on the **10 Topic Summative Assessment Questions**."
                            ]
                        }
                    },
                    {
                        "type": "concept_explanation",
                        "title": "Food Preservation: A Superpower for Food Security",
                        "content": {
                            "title": "The Big Picture of Animal Products",
                            "text": "Preserving animal products is not merely a cooking technique—it is a cornerstone of national food security, public health, and rural economic resilience. When we prevent fresh milk and meat from spoiling, we protect hard-earned household wealth, nourish our families with protein year-round, and eliminate agricultural waste!"
                        }
                    }
                ],
                # Page 2: National Food Security & Post-Harvest Waste
                [
                    {
                        "type": "concept_explanation",
                        "title": "Socio-Economic Dimensions of Preservation",
                        "content": {
                            "title": "Transforming Perishables into Wealth",
                            "text": "- **1. Slashing Post-Harvest Losses**: Over 30% of harvested milk and meat in developing nations is wasted due to poor storage and spoilage. Simple boiling, drying, and fermentation save millions of kilograms of food annually.\n- **2. Year-Round Protein Nutrition**: Growing children and teenagers require constant protein, iron, and calcium for cognitive and muscular development. Preserved reserves ensure nutrition continues during dry seasons when livestock milk yields drop.\n- **3. Income Generation & Value Addition**: Transforming raw perishable milk into thick fermented Mala or converting fresh beef into spiced Nyirinyiri increases market value by 40% to 80%, providing steady income for rural farming families."
                        }
                    },
                    {
                        "type": "suggested_diagram",
                        "title": "National Food Security & Animal Product Preservation Hub Mind Map",
                        "content": {
                            "title": "National Food Security & Animal Product Preservation Hub Mind Map",
                            "caption": "Central Food Security Hub branching out into: 1. Protein Availability (year-round muscle growth) • 2. Financial Stability (value addition & market sales) • 3. Disaster Shield (drought reserves) • 4. Waste Reduction (eliminating 30% post-harvest loss)."
                        }
                    }
                ],
                # Page 3: Conducting a Household Preservation Audit
                [
                    {
                        "type": "step_process",
                        "title": "Standard Operating Procedure: Household Kitchen Audit",
                        "content": {
                            "title": "How to Conduct a Home Food Audit",
                            "steps": [
                                "**Step 1: Survey Kitchen Methods**: Ask your guardians which preservation methods (boiling, salting, drying, fermentation, cooling) are used for milk and meat at home.",
                                "**Step 2: Inspect Containers**: Check storage containers: Are they clean, scalded, covered tightly, and raised off the floor away from pests?",
                                "**Step 3: Log Data**: Record food items, preservation method, container type, and estimated shelf life achieved.",
                                "**Step 4: Formulate Hygiene Improvement**: Propose one scientific improvement (e.g., scalding milk bottles with boiling water or drying meat beneath a mesh net)."
                            ]
                        }
                    }
                ],
                # Page 4: Interactive Food Security Scenario Challenge
                [
                    {
                        "type": "interactive_scenario",
                        "title": "Food Security Scenario Classification",
                        "content": {
                            "title": "Classifying Agricultural Scenarios",
                            "instructions": "Determine whether the scenario represents Food Security, Post-Harvest Loss, or Value Addition:",
                            "scenario": "During a severe 4-month dry season, a family feeds their children with dried beef strips (nyirinyiri) and fermented sour milk (mala) prepared during the rainy harvest season.",
                            "question": "What agricultural principle does this scenario demonstrate?",
                            "options": [
                                "Food Security (stored preserved food reserves acting as a nutrition shield against seasonal food shortages).",
                                "Post-Harvest Loss",
                                "Soil Erosion",
                                "Chemical Contamination"
                            ],
                            "correct_feedback": "Correct! Preserving food reserves during harvest abundance ensures constant protein nutrition during droughts, creating true household Food Security.",
                            "incorrect_feedback": "Incorrect. Using preserved food reserves during a drought is the definition of household Food Security."
                        }
                    }
                ],
                # Page 5: Formative Knowledge Check & Master Summary
                [
                    {
                        "type": "knowledge_check",
                        "title": "Knowledge Check: Post-Harvest Loss Definition",
                        "content": {
                            "question": "What is the meaning of 'post-harvest loss' in animal product management?",
                            "options": [
                                "The measurable loss in quantity, quality, and economic value of food occurring between the time of animal slaughter/milking and final consumption.",
                                "Losing money when buying land.",
                                "Feeding too much grass to cows.",
                                "Planting seeds in the rainy season."
                            ],
                            "answer": "A",
                            "explanation": "Post-harvest loss refers to the reduction in edible food mass and quality across harvesting, processing, storage, and distribution."
                        }
                    },
                    {
                        "type": "key_takeaway",
                        "title": "Topic 6 Master Summary: Preparation of Animal Products",
                        "content": {
                            "text": "- **Fish**: Scale tail-to-head at 45°, shallow belly slit, remove gills/viscera, score muscles, pat-dry, and fry away from body.\n- **Poultry**: Humane stunning, rapid bleeding in cone, scald at 60-65°C, pluck with grain, excise gallbladder without bile leak, and drain upside down.\n- **Meat**: Preserve via **osmotic dry-salting** (2-4 weeks), **boiling at 100°C** (2-4 days), **sun-drying** (<10% moisture), or **hardwood smoking** (phenols/acids).\n- **Milk**: **Boil at 100°C for 2-3 mins** with stir-aeration, **ferment into mala** (lactic acid pH < 4.5), or store in **evaporative charcoal coolers**."
                        }
                    }
                ],
                # Page 6: Topic Video Review
                [
                    {
                        "type": "suggested_video",
                        "title": "Topic Video Review: Animal Product Processing & Preservation",
                        "content": {
                            "title": "Topic Video Review: Animal Product Processing & Preservation",
                            "url": "https://www.youtube.com/watch?v=Ei5z_0Lxmic",
                            "resolved_video_id": "Ei5z_0Lxmic",
                            "caption": "Watch this comprehensive educational review covering fish scaling, humane poultry dressing, meat salting, milk boiling, and low-cost charcoal cooling."
                        }
                    },
                    {
                        "type": "concept_explanation",
                        "title": "Key Review Questions for Video Analysis",
                        "content": {
                            "title": "Final Review Highlights",
                            "text": "- **1. Surgical Cleanliness**: Notice how separating edible giblets from waste prevents cross-contamination.\n- **2. The Scalding Window**: Observe how 60°C water relaxes feather follicles perfectly.\n- **3. Household Resilience**: See how off-grid preservation shields rural families from food insecurity."
                        }
                    }
                ],
                # Page 7: Topic Assessment Part 1 (Questions 1 to 2)
                [
                    {
                        "type": "knowledge_check",
                        "title": "Topic Assessment - Question 1: Fresh Fish Selection Indicators",
                        "content": {
                            "question": "Which set of sensory indicators confirms that a freshly caught fish is in prime condition and safe for processing?",
                            "options": [
                                "Bright red/pink gills, clear and bulging eyes, firm elastic flesh, and a fresh clean-water smell.",
                                "Sunken cloudy grey eyes, soft slimy flesh, and a sour ammonia odor.",
                                "Brown slimy gills and loose falling scales.",
                                "Dry cracked yellow skin with green spots."
                            ],
                            "answer": "A",
                            "explanation": "Fresh fish has clear bulging eyes, bright red gills free of slime, firm elastic flesh, and clean-water aroma."
                        }
                    },
                    {
                        "type": "knowledge_check",
                        "title": "Topic Assessment - Question 2: Fish Belly Midline Slit Logic",
                        "content": {
                            "question": "When slitting the belly of a fish from the vent forward, why must the knife cut be kept shallow?",
                            "options": [
                                "To avoid puncturing the intestines and stomach, preventing fecal waste and digestive juices from contaminating the edible meat.",
                                "To keep the scales on the outside.",
                                "To avoid breaking the knife blade.",
                                "To make the fish fry faster."
                            ],
                            "answer": "A",
                            "explanation": "A shallow cut penetrates only the outer abdominal skin, keeping internal organs intact so waste and bacteria do not spill onto meat."
                        }
                    }
                ],
                # Page 8: Topic Assessment Part 2 (Questions 3 to 5)
                [
                    {
                        "type": "knowledge_check",
                        "title": "Topic Assessment - Question 3: Milk Boiling Temperature & Duration",
                        "content": {
                            "question": "Why must raw cow's milk be brought to an active boil at 100°C for at least 2 to 3 minutes before storage or drinking?",
                            "options": [
                                "To pasteurize the milk, destroying dangerous disease-causing pathogens like Bovine Tuberculosis and Brucellosis.",
                                "To turn the natural lactose sugar into salt.",
                                "To evaporate all water and turn milk into solid butter.",
                                "To make the milk turn sour immediately."
                            ],
                            "answer": "A",
                            "explanation": "Boiling at 100°C for 2-3 minutes pasteurizes raw milk, killing pathogens that transmit zoonotic diseases like Tuberculosis and Brucellosis."
                        }
                    },
                    {
                        "type": "knowledge_check",
                        "title": "Topic Assessment - Question 4: Charcoal Cooler Evaporative Physics",
                        "content": {
                            "question": "What is the primary physical process that allows a charcoal cooler cabinet to drop internal temperatures by 5°C to 10°C without electricity?",
                            "options": [
                                "Evaporation of water from wet charcoal mesh walls absorbing thermal heat energy from inside the cabinet.",
                                "Electrical compression of cooling gases.",
                                "Chemical reactions between dry wood and air.",
                                "High pressure steam escaping from an engine."
                            ],
                            "answer": "A",
                            "explanation": "Charcoal coolers work via evaporative cooling: passing breeze evaporates water from wet charcoal, absorbing latent heat and lowering internal temperatures."
                        }
                    },
                    {
                        "type": "knowledge_check",
                        "title": "Topic Assessment - Question 5: Poultry Carcass Drainage Rationale",
                        "content": {
                            "question": "Why must a freshly eviscerated and washed poultry carcass be hung upside down by its legs for 15 to 20 minutes?",
                            "options": [
                                "To allow all cavity wash water and residual blood to drain out completely, eliminating stagnant moisture pools where bacteria multiply.",
                                "To stretch the leg muscles for frying.",
                                "To make the skin absorb salt faster.",
                                "To allow feathers to loosen."
                            ],
                            "answer": "A",
                            "explanation": "Suspending the carcass upside down drains pooled washing water and blood, eliminating wet environments where spoilage bacteria breed."
                        }
                    }
                ],
                # Page 9: Topic Assessment Part 3 (Questions 6 to 8)
                [
                    {
                        "type": "knowledge_check",
                        "title": "Topic Assessment - Question 6: Dry-Salting Dehydration Mechanics",
                        "content": {
                            "question": "How does coating raw meat strips heavily with dry salt crystals prevent bacterial rot and decomposition?",
                            "options": [
                                "Salt crystals create a high osmotic concentration that draws moisture out of meat tissue and bacterial cells, causing the bacteria to dehydrate and die.",
                                "Salt heats the meat up to 100°C.",
                                "Salt creates a poisonous gas that kills insects.",
                                "Salt turns the meat into solid stone."
                            ],
                            "answer": "A",
                            "explanation": "Dry salt draws out cellular moisture via osmosis, dehydrating and killing bacteria while eliminating free water needed for microbial growth."
                        }
                    },
                    {
                        "type": "knowledge_check",
                        "title": "Topic Assessment - Question 7: Toxic Resins in Meat Smoking",
                        "content": {
                            "question": "Why must softwoods like pine, cypress, and cedar NEVER be used to smoke meat for preservation?",
                            "options": [
                                "They contain sticky resin and sap that produce toxic, bitter black soot, ruining meat flavor and depositing harmful chemical residues.",
                                "They do not burn or release any smoke.",
                                "They cause the meat to absorb too much moisture.",
                                "They burn too cold to warm the air."
                            ],
                            "answer": "A",
                            "explanation": "Resinous softwoods produce thick, bitter, tar-like soot and toxic resins that ruin meat flavor and contaminate food. Always use hardwoods like acacia."
                        }
                    },
                    {
                        "type": "knowledge_check",
                        "title": "Topic Assessment - Question 8: Calabash Gourd Scalding Sterilization",
                        "content": {
                            "question": "Before pouring milk into a traditional calabash gourd for natural fermentation into mala, what critical sterilization step must be performed?",
                            "options": [
                                "Washing and scalding the inside of the gourd with boiling water and hot charcoal embers to eliminate unwanted rot microbes.",
                                "Painting the inside of the gourd with chemical paint.",
                                "Leaving the gourd open in a muddy puddle.",
                                "Washing the gourd with salty ocean water."
                            ],
                            "answer": "A",
                            "explanation": "Scalding with boiling water and traditional charcoal embers sterilizes the gourd, ensuring only beneficial lactic acid bacteria guide fermentation."
                        }
                    }
                ],
                # Page 10: Topic Assessment Part 4 (Questions 9 to 10)
                [
                    {
                        "type": "knowledge_check",
                        "title": "Topic Assessment - Question 9: Coastal Climatic Preservation Selection",
                        "content": {
                            "question": "A farming family in a hot, humid coastal village with high air humidity needs to preserve beef strips without electricity. Why is dry-salting more reliable than sun-drying?",
                            "options": [
                                "In humid coastal air, saturated water vapor slows down solar evaporation, causing meat to rot before it dries; dry-salting extracts moisture chemically regardless of air humidity.",
                                "Sun-drying only works in the ocean.",
                                "Humid air makes salt turn into ice.",
                                "Dry-salting requires a refrigerator to work."
                            ],
                            "answer": "A",
                            "explanation": "High humidity prevents solar evaporation, causing meat to rot on drying lines. Dry-salting works via osmotic pressure independent of air humidity."
                        }
                    },
                    {
                        "type": "knowledge_check",
                        "title": "Topic Assessment - Question 10: Gallbladder Puncture Consequence",
                        "content": {
                            "question": "During chicken evisceration, a student accidentally slices open the green gallbladder attached to the liver. What is the consequence of this error?",
                            "options": [
                                "Bitter green bile spills onto the surrounding meat, permanently staining it green and imparting an intolerable bitter flavor that makes it unmarketable.",
                                "The meat becomes sweeter and tender.",
                                "The feathers turn white.",
                                "The bones turn into liquid."
                            ],
                            "answer": "A",
                            "explanation": "The gallbladder contains concentrated green bile. If ruptured, bile permanently stains the meat green and imparts a strong, intolerable bitter flavor."
                        }
                    }
                ]
            ]
        }
    ]

def ingest_cbc_grade8_agriculture_topic6(replace: bool = True):
    """Executes the database transaction to ingest Topic 6 into CBC Grade 8 Agriculture."""
    print("=" * 80)
    print("STARTING CONTENT INGESTION: CBC GRADE 8 AGRICULTURE — TOPIC 6 (DEEP EDITION)")
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

        topic_name = "Preparation of Animal Products"
        if replace:
            existing_topics = Topic.objects.filter(subject=subject, name=topic_name)
            if existing_topics.exists():
                print(f"[*] Found existing topic '{topic_name}' (ID: {existing_topics.first().id}). Deleting for clean replace...")
                existing_topics.delete()

        topic, created = Topic.objects.get_or_create(
            subject=subject,
            name=topic_name,
            defaults={
                "order": 6,
                "description": "Comprehensive animal product processing and preservation: fish scaling, gutting, scoring, and safe pan-frying; humane poultry stunning, bleeding, defeathering, evisceration, and upside-down drainage; meat preservation by osmotic dry-salting, parboiling, solar drying, and hardwood smoking; milk preservation by 100°C boiling with stir-aeration, lactic acid fermentation (mala/mursik), evaporative charcoal coolers, and household food security audits."
            }
        )
        print(f"[*] Topic: '{topic.name}' (ID: {topic.id}, Created: {created})")

        curriculum_data = build_topic6_curriculum()
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
                        block_id=f"g8_agri_t6_u{u_order}_p{page_idx}_b{comp_idx}",
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
        print(f"[SUCCESS] Ingestion Complete for Grade 8 Topic 6: '{topic.name}'")
        print(f"[*] Units Created:   {total_units}")
        print(f"[*] Lessons Created: {total_lessons}")
        print(f"[*] Total Pages:     {total_pages}")
        print(f"[*] Total Blocks:    {total_blocks}")
        print("=" * 80)

if __name__ == "__main__":
    replace_flag = "--replace" in sys.argv or True
    ingest_cbc_grade8_agriculture_topic6(replace=replace_flag)
