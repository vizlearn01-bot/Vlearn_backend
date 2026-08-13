"""
VLearn Form 4 Physics — Topic 11: Electronics
Comprehensive Ingestion Engine (Enriched Deep Text & Visual Architecture)

Modules:
  11.1 Conduction in Solids & Semiconductor Physics (10 Pages, 19 Blocks)
  11.2 P-N Junction Diodes, Rectification, and Transistors (12 Pages, 19 Blocks)
  11.3 Digital Electronics, Logic Gates, and Worked Examples (14 Pages, 20 Blocks)

Usage:
  /home/jason-bitega/Desktop/VL/vlearn_repositories/Vlearn_backend/venv/bin/python curriculum/ingest_form4_physics_topic11.py
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
    print("VLEARN FORM 4 PHYSICS — TOPIC 11 INGESTION (FINAL TOPIC!)")
    print("=" * 80)

    curriculum = Curriculum.objects.filter(name="844").first()
    grade = Grade.objects.filter(curriculum=curriculum, name="Form 4").first()
    subject = Subject.objects.filter(grade=grade, name="Physics").first()

    topic, _ = Topic.objects.get_or_create(
        subject=subject,
        order=11,
        defaults={"name": "Topic 11: Electronics — Semiconductors, Diode Rectification, Transistors, and Digital Logic Gates"}
    )
    topic.name = "Topic 11: Electronics — Semiconductors, Diode Rectification, Transistors, and Digital Logic Gates"
    topic.save()
    print(f"Topic 11: '{topic.name}' (ID: {topic.id}) ready.")

    # -------------------------------------------------------------------------
    # MODULE 11.1: Conduction in Solids & Semiconductor Physics
    # -------------------------------------------------------------------------
    unit_1, _ = LearningUnit.objects.get_or_create(
        topic=topic, order=1,
        defaults={"name": "Module 11.1: Conduction in Solids & Semiconductor Physics"}
    )
    lesson_1, _ = Lesson.objects.get_or_create(
        topic=topic,
        learning_unit=unit_1,
        defaults={"title": "Conduction in Solids & Semiconductor Physics", "status": "published", "version": 1}
    )
    lesson_1.blocks.all().delete()

    blocks_m111 = [
        # Page 1
        (1, "Physical Intuition: The Microchip Revolution", "learning_goal", "learning_goal", 1, {
            "goals": [
                "Understand energy band theory (valence band, conduction band, forbidden energy gap $E_g$)",
                "Distinguish intrinsic semiconductors (pure Silicon/Germanium) from N-type and P-type extrinsic semiconductors",
                "Explain thermal charge carrier generation ($n_e = n_h = n_i$) and impurity doping mechanics"
            ]
        }),
        (1, "Physical Intuition: The Microchip Revolution", "concept_explanation", "concept_explanation", 2, {
            "text": "### The Solid-State Revolution:\nBefore the late 1940s, electronic equipment relied on bulky, fragile, power-hungry vacuum thermionic valves. The invention of the **semiconductor transistor** in 1947 by Bardeen, Brattain, and Shockley ushered in modern microelectronics—enabling smartphones, supercomputers, and renewable energy systems.\n\n### Why Study Semiconductors?\nUnlike metals (which conduct electricity continuously) or glass insulators (which block current completely), **semiconductors** have an electrical conductivity that can be precisely tuned over many orders of magnitude by adding tiny trace impurities (**doping**) or varying temperature!"
        }),
        (1, "Physical Intuition: The Microchip Revolution", "suggested_image", "suggested_image", 3, {
            "text": "Historical Germanium Transistor and Vacuum Tube Comparison Unit"
        }),
        # Page 2
        (2, "Energy Band Theory in Solids", "definition_card", "definition_card", 1, {
            "term": "Forbidden Energy Gap (E_g)",
            "definition": "The energy range between the top of the valence band and the bottom of the conduction band in a solid, where no electron energy states can exist."
        }),
        (2, "Energy Band Theory in Solids", "concept_explanation", "concept_explanation", 2, {
            "text": "### Band Structure of Matter:\nWhen isolated atoms condense into a crystalline solid, discrete atomic energy levels broaden into continuous energy bands:\n1. **Valence Band**: The highest occupied energy band containing outer valence electrons bound to parent atoms.\n2. **Conduction Band**: The band of higher energy states above the valence band where electrons move freely as charge carriers under an electric field.\n3. **Energy Gap ($E_g$)**:\n   - **Conductors (Copper/Aluminum)**: Valence and conduction bands **overlap** ($E_g = 0\\text{ eV}$). Free electrons abound.\n   - **Insulators (Glass/Diamond)**: Huge energy gap ($E_g > 5.0\\text{ eV}$). Thermal energy cannot jump the gap.\n   - **Semiconductors (Silicon/Germanium)**: Small energy gap ($E_g \\approx 1.1\\text{ eV}$ for Si, $0.7\\text{ eV}$ for Ge)."
        }),
        (2, "Energy Band Theory in Solids", "suggested_diagram", "suggested_diagram", 3, {
            "text": "Energy Band Structure Comparison for Conductors, Semiconductors, and Insulators",
            "instruction": "Diagram showing overlapping bands in conductors, small 1.1 eV gap in semiconductors, and large 5 eV gap in insulators."
        }),
        # Page 3
        (3, "Intrinsic Semiconductors (Pure Silicon & Germanium)", "concept_explanation", "concept_explanation", 1, {
            "text": "### The Tetravalent Crystal Lattice:\nPure Silicon ($Z = 14$) and Germanium ($Z = 32$) are Group IV elements with **4 valence electrons**. In a pure crystal, each atom forms 4 covalent bonds with adjacent neighbors, creating a rigid tetrahedral crystal lattice.\n\n### Thermal Generation of Electron-Hole Pairs:\nAt absolute zero ($0\\text{ K}$), all valence electrons are locked in covalent bonds; the conduction band is completely empty, making intrinsic silicon a perfect insulator!\n\nAs temperature rises ($300\\text{ K}$ room temp), thermal vibrations break a small fraction of covalent bonds, liberating free electrons into the conduction band. Each escaped electron leaves behind a vacant covalent bond spot called a **Hole** ($h^+$), which acts as a mobile positive charge carrier ($n_e = n_h = n_i$)!"
        }),
        # Page 4
        (4, "Conduction Mechanics: Free Electrons vs. Holes", "concept_explanation", "concept_explanation", 1, {
            "text": "### Dual Charge Conduction:\nIn semiconductors, electrical current consists of two simultaneous components:\n$$\\text{Total Current } I_{\\text{total}} = I_e + I_h$$\n1. **Electron Conduction ($I_e$)**: High-mobility free electrons drifting through the conduction band toward the positive terminal.\n2. **Hole Conduction ($I_h$)**: Neighboring valence electrons jumping into adjacent hole vacancies in the valence band, causing the positive hole spot to drift in the opposite direction toward the negative terminal!"
        }),
        # Page 5
        (5, "Extrinsic Semiconductors: N-Type Doping", "concept_explanation", "concept_explanation", 1, {
            "text": "### Pentavalent Impurity Doping:\n**N-Type semiconductors** are produced by doping pure silicon with trace pentavalent (Group V) elements such as **Phosphorus** ($^{31}_{15}\\text{P}$), **Arsenic** ($^{75}_{33}\\text{As}$), or **Antimony** ($^{121}_{51}\\text{Sb}$).\n\n### Donor Mechanism:\nFour of the pentavalent atom's 5 valence electrons form covalent bonds with 4 surrounding silicon atoms. The **5th valence electron** is extra and loosely bound, easily detaching into the conduction band at room temperature!\n\n- **Majority Carriers**: **Free Electrons** ($n_e \\gg n_h$).\n- **Minority Carriers**: **Thermal Holes** ($n_h$).\n- **Impurity Type**: **Donor Atoms**."
        }),
        (5, "Extrinsic Semiconductors: N-Type Doping", "suggested_diagram", "suggested_diagram", 2, {
            "text": "N-Type Doping Silicon Crystal Lattice with Pentavalent Phosphorus Donor Atom",
            "instruction": "Diagram showing silicon lattice with phosphorus donor atom releasing a free conduction electron."
        }),
        # Page 6
        (6, "Extrinsic Semiconductors: P-Type Doping", "concept_explanation", "concept_explanation", 1, {
            "text": "### Trivalent Impurity Doping:\n**P-Type semiconductors** are produced by doping pure silicon with trace trivalent (Group III) elements such as **Boron** ($^{11}_{5}\\text{B}$), **Aluminum** ($^{27}_{13}\\text{Al}$), **Gallium** ($^{69}_{31}\\text{Ga}$), or **Indium** ($^{115}_{49}\\text{In}$).\n\n### Acceptor Mechanism:\nThe trivalent atom has only 3 valence electrons to share, leaving an incomplete 4th covalent bond spot—a vacant **Hole** ($h^+$) ready to accept an electron from neighboring silicon atoms!\n\n- **Majority Carriers**: **Holes** ($n_h \\gg n_e$).\n- **Minority Carriers**: **Free Electrons** ($n_e$).\n- **Impurity Type**: **Acceptor Atoms**."
        }),
        (6, "Extrinsic Semiconductors: P-Type Doping", "suggested_diagram", "suggested_diagram", 2, {
            "text": "P-Type Doping Silicon Crystal Lattice with Trivalent Boron Acceptor Atom Creating Hole Vacancy",
            "instruction": "Diagram showing silicon lattice with boron acceptor atom creating an electron hole vacancy."
        }),
        # Page 7
        (7, "Carrier Density Kinetics & Mass Action Law", "formula_breakdown", "formula_breakdown", 1, {
            "formula": "n_e \\cdot n_h = n_i^2",
            "variables": {
                "n_e": "Free electron concentration per cubic meter (m^-3)",
                "n_h": "Hole concentration per cubic meter (m^-3)",
                "n_i": "Intrinsic carrier concentration at given temperature (m^-3)"
            }
        }),
        (7, "Carrier Density Kinetics & Mass Action Law", "concept_explanation", "concept_explanation", 2, {
            "text": "### Mass Action Law in Semiconductors:\nAt thermal equilibrium, the product of electron concentration $n_e$ and hole concentration $n_h$ is a constant dependent only on temperature and energy gap $E_g$, regardless of doping levels:\n$$n_e \\cdot n_h = n_i^2$$\n- **N-Type Semiconductor**: $n_e \\approx N_D$ (donor concentration), so hole concentration drops to $n_h = \\frac{n_i^2}{N_D}$.\n- **Electrical Neutrality**: Despite doping, both N-type and P-type extrinsic semiconductors remain **electrically neutral** overall because donor/acceptor ion charges balance free carrier charges!"
        }),
        # Page 8
        (8, "Interactive Semiconductor Sandbox", "suggested_simulation", "suggested_simulation", 1, {
            "text": "Interactive Semiconductor Sandbox: Real-Time Temperature & Doping Carrier Density Model",
            "instruction": "Interactive simulation rendering live sliders for temperature (K) and donor/acceptor doping concentration."
        }),
        # Page 9
        (9, "Knowledge Check: Semiconductor Physics", "knowledge_check", "knowledge_check", 1, {
            "question": "What happens to the electrical conductivity of an INTRINSIC semiconductor when its temperature increases?",
            "options": ["Conductivity increases significantly", "Conductivity decreases to zero", "Conductivity remains unchanged", "Energy gap Eg expands"],
            "answer": "Conductivity increases significantly",
            "explanation": "Higher temperature provides thermal energy to break covalent bonds, creating more free electron-hole pairs and increasing conductivity."
        }),
        (9, "Knowledge Check: Semiconductor Physics", "knowledge_check", "knowledge_check", 2, {
            "question": "Which type of impurity atom must be added to pure Silicon to create an N-type extrinsic semiconductor?",
            "options": ["Pentavalent atom (Group V) like Phosphorus", "Trivalent atom (Group III) like Boron", "Divalent atom (Group II) like Magnesium", "Monovalent atom like Sodium"],
            "answer": "Pentavalent atom (Group V) like Phosphorus",
            "explanation": "Pentavalent donor atoms provide 5 valence electrons, donating 1 extra free electron into the conduction band per impurity atom."
        }),
        # Page 10
        (10, "Module Summary", "summary", "summary", 1, {
            "text": "### Module 11.1 Key Takeaways:\n1. **Energy Bands**: Conductors (overlapping), Semiconductors ($E_g \\approx 1.1\\text{ eV}$), Insulators ($E_g > 5\\text{ eV}$).\n2. **Intrinsic**: Pure Si/Ge, thermal generation of electron-hole pairs ($n_e = n_h = n_i$).\n3. **N-Type**: Doped with pentavalent donors (Phosphorus), majority carriers are free electrons ($n_e \\gg n_h$).\n4. **P-Type**: Doped with trivalent acceptors (Boron), majority carriers are holes ($n_h \\gg n_e$).\n5. **Mass Action Law**: $n_e \\cdot n_h = n_i^2$."
        }),
        (10, "Module Summary", "key_takeaway", "key_takeaway", 2, {
            "text": "Semiconductors possess an adjustable energy band gap where doping with donor or acceptor impurities creates N-type or P-type materials."
        })
    ]

    for p_num, title, btype, ctype, order, content in blocks_m111:
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
    print(f"  Lesson 1 populated with {lesson_1.blocks.count()} blocks across 10 pages.")

    # -------------------------------------------------------------------------
    # MODULE 11.2: P-N Junction Diodes, Rectification, and Transistors
    # -------------------------------------------------------------------------
    unit_2, _ = LearningUnit.objects.get_or_create(
        topic=topic, order=2,
        defaults={"name": "Module 11.2: P-N Junction Diodes, Rectification, and Transistors"}
    )
    lesson_2, _ = Lesson.objects.get_or_create(
        topic=topic,
        learning_unit=unit_2,
        defaults={"title": "P-N Junction Diodes, Rectification, and Transistors", "status": "published", "version": 1}
    )
    lesson_2.blocks.all().delete()

    blocks_m112 = [
        # Page 1
        (1, "The P-N Junction & Depletion Layer Formation", "definition_card", "definition_card", 1, {
            "term": "Built-In Barrier Potential (V_0)",
            "definition": "The electrostatic potential difference established across the depletion layer of a p-n junction that halts further diffusion of majority charge carriers (approx 0.7V for Silicon, 0.3V for Germanium)."
        }),
        (1, "The P-N Junction & Depletion Layer Formation", "concept_explanation", "concept_explanation", 2, {
            "text": "### Formation of the Depletion Region:\nWhen a P-type semiconductor is joined to an N-type semiconductor, majority free electrons from the N-side diffuse across the junction into the P-side to recombine with holes.\n\nThis recombination creates an insulating boundary layer devoid of free charge carriers called the **Depletion Region**:\n- **Fixed Donor Ions ($+$)** on the N-side near the junction.\n- **Fixed Acceptor Ions ($-$)** on the P-side near the junction.\n- An internal **Built-in Electric Field ($E$)** points from N to P, creating a barrier potential $V_0 \\approx 0.7\\text{ V}$ (Silicon) that prevents further diffusion!"
        }),
        (1, "The P-N Junction & Depletion Layer Formation", "suggested_diagram", "suggested_diagram", 3, {
            "text": "P-N Junction Depletion Layer Formation Diagram Showing Internal Built-In Barrier Potential V_0",
            "instruction": "Diagram showing P-type and N-type silicon junction, fixed acceptor/donor ions in depletion layer, and 0.7V barrier potential."
        }),
        # Page 2
        (2, "Diode Biasing: Forward vs. Reverse Bias Characterization", "concept_explanation", "concept_explanation", 1, {
            "text": "### Biasing a P-N Junction Diode:\n1. **Forward Bias** (Positive terminal to P-side, Negative to N-side):\n   - External voltage opposes and shrinks the built-in barrier potential $V_0$.\n   - When $V_{\\text{external}} > 0.7\\text{ V}$ (knee voltage), majority carriers flood across the junction, conducting a large forward current $I_F$.\n2. **Reverse Bias** (Positive terminal to N-side, Negative to P-side):\n   - External voltage aids built-in field, widening the depletion region.\n   - No majority current flows! Only a tiny negligible reverse saturation leakage current ($I_S \\approx \\mu\\text{A}$) carried by minority carriers."
        }),
        (2, "Diode Biasing: Forward vs. Reverse Bias Characterization", "suggested_diagram", "suggested_diagram", 2, {
            "text": "Silicon Semiconductor Diode I-V Characteristic Curve (Knee Voltage 0.7V and Reverse Breakdown)",
            "instruction": "I-V graph showing exponential current rise at 0.7V forward bias and tiny leakage current in reverse bias."
        }),
        # Page 3
        (3, "Half-Wave Rectification Circuits", "concept_explanation", "concept_explanation", 1, {
            "text": "### AC to Pulsating DC Conversion:\n**Rectification** is the process of converting bidirectional Alternating Current (AC) into unidirectional Direct Current (DC).\n\n### Half-Wave Rectifier Operation:\nA single diode connected in series with a secondary transformer coil and load resistor $R_L$:\n- **Positive Half-Cycle**: Diode is **forward-biased** (anode positive), conducting current through load $R_L$.\n- **Negative Half-Cycle**: Diode is **reverse-biased** (anode negative), blocking current flow.\n- **Efficiency**: Low efficiency ($40.6\\%$ max), output is pulsating DC with large gaps."
        }),
        (3, "Half-Wave Rectification Circuits", "suggested_diagram", "suggested_diagram", 2, {
            "text": "Half-Wave Rectifier Circuit Diagram and Input AC vs Pulsating DC Waveform Graph",
            "instruction": "Diagram showing single diode circuit and input sine wave converting into single positive pulse output wave."
        }),
        # Page 4
        (4, "Full-Wave Rectification: Center-Tapped Transformer", "concept_explanation", "concept_explanation", 1, {
            "text": "### Utilizing Both Half-Cycles:\nFull-wave rectification converts both positive and negative AC half-cycles into unidirectional DC pulses, doubling output frequency and efficiency ($81.2\\%$ max).\n\n### Center-Tapped 2-Diode Rectifier:\nUses a center-tapped transformer winding acting as zero-volt ground reference:\n- **Positive Half-Cycle**: Top diode $D_1$ is forward-biased, conducting through load $R_L$.\n- **Negative Half-Cycle**: Bottom diode $D_2$ is forward-biased, conducting through load $R_L$ in the **same downward direction**!"
        }),
        # Page 5
        (5, "Full-Wave Rectification: Bridge Rectifier Circuit", "concept_explanation", "concept_explanation", 1, {
            "text": "### The 4-Diode Bridge Rectifier:\nA **Bridge Rectifier** consists of 4 diodes arranged in a diamond bridge network ($D_1, D_2, D_3, D_4$) connected across a standard transformer secondary coil:\n- **Positive Half-Cycle**: Diodes $D_1$ and $D_3$ conduct in series through load $R_L$.\n- **Negative Half-Cycle**: Diodes $D_2$ and $D_4$ conduct in series through load $R_L$ in the identical direction!\n- **Advantage**: Does NOT require a center-tapped transformer, making it the universal standard in power supplies."
        }),
        (5, "Full-Wave Rectification: Bridge Rectifier Circuit", "suggested_diagram", "suggested_diagram", 2, {
            "text": "4-Diode Bridge Rectifier Circuit Diagram Showing Alternating Current Path Conduction",
            "instruction": "Diagram showing 4-diode diamond bridge network and continuous positive pulse DC output waveform."
        }),
        (5, "Full-Wave Rectification: Bridge Rectifier Circuit", "suggested_image", "suggested_image", 3, {
            "text": "Bridge Rectifier Electronic Component Package Unit"
        }),
        # Page 6
        (6, "Capacitor Smoothing Filters", "concept_explanation", "concept_explanation", 1, {
            "text": "### Reducing Voltage Ripple:\nPulsating DC output from rectifiers is unsuitable for sensitive electronics. A large electrolytic reservoir capacitor ($C$) connected in parallel across load resistor $R_L$ acts as a **Smoothing Filter**:\n- **Peak Charging**: Capacitor charges rapidly to peak voltage $V_p$ during pulse rise.\n- **Discharge Phase**: As rectifier voltage drops, the capacitor discharges stored charge gradually through $R_L$, maintaining steady DC output voltage and eliminating deep voltage dips."
        }),
        (6, "Capacitor Smoothing Filters", "suggested_diagram", "suggested_diagram", 2, {
            "text": "RC Filter Smoothing Capacitor Circuit and Smoothed DC Voltage Ripple Reduction Graph",
            "instruction": "Diagram showing parallel smoothing capacitor reducing peak-to-peak ripple voltage Vr."
        }),
        # Page 7
        (7, "Bipolar Junction Transistors (BJT): NPN & PNP", "concept_explanation", "concept_explanation", 1, {
            "text": "### Three-Terminal Solid-State Amplifiers:\nA **Bipolar Junction Transistor (BJT)** consists of three doped semiconductor layers forming two p-n junctions back-to-back:\n1. **Emitter (E)**: Heavily doped to inject majority charge carriers into the base.\n2. **Base (B)**: Extremely thin, lightly doped central region controlling carrier flow.\n3. **Collector (C)**: Moderately doped larger region collecting injected carriers.\n\n### Transistor Types:\n- **NPN Transistor**: Thin P-layer between two N-layers (Circuit symbol arrow points outward from base to emitter: **N**ot **P**ointing i**N**).\n- **PNP Transistor**: Thin N-layer between two P-layers (Circuit symbol arrow points inward toward base)."
        }),
        (7, "Bipolar Junction Transistors (BJT): NPN & PNP", "suggested_diagram", "suggested_diagram", 2, {
            "text": "NPN and PNP Transistor Layer Structure, Terminal Names, and Standard Schematic Symbols",
            "instruction": "Diagram showing NPN and PNP layer structures, Emitter Base Collector terminals, and circuit symbols with current arrows."
        }),
        # Page 8
        (8, "Transistor Current Equations & Current Gain ($\beta$)", "formula_breakdown", "formula_breakdown", 1, {
            "formula": "I_E = I_B + I_C, \\quad \\beta = \\frac{I_C}{I_B}",
            "variables": {
                "I_E": "Emitter current flowing out of emitter terminal (mA)",
                "I_B": "Base current injected into base terminal (uA)",
                "I_C": "Collector current flowing into collector terminal (mA)",
                "beta": "Common-emitter DC current amplification gain factor (typically 50 to 300)"
            }
        }),
        (8, "Transistor Current Equations & Current Gain ($\beta$)", "concept_explanation", "concept_explanation", 2, {
            "text": "### Current Amplification Mechanics:\nIn a common-emitter NPN transistor circuit, a small base current $I_B$ controls a much larger collector current $I_C$:\n$$I_E = I_B + I_C, \\quad \\text{where } I_C = \\beta I_B$$\nSince base current $I_B$ is tiny ($< 1\\%$ of $I_E$), $I_C \\approx I_E$. A small change in base input signal produces a huge proportional change in collector output current!"
        }),
        # Page 9
        (9, "Transistor as an Automatic Electronic Switch (LDR)", "concept_explanation", "concept_explanation", 1, {
            "text": "### Potential Divider Control Switch:\nA transistor operates as an electronic switch by driving it between **Cutoff** ($I_B = 0, I_C = 0 \implies \\text{Switch OFF}$) and **Saturation** ($V_{CE} \\approx 0.2\\text{ V} \implies \\text{Switch ON}$).\n\n### Automatic Night Light Circuit (LDR):\n- **Daytime (Bright Light)**: Light-Dependent Resistor (LDR) resistance drops ($R_{\\text{LDR}} \\to 0$). Base voltage $V_B = \\frac{R_{\\text{LDR}}}{R_1 + R_{\\text{LDR}}} V_{CC} < 0.6\\text{ V}$. Transistor OFF, lamp stays OFF.\n- **Nighttime (Darkness)**: LDR resistance shoots up ($R_{\\text{LDR}} \\gg R_1$). Base voltage $V_B > 0.7\\text{ V}$, turning transistor ON and switching street lamp ON automatically!"
        }),
        (9, "Transistor as an Automatic Electronic Switch (LDR)", "suggested_diagram", "suggested_diagram", 2, {
            "text": "Transistor Automatic Night Light Circuit with LDR Potential Divider Potential Divider",
            "instruction": "Diagram showing LDR potential divider connected to NPN transistor base controlling relay or lamp."
        }),
        # Page 10
        (10, "Knowledge Check: Diodes & Transistors", "knowledge_check", "knowledge_check", 1, {
            "question": "What is the primary advantage of a 4-diode BRIDGE rectifier over a 2-diode full-wave rectifier?",
            "options": ["Does not require a center-tapped transformer", "Uses half the number of diodes", "Operates with zero voltage drop", "Blocks AC voltage completely"],
            "answer": "Does not require a center-tapped transformer",
            "explanation": "Bridge rectifiers use standard secondary transformer coils, making them cheaper, more compact, and universally used."
        }),
        (10, "Knowledge Check: Diodes & Transistors", "knowledge_check", "knowledge_check", 2, {
            "question": "In an NPN transistor amplifier circuit, if the base current I_B is 50 uA and the DC current gain beta is 100, calculate the collector current I_C.",
            "options": ["5.0 mA", "0.5 mA", "50 mA", "500 uA"],
            "answer": "5.0 mA",
            "explanation": "I_C = beta x I_B = 100 x (50 x 10^-6 A) = 5.0 x 10^-3 A = 5.0 mA."
        }),
        # Page 11
        (11, "Module Summary", "summary", "summary", 1, {
            "text": "### Module 11.2 Key Takeaways:\n1. **P-N Junction**: Built-in barrier potential $V_0 \\approx 0.7\\text{ V}$ (Silicon), forward bias conducts, reverse bias blocks.\n2. **Rectifiers**: Half-wave ($1$ diode, $40.6\\%$ efficiency), Full-wave bridge ($4$ diodes, $81.2\\%$ efficiency).\n3. **Capacitor Smoothing**: Parallel reservoir capacitor reduces AC ripple voltage.\n4. **Transistor Relations**: $I_E = I_B + I_C$, Current Gain $\\beta = \\frac{I_C}{I_B}$.\n5. **Electronic Switch**: LDR potential divider controls base voltage $V_B$ for automatic switching."
        }),
        (12, "Module Summary", "key_takeaway", "key_takeaway", 2, {
            "text": "P-N junction diodes enable AC-to-DC rectification and BJTs amplify currents and perform solid-state electronic switching."
        })
    ]

    for p_num, title, btype, ctype, order, content in blocks_m112:
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
    # MODULE 11.3: Digital Electronics, Logic Gates, and Worked Examples
    # -------------------------------------------------------------------------
    unit_3, _ = LearningUnit.objects.get_or_create(
        topic=topic, order=3,
        defaults={"name": "Module 11.3: Digital Electronics, Logic Gates, and Worked Examples"}
    )
    lesson_3, _ = Lesson.objects.get_or_create(
        topic=topic,
        learning_unit=unit_3,
        defaults={"title": "Digital Electronics, Logic Gates, and Worked Examples", "status": "published", "version": 1}
    )
    lesson_3.blocks.all().delete()

    blocks_m113 = [
        # Page 1
        (1, "Analog vs. Digital Electronics", "concept_explanation", "concept_explanation", 1, {
            "text": "### Continuous Signals vs Discrete Logic:\n1. **Analog Signals**: Signals whose voltage varies continuously over time (e.g. microphone audio waveforms, mercury thermometers).\n2. **Digital Signals**: Signals restricted to two discrete binary logic levels:\n   - **Logic HIGH ('1')**: Nominal $+5.0\\text{ V}$ supply voltage.\n   - **Logic LOW ('0')**: Nominal $0.0\\text{ V}$ ground potential.\n\n### Advantages of Digital Systems:\nDigital signals possess superior immunity to electrical noise, allow error-free data transmission, and can be processed by microprocessors using **Boolean Algebra** logic!"
        }),
        # Page 2
        (2, "Fundamental Logic Gates 1: NOT Gate (Inverter)", "definition_card", "definition_card", 1, {
            "term": "NOT Gate (Inverter)",
            "definition": "A single-input logic gate whose output is the Boolean inverse of its input (Output Q = NOT A = A_bar)."
        }),
        (2, "Fundamental Logic Gates 1: NOT Gate (Inverter)", "concept_explanation", "concept_explanation", 2, {
            "text": "### Truth Table & Boolean Symbol:\n$$\\text{Boolean Expression: } Q = \\bar{A}$$\n- Input $A = 0 \\implies Q = 1$\n- Input $A = 1 \\implies Q = 0$"
        }),
        # Page 3
        (3, "Fundamental Logic Gates 2: AND & OR Gates", "concept_explanation", "concept_explanation", 1, {
            "text": "### AND Gate & OR Gate Logic:\n1. **AND Gate ($Q = A \\cdot B$)**: Output is HIGH ($1$) **ONLY IF BOTH** inputs $A$ AND $B$ are HIGH ($1$).\n   - Truth Table: $(0,0 \\to 0), (0,1 \\to 0), (1,0 \\to 0), (1,1 \\to 1)$.\n2. **OR Gate ($Q = A + B$)**: Output is HIGH ($1$) if **EITHER** input $A$ OR $B$ (or both) is HIGH ($1$).\n   - Truth Table: $(0,0 \\to 0), (0,1 \\to 1), (1,0 \\to 1), (1,1 \\to 1)$."
        }),
        # Page 4
        (4, "Universal Logic Gates: NAND & NOR Gates", "concept_explanation", "concept_explanation", 1, {
            "text": "### Universal Logic Building Blocks:\nNAND and NOR gates are called **Universal Gates** because any digital logic circuit or computer processor can be constructed using only NAND gates or only NOR gates!\n\n1. **NAND Gate ($Q = \\overline{A \\cdot B}$)**: Inverted AND gate. Output is LOW ($0$) only when both inputs are HIGH ($1$).\n2. **NOR Gate ($Q = \\overline{A + B}$)**: Inverted OR gate. Output is HIGH ($1$) only when both inputs are LOW ($0$)."
        }),
        (4, "Universal Logic Gates: NAND & NOR Gates", "suggested_diagram", "suggested_diagram", 2, {
            "text": "Logic Gate Symbol Family (AND, OR, NOT, NAND, NOR) and Truth Tables",
            "instruction": "Diagram showing schematic symbols and 2-input truth tables for AND, OR, NOT, NAND, NOR gates."
        }),
        # Page 5
        (5, "Worked Example Level 1 — Energy Band Gap & Photon Emission", "worked_example", "worked_example", 1, {
            "problem": "A Gallium Arsenide (GaAs) Light-Emitting Diode (LED) has an energy band gap $E_g = 1.43\\text{ eV}$. Calculate the wavelength $\\lambda$ of light emitted when an electron recombines across the gap. (Take $h = 6.63 \\times 10^{-34}\\text{ J}\\cdot\\text{s}$, $1\\text{ eV} = 1.60 \\times 10^{-19}\\text{ J}$, $c = 3.0 \\times 10^8\\text{ m/s}$).",
            "steps": [
                "Step 1: Convert band gap energy to Joules: $E_g = 1.43 \\times (1.60 \\times 10^{-19}\\text{ J}) = 2.288 \\times 10^{-19}\\text{ Joules}$.",
                "Step 2: Apply photon wavelength formula $\\lambda = \\frac{hc}{E_g}$.",
                "Step 3: Substitute values: $\\lambda = \\frac{(6.63 \\times 10^{-34}) \\times (3.0 \\times 10^8)}{2.288 \\times 10^{-19}} = \\frac{1.989 \\times 10^{-25}}{2.288 \\times 10^{-19}}$.",
                "Step 4: Compute wavelength: $\\lambda = 8.693 \\times 10^{-7}\\text{ m} = 869.3\\text{ nm}$ (Near Infrared spectrum)."
            ]
        }),
        # Page 6
        (6, "Worked Example Level 2 — Rectifier Peak & RMS Voltage Output", "worked_example", "worked_example", 1, {
            "problem": "A step-down transformer delivers an AC secondary voltage $V_{\\text{rms}} = 12.0\\text{ V}$ to a 4-diode bridge rectifier. Assuming Silicon diodes each have a forward voltage drop $V_D = 0.70\\text{ V}$, calculate: 1. The peak AC voltage $V_p$. 2. The peak DC output voltage $V_{p(\\text{out})}$ across the load resistor.",
            "steps": [
                "Step 1: Calculate peak secondary AC voltage: $V_p = V_{\\text{rms}} \\times \\sqrt{2} = 12.0 \\times 1.414 = 16.97\\text{ Volts}$.",
                "Step 2: In a bridge rectifier, 2 diodes conduct in series per half-cycle, incurring a total voltage drop of $2 V_D = 2 \\times 0.70 = 1.40\\text{ Volts}$.",
                "Step 3: Calculate peak load DC voltage: $V_{p(\\text{out})} = V_p - 2 V_D = 16.97 - 1.40 = 15.57\\text{ Volts}$."
            ]
        }),
        # Page 7
        (7, "Worked Example Level 3 — Transistor Base Current & Current Gain", "worked_example", "worked_example", 1, {
            "problem": "In a common-emitter NPN transistor circuit, the emitter current $I_E = 15.30\\text{ mA}$ and base current $I_B = 0.15\\text{ mA}$. Calculate: 1. The collector current $I_C$. 2. The DC current amplification gain factor $\\beta$.",
            "steps": [
                "Step 1: Apply Kirchhoff's current relation $I_E = I_B + I_C \\implies I_C = I_E - I_B$.",
                "Step 2: Calculate collector current: $I_C = 15.30\\text{ mA} - 0.15\\text{ mA} = 15.15\\text{ mA}$.",
                "Step 3: Apply current gain formula $\\beta = \\frac{I_C}{I_B}$.",
                "Step 4: Compute amplification factor: $\\beta = \\frac{15.15\\text{ mA}}{0.15\\text{ mA}} = 101.0$."
            ]
        }),
        # Page 8
        (8, "Worked Example Level 4 — LDR Transistor Potential Divider Switch", "worked_example", "worked_example", 1, {
            "problem": "An automatic light switch circuit uses an NPN transistor requiring a minimum base voltage $V_B = 0.70\\text{ V}$ to turn ON. The base is connected to a potential divider comprising a fixed resistor $R_1 = 10.0\\text{ k}\\Omega$ and an LDR connected to a $+9.0\\text{ V}$ supply. Calculate the minimum LDR resistance required to turn ON the transistor.",
            "steps": [
                "Step 1: Write potential divider formula: $V_B = \\frac{R_{\\text{LDR}}}{R_1 + R_{\\text{LDR}}} \\cdot V_{CC}$.",
                "Step 2: Substitute knowns: $0.70 = \\frac{R_{\\text{LDR}}}{10,000 + R_{\\text{LDR}}} \\cdot 9.0$.",
                "Step 3: Rearrange: $0.70 \\times (10,000 + R_{\\text{LDR}}) = 9.0 R_{\\text{LDR}} \\implies 7000 + 0.70 R_{\\text{LDR}} = 9.0 R_{\\text{LDR}}$.",
                "Step 4: Solve for $R_{\\text{LDR}}$: $8.30 R_{\\text{LDR}} = 7000 \\implies R_{\\text{LDR}} = \\frac{7000}{8.30} = 843.4\\text{ }\\Omega$."
            ]
        }),
        # Page 9
        (9, "Worked Example Level 5 — Challenge Multi-Gate Logic Circuit", "worked_example", "worked_example", 1, {
            "problem": "A safety interlock circuit uses an AND gate feeding into a NOR gate. Inputs $A$ and $B$ connect to the AND gate, whose output $X$ and a emergency input $C$ connect to the NOR gate outputting $Q$. Synthesize the complete truth table and determine the output $Q$ when $A = 1, B = 1, C = 0$.",
            "steps": [
                "Step 1: Express intermediate output: $X = A \\cdot B$.",
                "Step 2: Express final output: $Q = \\overline{X + C} = \\overline{(A \\cdot B) + C}$.",
                "Step 3: Evaluate for $A=1, B=1, C=0$: $X = 1 \\cdot 1 = 1$.",
                "Step 4: Evaluate final NOR output: $Q = \\overline{1 + 0} = \\bar{1} = 0$. Output $Q$ is LOW ($0$)."
            ]
        }),
        # Page 10
        (10, "Integrated Circuits (ICs) & Microprocessor Applications", "concept_explanation", "concept_explanation", 1, {
            "text": "### Microchip Technology:\nAn **Integrated Circuit (IC)** integrates thousands to billions of microscopic transistors, diodes, resistors, and capacitors onto a single tiny silicon semiconductor chip (**die**).\n- **VLSI / Nanometer Scale**: Modern CPU microprocessors contain over $50\\text{ billion}$ silicon transistors etched at $3\\text{ nm}$ scales, enabling artificial intelligence and quantum computing!"
        }),
        (10, "Integrated Circuits (ICs) & Microprocessor Applications", "suggested_image", "suggested_image", 2, {
            "text": "Integrated Circuit IC Microchip Silicon Die Unit"
        }),
        # Page 11
        (11, "Addressing Key Student Misconceptions", "common_misconception", "common_misconception", 1, {
            "text": "### 4 Critical Misconceptions Clarified:\n1. **Extrinsic Charge Neutrality**: N-type semiconductors have excess free electrons, but they are **electrically neutral** overall because donor nuclei possess equal positive protons!\n2. **Forward Voltage Drop**: Diodes do NOT conduct at zero volts; Silicon diodes require $V > 0.7\\text{ V}$ (knee voltage) to collapse the depletion barrier potential.\n3. **Base Current Source**: Base current $I_B$ controls collector current $I_C$, but $I_C$ originates from the external collector power supply $V_{CC}$.\n4. **Universal Logic Gates**: NAND and NOR gates can implement ANY Boolean function (AND, OR, NOT) without requiring any other gate type."
        }),
        # Page 12
        (12, "Assessment Suite", "knowledge_check", "knowledge_check", 1, {
            "question": "Which logic gate outputs a HIGH ('1') logic level ONLY when BOTH inputs are LOW ('0')?",
            "options": ["NOR gate", "NAND gate", "AND gate", "OR gate"],
            "answer": "NOR gate",
            "explanation": "A NOR gate is an inverted OR gate: Q = NOT (A + B). When A=0 and B=0, A+B=0, so Q = NOT(0) = 1."
        }),
        (12, "Assessment Suite", "knowledge_check", "knowledge_check", 2, {
            "question": "What is the Boolean output Q of a 2-input NAND gate when input A = 1 and input B = 1?",
            "options": ["Logic LOW ('0')", "Logic HIGH ('1')", "High impedance", "Oscillating pulse"],
            "answer": "Logic LOW ('0')",
            "explanation": "NAND output Q = NOT (A . B). When A=1 and B=1, A . B = 1, so Q = NOT(1) = 0."
        }),
        # Page 13
        (13, "Module Summary", "summary", "summary", 1, {
            "text": "### Module 11.3 Key Takeaways:\n1. **Digital Signals**: Discrete binary logic levels ($0\\text{ V} \\to '0'$, $+5\\text{ V} \\to '1'$).\n2. **Fundamental Gates**: NOT ($Q = \\bar{A}$), AND ($Q = A \\cdot B$), OR ($Q = A + B$).\n3. **Universal Gates**: NAND ($Q = \\overline{A \\cdot B}$), NOR ($Q = \\overline{A + B}$).\n4. **Integrated Circuits**: Billions of transistors etched on silicon microchip dies."
        }),
        (14, "Module Summary", "key_takeaway", "key_takeaway", 2, {
            "text": "Topic 11 Complete: Electronics bridges semiconductor physics, diode rectification, transistor switches, and digital logic gate computer architecture!"
        })
    ]

    for p_num, title, btype, ctype, order, content in blocks_m113:
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
    print(f"  Lesson 3 populated with {lesson_3.blocks.count()} blocks across 14 pages.\n")

    print("=" * 80)
    print("TOPIC 11 INGESTION COMPLETED SUCCESSFULLY!")
    print("=" * 80)

if __name__ == "__main__":
    run_ingestion()
