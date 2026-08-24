"""
VLearn CBC Grade 8 Agriculture — Topic 4: Poultry Rearing in a Fold
Production Ingestion Engine (Phase 1: Content & Card Architecture - Deep Pedagogical Edition)

Curriculum: CBC (Curriculum ID: 5)
Grade: Grade 8 (ID: 15, Level: 8)
Subject: Agriculture
Topic: Poultry Rearing in a Fold (Topic Order: 4)

Decomposed into 9 Learning Units & 9 Published Lessons:
  1. Meaning of Poultry Rearing and the Concept of Folds (7 Pages, 13 Blocks)
  2. Rearing Practices of Poultry in a Fold (7 Pages, 14 Blocks)
  3. Factors to Consider When Constructing a Poultry Fold (7 Pages, 13 Blocks)
  4. Materials and Construction Planning for a Poultry Fold (7 Pages, 13 Blocks)
  5. Practical Activity: Constructing a Poultry Fold (7 Pages, 14 Blocks)
  6. Evaluating and Assessing a Poultry Fold (7 Pages, 13 Blocks)
  7. Benefits of Rearing Poultry in a Fold (7 Pages, 13 Blocks)
  8. Practical Activity: Daily Care and Flock Management (7 Pages, 13 Blocks)
  9. Integrated Food Production: Gardening & Poultry Loops (10 Pages, 22 Blocks)

Deep Pedagogical Enhancements:
  - Strict 1 Card = 1 Understandable Idea progression.
  - Zero citation leaks ([1], [245]), zero developer meta-tags, zero raw unrendered LaTeX.
  - Formative scenario MCQs and Topic Summative MCQs with comprehensive educational explanations.
  - Multi-video integrations embedded across individual practical lessons.

Usage:
  ./venv/bin/python curriculum/ingest_cbc_grade8_agriculture_topic4.py [--replace]
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

def build_topic4_curriculum():
    """Returns the comprehensive pedagogical page and block structure for Grade 8 Topic 4: Poultry Rearing in a Fold."""
    return [
        # =====================================================================
        # LESSON 1: Meaning of Poultry Rearing and the Concept of Folds
        # =====================================================================
        {
            "unit_order": 1,
            "unit_name": "Meaning of Poultry Rearing and the Concept of Folds",
            "unit_description": "Definition of poultry rearing, types of domestic birds, mobile fold definitions, and comparison of poultry housing systems (Free-Range vs Deep Litter vs Mobile Fold).",
            "lesson_title": "Meaning of Poultry Rearing and the Concept of Folds",
            "pages": [
                # Page 1: Visual Hook & Learning Objectives
                [
                    {
                        "type": "suggested_image",
                        "title": "Mobile Pastoral Shelter: The Poultry Fold",
                        "content": {
                            "title": "Mobile Pastoral Shelter: The Poultry Fold",
                            "caption": "A classic wooden and wire-mesh mobile poultry fold positioned on green grass pasture, combining an enclosed sleeping cabin with an open foraging run."
                        }
                    },
                    {
                        "type": "learning_goal",
                        "title": "Learning Objectives: Poultry Systems & Fold Dynamics",
                        "content": {
                            "title": "What We Will Accomplish Today",
                            "goals": [
                                "Define **poultry rearing** and identify the 4 primary types of domesticated birds.",
                                "Explain the agricultural engineering concept of a **mobile poultry fold**.",
                                "Contrast mobile folds with **free-range foraging** and **permanent deep litter housing**.",
                                "Describe how open-bottom mesh frames enable daily foraging and soil fertilization."
                            ]
                        }
                    },
                    {
                        "type": "concept_explanation",
                        "title": "Bridging Pasture Grazing and Security",
                        "content": {
                            "title": "The Evolution of Poultry Shelters",
                            "text": "In traditional rural farming, chickens either roam completely free (facing fatal attacks from hawks, mongoose, and dogs) or remain locked inside dark, dusty sheds (lacking fresh green grass and exercise). The **mobile poultry fold** bridges this gap: it provides absolute predator defense while allowing birds to graze directly on fresh pasture every single day!"
                        }
                    }
                ],
                # Page 2: What is Poultry Rearing & Bird Types
                [
                    {
                        "type": "concept_explanation",
                        "title": "Domestic Poultry Classifications",
                        "content": {
                            "title": "Raising Birds for Food & Income",
                            "text": "**Poultry rearing** refers to the agricultural practice of breeding, housing, feeding, and caring for domesticated birds:\n\n- **Chickens (Gallus domesticus)**: Raised for eggs (layers), meat (broilers), or dual-purpose indigenous kienyeji flocks.\n- **Ducks & Geese**: Kept for rich eggs, meat, and biological snail control.\n- **Turkeys**: Raised for high-weight holiday meat production.\n- **Guinea Fowls**: Prized for tasty lean meat, eggs, and grazing tick control on pastures."
                        }
                    },
                    {
                        "type": "suggested_diagram",
                        "title": "Poultry Housing Systems Comparison Matrix",
                        "content": {
                            "title": "Poultry Housing Systems Comparison Matrix",
                            "caption": "Comparative visual architecture: 1. Free-Range (high predator risk, lost eggs) • 2. Deep Litter (expensive indoor confinement, zero grazing) • 3. Mobile Poultry Fold (portable, 100% predator-proof, fresh pasture grazing)."
                        }
                    }
                ],
                # Page 3: The Architecture of a Mobile Fold
                [
                    {
                        "type": "concept_explanation",
                        "title": "The Structural Anatomy of a Poultry Fold",
                        "content": {
                            "title": "A Portable Ark on Pasture",
                            "text": "A **poultry fold** (folding unit or portable ark) consists of two integrated zones:\n\n- **1. Open-Bottom Foraging Run**: Wrapped in wire mesh, allowing birds to walk directly on pasture, eating green shoots, weed seeds, and soil insects.\n- **2. Enclosed Roosting Cabin**: Solid wooden walls and waterproof roof at one end, providing warmth, perches, and secure nesting boxes.\n- **3. Mobility Principle**: The entire structure is fitted with handles and is shifted manually to clean grass every 24 hours!"
                        }
                    },
                    {
                        "type": "comparison_table",
                        "title": "Poultry Housing Systems Comparison",
                        "content": {
                            "title": "Housing Performance Matrix",
                            "headers": ["Housing System", "Predator Security", "Access to Fresh Pasture", "Capital Setup Cost", "Disease & Parasite Risk"],
                            "rows": [
                                ["Free-Range System", "Very Low (High predator attacks & theft)", "High (Unlimited roaming)", "Minimal / Free", "Moderate to High (Contact with wild birds)"],
                                ["Deep Litter System", "High (Solid building)", "None (Permanent indoor confinement)", "Very High (Concrete walls, wood shavings)", "High (Manure accumulation triggers coccidiosis)"],
                                ["Mobile Poultry Fold", "High (Strong wire mesh & lockable cabin)", "High (Fresh daily pasture shift)", "Low (Built from recycled local timber)", "Low (Daily shifting breaks parasite cycles)"]
                            ]
                        }
                    }
                ],
                # Page 4: Interactive Housing Selection Challenge
                [
                    {
                        "type": "interactive_scenario",
                        "title": "Housing System Selection Challenge",
                        "content": {
                            "title": "Choosing the Optimal Poultry Housing",
                            "instructions": "Determine the best housing system for the smallholder farmer:",
                            "scenario": "Farmer Kiprono has a small grassy farm with roaming wild dogs and hawks. He wants his 5 kienyeji chickens to eat fresh grass and insects daily without getting eaten by predators or needing an expensive concrete barn.",
                            "question": "Which housing system should Farmer Kiprono construct?",
                            "options": [
                                "A Mobile Poultry Fold with an open mesh bottom and lockable cabin",
                                "A Free-Range system leaving chickens outdoors overnight",
                                "A 5-story commercial concrete battery cage building",
                                "Tying the chickens to fence posts with string"
                            ],
                            "correct_feedback": "Correct! A mobile poultry fold protects the 5 chickens from predators with wire mesh while allowing them to graze on fresh pasture daily at low cost.",
                            "incorrect_feedback": "Incorrect. Free-range exposes birds to predators, while commercial concrete buildings are too expensive for 5 birds. A mobile fold is ideal."
                        }
                    }
                ],
                # Page 5: Formative Knowledge Check
                [
                    {
                        "type": "knowledge_check",
                        "title": "Knowledge Check: Open Mesh Bottom Rationale",
                        "content": {
                            "question": "Why is a mobile poultry fold designed with an open wire-mesh bottom rather than a solid wooden floor?",
                            "options": [
                                "To allow chickens to forage directly on fresh grass, weed seeds, and insects while depositing fertilizer onto the soil.",
                                "To make the structure lighter so the wind blows it away.",
                                "To encourage chickens to bury their eggs underground.",
                                "Because wood cannot touch green grass without catching fire."
                            ],
                            "answer": "A",
                            "explanation": "An open bottom allows birds to peck at fresh grass, weed seeds, and insects directly, enriching their diet and reducing supplementary feed costs while naturally fertilizing the pasture."
                        }
                    }
                ],
                # Page 6: Summary & Connection Forward
                [
                    {
                        "type": "key_takeaway",
                        "title": "Lesson Summary",
                        "content": {
                            "text": "- **Poultry** includes domesticated birds raised for meat, eggs, and manure (chickens, ducks, turkeys, guinea fowls).\n- A **poultry fold** is a lightweight, mobile house-and-run structure shifted across pasture daily.\n- Folds combine **predator safety** with the nutritional benefits of **fresh outdoor foraging**.\n- Moving the fold daily **breaks disease cycles and spreads nitrogen-rich manure evenly**."
                        }
                    },
                    {
                        "type": "transition",
                        "title": "Looking Ahead",
                        "content": {
                            "text": "How do we care for chickens inside a fold on a day-to-day basis? In Lesson 2, we master daily feeding routines, watering hygiene, and pasture shifting protocols!"
                        }
                    }
                ],
                # Page 7: Flock Density Rule Callout
                [
                    {
                        "type": "concept_explanation",
                        "title": "Flock Capacity Standards",
                        "content": {
                            "title": "The Ergonomic Sizing Rule",
                            "text": "Because folds must be moved manually by one or two students, they are designed for small flocks of **3 to 6 adult birds**. A typical 6x4-foot fold provides 24 square feet of total floor space—ensuring 4 to 5 square feet per bird, which prevents overcrowding stress and feather pecking."
                        }
                    }
                ]
            ]
        },

        # =====================================================================
        # LESSON 2: Rearing Practices of Poultry in a Fold
        # =====================================================================
        {
            "unit_order": 2,
            "unit_name": "Rearing Practices of Poultry in a Fold",
            "unit_description": "Daily husbandry practices: pasture shifting protocols, supplementary nutrition (starter, growers, layers mash), water hygiene, and parasite disruption (coccidiosis prevention).",
            "lesson_title": "Rearing Practices of Poultry in a Fold",
            "pages": [
                # Page 1: Visual Hook & Learning Objectives
                [
                    {
                        "type": "suggested_image",
                        "title": "Daily Pasture Grazing: Healthy Hens in Action",
                        "content": {
                            "title": "Daily Pasture Grazing: Healthy Hens in Action",
                            "caption": "Healthy kienyeji hens actively pecking at tender green grass and supplementary feed troughs inside a clean, well-managed pasture fold."
                        }
                    },
                    {
                        "type": "learning_goal",
                        "title": "Learning Objectives: Daily Fold Husbandry",
                        "content": {
                            "title": "What We Will Accomplish Today",
                            "goals": [
                                "Execute the 24-hour **pasture shifting protocol** safely without injuring birds.",
                                "Formulate a **supplementary feeding schedule** (starter, growers, layers mash + kitchen greens).",
                                "Explain how daily fold rotation breaks the **coccidiosis parasite cycle**.",
                                "Follow the structured **morning, afternoon, and evening flock care checklist**."
                            ]
                        }
                    },
                    {
                        "type": "concept_explanation",
                        "title": "The 24-Hour Golden Rule",
                        "content": {
                            "title": "Why Daily Shifting is Non-Negotiable",
                            "text": "If a fold is left on the same spot for more than one day, two disasters occur: the grass is scratched down to bare dirt, and concentrated manure accumulates. Shifting the fold every morning ensures birds always step onto clean, green pasture, breaking parasite life cycles and accelerating grass regrowth!"
                        }
                    }
                ],
                # Page 2: The Shift Protocol & Parasite Break Cycle
                [
                    {
                        "type": "suggested_diagram",
                        "title": "Daily Pasture Shift & Coccidiosis Break Cycle",
                        "content": {
                            "title": "Daily Pasture Shift & Coccidiosis Break Cycle",
                            "caption": "Diagram showing how advancing the fold 2 meters forward daily leaves behind manure to fertilize recovering grass, while keeping birds on clean ground and breaking parasite egg cycles."
                        }
                    },
                    {
                        "type": "step_process",
                        "title": "Standard Operating Procedure: Shifting the Fold Safely",
                        "content": {
                            "title": "How to Move the Fold Without Hurting Birds",
                            "steps": [
                                "**1. Clear the Run**: Remove the hanging feed trough and water drinker so they do not spill or crush birds.",
                                "**2. Position Two Handlers**: Two students stand at the front and back handles of the fold.",
                                "**3. Slow Forward Slide**: Lift the frame just 5 cm off the ground and slide it slowly forward in a straight line.",
                                "**4. Foot Clearance Check**: Ensure all chickens step forward with the frame and no feet are pinched under timber edges.",
                                "**5. Replace Feed & Water**: Re-hang clean drinkers and feeders inside the freshly positioned run!"
                            ]
                        }
                    }
                ],
                # Page 3: Supplementary Nutrition & Feed Formulation
                [
                    {
                        "type": "concept_explanation",
                        "title": "Supplementary Feeds for Folded Flocks",
                        "content": {
                            "title": "Balancing Pasture Forage with Protein & Calcium",
                            "text": "Pasture grass provides fiber, beta-carotene, and vitamins, but cannot supply all the protein and energy needed for fast growth or continuous egg laying:\n\n- **Chick Starter Mash (20% Protein)**: Weeks 1 to 8 for rapid muscle and organ development.\n- **Growers' Mash (16% Protein)**: Weeks 8 to 18 for strong skeletal bone frame.\n- **Layers' Mash (14% Protein + 3.5% Calcium)**: For hens laying eggs to ensure thick, crack-resistant eggshells.\n- **Kitchen Scraps & Greens**: Chopped sukumawiki, cabbage leaves, and fruit rinds provide natural digestive enzymes."
                        }
                    },
                    {
                        "type": "comparison_table",
                        "title": "Poultry Feed Stages & Daily Rations",
                        "content": {
                            "title": "Nutritional Stage Matrix",
                            "headers": ["Bird Life Stage", "Recommended Feed Type", "Daily Amount per Bird", "Key Nutritional Purpose"],
                            "rows": [
                                ["Chicks (0–8 Weeks)", "Chick Starter Mash", "30–50 grams", "High protein for rapid muscle development"],
                                ["Growers / Pullets (8–18 Weeks)", "Growers' Mash", "70–90 grams", "Balanced minerals for strong skeletal growth"],
                                ["Laying Hens (18+ Weeks)", "Layers' Mash", "120–130 grams", "High calcium for hard eggshells & egg production"],
                                ["All Stages (Daily Snack)", "Chopped Green Vegetables", "Handful per flock", "Vitamins A & C, digestive fiber, yolk coloring"]
                            ]
                        }
                    }
                ],
                # Page 4: Video Resource — Poultry Pasture Management in Kenya
                [
                    {
                        "type": "suggested_video",
                        "title": "Instructional Video: Smart Farm Poultry & Pasture Management",
                        "content": {
                            "title": "Instructional Video: Smart Farm Poultry & Pasture Management",
                            "url": "https://www.youtube.com/watch?v=TXJPk-QfhDU",
                            "resolved_video_id": "TXJPk-QfhDU",
                            "caption": "Watch this Citizen TV Smart Farm documentary exploring pasture rotation, poultry nutrition, biosecurity, and feed conservation in Kenya."
                        }
                    },
                    {
                        "type": "concept_explanation",
                        "title": "Key Field Observations from the Video",
                        "content": {
                            "title": "Best Practices in Pasture Husbandry",
                            "text": "- **1. Water Cleanliness**: Watch how drinkers are scrubbed daily to prevent algae and bacterial slime buildup.\n- **2. Rotational Grid**: Observe how pastures are divided into linear paths to ensure grass has 2 to 3 weeks to recover before the fold returns.\n- **3. Nighttime Security**: Notice how locking birds into the enclosed cabin at dusk prevents nocturnal predator attacks."
                        }
                    }
                ],
                # Page 5: Interactive Daily Chore Sequencing
                [
                    {
                        "type": "interactive_scenario",
                        "title": "Daily Chore Sequencing Challenge",
                        "content": {
                            "title": "Ordering Morning Husbandry Tasks",
                            "instructions": "Place the morning poultry tasks in the correct chronological order:",
                            "scenario": "Your student group arrives at the school farm at 7:00 AM to manage the poultry fold.",
                            "question": "What is the correct sequence of morning activities?",
                            "options": [
                                "1. Inspect flock health -> 2. Clean & refill drinkers/feeders -> 3. Shift fold forward -> 4. Lock cabin door at night",
                                "1. Shift fold violently -> 2. Throw stones at chickens -> 3. Drink their water",
                                "1. Collect eggs -> 2. Feed birds once a week -> 3. Never move the fold",
                                "1. Paint the fold -> 2. Buy new chickens -> 3. Remove all grass"
                            ],
                            "correct_feedback": "Correct! Always inspect bird health first, service feed and water, shift the fold onto fresh grass, and lock the cabin safely at dusk.",
                            "incorrect_feedback": "Incorrect. Always begin with health inspection, followed by water cleaning, gentle fold shifting, and evening lockdown."
                        }
                    }
                ],
                # Page 6: Formative Knowledge Check
                [
                    {
                        "type": "knowledge_check",
                        "title": "Knowledge Check: Coccidiosis Prevention",
                        "content": {
                            "question": "How does shifting a poultry fold to fresh ground every 24 hours prevent deadly coccidiosis and worm infestations?",
                            "options": [
                                "It breaks the parasite lifecycle by moving birds away from their droppings before parasite eggs can sporulate and become infectious.",
                                "It causes all parasites to freeze to death instantly.",
                                "It makes the chickens run so fast that parasites fall off.",
                                "It changes the color of the grass to purple."
                            ],
                            "answer": "A",
                            "explanation": "Coccidia parasite eggs passed in chicken droppings require 24 to 48 hours of warmth and moisture to sporulate and become infectious. Moving the fold daily leaves the unsporulated droppings behind, breaking the infection cycle."
                        }
                    }
                ],
                # Page 7: Summary & Connection Forward
                [
                    {
                        "type": "key_takeaway",
                        "title": "Lesson Summary",
                        "content": {
                            "text": "- Shifting the fold **every 24 hours** supplies fresh forage and breaks **parasite disease cycles**.\n- Provide **supplementary mash** (starter, growers, layers) as pasture alone cannot supply full protein needs.\n- Maintain **water hygiene** by scrubbing heavy drinkers daily.\n- Follow the structured **morning inspection, afternoon check, and evening lockdown** routine."
                        }
                    },
                    {
                        "type": "transition",
                        "title": "Looking Ahead",
                        "content": {
                            "text": "Before we construct a physical fold, what dimensions and environmental factors must we calculate? In Lesson 3, we analyze spatial density, ventilation physics, and predator defenses!"
                        }
                    }
                ]
            ]
        },

        # =====================================================================
        # LESSON 3: Factors to Consider When Constructing a Poultry Fold
        # =====================================================================
        {
            "unit_order": 3,
            "unit_name": "Factors to Consider When Constructing a Poultry Fold",
            "unit_description": "Design engineering: spatial density formulas (4-5 sq ft/bird), cross-ventilation physics vs draft protection, lightweight portability balance, and predator defense barriers.",
            "lesson_title": "Factors to Consider When Constructing a Poultry Fold",
            "pages": [
                # Page 1: Visual Hook & Learning Objectives
                [
                    {
                        "type": "suggested_image",
                        "title": "Engineering Shelter: The Ergonomic Poultry Fold",
                        "content": {
                            "title": "Engineering Shelter: The Ergonomic Poultry Fold",
                            "caption": "A well-engineered poultry fold showing secure galvanized wire mesh, a solid waterproof cabin, and carrying handles designed for two-person mobility."
                        }
                    },
                    {
                        "type": "learning_goal",
                        "title": "Learning Objectives: Architectural Factors",
                        "content": {
                            "title": "What We Will Accomplish Today",
                            "goals": [
                                "Calculate total fold dimensions using the **spatial density formula** (4–5 sq ft per bird).",
                                "Explain the difference between **beneficial cross-ventilation** and **harmful cold drafts**.",
                                "Analyze the **strength-to-weight balance** required for daily manual shifting.",
                                "Design **predator defense barriers** against mongooses, dogs, and birds of prey."
                            ]
                        }
                    },
                    {
                        "type": "concept_explanation",
                        "title": "Balancing Three Competing Constraints",
                        "content": {
                            "title": "The Engineering Challenge",
                            "text": "Designing a poultry fold requires balancing three critical engineering demands:\n1. **Strength**: Strong enough to block predators and withstand stormy weather.\n2. **Lightweight Portability**: Light enough for two Grade 8 students to slide daily.\n3. **Bird Comfort**: Spacious, well-ventilated, dry, and draft-free."
                        }
                    }
                ],
                # Page 2: Spatial Density & Dimension Formulas
                [
                    {
                        "type": "concept_explanation",
                        "title": "Spatial Density Math & Formulas",
                        "content": {
                            "title": "Calculating Fold Dimensions",
                            "text": "Overcrowding leads to stress, cannibalistic feather pecking, and stunted growth:\n\n- **Open Run Space**: 3 to 4 sq ft per adult bird (for grazing and exercise).\n- **Cabin Space**: 1.5 to 2 sq ft per adult bird (for roosting and egg laying).\n- **Total Space per Bird**: **4.5 to 5.0 sq ft**.\n\n*Worked Sizing Example*: For a standard flock of **4 chickens**:\n$$\\text{Total Area} = 4 \\text{ birds} \\times 5 \\text{ sq ft/bird} = 20 \\text{ sq ft}$$\n- A standard rectangular frame measuring **6 feet long by 4 feet wide** provides 24 sq ft—offering generous comfort!"
                        }
                    },
                    {
                        "type": "suggested_diagram",
                        "title": "3D Orthographic Fold Layout & Ventilation Dynamics",
                        "content": {
                            "title": "3D Orthographic Fold Layout & Ventilation Dynamics",
                            "caption": "Engineering schematic detailing: 6ft x 4ft x 2ft dimensions • 2ft x 4ft enclosed sleeping cabin • 4ft x 4ft open grazing run • Cross-ventilation airflow vectors • Lockable cabin door."
                        }
                    }
                ],
                # Page 3: Ventilation Physics vs. Cold Drafts
                [
                    {
                        "type": "concept_explanation",
                        "title": "Ventilation vs. Cold Drafts",
                        "content": {
                            "title": "Managing Air Quality Without Chilling Birds",
                            "text": "- **Why Ventilation is Critical**: Chickens exhale high amounts of moisture and produce ammonia gas from manure. Without continuous airflow, damp air causes respiratory infections.\n- **Cross-Ventilation in the Run**: The daytime run uses open wire mesh on all sides, allowing cooling breezes to sweep away heat and dust.\n- **Draft-Free Sleeping Cabin**: The night cabin has solid walls on 3 sides to block chilling wind currents (drafts) while small vents near the roof ridge allow rising warm, damp air to escape safely."
                        }
                    },
                    {
                        "type": "comparison_table",
                        "title": "Fold Design Factors & Engineering Solutions",
                        "content": {
                            "title": "Design Requirements Matrix",
                            "headers": ["Environmental Challenge", "Impact on Birds", "Specific Engineering Solution"],
                            "rows": [
                                ["Predator Attacks (Dogs/Mongooses)", "Fatal trauma and flock loss", "Heavy 1-inch galvanized wire mesh secured with U-nails; flush ground frame"],
                                ["Overcrowding Stress", "Feather pecking, cannibalism, stress", "Standard 5 sq ft total floor area per adult bird (e.g. 6x4 ft for 4 birds)"],
                                ["Cold Rain & Night Drafts", "Hypothermia and respiratory sickness", "Solid wooden cabin walls on 3 sides with overlapping waterproof iron/plastic roof"],
                                ["Excessive Weight", "Fold cannot be moved daily -> manure piles up", "Use 2x2 inch softwood timber offcuts or bamboo instead of heavy hardwood logs"]
                            ]
                        }
                    }
                ],
                # Page 4: Interactive Dimensioning Challenge
                [
                    {
                        "type": "interactive_scenario",
                        "title": "Dimensioning & Sizing Challenge",
                        "content": {
                            "title": "Calculating Fold Capacity",
                            "instructions": "Calculate the maximum number of adult chickens for the given fold size:",
                            "scenario": "Your agriculture group builds a rectangular poultry fold measuring 5 feet long by 4 feet wide (total area = 20 square feet).",
                            "question": "Based on standard spatial density rules (5 sq ft per bird), how many adult chickens can safely live in this fold?",
                            "options": [
                                "4 Chickens (20 sq ft ÷ 5 sq ft/bird = 4 birds)",
                                "20 Chickens",
                                "1 Chicken",
                                "50 Chickens"
                            ],
                            "correct_feedback": "Correct! 20 sq ft ÷ 5 sq ft/bird = 4 chickens. This ensures generous space for foraging, exercise, and roosting without stress.",
                            "incorrect_feedback": "Incorrect. Divide Total Area (20 sq ft) by Space per Bird (5 sq ft) = 4 birds. Overcrowding 20 birds would cause severe stress and disease."
                        }
                    }
                ],
                # Page 5: Formative Knowledge Check
                [
                    {
                        "type": "knowledge_check",
                        "title": "Knowledge Check: Weight & Portability Balance",
                        "content": {
                            "question": "What is the main danger of constructing a poultry fold using thick, heavy hardwood railway sleepers instead of lightweight 2x2 inch softwood?",
                            "options": [
                                "The fold will be too heavy for students to move daily, causing manure accumulation and grass destruction in one spot.",
                                "Hardwood dissolves when exposed to rainwater.",
                                "Chickens refuse to walk on hardwood timber.",
                                "Predators prefer the smell of softwood timber."
                            ],
                            "answer": "A",
                            "explanation": "A poultry fold must be portable. If built from excessively heavy hardwood, daily shifting becomes impossible, resulting in severe manure accumulation, odor, and parasite proliferation."
                        }
                    }
                ],
                # Page 6: Summary & Connection Forward
                [
                    {
                        "type": "key_takeaway",
                        "title": "Lesson Summary",
                        "content": {
                            "text": "- Design folds allocating **4 to 5 square feet per bird** (e.g. 6x4 ft for 4 chickens).\n- Provide **cross-ventilation in the daytime run** and **draft-free shelter in the sleeping cabin**.\n- Use **lightweight 2x2 softwood timber** to ensure two students can shift the fold effortlessly.\n- Secure all wire mesh with **tight U-nails** to prevent predator entry."
                        }
                    },
                    {
                        "type": "transition",
                        "title": "Looking Ahead",
                        "content": {
                            "text": "What physical materials and hand tools do we need to gather from our school and community? In Lesson 4, we create our bill of materials and construction workflow plan!"
                        }
                    }
                ],
                # Page 7: Deep Dive Callout
                [
                    {
                        "type": "concept_explanation",
                        "title": "Deep Dive: Mesh Gauge & Aperture Sizing",
                        "content": {
                            "title": "Selecting the Right Wire Mesh",
                            "text": "Never use thin plastic insect mesh for a poultry fold—rats and mongooses chew through soft plastic in minutes. Always use **1-inch (25 mm) galvanized hexagonal chicken wire** or **welded wire mesh**. The 1-inch aperture allows chicken heads to peck grass without getting stuck, while completely barring predator paws."
                        }
                    }
                ]
            ]
        },

        # =====================================================================
        # LESSON 4: Materials and Construction Planning for a Poultry Fold
        # =====================================================================
        {
            "unit_order": 4,
            "unit_name": "Materials and Construction Planning for a Poultry Fold",
            "unit_description": "Material selection (timber offcuts, bamboo, wire mesh, recycled plastic), tool safety protocols (hand saw, claw hammer, wire cutters), and 5-phase assembly sequencing.",
            "lesson_title": "Materials and Construction Planning for a Poultry Fold",
            "pages": [
                # Page 1: Visual Hook & Learning Objectives
                [
                    {
                        "type": "suggested_image",
                        "title": "Tools of the Trade: Carpentry Materials & Tools",
                        "content": {
                            "title": "Tools of the Trade: Carpentry Materials & Tools",
                            "caption": "A neatly organized carpentry workbench featuring a hand saw, claw hammer, measuring tape, wire cutters, U-nails, and timber offcuts."
                        }
                    },
                    {
                        "type": "learning_goal",
                        "title": "Learning Objectives: Materials & Planning",
                        "content": {
                            "title": "What We Will Accomplish Today",
                            "goals": [
                                "Identify at least 5 **locally available and recycled construction materials**.",
                                "Select the correct hand tools and follow **workshop safety guidelines**.",
                                "Draft a complete **Bill of Materials (BOM)** and quantity budget.",
                                "Sequence the **5-phase fabrication plan** before starting woodwork."
                            ]
                        }
                    },
                    {
                        "type": "concept_explanation",
                        "title": "Building Sturdy Structures for Low Cost",
                        "content": {
                            "title": "The Resourceful Agricultural Mindset",
                            "text": "A great agricultural engineer does not waste money buying expensive imported hardware. By creatively repurposing sawmill offcuts, discarded plastic sheets, bamboo stalks, and fence wire scraps, students can construct a high-quality, weather-resistant poultry fold for almost zero cost!"
                        }
                    }
                ],
                # Page 2: Local & Recycled Material Selection
                [
                    {
                        "type": "comparison_table",
                        "title": "Locally Available Materials for Poultry Fold",
                        "content": {
                            "title": "Bill of Materials & Alternatives Matrix",
                            "headers": ["Component Part", "Standard Material", "Low-Cost Recycled Alternative", "Structural Purpose"],
                            "rows": [
                                ["Structural Skeleton", "2x2 inch cypress/pine offcuts", "Straight bamboo poles or tree branches", "Forms rigid 6x4x2 ft rectangular box frame"],
                                ["Grazing Run Walls", "1-inch galvanized chicken wire", "Interlaced split-bamboo lattice", "Confines birds; allows sunlight & cross-ventilation"],
                                ["Sleeping Cabin Walls", "1/2 inch plywood / timber boards", "Flattened plastic oil drums or woven mats", "Insulates roosting birds from cold night winds"],
                                ["Waterproof Roof", "Corrugated galvanized iron scrap", "UV-treated plastic sheets or dry grass thatch", "Sheds rainwater away from roosting cabin"],
                                ["Fasteners & Hinges", "2-inch & 3-inch nails, U-nails", "Sisal twine, tire rubber strip hinges", "Binds structural joints and secures wire mesh"]
                            ]
                        }
                    },
                    {
                        "type": "suggested_diagram",
                        "title": "Bill of Materials & Exploded Construction Anatomy",
                        "content": {
                            "title": "Bill of Materials & Exploded Construction Anatomy",
                            "caption": "Exploded 3D structural diagram: Base frame rails • 4 corner vertical posts • Top horizontal rails • Sleeping cabin partition • Galvanized wire mesh wrapping • Corrugated roof cover • Rope carrying handles."
                        }
                    }
                ],
                # Page 3: Tools & Workshop Safety Protocols
                [
                    {
                        "type": "concept_explanation",
                        "title": "Tool Selection & Safety Operating Guidelines",
                        "content": {
                            "title": "Safe Hands in the Workshop",
                            "text": "- **Cross-Cut Hand Saw**: For sawing timber rails to length. *Safety*: Cut on the push stroke away from your body; keep free hand at least 15 cm away from the blade.\n- **Claw Hammer**: For driving nails and extracting bent nails. *Safety*: Hold hammer near the handle base; blunt nail tips slightly to prevent wood splitting.\n- **Wire Cutters / Pliers**: For cutting wire mesh. *Safety*: Wear heavy leather gloves to prevent wire puncture wounds; bend sharp ends inward.\n- **Measuring Tape & Square**: For marking exact 90-degree corner joints."
                        }
                    }
                ],
                # Page 4: The 5-Phase Assembly Sequence
                [
                    {
                        "type": "step_process",
                        "title": "Standard Operating Procedure: 5-Phase Assembly Sequence",
                        "content": {
                            "title": "Chronological Construction Workflow",
                            "steps": [
                                "**Phase 1: Framing the Skeleton**: Measure, mark, and cut timber. Assemble the 6x4 ft rectangular base, erect four 2-ft upright posts, and nail top rails.",
                                "**Phase 2: Enclosing Sleeping Cabin**: Wall off 2 feet at one end with solid boards or plastic sheets; install internal roosting branch 10 cm above ground.",
                                "**Phase 3: Wire Mesh Tensioning**: Roll out chicken wire over the 4-ft run, pull tight (tensioning), and hammer U-nails at 10 cm intervals.",
                                "**Phase 4: Waterproof Roofing**: Nail corrugated iron or UV plastic over the cabin, ensuring a 5 cm overhang to shed rain.",
                                "**Phase 5: Fittings & Handles**: Attach rope carrying handles at both ends and construct a hinged access door for feeding and cleaning."
                            ]
                        }
                    }
                ],
                # Page 5: Interactive Assembly Sequencing Challenge
                [
                    {
                        "type": "interactive_scenario",
                        "title": "Assembly Sequencing Challenge",
                        "content": {
                            "title": "Ordering Construction Phases",
                            "instructions": "Place the construction steps in the correct chronological order:",
                            "scenario": "Your group has gathered timber offcuts, wire mesh, nails, and corrugated iron.",
                            "question": "Which activity must be completed first?",
                            "options": [
                                "Assemble the rigid 3D rectangular box skeleton frame.",
                                "Nail the iron roofing sheet onto the empty air.",
                                "Tension wire mesh without any wooden posts.",
                                "Put chickens on the bare ground before building."
                            ],
                            "correct_feedback": "Correct! Always assemble the rigid wooden skeleton frame first because all walls, mesh panels, and roofing attach to the frame.",
                            "incorrect_feedback": "Incorrect. You cannot attach mesh or roofing without a rigid wooden skeleton frame."
                        }
                    }
                ],
                # Page 6: Formative Knowledge Check
                [
                    {
                        "type": "knowledge_check",
                        "title": "Knowledge Check: Tool Selection for Mesh Fastening",
                        "content": {
                            "question": "Which combination of tools and fasteners is required to cut and securely lock chicken wire mesh onto a timber frame?",
                            "options": [
                                "Wire cutters (to cut mesh) and a claw hammer with U-nails/staples (to fasten wire).",
                                "A wood chisel and standard 4-inch roofing nails.",
                                "A hand saw and paper glue.",
                                "A panga and plastic tape."
                            ],
                            "answer": "A",
                            "explanation": "Wire cutters allow clean trimming of wire mesh without fraying, and U-nails (double-pointed staples) grip the wire strands tightly to the timber without slipping."
                        }
                    }
                ],
                # Page 7: Summary & Connection Forward
                [
                    {
                        "type": "key_takeaway",
                        "title": "Lesson Summary",
                        "content": {
                            "text": "- Maximize **recycled materials** (softwood offcuts, bamboo, fence wire, plastic sheets).\n- Observe **workshop safety**: wear gloves when cutting wire and blunt nail tips to prevent wood splitting.\n- Follow the **5-phase assembly sequence**: Skeleton Frame -> Cabin Walls -> Wire Mesh -> Roofing -> Handles.\n- Pre-planning saves materials and guarantees a sturdy, durable structure."
                        }
                    },
                    {
                        "type": "transition",
                        "title": "Looking Ahead",
                        "content": {
                            "text": "Planning is complete! In Lesson 5, we step into the workshop for our hands-on practical carpentry and fold assembly session!"
                        }
                    }
                ]
            ]
        },

        # =====================================================================
        # LESSON 5: Practical Activity: Constructing a Poultry Fold
        # =====================================================================
        {
            "unit_order": 5,
            "unit_name": "Practical Activity: Constructing a Poultry Fold",
            "unit_description": "Hands-on carpentry: measuring & sawing timber, corner lap joints, perch fitting, wire mesh tensioning, roof overlap waterproofing, and project video.",
            "lesson_title": "Practical Activity: Constructing a Poultry Fold",
            "pages": [
                # Page 1: Visual Hook & Practical Objectives
                [
                    {
                        "type": "suggested_image",
                        "title": "Active Workshop: Hands-On Fold Fabrication",
                        "content": {
                            "title": "Active Workshop: Hands-On Fold Fabrication",
                            "caption": "Students working collaboratively in the school workshop, assembling a wooden frame base, tensioning wire mesh, and hammering U-nails."
                        }
                    },
                    {
                        "type": "learning_goal",
                        "title": "Learning Objectives: Practical Carpentry",
                        "content": {
                            "title": "What We Will Accomplish Today",
                            "goals": [
                                "Demonstrate teamwork in measuring, marking, and sawing timber rails accurately.",
                                "Assemble a square, rigid **6x4x2 ft 3D frame skeleton** using corner lap joints.",
                                "Tension and fasten **wire mesh tightly** without sagging panels.",
                                "Install a **waterproof roof overlap** and durable rope carrying handles.",
                                "Watch a practical project video and practice strict workshop housekeeping."
                            ]
                        }
                    },
                    {
                        "type": "concept_explanation",
                        "title": "Turning Blueprints into Reality",
                        "content": {
                            "title": "Collaborative Carpentry Skills",
                            "text": "Today we turn our sketches into a physical poultry shelter! Success in carpentry depends on precision and coordination: one student holding the timber steady, another driving the nail, and another checking angles with a square."
                        }
                    }
                ],
                # Page 2: Step-by-Step Framing & Woodworking Joints
                [
                    {
                        "type": "suggested_diagram",
                        "title": "5-Phase Carpentry Assembly Workflow",
                        "content": {
                            "title": "5-Phase Carpentry Assembly Workflow",
                            "caption": "Sequential carpentry diagram: 1. Base rectangle (6x4 ft) • 2. Corner vertical posts (2 ft) • 3. Solid cabin siding & roost perch • 4. Wire mesh tensioning with U-nails • 5. Roof sheet overlap & handles."
                        }
                    },
                    {
                        "type": "step_process",
                        "title": "Standard Operating Procedure: Practical Assembly",
                        "content": {
                            "title": "Step-by-Step Fabrication Protocols",
                            "steps": [
                                "**1. Sawing Rails**: Cut four 6-ft side rails, six 4-ft crossbars, and four 2-ft upright posts from cypress offcuts.",
                                "**2. Base Rectangle**: Join two 6-ft rails and two 4-ft crossbars. Drive two 3-inch nails at each corner joint.",
                                "**3. 3D Skeleton**: Nail vertical posts inside corners; top with upper rails to lock a rigid 3D box.",
                                "**4. Roosting Perch**: Nail a smooth 4-ft branch inside the cabin, elevated 10 cm above the ground.",
                                "**5. Mesh Tensioning**: Pull wire mesh tightly across the open run; drive U-nails every 10 cm.",
                                "**6. Trim & Fold Points**: Snip excess wire with cutters and bend all sharp wire ends inward into the timber!"
                            ]
                        }
                    }
                ],
                # Page 3: Waterproofing the Roof & Fitting Handles
                [
                    {
                        "type": "concept_explanation",
                        "title": "Roof Overhang & Carrying Handles",
                        "content": {
                            "title": "Weatherproofing and Portability Details",
                            "text": "- **Roof Overhang**: Nail corrugated iron or UV-stabilized plastic over the sleeping cabin, ensuring a **5 cm overhang on all sides**. This prevents driving wind-rain from running down the walls into the sleeping birds.\n- **Rope Handles**: Drill holes or nail thick sisal/nylon rope loops at the front and rear bottom corners, positioned at a comfortable lifting height for two handlers.\n- **Access Door**: Install a hinged 1.5x1.5 ft door on the top or side of the run, secured with a wooden swivel latch."
                        }
                    }
                ],
                # Page 4: Video Resource — Kitchen Garden & Poultry Housing
                [
                    {
                        "type": "suggested_video",
                        "title": "Practical Video: Grade 8 Agriculture Project & Shelter Fabrication",
                        "content": {
                            "title": "Practical Video: Grade 8 Agriculture Project & Shelter Fabrication",
                            "url": "https://www.youtube.com/watch?v=6ZjkLwQt_YE",
                            "resolved_video_id": "6ZjkLwQt_YE",
                            "caption": "Watch this step-by-step practical video demonstration on fabricating mobile shelters, garden beds, and small-scale livestock systems for CBC Grade 8 Agriculture."
                        }
                    },
                    {
                        "type": "concept_explanation",
                        "title": "Key Construction Lessons from the Video",
                        "content": {
                            "title": "Field Workshop Tips",
                            "text": "- **1. Pre-blunting Nails**: Tap the sharp point of nails with a hammer before driving them into dry softwood to crush wood fibers rather than splitting the grain.\n- **2. Wire Tensioning Teamwork**: Have two students pull the mesh taut with pliers while the third hammers the U-nail.\n- **3. Diagonal Bracing**: Add small diagonal corner timber braces if the box wobbles when lifted."
                        }
                    }
                ],
                # Page 5: Interactive Workshop Safety Diagnosis
                [
                    {
                        "type": "interactive_scenario",
                        "title": "Workshop Safety Diagnosis Challenge",
                        "content": {
                            "title": "Identifying Workshop Hazards",
                            "instructions": "Classify the workshop practice as safe or hazardous:",
                            "scenario": "A student trims chicken wire and leaves sharp 5 cm metal wire clippings scattered across the workshop floor where classmates are walking.",
                            "question": "How is this workshop practice classified?",
                            "options": [
                                "Extremely Hazardous Practice (Violates Workshop Housekeeping)",
                                "Safe & Recommended Practice"
                            ],
                            "correct_feedback": "Correct! Wire clippings and loose nails are major puncture hazards. Proper housekeeping requires sweeping waste immediately into disposal bins.",
                            "incorrect_feedback": "Incorrect. Leaving sharp metal clippings on the floor causes severe foot injuries. Waste must be swept and binned immediately."
                        }
                    }
                ],
                # Page 6: Formative Knowledge Check
                [
                    {
                        "type": "knowledge_check",
                        "title": "Knowledge Check: Correcting Sagging Mesh",
                        "content": {
                            "question": "While attaching chicken wire to the frame, a team notices the wire mesh is loose and sagging in the middle. How should they correct this?",
                            "options": [
                                "Remove the loose staples, pull the mesh tightly across the frame (tensioning), and re-drive the U-nails firmly.",
                                "Glue paper over the sagging mesh.",
                                "Leave it loose because chickens like soft walls.",
                                "Cut a large hole in the sagging section."
                            ],
                            "answer": "A",
                            "explanation": "Wire mesh must be pulled tight (tensioned) before driving U-nails to ensure rigid, gap-free predator protection."
                        }
                    }
                ],
                # Page 7: Summary & Connection Forward
                [
                    {
                        "type": "key_takeaway",
                        "title": "Lesson Summary",
                        "content": {
                            "text": "- Assemble the frame sequentially: **base rectangle, vertical posts, top rails**.\n- Pre-blunt nails to **prevent softwood from splitting**.\n- **Tension wire mesh tightly** and bend all sharp cut ends inward.\n- Provide a **5 cm roof overhang** to keep the roosting cabin 100% dry.\n- Maintain **workshop housekeeping** by collecting sawdust and wire scraps."
                        }
                    },
                    {
                        "type": "transition",
                        "title": "Looking Ahead",
                        "content": {
                            "text": "Our fold is built! But is it safe and compliant with animal welfare standards? In Lesson 6, we perform a structured quality audit and peer evaluation!"
                        }
                    }
                ]
            ]
        },

        # =====================================================================
        # LESSON 6: Evaluating and Assessing a Poultry Fold
        # =====================================================================
        {
            "unit_order": 6,
            "unit_name": "Evaluating and Assessing a Poultry Fold",
            "unit_description": "Quality auditing: structural rigidity test, escape-point security audit (<2.5 cm gaps), waterproofing leak test, weight analysis, and peer evaluation scorecard.",
            "lesson_title": "Evaluating and Assessing a Poultry Fold",
            "pages": [
                # Page 1: Visual Hook & Learning Objectives
                [
                    {
                        "type": "suggested_image",
                        "title": "Quality Audit: Peer Inspection of Completed Fold",
                        "content": {
                            "title": "Quality Audit: Peer Inspection of Completed Fold",
                            "caption": "Students conducting a systematic quality audit on a completed poultry fold, testing door latches, checking wire tension, and scoring benchmarks."
                        }
                    },
                    {
                        "type": "learning_goal",
                        "title": "Learning Objectives: Audit & Quality Benchmarks",
                        "content": {
                            "title": "What We Will Accomplish Today",
                            "goals": [
                                "Execute a structured **quality audit checklist** across 5 engineering criteria.",
                                "Identify and fix **escape points and predator gaps** (any opening > 2.5 cm).",
                                "Conduct a **portability test** and **waterproofing leak test**.",
                                "Document project results using digital photographs and oral presentations."
                            ]
                        }
                    },
                    {
                        "type": "concept_explanation",
                        "title": "The Agricultural Inspector Mindset",
                        "content": {
                            "title": "Auditing Before Introducing Livestock",
                            "text": "Before putting live chickens into a newly constructed fold, an agricultural engineer must audit the structure thoroughly. A single protruding nail head can blind a bird, a loose latch allows dogs to break in, and a roof leak causes hypothermia in baby chicks."
                        }
                    }
                ],
                # Page 2: The 5 Quality Audit Benchmarks
                [
                    {
                        "type": "comparison_table",
                        "title": "Poultry Fold Quality Audit Scorecard",
                        "content": {
                            "title": "Peer Assessment Audit Matrix",
                            "headers": ["Audit Criterion", "Target Quality Benchmark", "Practical Testing Method", "Max Score"],
                            "rows": [
                                ["1. Structural Rigidity", "Frame remains square and rigid without warping when lifted", "Lift fold 10 cm off ground by handles; shake gently", "5 Marks"],
                                ["2. Predator Security", "Zero gaps > 2.5 cm; wire tightly stapled; latch locks tightly", "Visual scan and run gloved hand along all seams & doors", "5 Marks"],
                                ["3. Cabin Waterproofing", "Roof completely sheds water; cabin interior remains bone dry", "Pour 1 liter of water on roof; check interior for leaks", "5 Marks"],
                                ["4. Portability & Weight", "Two students can slide the fold 2 meters smoothly", "Two-person manual lift and slide test across pasture", "5 Marks"],
                                ["5. Finish & Safety", "All nail heads hammered flush; zero sharp wire points", "Tactile inspection of all inner and outer frame surfaces", "5 Marks"]
                            ]
                        }
                    },
                    {
                        "type": "suggested_diagram",
                        "title": "Quality Audit Scorecard & Escape-Point Risk Map",
                        "content": {
                            "title": "Quality Audit Scorecard & Escape-Point Risk Map",
                            "caption": "Quality audit inspection diagram: Critical audit zones: 1. Roof leak points • 2. Door latch security • 3. Bottom ground clearance (<2.5cm) • 4. Handle strength • 5. Protruding wire check."
                        }
                    }
                ],
                # Page 3: Digital Documentation & Peer Feedback
                [
                    {
                        "type": "step_process",
                        "title": "Standard Operating Procedure: Digital Documentation",
                        "content": {
                            "title": "Capturing Project Evidence",
                            "steps": [
                                "**Photo 1: Isometric Overview**: Capture entire 6x4 ft fold showing open run and roofed cabin.",
                                "**Photo 2: Cabin Interior**: Close-up showing roosting perch, ventilation gap, and dry floor.",
                                "**Photo 3: Wire & Joint Detail**: Close-up of corner joints, blunted nails, and neat wire trimming.",
                                "**Photo 4: Portability Test**: Group members demonstrating safe two-person lifting by handles.",
                                "**Oral Pitch**: Present a 2-minute summary explaining materials used, budget savings, and audit score."
                            ]
                        }
                    }
                ],
                # Page 4: Interactive Audit Diagnosis Challenge
                [
                    {
                        "type": "interactive_scenario",
                        "title": "Quality Audit Diagnosis Challenge",
                        "content": {
                            "title": "Evaluating Audit Observations",
                            "instructions": "Determine if the observation passes or fails safety compliance:",
                            "scenario": "During inspection, an auditor finds that the sleeping cabin roof has a 1 cm crack between boards where water drips inside, and a corner wire has a 6 cm open hole at ground level.",
                            "question": "What is the correct audit verdict?",
                            "options": [
                                "FAILS Quality Standards: Must seal roof leak and re-staple wire mesh before birds enter",
                                "PASSES Quality Standards: Chickens enjoy rainwater and large holes"
                            ],
                            "correct_feedback": "Correct! Roof leaks cause chick hypothermia, and a 6 cm gap allows mongooses and snakes to enter easily. Both must be repaired immediately.",
                            "incorrect_feedback": "Incorrect. Any roof leak or hole over 2.5 cm fails safety standards and must be repaired before introducing chickens."
                        }
                    }
                ],
                # Page 5: Formative Knowledge Check
                [
                    {
                        "type": "knowledge_check",
                        "title": "Knowledge Check: Maximum Safe Mesh Gap",
                        "content": {
                            "question": "What is the maximum allowable gap size anywhere along the wire mesh or door frame of a secure poultry fold?",
                            "options": [
                                "No gap larger than 2.5 cm (1 inch), to prevent small predators like mongooses, weasels, and snakes from slipping inside.",
                                "Gaps up to 15 cm are acceptable.",
                                "Any gap that a human hand cannot fit through.",
                                "Gaps do not matter as long as the wood is painted."
                            ],
                            "answer": "A",
                            "explanation": "Predators like mongooses, rats, and snakes can squeeze through openings larger than 2.5 cm (1 inch). All wire mesh and door frames must be sealed to under 2.5 cm."
                        }
                    }
                ],
                # Page 6: Summary & Connection Forward
                [
                    {
                        "type": "key_takeaway",
                        "title": "Lesson Summary",
                        "content": {
                            "text": "- Audit folds across **5 criteria: rigidity, security, waterproofing, portability, and safety finish**.\n- Ensure **zero gaps over 2.5 cm** to prevent predator entry.\n- Conduct a **water leak test** on the cabin roof before introducing birds.\n- Document work with **digital photos from 4 angles** and present peer evaluations."
                        }
                    },
                    {
                        "type": "transition",
                        "title": "Looking Ahead",
                        "content": {
                            "text": "Our fold is certified safe and ready! In Lesson 7, we explore the deep ecological and economic benefits of fold-raised poultry on farm soil and pest control!"
                        }
                    }
                ],
                # Page 7: Corrective Action SOP Callout
                [
                    {
                        "type": "concept_explanation",
                        "title": "Standard Corrective Action Protocol",
                        "content": {
                            "title": "Fixing Audit Deficiencies",
                            "text": "If a fold scores below 20/25 on the audit scorecard, the team must execute corrective fixes within 24 hours: adding diagonal bracing for wobbling frames, hammering a metal cover strip over mesh gaps, or adding a secondary waterproof plastic layer over roof seams."
                        }
                    }
                ]
            ]
        },

        # =====================================================================
        # LESSON 7: Benefits of Rearing Poultry in a Fold
        # =====================================================================
        {
            "unit_order": 7,
            "unit_name": "Benefits of Rearing Poultry in a Fold",
            "unit_description": "Ecological and agronomic benefits: uniform nitrogen-rich manure deposition, biological pest control (cutworms, termites), weed suppression, and lower capital costs.",
            "lesson_title": "Benefits of Rearing Poultry in a Fold",
            "pages": [
                # Page 1: Visual Hook & Learning Objectives
                [
                    {
                        "type": "suggested_image",
                        "title": "Ecological Workers: Pasture Scratching & Fertilization",
                        "content": {
                            "title": "Ecological Workers: Pasture Scratching & Fertilization",
                            "caption": "A flock of pasture-raised chickens scratching topsoil, consuming destructive insect larvae and depositing nitrogen-rich droppings across a grassy paddock."
                        }
                    },
                    {
                        "type": "learning_goal",
                        "title": "Learning Objectives: Ecological & Economic Synergies",
                        "content": {
                            "title": "What We Will Accomplish Today",
                            "goals": [
                                "Explain how mobile folding achieves **uniform soil fertilization** without labor costs.",
                                "Analyze chickens as **biological pest control agents** (controlling cutworms, termites, grasshoppers).",
                                "Contrast the **capital and operational costs** of folding vs permanent indoor housing.",
                                "Describe the animal-welfare advantages of **sunlight, exercise, and pasture foraging**."
                            ]
                        }
                    },
                    {
                        "type": "concept_explanation",
                        "title": "The Ultimate Farm Helpers",
                        "content": {
                            "title": "Feathered Soil Cultivators",
                            "text": "In conventional farming, a farmer pays for synthetic fertilizer, pays for chemical insecticides, and spends hours weeding. In a mobile fold, chickens perform all three services naturally for free: scratching up weed seeds, devouring destructive pests, and fertilizing the soil with rich nitrogen droppings!"
                        }
                    }
                ],
                # Page 2: Manure Deposition & Nitrogen Dynamics
                [
                    {
                        "type": "suggested_diagram",
                        "title": "Ecological Benefits Flow: Soil Fertilization & Biological Control",
                        "content": {
                            "title": "Ecological Benefits Flow: Soil Fertilization & Biological Control",
                            "caption": "Ecological flowchart: Pasture grazing -> Topsoil aeration & scratch weeding -> Ingestion of insect larvae -> High-nitrogen manure deposition -> Rapid pasture regrowth."
                        }
                    },
                    {
                        "type": "concept_explanation",
                        "title": "Even Nutrient Distribution",
                        "content": {
                            "title": "No Manure Hauling Required",
                            "text": "- **In a Fixed Coop**: Manure accumulates in one foul-smelling heap, requiring manual shoveling, wheelbarrows, and labor.\n- **In a Mobile Fold**: Chickens deposit fresh droppings directly over the grass root zone every single day.\n- **Rich Nutrient Content**: Poultry manure contains **3x more nitrogen, phosphorus, and potassium** than cow manure, triggering lush, dark green pasture regeneration within 14 days!"
                        }
                    }
                ],
                # Page 3: Biological Pest & Weed Control
                [
                    {
                        "type": "comparison_table",
                        "title": "Ecological Services Provided by Folded Poultry",
                        "content": {
                            "title": "Ecological Pest & Weed Action Matrix",
                            "headers": ["Farm Target", "Traditional Expensive Method", "Mobile Fold Biological Method", "Ecological Advantage"],
                            "rows": [
                                ["Soil Pests (Cutworms, Termites, Armyworms)", "Spraying chemical insecticides", "Chickens scratch topsoil and eat larvae directly", "100% chemical-free; converts pests into protein & eggs"],
                                ["Pasture Weed Seeds", "Spraying toxic chemical herbicides", "Chickens eagerly peck and ingest weed seeds", "Suppresses weed multiplication naturally"],
                                ["Pasture Fertilization", "Buying synthetic inorganic fertilizer bags", "Chickens deposit concentrated organic manure daily", "Enriches soil organic matter and improves water retention"],
                                ["Animal Bedding & Litter", "Buying and replacing wood shavings weekly", "Pasture floor provides natural, self-cleaning bedding", "Zero bedding cost; zero indoor ammonia fumes"]
                            ]
                        }
                    }
                ],
                # Page 4: Interactive Benefit Matching Challenge
                [
                    {
                        "type": "interactive_scenario",
                        "title": "Ecological Service Matching Challenge",
                        "content": {
                            "title": "Matching Chicken Behaviors to Farm Outcomes",
                            "instructions": "Match the natural chicken behavior to its direct agricultural benefit:",
                            "scenario": "A flock of 5 chickens is shifted daily across a school pasture plot.",
                            "question": "What is the primary benefit of chickens scratching topsoil with their claws?",
                            "options": [
                                "Unearthing and consuming hidden insect pests like cutworms while aerating the soil surface.",
                                "Digging deep holes for planting large timber trees.",
                                "Sharpening their claws so they can climb trees.",
                                "Removing all soil down to the bedrock."
                            ],
                            "correct_feedback": "Correct! Scratching aerates the soil and unearths destructive insect pests, turning them into high-protein feed naturally.",
                            "incorrect_feedback": "Incorrect. Scratching unearths soil pests and aerates the surface, providing biological pest control."
                        }
                    }
                ],
                # Page 5: Formative Knowledge Check
                [
                    {
                        "type": "knowledge_check",
                        "title": "Knowledge Check: Fold Manure vs Fixed Coop Manure",
                        "content": {
                            "question": "Why is manure deposition from a mobile poultry fold superior to manure management in a permanent deep litter house?",
                            "options": [
                                "Manure is deposited evenly and directly onto pasture root zones daily with zero shoveling labor, while fixed coops accumulate ammonia-heavy waste in one spot.",
                                "Fold manure does not contain any nitrogen.",
                                "Fixed coop manure turns into liquid gold immediately.",
                                "Fold manure dissolves into pure oxygen within seconds."
                            ],
                            "answer": "A",
                            "explanation": "Mobile folds spread manure evenly across pastures with zero manual shoveling or transport labor, fertilizing recovering grass immediately without toxic indoor ammonia buildup."
                        }
                    }
                ],
                # Page 6: Summary & Connection Forward
                [
                    {
                        "type": "key_takeaway",
                        "title": "Lesson Summary",
                        "content": {
                            "text": "- Folds deposit **high-nitrogen manure evenly** across pastures, accelerating grass regrowth.\n- Chickens provide **biological pest control**, eating cutworms, termites, and weed seeds.\n- Low capital setup costs and **zero bedding expense** make folding highly profitable.\n- Outdoor grazing, exercise, and sunlight enhance **bird welfare and produce rich, yellow egg yolks**."
                        }
                    },
                    {
                        "type": "transition",
                        "title": "Looking Ahead",
                        "content": {
                            "text": "How do we put our daily management into action on the school farm? In Lesson 8, we organize chore rosters, execute clinical health checks, and manage flock health!"
                        }
                    }
                ],
                # Page 7: Egg Quality Nutrition Callout
                [
                    {
                        "type": "concept_explanation",
                        "title": "The Golden Yolk Science",
                        "content": {
                            "title": "Why Pastured Eggs are Healthier",
                            "text": "Pastured hens that forage on fresh green grass, clover, and insects produce eggs with deep golden-orange yolks. These yolks contain **2x more Vitamin E, 3x more Vitamin A, and 2x more Omega-3 fatty acids** than industrial caged eggs, providing superior nutrition for growing school children."
                        }
                    }
                ]
            ]
        },

        # =====================================================================
        # LESSON 8: Practical Activity: Daily Care and Flock Management
        # =====================================================================
        {
            "unit_order": 8,
            "unit_name": "Practical Activity: Daily Care and Flock Management",
            "unit_description": "Field execution: 4-role team chore roster (feeder, waterer, shifter, health inspector), clinical health indicators (healthy vs sick), quarantine isolation protocols, and biosecurity.",
            "lesson_title": "Practical Activity: Daily Care and Flock Management",
            "pages": [
                # Page 1: Visual Hook & Practical Objectives
                [
                    {
                        "type": "suggested_image",
                        "title": "Flock Vigilance: Morning Health Check",
                        "content": {
                            "title": "Flock Vigilance: Morning Health Check",
                            "caption": "Agriculture students performing a clinical health check on a kienyeji rooster, inspecting comb color, eye clarity, feather smoothness, and vent hygiene."
                        }
                    },
                    {
                        "type": "learning_goal",
                        "title": "Learning Objectives: Daily Flock Management",
                        "content": {
                            "title": "What We Will Accomplish Today",
                            "goals": [
                                "Establish a weekly **4-member duty roster (Feeder, Waterer, Shifter, Inspector)**.",
                                "Conduct a clinical **poultry health inspection** (differentiating healthy vs sick indicators).",
                                "Execute the **4-step sickness isolation protocol** (Quarantine, Disinfect, Consult, Record).",
                                "Maintain strict **biosecurity and hygiene standards** on the school farm."
                            ]
                        }
                    },
                    {
                        "type": "concept_explanation",
                        "title": "The Responsibility of Animal Stewardship",
                        "content": {
                            "title": "Caring for Living Flocks",
                            "text": "Confining animals inside a fold places 100% of their wellbeing in our hands. If we forget water for a single afternoon under the hot sun, birds suffer heat stroke. Executing a disciplined daily roster ensures high egg yields, rapid growth, and zero preventable sickness!"
                        }
                    }
                ],
                # Page 2: The 4-Role Team Chore Roster
                [
                    {
                        "type": "step_process",
                        "title": "Standard Operating Procedure: The 4-Role Team Chore Roster",
                        "content": {
                            "title": "Weekly Group Task Allocations",
                            "steps": [
                                "**Role 1: The Feeder**: Measures 120 grams of mash per adult bird; pours into clean troughs; supplements with chopped garden greens.",
                                "**Role 2: The Waterer**: Empties stale water; scrubs out dirt and algae; refills heavy drinkers with clean, cool water.",
                                "**Role 3: The Shifter**: Coordinates the gentle 2-person forward slide of the fold onto fresh, clean grass.",
                                "**Role 4: The Health Inspector & Egg Collector**: Checks eyes, combs, and feathers; gathers laid eggs from the nesting box."
                            ]
                        }
                    },
                    {
                        "type": "suggested_diagram",
                        "title": "Daily Husbandry Care Roster & Health Check Indicators",
                        "content": {
                            "title": "Daily Husbandry Care Roster & Health Check Indicators",
                            "caption": "Comparative clinical health diagram: Healthy bird (bright red comb, clear alert eyes, smooth feathers, active scratching) vs Sick bird (pale comb, runny eyes, ruffled feathers, drooping wings, listless corner crouching)."
                        }
                    }
                ],
                # Page 3: Clinical Health Indicators & Diagnostics
                [
                    {
                        "type": "comparison_table",
                        "title": "Clinical Health Indicators: Healthy vs. Sick Poultry",
                        "content": {
                            "title": "Diagnostic Health Matrix",
                            "headers": ["Body Part / Behavior", "Healthy Chicken Indicator", "Sick Chicken Indicator (Requires Action)"],
                            "rows": [
                                ["Eyes & Nostrils", "Bright, clear, alert, dry nostrils", "Cloudy, runny, half-closed eyes; nasal discharge"],
                                ["Comb & Wattles", "Bright red, warm, plump, and firm", "Pale, shrunken, bluish, or scabby"],
                                ["Feathers & Plumage", "Smooth, glossy, well-groomed, clean", "Ruffled, dull, dusty, or missing feathers (pecking)"],
                                ["Posture & Behavior", "Active, vocal, continuously pecking and scratching", "Listless, crouching in corner, drooping wings, open beak gasping"],
                                ["Vent / Cloaca", "Clean, dry, and free of stains", "Wet, pasty, smeared with white or bloody diarrhea"]
                            ]
                        }
                    }
                ],
                # Page 4: Sickness Emergency Action Protocol
                [
                    {
                        "type": "step_process",
                        "title": "Standard Operating Procedure: Sickness Emergency Protocol",
                        "content": {
                            "title": "Action Steps When Sickness is Detected",
                            "steps": [
                                "**Step 1: Immediate Quarantine**: Remove the sick chicken immediately and place it in a separate isolation box away from the flock.",
                                "**Step 2: Sanitize Equipment**: Scrub and disinfect the fold's feeders and drinkers with mild soapy water.",
                                "**Step 3: Consult & Diagnose**: Report symptoms to your agricultural teacher or local veterinary officer.",
                                "**Step 4: Farm Journal Entry**: Record the date, bird symptoms, and treatment given in your farm record book."
                            ]
                        }
                    }
                ],
                # Page 5: Interactive Health Diagnosis Challenge
                [
                    {
                        "type": "interactive_scenario",
                        "title": "Health Diagnosis Challenge",
                        "content": {
                            "title": "Diagnosing Flock Health",
                            "instructions": "Determine the correct immediate action for the scenario:",
                            "scenario": "During your morning inspection, you find one hen sitting listlessly in the corner with ruffled feathers, pale comb, and green diarrhea around its vent.",
                            "question": "What is the very first action your group must take?",
                            "options": [
                                "Immediately remove and isolate the sick hen in a separate quarantine cage to protect the flock.",
                                "Force the hen to eat extra grain inside the fold.",
                                "Slide the fold faster across the grass.",
                                "Wait 5 days to see if the hen recovers on its own."
                            ],
                            "correct_feedback": "Correct! Immediate isolation is the golden rule of biosecurity. It prevents infectious pathogens from spreading to healthy birds.",
                            "incorrect_feedback": "Incorrect. The first rule is immediate isolation in a quarantine pen to prevent contagious disease spread."
                        }
                    }
                ],
                # Page 6: Formative Knowledge Check
                [
                    {
                        "type": "knowledge_check",
                        "title": "Knowledge Check: Clinical Signs of Healthy Layers",
                        "content": {
                            "question": "Which of the following physical signs indicates that a laying hen inside a poultry fold is in peak physical health?",
                            "options": [
                                "Bright red plump comb, clear alert eyes, smooth glossy feathers, and active pecking behavior.",
                                "Drooping wings, watery eyes, and sleeping all day in a corner.",
                                "Ruffled plumage and a pale shrunken comb.",
                                "Continuous open-beak panting and swollen nostrils."
                            ],
                            "answer": "A",
                            "explanation": "A bright red comb, clear alert eyes, groomed feathers, and vigorous scratching are universal indicators of excellent poultry health and vitality."
                        }
                    }
                ],
                # Page 7: Summary & Connection Forward
                [
                    {
                        "type": "key_takeaway",
                        "title": "Lesson Summary",
                        "content": {
                            "text": "- Execute daily chores using a **4-role duty roster (Feeder, Waterer, Shifter, Inspector)**.\n- Healthy birds display **bright red combs, clear eyes, and active scratching**.\n- Sick birds show **drooping wings, pale combs, and ruffled plumage**.\n- Follow the **4-step isolation protocol**: Quarantine, Sanitize, Consult, Record."
                        }
                    },
                    {
                        "type": "transition",
                        "title": "Looking Ahead",
                        "content": {
                            "text": "We have mastered fold construction and flock husbandry! In our final lesson, we connect poultry folding with our vegetable gardens into an integrated, zero-waste farm loop and complete the Topic Capstone Assessment!"
                        }
                    }
                ]
            ]
        },

        # =====================================================================
        # LESSON 9: Integrated Food Production: Gardening & Poultry Loops & Capstone
        # =====================================================================
        {
            "unit_order": 9,
            "unit_name": "Integrated Food Production: Gardening & Poultry Loops",
            "unit_description": "Integrated agriculture: crop-to-poultry feed loop (vegetable residues), poultry-to-crop fertilizer loop (composted manure), circular farm design, topic video review, and 10 topic summative MCQs.",
            "lesson_title": "Integrated Food Production: Gardening & Poultry Loops & Capstone",
            "pages": [
                # Page 1: Visual Hook & Capstone Objectives
                [
                    {
                        "type": "suggested_image",
                        "title": "The Sustainable Homestead: Integrated Garden & Fold",
                        "content": {
                            "title": "The Sustainable Homestead: Integrated Garden & Fold",
                            "caption": "A thriving integrated smallholding in Kenya showcasing raised vegetable beds right beside a mobile poultry fold, recycling resources in a closed-loop system."
                        }
                    },
                    {
                        "type": "learning_goal",
                        "title": "Learning Objectives: Integrated Closed Loops & Assessment",
                        "content": {
                            "title": "What We Will Accomplish Today",
                            "goals": [
                                "Explain the principles of **nutrient recycling and resource synergy** between crops and poultry.",
                                "Recycle **kitchen garden residues** as supplementary poultry feed.",
                                "Process **chicken droppings into rich compost manure** for raised vegetable beds.",
                                "Design a complete **closed-loop backyard farm plan** on paper.",
                                "Review the Topic Video and demonstrate total mastery on the **10 Topic Summative Assessment Questions**."
                            ]
                        }
                    },
                    {
                        "type": "concept_explanation",
                        "title": "The Zero-Waste Permaculture Loop",
                        "content": {
                            "title": "Eliminating Waste Through Integration",
                            "text": "In nature, waste does not exist. Today we unite our Grade 8 Agriculture knowledge: connecting our Topic 3 Kitchen Garden with our Topic 4 Poultry Fold. Leftover cabbage leaves feed the chickens, and nitrogen-rich chicken manure fertilizes our vegetable beds. Nothing is wasted, and food production skyrockets!"
                        }
                    }
                ],
                # Page 2: The Two Reciprocal Nutrient Loops
                [
                    {
                        "type": "concept_explanation",
                        "title": "The Two Reciprocal Nutrient Loops",
                        "content": {
                            "title": "Crop-Poultry Symbiosis",
                            "text": "- **Loop 1: Crop-to-Poultry Feed**: Damaged cabbage leaves, thinned-out carrot tops, and weed seedlings are chopped and tossed into the poultry run, cutting feed costs and providing vitamins.\n- **Loop 2: Poultry-to-Crop Fertilizer**: Concentrated chicken droppings are mixed with dry garden leaves in a compost heap. High nitrogen accelerates decomposition, producing dark, rich humus to fertilize vegetable beds within weeks!"
                        }
                    },
                    {
                        "type": "suggested_diagram",
                        "title": "Circular Closed-Loop Farm Symbiosis Architecture",
                        "content": {
                            "title": "Circular Closed-Loop Farm Symbiosis Architecture",
                            "caption": "Circular agro-ecological diagram: 1. Kitchen Garden (cabbage, sukumawiki) -> Leftover leaves -> 2. Mobile Poultry Fold -> High-nitrogen manure -> 3. Compost Pile -> Rich organic humus -> 1. Kitchen Garden."
                        }
                    }
                ],
                # Page 3: Designing a Closed-Loop Backyard Blueprint
                [
                    {
                        "type": "step_process",
                        "title": "Standard Operating Procedure: Backyard Blueprinting",
                        "content": {
                            "title": "How to Map an Integrated Backyard System",
                            "steps": [
                                "**Step 1: Position Raised Beds**: Map 4x4 ft vegetable beds near the kitchen for daily harvesting and watering.",
                                "**Step 2: Define Poultry Rotation Lanes**: Map grass corridors adjacent to the garden where the fold shifts daily.",
                                "**Step 3: Establish Central Compost Station**: Position a 3-bin compost heap between the garden and the poultry run.",
                                "**Step 4: Draw Resource Vectors**: Draw green arrows (crop waste -> chickens) and brown arrows (manure -> compost -> crop soil)!"
                            ]
                        }
                    }
                ],
                # Page 4: Interactive Nutrient Flow Matching
                [
                    {
                        "type": "interactive_scenario",
                        "title": "Closed-Loop Resource Matching Challenge",
                        "content": {
                            "title": "Mapping Circular Farm Flows",
                            "instructions": "Match each farm resource to its role in the integrated loop:",
                            "scenario": "You have harvested cabbages and cleaned your poultry fold.",
                            "question": "What is the correct treatment for fresh, concentrated chicken droppings?",
                            "options": [
                                "Mix into a compost pile with dry leaves to create rich organic humus before applying to vegetable beds.",
                                "Dump them raw directly onto tiny lettuce seedlings to burn their roots.",
                                "Throw them into a plastic trash bag and send them to the city landfill.",
                                "Wash them down the drain with tap water."
                            ],
                            "correct_feedback": "Correct! Composting stabilizes high-nitrogen chicken droppings, preventing root burning and turning manure into fertile organic soil humus.",
                            "incorrect_feedback": "Incorrect. Raw droppings burn tender roots, and dumping manure wastes valuable nutrients. Composting with dry leaves is the correct method."
                        }
                    }
                ],
                # Page 5: Formative Knowledge Check & Topic Master Summary
                [
                    {
                        "type": "knowledge_check",
                        "title": "Knowledge Check: Raw Manure vs Composted Manure",
                        "content": {
                            "question": "Why should fresh chicken manure be composted with organic matter before being applied to delicate garden vegetables?",
                            "options": [
                                "Fresh chicken manure has extremely high concentrated nitrogen that will chemically burn delicate plant root tissues unless decomposed in compost.",
                                "Fresh manure freezes plant roots into ice.",
                                "Fresh manure turns all vegetables into weeds.",
                                "Composting removes all nutrients so plants stay small."
                            ],
                            "answer": "A",
                            "explanation": "Fresh poultry manure is very high in uric acid and nitrogen. Composting with carbon-rich dry leaves stabilizes the nitrogen, creating safe, nutrient-rich organic humus that won't burn delicate crop roots."
                        }
                    },
                    {
                        "type": "key_takeaway",
                        "title": "Topic 4 Master Summary: Poultry Rearing in a Fold",
                        "content": {
                            "text": "- **Poultry folds** provide predator defense while enabling **daily fresh pasture foraging**.\n- Shifting folds every **24 hours breaks parasite cycles** and distributes **nitrogen manure evenly**.\n- Construct folds with **4-5 sq ft per bird**, cross-ventilation, solid draft-free cabins, and tight wire mesh.\n- Follow disciplined **daily husbandry rosters** and clinical **health checks**.\n- Connect folds with **kitchen gardens into a zero-waste integrated circular farm loop**."
                        }
                    }
                ],
                # Page 6: Topic Video Review
                [
                    {
                        "type": "suggested_video",
                        "title": "Topic Video Review: Integrated Farming & Zero-Waste Systems",
                        "content": {
                            "title": "Topic Video Review: Integrated Farming & Zero-Waste Systems",
                            "url": "https://www.youtube.com/watch?v=uFnDdYWgkV8",
                            "resolved_video_id": "uFnDdYWgkV8",
                            "caption": "Watch this comprehensive real-world tour of G-BiACK Kenya demonstrating zero-waste integrated farming, closed-loop nutrient recycling, and mobile poultry systems."
                        }
                    },
                    {
                        "type": "concept_explanation",
                        "title": "Key Focus Questions for Video Review",
                        "content": {
                            "title": "Final Review Concepts",
                            "text": "- **1. Closed-Loop Flows**: Notice how crop residues feed small livestock, and animal wastes are composted into organic fertilizer.\n- **2. Daily Routines**: Observe the discipline of shifting mobile pens, cleaning drinkers, and inspecting bird health.\n- **3. Economic Impact**: See how smallholder families eliminate grocery and fertilizer purchases through smart integration."
                        }
                    }
                ],
                # Page 7: Topic Assessment Part 1 (Questions 1 to 2)
                [
                    {
                        "type": "knowledge_check",
                        "title": "Topic Assessment - Question 1: Poultry Fold Definition",
                        "content": {
                            "question": "What is the primary function of a mobile poultry fold?",
                            "options": [
                                "To provide a portable wood-and-wire enclosure that allows a small flock of birds to graze on fresh pasture safely under predator protection.",
                                "To herd cattle across dry arid plains.",
                                "To store dry grain sacks during the rainy season.",
                                "To transport vegetables to urban markets on buses."
                            ],
                            "answer": "A",
                            "explanation": "A poultry fold is a mobile housing structure combining a secure sleeping cabin with an open-bottom grazing run shifted across pasture daily."
                        }
                    },
                    {
                        "type": "knowledge_check",
                        "title": "Topic Assessment - Question 2: Wire Mesh Selection",
                        "content": {
                            "question": "Which material is best suited for covering the daytime grazing run of a mobile poultry fold?",
                            "options": [
                                "1-inch galvanized chicken wire mesh secured with U-nails.",
                                "Thin mosquito netting.",
                                "Corrugated black plastic sheets.",
                                "Cardboard boxes."
                            ],
                            "answer": "A",
                            "explanation": "Galvanized wire mesh provides strong cross-ventilation, allows sunlight to enter, and prevents predators from tearing their way inside."
                        }
                    }
                ],
                # Page 8: Topic Assessment Part 2 (Questions 3 to 5)
                [
                    {
                        "type": "knowledge_check",
                        "title": "Topic Assessment - Question 3: Daily Shifting Frequency",
                        "content": {
                            "question": "How often should a mobile poultry fold be shifted to a new patch of pasture?",
                            "options": [
                                "Every single day (every 24 hours).",
                                "Once every month.",
                                "Once a year.",
                                "Only after severe hailstorms."
                            ],
                            "answer": "A",
                            "explanation": "Daily shifting is essential to supply fresh green forage, prevent grass root destruction, and break parasite disease cycles."
                        }
                    },
                    {
                        "type": "knowledge_check",
                        "title": "Topic Assessment - Question 4: Pasture Fertilization Effect",
                        "content": {
                            "question": "What happens to a pasture plot after a mobile poultry fold is rotated across it in a planned grid?",
                            "options": [
                                "The topsoil is aerated by scratching and fertilized by concentrated nitrogen droppings, stimulating rapid, thick grass regrowth.",
                                "The soil turns into toxic ash where no plants can grow.",
                                "The grass is permanently killed forever.",
                                "Wild hawks build permanent nests on the ground."
                            ],
                            "answer": "A",
                            "explanation": "Scratching aerates topsoil while concentrated droppings add nitrogen, phosphorus, and potassium, triggering vigorous grass regeneration."
                        }
                    },
                    {
                        "type": "knowledge_check",
                        "title": "Topic Assessment - Question 5: Solid Cabin Walls Rationale",
                        "content": {
                            "question": "Why are the sleeping cabins in poultry folds built with solid wooden walls on three sides?",
                            "options": [
                                "To protect roosting birds from freezing drafts and cold wind-driven rain at night.",
                                "To prevent the chickens from looking at the stars.",
                                "To make the fold heavier so students cannot move it.",
                                "To stop birds from singing in the morning."
                            ],
                            "answer": "A",
                            "explanation": "Solid walls shield roosting birds from chilling drafts and damp night winds, preventing hypothermia and respiratory sickness."
                        }
                    }
                ],
                # Page 9: Topic Assessment Part 3 (Questions 6 to 8)
                [
                    {
                        "type": "knowledge_check",
                        "title": "Topic Assessment - Question 6: Spatial Density Calculation",
                        "content": {
                            "question": "A student group is building a poultry fold for 4 adult kienyeji chickens. According to standard spatial density rules (5 sq ft per bird), what are the optimal dimensions?",
                            "options": [
                                "6 feet long by 4 feet wide (24 square feet total area).",
                                "1 foot long by 1 foot wide.",
                                "20 feet long by 20 feet wide.",
                                "10 feet tall by 1 foot wide."
                            ],
                            "answer": "A",
                            "explanation": "For 4 adult birds, 4 × 5 = 20 sq ft minimum. A 6x4 ft frame provides 24 sq ft, ensuring ample space for foraging, perching, and exercise."
                        }
                    },
                    {
                        "type": "knowledge_check",
                        "title": "Topic Assessment - Question 7: Biological Pest Control Mechanism",
                        "content": {
                            "question": "How do pastured chickens act as effective biological control agents on a farm?",
                            "options": [
                                "They naturally scratch topsoil to hunt and devour destructive insect pests like cutworms, termites, and armyworms without chemical sprays.",
                                "They spray chemical pesticides from their beaks.",
                                "They lay eggs that frighten insect pests away.",
                                "They create loud sounds that scare weeds away."
                            ],
                            "answer": "A",
                            "explanation": "Chickens actively scratch topsoil and consume insect larvae and weed seeds, providing chemical-free biological pest management."
                        }
                    },
                    {
                        "type": "knowledge_check",
                        "title": "Topic Assessment - Question 8: Sickness Isolation Protocol",
                        "content": {
                            "question": "During a morning inspection, a student notices one chicken standing in a corner with ruffled feathers, pale comb, and drooping wings. What is the first emergency step?",
                            "options": [
                                "Immediately isolate the sick bird in a separate quarantine cage to prevent disease transmission to the rest of the flock.",
                                "Slide the fold rapidly across the farm.",
                                "Add extra grain to the feeder and leave the bird inside.",
                                "Spray the sick bird with cold tap water."
                            ],
                            "answer": "A",
                            "explanation": "Immediate isolation in a quarantine pen prevents contagious disease spread, followed by sanitizing feeders/drinkers and consulting a veterinarian."
                        }
                    }
                ],
                # Page 10: Topic Assessment Part 4 (Questions 9 to 10)
                [
                    {
                        "type": "knowledge_check",
                        "title": "Topic Assessment - Question 9: Carpentry Blunted Nail Rationale",
                        "content": {
                            "question": "Why is it recommended to slightly blunt the sharp tip of nails with a hammer before driving them into dry cypress timber frames?",
                            "options": [
                                "Blunted nails punch through and crush wood fibers rather than wedging along the grain, preventing dry timber from splitting and cracking.",
                                "Blunted nails make the wood change into steel.",
                                "Blunted nails make hammering louder.",
                                "Sharp nails attract termites to the joints."
                            ],
                            "answer": "A",
                            "explanation": "A blunted nail tip crushes through wood fibers instead of acting as a wedge, preventing dry softwood from splitting along the grain."
                        }
                    },
                    {
                        "type": "knowledge_check",
                        "title": "Topic Assessment - Question 10: Closed-Loop Integration Dynamics",
                        "content": {
                            "question": "In an integrated backyard food system, how do kitchen gardening and poultry folding create a zero-waste circular loop?",
                            "options": [
                                "Garden vegetable residues feed the chickens (providing vitamins), while chicken droppings are composted with dry leaves to fertilize vegetable beds (providing nutrients).",
                                "Chickens are buried in the garden beds to grow new vegetables.",
                                "Vegetable plants are moved inside the chicken coop to replace wood perches.",
                                "The chickens are trained to weed the garden with metal hoes."
                            ],
                            "answer": "A",
                            "explanation": "Crop residues supply green supplementary poultry feed, while chicken manure accelerates composting to fertilize crop beds in a complete zero-waste cycle."
                        }
                    }
                ]
            ]
        }
    ]

def ingest_cbc_grade8_agriculture_topic4(replace: bool = True):
    """Executes the database transaction to ingest Topic 4 into CBC Grade 8 Agriculture."""
    print("=" * 80)
    print("STARTING CONTENT INGESTION: CBC GRADE 8 AGRICULTURE — TOPIC 4 (DEEP EDITION)")
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

        topic_name = "Poultry Rearing in a Fold"
        if replace:
            existing_topics = Topic.objects.filter(subject=subject, name=topic_name)
            if existing_topics.exists():
                print(f"[*] Found existing topic '{topic_name}' (ID: {existing_topics.first().id}). Deleting for clean replace...")
                existing_topics.delete()

        topic, created = Topic.objects.get_or_create(
            subject=subject,
            name=topic_name,
            defaults={
                "order": 4,
                "description": "Comprehensive poultry husbandry in mobile folds: housing system comparison, daily pasture shifting, spatial density formulas (6x4 ft), local material selection, practical carpentry assembly, quality safety auditing, ecological fertilization & pest control, clinical health management, and integrated closed-loop backyard gardening."
            }
        )
        print(f"[*] Topic: '{topic.name}' (ID: {topic.id}, Created: {created})")

        curriculum_data = build_topic4_curriculum()
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
                        block_id=f"g8_agri_t4_u{u_order}_p{page_idx}_b{comp_idx}",
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
        print(f"[SUCCESS] Ingestion Complete for Grade 8 Topic 4: '{topic.name}'")
        print(f"[*] Units Created:   {total_units}")
        print(f"[*] Lessons Created: {total_lessons}")
        print(f"[*] Total Pages:     {total_pages}")
        print(f"[*] Total Blocks:    {total_blocks}")
        print("=" * 80)

if __name__ == "__main__":
    replace_flag = "--replace" in sys.argv or True
    ingest_cbc_grade8_agriculture_topic4(replace=replace_flag)
