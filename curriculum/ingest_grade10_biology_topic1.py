"""
VLearn Grade 10 Biology — Topic 1: Cell Biology and Biodiversity
Production Ingestion Engine (Updated Syllabus Structure: 4 Comprehensive Lessons)

Curriculum: CBC (Curriculum ID: 5)
Grade: Grade 10 (Grade ID: 5, Level: 10)
Subject: Biology (Grade 10 CBC)
Topic: Cell Biology and Biodiversity (Topic Order: 1)

Structured into 4 Comprehensive Learning Units & 4 Published Lessons (~50 Concept Cards):
  1. Introduction to Biology (11 Pages)
  2. Scientific Investigations, Specimen Collection, and Preservation (13 Pages)
  3. Cell Structure and Specialization (14 Pages)
  4. Chemicals of Life (14 Pages)

Usage:
  ./venv/bin/python curriculum/ingest_grade10_biology_topic1.py [--replace]
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
    """Removes bracket citations [104, 110], visual prompt text, and cleans double spaces."""
    if not text:
        return ""
    # Remove bracket citations like [104], [101, 102], [image_1]
    text = re.sub(r'\[(?:\d+|image_\d+|S\d+.*?|[\d,\s]+)\]', '', text)
    # Remove internal visual generation tags
    text = re.sub(r'\[VISUAL:\s*[^\]]+\]', '', text, flags=re.IGNORECASE)
    # Normalize unicode bullets into markdown list dashes
    text = re.sub(r'^[ \t]*[•\u2022][ \t]*', '- ', text, flags=re.MULTILINE)
    text = re.sub(r'([^\n])[ \t]+[•\u2022][ \t]+', r'\1\n- ', text)
    text = re.sub(r'^([^\n\-\*\d\>#][^\n]*)\n(- |\* )', r'\1\n\n\2', text, flags=re.MULTILINE)
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

def build_topic1_curriculum():
    """Returns the comprehensive pedagogical page and block structure for Grade 10 Biology Topic 1."""
    return [
        # =====================================================================
        # LESSON 1.1: Introduction to Biology
        # =====================================================================
        {
            "unit_order": 1,
            "unit_name": "Introduction to Biology",
            "unit_description": "Meaning and scope of biology, everyday applications, botany vs zoology, specialized fields, career opportunities, and objective career choices.",
            "lesson_title": "Introduction to Biology",
            "pages": [
                # Page 1: Introduction & Real-World Hook
                [
                    {
                        "type": "learning_goal",
                        "title": "Learning Focus: Introduction to Biology",
                        "content": {
                            "title": "Learning Focus: Introduction to Biology",
                            "goals": [
                                "Define Biology and explain its scope across microscopic and global ecosystem scales.",
                                "Identify and explain the everyday applications of Biology in health, agriculture, food security, and environmental conservation.",
                                "Distinguish between the two broad foundational branches: Botany and Zoology.",
                                "Identify specialized fields of Biology (Taxonomy, Genetics, Microbiology, Parasitology, Entomology, Biochemistry, Anatomy & Physiology).",
                                "Relate specialized biological fields to corresponding professional career opportunities.",
                                "Analyze factors that should (interest, ability) and should not (gender, culture, disability, stereotypes) guide career choices."
                            ]
                        }
                    },
                    {
                        "type": "concept_explanation",
                        "title": "Welcome to Biology: The Science of Life",
                        "content": {
                            "title": "Welcome to Biology: The Science of Life",
                            "text": "Imagine walking through a lush forest on the slopes of Mount Kenya or observing a small garden in your school compound. You see a vibrant world filled with plants, birds, insects, and microorganisms, all interacting with the soil, water, and air.\n\nWhat makes these organisms alive? How do they survive, grow, and adapt? Biology is the key that unlocks these mysteries. It is not just a subject in a textbook; it is the scientific study of yourself and every other living entity on Earth, helping us understand the delicate balance of life."
                        }
                    }
                ],
                # Page 2: Key Terms
                [
                    {
                        "type": "definition_card",
                        "title": "Foundational Biological Vocabulary",
                        "content": {
                            "term": "Essential Terminology",
                            "definition": "Biology is the branch of science that deals with the study of living things and their interactions with the non-living environment.",
                            "key_points": [
                                "Organism: Any individual living entity, ranging from microscopic bacteria to complex multicellular plants and animals.",
                                "Botany: The branch of Biology that deals with the scientific study of plant life.",
                                "Zoology: The branch of Biology that deals with the scientific study of animal life.",
                                "Taxonomy: The science of identifying, naming, and classifying living organisms based on evolutionary relationships.",
                                "Ecology: The study of how organisms interact with each other and their non-living physical environment.",
                                "Biotechnology: The application of biological systems, organisms, or cellular components to develop industrial and medical products."
                            ]
                        }
                    }
                ],
                # Page 3: The Scope and Everyday Applications of Biology
                [
                    {
                        "type": "concept_explanation",
                        "title": "Scope and Everyday Applications of Biology",
                        "content": {
                            "title": "Scope and Everyday Applications of Biology",
                            "text": "Biology is a dynamic science that bridges the microscopic world of cellular molecules to the grand scale of global biomes. Living organisms cannot survive in isolation; they are entirely dependent on their non-living environment (such as water, sunlight, soil gases, and temperature).\n\nOur understanding of biology directly addresses humanity's most critical challenges:"
                        }
                    },
                    {
                        "type": "comparison_table",
                        "title": "Applications of Biological Sciences in Society",
                        "content": {
                            "headers": ["Field of Application", "Biological Mechanisms", "Real-World Societal Impact"],
                            "rows": [
                                ["Medicine & Public Health", "Studying pathogens (viruses, bacteria) to develop vaccines, antibiotics, and surgical techniques", "Protecting human and animal life against infectious epidemics and chronic diseases"],
                                ["Agriculture & Food Security", "Applying genetics, tissue culture, and plant physiology to breed drought-tolerant crops", "Breeding dryland maize, improving livestock yields, and securing reliable food supplies"],
                                ["Environmental Conservation", "Managing wetlands, restoring degraded forests, combating pollution, and monitoring species", "Protecting endangered wildlife (e.g. northern white rhinos) and mitigating climate change"],
                                ["Biotechnology & Industry", "Harnessing microorganisms (yeast, bacteria) for commercial biochemical processes", "Producing foods (bread, yogurt, fermented porridge), biofuels, pharmaceuticals, and industrial enzymes"]
                            ]
                        }
                    }
                ],
                # Page 4: Visualizing Scope (Wikimedia)
                [
                    {
                        "type": "suggested_image",
                        "title": "The Vast Spectrum of Biology: From Ecosystems to Cellular Cultures",
                        "content": {
                            "description": "Side-by-side visual comparison showing a diverse Kenyan savanna ecosystem on the left and a modern laboratory researcher analyzing cellular petri dish cultures on the right.",
                            "caption": "Biology bridges massive, observable terrestrial ecosystems down to microscopic cellular and molecular investigations."
                        }
                    }
                ],
                # Page 5: Major Specialized Fields and Careers
                [
                    {
                        "type": "concept_explanation",
                        "title": "Specialized Fields of Biology & Career Pathways",
                        "content": {
                            "title": "Specialized Fields of Biology & Career Pathways",
                            "text": "While Botany and Zoology represent the two historic pillars of biological science, modern biology overlaps these branches into highly specialized disciplines that align directly with professional careers:"
                        }
                    },
                    {
                        "type": "comparison_table",
                        "title": "Specialized Biological Fields & Professional Careers",
                        "content": {
                            "headers": ["Specialized Field", "Area of Scientific Investigation", "Professional Career Opportunities"],
                            "rows": [
                                ["Taxonomy", "Classifying, identifying, and naming organism species", "Taxonomist, Herbarium Curator, Biodiversity Officer"],
                                ["Genetics", "Heredity, DNA structure, and genetic variation across generations", "Plant Breeder, Forensic DNA Analyst, Genetic Counsellor"],
                                ["Microbiology", "Microscopic life (bacteria, viruses, microscopic fungi)", "Medical Pathologist, Food Safety Officer, Epidemiologist"],
                                ["Parasitology", "Parasites, host relationships, and vector disease transmission", "Veterinary Parasitologist, Public Health Vector Officer"],
                                ["Entomology", "Insect biology, physiology, and ecological roles", "Pest Management Consultant, Agricultural Extension Officer"],
                                ["Biochemistry", "Chemical compounds and metabolic reactions within cells", "Pharmacist, Clinical Biochemist, Industrial Biotechnologist"],
                                ["Anatomy & Physiology", "Physical body structures and metabolic organ system functions", "Medical Doctor, Surgeon, Physiotherapist, Exercise Physiologist"]
                            ]
                        }
                    }
                ],
                # Page 6: Overlapping Fields SVG Diagram
                [
                    {
                        "type": "suggested_diagram",
                        "title": "Overlapping Disciplines and Career Pathways in Biology",
                        "content": {
                            "description": "Venn diagram showing Botany and Zoology intersecting with specialized disciplines (Microbiology, Genetics, Ecology, Anatomy, Physiology, Biotechnology, Parasitology, Entomology, Biochemistry) and connecting to professional career pathways.",
                            "caption": "The multi-disciplinary and overlapping architecture of biological sciences and their professional career pathways."
                        }
                    }
                ],
                # Page 7: Choosing a Biology Career Responsibly
                [
                    {
                        "type": "concept_explanation",
                        "title": "Responsible Career Decision Making in Science",
                        "content": {
                            "title": "Responsible Career Decision Making in Science",
                            "text": "Selecting a future career should be guided by objective, personal alignment rather than external pressures, social myths, or arbitrary stereotypes:"
                        }
                    },
                    {
                        "type": "comparison_table",
                        "title": "Factors Influencing Career Choice",
                        "content": {
                            "headers": ["Decision Factor", "Influence Category", "Scientific & Ethical Evaluation"],
                            "rows": [
                                ["Personal Interest & Passion", "Appropriate Factor (Must Guide You)", "Genuine curiosity sustains lifelong learning, creative problem-solving, and career fulfillment."],
                                ["Academic & Practical Ability", "Appropriate Factor (Must Guide You)", "Aligning your strengths with field/lab requirements ensures competence and excellence."],
                                ["Gender Stereotypes", "Inappropriate Factor (Must Reject)", "False belief that surgery/fieldwork is for males and nursing/botany is for females. Intellectual and surgical capacity are gender-neutral."],
                                ["Cultural Taboos & Myths", "Inappropriate Factor (Must Reject)", "Belief that handling soil, specimens, or dissections is unclean. Modern sterile protocols make biology safe and noble."],
                                ["Physical Disability Biases", "Inappropriate Factor (Must Reject)", "Assuming physical limitations prevent scientific work. Modern laboratories feature accessible adjustable benches, automated pipettes, and digital microscopes."]
                            ]
                        }
                    }
                ],
                # Page 8: Deep Dive Educational Video
                [
                    {
                        "type": "suggested_video",
                        "title": "Deep Dive: Introduction to Biology and Careers in Science",
                        "content": {
                            "description": "Educational lecture exploring the definition, scope, foundational branches, specialized disciplines, and modern career opportunities in biological sciences."
                        }
                    }
                ],
                # Page 9: Common Misconception
                [
                    {
                        "type": "common_misconception",
                        "title": "Misconception: Biology Only Studies Living Things",
                        "content": {
                            "misconception": "Biology only studies living organisms and has nothing to do with non-living things.",
                            "correction": "Living organisms cannot survive in a vacuum; they are completely dependent on their non-living environment (such as water, sunlight, soil gases, and ambient temperature). Ecology, a major branch of Biology, focuses specifically on how living things interact with these abiotic elements. Therefore, studying the non-living environment is a core part of biological science."
                        }
                    }
                ],
                # Page 10: Knowledge Check
                [
                    {
                        "type": "knowledge_check",
                        "title": "Check Your Understanding: Investigating a Crop Disease",
                        "content": {
                            "question": "An outbreak of a mysterious crop disease is causing maize leaves in a Kenyan village to turn yellow, develop dark spots, and rot. Which combination of biological specialists should the local agricultural department send to investigate?",
                            "options": [
                                "An entomologist and a zoologist",
                                "A plant taxonomist and an animal anatomist",
                                "A botanist, a microbiologist, and a plant pathologist",
                                "A biochemist and an ecologist"
                            ],
                            "correct_answer": "C",
                            "explanation": "A botanist understands plant physiology, a microbiologist can identify bacterial or fungal pathogens on the leaves, and a plant pathologist specializes in diagnosing and treating crop diseases, making this the ideal team to solve a crop disease outbreak."
                        }
                    }
                ],
                # Page 11: Summary
                [
                    {
                        "type": "summary",
                        "title": "Lesson Summary: Introduction to Biology",
                        "content": {
                            "title": "Lesson Summary: Introduction to Biology",
                            "points": [
                                "Biology is the scientific study of living organisms and their dynamic interactions with the physical environment.",
                                "Biological science underpins vital solutions in human medicine, agriculture, environmental conservation, and industrial biotechnology.",
                                "Botany (plants) and Zoology (animals) form the two primary pillars, branching into specialized fields like Genetics, Microbiology, and Biochemistry.",
                                "Career choices must be guided by objective interest and capability, rejecting gender stereotypes, cultural myths, and disability biases."
                            ]
                        }
                    }
                ]
            ]
        },

        # =====================================================================
        # LESSON 1.2: Scientific Investigations, Specimen Collection, and Preservation
        # =====================================================================
        {
            "unit_order": 2,
            "unit_name": "Scientific Investigations, Specimen Collection, and Preservation",
            "unit_description": "Biological specimens, collection apparatus (pooter, pitfall trap, sweep net, Tullgren funnel), herbarium construction, animal dry vs wet preservation, financial budgeting, and field safety ethics.",
            "lesson_title": "Scientific Investigations, Specimen Collection, and Preservation",
            "pages": [
                # Page 1: Introduction & Learning Focus
                [
                    {
                        "type": "learning_goal",
                        "title": "Learning Focus: Specimen Collection & Preservation",
                        "content": {
                            "title": "Learning Focus: Specimen Collection & Preservation",
                            "goals": [
                                "Identify and explain the functions of conventional apparatus and materials used for collecting, processing, and preserving specimens.",
                                "Improvise specimen collection apparatus from locally available materials.",
                                "Demonstrate step-by-step techniques to collect, press, dry, mount, label, and store plant specimens to build a herbarium.",
                                "Compare wet and dry preservation techniques for animal specimens.",
                                "Apply ethical guidelines, animal welfare standards, and safety precautions during field investigations.",
                                "Outline a basic project plan and budget using financial literacy skills to design a specimen collection project."
                            ]
                        }
                    },
                    {
                        "type": "concept_explanation",
                        "title": "Evidence in Biological Science: The Specimen",
                        "content": {
                            "title": "Evidence in Biological Science: The Specimen",
                            "text": "To study biology effectively, scientists cannot rely only on textbook drawings—they must examine real-world organisms. The actual living things or representative parts of living things collected for biological study and observation are called **specimens**.\n\nIn this lesson, we explore how to safely, ethically, and cost-effectively collect, process, and preserve plant and animal specimens using both standard and improvised tools."
                        }
                    }
                ],
                # Page 2: Key Terms
                [
                    {
                        "type": "definition_card",
                        "title": "Field Investigation & Preservation Vocabulary",
                        "content": {
                            "term": "Essential Field Terminology",
                            "definition": "Standard tools and scientific protocols used to study and preserve biological organisms.",
                            "key_points": [
                                "Specimen: A whole organism or representative part collected and used for biological study, identification, and experimentation.",
                                "Pooter (Aspirator): A simple double-tubed jar device used for sucking small crawling insects safely from barks or leaves.",
                                "Pitfall Trap: A smooth-walled container buried flush with the soil to capture ground-crawling invertebrates.",
                                "Herbarium: A systematically organized permanent collection of dried, pressed, mounted, and labelled plant specimens used for scientific reference.",
                                "Preservation: Chemical and physical methods used to halt cellular decay and prevent structural damage to collected specimens over time."
                            ]
                        }
                    }
                ],
                # Page 3: Apparatus for Specimen Collection
                [
                    {
                        "type": "comparison_table",
                        "title": "Apparatus for Specimen Collection: Conventional vs Improvised",
                        "content": {
                            "headers": ["Apparatus / Material", "Conventional Field Use", "Improvised Low-Cost Alternative"],
                            "rows": [
                                ["Pooter / Aspirator", "Sucking small crawling insects safely from barks, leaves, or stones", "Constructed from a recycled clear plastic jar, two flexible drinking straws, and a piece of fine mesh gauze"],
                                ["Pitfall Trap", "Trapping crawling insects or small soil-dwelling invertebrates", "A clean plastic bottle or tin can buried flush with soil level, covered with a flat stone on twigs"],
                                ["Sweep Net / Aerial Net", "Catching flying insects from tall vegetation canopy or air", "Constructed from a wire coat hanger loop attached to a wooden broomstick with recycled mosquito netting"],
                                ["Tullgren Funnel", "Extracting tiny soil-dwelling animals from leaf litter using heat and light", "Plastic bottle funnel with wire mesh screen placed over a collection jar under a warm desk lamp"],
                                ["Forceps", "Picking up small, delicate, or stinging specimens without crushing them", "Improvised from split bamboo sticks, carved twigs, or plastic clothes pegs"],
                                ["Secateurs", "Cutting plant twigs, leaves, and stems cleanly without tearing cambium", "Sharp garden shears or clean pocket knife"]
                            ]
                        }
                    }
                ],
                # Page 4: Engineering Schematic SVG (Pooter & Pitfall Trap)
                [
                    {
                        "type": "suggested_diagram",
                        "title": "Mechanical Engineering of Field Tools: Pooter and Pitfall Trap",
                        "content": {
                            "description": "Clear, labeled engineering-style diagram showing the airflow mechanics of a pooter (suction tube with protective internal gauze filter and entry tube pointing to specimen) alongside a soil cross-section of a pitfall trap buried flush with the ground with stone rain cover.",
                            "caption": "Operational mechanics of the pooter aspirator and buried pitfall trap showing safety features and soil positioning."
                        }
                    }
                ],
                # Page 5: Step-by-Step Herbarium Construction
                [
                    {
                        "type": "step_process",
                        "title": "The Six Steps of Botanical Herbarium Construction",
                        "content": {
                            "title": "The Six Steps of Botanical Herbarium Construction",
                            "steps": [
                                {
                                    "step_number": 1,
                                    "title": "Collection",
                                    "description": "Use secateurs to cut leaves, flowers, or small twigs with fruits. Collect only representative samples and place them in polythene bags to prevent wilting."
                                },
                                {
                                    "step_number": 2,
                                    "title": "Pressing",
                                    "description": "Place the plant specimen carefully between sheets of dry blotting paper or old newspapers. Arrange leaves flat to expose both upper (adaxial) and lower (abaxial) surfaces."
                                },
                                {
                                    "step_number": 3,
                                    "title": "Drying",
                                    "description": "Sandwich the specimen under a flat wooden press with heavy weights. Change newspapers every 1-2 days to eliminate moisture and prevent fungal decay."
                                },
                                {
                                    "step_number": 4,
                                    "title": "Mounting",
                                    "description": "Once completely dried and brittle, glue or stitch the specimen onto a clean sheet of stiff, acid-free mounting paper."
                                },
                                {
                                    "step_number": 5,
                                    "title": "Labelling",
                                    "description": "Affix a standardized scientific label in the bottom-right corner recording: common/local name, scientific binomial name, collection date, exact locality/GPS, habitat, and collector's name."
                                },
                                {
                                    "step_number": 6,
                                    "title": "Storage",
                                    "description": "Store finished sheets in dry, sealed, pest-proof cabinets with mothballs (naphthalene) or silica gel desiccant."
                                }
                            ]
                        }
                    }
                ],
                # Page 6: Museum Herbarium Sheet Image
                [
                    {
                        "type": "suggested_image",
                        "title": "Museum-Grade Botanical Herbarium Specimen Sheet",
                        "content": {
                            "description": "High-resolution museum herbarium sheet showing a meticulously pressed flowering plant showing leaves, stem, floral anatomy, and standardized taxonomic metadata in the bottom-right label.",
                            "caption": "A professionally mounted botanical herbarium specimen displaying preserved morphological structures and standard scientific label metadata."
                        }
                    }
                ],
                # Page 7: Animal Specimen Processing and Preservation
                [
                    {
                        "type": "comparison_table",
                        "title": "Animal Specimen Preservation: Dry Pinning vs Wet Liquid Immersion",
                        "content": {
                            "headers": ["Preservation Method", "Target Animal Specimens", "Step-by-Step Technique", "Key Advantage & Safety Rule"],
                            "rows": [
                                ["Dry Pinning", "Hard-bodied insects (beetles, butterflies, grasshoppers, wasps)", "1. Pin fresh specimen through thorax on soft cork board\n2. Spread wings with paper strips\n3. Dry in ventilated box with mothballs", "Preserves 3D chitinous exoskeleton shape. Keep away from museum beetles."],
                                ["Wet Liquid Immersion", "Soft-bodied invertebrates (caterpillars, earthworms, spiders) and small vertebrates", "1. Fix in dilute Formalin (3-5%) to harden tissue\n2. Transfer to sealed jar with 70% Ethanol\n3. Insert waterproof label inside jar", "Ethanol halts bacterial decay and keeps soft organs hydrated without shriveling. Never handle flammable ethanol near flames."]
                            ]
                        }
                    }
                ],
                # Page 8: Project Planning & Financial Literacy Integration
                [
                    {
                        "type": "concept_explanation",
                        "title": "Project Planning & Financial Literacy in Fieldwork",
                        "content": {
                            "title": "Project Planning & Financial Literacy in Fieldwork",
                            "text": "When designing a biological field sampling project, scientists apply core financial literacy and project management principles:\n\n- **Budgeting**: Accurately estimate and record costs for transport, glassware, preservatives, and mounting cards before starting.\n- **Cost Saving via Improvisation**: Actively reduce expenditure by fabricating **improvised collection tools** (nets, pitfall traps, pooters) from clean household recyclable waste instead of purchasing expensive commercial gear.\n- **Resource Scheduling**: Create an organized field itinerary, allocating specific roles (catcher, recorder, preservative handler) to team members to maximize sampling efficiency."
                        }
                    }
                ],
                # Page 9: Practical Investigation: Constructing an Improvised Pooter
                [
                    {
                        "type": "step_process",
                        "title": "Practical Activity: Constructing and Using an Improvised Pooter",
                        "content": {
                            "title": "Practical Activity: Constructing and Using an Improvised Pooter",
                            "steps": [
                                {
                                    "step_number": 1,
                                    "title": "Cap Preparation",
                                    "description": "Bore two snug holes through a clean plastic bottle cap, making them slightly smaller than the straw diameter for an airtight fit."
                                },
                                {
                                    "step_number": 2,
                                    "title": "Attach Gauze Safety Barrier",
                                    "description": "Insert flexible straw A (suction tube) 3 cm into the cap. Securely wrap fine mesh gauze over the internal end with a rubber band to prevent swallowing insects."
                                },
                                {
                                    "step_number": 3,
                                    "title": "Insert Entry Tube & Seal",
                                    "description": "Insert straw B (entry tube) extending 6 cm into the bottle. Seal around holes with modeling clay to ensure an airtight suction chamber."
                                },
                                {
                                    "step_number": 4,
                                    "title": "Field Testing & Sampling",
                                    "description": "Point entry tube B at a small crawling ant on tree bark. Inhale sharply through suction straw A. The ant is drawn safely into the bottle bottom."
                                }
                            ]
                        }
                    }
                ],
                # Page 10: Deep Dive Educational Video
                [
                    {
                        "type": "suggested_video",
                        "title": "Deep Dive: Field Sampling Techniques, Pooters, and Herbarium Curation",
                        "content": {
                            "description": "Field biology video demonstrating ecological sampling apparatus (pooters, pitfall traps, sweep nets) and step-by-step museum herbarium specimen preservation."
                        }
                    }
                ],
                # Page 11: Common Misconception
                [
                    {
                        "type": "common_misconception",
                        "title": "Misconception: Collecting and Killing Large Numbers of Animals",
                        "content": {
                            "misconception": "To study animal specimens scientifically, we must collect and kill as many different animals as possible.",
                            "correction": "Ethical science dictates that we must practice humane handling and minimal collection! Collect only the absolute minimum number of specimens required. Whenever possible, observe animals live in their natural habitat and release them unharmed. Unnecessary killing disrupts local ecosystems and violates biological conservation ethics."
                        }
                    }
                ],
                # Page 12: Knowledge Check
                [
                    {
                        "type": "knowledge_check",
                        "title": "Check Your Understanding: Choosing Animal Preservation Methods",
                        "content": {
                            "question": "A student wants to preserve a soft-bodied caterpillar she found in her backyard for a biology class presentation next month. Which processing and preservation method is most scientifically appropriate?",
                            "options": [
                                "Press the caterpillar between dry newspapers under heavy books for two weeks, then glue it to cardboard.",
                                "Pin the caterpillar immediately onto a soft corkboard and expose it to the sun to dry.",
                                "Place the caterpillar in a sealed specimen bottle filled with 70% Ethanol.",
                                "Keep the caterpillar in a plastic bag with wet soil and seal it tightly."
                            ],
                            "correct_answer": "C",
                            "explanation": "Soft-bodied invertebrates like caterpillars contain high water content and lack a rigid chitinous exoskeleton. If pressed or dried, they shrivel and rot. Wet liquid preservation in 70% ethanol halts bacterial decomposition while maintaining soft internal and external anatomy."
                        }
                    }
                ],
                # Page 13: Summary
                [
                    {
                        "type": "summary",
                        "title": "Lesson Summary: Specimen Collection & Preservation",
                        "content": {
                            "title": "Lesson Summary: Specimen Collection & Preservation",
                            "points": [
                                "Specimens are physical representatives of organisms used for empirical biological investigation.",
                                "Apparatus (pooters, pitfall traps, sweep nets, Tullgren funnels) can be constructed from low-cost recycled materials.",
                                "Herbarium sheets require systematic pressing, rapid drying, and complete scientific label metadata.",
                                "Hard insects are dry-pinned; soft-bodied invertebrates require wet immersion in 70% ethanol.",
                                "Field biology strictly requires minimal collection ethics and humane animal handling."
                            ]
                        }
                    }
                ]
            ]
        },

        # =====================================================================
        # LESSON 1.3: Cell Structure and Specialization
        # =====================================================================
        {
            "unit_order": 3,
            "unit_name": "Cell Structure and Specialization",
            "unit_description": "Light vs electron microscopes, temporary slide preparation, cell size calculation (FOV), plant vs animal ultrastructure, specialized cells, and levels of biological organization.",
            "lesson_title": "Cell Structure and Specialization",
            "pages": [
                # Page 1: Introduction & Learning Focus
                [
                    {
                        "type": "learning_goal",
                        "title": "Learning Focus: Cell Structure & Specialization",
                        "content": {
                            "title": "Learning Focus: Cell Structure & Specialization",
                            "goals": [
                                "Differentiate between light and electron microscopes based on illumination, magnification, resolution, specimen state, and vacuum requirements.",
                                "Prepare temporary specimen slides, stain them correctly, and observe them under a light microscope.",
                                "Estimate cell size in micrometers using the field of view method.",
                                "Describe the structure and functions of plant and animal cell organelles as observed under an electron microscope.",
                                "Compare plant and animal cells, highlighting structural similarities and differences.",
                                "Relate structural adaptations of specialized cells (root hair, palisade, guard, red blood, sperm) to their specific functions.",
                                "Explain the levels of biological organization from organelles up to multicellular organisms."
                            ]
                        }
                    },
                    {
                        "type": "concept_explanation",
                        "title": "The Microscopic Building Blocks of Life: Cells",
                        "content": {
                            "title": "The Microscopic Building Blocks of Life: Cells",
                            "text": "If you look at a giant, towering eucalyptus tree or a running cheetah, it is hard to believe they have anything in common. Yet, under the lens of a microscope, we discover they are both built from the exact same microscopic building blocks: **cells**.\n\nThe cell is the fundamental structural and functional unit of all life. In this lesson, we step into the microscopic world to compare microscopes, prepare live plant slides, explore organelle ultrastructure, and trace how specialized cells cooperate to build complex living organisms."
                        }
                    }
                ],
                # Page 2: Key Terms
                [
                    {
                        "type": "definition_card",
                        "title": "Cytology & Microscopy Vocabulary",
                        "content": {
                            "term": "Essential Cellular Terminology",
                            "definition": "Key concepts in cytology and optical instrumentation.",
                            "key_points": [
                                "Magnification: The number of times an image is enlarged compared to the actual physical size of the specimen.",
                                "Resolution (Resolving Power): The ability of an optical system to distinguish two separate adjacent points as distinct entities.",
                                "Temporary Slide (Wet Mount): A specimen mounted in water or stain with a coverslip for short-term microscopic observation.",
                                "Organelle: A specialized membrane-bound sub-cellular structure suspended in cytoplasm that carries out specific metabolic jobs.",
                                "Specialized Cell: A cell that has undergone differentiation, modifying its shape and organelles to perform a dedicated physiological function."
                            ]
                        }
                    }
                ],
                # Page 3: Differentiating Light and Electron Microscopes
                [
                    {
                        "type": "comparison_table",
                        "title": "Light Microscope vs Electron Microscope",
                        "content": {
                            "headers": ["Feature / Parameter", "Compound Light Microscope", "Transmission / Scanning Electron Microscope"],
                            "rows": [
                                ["Illumination Source", "Visible light rays (~400–700 nm wavelength)", "Focused high-velocity beam of electrons (~0.005 nm wavelength)"],
                                ["Lenses Used", "Curved optical glass lenses", "Electromagnetic coils (solenoid lenses)"],
                                ["Maximum Magnification", "Up to ~1,500×", "Up to ~500,000× to 2,000,000×"],
                                ["Resolving Limit", "~0.2 µm (200 nm) — limited by light wavelength", "~0.0002 µm (0.2 nm) — reveals molecular and organelle details"],
                                ["Specimen State", "Can examine living or dead cells in natural color", "Only dead, dehydrated, heavy-metal stained specimens in a high vacuum"],
                                ["Portability & Cost", "Affordable, lightweight, portable, simple preparation", "Extremely expensive, large floor-standing units, requires expert operation"]
                            ]
                        }
                    }
                ],
                # Page 4: Step-by-Step Temporary Slide Preparation
                [
                    {
                        "type": "step_process",
                        "title": "Protocol: Preparing a Temporary Wet Mount (Onion Epidermis)",
                        "content": {
                            "title": "Protocol: Preparing a Temporary Wet Mount (Onion Epidermis)",
                            "steps": [
                                {
                                    "step_number": 1,
                                    "title": "Peeling",
                                    "description": "Use forceps to peel a thin, transparent layer of epidermis from the fleshy inner scale leaf of an onion bulb."
                                },
                                {
                                    "step_number": 2,
                                    "title": "Mounting",
                                    "description": "Place the flat epidermal peel smoothly on a clean glass slide and add a drop of water to keep it hydrated."
                                },
                                {
                                    "step_number": 3,
                                    "title": "Staining",
                                    "description": "Add a drop of Iodine solution. Iodine selectively stains cell walls, cytoplasm, and nuclei yellow-brown, dramatically enhancing optical contrast."
                                },
                                {
                                    "step_number": 4,
                                    "title": "45° Coverslip Placement",
                                    "description": "Rest a glass coverslip at a 45-degree angle on the liquid edge and lower it slowly with a mounted needle to eliminate obstructive air bubbles."
                                },
                                {
                                    "step_number": 5,
                                    "title": "Microscopic Focusing",
                                    "description": "Focus first under low power using the coarse adjustment knob, then switch to high power and refine image sharpness with the fine adjustment knob."
                                }
                            ]
                        }
                    }
                ],
                # Page 5: Onion Epidermis Micrograph Image
                [
                    {
                        "type": "suggested_image",
                        "title": "Onion Epidermal Cells Stained with Iodine under Light Microscope",
                        "content": {
                            "description": "High-clarity light micrograph of onion epidermal cells stained with iodine at 400x magnification, displaying rectangular cellulose cell walls, cytoplasm, and distinct stained nuclei.",
                            "caption": "Light micrograph of onion epidermal cells at 400x magnification revealing rigid rectangular cell walls, cytoplasm, and dark stained nuclei."
                        }
                    }
                ],
                # Page 6: Estimating Cell Size in Micrometers
                [
                    {
                        "type": "step_process",
                        "title": "Method: Calculating Microscopic Cell Size Using Field of View (FOV)",
                        "content": {
                            "title": "Method: Calculating Microscopic Cell Size Using Field of View (FOV)",
                            "steps": [
                                {
                                    "step_number": 1,
                                    "title": "Measure FOV Diameter",
                                    "description": "Place a transparent plastic millimeter ruler on the stage under low power. If 3 mm span the circular view, your FOV is 3 mm."
                                },
                                {
                                    "step_number": 2,
                                    "title": "Convert mm to Micrometers",
                                    "description": "Multiply by 1,000 ($1\\text{ mm} = 1,000\\ \\mu\\text{m}$):\n$$3\\text{ mm} \\times 1,000 = 3,000\\ \\mu\\text{m}$$"
                                },
                                {
                                    "step_number": 3,
                                    "title": "Count Cells Across Diameter",
                                    "description": "Place your prepared specimen slide on the stage. Count the number of cells aligned lengthwise end-to-end across the diameter (e.g. 10 cells)."
                                },
                                {
                                    "step_number": 4,
                                    "title": "Calculate Cell Length",
                                    "description": "Apply the cell size formula:\n$$\\text{Cell Size} = \\frac{\\text{Diameter of Field of View}}{\\text{Number of Cells}} = \\frac{3,000\\ \\mu\\text{m}}{10\\text{ cells}} = 300\\ \\mu\\text{m}$$"
                                }
                            ]
                        }
                    }
                ],
                # Page 7: Electron Microscope Organelles and Functions
                [
                    {
                        "type": "comparison_table",
                        "title": "Organelles: Structure, Adaptations, and Metabolic Functions",
                        "content": {
                            "headers": ["Organelle", "Structural Characteristics", "Metabolic Function & Adaptation"],
                            "rows": [
                                ["Nucleus", "Double nuclear membrane with pores, containing chromatin DNA and nucleolus", "Directs all cellular metabolic activities and houses genetic hereditary code"],
                                ["Mitochondrion", "Rod-shaped double membrane; inner membrane folded into finger-like cristae", "Site of aerobic respiration; folded cristae maximize surface area for ATP generation enzymes"],
                                ["Chloroplast", "Double membrane; thylakoids stacked into grana suspended in stroma", "Site of photosynthesis; chlorophyll in grana traps light; stroma synthesizes glucose"],
                                ["Ribosomes", "Tiny non-membrane bound granules made of ribosomal RNA and protein", "Sites of protein synthesis; translates mRNA into polypeptide chains"],
                                ["Endoplasmic Reticulum (ER)", "Membrane network: Rough ER studded with ribosomes; Smooth ER tubular", "Rough ER transports synthesized proteins; Smooth ER synthesizes lipids and steroid hormones"],
                                ["Golgi Apparatus", "Stacks of flattened membrane-bound cisternae producing secretory vesicles", "Chemically modifies, sorts, packages, and secretes cellular proteins and enzymes"],
                                ["Lysosomes", "Spherical vesicles containing powerful hydrolytic digestive enzymes", "Breaks down worn-out cellular organelles, cellular debris, and engulfed pathogens"],
                                ["Cell Wall (Plants Only)", "Rigid, non-living outer layer composed of tough cellulose microfibrils", "Provides mechanical support, maintains plant cell turgor, and prevents osmotic lysis"]
                            ]
                        }
                    }
                ],
                # Page 8: Eukaryotic Cell Ultrastructure SVG Diagram
                [
                    {
                        "type": "suggested_diagram",
                        "title": "Detailed Ultrastructure: Plant Cell vs. Animal Cell",
                        "content": {
                            "description": "Side-by-side comparative diagrams of a plant cell and an animal cell as seen under an electron microscope, highlighting cellulose cell wall, chloroplasts with grana stacks, large central vacuole, mitochondria with cristae, nucleus, ER, Golgi, centrioles, and lysosomes.",
                            "caption": "Ultrastructure comparison between eukaryotic plant cells (rigid wall, chloroplasts, central vacuole) and animal cells (flexible membrane, centrioles, small vacuoles)."
                        }
                    }
                ],
                # Page 9: Adaptations of Specialized Cells
                [
                    {
                        "type": "comparison_table",
                        "title": "Structure-to-Function Adaptations of Specialized Cells",
                        "content": {
                            "headers": ["Specialized Cell", "Tissue / Location", "Major Structural Adaptation", "Physiological Function"],
                            "rows": [
                                ["Root Hair Cell", "Root epidermis (Plant)", "Long, slender hair-like lateral extension; thin wall, large vacuole", "Vastly increases surface area for rapid absorption of water (osmosis) and mineral ions (active transport)"],
                                ["Palisade Mesophyll Cell", "Upper leaf mesophyll (Plant)", "Tightly packed columnar cells packed with dense chloroplasts", "Maximizes sunlight capture for photosynthesis; columnar shape allows deep light penetration"],
                                ["Guard Cell", "Leaf epidermis (Plant)", "Bean-shaped with unevenly thickened walls (thick inner, thin outer wall)", "Controls opening and closing of stomatal pores to regulate gas exchange and transpiration"],
                                ["Red Blood Cell (Erythrocyte)", "Bloodstream (Animal)", "Biconcave disc shape, flexible membrane, lacks nucleus when mature", "Biconcave shape maximizes surface-area-to-volume ratio; lack of nucleus provides maximum space for oxygen-carrying hemoglobin"],
                                ["Sperm Cell", "Testes / Semen (Animal)", "Streamlined head with acrosome enzymes, midpiece packed with mitochondria, long flagellum tail", "Acrosome digests outer egg coat; mitochondria generate ATP to power flagellar swimming to ovum"]
                            ]
                        }
                    }
                ],
                # Page 10: Levels of Biological Organization
                [
                    {
                        "type": "step_process",
                        "title": "The Structural Hierarchy of Life",
                        "content": {
                            "title": "The Structural Hierarchy of Life",
                            "steps": [
                                {
                                    "step_number": 1,
                                    "title": "Organelle",
                                    "description": "Sub-cellular specialized compartment performing a metabolic task (e.g. Mitochondrion, Chloroplast)."
                                },
                                {
                                    "step_number": 2,
                                    "title": "Cell",
                                    "description": "The fundamental structural and functional unit of life (e.g. Palisade mesophyll cell, Cardiac muscle cell)."
                                },
                                {
                                    "step_number": 3,
                                    "title": "Tissue",
                                    "description": "A group of similar specialized cells integrated to execute a common function (e.g. Palisade mesophyll tissue, Muscular tissue)."
                                },
                                {
                                    "step_number": 4,
                                    "title": "Organ",
                                    "description": "A distinct structure composed of different coordinated tissues performing a major bodily function (e.g. Leaf, Heart)."
                                },
                                {
                                    "step_number": 5,
                                    "title": "Organ System",
                                    "description": "A group of organs cooperating to carry out comprehensive life functions (e.g. Shoot system, Circulatory system)."
                                },
                                {
                                    "step_number": 6,
                                    "title": "Organism",
                                    "description": "A complete, individual living entity capable of independent survival (e.g. Maize plant, Human being)."
                                }
                            ]
                        }
                    }
                ],
                # Page 11: Deep Dive Educational Video
                [
                    {
                        "type": "suggested_video",
                        "title": "Deep Dive: Eukaryotic Cell Structure, Organelles, and Microscopy",
                        "content": {
                            "description": "Comprehensive video exploration of eukaryotic plant and animal cell ultrastructure, organelle adaptations, and optical light microscopy techniques."
                        }
                    }
                ],
                # Page 12: Common Misconception
                [
                    {
                        "type": "common_misconception",
                        "title": "Misconception: Plant Cells Do Not Need Mitochondria",
                        "content": {
                            "misconception": "Animal cells have mitochondria to perform respiration, but plant cells do not need mitochondria because they have chloroplasts.",
                            "correction": "Plant cells absolutely contain mitochondria and must perform cellular respiration day and night to stay alive! While chloroplasts capture solar energy to manufacture glucose during the day, plant cells must still use mitochondria to break down that glucose and release usable ATP energy for growth and active transport."
                        }
                    }
                ],
                # Page 13: Knowledge Check
                [
                    {
                        "type": "knowledge_check",
                        "title": "Check Your Understanding: Identifying Organelles in Specialized Cells",
                        "content": {
                            "question": "A plant biologist isolates a cell from a plant and observes that it contains an extremely high density of mitochondria but has no chloroplasts. Which of the following is the most likely identity of this cell?",
                            "options": [
                                "A palisade mesophyll cell",
                                "An epidermal guard cell",
                                "An active root hair absorption cell",
                                "A xylem vessel element"
                            ],
                            "correct_answer": "C",
                            "explanation": "Root hair cells are located underground in the soil where there is no sunlight, so they do not have chloroplasts and cannot photosynthesize. However, they absorb dissolved mineral salts against concentration gradients from the soil via active transport—a process demanding continuous ATP energy provided by densely packed mitochondria."
                        }
                    }
                ],
                # Page 14: Summary
                [
                    {
                        "type": "summary",
                        "title": "Lesson Summary: Cell Structure & Organization",
                        "content": {
                            "title": "Lesson Summary: Cell Structure & Organization",
                            "points": [
                                "Light microscopes use glass lenses and light to view live cells (~1500×); electron microscopes use electron beams in a vacuum to reveal organelle ultrastructure (~500,000×).",
                                "Temporary wet mounts require thin translucent sectioning, water mounting, iodine staining, and bubble-free 45° coverslip lowering.",
                                "Organelles demonstrate structure-to-function specialization: mitochondria (cristae for ATP), chloroplasts (grana/stroma for photosynthesis), nucleus, ER, and Golgi.",
                                "Cell differentiation produces specialized cells (root hair, palisade, guard, RBC, sperm) structured into 5 ascending organizational tiers: Organelle → Cell → Tissue → Organ → System → Organism."
                            ]
                        }
                    }
                ]
            ]
        },

        # =====================================================================
        # LESSON 1.4: Chemicals of Life
        # =====================================================================
        {
            "unit_order": 4,
            "unit_name": "Chemicals of Life",
            "unit_description": "Biomolecules (carbohydrates, lipids, proteins), vitamins A/C/D/K and deficiency diseases, water and mineral ions, diagnostic food tests, lock-and-key enzyme mechanism, catalase practical, and environmental kinetic curves.",
            "lesson_title": "Chemicals of Life",
            "pages": [
                # Page 1: Introduction & Learning Focus
                [
                    {
                        "type": "learning_goal",
                        "title": "Learning Focus: Chemicals of Life & Enzyme Kinetics",
                        "content": {
                            "title": "Learning Focus: Chemicals of Life & Enzyme Kinetics",
                            "goals": [
                                "Describe the biological composition, properties, and functions of carbohydrates, lipids, proteins, and vitamins in organisms.",
                                "Identify major vitamins (A, C, D, K) and their corresponding deficiency diseases (night blindness, scurvy, rickets, excessive bleeding).",
                                "Explain the biological importance of water and mineral ions (Sodium, Calcium, Iron).",
                                "Conduct laboratory experiments to test for carbohydrates, lipids, proteins, and Vitamin C in food substances.",
                                "Examine food packaging labels to evaluate nutritional safety and quality.",
                                "Explain the properties and mechanisms of action of enzymes as biological catalysts using the Lock-and-Key hypothesis.",
                                "Investigate catalase activity in living tissues and determine factors affecting enzyme rates (temperature, pH, substrate concentration, inhibitors)."
                            ]
                        }
                    },
                    {
                        "type": "concept_explanation",
                        "title": "The Molecular Factory of Life",
                        "content": {
                            "title": "The Molecular Factory of Life",
                            "text": "Every living cell is a complex biochemical factory. The growth, cellular repair, energy generation, and responses of organisms are coordinated by organic and inorganic compounds called the **chemicals of life**.\n\nIn this lesson, we explore the macromolecules that build cells (carbohydrates, lipids, proteins, vitamins), the vital roles of water and mineral salts, standard diagnostic food tests, and the protein catalysts called **enzymes** that drive all metabolic life processes."
                        }
                    }
                ],
                # Page 2: Key Terms
                [
                    {
                        "type": "definition_card",
                        "title": "Biochemistry & Enzymology Vocabulary",
                        "content": {
                            "term": "Essential Biochemical Terminology",
                            "definition": "Key concepts in biological chemistry and enzyme action.",
                            "key_points": [
                                "Carbohydrate: An organic biomolecule composed of Carbon, Hydrogen, and Oxygen in a 1:2:1 ratio, acting as the primary source of cellular energy.",
                                "Enzyme: A globular protein molecule acting as a biological catalyst that speeds up metabolic reactions without being consumed.",
                                "Catalase: An intracellular enzyme abundant in living tissues (liver, potato) that rapidly breaks down toxic metabolic hydrogen peroxide into water and oxygen.",
                                "Active Site: The specific 3D cleft on an enzyme's protein surface where substrate molecules bind to undergo chemical reactions.",
                                "Denaturation: The permanent, irreversible alteration of an enzyme's tertiary protein shape caused by extreme heat or pH, destroying its active site."
                            ]
                        }
                    }
                ],
                # Page 3: Biomolecules and Vitamins Matrix
                [
                    {
                        "type": "comparison_table",
                        "title": "Major Biomolecules & Essential Vitamins",
                        "content": {
                            "headers": ["Nutrient / Vitamin", "Constituent Elements / Rich Food Sources", "Biological Function in Cells", "Deficiency Disease & Symptoms"],
                            "rows": [
                                ["Carbohydrates", "C, H, O (Monosaccharides: glucose; Polysaccharides: starch, glycogen)", "Primary immediate source of cellular ATP energy; cellulose builds rigid cell walls", "Marasmus (general calorie starvation, extreme emaciation)"],
                                ["Lipids (Fats & Oils)", "C, H, O (Glycerol + 3 fatty acid chains; butter, vegetable oils)", "High-density energy storage, cell membrane phospholipids, subcutaneous thermal insulation", "Weight loss, lack of insulation, impaired fat-soluble vitamin absorption"],
                                ["Proteins", "C, H, O, N (often S, P; amino acid polymers in meat, beans, eggs)", "Growth, tissue repair, enzyme catalysts, antibodies, structural collagen and keratin", "Kwashiorkor (protein deficiency with swollen abdomen/oedema, wasted muscles)"],
                                ["Vitamin A (Retinol)", "Carrots, spinach, sweet potatoes, liver, egg yolk", "Forms rhodopsin visual pigment in retina for low-light vision; maintains epithelial tissue", "**Night Blindness**: Inability to see clearly in dim light; xerophthalmia (dry cornea)"],
                                ["Vitamin C (Ascorbic Acid)", "Citrus fruits (oranges, lemons), guavas, fresh tomatoes", "Essential for collagen synthesis, capillary strength, wound healing, and immunity", "**Scurvy**: Bleeding swollen gums, fragile capillaries, loose teeth, delayed wound healing"],
                                ["Vitamin D (Calciferol)", "Fish liver oil, egg yolks, synthesized in skin exposed to sunlight", "Promotes intestinal absorption of Calcium and Phosphorus to mineralize bones and teeth", "**Rickets**: Soft, weak, bow-legged bones in children; osteomalacia in adults"],
                                ["Vitamin K (Phylloquinone)", "Dark green leafy vegetables (sukumawiki/spinach), cabbage", "Essential co-factor for liver synthesis of prothrombin clotting factors", "**Excessive Bleeding (Haemorrhage)**: Impaired, delayed blood clotting after injury"]
                            ]
                        }
                    }
                ],
                # Page 4: Water and Mineral Salts
                [
                    {
                        "type": "comparison_table",
                        "title": "Water & Essential Mineral Ions in Cellular Physiology",
                        "content": {
                            "headers": ["Inorganic Substance", "Key Dietary Sources", "Physiological Functions in Cells", "Deficiency Disorder"],
                            "rows": [
                                ["Water ($H_2O$)", "Drinking water, fruits, metabolic water", "Universal cellular solvent, circulatory transport vehicle (blood/sap), evaporative cooling (sweat/transpiration), hydrostatic plant support", "Dehydration, circulatory failure, wilting in plants"],
                                ["Sodium ($Na^+$)", "Table salt ($NaCl$), seafood, dairy, cured meats", "Maintains cellular osmotic fluid balance; essential for electrical nerve impulse conduction and muscle contraction", "Muscle cramps, dehydration, lethargy, low blood pressure, nervous dysfunction"],
                                ["Calcium ($Ca^{2+}$)", "Milk, cheese, small whole fish (omena), dark green vegetables", "Forms structural calcium phosphate in bones and teeth; required for blood clotting cascade and muscle contraction", "**Rickets** in children, **osteoporosis** (brittle bones) in adults, tetany (muscle spasms)"],
                                ["Iron ($Fe^{2+}$)", "Red meat, liver, kidney, dark green leafy vegetables, legumes", "Forms the central metallic core of **hemoglobin** in erythrocytes, binding oxygen for transport", "**Nutritional Anaemia**: Reduced hemoglobin, pale conjunctiva, chronic fatigue, breathlessness on exertion"]
                            ]
                        }
                    }
                ],
                # Page 5: Qualitative Food Tests Summary Table
                [
                    {
                        "type": "comparison_table",
                        "title": "Laboratory Protocol for Diagnostic Qualitative Food Tests",
                        "content": {
                            "headers": ["Target Nutrient", "Diagnostic Chemical Reagent", "Initial Reagent Color", "Positive Test Result", "Crucial Laboratory Conditions"],
                            "rows": [
                                ["Starch", "Iodine solution", "Yellow-brown", "**Blue-black** coloration", "Add drops directly to solid or cold liquid sample; no heating"],
                                ["Reducing Sugars (e.g. Glucose)", "Benedict's solution", "Light blue", "Green -> Yellow -> Orange -> **Brick-red precipitate**", "Add equal volume of Benedict's; boil in water bath for 5 minutes"],
                                ["Proteins", "Biuret reagent (10% NaOH + 1% CuSO4)", "Pale blue", "**Purple / Violet** coloration", "Add NaOH then drops of dilute CuSO4; mix cold without heating"],
                                ["Lipids (Fats & Oils)", "Ethanol Emulsion test", "Clear colorless", "**Cloudy white emulsion layer**", "Dissolve sample in ethanol, shake thoroughly, decant into cold water; KEEP AWAY FROM FLAMES"],
                                ["Vitamin C (Ascorbic Acid)", "DCPIP solution", "Deep blue", "**Decolorizes (turns completely clear/colorless)**", "Add sample juice drop-by-drop to 1 ml of DCPIP without heating"]
                            ]
                        }
                    }
                ],
                # Page 6: Photographic Food Test Results
                [
                    {
                        "type": "suggested_image",
                        "title": "Positive Diagnostic Color Results in Food Testing",
                        "content": {
                            "description": "Laboratory test tubes side-by-side displaying distinct positive food test reactions: Benedict's solution turning from blue into a dense brick-red precipitate in the presence of reducing sugars.",
                            "caption": "Diagnostic color transitions in biochemical food testing: Benedict's reduction reaction indicating reducing sugars."
                        }
                    }
                ],
                # Page 7: Enzymes and Catalase Activity
                [
                    {
                        "type": "concept_explanation",
                        "title": "Enzymes: Biological Catalysts & Catalase Mechanics",
                        "content": {
                            "title": "Enzymes: Biological Catalysts & Catalase Mechanics",
                            "text": "Inside cells, chemical reactions must occur at lightning speed without extreme heat. Cells rely on protein catalysts called **enzymes**.\n\nEnzymes operate via the **Lock and Key Hypothesis**: the substrate molecule (the key) has a complementary 3D shape that fits precisely into the active site of the enzyme (the lock). The enzyme forms a temporary enzyme-substrate complex, lowers activation energy, converts substrate to products, and releases them unchanged.\n\n**Catalase** is a vital protective enzyme in living tissues. During cellular respiration, cells produce toxic **hydrogen peroxide ($H_2O_2$)**. Catalase detoxifies it immediately:\n$$2\\text{H}_2\\text{O}_2 \\xrightarrow{\\text{Catalase}} 2\\text{H}_2\\text{O} + \\text{O}_2\\text{ (gas)}$$"
                        }
                    }
                ],
                # Page 8: Factors Affecting Enzyme Activity
                [
                    {
                        "type": "concept_explanation",
                        "title": "Environmental Factors Governing Enzyme Velocity",
                        "content": {
                            "title": "Environmental Factors Governing Enzyme Velocity",
                            "text": "Enzyme velocity is governed by environmental physical and chemical conditions:\n\n1. **Temperature**: Rate rises with temperature due to increased molecular kinetic collisions until reaching the **optimum temperature** (~$37^\circ\\text{C}$ in humans). Beyond optimum, intense thermal vibration breaks hydrogen bonds, causing **denaturation**—the active site permanently loses its complementary shape.\n2. **pH**: Enzymes possess a specific **optimum pH** (e.g. Pepsin at pH 2 in the acidic stomach; Salivary Amylase at pH 7; Trypsin at pH 8 in the alkaline duodenum). Extreme pH changes alter ionic charges on active site amino acids, causing denaturation.\n3. **Substrate Concentration**: As substrate increases, more active sites are occupied and rate rises linearly until reaching the **maximum velocity ($V_{max}$)**, where all active sites are saturated and the curve plateaus.\n4. **Inhibitors**: **Competitive inhibitors** resemble substrate and block active sites; **Non-competitive inhibitors** (lead, cyanide) bind elsewhere on the enzyme, permanently warping the active site shape."
                        }
                    }
                ],
                # Page 9: Multi-Panel Enzyme Kinetics Charts SVG
                [
                    {
                        "type": "suggested_diagram",
                        "title": "Lock-and-Key Mechanism and Enzyme Activity Kinetics Graphs",
                        "content": {
                            "description": "Multi-panel chart illustrating: 1. The Lock-and-Key enzyme catalysis mechanism. 2. Rate vs Temperature curve showing rise to 37C optimum and sharp denaturation drop to zero. 3. Rate vs pH bell curves contrasting Pepsin (pH 2) and Amylase (pH 7). 4. Rate vs Substrate Concentration showing saturation plateau at Vmax.",
                            "caption": "Lock-and-key active site binding mechanism and kinetic response curves to temperature, pH, and substrate concentration."
                        }
                    }
                ],
                # Page 10: Practical Investigation: Testing Factors Affecting Catalase Activity
                [
                    {
                        "type": "step_process",
                        "title": "Practical Activity: Investigating Catalase Activity and Thermal Denaturation",
                        "content": {
                            "title": "Practical Activity: Investigating Catalase Activity and Thermal Denaturation",
                            "steps": [
                                {
                                    "step_number": 1,
                                    "title": "Prepare Liver Samples",
                                    "description": "Cut two equal-sized cubes ($1\\text{ cm}^3$ each) of fresh chicken/beef liver (rich in active catalase)."
                                },
                                {
                                    "step_number": 2,
                                    "title": "Boil Tube B Sample",
                                    "description": "Place Cube 1 into Test Tube A at room temperature. Boil Cube 2 in boiling water for 5 minutes, let it cool, and place it into Test Tube B."
                                },
                                {
                                    "step_number": 3,
                                    "title": "Add Hydrogen Peroxide",
                                    "description": "Add 5 ml of dilute hydrogen peroxide ($3\\%\\ H_2O_2$) solution to both test tubes simultaneously."
                                },
                                {
                                    "step_number": 4,
                                    "title": "Observe & Test with Glowing Splint",
                                    "description": "Tube A shows vigorous effervescence; a glowing wooden splint held over the mouth relights, confirming Oxygen ($O_2$) gas. Tube B shows zero bubbling."
                                }
                            ]
                        }
                    },
                    {
                        "type": "callout",
                        "title": "Scientific Explanation of Results",
                        "content": {
                            "title": "Scientific Explanation of Results",
                            "text": "Raw liver in Tube A contains active, intact catalase enzymes that rapidly break down hydrogen peroxide into water and oxygen gas. In Tube B, boiling at $100^\\circ\\text{C}$ provided excessive thermal kinetic energy that ruptured the protein's hydrogen bonds, permanently **denaturing** the enzyme's active site so no catalytic reaction could occur."
                        }
                    }
                ],
                # Page 11: Deep Dive Educational Video
                [
                    {
                        "type": "suggested_video",
                        "title": "Deep Dive: Enzymes, Catalase Breakdown, and Biochemical Food Tests",
                        "content": {
                            "description": "Laboratory demonstration video detailing enzyme kinetics, lock-and-key catalysis, catalase hydrogen peroxide breakdown, and standard food testing reagents."
                        }
                    }
                ],
                # Page 12: Common Misconception
                [
                    {
                        "type": "common_misconception",
                        "title": "Misconception: Freezing Denatures Enzymes Like Boiling Does",
                        "content": {
                            "misconception": "Freezing cold temperatures denature enzymes in the same way that boiling heat does.",
                            "correction": "Freezing cold temperatures DO NOT denature enzymes! Cold simply reduces the kinetic energy of molecules, causing them to move very sluggishly and drastically reducing collisions with active sites. This temporarily inactivates the enzyme. If you warm the enzyme back up to its optimum temperature, full activity is restored. Heat permanently denatures; cold merely temporarily inactivates."
                        }
                    }
                ],
                # Page 13: Knowledge Check
                [
                    {
                        "type": "knowledge_check",
                        "title": "Check Your Understanding: Diagnosing Vitamin & Mineral Deficiencies",
                        "content": {
                            "question": "A child living in an informal settlement in Nairobi is brought to a clinic. The doctor observes that the child's legs are noticeably bowed outward, and his wrists are swollen. Upon examining his diet, the doctor finds he rarely eats eggs, fish, or dairy, and spends almost all day indoors. Which vitamin and mineral deficiency is this child most likely suffering from?",
                            "options": [
                                "Vitamin C and Iron",
                                "Vitamin D and Calcium",
                                "Vitamin A and Sodium",
                                "Vitamin K and Calcium"
                            ],
                            "correct_answer": "B",
                            "explanation": "Bowed legs and swollen joints in children are classic hallmarks of Rickets, caused by deficiency in Vitamin D or Calcium. Vitamin D is required for intestinal absorption of calcium to mineralize rigid bone matrix. Lacking sunlight exposure (to synthesize Vitamin D) and dairy (calcium) causes bones to remain soft and bow under body weight."
                        }
                    }
                ],
                # Page 14: Summary
                [
                    {
                        "type": "summary",
                        "title": "Lesson Summary: Chemicals of Life",
                        "content": {
                            "title": "Lesson Summary: Chemicals of Life",
                            "points": [
                                "Carbohydrates, lipids, and proteins form the organic structural and energetic matrix of living cells.",
                                "Vitamins (A, C, D, K) and mineral ions ($Na^+, Ca^{2+}, Fe^{2+}$) act as essential metabolic regulators, preventing diseases like scurvy, rickets, and anaemia.",
                                "Diagnostic food tests utilize Iodine (starch), Benedict's with boiling (reducing sugars), Biuret (proteins), Ethanol emulsion (lipids), and DCPIP (Vitamin C).",
                                "Enzymes are specific protein catalysts operating via the Lock-and-Key hypothesis.",
                                "Catalase rapidly converts toxic metabolic $H_2O_2$ into water and oxygen; boiling causes irreversible active site denaturation."
                            ]
                        }
                    }
                ]
            ]
        }
    ]

def ingest_grade10_biology_topic1(replace=False):
    """Executes the database ingestion for Grade 10 Biology Topic 1."""
    print("=" * 80)
    print("VLearn Grade 10 Biology — Ingestion Engine (Updated Syllabus)")
    print("Topic 1: Cell Biology and Biodiversity (CBC Curriculum ID: 5)")
    print("=" * 80)

    # 1. Resolve Curriculum
    curriculum = Curriculum.objects.filter(name="CBC").first() or Curriculum.objects.filter(id=5).first()
    if not curriculum:
        print("[!] Fatal: Curriculum 'CBC' (ID: 5) not found in database!")
        return

    print(f"[*] Curriculum: {curriculum.name} (ID: {curriculum.id})")

    # 2. Resolve Grade
    grade = Grade.objects.filter(curriculum=curriculum, name="Grade 10").first() or Grade.objects.filter(curriculum=curriculum, level=10).first()
    if not grade:
        print("[!] Fatal: Grade 'Grade 10' under CBC not found in database!")
        return

    print(f"[*] Grade: {grade.name} (ID: {grade.id}, Level: {grade.level})")

    # 3. Resolve Subject under Grade 10 CBC (Strict Scope Isolation)
    subject, created = Subject.objects.get_or_create(
        grade=grade,
        name="Biology",
        defaults={"description": "Grade 10 Biology Curriculum under CBC senior secondary science pathway."}
    )
    print(f"[*] Subject: {subject.name} under {grade.name} (ID: {subject.id})")

    # 4. Resolve Topic 1
    topic_name = "Cell Biology and Biodiversity"
    topic = Topic.objects.filter(subject=subject, name=topic_name).first()

    if topic and replace:
        print(f"[*] Found existing Topic '{topic_name}' (ID: {topic.id}). Performing clean replacement of child units/lessons...")
        topic.learning_units.all().delete()
        topic.lessons.all().delete()
    elif not topic:
        topic = Topic.objects.create(
            subject=subject,
            name=topic_name,
            order=1,
            description="Comprehensive syllabus on cell biology, microscopy, organelles, specialized cells, levels of organization, chemicals of life, food tests, and enzyme kinetics."
        )
        print(f"[+] Created Topic: {topic.name} (ID: {topic.id})")
    else:
        print(f"[*] Using existing Topic: {topic.name} (ID: {topic.id})")

    curriculum_data = build_topic1_curriculum()
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

            learning_unit.name = unit_name
            learning_unit.description = unit_desc
            learning_unit.save()

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
            print(f"  [+] Ingesting Lesson {unit_order}: {lesson.title} (Lesson ID: {lesson.id})")

            block_order = 10
            lesson_page_count = len(pages_data)

            for page_idx, page_blocks in enumerate(pages_data, 1):
                first_block_title = page_blocks[0].get("title", f"Concept Card {page_idx}")
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
            print(f"      [OK] Ingested {lesson_page_count} Concept Cards for Lesson {unit_order}.")

    print("=" * 80)
    print("[SUCCESS] Grade 10 Biology Topic 1 Ingestion Complete!")
    print(f"[*] Total Lessons Ingested: {total_lessons}")
    print(f"[*] Total Pages/Cards:      {total_pages}")
    print(f"[*] Total Blocks Created:   {total_blocks}")
    print("=" * 80)

if __name__ == "__main__":
    replace_flag = "--replace" in sys.argv
    ingest_grade10_biology_topic1(replace=replace_flag)
