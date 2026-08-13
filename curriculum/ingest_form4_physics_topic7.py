"""
VLearn Form 4 Physics — Topic 7: Cathode Rays
Comprehensive Ingestion Engine (Enriched Deep Text & Visual Architecture)

Modules:
  7.1 Production and Properties of Cathode Rays (11 Pages, 20 Blocks)
  7.2 The Cathode-Ray Tube (CRT) and Oscilloscope (CRO) (13 Pages, 20 Blocks)
  7.3 Quantitative Electrodynamics, Laboratory Diagnostics, and Waveform Analysis (15 Pages, 22 Blocks)

Usage:
  /home/jason-bitega/Desktop/VL/vlearn_repositories/Vlearn_backend/venv/bin/python curriculum/ingest_form4_physics_topic7.py
"""

import os
import sys
import django

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "Nexus_backend.settings")
django.setup()

from curriculum.models import (
    Curriculum, Grade, Subject, Topic,
    LearningUnit, Lesson, LessonBlock
)

def run_ingestion():
    print("=" * 80)
    print("VLEARN FORM 4 PHYSICS — TOPIC 7 ENRICHED INGESTION")
    print("=" * 80)

    curriculum = Curriculum.objects.filter(name="844").first()
    grade = Grade.objects.filter(curriculum=curriculum, name="Form 4").first()
    subject = Subject.objects.filter(grade=grade, name="Physics").first()

    topic, _ = Topic.objects.get_or_create(
        subject=subject,
        order=7,
        defaults={"name": "Topic 7: Cathode Rays — Principles, CRT Mechanics, and Oscilloscope Applications"}
    )
    topic.name = "Topic 7: Cathode Rays — Principles, CRT Mechanics, and Oscilloscope Applications"
    topic.save()
    print(f"Topic 7: '{topic.name}' (ID: {topic.id}) ready.")

    # -------------------------------------------------------------------------
    # MODULE 7.1: Production and Properties of Cathode Rays
    # -------------------------------------------------------------------------
    unit_1, _ = LearningUnit.objects.get_or_create(
        topic=topic, order=1,
        defaults={"name": "Module 7.1: Production and Properties of Cathode Rays"}
    )
    lesson_1, _ = Lesson.objects.get_or_create(
        learning_unit=unit_1,
        defaults={"title": "Production and Properties of Cathode Rays", "status": "published", "version": 1}
    )
    lesson_1.blocks.all().delete()

    blocks_m71 = [
        # Page 1
        (1, "Physical Intuition: Bulky Television Warm-Ups", "learning_goal", "learning_goal", 1, {
            "goals": [
                "Understand thermionic emission as thermal electron escape from metal surfaces",
                "Explain the necessity of high vacuum in discharge tubes to minimize electron-gas collisions",
                "Differentiate cathode rays (stream of material electrons) from electromagnetic light waves"
            ]
        }),
        (1, "Physical Intuition: Bulky Television Warm-Ups", "concept_explanation", "concept_explanation", 2, {
            "text": "### Why Did Older Televisions Take Time to Turn On?\nBefore sleek flat-screen OLED monitors, television sets and computer monitors relied on heavy, glass Cathode-Ray Tubes (CRTs). When you switched on an older television, you heard a low hum and a distinct static crackle, but the screen remained dark for several seconds before the picture bloomed into view.\n\n### The Steam Analogy:\nThink of boiling water in a kettle. At room temperature, liquid water molecules are trapped inside the vessel. As you apply heat, the molecules gain kinetic energy until they overcome internal attractive forces and escape as steam. In a cathode-ray tube, a metal filament is electrically heated. The free electrons in the metal gain thermal energy, overcome the surface attractive forces (the work function $\\Phi$), and boil off into the surrounding vacuum space as a cloud of electrons."
        }),
        # Page 2
        (2, "The Thermal Escape: Thermionic Emission", "definition_card", "definition_card", 1, {
            "term": "Thermionic Emission",
            "definition": "The emission of free electrons from the surface of a metal when heated to a high temperature."
        }),
        (2, "The Thermal Escape: Thermionic Emission", "concept_explanation", "concept_explanation", 2, {
            "text": "### Factors Governing Thermionic Emission:\n1. **Temperature of the Metal**: As temperature increases, electrons gain greater thermal kinetic energy, leading to a exponentially higher rate of electron emission.\n2. **Surface Area of the Emitter**: Larger surface area provides a greater number of available free electrons to escape per second.\n3. **Work Function (\\$\\Phi\\$) of the Material**: The minimum energy required to liberate an electron from a metal surface. Metals with low work functions (such as barium oxide or strontium oxide coatings) emit electrons copiously at much lower operating temperatures ($800^\\circ\\text{C}$) compared to pure tungsten ($2,500^\\circ\\text{C}$)."
        }),
        # Page 3
        (3, "The Gaseous Discharge Tube", "concept_explanation", "concept_explanation", 1, {
            "text": "### Why Low Pressure is Mandatory:\nIf thermionic emission occurs in normal atmospheric air ($760\\text{ mmHg}$), liberated electrons collide immediately with heavy nitrogen and oxygen gas molecules, losing their kinetic energy within a fraction of a millimeter.\n\n### Pressure Reduction Stages in a Discharge Tube:\n- **At $10\\text{ mmHg}$ (Moderate Vacuum)**: High voltage ionizes the gas, producing glowing streamers and sparks across the tube.\n- **At $0.01\\text{ mmHg}$ (High Vacuum)**: Gas molecules are so sparse that electrons travel unimpeded from the negative cathode to the positive anode. When these high-speed cathode rays strike the glass tube walls opposite the cathode, they excite the glass atoms, producing a brilliant green phosphor fluorescence!"
        }),
        (3, "The Gaseous Discharge Tube", "suggested_diagram", "suggested_diagram", 2, {
            "text": "Gaseous Discharge Tube at Moderate Pressure vs. Near-Vacuum Cathode Ray Fluorescence",
            "instruction": "Diagram showing discharge tube connected to EHT supply, illustrating streamer ionization at 10 mmHg versus green phosphor fluorescence at 0.01 mmHg."
        }),
        (3, "The Gaseous Discharge Tube", "suggested_image", "suggested_image", 3, {
            "text": "Crookes Gaseous Discharge Tube Demonstrating Cathode Rays"
        }),
        # Page 4
        (4, "Academic History Correction: J.J. Thomson in 1897", "common_misconception", "common_misconception", 1, {
            "text": "### Academic Accuracy Note: J.J. Thomson (1897)\nSome revision summaries contain chronological typos claiming J.J. Thomson discovered cathode rays in the 18th century. This is historically incorrect. Sir Joseph John Thomson was born in 1856 and conducted his monumental deflection experiments at the Cavendish Laboratory in **1897 (the late 19th century)**, proving that cathode rays consist of universal subatomic particles possessing mass and negative charge, which he named **electrons**."
        }),
        # Page 5
        (5, "The Eight Properties of Cathode Rays (Part 1)", "step_process", "step_process", 1, {
            "steps": [
                "**1. Rectilinear Propagation**: Cathode rays travel in straight lines perpendicular to the cathode surface. *Proof*: An opaque metal Maltese Cross placed in the path of the beam casts a sharp, dark shadow on the fluorescent screen at the end of the tube.",
                "**2. Particulate Nature & Momentum**: Cathode rays possess mass ($m_e$), velocity ($v$), and momentum ($p = m_e v$). *Proof*: Rays striking a lightweight, friction-free glass paddle wheel force it to rotate and roll along glass rails toward the anode.",
                "**3. Negative Electrical Charge**: Cathode rays carry negative electrical charge. *Proof*: When passed through a uniform electric field between parallel metal plates, the beam deflects in a smooth parabolic arc toward the positive plate ($+V$)."
            ]
        }),
        (5, "The Eight Properties of Cathode Rays (Part 1)", "suggested_diagram", "suggested_diagram", 2, {
            "text": "Maltese Cross Rectilinear Propagation Shadow Experiment",
            "instruction": "Diagram showing Maltese Cross tube casting a sharp shadow on the fluorescent screen."
        }),
        # Page 6
        (6, "The Eight Properties of Cathode Rays (Part 2)", "concept_explanation", "concept_explanation", 1, {
            "text": "### 4. Magnetic Field Deflection & Fleming's Left-Hand Rule:\nWhen a magnetic field is brought near the discharge tube, the electron beam deflects perpendicularly to both the magnetic field lines and the velocity vector.\n\n### Critical Rule: Conventional Current Reversal!\nCathode rays consist of moving negative charges (electrons) traveling from cathode to anode. Therefore, **conventional electric current flows in the OPPOSITE direction** (from anode to cathode). When applying Fleming's Left-Hand Rule, you must align your second finger (Current $I$) in the direction opposite to electron travel!"
        }),
        (6, "The Eight Properties of Cathode Rays (Part 2)", "suggested_diagram", "suggested_diagram", 2, {
            "text": "Electric Parabolic Deflection vs. Magnetic Perpendicular Deflection (Fleming's LHR)",
            "instruction": "Diagram showing parabolic bending in electric fields and perpendicular deflection in magnetic fields with Fleming's LHR vectors."
        }),
        # Page 7
        (7, "The Eight Properties of Cathode Rays (Part 3)", "step_process", "step_process", 1, {
            "steps": [
                "**5. Fluorescence**: Cathode rays excite atoms in glass, zinc sulphide, or phosphor screen coatings, causing them to emit bright visible light.",
                "**6. High Penetrating Power**: Cathode rays pass through very thin sheets of paper, aluminum foil, or gold leaf without tearing the foil.",
                "**7. Production of X-Rays**: When high-speed cathode rays are accelerated by tens of thousands of volts and stopped abruptly by a heavy tungsten metal target, their kinetic energy converts into high-frequency X-ray photons.",
                "**8. Photographic Effect**: Cathode rays fog photographic plates and film upon impact, similar to ultraviolet light or X-rays."
            ]
        }),
        # Page 8
        (8, "Interactive CRT Electron Sandbox", "suggested_simulation", "suggested_simulation", 1, {
            "text": "Interactive CRT Sandbox: Parameter Slider Controls and Real-Time Trajectory"
        }),
        # Page 9
        (9, "J.J. Thomson e/m Charge-to-Mass Ratio Experiment", "concept_explanation", "concept_explanation", 1, {
            "text": "### J.J. Thomson's Velocity Selector & Charge-to-Mass Ratio ($e/m_e$):\nIn 1897, J.J. Thomson applied mutually perpendicular (crossed) electric ($E$) and magnetic ($B$) fields to a cathode ray beam.\n\n### 1. Velocity Selector Condition:\nBy tuning field strengths so electric force $F_e = eE$ exactly balances magnetic force $F_b = evB$, the beam passes undeviated:\n$$eE = evB \\implies v = \\frac{E}{B}$$\n\n### 2. Specific Charge ($e/m_e$):\nWith magnetic field alone, the beam bends in a circular arc of radius $r$ ($evB = \\frac{m_e v^2}{r}$):\n$$\\frac{e}{m_e} = \\frac{v}{B r} = \\frac{E}{B^2 r} = 1.76 \\times 10^{11}\\text{ C/kg}$$\nThis constant value proved that electrons are identical universal subatomic constituents of all matter!"
        }),
        # Page 10
        (10, "Knowledge Check: Cathode Ray Properties", "knowledge_check", "knowledge_check", 1, {
            "question": "Which experiment conclusively proved that cathode rays possess momentum and kinetic energy?",
            "options": ["Maltese Cross shadow experiment", "Lightweight paddle wheel rotation", "Gold leaf penetration test", "Phosphor screen fluorescence"],
            "answer": "Lightweight paddle wheel rotation",
            "explanation": "Rays striking the lightweight paddle wheel transfer mechanical momentum p = m_e v, forcing it to rotate and roll along glass rails."
        }),
        (10, "Knowledge Check: Thermionic Emission", "knowledge_check", "knowledge_check", 2, {
            "question": "Why are oxide coatings (barium or strontium oxide) used on cathode surfaces?",
            "options": ["To increase electrical resistance", "To lower the work function and emit electrons at lower temperatures", "To reflect light rays", "To prevent corrosion"],
            "answer": "To lower the work function and emit electrons at lower temperatures",
            "explanation": "Oxide coatings drastically reduce the metal work function (Phi), enabling abundant thermionic emission at ~800 °C instead of 2,500 °C."
        }),
        # Page 11
        (11, "Module Summary", "summary", "summary", 1, {
            "text": "### Key Takeaways:\n1. **Thermionic Emission**: Liberates electrons via thermal kinetic energy overcoming work function $\\Phi$.\n2. **Vacuum Necessity**: High vacuum ($0.01\\text{ mmHg}$) is required for unimpeded electron acceleration.\n3. **Properties**: Rectilinear propagation, particulate momentum, negative charge, magnetic deflection (Fleming's LHR), fluorescence, X-ray generation.\n4. **Thomson's $e/m_e$**: Specific charge $1.76 \\times 10^{11}\\text{ C/kg}$ established the electron as a universal particle."
        }),
        (11, "Module Summary", "key_takeaway", "key_takeaway", 2, {
            "text": "Cathode rays are streams of high-speed negative electrons produced by thermionic emission in high vacuum tubes."
        })
    ]

    for p_num, title, btype, ctype, order, content in blocks_m71:
        LessonBlock.objects.create(
            lesson=lesson_1,
            page_number=p_num,
            page_title=title,
            title=title,
            block_type=btype,
            component_type=ctype,
            component_order=order,
            order=p_num * 10 + order,
            content=content
        )
    print(f"  Lesson 1 populated with {lesson_1.blocks.count()} blocks across 11 pages.")

    # -------------------------------------------------------------------------
    # MODULE 7.2: The Cathode-Ray Tube (CRT) and Oscilloscope (CRO)
    # -------------------------------------------------------------------------
    unit_2, _ = LearningUnit.objects.get_or_create(
        topic=topic, order=2,
        defaults={"name": "Module 7.2: The Cathode-Ray Tube (CRT) and Oscilloscope (CRO)"}
    )
    lesson_2, _ = Lesson.objects.get_or_create(
        learning_unit=unit_2,
        defaults={"title": "The Cathode-Ray Tube (CRT) and Oscilloscope (CRO)", "status": "published", "version": 1}
    )
    lesson_2.blocks.all().delete()

    blocks_m72 = [
        # Page 1
        (1, "Overview of CRT Construction", "learning_goal", "learning_goal", 1, {
            "goals": [
                "Identify the three functional assemblies of a Cathode-Ray Tube (Electron Gun, Deflection System, Screen)",
                "Explain the role of the negative control grid in controlling beam intensity and screen brightness",
                "Describe how orthogonal Y-plates and X-plates steer the electron beam across the screen"
            ]
        }),
        (1, "Overview of CRT Construction", "concept_explanation", "concept_explanation", 2, {
            "text": "### What is a Cathode-Ray Tube (CRT)?\nA Cathode-Ray Tube is a highly evacuated glass envelope containing an electron gun, an electrostatic deflection system, and a phosphor-coated display screen. It acts as the heart of laboratory oscilloscopes, radar displays, and medical heart monitors, converting electrical voltage signals into instant visual graphs."
        }),
        (1, "Overview of CRT Construction", "suggested_diagram", "suggested_diagram", 3, {
            "text": "Complete Internal Assembly Anatomy of a Cathode-Ray Tube (CRT)",
            "instruction": "Diagram showing electron gun, Y-plates, X-plates, and phosphor screen in an evacuated glass tube."
        }),
        (1, "Overview of CRT Construction", "suggested_image", "suggested_image", 4, {
            "text": "Cathode-Ray Tube Glass Hardware Construction Unit"
        }),
        # Page 2
        (2, "Assembly A: The Electron Gun", "concept_explanation", "concept_explanation", 1, {
            "text": "### 1. Heater & Cathode:\n- **Heater Filament**: A tungsten wire powered by a low voltage ($6\\text{ V}$) supply.\n- **Cathode**: A metal cylinder coated with barium/strontium oxides heated indirectly to liberate electrons by thermionic emission.\n\n### 2. Control Grid ($-V_g$):\nA metal cup with a central aperture surrounding the cathode, maintained at a negative potential relative to the cathode.\n- **Function**: Repels electrons toward the central axis. Adjusting grid negativity controls the number of electrons passing through per second, thereby acting as the **BRIGHTNESS CONTROL KNOB** on the oscilloscope panel!"
        }),
        (2, "Assembly A: The Electron Gun", "suggested_diagram", "suggested_diagram", 2, {
            "text": "Detailed Construction & Function of the CRT Electron Gun Components",
            "instruction": "Diagram showing filament, oxide cathode, and negative control grid controlling electron emission rate."
        }),
        # Page 3
        (3, "Electrostatic Focusing and Acceleration", "concept_explanation", "concept_explanation", 1, {
            "text": "### 3. Focusing and Accelerating Anodes:\nTwo or more coaxial metal cylinders maintained at high positive potentials ($200\\text{ V}$ to $5,000\\text{ V}$).\n- **Electrostatic Lens Effect**: The curved electric field lines established between anode cylinders focus divergent electron paths into a razor-sharp beam.\n- **Beam Acceleration**: High positive potential energy accelerates electrons to high kinetic speeds before entering the deflection system."
        }),
        # Page 4
        (4, "Assembly B: The Deflection System", "step_process", "step_process", 1, {
            "steps": [
                "**Step 1: Electron Beam Acceleration**: High-speed electrons leave the final accelerating anode of the electron gun and enter the deflection assembly region.",
                "**Step 2: Y-Plate Deflection (Vertical Steering)**: The beam passes between the upper and lower horizontal Y-plates. An external test signal voltage creates a vertical electric field, deflecting the beam up or down on the screen to measure signal amplitude.",
                "**Step 3: X-Plate Deflection (Horizontal Steering)**: The beam enters the vertical left and right X-plates. An internal time-base circuit applies a sawtooth voltage, steadily pulling the beam horizontally from left to right at constant speed.",
                "**Step 4: Instant Flyback & Cycle Repeat**: Once the beam reaches the right edge of the screen, the sawtooth voltage drops instantly to zero, snapping the spot back to the left edge to begin the next waveform trace."
            ]
        }),
        (4, "Assembly B: The Deflection System", "suggested_diagram", "suggested_diagram", 2, {
            "text": "Orthogonal Y-Plates (Vertical Input) vs. X-Plates (Horizontal Time-Base Sweep)",
            "instruction": "Diagram showing Y-plates deflecting vertically and X-plates deflecting horizontally."
        }),
        # Page 5
        (5, "Assembly C: The Fluorescent Screen", "concept_explanation", "concept_explanation", 1, {
            "text": "### Converting Kinetic Energy into Light:\nThe inner face of the glass screen is coated with phosphor dots (such as zinc sulphide). When the high-speed electron beam strikes the phosphor screen, the kinetic energy of the electrons ($E_k = \\frac{1}{2}m_e v^2$) is instantly converted into bright green visible light dots."
        }),
        # Page 6
        (6, "The Time Base Circuit & Sawtooth Waveform", "concept_explanation", "concept_explanation", 1, {
            "text": "### Why a Sawtooth Waveform is Essential:\nIf an alternating voltage is connected to Y-plates with zero X-plate voltage, the beam bobs up and down, drawing a simple vertical line. To display voltage changing over time, the X-plates must pull the beam horizontally across the screen at a steady speed.\n\n### The Sawtooth Cycle:\n1. **Linear Sweep ($$-V_p \\rightarrow +V_p$$)**: X-plate voltage increases linearly with time, dragging the electron spot smoothly from left to right across the screen.\n2. **Instant Flyback ($$+V_p \\rightarrow -V_p$$)**: Voltage drops instantly back to $-V_p$, snapping the beam back to the left edge so rapidly that the return path is invisible."
        }),
        (6, "The Time Base Circuit & Sawtooth Waveform", "suggested_diagram", "suggested_diagram", 2, {
            "text": "Time-Base Circuit Sawtooth Waveform: Linear Sweep and Instant Flyback",
            "instruction": "Graph showing sawtooth voltage vs time with linear sweep and instant flyback phase."
        }),
        # Page 7
        (7, "CRO Control Panel Calibration", "comparison_table", "comparison_table", 1, {
            "headers": ["Control Knob", "Circuit Connection", "Primary Function / Metric"],
            "rows": [
                ["Y-Gain (Volts/cm)", "Y-Deflection Plates", "Sets vertical scale amplifier. Measures Peak-to-Peak Voltage (V_p-p = height x Y-Gain)."],
                ["Time-Base (ms/cm)", "X-Deflection Plates", "Sets horizontal sweep speed. Measures Period (T = length x Time-Base) & Frequency (f = 1/T)."],
                ["Intensity / Brightness", "Control Grid (-Vg)", "Adjusts grid potential to change electron beam density and spot brightness."],
                ["Focus Control", "Anode 1 Potential", "Adjusts electrostatic lens potential difference to sharpen beam spot on screen."]
            ]
        }),
        # Page 8
        (8, "Worked Example: Time-Base Period & Frequency", "worked_example", "worked_example", 1, {
            "problem": "A CRO time-base is set at $5.0\\text{ ms/cm}$. A full wave cycle on the screen occupies a horizontal distance of $2.0\\text{ cm}$. Calculate: 1. Period $T$. 2. Frequency $f$.",
            "steps": [
                "Step 1: Identify knowns: Horizontal distance $d = 2.0\\text{ cm}$, Time-Base $TB = 5.0\\text{ ms/cm} = 0.005\\text{ s/cm}$.",
                "Step 2: Calculate Period: $T = d \\times TB = 2.0\\text{ cm} \\times 0.005\\text{ s/cm} = 0.010\\text{ s}$ ($10\\text{ ms}$).",
                "Step 3: Calculate Frequency: $f = \\frac{1}{T} = \\frac{1}{0.010\\text{ s}} = 100\\text{ Hz}$."
            ]
        }),
        # Page 9
        (9, "Knowledge Check: Control Grid", "knowledge_check", "knowledge_check", 1, {
            "question": "Making the control grid MORE negative relative to the cathode causes the screen spot to:",
            "options": ["Become brighter", "Become dimmer or disappear", "Move upward", "Deflect horizontally"],
            "answer": "Become dimmer or disappear",
            "explanation": "Increasing grid negativity repels more electrons back toward the cathode, reducing beam current density and making the spot dimmer."
        }),
        (10, "Knowledge Check: Time-Base Waveform", "knowledge_check", "knowledge_check", 2, {
            "question": "What type of voltage waveform does the time-base circuit apply to the X-deflection plates?",
            "options": ["Sinusoidal wave", "Square wave", "Sawtooth wave", "Constant D.C. voltage"],
            "answer": "Sawtooth wave",
            "explanation": "A sawtooth voltage linearly increases voltage to sweep the spot left to right, then drops instantly during flyback."
        }),
        # Page 11
        (11, "Module Summary", "summary", "summary", 1, {
            "text": "### Module Summary:\n1. **CRT Components**: Electron gun (heater, cathode, grid, anodes), Deflection system (Y & X plates), Phosphor screen.\n2. **Brightness & Focus**: Grid potential controls brightness; Anode 1 potential controls sharp focusing.\n3. **Waveform Plotting**: Y-plates input signal; X-plates sawtooth sweep plots voltage against time."
        }),
        (12, "Module Summary", "key_takeaway", "key_takeaway", 2, {
            "text": "The CRO uses electrostatic deflection and time-base sweep to display real-time voltage waveforms on a phosphor screen."
        })
    ]

    for p_num, title, btype, ctype, order, content in blocks_m72:
        LessonBlock.objects.create(
            lesson=lesson_2,
            page_number=p_num,
            page_title=title,
            title=title,
            block_type=btype,
            component_type=ctype,
            component_order=order,
            order=p_num * 10 + order,
            content=content
        )
    print(f"  Lesson 2 populated with {lesson_2.blocks.count()} blocks across 12 pages.")

    # -------------------------------------------------------------------------
    # MODULE 7.3: Quantitative Electrodynamics, Laboratory Diagnostics, and Waveform Analysis
    # -------------------------------------------------------------------------
    unit_3, _ = LearningUnit.objects.get_or_create(
        topic=topic, order=3,
        defaults={"name": "Module 7.3: Quantitative Electrodynamics, Laboratory Diagnostics, and Waveform Analysis"}
    )
    lesson_3, _ = Lesson.objects.get_or_create(
        learning_unit=unit_3,
        defaults={"title": "Quantitative Electrodynamics, Laboratory Diagnostics, and Waveform Analysis", "status": "published", "version": 1}
    )
    lesson_3.blocks.all().delete()

    blocks_m73 = [
        # Page 1
        (1, "Governing Mathematics 1: Energy Conservation", "formula_breakdown", "formula_breakdown", 1, {
            "formula": "e V = \\frac{1}{2} m_e v^2 \\implies v = \\sqrt{\\frac{2 e V}{m_e}}",
            "variables": {
                "e": "Elementary electron charge (1.6 x 10^-19 Coulombs)",
                "V": "Accelerating anode voltage (Volts)",
                "m_e": "Electron rest mass (9.1 x 10^-31 kg)",
                "v": "Electron beam velocity leaving anode (m/s)"
            }
        }),
        (1, "Governing Mathematics 1: Energy Conservation", "suggested_diagram", "suggested_diagram", 2, {
            "text": "Conservation of Energy in the Electron Gun: Electrostatic Work to Kinetic Energy",
            "instruction": "Diagram showing electrostatic potential work converting to kinetic energy."
        }),
        # Page 2
        (2, "Governing Mathematics 2: CRO Graticule Measurements", "formula_breakdown", "formula_breakdown", 1, {
            "formula": "T = d \\times TB, \\quad f = \\frac{1}{T}, \\quad V_0 = h \\times Y_{\\text{gain}}",
            "variables": {
                "d": "Horizontal grid length of one cycle (cm)",
                "TB": "Time-Base setting (s/cm or ms/cm)",
                "h": "Vertical peak height from center line (cm)",
                "Y_gain": "Y-Gain sensitivity setting (V/cm)"
            }
        }),
        (2, "Governing Mathematics 2: CRO Graticule Measurements", "suggested_diagram", "suggested_diagram", 2, {
            "text": "CRO Graticule Screen Trace Measurements for Amplitude, Period, and Frequency",
            "instruction": "Diagram showing CRO grid trace with peak height h and cycle length d indicators."
        }),
        (2, "Governing Mathematics 2: CRO Graticule Measurements", "suggested_image", "suggested_image", 3, {
            "text": "Cathode-Ray Oscilloscope Screen Display Trace"
        }),
        # Page 3
        (3, "Voltage Metrics: Peak, Peak-to-Peak, and RMS", "concept_explanation", "concept_explanation", 1, {
            "text": "### Differentiating Voltage Metrics:\n- **Peak Voltage ($V_0$)**: Maximum vertical displacement from the central zero reference line ($V_0 = h \\times Y_{\\text{gain}}$).\n- **Peak-to-Peak Voltage ($V_{\\text{p-p}}$)**: Total vertical distance from lowest trough to highest crest ($V_{\\text{p-p}} = 2 V_0$).\n- **Root-Mean-Square Voltage ($V_{\\text{rms}}$)**: The equivalent D.C. voltage that delivers the same heating power ($V_{\\text{rms}} = \\frac{V_0}{\\sqrt{2}} \\approx 0.707 V_0$)."
        }),
        # Page 4
        (4, "Worked Example Level 1 — Direct Substitution", "worked_example", "worked_example", 1, {
            "problem": "A waveform displayed on a CRO screen has a horizontal length of $1.8\\text{ cm}$ for one complete cycle. If the time-base control is set at $10\\text{ ms/cm}$, calculate the frequency of the wave.",
            "steps": [
                "Step 1: Identify knowns: Horizontal cycle length $d = 1.8\\text{ cm}$, Time-base $TB = 10\\text{ ms/cm} = 0.010\\text{ s/cm}$.",
                "Step 2: Identify required: Frequency $f$.",
                "Step 3: Write equations: $T = d \\times TB$, $f = \\frac{1}{T}$.",
                "Step 4: Substitute values: $T = 1.8\\text{ cm} \\times 0.010\\text{ s/cm} = 0.018\\text{ s}$.",
                "Step 5: Calculate frequency: $f = \\frac{1}{0.018\\text{ s}} = 55.56\\text{ Hz}$.",
                "Step 6: Attach unit: $f = 56\\text{ Hz}$ (or $55.6\\text{ Hz}$).",
                "Step 7: Physical check: An $18\\text{ ms}$ period corresponds to a low audio/mains frequency scale, which is physically reasonable."
            ]
        }),
        # Page 5
        (5, "Worked Example Level 2 — Formula Rearrangement", "worked_example", "worked_example", 1, {
            "problem": "An electron gun uses an accelerating potential difference of $2.0\\text{ kV}$. Calculate the maximum speed of the electrons as they leave the anode. (Take $e = 1.6 \\times 10^{-19}\\text{ C}$, $m_e = 9.1 \\times 10^{-31}\\text{ kg}$).",
            "steps": [
                "Step 1: Identify knowns: $V = 2.0\\text{ kV} = 2000\\text{ V}$, $e = 1.6 \\times 10^{-19}\\text{ C}$, $m_e = 9.1 \\times 10^{-31}\\text{ kg}$.",
                "Step 2: Required: Electron velocity $v$.",
                "Step 3: Equation: $e V = \\frac{1}{2} m_e v^2$.",
                "Step 4: Rearrange: $v = \\sqrt{\\frac{2 e V}{m_e}}$.",
                "Step 5: Substitute: $v = \\sqrt{\\frac{2 \\times (1.6 \\times 10^{-19}) \\times 2000}{9.1 \\times 10^{-31}}}$.",
                "Step 6: Calculate: $v = \\sqrt{\\frac{6.4 \\times 10^{-16}}{9.1 \\times 10^{-31}}} = \\sqrt{7.0329 \\times 10^{14}} = 2.65 \\times 10^7\\text{ m/s}$.",
                "Step 7: Unit: $v = 2.65 \\times 10^7\\text{ m/s}$ (about $9\\%$ the speed of light).",
                "Step 8: Physical check: High-speed electrons in vacuum tubes typically travel around $10^7\\text{ m/s}$, which is physically correct."
            ]
        }),
        # Page 6
        (6, "Worked Example Level 3 — Multi-Step Voltage", "worked_example", "worked_example", 1, {
            "problem": "An alternating signal connected to the Y-plates has a peak-to-peak vertical trace height of $4.0\\text{ cm}$. The Y-gain is set to $5.0\\text{ V/cm}$. Calculate: 1. Peak voltage $V_0$. 2. RMS voltage $V_{\\text{rms}}$.",
            "steps": [
                "Step 1: Knowns: Peak-to-peak height $h_{\\text{p-p}} = 4.0\\text{ cm}$, Y-gain $Y_{\\text{gain}} = 5.0\\text{ V/cm}$.",
                "Step 2: Required: Peak voltage $V_0$ and RMS voltage $V_{\\text{rms}}$.",
                "Step 3: Equations: $V_{\\text{p-p}} = h_{\\text{p-p}} \\times Y_{\\text{gain}}$, $V_0 = \\frac{V_{\\text{p-p}}}{2}$, $V_{\\text{rms}} = \\frac{V_0}{\\sqrt{2}}$.",
                "Step 4: Calculate Peak-to-Peak Voltage: $V_{\\text{p-p}} = 4.0\\text{ cm} \\times 5.0\\text{ V/cm} = 20.0\\text{ V}$.",
                "Step 5: Calculate Peak Voltage: $V_0 = \\frac{20.0\\text{ V}}{2} = 10.0\\text{ V}$.",
                "Step 6: Calculate RMS Voltage: $V_{\\text{rms}} = \\frac{10.0\\text{ V}}{\\sqrt{2}} \\approx 7.07\\text{ V}$."
            ]
        }),
        # Page 7
        (7, "Worked Example Level 4 — Visual Trace Interpretation", "worked_example", "worked_example", 1, {
            "problem": "A CRO trace shows a sine wave rising to $+2.0\\text{ cm}$ and falling to $-2.0\\text{ cm}$. One cycle occupies $4.0\\text{ cm}$ horizontally. Y-gain is $2.0\\text{ V/cm}$ and Time-Base is $2.5\\text{ ms/cm}$. Determine Peak Voltage $V_0$ and Frequency $f$.",
            "steps": [
                "Step 1: Knowns: Peak height $h = 2.0\\text{ cm}$, Cycle length $d = 4.0\\text{ cm}$, Y-gain $= 2.0\\text{ V/cm}$, Time-Base $TB = 2.5\\text{ ms/cm} = 0.0025\\text{ s/cm}$.",
                "Step 2: Peak Voltage: $V_0 = h \\times Y_{\\text{gain}} = 2.0\\text{ cm} \\times 2.0\\text{ V/cm} = 4.0\\text{ V}$.",
                "Step 3: Period: $T = d \\times TB = 4.0\\text{ cm} \\times 0.0025\\text{ s/cm} = 0.010\\text{ s}$.",
                "Step 4: Frequency: $f = \\frac{1}{T} = \\frac{1}{0.010\\text{ s}} = 100\\text{ Hz}$."
            ]
        }),
        # Page 8
        (8, "Worked Example Level 5 — Dual-Axis Electrodynamics", "worked_example", "worked_example", 1, {
            "problem": "Electrons are accelerated through $2.5\\text{ kV}$ and enter parallel deflecting plates of length $4.0\\text{ cm}$ separated by $1.0\\text{ cm}$ with a deflecting voltage of $150\\text{ V}$. Calculate horizontal velocity $v_x$ and transit time $t$.",
            "steps": [
                "Step 1: Knowns: $V_{\\text{acc}} = 2500\\text{ V}$, $L = 0.040\\text{ m}$, $d = 0.010\\text{ m}$, $V_{\\text{defl}} = 150\\text{ V}$, $e = 1.6 \\times 10^{-19}\\text{ C}$, $m_e = 9.1 \\times 10^{-31}\\text{ kg}$.",
                "Step 2: Horizontal velocity: $v_x = \\sqrt{\\frac{2 e V_{\\text{acc}}}{m_e}} = \\sqrt{\\frac{2 \\times (1.6 \\times 10^{-19}) \\times 2500}{9.1 \\times 10^{-31}}} = 2.97 \\times 10^7\\text{ m/s}$.",
                "Step 3: Transit time: $t = \\frac{L}{v_x} = \\frac{0.040\\text{ m}}{2.97 \\times 10^7\\text{ m/s}} = 1.35 \\times 10^{-9}\\text{ s}$ ($1.35\\text{ nanoseconds}$)."
            ]
        }),
        # Page 9
        (9, "Laboratory Investigation 1: Maltese Cross Tube", "concept_explanation", "concept_explanation", 1, {
            "text": "### Laboratory Procedure: Maltese Cross Shadow Experiment\n1. **Apparatus Setup**: Connect a Maltese Cross tube to an Extra High Tension (EHT) power supply set to $3,000\\text{ V}$ D.C.\n2. **Observation**: A sharp, dark cross-shaped shadow appears in the center of a brilliant green fluorescent screen at the end of the tube.\n3. **Hinged Folding Test**: Unhook the Maltese cross so it falls flat; the shadow disappears, and the screen glows uniformly green.\n4. **Magnetic Deflection**: Bring the North pole of a bar magnet near the top of the glass envelope. The cross shadow shifts downward on the screen, verifying magnetic deflection via Fleming's Left-Hand Rule."
        }),
        (9, "Laboratory Investigation 1: Maltese Cross Tube", "suggested_diagram", "suggested_diagram", 2, {
            "text": "Laboratory Maltese Cross Shadow & Magnetic Field Deflection Circuit Setup",
            "instruction": "Diagram showing Maltese cross tube connected to EHT supply with bar magnet deflection setup."
        }),
        # Page 10
        (10, "Laboratory Investigation 2: CRO Waveform Diagnostics", "concept_explanation", "concept_explanation", 1, {
            "text": "### Laboratory Procedure: Measuring AC Mains Voltage & Frequency\n1. **Setup**: Connect a step-down secondary transformer output ($6\\text{ V AC}$) to the CRO Y-input terminals.\n2. **Time-Base OFF**: Turn the time-base switch OFF. A bright vertical green line appears on the screen (height $= 2.8\\text{ cm}$).\n3. **Time-Base ON**: Turn the time-base to $5.0\\text{ ms/cm}$. A smooth sine wave appears across the graticule grid.\n4. **Measurements**: Peak height $h = 1.4\\text{ cm}$ ($V_0 = 1.4 \\times 6.0\\text{ V/cm} = 8.4\\text{ V}$); Cycle length $d = 4.0\\text{ cm}$ ($T = 4.0 \\times 5.0\\text{ ms/cm} = 20\\text{ ms} \\implies f = 50\\text{ Hz}$, matching Kenya Power mains frequency!)."
        }),
        # Page 11
        (11, "Addressing Common Misconceptions", "common_misconception", "common_misconception", 1, {
            "text": "### 4 Critical Misconceptions Clarified:\n1. **Filament Current vs. Anode Voltage**: Filament current controls the temperature and electron emission rate (brightness), while anode voltage controls electron kinetic velocity ($v = \\sqrt{2eV/m_e}$).\n2. **Control Grid Function**: The control grid does not accelerate electrons; it repels them to regulate beam density.\n3. **Light vs. Cathode Rays**: Cathode rays are negative material particles with mass, momentum, and charge—not electromagnetic light waves.\n4. **Trajectory Geometry**: Inside parallel deflecting plates, the path is a smooth parabolic arc. Outside the plates, where no electric field exists, the electrons follow a straight linear tangent path!"
        }),
        (11, "Addressing Common Misconceptions", "suggested_diagram", "suggested_diagram", 2, {
            "text": "Electron Trajectory Geometry: Parabolic Arc Inside Field vs. Straight Tangent Outside",
            "instruction": "Diagram showing parabolic trajectory inside parallel plates and straight tangent line outside."
        }),
        # Page 12
        (12, "Lissajous Figures on CRO Screen Grid", "concept_explanation", "concept_explanation", 1, {
            "text": "### Phase Shift & Frequency Diagnostics using Lissajous Patterns:\nWhen two sinusoidal AC signals are applied simultaneously to the Y-plates and X-plates (with time-base OFF), the beam draws a **Lissajous Figure** on the CRO screen.\n\n### Key Diagnostics:\n- **$1:1$ Ratio ($f_y = f_x$)**: Produces a circle when phase difference $\\phi = 90^\\circ$, or an inclined straight line when $\\phi = 0^\\circ$ or $180^\\circ$.\n- **$1:2$ Ratio ($f_y = 2 f_x$)**: Produces a figure-eight shape (two vertical loops to one horizontal loop).\nLissajous patterns allow precise, instant frequency ratio and phase shift measurements without relying on time-base calibration!"
        }),
        (12, "Lissajous Figures on CRO Screen Grid", "suggested_diagram", "suggested_diagram", 2, {
            "text": "Lissajous Figures on CRO Screen Grid for Phase Shift and Frequency Diagnostics",
            "instruction": "Diagram showing 1:1 circle/ellipse and 1:2 figure-8 Lissajous patterns on green graticule screen."
        }),
        # Page 13
        (13, "Knowledge Check: Energy Conservation", "knowledge_check", "knowledge_check", 1, {
            "question": "If the accelerating anode voltage of an electron gun is quadrupled (multiplied by 4), the velocity of the electrons:",
            "options": ["Doubles (multiplied by 2)", "Quadruples (multiplied by 4)", "Remains unchanged", "Halves"],
            "answer": "Doubles (multiplied by 2)",
            "explanation": "Velocity v = sqrt(2eV/m_e) is proportional to the square root of voltage V. Therefore, sqrt(4) = 2."
        }),
        (13, "Knowledge Check: RMS Voltage", "knowledge_check", "knowledge_check", 2, {
            "question": "A CRO trace displays a peak voltage of 14.14 V. What is the equivalent RMS voltage?",
            "options": ["10.0 V", "14.14 V", "20.0 V", "7.07 V"],
            "answer": "10.0 V",
            "explanation": "V_rms = V_0 / sqrt(2) = 14.14 / 1.414 = 10.0 V."
        }),
        # Page 14
        (14, "Module Summary", "summary", "summary", 1, {
            "text": "### Topic Summary:\n- **Energy Conservation**: $eV = \\frac{1}{2} m_e v^2 \\implies v = \\sqrt{\\frac{2eV}{m_e}}$.\n- **CRO Metrics**: $V_0 = h \\times Y_{\\text{gain}}$, $T = d \\times TB$, $f = \\frac{1}{T}$.\n- **Diagnostics**: CRO measures peak voltage, frequency, period, phase shift, and Lissajous figures with zero current loading."
        }),
        (15, "Module Summary", "key_takeaway", "key_takeaway", 2, {
            "text": "Topic 7 Complete: Cathode rays combine thermionic emission, high vacuum electrodynamics, and CRO diagnostics into a cornerstone of modern electronics."
        })
    ]

    for p_num, title, btype, ctype, order, content in blocks_m73:
        LessonBlock.objects.create(
            lesson=lesson_3,
            page_number=p_num,
            page_title=title,
            title=title,
            block_type=btype,
            component_type=ctype,
            component_order=order,
            order=p_num * 10 + order,
            content=content
        )
    print(f"  Lesson 3 populated with {lesson_3.blocks.count()} blocks across 15 pages.\n")

    print("=" * 80)
    print("TOPIC 7 INGESTION COMPLETED SUCCESSFULLY!")
    print("=" * 80)

if __name__ == "__main__":
    run_ingestion()
