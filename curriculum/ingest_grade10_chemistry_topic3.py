"""
VLearn CBC Grade 10 Chemistry — Topic 3: The Periodic Table
Production Ingestion Engine (Senior Secondary Pedagogical Edition)

Curriculum: CBC (ID: 5)
Grade: Grade 10 (ID: 5, Level: 10)
Subject: Chemistry (ID: 5)
Topic: The Periodic Table (Topic Order: 3)

Decomposed into 6 Learning Units & 6 Published Lessons:
  1. Development and Organization of the Periodic Table (5 Pages, 11 Blocks)
  2. Chemical Families and Stability (5 Pages, 11 Blocks)
  3. Ion Formation, Valency, and Oxidation Number (5 Pages, 11 Blocks)
  4. Formulae of Compounds and Radicals (5 Pages, 11 Blocks)
  5. Chemical Equations and Balancing (5 Pages, 11 Blocks)
  6. Periodic Table-to-Reaction Integration (5 Pages, 11 Blocks)
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

def build_topic3_curriculum():
    """Returns the comprehensive pedagogical page and block structure for Grade 10 Topic 3: The Periodic Table."""
    return [
        # =====================================================================
        # LESSON 1: Development and Organization of the Periodic Table
        # =====================================================================
        {
            "unit_order": 1,
            "unit_name": "Development and Organization of the Periodic Table",
            "unit_description": "Trace the historical evolution of the periodic table from Döbereiner's triads, Newlands' octaves, and Mendeleev's mass-based table to Moseley's atomic number arrangement. Define Groups and Periods.",
            "lesson_title": "Development and Organization of the Periodic Table",
            "pages": [
                # Card 1: Hook & Objectives
                [
                    {
                        "type": "suggested_image",
                        "title": "The Chemist's Map: The Periodic Table",
                        "content": {
                            "title": "The Chemist's Map: The Periodic Table",
                            "caption": "Historical manuscript and early periodic classifications organizing elements into structured chemical systems."
                        }
                    },
                    {
                        "type": "learning_goal",
                        "title": "Lesson Objectives: The Organization of Elements",
                        "content": {
                            "title": "What We Will Master Today",
                            "goals": [
                                "Trace the historical journey from **Döbereiner's Triads**, **Newlands' Octaves**, and **Mendeleev's Table** to **Moseley's Modern Periodic Law**.",
                                "Distinguish between **Groups (Vertical Columns)** and **Periods (Horizontal Rows)** on the Periodic Table.",
                                "Relate group numbers to **valence electrons** and period numbers to **occupied energy levels (shells)**.",
                                "Determine the group and period coordinates of the first 20 elements from their $s$ and $p$ electron configurations."
                            ]
                        }
                    },
                    {
                        "type": "concept_explanation",
                        "title": "The Chemist's Library: Organizing the Elements",
                        "content": {
                            "title": "A Master Blueprint for All Known Matter",
                            "text": "Imagine walking into a massive library where thousands of books are piled on the floor in random heaps. Finding a book on Kenyan history would be a nightmare! But if the librarian sorts those books onto shelves by subject, author, and country, you can find your book in seconds.\n\nThe **Periodic Table** is the chemist's master library. Today, it arranges all known chemical elements so that we can predict their chemical reactivity, electron configurations, and bonding behavior at a single glance."
                        }
                    }
                ],
                # Card 2: Historical Evolution of Classification
                [
                    {
                        "type": "concept_explanation",
                        "title": "The Historical Journey of Chemical Classification",
                        "content": {
                            "title": "From Triads to Modern Atomic Number",
                            "text": "Our modern Periodic Table was built step-by-step through experimental discoveries:\n\n1. **Johann Wolfgang Döbereiner (Triads, 1829)**: Grouped elements into sets of three with similar chemical properties (e.g., $\\text{Li}, \\text{Na}, \\text{K}$). The atomic mass of the middle element was roughly the arithmetic average of the other two.\n2. **John Newlands (Law of Octaves, 1864)**: Arranged elements in order of increasing atomic mass and noticed properties repeated every 8th element, analogous to musical octaves.\n3. **Dmitri Mendeleev (The Breakthrough, 1869)**: The 'Father of the Periodic Table.' Arranged elements by atomic mass, but crucially **left blank gaps** for undiscovered elements (like Germanium) and accurately predicted their properties!\n4. **Henry Moseley (Modern Atomic Number, 1913)**: Discovered that elements should be arranged by **Atomic Number ($Z$, proton count)** rather than atomic mass, resolving all placement anomalies."
                        }
                    },
                    {
                        "type": "definition_card",
                        "title": "Core Definition: Modern Periodic Law",
                        "content": {
                            "term": "The Modern Periodic Law",
                            "definition": "The principle stating that the physical and chemical properties of the elements are periodic functions of their atomic numbers (number of nuclear protons).",
                            "example": "Arranging elements in order of atomic number automatically aligns elements with identical valence electron counts into the same vertical column."
                        }
                    }
                ],
                # Card 3: Groups vs. Periods
                [
                    {
                        "type": "concept_explanation",
                        "title": "Groups (Columns) and Periods (Rows)",
                        "content": {
                            "title": "The Coordinates of the Periodic Grid",
                            "text": "The modern table is organized into a grid of columns and rows:\n\n- **Groups (Vertical Columns, 1 to 18)**:\n  - Elements in the same group have the **same number of valence electrons** in their outermost shell.\n  - Because outer electrons dictate chemical behavior, elements in the same group belong to the same **chemical family** and share similar reactivity.\n  - *Example*: $\\text{Na}$ ($1s^2 2s^2 2p^6 3s^1$) and $\\text{K}$ ($1s^2 2s^2 2p^6 3s^2 3p^6 4s^1$) both have **1 valence electron** $\\rightarrow$ Group 1.\n\n- **Periods (Horizontal Rows, 1 to 7)**:\n  - The period number equals the **number of occupied principal energy levels (shells)**.\n  - *Example*: Oxygen ($1s^2 2s^2 2p^4$) has electrons occupying 2 energy levels ($n=1, 2$) $\\rightarrow$ **Period 2**.\n  - *Example*: Argon ($1s^2 2s^2 2p^6 3s^2 3p^6$) has electrons occupying 3 energy levels ($n=1, 2, 3$) $\\rightarrow$ **Period 3**."
                        }
                    },
                    {
                        "type": "suggested_diagram",
                        "title": "Periodic Table Coordinates: Groups vs. Periods",
                        "content": {
                            "title": "Periodic Table Coordinates: Groups vs. Periods",
                            "caption": "Color-coded schematic of the Periodic Table illustrating vertical Groups (valence electrons) and horizontal Periods (occupied electron shells)."
                        }
                    }
                ],
                # Card 4: Practical Investigation: Grid Mapping
                [
                    {
                        "type": "step_process",
                        "title": "Practical Investigation: Locating the First 20 Elements",
                        "content": {
                            "title": "Periodic Grid Mapping Protocol",
                            "steps": [
                                "1. **Determine Atomic Number ($Z$)**: Identify the total proton/electron count for the target element (e.g., Phosphorus, $Z = 15$).",
                                "2. **Write Full $s/p$ Configuration**: Write out the ground-state electron configuration ($1s^2 2s^2 2p^6 3s^2 3p^3$).",
                                "3. **Count Occupied Shells for Period**: Find the highest principal quantum number ($n=3$). This sets **Period = 3**.",
                                "4. **Count Valence Electrons for Group**: Sum outer shell electrons ($3s^2 3p^3 \\rightarrow 2 + 3 = 5$ valence electrons). Main group position is **Group 15 (Group V)**.",
                                "5. **Verify Placement**: Check coordinates (Period 3, Group 15) against the standard Periodic Table."
                            ]
                        }
                    },
                    {
                        "type": "common_misconception",
                        "title": "Common Mistake: Confusing Group with Period",
                        "content": {
                            "misconception": "Thinking the last number written in an electron configuration (like 4 in $4s^1$) is the Group number.",
                            "correction": "The principal quantum number (4 in $4s^1$) represents the energy level, which gives the **Period number** (Period 4). The superscript exponent (1 in $4s^1$) gives the valence electron count, which determines the **Group number** (Group 1).",
                            "why_it_matters": "Distinguishing shells from valence electrons prevents coordinate reversal errors in exam questions."
                        }
                    }
                ],
                # Card 5: Formative Knowledge Checks
                [
                    {
                        "type": "knowledge_check",
                        "title": "Knowledge Check: Moseley's Scientific Breakthrough",
                        "content": {
                            "question": "Dmitri Mendeleev organized his periodic table by increasing atomic mass, while Henry Moseley reorganized it by increasing atomic number. Why was Moseley's rearrangement a major scientific improvement?",
                            "options": [
                                "It made the elements lighter and easier to work with.",
                                "It resolved inconsistencies where elements (like Tellurium and Iodine) were out of sequence based on their chemical properties.",
                                "It placed nonmetals on the left side of the table.",
                                "It removed all the gaps that Mendeleev had left behind."
                            ],
                            "answer": "It resolved inconsistencies where elements (like Tellurium and Iodine) were out of sequence based on their chemical properties.",
                            "explanation": "Correct! Mendeleev had to reverse the positions of certain element pairs (e.g., Tellurium and Iodine) to keep them in groups with matching chemical properties. Moseley proved that atomic number (proton count) is the true fundamental basis of periodicity, resolving these ordering anomalies."
                        }
                    },
                    {
                        "type": "knowledge_check",
                        "title": "Knowledge Check: Locating Element X from Configuration",
                        "content": {
                            "question": "An atom of element X has the electron configuration $1s^2 2s^2 2p^6 3s^2 3p^5$. In which Group and Period of the Periodic Table is element X located?",
                            "options": [
                                "Group 5, Period 3",
                                "Group 15, Period 5",
                                "Group 17, Period 3",
                                "Group 7, Period 5"
                            ],
                            "answer": "Group 17, Period 3",
                            "explanation": "Correct! The highest principal energy level is $n=3$, giving Period 3 (3 occupied shells). The outermost shell ($n=3$) contains $2 + 5 = 7$ valence electrons ($3s^2 3p^5$), corresponding to Group 17 (the Halogens)."
                        }
                    }
                ]
            ]
        },

        # =====================================================================
        # LESSON 2: Chemical Families and Stability
        # =====================================================================
        {
            "unit_order": 2,
            "unit_name": "Chemical Families and Stability",
            "unit_description": "Examine the main chemical families (Alkali Metals, Alkaline Earth Metals, Halogens, Noble Gases). Understand the quest for chemical stability via duplet and octet electronic configurations.",
            "lesson_title": "Chemical Families and Stability",
            "pages": [
                # Card 1: Hook & Objectives
                [
                    {
                        "type": "suggested_image",
                        "title": "Chemical Families in the Laboratory",
                        "content": {
                            "title": "Chemical Families in the Laboratory",
                            "caption": "Reactivity of Group 1 alkali metals stored under protective mineral oil compared with glowing noble gas discharge tubes."
                        }
                    },
                    {
                        "type": "learning_goal",
                        "title": "Lesson Objectives: Chemical Families & Stability",
                        "content": {
                            "title": "What We Will Master Today",
                            "goals": [
                                "Identify key characteristics of **Alkali Metals (Group 1)**, **Alkaline Earth Metals (Group 2)**, **Halogens (Group 17)**, and **Noble Gases (Group 18)**.",
                                "Explain the **Duplet Rule (2 electrons)** and **Octet Rule (8 electrons)** for chemical stability.",
                                "Analyze why Noble Gases are chemically inert while Alkali Metals and Halogens are intensely reactive.",
                                "Predict how atoms lose, gain, or share electrons to attain noble gas configurations."
                            ]
                        }
                    },
                    {
                        "type": "concept_explanation",
                        "title": "Meet the Chemical Families: Personalities of the Elements",
                        "content": {
                            "title": "Why Elements in the Same Group Behave Alike",
                            "text": "In the Periodic Table, elements with identical valence electron configurations are grouped into **chemical families**. Just like human families share traits, chemical family members share signature physical and chemical properties:\n\n- **Group 1: Alkali Metals** ($\\text{Li}, \\text{Na}, \\text{K}$): Soft, silvery metals cut easily with a knife, highly reactive with water, stored under oil.\n- **Group 2: Alkaline Earth Metals** ($\\text{Be}, \\text{Mg}, \\text{Ca}$): Denser, less reactive than Group 1, burn with brilliant white or colored flames.\n- **Group 17: Halogens** ($\\text{F}, \\text{Cl}, \\text{Br}, \\text{I}$): Toxic, colored nonmetals that form salts with metals.\n- **Group 18: Noble Gases** ($\\text{He}, \\text{Ne}, \\text{Ar}$): Colorless, unreactive (inert) gases with complete valence shells."
                        }
                    }
                ],
                # Card 2: The Quest for Chemical Stability
                [
                    {
                        "type": "concept_explanation",
                        "title": "The Duplet and Octet Rules for Stability",
                        "content": {
                            "title": "Why Atoms React: Seeking Full Outer Shells",
                            "text": "In chemistry, **stability** is the driving force of reactions. An atom is energetically stable when its outermost energy level is completely filled with electrons:\n\n- **Duplet Rule**: For the first energy level ($n=1$), stability is achieved with **2 electrons** (e.g., Helium, $1s^2$).\n- **Octet Rule**: For higher energy levels ($n=2, 3, 4$), stability is achieved with **8 valence electrons** ($ns^2 np^6$, e.g., Neon $1s^2 2s^2 2p^6$, Argon $1s^2 2s^2 2p^6 3s^2 3p^6$).\n\nNoble gases already possess full outer shells, making them chemically inert. All other elements have incomplete valence shells and must **lose, gain, or share electrons** to achieve noble gas stability!"
                        }
                    },
                    {
                        "type": "definition_card",
                        "title": "Core Concept: The Octet Rule",
                        "content": {
                            "term": "The Octet Rule",
                            "definition": "The chemical guideline stating that main-group atoms tend to undergo chemical reactions by losing, gaining, or sharing electrons until they possess eight valence electrons in their outermost shell, resembling the nearest noble gas.",
                            "example": "Sodium ($1s^2 2s^2 2p^6 3s^1$) loses 1 electron to become $\\text{Na}^+$ with a stable neon octet ($1s^2 2s^2 2p^6$)."
                        }
                    }
                ],
                # Card 3: Summary Table of Family Valence Patterns
                [
                    {
                        "type": "comparison_table",
                        "title": "Valence Patterns and Stability Pathways across Chemical Families",
                        "content": {
                            "headers": ["Chemical Family", "Group", "Outer Pattern", "Valence e⁻", "Stability Pathway", "Reactivity"],
                            "rows": [
                                ["Alkali Metals", "Group 1", "ns¹", "1", "Lose 1 electron (form +1 cations)", "Extremely reactive metals"],
                                ["Alkaline Earth", "Group 2", "ns²", "2", "Lose 2 electrons (form +2 cations)", "Reactive metals"],
                                ["Halogens", "Group 17", "ns² np⁵", "7", "Gain 1 electron (form -1 anions)", "Extremely reactive nonmetals"],
                                ["Noble Gases", "Group 18", "ns² np⁶", "8 (He: 2)", "Already stable (duplet/octet)", "Completely inert / unreactive"]
                            ]
                        }
                    },
                    {
                        "type": "suggested_diagram",
                        "title": "Chemical Families & Electron Stability Pathways",
                        "content": {
                            "title": "Chemical Families & Electron Stability Pathways",
                            "caption": "Comparison of valence electron configurations across Group 1, Group 2, Group 17, and Group 18 illustrating electron loss, gain, and inert octets."
                        }
                    }
                ],
                # Card 4: Noble Gases vs. Reactive Elements
                [
                    {
                        "type": "concept_explanation",
                        "title": "Why Are Noble Gases So Stable?",
                        "content": {
                            "title": "The Aloof Noble Gases",
                            "text": "Historically called 'inert' or 'noble' because, like old royalty who stayed separate from common crowds, noble gases do not easily react or form bonds with other elements.\n\nBecause their outer $s$ and $p$ suborbitals are completely filled ($ns^2 np^6$), they have exceptionally high ionization energies (reluctant to lose electrons) and zero electron affinities (reluctant to gain electrons)."
                        }
                    },
                    {
                        "type": "callout",
                        "title": "Why Do Elements in the Same Family Share Properties?",
                        "content": {
                            "title": "Valence Electrons Dictate Chemical Behavior",
                            "text": "When atoms collide, their nuclei and core electrons never touch—only their outermost valence electrons interact. Because all elements in Group 1 have exactly 1 valence electron ($ns^1$), they all undergo the same fundamental reaction: losing that single electron to form $+1$ cations."
                        }
                    }
                ],
                # Card 5: Formative Knowledge Checks
                [
                    {
                        "type": "knowledge_check",
                        "title": "Knowledge Check: Why Noble Gases Do Not Form Compounds",
                        "content": {
                            "question": "Why do Group 18 elements (Helium, Neon, Argon) exist naturally as isolated, unreactive single atoms (monatomic gases)?",
                            "options": [
                                "They are too heavy to collide with other atoms.",
                                "Their outermost principal energy levels are completely filled with electrons (stable duplet or octet), giving them maximum stability.",
                                "They contain no electrons in their atomic structure.",
                                "They only react under zero gravity in space."
                            ],
                            "answer": "Their outermost principal energy levels are completely filled with electrons (stable duplet or octet), giving them maximum stability.",
                            "explanation": "Correct! Noble gases possess completely full outer shells (Helium has a full duplet $1s^2$, while Neon and Argon have full octets $ns^2 np^6$), meaning they do not need to lose, gain, or share electrons to attain stability."
                        }
                    },
                    {
                        "type": "knowledge_check",
                        "title": "Knowledge Check: Chemical Similarity of Group 2 Metals",
                        "content": {
                            "question": "Beryllium ($1s^2 2s^2$) and Magnesium ($1s^2 2s^2 2p^6 3s^2$) belong to Group 2. Which statement best explains why they share similar chemical properties?",
                            "options": [
                                "They have the same total number of electrons.",
                                "Both possess exactly 2 valence electrons in their outermost energy level ($s^2$), reacting by losing those 2 electrons to form $+2$ cations.",
                                "They are both colorless gases at room temperature.",
                                "Both need to gain 6 electrons to achieve stability."
                            ],
                            "answer": "Both possess exactly 2 valence electrons in their outermost energy level ($s^2$), reacting by losing those 2 electrons to form $+2$ cations.",
                            "explanation": "Correct! Chemical behavior is governed by valence electron count. Both Be and Mg have 2 outer electrons ($ns^2$) and achieve octet stability by losing these 2 electrons to form divalent $+2$ cations."
                        }
                    }
                ]
            ]
        },

        # =====================================================================
        # LESSON 3: Ion Formation, Valency, and Oxidation Number
        # =====================================================================
        {
            "unit_order": 3,
            "unit_name": "Ion Formation, Valency, and Oxidation Number",
            "unit_description": "Explain cation and anion formation through electron transfer. Define valency (combining power) versus oxidation number (formal signed charge) and examine variable oxidation states in transition metals.",
            "lesson_title": "Ion Formation, Valency, and Oxidation Number",
            "pages": [
                # Card 1: Hook & Objectives
                [
                    {
                        "type": "suggested_image",
                        "title": "The Transformation from Atoms to Ions",
                        "content": {
                            "title": "The Transformation from Atoms to Ions",
                            "caption": "Submicroscopic representation of electron transfer between metallic and non-metallic atoms forming charged ions."
                        }
                    },
                    {
                        "type": "learning_goal",
                        "title": "Lesson Objectives: Ions, Valency, and Oxidation States",
                        "content": {
                            "title": "What We Will Master Today",
                            "goals": [
                                "Explain how neutral atoms transform into **cations ($+$)** and **anions ($-$)** during electron transfer.",
                                "Define **Valency** as combining power (signless whole number) and **Oxidation Number** as formal signed charge.",
                                "Determine valency and oxidation numbers for main group elements from their electron arrangements.",
                                "Interpret variable oxidation states in **transition metals** (e.g., $\\text{Fe}^{2+}$ vs $\\text{Fe}^{3+}$)."
                            ]
                        }
                    },
                    {
                        "type": "concept_explanation",
                        "title": "Breaking the Electrical Balance: How Ions Form",
                        "content": {
                            "title": "From Neutral Atoms to Charged Ions",
                            "text": "In every neutral atom, the number of positive nuclear protons equals the number of negative orbiting electrons ($p^+ = e^-$). The net electrical charge is zero.\n\nHowever, when atoms lose or gain valence electrons in their quest for octet stability, this electrical balance is broken, converting neutral atoms into **ions**."
                        }
                    }
                ],
                # Card 2: Cations vs. Anions
                [
                    {
                        "type": "concept_explanation",
                        "title": "Cations (Positive) and Anions (Negative)",
                        "content": {
                            "title": "Electron Loss vs. Electron Gain",
                            "text": "1. **Cation Formation (Electron Loss)**:\n   - Metal atoms have few valence electrons ($1, 2,$ or $3$). It is energetically favorable to lose them.\n   - *Example: Sodium Atom $\\rightarrow$ Sodium Ion*:\n     $$\\text{Na } (1s^2 2s^2 2p^6 3s^1, 11p^+, 11e^-) \\xrightarrow{-1e^-} \\text{Na}^+ (1s^2 2s^2 2p^6, 11p^+, 10e^-)$$\n     Net charge $= +1$ ($11 - 10 = +1$).\n\n2. **Anion Formation (Electron Gain)**:\n   - Nonmetal atoms have $5, 6,$ or $7$ valence electrons. They gain electrons to complete their octet.\n   - *Example: Chlorine Atom $\\rightarrow$ Chloride Ion*:\n     $$\\text{Cl } (1s^2 2s^2 2p^6 3s^2 3p^5, 17p^+, 17e^-) \\xrightarrow{+1e^-} \\text{Cl}^- (1s^2 2s^2 2p^6 3s^2 3p^6, 17p^+, 18e^-)$$\n     Net charge $= -1$ ($17 - 18 = -1$)."
                        }
                    },
                    {
                        "type": "suggested_diagram",
                        "title": "Electron Transfer: Sodium Cation & Chloride Anion Formation",
                        "content": {
                            "title": "Electron Transfer: Sodium Cation & Chloride Anion Formation",
                            "caption": "Submicroscopic schematic showing 3s¹ electron migration from Sodium to Chlorine resulting in stable Na⁺ and Cl⁻ octets."
                        }
                    }
                ],
                # Card 3: Valency vs. Oxidation Number
                [
                    {
                        "type": "concept_explanation",
                        "title": "Valency vs. Oxidation Number",
                        "content": {
                            "title": "Combining Power vs. Formal Charge",
                            "text": "- **Valency**: The **combining power** of an element. It is the number of electrons an atom loses, gains, or shares to achieve stability. Valency is always a **pure whole number with NO positive or negative sign** (e.g., Sodium = 1, Oxygen = 2, Nitrogen = 3).\n- **Oxidation Number (Oxidation State)**: The **formal electrical charge** an atom appears to carry when bonding in a compound. It is always written **WITH a sign** ($+1, +2, -2, -3$).\n\n### Variable Oxidation Numbers in Transition Metals:\nTransition elements (like Iron or Copper) can exhibit multiple combining powers depending on conditions. We specify the oxidation state using Roman numerals in brackets:\n- $\\text{Fe}^{2+}$ is named **Iron(II)** (Oxidation number $+2$, Valency $2$)\n- $\\text{Fe}^{3+}$ is named **Iron(III)** (Oxidation number $+3$, Valency $3$)"
                        }
                    },
                    {
                        "type": "definition_card",
                        "title": "Core Definition: Valency vs Oxidation Number",
                        "content": {
                            "term": "Valency vs Oxidation Number",
                            "definition": "**Valency** is the combining power of an element expressed as a positive integer without a sign. **Oxidation Number** is the apparent electrostatic charge of an atom within a chemical entity, indicated by a positive or negative sign followed by the integer.",
                            "example": "Oxygen has a valency of 2 and an oxidation number of -2 in water (H₂O)."
                        }
                    }
                ],
                # Card 4: Summary Table for Main Group Elements
                [
                    {
                        "type": "comparison_table",
                        "title": "Atoms to Stable Ions: Valency and Oxidation States",
                        "content": {
                            "headers": ["Element", "Symbol", "Z", "Atom Config", "Stable Ion", "Ion Config ($s/p$)", "Valency", "Oxidation Number"],
                            "rows": [
                                ["Sodium", "Na", "11", "1s² 2s² 2p⁶ 3s¹", "Na⁺", "1s² 2s² 2p⁶ [Ne]", "1", "+1"],
                                ["Magnesium", "Mg", "12", "1s² 2s² 2p⁶ 3s²", "Mg²⁺", "1s² 2s² 2p⁶ [Ne]", "2", "+2"],
                                ["Aluminium", "Al", "13", "1s² 2s² 2p⁶ 3s² 3p¹", "Al³⁺", "1s² 2s² 2p⁶ [Ne]", "3", "+3"],
                                ["Oxygen", "O", "8", "1s² 2s² 2p⁴", "O²⁻", "1s² 2s² 2p⁶ [Ne]", "2", "-2"],
                                ["Nitrogen", "N", "7", "1s² 2s² 2p³", "N³⁻", "1s² 2s² 2p⁶ [Ne]", "3", "-3"],
                                ["Chlorine", "Cl", "17", "1s² 2s² 2p⁶ 3s² 3p⁵", "Cl⁻", "1s² 2s² 2p⁶ 3s² 3p⁶ [Ar]", "1", "-1"]
                            ]
                        }
                    },
                    {
                        "type": "callout",
                        "title": "Protons Never Move During Chemical Reactions!",
                        "content": {
                            "title": "Nuclear Integrity in Chemistry",
                            "text": "A common mistake is thinking that positive ions form by gaining protons. Nuclear protons are locked tightly in the nucleus by the strong nuclear force. All ion formation occurs solely by losing or gaining outer valence electrons!"
                        }
                    }
                ],
                # Card 5: Formative Knowledge Checks
                [
                    {
                        "type": "knowledge_check",
                        "title": "Knowledge Check: Why Magnesium Forms Mg²⁺",
                        "content": {
                            "question": "Why does a Magnesium ion carry a $+2$ charge ($\\text{Mg}^{2+}$) while a neutral Magnesium atom has no charge?",
                            "options": [
                                "The ion gained 2 extra protons in its nucleus.",
                                "The neutral atom lost 2 valence electrons ($3s^2$), leaving 12 positive protons in the nucleus and only 10 negative electrons orbiting.",
                                "The ion shared 2 electrons with another metal atom.",
                                "The nucleus of Magnesium split into two smaller nuclei."
                            ],
                            "answer": "The neutral atom lost 2 valence electrons ($3s^2$), leaving 12 positive protons in the nucleus and only 10 negative electrons orbiting.",
                            "explanation": "Correct! Nuclear protons never change during chemical reactions. Magnesium ($Z=12$) has 12 protons ($12+$). When it loses its 2 valence electrons to form an octet, it has 10 electrons ($10-$), resulting in a net charge of $12 - 10 = +2$."
                        }
                    },
                    {
                        "type": "knowledge_check",
                        "title": "Knowledge Check: Electron Configuration of Oxide Ion",
                        "content": {
                            "question": "What is the $s$ and $p$ electron configuration of an Oxide ion ($\\text{O}^{2-}$)? (Atomic number of Oxygen = 8)",
                            "options": [
                                "$1s^2 2s^2 2p^4$",
                                "$1s^2 2s^2 2p^2$",
                                "$1s^2 2s^2 2p^6$",
                                "$1s^2 2s^2 2p^6 3s^2$"
                            ],
                            "answer": "$1s^2 2s^2 2p^6$",
                            "explanation": "Correct! Neutral Oxygen has 8 electrons ($1s^2 2s^2 2p^4$). To form an Oxide anion ($\\text{O}^{2-}$), it gains 2 electrons to complete its valence shell: $8 + 2 = 10$ electrons, giving configuration $1s^2 2s^2 2p^6$ (isoelectronic with Neon)."
                        }
                    }
                ]
            ]
        },

        # =====================================================================
        # LESSON 4: Formulae of Compounds and Radicals
        # =====================================================================
        {
            "unit_order": 4,
            "unit_name": "Formulae of Compounds and Radicals",
            "unit_description": "Master the valency swap (crossover) method for writing binary and polyatomic compound formulae. Learn common radicals and apply the mandatory bracket rule.",
            "lesson_title": "Formulae of Compounds and Radicals",
            "pages": [
                # Card 1: Hook & Objectives
                [
                    {
                        "type": "suggested_image",
                        "title": "Chemical Recipes: Formulating Compounds",
                        "content": {
                            "title": "Chemical Recipes: Formulating Compounds",
                            "caption": "Crystalline inorganic compounds demonstrating stoichiometric ratios and electroneutrality in chemical formulae."
                        }
                    },
                    {
                        "type": "learning_goal",
                        "title": "Lesson Objectives: Writing Chemical Formulae",
                        "content": {
                            "title": "What We Will Master Today",
                            "goals": [
                                "Identify common **polyatomic radicals** (Ammonium, Hydroxide, Nitrate, Carbonate, Sulfate, Phosphate) and their valencies.",
                                "Apply the **5-Step Valency Swap (Crossover) Method** to derive neutral chemical formulae.",
                                "Simplify subscript ratios to lowest whole numbers.",
                                "Enforce the **Radical Bracket Rule** correctly (e.g., $\\text{Mg(OH)}_2$ vs $\\text{MgOH}_2$)."
                            ]
                        }
                    },
                    {
                        "type": "concept_explanation",
                        "title": "Chemical Formulae: The Universal Recipes of Chemistry",
                        "content": {
                            "title": "The Recipe of Matter",
                            "text": "A **chemical formula** tells us which elements are present in a substance and the exact ratio of atoms or ions combined to create a neutral compound with zero net charge."
                        }
                    }
                ],
                # Card 2: Polyatomic Radicals Matrix
                [
                    {
                        "type": "comparison_table",
                        "title": "Essential Polyatomic Radicals (Grade 10 Reference)",
                        "content": {
                            "headers": ["Radical Name", "Formula & Charge", "Valency", "Oxidation State", "Common Compound Example"],
                            "rows": [
                                ["Ammonium", "NH₄⁺", "1", "+1", "Ammonium Nitrate: NH₄NO₃"],
                                ["Hydroxide", "OH⁻", "1", "-1", "Sodium Hydroxide: NaOH"],
                                ["Nitrate", "NO₃⁻", "1", "-1", "Potassium Nitrate: KNO₃"],
                                ["Carbonate", "CO₃²⁻", "2", "-2", "Calcium Carbonate: CaCO₃"],
                                ["Sulfate", "SO₄²⁻", "2", "-2", "Copper(II) Sulfate: CuSO₄"],
                                ["Phosphate", "PO₄³⁻", "3", "-3", "Calcium Phosphate: Ca₃(PO₄)₂"]
                            ]
                        }
                    },
                    {
                        "type": "definition_card",
                        "title": "Core Definition: Polyatomic Radical",
                        "content": {
                            "term": "Polyatomic Radical",
                            "definition": "A tightly bound cluster of atoms of different elements carrying a net overall electrical charge that behaves as a single indivisible chemical unit during reactions.",
                            "example": "The sulfate radical (SO₄²⁻) consists of 1 sulfur and 4 oxygen atoms carrying a -2 charge."
                        }
                    }
                ],
                # Card 3: The 5-Step Valency Swap Method & Bracket Rule
                [
                    {
                        "type": "step_process",
                        "title": "The 5-Step Valency Swap (Crossover) Protocol",
                        "content": {
                            "title": "Step-by-Step Formula Derivation",
                            "steps": [
                                "1. **Write Symbols**: Write the cation (metal) first, anion (nonmetal/radical) second side-by-side.",
                                "2. **Write Valencies**: Place the valency numbers directly above each symbol.",
                                "3. **Cross Over (Swap)**: Swap the numbers diagonally and write them as subscripts at the bottom-right.",
                                "4. **Simplify Subscripts**: Divide subscripts by their highest common factor to reduce to the lowest whole-number ratio (e.g., $\\text{C}_2\\text{O}_4 \\rightarrow \\text{CO}_2$). Omit the subscript '1'.",
                                "5. **Apply Radical Bracket Rule**: If a polyatomic radical has a crossed-over subscript of 2 or more, wrap the entire radical in brackets before writing the subscript (e.g., $\\text{Mg(OH)}_2$)."
                            ]
                        }
                    },
                    {
                        "type": "suggested_diagram",
                        "title": "The Valency Swap Method and Bracket Rule",
                        "content": {
                            "title": "The Valency Swap Method and Bracket Rule",
                            "caption": "Diagonal crossover arrows illustrating formula derivation for Aluminium Oxide (Al₂O₃) and Magnesium Hydroxide (Mg(OH)₂)."
                        }
                    }
                ],
                # Card 4: Worked Examples & Common Mistake Alert
                [
                    {
                        "type": "worked_example",
                        "title": "Worked Examples: Formula Derivation",
                        "content": {
                            "title": "Mastering the Valency Crossover",
                            "text": "### Example 1: Aluminium Oxide\n- Symbols: $\\text{Al}$ (valency 3) and $\\text{O}$ (valency 2)\n- Crossover: $\\text{Al}^3 \\quad \\text{O}^2 \\xrightarrow{\\text{Swap}} \\mathbf{Al_2O_3}$\n- Ratio $2:3$ cannot be simplified. Formula is $\\mathbf{Al_2O_3}$.\n\n### Example 2: Magnesium Hydroxide\n- Symbols: $\\text{Mg}$ (valency 2) and radical $\\text{OH}$ (valency 1)\n- Crossover: $\\text{Mg}^2 \\quad (\\text{OH})^1 \\xrightarrow{\\text{Swap}} \\text{Mg}_1(\\text{OH})_2$\n- Omit '1' and apply brackets: $\\mathbf{Mg(OH)_2}$."
                        }
                    },
                    {
                        "type": "common_misconception",
                        "title": "Common Mistake Alert: The Bracket Rule",
                        "content": {
                            "misconception": "Writing $\\text{MgOH}_2$ instead of $\\text{Mg(OH)}_2$.",
                            "correction": "$\\text{MgOH}_2$ means 1 magnesium, 1 oxygen, and 2 hydrogens (incorrect!). $\\text{Mg(OH)}_2$ means 1 magnesium and 2 entire hydroxide units $(\\text{OH}^-)$ balancing the $+2$ charge of $\\text{Mg}^{2+}$.",
                            "why_it_matters": "Omitting brackets violates radical stoichiometry and results in incorrect molar mass calculations."
                        }
                    }
                ],
                # Card 5: Formative Knowledge Checks
                [
                    {
                        "type": "knowledge_check",
                        "title": "Knowledge Check: Formula of Calcium Nitrate",
                        "content": {
                            "question": "What is the correct chemical formula of Calcium Nitrate? (Valency of Calcium = 2; Nitrate radical is $\\text{NO}_3^-$ with valency 1)",
                            "options": [
                                "$\\text{CaNO}_3$",
                                "$\\text{Ca}_2\\text{NO}_3$",
                                "$\\text{Ca(NO}_3)_2$",
                                "$\\text{Ca(NO}_3)_3$"
                            ],
                            "answer": "$\\text{Ca(NO}_3)_2$",
                            "explanation": "Correct! Calcium has valency 2 and Nitrate has valency 1. Swapping gives $\\text{Ca}_1(\\text{NO}_3)_2$. We omit subscript 1 and keep brackets around the radical, giving $\\text{Ca(NO}_3)_2$."
                        }
                    },
                    {
                        "type": "knowledge_check",
                        "title": "Knowledge Check: Formula of Ammonium Sulfate",
                        "content": {
                            "question": "Ammonium Sulfate is a widely used agricultural fertilizer in Kenya. What is its correct chemical formula? (Ammonium is $\\text{NH}_4^+$ with valency 1; Sulfate is $\\text{SO}_4^{2-}$ with valency 2)",
                            "options": [
                                "$\\text{NH}_4\\text{SO}_4$",
                                "$(\\text{NH}_4)_2\\text{SO}_4$",
                                "$\\text{NH}_4(\\text{SO}_4)_2$",
                                "$(\\text{NH}_4)_2(\\text{SO}_4)_2$"
                            ],
                            "answer": "$(\\text{NH}_4)_2\\text{SO}_4$",
                            "explanation": "Correct! Swapping valencies between $(\\text{NH}_4)^1$ and $(\\text{SO}_4)^2$ gives $(\\text{NH}_4)_2(\\text{SO}_4)_1$. We omit the subscript 1 on Sulfate, resulting in $(\\text{NH}_4)_2\\text{SO}_4$."
                        }
                    }
                ]
            ]
        },

        # =====================================================================
        # LESSON 5: Chemical Equations and Balancing
        # =====================================================================
        {
            "unit_order": 5,
            "unit_name": "Chemical Equations and Balancing",
            "unit_description": "Translate word equations into balanced chemical equations. Apply the Law of Conservation of Mass, incorporate state symbols, and balance coefficients step-by-step.",
            "lesson_title": "Chemical Equations and Balancing",
            "pages": [
                # Card 1: Hook & Objectives
                [
                    {
                        "type": "suggested_image",
                        "title": "The Conservation of Mass in Chemical Reactions",
                        "content": {
                            "title": "The Conservation of Mass in Chemical Reactions",
                            "caption": "Laboratory balance verifying the conservation of mass during chemical precipitation reactions."
                        }
                    },
                    {
                        "type": "learning_goal",
                        "title": "Lesson Objectives: Chemical Equations & Balancing",
                        "content": {
                            "title": "What We Will Master Today",
                            "goals": [
                                "Identify **reactants**, **products**, and state symbols ($(s), (l), (g), (aq)$) in chemical equations.",
                                "Apply the **Law of Conservation of Mass** to explain why equations must be balanced.",
                                "Distinguish between **coefficients** (amounts) and **subscripts** (chemical identity).",
                                "Balance complex chemical equations step-by-step using systematic atom accounting."
                            ]
                        }
                    },
                    {
                        "type": "concept_explanation",
                        "title": "The Language of Equations: Reactants to Products",
                        "content": {
                            "title": "Shorthand for Chemical Transformations",
                            "text": "When you bake a cake, you combine raw ingredients and transform them into a delicious new food. In chemistry, we represent chemical transformations using **chemical equations**:\n\n$$\\text{Reactants (Starting Materials)} \\xrightarrow{\\text{Yields}} \\text{Products (New Substances)}$$\n\nWe include **state symbols** to describe physical states in the laboratory: $(s)$ for solid, $(l)$ for pure liquid, $(g)$ for gas, and $(aq)$ for aqueous solution (dissolved in water)."
                        }
                    }
                ],
                # Card 2: The Law of Conservation of Mass
                [
                    {
                        "type": "concept_explanation",
                        "title": "The Law of Conservation of Mass",
                        "content": {
                            "title": "Matter Cannot Be Created or Destroyed",
                            "text": "Formulated by Antoine Lavoisier in 1789, the **Law of Conservation of Mass** states that matter is neither created nor destroyed during chemical reactions.\n\nEvery single atom present in the reactants must be accounted for in the products. Atoms are simply rearranged into new chemical combinations. To obey this fundamental law, every chemical equation must be **balanced**."
                        }
                    },
                    {
                        "type": "definition_card",
                        "title": "Core Rule: Coefficients vs Subscripts",
                        "content": {
                            "term": "The Golden Rule of Balancing",
                            "definition": "You can ONLY adjust stoichiometric coefficients (the numbers in front of a formula). You must NEVER alter chemical subscripts, because changing subscripts changes the fundamental identity of the substance.",
                            "example": "Changing H₂O to H₂O₂ turns harmless water into toxic hydrogen peroxide!"
                        }
                    }
                ],
                # Card 3: Step-by-Step Balancing Protocol
                [
                    {
                        "type": "step_process",
                        "title": "Step-by-Step Equation Balancing Protocol",
                        "content": {
                            "title": "Systematic Atom Accounting",
                            "steps": [
                                "1. **Write Skeleton Equation**: Write correct chemical formulae for all reactants and products with state symbols.",
                                "2. **Count Atoms on Both Sides**: Tabulate the number of atoms of each element on the reactant side vs product side.",
                                "3. **Balance Elements One by One**: Adjust coefficients in front of formulae to equalize atom counts (tip: balance metals first, then nonmetals, leaving hydrogen and oxygen last).",
                                "4. **Recount Atoms**: Re-tally all elements to verify that the multiplier has balanced all constituent atoms.",
                                "5. **Confirm Lowest Whole Numbers**: Ensure coefficients are in their simplest whole-number ratio."
                            ]
                        }
                    },
                    {
                        "type": "suggested_diagram",
                        "title": "Submicroscopic Atom Accounting: 2Mg + O₂ → 2MgO",
                        "content": {
                            "title": "Submicroscopic Atom Accounting: 2Mg + O₂ → 2MgO",
                            "caption": "Visual particle diagram demonstrating atom conservation before and after the reaction: 2 Mg atoms + 1 O₂ molecule yields 2 MgO formula units."
                        }
                    }
                ],
                # Card 4: Worked Example: Iron Rusting Reaction
                [
                    {
                        "type": "worked_example",
                        "title": "Worked Balancing: The Rusting of Iron",
                        "content": {
                            "title": "Balancing 4Fe + 3O₂ → 2Fe₂O₃",
                            "text": "**Reaction**: Solid Iron reacts with Oxygen gas to form solid Iron(III) Oxide (rust).\n\n- **Step 1 (Skeleton)**: $\\text{Fe}(s) + \\text{O}_2(g) \\longrightarrow \\text{Fe}_2\\text{O}_3(s)$\n- **Step 2 (Atom Count)**: Left: $\\text{Fe}=1, \\text{O}=2$. Right: $\\text{Fe}=2, \\text{O}=3$.\n- **Step 3 (Balance Oxygen)**: LCM of 2 and 3 is 6. Place $3$ in front of $\\text{O}_2$ and $2$ in front of $\\text{Fe}_2\\text{O}_3$:\n  $$\\text{Fe}(s) + 3\\text{O}_2(g) \\longrightarrow 2\\text{Fe}_2\\text{O}_3(s)$$\n- **Step 4 (Balance Iron)**: Right side has $2 \\times 2 = 4$ Iron atoms. Place $4$ in front of reactant $\\text{Fe}$:\n  $$\\mathbf{4Fe(s) + 3O_2(g) \\longrightarrow 2Fe_2O_3(s)}$$\n- **Step 5 (Final Check)**: Reactants: $4\\text{Fe}, 6\\text{O}$. Products: $4\\text{Fe}, 6\\text{O}$. Perfectly balanced!"
                        }
                    },
                    {
                        "type": "callout",
                        "title": "Recognizing Diatomic Elements in Equations",
                        "content": {
                            "title": "The Diatomic 7",
                            "text": "Remember that seven nonmetal elements exist as diatomic molecules when in elemental form: $\\text{H}_2, \\text{N}_2, \\text{O}_2, \\text{F}_2, \\text{Cl}_2, \\text{Br}_2, \\text{I}_2$. Always write them with a subscript 2 when they appear as pure elemental reactants or products!"
                        }
                    }
                ],
                # Card 5: Formative Knowledge Checks
                [
                    {
                        "type": "knowledge_check",
                        "title": "Knowledge Check: Why Subscripts Cannot Be Changed",
                        "content": {
                            "question": "Why is it scientifically invalid to balance the reaction $\\text{H}_2 + \\text{O}_2 \\longrightarrow \\text{H}_2\\text{O}$ by writing $\\text{H}_2 + \\text{O}_2 \\longrightarrow \\text{H}_2\\text{O}_2$?",
                            "options": [
                                "Because $\\text{H}_2\\text{O}_2$ is an imaginary substance that does not exist.",
                                "Because changing subscripts changes the chemical identity from water ($\\text{H}_2\\text{O}$) into hydrogen peroxide ($\\text{H}_2\\text{O}_2$).",
                                "Because oxygen atoms cannot have subscripts.",
                                "Because the reaction would produce solid ice instead of liquid water."
                            ],
                            "answer": "Because changing subscripts changes the chemical identity from water ($\\text{H}_2\\text{O}$) into hydrogen peroxide ($\\text{H}_2\\text{O}_2$).",
                            "explanation": "Correct! Changing a subscript alters the molecular identity of the substance. Coefficients in front of formulae must be adjusted instead to change the amount of molecules while preserving substance identity."
                        }
                    },
                    {
                        "type": "knowledge_check",
                        "title": "Knowledge Check: Balanced Equation for Ammonia Synthesis",
                        "content": {
                            "question": "Which of the following represents the correctly balanced equation for the synthesis of Ammonia ($\\text{NH}_3$) from Nitrogen and Hydrogen gases?",
                            "options": [
                                "$\\text{N}_2(g) + \\text{H}_2(g) \\longrightarrow \\text{NH}_3(g)$",
                                "$\\text{N}_2(g) + 3\\text{H}_2(g) \\longrightarrow 2\\text{NH}_3(g)$",
                                "$2\\text{N}(g) + 6\\text{H}(g) \\longrightarrow 2\\text{NH}_3(g)$",
                                "$\\text{N}_2(g) + 2\\text{H}_2(g) \\longrightarrow 2\\text{NH}_3(g)$"
                            ],
                            "answer": "$\\text{N}_2(g) + 3\\text{H}_2(g) \\longrightarrow 2\\text{NH}_3(g)$",
                            "explanation": "Correct! Left side: $2\\text{ N}$ atoms and $3 \\times 2 = 6\\text{ H}$ atoms. Right side: $2 \\times 1 = 2\\text{ N}$ atoms and $2 \\times 3 = 6\\text{ H}$ atoms. The equation obeys the Law of Conservation of Mass."
                        }
                    }
                ]
            ]
        },

        # =====================================================================
        # LESSON 6: Periodic Table-to-Reaction Integration
        # =====================================================================
        {
            "unit_order": 6,
            "unit_name": "Periodic Table-to-Reaction Integration",
            "unit_description": "Synthesize the 4-step chemical reasoning chain: from electron configuration to stable ion prediction, compound formula derivation, and final balanced chemical equation.",
            "lesson_title": "Periodic Table-to-Reaction Integration",
            "pages": [
                # Card 1: Hook & Objectives
                [
                    {
                        "type": "suggested_image",
                        "title": "The Master Chemistry Reasoning Pathway",
                        "content": {
                            "title": "The Master Chemistry Reasoning Pathway",
                            "caption": "Modern chemical laboratory synthesizing novel inorganic compounds through periodic property predictions."
                        }
                    },
                    {
                        "type": "learning_goal",
                        "title": "Lesson Objectives: Chemistry Reasoning Chain",
                        "content": {
                            "title": "What We Will Master Today",
                            "goals": [
                                "Execute the **4-Step Chemistry Reasoning Chain** connecting atomic structure to chemical reactions.",
                                "Predict unknown compound formulae from Periodic Table coordinates.",
                                "Write complete balanced equations with correct state symbols for reactions between metals and nonmetals.",
                                "Achieve mastery across the complete Grade 10 CBC Topic 1.3 syllabus."
                            ]
                        }
                    },
                    {
                        "type": "concept_explanation",
                        "title": "The Master Reasoning Chain: Connecting All the Pieces",
                        "content": {
                            "title": "Thinking Like a Research Chemist",
                            "text": "You now possess all the core tools of chemical theory! When a chemist wants to predict how two elements will react, they follow an unbroken logical chain:\n\n$$\\text{1. Electron Configuration} \\longrightarrow \\text{2. Stable Ion Formed} \\longrightarrow \\text{3. Compound Formula} \\longrightarrow \\text{4. Balanced Equation}$$\n\nLet us trace this complete pathway with a real reaction challenge."
                        }
                    }
                ],
                # Card 2: Full Worked Case Study: Aluminium + Oxygen
                [
                    {
                        "type": "worked_example",
                        "title": "Full Synthesis Case Study: Aluminium Metal + Oxygen Gas",
                        "content": {
                            "title": "The 4-Step Pathway in Action",
                            "text": "- **Step 1 (Electron Configurations)**:\n  - Aluminium ($Z=13$): $1s^2 2s^2 2p^6 3s^2 3p^1$ ($3$ valence electrons).\n  - Oxygen ($Z=8$): $1s^2 2s^2 2p^4$ ($6$ valence electrons).\n- **Step 2 (Predict Stable Ions)**:\n  - Aluminium loses 3 electrons $\\rightarrow \\text{Al}^{3+}$ (valency 3).\n  - Oxygen gains 2 electrons $\\rightarrow \\text{O}^{2-}$ (valency 2).\n- **Step 3 (Derive Formula)**:\n  - Crossover valencies: $\\text{Al}^3 \\quad \\text{O}^2 \\rightarrow \\mathbf{Al_2O_3}$ (Aluminium Oxide).\n- **Step 4 (Write & Balance Equation)**:\n  - Skeleton: $\\text{Al}(s) + \\text{O}_2(g) \\longrightarrow \\text{Al}_2\\text{O}_3(s)$\n  - Balance Oxygen: $\\text{Al}(s) + 3\\text{O}_2(g) \\longrightarrow 2\\text{Al}_2\\text{O}_3(s)$\n  - Balance Aluminium: $\\mathbf{4Al(s) + 3O_2(g) \\longrightarrow 2Al_2O_3(s)}$."
                        }
                    },
                    {
                        "type": "suggested_diagram",
                        "title": "The 4-Step Chemistry Reasoning Pathway: Element to Balanced Equation",
                        "content": {
                            "title": "The 4-Step Chemistry Reasoning Pathway: Element to Balanced Equation",
                            "caption": "Sequential roadmap linking electron configuration, ion formation, formula derivation, and stoichiometric equation balancing."
                        }
                    }
                ],
                # Card 3: Summary & Transition to Chemical Bonding
                [
                    {
                        "type": "summary",
                        "title": "Topic 1.3 Master Summary & Key Takeaways",
                        "content": {
                            "title": "Key Periodic Principles Mastered",
                            "summary_points": [
                                "**Periodic Grid**: Periodic Table is arranged by increasing Atomic Number ($Z$). Groups = valence electrons; Periods = occupied shells.",
                                "**Chemical Families**: Group 1 (Alkali Metals), Group 2 (Alkaline Earth), Group 17 (Halogens), Group 18 (Noble Gases).",
                                "**Stability Quest**: Atoms react to achieve stable noble gas configurations (Duplet or Octet).",
                                "**Valency vs Oxidation Number**: Valency is combining power (signless integer); Oxidation number is signed formal charge.",
                                "**Formula Derivation**: Valency swap crossover method balances charges to form neutral compounds; use brackets for multiple polyatomic radicals.",
                                "**Balancing Equations**: Obeys Law of Conservation of Mass by adjusting coefficients in front of formulas, never subscripts."
                            ]
                        }
                    },
                    {
                        "type": "transition",
                        "title": "Looking Ahead: Topic 1.4 — Chemical Bonding",
                        "content": {
                            "title": "Next Step: Topic 1.4 — Chemical Bonding",
                            "text": "Now that you can predict compound formulae and write balanced equations, you are ready to explore **Chemical Bonding**! You will examine the forces that hold atoms and ions together (Ionic, Covalent, Metallic) and discover how microscopic bonding dictates macroscopic material properties."
                        }
                    }
                ],
                # Card 4: Collaborative Inquiry Synthesis
                [
                    {
                        "type": "concept_explanation",
                        "title": "Applying the Chemical Pathway in Everyday Life",
                        "content": {
                            "title": "From Soil Chemistry to Industrial Synthesis",
                            "text": "Whether calculating fertilizer dosages (such as Ammonium Nitrate $\\text{NH}_4\\text{NO}_3$ and Calcium Phosphate $\\text{Ca}_3(\\text{PO}_4)_2$) or analyzing water treatment chemicals (such as Aluminium Sulfate $\\text{Al}_2(\\text{SO}_4)_3$), the Periodic Table provides the predictive framework for modern science and agriculture."
                        }
                    },
                    {
                        "type": "callout",
                        "title": "Exam Strategy: The Golden 4-Step Checklist",
                        "content": {
                            "title": "Always Write Down Configurations First",
                            "text": "When tackling complex chemical synthesis problems on national examinations, always begin by writing out the ground-state electron configuration of the reacting elements. It unlocks group position, ion charge, valency, formula, and stoichiometric ratios instantly!"
                        }
                    }
                ],
                # Card 5: End-of-Topic Mastery Challenges
                [
                    {
                        "type": "knowledge_check",
                        "title": "Mastery Challenge: Predicting Compound WZ₂",
                        "content": {
                            "question": "Element W is in Group 2, Period 3. It reacts with element Z which is in Group 17, Period 2. What is the correct formula of the compound formed between W and Z?",
                            "options": [
                                "$\\text{WZ}$",
                                "$\\text{W}_2\\text{Z}$",
                                "$\\text{WZ}_2$",
                                "$\\text{W}_2\\text{Z}_7$"
                            ],
                            "answer": "$\\text{WZ}_2$",
                            "explanation": "Correct! Element W (Group 2) has 2 valence electrons and forms $\\text{W}^{2+}$ (valency 2). Element Z (Group 17) has 7 valence electrons and forms $\\text{Z}^-$ (valency 1). Swapping valencies yields $\\text{WZ}_2$."
                        }
                    },
                    {
                        "type": "knowledge_check",
                        "title": "Mastery Challenge: Sodium and Chlorine Gas Reaction",
                        "content": {
                            "question": "Which of the following represents the correctly balanced equation for the reaction between solid Sodium metal and gaseous Chlorine gas to form solid Sodium Chloride?",
                            "options": [
                                "$\\text{Na}(s) + \\text{Cl}(g) \\longrightarrow \\text{NaCl}(s)$",
                                "$2\\text{Na}(s) + \\text{Cl}_2(g) \\longrightarrow 2\\text{NaCl}(s)$",
                                "$\\text{Na}(s) + \\text{Cl}_2(g) \\longrightarrow \\text{NaCl}_2(s)$",
                                "$2\\text{Na}(s) + 2\\text{Cl}(g) \\longrightarrow 2\\text{NaCl}(s)$"
                            ],
                            "answer": "$2\\text{Na}(s) + \\text{Cl}_2(g) \\longrightarrow 2\\text{NaCl}(s)$",
                            "explanation": "Correct! Elemental chlorine is a diatomic gas ($\\text{Cl}_2(g)$). Sodium forms $\\text{Na}^+$ and chlorine forms $\\text{Cl}^-$, producing $\\text{NaCl}(s)$. The balanced equation is $2\\text{Na}(s) + \\text{Cl}_2(g) \\longrightarrow 2\\text{NaCl}(s)$."
                        }
                    }
                ]
            ]
        }
    ]

@transaction.atomic
def ingest_topic3():
    print("=" * 80)
    print("INGESTING GRADE 10 CHEMISTRY — TOPIC 3: THE PERIODIC TABLE")
    print("=" * 80)

    # 1. Resolve Hierarchy
    cbc = Curriculum.objects.filter(name__icontains="CBC").first()
    grade10 = Grade.objects.filter(curriculum=cbc, level=10).first()
    chem = Subject.objects.filter(grade=grade10, id=5).first() or Subject.objects.filter(grade=grade10, name__icontains="Chem").first()

    print(f"Target Subject: [{chem.id}] {chem.name} (Grade: {grade10.name}, Curr: {cbc.name})")

    # 2. Resolve or Create Topic 3
    topic, created = Topic.objects.get_or_create(
        subject=chem,
        order=3,
        defaults={
            "name": "The Periodic Table",
            "description": "Trace the historical development of the Periodic Table, categorize chemical families and stability pathways, derive compound formulae using valencies and radicals, and write balanced chemical equations."
        }
    )
    if not created:
        topic.name = "The Periodic Table"
        topic.description = "Trace the historical development of the Periodic Table, categorize chemical families and stability pathways, derive compound formulae using valencies and radicals, and write balanced chemical equations."
        topic.save()
    print(f"Resolved Topic 3: [{topic.id}] {topic.name}")

    # 3. Ingest Lessons & Blocks
    curriculum_data = build_topic3_curriculum()

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

    print("\nSUCCESS: Topic 3 Ingestion Completed Idempotently!")

if __name__ == "__main__":
    ingest_topic3()
