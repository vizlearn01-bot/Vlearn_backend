"""
VLearn Grade 10 Biology — Topic 8: Animal Nutrition and Feeding Adaptations
Production Ingestion Engine (2 Comprehensive Lessons)

Curriculum: CBC (Curriculum ID: 5)
Grade: Grade 10 (Grade ID: 5, Level: 10)
Subject: Biology (Grade 10 CBC)
Topic: Animal Nutrition and Feeding Adaptations (Topic Order: 8)

Structured into 2 Comprehensive Learning Units & 2 Published Lessons (19 Concept Cards):
  1. Insect Mouthparts and Feeding Adaptations (9 Pages)
  2. Bird Beaks and Feeding Adaptations (10 Pages)

Usage:
  ./venv/bin/python curriculum/ingest_grade10_biology_topic8.py [--replace]
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
    """Removes bracket citations [52, 134], visual prompt text, and cleans double spaces."""
    if not text:
        return ""
    # Remove bracket citations like [52], [52, 134], [image_1]
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

def build_topic8_curriculum():
    """Returns the comprehensive pedagogical page and block structure for Grade 10 Biology Topic 8."""
    return [
        # =====================================================================
        # LESSON 8.1: Insect Mouthparts and Feeding Adaptations
        # =====================================================================
        {
            "unit_order": 1,
            "unit_name": "Insect Mouthparts and Feeding Adaptations",
            "unit_description": "Mechanical architecture of five insect mouthparts (biting/chewing, piercing/sucking, siphoning, cutting/lapping, sponging), dietary adaptations, and public health vector roles.",
            "lesson_title": "Insect Mouthparts and Feeding Adaptations",
            "pages": [
                # Page 1: Introduction & Learning Focus
                [
                    {
                        "type": "learning_goal",
                        "title": "Learning Focus: Insect Mouthparts Architecture",
                        "content": {
                            "title": "Learning Focus: Insect Mouthparts Architecture",
                            "goals": [
                                "Describe the anatomical structure of five main types of insect mouthparts.",
                                "Relate the structure of each insect mouthpart type to its specific feeding adaptation and diet.",
                                "Identify insect disease vectors based on their mouthpart morphology and evaluate their public health impact."
                            ]
                        }
                    },
                    {
                        "type": "concept_explanation",
                        "title": "Precision Biological Tools",
                        "content": {
                            "title": "Precision Biological Tools",
                            "text": "Have you ever wondered why a mosquito can effortlessly pierce skin to suck blood, while a grasshopper cleanly slices through tough leaves, and a butterfly gently sips nectar from deep inside flowers?\n\nDespite sharing a common insect body plan, insects have evolved highly specialized mouthparts that act as precision tools, enabling them to exploit diverse food resources without competing with one another."
                        }
                    }
                ],
                # Page 2: Key Terms
                [
                    {
                        "type": "definition_card",
                        "title": "Insect Cranial Anatomy Vocabulary",
                        "content": {
                            "term": "Essential Insect Mouthpart Terms",
                            "definition": "Anatomical components of the generalized and specialized insect head.",
                            "key_points": [
                                "Mandible: Heavy, hard, heavily-chitinized jaw structures used for cutting, crushing, and masticating food.",
                                "Maxilla (plural Maxillae): Paired accessory jaws located behind mandibles that assist in food manipulation or are modified into elongated tubes.",
                                "Proboscis: An elongated tubular feeding apparatus used by sucking insects to draw up liquid nutrients.",
                                "Labium: The lower lip of an insect's mouthparts that often forms a protective sheath or supporting base.",
                                "Labellum (plural Labella): A fleshy, sponge-like paired lobe at the tip of the labium in flies, used to absorb liquefied foods.",
                                "Pseudotracheae: Microscopic, open-grooved capillary channels covering the labellum that draw in liquid food via capillary action."
                            ]
                        }
                    }
                ],
                # Page 3: The Five Main Feeding Adaptations
                [
                    {
                        "type": "concept_explanation",
                        "title": "The Five Main Insect Feeding Adaptations",
                        "content": {
                            "title": "The Five Main Insect Feeding Adaptations",
                            "text": "All insect mouthparts are evolutionary modifications of a single ancestral plan (labrum, mandibles, maxillae, labium, and hypopharynx):\n\n1. **Biting and Chewing (Locust, Grasshopper, Cockroach)**: Heavily-chitinized, serrated mandibles move horizontally to slice and grind tough fibrous plant leaves.\n2. **Piercing and Sucking (Female Mosquito, Aphid, Bedbug)**: Six sharp, needle-like **stylets** penetrate skin or plant phloem to suck blood or sugary sap, enclosed in a protective labium sheath.\n3. **Siphoning (Butterfly, Moth)**: Mandibles are absent; maxillae are elongated and fused into a long, coiled, spring-like **proboscis** that uncoils to sip floral nectar.\n4. **Cutting and Lapping (Tsetse Fly, Horsefly)**: A stiff proboscis ending in a labellum equipped with sharp microscopic **prestomal teeth** that saw skin open to lap pooling blood.\n5. **Sponging (Housefly)**: An elbowed proboscis terminating in fleshy **labella** lined with pseudotracheae that sponge up pre-liquefied organic fluids."
                        }
                    }
                ],
                # Page 4: 5-Panel Insect Mouthparts SVG
                [
                    {
                        "type": "suggested_diagram",
                        "title": "Comparative Insect Mouthparts & Feeding Adaptations",
                        "content": {
                            "description": "Five-panel horizontal comparative diagram showing insect heads and highlighted mouthparts: 1. Grasshopper with broad serrated cutting mandibles; 2. Mosquito with 6 needle-like piercing stylets and retractable labium sheath; 3. Butterfly with long uncoiled siphoning proboscis tube; 4. Tsetse fly with forward-pointing cutting proboscis and sharp prestomal teeth; 5. Housefly with elbowed sponging proboscis, fleshy labella lobes, and fine pseudotracheae channels.",
                            "caption": "Comparative anatomical architecture of the five primary insect mouthpart modifications and feeding adaptations."
                        }
                    }
                ],
                # Page 5: Comparison Table: 5 Insect Mouthparts
                [
                    {
                        "type": "comparison_table",
                        "title": "Comparison: Five Insect Mouthpart Adaptations & Diets",
                        "content": {
                            "headers": ["Mouthpart Type", "Representative Insect", "Key Structural Modifications", "Diet & Feeding Mechanism", "Ecological / Medical Significance"],
                            "rows": [
                                ["Biting and Chewing", "Locust, Grasshopper, Cockroach", "Broad, heavily-sintered chitinous **mandibles** with sharp cutting teeth", "Cuts, masticates, and grinds solid plant foliage and organic debris", "Major agricultural crop pests (e.g., desert locust swarms)"],
                                ["Piercing and Sucking", "Female Mosquito (*Anopheles*), Aphid", "Six needle-like **stylets** inside a retractable labial sheath forming a food canal", "Pierces animal skin to suck blood or plant stems to suck phloem sap", "Primary vector for malaria (*Plasmodium*), dengue, and plant viruses"],
                                ["Siphoning", "Butterfly, Hawk Moth", "Maxillae fused into a long, flexible, coiled **proboscis**; mandibles absent", "Uncoils by hydrostatic pressure to reach nectar deep within tubular flowers", "Essential pollinators of wild flowers and commercial crops"],
                                ["Cutting and Lapping", "Tsetse Fly (*Glossina*)", "Stiff forward proboscis with sharp **prestomal teeth** on labellum", "Saws open host skin to rupture capillaries, then laps pooling blood", "Biological vector of Trypanosomiasis (Sleeping sickness / Nagana)"],
                                ["Sponging", "Housefly (*Musca domestica*)", "Elbowed proboscis ending in fleshy **labella** covered in **pseudotracheae**", "Regurgitates salivary enzymes to liquefy solid food, then sponges up liquid", "Mechanical vector transmitting cholera, typhoid, and dysentery pathogens"]
                            ]
                        }
                    }
                ],
                # Page 6: Housefly Sponging Mechanism
                [
                    {
                        "type": "step_process",
                        "title": "The Housefly Sponging & External Digestion Mechanism",
                        "content": {
                            "title": "The Housefly Sponging & External Digestion Mechanism",
                            "steps": [
                                {
                                    "step_number": 1,
                                    "title": "Food Localization & Contact",
                                    "description": "The housefly lands on solid food (e.g., sugar crystals, decaying meat) and extends its elbowed proboscis downwards."
                                },
                                {
                                    "step_number": 2,
                                    "title": "Salivary Regurgitation",
                                    "description": "Because it completely lacks mandibles to chew or stylets to pierce, it regurgitates acidic salivary digestive enzymes onto the food."
                                },
                                {
                                    "step_number": 3,
                                    "title": "External Solubilization",
                                    "description": "The enzymes digest and liquefy the solid food externally into a nutrient-rich fluid solution."
                                },
                                {
                                    "step_number": 4,
                                    "title": "Pseudotracheal Capillary Uptake",
                                    "description": "The fleshy labella press onto the liquid; capillary action draws the fluid into the microscopic pseudotracheae channels directly into the mouth."
                                }
                            ]
                        }
                    }
                ],
                # Page 7: Micrograph of Insect Mouthparts
                [
                    {
                        "type": "suggested_image",
                        "title": "Micrograph of Housefly Sponging Labella with Pseudotracheae Channels",
                        "content": {
                            "description": "High-magnification Scanning Electron Micrograph (SEM) showing the fleshy, lobed labellum of a housefly proboscis, revealing the intricate open-grooved pseudotracheae capillary channels.",
                            "caption": "Scanning electron micrograph of housefly labella showing the open pseudotracheae channels that absorb liquefied food via capillarity."
                        }
                    }
                ],
                # Page 8: Deep Dive Educational Video
                [
                    {
                        "type": "suggested_video",
                        "title": "Deep Dive: Insect Mouthparts and Feeding Adaptations",
                        "content": {
                            "description": "Educational presentation and high-speed microscopic video showing biting locust jaws, mosquito stylet skin penetration, butterfly proboscis uncoiling, and housefly sponging feeding."
                        }
                    }
                ],
                # Page 9: Knowledge Check & Summary
                [
                    {
                        "type": "knowledge_check",
                        "title": "Check Your Understanding: Housefly Inability to Pierce Skin",
                        "content": {
                            "question": "Why is a common housefly completely unable to bite or pierce human skin to suck blood, unlike a tsetse fly or mosquito?",
                            "options": [
                                "Housefly mouthparts are too long and flexible to penetrate skin.",
                                "Houseflies lack hard mandibles or sharp piercing stylets, possessing instead a fleshy labellum adapted solely to sponge up pre-liquefied fluids.",
                                "Houseflies do not have salivary glands to liquefy blood.",
                                "Houseflies only feed on carbon dioxide gas."
                            ],
                            "correct_answer": "B",
                            "explanation": "Houseflies have sponging mouthparts. They completely lack the sharp cutting mandibles of grasshoppers, the piercing needle-like stylets of mosquitoes, or the cutting prestomal teeth of tsetse flies. Their mouthparts terminate in sponge-like labella, which can only absorb liquid foods that have been liquefied externally by regurgitated saliva."
                        }
                    },
                    {
                        "type": "summary",
                        "title": "Lesson Summary: Insect Mouthparts",
                        "content": {
                            "title": "Lesson Summary: Insect Mouthparts",
                            "points": [
                                "Insect mouthparts are modified from a single ancestral template into 5 distinct functional feeding tools.",
                                "Grasshoppers bite/chew with serrated mandibles; mosquitoes pierce/suck with 6 needle stylets.",
                                "Butterflies siphon nectar with a coiled maxilla proboscis; tsetse flies cut skin with prestomal teeth.",
                                "Houseflies sponge pre-liquefied food using fleshy labella lined with capillary pseudotracheae.",
                                "Understanding mouthpart structures helps identify disease vectors and devise targeted public health control methods."
                            ]
                        }
                    }
                ]
            ]
        },

        # =====================================================================
        # LESSON 8.2: Bird Beaks and Feeding Adaptations
        # =====================================================================
        {
            "unit_order": 2,
            "unit_name": "Bird Beaks and Feeding Adaptations",
            "unit_description": "Five avian beak morphologies (cracking, tearing, sipping, spearing, filtering), ecological niche differentiation, and Lake Nakuru foraging frequency data analysis.",
            "lesson_title": "Bird Beaks and Feeding Adaptations",
            "pages": [
                # Page 1: Introduction & Learning Focus
                [
                    {
                        "type": "learning_goal",
                        "title": "Learning Focus: Avian Beaks & Niche Differentiation",
                        "content": {
                            "title": "Learning Focus: Avian Beaks & Niche Differentiation",
                            "goals": [
                                "Describe the structural adaptations of five major types of avian beaks.",
                                "Relate beak shapes and sizes to specific diets and foraging strategies.",
                                "Analyze ecological frequency data from Kenyan wetlands to explain how beak adaptations prevent niche overlap and eliminate interspecific competition."
                            ]
                        }
                    },
                    {
                        "type": "concept_explanation",
                        "title": "The Avian Survival Tool",
                        "content": {
                            "title": "The Avian Survival Tool",
                            "text": "In the bird kingdom, the beak is the ultimate multi-purpose tool. Because birds lack hands, arms, and teeth, their beaks must perform every mechanical task: building intricate nests, preening feathers, defending territories, and capturing and processing food.\n\nIn Kenya's rich ecosystems—from Mt. Kenya's highland forests to the Great Rift Valley soda lakes—beak morphology directly reveals a bird's ecological diet and evolutionary lifestyle."
                        }
                    }
                ],
                # Page 2: Key Terms
                [
                    {
                        "type": "definition_card",
                        "title": "Avian Ecology & Anatomy Vocabulary",
                        "content": {
                            "term": "Essential Avian Ecological Terms",
                            "definition": "Key concepts in ornithology, cranial adaptations, and community ecology.",
                            "key_points": [
                                "Beak (Bill): The external, keratinized anatomical structure covering the upper and lower jaws of birds.",
                                "Lamellae: Fine, comb-like filtering plates lining the margins of a filter-feeding bird's bill to strain plankton and algae.",
                                "Ecological Niche: The functional role, physical space, and specific resource utilization pattern of an organism within its community.",
                                "Interspecific Competition: The competition between individuals of different species for the same limited ecological resources.",
                                "Niche Differentiation (Resource Partitioning): The evolutionary process where competing species use different resources or habitats, minimizing competition and allowing stable coexistence."
                            ]
                        }
                    }
                ],
                # Page 3: Five Key Avian Beak Adaptations
                [
                    {
                        "type": "concept_explanation",
                        "title": "Five Key Avian Beak Adaptations",
                        "content": {
                            "title": "Five Key Avian Beak Adaptations",
                            "text": "1. **Conical, Seed-Cracking Beaks (Finches, Sparrows, Weavers)**: Short, stout, and thick. Works like heavy pliers to exert high crushing force on tough seed coats.\n2. **Hooked, Flesh-Tearing Beaks (Eagles, Hawks, Owls)**: Strong, razor-sharp, and curved downward into a sharp hook. Operates like a carving knife to rip and dissect prey muscle tissue.\n3. **Down-Curved, Tubular Nectar-Sipping Beaks (Sunbirds)**: Exceptionally long, slender, and curved downward. Functions like a drinking straw to reach deep floral nectaries without harming flowers.\n4. **Spear-Like, Fish-Catching Beaks (Herons, Kingfishers, Egrets)**: Long, straight, heavy, and sharply pointed. Plunges forward with rapid velocity to spear or grip slippery aquatic fish and amphibians.\n5. **Bent, Filter-Feeding Beaks (Flamingos)**: Deeply bent downward and lined with fine, comb-like **lamellae**. Operated upside-down using the muscular tongue as a hydraulic pump to strain microscopic *Spirulina* algae and brine shrimp."
                        }
                    }
                ],
                # Page 4: Avian Beaks & Lake Nakuru Zonation SVG
                [
                    {
                        "type": "suggested_diagram",
                        "title": "Avian Beak Morphologies, Feeding Mechanics & Lake Nakuru Ecological Zonation",
                        "content": {
                            "description": "Dual-panel diagram. Top panel: 5 distinct avian beak morphologies labeled with mechanical action (1. Finch conical seed-cracker; 2. Eagle hooked flesh-tearer; 3. Sunbird down-curved nectar straw; 4. Heron straight spear-bill; 5. Flamingo bent filter-feeder with lamellae bristles). Bottom panel: Ecological wetland profile of Lake Nakuru showing zonation and resource partitioning: Lesser Flamingo in deep water filtering Spirulina algae; Yellow-billed Stork in shallow mudflats spearing fish; Superb Starling on dry grassy shore collecting seeds and insects.",
                            "caption": "Avian beak morphological diversity alongside wetland ecological zonation at Lake Nakuru illustrating niche differentiation."
                        }
                    }
                ],
                # Page 5: Comparison Table: Avian Beak Types
                [
                    {
                        "type": "comparison_table",
                        "title": "Comparison: Five Avian Beak Adaptations & Ecological Niches",
                        "content": {
                            "headers": ["Beak Adaptation", "Representative Kenyan Birds", "Structural Beak Features", "Primary Diet & Foraging Mechanism", "Mechanical Analogy"],
                            "rows": [
                                ["Conical Seed-Cracker", "Finch, House Sparrow, Weaver Bird", "Short, stout, thick, heavily reinforced conical bone core", "Crushes hard seed coats and grains using powerful jaw muscles", "Heavy-duty crushing pliers"],
                                ["Hooked Flesh-Tearer", "Fish Eagle, Crowned Eagle, Hawk, Owl", "Sharp, sharp-edged, heavily curved downward hook", "Tears and dissects vertebrate flesh, muscle, and tendons", "Curved surgeon's scalpel / carving knife"],
                                ["Tubular Nectar-Sipper", "Bronze Sunbird, Scarlet-chested Sunbird", "Long, exceptionally slender, gently down-curved bill", "Reaches deep into tubular floral corollas to sip nectar", "Precision drinking straw"],
                                ["Spear-Like Fish-Catcher", "Goliath Heron, Pied Kingfisher, Little Egret", "Long, straight, heavy, dagger-sharp pointed bill", "Strikes rapidly into water to impale or grip slippery fish and frogs", "Hunting harpoon / spear"],
                                ["Bent Filter-Feeder", "Lesser Flamingo, Greater Flamingo", "Deeply bent mid-section, outer margins lined with fine **lamellae**", "Submerges beak upside-down, pumping water across lamellae to trap algae", "Hydraulic filtration sieve"]
                            ]
                        }
                    }
                ],
                # Page 6: Data Analysis: Lake Nakuru Avian Foraging
                [
                    {
                        "type": "comparison_table",
                        "title": "Ecological Data Practical: Avian Foraging Frequency at Lake Nakuru",
                        "content": {
                            "headers": ["Bird Species & Beak Type", "Deep Water Zone (Submerged)", "Shallow Mudflat Zone (0–10 cm)", "Dry Grassy Shore Zone", "Ecological Zone Preference & Food Source"],
                            "rows": [
                                ["**Lesser Flamingo** (Bent filter-feeder)", "**92 visits**", "8 visits", "0 visits", "Deep water: floats and filters microscopic *Spirulina* algae via lamellae"],
                                ["**Yellow-billed Stork** (Heavy spear-bill)", "5 visits", "**85 visits**", "2 visits", "Shallow mudflat: wades in 0–10 cm depth to spear fish and frogs"],
                                ["**Superb Starling** (Straight generalist bill)", "0 visits", "4 visits", "**115 visits**", "Dry grassy shore: walks on dry ground picking seeds, fruits, and beetles"],
                                ["**ECOLOGICAL CONCLUSION**", "Niche 1: Filter Feeder", "Niche 2: Aquatic Predator", "Niche 3: Terrestrial Forager", "**Zero Niche Overlap $\\rightarrow$ Low Interspecific Competition $\\rightarrow$ Stable Coexistence!**"]
                            ]
                        }
                    }
                ],
                # Page 7: Lesser Flamingo Micrograph Image
                [
                    {
                        "type": "suggested_image",
                        "title": "Kenyan Lesser Flamingo in Lake Nakuru with Filter Lamellae",
                        "content": {
                            "description": "High-resolution photograph of a Kenyan Lesser Flamingo standing in the saline waters of Lake Nakuru with its head bent upside-down filtering water, with an inset showing the fine microscopic comb-like lamellae plates lining the beak edge.",
                            "caption": "Kenyan Lesser Flamingo in Lake Nakuru utilizing its bent beak and microscopic lamellae to filter-feed on microscopic blue-green algae."
                        }
                    }
                ],
                # Page 8: Deep Dive Educational Video
                [
                    {
                        "type": "suggested_video",
                        "title": "Deep Dive: Bird Beak Adaptations, Diet & Ecological Niches",
                        "content": {
                            "description": "Comprehensive video documentary covering avian beak evolutionary adaptations, seed cracking mechanics, eagle raptor hunting, sunbird pollination, and flamingo filter feeding."
                        }
                    }
                ],
                # Page 9: Knowledge Check
                [
                    {
                        "type": "knowledge_check",
                        "title": "Check Your Understanding: Sunbird vs. Finch Niche Differentiation",
                        "content": {
                            "question": "Sunbirds and finches are frequently observed visiting the same garden flowering shrubs in Nairobi, yet they never fight over food or compete with one another. What biological principle explains this peaceful coexistence?",
                            "options": [
                                "Finches are nocturnal, while sunbirds only feed during the day.",
                                "They have evolved different beak adaptations—finches have short, thick conical beaks to crack seeds, while sunbirds have long, thin curved beaks to sip flower nectar, meaning they occupy completely separate ecological niches and do not share the same food resource.",
                                "Sunbirds defend finches from predators.",
                                "Finches eat sunbirds' eggs."
                            ],
                            "correct_answer": "B",
                            "explanation": "Because they possess highly specialized beak adaptations, finches and sunbirds target entirely different food resources. Finches crack seeds, whereas sunbirds sip floral nectar. This structural specialization prevents niche overlap and eliminates interspecific competition, allowing both species to live sustainably in the exact same geographic garden."
                        }
                    }
                ],
                # Page 10: Summary
                [
                    {
                        "type": "summary",
                        "title": "Lesson Summary: Avian Beak Adaptations",
                        "content": {
                            "title": "Lesson Summary: Avian Beak Adaptations",
                            "points": [
                                "Avian beaks are specialized tools: conical (seed cracking), hooked (flesh tearing), tubular (nectar sipping), spear (fish catching), and bent (filter feeding).",
                                "Flamingos use comb-like lamellae and hydraulic tongue pumping to filter algae from salty lake water.",
                                "Structural adaptations divide food resources and physical habitats among species (niche differentiation).",
                                "Eliminating niche overlap drastically reduces interspecific competition, promoting rich biological diversity."
                            ]
                        }
                    }
                ]
            ]
        }
    ]

def ingest_grade10_biology_topic8(replace=False):
    """Executes the database ingestion for Grade 10 Biology Topic 8."""
    print("=" * 80)
    print("VLearn Grade 10 Biology — Ingestion Engine")
    print("Topic 8: Animal Nutrition and Feeding Adaptations (CBC Curriculum ID: 5)")
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

    # 4. Resolve Topic 8
    topic_name = "Animal Nutrition and Feeding Adaptations"
    topic = Topic.objects.filter(subject=subject, name=topic_name).first()

    if topic and replace:
        print(f"[*] Found existing Topic '{topic_name}' (ID: {topic.id}). Performing clean replacement of child units/lessons...")
        topic.learning_units.all().delete()
        topic.lessons.all().delete()
    elif not topic:
        topic = Topic.objects.create(
            subject=subject,
            name=topic_name,
            order=8,
            description="Comprehensive syllabus on insect mouthparts (biting, piercing, siphoning, cutting, sponging) and avian beak adaptations (cracking, tearing, sipping, spearing, filtering) for ecological niche differentiation."
        )
        print(f"[+] Created Topic: {topic.name} (ID: {topic.id})")
    else:
        print(f"[*] Using existing Topic: {topic.name} (ID: {topic.id})")

    curriculum_data = build_topic8_curriculum()
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
    print("[SUCCESS] Grade 10 Biology Topic 8 Ingestion Complete!")
    print(f"[*] Total Lessons Ingested: {total_lessons}")
    print(f"[*] Total Pages/Cards:      {total_pages}")
    print(f"[*] Total Blocks Created:   {total_blocks}")
    print("=" * 80)

if __name__ == "__main__":
    replace_flag = "--replace" in sys.argv
    ingest_grade10_biology_topic8(replace=replace_flag)
