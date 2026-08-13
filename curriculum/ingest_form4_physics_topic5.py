"""
VLearn Form 4 Physics — Topic 5: Electromagnetic Induction
Ingestion Script

Source: Lessons.md (Topic 5)
Grade: Form 4
Subject: Physics
Curriculum: 844 (Kenyan 8-4-4 Secondary Curriculum)

Pedagogical Architecture:
  3 Learning Units / Modules:
  - Module 5.1: Induced E.M.F., Faraday's Law, and Lenz's Law (13 pages)
  - Module 5.2: Generators, Alternating Current, and Sound Transducers (14 pages)
  - Module 5.3: Mutual Induction, Transformers, and Grid Systems (13 pages)

Features:
  - Adaptive 8-step analytical problem-solving framework
  - Multi-tier worked examples (Levels 1 to 5)
  - Full laboratory experimental protocols (Mutual induction & transformer efficiency)
  - Real-world engineering systems (A.C./D.C. generators, microphones, transformers, national grid)
  - Purposeful interactions (prediction, simulation sandbox, reflections, knowledge checks)
  - Clean student-facing titles and zero developer terminology leaks
  - Idempotent safe updates (preserves enriched assets on rerun)

Usage:
  /home/jason-bitega/Desktop/VL/vlearn_repositories/Vlearn_backend/venv/bin/python curriculum/ingest_form4_physics_topic5.py
  Optional flag: --replace
"""

import os
import sys
import uuid
import re
import argparse
import django

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "Nexus_backend.settings")
django.setup()

from django.db import transaction
from curriculum.models import (
    Curriculum, Grade, Subject, Topic,
    LearningUnit, Lesson, LessonBlock, LessonAsset
)

def clean_text(raw_str):
    """Remove source citation brackets like [89], [90], [image_0] and clean whitespace."""
    if not isinstance(raw_str, str):
        return raw_str
    cleaned = re.sub(r'\[(?:\d+|image_\d+|[\d,\s]+)\]', '', raw_str)
    cleaned = re.sub(r'[ \t]+', ' ', cleaned)
    return cleaned.strip()

def clean_content_dict(data):
    """Recursively clean text within content dicts or lists."""
    if isinstance(data, str):
        return clean_text(data)
    elif isinstance(data, list):
        return [clean_content_dict(item) for item in data]
    elif isinstance(data, dict):
        return {k: clean_content_dict(v) for k, v in data.items()}
    return data


# =============================================================================
# MODULE 5.1 DATA — Induced E.M.F., Faraday's Law & Lenz's Law
# =============================================================================
MODULE_5_1 = {
    "unit_name": "Module 5.1: Induced E.M.F., Faraday's Law, and Lenz's Law",
    "unit_order": 1,
    "lesson_title": "Induced E.M.F., Faraday's Law, and Lenz's Law",
    "cards": [
        # Page 1: Hook & Goals
        {
            "page_number": 1,
            "page_title": "Power Without Batteries: The Physics of Induction",
            "block_type": "learning_goal",
            "component_type": "learning_goal",
            "content": {
                "text": (
                    "Have you ever ridden a bicycle equipped with a bottle dynamo touching the tire? "
                    "As you pedal faster, the headlight shines brighter. When you stop pedaling, the light instantly goes out. "
                    "There is no battery inside the dynamo! Where does the electrical energy come from?\n\n"
                    "Similarly, when you use a tap-to-pay credit card or a wireless phone charger, electrical energy transfers across "
                    "an open air gap without any physical wires touching!\n\n"
                    "In both cases, we are witnessing **electromagnetic induction**: the process of generating an electromotive force (e.m.f.) "
                    "and electric current purely through relative motion or changing magnetic fields.\n\n"
                    "By the end of this lesson, you will be able to:\n"
                    "- Explain the physical origin of induced e.m.f. via magnetic flux cutting\n"
                    "- State and apply Faraday's Law of Magnetic Induction ($\\varepsilon \\propto \\frac{\\Delta \\Phi}{\\Delta t}$)\n"
                    "- State Lenz's Law and prove its alignment with the Law of Conservation of Energy\n"
                    "- Use Fleming's Right-Hand Rule to map magnetic field, motion, and induced current vectors in 3D"
                )
            }
        },
        # Page 2: Origin of Induced E.M.F.
        {
            "page_number": 2,
            "page_title": "The Origin of Induced Electromotive Force (E.M.F.)",
            "block_type": "concept_explanation",
            "component_type": "concept_explanation",
            "content": {
                "text": (
                    "### How Does Motion Create Voltage?\n"
                    "A copper wire contains delocalized free electrons. Under normal conditions, these electrons move in random thermal directions, "
                    "producing zero net electric current.\n\n"
                    "However, when a segment of this wire is physically pushed through a magnetic field, the free electrons move together with the wire:\n"
                    "1. Moving charges inside a magnetic field experience a magnetic force perpendicular to both their velocity and the field lines.\n"
                    "2. This force drives electrons toward one end of the conductor, creating an accumulation of negative charge at one terminal "
                    "and a deficit (positive charge) at the other.\n"
                    "3. This separation of charge produces a potential difference across the wire called an **induced electromotive force (e.m.f.)**.\n"
                    "4. If the conductor is part of a closed circuit, this induced e.m.f. drives an **induced current**!"
                )
            }
        },
        {
            "page_number": 2,
            "page_title": "Conductor Motion and Terminal Charge Separation",
            "block_type": "suggested_diagram",
            "component_type": "suggested_diagram",
            "content": {
                "text": "Diagram showing a copper conductor wire segment moving downward through horizontal magnetic field lines (North to South), forcing free electrons to drift toward the right terminal creating an induced potential difference (e.m.f.).",
                "instruction": (
                    "Draw horizontal magnetic field lines from North pole (left) to South pole (right). "
                    "Draw copper wire moving downward cutting field lines. "
                    "Show magnetic Lorentz force arrows pushing electrons to right terminal (-), leaving left terminal (+). "
                    "Label induced e.m.f. voltage vector."
                )
            }
        },
        # Page 3: Basic Induction Laboratory Experiment
        {
            "page_number": 3,
            "page_title": "Experimental Investigation of Magnetic Flux Cutting",
            "block_type": "step_process",
            "component_type": "step_process",
            "content": {
                "title": "Straight Conductor Motion Protocol",
                "steps": [
                    "**Apparatus Required:** Powerful U-shaped horseshoe magnet, straight copper wire, flexible connecting leads, sensitive centre-zero galvanometer ($G$).",
                    "**Procedure Stage 1 (Moving Vertically Upwards):** Push the wire rapidly upwards through the horizontal magnetic field. Observe a momentary deflection of the galvanometer pointer to the right.",
                    "**Procedure Stage 2 (Moving Vertically Downwards):** Push the wire downwards. Observe a momentary deflection to the left (opposite direction).",
                    "**Procedure Stage 3 (Held Stationary):** Hold the wire completely motionless inside the field. The galvanometer pointer stays at exactly zero ($0$).",
                    "**Procedure Stage 4 (Moving Horizontally):** Slide the wire horizontally parallel to the magnetic field lines. The pointer remains at zero because no field lines are cut."
                ]
            }
        },
        {
            "page_number": 3,
            "page_title": "Straight Conductor Induction Setup with Galvanometer",
            "block_type": "suggested_diagram",
            "component_type": "suggested_diagram",
            "content": {
                "text": "Laboratory diagram of a horizontal straight wire held between the poles of a U-shaped horseshoe magnet and connected to a centre-zero galvanometer G, showing pointer deflections for upward and downward motions.",
                "instruction": (
                    "Draw U-shaped magnet with North and South poles facing each other. "
                    "Draw straight copper wire suspended between poles connected to centre-zero galvanometer G. "
                    "Show upward motion arrow causing pointer deflection to right. "
                    "Show downward motion arrow causing deflection to left."
                )
            }
        },
        # Page 4: Factors Affecting Magnitude
        {
            "page_number": 4,
            "page_title": "Factors Governing the Magnitude of Induced E.M.F.",
            "block_type": "comparison_table",
            "component_type": "comparison_table",
            "content": {
                "headers": ["Physical Variable", "Experimental Alteration", "Effect on Galvanometer Deflection", "Physical Reason"],
                "rows": [
                    ["Relative Speed ($v$)", "Move wire / magnet faster", "Deflection increases significantly", "Cuts more magnetic flux lines per second"],
                    ["Magnetic Field Strength ($B$)", "Use stronger permanent magnet", "Deflection increases", "Higher magnetic flux density per unit area"],
                    ["Number of Turns / Length ($N$)", "Wind wire into multi-turn coil", "Deflection scales proportionally with $N$", "Cumulative charge separation across each turn"]
                ]
            }
        },
        # Page 5: Faraday's Law
        {
            "page_number": 5,
            "page_title": "Faraday's Law of Magnetic Induction",
            "block_type": "definition_card",
            "component_type": "definition_card",
            "content": {
                "term": "Faraday's Law",
                "definition": (
                    "**Faraday's Law of Magnetic Induction** states that the magnitude of the induced electromotive force (e.m.f.) "
                    "in a conductor is directly proportional to the rate of change of magnetic flux linking the conductor.\n\n"
                    "$$\\mathbf{\\varepsilon = -N \\frac{\\Delta \\Phi}{\\Delta t}}$$\n\n"
                    "Where:\n"
                    "- $\\varepsilon$: Induced e.m.f. in Volts ($\\text{V}$)\n"
                    "- $N$: Number of turns in the conductor coil\n"
                    "- $\\Delta \\Phi$: Change in magnetic flux in Webers ($\\text{Wb}$)\n"
                    "- $\\Delta t$: Time duration in seconds ($\\text{s}$)\n"
                    "- Negative sign ($-$): Represents Lenz's Law direction opposition"
                )
            }
        },
        # Page 6: Lenz's Law & Energy Conservation
        {
            "page_number": 6,
            "page_title": "Lenz's Law and Energy Conservation",
            "block_type": "concept_explanation",
            "component_type": "concept_explanation",
            "content": {
                "text": (
                    "### Direction of Induced Current\n"
                    "**Lenz's Law**: The induced current flows in such a direction that its resulting magnetic field opposes the change in magnetic flux that produced it.\n\n"
                    "### The Energy Conservation Proof:\n"
                    "1. **Approaching North Pole**: When you push the North pole of a bar magnet toward a solenoid, the solenoid induces a current that creates a **North pole on the facing end** to repel the incoming magnet.\n"
                    "   - You must perform mechanical work against this repulsive force to push the magnet closer.\n"
                    "   - Your mechanical work is converted directly into the electrical energy of the induced current!\n\n"
                    "2. **Receding North Pole**: When you pull the North pole away from the solenoid, the coil face instantly switches to a **South pole to attract the magnet**, fighting your pulling motion.\n"
                    "   - Again, you must do mechanical work to pull it away, which maintains the electrical energy flow."
                )
            }
        },
        {
            "page_number": 6,
            "page_title": "Lenz's Law Bar Magnet and Solenoid Interaction",
            "block_type": "suggested_diagram",
            "component_type": "suggested_diagram",
            "content": {
                "text": "Diagram showing a bar magnet with North pole approaching a solenoid, inducing a North pole on the solenoid face that repels the magnet, illustrating mechanical work conversion to electrical energy.",
                "instruction": (
                    "Draw bar magnet with North pole moving right toward solenoid. "
                    "Draw solenoid coil linked to galvanometer. "
                    "Show induced current direction creating North pole (N) on left solenoid face. "
                    "Add repulsive force arrows opposing incoming magnet motion."
                )
            }
        },
        # Page 7: Fleming's Right-Hand Rule
        {
            "page_number": 7,
            "page_title": "Fleming's Right-Hand Generator Rule",
            "block_type": "concept_explanation",
            "component_type": "concept_explanation",
            "content": {
                "text": (
                    "To quickly map 3D vectors for straight conductors moving through magnetic fields, use **Fleming's Right-Hand Rule**:\n\n"
                    "Hold the **Thumb**, **First Finger**, and **Second Finger** of your right hand mutually perpendicular to each other:\n\n"
                    "- **Thu**mb $\\longrightarrow$ Motion / Force direction (**Thu**mb = Motion)\n"
                    "- **F**irst Finger $\\longrightarrow$ Magnetic **F**ield direction (North to South)\n"
                    "- **Se**cond Finger $\\longrightarrow$ **C**urrent / Induced e.m.f. direction (**Se**cond = Current)\n\n"
                    "*(Memory Trick: **F**irst finger = **F**ield, **Se**cond finger = **C**urrent, **Thu**mb = **M**otion/Force)*"
                )
            }
        },
        {
            "page_number": 7,
            "page_title": "Fleming's Right-Hand Rule 3D Vector Alignment",
            "block_type": "suggested_diagram",
            "component_type": "suggested_diagram",
            "content": {
                "text": "Vector alignment diagram of Fleming's Right-Hand Rule showing mutually perpendicular Thumb (Motion/Force), Index Finger (Magnetic Field N-S), and Middle Finger (Induced Current).",
                "instruction": (
                    "Draw right hand with thumb, index finger, and middle finger extended at 90 degrees to each other. "
                    "Label Thumb: Motion / Force (Input). Label Index Finger: Magnetic Field (N to S). Label Middle Finger: Induced Current (Output)."
                )
            }
        },
        # Page 8: Left-Hand vs Right-Hand Comparison
        {
            "page_number": 8,
            "page_title": "Comparing Fleming's Left-Hand and Right-Hand Rules",
            "block_type": "comparison_table",
            "component_type": "comparison_table",
            "content": {
                "headers": ["Rule", "Common Name", "Primary Device Application", "Input Energy", "Output Energy"],
                "rows": [
                    ["Fleming's Left-Hand Rule", "The Motor Rule", "Electric Motors, Moving Coil Loudspeakers", "Electrical Energy (Current)", "Mechanical Energy (Motion/Force)"],
                    ["Fleming's Right-Hand Rule", "The Generator Rule", "A.C. Alternators, D.C. Dynamos, Induction Coils", "Mechanical Energy (Motion/Force)", "Electrical Energy (Induced Current)"]
                ]
            }
        },
        # Page 9: Interactive Simulation / Sandbox
        {
            "page_number": 9,
            "page_title": "Interactive Exploration: The Induction Sandbox",
            "block_type": "prediction",
            "component_type": "prediction",
            "content": {
                "text": (
                    "**Think & Predict Before Simulating:**\n\n"
                    "A bar magnet is dropped vertically through a multi-turn copper coil connected to a galvanometer:\n"
                    "1. How does doubling the falling speed of the magnet alter the galvanometer deflection?\n"
                    "2. What happens to the direction of the galvanometer needle as the magnet exits the bottom of the coil?"
                )
            }
        },
        {
            "page_number": 9,
            "page_title": "Interactive Electromagnetic Induction Sandbox",
            "block_type": "suggested_simulation",
            "component_type": "suggested_simulation",
            "content": {
                "text": "Interactive induction simulation allowing students to adjust magnet velocity v, coil turns N (10 to 500), and magnetic field strength B while observing live galvanometer deflections and field line cutting.",
                "instruction": "Simulation Key: induction_sandbox. Real-time rendering of solenoid flux linkage and galvanometer pointer needle movement."
            }
        },
        {
            "page_number": 9,
            "page_title": "Reflecting on Flux Linkage and Deflection",
            "block_type": "reflection",
            "component_type": "reflection",
            "content": {
                "text": (
                    "Doubling falling speed doubles the rate of flux cutting ($\\frac{\\Delta \\Phi}{\\Delta t}$), doubling induced e.m.f. and pointer deflection. "
                    "As the magnet leaves the coil, the exiting pole causes a collapsing flux linkage, reversing the galvanometer needle direction in accordance with Lenz's Law."
                )
            }
        },
        # Page 10: Knowledge Check (MCQ)
        {
            "page_number": 10,
            "page_title": "Check Your Understanding: Lenz's Law Direction",
            "block_type": "knowledge_check",
            "component_type": "knowledge_check",
            "content": {
                "check_type": "multiple_choice",
                "question": "When the South pole of a bar magnet is pulled away from the right end of a solenoid, what magnetic pole is induced at that right end of the solenoid?",
                "options": [
                    "North pole (attracting the receding South pole)",
                    "South pole (repelling the receding South pole)",
                    "Neutral pole (no magnetic effect)",
                    "Alternating North and South pole"
                ],
                "answer": "A",
                "explanation": (
                    "According to Lenz's Law, the induced current opposes the motion causing it. When a South pole is pulled away, the solenoid face induces a North pole to attract the magnet and resist its withdrawal."
                )
            }
        },
        # Page 11: Knowledge Check (MCQ)
        {
            "page_number": 11,
            "page_title": "Check Your Understanding: Increasing Induced Voltage",
            "block_type": "knowledge_check",
            "component_type": "knowledge_check",
            "content": {
                "check_type": "multiple_choice",
                "question": "Which of the following actions will NOT increase the magnitude of the induced e.m.f. in a coil?",
                "options": [
                    "Moving the magnet parallel to the coil axis without cutting flux lines",
                    "Increasing the speed at which the magnet moves through the coil",
                    "Using a stronger magnet with higher flux density",
                    "Winding more turns of wire onto the coil"
                ],
                "answer": "A",
                "explanation": (
                    "Induction requires cutting across magnetic flux lines. Sliding parallel to field lines means delta_Phi / delta_t = 0, producing zero induced e.m.f."
                )
            }
        },
        # Page 12: Summary & Key Takeaways
        {
            "page_number": 12,
            "page_title": "Module 5.1 Summary: Induction Laws",
            "block_type": "summary",
            "component_type": "summary",
            "content": {
                "text": (
                    "### Key Physical Laws:\n"
                    "- **Origin**: Conductor motion cuts flux lines, driving electron drift and terminal e.m.f.\n"
                    "- **Faraday's Law**: $\\varepsilon = -N \\frac{\\Delta \\Phi}{\\Delta t}$\n"
                    "- **Lenz's Law**: Induced current opposes the flux change causing it (energy conservation).\n"
                    "- **Fleming's Right-Hand Rule**: **T**humb = Motion, **F**irst finger = **F**ield, **S**econd finger = **C**urrent."
                )
            }
        },
        {
            "page_number": 12,
            "page_title": "Core Takeaways on Induction Mechanics",
            "block_type": "key_takeaway",
            "component_type": "key_takeaway",
            "content": {
                "text": "Electromagnetic induction converts mechanical work into electrical potential whenever conductors cut across magnetic flux lines."
            }
        }
    ]
}


# =============================================================================
# MODULE 5.2 DATA — Generators, Waveforms, Eddy Currents & Transducers
# =============================================================================
MODULE_5_2 = {
    "unit_name": "Module 5.2: Generators, Alternating Current, and Sound Transducers",
    "unit_order": 2,
    "lesson_title": "Generators, Alternating Current, and Sound Transducers",
    "cards": [
        # Page 1: Hook & Goals
        {
            "page_number": 1,
            "page_title": "Engineering Motion into Electrical Energy",
            "block_type": "learning_goal",
            "component_type": "learning_goal",
            "content": {
                "text": (
                    "How do power stations turn spinning turbines into the electrical currents that power homes? "
                    "How do studio microphones convert human voices into high-fidelity electrical signals?\n\n"
                    "In this module, you will explore the construction of A.C. alternators and D.C. dynamos, "
                    "analyze sinusoidal voltage waveforms across $360^\\circ$ rotations, study moving coil microphones, "
                    "and discover how **eddy currents** are controlled through core laminations.\n\n"
                    "By the end of this lesson, you will be able to:\n"
                    "- Detail the construction and function of A.C. alternators (slip rings) and D.C. dynamos (split-ring commutators)\n"
                    "- Map the sinusoidal voltage output curve to armature rotation angles ($0^\\circ, 90^\\circ, 180^\\circ, 270^\\circ, 360^\\circ$)\n"
                    "- Explain the sound-to-electricity transduction process in moving coil microphones\n"
                    "- Describe eddy current Joule heating losses ($P = I^2R$) and the core lamination solution"
                )
            }
        },
        # Page 2: A.C. Generator (Alternator) Construction
        {
            "page_number": 2,
            "page_title": "The Alternating Current (A.C.) Generator",
            "block_type": "concept_explanation",
            "component_type": "concept_explanation",
            "content": {
                "text": (
                    "An **A.C. generator (alternator)** converts mechanical rotation into alternating current electricity:\n\n"
                    "### Core Structural Components:\n"
                    "1. **Armature Coil**: Multi-turn rectangular coil of insulated copper wire wound on a soft iron core to concentrate flux.\n"
                    "2. **Field Magnets**: Powerful permanent or electromagnets providing a strong, uniform magnetic field.\n"
                    "3. **Slip Rings ($A$ and $B$)**: Two continuous brass rings that rotate with the axle, each permanently connected to one coil end.\n"
                    "4. **Carbon Brushes**: Fixed graphite blocks pressing lightly against rotating slip rings to draw current without twisting wires."
                )
            }
        },
        {
            "page_number": 2,
            "page_title": "Construction Schematic of an A.C. Generator",
            "block_type": "suggested_diagram",
            "component_type": "suggested_diagram",
            "content": {
                "text": "Detailed mechanical diagram of an A.C. generator showing rectangular armature coil rotating between N and S magnetic poles, connected to two continuous slip rings and fixed carbon brushes.",
                "instruction": (
                    "Draw rectangular armature coil between North and South magnetic poles. "
                    "Show axle extending to two continuous brass slip rings. "
                    "Draw carbon brushes pressing against slip rings connected to load resistor. "
                    "Annotate rotation direction arrow."
                )
            }
        },
        # Page 3: Sinusoidal A.C. Waveform Generation
        {
            "page_number": 3,
            "page_title": "Sinusoidal Voltage Waveform Generation",
            "block_type": "concept_explanation",
            "component_type": "concept_explanation",
            "content": {
                "text": (
                    "As the armature coil rotates at constant speed, the rate of flux cutting changes continuously with angle $\\theta$:\n\n"
                    "- **At $0^\\circ$ (Coil Vertical)**: Wires move parallel to field lines. Rate of cutting flux $= 0 \\implies \\mathbf{\\varepsilon = 0\\text{ V}}$.\n"
                    "- **At $90^\\circ$ (Coil Horizontal)**: Wires cut field lines perpendicularly. Maximum rate of cutting flux $\\implies \\mathbf{\\varepsilon = +V_{\\text{peak}}}$.\n"
                    "- **At $180^\\circ$ (Coil Vertical Inverted)**: Wires move parallel to field lines. Rate of cutting flux $= 0 \\implies \\mathbf{\\varepsilon = 0\\text{ V}}$.\n"
                    "- **At $270^\\circ$ (Coil Horizontal Inverted)**: Wires cut field lines in opposite direction $\\implies \\mathbf{\\varepsilon = -V_{\\text{peak}}}$.\n"
                    "- **At $360^\\circ$ (Complete Loop)**: Returns to initial vertical state $\\implies \\mathbf{\\varepsilon = 0\\text{ V}}$."
                )
            }
        },
        {
            "page_number": 3,
            "page_title": "Sinusoidal A.C. Voltage Waveform vs Rotation Angle",
            "block_type": "suggested_diagram",
            "component_type": "suggested_diagram",
            "content": {
                "text": "Graph showing sinusoidal A.C. voltage output on y-axis against armature rotation angle on x-axis (0, 90, 180, 270, 360 degrees) with coil orientation diagrams at each cardinal angle.",
                "instruction": (
                    "Draw graph with y-axis voltage (+V_peak to -V_peak) and x-axis angle (0 to 360 deg). "
                    "Draw smooth sine wave trace starting at 0, reaching +V_peak at 90 deg, 0 at 180 deg, -V_peak at 270 deg, and 0 at 360 deg. "
                    "Draw inset coil diagrams at each key angle."
                )
            }
        },
        # Page 4: D.C. Generator (Split-Ring Commutator)
        {
            "page_number": 4,
            "page_title": "The Direct Current (D.C.) Generator",
            "block_type": "concept_explanation",
            "component_type": "concept_explanation",
            "content": {
                "text": (
                    "To obtain a unidirectional direct current (D.C.) output, the two continuous slip rings are replaced by a **split-ring commutator**:\n\n"
                    "### Mechanical Commutation Process:\n"
                    "1. The split-ring commutator consists of a single copper cylinder split into two insulated half-rings.\n"
                    "2. Every time the armature coil rotates past the vertical position ($180^\\circ$), the induced current inside the coil reverses direction.\n"
                    "3. However, at that exact instant, the two split halves swap contact with the fixed carbon brushes!\n"
                    "4. This mechanical swapping ensures the external output brush always stays positive, delivering a **pulsating unidirectional D.C. waveform**."
                )
            }
        },
        {
            "page_number": 4,
            "page_title": "D.C. Generator Split-Ring Commutator & Output Waveform",
            "block_type": "suggested_diagram",
            "component_type": "suggested_diagram",
            "content": {
                "text": "Diagram of D.C. generator with split-ring commutator and resulting unidirectional pulsating D.C. voltage waveform (all positive half-cycles).",
                "instruction": (
                    "Draw D.C. generator armature coil with split-ring commutator (two half rings). "
                    "Draw fixed carbon brushes. "
                    "Show output waveform graph: pulsating positive half-sine humps (always above zero axis)."
                )
            }
        },
        # Page 5: Moving Coil Microphone
        {
            "page_number": 5,
            "page_title": "The Moving Coil Microphone",
            "block_type": "concept_explanation",
            "component_type": "concept_explanation",
            "content": {
                "text": (
                    "A **moving coil microphone** is a sound transducer operating on electromagnetic induction:\n\n"
                    "### Transduction Steps:\n"
                    "1. **Sound Compression Waves**: Acoustic pressure waves hit the lightweight flexible plastic diaphragm, causing it to vibrate.\n"
                    "2. **Attached Coil**: A small copper coil attached to the diaphragm vibrates back and forth at the exact same acoustic frequency.\n"
                    "3. **Radial Magnetic Field**: The coil is suspended inside the cylindrical magnetic field of a central permanent magnet.\n"
                    "4. **Induced E.M.F.**: As the coil vibrates back and forth across magnetic flux lines, an alternating e.m.f. is induced matching the sound frequency!"
                )
            }
        },
        {
            "page_number": 5,
            "page_title": "Cross-Section of a Moving Coil Microphone",
            "block_type": "suggested_diagram",
            "component_type": "suggested_diagram",
            "content": {
                "text": "Cross-sectional anatomical diagram of a moving coil microphone showing flexible diaphragm, attached voice coil, central permanent magnet cup, and electrical output leads.",
                "instruction": (
                    "Draw microphone body cross section. Show incoming sound waves striking flexible diaphragm. "
                    "Draw attached light copper coil suspended inside radial gap of cylindrical permanent magnet. "
                    "Show output signal wires carrying induced audio A.C. voltage."
                )
            }
        },
        # Page 6: Eddy Currents & Joule Heating
        {
            "page_number": 6,
            "page_title": "Eddy Currents and Parasitic Heating Losses",
            "block_type": "concept_explanation",
            "component_type": "concept_explanation",
            "content": {
                "text": (
                    "When a solid block of metal (like an iron transformer core) experiences a changing magnetic field, "
                    "induction occurs throughout the entire bulk metal volume, creating closed circular current loops called **eddy currents**.\n\n"
                    "### The Problems Caused by Eddy Currents:\n"
                    "1. **Joule Heating Losses ($P = I^2R$)**: Solid iron has low resistance, permitting huge eddy currents that waste electrical energy as excessive heat.\n"
                    "2. **Magnetic Drag (Lenz's Opposition)**: According to Lenz's Law, eddy currents create opposing magnetic fields that drag and slow down rotating machinery."
                )
            }
        },
        # Page 7: Lamination Solution
        {
            "page_number": 7,
            "page_title": "The Core Lamination Solution",
            "block_type": "concept_explanation",
            "component_type": "concept_explanation",
            "content": {
                "text": (
                    "### How Engineers Eliminate Eddy Currents:\n"
                    "Instead of solid iron blocks, cores are constructed out of thin, insulated sheets called **laminations**:\n\n"
                    "1. The core is sliced into thin sheets of soft iron.\n"
                    "2. Each sheet is coated with a non-conducting varnish or lacquer insulation.\n"
                    "3. The insulated boundaries are aligned **perpendicular to the path of the eddy currents**.\n"
                    "4. This physically breaks the large circular current loops into tiny, harmless paths, reducing power loss to near zero!"
                )
            }
        },
        {
            "page_number": 7,
            "page_title": "Solid Metal Plate vs. Laminated Sheet Core Comparison",
            "block_type": "suggested_diagram",
            "component_type": "suggested_diagram",
            "content": {
                "text": "Comparative diagram showing large circular eddy current loops in a solid metal block versus interrupted tiny loops in a laminated sheet core insulated with lacquer.",
                "instruction": (
                    "Left Panel: Solid iron block with large red circular eddy current loops flowing throughout bulk metal. "
                    "Right Panel: Laminated iron core made of thin vertical sheets separated by insulating varnish lines, showing tiny restricted eddy loops."
                )
            }
        },
        # Page 8: Electromagnetic Damping
        {
            "page_number": 8,
            "page_title": "Useful Application: Electromagnetic Damping",
            "block_type": "concept_explanation",
            "component_type": "concept_explanation",
            "content": {
                "text": (
                    "While eddy currents waste energy in transformers, they are intentionally harnessed in **galvanometers** for **electromagnetic damping**:\n\n"
                    "- When current is cut, the meter pointer would normally oscillate back and forth repeatedly before coming to rest.\n"
                    "- By winding the coil on a metallic aluminum frame, the motion induces eddy currents in the frame.\n"
                    "- According to Lenz's Law, these eddy currents create an opposing magnetic force that **instantly stops the pointer's wobble**, bringing it to rest quickly!"
                )
            }
        },
        # Page 9: Knowledge Check (MCQ)
        {
            "page_number": 9,
            "page_title": "Check Your Understanding: Commutator vs Slip Rings",
            "block_type": "knowledge_check",
            "component_type": "knowledge_check",
            "content": {
                "check_type": "multiple_choice",
                "question": "What is the primary physical function of replacing slip rings with a split-ring commutator in a generator?",
                "options": [
                    "To mechanically reverse external circuit connections every 180 degrees, producing unidirectional D.C. output",
                    "To increase the speed of rotation of the armature coil",
                    "To eliminate all mechanical friction between brushes and rings",
                    "To increase the magnetic field strength of the permanent magnets"
                ],
                "answer": "A",
                "explanation": (
                    "A split-ring commutator swaps brush contacts every half-rotation (180 deg) just as induced current inside the coil reverses, maintaining unidirectional D.C. flow in the external circuit."
                )
            }
        },
        # Page 10: Knowledge Check (MCQ)
        {
            "page_number": 10,
            "page_title": "Check Your Understanding: Transformer Lamination",
            "block_type": "knowledge_check",
            "component_type": "knowledge_check",
            "content": {
                "check_type": "multiple_choice",
                "question": "Why are transformer cores constructed using thin insulated laminated sheets rather than a solid piece of soft iron?",
                "options": [
                    "To break large circular eddy current loops, increasing electrical resistance and reducing I^2R heat losses",
                    "To prevent the transformer from overheating due to high primary voltages",
                    "To make the transformer lighter for transport",
                    "To convert direct current into alternating current"
                ],
                "answer": "A",
                "explanation": (
                    "Laminations introduce insulating varnish barriers perpendicular to eddy current paths, breaking large circular loops into tiny paths and drastically reducing I^2R heat waste."
                )
            }
        },
        # Page 11: Summary & Key Takeaways
        {
            "page_number": 11,
            "page_title": "Module 5.2 Summary: Generators & Transducers",
            "block_type": "summary",
            "component_type": "summary",
            "content": {
                "text": (
                    "### Key Engineering Mechanisms:\n"
                    "- **A.C. Alternator**: Armature coil + continuous slip rings $\\rightarrow$ Sinusoidal A.C. output.\n"
                    "- **D.C. Dynamo**: Armature coil + split-ring commutator $\\rightarrow$ Pulsating D.C. output.\n"
                    "- **Microphone**: Sound pressure waves $\\rightarrow$ Diaphragm vibration $\\rightarrow$ Moving coil in magnetic field $\\rightarrow$ A.C. audio signal.\n"
                    "- **Eddy Currents**: Reduced via laminated insulated soft iron cores."
                )
            }
        },
        {
            "page_number": 11,
            "page_title": "Core Takeaways on Generators & Transducers",
            "block_type": "key_takeaway",
            "component_type": "key_takeaway",
            "content": {
                "text": "Rotary generators convert mechanical work into AC or DC electrical power, while core laminations prevent parasitic eddy current losses."
            }
        }
    ]
}


# =============================================================================
# MODULE 5.3 DATA — Mutual Induction, Transformers & Grid Systems
# =============================================================================
MODULE_5_3 = {
    "unit_name": "Module 5.3: Mutual Induction, Transformers, and Grid Systems",
    "unit_order": 3,
    "lesson_title": "Mutual Induction, Transformers, and Grid Systems",
    "cards": [
        # Page 1: Hook & Goals
        {
            "page_number": 1,
            "page_title": "Static Voltage Transformation and National Grids",
            "block_type": "learning_goal",
            "component_type": "learning_goal",
            "content": {
                "text": (
                    "How is electricity transmitted across hundreds of kilometers from hydroelectric dams to distant cities without melting transmission cables? "
                    "Why can't you step up the voltage of a simple D.C. battery using a transformer?\n\n"
                    "In this module, you will master mutual induction, derive the transformer turns ratio ($\\frac{N_p}{N_s} = \\frac{V_p}{V_s}$), "
                    "analyze real-world energy losses, and learn how national power grids use $400\\text{ kV}$ high-voltage transmission to minimize $I^2R$ line losses.\n\n"
                    "By the end of this lesson, you will be able to:\n"
                    "- Explain the principle of mutual induction between primary and secondary coils\n"
                    "- Calculate transformer turns ratios, voltages, and currents for ideal and real transformers\n"
                    "- Explain why transformers require alternating current (A.C.) and fail on direct current (D.C.)\n"
                    "- Detail the 4 major energy losses in transformers (resistance, eddy currents, hysteresis, flux leakage)\n"
                    "- Prove mathematically why stepping up voltage to $400\\text{ kV}$ drastically reduces national grid power line losses"
                )
            }
        },
        # Page 2: Mutual Induction Principle
        {
            "page_number": 2,
            "page_title": "The Principle of Mutual Induction",
            "block_type": "concept_explanation",
            "component_type": "concept_explanation",
            "content": {
                "text": (
                    "**Mutual Induction** occurs when two independent coils are placed near each other, and a changing current in the primary coil "
                    "induces an e.m.f. in the secondary coil:\n\n"
                    "1. **Primary Coil ($P$)**: Connected to an alternating current supply, creating a continuously expanding and collapsing magnetic field.\n"
                    "2. **Secondary Coil ($S$)**: Placed nearby. The changing magnetic flux lines pass through (link with) the secondary turns.\n"
                    "3. **Result**: The secondary coil experiences a changing magnetic flux linkage ($\\frac{\\Delta \\Phi}{\\Delta t}$), inducing an alternating e.m.f. across its terminals!"
                )
            }
        },
        {
            "page_number": 2,
            "page_title": "Mutual Induction Primary and Secondary Coil Linkage",
            "block_type": "suggested_diagram",
            "component_type": "suggested_diagram",
            "content": {
                "text": "Diagram of mutual induction between primary coil connected to A.C. supply and switch and secondary coil connected to centre-zero galvanometer G, showing expanding magnetic flux lines linking both coils.",
                "instruction": (
                    "Draw Primary coil P connected to A.C. supply and switch. "
                    "Draw Secondary coil S insulated nearby connected to galvanometer G. "
                    "Draw expanding/collapsing magnetic flux loops (blue dashed lines) linking primary to secondary."
                )
            }
        },
        # Page 3: Transformer Construction & Turns Ratio
        {
            "page_number": 3,
            "page_title": "Transformer Construction and Turns Ratio",
            "block_type": "formula_breakdown",
            "component_type": "formula_breakdown",
            "content": {
                "formula": "$$\\mathbf{\\frac{N_p}{N_s} = \\frac{V_p}{V_s}} \\qquad \\implies \\qquad V_s = \\frac{N_s}{N_p} \\cdot V_p$$",
                "content": (
                    "A **transformer** is a static device that steps up or steps down alternating voltage:\n\n"
                    "- **Step-Up Transformer**: Has more turns in secondary than primary ($N_s > N_p$), so **$V_s > V_p$**.\n"
                    "- **Step-Down Transformer**: Has fewer turns in secondary than primary ($N_s < N_p$), so **$V_s < V_p$**.\n\n"
                    "Where:\n"
                    "- $N_p, N_s$: Primary and secondary turn counts\n"
                    "- $V_p, V_s$: Primary and secondary alternating voltages"
                )
            }
        },
        {
            "page_number": 3,
            "page_title": "Step-Up vs Step-Down Transformer Construction Schematics",
            "block_type": "suggested_diagram",
            "component_type": "suggested_diagram",
            "content": {
                "text": "Comparative schematic diagram showing a Step-Up transformer (Np < Ns, Vs > Vp) and a Step-Down transformer (Np > Ns, Vs < Vp) wound on a laminated soft iron core.",
                "instruction": (
                    "Draw two iron core transformer diagrams: "
                    "Left: Step-Up (Primary Np=5 turns, Secondary Ns=15 turns, Vs > Vp). "
                    "Right: Step-Down (Primary Np=15 turns, Secondary Ns=5 turns, Vs < Vp). "
                    "Label laminated soft iron core."
                )
            }
        },
        # Page 4: Why Transformers Fail on D.C.
        {
            "page_number": 4,
            "page_title": "Why Transformers Fail on Direct Current (D.C.)",
            "block_type": "common_misconception",
            "component_type": "common_misconception",
            "content": {
                "text": (
                    "### The D.C. Transformer Trap\n"
                    "**The Misconception**: Connecting a $12\\text{ V}$ D.C. battery to a 1:10 step-up transformer will produce a steady $120\\text{ V}$ D.C. output.\n\n"
                    "**The Physics Reality**: The secondary output voltage will be **EXACTLY $0\\text{ V}$**!\n\n"
                    "1. A D.C. battery produces a constant current, which generates a **static, unchanging magnetic field**.\n"
                    "2. Since the magnetic field does not change, the rate of change of magnetic flux linking the secondary is zero ($\\frac{\\Delta \\Phi}{\\Delta t} = 0$).\n"
                    "3. According to Faraday's Law, without changing flux, **zero voltage is induced**.\n"
                    "4. Connecting D.C. will simply overheat and burn the primary coil due to its low resistance without delivering any secondary output!"
                )
            }
        },
        # Page 5: Ideal Transformer Power & Current
        {
            "page_number": 5,
            "page_title": "Ideal Transformer Power and Current Relations",
            "block_type": "formula_breakdown",
            "component_type": "formula_breakdown",
            "content": {
                "formula": "$$\\text{Power Input } (P_p) = \\text{Power Output } (P_s) \\implies I_p \\cdot V_p = I_s \\cdot V_s \\implies \\mathbf{\\frac{I_p}{I_s} = \\frac{V_s}{V_p} = \\frac{N_s}{N_p}}$$",
                "content": (
                    "In an **ideal transformer** ($100\\%$ efficiency), electrical power is conserved.\n\n"
                    "### Critical Current Inverse Relationship:\n"
                    "- A **Step-Up Transformer** increases voltage ($V_s > V_p$) but **decreases current proportionally ($I_s < I_p$)**.\n"
                    "- A **Step-Down Transformer** decreases voltage ($V_s < V_p$) but **increases current ($I_s > I_p$)**.\n"
                    "- A transformer is a voltage/current converter, NOT a power multiplier!"
                )
            }
        },
        # Page 6: Real Transformer Losses & Remedies
        {
            "page_number": 6,
            "page_title": "Four Major Energy Losses in Real Transformers",
            "block_type": "comparison_table",
            "component_type": "comparison_table",
            "content": {
                "headers": ["Loss Mechanism", "Physical Cause", "Thermal Result", "Engineering Remedy"],
                "rows": [
                    ["Winding Resistance ($I^2R$ Loss)", "Electrical resistance of copper wire coils", "Joule heating ($P = I^2R$) in primary/secondary windings", "Use thick copper wire with low electrical resistance"],
                    ["Eddy Currents", "Induced circular currents inside bulk iron core", "Core overheating and energy waste", "Construct core out of thin, varnish-insulated laminated soft iron sheets"],
                    ["Hysteresis Loss", "Magnetic domain friction as iron magnetizes/demagnetizes 50 times/sec", "Thermal energy from magnetic domain rotation friction", "Use soft iron core with high magnetic permeability and low retentivity"],
                    ["Flux Leakage", "Some primary magnetic flux lines fail to link secondary turns", "Unlinked energy lost to surrounding air", "Wind secondary coil directly over primary coil on a closed shell core"]
                ]
            }
        },
        # Page 7: National Grid High-Voltage Engineering
        {
            "page_number": 7,
            "page_title": "National Grid High-Voltage Power Transmission",
            "block_type": "concept_explanation",
            "component_type": "concept_explanation",
            "content": {
                "text": (
                    "### Why Transmit Electricity at 400,000 Volts?\n"
                    "Long-distance transmission cables have significant resistance ($R_{\\text{line}}$). The power lost as heat along the wires is:\n"
                    "$$P_{\\text{loss}} = I^2 \\cdot R_{\\text{line}}$$\n\n"
                    "1. **Low-Voltage Problem**: Transmitting power $P = VI$ at low voltage requires a huge current $I$. Because current is squared ($I^2$), high current wastes massive energy as heat and melts lines!\n"
                    "2. **High-Voltage Solution**: Using a step-up transformer at power stations to raise voltage to $400\\text{ kV}$ reduces current $I$ by a factor of $100\\times$.\n"
                    "3. **Mathematical Savings**: Reducing current by $100\\times$ reduces $I^2R$ line losses by **$10,000\\times$** ($100^2$)!\n"
                    "4. Sub-stations near cities use step-down transformers ($33\\text{ kV} \\rightarrow 11\\text{ kV} \\rightarrow 240\\text{ V}$) for safe domestic distribution."
                )
            }
        },
        {
            "page_number": 7,
            "page_title": "National Electrical Grid Step-Up and Step-Down Flow",
            "block_type": "suggested_diagram",
            "component_type": "suggested_diagram",
            "content": {
                "text": "Block diagram of a national power grid: Power Station (25 kV) -> Step-Up Transformer (400 kV Grid Lines) -> Step-Down Substation (33 kV / 11 kV) -> Consumer Transformer (240 V Domestic).",
                "instruction": (
                    "Draw Power Station generator (25 kV). Draw Step-Up Transformer raising voltage to 400 kV grid towers. "
                    "Draw long-distance pylon cables. Draw Step-Down Substation lowering to 11 kV. "
                    "Draw pole transformer lowering to 240 V domestic house connection."
                )
            }
        },
        # Page 8: Worked Example Level 1
        {
            "page_number": 8,
            "page_title": "Example 1: Transformer Turns and Voltages",
            "block_type": "worked_example",
            "component_type": "worked_example",
            "content": {
                "problem": (
                    "A step-up transformer has a primary coil of $200\\text{ turns}$ and is connected to a $240\\text{ V}$ a.c. mains supply. "
                    "Determine the number of turns required in the secondary coil to obtain an output voltage of $1,440\\text{ V}$."
                ),
                "steps": [
                    "**Given & Required:** Primary turns $N_p = 200$, Primary voltage $V_p = 240\\text{ V}$, Required secondary voltage $V_s = 1440\\text{ V}$. Required: Secondary turns $N_s$.",
                    "**Governing Equation:** $$\\frac{N_p}{N_s} = \\frac{V_p}{V_s} \\implies N_s = \\frac{N_p \\cdot V_s}{V_p}$$",
                    "**Substitution & Calculation:** $$N_s = \\frac{200 \\times 1440}{240} = \\frac{288,000}{240} = \\mathbf{1,200\\text{ turns}}$$",
                    "**Attach Unit:** $N_s = 1,200\\text{ turns}$",
                    "**Physical Reasonableness Check:** A step-up transformer ($1440\\text{ V} > 240\\text{ V}$) requires $N_s > N_p$. $1200 > 200$, which is correct."
                ]
            }
        },
        # Page 9: Worked Example Level 2
        {
            "page_number": 9,
            "page_title": "Example 2: Ideal Transformer Secondary Current",
            "block_type": "worked_example",
            "component_type": "worked_example",
            "content": {
                "problem": (
                    "An ideal step-down transformer with $400\\text{ primary turns}$ and $100\\text{ secondary turns}$ has a primary current "
                    "of $1.5\\text{ A}$ flowing through it. Calculate the current in the secondary circuit."
                ),
                "steps": [
                    "**Given & Required:** $N_p = 400$, $N_s = 100$, Primary current $I_p = 1.5\\text{ A}$. Required: Secondary current $I_s$.",
                    "**Ideal Current Equation:** $$\\frac{I_p}{I_s} = \\frac{N_s}{N_p} \\implies I_s = \\frac{I_p \\cdot N_p}{N_s}$$",
                    "**Substitution & Calculation:** $$I_s = \\frac{1.5 \\times 400}{100} = \\frac{600}{100} = \\mathbf{6.0\\text{ A}}$$",
                    "**Attach Unit:** $I_s = 6.0\\text{ A}$",
                    "**Physical Reasonableness Check:** A step-down transformer ($N_s < N_p$) decreases voltage but increases current. $6.0\\text{ A} > 1.5\\text{ A}$, confirming accuracy."
                ]
            }
        },
        # Page 10: Worked Example Level 3 (Real Transformer with Efficiency)
        {
            "page_number": 10,
            "page_title": "Example 3: Real Transformer with Efficiency",
            "block_type": "worked_example",
            "component_type": "worked_example",
            "content": {
                "problem": (
                    "A transformer has $100\\text{ turns}$ on its primary coil and $10,000\\text{ turns}$ on its secondary coil. "
                    "The primary coil is connected to a $12.0\\text{ V}$ a.c. supply and draws a current of $0.50\\text{ A}$. "
                    "If the transformer operates at an efficiency of $90\\%$, calculate the secondary current $I_s$."
                ),
                "steps": [
                    "**Given Data:** $N_p = 100$, $N_s = 10000$, $V_p = 12.0\\text{ V}$, $I_p = 0.50\\text{ A}$, Efficiency $\\eta = 90\\%$. Required: Secondary current $I_s$.",
                    "**Part A — Secondary Voltage ($V_s$):** $$V_s = \\frac{N_s}{N_p} \\cdot V_p = \\frac{10000}{100} \\times 12.0 = 1200\\text{ V}$$",
                    "**Part B — Primary Power Input ($P_p$):** $$P_p = I_p \\cdot V_p = 0.50\\text{ A} \\times 12.0\\text{ V} = 6.0\\text{ W}$$",
                    "**Part C — Efficiency Equation:** $$\\eta = \\frac{I_s \\cdot V_s}{P_p} \\times 100\\% \\implies I_s = \\frac{\\eta \\cdot P_p}{100 \\cdot V_s}$$",
                    "**Substitution & Calculation:** $$I_s = \\frac{90 \\times 6.0}{100 \\times 1200} = \\frac{540}{120,000} = \\mathbf{0.0045\\text{ A}} \\text{ (or } 4.5\\text{ mA})$$",
                    "**Physical Reasonableness Check:** Stepping up voltage by $100\\times$ reduces current to $\\approx 1/100\\text{th}$. With $90\\%$ efficiency, $I_s = 4.5\\text{ mA}$ (slightly less than the ideal $5.0\\text{ mA}$ due to heat loss)."
                ]
            }
        },
        # Page 11: Worked Example Level 4 (Grid Line Loss Comparison)
        {
            "page_number": 11,
            "page_title": "Example 4: Grid Power Line Loss Reduction",
            "block_type": "worked_example",
            "component_type": "worked_example",
            "content": {
                "problem": (
                    "A power station generates $120\\text{ kW}$ of electrical power. Compare the power lost as heat along a transmission line "
                    "of resistance $5.0\\ \\Omega$ under two scenarios:\n"
                    "(a) Transmitted directly at a low voltage of $2.4\\text{ kV}$.\n"
                    "(b) Stepped up to a high voltage of $24\\text{ kV}$ using an ideal transformer."
                ),
                "steps": [
                    "**Given Data:** Generated Power $P = 120\\text{ kW} = 120,000\\text{ W}$, Line Resistance $R = 5.0\\ \\Omega$.",
                    "**(a) Low-Voltage Transmission ($2.4\\text{ kV} = 2,400\\text{ V}$):**\n"
                    "Line Current $I_1 = \\frac{P}{V_1} = \\frac{120000}{2400} = 50\\text{ A}$.\n"
                    "Power Loss $P_{\\text{loss1}} = I_1^2 \\cdot R = (50)^2 \\times 5.0 = 2500 \\times 5.0 = \\mathbf{12,500\\text{ W}} \\text{ (}12.5\\text{ kW})$.",
                    "**(b) High-Voltage Transmission ($24\\text{ kV} = 24,000\\text{ V}$):**\n"
                    "Line Current $I_2 = \\frac{P}{V_2} = \\frac{120000}{24000} = 5.0\\text{ A}$.\n"
                    "Power Loss $P_{\\text{loss2}} = I_2^2 \\cdot R = (5.0)^2 \\times 5.0 = 25 \\times 5.0 = \\mathbf{125\\text{ W}} \\text{ (}0.125\\text{ kW})$.",
                    "**Conclusion:** Stepping up voltage by $10\\times$ drops line current by $10\\times$, reducing heat power loss by **$100\\times$** (from $12,500\\text{ W}$ to $125\\text{ W}$), saving $99\\%$ of wasted energy!"
                ]
            }
        },
        # Page 12: Worked Example Level 5 (Dual Secondary Challenge)
        {
            "page_number": 12,
            "page_title": "Challenge Problem: Transformer with Dual Secondaries",
            "block_type": "worked_example",
            "component_type": "worked_example",
            "content": {
                "problem": (
                    "A step-down transformer has a primary coil of $1,000\\text{ turns}$ connected to a $240\\text{ V}$ a.c. supply. "
                    "It has two independent secondary coils wound on the same core:\n"
                    "- Secondary A has $50\\text{ turns}$ running a radio rated at $12\\text{ V}, 2.0\\text{ A}$.\n"
                    "- Secondary B has $25\\text{ turns}$ running a charger drawing $2.0\\text{ A}$ at $6.0\\text{ V}$.\n"
                    "Assuming an ideal transformer, calculate the total current drawn from the $240\\text{ V}$ primary supply."
                ),
                "steps": [
                    "**Given Data:** $N_p = 1000$, $V_p = 240\\text{ V}$. Secondary A: $N_{sA} = 50$, $V_{sA} = 12\\text{ V}$, $I_{sA} = 2.0\\text{ A}$. Secondary B: $N_{sB} = 25$, $V_{sB} = 6.0\\text{ V}$, $I_{sB} = 2.0\\text{ A}$. Required: Primary current $I_p$.",
                    "**Part A — Power of Secondary A ($P_{sA}$):** $$P_{sA} = I_{sA} \\cdot V_{sA} = 2.0\\text{ A} \\times 12\\text{ V} = 24.0\\text{ W}$$",
                    "**Part B — Power of Secondary B ($P_{sB}$):** $$P_{sB} = I_{sB} \\cdot V_{sB} = 2.0\\text{ A} \\times 6.0\\text{ V} = 12.0\\text{ W}$$",
                    "**Part C — Total Power Conservation:** $$P_p = P_{sA} + P_{sB} = 24.0\\text{ W} + 12.0\\text{ W} = \\mathbf{36.0\\text{ W}}$$",
                    "**Part D — Primary Current ($I_p$):** $$P_p = I_p \\cdot V_p \\implies I_p = \\frac{36.0\\text{ W}}{240\\text{ V}} = \\mathbf{0.15\\text{ A}}$$",
                    "**Physical Reality Check:** The primary mains draws $0.15\\text{ A}$ at $240\\text{ V}$ ($36\\text{ W}$), perfectly supplying both secondary loads ($24\\text{ W} + 12\\text{ W} = 36\\text{ W}$)."
                ]
            }
        },
        # Page 13: Knowledge Check 1
        {
            "page_number": 13,
            "page_title": "Check Your Understanding: Direct Current and Transformers",
            "block_type": "knowledge_check",
            "component_type": "knowledge_check",
            "content": {
                "check_type": "multiple_choice",
                "question": "What happens when the primary coil of a step-up transformer is connected to a 12 V D.C. battery?",
                "options": [
                    "The secondary output voltage is 0 V because static D.C. produces zero rate of flux change (delta_Phi / delta_t = 0)",
                    "The secondary output voltage is stepped up to 120 V D.C.",
                    "The transformer outputs 12 V alternating current",
                    "The transformer acts as an electrical generator"
                ],
                "answer": "A",
                "explanation": (
                    "Transformers rely on mutual induction, which requires a changing magnetic field. Static D.C. creates constant flux (delta_Phi / delta_t = 0), inducing 0 V in the secondary."
                )
            }
        },
        # Page 14: Knowledge Check 2
        {
            "page_number": 14,
            "page_title": "Check Your Understanding: Grid Transmission Losses",
            "block_type": "knowledge_check",
            "component_type": "knowledge_check",
            "content": {
                "check_type": "multiple_choice",
                "question": "If transmission voltage is stepped up by a factor of 10 using a transformer, by what factor is the power lost as heat (I^2R) along the grid lines reduced?",
                "options": [
                    "100 times (10^2)",
                    "10 times",
                    "20 times",
                    "1,000 times"
                ],
                "answer": "A",
                "explanation": (
                    "Stepping up voltage by 10x reduces current I by 10x. Since heat loss P_loss = I^2 R depends on current squared, reducing I by 10x reduces heat loss by 10^2 = 100 times."
                )
            }
        },
        # Page 15: Summary & Key Takeaways
        {
            "page_number": 15,
            "page_title": "Module 5.3 Summary: Transformers & Grid Systems",
            "block_type": "summary",
            "component_type": "summary",
            "content": {
                "text": (
                    "### Key Applied Principles:\n"
                    "- **Mutual Induction**: Changing A.C. primary current induces secondary e.m.f.\n"
                    "- **Turns Ratio**: $\\frac{N_p}{N_s} = \\frac{V_p}{V_s}$ (Fails on static D.C. because $\\frac{\\Delta \\Phi}{\\Delta t} = 0$).\n"
                    "- **Ideal Current Inverse**: $\\frac{I_p}{I_s} = \\frac{V_s}{V_p}$. Step-up raises voltage but drops current.\n"
                    "- **Real Efficiency**: $\\eta = \\frac{I_s V_s}{I_p V_p} \\times 100\\%$.\n"
                    "- **4 Losses**: Winding $I^2R$, Eddy currents, Hysteresis, Flux leakage.\n"
                    "- **Grid Engineering**: Stepping up to $400\\text{ kV}$ drops line current $I$, reducing $I^2R$ heat losses by $10,000\\times$."
                )
            }
        },
        {
            "page_number": 15,
            "page_title": "Core Takeaways on Grid Engineering",
            "block_type": "key_takeaway",
            "component_type": "key_takeaway",
            "content": {
                "text": "Transformers and high-voltage grid transmission allow electrical energy to be distributed over long distances with minimal heat loss."
            }
        }
    ]
}

ALL_MODULES_TOPIC5 = [MODULE_5_1, MODULE_5_2, MODULE_5_3]


# =============================================================================
# INGESTION EXECUTOR
# =============================================================================

def run_ingestion_topic5(replace_mode=False):
    print("=" * 80)
    print("VLEARN FORM 4 PHYSICS — TOPIC 5: ELECTROMAGNETIC INDUCTION INGESTION")
    print(f"Mode: {'REPLACE (Destructive Fresh Ingestion)' if replace_mode else 'IDEMPOTENT SAFE UPDATE'}")
    print("=" * 80)

    curriculum = Curriculum.objects.filter(name="844").first()
    grade = Grade.objects.filter(curriculum=curriculum, name="Form 4").first()
    subject = Subject.objects.filter(grade=grade, name="Physics").first()

    topic, created = Topic.objects.get_or_create(
        subject=subject,
        name="Topic 5: Electromagnetic Induction",
        defaults={
            "description": (
                "Physical principles of induced e.m.f., flux linkage, Faraday's Law, Lenz's Law, Fleming's Right-Hand Rule, "
                "A.C. alternators, D.C. dynamos, sinusoidal waveforms, moving coil microphones, eddy currents, core laminations, "
                "mutual induction, transformers, energy losses, and national high-voltage electrical grid systems."
            ),
            "order": 5
        }
    )
    print(f"Topic verified: {topic.name} (ID: {topic.id}) under {subject.name}\n")

    total_blocks_created = 0
    total_blocks_updated = 0

    for m_idx, m_data in enumerate(ALL_MODULES_TOPIC5, start=1):
        unit, created = LearningUnit.objects.get_or_create(
            topic=topic,
            name=m_data["unit_name"],
            defaults={"order": m_data["unit_order"]}
        )
        print(f"[{m_idx}/3] Learning Unit: '{unit.name}' ({'Created' if created else 'Found'})")

        lesson, created = Lesson.objects.get_or_create(
            learning_unit=unit,
            defaults={
                "title": m_data["lesson_title"],
                "topic": topic,
                "status": "published",
                "version": 1
            }
        )
        if not created:
            lesson.title = m_data["lesson_title"]
            lesson.status = "published"
            lesson.save()
        print(f"     Lesson: '{lesson.title}' (ID: {lesson.id}, status={lesson.status})")

        with transaction.atomic():
            if replace_mode:
                del_blocks, _ = LessonBlock.objects.filter(lesson=lesson).delete()
                del_assets, _ = LessonAsset.objects.filter(lesson=lesson).delete()
                if del_blocks or del_assets:
                    print(f"     [Replace Mode] Purged {del_blocks} existing blocks, {del_assets} existing assets")

            for order, card in enumerate(m_data["cards"], start=1):
                clean_card = clean_content_dict(card)
                block_id = f"block_{lesson.id}_p{clean_card['page_number']}_{order}_{uuid.uuid4().hex[:6]}"

                if replace_mode:
                    LessonBlock.objects.create(
                        lesson=lesson,
                        block_id=block_id,
                        order=order,
                        page_number=clean_card["page_number"],
                        page_title=clean_card["page_title"],
                        block_type=clean_card["block_type"],
                        component_type=clean_card["component_type"],
                        component_order=order,
                        title=clean_card["page_title"],
                        content=clean_card["content"]
                    )
                    total_blocks_created += 1
                else:
                    existing_block = LessonBlock.objects.filter(
                        lesson=lesson,
                        page_number=clean_card["page_number"],
                        block_type=clean_card["block_type"]
                    ).first()

                    if existing_block:
                        existing_block.order = order
                        existing_block.page_title = clean_card["page_title"]
                        existing_block.component_type = clean_card["component_type"]
                        existing_block.component_order = order
                        existing_block.title = clean_card["page_title"]
                        
                        if isinstance(existing_block.content, dict) and 'svg_content' in existing_block.content:
                            clean_card["content"]["svg_content"] = existing_block.content["svg_content"]
                            clean_card["content"]["svg"] = existing_block.content.get("svg")
                        
                        existing_block.content = clean_card["content"]
                        existing_block.save()
                        total_blocks_updated += 1
                    else:
                        LessonBlock.objects.create(
                            lesson=lesson,
                            block_id=block_id,
                            order=order,
                            page_number=clean_card["page_number"],
                            page_title=clean_card["page_title"],
                            block_type=clean_card["block_type"],
                            component_type=clean_card["component_type"],
                            component_order=order,
                            title=clean_card["page_title"],
                            content=clean_card["content"]
                        )
                        total_blocks_created += 1

        num_pages = max(c["page_number"] for c in m_data["cards"])
        print(f"     Processed {len(m_data['cards'])} cards across {num_pages} pages.\n")

    print("=" * 80)
    print("TOPIC 5 INGESTION COMPLETED SUCCESSFULLY!")
    print(f"Total Blocks Created: {total_blocks_created} | Total Blocks Updated: {total_blocks_updated}")
    print(f"Topic: {topic.name} (ID: {topic.id}) under Subject: {subject.name}")
    print("=" * 80)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Form 4 Physics Topic 5 Ingestion")
    parser.add_argument("--replace", action="store_true", help="Purge and replace blocks fresh")
    args = parser.parse_args()
    run_ingestion_topic5(replace_mode=args.replace)
