"""
VLearn Form 4 Physics — Topic 10: Radioactivity
Comprehensive Ingestion Engine (Enriched Deep Text & Visual Architecture)

Modules:
  10.1 Nuclear Structure and Radiations (Alpha, Beta, Gamma) (10 Pages, 19 Blocks)
  10.2 Radioactive Decay Equations, Half-Life Kinetics, and Dating (12 Pages, 20 Blocks)
  10.3 Nuclear Energy (Fission vs Fusion), Hazards, and Worked Examples (14 Pages, 19 Blocks)

Usage:
  /home/jason-bitega/Desktop/VL/vlearn_repositories/Vlearn_backend/venv/bin/python curriculum/ingest_form4_physics_topic10.py
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
    print("VLEARN FORM 4 PHYSICS — TOPIC 10 INGESTION")
    print("=" * 80)

    curriculum = Curriculum.objects.filter(name="844").first()
    grade = Grade.objects.filter(curriculum=curriculum, name="Form 4").first()
    subject = Subject.objects.filter(grade=grade, name="Physics").first()

    topic, _ = Topic.objects.get_or_create(
        subject=subject,
        order=10,
        defaults={"name": "Topic 10: Radioactivity — Nuclear Physics, Half-Life Kinetics, and Fission/Fusion Applications"}
    )
    topic.name = "Topic 10: Radioactivity — Nuclear Physics, Half-Life Kinetics, and Fission/Fusion Applications"
    topic.save()
    print(f"Topic 10: '{topic.name}' (ID: {topic.id}) ready.")

    # -------------------------------------------------------------------------
    # MODULE 10.1: Nuclear Structure and Radiations (Alpha, Beta, Gamma)
    # -------------------------------------------------------------------------
    unit_1, _ = LearningUnit.objects.get_or_create(
        topic=topic, order=1,
        defaults={"name": "Module 10.1: Nuclear Structure and Radiations (Alpha, Beta, Gamma)"}
    )
    lesson_1, _ = Lesson.objects.get_or_create(
        topic=topic,
        learning_unit=unit_1,
        defaults={"title": "Nuclear Structure and Radiations (Alpha, Beta, Gamma)", "status": "published", "version": 1}
    )
    lesson_1.blocks.all().delete()

    blocks_m101 = [
        # Page 1
        (1, "Physical Intuition: Discovery of Radioactivity", "learning_goal", "learning_goal", 1, {
            "goals": [
                "Understand nuclear structure and standard nuclide notation $^{A}_{Z}\\text{X}$",
                "Compare alpha (\\$\\alpha\\$), beta (\\$\\beta^-\\$), and gamma (\\$\\gamma\\$) radiations by charge, mass, ionization, and penetration",
                "Explain the operating principles of gold-leaf electroscopes, cloud chambers, and Geiger-Müller (GM) detectors"
            ]
        }),
        (1, "Physical Intuition: Discovery of Radioactivity", "concept_explanation", "concept_explanation", 2, {
            "text": "### The Serendipitous Discovery (1896):\nIn 1896, French physicist Henri Becquerel wrapped uranium salts in thick black paper and stored them in a dark drawer alongside unexposed photographic plates. When he developed the plates, he was astonished to find dark fogged silhouettes of the uranium crystals! Becquerel realized that uranium spontaneously emits penetrating invisible rays without any external energy source.\n\n### Marie & Pierre Curie's Breakthrough:\nMarie Curie and her husband Pierre isolated two previously unknown radioactive elements—**Polonium** and **Radium**. Marie coined the term **Radioactivity** to describe the spontaneous disintegration of unstable atomic nuclei."
        }),
        (1, "Physical Intuition: Discovery of Radioactivity", "suggested_image", "suggested_image", 3, {
            "text": "Historical Becquerel Uranium Salt Photographic Plate Fogging Silhouette (1896)"
        }),
        # Page 2
        (2, "Atomic Structure & Nuclide Notation", "definition_card", "definition_card", 1, {
            "term": "Nuclide Notation (^{A}_{Z}X)",
            "definition": "A standard chemical shorthand representation of an atomic nucleus, where A is the nucleon (mass) number, Z is the proton (atomic) number, and X is the chemical symbol."
        }),
        (2, "Atomic Structure & Nuclide Notation", "concept_explanation", "concept_explanation", 2, {
            "text": "### Anatomy of the Atomic Nucleus:\nAt the center of an atom lies a tiny dense nucleus containing **protons** ($^{1}_{1}\\text{p}$) and **neutrons** ($^{1}_{0}\\text{n}$), collectively called **nucleons**.\n- **Atomic Number ($Z$)**: Total number of protons in the nucleus (defines element identity).\n- **Mass Number ($A$)**: Total number of protons + neutrons ($A = Z + N$).\n- **Isotopes**: Atoms of the same element having identical atomic number $Z$ but different mass numbers $A$ due to varying neutron count $N$ (e.g. Carbon-12 $^{12}_{6}\\text{C}$ vs radioactive Carbon-14 $^{14}_{6}\\text{C}$)."
        }),
        # Page 3
        (3, "Alpha ($\alpha$) Radiation Properties", "concept_explanation", "concept_explanation", 1, {
            "text": "### Nature of Alpha ($\alpha$) Particles:\nAn **alpha particle** is a fast-moving Helium nucleus consisting of 2 protons and 2 neutrons bound together ($^{4}_{2}\\text{He}$ or $^{4}_{2}\\alpha$).\n\n### Key Physical Properties:\n- **Mass & Charge**: Heavy mass ($m = 6.64 \\times 10^{-27}\\text{ kg}$), double positive charge ($+2e = +3.2 \\times 10^{-19}\\text{ C}$).'\n- **Ionizing Power**: **Extremely High**. Because of its large size and $+2e$ charge, an $\\alpha$ particle strongly strips electrons from air molecules, producing over $10^5$ ion pairs per centimeter.\n- **Penetrating Power**: **Very Low**. Stopped by a single sheet of paper or a few centimeters of air ($3-8\\text{ cm}$)."
        }),
        (3, "Alpha ($\alpha$) Radiation Properties", "suggested_diagram", "suggested_diagram", 2, {
            "text": "Alpha, Beta, and Gamma Radiation Penetration Shielding Comparison Diagram",
            "instruction": "Diagram showing alpha stopped by paper, beta stopped by aluminum plate, and gamma attenuated by thick lead shield."
        }),
        # Page 4
        (4, "Beta ($\beta^-$) Radiation Properties", "concept_explanation", "concept_explanation", 1, {
            "text": "### Nature of Beta ($\beta^-$) Particles:\nA **beta particle** is a high-speed electron ($^{0}_{-1}\\text{e}$ or $^{0}_{-1}\\beta$) ejected from an unstable nucleus when a neutron decays into a proton ($^{1}_{0}\\text{n} \\rightarrow ^{1}_{1}\\text{p} + ^{0}_{-1}\\text{e} + \\bar{\\nu}_e$).\n\n### Key Physical Properties:\n- **Mass & Charge**: Negligible mass ($m_e = 9.1 \\times 10^{-31}\\text{ kg}$), single negative charge ($-1e = -1.6 \\times 10^{-19}\\text{ C}$).'\n- **Ionizing Power**: **Moderate** (about $100$ times less than $\\alpha$ particles).\n- **Penetrating Power**: **Moderate**. Passes through paper, but is completely stopped by a $5\\text{ mm}$ sheet of aluminum metal."
        }),
        # Page 5
        (5, "Gamma ($\gamma$) Radiation Properties", "concept_explanation", "concept_explanation", 1, {
            "text": "### Nature of Gamma ($\gamma$) Rays:\n**Gamma rays** are high-frequency electromagnetic photons ($^{0}_{0}\\gamma$) emitted from an excited nucleus returning to a lower energy ground state.\n\n### Key Physical Properties:\n- **Mass & Charge**: **Zero rest mass, zero charge** ($m = 0$, $q = 0$).\n- **Speed**: Travels through vacuum at the speed of light ($c = 3.0 \\times 10^8\\text{ m/s}$).'\n- **Ionizing Power**: **Low**. Interacts weakly with matter via photoelectric absorption and Compton scattering.\n- **Penetrating Power**: **Extremely High**. Requires several centimeters of dense lead or several meters of concrete to absorb."
        }),
        # Page 6
        (6, "Magnetic & Electric Field Deflections", "concept_explanation", "concept_explanation", 1, {
            "text": "### Deflection in Perpendicular Fields:\nWhen $\\alpha, \\beta, \\gamma$ rays pass through electric or magnetic fields:\n- **Alpha ($\alpha$) Rays**: Deflected slightly toward the negative electric plate (or according to Fleming's LHR in magnetic fields) due to their positive $+2e$ charge and heavy mass.\n- **Beta ($\beta^-$) Rays**: Deflected strongly in the opposite direction toward the positive electric plate because of their negative charge ($-1e$) and light electron mass.\n- **Gamma ($\gamma$) Rays**: Pass straight through without any deflection because they carry **zero electrical charge**!"
        }),
        (6, "Magnetic & Electric Field Deflections", "suggested_diagram", "suggested_diagram", 2, {
            "text": "Electric and Magnetic Field Trajectory Deflections of Alpha, Beta, and Gamma Rays",
            "instruction": "Diagram showing alpha curving toward negative plate, beta curving strongly toward positive plate, and gamma passing straight."
        }),
        # Page 7
        (7, "Radiation Detectors: Electroscope & Cloud Chamber", "concept_explanation", "concept_explanation", 1, {
            "text": "### Visualizing Radiation Tracks:\n1. **Charged Gold-Leaf Electroscope**: Alpha particles heavily ionize surrounding air, producing positive ions and free electrons that discharge a negatively charged electroscope, causing leaves to collapse.\n2. **Wilson Cloud Chamber**: Contains supersaturated alcohol vapor. When ionizing radiation passes through, ions act as condensation nuclei, forming visible white liquid droplet tracks:\n   - **$\\alpha$-tracks**: Dense, thick, straight tracks of uniform length.\n   - **$\\beta$-tracks**: Thin, faint, wispy, erratic zigzag tracks due to scattering."
        }),
        (7, "Radiation Detectors: Electroscope & Cloud Chamber", "suggested_diagram", "suggested_diagram", 2, {
            "text": "Wilson Cloud Chamber Condensation Tracks: Thick Straight Alpha vs Thin Zigzag Beta Tracks",
            "instruction": "Diagram showing cloud chamber vapor tracks for heavy alpha particles vs light scattered beta particles."
        }),
        # Page 8
        (8, "Radiation Detectors: Geiger-Müller (GM) Tube", "concept_explanation", "concept_explanation", 1, {
            "text": "### Construction & Operation of GM Tube:\nA **Geiger-Müller (GM) Tube** consists of a hollow metal cylinder (cathode) containing low-pressure argon gas mixed with bromine quenching gas, with a thin wire anode running down the center.\n\nWhen an ionizing particle enters through the thin mica window, it ionizes an argon atom. Accelerated free electrons collide with adjacent argon atoms, creating an **Townsend electron avalanche**. This pulse flows to an electronic counter, recording individual radiation counts!"
        }),
        (8, "Radiation Detectors: Geiger-Müller (GM) Tube", "suggested_diagram", "suggested_diagram", 2, {
            "text": "Geiger-Muller GM Tube Internal Anatomy: Mica Window, Central Anode Wire, and Pulse Counter Circuit",
            "instruction": "Diagram showing GM tube construction with mica window, anode wire, argon gas, high voltage supply, and pulse counter."
        }),
        (8, "Radiation Detectors: Geiger-Müller (GM) Tube", "suggested_image", "suggested_image", 3, {
            "text": "Geiger-Muller Counter Hardware Tube Unit"
        }),
        # Page 9
        (9, "Knowledge Check: Radiation Properties", "knowledge_check", "knowledge_check", 1, {
            "question": "Which type of nuclear radiation has the HIGHEST ionizing power but LOWEST penetrating power?",
            "options": ["Alpha (alpha) particles", "Beta (beta) particles", "Gamma (gamma) rays", "X-rays"],
            "answer": "Alpha (alpha) particles",
            "explanation": "Alpha particles carry double positive charge (+2e) and large mass, producing dense ionization but stopping within paper or a few cm of air."
        }),
        (9, "Knowledge Check: Radiation Properties", "knowledge_check", "knowledge_check", 2, {
            "question": "Why are Gamma (gamma) rays un-deflected when passing through strong electric and magnetic fields?",
            "options": ["They travel faster than light", "They carry zero electrical charge", "They have huge positive mass", "They absorb magnetic flux"],
            "answer": "They carry zero electrical charge",
            "explanation": "Gamma rays are uncharged electromagnetic photons (q = 0), so Lorentz forces (F = q E and F = q v B) are zero."
        }),
        # Page 10
        (10, "Module Summary", "summary", "summary", 1, {
            "text": "### Module 10.1 Key Takeaways:\n1. **Nuclide Notation**: $^{A}_{Z}\\text{X}$ (Mass number $A$, Atomic number $Z$).\n2. **Alpha ($\\alpha$)**: Helium nucleus $^{4}_{2}\\text{He}$, highest ionization, stopped by paper.\n3. **Beta ($\\beta^-$)**: High-speed electron $^{0}_{-1}\\text{e}$, moderate ionization, stopped by $5\\text{ mm}$ aluminum.\n4. **Gamma ($\\gamma$)**: High energy photon, zero charge, highest penetration (stopped by thick lead).\n5. **Detectors**: Electroscope, Wilson cloud chamber, Geiger-Müller (GM) counter tube."
        }),
        (10, "Module Summary", "key_takeaway", "key_takeaway", 2, {
            "text": "Radioactivity is the spontaneous disintegration of unstable nuclei emitting alpha, beta, or gamma rays with distinct ionizing and penetrating properties."
        })
    ]

    for p_num, title, btype, ctype, order, content in blocks_m101:
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
    # MODULE 10.2: Radioactive Decay Equations, Half-Life Kinetics, and Dating
    # -------------------------------------------------------------------------
    unit_2, _ = LearningUnit.objects.get_or_create(
        topic=topic, order=2,
        defaults={"name": "Module 10.2: Radioactive Decay Equations, Half-Life Kinetics, and Dating"}
    )
    lesson_2, _ = Lesson.objects.get_or_create(
        topic=topic,
        learning_unit=unit_2,
        defaults={"title": "Radioactive Decay Equations, Half-Life Kinetics, and Dating", "status": "published", "version": 1}
    )
    lesson_2.blocks.all().delete()

    blocks_m102 = [
        # Page 1
        (1, "The Law of Radioactive Decay", "learning_goal", "learning_goal", 1, {
            "goals": [
                "Write balanced nuclear decay equations for alpha, beta, and gamma emissions",
                "Define half-life $T_{1/2}$ and decay constant $\\lambda$, deriving $T_{1/2} = \\frac{\\ln 2}{\\lambda}$",
                "Apply Carbon-14 radioactive dating to determine archaeological artifact age"
            ]
        }),
        (1, "The Law of Radioactive Decay", "concept_explanation", "concept_explanation", 2, {
            "text": "### Spontaneous & Random Disintegration:\nRadioactive decay is a **spontaneous and random process** unaffected by environmental conditions like temperature, pressure, or chemical bonding.\n\n### The Exponential Decay Equation:\nThe rate of nuclear decay (Activity $A = -\\frac{dN}{dt}$) is directly proportional to the number of undecayed nuclei $N$ present:\n$$A = \\lambda N \\implies N(t) = N_0 e^{-\\lambda t}$$\n- $N_0$: Initial number of radioactive nuclei at time $t = 0$.\n- $N(t)$: Remaining undecayed nuclei at time $t$.\n- $\\lambda$: **Decay Constant** (fractional probability of decay per second, $\\text{s}^{-1}$)."
        }),
        # Page 2
        (2, "Alpha ($\alpha$) Decay Nuclear Balance", "concept_explanation", "concept_explanation", 1, {
            "text": "### Balancing Alpha Decay Equations:\nWhen a parent nucleus emits an alpha particle ($^{4}_{2}\\text{He}$):\n1. **Mass Number Conservation**: Mass number drops by $4$ ($A \\rightarrow A - 4$).\n2. **Atomic Number Conservation**: Atomic number drops by $2$ ($Z \\rightarrow Z - 2$).\n$$\\text{General Formula: } ^{A}_{Z}\\text{X} \\rightarrow ^{A-4}_{Z-2}\\text{Y} + ^{4}_{2}\\text{He}$$\n\n### Example (Uranium-238 Decay):\n$$^{238}_{92}\\text{U} \\rightarrow ^{234}_{90}\\text{Th} + ^{4}_{2}\\text{He}$$\nUranium-238 transmutes into Thorium-234!"
        }),
        (2, "Alpha ($\alpha$) Decay Nuclear Balance", "suggested_diagram", "suggested_diagram", 2, {
            "text": "Alpha Decay Nuclear Transmutation Diagram (Parent Nucleus Ejecting Helium Nucleus)",
            "instruction": "Diagram showing parent Uranium nucleus emitting helium nucleus to form daughter Thorium nucleus."
        }),
        # Page 3
        (3, "Beta ($\beta^-$) Decay Nuclear Balance", "concept_explanation", "concept_explanation", 1, {
            "text": "### Balancing Beta Decay Equations:\nDuring beta minus decay, a nuclear neutron turns into a proton, emitting an electron ($^{0}_{-1}\\text{e}$) and an antineutrino ($\\bar{\\nu}_e$):\n1. **Mass Number Conservation**: Mass number remains unchanged ($A \\rightarrow A$).\n2. **Atomic Number Conservation**: Atomic number increases by $1$ ($Z \\rightarrow Z + 1$).\n$$\\text{General Formula: } ^{A}_{Z}\\text{X} \\rightarrow ^{A}_{Z+1}\\text{Y} + ^{0}_{-1}\\text{e} + \\bar{\\nu}_e$$\n\n### Example (Carbon-14 Decay):\n$$^{14}_{6}\\text{C} \\rightarrow ^{14}_{7}\\text{N} + ^{0}_{-1}\\text{e} + \\bar{\\nu}_e$$\nCarbon-14 transmutes into Nitrogen-14!"
        }),
        (3, "Beta ($\beta^-$) Decay Nuclear Balance", "suggested_diagram", "suggested_diagram", 2, {
            "text": "Beta Decay Nuclear Transmutation Reaction (Neutron Converting into Proton and Electron)",
            "instruction": "Diagram showing nuclear neutron splitting into proton, high-speed electron, and antineutrino."
        }),
        # Page 4
        (4, "Gamma ($\gamma$) Emission Mechanics", "concept_explanation", "concept_explanation", 1, {
            "text": "### Excited Nuclear Energy States:\nFollowing $\\alpha$ or $\\beta$ emission, the daughter nucleus is often left in an excited nuclear energy state (denoted $^{A}_{Z}\\text{Y}^*$).\n\nTo reach ground state stability, the nucleus releases surplus energy as a high-frequency gamma photon ($^{0}_{0}\\gamma$):\n$$^{A}_{Z}\\text{Y}^* \\rightarrow ^{A}_{Z}\\text{Y} + ^{0}_{0}\\gamma$$\nNotice that gamma emission causes **ZERO change** in mass number $A$ or atomic number $Z$!"
        }),
        # Page 5
        (5, "Half-Life ($T_{1/2}$) & Decay Curve Kinetics", "definition_card", "definition_card", 1, {
            "term": "Half-Life (T_1/2)",
            "definition": "The time taken for exactly half of the radioactive atoms in a sample to disintegrate, or for the activity of the sample to decrease to half its initial value."
        }),
        (5, "Half-Life ($T_{1/2}$) & Decay Curve Kinetics", "concept_explanation", "concept_explanation", 2, {
            "text": "### The Half-Life Rule:\nAfter $n$ half-lives, the fraction of initial nuclei remaining is:\n$$N = N_0 \\left(\\frac{1}{2}\\right)^n, \\quad \\text{where } n = \\frac{t}{T_{1/2}}$$\n- After $1$ half-life: $N = \\frac{1}{2} N_0 = 50\\%$.\n- After $2$ half-lives: $N = \\frac{1}{4} N_0 = 25\\%$.\n- After $3$ half-lives: $N = \\frac{1}{8} N_0 = 12.5\\%$."
        }),
        (5, "Half-Life ($T_{1/2}$) & Decay Curve Kinetics", "suggested_diagram", "suggested_diagram", 3, {
            "text": "Radioactive Decay Curve Graph Showing Activity Halving Over Consecutive Half-Life Intervals",
            "instruction": "Exponential decay curve showing N_0 halving to N_0/2 at T_1/2 and N_0/4 at 2 T_1/2."
        }),
        # Page 6
        (6, "Mathematical Derivation: $T_{1/2} = \frac{\ln 2}{\lambda}$", "formula_breakdown", "formula_breakdown", 1, {
            "formula": "T_{1/2} = \\frac{\\ln 2}{\\lambda} = \\frac{0.693}{\\lambda}",
            "variables": {
                "T_1/2": "Half-life of radioactive isotope (seconds, days, or years)",
                "lambda": "Decay constant of isotope (s^-1, day^-1, or year^-1)",
                "ln2": "Natural logarithm of 2 (approx 0.69315)"
            }
        }),
        (6, "Mathematical Derivation: $T_{1/2} = \frac{\ln 2}{\lambda}$", "concept_explanation", "concept_explanation", 2, {
            "text": "### Deriving the Half-Life Relationship:\nStarting from $N(t) = N_0 e^{-\\lambda t}$, substitute $t = T_{1/2}$ and $N = \\frac{N_0}{2}$:\n$$\\frac{N_0}{2} = N_0 e^{-\\lambda T_{1/2}} \\implies \\frac{1}{2} = e^{-\\lambda T_{1/2}}$$\nTaking natural logarithms on both sides:\n$$\\ln\\left(\\frac{1}{2}\\right) = -\\lambda T_{1/2} \\implies -\\ln 2 = -\\lambda T_{1/2} \\implies T_{1/2} = \\frac{\\ln 2}{\\lambda} \\approx \\frac{0.693}{\\lambda}$$"
        }),
        # Page 7
        (7, "Carbon-14 Radioactive Dating ($^{14}\\text{C}$)", "concept_explanation", "concept_explanation", 1, {
            "text": "### Archaeometry & Carbon Dating:\nCosmic rays in the upper atmosphere continually convert nitrogen into radioactive Carbon-14 ($^{14}_{6}\\text{C}$, half-life $5,730\\text{ years}$).\n- **Living Organisms**: Plants absorb $^{14}\\text{C}$ via photosynthesis, and animals eat plants, maintaining a constant ratio of $^{14}\\text{C}$ to stable $^{12}\\text{C}$.\n- **After Death**: Photosynthesis ceases. The $^{14}\\text{C}$ present in wood, bones, or linen decays via beta emission without replacement.\n- **Age Calculation**: Measuring the remaining $^{14}\\text{C}$ activity per gram of carbon reveals the exact elapsed time since death!"
        }),
        (7, "Carbon-14 Radioactive Dating ($^{14}\\text{C}$)", "suggested_diagram", "suggested_diagram", 2, {
            "text": "Carbon-14 Atmospheric Production Cycle and Archaeological Artifact Decay Timeline",
            "instruction": "Diagram showing cosmic ray conversion of N-14 to C-14, absorption by living trees, and decay in dead artifacts."
        }),
        # Page 8
        (8, "Industrial & Medical Radioisotope Applications", "concept_explanation", "concept_explanation", 1, {
            "text": "### Practical Uses of Radioisotopes:\n1. **Medical Tracer Diagnostics**: Iodine-131 ($^{131}\\text{I}$) is swallowed to diagnose thyroid gland disorders. Technetium-99m ($^{99m}\\text{Tc}$) maps organ blood flow.\n2. **Radiotherapy Cancer Treatment**: High-dose gamma rays from Cobalt-60 ($^{60}\\text{Co}$) target and destroy malignant cancer tumors.\n3. **Industrial Thickness Gauges**: A beta emitter (Strontium-90) monitors paper or metal sheet thickness. Variations in detected beta counts adjust rolling mill rollers automatically."
        }),
        # Page 9
        (9, "Knowledge Check: Decay Equations", "knowledge_check", "knowledge_check", 1, {
            "question": "When Uranium-238 (^238_92 U) undergoes ALPHA decay, what are the mass number (A) and atomic number (Z) of the resulting daughter nucleus?",
            "options": ["A = 234, Z = 90", "A = 238, Z = 93", "A = 234, Z = 91", "A = 236, Z = 90"],
            "answer": "A = 234, Z = 90",
            "explanation": "Alpha emission (^4_2 He) reduces mass number A by 4 (238 - 4 = 234) and atomic number Z by 2 (92 - 2 = 90), forming Thorium-234."
        }),
        (10, "Knowledge Check: Half-Life Kinetics", "knowledge_check", "knowledge_check", 2, {
            "question": "A radioactive sample has an initial activity of 800 Bq. If its half-life is 4 hours, what will its activity be after 12 hours?",
            "options": ["100 Bq", "200 Bq", "400 Bq", "50 Bq"],
            "answer": "100 Bq",
            "explanation": "Number of half-lives n = 12 hrs / 4 hrs = 3. Activity = 800 x (1/2)^3 = 800 / 8 = 100 Bq."
        }),
        # Page 11
        (11, "Module Summary", "summary", "summary", 1, {
            "text": "### Module 10.2 Key Takeaways:\n1. **Alpha Decay**: $^{A}_{Z}\\text{X} \\rightarrow ^{A-4}_{Z-2}\\text{Y} + ^{4}_{2}\\text{He}$.\n2. **Beta Decay**: $^{A}_{Z}\\text{X} \\rightarrow ^{A}_{Z+1}\\text{Y} + ^{0}_{-1}\\text{e} + \\bar{\\nu}_e$.\n3. **Half-Life Equation**: $T_{1/2} = \\frac{0.693}{\\lambda}$, $N = N_0 (1/2)^n$.\n4. **Applications**: Carbon-14 dating ($5,730\\text{ yrs}$), Cobalt-60 radiotherapy, industrial paper gauges."
        }),
        (12, "Module Summary", "key_takeaway", "key_takeaway", 2, {
            "text": "Radioactive decay follows strict mass/charge conservation laws and exponential kinetics, enabling half-life dating and nuclear medicine."
        })
    ]

    for p_num, title, btype, ctype, order, content in blocks_m102:
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
    # MODULE 10.3: Nuclear Energy (Fission vs Fusion), Hazards, and Worked Examples
    # -------------------------------------------------------------------------
    unit_3, _ = LearningUnit.objects.get_or_create(
        topic=topic, order=3,
        defaults={"name": "Module 10.3: Nuclear Energy (Fission vs Fusion), Hazards, and Worked Examples"}
    )
    lesson_3, _ = Lesson.objects.get_or_create(
        topic=topic,
        learning_unit=unit_3,
        defaults={"title": "Nuclear Energy (Fission vs Fusion), Hazards, and Worked Examples", "status": "published", "version": 1}
    )
    lesson_3.blocks.all().delete()

    blocks_m103 = [
        # Page 1
        (1, "Governing Mathematics 1: Einstein's $E = \Delta m c^2$", "formula_breakdown", "formula_breakdown", 1, {
            "formula": "E = \\Delta m \\cdot c^2",
            "variables": {
                "E": "Energy released in nuclear reaction (Joules)",
                "delta_m": "Mass defect = Mass of reactants - Mass of products (kg)",
                "c": "Speed of light (3.0 x 10^8 m/s)"
            }
        }),
        (1, "Governing Mathematics 1: Einstein's $E = \Delta m c^2$", "concept_explanation", "concept_explanation", 2, {
            "text": "### Mass Defect & Nuclear Binding Energy:\nIn any nuclear reaction, the total mass of the products is slightly less than the total mass of the initial reactants. This missing mass is called the **Mass Defect ($\\Delta m$)**.\n\nAccording to Einstein's mass-energy equivalence equation ($E = \\Delta m c^2$), a tiny mass defect converts into a staggering quantity of energy ($1\\text{ kg of mass} = 9 \\times 10^{16}\\text{ Joules}$ of energy)!"
        }),
        # Page 2
        (2, "Nuclear Fission Mechanics", "concept_explanation", "concept_explanation", 1, {
            "text": "### Splitting Heavy Nuclei:\n**Nuclear Fission** is the splitting of a heavy, unstable nucleus (such as Uranium-235) into two medium-sized daughter fragments upon absorbing a thermal neutron.\n\n### Typical Uranium-235 Fission Reaction:\n$$^{235}_{92}\\text{U} + ^{1}_{0}\\text{n} \\rightarrow ^{141}_{56}\\text{Ba} + ^{92}_{36}\\text{Kr} + 3 ^{1}_{0}\\text{n} + Q$$\n- **Chain Reaction**: The $3$ secondary neutrons released strike adjacent Uranium-235 nuclei, triggering a self-sustaining exponential **Chain Reaction**!"
        }),
        (2, "Nuclear Fission Mechanics", "suggested_diagram", "suggested_diagram", 2, {
            "text": "Uranium-235 Fission Chain Reaction Diagram Splitting into Barium, Krypton, and 3 Neutrons",
            "instruction": "Diagram showing thermal neutron striking U-235, splitting into Ba-141 and Kr-92 releasing 3 neutrons."
        }),
        # Page 3
        (3, "Controlled Nuclear Reactors", "concept_explanation", "concept_explanation", 1, {
            "text": "### Components of a Nuclear Reactor:\n1. **Fuel Rods**: Uranium enriched with $^{235}\\text{U}$.\n2. **Moderator (Heavy Water or Graphite)**: Slows down fast secondary neutrons to thermal energy speeds so they can be absorbed by $^{235}\\text{U}$.\n3. **Control Rods (Boron or Cadmium)**: Absorbs excess neutrons. Lowering control rods halts the chain reaction; raising them increases power output.\n4. **Coolant (Water or Liquid Sodium)**: Extracts thermal energy to boil water into high-pressure steam for electricity turbines."
        }),
        (3, "Controlled Nuclear Reactors", "suggested_image", "suggested_image", 2, {
            "text": "Nuclear Power Plant Reactor Containment Dome Hardware Unit"
        }),
        # Page 4
        (4, "Nuclear Fusion Mechanics ($^{2}_{1}\\text{H} + ^{3}_{1}\\text{H}$)", "concept_explanation", "concept_explanation", 1, {
            "text": "### Combining Light Nuclei:\n**Nuclear Fusion** is the combining of two light atomic nuclei (like Deuterium $^{2}_{1}\\text{H}$ and Tritium $^{3}_{1}\\text{H}$) under ultra-high temperatures ($> 10^7\\text{ K}$) to form a heavier Helium nucleus ($^{4}_{2}\\text{He}$) plus a neutron.\n\n### Deuterium-Tritium Thermonuclear Fusion:\n$$^{2}_{1}\\text{H} + ^{3}_{1}\\text{H} \\rightarrow ^{4}_{2}\\text{He} + ^{1}_{0}\\text{n} + 17.6\\text{ MeV}$$\n- **Stellar Energy**: Fusion powers the Sun and all stars! Fusion produces zero long-lived radioactive waste and yields more energy per gram than fission."
        }),
        (4, "Nuclear Fusion Mechanics ($^{2}_{1}\\text{H} + ^{3}_{1}\\text{H}$)", "suggested_diagram", "suggested_diagram", 2, {
            "text": "Deuterium-Tritium Thermonuclear Fusion Reaction Diagram Yielding Helium and 17.6 MeV Energy",
            "instruction": "Diagram showing H-2 and H-3 fusing at high temperature to form He-4 and neutron with energy release."
        }),
        # Page 5
        (5, "Worked Example Level 1 — Balancing Nuclear Decay Equations", "worked_example", "worked_example", 1, {
            "problem": "Radon-222 ($^{222}_{86}\\text{Rn}$) decays by alpha emission into Polonium (Po). Write the balanced nuclear equation and determine the mass number and atomic number of the daughter Polonium nucleus.",
            "steps": [
                "Step 1: Identify parent: $^{222}_{86}\\text{Rn}$, emitted particle: $^{4}_{2}\\text{He}$.",
                "Step 2: Apply mass number conservation: $A = 222 - 4 = 218$.",
                "Step 3: Apply atomic number conservation: $Z = 86 - 2 = 84$.",
                "Step 4: Write balanced nuclear equation: $^{222}_{86}\\text{Rn} \\rightarrow ^{218}_{84}\\text{Po} + ^{4}_{2}\\text{He}$.",
                "Step 5: Conclusion: Daughter is Polonium-218 ($^{218}_{84}\\text{Po}$)."
            ]
        }),
        # Page 6
        (6, "Worked Example Level 2 — Half-Life Fraction Remaining", "worked_example", "worked_example", 1, {
            "problem": "A medical sample contains $64.0\\text{ mg}$ of Technetium-99m ($^{99m}\\text{Tc}$) having a half-life of $6.0\\text{ hours}$. Calculate the mass of Technetium-99m remaining after $24.0\\text{ hours}$.",
            "steps": [
                "Step 1: Knowns: Initial mass $M_0 = 64.0\\text{ mg}$, $T_{1/2} = 6.0\\text{ hours}$, elapsed time $t = 24.0\\text{ hours}$.",
                "Step 2: Number of half-lives: $n = \\frac{t}{T_{1/2}} = \\frac{24.0}{6.0} = 4\\text{ half-lives}$.",
                "Step 3: Equation: $M = M_0 \\left(\\frac{1}{2}\\right)^n = 64.0 \\times \\left(\\frac{1}{2}\\right)^4 = \\frac{64.0}{16}$.",
                "Step 4: Compute final mass: $M = 4.0\\text{ mg}$."
            ]
        }),
        # Page 7
        (7, "Worked Example Level 3 — Activity & Decay Constant Calculation", "worked_example", "worked_example", 1, {
            "problem": "A radioactive isotope has a decay constant $\\lambda = 3.50 \\times 10^{-6}\\text{ s}^{-1}$. Calculate: 1. Its half-life $T_{1/2}$ in seconds and hours. 2. The activity of a sample containing $4.0 \\times 10^{18}$ radioactive atoms.",
            "steps": [
                "Step 1: Calculate half-life: $T_{1/2} = \\frac{\\ln 2}{\\lambda} = \\frac{0.69315}{3.50 \\times 10^{-6}} = 1.980 \\times 10^5\\text{ seconds}$.",
                "Step 2: Convert to hours: $T_{1/2} = \\frac{1.980 \\times 10^5}{3600} = 55.0\\text{ hours}$.",
                "Step 3: Calculate sample activity $A = \\lambda N = (3.50 \\times 10^{-6}\\text{ s}^{-1}) \\times (4.0 \\times 10^{18}) = 1.40 \\times 10^{13}\\text{ Bq}$ (Bequerels)."
            ]
        }),
        # Page 8
        (8, "Worked Example Level 4 — Mass Defect & Released Energy ($E = \Delta m c^2$)", "worked_example", "worked_example", 1, {
            "problem": "In a nuclear fission reaction, the mass of reactants is $236.0526\\text{ u}$ and mass of products is $235.8376\\text{ u}$. Calculate the energy released in Joules. (Take $1\\text{ u} = 1.66 \\times 10^{-27}\\text{ kg}$, $c = 3.0 \\times 10^8\\text{ m/s}$).",
            "steps": [
                "Step 1: Calculate mass defect $\\Delta m = 236.0526 - 235.8376 = 0.2150\\text{ u}$.",
                "Step 2: Convert mass defect to kilograms: $\\Delta m = 0.2150 \\times (1.66 \\times 10^{-27}\\text{ kg}) = 3.569 \\times 10^{-28}\\text{ kg}$.",
                "Step 3: Apply Einstein formula $E = \\Delta m c^2 = (3.569 \\times 10^{-28}) \\times (3.0 \\times 10^8)^2$.",
                "Step 4: Compute energy: $E = (3.569 \\times 10^{-28}) \\times (9.0 \\times 10^{16}) = 3.212 \\times 10^{-11}\\text{ Joules}$."
            ]
        }),
        # Page 9
        (9, "Worked Example Level 5 — Challenge Multi-Step (Carbon Dating)", "worked_example", "worked_example", 1, {
            "problem": "A ancient wooden spearhead excavated from a cave displays a Carbon-14 activity of $3.75\\text{ counts/min per gram}$. Freshly cut living wood displays a Carbon-14 activity of $15.00\\text{ counts/min per gram}$. Given $^{14}\\text{C}$ half-life $T_{1/2} = 5,730\\text{ years}$, calculate the age of the wooden spearhead.",
            "steps": [
                "Step 1: Identify activity ratio: $\\frac{A}{A_0} = \\frac{3.75}{15.00} = 0.25 = \\frac{1}{4}$.",
                "Step 2: Determine number of half-lives $n$: Since $\\left(\\frac{1}{2}\\right)^n = \\frac{1}{4} \\implies n = 2\\text{ half-lives}$.",
                "Step 3: Calculate age: $t = n \\times T_{1/2} = 2 \\times 5,730\\text{ years} = 11,460\\text{ years old}$."
            ]
        }),
        # Page 10
        (10, "Biological Hazards & Nuclear Waste Safety Protocols", "concept_explanation", "concept_explanation", 1, {
            "text": "### Radiation Hazards & Protection:\n- **Biological Risks**: Ionizing radiation breaks chemical bonds in DNA, leading to radiation sickness, tissue necrosis, leukemia, and hereditary genetic mutations.\n- **Waste Management**: High-level nuclear waste remains radioactive for thousands of years. Waste is vitrified into solid borosilicate glass blocks, encased in heavy stainless steel containers, and buried deep underground in stable geological formations."
        }),
        (10, "Biological Hazards & Nuclear Waste Safety Protocols", "suggested_diagram", "suggested_diagram", 2, {
            "text": "Nuclear Trefoil Warning Symbol, Lead Storage Cask, and Deep Geological Waste Storage",
            "instruction": "Diagram showing trefoil warning icon, lead container cask, and deep underground vitrified waste storage."
        }),
        # Page 11
        (11, "Addressing Key Student Misconceptions", "common_misconception", "common_misconception", 1, {
            "text": "### 4 Critical Misconceptions Clarified:\n1. **Fission vs Fusion**: Fission splits heavy nuclei ($^{235}\\text{U}$); Fusion combines light nuclei ($^{2}\\text{H} + ^{3}\\text{H}$).\n2. **Half-Life & Temperature**: Half-life is a fundamental nuclear property; heating or cooling a sample does **NOT** speed up or slow down decay.\n3. **Mass Number vs Atomic Number**: Alpha decay drops $A$ by $4$ and $Z$ by $2$; Beta decay leaves $A$ unchanged and increases $Z$ by $1$.\n4. **Radioactivity vs Radiation**: Radioactivity is the process of nuclear decay; Radiation refers to the emitted particles or waves."
        }),
        # Page 12
        (12, "Assessment Suite", "knowledge_check", "knowledge_check", 1, {
            "question": "What is the primary role of a MODERATOR (like heavy water or graphite) in a thermal nuclear fission reactor?",
            "options": ["Absorb all secondary neutrons to stop the reactor", "Slow down fast neutrons to thermal speeds for efficient absorption by U-235", "Generate electricity directly from alpha particles", "Prevent gamma radiation leakage"],
            "answer": "Slow down fast neutrons to thermal speeds for efficient absorption by U-235",
            "explanation": "Fast neutrons released during fission must be slowed down (moderated) to thermal velocities (~2200 m/s) to be absorbed effectively by U-235 nuclei."
        }),
        (12, "Assessment Suite", "knowledge_check", "knowledge_check", 2, {
            "question": "If a sample containing 100 grams of an isotope with a half-life of 10 days is left for 30 days, how much of the original isotope remains undecayed?",
            "options": ["12.5 grams", "25.0 grams", "50.0 grams", "6.25 grams"],
            "answer": "12.5 grams",
            "explanation": "30 days / 10 days = 3 half-lives. Remaining mass = 100 x (1/2)^3 = 100 / 8 = 12.5 grams."
        }),
        # Page 13
        (13, "Module Summary", "summary", "summary", 1, {
            "text": "### Module 10.3 Key Takeaways:\n1. **Mass Defect**: Energy released $E = \\Delta m c^2$.\n2. **Fission**: Splitting $^{235}\\text{U}$ with neutrons in controlled power reactors.\n3. **Fusion**: Thermonuclear combining of $^{2}\\text{H} + ^{3}\\text{H} \\rightarrow ^{4}_{2}\\text{He} + n + 17.6\\text{ MeV}$.\n4. **Safety**: Borosilicate glass vitrification, deep geological burial, control rods, and lead casks."
        }),
        (14, "Module Summary", "key_takeaway", "key_takeaway", 2, {
            "text": "Topic 10 Complete: Radioactivity connects atomic nuclear physics to half-life kinetics, Carbon-14 dating, and clean nuclear fusion power."
        })
    ]

    for p_num, title, btype, ctype, order, content in blocks_m103:
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
    print("TOPIC 10 INGESTION COMPLETED SUCCESSFULLY!")
    print("=" * 80)

if __name__ == "__main__":
    run_ingestion()
