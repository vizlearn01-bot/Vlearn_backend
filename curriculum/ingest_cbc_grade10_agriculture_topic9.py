"""
VLearn CBC Grade 10 Agriculture — Topic 9: Animal Handling and Safety
Production Ingestion Engine (Deep Senior Secondary Pedagogical Edition)

Curriculum: CBC (ID: 5)
Grade: Grade 10 (ID: 5, Level: 10)
Subject: Agriculture
Topic: Animal Handling and Safety (Topic Order: 9)

Decomposed into 9 Learning Units & 9 Published Lessons:
  1. Introduction to Animal Handling and Safety (5 Pages, 11 Blocks)
  2. Forms of Handling in the Community (Safe Practices) (5 Pages, 11 Blocks)
  3. Forms of Handling (Inhumane Treatments to Avoid) (5 Pages, 11 Blocks)
  4. Safety Structures for Handling Livestock (5 Pages, 11 Blocks)
  5. Tools and Equipment for Safe Handling (5 Pages, 11 Blocks)
  6. Safe Restraint and Positioning (Animal Behavior Concepts) (5 Pages, 11 Blocks)
  7. Safety of Persons Handling Animals (Zoonoses & Safety Habits) (5 Pages, 11 Blocks)
  8. Community Safety Observation & Excursion (5 Pages, 11 Blocks)
  9. Topic Review and Practical Assessment (8 Pages, 17 Blocks)
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

def build_topic9_curriculum():
    """Returns the comprehensive pedagogical page and block structure for Grade 10 Topic 9: Animal Handling and Safety."""
    return [
        # =====================================================================
        # LESSON 1: Introduction to Animal Handling and Safety
        # =====================================================================
        {
            "unit_order": 1,
            "unit_name": "Introduction to Animal Handling and Safety",
            "unit_description": "Definition of animal handling; 4 pillars (Animal Welfare, Handler Safety, Improved Productivity, Reduced Economic Losses); endocrine response to stress (adrenaline blocking oxytocin milk let-down; carcass bruising losses at abattoirs).",
            "lesson_title": "Principles of Animal Handling, Welfare, and Endocrine Stress Physiology",
            "pages": [
                [
                    {
                        "type": "suggested_image",
                        "title": "Farmer Handling Dairy Cow Gently on Pasture",
                        "content": {
                            "title": "Farmer Handling Dairy Cow Gently on Pasture",
                            "caption": "A livestock farmer interacting calmly with a dairy cow, establishing trust and reducing fear to optimize milk production and animal wellbeing."
                        }
                    },
                    {
                        "type": "learning_goal",
                        "title": "Lesson Objectives: Introduction to Handling",
                        "content": {
                            "title": "What We Will Master Today",
                            "goals": [
                                "Define **animal handling** within a commercial livestock enterprise context.",
                                "Analyze the **4 Pillars of Humane Animal Handling** (Welfare, Safety, Productivity, Economics).",
                                "Explain how **stress hormones (adrenaline and cortisol)** block milk let-down and reduce daily live weight gain.",
                                "Evaluate slaughterhouse **carcass bruising financial deductions** at the Kenya Meat Commission (KMC)."
                            ]
                        }
                    },
                    {
                        "type": "concept_explanation",
                        "title": "What is Animal Handling?",
                        "content": {
                            "title": "The Art and Science of Humane Livestock Management",
                            "text": "**Animal handling** encompasses the complete spectrum of physical methods, behavioral strategies, and restraining interactions used by farmers to manage livestock during daily operations.\n\n- **Beyond Physical Force**: Proper handling is not about physical overpowering; it is a sophisticated application of animal psychology, sensory perception, and low-stress behavioral guiding.\n- **The Ethical Mandate**: Livestock are sentient beings capable of feeling pain, fear, and distress. Humane treatment ensures farm animals live with dignity while maximizing agricultural profitability."
                        }
                    }
                ],
                [
                    {
                        "type": "concept_explanation",
                        "title": "The 4 Pillars of Humane Animal Handling",
                        "content": {
                            "title": "Why Handling Protocols Drive Agribusiness Profit",
                            "text": "1. **Animal Welfare**: Eliminates physical pain, chronic fear, and suffering; fulfills the international 'Five Freedoms' of animal welfare.\n2. **Handler Safety**: Working with powerful, unpredictable animals ($500\\text{--}800\\text{ kg}$ bulls, protective sows) carries severe injury risks (goring, crushing, kicks). Humane restraint guarantees zero human injuries.\n3. **Biological Productivity & Endocrine Health**:\n- In Dairy: Fear triggers the release of **adrenaline**, which acts as a direct biochemical antagonist to **oxytocin**, causing complete **milk let-down failure**!\n- In Beef & Pigs: Elevated **cortisol** suppresses immune defenses, slows daily feed conversion, and causes dark, firm, dry (DFD) meat.\n4. **Economic Loss Prevention**: Eliminates muscle bruising; bruised meat is condemned and trimmed during abattoir post-mortem inspections, causing massive financial losses to farmers."
                        }
                    },
                    {
                        "type": "suggested_diagram",
                        "title": "The 4 Pillars of Humane Animal Handling",
                        "content": {
                            "title": "The 4 Pillars of Humane Animal Handling",
                            "caption": "Conceptual framework diagram: 1 Animal Welfare (Dignity & Care) -> 2 Handler Safety (Zero Farm Injuries) -> 3 High Productivity (Oxytocin Flow & Weight Gain) -> 4 Economic Profit (Zero Carcass Bruising & Vet Savings)."
                        }
                    }
                ],
                [
                    {
                        "type": "comparison_table",
                        "title": "Humane Handling vs Rough Handling Impacts",
                        "content": {
                            "title": "Livestock Handling Impact Matrix",
                            "headers": ["Operational Factor", "Humane Low-Stress Handling", "Rough Aggressive Handling (Beating / Shouting)"],
                            "rows": [
                                ["Endocrine Response", "High oxytocin release; low cortisol", "Surge of adrenaline and cortisol"],
                                ["Dairy Milk Let-Down", "Complete, rapid milk extraction; healthy udder", "Milk let-down failure; residual milk; mastitis risk"],
                                ["Beef Weight Gain", "Steady daily gain (1.0–1.5 kg/day)", "Depressed feed intake; weight loss from stress"],
                                ["Slaughter Carcass Grade", "Clean, unbruised Grade 1 carcass", "Severe hematomas; condemned bruised muscle tissue"],
                                ["Handler Injury Risk", "Zero to minimal (Animals remain calm)", "High risk of kicks, goring, and broken bones"]
                            ]
                        }
                    },
                    {
                        "type": "suggested_video",
                        "title": "Principles of Safe Animal Handling & Flight Zones",
                        "content": {
                            "title": "Principles of Safe Animal Handling & Flight Zones",
                            "description": "Agronomic instructional guide demonstrating low-stress cattle movement, flight zone dynamics, and the elimination of fear-induced milk withholding.",
                            "url": "https://www.youtube.com/watch?v=dQw4w9WgXcQ"
                        }
                    }
                ],
                [
                    {
                        "type": "mini_activity",
                        "title": "Classroom Practical: Observing Animal Fear Reactions",
                        "content": {
                            "title": "Behavioral Reaction Diagnostic",
                            "task": "1. In the school farm or home compound, observe a group of dairy cattle or goats.\n2. Step Approach A: Approach calmly and slowly while speaking in a low, gentle voice.\n3. Step Approach B: Approach quickly while waving hands and shouting.\n4. Record animal physical reactions: ear posture, tail movement, eye whites, and flight distance.",
                            "materials": ["Observation Sheet", "Pen", "Livestock Paddock"],
                            "safety": "Do not enter pen with aggressive bulls; observe from safe perimeter."
                        }
                    },
                    {
                        "type": "key_takeaway",
                        "title": "Core Summary: Handling Principles",
                        "content": {
                            "title": "Key Takeaways",
                            "text": "- **Animal handling is guiding livestock safely** using behavioral psychology.\n- **4 Pillars**: Welfare, Handler Safety, Productivity, and Economic profit.\n- **Stress triggers adrenaline**, which blocks oxytocin and halts milk let-down.\n- **Rough handling causes severe carcass bruising**, resulting in abattoir deductions."
                        }
                    }
                ],
                [
                    {
                        "type": "knowledge_check",
                        "title": "Check Your Understanding: Physiological Cause of Milk Let-Down Failure",
                        "content": {
                            "question": "Why does rough, aggressive handling and shouting at a dairy cow immediately prior to milking cause a sudden and drastic drop in milk yield?",
                            "options": [
                                "The cow physically drinks all its milk back into its stomach",
                                "Fear and pain trigger the release of adrenaline, which physiologically blocks oxytocin, preventing the contraction of alveolar myoepithelial cells and halting milk let-down",
                                "The milk turns to solid cheese inside the teat canal",
                                "The cow's rumen bacteria stop digesting cellulose"
                            ],
                            "answer": "B",
                            "explanation": "Milk let-down is an endocrine reflex mediated by the hormone oxytocin. When a cow is frightened or beaten, its adrenal glands release adrenaline. Adrenaline constricts mammary blood vessels and directly blocks oxytocin receptors, preventing alveolar contraction and leaving milk trapped in the udder."
                        }
                    }
                ]
            ]
        },

        # =====================================================================
        # LESSON 2: Forms of Handling in the Community (Safe Practices)
        # =====================================================================
        {
            "unit_order": 2,
            "unit_name": "Forms of Handling in the Community (Safe Practices)",
            "unit_description": "Routine operations (feeding, watering, milking, breeding/AI, health/drenching); safe transport protocols (non-slip loading ramps with solid side walls, bedding, ventilation, stocking density); quick-release knot halter hitch.",
            "lesson_title": "Routine Livestock Handling Operations, Safe Transport, and Loading Protocols",
            "pages": [
                [
                    {
                        "type": "suggested_image",
                        "title": "Livestock Loading Ramp with Non-Slip Cleats and Solid Side Rails",
                        "content": {
                            "title": "Livestock Loading Ramp with Non-Slip Cleats and Solid Side Rails",
                            "caption": "A permanent concrete and timber livestock loading ramp designed with a gentle slope and solid walls to guide cattle safely onto transport vehicles without balking."
                        }
                    },
                    {
                        "type": "learning_goal",
                        "title": "Lesson Objectives: Safe Handling & Transport",
                        "content": {
                            "title": "What We Will Master Today",
                            "goals": [
                                "Execute safe handling procedures during **feeding, watering, milking, and breeding/AI**.",
                                "Design and evaluate **livestock transport protocols** (loading ramps, ventilation, bedding, stocking density).",
                                "Explain why **solid side walls on loading ramps** prevent livestock balking.",
                                "Tie and deploy a **Quick-Release Halter Hitch knot**."
                            ]
                        }
                    },
                    {
                        "type": "concept_explanation",
                        "title": "Routine Daily Handling Operations",
                        "content": {
                            "title": "Safe Execution of Daily Farm Tasks",
                            "text": "1. **Feeding & Watering**: Deliver rations calmly. Ensure feed troughs provide adequate linear spacing ($60\\text{--}70\\text{ cm/cow}$) to prevent dominant animals from bullying weaker heifers.\n2. **Hygienic Milking**: Approach cows from the side; wash udder with warm water and a clean towel (stimulating oxytocin); strip first streams into a strip cup; handle teats gently.\n3. **Breeding & Artificial Insemination (AI)**: Always secure the cow in a **cattle crush with a rear service gate** to protect the AI technician from backward kicks.\n4. **Health Interventions (Drenching / Vaccination)**: Restrain the animal's head securely with a halter or head gate before inserting drenching nozzles into the corner of the mouth."
                        }
                    }
                ],
                [
                    {
                        "type": "concept_explanation",
                        "title": "Livestock Transport Engineering & Safety Protocols",
                        "content": {
                            "title": "Eliminating Transit Trauma and Trampling",
                            "text": "Transporting livestock is a high-risk operation requiring strict engineering standards:\n\n- **Non-Slip Loading Ramp**: Slope angle must **never exceed 20 degrees**; fitted with horizontal non-slip cleats ($20\\text{ cm}$ spacing).\n- **THE SOLID-WALL RULE**: Loading ramps and races must have **solid side walls**. Cattle have wide-angle vision ($330^\\circ$) but poor depth perception; solid walls block out distracting shadows, moving trucks, and people, preventing animals from balking or reversing.\n- **Vehicle Standards**: Adequate cross-ventilation, smooth padded internal partitions, and a **10 cm clean straw/sawdust bedding layer** to prevent animals from slipping in urine/manure.\n- **Stocking Density**: Never overload trucks! Overcrowding causes animals to slip, fall, and be trampled to death under the hooves of the herd."
                        }
                    },
                    {
                        "type": "suggested_diagram",
                        "title": "Safe Livestock Transport & Solid-Wall Loading Ramp Dynamics",
                        "content": {
                            "title": "Safe Livestock Transport & Solid-Wall Loading Ramp Dynamics",
                            "caption": "Engineering schematic showing: 1 Solid-wall loading ramp (≤20° slope), 2 Non-slip stepped cleats, 3 Ventilated padded transport truck with clean straw bedding, and 4 Safe partitioned stocking density."
                        }
                    }
                ],
                [
                    {
                        "type": "comparison_table",
                        "title": "Safe Transport vs Unsafe Transport Standards",
                        "content": {
                            "title": "Livestock Transport Safety Matrix",
                            "headers": ["Transport Parameter", "Safe Standard Operating Procedure", "Dangerous Inhumane Practice"],
                            "rows": [
                                ["Loading Method", "Gradual ramp (≤20° slope) with solid walls", "Forcing animals to jump from high truck beds"],
                                ["Truck Flooring", "Non-slip rubber mats with deep straw bedding", "Bare wet metal/wooden floor slick with manure"],
                                ["Stocking Density", "Adequate standing room; partitioned by size", "Severe overcrowding (causes fatal trampling)"],
                                ["Ventilation & Shade", "Open slatted upper sides with roof cover", "Completely enclosed unventilated canvas tarp"],
                                ["Rest & Watering", "Stop every 6–8 hours for water and rest", "Non-stop transit under scorching sun without water"]
                            ]
                        }
                    },
                    {
                        "type": "mini_activity",
                        "title": "Laboratory Practical: Tying the Quick-Release Halter Hitch Knot",
                        "content": {
                            "title": "Emergency Knot-Tying Practicum",
                            "task": "1. Obtain a 2-meter length of sisal/hemp rope.\n2. Practice tying a Quick-Release Halter Hitch around a wooden post.\n3. Apply strong tension to simulate an animal pulling back.\n4. Pull the free loop end to verify that the knot releases instantly with one hand!",
                            "materials": ["2m Sisal / Cotton Rope", "Wooden Post"],
                            "safety": "Keep fingers clear of tightening loops."
                        }
                    }
                ],
                [
                    {
                        "type": "key_takeaway",
                        "title": "Core Summary: Safe Handling & Transport",
                        "content": {
                            "title": "Key Takeaways",
                            "text": "- **Restrain cattle in a crush** during AI and medical treatments.\n- **Use loading ramps with solid walls** to block visual distractions and prevent balking.\n- **Keep ramp slopes below 20 degrees** with non-slip cleats.\n- **Always use quick-release knots** to allow instant freeing in emergencies."
                        }
                    },
                    {
                        "type": "knowledge_check",
                        "title": "Check Your Understanding: Rationale for Solid Side Walls on Loading Ramps",
                        "content": {
                            "question": "What is the primary biological and behavioral reason why livestock loading ramps must be constructed with solid, opaque side walls rather than open-slat rails?",
                            "options": [
                                "Solid walls prevent cold wind from blowing onto the animals' legs",
                                "Cattle have wide-angle vision but poor depth perception; solid walls block distracting peripheral visual movements, shadows, and people, preventing animals from balking and refusing to load",
                                "Solid walls make the ramp 50% lighter to carry",
                                "To ensure that handlers cannot see which animals are entering the truck"
                            ],
                            "answer": "B",
                            "explanation": "Livestock possess a wide panoramic visual field and are easily spooked by sudden peripheral motion, light reflections, and moving shadows. Solid side walls eliminate these lateral visual distractions, creating a calm, clear forward path that encourages smooth, continuous forward movement without balking or panic."
                        }
                    }
                ]
            ]
        },

        # =====================================================================
        # LESSON 3: Forms of Handling (Inhumane Treatments to Avoid)
        # =====================================================================
        {
            "unit_order": 3,
            "unit_name": "Forms of Handling (Inhumane Treatments to Avoid)",
            "unit_description": "Inhumane practices (beating, tail-twisting, thin wire/nylon rope cutting, overloaded draught donkeys in heat, blunt castration); humane alternatives (herding flags/boards, wide padded chest harnesses, scheduled cool-hour work).",
            "lesson_title": "Inhumane Animal Treatments: Identification, Consequences, and Humane Alternatives",
            "pages": [
                [
                    {
                        "type": "suggested_image",
                        "title": "Working Draught Donkey Fitted with Padded Chest Harness",
                        "content": {
                            "title": "Working Draught Donkey Fitted with Padded Chest Harness",
                            "caption": "A working donkey in a rural community fitted with a wide, padded canvas chest harness that distributes pulling force evenly across the skeletal frame without cutting into skin."
                        }
                    },
                    {
                        "type": "learning_goal",
                        "title": "Lesson Objectives: Inhumane Treatments & Alternatives",
                        "content": {
                            "title": "What We Will Master Today",
                            "goals": [
                                "Identify common **inhumane livestock handling practices** in local communities.",
                                "Analyze the severe welfare and productivity consequences of **beating, tail-twisting, and wire tethering**.",
                                "Explain the mechanical damage caused by **unpadded rope harnesses on draught donkeys**.",
                                "Deploy **humane alternatives: Herding flags, herding boards, and padded harnesses**."
                            ]
                        }
                    },
                    {
                        "type": "concept_explanation",
                        "title": "Identifying Inhumane Livestock Practices",
                        "content": {
                            "title": "Cruelty Destroys Farm Profit and Animal Dignity",
                            "text": "Under the CBC Agriculture framework, learners must actively identify and eliminate harmful traditional practices:\n\n1. **Beating and Whipping**: Using heavy wooden sticks, metal pipes, or thorny switches to drive animals. Causes severe hematomas, bone fractures, and extreme chronic fear.\n2. **Tail-Twisting and Breaking**: Twisting cattle tails violently to force forward movement; breaks coccygeal vertebrae and damages spinal nerves.\n3. **Wire and Unpadded Nylon Tethering**: Tying legs with thin nylon cord or fencing wire that cuts through skin and tendons, causing septic gangrene.\n4. **Overloading Draught Animals**: Forcing donkeys/oxen to pull carts exceeding their body weight during the scorching midday heat without water, causing heat stroke and spinal collapse.\n5. **Blunt Castration & Inhumane Slaughter**: Using rusty knives or dull elastrator bands on mature animals without anesthesia."
                        }
                    }
                ],
                [
                    {
                        "type": "concept_explanation",
                        "title": "Humane, Low-Stress Alternatives",
                        "content": {
                            "title": "Working Smarter with Behavioral Tools",
                            "text": "- **Plastic Herding Flags & Sorting Paddles**: Lightweight plastic flags attached to a fiberglass cane. Waved gently, they create a visual barrier that directs animals quietly using their natural flight instinct—zero physical pain!\n- **Plywood Herding Boards**: Used in pig handling; handler holds a lightweight board to block the pig's line of sight, guiding it smoothly into pens without shouting or kicking.\n- **Padded Chest Harnesses for Donkeys**: Replace thin neck ropes with wide ($8\\text{--}10\\text{ cm}$), padded leather or canvas chest straps that distribute draft force across the pectoral muscles.\n- **Cool-Hour Work Schedules**: Work draught animals early morning (6:00 AM – 10:00 AM) and late afternoon (4:00 PM – 6:00 PM), providing clean water every 2 hours."
                        }
                    },
                    {
                        "type": "suggested_diagram",
                        "title": "Inhumane vs Humane Livestock Driving & Harnessing Methods",
                        "content": {
                            "title": "Inhumane vs Humane Livestock Driving & Harnessing Methods",
                            "caption": "Comparative visual graphic: Inhumane Methods (Wooden Sticks, Tail-Twisting, Thin Wire Tethers, Overloaded Midday Donkeys) vs Humane Solutions (Plastic Herding Flags, Padded Chest Harnesses, Sorting Boards, Shaded Rest)."
                        }
                    }
                ],
                [
                    {
                        "type": "comparison_table",
                        "title": "Inhumane Practices vs Humane Solutions Matrix",
                        "content": {
                            "title": "Animal Welfare Correction Framework",
                            "headers": ["Inhumane Practice", "Physical & Economic Damage", "Humane Modern Alternative", "Agribusiness Benefit"],
                            "rows": [
                                ["Hitting cattle with wooden sticks", "Hematomas, bruised carcass, fear stress", "Lightweight plastic herding flags & canes", "Zero carcass bruising; calm herd"],
                                ["Twisting & breaking cattle tails", "Fractured vertebrae, chronic nerve damage", "Gentle tapping or opening sorting gate", "Zero spinal injuries; compliant animals"],
                                ["Thin nylon rope donkey harness", "Raw bleeding neck sores, infection", "Wide (8cm) padded canvas chest harness", "Zero harness sores; 40% more pulling power"],
                                ["Overworking donkeys in midday heat", "Heat stroke, dehydration, early mortality", "Work early morning/evening with water stops", "Doubled working lifespan of draught animals"],
                                ["Lifting sheep by wool fleece", "Skin tears, hematomas, joint dislocation", "Support under chest and rump with two hands", "Zero skin trauma; premium fleece quality"]
                            ]
                        }
                    },
                    {
                        "type": "mini_activity",
                        "title": "Agribusiness Practical: Making a Padded Donkey Harness from Local Materials",
                        "content": {
                            "title": "Humane Harness Crafting Workshop",
                            "task": "1. Collect discarded canvas sacking, cotton padding, and a wide woven strap.\n2. Stitch a 10 cm wide padded chest band designed to fit across a donkey's pectoral girdle.\n3. Fit the harness onto a school farm donkey, ensuring no pressure rests on the windpipe.\n4. Demonstrate that the donkey pulls comfortably without friction chafing.",
                            "materials": ["Woven Canvas Strap", "Cotton Padding", "Needle and Twine", "Donkey"],
                            "safety": "Work gently around the donkey's head; do not startle the animal."
                        }
                    }
                ],
                [
                    {
                        "type": "key_takeaway",
                        "title": "Core Summary: Inhumane Treatments",
                        "content": {
                            "title": "Key Takeaways",
                            "text": "- **Never beat animals or twist tails**; use plastic herding flags.\n- **Fit draught donkeys with wide padded chest harnesses** to prevent raw sores.\n- **Work draught animals in cool morning and evening hours** with regular water.\n- **Never lift sheep by their wool**; support under chest and rump."
                        }
                    },
                    {
                        "type": "knowledge_check",
                        "title": "Check Your Understanding: Humane Solution for Donkey Harness Sores",
                        "content": {
                            "question": "A smallholder donkey owner notices deep, bleeding friction wounds developing along the donkey's neck and chest during cart transport. What is the root cause and the correct humane solution?",
                            "options": [
                                "The donkey is genetically weak; the owner should sell it for slaughter",
                                "The sores are caused by using thin, unpadded nylon ropes that concentrate draft force on a tiny surface area; the solution is to fit a wide (8–10 cm) padded canvas chest harness that distributes the pulling load across the chest muscles",
                                "The donkey needs to be worked harder in the midday sun to dry out the wounds",
                                "The cart needs to be loaded with more weight to balance the donkey's neck"
                            ],
                            "answer": "B",
                            "explanation": "Thin ropes concentrate hundreds of kilograms of pulling draft force onto a tiny, sharp surface line, cutting directly into the donkey's skin and muscle. Switching to a wide, padded canvas or leather breast-collar harness spreads the mechanical load evenly across the animal's strong chest musculature, eliminating friction sores."
                        }
                    }
                ]
            ]
        },

        # =====================================================================
        # LESSON 4: Safety Structures for Handling Livestock
        # =====================================================================
        {
            "unit_order": 4,
            "unit_name": "Safety Structures for Handling Livestock",
            "unit_description": "Cattle crush & squeeze chute anatomy (rear sliding gate, side squeeze rails, yoke/head gate, service gate, operator safety path); loading ramps (≤20° slope, non-slip cleats); milking parlors; gate safety.",
            "lesson_title": "Livestock Safety Structures: The Cattle Crush, Squeeze Chutes, and Loading Ramps",
            "pages": [
                [
                    {
                        "type": "suggested_image",
                        "title": "Cattle Restrained Safely in Timber Cattle Crush for Veterinary Inspection",
                        "content": {
                            "title": "Cattle Restrained Safely in Timber Cattle Crush for Veterinary Inspection",
                            "caption": "A dairy cow secured inside a sturdy wooden cattle crush, allowing the veterinary officer to safely inspect for ticks and administer injections without physical danger."
                        }
                    },
                    {
                        "type": "learning_goal",
                        "title": "Lesson Objectives: Safety Structures",
                        "content": {
                            "title": "What We Will Master Today",
                            "goals": [
                                "Describe the engineering design and agricultural purpose of a **Cattle Crush (Squeeze Chute)**.",
                                "Label the critical components of a crush: **Head Gate (Yoke), Side Rails, Rear Sliding Gate, and Service Gate**.",
                                "Design a **Livestock Loading Ramp** ($\le 20^\circ$ slope, non-slip cleats, solid side walls).",
                                "Analyze how safety structures protect handlers and animals during routine veterinary procedures."
                            ]
                        }
                    },
                    {
                        "type": "concept_explanation",
                        "title": "The Anatomy of a Standard Cattle Crush",
                        "content": {
                            "title": "The Indispensable Farm Restraint Corridor",
                            "text": "A **cattle crush** is a narrow, heavily built wooden or steel corridor designed to restrain a single bovine animal safely for veterinary and management procedures:\n\n1. **Head Gate (Yoke)**: Located at the front exit; locks firmly around the animal's neck just behind the jaw, immobilizing the head while preventing forward lunging or backing up.\n2. **Side Rails / Squeeze Mechanism**: Sturdy horizontal timber/metal rails spaced to prevent limbs from protruding. In squeeze chutes, side walls move inward slightly, supporting the animal and exerting calming deep-tissue pressure.\n3. **Rear Sliding Gate**: Slides shut behind the animal to prevent it from reversing and to block the next animal in the race.\n4. **Service / Vet Gate**: A small hinged door at the rear allowing safe access to the animal's flank and rectum (for AI or pregnancy diagnosis) without standing in the kicking zone."
                        }
                    }
                ],
                [
                    {
                        "type": "suggested_diagram",
                        "title": "Top-Down Architectural Schematic of a Standard Cattle Crush",
                        "content": {
                            "title": "Top-Down Architectural Schematic of a Standard Cattle Crush",
                            "caption": "Engineering top-down blueprint: 1 Funnel Entrance Race, 2 Rear Sliding Gate, 3 Narrow Single-Animal Corridor (65–70cm width), 4 Head Gate / Yoke, and 5 Safe Operator Working Zone outside the rails."
                        }
                    },
                    {
                        "type": "concept_explanation",
                        "title": "Loading Ramps and Milking Parlor Structures",
                        "content": {
                            "title": "Engineering for Safety and Ergonomics",
                            "text": "- **Loading Ramps**: Must have a slope angle **not exceeding 20 degrees**; fitted with horizontal non-slip cleats ($20\\text{ cm}$ spacing) and solid side walls ($1.5\\text{ m}$ height) to prevent jumping.\n- **Milking Parlors (Herringbone / Tandem)**: Feature elevated cow platforms ($80\\text{--}90\\text{ cm}$ high) with safety pit design, allowing milkers to work upright without back strain while shielding the milker's face from kicks.\n- **Fences & Gates**: Must swing smoothly with self-latching locks on the **outside of posts** to prevent crushed fingers."
                        }
                    }
                ],
                [
                    {
                        "type": "comparison_table",
                        "title": "Livestock Safety Structures and Their Specialized Agricultural Uses",
                        "content": {
                            "title": "Safety Structures Functional Matrix",
                            "headers": ["Safety Structure", "Key Engineering Features", "Primary Operations Conducted", "Handler Safety Protection"],
                            "rows": [
                                ["Cattle Crush / Chute", "Single-animal width (65–70cm), head yoke, sliding gate", "Vaccination, drenching, AI, dehorning, tagging", "Zero goring, charging, or lateral crushing"],
                                ["Livestock Loading Ramp", "Slope ≤20°, non-slip cleats, solid side walls", "Loading/unloading trucks for transport/market", "Prevents jumping, falling, and ramp refusal"],
                                ["Elevated Milking Parlor", "Raised platform (85cm), safety pit barrier", "Hygienic machine/manual milking", "Prevents milker back strain and face kicks"],
                                ["Sorting Race & Gates", "Funnel race with 2-way / 3-way drafting gates", "Drafting herd into groups (slaughter, breeding)", "Allows one handler to sort 100 cattle safely"]
                            ]
                        }
                    },
                    {
                        "type": "mini_activity",
                        "title": "Field Practical: Architectural Sketching and Audit of a Cattle Crush",
                        "content": {
                            "title": "Farm Safety Structure Audit",
                            "task": "1. Inspect the school farm or local dip tank cattle crush.\n2. Measure the internal corridor width (optimal: 65–70 cm for adults) and side rail height.\n3. Test the locking mechanism of the head gate and rear sliding gate.\n4. Draw a labeled top-down architectural sketch in your notebook.",
                            "materials": ["Measuring Tape", "Graph Notebook", "Pencil"],
                            "safety": "Do not climb inside the crush while cattle are present."
                        }
                    }
                ],
                [
                    {
                        "type": "key_takeaway",
                        "title": "Core Summary: Safety Structures",
                        "content": {
                            "title": "Key Takeaways",
                            "text": "- **A cattle crush secures single animals** for vaccinations, AI, and drenching.\n- **The head gate (yoke) locks the neck**, immobilizing head movement.\n- **Loading ramps must have $\\le 20^\\circ$ slope** with solid side walls and non-slip cleats.\n- **Elevated milking parlors protect milkers** from back strain and kicks."
                        }
                    },
                    {
                        "type": "knowledge_check",
                        "title": "Check Your Understanding: Rationale for Cattle Crush in Bull Vaccination",
                        "content": {
                            "question": "Which farm operation must ALWAYS be executed inside a well-constructed cattle crush with the head gate secured, rather than in an open grazing paddock?",
                            "options": [
                                "Leading a 3-week-old calf to drink clean water",
                                "Administering a jugular blood draw and intramuscular vaccine to a mature 700kg breeding bull",
                                "Letting dairy cows graze on Napier grass in the morning",
                                "Feeding salt mineral blocks to sheep"
                            ],
                            "answer": "B",
                            "explanation": "Administering medical injections or drawing jugular blood from a mature 700kg bull in an open paddock is extremely dangerous. The bull can charge, kick, or crush the handler. Securing the bull in a cattle crush with its head immobilized in the yoke eliminates charging and lateral movement, guaranteeing total safety for both handler and animal."
                        }
                    }
                ]
            ]
        },

        # =====================================================================
        # LESSON 5: Tools and Equipment for Safe Handling
        # =====================================================================
        {
            "unit_order": 5,
            "unit_name": "Tools and Equipment for Safe Handling",
            "unit_description": "Leading & control tools (rope halter fitting, restraining ropes, brass/steel bull ring in nasal septum + solid lead stick); PPE (steel-toed boots with non-slip treads, heavy leather gloves, overalls).",
            "lesson_title": "Handling Tools, Restraint Equipment, and Personal Protective Gear (PPE)",
            "pages": [
                [
                    {
                        "type": "suggested_image",
                        "title": "Dairy Cow Fitted with a Properly Positioned Head Halter",
                        "content": {
                            "title": "Dairy Cow Fitted with a Properly Positioned Head Halter",
                            "caption": "A dairy cow wearing a properly fitted head halter with the noseband sitting midway between the eyes and muzzle, allowing secure, gentle directional leading."
                        }
                    },
                    {
                        "type": "learning_goal",
                        "title": "Lesson Objectives: Handling Tools & PPE",
                        "content": {
                            "title": "What We Will Master Today",
                            "goals": [
                                "Identify primary livestock leading and control tools (**Halter, Restraining Ropes, Bull Ring, Lead Stick**).",
                                "Demonstrate how to **fit a rope halter correctly** without pinching nostrils.",
                                "Explain the mechanical control principle of the **Bull Ring and Lead Stick**.",
                                "Select appropriate **Personal Protective Equipment (PPE)** for farm tasks."
                            ]
                        }
                    },
                    {
                        "type": "concept_explanation",
                        "title": "Leading and Restraint Tools",
                        "content": {
                            "title": "Safe Physical Control Instruments",
                            "text": "1. **Rope / Leather Halter**: A headstall fitting over the poll and nosebridge. Allows the handler to guide the animal's head effortlessly (where the head goes, the body follows).\n2. **Restraining Ropes**: High-strength natural fiber (sisal, hemp) or braided cotton ropes. Used for casting (gently laying down large animals for surgical procedures using the Reuff's method) and leg tying.\n3. **Bull Ring and Solid Lead Stick**:\n- **The Nasal Septum Principle**: The nasal septum of cattle is richly innervated with sensitive nerve endings. A permanent brass/steel ring is inserted through the septum.\n- **The Lead Stick**: When connected to the ring, a rigid steel/hardwood lead stick ($1.5\\text{ m}$ long) acts as a rigid standoff rod, preventing a powerful bull from charging into the handler's space while allowing gentle directional control."
                        }
                    }
                ],
                [
                    {
                        "type": "concept_explanation",
                        "title": "Personal Protective Equipment (PPE) Standards",
                        "content": {
                            "title": "Armoring the Livestock Handler",
                            "text": "Handlers must protect themselves from severe mechanical injuries, chemical burns, and zoonotic pathogens:\n\n- **Steel-Toed Safety Boots**: Feature internal steel toe caps ($>200\\text{ Joules}$ impact resistance) to protect feet from being crushed when stepped on by a $600\\text{ kg}$ cow, with deep oil-resistant rubber treads to prevent slipping on wet manure.\n- **Heavy-Duty Leather Gloves**: Shield hands from severe friction rope burns during animal lunges, animal bites, and abrasive wire scratches.\n- **Cotton Overalls**: Form a physical barrier protecting the skin and clothes from manure, drench chemicals, and external parasites (ticks and mange mites)."
                        }
                    },
                    {
                        "type": "suggested_diagram",
                        "title": "Animal Restraint Tools & Essential Handler PPE Ensemble",
                        "content": {
                            "title": "Animal Restraint Tools & Essential Handler PPE Ensemble",
                            "caption": "Illustrated equipment catalog: 1 Correctly fitted rope halter, 2 Bull ring and 1.5m solid lead staff, 3 Heavy-duty leather gloves, 4 Steel-toed non-slip gumboots, and 5 Cotton farm overall."
                        }
                    }
                ],
                [
                    {
                        "type": "comparison_table",
                        "title": "Handling Equipment and PPE Application Matrix",
                        "content": {
                            "title": "Tool & PPE Specification Chart",
                            "headers": ["Tool / PPE Item", "Material Construction", "Correct Application Procedure", "Hazard Prevented"],
                            "rows": [
                                ["Rope Halter", "Braided cotton / soft sisal", "Noseband placed midway between eyes & muzzle", "Head tossing; animal escaping while leading"],
                                ["Bull Ring & Lead Stick", "Brass ring + 1.5m rigid rod", "Clip stick snap-hook to ring; lead from side", "Bull charging or goring the handler"],
                                ["Steel-Toed Boots", "Rubber / leather with steel cap", "Wear with deep non-slip treads on concrete", "Foot crush fractures; slipping on manure"],
                                ["Leather Gloves", "Thick cowhide leather", "Wear during casting, halter leading, and roping", "Friction rope burns; skin lacerations"],
                                ["Waterproof Gumboots", "Heavy PVC / Nitrile rubber", "Wear during pigsty washing and footbath dipping", "Zoonotic bacterial infection; chemical burns"]
                            ]
                        }
                    },
                    {
                        "type": "mini_activity",
                        "title": "Laboratory Practical: Halter Fitting and PPE Inspection Lab",
                        "content": {
                            "title": "Halter Fitting Practicum",
                            "task": "1. Put on full PPE (Overalls, steel-toed boots, leather gloves).\n2. Obtain a standard rope halter.\n3. Under teacher supervision, fit the halter onto a calm calf or goat.\n4. Check that the noseband does not pinch the nostrils and the lead rope runs under the chin.\n5. Lead the animal 20 meters, turn 180 degrees, and return.",
                            "materials": ["Rope Halter", "Calf / Goat", "PPE Kit"],
                            "safety": "Keep feet clear of hooves; never wrap the lead rope around your wrist or hand!"
                        }
                    }
                ],
                [
                    {
                        "type": "key_takeaway",
                        "title": "Core Summary: Tools & PPE",
                        "content": {
                            "title": "Key Takeaways",
                            "text": "- **Fit halters with the noseband midway** between eyes and muzzle.\n- **Never wrap a lead rope around your hand** or wrist.\n- **Bull rings and lead sticks provide standoff distance** and control over bulls.\n- **Always wear steel-toed boots and leather gloves** when handling large stock."
                        }
                    },
                    {
                        "type": "knowledge_check",
                        "title": "Check Your Understanding: Rationale for Bull Ring and Lead Stick",
                        "content": {
                            "question": "Why is a permanent brass ring inserted into the nasal septum of a mature bull, and how does the solid lead stick ensure handler safety?",
                            "options": [
                                "The ring measures the bull's core body temperature continuously",
                                "The nasal septum is richly innervated and sensitive; gentle pressure provides control, while the rigid solid lead stick maintains a safe 1.5m standoff distance that physically prevents the bull from charging into the handler",
                                "The ring locks the bull's jaw shut so it cannot chew pasture",
                                "The lead stick is used to hit the bull on the back"
                            ],
                            "answer": "B",
                            "explanation": "The nasal septum has high nerve sensitivity, meaning the bull cooperates readily with minimal force. The rigid lead stick connects to the ring, acting as a solid physical spacer that keeps the bull at a safe 1.5m distance and prevents it from lunging or charging into the handler's personal space."
                        }
                    }
                ]
            ]
        },

        # =====================================================================
        # LESSON 6: Safe Restraint and Positioning (Animal Behavior Concepts)
        # =====================================================================
        {
            "unit_order": 6,
            "unit_name": "Safe Restraint and Positioning (Animal Behavior Concepts)",
            "unit_description": "Flight zone personal space perimeter; Point of Balance at the shoulder (behind moves forward, in front moves backward); Blind spot behind hindquarters (kicking hazard); reading stress signals (ears, tail, eyes, hooves); escape routes.",
            "lesson_title": "Animal Behavior Mastery: Flight Zones, Point of Balance, and Stress Signals",
            "pages": [
                [
                    {
                        "type": "suggested_image",
                        "title": "Cattle Herd Moving Calmly on Highland Grazing Pasture",
                        "content": {
                            "title": "Cattle Herd Moving Calmly on Highland Grazing Pasture",
                            "caption": "A herd of cattle moving smoothly along a pasture trail as the handler works on the boundary of their collective flight zone, demonstrating low-stress behavioral guiding."
                        }
                    },
                    {
                        "type": "learning_goal",
                        "title": "Lesson Objectives: Animal Behavior & Positioning",
                        "content": {
                            "title": "What We Will Master Today",
                            "goals": [
                                "Define an animal's **Flight Zone** and explain how its size varies with tameness.",
                                "Apply the **Point of Balance principle at the shoulder** to move animals forward or backward.",
                                "Identify the animal's **Blind Spot and Kicking Hazard Zone**.",
                                "Recognize subtle **stress and aggression signals** (pinned ears, eye whites, tucked tails, hoof stomping)."
                            ]
                        }
                    },
                    {
                        "type": "concept_explanation",
                        "title": "The Flight Zone and Point of Balance",
                        "content": {
                            "title": "The Invisible Boundaries of Animal Movement",
                            "text": "1. **The Flight Zone**: The animal's personal safety perimeter.\n- Step **inside** the flight zone $\\rightarrow$ Animal moves away.\n- Step **outside** the flight zone $\\rightarrow$ Animal stops and turns to face you.\n- *Tame dairy cows have a flight zone of 0–1 meter; wild range cattle have a flight zone of 10–30 meters*.\n\n2. **The Point of Balance**: Located at the animal's **shoulder** (perpendicular to body axis):\n- Handler stands **BEHIND the shoulder** $\\rightarrow$ Animal moves **FORWARD**.\n- Handler stands **IN FRONT of the shoulder** $\\rightarrow$ Animal stops or moves **BACKWARD**."
                        }
                    }
                ],
                [
                    {
                        "type": "concept_explanation",
                        "title": "The Blind Spot and Safe Positioning",
                        "content": {
                            "title": "Staying Clear of the Danger Zones",
                            "text": "3. **The Blind Spot**: Cattle and horses have a panoramic field of vision ($330^\\circ$), but have a **blind spot directly behind their tail (hindquarters)**.\n- *DANGER*: Approaching silently into the blind spot startles prey animals, triggering an instinctive, violent **defensive kick**.\n- *Always speak calmly before approaching from behind*.\n\n4. **The Safe Working Zone & Escape Routes**:\n- Work close to the shoulder or flank while maintaining gentle physical contact (reducing kick acceleration force), or stand completely outside the kicking radius.\n- **Never get pinned between an animal and a solid wall!** Always maintain an unobstructed **escape route**."
                        }
                    },
                    {
                        "type": "suggested_diagram",
                        "title": "The Flight Zone, Point of Balance, and Kicking Blind Spot",
                        "content": {
                            "title": "The Flight Zone, Point of Balance, and Kicking Blind Spot",
                            "caption": "Circular behavioral schematic showing: 1 Point of Balance (Line through shoulders), 2 Flight Zone perimeter, 3 Handler forward movement entry vector (behind shoulder), and 4 Rear 30° Blind Spot (High Kick Danger Zone)."
                        }
                    }
                ],
                [
                    {
                        "type": "comparison_table",
                        "title": "Livestock Stress Signals by Species",
                        "content": {
                            "title": "Animal Body Language & Stress Diagnostic",
                            "headers": ["Species", "Relaxed / Content Signals", "Early Stress / Fear Signals", "Imminent Aggression / Attack"],
                            "rows": [
                                ["Cattle", "Slow chewing cud; ears relaxed; tail swishing flies", "Head raised high; whites of eyes showing; loud bellowing", "Head lowered, pawing ground, rapid flank breathing, charging"],
                                ["Pigs", "Soft grunting; wagging tail; rooting calmly", "High-pitched squealing; pacing along fence lines", "Champing jaws (foaming mouth), bristling spine hair, biting"],
                                ["Goats & Sheep", "Grazing in loose herd; rhythmic chewing", "Head held rigid; nostrils flaring; herd bunching", "Stamping front hooves, lowering horns, snorting loudly"],
                                ["Donkeys / Horses", "Ears pointed forward; soft eyes; resting one hind leg", "Ears pinned flat against neck; tail swishing violently", "Bared teeth, lunging to bite, spinning to double-kick"]
                            ]
                        }
                    },
                    {
                        "type": "mini_activity",
                        "title": "Field Practical: Moving Cattle Using the Point of Balance",
                        "content": {
                            "title": "Low-Stress Cattle Herding Lab",
                            "task": "1. In an open paddock or race, approach a dairy cow from the side.\n2. Cross the Flight Zone boundary behind the shoulder: observe the cow walking forward.\n3. Walk forward and cross in front of the shoulder line: observe the cow halting and turning.\n4. Record observations and refine handler positioning.",
                            "materials": ["Paddock / Race", "Cattle", "Notebook"],
                            "safety": "Never position yourself directly behind the animal in its blind spot."
                        }
                    }
                ],
                [
                    {
                        "type": "key_takeaway",
                        "title": "Core Summary: Animal Behavior",
                        "content": {
                            "title": "Key Takeaways",
                            "text": "- **Flight Zone is the animal's personal space**; enter to move, exit to stop.\n- **Point of Balance is at the shoulder**: stand behind to move forward.\n- **Never enter the blind spot behind the tail** without speaking calmly.\n- **Always ensure a clear escape route** when working in confined pens."
                        }
                    },
                    {
                        "type": "knowledge_check",
                        "title": "Check Your Understanding: Application of Point of Balance",
                        "content": {
                            "question": "A livestock handler needs to move a mature dairy cow forward into a single-file crush without shouting or using sticks. Based on animal behavior principles, where should the handler stand relative to the cow?",
                            "options": [
                                "Directly in front of the cow's nose, waving a white jacket",
                                "Just behind the cow's shoulder line (Point of Balance), stepping calmly into its flight zone from the side",
                                "Directly behind the cow's tail in its blind spot",
                                "Sitting on the roof of the barn"
                            ],
                            "answer": "B",
                            "explanation": "The 'Point of Balance' is located at the animal's shoulder. Stepping inside the flight zone behind the shoulder line naturally motivates the animal to move forward. Stepping in front of the shoulder would block the animal and cause it to stop or reverse."
                        }
                    }
                ]
            ]
        },

        # =====================================================================
        # LESSON 7: Safety of Persons Handling Animals (Zoonoses & Safety Habits)
        # =====================================================================
        {
            "unit_order": 7,
            "unit_name": "Safety of Persons Handling Animals (Zoonoses & Safety Habits)",
            "unit_description": "Zoonoses (Anthrax spore hazard & non-clotting dark blood; Brucellosis raw milk & calving fluids; Ringworm); essential safety habits (handwashing biosecurity, zero food/drink in barns, teamwork on agitated animals).",
            "lesson_title": "Zoonotic Disease Defense, Handler Biosecurity, and Workplace Safety Habits",
            "pages": [
                [
                    {
                        "type": "suggested_image",
                        "title": "Veterinarian Administering Preventive Healthcare with Protective Gear",
                        "content": {
                            "title": "Veterinarian Administering Preventive Healthcare with Protective Gear",
                            "caption": "A veterinary professional wearing protective gloves and overalls while conducting a cattle clinical examination, demonstrating personal biosecurity against zoonoses."
                        }
                    },
                    {
                        "type": "learning_goal",
                        "title": "Lesson Objectives: Zoonoses & Biosecurity",
                        "content": {
                            "title": "What We Will Master Today",
                            "goals": [
                                "Define **zoonotic diseases** and explain their human transmission pathways.",
                                "Analyze high-risk livestock zoonoses (**Anthrax, Brucellosis, Rabies, Ringworm**).",
                                "Explain why an **Anthrax-suspected carcass must NEVER be opened or dissected**.",
                                "Execute **WHO standard handwashing biosecurity** and personal safety protocols."
                            ]
                        }
                    },
                    {
                        "type": "concept_explanation",
                        "title": "Major Livestock Zoonoses and Transmission Routes",
                        "content": {
                            "title": "Diseases Shared Between Animals and Humans",
                            "text": "**Zoonoses** are infectious diseases naturally transmissible between vertebrate animals and humans:\n\n1. **Anthrax (*Bacillus anthracis*)**:\n- **Clinical Signs**: Sudden death in livestock with **dark, tarry, non-clotting blood oozing from mouth, nostrils, and anus**, and absence of rigor mortis.\n- **THE BIOSECURITY RULE**: **NEVER OPEN OR DISSECT AN ANTHRAX CARCASS!** Exposure to oxygen triggers the bacteria to form indestructible spores that contaminate pasture for 50+ years and cause fatal cutaneous or pulmonary anthrax in humans!\n\n2. **Brucellosis (*Brucella abortus*)**:\n- **Transmission**: Drinking raw unpasteurized milk or direct contact with aborted fetuses/afterbirth fluids.\n- **Human Impact**: Severe undulating fever, chronic arthritis, and infertility.\n\n3. **Ringworm (*Trichophyton verrucosum*)**:\n- Highly contagious fungal infection forming circular, crusty, itchy skin lesions."
                        }
                    }
                ],
                [
                    {
                        "type": "concept_explanation",
                        "title": "Essential Handler Safety and Hygiene Habits",
                        "content": {
                            "title": "4 Golden Rules of Farm Biosecurity",
                            "text": "1. **Mandatory Handwashing**: Wash hands with warm water and disinfectant soap for at least **20 seconds** immediately after handling livestock or cleaning pens.\n2. **Zero Eating / Drinking in Barns**: Never consume food, drink water, or chew gum inside animal housing to prevent oral ingestion of fecal pathogens (*E. coli*, *Salmonella*).\n3. **Teamwork on Agitated Animals**: Never attempt to handle a sick, frightened, or calving cow alone; always work in pairs with a designated lookout.\n4. **Carcass Quarantine**: Immediately quarantine and bury deep (2 meters with quicklime) any carcass suspected of contagious zoonotic death."
                        }
                    },
                    {
                        "type": "suggested_diagram",
                        "title": "Major Livestock Zoonoses & Handlers Biosecurity Barrier",
                        "content": {
                            "title": "Major Livestock Zoonoses & Handlers Biosecurity Barrier",
                            "caption": "Biosecurity defense graphic: Pathogen Sources (Blood, Raw Milk, Feces, Abortions) Blocked by the 4 Handler Barriers (Milk Pasteurization, Waterproof Gloves, 20-Sec Handwashing, Sealed Anthrax Quarantine)."
                        }
                    }
                ],
                [
                    {
                        "type": "comparison_table",
                        "title": "Major Livestock Zoonoses Diagnostic & Prevention Chart",
                        "content": {
                            "title": "Zoonotic Diseases Protocol Matrix",
                            "headers": ["Zoonotic Disease", "Causative Agent", "Primary Animal Species", "Transmission Pathway to Humans", "Critical Preventive Protocol"],
                            "rows": [
                                ["Anthrax", "Bacillus anthracis (Bacterium)", "Cattle, sheep, goats", "Contact with blood/spores of dead carcass", "NEVER open carcass; deep burial with quicklime"],
                                ["Brucellosis", "Brucella abortus (Bacterium)", "Dairy cattle, goats", "Drinking raw milk; contact with placenta/fluids", "Boil/pasteurize milk; wear obstetrical gloves at birth"],
                                ["Rabies", "Rabies Lyssavirus (Virus)", "Dogs, cattle, donkeys", "Bites / saliva contacting open scratches", "Annual vaccination of farm dogs; avoid rabid animals"],
                                ["Ringworm", "Trichophyton (Fungus)", "Calves, young goats", "Direct skin contact with circular crusty lesions", "Wear gloves; apply antifungal wash to calf lesions"]
                            ]
                        }
                    },
                    {
                        "type": "mini_activity",
                        "title": "Laboratory Practical: The WHO 20-Second Handwashing Biosecurity Drill",
                        "content": {
                            "title": "Practical Biosecurity Handwashing Lab",
                            "task": "1. Following livestock handling, proceed to the sanitization sink.\n2. Wet hands, apply antibacterial soap, lather palms, back of hands, interlaced fingers, thumbs, and wrists.\n3. Maintain vigorous friction for a full 20 seconds (sing 'Happy Birthday' twice).\n4. Rinse with clean running water and dry with single-use paper towel.",
                            "materials": ["Sink with Running Water", "Antibacterial Soap", "Paper Towels", "Timer"],
                            "safety": "Ensure proper hygiene execution."
                        }
                    }
                ],
                [
                    {
                        "type": "key_takeaway",
                        "title": "Core Summary: Zoonoses & Biosecurity",
                        "content": {
                            "title": "Key Takeaways",
                            "text": "- **Zoonoses are diseases transmissible** from animals to humans.\n- **Never open a carcass suspected of Anthrax** (non-clotting dark blood).\n- **Always pasteurize milk** and wear gloves during calving to block Brucellosis.\n- **Wash hands for 20 seconds** with soap and never eat inside animal housing."
                        }
                    },
                    {
                        "type": "knowledge_check",
                        "title": "Check Your Understanding: Emergency Protocol for Suspected Anthrax",
                        "content": {
                            "question": "A farmer finds a mature steer dead in the pasture with dark, tarry blood that fails to clot oozing from its mouth, nose, and anus. What is the mandatory immediate biosecurity protocol?",
                            "options": [
                                "Perform an immediate post-mortem dissection to check the stomach contents",
                                "Do NOT cut or open the carcass under any circumstances; immediately quarantine the site and report to veterinary authorities for deep burial with quicklime",
                                "Skin the steer and sell the meat to the local community butcher",
                                "Feed the carcass to the farm pigs to avoid waste"
                            ],
                            "answer": "B",
                            "explanation": "These symptoms are classic signs of Anthrax (Bacillus anthracis). Opening the carcass exposes the bacteria to atmospheric oxygen, causing them to form highly resistant spores that persist in the soil for decades and infect humans with potentially lethal pulmonary or cutaneous anthrax. The carcass must remain sealed and be buried 2 meters deep covered in quicklime."
                        }
                    }
                ]
            ]
        },

        # =====================================================================
        # LESSON 8: Community Safety Observation & Excursion
        # =====================================================================
        {
            "unit_order": 8,
            "unit_name": "Community Safety Observation & Excursion",
            "unit_description": "Field excursion planning; observation rubrics for markets/dip tanks; community advocacy (building concrete loading ramps, training on herding flags, stopping fleece-lifting).",
            "lesson_title": "Field Excursion: Community Livestock Safety Audit and Humane Advocacy",
            "pages": [
                [
                    {
                        "type": "suggested_image",
                        "title": "Agricultural Extension and Community Livestock Market Inspection",
                        "content": {
                            "title": "Agricultural Extension and Community Livestock Market Inspection",
                            "caption": "Agriculture students and livestock officers conducting a field survey at a rural livestock yard, auditing handling structures, loading ramps, and animal welfare practices."
                        }
                    },
                    {
                        "type": "learning_goal",
                        "title": "Lesson Objectives: Community Safety Audit",
                        "content": {
                            "title": "What We Will Master Today",
                            "goals": [
                                "Draft an objective **Community Animal Handling Observation Rubric**.",
                                "Conduct an on-site field excursion to a **livestock market, dip tank, or abattoir**.",
                                "Analyze observed safe vs unsafe handling practices.",
                                "Formulate a **Community Humane Handling Advocacy Campaign**."
                            ]
                        }
                    },
                    {
                        "type": "concept_explanation",
                        "title": "Designing a Community Handling Audit",
                        "content": {
                            "title": "Bridging Classroom Knowledge to Real-World Agribusiness",
                            "text": "Visiting a local livestock market, communal dip tank, or slaughterhouse exposes learners to actual industry practices:\n\n1. **Pre-Excursion Preparation**: Establish an audit rubric focusing on 4 observation parameters:\n- *Driving Methods*: Are handlers using sticks, whips, or herding flags?\n- *Restraint & Holding*: Are pens overcrowded? Are ropes cutting into skin?\n- *Physical Structures*: Are loading ramps, races, and crushes functional and non-slip?\n- *Water & Shade*: Do animals have access to drinking water and shade during full-day markets?"
                        }
                    }
                ],
                [
                    {
                        "type": "concept_explanation",
                        "title": "From Observation to Community Advocacy",
                        "content": {
                            "title": "Empowering Youth as Animal Welfare Champions",
                            "text": "Once field data is gathered, learners transform findings into practical, constructive solutions:\n\n- **Identified Hazard**: Traders beating bulls because the market lacks a loading ramp.\n- **Constructive Community Solution**: Senior school class partners with the County Livestock Department and Market Committee to build a simple wooden/concrete loading ramp and demonstrates the use of plastic herding flags.\n- **The Economic Case**: Explaining to traders that eliminating beating prevents **KES 3,000–5,000 in carcass bruising deductions** per animal at the slaughterhouse!"
                        }
                    },
                    {
                        "type": "comparison_table",
                        "title": "Sample Community Livestock Market Observation Rubric",
                        "content": {
                            "title": "Market Audit Rubric Template",
                            "headers": ["Audit Parameter", "Observed Field Practice", "Welfare Status (Safe / Unsafe)", "Proposed Humane Community Correction"],
                            "rows": [
                                ["Loading onto trucks", "Beating with thorny sticks onto 1.2m bed", "UNSAFE / INHUMANE", "Construct a 20° concrete loading ramp; use herding flags"],
                                ["Sheep handling", "Lifting sheep by wool fleece into pickup", "UNSAFE / INHUMANE", "Train handlers to support under chest and rump with 2 hands"],
                                ["Draught donkeys", "Thin nylon ropes cutting raw neck sores", "UNSAFE / INHUMANE", "Demonstrate stitching 10cm padded canvas chest harnesses"],
                                ["Cattle holding pens", "Clean water troughs provided; uncrowded", "SAFE / EXCELLENT", "Commend market committee; maintain daily sanitation"]
                            ]
                        }
                    }
                ],
                [
                    {
                        "type": "mini_activity",
                        "title": "Agribusiness Practical: Drafting a 1-Page Market Handling Reform Proposal",
                        "content": {
                            "title": "Community Advocacy Campaign Design",
                            "task": "1. In groups of four, draft a 1-page Action Brief for your local County Livestock Committee.\n2. Identify the top 2 animal welfare violations observed in local livestock trade.\n3. Present 2 low-cost, high-impact engineering and behavioral solutions.\n4. Calculate the financial savings in prevented meat bruising for local farmers.",
                            "materials": ["Advocacy Template", "Financial Calculator", "Pen"],
                            "safety": "Ensure professional, evidence-based recommendations."
                        }
                    },
                    {
                        "type": "key_takeaway",
                        "title": "Core Summary: Community Advocacy",
                        "content": {
                            "title": "Key Takeaways",
                            "text": "- **Audit real-world markets** using structured observation rubrics.\n- **Advocate for permanent loading ramps** and herding flags.\n- **Stop inhumane sheep fleece-lifting** and thin-rope donkey harnesses.\n- **Humane handling protects farm profits** and community food security."
                        }
                    }
                ],
                [
                    {
                        "type": "knowledge_check",
                        "title": "Check Your Understanding: Constructive Market Advocacy Rationale",
                        "content": {
                            "question": "What is the most effective and constructive way for a Senior School Agriculture class to convince local livestock traders to stop beating cattle with heavy sticks at the market?",
                            "options": [
                                "Shouting insults and throwing stones at the traders' trucks",
                                "Demonstrating the economic benefits of herding flags and partnering with the market committee to construct a permanent loading ramp that eliminates the cause of animal refusal",
                                "Refusing to attend school until the market is shut down",
                                "Stealing all the wooden driving sticks at night"
                            ],
                            "answer": "B",
                            "explanation": "Constructive advocacy relies on education, physical solutions, and economic evidence. Demonstrating that herding flags move cattle faster without pain, and providing a safe loading ramp that stops animal balking, directly solves the traders' operational problems while protecting them from slaughterhouse carcass bruising deductions."
                        }
                    }
                ]
            ]
        },

        # =====================================================================
        # LESSON 9: Topic Review and Practical Assessment
        # =====================================================================
        {
            "unit_order": 9,
            "unit_name": "Topic Review and Practical Assessment",
            "unit_description": "Synthesis: working with natural animal instincts; Farm Safety Audit performance task; 8 Summative Topic Assessment MCQs covering the complete Topic 9 module.",
            "lesson_title": "Synthesis of Animal Handling, Safety Systems, and Summative Assessment",
            "pages": [
                [
                    {
                        "type": "suggested_image",
                        "title": "Well-Organized Modern Dairy Handling Facility with Safety Corridors",
                        "content": {
                            "title": "Well-Organized Modern Dairy Handling Facility with Safety Corridors",
                            "caption": "A premier agricultural handling facility integrating non-slip flooring, sturdy cattle crushes, safe gates, and humane management protocols."
                        }
                    },
                    {
                        "type": "learning_goal",
                        "title": "Lesson Objectives: Synthesis & Summative Assessment",
                        "content": {
                            "title": "What We Will Master Today",
                            "goals": [
                                "Synthesize the **complete Animal Handling and Safety framework**.",
                                "Complete the **Farm Safety Audit consulting task**.",
                                "Resolve the **Agitated Dairy Steer Escape Simulation**.",
                                "Complete the comprehensive **Summative Topic Assessment** covering all 9 lessons of Topic 9."
                            ]
                        }
                    },
                    {
                        "type": "concept_explanation",
                        "title": "Master Animal Handling & Safety Operational Synthesis",
                        "content": {
                            "title": "The Unified Framework of Humane Livestock Management",
                            "text": "1. **Ethical Foundation**: The 4 Pillars (Welfare, Safety, Productivity, Economics); adrenaline blocks oxytocin milk let-down; rough handling causes abattoir carcass bruising.\n2. **Engineering Structures**: Cattle crush with head gate/yoke for single-animal restraint; loading ramps ($\le 20^\circ$ slope, non-slip cleats, solid side walls); elevated milking parlors.\n3. **Restraint Tools & PPE**: Properly fitted rope halters; bull ring and $1.5\\text{ m}$ lead stick; steel-toed boots with deep treads; heavy leather gloves.\n4. **Behavioral Dynamics**: Flight zone navigation; point of balance at the shoulder (stand behind to move forward); avoid rear blind spot; maintain escape routes.\n5. **Biosecurity & Zoonoses**: Anthrax (never open carcass; non-clotting blood); Brucellosis (pasteurize milk, gloves at calving); 20-second handwashing."
                        }
                    }
                ],
                [
                    {
                        "type": "suggested_diagram",
                        "title": "Master Animal Handling & Safety Operational Synthesis",
                        "content": {
                            "title": "Master Animal Handling & Safety Operational Synthesis",
                            "caption": "Comprehensive system diagram linking: 1 Behavioral Understanding (Flight Zone & Point of Balance) -> 2 Safety Structures (Crush & Ramp) -> 3 PPE & Restraint Tools -> 4 Biosecurity Protocol -> 5 High Agribusiness Profit."
                        }
                    },
                    {
                        "type": "comparison_table",
                        "title": "Master Animal Handling Protocol Summary",
                        "content": {
                            "title": "Synthesized Animal Handling & Safety Matrix",
                            "headers": ["Management Scenario", "Required Safety Structure", "Specialized Handling Tool", "Key Behavioral / Safety Rule"],
                            "rows": [
                                ["Bull Vaccination / Blood Draw", "Cattle crush with locked head yoke", "Halter & 1.5m solid lead stick", "Work from outside rails; never stand inside"],
                                ["Truck Loading for Market", "Solid-wall loading ramp (≤20° slope)", "Plastic herding flags / canes", "Avoid shouting; do not overload vehicle"],
                                ["Dairy Cow Milking", "Elevated milking parlor stanchion", "Strip cup & clean warm cloth", "Gentle touch; stimulate oxytocin; zero stress"],
                                ["Draught Donkey Cart Pulling", "Cart with balanced load capacity", "Wide (10cm) padded canvas harness", "Work early morning/evening; water every 2 hours"],
                                ["Suspected Anthrax Death", "Quarantine perimeter fence", "None (Do NOT touch or open carcass)", "Deep burial (2m) with quicklime; notify vet"]
                            ]
                        }
                    }
                ],
                [
                    {
                        "type": "mini_activity",
                        "title": "Performance Task: The Agitated Dairy Steer Emergency Response Plan",
                        "content": {
                            "title": "Emergency Handling Consulting Scenario",
                            "task": "A 300kg dairy steer has escaped into the school compound, tossing its head, bellowing, and stamping hooves. A farm hand wants to chase it with a whip and lasso its hind leg.\n\n**Your Deliverable**: Draft an Emergency Handling Protocol:\n1. Explain why chasing with a whip is dangerous and triggers adrenaline.\n2. Detail the step-by-step humane procedure to guide the steer into a holding pen and cattle crush using its flight zone and a companion cow.\n3. List the PPE required for your team.",
                            "materials": ["Case Handout", "Response Template", "Pen"],
                            "safety": "Ensure rigorous, evidence-based safety protocols."
                        }
                    },
                    {
                        "type": "key_takeaway",
                        "title": "Core Summary: Handling Mastery",
                        "content": {
                            "title": "Key Takeaways",
                            "text": "- **Work with animal instincts**, not against them.\n- **Use cattle crushes and loading ramps** for total physical safety.\n- **Protect handlers with steel-toed boots, leather gloves, and biosecurity**.\n- **Humane handling maximizes milk, meat quality, and farm profits**."
                        }
                    }
                ],
                # Pages 4 to 8: 8 Summative Assessment MCQs
                [
                    {
                        "type": "knowledge_check",
                        "title": "Summative MCQ 1: Endocrine Mechanism of Milk Withholding",
                        "content": {
                            "question": "What is the specific physiological and endocrine mechanism that causes a dairy cow to withhold its milk when subjected to shouting, beating, or fear in the milking parlor?",
                            "options": [
                                "The cow drinks its own milk through an internal esophagus duct",
                                "Fear triggers the release of adrenaline from the adrenal medulla, which physiologically blocks oxytocin receptors and constricts mammary blood vessels, preventing milk let-down",
                                "The milk turns into solid butter inside the cow's teats",
                                "The cow's rumen stops producing digestive acids"
                            ],
                            "answer": "B",
                            "explanation": "Milk let-down is stimulated by oxytocin, which contracts the myoepithelial cells surrounding milk alveoli. When fear or pain occurs, adrenaline is released, causing immediate vasoconstriction and blocking oxytocin action, resulting in milk let-down failure."
                        }
                    },
                    {
                        "type": "knowledge_check",
                        "title": "Summative MCQ 2: Solid-Wall Loading Ramp Rationale",
                        "content": {
                            "question": "Why are commercial livestock loading ramps constructed with solid, opaque side walls and a maximum slope of 20 degrees?",
                            "options": [
                                "To prevent wind from cooling the animals' tails",
                                "To block lateral visual distractions and moving shadows that trigger balking, while ensuring a gentle slope with non-slip cleats that prevents slipping and trampling",
                                "To make the loading ramp invisible to wild birds",
                                "To ensure handlers cannot count the number of animals loading"
                            ],
                            "answer": "B",
                            "explanation": "Livestock possess wide-angle peripheral vision and poor depth perception, making them balk at shadows and motion. Solid walls eliminate these visual distractions, and a gentle ≤20° slope with cleats prevents slipping, ensuring calm, continuous forward loading."
                        }
                    }
                ],
                [
                    {
                        "type": "knowledge_check",
                        "title": "Summative MCQ 3: Humane Draught Donkey Harnessing",
                        "content": {
                            "question": "What is the primary agricultural engineering reason for replacing thin nylon rope harnesses on draught donkeys with wide, padded canvas or leather chest straps?",
                            "options": [
                                "Thin ropes make the cart travel too fast",
                                "Thin ropes concentrate high draft forces on a tiny surface area, cutting into skin and causing painful bleeding sores, whereas wide padded straps distribute the load safely across pectoral muscles",
                                "Padded harnesses change the donkey's coat color to white",
                                "Thin ropes attract biting flies from the forest"
                            ],
                            "answer": "B",
                            "explanation": "Pressure equals force divided by area. Thin ropes concentrate the cart's full draft weight onto a narrow band, slicing through skin. Wide, padded harnesses spread the pulling load over a broad surface area of strong chest muscles, preventing friction wounds and maximizing pulling efficiency."
                        }
                    },
                    {
                        "type": "knowledge_check",
                        "title": "Summative MCQ 4: Cattle Crush Function and Yoke Mechanism",
                        "content": {
                            "question": "What is the primary function of the head gate (yoke) located at the front of a cattle crush during veterinary operations?",
                            "options": [
                                "To weigh the animal's head",
                                "To lock securely around the animal's neck, immobilizing head movement and preventing forward lunging or backward reversing during injections and drenching",
                                "To provide a mirror for the animal to look at",
                                "To cut the animal's horns automatically"
                            ],
                            "answer": "B",
                            "explanation": "The head yoke locks behind the animal's jaw and neck, restricting both forward and backward head movement, enabling safe access for drenching, ear tagging, blood sampling, and dehorning while protecting the handler."
                        }
                    }
                ],
                [
                    {
                        "type": "knowledge_check",
                        "title": "Summative MCQ 5: Bull Ring and Solid Lead Stick Principle",
                        "content": {
                            "question": "How does the combination of a brass bull ring in the nasal septum and a solid lead stick provide absolute safety when leading a mature breeding bull?",
                            "options": [
                                "The ring emits an electrical shock whenever the bull moves",
                                "The sensitive nasal septum ensures compliance with gentle force, while the 1.5m rigid lead stick acts as a physical spacer that prevents the bull from charging into the handler's space",
                                "The stick makes the bull fall asleep while walking",
                                "The ring locks the bull's eyes so it cannot see the handler"
                            ],
                            "answer": "B",
                            "explanation": "The rich nerve supply of the nasal septum ensures responsive directional control with gentle pressure, while the rigid lead stick prevents the bull from advancing into the handler's personal perimeter, maintaining a safe 1.5m standoff distance."
                        }
                    },
                    {
                        "type": "knowledge_check",
                        "title": "Summative MCQ 6: Point of Balance Forward Movement Vector",
                        "content": {
                            "question": "According to livestock behavioral psychology, where must a handler position themselves to encourage a cow to move forward along a handling race without using force?",
                            "options": [
                                "Directly in front of the cow's nose",
                                "Behind the cow's shoulder line (Point of Balance), entering its flight zone from the side",
                                "Directly behind its tail in the blind spot",
                                "On top of the cow's back"
                            ],
                            "answer": "B",
                            "explanation": "The shoulder is the animal's Point of Balance. Stepping inside the flight zone behind the shoulder line stimulates the animal's natural instinct to move forward along the race."
                        }
                    }
                ],
                [
                    {
                        "type": "knowledge_check",
                        "title": "Summative MCQ 7: Anthrax Biosecurity Protocol",
                        "content": {
                            "question": "Why is it strictly forbidden by veterinary and public health laws to open or dissect the carcass of a cow that died suddenly with non-clotting dark blood oozing from body orifices?",
                            "options": [
                                "The carcass contains valuable diamonds in its stomach",
                                "Opening the carcass exposes Bacillus anthracis bacteria to atmospheric oxygen, triggering the formation of highly resilient spores that persist in soil for decades and cause fatal Anthrax in humans",
                                "The blood will turn into sulfuric acid and dissolve dissecting tools",
                                "It makes the surrounding grass grow too tall"
                            ],
                            "answer": "B",
                            "explanation": "Bacillus anthracis vegetative cells sporulate when exposed to air. Opening the carcass releases millions of indestructible spores into the environment, contaminating pastures for decades and exposing handlers to lethal anthrax infection."
                        }
                    },
                    {
                        "type": "knowledge_check",
                        "title": "Summative MCQ 8: Economic Impact of Carcass Bruising",
                        "content": {
                            "question": "How does rough handling, beating with wooden sticks, and overcrowding in transport trucks directly cause severe economic losses to beef farmers at the slaughterhouse?",
                            "options": [
                                "It turns the beef into chicken meat",
                                "It causes severe deep-tissue bruising and hematomas; during post-mortem meat inspection, all bruised muscle tissue is condemned and trimmed away, drastically reducing the marketable carcass weight and price",
                                "It makes the leather impossible to tan",
                                "It causes slaughterhouses to charge double for electricity"
                            ],
                            "answer": "B",
                            "explanation": "Physical impacts rupture blood vessels, pooling blood into the muscle (hematomas/bruising). Under public health laws, all bruised meat must be condemned and trimmed away, causing massive weight deductions and financial penalties on the farmer's payout."
                        }
                    }
                ],
                # Page 8: Capstone Summary
                [
                    {
                        "type": "summary",
                        "title": "Topic 9 Capstone Summary: Animal Handling and Safety Mastery",
                        "content": {
                            "title": "Mastery Overview: Grade 10 Animal Handling, Welfare & Farm Safety",
                            "text": "Congratulations on mastering **Topic 9: Animal Handling and Safety**!\n\nYou have mastered:\n- **Principles & Stress Physiology**: The 4 Pillars (Welfare, Safety, Productivity, Economics); adrenaline blocking oxytocin; carcass bruising.\n- **Safe Routine Operations**: Milking, drenching, AI, and transport with non-slip solid-wall loading ramps ($\le 20^\\circ$ slope).\n- **Inhumane Treatments & Alternatives**: Eliminating beating and tail-twisting; using herding flags, sorting boards, and wide padded donkey harnesses.\n- **Safety Structures**: Complete cattle crush architecture (head yoke, sliding gate, service gate); loading ramps; milking parlors.\n- **Restraint Tools & PPE**: Halter fitting; bull rings with $1.5\\text{ m}$ lead sticks; steel-toed boots; heavy leather gloves.\n- **Behavioral Dynamics**: Flight zone navigation; point of balance at the shoulder; avoiding rear blind spots; escape routes.\n- **Zoonoses & Biosecurity**: Anthrax quarantine (never open carcass); Brucellosis defense; 20-second handwashing standard.\n- **Community Advocacy**: Conducting market audits and promoting humane handling campaigns."
                        }
                    },
                    {
                        "type": "key_takeaway",
                        "title": "Topic 9 Final Takeaway",
                        "content": {
                            "title": "The Humane Animal Handling Maxim",
                            "text": "Work with the animal's natural instincts, utilize proper safety structures and PPE, and treat all livestock with dignity to safeguard human life, protect animal welfare, and maximize farm profitability."
                        }
                    }
                ]
            ]
        }
    ]

@transaction.atomic
def ingest_grade10_topic9(replace=False):
    """Executes the complete production ingestion of Grade 10 Agriculture Topic 9: Animal Handling and Safety."""
    print("=" * 80)
    print("STARTING INGESTION: CBC Grade 10 Agriculture — Topic 9: Animal Handling and Safety")
    print("=" * 80)

    curriculum = Curriculum.objects.filter(name__iexact="CBC").first()
    grade = Grade.objects.filter(curriculum=curriculum, name__icontains="10").first()
    subject = Subject.objects.filter(grade=grade, name__iexact="Agriculture").first()

    assert curriculum and grade and subject, "Curriculum/Grade/Subject not found!"

    topic_name = "Animal Handling and Safety"
    topic = Topic.objects.filter(subject=subject, name=topic_name).first()
    if not topic:
        topic = Topic.objects.create(
            subject=subject,
            name=topic_name,
            description="Comprehensive theoretical, behavioral, and technical study of humane animal handling, stress endocrine physiology, cattle crush and loading ramp structures, restraint tools, flight zones, zoonotic biosecurity, and community welfare advocacy.",
            order=9
        )
        print(f"Created Topic 9: {topic.name} (ID: {topic.id})")
    else:
        topic.order = 9
        topic.description = "Comprehensive theoretical, behavioral, and technical study of humane animal handling, stress endocrine physiology, cattle crush and loading ramp structures, restraint tools, flight zones, zoonotic biosecurity, and community welfare advocacy."
        topic.save()
        print(f"Resolved Topic 9: {topic.name} (ID: {topic.id})")

    if replace:
        print("Flag --replace active: Clearing existing LearningUnits and Lessons for Topic 9...")
        topic.learning_units.all().delete()
        topic.lessons.all().delete()

    curriculum_data = build_topic9_curriculum()
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
                    "topic_order": 9,
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
                    block_id=f"g10_agri_t9_u{u_order}_p{page_idx}_b{comp_idx}",
                    block_type=b_type,
                    component_type=b_type,
                    title=b_title,
                    content=b_content,
                    order=block_order_counter,
                    page_number=page_idx,
                    component_order=comp_idx,
                    page_title=b_title if comp_idx == 1 else None,
                    metadata={"topic_order": 9, "unit_order": u_order, "page": page_idx}
                )
                block_order_counter += 1
                total_blocks += 1

        print(f"  Ingested Unit {u_order}: {u_name} -> Lesson '{l_title}' ({len(pages)} Pages, {block_order_counter - 1} Blocks)")

    print("=" * 80)
    print(f"INGESTION COMPLETE: Topic 9 '{topic.name}'")
    print(f"  Total Units:   {total_units}")
    print(f"  Total Lessons: {total_lessons}")
    print(f"  Total Pages:   {total_pages}")
    print(f"  Total Blocks:  {total_blocks}")
    print("=" * 80)

if __name__ == "__main__":
    replace_flag = "--replace" in sys.argv
    ingest_grade10_topic9(replace=replace_flag)
