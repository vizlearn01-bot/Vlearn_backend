"""
VLearn CBC Grade 8 Agriculture — Topic 5: Crop Pest and Disease Control
Production Ingestion Engine (Phase 1: Content & Card Architecture - Deep Pedagogical Edition)

Curriculum: CBC (Curriculum ID: 5)
Grade: Grade 8 (ID: 15, Level: 8)
Subject: Agriculture
Topic: Crop Pest and Disease Control (Topic Order: 5)

Decomposed into 8 Learning Units & 8 Published Lessons:
  1. Identifying Crop Pests and affected Vegetables (7 Pages, 12 Blocks)
  2. Identifying Vegetable Crop Diseases (7 Pages, 12 Blocks)
  3. General Pest Control Methods (7 Pages, 12 Blocks)
  4. General Disease Control Methods (7 Pages, 13 Blocks)
  5. Economic and Production Impacts (7 Pages, 12 Blocks)
  6. Natural Pesticides: The Science and Safety of Ash (7 Pages, 12 Blocks)
  7. Practical Activity: Preparing and Applying Wood Ash (7 Pages, 13 Blocks)
  8. Topic Assessment and Review on Crop Pest and Disease Control (10 Pages, 22 Blocks)

Deep Pedagogical Enhancements:
  - Strict 1 Card = 1 Understandable Idea progression.
  - Zero citation leaks ([1], [112]), zero developer meta-tags, zero raw unrendered LaTeX.
  - Formative scenario MCQs and Topic Summative MCQs with comprehensive educational explanations.
  - Multi-video integrations embedded across individual practical lessons.

Usage:
  ./venv/bin/python curriculum/ingest_cbc_grade8_agriculture_topic5.py [--replace]
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

def build_topic5_curriculum():
    """Returns the comprehensive pedagogical page and block structure for Grade 8 Topic 5: Crop Pest and Disease Control."""
    return [
        # =====================================================================
        # LESSON 1: Identifying Crop Pests and affected Vegetables
        # =====================================================================
        {
            "unit_order": 1,
            "unit_name": "Identifying Crop Pests and affected Vegetables",
            "unit_description": "Pest definition, insect classification by mouthparts (biting/chewing, piercing/sucking, boring/burrowing), host vegetables (kale, spinach, tomato), and beneficial predatory insects.",
            "lesson_title": "Identifying Crop Pests and affected Vegetables",
            "pages": [
                # Page 1: Visual Hook & Learning Objectives
                [
                    {
                        "type": "suggested_image",
                        "title": "Garden Hunters & Pests: Aphids on Green Foliage",
                        "content": {
                            "title": "Garden Hunters & Pests: Aphids on Green Foliage",
                            "caption": "A close-up of a leafy vegetable showing tiny sap-sucking aphids clustered under the leaf veins, being hunted by a beneficial predatory ladybug."
                        }
                    },
                    {
                        "type": "learning_goal",
                        "title": "Learning Objectives: Entomological Classifications",
                        "content": {
                            "title": "What We Will Accomplish Today",
                            "goals": [
                                "Define **crop pest** as any living organism capable of causing economic damage or death to crop plants.",
                                "Classify insect pests into 3 groups based on **mouthparts and feeding modes**.",
                                "Identify common vegetable pests affecting **kale (sukumawiki), spinach, tomatoes, and onions**.",
                                "Distinguish **destructive crop pests** from **beneficial predatory garden insects**."
                            ]
                        }
                    },
                    {
                        "type": "concept_explanation",
                        "title": "Becoming a Plant Doctor",
                        "content": {
                            "title": "Observing the Invisible Saboteurs",
                            "text": "When we walk into our vegetable gardens, we often find holes in leaves, curled yellow shoots, and seedlings chopped off at the soil line. To protect our food supply, we must act as **Plant Doctors**: identifying the specific insect pests by examining the damage left behind on our crops!"
                        }
                    }
                ],
                # Page 2: Classification of Insect Pests by Mouthparts
                [
                    {
                        "type": "concept_explanation",
                        "title": "Insect Feeding Modes & Mouthpart Anatomy",
                        "content": {
                            "title": "How Insects Eat Our Crops",
                            "text": "Insects attack crops using three specialized mouthpart mechanisms:\n\n- **1. Biting and Chewing Insects**: Possess strong mandibles (jaws) to bite, chew, and tear solid leaf tissue. *Examples*: Grasshoppers, leaf-eating caterpillars, and armyworms. *Damage*: Large ragged holes in leaves, skeletonized foliage, and complete defoliation.\n- **2. Piercing and Sucking Insects**: Possess needle-like stylets to puncture plant epidermis and suck sweet sap. *Examples*: Aphids, whiteflies, thrips, and spider mites. *Damage*: Curled leaves, yellow mottling, stunted growth, and sticky black honeydew mold.\n- **3. Boring and Burrowing Insects**: Possess tunneling jaws adapted to drill inside stems, fruits, and stored grains. *Examples*: Stem borers, tomato fruit borers, and maize weevils. *Damage*: Hollowed stems, entry holes in fruits, and powdery flour on stored seeds."
                        }
                    },
                    {
                        "type": "suggested_diagram",
                        "title": "Insect Pest Mouthparts & Feeding Damage Classification",
                        "content": {
                            "title": "Insect Pest Mouthparts & Feeding Damage Classification",
                            "caption": "Entomological diagnostic chart: 1. Biting/Chewing (caterpillars -> leaf holes) • 2. Piercing/Sucking (aphids -> leaf curling & honeydew) • 3. Boring/Burrowing (weevils -> hollow stems & grains)."
                        }
                    }
                ],
                # Page 3: Beneficial Insects (The Farmer's Friends)
                [
                    {
                        "type": "concept_explanation",
                        "title": "Beneficial Predators: Nature's Pest Regulators",
                        "content": {
                            "title": "Not All Bugs are Enemies!",
                            "text": "Many insects in our gardens are crucial allies that hunt and consume crop pests naturally:\n\n- **Ladybugs (Ladybird Beetles)**: Both larvae and adults are voracious predators that devour up to 50 aphids every single day!\n- **Praying Mantises & Assassin Bugs**: Ambush and consume large caterpillars, grasshoppers, and beetles.\n- **Spiders & Lacewings**: Weave webs and actively hunt flying moth pests and thrips.\n- **Ecological Value**: Protecting beneficial insects reduces pest populations naturally without requiring toxic chemical pesticides!"
                        }
                    },
                    {
                        "type": "comparison_table",
                        "title": "Crop Pests vs. Beneficial Garden Predators",
                        "content": {
                            "title": "Garden Insect Classification Matrix",
                            "headers": ["Insect Name", "Ecological Role", "Feeding Mode / Food Source", "Impact on Vegetable Garden"],
                            "rows": [
                                ["Aphid", "Destructive Crop Pest", "Piercing & sucking plant sap", "Causes leaf curling, yellowing, and spreads viral diseases"],
                                ["Caterpillar (Leaf Worm)", "Destructive Crop Pest", "Biting & chewing green foliage", "Chews large ragged holes, defoliating whole plants"],
                                ["Cutworm", "Destructive Soil Pest", "Biting seedling stems at soil line", "Chops down newly transplanted seedlings overnight"],
                                ["Ladybug Beetle", "Beneficial Predator", "Carnivorous predation on aphids", "Controls aphid populations naturally for free"],
                                ["Praying Mantis", "Beneficial Predator", "Carnivorous hunting of large bugs", "Preys on grasshoppers, moths, and caterpillars"],
                                ["Garden Spider", "Beneficial Predator", "Web trapping of flying insects", "Captures moths and flies before they lay eggs on crops"]
                            ]
                        }
                    }
                ],
                # Page 4: Interactive Pest Classification Challenge
                [
                    {
                        "type": "interactive_scenario",
                        "title": "Pest & Predator Diagnosis Challenge",
                        "content": {
                            "title": "Diagnosing Garden Bugs",
                            "instructions": "Determine whether the insect is a destructive crop pest or a beneficial friend:",
                            "scenario": "While inspecting your kale bed, you find a fat brown caterpillar chewing through a leaf, and nearby, a bright red ladybug beetle eating a cluster of yellow aphids.",
                            "question": "What is the correct agricultural action?",
                            "options": [
                                "Remove/handpick the caterpillar (crop pest) while protecting and leaving the ladybug (beneficial predator) on the plant.",
                                "Spray strong poison to kill both the caterpillar and the ladybug immediately.",
                                "Feed more leaves to the caterpillar.",
                                "Remove the ladybug because red bugs eat wood."
                            ],
                            "correct_feedback": "Correct! Always remove destructive pests like caterpillars while preserving beneficial predators like ladybugs, which control aphids naturally for free.",
                            "incorrect_feedback": "Incorrect. Ladybugs are beneficial predators that eat aphids. You must protect ladybugs and only remove destructive pests."
                        }
                    }
                ],
                # Page 5: Formative Knowledge Check
                [
                    {
                        "type": "knowledge_check",
                        "title": "Knowledge Check: Soil Cutworm Behavior",
                        "content": {
                            "question": "Which destructive pest lives hidden in the topsoil and is notorious for chopping down young vegetable seedlings right at the ground level?",
                            "options": [
                                "Cutworms (caterpillars of night-flying moths that sever young stems at the soil surface).",
                                "Ladybugs.",
                                "Honeybees.",
                                "Earthworms."
                            ],
                            "answer": "A",
                            "explanation": "Cutworms hide in topsoil during the day and emerge at night to chew through the stems of young seedlings right at ground level, felling them like tiny trees."
                        }
                    }
                ],
                # Page 6: Summary & Connection Forward
                [
                    {
                        "type": "key_takeaway",
                        "title": "Lesson Summary",
                        "content": {
                            "text": "- A **crop pest** causes physical damage or death to crops (insects, rodents, nematodes).\n- Insects feed via **biting/chewing** (caterpillars), **piercing/sucking** (aphids), or **boring/burrowing** (weevils).\n- **Beneficial predators** like ladybugs and spiders naturally regulate pest numbers.\n- Careful observation helps farmers identify pest attacks early before severe yield loss occurs."
                        }
                    },
                    {
                        "type": "transition",
                        "title": "Looking Ahead",
                        "content": {
                            "text": "What about microscopic germs that cause plants to spot, rot, and wilt without visible insects? In Lesson 2, we learn how to diagnose vegetable crop diseases!"
                        }
                    }
                ],
                # Page 7: Soil Pest Callout
                [
                    {
                        "type": "concept_explanation",
                        "title": "Microscopic Nematodes: Hidden Root Pests",
                        "content": {
                            "title": "The Underground Attackers",
                            "text": "Not all pests have legs or wings! **Root-knot nematodes** are microscopic roundworms living in soil that burrow into tomato and carrot roots. They cause abnormal swelling (galls/knots), preventing roots from absorbing water and fertilizer, leaving plants permanently stunted and yellow."
                        }
                    }
                ]
            ]
        },

        # =====================================================================
        # LESSON 2: Identifying Vegetable Crop Diseases
        # =====================================================================
        {
            "unit_order": 2,
            "unit_name": "Identifying Vegetable Crop Diseases",
            "unit_description": "Definition of crop disease, pathogenic causes (fungi, bacteria, viruses), diagnostic symptoms (leaf spots, powdery mildew, early/late blight, bacterial wilt), and field survey protocols.",
            "lesson_title": "Identifying Vegetable Crop Diseases",
            "pages": [
                # Page 1: Visual Hook & Learning Objectives
                [
                    {
                        "type": "suggested_image",
                        "title": "Field Pathology: Inspecting Diseased Crops",
                        "content": {
                            "title": "Field Pathology: Inspecting Diseased Crops",
                            "caption": "An agriculture student closely inspecting a tomato leaf showing distinct dark brown circular leaf spots with yellow halo margins caused by a fungal pathogen."
                        }
                    },
                    {
                        "type": "learning_goal",
                        "title": "Learning Objectives: Diagnosing Plant Pathology",
                        "content": {
                            "title": "What We Will Accomplish Today",
                            "goals": [
                                "Define **crop disease** and identify its 3 primary microscopic causes (fungi, bacteria, viruses).",
                                "Recognize and diagnose 4 primary visual symptoms: **leaf spots, powdery mildew, blight rot, and bacterial wilt**.",
                                "Execute a structured **field disease survey** using digital photography and journals.",
                                "Follow strict hygiene rules to avoid transferring spores between beds."
                            ]
                        }
                    },
                    {
                        "type": "concept_explanation",
                        "title": "The Invisible Germs of Agriculture",
                        "content": {
                            "title": "Why Vegetables Get Sick",
                            "text": "A plant disease occurs when microscopic pathogens invade plant tissues, disrupting normal physiology like photosynthesis or water uptake. Unlike insect damage where leaves are physically eaten, diseased plants develop discoloration, dead tissue patches, or sudden structural collapse!"
                        }
                    }
                ],
                # Page 2: The 4 Primary Disease Symptoms
                [
                    {
                        "type": "concept_explanation",
                        "title": "The 4 Core Disease Symptoms in Vegetables",
                        "content": {
                            "title": "Visual Signs of Plant Infection",
                            "text": "- **1. Leaf Spot (Fungal / Bacterial)**: Distinct circular brown or black dead lesions surrounded by yellow halos (e.g., Early Blight on tomatoes and Septoria on kales). Concentric rings create a 'bullseye' target pattern.\n- **2. Powdery Mildew (Fungal)**: A flour-like white powder coating the upper surfaces of leaves (common on pumpkins, courgettes, and peas), blocking sunlight and starving the plant.\n- **3. Blight Rot (Fungal / Water Mold)**: Rapid browning and water-soaked rotting of leaves, stems, and fruits. Late blight turns whole tomato crops black and slimy within days of wet weather.\n- **4. Bacterial Wilt (Bacterial)**: The entire plant collapses and droops suddenly while the soil remains wet. Bacteria multiply inside the stem's vascular xylem vessels, physically blocking water movement from roots to leaves!"
                        }
                    },
                    {
                        "type": "suggested_diagram",
                        "title": "Crop Disease Diagnostic Anatomy & Pathogen Cross-Sections",
                        "content": {
                            "title": "Crop Disease Diagnostic Anatomy & Pathogen Cross-Sections",
                            "caption": "Diagnostic plant pathology anatomy: 1. Leaf Spot (bullseye necrotic center) • 2. Powdery Mildew (white fungal mycelium layer) • 3. Blight Rot (water-soaked black tissue) • 4. Bacterial Wilt (xylem vessel blockage & sudden collapse)."
                        }
                    }
                ],
                # Page 3: Pathogen Classes & Transmission Vectors
                [
                    {
                        "type": "comparison_table",
                        "title": "Crop Pathogen Classes & Characteristics",
                        "content": {
                            "title": "Microscopic Pathogen Comparison Matrix",
                            "headers": ["Pathogen Class", "Microscopic Nature", "Typical Symptoms", "Primary Spread Vector", "Key Control Strategy"],
                            "rows": [
                                ["Fungi", "Spore-forming microscopic filaments", "Leaf spots, powdery mildew, rusts, blights", "Wind gusts, rainwater splashing, wet tools", "Pruning, wood ash dusting, dry spacing"],
                                ["Bacteria", "Single-celled microscopic organisms", "Soft slimy rots, bacterial wilt, leaf spots", "Dirty pruning knives, root wounds, contaminated water", "Tool sterilization, crop culling, deep pit burial"],
                                ["Viruses", "Sub-microscopic genetic capsules", "Mosaic mottling, yellow veins, stunted curling", "Insect vectors (aphids, whiteflies), infected seeds", "Control insect vectors, plant certified clean seeds"],
                                ["Nematodes", "Microscopic soil roundworms", "Root swelling galls, stunting, chronic wilting", "Contaminated topsoil, dirty jembes, infected seedlings", "Crop rotation with marigolds, solarization"]
                            ]
                        }
                    }
                ],
                # Page 4: Interactive Disease Diagnostic Challenge
                [
                    {
                        "type": "interactive_scenario",
                        "title": "Disease Diagnostic Challenge",
                        "content": {
                            "title": "Diagnosing Field Symptoms",
                            "instructions": "Match the plant symptom to its correct scientific disease diagnosis:",
                            "scenario": "You water your tomato plants in the morning. By 2:00 PM, one healthy-looking plant has completely collapsed and drooped, even though the soil is wet.",
                            "question": "What disease has attacked this tomato plant?",
                            "options": [
                                "Bacterial Wilt (bacteria multiplying inside xylem stems and blocking water transport)",
                                "Drought (the plant needs 50 liters of water)",
                                "Powdery Mildew (white flour on leaves)",
                                "Bird Attack (birds drank all the sap)"
                            ],
                            "correct_feedback": "Correct! Sudden wilting while soil is wet is the classic symptom of Bacterial Wilt. Bacteria plug the water channels inside the stem.",
                            "incorrect_feedback": "Incorrect. Drought only occurs in dry soil. Sudden collapse in wet soil is Bacterial Wilt."
                        }
                    }
                ],
                # Page 5: Formative Knowledge Check
                [
                    {
                        "type": "knowledge_check",
                        "title": "Knowledge Check: Powdery Mildew Mechanism",
                        "content": {
                            "question": "Why does a powdery mildew fungal infection harm crop growth even if it does not chew holes in the leaves?",
                            "options": [
                                "The white fungal layer coats the leaf surface, physically blocking sunlight from reaching chlorophyll and stopping photosynthesis.",
                                "It makes the leaves turn into ice.",
                                "It attracts monkeys to the garden.",
                                "It causes the soil to dissolve."
                            ],
                            "answer": "A",
                            "explanation": "Powdery mildew forms a dense white carpet of fungal mycelium over the leaf surface, blocking sunlight and severely inhibiting photosynthesis, starving the plant."
                        }
                    }
                ],
                # Page 6: Summary & Connection Forward
                [
                    {
                        "type": "key_takeaway",
                        "title": "Lesson Summary",
                        "content": {
                            "text": "- **Crop diseases** are caused by microscopic **fungi, bacteria, viruses, or nematodes**.\n- Core symptoms include **leaf spots, powdery mildew, blight rot, and bacterial wilt**.\n- **Bacterial wilt** causes sudden drooping in wet soil due to vascular stem blockage.\n- Field diagnosis requires close inspection, photographic logging, and tool hygiene."
                        }
                    },
                    {
                        "type": "transition",
                        "title": "Looking Ahead",
                        "content": {
                            "text": "Now that we can identify pests and diseases, what methods do we use to control them? In Lesson 3, we compare the 5 major pest control pathways!"
                        }
                    }
                ],
                # Page 7: Raindrop Splashing Callout
                [
                    {
                        "type": "concept_explanation",
                        "title": "Raindrop Spore Splashing Physics",
                        "content": {
                            "title": "How Fungi Jump to Leaves",
                            "text": "Most fungal spores sleep in the topsoil. When heavy raindrops hit bare soil, the kinetic energy creates muddy splash droplets that fling spores up to 60 cm into the air, landing on lower vegetable leaves! Mulching with dry straw covers bare soil, physically blocking rain splashes and preventing 80% of fungal infections."
                        }
                    }
                ]
            ]
        },

        # =====================================================================
        # LESSON 3: General Pest Control Methods
        # =====================================================================
        {
            "unit_order": 3,
            "unit_name": "General Pest Control Methods",
            "unit_description": "Five control categories: Cultural (crop rotation, clean weeding), Mechanical (handpicking, sticky traps), Biological (beneficial predators), Chemical (synthetic sprays as last resort), and Biotechnology (resistant seed varieties).",
            "lesson_title": "General Pest Control Methods",
            "pages": [
                # Page 1: Visual Hook & Learning Objectives
                [
                    {
                        "type": "suggested_image",
                        "title": "Integrated Pest Management: Biological Control in Action",
                        "content": {
                            "title": "Integrated Pest Management: Biological Control in Action",
                            "caption": "A beneficial ladybug beetle actively hunting and eating destructive aphids on a vegetable plant, providing chemical-free biological pest regulation."
                        }
                    },
                    {
                        "type": "learning_goal",
                        "title": "Learning Objectives: Pest Management Pathways",
                        "content": {
                            "title": "What We Will Accomplish Today",
                            "goals": [
                                "List and explain the **5 primary categories of crop pest control**.",
                                "Describe how **cultural practices (crop rotation, timely planting)** prevent pest build-up.",
                                "Analyze why **biological and mechanical methods** are environmentally superior to synthetic chemicals.",
                                "Explain why **synthetic chemicals should only be an emergency last resort**."
                            ]
                        }
                    },
                    {
                        "type": "concept_explanation",
                        "title": "The Hierarchy of Pest Control",
                        "content": {
                            "title": "Prevent First, Spray Last",
                            "text": "Modern agricultural science follows **Integrated Pest Management (IPM)**: we use smart preventive habits (cultural), physical traps (mechanical), and natural predators (biological) first. We only use synthetic chemical poisons as an emergency last resort because chemicals kill friendly bugs, contaminate water, and leave toxic residues on our food!"
                        }
                    }
                ],
                # Page 2: The 5 Pest Control Pathways
                [
                    {
                        "type": "comparison_table",
                        "title": "The 5 Crop Pest Control Pathways",
                        "content": {
                            "title": "Pest Control Methodology Matrix",
                            "headers": ["Control Category", "Mechanism of Action", "Practical Farm Examples", "Key Advantage", "Environmental Safety"],
                            "rows": [
                                ["1. Cultural Control", "Modifying farming habits to prevent pest survival", "Crop rotation, clean border weeding, early planting", "Zero cash cost; prevents outbreaks naturally", "100% Green & Safe"],
                                ["2. Mechanical Control", "Physically capturing, crushing, or barrier-blocking pests", "Handpicking caterpillars into soapy water, yellow sticky traps", "Immediate pest removal; zero chemicals", "100% Green & Safe"],
                                ["3. Biological Control", "Utilizing natural enemies (predators, parasites, fungi)", "Releasing ladybugs to eat aphids, predatory wasps", "Self-sustaining; targets only pest species", "100% Green & Safe"],
                                ["4. Biotechnology", "Breeding or selecting pest-immune seed varieties", "Planting African maize varieties bred to resist stem borers", "Internal plant defense; zero labor during growth", "Safe & Sustainable"],
                                ["5. Chemical Control", "Spraying synthetic chemical poisons (insecticides)", "Spraying organophosphate chemical insecticides", "Fast knockdown during catastrophic outbreaks", "High Risk (Toxic residues & water pollution)"]
                            ]
                        }
                    },
                    {
                        "type": "suggested_diagram",
                        "title": "5 Pest Control Pathways Comparison Matrix & Hierarchy",
                        "content": {
                            "title": "5 Pest Control Pathways Comparison Matrix & Hierarchy",
                            "caption": "IPM Pyramidal Hierarchy: Base: Cultural Prevention (Crop rotation) -> Tier 2: Mechanical (Handpicking & traps) -> Tier 3: Biological (Ladybugs) -> Tier 4: Natural Botanicals (Ash) -> Apex: Synthetic Chemicals (Last resort)."
                        }
                    }
                ],
                # Page 3: Crop Rotation Science & Family Disruption
                [
                    {
                        "type": "concept_explanation",
                        "title": "The Botanical Science of Crop Rotation",
                        "content": {
                            "title": "Starving Family-Specific Pests",
                            "text": "- **The Danger of Monoculture**: When you plant kales in the same bed season after season, kale pests (diamondback moths and aphids) multiply exponentially because their favorite food never disappears.\n- **The 4-Year Rotation Cycle**: Rotate through 4 botanical families: *1. Leaf Crops* (Kales/Spinach) -> *2. Legumes* (Beans/Peas) -> *3. Root Crops* (Carrots/Onions) -> *4. Fruit Crops* (Tomatoes/Peppers).\n- **Result**: Pests emerging from the soil in season 2 find only non-host crops and starve to death!"
                        }
                    }
                ],
                # Page 4: Interactive Control Selection Challenge
                [
                    {
                        "type": "interactive_scenario",
                        "title": "Pest Control Method Selection Challenge",
                        "content": {
                            "title": "Choosing the Best Control Action",
                            "instructions": "Determine the most appropriate pest control method:",
                            "scenario": "A school garden has 20 cabbage plants. A student notices 6 large green caterpillars chewing leaves on 3 plants.",
                            "question": "What is the best, safest, and most economical control action?",
                            "options": [
                                "Mechanical Control: Handpick the 6 caterpillars using gloved hands and drop them into soapy water.",
                                "Chemical Control: Buy an expensive synthetic pesticide spray and coat the entire school compound.",
                                "Do nothing and let the caterpillars eat all 20 cabbages.",
                                "Burn the whole garden down."
                            ],
                            "correct_feedback": "Correct! For small numbers of large pests, mechanical handpicking is 100% free, immediate, and leaves zero toxic chemicals on the food.",
                            "incorrect_feedback": "Incorrect. Buying chemical sprays for 6 caterpillars is expensive, dangerous, and unnecessary. Handpicking is ideal."
                        }
                    }
                ],
                # Page 5: Formative Knowledge Check
                [
                    {
                        "type": "knowledge_check",
                        "title": "Knowledge Check: Crop Rotation Rationale",
                        "content": {
                            "question": "Why does rotating crops between different botanical families each season effectively reduce pest and disease outbreaks?",
                            "options": [
                                "It breaks pest and disease lifecycles by starving out family-specific pests when non-host crops are planted.",
                                "It makes crops invisible to insects.",
                                "It turns soil into liquid fertilizer automatically.",
                                "It cools the air temperature over the farm."
                            ],
                            "answer": "A",
                            "explanation": "Most pests feed on specific botanical families. Rotating to a non-host crop deprives newly hatched pests of their required food source, causing them to starve and breaking the infestation cycle."
                        }
                    }
                ],
                # Page 6: Summary & Connection Forward
                [
                    {
                        "type": "key_takeaway",
                        "title": "Lesson Summary",
                        "content": {
                            "text": "- Manage pests using **Cultural, Mechanical, Biological, Biotech, and Chemical** pathways.\n- **Cultural controls** (crop rotation, clean weeding) prevent pest build-up for zero cost.\n- **Mechanical handpicking and traps** remove pests immediately without chemical toxins.\n- **Biological predators** (ladybugs) maintain natural ecological balance.\n- **Synthetic chemicals** should only be considered as an emergency last resort."
                        }
                    },
                    {
                        "type": "transition",
                        "title": "Looking Ahead",
                        "content": {
                            "text": "How do we manage contagious plant diseases like blights and wilts? In Lesson 4, we master garden sanitation, tool sterilization, and safe plant culling protocols!"
                        }
                    }
                ],
                # Page 7: Trap Cropping Callout
                [
                    {
                        "type": "concept_explanation",
                        "title": "Trap Cropping: The Decoy Strategy",
                        "content": {
                            "title": "Luring Pests Away from Cash Crops",
                            "text": "In cultural control, a **trap crop** is a plant grown around garden borders specifically to attract pests away from valuable vegetables. For example, planting Indian mustard around cabbage beds lures diamondback moths to the mustard, leaving the central cabbage heads pristine and undamaged!"
                        }
                    }
                ]
            ]
        },

        # =====================================================================
        # LESSON 4: General Disease Control Methods
        # =====================================================================
        {
            "unit_order": 4,
            "unit_name": "General Disease Control Methods",
            "unit_description": "Disease management protocols: tool sterilization (disinfectants/soapy water), clean pruning techniques, culling heavily diseased plants, and safe disposal (fire vs 2-foot deep pit burial; zero composting).",
            "lesson_title": "General Disease Control Methods",
            "pages": [
                # Page 1: Visual Hook & Learning Objectives
                [
                    {
                        "type": "suggested_image",
                        "title": "Hygienic Horticulture: Pruning & Sanitation Tools",
                        "content": {
                            "title": "Hygienic Horticulture: Pruning & Sanitation Tools",
                            "caption": "Clean, sterilized pruning shears and garden knives prepared for safe removal of infected vegetable foliage on a school farm."
                        }
                    },
                    {
                        "type": "learning_goal",
                        "title": "Learning Objectives: Disease Sanitation & Culling",
                        "content": {
                            "title": "What We Will Accomplish Today",
                            "goals": [
                                "Explain why **tool sterilization** is critical to prevent spreading microscopic spores.",
                                "Execute clean **pruning of leaf-spotted foliage** without tearing bark.",
                                "Demonstrate the **4-step culling procedure** for incurable bacterial wilt plants.",
                                "Explain why diseased crop residues must **never be added to compost piles**."
                            ]
                        }
                    },
                    {
                        "type": "concept_explanation",
                        "title": "Preventing Plant Epidemics",
                        "content": {
                            "title": "The Importance of Farm Hygiene",
                            "text": "Just as a surgeon sterilizes scalpels between operations, a plant doctor must sterilize pruning tools between garden beds! Microscopic fungal spores and bacteria cling to metal blades; cutting a healthy plant with a contaminated knife injects millions of pathogens directly into its vascular tissues."
                        }
                    }
                ],
                # Page 2: Tool Hygiene & Sterilization SOP
                [
                    {
                        "type": "step_process",
                        "title": "Standard Operating Procedure: Tool Sterilization",
                        "content": {
                            "title": "How to Disinfect Farm Tools",
                            "steps": [
                                "**Step 1: Scrape Off Soil**: Remove all caked mud and organic matter from pruning blades with a wire brush.",
                                "**Step 2: Disinfect Blade**: Wipe blades with 70% rubbing alcohol, diluted household bleach (1:9 water), or scrub with antibacterial soapy water.",
                                "**Step 3: Air Dry**: Allow blades to dry for 30 seconds before making cuts on healthy plants.",
                                "**Step 4: Wash Hands**: Wash hands with soap and water after handling infected crops."
                            ]
                        }
                    },
                    {
                        "type": "suggested_diagram",
                        "title": "Tool Sterilization & Safe Crop Culling 4-Step Flowchart",
                        "content": {
                            "title": "Tool Sterilization & Safe Crop Culling 4-Step Flowchart",
                            "caption": "Safe disease disposal flowchart: 1. Loosen soil with trowel -> 2. Lift entire plant & root ball -> 3. Bag immediately to trap spores -> 4. Deep burial (2ft pit) or safe incinerator (NEVER compost!)."
                        }
                    }
                ],
                # Page 3: Pruning Diseased Leaves vs Culling Whole Plants
                [
                    {
                        "type": "concept_explanation",
                        "title": "Pruning vs. Total Plant Culling",
                        "content": {
                            "title": "Knowing When to Prune and When to Uproot",
                            "text": "- **When to Prune**: When only 1 or 2 lower leaves show early leaf spots or powdery mildew. Snip the leaf stalk cleanly near the main stem with sterilized shears. Place cut leaves directly into a bucket—never drop them on the soil!\n- **When to Cull (Uproot Entire Plant)**: When a plant has incurable bacterial wilt or systemic viral mosaic. Leaving a wilted plant in the bed allows bacteria to seep into the soil and infect neighboring crops."
                        }
                    },
                    {
                        "type": "comparison_table",
                        "title": "Disease Treatment: Pruning vs. Culling Decision Matrix",
                        "content": {
                            "title": "Plant Doctor Action Decision Matrix",
                            "headers": ["Disease Condition", "Severity Level", "Correct Action", "Disposal Method"],
                            "rows": [
                                ["Early Leaf Spot (1-2 lower leaves)", "Mild (Localized)", "Prune affected leaves cleanly at stem base", "Collect in bucket; burn or bury deep"],
                                ["Powdery Mildew (surface dust)", "Mild to Moderate", "Prune worst leaves; dust healthy leaves with ash", "Collect in bucket; bury deep"],
                                ["Bacterial Wilt (entire plant collapsed)", "Severe (Systemic/Incurable)", "Cull (uproot entire plant, roots & root soil)", "Bag immediately; incinerate or bury 2ft deep"],
                                ["Tomato Late Blight (black rotting fruits)", "Severe (Highly Contagious)", "Uproot whole plant and bag immediately", "Burn completely in incinerator (Never compost!)"]
                            ]
                        }
                    }
                ],
                # Page 4: Video Resource — Organic Pest & Disease Management
                [
                    {
                        "type": "suggested_video",
                        "title": "Instructional Video: Organic Crop Disease & Pest Control",
                        "content": {
                            "title": "Instructional Video: Organic Crop Disease & Pest Control",
                            "url": "https://www.youtube.com/watch?v=Ei5z_0Lxmic",
                            "resolved_video_id": "Ei5z_0Lxmic",
                            "caption": "Watch this field demonstration on identifying vegetable diseases, practicing garden sanitation, tool sterilization, and botanical pest management in Kenya."
                        }
                    },
                    {
                        "type": "concept_explanation",
                        "title": "Key Field Takeaways from the Video",
                        "content": {
                            "title": "Plant Doctor Practical Lessons",
                            "text": "- **1. Clean Cuts**: Watch how sharp shears make clean, angled cuts that shed water quickly.\n- **2. The Compost Ban**: Notice how diseased leaves are strictly kept away from compost heaps.\n- **3. Airflow Pruning**: Observe how removing crowded lower leaves improves sunlight penetration and keeps foliage dry."
                        }
                    }
                ],
                # Page 5: Interactive Disease Disposal Diagnosis
                [
                    {
                        "type": "interactive_scenario",
                        "title": "Disease Disposal Diagnosis Challenge",
                        "content": {
                            "title": "Disposing of Blighted Tomato Stalks",
                            "instructions": "Determine the correct disposal method:",
                            "scenario": "You have uprooted 4 tomato plants completely destroyed by black Late Blight rot.",
                            "question": "Where should you dispose of these diseased tomato plants?",
                            "options": [
                                "Burn them completely in a safe incinerator or bury them in a deep 2-foot pit far from garden beds.",
                                "Chop them up and mix them into the school vegetable compost heap.",
                                "Leave them on the garden soil as mulch around healthy kales.",
                                "Feed them to the farm chickens."
                            ],
                            "correct_feedback": "Correct! Contagious fungal spores survive in standard compost heaps and will re-infect future crops. Burning or deep 2-foot burial is required.",
                            "incorrect_feedback": "Incorrect. Never compost diseased plants! Pathogen spores survive in compost and contaminate your future garden beds."
                        }
                    }
                ],
                # Page 6: Formative Knowledge Check
                [
                    {
                        "type": "knowledge_check",
                        "title": "Knowledge Check: Why Diseased Crops Cannot Be Composted",
                        "content": {
                            "question": "Why is it strictly forbidden to throw heavily diseased, blighted vegetable plants into the crop compost heap?",
                            "options": [
                                "Microscopic pathogen spores and bacteria survive in the compost pile, turning the finished compost into an infectious source that re-infects future garden crops.",
                                "Diseased plants cause compost piles to turn into ice.",
                                "Earthworms refuse to live in dark soil.",
                                "Compost piles only accept metal materials."
                            ],
                            "answer": "A",
                            "explanation": "Standard backyard compost piles do not reach high enough sustained temperatures to kill resilient fungal spores and viral pathogens. Spreading that compost will contaminate new crop beds."
                        }
                    }
                ],
                # Page 7: Summary & Connection Forward
                [
                    {
                        "type": "key_takeaway",
                        "title": "Lesson Summary",
                        "content": {
                            "text": "- **Sterilize pruning tools** with disinfectant or soapy water between beds.\n- **Prune lower spotted leaves** cleanly to improve airflow and halt fungal spread.\n- **Cull incurable wilted plants** by uprooting the entire root ball.\n- **NEVER compost diseased plants**: burn them in an incinerator or bury in a 2-foot deep pit."
                        }
                    },
                    {
                        "type": "transition",
                        "title": "Looking Ahead",
                        "content": {
                            "text": "What happens if a farmer ignores pests and diseases? In Lesson 5, we analyze the devastating economic and post-harvest losses caused by delayed crop protection!"
                        }
                    }
                ]
            ]
        },

        # =====================================================================
        # LESSON 5: Economic and Production Impacts
        # =====================================================================
        {
            "unit_order": 5,
            "unit_name": "Economic and Production Impacts",
            "unit_description": "Economic impacts: yield reduction, market unmarketability (scarred/worm-holed leaves), vector disease transmission, post-harvest storage losses (weevil boring), and farmer profit margin formulas.",
            "lesson_title": "Economic and Production Impacts",
            "pages": [
                # Page 1: Visual Hook & Learning Objectives
                [
                    {
                        "type": "suggested_image",
                        "title": "Market Realities: Post-Harvest & Quality Losses",
                        "content": {
                            "title": "Market Realities: Post-Harvest & Quality Losses",
                            "caption": "A comparison showing clean, unblemished market produce on the left versus scarred, insect-bitten vegetables rejected by market customers on the right."
                        }
                    },
                    {
                        "type": "learning_goal",
                        "title": "Learning Objectives: Agricultural Economics",
                        "content": {
                            "title": "What We Will Accomplish Today",
                            "goals": [
                                "Explain how pest damage directly reduces **crop yield weight and physical harvest quantity**.",
                                "Describe how cosmetic leaf and fruit blemishes destroy **market value and customer demand**.",
                                "Explain how boring weevils destroy **seed viability and post-harvest storage life**.",
                                "Calculate farmer profits using the economic formula: $$\\text{Profit} = \\text{Revenue} - \\text{Cost}$$."
                            ]
                        }
                    },
                    {
                        "type": "concept_explanation",
                        "title": "Connecting Field Damage to the Wallet",
                        "content": {
                            "title": "The High Price of Inaction",
                            "text": "Farming is both a science and a business. When caterpillars chew holes in our sukumawiki or weevils drill into our stored bean seeds, the damage is not just biological—it is financial! Unchecked pests destroy family income, waste expensive seeds, and threaten household food security."
                        }
                    }
                ],
                # Page 2: Yield Loss & Market Unmarketability
                [
                    {
                        "type": "concept_explanation",
                        "title": "Field Production & Market Quality Collapse",
                        "content": {
                            "title": "How Pests Slash Farm Revenue",
                            "text": "- **1. Stunted Biomass Yield**: Aphids suck sugary sap while caterpillars strip leaves, drastically reducing photosynthesis. Plants grow stunted and produce only 30% to 50% of their expected harvest weight.\n- **2. Market Rejection**: Customers in fresh markets demand clean, intact, vibrant green vegetables. Kales full of caterpillar holes or tomatoes covered in black spot blemishes are rejected or sold at throwaway prices.\n- **3. Vector Transmission**: Sucking insects act as disease vectors, injecting viral pathogens into stems and collapsing whole fields."
                        }
                    },
                    {
                        "type": "suggested_diagram",
                        "title": "Socio-Economic Chain Reaction of Unchecked Pest Damage",
                        "content": {
                            "title": "Socio-Economic Chain Reaction of Unchecked Pest Damage",
                            "caption": "Financial loss flowchart: Pest infestation in field -> 40% yield drop + scarred leaves -> Produce rejected at market -> Storage weevil decay -> Farmer revenue collapses while control costs double."
                        }
                    }
                ],
                # Page 3: Post-Harvest Destruction & Storage Weevils
                [
                    {
                        "type": "concept_explanation",
                        "title": "Post-Harvest Storage Losses & Seed Viability",
                        "content": {
                            "title": "The Threat Inside the Storehouse",
                            "text": "- **Weevil Infestations**: Maize weevils and bean bruchid beetles drill into harvested grains, laying eggs inside. The larvae eat the seed endosperm from the inside out, reducing grains to hollow shells and dusty powder.\n- **Loss of Seed Viability**: A seed whose embryo has been eaten by weevils will never germinate when planted next season, wasting the farmer's land preparation labor!\n- **Mold & Aflatoxin Contamination**: Insect bite wounds allow toxic storage molds (Aspergillus) to grow, producing deadly **aflatoxins** that make food poisonous for humans and animals."
                        }
                    },
                    {
                        "type": "comparison_table",
                        "title": "Pest Attacks vs. Direct Economic Losses",
                        "content": {
                            "title": "Pest Economic Impact Matrix",
                            "headers": ["Pest Attack Mode", "Crop Type Affected", "Direct Biological Damage", "Economic & Market Consequence"],
                            "rows": [
                                ["Caterpillars chewing leaves", "Kales (Sukumawiki), Cabbages", "Ragged holes, defoliation, stunted growth", "Unmarketable appearance; 50% price drop or total rejection"],
                                ["Aphids sucking sap & virus vector", "Tomatoes, Spinach, Kales", "Leaf curling, viral mosaic stunting", "70% yield loss; field collapse; zero marketable fruit"],
                                ["Bean Weevils boring grains", "Stored beans, cowpeas, maize", "Hollows out seed endosperm & embryo", "Destroys seed germination viability; food turns to dust"],
                                ["Storage Mold on bitten fruits", "Tomatoes, onions, stored grain", "Rotting, foul smell, mycotoxins", "Aflatoxin poisoning risk; 100% loss of stored crop value"]
                            ]
                        }
                    }
                ],
                # Page 4: Interactive Profit Calculation Challenge
                [
                    {
                        "type": "interactive_scenario",
                        "title": "Farm Profit & Loss Calculation Challenge",
                        "content": {
                            "title": "Calculating the Cost of Inaction",
                            "instructions": "Calculate the farmer's profit or loss:",
                            "scenario": "Farmer Mwangi invested KES 3,000 to plant a kale garden, expecting to sell 200 bundles at KES 30 each (Expected Revenue = KES 6,000). However, caterpillars destroyed half the crop and scarred the rest, so Mwangi could only sell 50 bundles at KES 20 each.",
                            "question": "What was Farmer Mwangi's final financial outcome?",
                            "options": [
                                "A Net Loss of KES 2,000 (Revenue = KES 1,000 minus Costs = KES 3,000)",
                                "A Net Profit of KES 10,000",
                                "A Net Profit of KES 3,000",
                                "Zero change"
                            ],
                            "correct_feedback": "Correct! Revenue = 50 bundles × KES 20 = KES 1,000. Profit = KES 1,000 - KES 3,000 = -KES 2,000 (Loss). Delayed pest control resulted in severe financial loss.",
                            "incorrect_feedback": "Incorrect. Calculate Revenue (50 × 20 = KES 1,000) minus Production Cost (KES 3,000) = -KES 2,000 Loss."
                        }
                    }
                ],
                # Page 5: Formative Knowledge Check
                [
                    {
                        "type": "knowledge_check",
                        "title": "Knowledge Check: Storage Weevil Impact on Seed Viability",
                        "content": {
                            "question": "How does bean weevil damage during post-harvest storage destroy seed germination viability for the next planting season?",
                            "options": [
                                "The weevil larvae consume the internal embryo and nutrient endosperm reserves, leaving hollow seeds that cannot germinate.",
                                "The weevils turn seeds into solid rock.",
                                "The weevils make seeds too heavy to plant.",
                                "The weevils paint the seeds purple."
                            ],
                            "answer": "A",
                            "explanation": "Weevil larvae feed on the seed embryo (germ) and cotyledon food reserves. Without an intact embryo or food energy, the seed is biologically dead and cannot germinate."
                        }
                    }
                ],
                # Page 6: Summary & Connection Forward
                [
                    {
                        "type": "key_takeaway",
                        "title": "Lesson Summary",
                        "content": {
                            "text": "- Pests reduce **crop harvest weight and photosynthesis capacity**.\n- Chewed and scarred vegetables **lose market value and customer demand**.\n- Storage weevils hollow out seeds, **destroying seed germination viability**.\n- Storage molds on pest wounds produce **poisonous aflatoxins**.\n- Timely organic control **protects farm profits and household food security**."
                        }
                    },
                    {
                        "type": "transition",
                        "title": "Looking Ahead",
                        "content": {
                            "text": "How can we protect our crops from pests for zero cost without buying toxic chemicals? In Lesson 6, we explore the science and safety of natural wood ash!"
                        }
                    }
                ],
                # Page 7: Aflatoxin Warning Callout
                [
                    {
                        "type": "concept_explanation",
                        "title": "Aflatoxin Danger in Stored Crops",
                        "content": {
                            "title": "The Silent Poison",
                            "text": "When weevils bore into stored maize and groundnuts in damp storage, Aspergillus fungi invade the bite tunnels. These molds produce **aflatoxins**—extremely potent chemical toxins that cause liver cancer, acute poisoning, and stunted growth in children. Keeping crops pest-free and dry protects human lives!"
                        }
                    }
                ]
            ]
        },

        # =====================================================================
        # LESSON 6: Natural Pesticides: The Science and Safety of Ash
        # =====================================================================
        {
            "unit_order": 6,
            "unit_name": "Natural Pesticides: The Science and Safety of Ash",
            "unit_description": "Natural pesticide definitions, mineral composition of wood ash (calcium, potassium, silica), physical dehydration mechanism of insect cuticle, and PPE safety protocols (dust mask, goggles, gloves, upwind position).",
            "lesson_title": "Natural Pesticides: The Science and Safety of Ash",
            "pages": [
                # Page 1: Visual Hook & Learning Objectives
                [
                    {
                        "type": "suggested_image",
                        "title": "Natural Crop Care: Sieved Fireplace Wood Ash",
                        "content": {
                            "title": "Natural Crop Care: Sieved Fireplace Wood Ash",
                            "caption": "Fine, powdery sieved wood ash stored in a clean container, ready for safe organic dusting on garden vegetables."
                        }
                    },
                    {
                        "type": "learning_goal",
                        "title": "Learning Objectives: The Science of Ash",
                        "content": {
                            "title": "What We Will Accomplish Today",
                            "goals": [
                                "Define **natural pesticide** and list its ecological advantages over synthetic poisons.",
                                "Explain the scientific **cuticle-scratching and physical dehydration mechanism** of wood ash.",
                                "Demonstrate the required **PPE safety gear (dust mask, goggles, gloves)**.",
                                "Explain the **upwind positioning rule** to protect eyes and lungs during dusting."
                            ]
                        }
                    },
                    {
                        "type": "concept_explanation",
                        "title": "The Power of Ancient Farm Science",
                        "content": {
                            "title": "Pest Control from the Fireplace",
                            "text": "For generations, Kenyan farmers have used wood ash from kitchen cooking fires to protect their crops. Wood ash is not a chemical poison; it is an organic, non-toxic mineral powder that kills soft-bodied insect pests through physical dehydration—leaving zero toxic residues on our food!"
                        }
                    }
                ],
                # Page 2: The Physical Science of Wood Ash Dehydration
                [
                    {
                        "type": "concept_explanation",
                        "title": "The Cuticle Dehydration Mechanism",
                        "content": {
                            "title": "How Wood Ash Destroys Soft-Bodied Pests",
                            "text": "- **The Insect Waxy Cuticle**: Soft-bodied insects like aphids, thrips, and young caterpillars possess an ultra-thin waxy outer skin layer (cuticle) that prevents their internal body water from evaporating.\n- **1. Microscopic Abrasive Action**: Wood ash contains sharp microscopic silica mineral crystals. When dusted onto insects, the sharp crystals scratch and wear away the waxy cuticle as the insect crawls.\n- **2. Desiccation & Dehydration**: The highly alkaline, dry mineral powder (rich in potassium and calcium carbonates) rapidly absorbs the insect's body moisture through the scratched cuticle, causing the pest to shrivel and die within hours!\n- **3. Repellent Texture**: Biting insects find ash-coated leaves gritty and unpalatable, preventing further feeding."
                        }
                    },
                    {
                        "type": "suggested_diagram",
                        "title": "The Physical Science of Wood Ash Dehydration & Upwind Dusting Setup",
                        "content": {
                            "title": "The Physical Science of Wood Ash Dehydration & Upwind Dusting Setup",
                            "caption": "Biophysical mechanism diagram: 1. Insect waxy cuticle intact -> 2. Sharp silica crystals in ash scratch cuticle -> 3. Alkaline ash absorbs body water -> 4. Rapid pest death by dehydration. Plus upwind operator positioning schematic."
                        }
                    }
                ],
                # Page 3: Personal Protective Equipment (PPE) & Wind Protocol
                [
                    {
                        "type": "concept_explanation",
                        "title": "Safety Protocols When Handling Alkaline Ash Dust",
                        "content": {
                            "title": "Protecting Lungs, Eyes, and Skin",
                            "text": "Although wood ash is completely organic and non-toxic on food, it is an extremely fine, highly alkaline dust that irritates human mucous membranes:\n\n- **1. Respiratory Protection**: Always wear a dust mask or tie a clean damp cloth over your nose and mouth to prevent inhaling fine ash particles, which trigger coughing and lung irritation.\n- **2. Eye Protection**: Wear safety goggles. Getting alkaline ash in eyes causes burning and redness.\n- **3. Skin Protection**: Wear rubber gardening gloves to prevent dry alkaline skin cracking. Wash hands with soap after work.\n- **4. The Upwind Wind Rule**: Never dust on windy afternoons! Always stand **upwind** (with the gentle breeze blowing from behind your back toward the crop) so dust blows away from your face."
                        }
                    },
                    {
                        "type": "comparison_table",
                        "title": "Natural Wood Ash vs. Synthetic Chemical Insecticides",
                        "content": {
                            "title": "Pesticide Safety Comparison Matrix",
                            "headers": ["Characteristic", "Natural Sieved Wood Ash", "Synthetic Chemical Insecticide"],
                            "rows": [
                                ["Active Mechanism", "Physical cuticle abrasion & moisture dehydration", "Chemical neurotoxins poisoning insect nervous system"],
                                ["Cash Purchase Cost", "Zero cost (Recycled from kitchen cooking fire)", "High cost (KES 800 - 2,500 per bottle)"],
                                ["Food Safety & Harvest Interval", "Safe to wash and eat the exact same day", "Must wait 7 to 14 days before harvest (toxic residues)"],
                                ["Impact on Ladybugs & Bees", "Minimal (Harms only soft-bodied crawling pests)", "Lethal (Kills beneficial bees and ladybugs instantly)"],
                                ["Soil & Water Impact", "Adds beneficial potassium & calcium to soil", "Contaminates groundwater; kills soil earthworms"]
                            ]
                        }
                    }
                ],
                # Page 4: Interactive Safety Diagnosis Challenge
                [
                    {
                        "type": "interactive_scenario",
                        "title": "Wood Ash Safety Setup Challenge",
                        "content": {
                            "title": "Evaluating Field Safety Habits",
                            "instructions": "Determine whether the practice is safe or dangerous:",
                            "scenario": "A student stands facing directly into a strong afternoon wind, throwing handfuls of dry un-sieved ash into the air without wearing a mask or goggles.",
                            "question": "How is this dusting practice classified?",
                            "options": [
                                "Extremely Dangerous: Violates wind rules, lacks PPE, and causes severe eye and lung irritation.",
                                "Safe & Recommended Practice"
                            ],
                            "correct_feedback": "Correct! Dusting into the wind without PPE blows alkaline ash into your eyes and lungs. You must always wear a mask, goggles, and stand upwind.",
                            "incorrect_feedback": "Incorrect. Dusting facing the wind without PPE causes severe respiratory and eye injuries. Always wear PPE and stand upwind."
                        }
                    }
                ],
                # Page 5: Formative Knowledge Check
                [
                    {
                        "type": "knowledge_check",
                        "title": "Knowledge Check: Dehydration Science of Ash",
                        "content": {
                            "question": "What is the physical scientific mechanism by which dry sieved wood ash kills soft-bodied insect pests like aphids?",
                            "options": [
                                "Sharp silica crystals scratch the insect's protective waxy cuticle, allowing the dry alkaline powder to absorb internal body fluids and kill the pest by dehydration.",
                                "It freezes the insect into a block of ice.",
                                "It causes the insect to grow wings and fly to another country.",
                                "It poisons the plant's leaves so the whole plant dies."
                            ],
                            "answer": "A",
                            "explanation": "Wood ash works via physical desiccation: silica crystals abrade the waxy outer cuticle of soft-bodied insects, and the alkaline powder draws out body water, causing fatal dehydration."
                        }
                    }
                ],
                # Page 6: Summary & Connection Forward
                [
                    {
                        "type": "key_takeaway",
                        "title": "Lesson Summary",
                        "content": {
                            "text": "- **Natural pesticides** are affordable, biodegradable, non-toxic, and environmentally safe.\n- **Wood ash** kills soft-bodied pests via **cuticle abrasion and physical dehydration**.\n- Always wear **PPE (dust mask, safety goggles, rubber gloves)** when handling ash.\n- Observe the **upwind rule**: stand with your back to the gentle breeze so dust blows away from you."
                        }
                    },
                    {
                        "type": "transition",
                        "title": "Looking Ahead",
                        "content": {
                            "text": "Our safety gear is ready and we understand the science! In Lesson 7, we step outside to the school garden for our hands-on practical wood ash preparation and dry dusting session!"
                        }
                    }
                ],
                # Page 7: Soil pH Neutralizer Callout
                [
                    {
                        "type": "concept_explanation",
                        "title": "Bonus Benefit: Soil Acidity Neutralizer",
                        "content": {
                            "title": "Ash Feeds the Soil While Killing Pests",
                            "text": "When wood ash falls from the leaves onto the soil bed, it acts as an agricultural liming agent! Rich in potassium (K) and calcium carbonate ($$\\text{CaCO}_3$$), it gently raises the pH of acidic soils, enhancing vegetable root nutrient uptake while eliminating pests above ground."
                        }
                    }
                ]
            ]
        },

        # =====================================================================
        # LESSON 7: Practical Activity: Preparing and Applying Wood Ash
        # =====================================================================
        {
            "unit_order": 7,
            "unit_name": "Practical Activity: Preparing and Applying Wood Ash",
            "unit_description": "Hands-on field practical: sieving raw fireplace ash to remove charcoal chunks, checking morning dew adhesion, shaker bottle fabrication, dusting leaf undersides, and project cleanup.",
            "lesson_title": "Practical Activity: Preparing and Applying Wood Ash",
            "pages": [
                # Page 1: Visual Hook & Practical Objectives
                [
                    {
                        "type": "suggested_image",
                        "title": "Active Field Practical: Dusting Morning Kales",
                        "content": {
                            "title": "Active Field Practical: Dusting Morning Kales",
                            "caption": "Students wearing protective masks using perforated shaker bottles to apply fine sieved wood ash to dew-covered kale leaves on the school farm."
                        }
                    },
                    {
                        "type": "learning_goal",
                        "title": "Learning Objectives: Hands-On Ash Application",
                        "content": {
                            "title": "What We Will Accomplish Today",
                            "goals": [
                                "Sieve raw fireplace ash through a **wire mesh screen** to remove charcoal chunks and debris.",
                                "Construct an **upcycled shaker bottle** with perforated cap and internal agitator pebble.",
                                "Apply fine ash to **dew-covered kale leaves and undersides** using the upwind dusting protocol.",
                                "Perform post-practical **cleanup, tool storage, and personal sanitation**."
                            ]
                        }
                    },
                    {
                        "type": "concept_explanation",
                        "title": "Early Morning Dew: Our Natural Water Glue",
                        "content": {
                            "title": "Why Timing is Everything",
                            "text": "Today we step into the cool morning garden! Notice how the kale leaves sparkle with overnight dew. This dew is our secret partner: it acts as a natural water adhesive, capturing our fine wood ash dust and holding it tightly to the leaf surfaces where aphids feed!"
                        }
                    }
                ],
                # Page 2: Step-by-Step Ash Sieving & Shaker Bottle Fabrication
                [
                    {
                        "type": "step_process",
                        "title": "Standard Operating Procedure: Sieving & Shaker Prep",
                        "content": {
                            "title": "Preparing Fine Powder & Shaker Applicators",
                            "steps": [
                                "**Step 1: Put on PPE**: Don dust mask, safety goggles, and rubber gloves before opening the raw ash container.",
                                "**Step 2: Sieve Raw Ash**: Place a fine kitchen sieve or wire mesh screen over a clean bucket. Scoop raw ash and shake gently. Large charcoal chunks and nails remain on top; fine flour-like grey ash collects below.",
                                "**Step 3: Repurpose Charcoal**: Empty large charcoal chunks into your compost heap to act as biochar.",
                                "**Step 4: Build Shaker Bottle**: Take an empty clean plastic water bottle. Punch 8 small nail holes in the screw cap. Drop a small clean pebble inside (to act as an agitator).",
                                "**Step 5: Fill Shaker**: Funnel fine sieved ash into the bottle until 2/3 full. Screw the perforated cap tightly."
                            ]
                        }
                    },
                    {
                        "type": "suggested_diagram",
                        "title": "5-Phase Wood Ash Preparation & Early-Morning Dew Dusting Workflow",
                        "content": {
                            "title": "5-Phase Wood Ash Preparation & Early-Morning Dew Dusting Workflow",
                            "caption": "Sequential practical workflow: 1. Put on PPE -> 2. Sieve raw ash through mesh screen -> 3. Check early-morning dew on leaves -> 4. Stand upwind & dust leaf undersides with shaker bottle -> 5. Sanitize tools & log in farm journal."
                        }
                    }
                ],
                # Page 3: Dry Dusting Application Technique
                [
                    {
                        "type": "step_process",
                        "title": "Standard Operating Procedure: Garden Dusting Technique",
                        "content": {
                            "title": "How to Dust Crops for Maximum Pest Impact",
                            "steps": [
                                "**1. Check Dew**: Ensure leaves are damp with early-morning dew (between 6:30 AM and 8:00 AM).",
                                "**2. Check Wind**: Observe grass movement. Stand upwind of the bed so the breeze blows toward the plants.",
                                "**3. Target Undersides**: Hold the shaker bottle angled upward beneath the leaves. Shake gently to create a fine grey cloud that coats the leaf undersides where aphids cluster.",
                                "**4. Light Uniform Dusting**: Coat leaves in a thin, translucent grey veil. Do not dump heavy piles of ash, as thick heaps block sunlight."
                            ]
                        }
                    }
                ],
                # Page 4: Practical Video — Grade 8 Agriculture Project
                [
                    {
                        "type": "suggested_video",
                        "title": "Practical Video: Grade 8 Agriculture Project & Organic Pest Control",
                        "content": {
                            "title": "Practical Video: Grade 8 Agriculture Project & Organic Pest Control",
                            "url": "https://www.youtube.com/watch?v=6ZjkLwQt_YE",
                            "resolved_video_id": "6ZjkLwQt_YE",
                            "caption": "Watch this step-by-step practical video demonstration on preparing organic pest solutions, wood ash dusting, and managing school farm vegetable plots in Kenya."
                        }
                    },
                    {
                        "type": "concept_explanation",
                        "title": "Practical Field Reminders from the Video",
                        "content": {
                            "title": "Field Workshop Reminders",
                            "text": "- **1. Agitator Pebble**: Watch how shaking the bottle with an internal pebble prevents fine ash from clumping in damp morning air.\n- **2. Translucent Veil**: Notice how the ash coating is light and dusty, not a heavy mud layer.\n- **3. Journal Entry**: Observe how students document treated bed numbers and pest counts."
                        }
                    }
                ],
                # Page 5: Interactive Practical Sequencing Challenge
                [
                    {
                        "type": "interactive_scenario",
                        "title": "Practical Application Sequencing Challenge",
                        "content": {
                            "title": "Ordering Practical Ash Steps",
                            "instructions": "Place the practical steps in the correct chronological order:",
                            "scenario": "Your agriculture team is ready to apply wood ash to the school kale beds.",
                            "question": "What is the correct sequence of practical actions?",
                            "options": [
                                "1. Put on PPE -> 2. Sieve raw ash -> 3. Verify morning dew & wind -> 4. Dust leaf undersides -> 5. Clean up & log journal",
                                "1. Dust bare hands in heavy wind -> 2. Wash face with ash -> 3. Sieve ash after harvesting",
                                "1. Throw ash at classmates -> 2. Eat the ash -> 3. Put on mask at night",
                                "1. Dump raw un-sieved charcoal chunks on tiny seedlings"
                            ],
                            "correct_feedback": "Correct! Always gear up in PPE first, sieve the ash, verify dew and wind conditions, dust leaf undersides gently, and sanitize tools and hands last.",
                            "incorrect_feedback": "Incorrect. Follow the chronological safety order: PPE -> Sieve -> Check Dew/Wind -> Dust -> Cleanup & Journal."
                        }
                    }
                ],
                # Page 6: Formative Knowledge Check
                [
                    {
                        "type": "knowledge_check",
                        "title": "Knowledge Check: Morning Dew Role in Ash Adhesion",
                        "content": {
                            "question": "Why is the early morning the single most effective time of day to apply dry sieved wood ash to vegetable crop leaves?",
                            "options": [
                                "Overnight leaf dew provides natural moisture droplets that capture and stick dry ash powder firmly to leaf surfaces and insect bodies.",
                                "Insects are frozen solid and cannot move.",
                                "The sun is too dark for insects to see.",
                                "Wood ash dissolves into steam in the afternoon."
                            ],
                            "answer": "A",
                            "explanation": "Overnight dew creates microscopic water droplets on foliage, acting as natural adhesive glue that binds fine ash particles to leaf undersides where pests feed."
                        }
                    }
                ],
                # Page 7: Summary & Connection Forward
                [
                    {
                        "type": "key_takeaway",
                        "title": "Lesson Summary",
                        "content": {
                            "text": "- **Sieve raw ash** through wire mesh to remove sharp charcoal chunks.\n- Build an **upcycled shaker bottle** with a perforated cap and internal agitator pebble.\n- Apply in **early-morning dew** to ensure maximum powder adhesion.\n- Stand **upwind** and target the **leaf undersides where aphid colonies hide**.\n- Sanitize tools, wash hands with soap, and record data in your **garden journal**."
                        }
                    },
                    {
                        "type": "transition",
                        "title": "Looking Ahead",
                        "content": {
                            "text": "Congratulations on mastering organic crop protection! In our final lesson, we conduct our Topic Master Review and tackle the 10 Topic Summative Assessment Questions!"
                        }
                    }
                ]
            ]
        },

        # =====================================================================
        # LESSON 8: Topic Assessment and Review on Crop Pest and Disease Control
        # =====================================================================
        {
            "unit_order": 8,
            "unit_name": "Topic Assessment and Review on Crop Pest and Disease Control",
            "unit_description": "Cumulative topic synthesis: pest mouthparts review, disease symptom diagnostics, IPM control hierarchy, wood ash science, topic video review, and 10 topic summative MCQs.",
            "lesson_title": "Topic Assessment and Review on Crop Pest and Disease Control & Capstone",
            "pages": [
                # Page 1: Visual Hook & Capstone Objectives
                [
                    {
                        "type": "suggested_image",
                        "title": "The Thriving Harvest: A Pest-Free Organic Garden",
                        "content": {
                            "title": "The Thriving Harvest: A Pest-Free Organic Garden",
                            "caption": "A lush, vibrant, chemical-free school vegetable garden filled with crisp, healthy kales, cabbages, and tomatoes protected by organic practices."
                        }
                    },
                    {
                        "type": "learning_goal",
                        "title": "Learning Objectives: Cumulative Topic Mastery",
                        "content": {
                            "title": "What We Will Accomplish Today",
                            "goals": [
                                "Synthesize the scientific differences between **crop pests and crop diseases**.",
                                "Map out the complete **Integrated Pest Management (IPM) decision hierarchy**.",
                                "Analyze real-world farm diagnostic scenarios as certified **Junior Plant Doctors**.",
                                "Review the Topic Video and demonstrate total mastery on the **10 Topic Summative Assessment Questions**."
                            ]
                        }
                    },
                    {
                        "type": "concept_explanation",
                        "title": "The Certified Junior Plant Doctor",
                        "content": {
                            "title": "Mastering Organic Crop Stewardship",
                            "text": "Over the past 7 lessons, we have transformed into skilled plant doctors. We can identify whether damage is caused by a chewing caterpillar or a sucking aphid, diagnose bacterial wilt versus leaf spots, practice tool sterilization, and apply natural wood ash safely in morning dew. Now, let's prove our mastery!"
                        }
                    }
                ],
                # Page 2: Master Diagnostic Matrix
                [
                    {
                        "type": "comparison_table",
                        "title": "Master Crop Doctor Diagnostic & Solution Matrix",
                        "content": {
                            "title": "Comprehensive Diagnostic Guide",
                            "headers": ["Observed Field Symptom", "Primary Cause / Pathogen", "Entomological / Pathological Mechanism", "Recommended Organic Farm Solution"],
                            "rows": [
                                ["Ragged leaf holes; green frass", "Biting & chewing caterpillars", "Mandibles tear solid green leaf tissue", "Mechanical handpicking with gloves into soapy water"],
                                ["Curled yellow leaves; black mold", "Piercing & sucking aphids", "Stylet withdraws cell sap; secretes honeydew", "Early-morning dry dusting of sieved wood ash upwind"],
                                ["Seedlings chopped at ground line", "Soil cutworms", "Caterpillar chews seedling stem at soil line", "Clear crop debris; place physical collar around stems"],
                                ["Round brown spots with yellow ring", "Fungal leaf spot (Early Blight)", "Fungal spores germinate in wet foliage", "Prune lower infected leaves cleanly; sterilize tools"],
                                ["Plant collapses suddenly in wet soil", "Bacterial Wilt", "Bacteria multiply inside xylem vessels", "Cull entire plant & root ball; burn or bury 2ft deep"],
                                ["Hollowed stored seeds & grain dust", "Boring maize/bean weevils", "Larvae consume internal seed endosperm", "Hermetic bag storage; mix grain with fine wood ash"]
                            ]
                        }
                    },
                    {
                        "type": "suggested_diagram",
                        "title": "Master Crop Doctor Diagnostic Matrix & Organic Farm Solutions",
                        "content": {
                            "title": "Master Crop Doctor Diagnostic Matrix & Organic Farm Solutions",
                            "caption": "Diagnostic flowchart linking visible field symptoms (chewed holes, curled leaves, wilting, spotted leaves) to precise biological causes and approved organic control responses."
                        }
                    }
                ],
                # Page 3: The Sustainable Farmer's Stewardship Creed
                [
                    {
                        "type": "concept_explanation",
                        "title": "The Sustainable Land Steward's Creed",
                        "content": {
                            "title": "Principles of Ecological Farming",
                            "text": "- **1. Prevention First**: Rotate crops between botanical families and maintain clean border cultivation.\n- **2. Protect Biodiversity**: Preserve beneficial ladybugs, spiders, and praying mantises that regulate pests naturally for free.\n- **3. Chemical-Free Nutrition**: Prioritize physical handpicking, organic compost, and natural mineral wood ash to protect family health and clean groundwater.\n- **4. Strict Biosecurity**: Sterilize tools and incinerate or deep-bury incurable diseased plants to protect future generations of crops."
                        }
                    }
                ],
                # Page 4: Interactive Master Diagnostic Challenge
                [
                    {
                        "type": "interactive_scenario",
                        "title": "Master Plant Doctor Diagnostic Challenge",
                        "content": {
                            "title": "Diagnosing a Complex Farm Outbreak",
                            "instructions": "Diagnose the crop problem and prescribe the correct organic response:",
                            "scenario": "A farmer finds that 15 of her kale plants have curled, yellowish leaves covered underneath by thousands of tiny yellow insects, while 2 tomato plants nearby have suddenly collapsed into limp wilt despite heavy rain.",
                            "question": "What is the correct dual diagnosis and management plan?",
                            "options": [
                                "Aphid infestation on kales (treat with sieved wood ash dusting) AND Bacterial Wilt on tomatoes (uproot entire plants and bury 2ft deep).",
                                "Spray gasoline on the entire garden and abandon the farm.",
                                "Water the wilted tomatoes with hot boiling water.",
                                "Feed the kales to caterpillars."
                            ],
                            "correct_feedback": "Correct! Yellow insects under curled leaves are sap-sucking aphids (treat with wood ash). Sudden collapse in wet soil is Bacterial Wilt (uproot and bury deep).",
                            "incorrect_feedback": "Incorrect. Diagnose carefully: Curled leaves with tiny bugs = aphids (wood ash). Sudden collapse in wet soil = bacterial wilt (uproot and bury deep)."
                        }
                    }
                ],
                # Page 5: Formative Knowledge Check & Topic Master Summary
                [
                    {
                        "type": "knowledge_check",
                        "title": "Knowledge Check: Integrated Pest Management Hierarchy",
                        "content": {
                            "question": "In Integrated Pest Management (IPM), what is the correct order of control strategies from first line of defense to final emergency resort?",
                            "options": [
                                "1. Cultural Prevention -> 2. Mechanical Removal -> 3. Biological Predators -> 4. Natural Botanicals/Ash -> 5. Synthetic Chemicals (Last Resort).",
                                "1. Spray maximum chemicals -> 2. Burn soil -> 3. Handpick bugs -> 4. Plant seeds.",
                                "1. Wait for weeds to take over -> 2. Buy new land -> 3. Water crops once a year.",
                                "1. Paint leaves green -> 2. Use synthetic chemicals exclusively."
                            ],
                            "answer": "A",
                            "explanation": "IPM prioritizes prevention first (cultural rotation), followed by manual removal (mechanical), natural enemies (biological), non-toxic botanicals (ash), and reserves synthetic chemicals strictly for emergency outbreaks."
                        }
                    },
                    {
                        "type": "key_takeaway",
                        "title": "Topic 5 Master Summary: Crop Pest and Disease Control",
                        "content": {
                            "text": "- **Pests** feed via biting, piercing, or boring; **diseases** cause spots, mildews, blights, and wilts.\n- **Beneficial insects** like ladybugs provide chemical-free biological pest regulation.\n- **Crop rotation** starves family-specific pests and breaks pathogen cycles.\n- **Sterilize tools** and **NEVER compost diseased plants** (burn or bury 2ft deep).\n- **Wood ash** dehydrates soft-bodied pests safely when applied to **early-morning dew upwind**."
                        }
                    }
                ],
                # Page 6: Topic Video Review
                [
                    {
                        "type": "suggested_video",
                        "title": "Topic Video Review: Organic Pest Management & Botanical Sprays",
                        "content": {
                            "title": "Topic Video Review: Organic Pest Management & Botanical Sprays",
                            "url": "https://www.youtube.com/watch?v=4oWEI6Wl-xI",
                            "resolved_video_id": "4oWEI6Wl-xI",
                            "caption": "Watch this comprehensive organic farming tutorial covering botanical pesticide preparation, companion planting, natural pest repellents, and safe crop care."
                        }
                    },
                    {
                        "type": "concept_explanation",
                        "title": "Key Focus Questions for Video Review",
                        "content": {
                            "title": "Final Review Concepts",
                            "text": "- **1. Companion Planting**: Notice how marigolds and onions planted alongside vegetables repel flying insect pests.\n- **2. Natural Repellents**: Observe how non-toxic botanical extracts disrupt insect feeding without chemical toxicity.\n- **3. Economic Sustainability**: See how organic inputs save smallholder families money while producing premium chemical-free food."
                        }
                    }
                ],
                # Page 7: Topic Assessment Part 1 (Questions 1 to 2)
                [
                    {
                        "type": "knowledge_check",
                        "title": "Topic Assessment - Question 1: Crop Pest Definition",
                        "content": {
                            "question": "What is the scientific definition of a crop pest?",
                            "options": [
                                "Any living organism (insect, bird, rodent, nematode) capable of causing physical damage, yield loss, or death to crop plants.",
                                "A nutrient added to soil beds to make plants grow faster.",
                                "A tool used to measure straight furrow lines in gardens.",
                                "A type of compost prepared from dried grass."
                            ],
                            "answer": "A",
                            "explanation": "A crop pest is any biological organism that attacks, damages, or destroys cultivated agricultural plants."
                        }
                    },
                    {
                        "type": "knowledge_check",
                        "title": "Topic Assessment - Question 2: Piercing & Sucking Mouthparts",
                        "content": {
                            "question": "Which insect pest group possesses needle-like stylet mouthparts to puncture leaves and suck out sweet cell sap, causing leaf curling?",
                            "options": [
                                "Piercing and sucking insects (such as aphids, whiteflies, and thrips).",
                                "Biting and chewing insects.",
                                "Boring and burrowing insects.",
                                "Beneficial predatory insects."
                            ],
                            "answer": "A",
                            "explanation": "Piercing and sucking insects like aphids have sharp, needle-like mouthparts to extract sap, causing curling, stunting, and viral infection."
                        }
                    }
                ],
                # Page 8: Topic Assessment Part 2 (Questions 3 to 5)
                [
                    {
                        "type": "knowledge_check",
                        "title": "Topic Assessment - Question 3: Healthy Leaf Visual Benchmarks",
                        "content": {
                            "question": "What is the visual appearance of a healthy, disease-free vegetable leaf?",
                            "options": [
                                "Even, vibrant green, smooth, clean, and held upright toward the sun.",
                                "Pale yellow covered with black spot rings.",
                                "Coated in a white powdery dust layer.",
                                "Wrinkled and drooping limply toward the ground."
                            ],
                            "answer": "A",
                            "explanation": "Healthy vegetable leaves are clean, vibrant green, and held upright to capture maximum sunlight for photosynthesis."
                        }
                    },
                    {
                        "type": "knowledge_check",
                        "title": "Topic Assessment - Question 4: Role of Ladybugs",
                        "content": {
                            "question": "Why are ladybugs (ladybird beetles) highly valued and protected by sustainable organic farmers?",
                            "options": [
                                "They are beneficial predatory insects that naturally hunt and consume thousands of destructive aphids without chemical sprays.",
                                "They eat vegetable leaves to make them grow faster.",
                                "They produce sweet honey inside kale stems.",
                                "They dig planting holes in the soil."
                            ],
                            "answer": "A",
                            "explanation": "Ladybugs are beneficial predators that voraciously consume soft-bodied crop pests like aphids, providing natural biological pest regulation."
                        }
                    },
                    {
                        "type": "knowledge_check",
                        "title": "Topic Assessment - Question 5: Bacterial Wilt Symptoms",
                        "content": {
                            "question": "What distinct visible symptom indicates that a vegetable crop is suffering from Bacterial Wilt rather than simple drought stress?",
                            "options": [
                                "The plant collapses and wilts suddenly while the surrounding soil is damp and wet.",
                                "The leaves develop white powdery dust on top.",
                                "Large holes are chewed through the middle of the stem.",
                                "The leaves turn bright blue."
                            ],
                            "answer": "A",
                            "explanation": "Bacterial wilt causes plants to collapse suddenly despite wet soil because bacterial slime plugs the water-transport xylem channels inside the stem."
                        }
                    }
                ],
                # Page 9: Topic Assessment Part 3 (Questions 6 to 8)
                [
                    {
                        "type": "knowledge_check",
                        "title": "Topic Assessment - Question 6: Tool Sterilization Rationale",
                        "content": {
                            "question": "Why must a farmer disinfect and wipe pruning knives with soapy water or alcohol before moving to prune a healthy crop bed?",
                            "options": [
                                "To kill microscopic fungal spores and bacteria clinging to the blade, preventing the transmission of disease to healthy plants.",
                                "To make the blade smell like perfume.",
                                "To prevent the metal blade from getting heavy.",
                                "To attract beneficial birds to the farm."
                            ],
                            "answer": "A",
                            "explanation": "Pathogen spores adhere to metal cutting blades. Disinfecting tools stops the mechanical transmission of plant diseases between crops."
                        }
                    },
                    {
                        "type": "knowledge_check",
                        "title": "Topic Assessment - Question 7: Wood Ash Dehydration Mechanism",
                        "content": {
                            "question": "How does dry sieved wood ash control soft-bodied garden pests like aphids and small caterpillars?",
                            "options": [
                                "Its microscopic silica crystals abrade and scratch the insect's waxy cuticle, allowing the dry alkaline powder to absorb body fluids and kill the pest by dehydration.",
                                "It releases poisonous chemical fumes that suffocate insects.",
                                "It makes the leaves slippery so insects fall off.",
                                "It attracts giant spiders from the forest."
                            ],
                            "answer": "A",
                            "explanation": "Wood ash works via physical desiccation: abrasive silica abrades the waxy outer skin (cuticle) of soft-bodied insects, causing fatal dehydration."
                        }
                    },
                    {
                        "type": "knowledge_check",
                        "title": "Topic Assessment - Question 8: Diseased Plant Disposal Protocol",
                        "content": {
                            "question": "What is the correct protocol for disposing of heavily diseased, blighted vegetable plants uprooted from a garden?",
                            "options": [
                                "Bag them immediately and burn them in a safe incinerator or bury them in a deep 2-foot pit far from crops (NEVER add to compost!).",
                                "Mix them into the school vegetable compost heap to make manure.",
                                "Leave them lying on top of the garden soil as mulch.",
                                "Wash them in a river and feed them to fish."
                            ],
                            "answer": "A",
                            "explanation": "Infectious spores survive in standard compost heaps. Uprooting, bagging, and deep 2-foot pit burial or burning safely eliminates the pathogens."
                        }
                    }
                ],
                # Page 10: Topic Assessment Part 4 (Questions 9 to 10)
                [
                    {
                        "type": "knowledge_check",
                        "title": "Topic Assessment - Question 9: Upwind Wind Rule for Ash Dusting",
                        "content": {
                            "question": "When applying dry sieved wood ash to garden vegetables, what wind safety protocol must be followed?",
                            "options": [
                                "Stand with your back to the gentle breeze (upwind) wearing a dust mask and goggles so the fine alkaline dust blows away from your face.",
                                "Dust on a very windy afternoon facing into the wind.",
                                "Run around the garden throwing handfuls of ash in all directions.",
                                "Work inside an airtight sealed greenhouse with no ventilation."
                            ],
                            "answer": "A",
                            "explanation": "Alkaline ash dust irritates respiratory tissues and eyes. Standing upwind with PPE ensures the breeze carries the fine dust safely toward the crop and away from your face."
                        }
                    },
                    {
                        "type": "knowledge_check",
                        "title": "Topic Assessment - Question 10: Economic Impact of Delayed Pest Control",
                        "content": {
                            "question": "How does delayed or neglected pest management result in severe financial loss for smallholder vegetable farmers?",
                            "options": [
                                "It stunts crop yields, creates scarred unmarketable vegetables that customers reject, and allows storage weevils to destroy seed viability.",
                                "It makes seeds cheaper to buy in agro-vets.",
                                "It makes market customers pay double prices for worm-holed leaves.",
                                "It prevents weeds from competing with crops."
                            ],
                            "answer": "A",
                            "explanation": "Neglected pest control slashes crop weight, ruins vegetable market appearance (leading to price cuts or rejection), and destroys stored seed viability, devastating farmer profits."
                        }
                    }
                ]
            ]
        }
    ]

def ingest_cbc_grade8_agriculture_topic5(replace: bool = True):
    """Executes the database transaction to ingest Topic 5 into CBC Grade 8 Agriculture."""
    print("=" * 80)
    print("STARTING CONTENT INGESTION: CBC GRADE 8 AGRICULTURE — TOPIC 5 (DEEP EDITION)")
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

        topic_name = "Crop Pest and Disease Control"
        if replace:
            existing_topics = Topic.objects.filter(subject=subject, name=topic_name)
            if existing_topics.exists():
                print(f"[*] Found existing topic '{topic_name}' (ID: {existing_topics.first().id}). Deleting for clean replace...")
                existing_topics.delete()

        topic, created = Topic.objects.get_or_create(
            subject=subject,
            name=topic_name,
            defaults={
                "order": 5,
                "description": "Comprehensive crop pest and disease management: insect classification by mouthparts (biting, piercing, boring), disease diagnostics (spots, mildew, blight, wilt), 5 control pathways, tool sterilization and safe culling, economic loss analysis, the physical science of wood ash dehydration, practical early-morning dew dusting, and cumulative Junior Plant Doctor capstone."
            }
        )
        print(f"[*] Topic: '{topic.name}' (ID: {topic.id}, Created: {created})")

        curriculum_data = build_topic5_curriculum()
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
                        block_id=f"g8_agri_t5_u{u_order}_p{page_idx}_b{comp_idx}",
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
        print(f"[SUCCESS] Ingestion Complete for Grade 8 Topic 5: '{topic.name}'")
        print(f"[*] Units Created:   {total_units}")
        print(f"[*] Lessons Created: {total_lessons}")
        print(f"[*] Total Pages:     {total_pages}")
        print(f"[*] Total Blocks:    {total_blocks}")
        print("=" * 80)

if __name__ == "__main__":
    replace_flag = "--replace" in sys.argv or True
    ingest_cbc_grade8_agriculture_topic5(replace=replace_flag)
