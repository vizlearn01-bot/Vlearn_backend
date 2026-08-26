"""
VLearn CBC Grade 10 Chemistry — Topic 4: Chemical Bonding
Production Ingestion Engine (Senior Secondary Pedagogical Edition)

Curriculum: CBC (ID: 5)
Grade: Grade 10 (ID: 5, Level: 10)
Subject: Chemistry (ID: 5)
Topic: Chemical Bonding (Topic Order: 4)

Decomposed into 6 Learning Units & 6 Published Lessons:
  1. Stability and Valence Electrons in Bonding (5 Pages, 11 Blocks)
  2. Ionic Bonding and Giant Ionic Structures (5 Pages, 11 Blocks)
  3. Covalent and Dative Covalent Bonding (5 Pages, 11 Blocks)
  4. Intermolecular Forces and Metallic Bonding (5 Pages, 11 Blocks)
  5. Giant Atomic/Covalent and Giant Metallic Structures (5 Pages, 11 Blocks)
  6. Bonding, Properties, Uses, and Model Project (5 Pages, 11 Blocks)
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

def build_topic4_curriculum():
    """Returns the comprehensive pedagogical page and block structure for Grade 10 Topic 4: Chemical Bonding."""
    return [
        # =====================================================================
        # LESSON 1: Stability and Valence Electrons in Bonding
        # =====================================================================
        {
            "unit_order": 1,
            "unit_name": "Stability and Valence Electrons in Bonding",
            "unit_description": "Explore the nature of chemical bonds as attractive forces holding atoms together. Understand why only valence electrons participate in bonding and learn Lewis dot-and-cross structures.",
            "lesson_title": "Stability and Valence Electrons in Bonding",
            "pages": [
                # Card 1: Hook & Objectives
                [
                    {
                        "type": "suggested_image",
                        "title": "The Chemical Cement of the Universe",
                        "content": {
                            "title": "The Chemical Cement of the Universe",
                            "caption": "Molecular orbital visualization of electron density sharing between bonded atoms in a crystal lattice."
                        }
                    },
                    {
                        "type": "learning_goal",
                        "title": "Lesson Objectives: The Nature of Chemical Bonds",
                        "content": {
                            "title": "What We Will Master Today",
                            "goals": [
                                "Define a **chemical bond** as the strong attractive force linking atoms, ions, or molecules.",
                                "Explain why **valence electrons** participate in bonding while inner-core electrons remain inert.",
                                "Construct **Lewis dot-and-cross structures** for the first 20 elements.",
                                "Differentiate between electron transfer and electron sharing as pathways to octet/duplet stability."
                            ]
                        }
                    },
                    {
                        "type": "concept_explanation",
                        "title": "Why Do Atoms Stick Together?",
                        "content": {
                            "title": "The Snapping Together of Matter",
                            "text": "Have you ever held two strong magnets close to each other and felt them snap together with a satisfying click? Or watched bricks being cemented into an unshakeable wall?\n\nIn the submicroscopic world, atoms undergo **chemical bonding** to stick together permanently. Without chemical bonds, water would not exist, rocks would crumble into individual atoms, and living organisms could not survive!"
                        }
                    }
                ],
                # Card 2: Valence Electrons in Bonding
                [
                    {
                        "type": "concept_explanation",
                        "title": "The Exclusivity of Valence Electrons",
                        "content": {
                            "title": "Why Inner Electrons Do Not Bond",
                            "text": "Atoms are on a continuous quest to achieve stable noble gas configurations ($2$ outer electrons for duplet, $8$ for octet).\n\nWhen two atoms collide, their inner-core electrons are held extremely tightly by the positive nucleus in filled, stable energy levels. Only the outermost **valence electrons** are exposed, flexible, and free to participate in chemical bonding by being transferred or shared!"
                        }
                    },
                    {
                        "type": "definition_card",
                        "title": "Core Definition: Chemical Bond",
                        "content": {
                            "term": "Chemical Bond",
                            "definition": "A persistent attractive electrostatic force that holds atoms, ions, or molecules together to create stable chemical substances with lower potential energy.",
                            "example": "The electrostatic attraction between sodium cations (Na⁺) and chloride anions (Cl⁻) in table salt."
                        }
                    }
                ],
                # Card 3: Lewis Structures (Dot-and-Cross)
                [
                    {
                        "type": "concept_explanation",
                        "title": "Gilbert N. Lewis & Dot-and-Cross Diagrams",
                        "content": {
                            "title": "Symbolic Shorthand for Valence Electrons",
                            "text": "In 1916, American chemist Gilbert N. Lewis invented **Lewis dot-and-cross diagrams**:\n\n- The chemical symbol represents the atomic nucleus and all inner core electrons.\n- Valence electrons are drawn as small **dots ($\\bullet$)** or **crosses ($\\times$)** arranged in pairs around the symbol.\n- *Why use both dots and crosses?* While all electrons are physically identical, using dots for one element and crosses for another lets chemists visually track the origin and movement of valence electrons during chemical reactions!"
                        }
                    },
                    {
                        "type": "suggested_diagram",
                        "title": "Lewis Dot-and-Cross Structures for the First 20 Elements",
                        "content": {
                            "title": "Lewis Dot-and-Cross Structures for the First 20 Elements",
                            "caption": "Grid of Lewis structures showing valence electron arrangements (dots and crosses) across Groups 1, 2, 13, 14, 15, 16, 17, and 18."
                        }
                    }
                ],
                # Card 4: Lewis Representation Examples
                [
                    {
                        "type": "worked_example",
                        "title": "Drawing Lewis Structures for Reacting Atoms",
                        "content": {
                            "title": "Sodium and Chlorine Dot-and-Cross Setup",
                            "text": "- **Sodium (Na, $Z=11$)**: Ground state $1s^2 2s^2 2p^6 3s^1$. Outermost level $n=3$ has **1 valence electron**. We draw: $\\text{Na}\\times$.\n- **Chlorine (Cl, $Z=17$)**: Ground state $1s^2 2s^2 2p^6 3s^2 3p^5$. Outermost level $n=3$ has $2 + 5 = \\mathbf{7}$ **valence electrons**. We draw $\\text{Cl}$ surrounded by 3 pairs of dots and 1 lone dot."
                        }
                    },
                    {
                        "type": "callout",
                        "title": "Electrons are Indistinguishable in Nature",
                        "content": {
                            "title": "A Pedagogical Convention",
                            "text": "Remember: dots and crosses are a convenient human bookkeeping tool. In quantum reality, all electrons are completely identical and exchangeable subatomic wave-particles."
                        }
                    }
                ],
                # Card 5: Formative Knowledge Checks
                [
                    {
                        "type": "knowledge_check",
                        "title": "Knowledge Check: Why Inner-Core Electrons Do Not Bond",
                        "content": {
                            "question": "Why do inner-core electrons not participate in chemical reactions and bonding?",
                            "options": [
                                "They are too heavy and have no electrical charge.",
                                "They carry positive charges that repel other atoms.",
                                "They are tightly held by the positive nucleus in completely filled, stable energy levels.",
                                "They do not exist in neutral nonmetal atoms."
                            ],
                            "answer": "They are tightly held by the positive nucleus in completely filled, stable energy levels.",
                            "explanation": "Correct! Inner energy levels are completely filled, energetically stable, and shielded close to the nucleus. Only the outermost valence electrons have high enough energy and spatial exposure to interact during collisions."
                        }
                    },
                    {
                        "type": "knowledge_check",
                        "title": "Knowledge Check: Lewis Dot Count for Nitrogen",
                        "content": {
                            "question": "An atom of Nitrogen has the ground-state electron configuration $1s^2 2s^2 2p^3$. How many dots or crosses should be drawn around its chemical symbol in its Lewis structure?",
                            "options": [
                                "2 dots",
                                "3 dots",
                                "5 dots",
                                "7 dots"
                            ],
                            "answer": "5 dots",
                            "explanation": "Correct! The outermost occupied energy level is $n=2$, containing $2$ (in $2s$) $+ 3$ (in $2p$) $= 5$ valence electrons. Therefore, exactly 5 dots or crosses are drawn around the symbol N."
                        }
                    }
                ]
            ]
        },

        # =====================================================================
        # LESSON 2: Ionic Bonding and Giant Ionic Structures
        # =====================================================================
        {
            "unit_order": 2,
            "unit_name": "Ionic Bonding and Giant Ionic Structures",
            "unit_description": "Examine electron transfer from metals to nonmetals, forming ionic bonds and giant 3D ionic lattices. Explain hallmark properties: high melting points, brittleness, and electrical conductivity.",
            "lesson_title": "Ionic Bonding and Giant Ionic Structures",
            "pages": [
                # Card 1: Hook & Objectives
                [
                    {
                        "type": "suggested_image",
                        "title": "The Crystalline Architecture of Salt",
                        "content": {
                            "title": "The Crystalline Architecture of Salt",
                            "caption": "Natural halite (rock salt) crystals showcasing cubic cleavage planes arising from repeating 3D giant ionic lattices."
                        }
                    },
                    {
                        "type": "learning_goal",
                        "title": "Lesson Objectives: Ionic Bonding & Giant Lattices",
                        "content": {
                            "title": "What We Will Master Today",
                            "goals": [
                                "Describe **ionic bonding** as the strong electrostatic attraction between oppositely charged ions formed by electron transfer.",
                                "Analyze the 3D **giant ionic lattice structure** of Sodium Chloride ($\\text{NaCl}$).",
                                "Explain why ionic compounds have **exceptionally high melting points** and are **brittle**.",
                                "Investigate and explain **electrical conductivity** in solid vs. molten/aqueous states."
                            ]
                        }
                    },
                    {
                        "type": "concept_explanation",
                        "title": "Opposites Attract: The Genesis of the Ionic Bond",
                        "content": {
                            "title": "When Metals Meet Nonmetals",
                            "text": "When a metal atom (low electronegativity, wants to lose electrons) encounters a nonmetal atom (high electronegativity, wants to gain electrons), a full **electron transfer** occurs.\n\nThe metal forms a positive cation and the nonmetal forms a negative anion. Because opposite charges attract, a powerful electrostatic attraction locks them together in an **ionic bond**."
                        }
                    }
                ],
                # Card 2: The Sodium Chloride Ionic Story
                [
                    {
                        "type": "concept_explanation",
                        "title": "The Formation of Sodium Chloride (NaCl)",
                        "content": {
                            "title": "Submicroscopic Electron Transfer",
                            "text": "1. **Sodium Atom (Na)**: Configuration $1s^2 2s^2 2p^6 3s^1$. Loses its $1$ valence electron $\\rightarrow \\text{Na}^+$ cation ($1s^2 2s^2 2p^6$, stable neon octet).\n2. **Chlorine Atom (Cl)**: Configuration $1s^2 2s^2 2p^6 3s^2 3p^5$. Gains the electron into its $3p$ orbital $\\rightarrow \\text{Cl}^-$ anion ($1s^2 2s^2 2p^6 3s^2 3p^6$, stable argon octet).\n3. **Electrostatic Bond**: The $\\text{Na}^+$ and $\\text{Cl}^-$ ions attract each other with immense electrostatic force: $\\text{Na}^+ + \\text{Cl}^- \\longrightarrow \\text{NaCl}$."
                        }
                    },
                    {
                        "type": "definition_card",
                        "title": "Core Definition: Ionic Bond",
                        "content": {
                            "term": "Ionic Bond",
                            "definition": "The strong non-directional electrostatic force of attraction between oppositely charged ions (cations and anions) formed by the complete transfer of one or more valence electrons from a metal to a nonmetal.",
                            "example": "The bond formed between Mg²⁺ and O²⁻ in magnesium oxide (MgO)."
                        }
                    }
                ],
                # Card 3: Giant Ionic Lattices
                [
                    {
                        "type": "concept_explanation",
                        "title": "The Giant 3D Ionic Crystal Lattice",
                        "content": {
                            "title": "No Isolated NaCl Molecules!",
                            "text": "In a grain of table salt, there are no isolated $\\text{NaCl}$ molecules. Instead, billions of alternating $\\text{Na}^+$ and $\\text{Cl}^-$ ions arrange into a repeating three-dimensional grid called a **giant ionic lattice**.\n\nIn $\\text{NaCl}$, each $\\text{Na}^+$ cation is surrounded symmetrically by $6\\text{ Cl}^-$ anions, and each $\\text{Cl}^-$ anion is surrounded by $6\\text{ Na}^+$ cations ($6:6$ coordination), maximizing electrostatic attraction throughout the entire solid."
                        }
                    },
                    {
                        "type": "suggested_diagram",
                        "title": "3D Giant Ionic Lattice Architecture of Sodium Chloride (NaCl)",
                        "content": {
                            "title": "3D Giant Ionic Lattice Architecture of Sodium Chloride (NaCl)",
                            "caption": "Cubic crystal lattice showing alternating purple Na⁺ cations and green Cl⁻ anions in a repeating 6:6 octahedral coordination grid."
                        }
                    }
                ],
                # Card 4: Explaining Properties & Conductivity Lab
                [
                    {
                        "type": "comparison_table",
                        "title": "Macroscopic Properties of Ionic Compounds Explained Submicroscopically",
                        "content": {
                            "headers": ["Macroscopic Property", "Observation in NaCl", "Submicroscopic Scientific Explanation"],
                            "rows": [
                                ["Melting Point", "High (801 °C)", "Breaking the lattice requires massive thermal energy to overcome strong electrostatic attractions throughout the 3D network."],
                                ["Solid Conductivity", "Non-conductor (0 A)", "Ions are locked in rigid lattice positions; no mobile charged particles exist to carry electric current."],
                                ["Molten/Aqueous Conductivity", "Excellent conductor", "Thermal melting or water hydration breaks the rigid lattice, freeing Na⁺ and Cl⁻ ions to migrate toward electrodes."],
                                ["Brittleness", "Shatters when struck", "A hammer blow shifts lattice layers, aligning like charges (Na⁺ next to Na⁺); sudden electrostatic repulsion shatters the crystal."]
                            ]
                        }
                    },
                    {
                        "type": "step_process",
                        "title": "Practical Investigation: Testing Ionic Conductivity",
                        "content": {
                            "title": "Electrolytic Conductivity Protocol",
                            "steps": [
                                "1. **Test Solid Salt**: Insert graphite electrodes into dry crystalline $\\text{NaCl}$ in a circuit with a 6V battery and bulb. Bulb remains dark (ions immobile).",
                                "2. **Add Distilled Water**: Stir until salt dissolves completely. Bulb glows brightly (ions hydrated and mobile).",
                                "3. **Scientific Conclusion**: Electrical current in ionic solutions is carried by mobile migrating ions ($\\text{Na}^+$ to cathode, $\\text{Cl}^-$ to anode)."
                            ]
                        }
                    }
                ],
                # Card 5: Formative Knowledge Checks
                [
                    {
                        "type": "knowledge_check",
                        "title": "Knowledge Check: Why Ionic Solids Have High Melting Points",
                        "content": {
                            "question": "Why do ionic compounds such as Sodium Chloride (NaCl) possess exceptionally high melting points ($801^\\circ\\text{C}$)?",
                            "options": [
                                "They are composed of heavy metallic atoms.",
                                "The electrostatic forces of attraction holding oppositely charged ions together in the continuous 3D giant lattice are extremely strong and require vast thermal energy to break.",
                                "They contain strong intermolecular covalent bonds.",
                                "They absorb atmospheric heat without expanding."
                            ],
                            "answer": "The electrostatic forces of attraction holding oppositely charged ions together in the continuous 3D giant lattice are extremely strong and require vast thermal energy to break.",
                            "explanation": "Correct! An ionic crystal is not a collection of individual molecules; it is a giant network of millions of electrostatic attractions between positive and negative ions extending in all three dimensions."
                        }
                    },
                    {
                        "type": "knowledge_check",
                        "title": "Knowledge Check: Electrical Conductivity of Potassium Bromide",
                        "content": {
                            "question": "Under which of the following physical states will Potassium Bromide (KBr, an ionic compound) conduct electricity?",
                            "options": [
                                "Only as a dry, crystalline solid at room temperature.",
                                "Only when dissolved in water (aqueous solution) or melted into a molten liquid state.",
                                "Only when cooled below freezing temperatures.",
                                "It will never conduct electricity under any circumstances."
                            ],
                            "answer": "Only when dissolved in water (aqueous solution) or melted into a molten liquid state.",
                            "explanation": "Correct! Electrical conduction requires mobile charge carriers. In solid KBr, ions are immobilized in the rigid lattice. When melted or dissolved in water, the lattice breaks down, freeing $\\text{K}^+$ and $\\text{Br}^-$ ions to move and carry electric current."
                        }
                    }
                ]
            ]
        },

        # =====================================================================
        # LESSON 3: Covalent and Dative Covalent Bonding
        # =====================================================================
        {
            "unit_order": 3,
            "unit_name": "Covalent and Dative Covalent Bonding",
            "unit_description": "Explore electron sharing between nonmetals. Construct single, double, and triple covalent bonds, and understand dative covalent (coordinate) bonding via lone pair donation in NH₄⁺ and H₃O⁺.",
            "lesson_title": "Covalent and Dative Covalent Bonding",
            "pages": [
                # Card 1: Hook & Objectives
                [
                    {
                        "type": "suggested_image",
                        "title": "Electron Sharing: The Covalent Link",
                        "content": {
                            "title": "Electron Sharing: The Covalent Link",
                            "caption": "Molecular orbital overlap showing electron probability density concentrated between mutually attracting atomic nuclei."
                        }
                    },
                    {
                        "type": "learning_goal",
                        "title": "Lesson Objectives: Covalent & Coordinate Bonds",
                        "content": {
                            "title": "What We Will Master Today",
                            "goals": [
                                "Define a **covalent bond** as the mutual electrostatic attraction between positive nuclei and a shared pair of valence electrons.",
                                "Construct dot-and-cross diagrams for **single ($\\text{H}_2$), double ($\\text{O}_2$), and triple ($\\text{N}_2$)** covalent bonds.",
                                "Define **dative covalent (coordinate) bonding** and describe lone pair donation.",
                                "Analyze the formation of the **Ammonium ion ($\\text{NH}_4^+$)** and **Hydronium ion ($\\text{H}_3\\text{O}^+$)**."
                            ]
                        }
                    },
                    {
                        "type": "concept_explanation",
                        "title": "Cooperation Over Transfer: The Covalent Principle",
                        "content": {
                            "title": "When Neither Atom Gives Up Electrons",
                            "text": "When two nonmetal atoms collide, neither wants to lose electrons because both have high ionization energies and nearly full outer shells.\n\nTo attain noble gas stability, they compromise: they **share valence electron pairs**! The shared electrons spend time between both positive nuclei, electrostatically holding the atoms together in a **covalent bond**."
                        }
                    }
                ],
                # Card 2: Single, Double, and Triple Bonds
                [
                    {
                        "type": "concept_explanation",
                        "title": "Multiplicity of Covalent Bonds",
                        "content": {
                            "title": "Single, Double, and Triple Bonds",
                            "text": "Depending on how many electrons each nonmetal atom needs to complete its valence shell:\n\n1. **Single Covalent Bond (1 shared pair, 2 electrons)**: Represented as $\\text{H}-\\text{H}$ or $\\text{Cl}-\\text{Cl}$. Each atom contributes 1 electron.\n2. **Double Covalent Bond (2 shared pairs, 4 electrons)**: Represented as $\\text{O}=\\text{O}$ in Oxygen gas. Each atom contributes 2 electrons.\n3. **Triple Covalent Bond (3 shared pairs, 6 electrons)**: Represented as $\\text{N}\\equiv\\text{N}$ in Nitrogen gas. Extremely strong and short, making $\\text{N}_2$ highly unreactive in our atmosphere!"
                        }
                    },
                    {
                        "type": "suggested_diagram",
                        "title": "Dot-and-Cross Overlap Diagrams: Single, Double, and Triple Covalent Bonds",
                        "content": {
                            "title": "Dot-and-Cross Overlap Diagrams: Single, Double, and Triple Covalent Bonds",
                            "caption": "Orbital overlap diagrams illustrating shared electron pairs in Hydrogen (H₂), Oxygen (O₂), and Nitrogen (N₂)."
                        }
                    }
                ],
                # Card 3: Dative Covalent (Coordinate) Bonding
                [
                    {
                        "type": "concept_explanation",
                        "title": "Dative Covalent (Coordinate) Bonding",
                        "content": {
                            "title": "One-Sided Electron Pair Donation",
                            "text": "In a standard covalent bond, each atom contributes 1 electron to the shared pair. In a **dative covalent bond**, **both electrons** in the shared pair are contributed by only ONE of the bonded atoms (the donor atom):\n\n- The donor atom must possess an unbonded **lone pair of electrons**.\n- The acceptor species is typically an electron-deficient ion (like a bare proton $\\text{H}^+$ with 0 electrons).\n- Once formed, a coordinate bond has the exact same strength and properties as a regular covalent bond! We indicate it symbolically with an arrow ($\\longrightarrow$) pointing from donor to acceptor."
                        }
                    },
                    {
                        "type": "definition_card",
                        "title": "Core Definition: Dative Covalent Bond",
                        "content": {
                            "term": "Dative Covalent (Coordinate) Bond",
                            "definition": "A covalent bond in which both electrons in the shared pair originate from the lone pair of a single donor atom, rather than each atom contributing one electron.",
                            "example": "The formation of the ammonium ion (NH₄⁺) when ammonia (NH₃) donates its lone pair to a hydrogen ion (H⁺)."
                        }
                    }
                ],
                # Card 4: Case Studies: Ammonium (NH₄⁺) and Hydronium (H₃O⁺)
                [
                    {
                        "type": "worked_example",
                        "title": "Worked Formation: Ammonium & Hydronium Ions",
                        "content": {
                            "title": "Lone Pair Donation Mechanics",
                            "text": "### 1. Ammonium Ion ($\\text{NH}_4^+$)\n- Ammonia ($\\text{NH}_3$) has 3 standard $\\text{N}-\\text{H}$ covalent bonds and **one lone pair** on Nitrogen ($:N\\text{H}_3$).\n- A Hydrogen ion ($\\text{H}^+$, 0 electrons) approaches.\n- Nitrogen donates its entire lone pair into the empty $1s$ orbital of $\\text{H}^+$:\n  $$\\text{H}_3\\text{N}: + \\text{H}^+ \\longrightarrow [\\text{H}_3\\text{N} \\rightarrow \\text{H}]^+ \\quad (\\text{or } \\text{NH}_4^+)$$\n\n### 2. Hydronium Ion ($\\text{H}_3\\text{O}^+$)\n- Water ($\\text{H}_2\\text{O}$) has two lone pairs on Oxygen ($:\\ddot{\\text{O}}\\text{H}_2$).\n- Oxygen shares one lone pair with an $\\text{H}^+$ ion, forming $\\text{H}_3\\text{O}^+$."
                        }
                    },
                    {
                        "type": "callout",
                        "title": "Identical Behavior After Formation",
                        "content": {
                            "title": "No 'Memory' in Bonds",
                            "text": "In the $\\text{NH}_4^+$ ion, all four $\\text{N}-\\text{H}$ bonds are completely identical in length, energy, and behavior. Spectroscopic instruments cannot distinguish which of the four bonds was originally formed datively!"
                        }
                    }
                ],
                # Card 5: Formative Knowledge Checks
                [
                    {
                        "type": "knowledge_check",
                        "title": "Knowledge Check: Ionic vs Covalent Fundamental Difference",
                        "content": {
                            "question": "What is the primary fundamental difference between an ionic bond and a covalent bond?",
                            "options": [
                                "Ionic bonds involve sharing electrons, while covalent bonds involve transferring them.",
                                "Ionic bonds occur only between nonmetal gases.",
                                "Ionic bonds involve complete electron transfer from a metal to a nonmetal creating attracting ions, while covalent bonds involve the sharing of electron pairs between nonmetal atoms.",
                                "Covalent bonds only exist at extremely high temperatures."
                            ],
                            "answer": "Ionic bonds involve complete electron transfer from a metal to a nonmetal creating attracting ions, while covalent bonds involve the sharing of electron pairs between nonmetal atoms.",
                            "explanation": "Correct! Ionic bonding is electrostatic attraction following electron transfer between metals and nonmetals. Covalent bonding is orbital sharing of electron pairs between nonmetals."
                        }
                    },
                    {
                        "type": "knowledge_check",
                        "title": "Knowledge Check: Atmospheric Stability of Nitrogen Gas",
                        "content": {
                            "question": "Why is Nitrogen gas ($\\text{N}_2$) so chemically inert and stable in Earth's atmosphere (making up 78% of air)?",
                            "options": [
                                "It is a noble gas with a full atomic octet.",
                                "Its atoms are held together by an exceptionally strong triple covalent bond (sharing 3 electron pairs), requiring immense energy to break.",
                                "It conducts electricity away before reactions can occur.",
                                "It contains temporary dative covalent bonds."
                            ],
                            "answer": "Its atoms are held together by an exceptionally strong triple covalent bond (sharing 3 electron pairs), requiring immense energy to break.",
                            "explanation": "Correct! The two nitrogen atoms in an $\\text{N}_2$ molecule share 3 pairs of electrons in a triple covalent bond ($\\text{N}\\equiv\\text{N}$), possessing an extremely high bond dissociation energy ($945\\text{ kJ/mol}$)."
                        }
                    }
                ]
            ]
        },

        # =====================================================================
        # LESSON 4: Intermolecular Forces and Metallic Bonding
        # =====================================================================
        {
            "unit_order": 4,
            "unit_name": "Intermolecular Forces and Metallic Bonding",
            "unit_description": "Distinguish intramolecular bonds from intermolecular forces (Van der Waals and Hydrogen bonding). Explore metallic bonding: positive cations in a delocalized 'sea of electrons'.",
            "lesson_title": "Intermolecular Forces and Metallic Bonding",
            "pages": [
                # Card 1: Hook & Objectives
                [
                    {
                        "type": "suggested_image",
                        "title": "Intermolecular Forces & Metallic Structures",
                        "content": {
                            "title": "Intermolecular Forces & Metallic Structures",
                            "caption": "Polished metallic copper wire alongside water surface tension droplets illustrating intermolecular and metallic forces."
                        }
                    },
                    {
                        "type": "learning_goal",
                        "title": "Lesson Objectives: Intermolecular & Metallic Forces",
                        "content": {
                            "title": "What We Will Master Today",
                            "goals": [
                                "Distinguish **intramolecular bonds** (within molecules) from **intermolecular forces** (between molecules).",
                                "Compare weak **Van der Waals forces** with stronger **Hydrogen bonds** in water.",
                                "Describe **metallic bonding** as a lattice of positive metal cations immersed in a delocalized 'sea of electrons'.",
                                "Explain metallic properties: **high electrical conductivity, malleability, and ductility**."
                            ]
                        }
                    },
                    {
                        "type": "concept_explanation",
                        "title": "Forces Within vs. Forces Between",
                        "content": {
                            "title": "Why Does Water Flow While Iron is Solid?",
                            "text": "To understand why substances exist as gases, liquids, or solids at room temperature, we must distinguish the strong bonds inside a molecule from the subtle forces acting between different molecules."
                        }
                    }
                ],
                # Card 2: Intramolecular vs. Intermolecular Forces
                [
                    {
                        "type": "concept_explanation",
                        "title": "Intramolecular Bonds vs. Intermolecular Forces",
                        "content": {
                            "title": "What Breaks When Water Boils?",
                            "text": "- **Intramolecular Bonds**: Strong covalent bonds **inside** a molecule holding atoms together (e.g., the $\\text{O}-\\text{H}$ covalent bonds inside an $\\text{H}_2\\text{O}$ molecule).\n- **Intermolecular Forces**: Weaker attractive forces **between** neighboring molecules (e.g., hydrogen bonds between water molecules).\n\nWhen water boils ($100^\\circ\\text{C}$), the steam is still $\\text{H}_2\\text{O}$! Covalent bonds inside the molecules are NOT broken; only weak intermolecular forces are overcome!"
                        }
                    },
                    {
                        "type": "suggested_diagram",
                        "title": "Intramolecular Covalent Bonds vs. Intermolecular Hydrogen Bonds in Water",
                        "content": {
                            "title": "Intramolecular Covalent Bonds vs. Intermolecular Hydrogen Bonds in Water",
                            "caption": "Diagram showing solid covalent O-H bonds inside water molecules and dashed intermolecular hydrogen bonds between neighboring molecules."
                        }
                    }
                ],
                # Card 3: Metallic Bonding: The Electron Sea Model
                [
                    {
                        "type": "concept_explanation",
                        "title": "Metallic Bonding: The 'Sea of Delocalized Electrons'",
                        "content": {
                            "title": "How Metal Atoms Stick Together",
                            "text": "In a solid metal (like Copper or Iron), metal atoms pack closely into a regular crystalline lattice. Because metals have low ionization energies, they release their valence electrons:\n\n- The valence electrons become **delocalized**—free to roam across the entire metallic structure like a fluid 'sea'.\n- The remaining positive metal cores (cations) are held firmly in place by electrostatic attraction to this surrounding **sea of mobile electrons**."
                        }
                    },
                    {
                        "type": "definition_card",
                        "title": "Core Definition: Metallic Bond",
                        "content": {
                            "term": "Metallic Bond",
                            "definition": "The strong electrostatic attraction between fixed positive metal ions (cations) arranged in a regular lattice and the surrounding mobile pool of delocalized valence electrons.",
                            "example": "The metallic bond in copper wire consisting of Cu²⁺ ions in a sea of delocalized electrons."
                        }
                    }
                ],
                # Card 4: Explaining Metallic Properties
                [
                    {
                        "type": "comparison_table",
                        "title": "Submicroscopic Origin of Metallic Properties",
                        "content": {
                            "headers": ["Metallic Property", "Macroscopic Behavior", "Submicroscopic Explanation"],
                            "rows": [
                                ["Electrical Conductivity", "High in solid and liquid", "Mobile delocalized electrons flow freely through the metal when a potential difference (voltage) is applied."],
                                ["Thermal Conductivity", "Rapid heat transfer", "Delocalized electrons gain kinetic energy and rapidly transmit thermal vibrations across the lattice."],
                                ["Malleability & Ductility", "Can be hammered into sheets or drawn into wires", "When struck, positive metal layers slide past each other without breaking, because the flexible electron sea flows around them maintaining the bond."],
                                ["Metallic Lustre", "Shiny reflective surface", "Free surface electrons absorb and re-emit incident light photons across all visible wavelengths."]
                            ]
                        }
                    },
                    {
                        "type": "callout",
                        "title": "Why Glass Shatters but Copper Bends",
                        "content": {
                            "title": "Brittleness vs Malleability",
                            "text": "When brittle glass or ionic crystals are struck, displacement forces like-charges together, triggering violent repulsion and shattering. In metals, the fluid sea of electrons cushions shifting cations, keeping the bond intact."
                        }
                    }
                ],
                # Card 5: Formative Knowledge Checks
                [
                    {
                        "type": "knowledge_check",
                        "title": "Knowledge Check: Forces Overcome During Boiling",
                        "content": {
                            "question": "When liquid water boils at $100^\\circ\\text{C}$ to form steam, which of the following forces are being overcome (broken)?",
                            "options": [
                                "The strong covalent bonds holding hydrogen and oxygen atoms together inside each water molecule.",
                                "The weaker intermolecular hydrogen bonds holding neighboring water molecules close to one another.",
                                "Nuclear forces inside the oxygen nuclei.",
                                "Ionic electrostatic attractions."
                            ],
                            "answer": "The weaker intermolecular hydrogen bonds holding neighboring water molecules close to one another.",
                            "explanation": "Correct! Boiling is a physical change of state. The $\\text{H}_2\\text{O}$ molecules remain chemically intact; thermal energy only overcomes the intermolecular hydrogen bonds between molecules."
                        }
                    },
                    {
                        "type": "knowledge_check",
                        "title": "Knowledge Check: Submicroscopic Model of Copper Wire",
                        "content": {
                            "question": "Which of the following descriptions best models the submicroscopic structure of a piece of copper wire?",
                            "options": [
                                "A giant lattice of alternating positive and negative ions.",
                                "Isolated neutral copper molecules held by weak Van der Waals forces.",
                                "A regular lattice of positive copper cations surrounded by and electrostatically attracted to a mobile 'sea' of delocalized valence electrons.",
                                "A continuous chain of copper atoms held by dative covalent bonds."
                            ],
                            "answer": "A regular lattice of positive copper cations surrounded by and electrostatically attracted to a mobile 'sea' of delocalized valence electrons.",
                            "explanation": "Correct! Metallic bonding is defined as a regular lattice of positive metal cores held together by electrostatic attraction to a shared, mobile sea of delocalized valence electrons."
                        }
                    }
                ]
            ]
        },

        # =====================================================================
        # LESSON 5: Giant Atomic/Covalent and Giant Metallic Structures
        # =====================================================================
        {
            "unit_order": 5,
            "unit_name": "Giant Atomic/Covalent and Giant Metallic Structures",
            "unit_description": "Compare giant covalent networks (Diamond, Graphite, Quartz) with giant metallic structures. Analyze why Diamond is the hardest insulator while Graphite is a soft electrical conductor.",
            "lesson_title": "Giant Atomic/Covalent and Giant Metallic Structures",
            "pages": [
                # Card 1: Hook & Objectives
                [
                    {
                        "type": "suggested_image",
                        "title": "Allotropes of Carbon: Diamond & Graphite",
                        "content": {
                            "title": "Allotropes of Carbon: Diamond & Graphite",
                            "caption": "Natural uncut diamond crystal alongside pure graphite mineral showcasing contrasting physical properties from identical carbon atoms."
                        }
                    },
                    {
                        "type": "learning_goal",
                        "title": "Lesson Objectives: Giant Covalent Allotropes",
                        "content": {
                            "title": "What We Will Master Today",
                            "goals": [
                                "Define **allotropes** as different structural forms of the same element in the same physical state.",
                                "Analyze the 3D tetrahedral giant covalent structure of **Diamond** and explain its extreme hardness and non-conductivity.",
                                "Analyze the layered hexagonal structure of **Graphite** and explain its softness and electrical conductivity.",
                                "Compare giant covalent structures with **Silicon Dioxide (Quartz)** and giant metallic lattices."
                            ]
                        }
                    },
                    {
                        "type": "concept_explanation",
                        "title": "Simple Molecular vs. Giant Networks",
                        "content": {
                            "title": "Cabins vs. Massive Stone Fortresses",
                            "text": "Some covalent substances form small, isolated units (called **simple molecular structures**, like $\\text{H}_2\\text{O}$ or $\\text{CO}_2$).\n\nOther covalent substances form vast, continuous three-dimensional networks of interlocking covalent bonds stretching across millions of atoms. These are called **giant covalent (or giant atomic) structures**."
                        }
                    }
                ],
                # Card 2: Diamond: The 3D Tetrahedral Fortress
                [
                    {
                        "type": "concept_explanation",
                        "title": "Diamond: 3D Tetrahedral Giant Network",
                        "content": {
                            "title": "The Hardest Natural Substance",
                            "text": "- **Structure**: Each Carbon atom is covalently bonded to **4 other Carbon atoms** in a rigid 3D tetrahedral network ($sp^3$ hybridization).\n- **Extreme Hardness & High Melting Point ($3550^\\circ\\text{C}$)**: The entire crystal is one continuous network of strong covalent bonds with no weak planes. Melting requires breaking millions of covalent bonds simultaneously.\n- **Complete Electrical Insulator**: All 4 valence electrons of every carbon atom are locked in localized covalent bonds. With zero mobile electrons, diamond cannot conduct electricity!"
                        }
                    },
                    {
                        "type": "definition_card",
                        "title": "Core Definition: Allotropy",
                        "content": {
                            "term": "Allotropes",
                            "definition": "Different physical structural forms of the same chemical element in the same physical state, possessing distinct chemical bonding arrangements and different physical properties.",
                            "example": "Diamond and Graphite are allotropes of pure elemental carbon."
                        }
                    }
                ],
                # Card 3: Graphite: The Sliding Conductive Sheets
                [
                    {
                        "type": "concept_explanation",
                        "title": "Graphite: Hexagonal Layers & Delocalized Electrons",
                        "content": {
                            "title": "Softness and Conductivity in Carbon",
                            "text": "- **Structure**: Each Carbon atom is covalently bonded to only **3 other Carbon atoms** in flat 2D hexagonal sheets ($sp^2$ hybridization).\n- **Softness & Lubricating Power**: The bonds within each sheet are strong covalent bonds, but the forces **between** adjacent sheets are weak **Van der Waals forces**. The layers easily slide over one another when pushed (used in pencil lead and industrial dry lubricants).\n- **Electrical Conductivity**: Because each carbon atom only uses 3 valence electrons for bonding, the 4th electron becomes **delocalized** and free to migrate across the sheets, conducting electric current like a metal!"
                        }
                    },
                    {
                        "type": "suggested_diagram",
                        "title": "Structural Comparison: Diamond (3D Tetrahedral) vs. Graphite (Layered Hexagons)",
                        "content": {
                            "title": "Structural Comparison: Diamond (3D Tetrahedral) vs. Graphite (Layered Hexagons)",
                            "caption": "Side-by-side 3D models illustrating diamond's rigid 4-bond tetrahedral framework vs. graphite's layered sheets with delocalized electrons."
                        }
                    }
                ],
                # Card 4: Giant Covalent Quartz & Giant Metallic Structures
                [
                    {
                        "type": "comparison_table",
                        "title": "Comparison of Giant Structures (Covalent vs. Metallic)",
                        "content": {
                            "headers": ["Structure", "Type of Bonding", "Structural Architecture", "Melting Point", "Electrical Conductivity", "Common Application"],
                            "rows": [
                                ["Diamond (C)", "Covalent", "3D tetrahedral network (4 bonds/C)", "Extreme (>3500 °C)", "Insulator (0 free e⁻)", "Cutting tools, drill bits, jewelry"],
                                ["Graphite (C)", "Covalent & Van der Waals", "Layered hexagonal sheets (3 bonds/C)", "High (>3600 °C)", "Conductor (1 delocalized e⁻/C)", "Pencil leads, dry lubricant, electrodes"],
                                ["Quartz (SiO₂)", "Covalent", "3D tetrahedral network (each Si bonded to 4 O)", "High (~1600 °C)", "Insulator", "Glass manufacturing, optical lenses"],
                                ["Aluminium (Al)", "Metallic", "3D lattice of Al³⁺ in sea of 3e⁻/atom", "Moderate (660 °C)", "Excellent conductor", "Aircraft fuselage, high-voltage power lines"]
                            ]
                        }
                    },
                    {
                        "type": "callout",
                        "title": "Silicon Dioxide (Quartz) Structure",
                        "content": {
                            "title": "A Giant Covalent Mineral",
                            "text": "Quartz is not a simple molecular gas like $\\text{CO}_2$. It is a giant covalent crystal where each silicon atom is bonded to 4 oxygen atoms and each oxygen is bonded to 2 silicon atoms, explaining its extreme hardness and insolubility in water."
                        }
                    }
                ],
                # Card 5: Formative Knowledge Checks
                [
                    {
                        "type": "knowledge_check",
                        "title": "Knowledge Check: Why Graphite Conducts Electricity",
                        "content": {
                            "question": "Why is graphite an excellent conductor of electricity while diamond, also made of pure carbon, is a complete insulator?",
                            "options": [
                                "Graphite is a metal, whereas diamond is an organic compound.",
                                "In graphite, each carbon atom bonds to only 3 neighbors, releasing 1 delocalized electron that flows along layers; in diamond, all 4 valence electrons are locked in bonds.",
                                "Graphite has a lower density which releases protons into the circuit.",
                                "Diamond is too transparent for electrons to travel through."
                            ],
                            "answer": "In graphite, each carbon atom bonds to only 3 neighbors, releasing 1 delocalized electron that flows along layers; in diamond, all 4 valence electrons are locked in bonds.",
                            "explanation": "Correct! Carbon has 4 valence electrons. Diamond uses all 4 in bonding (no free electrons $\\rightarrow$ insulator). Graphite uses only 3 in bonding, leaving 1 electron per atom delocalized and free to move along the hexagonal layers $\\rightarrow$ conductor."
                        }
                    },
                    {
                        "type": "knowledge_check",
                        "title": "Knowledge Check: Why Graphite Acts as a Dry Lubricant",
                        "content": {
                            "question": "Which structural feature allows graphite to be used as a dry lubricant in high-temperature machinery?",
                            "options": [
                                "Its rigid 3D tetrahedral framework.",
                                "Its hexagonal sheets are held together only by weak Van der Waals forces, allowing them to slide smoothly over each other.",
                                "Its high concentration of water molecules.",
                                "Its lack of carbon-carbon bonds."
                            ],
                            "answer": "Its hexagonal sheets are held together only by weak Van der Waals forces, allowing them to slide smoothly over each other.",
                            "explanation": "Correct! Graphite consists of 2D hexagonal sheets held together by weak intermolecular Van der Waals forces. When mechanical shear force is applied, these layers readily slide past one another, reducing friction."
                        }
                    }
                ]
            ]
        },

        # =====================================================================
        # LESSON 6: Bonding, Properties, Uses, and Model Project
        # =====================================================================
        {
            "unit_order": 6,
            "unit_name": "Bonding, Properties, Uses, and Model Project",
            "unit_description": "Synthesize the structure-property-use connection across giant ionic, simple molecular, giant covalent, and giant metallic systems. Build 3D physical models and critique model limitations.",
            "lesson_title": "Bonding, Properties, Uses, and Model Project",
            "pages": [
                # Card 1: Hook & Objectives
                [
                    {
                        "type": "suggested_image",
                        "title": "Connecting Structure to Engineering Applications",
                        "content": {
                            "title": "Connecting Structure to Engineering Applications",
                            "caption": "Engineering materials selected for aerospace, construction, and electronics based on submicroscopic bonding architecture."
                        }
                    },
                    {
                        "type": "learning_goal",
                        "title": "Lesson Objectives: Structure, Properties, and Modeling",
                        "content": {
                            "title": "What We Will Master Today",
                            "goals": [
                                "Synthesize the **Structure-Property-Use Connection** across the 4 major bonding types.",
                                "Construct physical **3D models** of Diamond, Graphite, and Sodium Chloride using local materials.",
                                "Critique the **limitations of physical scientific models**.",
                                "Achieve mastery across the complete Grade 10 CBC Topic 1.4 syllabus."
                            ]
                        }
                    },
                    {
                        "type": "concept_explanation",
                        "title": "The Grand Synthesis of Chemical Bonding",
                        "content": {
                            "title": "Predicting the Real World from the Subatomic",
                            "text": "As a chemist, when you know how atoms in a material are bonded, you can predict its melting point, electrical conductivity, mechanical strength, and ideal industrial application with precision!"
                        }
                    }
                ],
                # Card 2: Master Structure-Property-Use Matrix
                [
                    {
                        "type": "comparison_table",
                        "title": "Master Chemical Bonding & Material Architecture Matrix",
                        "content": {
                            "headers": ["Substance", "Bonding Type", "Structure Type", "Key Physical Properties", "Industrial / Practical Application", "Submicroscopic Rationale"],
                            "rows": [
                                ["Sodium Chloride (NaCl)", "Ionic", "Giant Ionic Lattice", "Brittle, high MP (801 °C), conducts when molten/aqueous", "Food seasoning, chlorine manufacturing", "Strong electrostatic attractions; water dissolves lattice freeing ions."],
                                ["Water (H₂O)", "Covalent & Hydrogen bonding", "Simple Molecular", "Liquid at room temp, MP 0 °C, BP 100 °C, insulator", "Universal solvent, life processes", "Strong intramolecular O-H bonds, but weak intermolecular hydrogen bonds."],
                                ["Diamond (C)", "Covalent", "Giant Covalent", "Extreme hardness, insulator, MP >3500 °C", "Drill bits, glass cutters, jewelry", "Continuous 3D tetrahedral network of 4 covalent bonds per carbon with no free electrons."],
                                ["Graphite (C)", "Covalent & Van der Waals", "Giant Covalent (Layered)", "Soft, slippery layers, excellent conductor", "Pencil lead, machinery lubricant, battery electrodes", "Hexagonal sheets slide due to weak Van der Waals forces; 1 delocalized e⁻/C conducts."],
                                ["Aluminium (Al)", "Metallic", "Giant Metallic", "Lightweight (low density), malleable, high conductivity", "Aircraft frames, power transmission lines", "Lattice of Al³⁺ cations held by dense sea of 3 delocalized electrons per atom."]
                            ]
                        }
                    },
                    {
                        "type": "suggested_diagram",
                        "title": "Master Synthesis: The 4 Major Material Architectures",
                        "content": {
                            "title": "Master Synthesis: The 4 Major Material Architectures",
                            "caption": "Comparative visual overview of Giant Ionic, Simple Molecular, Giant Covalent, and Giant Metallic structures."
                        }
                    }
                ],
                # Card 3: Collaborative Inquiry Project: Building 3D Models
                [
                    {
                        "type": "step_process",
                        "title": "Collaborative Inquiry Project: Building 3D Structural Models",
                        "content": {
                            "title": "Hands-On Modeling Protocol",
                            "steps": [
                                "1. **Form Groups**: Form teams of 3–4 students to build physical 3D representations using local materials (clay balls, seeds, toothpicks, flexible wire).",
                                "2. **Construct Diamond**: Connect each clay sphere tetrahedrally to 4 others. Observe the rigid, unbending 3D network.",
                                "3. **Construct Graphite**: Connect clay spheres in flat hexagonal rings (3 bonds each). Stack layers using toothpicks/wires. Observe how layers slide over one another.",
                                "4. **Construct Sodium Chloride**: Use two contrasting clay colors (red for $\\text{Na}^+$, green for $\\text{Cl}^-$) and assemble into an alternating cubic grid.",
                                "5. **Critique Model Limitations**: Present models and analyze limitations (e.g., bonds are attractive force fields, not physical wooden sticks; atoms are mostly empty space, not solid clay balls!)."
                            ]
                        }
                    },
                    {
                        "type": "common_misconception",
                        "title": "Scientific Thinking: Model Limitations",
                        "content": {
                            "misconception": "Classroom ball-and-stick models show the literal physical reality of atoms.",
                            "correction": "Models are helpful conceptual tools! In reality, atoms are 99.999% empty space, electrons are quantum clouds, and chemical bonds are invisible electrostatic forces.",
                            "why_it_matters": "Evaluating model constraints is an essential CBC scientific inquiry skill."
                        }
                    }
                ],
                # Card 4: Topic 1.4 Master Summary & Key Takeaways
                [
                    {
                        "type": "summary",
                        "title": "Topic 1.4 Master Summary & Key Takeaways",
                        "content": {
                            "title": "Key Bonding Principles Mastered",
                            "summary_points": [
                                "**Valence Electrons**: Only outermost valence electrons participate in bonding to achieve duplet/octet stability.",
                                "**Ionic Bonding**: Complete electron transfer from metals to nonmetals, creating giant lattices held by electrostatic attraction (high MP, conducts when molten/aqueous).",
                                "**Covalent Bonding**: Electron pair sharing between nonmetals (single, double, triple); simple molecules have low boiling points due to weak intermolecular forces.",
                                "**Coordinate (Dative) Bonding**: Both electrons in a shared pair provided by a single donor atom's lone pair (e.g., $\\text{NH}_4^+$, $\\text{H}_3\\text{O}^+$).",
                                "**Metallic Bonding**: Positive cations packed in a mobile 'sea of delocalized electrons' (malleable, ductile, high electrical conductivity).",
                                "**Giant Covalent Allotropes**: Diamond (hard 3D tetrahedral insulator) vs. Graphite (soft layered conductor with delocalized electrons)."
                            ]
                        }
                    },
                    {
                        "type": "transition",
                        "title": "Looking Ahead: Grade 10 Chemistry Topics 5 & 6",
                        "content": {
                            "title": "Next Step: Acids, Bases, and Salts",
                            "text": "With chemical bonding and structure mastered, you are prepared for subsequent units on **Acids, Bases, and Indicators** and **The Mole Concept and Stoichiometry**!"
                        }
                    }
                ],
                # Card 5: End-of-Topic Mastery Challenges
                [
                    {
                        "type": "knowledge_check",
                        "title": "Mastery Challenge: Material Selection for Aerospace",
                        "content": {
                            "question": "Why is Aluminium metal preferred over Iron for constructing aircraft fuselages and high-voltage power transmission cables?",
                            "options": [
                                "Aluminium contains ionic bonds making it completely transparent.",
                                "Aluminium possesses a much lower density (lightweight) while maintaining high mechanical strength and excellent electrical conductivity from its metallic electron sea.",
                                "Aluminium does not contain any electrons.",
                                "Aluminium is a giant covalent crystal."
                            ],
                            "answer": "Aluminium possesses a much lower density (lightweight) while maintaining high mechanical strength and excellent electrical conductivity from its metallic electron sea.",
                            "explanation": "Correct! Aluminium combines low density with high tensile strength and high electrical conductivity due to its metallic structure ($3$ delocalized electrons per atom), making it ideal for aerospace and power transmission."
                        }
                    },
                    {
                        "type": "knowledge_check",
                        "title": "Mastery Challenge: Identifying Unlabeled Samples A, B, and C",
                        "content": {
                            "question": "You are given three mystery solids: Sample A is shiny, malleable, and conducts as a solid. Sample B is a white crystal that dissolves in water and conducts electricity only when dissolved. Sample C is an exceptionally hard crystal that does not conduct in any state and has a melting point above $3000^\\circ\\text{C}$. What are their structural types?",
                            "options": [
                                "A = Giant Ionic, B = Giant Metallic, C = Simple Molecular",
                                "A = Giant Metallic, B = Giant Ionic, C = Giant Covalent/Atomic",
                                "A = Simple Molecular, B = Giant Covalent, C = Giant Metallic",
                                "A = Giant Covalent, B = Simple Molecular, C = Giant Ionic"
                            ],
                            "answer": "A = Giant Metallic, B = Giant Ionic, C = Giant Covalent/Atomic",
                            "explanation": "Correct! Sample A (malleable, solid conductor) is Giant Metallic. Sample B (soluble, conducts only in solution) is Giant Ionic. Sample C (extreme hardness, high MP, complete insulator) is Giant Covalent."
                        }
                    }
                ]
            ]
        }
    ]

@transaction.atomic
def ingest_topic4():
    print("=" * 80)
    print("INGESTING GRADE 10 CHEMISTRY — TOPIC 4: CHEMICAL BONDING")
    print("=" * 80)

    # 1. Resolve Hierarchy
    cbc = Curriculum.objects.filter(name__icontains="CBC").first()
    grade10 = Grade.objects.filter(curriculum=cbc, level=10).first()
    chem = Subject.objects.filter(grade=grade10, id=5).first() or Subject.objects.filter(grade=grade10, name__icontains="Chem").first()

    print(f"Target Subject: [{chem.id}] {chem.name} (Grade: {grade10.name}, Curr: {cbc.name})")

    # 2. Resolve or Create Topic 4
    topic, created = Topic.objects.get_or_create(
        subject=chem,
        order=4,
        defaults={
            "name": "Chemical Bonding",
            "description": "Analyze chemical bonding types (ionic, covalent, dative covalent, metallic), differentiate giant and simple molecular structures, and relate atomic bonding to macroscopic physical properties and applications."
        }
    )
    if not created:
        topic.name = "Chemical Bonding"
        topic.description = "Analyze chemical bonding types (ionic, covalent, dative covalent, metallic), differentiate giant and simple molecular structures, and relate atomic bonding to macroscopic physical properties and applications."
        topic.save()
    print(f"Resolved Topic 4: [{topic.id}] {topic.name}")

    # 3. Ingest Lessons & Blocks
    curriculum_data = build_topic4_curriculum()

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

    print("\nSUCCESS: Topic 4 Ingestion Completed Idempotently!")

if __name__ == "__main__":
    ingest_topic4()
