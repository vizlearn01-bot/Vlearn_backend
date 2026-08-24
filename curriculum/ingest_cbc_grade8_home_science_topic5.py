"""
VLearn CBC Grade 8 Home Science — Topic 5: Community Service Learning (CSL) Class Activity
Production Ingestion Engine (Phase 1: Content & Card Architecture)

Curriculum: CBC (Curriculum ID: 5)
Grade: Grade 8 (Level: 8)
Subject: Home Science (ID: 28)
Topic: Community Service Learning (CSL) Class Activity (Topic Order: 5)

Decomposed into 3 Learning Units & 3 Published Lessons (24 Total Structured Pages):
  1. Spotting Community Problems & Pertinent Issues (8 Pages)
  2. Community Research & Data Collection Tools (8 Pages)
  3. Project Planning, Resource Management & Reflection (8 Pages)

Features:
  - Standard markdown bullet lists (- ) with proper spacing
  - Bold key terms, concepts, and structured tables
  - Step processes, diagnostic audits, and scenario checks

Usage:
  ./venv/bin/python curriculum/ingest_cbc_grade8_home_science_topic5.py [--replace]
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
    text = re.sub(r'\[(?:\d+|image_\d+|S\d+.*?|[\d,\s]+|p\.\s*[ivxlcdm\d]+)\]', '', text)
    # Convert unicode bullets to markdown list items
    text = re.sub(r'^[ \t]*[•\u2022][ \t]*', '- ', text, flags=re.MULTILINE)
    text = re.sub(r'([^\n])[ \t]+[•\u2022][ \t]+', r'\1\n- ', text)
    text = re.sub(r'^([^\n\-\*\d\>#][^\n]*)\n(- |\* )', r'\1\n\n$2', text, flags=re.MULTILINE)
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
    """Returns the comprehensive pedagogical page and block structure for Topic 5: Community Service Learning."""
    return [
        # =====================================================================
        # LESSON 1: Spotting Community Problems & Pertinent Issues
        # =====================================================================
        {
            "unit_order": 1,
            "unit_name": "Spotting Community Problems & Pertinent Issues",
            "unit_description": "Understanding Community Service Learning (CSL), identifying the 7 core Pertinent and Contemporary Issues (PCIs), evaluating community problems based on danger, population affected, and student feasibility, and prioritizing an actionable project topic.",
            "lesson_title": "Spotting Community Problems & Pertinent Issues",
            "pages": [
                # Page 1: Topic Introduction & Visual Hook
                [
                    {
                        "type": "suggested_image",
                        "title": "The Neighborhood Walk: Spotting Community Needs",
                        "content": {
                            "title": "The Neighborhood Walk: Spotting Community Needs",
                            "caption": "An active Kenyan rural community where families interact, trade, and face daily environmental and health challenges."
                        }
                    },
                    {
                        "type": "learning_goal",
                        "title": "Learning Objectives: Spotting Community Problems",
                        "content": {
                            "title": "What We Will Learn Today",
                            "goals": [
                                "Define **Community Service Learning (CSL)** and recognize the value of active citizenship.",
                                "Identify and explain the **7 core Pertinent and Contemporary Issues (PCIs)** in society.",
                                "Differentiate between **individual personal challenges** and **collective community issues**.",
                                "Evaluate and prioritize candidate problems using the **Priority Decision Matrix**."
                            ]
                        }
                    },
                    {
                        "type": "concept_explanation",
                        "title": "What is Community Service Learning?",
                        "content": {
                            "title": "Becoming Active Problem Solvers",
                            "text": "**Community Service Learning (CSL)** is an experiential teaching and learning strategy where students apply classroom academic knowledge and practical skills to solve real-world problems in their local community.\n\nRather than remaining passive observers, Grade 8 learners investigate urgent community challenges, collaborate with local leaders, design creative solutions, and reflect on their personal growth in leadership and civic responsibility."
                        }
                    }
                ],
                # Page 2: The 7 Core Pertinent and Contemporary Issues (PCIs)
                [
                    {
                        "type": "suggested_diagram",
                        "title": "The 7 Primary Pertinent and Contemporary Issues Bento Map",
                        "content": {
                            "title": "The 7 Primary Pertinent and Contemporary Issues Bento Map",
                            "caption": "Bento infographic illustrating the 7 core societal challenges: Environmental Waste, Lifestyle Diseases, Illnesses, Poverty, Violence, Food Insecurity, and Conflicts."
                        }
                    },
                    {
                        "type": "comparison_table",
                        "title": "The 7 Core Pertinent and Contemporary Issues (PCIs)",
                        "content": {
                            "title": "Understanding Real-World Community Challenges",
                            "headers": ["PCI Category", "Real-World Manifestation", "Impact on Community Life", "Home Science Connection"],
                            "rows": [
                                ["Environmental Degradation", "Plastic litter in drainage channels, cutting trees, water stream pollution", "Breeds malaria mosquitoes, blocks clean stormwater flow, causes soil erosion", "Waste sorting, eco-friendly abrasives, organic composting"],
                                ["Lifestyle Diseases", "High consumption of ultra-processed junk food, physical inactivity, obesity", "Early-onset diabetes, hypertension, cardiovascular strain in young people", "Meal planning, balanced nutrition, active household chores"],
                                ["Communicable & Non-Communicable Diseases", "Outbreaks of cholera, typhoid from dirty water, chronic asthma from dust", "School absenteeism, medical expenses, physical weakness in children", "Food hygiene, boiling drinking water, kitchen sanitization"],
                                ["Poverty & Livelihood Strain", "Families unable to afford basic foodstuffs, decent clothing, or clean housing", "Child malnutrition, school dropout, severe stress on family health", "Budgeting, upcycling textile crafts, low-cost nutritious meals"],
                                ["Violence in the Community", "Bullying in school estates, gender-based violence, unsafe nighttime alleys", "Destroys peaceful coexistence, creates fear and physical trauma", "Creating safe home environments, conflict mediation"],
                                ["Food Security Concerns", "Unreliable access to fresh vegetables, high grain prices, food storage rot", "Malnutrition, stunted child growth, micro-nutrient deficiencies", "Container gardening, sack farming, hygienic food preservation"],
                                ["Community Conflicts", "Disagreements over water well access, land boundaries, or grazing pasture", "Disrupts neighborhood unity, damages communal property", "Resource sharing, collaborative team planning"]
                            ]
                        }
                    }
                ],
                # Page 3: The Priority Decision Matrix
                [
                    {
                        "type": "suggested_diagram",
                        "title": "Community Problem Priority Decision Matrix",
                        "content": {
                            "title": "Community Problem Priority Decision Matrix",
                            "caption": "Decision matrix evaluating candidate problems across health danger, population affected, financial cost, and student feasibility."
                        }
                    },
                    {
                        "type": "concept_explanation",
                        "title": "How Groups Prioritize a Community Problem",
                        "content": {
                            "title": "The 3 Golden Criteria for Selection",
                            "text": "A student group cannot solve every neighborhood challenge at once. To choose the best project, evaluate candidate issues across three criteria:\n\n- **1. Urgency & Health Danger**: How severely does this problem threaten lives, health, or safety right now?\n- **2. Population Affected**: Does it hurt the entire neighborhood collectively (e.g. contaminated market water), or just one individual?\n- **3. Student Feasibility**: Can Grade 8 students realistically implement a safe, high-impact solution within school time and local resources?"
                        }
                    }
                ],
                # Page 4: Worked Example — The JSS Group Plenary Debate
                [
                    {
                        "type": "step_process",
                        "title": "Worked Example: The JSS Group Plenary Debate & Problem Selection",
                        "content": {
                            "title": "Step-by-Step Priority Evaluation",
                            "steps": [
                                {
                                    "step_number": 1,
                                    "title": "Brainstorm Initial Candidate Issues",
                                    "description": "Group members list 3 observed problems: **Option A** (Cholera outbreak at market food stalls), **Option B** (Building a tarmac road across sub-county), and **Option C** (Broken TV in chief's house)."
                                },
                                {
                                    "step_number": 2,
                                    "title": "Filter Out Non-Community or Non-Feasible Issues",
                                    "description": "Reject Option C (it is a private personal item, not a public issue). Reject Option B (cost is millions of shillings; impossible for students)."
                                },
                                {
                                    "step_number": 3,
                                    "title": "Evaluate Option A Against Home Science Competencies",
                                    "description": "Market stall sanitation directly connects to Home Science food hygiene, has high disease urgency, and can be solved by student-led cleaning and sensitization."
                                },
                                {
                                    "step_number": 4,
                                    "title": "Adopt Option A as the Official Project Focus",
                                    "description": "Group records Option A in the official project minutes and notifies the class teacher for final endorsement."
                                }
                            ]
                        }
                    }
                ],
                # Page 5: Individual Concern vs. Community Issue
                [
                    {
                        "type": "comparison_table",
                        "title": "Individual Concern vs. Community Issue",
                        "content": {
                            "title": "Distinguishing Personal Challenges from Public PCIs",
                            "headers": ["Scenario", "Classification", "Why It Fits This Category", "Action Required"],
                            "rows": [
                                ["A student loses their Home Science pencil during class", "Personal Concern", "Affects only one individual learner; no broader public health or safety impact", "Buy or borrow a replacement pencil"],
                                ["Market vendors sell uncovered cooked food next to open sewage", "Community Issue (PCI)", "Affects hundreds of consumers; poses direct public cholera and typhoid epidemic threat", "Organize CSL food hygiene and sanitation project"],
                                ["A family's home radio battery runs out", "Personal Concern", "Private household luxury challenge with zero public consequence", "Replace the battery at home"],
                                ["The local stream used for drinking water is choked with plastic waste", "Community Issue (PCI)", "Contaminates drinking water for the entire village and breeds malaria vectors", "Conduct community cleanup and water protection campaign"]
                            ]
                        }
                    }
                ],
                # Page 6: Hands-On Local Neighborhood PCI Walk
                [
                    {
                        "type": "mini_activity",
                        "title": "Hands-On: The Local Neighborhood PCI Walk",
                        "content": {
                            "title": "Activity: Audit 3 Local Community Challenges",
                            "instructions": "Take a 15-minute walk around your school compound or local neighborhood:\n\n1. **Observe and Record**: Identify 3 specific challenges (e.g. uncollected trash, lack of vegetable gardens, open drainage pools).\n2. **Map to PCIs**: Classify each challenge under one of the 7 official curriculum PCIs.\n3. **Score Feasibility**: Rate each issue from 1 to 5 on whether JSS students can realistically help solve it.\n\nPresent your top priority issue to your group during the next class session."
                        }
                    }
                ],
                # Page 7: Key Takeaways & Recall Helper
                [
                    {
                        "type": "key_takeaway",
                        "title": "Key Takeaways: Spotting Community Problems",
                        "content": {
                            "title": "Core Ideas to Remember",
                            "takeaways": [
                                "**Community Service Learning (CSL)** combines classroom theory with practical civic action to solve real problems.",
                                "The 7 PCIs are **Environmental Degradation**, **Lifestyle Diseases**, **Diseases**, **Poverty**, **Violence**, **Food Insecurity**, and **Conflicts**.",
                                "A **community problem** affects the public collectively, unlike a minor personal inconvenience.",
                                "Always prioritize projects based on **health urgency**, **population affected**, and **student feasibility**."
                            ]
                        }
                    },
                    {
                        "type": "memory_tip",
                        "title": "PCI Priority Recall Helper",
                        "content": {
                            "title": "Remember 'U-P-F'",
                            "tip": "**U**rgency (Health danger) + **P**opulation (Collective impact) + **F**easibility (Can students do it?)!"
                        }
                    }
                ],
                # Page 8: Knowledge Check
                [
                    {
                        "type": "knowledge_check",
                        "title": "Knowledge Check: Identifying & Prioritizing PCIs",
                        "content": {
                            "question": "A Grade 8 JSS group notices that many children in their village frequently suffer from severe stomach ailments after eating unwashed raw fruits bought near open gutters. Which PCI does this situation represent, and what is the best student-led action?",
                            "options": [
                                "Violence in the Community; call the police to arrest the fruit sellers.",
                                "Communicable Diseases and Environmental Degradation; organize a food hygiene sensitization campaign and market stall sanitation activity.",
                                "Personal Concern; tell the children to stop eating all fruits permanently.",
                                "Lifestyle Diseases; construct a commercial gym next to the fruit stalls."
                            ],
                            "correct_index": 1,
                            "explanation": "Stomach infections from food exposed to dirty gutters combine Communicable Diseases with Environmental Degradation. A feasible student-led Home Science project involves food safety education and practical stall cleaning."
                        }
                    }
                ]
            ]
        },

        # =====================================================================
        # LESSON 2: Community Research & Data Collection Tools
        # =====================================================================
        {
            "unit_order": 2,
            "unit_name": "Community Research & Data Collection Tools",
            "unit_description": "Conducting collaborative community research, understanding questionnaires, interview guides, and observation schedules, ethical and polite question formulation, and drafting field data collection instruments.",
            "lesson_title": "Community Research & Data Collection Tools",
            "pages": [
                # Page 1: Topic Introduction & Visual Hook
                [
                    {
                        "type": "suggested_image",
                        "title": "The Community Detective: Gathering Evidence",
                        "content": {
                            "title": "The Community Detective: Gathering Evidence",
                            "caption": "Students collaborating in a learning environment, taking notes and reviewing field data for evidence-based community action."
                        }
                    },
                    {
                        "type": "learning_goal",
                        "title": "Learning Objectives: Community Research & Tools",
                        "content": {
                            "title": "What We Will Learn Today",
                            "goals": [
                                "Explain why **evidence-based research** is essential prior to launching any community project.",
                                "Compare the 3 primary data instruments: **Questionnaires**, **Interview Guides**, and **Observation Schedules**.",
                                "Apply ethical principles of **respect**, **politeness**, and **privacy** in survey design.",
                                "Draft clear, objective, and structured questions for community stakeholders."
                            ]
                        }
                    },
                    {
                        "type": "concept_explanation",
                        "title": "Why We Research Before Acting",
                        "content": {
                            "title": "Don't Guess — Find the Real Facts!",
                            "text": "Launching a community project without research is like a doctor prescribing medicine without examining the patient!\n\n**Community research** allows students to uncover the root causes of a problem, hear directly from affected families, consult local resource persons (health officers, elders), and ensure that every shilling and hour spent delivers maximum positive impact."
                        }
                    }
                ],
                # Page 2: The 3 Core Data Collection Instruments
                [
                    {
                        "type": "suggested_diagram",
                        "title": "The 3 Core Data Collection Instruments: Questionnaire, Interview, and Observation",
                        "content": {
                            "title": "The 3 Core Data Collection Instruments: Questionnaire, Interview, and Observation",
                            "caption": "Side-by-side template sheets comparing a 4-question survey questionnaire, an open interview guide, and an observation checklist."
                        }
                    },
                    {
                        "type": "comparison_table",
                        "title": "Comparison of Data Collection Instruments",
                        "content": {
                            "title": "Matching the Tool to Your Research Goal",
                            "headers": ["Instrument", "Format & Structure", "Target Respondent", "Best Suited For"],
                            "rows": [
                                ["Questionnaire", "Written printed sheet with tick-boxes and multiple-choice options", "Large groups of community members (40–100 households)", "Quick, anonymous, standardized statistical data (e.g. how many homes boil water)"],
                                ["Interview Guide", "Spoken conversation with structured, open-ended discussion prompts", "Key local resource persons (Village elders, clinical nurses, public health officers)", "Gathering deep technical explanations, historical context, and expert recommendations"],
                                ["Observation Schedule", "Visual checklist of physical features, conditions, and behaviors to record", "Direct physical field environment (market stalls, school bins, drainage channels)", "Collecting unbiased visual evidence without interrupting people's daily work"]
                            ]
                        }
                    }
                ],
                # Page 3: Ethical Guidelines in Community Research
                [
                    {
                        "type": "concept_explanation",
                        "title": "Research Ethics and Politeness",
                        "content": {
                            "title": "Respecting Community Members",
                            "text": "When collecting data in our community, we represent our school and must uphold high standards of integrity:\n\n- **1. Voluntary Consent**: Always introduce yourself politely, explain the purpose of your project, and ask for permission before asking questions.\n- **2. Privacy & Confidentiality**: Never share respondents' private names or sensitive family details publicly without permission.\n- **3. Objective, Non-Judgmental Language**: Never ask rude, accusatory, or embarrassing questions (e.g. 'Why is your stall so dirty?').\n- **4. Punctuality & Gratitude**: Respect people's busy working hours and always thank them warmly for their time."
                        }
                    },
                    {
                        "type": "callout",
                        "title": "Research Golden Rule",
                        "content": {
                            "title": "Keep Questionnaires Short and Clear!",
                            "text": "A questionnaire with 10 clear, polite questions gets 100% completion. A confusing survey with 50 complicated questions causes frustration and gets thrown away!"
                        }
                    }
                ],
                # Page 4: Designing Polite & Objective Questions
                [
                    {
                        "type": "suggested_diagram",
                        "title": "Ethical Community Research Flow & Question Design Rules",
                        "content": {
                            "title": "Ethical Community Research Flow & Question Design Rules",
                            "caption": "Flowchart illustrating respectful introduction, clear tick-box formatting, unbiased wording, and warm gratitude."
                        }
                    },
                    {
                        "type": "comparison_table",
                        "title": "Good Questions vs. Bad Questions",
                        "content": {
                            "title": "Refining Question Phrasing for Quality Data",
                            "headers": ["Topic", "Poor / Biased Question (Bad)", "Polite & Objective Question (Good)", "Why the Good Version Works"],
                            "rows": [
                                ["Food Storage", "'Why do you leave your food on the dirty floor to rot?'", "'Where do you store dry food grains at home? [ ] Sealed sacks off the ground [ ] Open bins [ ] Other'", "Objective, structured, non-judgmental, and easy to analyze"],
                                ["Water Safety", "'Do you drink dirty unsafe water like your neighbors?'", "'What method do you use to treat drinking water? [ ] Boiling [ ] Water Guard [ ] Filtration [ ] None'", "Respectful, neutral, and provides clear quantitative options"],
                                ["Waste Disposal", "'Are you too lazy to sweep your front yard?'", "'How often is household solid waste collected in this area? [ ] Daily [ ] Weekly [ ] Not collected'", "Focuses on the systemic public service rather than personal insult"]
                            ]
                        }
                    }
                ],
                # Page 5: Worked Example — Drafting a Food Sanitation Observation Schedule
                [
                    {
                        "type": "step_process",
                        "title": "Worked Example: Constructing a 4-Point Food Stall Observation Schedule",
                        "content": {
                            "title": "The Step-by-Step Observation Tool Design",
                            "steps": [
                                {
                                    "step_number": 1,
                                    "title": "Define Specific Observable Features",
                                    "description": "Identify 4 physical sanitation indicators: Food covering, hand-washing water, apron cleanliness, and trash bin presence."
                                },
                                {
                                    "step_number": 2,
                                    "title": "Create Clear Yes / No Tick Columns",
                                    "description": "Construct a simple table with columns: 'Item Observed', 'Yes [ ]', 'No [ ]', and 'Brief Notes'."
                                },
                                {
                                    "step_number": 3,
                                    "title": "Include Objective Observation Standards",
                                    "description": "Define criteria: E.g., 'Is cooked food enclosed in a glass display or covered with a clean mesh net?'"
                                },
                                {
                                    "step_number": 4,
                                    "title": "Test the Schedule Before Full Field Visit",
                                    "description": "Conduct a 5-minute pilot test in the school canteen to ensure group members record data consistently."
                                }
                            ]
                        }
                    }
                ],
                # Page 6: Hands-On Questionnaire Drafting Activity
                [
                    {
                        "type": "mini_activity",
                        "title": "Hands-On: Drafting a Mini Community Questionnaire",
                        "content": {
                            "title": "Activity: Create a 3-Question Survey",
                            "instructions": "In your Home Science notebook, design a short survey for local households investigating **Household Kitchen Waste Disposal**:\n\n1. **Greeting**: Write a 1-sentence polite greeting explaining your project.\n2. **Draft 3 Questions**: Include 1 multiple-choice question on organic composting, 1 on plastic sorting, and 1 on collection frequency.\n3. **Formatting**: Ensure each question has clear tick-boxes `[ ]`.\n\nExchange questionnaires with a partner to check for politeness and clarity."
                        }
                    }
                ],
                # Page 7: Key Takeaways & Recall Helper
                [
                    {
                        "type": "key_takeaway",
                        "title": "Key Takeaways: Community Research & Tools",
                        "content": {
                            "title": "Core Ideas to Remember",
                            "takeaways": [
                                "**Evidence-based research** ensures community projects target real root causes rather than guesses.",
                                "**Questionnaires** collect statistical data from large groups; **Interviews** provide expert depth; **Observation** gives unbiased physical evidence.",
                                "Always maintain **research ethics**: obtain voluntary consent, protect privacy, and write polite non-judgmental questions.",
                                "Good survey questions are **short**, **structured**, and provide **clear tick-boxes**."
                            ]
                        }
                    },
                    {
                        "type": "memory_tip",
                        "title": "Research Tools Recall Helper",
                        "content": {
                            "title": "Remember 'Q-I-O'",
                            "tip": "**Q**uestionnaire (Large survey), **I**nterview (Expert talk), **O**bservation (Eyes on the field)!"
                        }
                    }
                ],
                # Page 8: Knowledge Check
                [
                    {
                        "type": "knowledge_check",
                        "title": "Knowledge Check: Selecting Research Instruments & Question Design",
                        "content": {
                            "question": "A Grade 8 group wants to obtain detailed clinical advice and historical infection data on cholera outbreaks from the sub-county public health nurse. Which data collection instrument is most appropriate?",
                            "options": [
                                "An anonymous multiple-choice questionnaire dropped in a suggestion box.",
                                "A structured Interview Guide, because it allows direct spoken conversation to explore complex expert medical explanations in depth.",
                                "An observation schedule counting how many people walk past the hospital gate.",
                                "Writing a complaint letter to the newspaper."
                            ],
                            "correct_index": 1,
                            "explanation": "Interviews are the optimal research instrument for engaging key resource persons and experts, allowing researchers to ask follow-up questions and obtain comprehensive, detailed explanations."
                        }
                    }
                ]
            ]
        },

        # =====================================================================
        # LESSON 3: Project Planning, Resource Management & Reflection
        # =====================================================================
        {
            "unit_order": 3,
            "unit_name": "Project Planning, Resource Management & Reflection",
            "unit_description": "Designing feasible creative solutions, categorizing resources (human, technical, financial), constructing 4-week execution timetables, equitable role assignment, and compiling personal self-reflection growth journals.",
            "lesson_title": "Project Planning, Resource Management & Reflection",
            "pages": [
                # Page 1: Topic Introduction & Visual Hook
                [
                    {
                        "type": "suggested_image",
                        "title": "From Ideas to Action: The Power of Systematic Planning",
                        "content": {
                            "title": "From Ideas to Action: The Power of Systematic Planning",
                            "caption": "Students actively engaged in a tree planting and environmental restoration community project."
                        }
                    },
                    {
                        "type": "learning_goal",
                        "title": "Learning Objectives: Project Planning & Reflection",
                        "content": {
                            "title": "What We Will Learn Today",
                            "goals": [
                                "Categorize project resources across **Human**, **Technical**, and **Financial** bins.",
                                "Construct a realistic **4-week project execution timetable** with defined milestones.",
                                "Apply **financial literacy** by leveraging low-cost improvised materials and entrepreneurship.",
                                "Assign **equitable group roles** and evaluate personal growth using **reflective journals**."
                            ]
                        }
                    },
                    {
                        "type": "concept_explanation",
                        "title": "Why Great Projects Require Detailed Plans",
                        "content": {
                            "title": "Turning Visions into Reality",
                            "text": "A great idea without a structured plan is just a dream!\n\nIn the real world, community projects succeed when groups establish clear schedules, budget resources wisely, divide labor according to individual talents, and reflect on their progress.\n\nLearning how to manage budgets, set deadlines, and lead teams builds essential life and career skills for future nation builders."
                        }
                    }
                ],
                # Page 2: Categorizing Project Resources (Human, Technical, Financial)
                [
                    {
                        "type": "suggested_diagram",
                        "title": "The 3 Project Resource Bins: Human, Technical, and Financial",
                        "content": {
                            "title": "The 3 Project Resource Bins: Human, Technical, and Financial",
                            "caption": "Pantry shelf displaying three distinct color-coded resource bins: Human (Skills/Labor), Technical (Tools/Devices), and Financial (Money/Materials)."
                        }
                    },
                    {
                        "type": "comparison_table",
                        "title": "The 3 Project Resource Categories",
                        "content": {
                            "title": "Systematic Resource Inventory Breakdown",
                            "headers": ["Resource Category", "What It Includes", "Real-World Project Examples", "How to Secure It Affordably"],
                            "rows": [
                                ["Human Resources", "People, individual talents, specialized advice, physical labor", "Group members, class teacher, local health officer, village carpenter", "Volunteer labor, seeking free mentorship from community elders"],
                                ["Technical Resources", "Tools, hardware, digital devices, safety gear, software", "Tablets for photography, shovels, twig brooms, sewing needles, PPE aprons", "Borrowing school equipment, improvising tools from local wood and twigs"],
                                ["Financial Resources", "Money, commercial detergents, seeds, fabrics, transport funds", "Soap powder, tree seedlings, cotton fabric scraps, poster boards", "Using pocket savings, selling needlework crafts, using free wood ash/manure"]
                            ]
                        }
                    }
                ],
                # Page 3: Project Scheduling & 4-Week Timetable Construction
                [
                    {
                        "type": "suggested_diagram",
                        "title": "4-Week Community Project Execution Gantt Roadmap",
                        "content": {
                            "title": "4-Week Community Project Execution Gantt Roadmap",
                            "caption": "Horizontal 4-week timeline showing consecutive milestones: Week 1 Research, Week 2 Tool Sourcing, Week 3 Action, Week 4 Reflection."
                        }
                    },
                    {
                        "type": "step_process",
                        "title": "The 4-Week Project Execution Roadmap",
                        "content": {
                            "title": "Chronological Project Milestones",
                            "steps": [
                                {
                                    "step_number": 1,
                                    "title": "Week 1: Problem Research & Tool Pilot",
                                    "description": "Administer questionnaires to 40 households and interview the local health nurse; analyze data findings."
                                },
                                {
                                    "step_number": 2,
                                    "title": "Week 2: Resource Mobilization & Tool Prep",
                                    "description": "Source improvised brooms, collect wood ash, prepare protective aprons, and draft the execution schedule."
                                },
                                {
                                    "step_number": 3,
                                    "title": "Week 3: Practical Project Action",
                                    "description": "Execute the practical community activity (e.g. deep cleaning market stalls, planting kitchen vegetable gardens)."
                                },
                                {
                                    "step_number": 4,
                                    "title": "Week 4: Reflection & Portfolio Presentation",
                                    "description": "Compile the project photo portfolio, write individual reflection journals, and present results to school assembly."
                                }
                            ]
                        }
                    }
                ],
                # Page 4: Financial Literacy, Improvised Materials & Entrepreneurship
                [
                    {
                        "type": "concept_explanation",
                        "title": "Green Economics and Financial Literacy",
                        "content": {
                            "title": "Zero-Cost Innovation & Value Creation",
                            "text": "- **Financial Literacy**: Smart project managers do not rely on expensive commercial purchases or high parent contributions. They budget conservatively and seek cost-free local substitutes.\n- **Improvised Local Resources**:\n  - Use **sifted wood ash** and **crushed eggshells** instead of expensive commercial scouring chemicals.\n  - Fabricate **brooms from wild grass and sticks** instead of buying plastic factory brooms.\n  - Upcycle **tailoring fabric off-cuts** into soft furnishings, aprons, and table mats.\n- **Entrepreneurship**: Groups can sell excess nursery tree seedlings, vegetables from school sack gardens, or stitched pot holders during sports day to fund their community service activities permanently."
                        }
                    },
                    {
                        "type": "callout",
                        "title": "Financial Wisdom",
                        "content": {
                            "title": "Creativity Beats High Budgets!",
                            "text": "The most celebrated CSL projects in Kenya are those that turn discarded waste (old tyres, plastic bottles, wood ash) into valuable community assets with zero cash expenditure."
                        }
                    }
                ],
                # Page 5: Team Collaboration, Role Division & Personal Reflection
                [
                    {
                        "type": "suggested_diagram",
                        "title": "Team Collaboration, Role Division and Personal Reflective Log",
                        "content": {
                            "title": "Team Collaboration, Role Division and Personal Reflective Log",
                            "caption": "Student team circle showing Leader, Secretary, Treasurer, Resource Coordinator, and Presenter with personal growth reflections."
                        }
                    },
                    {
                        "type": "comparison_table",
                        "title": "Equitable Group Roles and Responsibilities",
                        "content": {
                            "title": "Matching Talents to Group Leadership Duties",
                            "headers": ["Role Title", "Primary Responsibilities", "Ideal Student Profile / Talent", "Personal Growth Outcome"],
                            "rows": [
                                ["Group Leader", "Coordinates group meetings, facilitates plenary debates, resolves disputes", "Diplomatic, encouraging, patient listener", "Grows in team leadership and conflict resolution"],
                                ["Group Secretary", "Records minutes, organizes research files, formats survey forms", "Organized, neat handwriting, detail-oriented", "Develops professional documentation and filing skills"],
                                ["Group Treasurer", "Manages material inventory, tracks project funds, budgets savings", "Strong in mathematics, prudent with money", "Builds practical accounting and financial literacy"],
                                ["Resource Coordinator", "Gathers tools, inspects PPE safety gear, prepares improvised materials", "Practical, handy, knows local community sources", "Grows in logistics and practical problem solving"],
                                ["Lead Presenter", "Speaks on behalf of group at school assemblies, creates display charts", "Articulate, expressive, confident public speaker", "Mastery of public speaking and civic advocacy"]
                            ]
                        }
                    }
                ],
                # Page 6: Hands-On 4-Week CSL Project Planning Activity
                [
                    {
                        "type": "mini_activity",
                        "title": "Hands-On: Constructing Your Group's 4-Week CSL Plan",
                        "content": {
                            "title": "Activity: Build Your Project Master Plan",
                            "instructions": "Working in your 5-member Home Science group:\n\n1. **Elect Roles**: Assign Leader, Secretary, Treasurer, Resource Coordinator, and Presenter based on individual strengths.\n2. **Map Resources**: List 2 Human, 2 Technical, and 2 Financial/improvised resources needed for your project.\n3. **Draw Timetable**: Sketch a 4-week calendar grid in your project binder with specific start and end dates.\n\nHave all group members sign the plan before submitting to your teacher for approval."
                        }
                    }
                ],
                # Page 7: Key Takeaways & Recall Helper
                [
                    {
                        "type": "key_takeaway",
                        "title": "Key Takeaways: Project Planning & Reflection",
                        "content": {
                            "title": "Core Ideas to Remember",
                            "takeaways": [
                                "Project resources are divided into **Human (labor/advice)**, **Technical (tools/devices)**, and **Financial (money/materials)**.",
                                "A **4-week schedule** guarantees structured execution: Research $\\rightarrow$ Tool Sourcing $\\rightarrow$ Action $\\rightarrow$ Reflection.",
                                "**Financial literacy** means budgeting wisely, using improvised materials (wood ash, scrap cloth), and generating small funds through crafts.",
                                "**Self-reflection logs** help learners recognize personal growth in leadership, communication, and civic empathy."
                            ]
                        }
                    },
                    {
                        "type": "memory_tip",
                        "title": "Resource Types Recall Helper",
                        "content": {
                            "title": "Remember 'H-T-F'",
                            "tip": "**H**uman (People & skills) + **T**echnical (Tools & tech) + **F**inancial (Funds & materials)!"
                        }
                    }
                ],
                # Page 8: Knowledge Check
                [
                    {
                        "type": "knowledge_check",
                        "title": "Knowledge Check: Resource Budgeting, Scheduling & Reflection",
                        "content": {
                            "question": "A student group is preparing a CSL project to clean and sanitize their school kitchen. They decide to use sifted firewood ash and crushed eggshells instead of buying commercial chemical powders, and assign tasks according to members' strengths. What principles are they demonstrating?",
                            "options": [
                                "Environmental neglect and disorganized planning.",
                                "Financial literacy, sustainable resource improvisation, and equitable role delegation.",
                                "Avoiding hard work because eggshells don't clean anything.",
                                "Failing to follow school regulations."
                            ],
                            "correct_index": 1,
                            "explanation": "Using local improvised abrasives (wood ash and eggshells) demonstrates financial literacy and green sustainability, while matching group roles to members' talents exemplifies effective collaborative project management."
                        }
                    }
                ]
            ]
        }
    ]

def ingest_cbc_grade8_home_science_topic5(replace=False):
    """Executes the atomic ingestion of CBC Grade 8 Home Science Topic 5."""
    print("=" * 80)
    print("STARTING INGESTION: CBC GRADE 8 HOME SCIENCE — TOPIC 5: CSL CLASS ACTIVITY")
    print("=" * 80)

    # 1. Resolve Curriculum
    curriculum = Curriculum.objects.filter(name__iexact="CBC").first()
    assert curriculum, "Curriculum 'CBC' not found!"
    print(f"[*] Found Curriculum: {curriculum.name} (ID: {curriculum.id})")

    # 2. Resolve Grade 8
    grade = Grade.objects.filter(curriculum=curriculum, name="Grade 8").first()
    assert grade, "Grade 'Grade 8' not found under CBC!"
    print(f"[*] Grade 8: ID {grade.id} (Level {grade.level})")

    # 3. Resolve Subject: Home Science
    subject = Subject.objects.filter(grade=grade, name="Home Science").first()
    assert subject, "Subject 'Home Science' not found under Grade 8!"
    print(f"[*] Subject: {subject.name} (ID {subject.id})")

    # 4. Resolve Topic: Community Service Learning (CSL) Class Activity (Order: 5)
    topic_name = "Community Service Learning (CSL) Class Activity"
    topic = Topic.objects.filter(subject=subject, name=topic_name).first()

    if topic and replace:
        print(f"[*] Found existing Topic '{topic_name}' (ID: {topic.id}). Removing for clean replace...")
        topic.delete()
        topic = None

    if not topic:
        topic = Topic.objects.create(
            subject=subject,
            name=topic_name,
            order=5,
            description="Comprehensive CBC Grade 8 module covering Community Service Learning (CSL) preparation: identifying Pertinent and Contemporary Issues (PCIs), conducting evidence-based community research, designing data collection instruments (questionnaires, interviews, observation schedules), budgeting human/technical/financial resources, 4-week timetable scheduling, equitable role delegation, and self-reflective learning logs."
        )
        print(f"[+] Created Topic: {topic.name} (ID: {topic.id}, Order: {topic.order})")
    else:
        print(f"[*] Using existing Topic: {topic.name} (ID: {topic.id}, Order: {topic.order})")

    curriculum_data = build_topic5_curriculum()
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
                lesson.version = 1
                lesson.save()
            else:
                lesson = Lesson.objects.create(
                    topic=topic,
                    learning_unit=learning_unit,
                    title=lesson_title,
                    status="published",
                    version=1
                )
            print(f"\n  [+] Ingesting Lesson {unit_order}: '{lesson.title}' (Lesson ID: {lesson.id})")

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
            print(f"      [OK] Ingested {lesson_page_count} Pages ({len(lesson.blocks.all())} Blocks) for Unit {unit_order}.")

    print("\n" + "=" * 80)
    print("[SUCCESS] CBC Grade 8 Home Science Topic 5 Ingestion Complete!")
    print(f"[*] Total Lessons Ingested: {total_lessons}")
    print(f"[*] Total Pages Ingested:   {total_pages}")
    print(f"[*] Total Blocks Ingested:  {total_blocks}")
    print("=" * 80)

if __name__ == "__main__":
    replace_flag = "--replace" in sys.argv
    ingest_cbc_grade8_home_science_topic5(replace=replace_flag)
