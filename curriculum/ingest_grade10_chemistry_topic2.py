"""
VLearn CBC Grade 10 Chemistry — Topic 2: The Atom
Production Ingestion Engine (Senior Secondary Pedagogical Edition)

Curriculum: CBC (ID: 5)
Grade: Grade 10 (ID: 5, Level: 10)
Subject: Chemistry (ID: 5)
Topic: The Atom (Topic Order: 2)

Decomposed into 5 Learning Units & 5 Published Lessons:
  1. Atomic Theory and Models (5 Pages, 11 Blocks)
  2. Subatomic Particles, Atomic Number, and Mass Number (5 Pages, 11 Blocks)
  3. Isotopes and Relative Atomic Mass (5 Pages, 11 Blocks)
  4. Energy Levels, Orbitals, and s/p Notation (5 Pages, 11 Blocks)
  5. Integrated Atomic Representation and Review (5 Pages, 11 Blocks)
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
    text = re.sub(r'\[VISUAL:\s*[A-Z]+\][^\n]*', '', text)
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

def build_topic2_curriculum():
    """Returns the comprehensive pedagogical page and block structure for Grade 10 Topic 2: The Atom."""
    return [
        # =====================================================================
        # LESSON 1: Atomic Theory and Models
        # =====================================================================
        {
            "unit_order": 1,
            "unit_name": "Atomic Theory and Models",
            "unit_description": "Trace the evolution of atomic theory from Dalton's solid indivisible sphere model to Rutherford's nuclear model based on the alpha-particle gold foil scattering experiment.",
            "lesson_title": "Atomic Theory and Models",
            "pages": [
                # Card 1: Hook & Scale of the Atom
                [
                    {
                        "type": "suggested_image",
                        "title": "Unlocking the Subatomic World",
                        "content": {
                            "title": "Unlocking the Subatomic World",
                            "caption": "Historical portrait of Sir Ernest Rutherford, discoverer of the atomic nucleus and pioneer of nuclear physics."
                        }
                    },
                    {
                        "type": "learning_goal",
                        "title": "Lesson Objectives: The Evolution of Atomic Models",
                        "content": {
                            "title": "What We Will Master Today",
                            "goals": [
                                "Appreciate the microscopic scale of atoms and the necessity of **scientific models**.",
                                "Analyze **John Dalton's Atomic Theory (1803)** and identify its foundational contributions and limitations.",
                                "Examine **Ernest Rutherford's Gold Foil Experiment (1911)**, connecting observations to submicroscopic deductions.",
                                "Explain the **Rutherford Nuclear Model of the Atom** (central positive nucleus and empty space)."
                            ]
                        }
                    },
                    {
                        "type": "concept_explanation",
                        "title": "How Small is an Atom? The Need for Scientific Models",
                        "content": {
                            "title": "The Scale of the Invisible",
                            "text": "A single grain of beach sand contains approximately **$2.2 \\times 10^{19}$ atoms** (22 quintillion atoms)! If you blew up a grain of sand to the size of planet Earth, a single atom inside it would be roughly the size of a football.\n\nBecause atoms cannot be observed with ordinary light microscopes, scientists construct **scientific models**—explanatory representations grounded in experimental evidence that predict how matter behaves."
                        }
                    }
                ],
                # Card 2: John Dalton's Atomic Model
                [
                    {
                        "type": "concept_explanation",
                        "title": "John Dalton's Solid Sphere Model (1803)",
                        "content": {
                            "title": "The First Scientific Atomic Theory",
                            "text": "In 1803, English chemist John Dalton formulated the first modern atomic theory based on mass ratios in chemical reactions:\n\n1. All matter is composed of tiny, indivisible, indestructible particles called **atoms**.\n2. Atoms of the same element are identical in mass, size, and chemical properties.\n3. Atoms of different elements possess different masses and properties.\n4. Chemical reactions consist of the **combination, separation, or rearrangement of intact atoms** in fixed whole-number ratios."
                        }
                    },
                    {
                        "type": "definition_card",
                        "title": "Core Model: Dalton's 'Billiard Ball' Model",
                        "content": {
                            "term": "Dalton's Atomic Model",
                            "definition": "A conceptual model portraying the atom as a tiny, hard, solid, indivisible sphere with uniform mass distribution and no internal subatomic structure.",
                            "example": "Imagining carbon atoms as tiny, indestructible solid spheres colliding to form compounds."
                        }
                    }
                ],
                # Card 3: Rutherford's Gold Foil Experiment
                [
                    {
                        "type": "concept_explanation",
                        "title": "Ernest Rutherford's Gold Foil Scattering Experiment (1911)",
                        "content": {
                            "title": "Shattering the Solid Sphere Model",
                            "text": "In 1911, Ernest Rutherford, Hans Geiger, and Ernest Marsden tested atomic structure by bombarding an ultra-thin gold foil (about 400 atoms thick) with high-energy, positively charged **alpha particles** ($\\alpha$, helium nuclei):\n\n### The Surprising Observations:\n- **$99.9\\%$ of alpha particles passed straight through** the gold foil without any deflection.\n- **A small fraction was deflected at very large angles** ($>90^\\circ$).\n- **About 1 in 8,000 bounced almost directly backwards** toward the radioactive source!"
                        }
                    },
                    {
                        "type": "suggested_diagram",
                        "title": "Rutherford Gold Foil Experiment & Alpha Particle Scattering",
                        "content": {
                            "title": "Rutherford Gold Foil Experiment & Alpha Particle Scattering",
                            "caption": "Schematic of alpha particle trajectory deflections demonstrating a dense positive nucleus surrounded by empty space."
                        }
                    }
                ],
                # Card 4: Rutherford's Nuclear Model & Video Demonstration
                [
                    {
                        "type": "concept_explanation",
                        "title": "Rutherford's Nuclear Model of the Atom",
                        "content": {
                            "title": "Deductions from Scattering Data",
                            "text": "Rutherford deduced three revolutionary facts about atomic architecture:\n\n1. **The Atom is Mostly Empty Space**: Because the vast majority of alpha particles passed straight through unimpeded, the volume of an atom is almost entirely empty space.\n2. **The Dense Positive Nucleus**: Because positive alpha particles were repelled backwards at sharp angles, all the positive charge and almost all the atomic mass are concentrated in an unimaginably tiny, dense core called the **nucleus**.\n3. **Orbiting Electrons**: Negative electrons orbit around this positive nucleus in the vast outer empty space, held by electrostatic attraction."
                        }
                    },
                    {
                        "type": "suggested_video",
                        "title": "3D Animation: Rutherford's Gold Foil Experiment and Nuclear Model",
                        "content": {
                            "title": "Rutherford Gold Foil Experiment in 3D",
                            "description": "Watch a high-definition 3D visualization showing alpha particles penetrating gold atomic lattices, experiencing electrostatic repulsion near the dense positive nucleus.",
                            "url": "https://www.youtube.com/watch?v=5pZj0u_XMbc"
                        }
                    }
                ],
                # Card 5: Formative Knowledge Checks
                [
                    {
                        "type": "knowledge_check",
                        "title": "Knowledge Check: Thought Experiment on Atomic Structure",
                        "content": {
                            "question": "In a hypothetical universe, a scientist repeats Rutherford's alpha particle gold foil experiment and discovers that EVERY SINGLE alpha particle bounces directly backward. What would this prove about the structure of atoms in that universe?",
                            "options": [
                                "The atoms in that universe have no mass at all.",
                                "The atoms are completely solid, impenetrable spheres of positive charge and mass with zero empty space, matching Dalton's solid sphere model.",
                                "The atoms are composed purely of negative electrons.",
                                "The alpha particles were traveling at the speed of light."
                            ],
                            "answer": "The atoms are completely solid, impenetrable spheres of positive charge and mass with zero empty space, matching Dalton's solid sphere model.",
                            "explanation": "Correct! If all alpha particles bounce back, there is no empty space for particles to pass through. The entire volume of the atom would have to be an impenetrable, solid barrier of mass and charge."
                        }
                    },
                    {
                        "type": "knowledge_check",
                        "title": "Knowledge Check: Deducing Nuclear Charge",
                        "content": {
                            "question": "What primary experimental evidence allowed Rutherford to conclude that the atomic nucleus carries a POSITIVE electrical charge?",
                            "options": [
                                "Electrons were observed falling into the nucleus.",
                                "Positively charged alpha particles were electrostatically repelled and deflected at sharp angles when passing close to the nucleus.",
                                "Most alpha particles passed straight through without deflection.",
                                "Gold foil is a shiny, malleable yellow metal."
                            ],
                            "answer": "Positively charged alpha particles were electrostatically repelled and deflected at sharp angles when passing close to the nucleus.",
                            "explanation": "Correct! In electrostatics, like charges repel. Because alpha particles carry a positive ($+2$) charge, they could only be deflected and repelled backwards by a localized, concentrated positive charge in the center of the gold atom."
                        }
                    }
                ]
            ]
        },

        # =====================================================================
        # LESSON 2: Subatomic Particles, Atomic Number, and Mass Number
        # =====================================================================
        {
            "unit_order": 2,
            "unit_name": "Subatomic Particles, Atomic Number, and Mass Number",
            "unit_description": "Compare protons, neutrons, and electrons. Define atomic number (Z) and mass number (A), write standard nuclide notation, and calculate particle counts in neutral atoms and ions.",
            "lesson_title": "Subatomic Particles, Atomic Number, and Mass Number",
            "pages": [
                # Card 1: Hook & Objectives
                [
                    {
                        "type": "suggested_image",
                        "title": "The Architecture of the Atom",
                        "content": {
                            "title": "The Architecture of the Atom",
                            "caption": "Subatomic particle arrangement showing central nucleons and orbiting electron probability shells."
                        }
                    },
                    {
                        "type": "learning_goal",
                        "title": "Lesson Objectives: Subatomic Particles & Nuclides",
                        "content": {
                            "title": "What We Will Master Today",
                            "goals": [
                                "Compare the charge, relative mass, and location of **protons, neutrons, and electrons**.",
                                "Define **Atomic Number ($Z$)** and **Mass Number ($A$)** and use them to calculate subatomic particle counts.",
                                "Write and interpret standard **nuclide notation** (${}^{A}_{Z}\\text{X}$).",
                                "Calculate electron, proton, and neutron counts in neutral atoms versus **cations ($+$)** and **anions ($-$)**."
                            ]
                        }
                    },
                    {
                        "type": "concept_explanation",
                        "title": "Inside the Atom: The Fundamental Triad",
                        "content": {
                            "title": "The Fundamental Triad of Matter",
                            "text": "Dalton believed the atom was indivisible, but 20th-century physics proved that all atoms are built from three fundamental **subatomic particles**: **protons**, **neutrons**, and **electrons**.\n\nProtons and neutrons reside tightly packed in the central nucleus (collectively called **nucleons**), while electrons orbit in quantized energy regions outside the nucleus."
                        }
                    }
                ],
                # Card 2: Subatomic Particles Matrix
                [
                    {
                        "type": "comparison_table",
                        "title": "Fundamental Properties of Subatomic Particles",
                        "content": {
                            "headers": ["Particle", "Symbol", "Relative Charge", "Actual Charge (C)", "Relative Mass (amu)", "Location in Atom"],
                            "rows": [
                                ["Proton", "p⁺", "+1", "+1.602 × 10⁻¹⁹", "1", "Inside the central nucleus"],
                                ["Neutron", "n⁰", "0 (Neutral)", "0", "1", "Inside the central nucleus"],
                                ["Electron", "e⁻", "-1", "-1.602 × 10⁻¹⁹", "1/1840 (0.00054)", "Orbiting in energy levels / orbitals"]
                            ]
                        }
                    },
                    {
                        "type": "callout",
                        "title": "Where is the Mass of an Atom?",
                        "content": {
                            "title": "The Nucleus Holds 99.95% of Atomic Mass",
                            "text": "Because an electron has a negligible relative mass ($\\approx \\frac{1}{1840}$ of a proton), virtually the entire mass of any atom is concentrated inside the nucleus. The orbiting electrons occupy almost all the volume but contribute almost zero mass!"
                        }
                    }
                ],
                # Card 3: Atomic Number, Mass Number, and Formulas
                [
                    {
                        "type": "concept_explanation",
                        "title": "Atomic Number (Z) vs. Mass Number (A)",
                        "content": {
                            "title": "Defining Atomic Identity and Mass",
                            "text": "Every element on the Periodic Table is uniquely identified by the number of protons in its nucleus:\n\n- **Atomic Number ($Z$)**: The number of protons in the nucleus of an atom. In a neutral atom, the number of positive protons equals the number of negative electrons ($p^+ = e^- = Z$).\n- **Mass Number ($A$)**: The total number of protons and neutrons in the nucleus ($A = p^+ + n^0$).\n\n### Essential Subatomic Calculation Formula:\n$$\\text{Number of Neutrons } (n^0) = \\text{Mass Number } (A) - \\text{Atomic Number } (Z)$$"
                        }
                    },
                    {
                        "type": "definition_card",
                        "title": "Core Definition: Atomic & Mass Number",
                        "content": {
                            "term": "Atomic Number (Z) and Mass Number (A)",
                            "definition": "**Atomic Number ($Z$)** is the fundamental identity number of an element, representing its nuclear proton count. **Mass Number ($A$)** is the integer sum of nuclear protons and neutrons (nucleons).",
                            "example": "Carbon has $Z = 6$ (6 protons) and $A = 12$, meaning it contains $12 - 6 = 6$ neutrons."
                        }
                    }
                ],
                # Card 4: Nuclide Notation and Ion Formation
                [
                    {
                        "type": "suggested_diagram",
                        "title": "Nuclide Notation and Carbon-12 Structure",
                        "content": {
                            "title": "Nuclide Notation and Carbon-12 Structure",
                            "caption": "Standard nuclide notation ${}^{A}_{Z}X$ deconstructed with the subatomic structure of a Carbon-12 atom."
                        }
                    },
                    {
                        "type": "concept_explanation",
                        "title": "Neutral Atoms vs. Charged Ions",
                        "content": {
                            "title": "How Electron Loss or Gain Creates Ions",
                            "text": "When an atom participates in chemical reactions, the number of nuclear protons never changes. However, atoms gain or lose valence electrons to achieve stable noble gas electron configurations:\n\n- **Cation (Positive Ion)**: Formed when a metal atom **loses electrons**. It has more protons than electrons ($p^+ > e^-$).\n  - *Example*: Sodium atom (${}^{23}_{11}\\text{Na}$, $11p^+, 11e^-$) loses $1e^-$ $\\rightarrow$ $\\text{Na}^+$ ion ($11p^+, 10e^-$).\n- **Anion (Negative Ion)**: Formed when a non-metal atom **gains electrons**. It has more electrons than protons ($e^- > p^+$).\n  - *Example*: Oxygen atom (${}^{16}_{8}\\text{O}$, $8p^+, 8e^-$) gains $2e^-$ $\\rightarrow$ $\\text{O}^{2-}$ oxide ion ($8p^+, 10e^-$)."
                        }
                    }
                ],
                # Card 5: Formative Knowledge Checks
                [
                    {
                        "type": "knowledge_check",
                        "title": "Knowledge Check: Calculating Subatomic Particles in Ions",
                        "content": {
                            "question": "A Calcium ion is represented in nuclide notation as ${}^{40}_{20}\\text{Ca}^{2+}$. How many protons, neutrons, and electrons does this ion contain?",
                            "options": [
                                "20 protons, 20 neutrons, and 20 electrons",
                                "20 protons, 20 neutrons, and 18 electrons",
                                "22 protons, 20 neutrons, and 20 electrons",
                                "20 protons, 40 neutrons, and 18 electrons"
                            ],
                            "answer": "20 protons, 20 neutrons, and 18 electrons",
                            "explanation": "Correct! Protons = $Z = 20$. Neutrons = $A - Z = 40 - 20 = 20$. Because the ion carries a $+2$ charge, it has lost 2 electrons: Electrons = $20 - 2 = 18$ electrons."
                        }
                    },
                    {
                        "type": "knowledge_check",
                        "title": "Knowledge Check: Chlorine Atom Particle Counts",
                        "content": {
                            "question": "A neutral atom of chlorine is represented as ${}^{37}_{17}\\text{Cl}$. What are its atomic number, mass number, and neutron count?",
                            "options": [
                                "Atomic Number = 17, Mass Number = 37, Neutrons = 20",
                                "Atomic Number = 37, Mass Number = 17, Neutrons = 20",
                                "Atomic Number = 17, Mass Number = 37, Neutrons = 17",
                                "Atomic Number = 20, Mass Number = 37, Neutrons = 17"
                            ],
                            "answer": "Atomic Number = 17, Mass Number = 37, Neutrons = 20",
                            "explanation": "Correct! Subscript $Z = 17$ (atomic number), superscript $A = 37$ (mass number). Neutrons = $A - Z = 37 - 17 = 20$ neutrons."
                        }
                    }
                ]
            ]
        },

        # =====================================================================
        # LESSON 3: Isotopes and Relative Atomic Mass
        # =====================================================================
        {
            "unit_order": 3,
            "unit_name": "Isotopes and Relative Atomic Mass",
            "unit_description": "Define isotopes and explain why atomic masses are non-integers. Master the weighted average formula for Relative Atomic Mass (RAM) with step-by-step worked examples (Chlorine and Copper).",
            "lesson_title": "Isotopes and Relative Atomic Mass",
            "pages": [
                # Card 1: Hook & The Non-Integer Mass Mystery
                [
                    {
                        "type": "suggested_image",
                        "title": "The Mystery of Fractional Atomic Masses",
                        "content": {
                            "title": "The Mystery of Fractional Atomic Masses",
                            "caption": "Sealed ampoule containing greenish-yellow elemental chlorine gas, whose relative atomic mass is 35.5 amu."
                        }
                    },
                    {
                        "type": "learning_goal",
                        "title": "Lesson Objectives: Isotopes and RAM",
                        "content": {
                            "title": "What We Will Master Today",
                            "goals": [
                                "Define **isotopes** and explain why isotopes share identical chemical properties but differ in physical properties.",
                                "Analyze the natural isotopic compositions of **Carbon, Chlorine, and Copper**.",
                                "Define **Relative Atomic Mass (RAM / $A_r$)** based on the Carbon-12 standard.",
                                "Execute step-by-step **weighted average RAM calculations** from percentage isotopic abundances."
                            ]
                        }
                    },
                    {
                        "type": "concept_explanation",
                        "title": "Why Are Atomic Masses on the Periodic Table Not Whole Numbers?",
                        "content": {
                            "title": "The Non-Integer Mass Mystery",
                            "text": "If protons and neutrons each have a relative mass of exactly 1, and electrons have virtually zero mass, why is the atomic mass of Chlorine on the Periodic Table listed as **$35.5$**, and Copper as **$63.5$**?\n\nDo half-protons or fractions of neutrons exist in nature? Absolutely not! The fractional values appear because natural elements exist as mixtures of different **isotopes** with varying abundances."
                        }
                    }
                ],
                # Card 2: What Are Isotopes?
                [
                    {
                        "type": "concept_explanation",
                        "title": "Understanding Isotopes: Sister Atoms",
                        "content": {
                            "title": "Same Protons, Different Neutrons",
                            "text": "All atoms of a particular element must have identical numbers of nuclear protons (the same atomic number $Z$). However, they can contain different numbers of neutrons in their nuclei.\n\n### The Three Natural Isotopes of Carbon:\n1. **Carbon-12 (${}^{12}_{6}\\text{C}$)**: $6p^+, 6n^0, 6e^-$ ($98.9\\%$ abundance, stable).\n2. **Carbon-13 (${}^{13}_{6}\\text{C}$)**: $6p^+, 7n^0, 6e^-$ ($1.1\\%$ abundance, stable).\n3. **Carbon-14 (${}^{14}_{6}\\text{C}$)**: $6p^+, 8n^0, 6e^-$ (Trace amounts, radioactive, used in radiocarbon dating)."
                        }
                    },
                    {
                        "type": "suggested_diagram",
                        "title": "Nuclear Structures of Carbon-12, Carbon-13, and Carbon-14",
                        "content": {
                            "title": "Nuclear Structures of Carbon-12, Carbon-13, and Carbon-14",
                            "caption": "Visual comparison of carbon isotopes showing invariant 6 protons and varying 6, 7, and 8 neutrons."
                        }
                    }
                ],
                # Card 3: Relative Atomic Mass (RAM) Concept & Formula
                [
                    {
                        "type": "concept_explanation",
                        "title": "Defining Relative Atomic Mass (RAM or Ar)",
                        "content": {
                            "title": "The Weighted Average of Isotopic Masses",
                            "text": "Because naturally occurring samples of elements contain a mixture of isotopes, chemists use a weighted average called the **Relative Atomic Mass (RAM or $A_r$)**.\n\nBy international standard, RAM is calibrated relative to $\\frac{1}{12}\\text{th}$ of the mass of a single Carbon-12 atom (${}^{12}\\text{C} = 12.000\\text{ amu}$).\n\n### The Master RAM Formula:\n$$\\text{RAM } (A_r) = \\frac{(\\%_1 \\times \\text{Mass}_1) + (\\%_2 \\times \\text{Mass}_2) + \\dots + (\\%_n \\times \\text{Mass}_n)}{100}$$"
                        }
                    },
                    {
                        "type": "definition_card",
                        "title": "Core Definition: Relative Atomic Mass",
                        "content": {
                            "term": "Relative Atomic Mass (RAM / Ar)",
                            "definition": "The weighted average mass of the naturally occurring isotopes of an element, on a scale where a carbon-12 atom has a mass of exactly 12 units.",
                            "example": "Chlorine has an $A_r$ of 35.5 because it is a weighted mixture of 75.77% Cl-35 and 24.23% Cl-37."
                        }
                    }
                ],
                # Card 4: Step-by-Step RAM Calculation (Chlorine Worked Example)
                [
                    {
                        "type": "worked_example",
                        "title": "Worked Calculation: Relative Atomic Mass of Chlorine",
                        "content": {
                            "title": "Step-by-Step Calculation for Natural Chlorine",
                            "text": "**Problem**: Naturally occurring chlorine consists of $75.77\\%$ of ${}^{35}\\text{Cl}$ (mass = 35.0 amu) and $24.23\\%$ of ${}^{37}\\text{Cl}$ (mass = 37.0 amu). Calculate the Relative Atomic Mass of chlorine.\n\n- **Step 1: Identify Given Data**: $\\%_1 = 75.77\\%$, $\\text{Mass}_1 = 35$; $\\%_2 = 24.23\\%$, $\\text{Mass}_2 = 37$.\n- **Step 2: Formula**: $\\text{RAM} = \\frac{(\\%_1 \\times \\text{Mass}_1) + (\\%_2 \\times \\text{Mass}_2)}{100}$\n- **Step 3: Substitute**: $\\text{RAM} = \\frac{(75.77 \\times 35) + (24.23 \\times 37)}{100}$\n- **Step 4: Compute Numerator**: $\\text{RAM} = \\frac{2651.95 + 896.51}{100} = \\frac{3548.46}{100}$\n- **Step 5: Final Result**: $\\text{RAM} = 35.4846 \\approx \\mathbf{35.5}\\text{ amu}$\n\n*Interpretation*: Because ${}^{35}\\text{Cl}$ is approximately 3 times more abundant than ${}^{37}\\text{Cl}$, the weighted average is pulled much closer to 35."
                        }
                    },
                    {
                        "type": "callout",
                        "title": "Chemical vs. Physical Properties of Isotopes",
                        "content": {
                            "title": "Why Do Isotopes React Identically?",
                            "text": "Chemical reactivity is determined entirely by the **number and arrangement of electrons** (specifically valence electrons). Because all isotopes of an element have the exact same number of protons and electrons, they exhibit **identical chemical properties**. They differ only in **physical properties** dependent on mass (such as density, rate of diffusion, and boiling points)."
                        }
                    }
                ],
                # Card 5: Formative Knowledge Checks
                [
                    {
                        "type": "knowledge_check",
                        "title": "Knowledge Check: Calculating Copper RAM",
                        "content": {
                            "question": "Copper exists naturally as two isotopes: Copper-63 (abundance 69.17%, mass = 63 amu) and Copper-65 (abundance 30.83%, mass = 65 amu). What is the Relative Atomic Mass of copper?",
                            "options": [
                                "64.00 amu",
                                "63.62 amu",
                                "64.50 amu",
                                "65.00 amu"
                            ],
                            "answer": "63.62 amu",
                            "explanation": "Correct! $\\text{RAM} = \\frac{(69.17 \\times 63) + (30.83 \\times 65)}{100} = \\frac{4357.71 + 2003.95}{100} = \\frac{6361.66}{100} = 63.62\\text{ amu}$."
                        }
                    },
                    {
                        "type": "knowledge_check",
                        "title": "Knowledge Check: Chemical Identity of Isotopes",
                        "content": {
                            "question": "Why do Carbon-12 and Carbon-14 react with oxygen gas at high temperature to form carbon dioxide in exactly the same chemical manner?",
                            "options": [
                                "Because they have the same mass number",
                                "Because both isotopes have identical electron configurations ($1s^2 2s^2 2p^2$) and 4 valence electrons, which dictate chemical reactivity",
                                "Because they have the same number of neutrons",
                                "Because both isotopes are radioactive"
                            ],
                            "answer": "Because both isotopes have identical electron configurations ($1s^2 2s^2 2p^2$) and 4 valence electrons, which dictate chemical reactivity",
                            "explanation": "Correct! Chemical reactions involve electron sharing and transfer. Since all carbon isotopes have 6 protons and 6 electrons with configuration $1s^2 2s^2 2p^2$, their chemical reactivity is identical."
                        }
                    }
                ]
            ]
        },

        # =====================================================================
        # LESSON 4: Energy Levels, Orbitals, and s/p Notation
        # =====================================================================
        {
            "unit_order": 4,
            "unit_name": "Energy Levels, Orbitals, and s/p Notation",
            "unit_description": "Advance from 2D Bohr shells to 3D atomic orbitals. Explore spherical s and dumbbell p sublevels, the Aufbau filling principle, and write s/p electron configurations for the first 20 elements.",
            "lesson_title": "Energy Levels, Orbitals, and s/p Notation",
            "pages": [
                # Card 1: Hook & Beyond 2D Circles
                [
                    {
                        "type": "suggested_image",
                        "title": "The Quantum Nature of Electron Orbitals",
                        "content": {
                            "title": "The Quantum Nature of Electron Orbitals",
                            "caption": "Spatial probability distributions of atomic orbitals mapping 3D electron densities around atomic nuclei."
                        }
                    },
                    {
                        "type": "learning_goal",
                        "title": "Lesson Objectives: Orbitals and s/p Notation",
                        "content": {
                            "title": "What We Will Master Today",
                            "goals": [
                                "Distinguish **Principal Energy Levels ($n$)**, **Sublevels ($s, p$)**, and 3D **Orbitals**.",
                                "Analyze the 3D spatial shapes and maximum electron capacities of **spherical $s$** and **dumbbell $p$** orbitals.",
                                "Apply the **Aufbau Principle** to determine orbital filling order ($1s \\rightarrow 2s \\rightarrow 2p \\rightarrow 3s \\rightarrow 3p \\rightarrow 4s$).",
                                "Write full **$s$ and $p$ electron arrangements** and determine valence electrons for the first 20 elements."
                            ]
                        }
                    },
                    {
                        "type": "concept_explanation",
                        "title": "Beyond 2D Shells: The 3D Quantum Electron Cloud",
                        "content": {
                            "title": "Moving Beyond Circular Train Tracks",
                            "text": "In junior secondary school, you visualized electrons orbiting the nucleus in flat concentric circles (Bohr orbits) with capacities of 2, 8, 8.\n\nIn Senior School Chemistry, modern quantum mechanics reveals that electrons do not travel along flat tracks. Instead, they occupy 3D probabilistic regions of space called **atomic orbitals** where there is a high probability ($>90\\%$) of locating an electron."
                        }
                    }
                ],
                # Card 2: Orbitals & Sublevels (s and p shapes)
                [
                    {
                        "type": "concept_explanation",
                        "title": "Sublevels and Orbital Geometries",
                        "content": {
                            "title": "Shapes of s and p Orbitals",
                            "text": "Each principal energy level ($n = 1, 2, 3, 4$) is subdivided into sublevels:\n\n1. **$s$ Sublevel**: Contains **one spherical orbital** centered on the nucleus. Holds a maximum of **2 electrons**.\n2. **$p$ Sublevel**: Contains **three dumbbell-shaped orbitals** oriented mutually perpendicular along the x, y, and z cartesian axes ($p_x, p_y, p_z$). Each $p$ orbital holds 2 electrons, giving the $p$ sublevel a maximum capacity of **6 electrons**.\n\n### Electron Capacity Table:\n- $n = 1$: Only $1s$ (Max 2 electrons)\n- $n = 2$: $2s + 2p$ (Max $2 + 6 = 8$ electrons)\n- $n = 3$: $3s + 3p$ ($+ 3d$) (First 8 filled before $4s$)\n- $n = 4$: $4s$ begins filling after $3p$"
                        }
                    },
                    {
                        "type": "suggested_diagram",
                        "title": "3D Geometries of Spherical s and Dumbbell px, py, pz Orbitals",
                        "content": {
                            "title": "3D Geometries of Spherical s and Dumbbell px, py, pz Orbitals",
                            "caption": "Cartesian axis diagrams of spherical s orbital and perpendicular dumbbell px, py, pz orbitals."
                        }
                    }
                ],
                # Card 3: The Aufbau Principle & Filling Sequence
                [
                    {
                        "type": "step_process",
                        "title": "The Aufbau Principle: Orbital Filling Sequence",
                        "content": {
                            "title": "Rules Governing Electron Placement",
                            "steps": [
                                "1. **Aufbau Principle ('Building Up')**: Electrons occupy the lowest available energy orbital before populating higher energy levels.",
                                "2. **Energy Order Sequence**: $1s \\rightarrow 2s \\rightarrow 2p \\rightarrow 3s \\rightarrow 3p \\rightarrow 4s$. (Note: $4s$ is slightly lower in energy than $3d$ and fills first!).",
                                "3. **Pauli Exclusion Principle**: An orbital holds a maximum of 2 electrons, which must have opposite spins ($\\uparrow\\downarrow$).",
                                "4. **Hund's Rule**: In degenerate orbitals of equal energy (like $2p_x, 2p_y, 2p_z$), electrons occupy orbitals singly with parallel spins before pairing up."
                            ]
                        }
                    },
                    {
                        "type": "definition_card",
                        "title": "Core Definition: Aufbau Principle",
                        "content": {
                            "term": "Aufbau Principle",
                            "definition": "The fundamental quantum chemical rule dictating that atomic orbitals are filled in order of increasing energy levels, starting from the lowest energy $1s$ orbital.",
                            "example": "Carbon fills $1s^2$, then $2s^2$, and finally places its remaining 2 electrons into $2p^2$."
                        }
                    }
                ],
                # Card 4: First 20 Elements s/p Configuration Matrix
                [
                    {
                        "type": "comparison_table",
                        "title": "Electron Configurations (s and p Notation) for Elements 1 to 20",
                        "content": {
                            "headers": ["Z", "Element", "Symbol", "s and p Electron Configuration", "Valence Electrons"],
                            "rows": [
                                ["1", "Hydrogen", "H", "1s¹", "1"],
                                ["2", "Helium", "He", "1s² (Duplet stable)", "2"],
                                ["3", "Lithium", "Li", "1s² 2s¹", "1"],
                                ["4", "Beryllium", "Be", "1s² 2s²", "2"],
                                ["5", "Boron", "B", "1s² 2s² 2p¹", "3"],
                                ["6", "Carbon", "C", "1s² 2s² 2p²", "4"],
                                ["7", "Nitrogen", "N", "1s² 2s² 2p³", "5"],
                                ["8", "Oxygen", "O", "1s² 2s² 2p⁴", "6"],
                                ["9", "Fluorine", "F", "1s² 2s² 2p⁵", "7"],
                                ["10", "Neon", "Ne", "1s² 2s² 2p⁶ (Octet stable)", "8"],
                                ["11", "Sodium", "Na", "1s² 2s² 2p⁶ 3s¹", "1"],
                                ["12", "Magnesium", "Mg", "1s² 2s² 2p⁶ 3s²", "2"],
                                ["13", "Aluminium", "Al", "1s² 2s² 2p⁶ 3s² 3p¹", "3"],
                                ["14", "Silicon", "Si", "1s² 2s² 2p⁶ 3s² 3p²", "4"],
                                ["15", "Phosphorus", "P", "1s² 2s² 2p⁶ 3s² 3p³", "5"],
                                ["16", "Sulfur", "S", "1s² 2s² 2p⁶ 3s² 3p⁴", "6"],
                                ["17", "Chlorine", "Cl", "1s² 2s² 2p⁶ 3s² 3p⁵", "7"],
                                ["18", "Argon", "Ar", "1s² 2s² 2p⁶ 3s² 3p⁶ (Octet stable)", "8"],
                                ["19", "Potassium", "K", "1s² 2s² 2p⁶ 3s² 3p⁶ 4s¹", "1"],
                                ["20", "Calcium", "Ca", "1s² 2s² 2p⁶ 3s² 3p⁶ 4s²", "2"]
                            ]
                        }
                    },
                    {
                        "type": "definition_card",
                        "title": "Key Concept: Valence Electrons",
                        "content": {
                            "term": "Valence Electrons",
                            "definition": "The electrons occupying the highest (outermost) principal energy level of an atom, responsible for chemical reactivity, valency, and chemical bonding.",
                            "example": "Phosphorus ($1s^2 2s^2 2p^6 3s^2 3p^3$) has outermost shell $n=3$ with $2 + 3 = 5$ valence electrons."
                        }
                    }
                ],
                # Card 5: Formative Knowledge Checks
                [
                    {
                        "type": "knowledge_check",
                        "title": "Knowledge Check: Identifying Elements from s/p Notation",
                        "content": {
                            "question": "An atom has the electron configuration $1s^2 2s^2 2p^6 3s^2 3p^3$. What is the element, its atomic number, and its number of valence electrons?",
                            "options": [
                                "Nitrogen, Atomic Number = 7, Valence Electrons = 5",
                                "Phosphorus, Atomic Number = 15, Valence Electrons = 5",
                                "Sulfur, Atomic Number = 16, Valence Electrons = 6",
                                "Aluminium, Atomic Number = 13, Valence Electrons = 3"
                            ],
                            "answer": "Phosphorus, Atomic Number = 15, Valence Electrons = 5",
                            "explanation": "Correct! Total electrons = $2 + 2 + 6 + 2 + 3 = 15$, which corresponds to Phosphorus ($Z = 15$). Its outermost shell ($n=3$) contains $3s^2 3p^3$, giving $2 + 3 = 5$ valence electrons."
                        }
                    },
                    {
                        "type": "knowledge_check",
                        "title": "Knowledge Check: Potassium Ion Electron Configuration",
                        "content": {
                            "question": "What is the correct s and p electron configuration for a Potassium ion ($\\text{K}^+$)?",
                            "options": [
                                "$1s^2 2s^2 2p^6 3s^2 3p^6 4s^1$",
                                "$1s^2 2s^2 2p^6 3s^2 3p^6$",
                                "$1s^2 2s^2 2p^6 3s^2 3p^5$",
                                "$1s^2 2s^2 2p^6 3s^2 3p^6 4s^2$"
                            ],
                            "answer": "$1s^2 2s^2 2p^6 3s^2 3p^6$",
                            "explanation": "Correct! Neutral Potassium ($Z=19$) has configuration $1s^2 2s^2 2p^6 3s^2 3p^6 4s^1$. To form a $\\text{K}^+$ cation, it loses its outermost $4s^1$ electron, attaining the stable noble gas electron octet of Argon ($1s^2 2s^2 2p^6 3s^2 3p^6$)."
                        }
                    }
                ]
            ]
        },

        # =====================================================================
        # LESSON 5: Integrated Atomic Representation and Review
        # =====================================================================
        {
            "unit_order": 5,
            "unit_name": "Integrated Atomic Representation and Review",
            "unit_description": "Synthesize atomic concepts across the chemical triplet using Sodium as a comprehensive case study. Build physical 3D atom models, evaluate model limitations, and complete the end-of-topic mastery challenge.",
            "lesson_title": "Integrated Atomic Representation and Review",
            "pages": [
                # Card 1: Hook & Chemical Toolkit
                [
                    {
                        "type": "suggested_image",
                        "title": "Connecting the Microscopic to the Macroscopic",
                        "content": {
                            "title": "Connecting the Microscopic to the Macroscopic",
                            "caption": "Freshly cut elemental sodium metal stored under paraffin oil, illustrating macroscopic metallic properties arising from atomic structure."
                        }
                    },
                    {
                        "type": "learning_goal",
                        "title": "Lesson Objectives: Atomic Synthesis & Model Evaluation",
                        "content": {
                            "title": "What We Will Master Today",
                            "goals": [
                                "Integrate atomic theory across the **Macroscopic, Submicroscopic, and Symbolic** levels using Sodium.",
                                "Construct a physical **3D atom model** using locally available materials and analyze model limitations.",
                                "Troubleshoot subatomic calculations involving neutral atoms, isotopes, and multi-charged ions.",
                                "Achieve mastery across the complete Grade 10 CBC Topic 1.2 syllabus."
                            ]
                        }
                    },
                    {
                        "type": "concept_explanation",
                        "title": "The Master Chemistry Toolkit",
                        "content": {
                            "title": "From Dalton to Modern Quantum Orbitals",
                            "text": "You have traced the journey of atomic discovery from Dalton's solid billiard ball, through Rutherford's planetary nuclear model, to modern 3D $s$ and $p$ orbital configurations.\n\nNow, let us bring these representations together into an integrated chemical profile."
                        }
                    }
                ],
                # Card 2: Triplet Case Study: The Sodium Atom
                [
                    {
                        "type": "concept_explanation",
                        "title": "Chemical Triplet Case Study: Sodium (Na)",
                        "content": {
                            "title": "How Atomic Structure Dictates Physical and Chemical Behavior",
                            "text": "1. **Macroscopic Level**: Sodium is a soft, silvery-white alkali metal that can be easily sliced with a butter knife, conducts electricity, and reacts violently with water to produce hydrogen gas and an alkaline solution.\n2. **Submicroscopic Level**: Each sodium atom consists of a nucleus with $11$ positive protons and $12$ neutral neutrons ($A = 23$), surrounded by $11$ electrons arranged in energy levels: 2 in $n=1$, 8 in $n=2$, and 1 loosely held valence electron in the outer $3s$ orbital.\n3. **Symbolic Level**: Represented by symbol $\\text{Na}$, nuclide notation ${}^{23}_{11}\\text{Na}$, and configuration $1s^2 2s^2 2p^6 3s^1$."
                        }
                    },
                    {
                        "type": "suggested_diagram",
                        "title": "Comprehensive Chemical Profile: Sodium (Na) Triplet Representation",
                        "content": {
                            "title": "Comprehensive Chemical Profile: Sodium (Na) Triplet Representation",
                            "caption": "Integrated diagram showing macroscopic sodium slicing, submicroscopic nuclear/orbital structure, and symbolic notation."
                        }
                    }
                ],
                # Card 3: Synthesis Practical Activity: Building a 3D Atom Model
                [
                    {
                        "type": "step_process",
                        "title": "Practical Activity: Constructing a 3D Atom Model",
                        "content": {
                            "title": "Physical Modeling Protocol",
                            "steps": [
                                "1. **Select an Element**: Choose one element from the first 20 elements (e.g., Carbon, Oxygen, Silicon, or Calcium).",
                                "2. **Gather Safe Local Materials**: Collect colored modeling clay, bottle caps, wire hoops, cardboard, and toothpicks.",
                                "3. **Construct Nucleus & Shells**: Use one color for protons ($p^+$), another for neutrons ($n^0$), and smaller beads/caps on wire rings for electrons ($e^-$).",
                                "4. **Attach Scientific Profile Tag**: Label your model with Element Name, Symbol, Nuclide Notation (${}^{A}_{Z}\\text{X}$), Full $s/p$ Configuration, and Valence Electron count.",
                                "5. **Critique Model Limitations**: Identify where your model oversimplifies reality (e.g. electrons are not solid balls on rigid wire tracks, and nucleus is not drawn to true scale!)."
                            ]
                        }
                    },
                    {
                        "type": "common_misconception",
                        "title": "Scientific Thinking: Understanding Model Limitations",
                        "content": {
                            "misconception": "Physical classroom atom models show exactly what real atoms look like.",
                            "correction": "All scientific models are useful approximations! If the nucleus of a real atom were the size of a marble in a stadium, the electrons would be tiny specks buzzing around the outer upper deck. Real electrons behave as quantum probability waves rather than solid spheres on wires.",
                            "why_it_matters": "Recognizing model limitations is a core CBC scientific inquiry skill preventing misconceptions in advanced bonding."
                        }
                    }
                ],
                # Card 4: Topic 1.2 Master Summary & Key Takeaways
                [
                    {
                        "type": "summary",
                        "title": "Topic 1.2 Master Summary & Key Takeaways",
                        "content": {
                            "title": "Key Atomic Principles Mastered",
                            "summary_points": [
                                "**Atomic Structure**: Atoms consist of a dense central nucleus ($p^+ + n^0$) surrounded by orbiting electrons ($e^-$) in quantized energy levels.",
                                "**Rutherford's Scattering**: Disproved Dalton's solid sphere, establishing that atoms are mostly empty space with a tiny positive nucleus.",
                                "**Subatomic Counts**: Atomic Number $Z = p^+ = e^-$ (in neutral atoms); Mass Number $A = p^+ + n^0$; Neutrons $n^0 = A - Z$.",
                                "**Isotopes & RAM**: Isotopes have identical proton counts but differing neutrons; Relative Atomic Mass ($A_r$) is a weighted average based on ${}^{12}\\text{C}$.",
                                "**Orbital Architecture**: Electrons populate spherical $s$ and dumbbell $p$ orbitals according to the Aufbau Principle ($1s \\rightarrow 2s \\rightarrow 2p \\rightarrow 3s \\rightarrow 3p \\rightarrow 4s$)."
                            ]
                        }
                    },
                    {
                        "type": "transition",
                        "title": "Looking Ahead: The Periodic Table",
                        "content": {
                            "title": "Next Step: Topic 1.3 — The Periodic Table",
                            "text": "With atomic structure and electron configurations mastered, you are ready to explore **The Periodic Table**! You will discover how valence electrons determine groups and periods, and how chemical patterns repeat across the elements."
                        }
                    }
                ],
                # Card 5: End-of-Topic Mastery Challenge
                [
                    {
                        "type": "knowledge_check",
                        "title": "Mastery Challenge: Nitrogen Isotopes",
                        "content": {
                            "question": "Nitrogen has two natural isotopes: Nitrogen-14 (${}^{14}_7\\text{N}$) and Nitrogen-15 (${}^{15}_7\\text{N}$). Which statement correctly compares their properties?",
                            "options": [
                                "Nitrogen-15 reacts much faster with hydrogen because it has more neutrons.",
                                "Both isotopes possess identical chemical properties because they share the same electron configuration ($1s^2 2s^2 2p^3$), but differ in physical mass due to Nitrogen-15 having 8 neutrons versus 7 in Nitrogen-14.",
                                "Nitrogen-14 is a metal while Nitrogen-15 is a non-metal.",
                                "Nitrogen-14 has 7 protons while Nitrogen-15 has 8 protons."
                            ],
                            "answer": "Both isotopes possess identical chemical properties because they share the same electron configuration ($1s^2 2s^2 2p^3$), but differ in physical mass due to Nitrogen-15 having 8 neutrons versus 7 in Nitrogen-14.",
                            "explanation": "Correct! Chemical behavior is governed by valence electron configurations ($1s^2 2s^2 2p^3$), which are identical for both isotopes. They differ only in physical mass because N-15 contains 8 neutrons ($15-7$) while N-14 contains 7 neutrons ($14-7$)."
                        }
                    },
                    {
                        "type": "knowledge_check",
                        "title": "Mastery Challenge: Ion Y²⁻ Identification",
                        "content": {
                            "question": "An ion of element Y carries a charge of $2-$ and has the electron configuration $1s^2 2s^2 2p^6 3s^2 3p^6$. If its nucleus contains 16 neutrons, what are the element's identity and mass number ($A$)?",
                            "options": [
                                "Argon (Ar), Mass Number = 34",
                                "Sulfur (S), Mass Number = 32",
                                "Oxygen (O), Mass Number = 16",
                                "Calcium (Ca), Mass Number = 40"
                            ],
                            "answer": "Sulfur (S), Mass Number = 32",
                            "explanation": "Correct! The ion has 18 electrons. Because it gained 2 electrons (charge $-2$), the neutral atom had $18 - 2 = 16$ electrons, meaning $Z = 16$ (Sulfur). Mass Number $A = \\text{protons} + \\text{neutrons} = 16 + 16 = 32$."
                        }
                    }
                ]
            ]
        }
    ]

@transaction.atomic
def ingest_topic2():
    print("=" * 80)
    print("INGESTING GRADE 10 CHEMISTRY — TOPIC 2: THE ATOM")
    print("=" * 80)

    # 1. Resolve Hierarchy
    cbc = Curriculum.objects.filter(name__icontains="CBC").first()
    if not cbc:
        raise ValueError("Curriculum CBC not found!")
    
    grade10 = Grade.objects.filter(curriculum=cbc, level=10).first()
    if not grade10:
        raise ValueError("Grade 10 not found under CBC!")

    chem = Subject.objects.filter(grade=grade10, id=5).first() or Subject.objects.filter(grade=grade10, name__icontains="Chem").first()
    if not chem:
        raise ValueError("Chemistry subject not found under Grade 10 CBC!")

    print(f"Target Subject: [{chem.id}] {chem.name} (Grade: {grade10.name}, Curr: {cbc.name})")

    # 2. Resolve or Create Topic 2
    topic, created = Topic.objects.get_or_create(
        subject=chem,
        order=2,
        defaults={
            "name": "The Atom",
            "description": "Describe atomic structure, relate atomic number and mass number to subatomic particles, calculate relative atomic mass from isotopic abundance, and write electron arrangements using s and p notation for the first 20 elements."
        }
    )
    if not created:
        topic.name = "The Atom"
        topic.description = "Describe atomic structure, relate atomic number and mass number to subatomic particles, calculate relative atomic mass from isotopic abundance, and write electron arrangements using s and p notation for the first 20 elements."
        topic.save()
    print(f"Resolved Topic 2: [{topic.id}] {topic.name}")

    # 3. Ingest Lessons & Blocks
    curriculum_data = build_topic2_curriculum()

    for unit_data in curriculum_data:
        unit_order = unit_data["unit_order"]
        unit_name = unit_data["unit_name"]
        unit_desc = unit_data["unit_description"]
        lesson_title = unit_data["lesson_title"]
        pages = unit_data["pages"]

        # Resolve Learning Unit
        learning_unit, u_created = LearningUnit.objects.get_or_create(
            topic=topic,
            order=unit_order,
            defaults={
                "name": unit_name,
                "description": unit_desc
            }
        )
        if not u_created:
            learning_unit.name = unit_name
            learning_unit.description = unit_desc
            learning_unit.save()

        # Resolve Lesson (Published, Version 1)
        lesson = Lesson.objects.filter(topic=topic, learning_unit=learning_unit).first()
        if not lesson:
            lesson = Lesson.objects.create(
                topic=topic,
                learning_unit=learning_unit,
                title=lesson_title,
                status="published",
                version=1
            )
            print(f"  [Created Lesson] ID {lesson.id}: {lesson_title}")
        else:
            lesson.title = lesson_title
            lesson.status = "published"
            lesson.version = 1
            lesson.save()
            print(f"  [Updated Lesson] ID {lesson.id}: {lesson_title}")

        # Clear old blocks for idempotent refresh
        lesson.blocks.all().delete()

        # Create structured blocks
        global_order = 0
        for page_idx, page_blocks in enumerate(pages, start=1):
            page_title = page_blocks[0].get("title", f"Page {page_idx}")
            for comp_idx, block_def in enumerate(page_blocks, start=1):
                global_order += 1
                b_type = block_def["type"]
                b_title = block_def["title"]
                b_content = clean_dict(block_def["content"])

                LessonBlock.objects.create(
                    lesson=lesson,
                    block_type=b_type,
                    component_type=b_type,
                    title=b_title,
                    page_number=page_idx,
                    page_title=page_title,
                    component_order=comp_idx,
                    order=global_order,
                    content=b_content
                )

        print(f"    -> Ingested {len(pages)} Pages, {global_order} Blocks for Lesson [{lesson.id}]")

    print("\nSUCCESS: Topic 2 Ingestion Completed Idempotently!")

if __name__ == "__main__":
    ingest_topic2()
