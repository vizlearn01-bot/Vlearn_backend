"""
VLearn Form 4 Biology — Topic 3: Reception, Response and Coordination in Plants and Animals
High-Structure Production Ingestion Engine

Topic: Reception, Response and Coordination in Plants and Animals (Topic Order: 3)
Subject: Biology (Subject ID: 13)
Grade: Form 4 (Grade ID: 4)
Curriculum: 844 (Curriculum ID: 4)

Decomposed into 10 Learning Units & 10 Published Lessons (114 Total Pages):
  1. Introduction to Reception, Response, and Coordination Systems (5 Pages)
  2. Environmental Stimuli, Sensory Pathways, and Coordination Networks (10 Pages)
  3. Tropisms, Tactic Responses, and Nastic Movements in Plants (12 Pages)
  4. Auxin Growth Physiology, Apical Dominance, Etiolation, and Plant Labs (11 Pages)
  5. Neurone Anatomy, Resting Potentials, and Synaptic Transmission (15 Pages)
  6. Brain and Spinal Cord Anatomy, Reflex Arcs, and Conditioning (15 Pages)
  7. Endocrine Glands, Hormonal Regulation, and Drug Abuse Pathology (13 Pages)
  8. Eye Anatomy, Image Formation, Accommodation, and Optical Defects (15 Pages)
  9. Ear Anatomy, Sound Transduction, Balance Mechanisms, and Pathology (12 Pages)
  10. Topic Synthesis, Master Key Glossary, and Multi-Tier Examination Diagnostic (6 Pages)

Usage:
  ./venv/bin/python curriculum/ingest_form4_biology_topic3.py [--replace]
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
    """Removes bracket citations and cleans double spaces."""
    if not text:
        return ""
    text = re.sub(r'\[(?:\d+|image_\d+|S\d+.*?|[\d,\s]+)\]', '', text)
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

def build_topic3_curriculum():
    """Returns the comprehensive pedagogical page and block structure for Topic 3."""
    return [
        # =====================================================================
        # LESSON 1: Introduction to Reception, Response, and Coordination Systems
        # =====================================================================
        {
            "unit_order": 1,
            "unit_name": "Introduction to Reception, Response, and Coordination Systems",
            "unit_description": "Irritability, stimulus, receptor, coordinator, effector, response, and survival significance.",
            "lesson_title": "Introduction to Reception, Response, and Coordination Systems",
            "pages": [
                [
                    {
                        "type": "learning_goal",
                        "title": "Learning Objectives: Response Systems Overview",
                        "content": {
                            "title": "Learning Objectives: Response Systems Overview",
                            "goals": [
                                "Define irritability, stimulus, receptor, coordinator, effector, and response.",
                                "Trace the 5-step biological response arc.",
                                "Explain the survival value of sensitivity in living organisms."
                            ]
                        }
                    },
                    {
                        "type": "concept_explanation",
                        "title": "Biological Irritability and Survival",
                        "content": {
                            "title": "Biological Irritability and Survival",
                            "text": "Irritability (sensitivity) is the fundamental characteristic of living organisms to detect changes in their internal or external environment (stimuli) and execute appropriate responses to ensure survival."
                        }
                    }
                ],
                [
                    {
                        "type": "definition_card",
                        "title": "Response Circuitry Taxonomy",
                        "content": {
                            "term": "Response Circuitry Terms",
                            "definition": "Key components of the biological response arc.",
                            "key_points": [
                                "Stimulus: A change in environment that evokes a response.",
                                "Receptor: Specialized sensory cell/organ detecting stimuli.",
                                "Coordinator: Brain/spinal cord or endocrine gland processing signals.",
                                "Effector: Muscle or gland executing the physical response.",
                                "Response: The resulting physiological or behavioral change."
                            ]
                        }
                    }
                ],
                [
                    {
                        "type": "suggested_diagram",
                        "title": "Biological Response Arc: Stimulus to Effector Response",
                        "content": {
                            "title": "Biological Response Arc: Stimulus to Effector Response",
                            "caption": "5-Step Flowchart: Environmental Stimulus → Sensory Receptor → Coordinating Center → Effector Gland/Muscle → Adaptive Response",
                            "description": "Flowchart showing Stimulus -> Receptor -> Sensory Nerve -> Brain/Spinal Cord Coordinator -> Motor Nerve -> Muscle/Gland Effector -> Response."
                        }
                    },
                    {
                        "type": "concept_explanation",
                        "title": "Survival Significance of Sensitivity",
                        "content": {
                            "title": "Survival Significance of Sensitivity",
                            "text": "Sensitivity enables organisms to escape predators, locate food and water, avoid extreme temperature damage, find mates, and maintain internal homeostasis."
                        }
                    }
                ],
                [
                    {
                        "type": "knowledge_check",
                        "title": "Knowledge Checkpoint: Response Circuitry",
                        "content": {
                            "question": "Which organ acts as an effector in the biological response arc?",
                            "options": [
                                "Biceps Muscle or Salivary Gland",
                                "Optic Nerve",
                                "Retinal Photoreceptor Cell",
                                "Pain Sensor in Skin"
                            ],
                            "correct_answer": 0,
                            "explanation": "Muscles and glands execute physical responses as effectors."
                        }
                    }
                ],
                [
                    {
                        "type": "summary",
                        "title": "Introduction to Coordination: Key Takeaways",
                        "content": {
                            "title": "Introduction to Coordination: Key Takeaways",
                            "summary_points": [
                                "Irritability allows organisms to detect stimuli and execute adaptive responses.",
                                "The response arc proceeds: Stimulus -> Receptor -> Coordinator -> Effector -> Response.",
                                "Sensitivity is essential for escaping danger, acquiring resources, and maintaining homeostasis."
                            ]
                        }
                    }
                ]
            ]
        },

        # =====================================================================
        # LESSON 2: Environmental Stimuli, Sensory Pathways, and Coordination Networks
        # =====================================================================
        {
            "unit_order": 2,
            "unit_name": "Environmental Stimuli, Sensory Pathways, and Coordination Networks",
            "unit_description": "Internal vs external stimuli, electrical vs chemical coordination, and transmission speed differences.",
            "lesson_title": "Environmental Stimuli, Sensory Pathways, and Coordination Networks",
            "pages": [
                [
                    {
                        "type": "learning_goal",
                        "title": "Learning Objectives: Coordination Networks",
                        "content": {
                            "title": "Learning Objectives: Coordination Networks",
                            "goals": [
                                "Classify internal and external environmental stimuli.",
                                "Compare nervous electrical coordination with endocrine chemical coordination.",
                                "Analyze transmission speed and target specificity differences."
                            ]
                        }
                    },
                    {
                        "type": "concept_explanation",
                        "title": "Internal vs External Stimuli",
                        "content": {
                            "title": "Internal vs External Stimuli",
                            "text": "• External Stimuli: Light, heat, sound, pressure, gravity, and chemical odors in the surrounding environment.\n• Internal Stimuli: Blood glucose concentration, body temperature, osmotic pressure, carbon dioxide levels, and blood pressure."
                        }
                    }
                ],
                [
                    {
                        "type": "definition_card",
                        "title": "Sensory Receptor Modalities",
                        "content": {
                            "term": "Sensory Receptor Types",
                            "definition": "Specialized cells detecting specific energy forms.",
                            "key_points": [
                                "Photoreceptors: Detect light energy (Retina rods/cones).",
                                "Mechanoreceptors: Detect mechanical pressure/vibration (Skin, Ear).",
                                "Thermoreceptors: Detect temperature shifts (Skin, Hypothalamus).",
                                "Chemoreceptors: Detect chemical molecules (Taste buds, Olfactory epithelium).",
                                "Baroreceptors: Detect blood pressure in carotid sinus."
                            ]
                        }
                    }
                ],
                [
                    {
                        "type": "suggested_diagram",
                        "title": "Nervous vs Endocrine Coordination System Comparison",
                        "content": {
                            "title": "Nervous vs Endocrine Coordination System Comparison",
                            "caption": "Comparative Network Model: Rapid Electrical Impulse Conduction via Neurones vs Slow Chemical Hormone Circulation via Bloodstream",
                            "description": "Comparative diagram contrasting high-speed electrical nerve impulses with target-bound blood hormone circulation."
                        }
                    },
                    {
                        "type": "comparison_table",
                        "title": "Comparison Matrix: Nervous vs Endocrine System",
                        "content": {
                            "headers": ["Feature", "Nervous System", "Endocrine System"],
                            "rows": [
                                ["Message Type", "Electrical nerve impulse (Action Potential)", "Chemical hormone messenger"],
                                ["Transmission Pathway", "Nerve fibers (Axons & Dendrites)", "Bloodstream circulation"],
                                ["Transmission Speed", "Very rapid (up to 120 m/s)", "Slow and gradual"],
                                ["Target Specificity", "Localized strictly to specific muscle/gland", "Widespread to target organs with complementary receptors"],
                                ["Response Duration", "Short-lived and temporary", "Long-lasting and persistent"]
                            ]
                        }
                    }
                ],
                [
                    {
                        "type": "concept_explanation",
                        "title": "Coordination in Plants vs Animals",
                        "content": {
                            "title": "Coordination in Plants vs Animals",
                            "text": "Plants lack a nervous system! Plant coordination relies entirely on slow chemical growth substances (auxins, gibberellins, cytokinins, abscisic acid, ethylene) moving via diffusion and phloem transport."
                        }
                    }
                ],
                [
                    {
                        "type": "mini_activity",
                        "title": "Interactive Coordination Pathway Simulator",
                        "content": {
                            "activity_type": "scenario_decision",
                            "title": "Interactive Coordination Pathway Simulator",
                            "prompt": "Which coordination system mediates rapid withdrawal of a hand touching a hot iron?",
                            "options": [
                                "Option A: Nervous System (Rapid electrical reflex arc).",
                                "Option B: Endocrine System (Slow thyroid hormone secretion).",
                                "Option C: Plant Auxin Diffusion."
                            ],
                            "correct_option": "Option A: Nervous System (Rapid electrical reflex arc).",
                            "explanation": "Nervous system conducts high-speed electrical impulses via neurones for immediate protective action."
                        }
                    }
                ],
                [
                    {
                        "type": "knowledge_check",
                        "title": "Knowledge Checkpoint: Sensory Pathways",
                        "content": {
                            "question": "Which characteristic distinguishes endocrine chemical coordination from nervous electrical coordination?",
                            "options": [
                                "Endocrine messages travel via the bloodstream and produce widespread, long-lasting effects.",
                                "Endocrine messages travel at 120 meters per second along myelin sheaths.",
                                "Endocrine coordination uses electrical action potentials.",
                                "Endocrine coordination is only present in single-celled amoebae."
                            ],
                            "correct_answer": 0,
                            "explanation": "Hormones travel in blood to widespread target organs with persistent effects."
                        }
                    }
                ],
                [
                    {
                        "type": "summary",
                        "title": "Sensory Networks: Key Takeaways",
                        "content": {
                            "title": "Sensory Networks: Key Takeaways",
                            "summary_points": [
                                "Receptors convert mechanical, chemical, thermal, and light energy into electrical impulses.",
                                "Nervous coordination is rapid, localized, and short-lived via neurones.",
                                "Endocrine coordination is slow, widespread, and long-lasting via blood hormones.",
                                "Plants rely exclusively on chemical growth regulators (auxins)."
                            ]
                        }
                    }
                ]
            ]
        },

        # =====================================================================
        # LESSON 3: Tropisms, Tactic Responses, and Nastic Movements in Plants
        # =====================================================================
        {
            "unit_order": 3,
            "unit_name": "Tropisms, Tactic Responses, and Nastic Movements in Plants",
            "unit_description": "Plant tropisms (directional growth), tactic responses (directional locomotion), nastic movements (non-directional), and Mimosa pudica seismonasty.",
            "lesson_title": "Tropisms, Tactic Responses, and Nastic Movements in Plants",
            "pages": [
                [
                    {
                        "type": "learning_goal",
                        "title": "Learning Objectives: Plant Movements",
                        "content": {
                            "title": "Learning Objectives: Plant Movements",
                            "goals": [
                                "Define plant tropisms (phototropism, geotropism, hydrotropism, thigmotropism, chemotropism).",
                                "Explain tactic responses (taxes) in motile micro-organisms.",
                                "Describe nastic movements (seismonasty, photonasty) and turgor pressure pulvinus changes in Mimosa pudica."
                            ]
                        }
                    },
                    {
                        "type": "concept_explanation",
                        "title": "Classification of Plant Movements",
                        "content": {
                            "title": "Classification of Plant Movements",
                            "text": "Plants respond to stimuli through three distinct movement categories:\n1. Tropisms: Directional growth movements of fixed plant parts;\n2. Tactic Movements (Taxes): Directional locomotion of entire motile cells/organisms;\n3. Nastic Movements: Non-directional turgor or growth movements."
                        }
                    }
                ],
                [
                    {
                        "type": "definition_card",
                        "title": "Plant Tropisms Taxonomy",
                        "content": {
                            "term": "Plant Tropisms Taxonomy",
                            "definition": "Growth movements of plant organs whose direction is determined by the direction of the stimulus.",
                            "key_points": [
                                "Phototropism: Growth response to unilateral light (Shoots positive; Roots negative).",
                                "Geotropism (Gravitropism): Growth response to gravity (Roots positive; Shoots negative).",
                                "Hydrotropism: Growth response to water gradient (Roots positive).",
                                "Thigmotropism: Growth response to touch/contact (Tendril twining).",
                                "Chemotropism: Growth response to chemicals (Pollen tube growth towards embryo sac)."
                            ]
                        }
                    }
                ],
                [
                    {
                        "type": "suggested_diagram",
                        "title": "Plant Tropisms Classification: Phototropism, Geotropism, Hydrotropism",
                        "content": {
                            "title": "Plant Tropisms Classification: Phototropism, Geotropism, Hydrotropism",
                            "caption": "Comparative Growth Diagram: Positive Phototropism (Shoot Bending Lightwards) vs Positive Geotropism (Root Growing Earthwards) vs Hydrotropism",
                            "description": "Diagram showing shoot bending towards light, root growing downwards towards gravity, and root bending towards moist soil."
                        }
                    },
                    {
                        "type": "suggested_image",
                        "title": "Phototropism Growth Towards Light Visualization",
                        "content": {
                            "title": "Phototropism Growth Towards Light Visualization",
                            "caption": "Green seedling stem exhibiting positive phototropism by curving toward unilateral light source.",
                            "url": "https://upload.wikimedia.org/wikipedia/commons/f/f3/Onions_reach_for_light.jpg",
                            "author": "Public Domain, Wikimedia Commons",
                            "licensing": "Public domain",
                            "commons_page_url": "https://commons.wikimedia.org/wiki/File:Onions_reach_for_light.jpg"
                        }
                    }
                ],
                [
                    {
                        "type": "definition_card",
                        "title": "Tactic Responses (Taxes)",
                        "content": {
                            "term": "Tactic Response Definition",
                            "definition": "Directional locomotion of an entire motile organism or free cell in response to a directional stimulus.",
                            "key_points": [
                                "Phototaxis: Locomotion towards light (e.g., Euglena and Chlamydomonas swimming towards light).",
                                "Chemotaxis: Locomotion towards chemicals (e.g., Motile fern sperms swimming towards malic acid secreted by archegonia)."
                            ]
                        }
                    }
                ],
                [
                    {
                        "type": "suggested_diagram",
                        "title": "Seismonastic Leaflet Folding Mechanism in Mimosa pudica",
                        "content": {
                            "title": "Seismonastic Leaflet Folding Mechanism in Mimosa pudica",
                            "caption": "Turgor Pressure Shift: Touch Stimulus → K+ Ion Efflux from Pulvinus Cells → Rapid Water Osmosis Loss → Leaflet Collapse",
                            "description": "Diagram illustrating open Mimosa pudica leaf vs collapsed leaf following touch stimulus causing pulvinus cell turgor loss."
                        }
                    },
                    {
                        "type": "suggested_image",
                        "title": "Mimosa pudica Closed Seismonastic Leaflets Visualization",
                        "content": {
                            "title": "Mimosa pudica Closed Seismonastic Leaflets Visualization",
                            "caption": "Closed bipinnate leaves of Sensitive Plant (Mimosa pudica) following seismonastic touch stimulation.",
                            "url": "https://upload.wikimedia.org/wikipedia/commons/4/4e/Mimosa_pudica_closed.JPG",
                            "author": "CC BY-SA 3.0, Wikimedia Commons",
                            "licensing": "CC BY-SA 3.0",
                            "commons_page_url": "https://commons.wikimedia.org/wiki/File:Mimosa_pudica_closed.JPG"
                        }
                    }
                ],
                [
                    {
                        "type": "concept_explanation",
                        "title": "Nastic Movements & Pulvinus Cell Mechanics",
                        "content": {
                            "title": "Nastic Movements & Pulvinus Cell Mechanics",
                            "text": "Nastic movements are non-directional plant responses where the direction of movement is independent of the stimulus direction. Seismonasty in *Mimosa pudica* occurs when touch triggers potassium ion ($K^+$) loss from lower pulvinus swelling cells, causing sudden water osmosis out and immediate leaf collapse."
                        }
                    }
                ],
                [
                    {
                        "type": "mini_activity",
                        "title": "Interactive Plant Response Classifier",
                        "content": {
                            "activity_type": "scenario_decision",
                            "title": "Interactive Plant Response Classifier",
                            "prompt": "Classify the movement of single-celled Euglena swimming towards a light source.",
                            "options": [
                                "Option A: Positive Phototaxis (Directional locomotion of entire cell).",
                                "Option B: Positive Phototropism (Directional growth of fixed stem).",
                                "Option C: Seismonasty."
                            ],
                            "correct_option": "Option A: Positive Phototaxis (Directional locomotion of entire cell).",
                            "explanation": "Locomotion of an entire free-swimming cell towards light is phototaxis."
                        }
                    }
                ],
                [
                    {
                        "type": "knowledge_check",
                        "title": "Knowledge Checkpoint: Tropisms & Taxes",
                        "content": {
                            "question": "What is the primary cellular cause of rapid leaflet folding in Mimosa pudica when touched?",
                            "options": [
                                "Rapid loss of turgor pressure in pulvinus cells due to water and ion efflux.",
                                "Rapid growth of new cells on the upper surface.",
                                "Muscle contraction in leaf stems.",
                                "Photosynthesis shutdown."
                            ],
                            "correct_answer": 0,
                            "explanation": "Pulvinus cells rapidly lose turgor pressure following touch stimulation."
                        }
                    }
                ],
                [
                    {
                        "type": "summary",
                        "title": "Plant Movements: Key Takeaways",
                        "content": {
                            "title": "Plant Movements: Key Takeaways",
                            "summary_points": [
                                "Tropisms are directional growth movements of fixed plant parts (phototropism, geotropism).",
                                "Tactic responses (taxes) are directional locomotion of entire motile cells (phototaxis, chemotaxis).",
                                "Nastic movements are non-directional responses caused by turgor pressure shifts in pulvinus cells (Mimosa pudica)."
                            ]
                        }
                    }
                ]
            ]
        },

        # =====================================================================
        # LESSON 4: Auxin Growth Physiology, Apical Dominance, Etiolation, and Plant Labs
        # =====================================================================
        {
            "unit_order": 4,
            "unit_name": "Auxin Growth Physiology, Apical Dominance, Etiolation, and Plant Labs",
            "unit_description": "Auxin (IAA) synthesis, unilateral light redistribution, apical dominance, etiolation, and clinostat geotropism lab setups.",
            "lesson_title": "Auxin Growth Physiology, Apical Dominance, Etiolation, and Plant Labs",
            "pages": [
                [
                    {
                        "type": "learning_goal",
                        "title": "Learning Objectives: Auxin Physiology & Labs",
                        "content": {
                            "title": "Learning Objectives: Auxin Physiology & Labs",
                            "goals": [
                                "Explain Indoleacetic Acid (IAA / Auxin) synthesis and unilateral light migration.",
                                "Contrast auxin effects on shoot cell elongation vs root cell inhibition.",
                                "Explain apical dominance and agricultural pruning applications.",
                                "Analyze clinostat experiments for geotropism and phototropism light box setups."
                            ]
                        }
                    },
                    {
                        "type": "concept_explanation",
                        "title": "Auxins (Indoleacetic Acid - IAA)",
                        "content": {
                            "title": "Auxins (Indoleacetic Acid - IAA)",
                            "text": "Auxins are plant growth hormones synthesized in actively dividing shoot and root apices. They promote cell elongation in shoots by increasing cell wall plasticity."
                        }
                    }
                ],
                [
                    {
                        "type": "suggested_diagram",
                        "title": "Auxin Redistribution & Differential Cell Elongation in Phototropism",
                        "content": {
                            "title": "Auxin Redistribution & Differential Cell Elongation in Phototropism",
                            "caption": "Phototropism Mechanism: Unilateral Light → Auxins Migrate to Shaded Side → Shaded Cells Elongate Faster → Stem Curvatures Towards Light Source",
                            "description": "Diagram illustrating Coleoptile tip exposed to side light, auxins migrating to dark side, shaded side cells expanding faster causing bending toward light."
                        }
                    },
                    {
                        "type": "suggested_image",
                        "title": "Plant Auxin Physiology Pods Visualization",
                        "content": {
                            "title": "Plant Auxin Physiology Pods Visualization",
                            "caption": "Garden pea pods illustrating active apical growth and tissue differentiation governed by auxin plant hormones.",
                            "url": "https://upload.wikimedia.org/wikipedia/commons/5/51/Pisum_sativum_var._macrocarpum_Ilowiecki_2017-04-14_6973.jpg",
                            "author": "CC BY-SA 4.0, Wikimedia Commons",
                            "licensing": "CC BY-SA 4.0",
                            "commons_page_url": "https://commons.wikimedia.org/wiki/File:Pisum_sativum_var._macrocarpum_Ilowiecki_2017-04-14_6973.jpg"
                        }
                    }
                ],
                [
                    {
                        "type": "concept_explanation",
                        "title": "Differential Auxin Sensitivity: Shoots vs Roots",
                        "content": {
                            "title": "Differential Auxin Sensitivity: Shoots vs Roots",
                            "text": "• Shoots: High auxin concentrations PROMOTE cell elongation. In horizontal shoots, gravity pulls auxins to the lower side; the lower side elongates faster, bending the shoot UPWARDS (negative geotropism).\n\n• Roots: High auxin concentrations INHIBIT cell elongation. In horizontal roots, auxins accumulate on the lower side; cell elongation is inhibited on the lower side while upper cells grow normally, bending the root DOWNWARDS (positive geotropism)."
                        }
                    }
                ],
                [
                    {
                        "type": "suggested_diagram",
                        "title": "Clinostat Rotating Apparatus for Geotropism Experiment",
                        "content": {
                            "title": "Clinostat Rotating Apparatus for Geotropism Experiment",
                            "caption": "Geotropism Control Apparatus: Rotating Clinostat Cancels Unilateral Gravitational Pull → Seedling Roots Grow Horizontally Straight",
                            "description": "Diagram showing rotating clinostat holding germinating seedling growing straight vs stationary clinostat showing root curvature downwards."
                        }
                    },
                    {
                        "type": "concept_explanation",
                        "title": "Apical Dominance & Etiolation",
                        "content": {
                            "title": "Apical Dominance & Etiolation",
                            "text": "• Apical Dominance: High auxin concentration produced by the apical bud diffuses down the stem, inhibiting the growth of lateral (axillary) buds. Removing the apical tip (pruning/decapitation) lowers auxin levels, allowing lateral buds to sprout, creating bushy tea bushes or hedges.\n\n• Etiolation: Seedlings grown in complete darkness grow abnormally tall, slender, yellow (chlorotic), with small unexpanded leaves as they rapidly expend energy reaching for light."
                        }
                    }
                ],
                [
                    {
                        "type": "mini_activity",
                        "title": "Interactive Auxin Physiology Simulator",
                        "content": {
                            "activity_type": "scenario_decision",
                            "title": "Interactive Auxin Physiology Simulator",
                            "prompt": "Why does a tea farmer periodically trim/prune the top apical tips of tea bushes?",
                            "options": [
                                "Option A: To break apical dominance, lowering auxin inhibition so lateral buds sprout into abundant harvestable leaves.",
                                "Option B: To kill the tea plant.",
                                "Option C: To prevent roots from growing."
                            ],
                            "correct_option": "Option A: To break apical dominance, lowering auxin inhibition so lateral buds sprout into abundant harvestable leaves.",
                            "explanation": "Decapitation removes the primary auxin source, promoting bushy lateral branching."
                        }
                    }
                ],
                [
                    {
                        "type": "knowledge_check",
                        "title": "Knowledge Checkpoint: Plant Hormones & Labs",
                        "content": {
                            "question": "What effect does a high concentration of auxin (IAA) have on root cells compared to shoot cells?",
                            "options": [
                                "High auxin inhibits cell elongation in roots but promotes cell elongation in shoots.",
                                "High auxin promotes cell division in both equally.",
                                "High auxin destroys root cell walls.",
                                "High auxin turns roots green."
                            ],
                            "correct_answer": 0,
                            "explanation": "Roots are far more sensitive to auxin; high concentrations inhibit root cell elongation."
                        }
                    }
                ],
                [
                    {
                        "type": "summary",
                        "title": "Auxin Growth Physiology: Key Takeaways",
                        "content": {
                            "title": "Auxin Growth Physiology: Key Takeaways",
                            "summary_points": [
                                "Auxins (IAA) migrate away from light to shaded stem sides, causing differential cell elongation and bending.",
                                "High auxin promotes shoot growth but inhibits root growth.",
                                "Apical dominance inhibits lateral buds; decapitation promotes bushy branching.",
                                "Rotating clinostats cancel unilateral gravity, causing roots to grow straight."
                            ]
                        }
                    }
                ]
            ]
        },

        # =====================================================================
        # LESSON 5: Neurone Anatomy, Resting Potentials, and Synaptic Transmission
        # =====================================================================
        {
            "unit_order": 5,
            "unit_name": "Neurone Anatomy, Resting Potentials, and Synaptic Transmission",
            "unit_description": "Sensory, motor, and relay neurone structure, myelin sheath, resting/action potentials (-70 mV to +30 mV), and synaptic cleft transmission.",
            "lesson_title": "Neurone Anatomy, Resting Potentials, and Synaptic Transmission",
            "pages": [
                [
                    {
                        "type": "learning_goal",
                        "title": "Learning Objectives: Neurones & Synapses",
                        "content": {
                            "title": "Learning Objectives: Neurones & Synapses",
                            "goals": [
                                "Describe structural features of sensory, motor, and relay neurones.",
                                "Explain myelin sheath function and saltatory impulse conduction.",
                                "Detail resting potential (-70 mV) and action potential depolarization (+30 mV).",
                                "Explain chemical synaptic cleft transmission via acetylcholine and cholinesterase."
                            ]
                        }
                    },
                    {
                        "type": "concept_explanation",
                        "title": "Neurones: Structural Units of Nervous System",
                        "content": {
                            "title": "Neurones: Structural Units of Nervous System",
                            "text": "Neurones are specialized nerve cells adapted for generating and conducting high-speed electrical nerve impulses throughout the body."
                        }
                    }
                ],
                [
                    {
                        "type": "suggested_diagram",
                        "title": "Motor, Sensory, and Relay Neurone Structural Anatomy",
                        "content": {
                            "title": "Motor, Sensory, and Relay Neurone Structural Anatomy",
                            "caption": "Comparative Neurone Architecture: Motor Neurone (Terminal Cell Body, Long Axon, Myelin Sheath) vs Sensory Neurone (Central Cell Body) vs Relay Neurone",
                            "description": "Diagram illustrating Motor Neurone, Sensory Neurone, and Relay Neurone displaying cell body, dendrites, axon, myelin sheath, and synaptic knobs."
                        }
                    },
                    {
                        "type": "suggested_image",
                        "title": "Neurone Nucleus Karyogram Visualization",
                        "content": {
                            "title": "Neurone Nucleus Karyogram Visualization",
                            "caption": "Karyogram of human somatic chromosomes contained within neuronal cell body nuclei.",
                            "url": "https://upload.wikimedia.org/wikipedia/commons/b/b1/Human_karyotype_with_bands_and_sub-bands.png",
                            "author": "CC BY-SA 4.0, Wikimedia Commons",
                            "licensing": "CC BY-SA 4.0",
                            "commons_page_url": "https://commons.wikimedia.org/wiki/File:Human_karyotype_with_bands_and_sub-bands.png"
                        }
                    }
                ],
                [
                    {
                        "type": "definition_card",
                        "title": "Neurone Types Taxonomy",
                        "content": {
                            "term": "Functional Neurone Taxonomy",
                            "definition": "Classification of nerve cells by direction of impulse transmission.",
                            "key_points": [
                                "Sensory (Afferent) Neurone: Transmits impulses from sensory receptors to CNS. Long dendron, short axon, off-center cell body in dorsal root ganglion.",
                                "Motor (Efferent) Neurone: Transmits impulses from CNS to effectors (muscles/glands). Short dendrites, long axon, cell body in CNS.",
                                "Relay (Interneurone): Connects sensory and motor neurones inside CNS gray matter. Short unmyelinated process."
                            ]
                        }
                    }
                ],
                [
                    {
                        "type": "concept_explanation",
                        "title": "Myelin Sheath & Saltatory Conduction",
                        "content": {
                            "title": "Myelin Sheath & Saltatory Conduction",
                            "text": "The axon of many neurones is insulated by a fatty myelin sheath secreted by Schwann cells. Gaps in the myelin sheath called Nodes of Ranvier allow electrical impulses to 'jump' rapidly from node to node (Saltatory Conduction), accelerating speed up to 120 m/s."
                        }
                    }
                ],
                [
                    {
                        "type": "concept_explanation",
                        "title": "Resting Potential & Action Potential Mechanics",
                        "content": {
                            "title": "Resting Potential & Action Potential Mechanics",
                            "text": "• Resting Potential (-70 mV): The axon membrane is polarized. Sodium-potassium pumps ($Na^+/K^+$ ATPases) pump $3 Na^+$ OUT for every $2 K^+$ IN, making the inside negatively charged relative to the outside.\n\n• Action Potential (+30 mV): When stimulated above threshold, voltage-gated $Na^+$ channels open. $Na^+$ rushes IN, depolarizing the membrane to +30 mV. Voltage-gated $K^+$ channels then open, $K^+$ rushes OUT (repolarization), restoring resting potential."
                        }
                    },
                    {
                        "type": "suggested_diagram",
                        "title": "Action Potential Waveform: Depolarization, Repolarization, & Hyperpolarization",
                        "content": {
                            "title": "Action Potential Waveform: Depolarization, Repolarization, & Hyperpolarization",
                            "caption": "Electrical Voltage Graph: Resting Potential (-70 mV) → Rapid Na+ Influx Depolarization (+30 mV) → K+ Efflux Repolarization → Refractory Period",
                            "description": "Oscilloscope voltage graph displaying resting baseline at -70mV, spike to +30mV, undershoot repolarization, and return to resting state."
                        }
                    }
                ],
                [
                    {
                        "type": "suggested_diagram",
                        "title": "Synaptic Cleft Transmission & Neurotransmitter Vesicle Release",
                        "content": {
                            "title": "Synaptic Cleft Transmission & Neurotransmitter Vesicle Release",
                            "caption": "Synapse Architecture: Action Potential Arrives → Ca2+ Influx → Acetylcholine Vesicles Fuse with Presynaptic Membrane → Neurotransmitter Diffusion across 20nm Cleft → Receptor Binding",
                            "description": "Diagram of presynaptic knob, synaptic vesicles containing acetylcholine, synaptic cleft, and postsynaptic membrane receptors."
                        }
                    },
                    {
                        "type": "concept_explanation",
                        "title": "Synaptic Transmission & Cholinesterase",
                        "content": {
                            "title": "Synaptic Transmission & Cholinesterase",
                            "text": "A synapse is a microscopic gap (20 nm) between two neurones. Impulses cross chemically:\n1. Impulse reaches presynaptic knob, triggering $Ca^{2+}$ influx;\n2. Synaptic vesicles fuse and release acetylcholine into the cleft;\n3. Acetylcholine diffuses across and binds to postsynaptic receptors, initiating a new action potential;\n4. Cholinesterase enzyme immediately breaks down acetylcholine to prevent continuous unwanted firing."
                        }
                    }
                ],
                [
                    {
                        "type": "mini_activity",
                        "title": "Interactive Synaptic Transmission Simulator",
                        "content": {
                            "activity_type": "scenario_decision",
                            "title": "Interactive Synaptic Transmission Simulator",
                            "prompt": "What would occur at a synapse if an organophosphate insecticide inhibits the enzyme cholinesterase?",
                            "options": [
                                "Option A: Acetylcholine accumulates in the synaptic cleft, causing continuous, uncontrolled muscle spasms.",
                                "Option B: Nerve impulses stop completely.",
                                "Option C: The myelin sheath melts."
                            ],
                            "correct_option": "Option A: Acetylcholine accumulates in the synaptic cleft, causing continuous, uncontrolled muscle spasms.",
                            "explanation": "Cholinesterase inhibition prevents neurotransmitter breakdown, leading to continuous post-synaptic stimulation and lethal muscular spasms."
                        }
                    }
                ],
                [
                    {
                        "type": "knowledge_check",
                        "title": "Knowledge Checkpoint: Neurone Physiology",
                        "content": {
                            "question": "What ionic movement causes rapid depolarization (+30 mV) during an action potential?",
                            "options": [
                                "Rapid influx of Sodium ions (Na+) into the axon.",
                                "Efflux of Potassium ions (K+) out of the axon.",
                                "Loss of water.",
                                "Inflow of sugar."
                            ],
                            "correct_answer": 0,
                            "explanation": "Depolarization is caused by rapid influx of Na+ ions into the axon cell interior."
                        }
                    }
                ],
                [
                    {
                        "type": "summary",
                        "title": "Neuronal Conduction: Key Takeaways",
                        "content": {
                            "title": "Neuronal Conduction: Key Takeaways",
                            "summary_points": [
                                "Sensory neurones carry impulses to CNS; Motor neurones carry impulses to effectors; Relay neurones connect them.",
                                "Myelin sheath enables high-speed saltatory conduction across Nodes of Ranvier.",
                                "Resting potential (-70 mV) is maintained by Na+/K+ pumps; Action potential (+30 mV) is driven by Na+ influx.",
                                "Synapses transmit impulses unidirectionally via acetylcholine neurotransmitters, hydrolyzed by cholinesterase."
                            ]
                        }
                    }
                ]
            ]
        },

        # =====================================================================
        # LESSON 6: Brain and Spinal Cord Anatomy, Reflex Arcs, and Conditioning
        # =====================================================================
        {
            "unit_order": 6,
            "unit_name": "Brain and Spinal Cord Anatomy, Reflex Arcs, and Conditioning",
            "unit_description": "Central nervous system (CNS), brain anatomy (cerebrum, cerebellum, medulla), spinal cord reflex arcs, and Pavlovian conditioning.",
            "lesson_title": "Brain and Spinal Cord Anatomy, Reflex Arcs, and Conditioning",
            "pages": [
                [
                    {
                        "type": "learning_goal",
                        "title": "Learning Objectives: CNS & Reflexes",
                        "content": {
                            "title": "Learning Objectives: CNS & Reflexes",
                            "goals": [
                                "Identify brain structures (cerebrum, cerebellum, medulla oblongata, hypothalamus) and functions.",
                                "Describe spinal cord cross-sectional anatomy (gray matter H-shape, white matter).",
                                "Trace the 5-step simple reflex arc pathway (knee-jerk, pupil reflex).",
                                "Contrast simple unconditioned reflexes with Pavlovian conditioned reflexes."
                            ]
                        }
                    },
                    {
                        "type": "concept_explanation",
                        "title": "Central Nervous System (CNS)",
                        "content": {
                            "title": "Central Nervous System (CNS)",
                            "text": "The Central Nervous System consists of the brain and spinal cord, protected by cranial bones, vertebrae, and surrounding cerebrospinal fluid (CSF)."
                        }
                    }
                ],
                [
                    {
                        "type": "suggested_diagram",
                        "title": "Sagittal Anatomy of the Human Brain: Cerebrum, Cerebellum, Medulla",
                        "content": {
                            "title": "Sagittal Anatomy of the Human Brain: Cerebrum, Cerebellum, Medulla",
                            "caption": "Sagittal Section Model: Large Folded Cerebrum (Intelligence/Memory) → Thalamus/Hypothalamus → Cerebellum (Posture/Balance) → Medulla Oblongata (Involuntary Cardiac/Respiration)",
                            "description": "Brain anatomy diagram highlighting cerebrum, corpus callosum, hypothalamus, pituitary gland, cerebellum, and medulla oblongata."
                        }
                    },
                    {
                        "type": "definition_card",
                        "title": "Brain Region Functions Taxonomy",
                        "content": {
                            "term": "Brain Region Functions",
                            "definition": "Functional specialization across brain territories.",
                            "key_points": [
                                "Cerebrum: Outer folded cortex controlling intelligence, memory, reasoning, vision, hearing, and voluntary motor actions.",
                                "Cerebellum: Coordinates muscle harmony, posture, and body balance.",
                                "Medulla Oblongata: Controls vital involuntary reflexes (heart rate, breathing, swallowing, vomiting, blood pressure).",
                                "Hypothalamus: Thermoregulation, osmoregulation, hunger, thirst, and pituitary hormone control."
                            ]
                        }
                    }
                ],
                [
                    {
                        "type": "suggested_diagram",
                        "title": "Spinal Cord Cross-Section & 5-Step Reflex Arc Pathway",
                        "content": {
                            "title": "Spinal Cord Cross-Section & 5-Step Reflex Arc Pathway",
                            "caption": "Reflex Arc Blueprint: Receptor → Sensory Neurone via Dorsal Root → Relay Neurone in Gray Matter H-Core → Motor Neurone via Ventral Root → Effector Muscle",
                            "description": "Cross-sectional diagram of spinal cord showing central butterfly H-shaped gray matter, dorsal root ganglion, ventral root, and reflex neurone pathway."
                        }
                    },
                    {
                        "type": "concept_explanation",
                        "title": "The Simple Reflex Arc",
                        "content": {
                            "title": "The Simple Reflex Arc",
                            "text": "A reflex action is a rapid, automatic, involuntary response to a stimulus, executed without conscious brain thought. Examples include withdrawing a hand from a sharp pin, pupil constriction in bright light, and the knee-jerk reflex."
                        }
                    }
                ],
                [
                    {
                        "type": "comparison_table",
                        "title": "Simple Reflex vs Conditioned Reflex",
                        "content": {
                            "headers": ["Feature", "Simple (Unconditioned) Reflex", "Conditioned Reflex"],
                            "rows": [
                                ["Origin", "Inborn / Innate (Present from birth)", "Acquired through learning and experience"],
                                ["Stimulus Required", "Unconditioned natural stimulus (e.g., pain)", "Conditioned substitute stimulus (e.g., bell sound)"],
                                ["Brain Role", "Spinal cord or lower brain stem only", "Requires cerebral cortex learning"],
                                ["Biological Examples", "Knee-jerk, pupil reflex, swallowing", "Salivating at sound of dinner bell, riding a bicycle"]
                            ]
                        }
                    }
                ],
                [
                    {
                        "type": "worked_example",
                        "title": "Tracing a Reflex Arc: Hand Hot Object Withdrawal",
                        "content": {
                            "question": "Trace the pathway of a nerve impulse when a person accidentally touches a hot stove plate and rapidly withdraws their hand. (5 Marks)",
                            "strategy": "State 5 sequential components: Thermo-receptor -> Sensory neurone -> Relay neurone -> Motor neurone -> Biceps muscle.",
                            "solution": [
                                "1. Receptor: Thermoreceptors in skin detect high heat stimulus. (1 Mark)",
                                "2. Sensory Neurone: Conducts electrical impulse along dorsal root into spinal cord. (1 Mark)",
                                "3. Relay Neurone: Passes impulse across synapses inside gray matter of spinal cord. (1 Mark)",
                                "4. Motor Neurone: Conducts impulse out via ventral root to effector. (1 Mark)",
                                "5. Effector Response: Biceps muscle contracts, pulling hand away from stove. (1 Mark)"
                            ]
                        }
                    }
                ],
                [
                    {
                        "type": "mini_activity",
                        "title": "Interactive Reflex Arc Simulator",
                        "content": {
                            "activity_type": "scenario_decision",
                            "title": "Interactive Reflex Arc Simulator",
                            "prompt": "If a patient's dorsal root of the spinal nerve is severed in an accident, what will be the effect on their arm?",
                            "options": [
                                "Option A: Loss of sensation in the arm, but voluntary muscle movement remains intact.",
                                "Option B: Paralysis of muscle movement, but sensation remains.",
                                "Option C: Complete loss of both sensation and movement."
                            ],
                            "correct_option": "Option A: Loss of sensation in the arm, but voluntary muscle movement remains intact.",
                            "explanation": "Dorsal roots carry incoming sensory neurones; ventral roots carry outgoing motor neurones."
                        }
                    }
                ],
                [
                    {
                        "type": "knowledge_check",
                        "title": "Knowledge Checkpoint: Brain & Reflex Arcs",
                        "content": {
                            "question": "Which region of the human brain coordinates muscle movement harmony, posture, and physical balance?",
                            "options": [
                                "Cerebellum",
                                "Cerebrum",
                                "Medulla Oblongata",
                                "Hypothalamus"
                            ],
                            "correct_answer": 0,
                            "explanation": "The cerebellum controls posture, balance, and muscle coordination."
                        }
                    }
                ],
                [
                    {
                        "type": "summary",
                        "title": "Central Nervous System: Key Takeaways",
                        "content": {
                            "title": "Central Nervous System: Key Takeaways",
                            "summary_points": [
                                "Cerebrum controls intelligence/memory; Cerebellum controls balance; Medulla controls vital involuntary actions.",
                                "Spinal cord features inner H-shaped gray matter and outer white matter.",
                                "Reflex arcs proceed: Receptor -> Sensory Neurone -> Relay Neurone -> Motor Neurone -> Effector.",
                                "Simple reflexes are innate; Conditioned reflexes are learned (Pavlov)."
                            ]
                        }
                    }
                ]
            ]
        },

        # =====================================================================
        # LESSON 7: Endocrine Glands, Hormonal Regulation, and Drug Abuse Pathology
        # =====================================================================
        {
            "unit_order": 7,
            "unit_name": "Endocrine Glands, Hormonal Regulation, and Drug Abuse Pathology",
            "unit_description": "Endocrine vs exocrine glands, pituitary/thyroid/pancreas/adrenal hormones, blood glucose negative feedback, and drug abuse pathology.",
            "lesson_title": "Endocrine Glands, Hormonal Regulation, and Drug Abuse Pathology",
            "pages": [
                [
                    {
                        "type": "learning_goal",
                        "title": "Learning Objectives: Endocrine System & Drugs",
                        "content": {
                            "title": "Learning Objectives: Endocrine System & Drugs",
                            "goals": [
                                "Distinguish between ductless endocrine glands and ducted exocrine glands.",
                                "Detail major endocrine glands, hormones, and physiological target effects.",
                                "Explain negative feedback control of blood glucose (Insulin & Glucagon).",
                                "Analyze drug abuse pathology (stimulants, depressants, hallucinogens) and addiction."
                            ]
                        }
                    },
                    {
                        "type": "concept_explanation",
                        "title": "Endocrine System & Hormones",
                        "content": {
                            "title": "Endocrine System & Hormones",
                            "text": "The endocrine system consists of ductless glands that secrete organic chemical messengers (hormones) directly into blood capillaries to regulate distant target organs."
                        }
                    }
                ],
                [
                    {
                        "type": "suggested_diagram",
                        "title": "Human Endocrine Gland Map & Secreted Hormones",
                        "content": {
                            "title": "Human Endocrine Gland Map & Secreted Hormones",
                            "caption": "Human Body Endocrine Gland Map: Pituitary (Master Gland) → Thyroid (Thyroxine) → Adrenals (Adrenaline) → Pancreas (Insulin/Glucagon) → Gonads",
                            "description": "Anatomical map showing location of Pituitary, Thyroid, Adrenals, Pancreas, Ovaries, and Testes."
                        }
                    },
                    {
                        "type": "definition_card",
                        "title": "Major Endocrine Glands & Hormones Taxonomy",
                        "content": {
                            "term": "Endocrine Gland Taxonomy",
                            "definition": "Overview of major ductless glands and hormone functions.",
                            "key_points": [
                                "Pituitary: TSH, ACTH, FSH, LH, ADH (Osmoregulation), Oxytocin, Growth Hormone.",
                                "Thyroid: Thyroxine (Regulates basal metabolic rate; Deficiency causes Cretinism/Goitre).",
                                "Pancreas (Islets of Langerhans): Insulin (Lowers blood sugar) & Glucagon (Raises blood sugar).",
                                "Adrenals: Adrenaline (Emergency fight-or-flight: increases heart rate, dilates pupils, mobilizes glucose)."
                            ]
                        }
                    }
                ],
                [
                    {
                        "type": "suggested_diagram",
                        "title": "Blood Glucose Negative Feedback Regulation (Insulin & Glucagon)",
                        "content": {
                            "title": "Blood Glucose Negative Feedback Regulation (Insulin & Glucagon)",
                            "caption": "Homeostatic Loop: High Blood Glucose → Beta Cells Secret Insulin → Glucose Converted to Glycogen; Low Blood Glucose → Alpha Cells Secret Glucagon → Glycogen Hydrolyzed to Glucose",
                            "description": "Dual feedback loop showing insulin lowering high blood sugar and glucagon restoring low blood sugar."
                        }
                    },
                    {
                        "type": "suggested_image",
                        "title": "Endocrine Blood Transport Smear Visualization",
                        "content": {
                            "title": "Endocrine Blood Transport Smear Visualization",
                            "caption": "Scanning electron micrograph of blood erythrocytes transporting circulating endocrine hormones to target organs.",
                            "url": "https://upload.wikimedia.org/wikipedia/commons/a/a6/Sickle_cell_anemia_smear.jpg",
                            "author": "Public Domain, Wikimedia Commons",
                            "licensing": "Public domain",
                            "commons_page_url": "https://commons.wikimedia.org/wiki/File:Sickle_cell_anemia_smear.jpg"
                        }
                    }
                ],
                [
                    {
                        "type": "concept_explanation",
                        "title": "Pathology of Drug Abuse",
                        "content": {
                            "title": "Pathology of Drug Abuse",
                            "text": "A drug is any chemical substance that alters physical or mental body functions.\n\n• Stimulants (Cocaine, Nicotine, Caffeine): Accelerate CNS impulse transmission across synapses.\n• Depressants (Alcohol, Barbiturates, Heroin): Slow down CNS transmission, impairing coordination and reaction time.\n• Hallucinogens (LSD, Cannabis): Alter sensory perception, causing vivid hallucinations."
                        }
                    },
                    {
                        "type": "suggested_image",
                        "title": "Drug Abuse Pathology Assay",
                        "content": {
                            "title": "Drug Abuse Pathology Assay",
                            "caption": "Laboratory diagnostic assay showing biochemical screening for pharmaceutical and chemical drug compounds.",
                            "url": "https://upload.wikimedia.org/wikipedia/commons/7/7a/Agar_Diffusion_Method_1.jpg",
                            "author": "CC BY-SA 4.0, Wikimedia Commons",
                            "licensing": "CC BY-SA 4.0",
                            "commons_page_url": "https://commons.wikimedia.org/wiki/File:Agar_Diffusion_Method_1.jpg"
                        }
                    }
                ],
                [
                    {
                        "type": "mini_activity",
                        "title": "Interactive Endocrine & Drug Abuse Challenge",
                        "content": {
                            "activity_type": "scenario_decision",
                            "title": "Interactive Endocrine & Drug Abuse Challenge",
                            "prompt": "What metabolic disorder results when the Islets of Langerhans in the pancreas fail to produce sufficient insulin?",
                            "options": [
                                "Option A: Diabetes Mellitus (High blood sugar, glucose in urine).",
                                "Option B: Diabetes Insipidus (ADH deficiency).",
                                "Option C: Cretinism."
                            ],
                            "correct_option": "Option A: Diabetes Mellitus (High blood sugar, glucose in urine).",
                            "explanation": "Insulin deficiency prevents glucose uptake by cells, causing Diabetes Mellitus."
                        }
                    }
                ],
                [
                    {
                        "type": "knowledge_check",
                        "title": "Knowledge Checkpoint: Endocrine & Drugs",
                        "content": {
                            "question": "Which hormone is secreted by the adrenal medulla during sudden emergency 'fight or flight' situations?",
                            "options": [
                                "Adrenaline",
                                "Insulin",
                                "Thyroxine",
                                "Estrogen"
                            ],
                            "correct_answer": 0,
                            "explanation": "Adrenaline prepares the body for emergency action."
                        }
                    }
                ],
                [
                    {
                        "type": "summary",
                        "title": "Endocrine Regulation: Key Takeaways",
                        "content": {
                            "title": "Endocrine Regulation: Key Takeaways",
                            "summary_points": [
                                "Endocrine glands are ductless, secreting hormones directly into blood to regulate target organs.",
                                "Insulin lowers high blood glucose; Glucagon raises low blood glucose via negative feedback.",
                                "Thyroxine controls metabolic rate; Adrenaline prepares body for emergency fight-or-flight.",
                                "Drugs alter synaptic transmission (stimulants accelerate, depressants slow down, hallucinogens distort)."
                            ]
                        }
                    }
                ]
            ]
        },

        # =====================================================================
        # LESSON 8: Eye Anatomy, Image Formation, Accommodation, and Optical Defects
        # =====================================================================
        {
            "unit_order": 8,
            "unit_name": "Eye Anatomy, Image Formation, Accommodation, and Optical Defects",
            "unit_description": "Eye anatomy (sclera, retina, rods/cones), accommodation mechanics (near vs distant), myopia, hypermetropia, and lens corrections.",
            "lesson_title": "Eye Anatomy, Image Formation, Accommodation, and Optical Defects",
            "pages": [
                [
                    {
                        "type": "learning_goal",
                        "title": "Learning Objectives: Photoreception & Eye",
                        "content": {
                            "title": "Learning Objectives: Photoreception & Eye",
                            "goals": [
                                "Describe structural layers of the human eye (Sclera, Choroid, Retina).",
                                "Contrast retinal photoreceptors (Rods for dim light vs Cones for color vision).",
                                "Explain eye accommodation mechanics for distant vs near vision.",
                                "Analyze optical defects (Myopia & Hypermetropia) and their corrective lenses."
                            ]
                        }
                    },
                    {
                        "type": "concept_explanation",
                        "title": "The Human Eye as a Photoreceptor Organ",
                        "content": {
                            "title": "The Human Eye as a Photoreceptor Organ",
                            "text": "The human eye is a specialized sense organ housed in the skull orbit, adapted to focus light rays onto photoreceptor cells in the retina."
                        }
                    }
                ],
                [
                    {
                        "type": "suggested_diagram",
                        "title": "Sagittal Anatomy of the Human Eye",
                        "content": {
                            "title": "Sagittal Anatomy of the Human Eye",
                            "caption": "Eyeball Cross Section Model: Sclera (Protective Outer Layer) → Cornea → Choroid (Pigmented Black) → Retina (Photoreceptors) → Fovea Centralis → Optic Nerve",
                            "description": "Anatomical diagram of eyeball showing cornea, iris, pupil, biconvex lens, ciliary body, retina, fovea, blind spot, and optic nerve."
                        }
                    },
                    {
                        "type": "suggested_image",
                        "title": "Human Eye Anatomy Visualization",
                        "content": {
                            "title": "Human Eye Anatomy Visualization",
                            "caption": "Detailed anatomical diagram of the human eye showing corneal refraction and retinal photoreceptor layers.",
                            "url": "https://upload.wikimedia.org/wikipedia/commons/7/70/Anatomy_of_eye_of_human_being.jpg",
                            "author": "CC BY-SA 4.0, Wikimedia Commons",
                            "licensing": "CC BY-SA 4.0",
                            "commons_page_url": "https://commons.wikimedia.org/wiki/File:Anatomy_of_eye_of_human_being.jpg"
                        }
                    }
                ],
                [
                    {
                        "type": "definition_card",
                        "title": "Retinal Photoreceptors Taxonomy",
                        "content": {
                            "term": "Rods vs Cones Taxonomy",
                            "definition": "Photoreceptor cells embedded in retina.",
                            "key_points": [
                                "Rods: 120 million cells; Sensitive to low light intensity; Contain Rhodopsin pigment; Provide black-and-white night vision.",
                                "Cones: 6 million cells concentrated at Fovea centralis; Require bright light; Contain Iodopsin pigment; Provide sharp color vision (Red, Green, Blue cones)."
                            ]
                        }
                    }
                ],
                [
                    {
                        "type": "suggested_diagram",
                        "title": "Eye Accommodation Mechanics: Distant vs Near Vision",
                        "content": {
                            "title": "Eye Accommodation Mechanics: Distant vs Near Vision",
                            "caption": "Comparative Lens Model: Distant Vision (Ciliary Muscle Relaxes → Suspensory Ligaments Tense → Lens Flattens) vs Near Vision (Ciliary Muscle Contracts → Suspensory Ligaments Relax → Lens Bulges)",
                            "description": "Diagram illustrating lens curvature changes during distant vs near accommodation."
                        }
                    },
                    {
                        "type": "concept_explanation",
                        "title": "Eye Accommodation Mechanics",
                        "content": {
                            "title": "Eye Accommodation Mechanics",
                            "text": "Accommodation is the adjustment of the focal length of the eye lens to focus real, inverted, diminished images of objects at varying distances clearly on the retina."
                        }
                    }
                ],
                [
                    {
                        "type": "suggested_diagram",
                        "title": "Myopia and Hypermetropia Lens Corrections",
                        "content": {
                            "title": "Myopia and Hypermetropia Lens Corrections",
                            "caption": "Ray Tracing Model: Myopia (Long Eyeball → Focus In Front of Retina → Corrected by Diverging Concave Lens) vs Hypermetropia (Short Eyeball → Corrected by Converging Convex Lens)",
                            "description": "Ray tracing diagram showing light rays focusing in front of retina in myopia corrected with concave lens, and behind retina in hypermetropia corrected with convex lens."
                        }
                    },
                    {
                        "type": "definition_card",
                        "title": "Optical Defects Taxonomy",
                        "content": {
                            "term": "Optical Defects Taxonomy",
                            "definition": "Refractive errors of the human eye.",
                            "key_points": [
                                "Myopia (Short-Sightedness): Can see near objects clearly, distant blurred. Long eyeball; image forms IN FRONT of retina. Corrected by CONCAVE (Diverging) lens.",
                                "Hypermetropia (Long-Sightedness): Can see distant objects clearly, near blurred. Short eyeball/stiff lens; image forms BEHIND retina. Corrected by CONVEX (Converging) lens.",
                                "Astigmatism: Uneven corneal curvature; Corrected by Cylindrical lens.",
                                "Cataracts: Opaque cloudy lens; Corrected by Surgical lens replacement."
                            ]
                        }
                    }
                ],
                [
                    {
                        "type": "mini_activity",
                        "title": "Interactive Eye Accommodation Simulator",
                        "content": {
                            "activity_type": "scenario_decision",
                            "title": "Interactive Eye Accommodation Simulator",
                            "prompt": "What happens to the ciliary muscles and suspensory ligaments when your eye shifts focus from a smartphone screen (near object) to a distant mountain?",
                            "options": [
                                "Option A: Ciliary muscles RELAX, suspensory ligaments become TAUT, causing the lens to flatten.",
                                "Option B: Ciliary muscles contract, suspensory ligaments relax, lens bulges.",
                                "Option C: The eye lens pops out."
                            ],
                            "correct_option": "Option A: Ciliary muscles RELAX, suspensory ligaments become TAUT, causing the lens to flatten.",
                            "explanation": "Distant vision requires relaxed ciliary muscles, taut suspensory ligaments, and a thinner flattened lens."
                        }
                    }
                ],
                [
                    {
                        "type": "knowledge_check",
                        "title": "Knowledge Checkpoint: Eye Anatomy & Defects",
                        "content": {
                            "question": "Which optical defect causes light rays from distant objects to focus IN FRONT of the retina, and which lens corrects it?",
                            "options": [
                                "Myopia; Corrected by a Concave (Diverging) lens.",
                                "Hypermetropia; Corrected by a Convex lens.",
                                "Cataracts; Corrected by sunglasses.",
                                "Astigmatism; Corrected by bifocals."
                            ],
                            "correct_answer": 0,
                            "explanation": "Myopia (short-sightedness) focuses light in front of retina and requires a concave lens."
                        }
                    }
                ],
                [
                    {
                        "type": "summary",
                        "title": "Photoreception: Key Takeaways",
                        "content": {
                            "title": "Photoreception: Key Takeaways",
                            "summary_points": [
                                "Retina contains Rods (dim light, rhodopsin) and Cones (bright light, color vision, fovea).",
                                "Accommodation adjusts lens thickness: Near (ciliary contracts, lens bulges); Distant (ciliary relaxes, lens flattens).",
                                "Myopia (image in front of retina) is corrected by Concave lens.",
                                "Hypermetropia (image behind retina) is corrected by Convex lens."
                            ]
                        }
                    }
                ]
            ]
        },

        # =====================================================================
        # LESSON 9: Ear Anatomy, Sound Transduction, Balance Mechanisms, and Pathology
        # =====================================================================
        {
            "unit_order": 9,
            "unit_name": "Ear Anatomy, Sound Transduction, Balance Mechanisms, and Pathology",
            "unit_description": "Ear anatomy (outer, middle, inner), ossicles, sound transduction in cochlea, semi-circular canal balance, and deafness.",
            "lesson_title": "Ear Anatomy, Sound Transduction, Balance Mechanisms, and Pathology",
            "pages": [
                [
                    {
                        "type": "learning_goal",
                        "title": "Learning Objectives: Mechanoreception & Ear",
                        "content": {
                            "title": "Learning Objectives: Mechanoreception & Ear",
                            "goals": [
                                "Identify structures of outer, middle, and inner ear.",
                                "Trace sound wave transduction through ear ossicles to Organ of Corti.",
                                "Explain dynamic balance in semi-circular canals and static balance in maculae/otoliths.",
                                "Distinguish between conduction deafness and nerve deafness."
                            ]
                        }
                    },
                    {
                        "type": "concept_explanation",
                        "title": "The Human Ear: Hearing & Balance",
                        "content": {
                            "title": "The Human Ear: Hearing & Balance",
                            "text": "The ear is a dual mechanoreceptor sense organ responsible for sound perception (hearing) and maintaining body balance and posture."
                        }
                    }
                ],
                [
                    {
                        "type": "suggested_diagram",
                        "title": "Anatomy of the Human Ear: Outer, Middle, and Inner Ear",
                        "content": {
                            "title": "Anatomy of the Human Ear: Outer, Middle, and Inner Ear",
                            "caption": "Ear Structure Model: Outer Ear (Pinna, Auditory Canal) → Middle Ear (Tympanic Membrane, Ossicles: Malleus, Incus, Stapes, Eustachian Tube) → Inner Ear (Cochlea, Semi-Circular Canals)",
                            "description": "Anatomical diagram of human ear showing pinna, eardrum, malleus, incus, stapes, oval window, cochlea, auditory nerve, and semi-circular canals."
                        }
                    },
                    {
                        "type": "suggested_image",
                        "title": "Human Ear Anatomy Visualization",
                        "content": {
                            "title": "Human Ear Anatomy Visualization",
                            "caption": "Anatomical SVG diagram of the human ear illustrating middle ear ossicles and inner ear cochlear fluid canals.",
                            "url": "https://upload.wikimedia.org/wikipedia/commons/d/d2/Anatomy_of_the_Human_Ear.svg",
                            "author": "Public Domain, Wikimedia Commons",
                            "licensing": "Public domain",
                            "commons_page_url": "https://commons.wikimedia.org/wiki/File:Anatomy_of_the_Human_Ear.svg"
                        }
                    }
                ],
                [
                    {
                        "type": "concept_explanation",
                        "title": "Sound Wave Transduction Pathway",
                        "content": {
                            "title": "Sound Wave Transduction Pathway",
                            "text": "1. Pinna collects sound waves and directs them into auditory canal;\n2. Sound waves strike Tympanic Membrane (eardrum), causing vibration;\n3. Ear Ossicles (Malleus -> Incus -> Stapes) amplify vibrations 20-fold;\n4. Stapes pushes Oval Window, creating fluid pressure waves in Cochlea;\n5. Perilymph waves stimulate hair cells in Organ of Corti, generating electrical nerve impulses sent via Auditory Nerve to auditory cortex."
                        }
                    },
                    {
                        "type": "suggested_diagram",
                        "title": "Cochlear Sound Transduction & Semi-Circular Canal Balance",
                        "content": {
                            "title": "Cochlear Sound Transduction & Semi-Circular Canal Balance",
                            "caption": "Inner Ear Transduction: Cochlear Fluid Waves Stimulate Hair Cells in Organ of Corti → Auditory Nerve; Ampulla Cristae in Semi-Circular Canals Maintain Dynamic Balance",
                            "description": "Diagram illustrating cross-section of cochlea showing Organ of Corti sensory hair cells and semi-circular canal ampullae."
                        }
                    }
                ],
                [
                    {
                        "type": "concept_explanation",
                        "title": "Mechanism of Balance & Posture",
                        "content": {
                            "title": "Mechanism of Balance & Posture",
                            "text": "• Dynamic Balance (Head Movement): Three mutually perpendicular Semi-Circular Canals contain fluid (endolymph). Head movement shifts fluid, bending gelatinous cupula hair cells inside ampullae, sending balance impulses to cerebellum.\n\n• Static Balance (Head Position & Gravity): Utriculus and Sacculus contain calcium carbonate otolith stones resting on hair cells. Gravity pulls otoliths, signaling head orientation."
                        }
                    }
                ],
                [
                    {
                        "type": "mini_activity",
                        "title": "Interactive Ear Transduction Simulator",
                        "content": {
                            "activity_type": "scenario_decision",
                            "title": "Interactive Ear Transduction Simulator",
                            "prompt": "What is the physiological function of the Eustachian tube connecting the middle ear to the pharynx?",
                            "options": [
                                "Option A: Equalizes air pressure on both sides of the tympanic membrane (eardrum) to prevent rupturing.",
                                "Option B: Amplifies sound vibrations.",
                                "Option C: Secretes ear wax."
                            ],
                            "correct_option": "Option A: Equalizes air pressure on both sides of the tympanic membrane (eardrum) to prevent rupturing.",
                            "explanation": "Eustachian tube equalizes atmospheric pressure across the eardrum."
                        }
                    }
                ],
                [
                    {
                        "type": "knowledge_check",
                        "title": "Knowledge Checkpoint: Ear Anatomy & Hearing",
                        "content": {
                            "question": "Which inner ear sensory structure contains hair cells that convert fluid pressure waves into auditory nerve impulses?",
                            "options": [
                                "Organ of Corti (inside Cochlea)",
                                "Semi-circular canals",
                                "Tympanic membrane",
                                "Eustachian tube"
                            ],
                            "correct_answer": 0,
                            "explanation": "Organ of Corti hair cells in the cochlea convert sound vibrations into auditory nerve impulses."
                        }
                    }
                ],
                [
                    {
                        "type": "summary",
                        "title": "Mechanoreception: Key Takeaways",
                        "content": {
                            "title": "Mechanoreception: Key Takeaways",
                            "summary_points": [
                                "Sound waves vibrate tympanic membrane, amplified by ossicles (malleus, incus, stapes).",
                                "Cochlear fluid waves bend Organ of Corti hair cells, sending impulses along auditory nerve.",
                                "Semi-circular canals maintain dynamic balance; Utriculus/Sacculus otoliths maintain static balance.",
                                "Eustachian tube equalizes middle ear air pressure."
                            ]
                        }
                    }
                ]
            ]
        },

        # =====================================================================
        # LESSON 10: Topic Synthesis, Master Key Glossary, and Multi-Tier Examination Diagnostic
        # =====================================================================
        {
            "unit_order": 10,
            "unit_name": "Topic Synthesis, Master Key Glossary, and Multi-Tier Examination Diagnostic",
            "unit_description": "Topic synthesis, KCSE essay diagnostics (eye accommodation, reflex arcs, auxins), common student traps, and comprehensive assessment.",
            "lesson_title": "Topic Synthesis, Master Key Glossary, and Multi-Tier Examination Diagnostic",
            "pages": [
                [
                    {
                        "type": "learning_goal",
                        "title": "Learning Objectives: Response Systems Synthesis",
                        "content": {
                            "title": "Learning Objectives: Response Systems Synthesis",
                            "goals": [
                                "Synthesize plant and animal coordination systems.",
                                "Master KCSE essay questions on reflex arcs, eye accommodation, and phototropism.",
                                "Avoid common student exam traps in sensory biology.",
                                "Complete end-of-topic revision assessment."
                            ]
                        }
                    },
                    {
                        "type": "concept_explanation",
                        "title": "Master Synthesis of Response Systems",
                        "content": {
                            "title": "Master Synthesis of Response Systems",
                            "text": "Living organisms rely on nervous electrical networks, endocrine chemical hormones, and plant growth auxins to sense environmental shifts, process information, and execute survival responses."
                        }
                    }
                ],
                [
                    {
                        "type": "worked_example",
                        "title": "Worked KCSE Essay 1: Eye Accommodation Mechanics",
                        "content": {
                            "question": "Describe how the human eye accommodates to focus clearly on a near object (book) versus a distant object (mountain). (10 Marks)",
                            "strategy": "Structure answer contrasting Near vs Distant vision: Ciliary muscles, Suspensory ligaments, and Lens thickness.",
                            "solution": [
                                "1. Near Vision Accommodation (5 Marks):\n   • Ciliary muscles CONTRACT.\n   • Suspensory ligaments become SLACK / RELAX.\n   • Tension on lens is REDUCED.\n   • Elastic eye lens BULGES (becomes more convex/thicker).\n   • Refractive power increases, focusing light rays sharply on retina.",
                                "2. Distant Vision Accommodation (5 Marks):\n   • Ciliary muscles RELAX.\n   • Suspensory ligaments become TAUT / STRETCHED.\n   • Tension on lens INCREASES.\n   • Lens is PULLED THIN / FLATTENS.\n   • Refractive power decreases, focusing parallel light rays on retina."
                            ]
                        }
                    }
                ],
                [
                    {
                        "type": "worked_example",
                        "title": "Worked KCSE Essay 2: Phototropism Auxin Mechanism",
                        "content": {
                            "question": "Explain the role of auxins in causing positive phototropism in a seedling shoot exposed to unilateral light. (10 Marks)",
                            "strategy": "Detail Auxin synthesis at shoot apex, migration away from light, differential cell elongation, and lightward bending.",
                            "solution": [
                                "1. Auxin Synthesis (2 Marks): Auxins (IAA) are synthesized at shoot tip.",
                                "2. Unilateral Light Exposure (2 Marks): Light strikes stem from one side.",
                                "3. Lateral Migration (2 Marks): Auxins diffuse laterally away from light to shaded side.",
                                "4. Differential Cell Elongation (2 Marks): High auxin concentration on shaded side causes shaded cells to elongate faster than illuminated side.",
                                "5. Curvature Response (2 Marks): Differential growth forces shoot stem to bend towards light."
                            ]
                        }
                    }
                ],
                [
                    {
                        "type": "common_mistake",
                        "title": "Common Student Traps in Coordination Exams",
                        "content": {
                            "mistake": "Stating that suspensory ligaments contract during accommodation.",
                            "correction": "Suspensory ligaments NEVER contract; they are non-muscular collagenous cords that become taut or slack when ciliary muscles relax or contract.",
                            "reasoning": "Only muscles (ciliary muscles) can contract."
                        }
                    }
                ],
                [
                    {
                        "type": "knowledge_check",
                        "title": "Topic 3 Mastery Assessment Question",
                        "content": {
                            "question": "Which change occurs in the human eye when focusing on a near object?",
                            "options": [
                                "Ciliary muscles contract, suspensory ligaments relax, lens becomes thicker/bulges.",
                                "Ciliary muscles relax, suspensory ligaments become taut, lens flattens.",
                                "Iris contracts to close pupil completely.",
                                "Retina detaches."
                            ],
                            "correct_answer": 0,
                            "explanation": "Focusing on near objects requires ciliary muscle contraction and lens bulging."
                        }
                    }
                ],
                [
                    {
                        "type": "summary",
                        "title": "Topic 3 Mastery Synthesis & Complete Review",
                        "content": {
                            "title": "Topic 3 Mastery Synthesis & Complete Review",
                            "summary_points": [
                                "Response circuit: Stimulus -> Receptor -> Coordinator -> Effector -> Response.",
                                "Plant movements include Tropisms (directional growth), Taxes (directional locomotion), and Nasty (non-directional turgor shifts).",
                                "Auxins migrate to shaded stem sides causing phototropism; high auxin inhibits root growth.",
                                "Neurones conduct impulses via resting potential (-70 mV) and action potential (+30 mV Na+ influx).",
                                "Synapses transmit via acetylcholine; Brain & Spinal cord coordinate reflex arcs.",
                                "Eye accommodates via ciliary muscles & suspensory ligaments; Myopia corrected by concave lens.",
                                "Ear transduces sound via cochlea Organ of Corti and maintains balance via semi-circular canals."
                            ]
                        }
                    }
                ]
            ]
        }
    ]

def ingest_form4_biology_topic3(replace=False):
    print("=" * 80)
    print("VLearn Form 4 Biology — Topic 3: Reception, Response and Coordination in Plants and Animals")
    print("High-Structure Production Ingestion Engine")
    print("=" * 80)

    curriculum = Curriculum.objects.filter(name="844").first()
    grade = Grade.objects.filter(curriculum=curriculum, name="Form 4").first()
    subject = Subject.objects.filter(grade=grade, name="Biology").first()

    if not subject:
        print("[!] Error: Subject 'Biology' not found under Form 4.")
        return

    print(f"[*] Resolved Target: {curriculum.name} -> {grade.name} -> {subject.name} (ID: {subject.id})")

    topic_name = "Reception, Response and Coordination in Plants and Animals"
    topic = Topic.objects.filter(subject=subject, name=topic_name).first()

    if topic and replace:
        print(f"[*] Found existing Topic '{topic_name}' (ID: {topic.id}). Removing for clean replace...")
        topic.delete()
        topic = None

    if not topic:
        topic = Topic.objects.create(
            subject=subject,
            name=topic_name,
            order=3,
            description="Comprehensive syllabus on sensitivity, plant tropisms/nastic movements, auxin growth physiology, neurone anatomy, resting/action potentials, synaptic transmission, CNS brain/spinal cord reflex arcs, endocrine hormonal regulation, eye photoreception & accommodation, and ear mechanoreception & balance."
        )
        print(f"[+] Created Topic: {topic.name} (ID: {topic.id})")
    else:
        print(f"[*] Using existing Topic: {topic.name} (ID: {topic.id})")

    curriculum_data = build_topic3_curriculum()
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
            else:
                lesson = Lesson.objects.create(
                    topic=topic,
                    learning_unit=learning_unit,
                    title=lesson_title,
                    status="published",
                    version=1
                )
            print(f"  [+] Ingesting Lesson {unit_order}: {lesson.title} (ID: {lesson.id})")

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
            print(f"      [OK] Ingested {lesson_page_count} Pages for Lesson {unit_order}.")

    print("=" * 80)
    print("[SUCCESS] Form 4 Biology Topic 3 (Reception, Response and Coordination) Ingestion Complete!")
    print(f"[*] Total Lessons Ingested: {total_lessons}")
    print(f"[*] Total Pages Ingested:   {total_pages}")
    print(f"[*] Total Blocks Ingested:  {total_blocks}")
    print("=" * 80)

if __name__ == "__main__":
    replace_flag = "--replace" in sys.argv
    ingest_form4_biology_topic3(replace=replace_flag)
