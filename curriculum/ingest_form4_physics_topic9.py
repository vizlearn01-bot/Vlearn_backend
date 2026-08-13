"""
VLearn Form 4 Physics — Topic 9: Photoelectric Effect
Comprehensive Ingestion Engine (Enriched Deep Text & Visual Architecture)

Modules:
  9.1 Quantum Foundations and Photoelectric Phenomena (10 Pages, 18 Blocks)
  9.2 Einstein's Photoelectric Equation, Stopping Potential, and Photocells (12 Pages, 19 Blocks)
  9.3 Quantitative Photo-Electrodynamics, Laboratory Protocols, and Worked Examples (14 Pages, 20 Blocks)

Usage:
  /home/jason-bitega/Desktop/VL/vlearn_repositories/Vlearn_backend/venv/bin/python curriculum/ingest_form4_physics_topic9.py
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
    print("VLEARN FORM 4 PHYSICS — TOPIC 9 INGESTION")
    print("=" * 80)

    curriculum = Curriculum.objects.filter(name="844").first()
    grade = Grade.objects.filter(curriculum=curriculum, name="Form 4").first()
    subject = Subject.objects.filter(grade=grade, name="Physics").first()

    topic, _ = Topic.objects.get_or_create(
        subject=subject,
        order=9,
        defaults={"name": "Topic 9: Photoelectric Effect — Quantum Mechanics, Einstein's Equation, and Solar Cell Applications"}
    )
    topic.name = "Topic 9: Photoelectric Effect — Quantum Mechanics, Einstein's Equation, and Solar Cell Applications"
    topic.save()
    print(f"Topic 9: '{topic.name}' (ID: {topic.id}) ready.")

    # -------------------------------------------------------------------------
    # MODULE 9.1: Quantum Foundations and Photoelectric Phenomena
    # -------------------------------------------------------------------------
    unit_1, _ = LearningUnit.objects.get_or_create(
        topic=topic, order=1,
        defaults={"name": "Module 9.1: Quantum Foundations and Photoelectric Phenomena"}
    )
    lesson_1, _ = Lesson.objects.get_or_create(
        topic=topic,
        learning_unit=unit_1,
        defaults={"title": "Quantum Foundations and Photoelectric Phenomena", "status": "published", "version": 1}
    )
    lesson_1.blocks.all().delete()

    blocks_m91 = [
        # Page 1
        (1, "Physical Intuition: Solar Calculators & Failure of Wave Theory", "learning_goal", "learning_goal", 1, {
            "goals": [
                "Define the photoelectric effect as light-induced surface electron ejection",
                "Explain why classical wave theory failed to account for instantaneous electron ejection and threshold frequency",
                "Define work function energy barrier $\\Phi = h f_0$ and threshold frequency $f_0$"
            ]
        }),
        (1, "Physical Intuition: Solar Calculators & Failure of Wave Theory", "concept_explanation", "concept_explanation", 2, {
            "text": "### Real-World Intuition: Pocket Solar Calculators:\nHave you ever used a pocket calculator powered by a small dark strip above the display? When ambient room light hits that strip, electricity flows immediately without any batteries! This direct conversion of light energy into electrical current is driven by the **Photoelectric Effect**.\n\n### The Puzzle That Shook Classical Physics:\nIn the late 19th century, classical physics treated light strictly as a continuous wave. According to wave theory, a low-intensity light wave should slowly transfer energy to bound metal surface electrons over time, causing a time delay before electrons accumulate enough energy to escape. However, experiments showed that electrons were ejected **instantaneously** (in less than $10^{-9}\\text{ seconds}$) as soon as light hit the metal, provided the light frequency was above a sharp minimum threshold ($f_0$)!"
        }),
        # Page 2
        (2, "Hertz & Lenard Experiments: Zinc Plate Electroscope", "definition_card", "definition_card", 1, {
            "term": "Photoelectric Effect",
            "definition": "The emission of free electrons (photoelectrons) from a clean metal surface when electromagnetic radiation of sufficiently high frequency illuminates the surface."
        }),
        (2, "Hertz & Lenard Experiments: Zinc Plate Electroscope", "concept_explanation", "concept_explanation", 2, {
            "text": "### The Classic Zinc Plate Electroscope Experiment:\n1. **Setup**: A freshly polished zinc plate is mounted on the cap of a negatively charged gold-leaf electroscope. The leaves collapse slightly and stay diverged due to mutual electrostatic repulsion.\n2. **Visible Light Exposure**: Illuminating the zinc plate with bright visible light (red or blue) produces **no effect**—the leaves remain diverged regardless of light intensity or exposure time.\n3. **Ultraviolet (UV) Exposure**: When an ultraviolet lamp shines on the zinc plate, the gold leaves **collapse immediately**!\n4. **Physics Cause**: UV light photon energy exceeds the energy barrier of zinc, ejecting negative electrons. As negative charge escapes into the air, the electroscope loses its charge and the leaves collapse."
        }),
        (2, "Hertz & Lenard Experiments: Zinc Plate Electroscope", "suggested_diagram", "suggested_diagram", 3, {
            "text": "Gold Leaf Electroscope Negatively Charged Zinc Plate UV Light Discharge Protocol",
            "instruction": "Diagram showing negatively charged zinc plate on electroscope discharging under UV light while visible light produces no effect."
        }),
        (2, "Hertz & Lenard Experiments: Zinc Plate Electroscope", "suggested_image", "suggested_image", 4, {
            "text": "Historical Hertz and Lenard Photoelectric Spark Gap Apparatus"
        }),
        # Page 3
        (3, "The 3 Fundamental Photoelectric Laws", "step_process", "step_process", 1, {
            "steps": [
                "**1. Existence of Threshold Frequency ($f_0$)**: For every metal surface, there exists a characteristic minimum light frequency $f_0$. If incoming light frequency $f < f_0$, zero photoelectrons are emitted regardless of light intensity or duration.",
                "**2. Instantaneous Emission**: Photoelectron ejection occurs instantaneously ($< 10^{-9}\\text{ s}$) upon illumination with light frequency $f \\ge f_0$.",
                "**3. Current Proportional to Light Intensity**: Above threshold frequency ($f \\ge f_0$), the rate of electron ejection (photoelectric current $I$) is directly proportional to light intensity (photon flux).",
                "**4. Kinetic Energy Independent of Intensity**: The maximum kinetic energy ($K_{\\max}$) of emitted photoelectrons depends strictly on light frequency $f$, and is completely independent of light intensity!"
            ]
        }),
        # Page 4
        (4, "Work Function Energy Barrier ($\Phi = h f_0$)", "concept_explanation", "concept_explanation", 1, {
            "text": "### The Metal Surface Energy Barrier:\nInside a metal lattice, conduction electrons move freely between metal atoms but are bound inside the crystal lattice by attractive electrostatic forces from positive atomic nuclei.\n\n### Definition of Work Function ($\Phi$):\nThe **Work Function ($\\Phi$)** is the minimum amount of energy required to liberate a conduction electron from a metal surface against surface potential forces.\n- **Formula**: $$\\Phi = h f_0$$\n- **Units**: Work function is measured in **Joules (J)** or **Electron-Volts (eV)**, where $1\\text{ eV} = 1.6 \\times 10^{-19}\\text{ Joules}$.\n- **Metal Dependence**: Alkali metals like Potassium ($\\Phi = 2.26\\text{ eV}$) and Sodium ($\\Phi = 2.28\\text{ eV}$) have low work functions, releasing photoelectrons under visible light. Platinum ($\\Phi = 5.65\\text{ eV}$) requires high-energy UV light."
        }),
        (4, "Work Function Energy Barrier ($\Phi = h f_0$)", "suggested_diagram", "suggested_diagram", 2, {
            "text": "Metal Surface Energy Potential Well and Work Function Energy Barrier Diagram",
            "instruction": "Diagram showing potential well barrier Phi = h f_0 required for electron to escape metal surface into vacuum."
        }),
        # Page 5
        (5, "Threshold Wavelength ($\lambda_0 = c / f_0$)", "concept_explanation", "concept_explanation", 1, {
            "text": "### The Maximum Cutoff Wavelength:\nSince wave speed is $c = f \\lambda$, a minimum threshold frequency $f_0$ corresponds to a **maximum threshold wavelength ($\\lambda_0$)**:\n$$\\lambda_0 = \\frac{c}{f_0} = \\frac{h c}{\\Phi}$$\n- **Key Distinction**: Photoelectrons are emitted **ONLY** when incoming light wavelength $\\lambda \\le \\lambda_0$. Wavelengths longer than $\\lambda_0$ possess insufficient photon energy ($h c / \\lambda < \\Phi$) to overcome the surface work function."
        }),
        # Page 6
        (6, "Photoelectric Current vs Light Intensity ($I \\propto \\text{Flux}$)", "concept_explanation", "concept_explanation", 1, {
            "text": "### Photon Flux & Current Dynamics:\nWhen monochromatic light of frequency $f > f_0$ strikes a metal cathode:\n- **Increasing Light Intensity**: Increases the number of photons hitting the surface per second (photon flux).\n- **1-to-1 Interaction**: Since each incoming photon interacts with exactly one electron, doubling light intensity doubles the number of photoelectrons released per second, doubling the saturation **Photoelectric Current ($I$)**!"
        }),
        (6, "Photoelectric Current vs Light Intensity ($I \\propto \\text{Flux}$)", "suggested_diagram", "suggested_diagram", 2, {
            "text": "Linear Graph of Photoelectric Saturation Current Against Light Intensity",
            "instruction": "Graph showing straight line passing through origin representing photoelectric current proportional to light intensity."
        }),
        # Page 7
        (7, "Kinetic Energy Dependence on Light Frequency", "concept_explanation", "concept_explanation", 1, {
            "text": "### Frequency vs Kinetic Energy:\nIncreasing the frequency $f$ of monochromatic light above $f_0$ increases the energy of each individual light photon ($E = hf$).\n\nBecause the work function $\\Phi$ remains constant for a given metal, the surplus energy increases the **Maximum Kinetic Energy ($K_{\\max}$)** of the escaping photoelectrons, causing them to fly off at higher maximum speeds ($v_{\\max} = \\sqrt{\\frac{2 K_{\\max}}{m_e}}$)!"
        }),
        (7, "Kinetic Energy Dependence on Light Frequency", "suggested_diagram", "suggested_diagram", 2, {
            "text": "Graph of Maximum Kinetic Energy K_max Against Light Frequency f Showing Threshold Frequency Intercept",
            "instruction": "Graph of K_max vs frequency f showing straight line intersecting frequency axis at f_0 with slope Planck's constant h."
        }),
        # Page 8
        (8, "Interactive Photoelectric Sandbox", "suggested_simulation", "suggested_simulation", 1, {
            "text": "Interactive Photoelectric Sandbox: Parameter Sliders for Light Frequency, Intensity, and Work Function"
        }),
        # Page 9
        (9, "Knowledge Check: Quantum Foundations", "knowledge_check", "knowledge_check", 1, {
            "question": "What happens when light of frequency LESS than the threshold frequency (f < f_0) strikes a metal plate with high intensity?",
            "options": ["Photoelectrons are emitted after a long delay", "Zero photoelectrons are emitted regardless of intensity or duration", "Photoelectrons are emitted with low kinetic energy", "The metal plate melts immediately"],
            "answer": "Zero photoelectrons are emitted regardless of intensity or duration",
            "explanation": "If photon frequency f < f_0, individual photon energy hf < Phi. No single photon has enough energy to liberate an electron, so zero photoelectrons are emitted."
        }),
        (9, "Knowledge Check: Quantum Foundations", "knowledge_check", "knowledge_check", 2, {
            "question": "Increasing the INTENSITY of light above the threshold frequency causes an increase in which property?",
            "options": ["Maximum kinetic energy of photoelectrons", "Threshold frequency of the metal", "Number of photoelectrons emitted per second (photoelectric current)", "Work function of the metal"],
            "answer": "Number of photoelectrons emitted per second (photoelectric current)",
            "explanation": "Higher intensity increases photon flux (photons/second), causing more 1-to-1 collisions per second and higher photoelectric current."
        }),
        # Page 10
        (10, "Module Summary", "summary", "summary", 1, {
            "text": "### Module 9.1 Key Takeaways:\n1. **Photoelectric Effect**: Ejection of electrons when light illuminates a clean metal surface.\n2. **Work Function**: Minimum energy $\\Phi = h f_0$ required for an electron to escape.\n3. **Threshold Frequency**: Minimum light frequency $f_0$ below which no photoelectrons are emitted.\n4. **Intensity vs Frequency**: Intensity governs electron quantity (current); Frequency governs electron quality ($K_{\\max}$)."
        }),
        (10, "Module Summary", "key_takeaway", "key_takeaway", 2, {
            "text": "The photoelectric effect demonstrates the particle nature of light, where photon energy governs electron kinetic energy and photon flux governs current."
        })
    ]

    for p_num, title, btype, ctype, order, content in blocks_m91:
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
    # MODULE 9.2: Einstein's Photoelectric Equation, Stopping Potential, and Photocells
    # -------------------------------------------------------------------------
    unit_2, _ = LearningUnit.objects.get_or_create(
        topic=topic, order=2,
        defaults={"name": "Module 9.2: Einstein's Photoelectric Equation, Stopping Potential, and Photocells"}
    )
    lesson_2, _ = Lesson.objects.get_or_create(
        topic=topic,
        learning_unit=unit_2,
        defaults={"title": "Einstein's Photoelectric Equation, Stopping Potential, and Photocells", "status": "published", "version": 1}
    )
    lesson_2.blocks.all().delete()

    blocks_m92 = [
        # Page 1
        (1, "Einstein's Photon Hypothesis (1905)", "learning_goal", "learning_goal", 1, {
            "goals": [
                "Apply Einstein's Photoelectric Equation $h f = \\Phi + K_{\\max}$ to energy conservation problems",
                "Explain stopping potential $V_s$ and derive $K_{\\max} = e V_s$",
                "Describe photocells and solar cell applications in modern electronics"
            ]
        }),
        (1, "Einstein's Photon Hypothesis (1905)", "concept_explanation", "concept_explanation", 2, {
            "text": "### Albert Einstein's Nobel Prize-Winning Insight:\nIn 1905, Albert Einstein proposed that light is not a continuous wave, but consists of discrete localized packets of energy called **Photons** (light quanta).\n- **Photon Energy**: Each photon carries an energy quantum: $$E = h f = \\frac{h c}{\\lambda}$$\n- **One-to-One Interaction**: One incoming photon transfers **ALL** its energy to a single surface electron in a single instant. The photon is completely absorbed, ceasing to exist!"
        }),
        # Page 2
        (2, "Einstein's Photoelectric Equation", "formula_breakdown", "formula_breakdown", 1, {
            "formula": "h f = \\Phi + K_{\\max} = h f_0 + \\frac{1}{2} m_e v_{\\max}^2",
            "variables": {
                "h": "Planck's constant (6.63 x 10^-34 J s)",
                "f": "Incoming light photon frequency (Hertz)",
                "Phi": "Metal work function energy barrier (Joules or eV)",
                "K_max": "Maximum kinetic energy of escaping photoelectrons (Joules)",
                "f_0": "Threshold frequency of metal surface (Hertz)",
                "v_max": "Maximum escape velocity of photoelectrons (m/s)"
            }
        }),
        (2, "Einstein's Photoelectric Equation", "concept_explanation", "concept_explanation", 2, {
            "text": "### Energy Conservation Breakdown:\nWhen a photon of energy $h f$ strikes a metal:\n1. **Part 1 (Work Function $\\Phi$)**: Energy $h f_0$ is consumed overcoming the surface binding potential to liberate the electron.\n2. **Part 2 (Kinetic Energy $K_{\\max}$)**: Any remaining surplus energy becomes kinetic energy of the escaping photoelectron: $$K_{\\max} = h f - \\Phi = h(f - f_0)$$"
        }),
        (2, "Einstein's Photoelectric Equation", "suggested_diagram", "suggested_diagram", 3, {
            "text": "Einstein Photoelectric Energy Balance Partition Diagram (hf -> Phi + K_max)",
            "instruction": "Diagram showing incoming photon energy hf splitting into surface work function Phi and escaping kinetic energy K_max."
        }),
        # Page 3
        (3, "Stopping Potential ($V_s$) Mechanics ($K_{\max} = e V_s$)", "definition_card", "definition_card", 1, {
            "term": "Stopping Potential (V_s)",
            "definition": "The minimum negative retarding potential applied to the anode collector plate required to halt even the fastest-moving photoelectrons, reducing photoelectric current to zero."
        }),
        (3, "Stopping Potential ($V_s$) Mechanics ($K_{\max} = e V_s$)", "concept_explanation", "concept_explanation", 2, {
            "text": "### Measuring $K_{\\max}$ Experimentally:\nBecause photoelectrons fly off inside a glass vacuum tube, we cannot measure their speed directly with a speedometer. Instead, we apply a negative reverse potential (retarding voltage) to the collector anode plate.\n\nAs the anode is made more negative, it repels incoming negative electrons. When retarding potential reaches **Stopping Potential ($V_s$)**, electrostatic work done stopping the fastest electron equals its maximum kinetic energy:\n$$K_{\\max} = \\frac{1}{2} m_e v_{\\max}^2 = e V_s$$\n- Substituting into Einstein's equation gives: $$e V_s = h f - \\Phi \\implies V_s = \\left(\\frac{h}{e}\\right) f - \\frac{\\Phi}{e}$$"
        }),
        (3, "Stopping Potential ($V_s$) Mechanics ($K_{\max} = e V_s$)", "suggested_diagram", "suggested_diagram", 3, {
            "text": "Retarding Potential Circuit Diagram Showing Electron Stopping Turning Point at V_s",
            "instruction": "Circuit diagram showing reverse potential supply decelerating photoelectrons to zero current at stopping voltage V_s."
        }),
        # Page 4
        (4, "Millikan's Experiment & Determination of $h$", "concept_explanation", "concept_explanation", 1, {
            "text": "### Robert Millikan's Experimental Proof (1916):\nAmerican physicist Robert Millikan set out to disprove Einstein's photon hypothesis by measuring stopping potential $V_s$ for clean sodium, potassium, and lithium surfaces across various monochromatic light frequencies.\n\nTo his surprise, Millikan's experimental plots of $V_s$ against frequency $f$ yielded perfect straight lines with identical slope $\\frac{h}{e}$, confirming Einstein's photoelectric equation beyond doubt and yielding an accurate experimental value for Planck's constant ($h = 6.57 \\times 10^{-34}\\text{ J s}$)!"
        }),
        # Page 5
        (5, "Millikan Graph Analysis ($V_s$ vs $f$)", "suggested_diagram", "suggested_diagram", 1, {
            "text": "Millikan Graph of Stopping Potential V_s Against Light Frequency f",
            "instruction": "Graph showing straight lines for different metals with slope h/e, frequency axis intercept f_0, and vertical intercept -Phi/e."
        }),
        # Page 6
        (6, "Vacuum Photoemissive Cells (Photocells)", "concept_explanation", "concept_explanation", 1, {
            "text": "### Construction & Operation of a Photocell:\nA **Photocell (Photoemissive Cell)** consists of an evacuated glass bulb containing two electrodes:\n1. **Curved Cathode ($C$)**: A semicylindrical metal plate coated with low work-function alkali material (Cesium/Potassium oxide).\n2. **Anode Ring ($A$)**: A central thin wire rod that collects emitted photoelectrons without casting a shadow on the cathode.\n\nWhen light strikes the cathode, emitted photoelectrons are attracted to the positive anode ring, creating a current proportional to light intensity."
        }),
        (6, "Vacuum Photoemissive Cells (Photocells)", "suggested_diagram", "suggested_diagram", 2, {
            "text": "Vacuum Photoemissive Cell Anatomy: Curved Alkali Cathode and Central Wire Anode Ring",
            "instruction": "Diagram showing evacuated glass bulb photocell with curved cathode plate and central anode wire."
        }),
        (6, "Vacuum Photoemissive Cells (Photocells)", "suggested_image", "suggested_image", 3, {
            "text": "Vacuum Photoemissive Cell Hardware Component"
        }),
        # Page 7
        (7, "Photovoltaic Solar Cells (P-N Junctions)", "concept_explanation", "concept_explanation", 1, {
            "text": "### Direct Conversion of Sunlight into Electricity:\nUnlike vacuum photocells, modern **Photovoltaic (PV) Solar Cells** use semiconductor p-n junctions.\n\nWhen sunlight photons strike the thin n-type top silicon layer, photon energy creates electron-hole pairs. The built-in electric field at the p-n junction sweeps free electrons to the negative terminal and holes to the positive terminal, driving direct current (DC) through external loads!"
        }),
        (7, "Photovoltaic Solar Cells (P-N Junctions)", "suggested_diagram", "suggested_diagram", 2, {
            "text": "Photovoltaic Solar Cell P-N Junction Electron-Hole Pair Generation Schematic",
            "instruction": "Diagram showing sunlight photons creating electron-hole pairs across silicon p-n junction."
        }),
        (7, "Photovoltaic Solar Cells (P-N Junctions)", "suggested_image", "suggested_image", 3, {
            "text": "Silicon Photovoltaic Solar Panel Array"
        }),
        # Page 8
        (8, "Industrial Applications of Photocells", "concept_explanation", "concept_explanation", 1, {
            "text": "### Practical Applications of Photocells:\n1. **Automatic Burglar Alarms**: An invisible infrared beam shines continuously onto a photocell. When an intruder blocks the beam, photocell current drops to zero, triggering an alarm relay.\n2. **Cinematography Film Soundtrack Readers**: Motion picture film has an optical audio track printed along its edge. Light passing through the variable-density track hits a photocell, converting light fluctuations into audio signals.\n3. **Photography Light Meters**: Measures ambient light intensity to automatically adjust camera shutter speed and aperture."
        }),
        # Page 9
        (9, "Knowledge Check: Einstein Equation", "knowledge_check", "knowledge_check", 1, {
            "question": "In the stopping potential equation V_s = (h/e) f - (Phi/e), what physical quantity is represented by the SLOPE of the V_s vs f graph?",
            "options": ["Work function Phi", "Threshold frequency f_0", "Ratio of Planck's constant to electron charge (h/e)", "Speed of light c"],
            "answer": "Ratio of Planck's constant to electron charge (h/e)",
            "explanation": "Comparing V_s = (h/e) f - (Phi/e) to straight-line equation y = m x + c shows that the slope m = h/e, which is constant for all metals."
        }),
        (10, "Knowledge Check: Applications", "knowledge_check", "knowledge_check", 2, {
            "question": "What is the primary operational difference between a vacuum photocell and a photovoltaic solar cell?",
            "options": ["Photocells require UV light while solar cells require X-rays", "Photocells use external DC voltage supply to collect photoelectrons, while solar cells generate direct voltage internally from sunlight", "Photocells absorb heat while solar cells emit light", "Photocells emit electrons while solar cells absorb protons"],
            "answer": "Photocells use external DC voltage supply to collect photoelectrons, while solar cells generate direct voltage internally from sunlight",
            "explanation": "Vacuum photocells require external DC biasing to attract photoelectrons to the anode ring, whereas photovoltaic solar cells generate internal electromotive force (EMF) at a p-n junction."
        }),
        # Page 11
        (11, "Module Summary", "summary", "summary", 1, {
            "text": "### Module 9.2 Key Takeaways:\n1. **Einstein's Equation**: $h f = \\Phi + K_{\\max} = h f_0 + e V_s$.\n2. **Stopping Potential**: Retarding voltage $V_s$ halting fastest electrons ($K_{\\max} = e V_s$).\n3. **Millikan Graph**: $V_s$ vs $f$ has slope $\\frac{h}{e}$ and horizontal intercept $f_0$.\n4. **Applications**: Burglar alarms, film soundtrack readers, photography light meters, solar cells."
        }),
        (12, "Module Summary", "key_takeaway", "key_takeaway", 2, {
            "text": "Einstein's photoelectric equation accurately balances photon energy against work function and stopping potential, enabling modern photocells and solar energy."
        })
    ]

    for p_num, title, btype, ctype, order, content in blocks_m92:
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
    # MODULE 9.3: Quantitative Photo-Electrodynamics, Laboratory Protocols, and Worked Examples
    # -------------------------------------------------------------------------
    unit_3, _ = LearningUnit.objects.get_or_create(
        topic=topic, order=3,
        defaults={"name": "Module 9.3: Quantitative Photo-Electrodynamics, Laboratory Protocols, and Worked Examples"}
    )
    lesson_3, _ = Lesson.objects.get_or_create(
        topic=topic,
        learning_unit=unit_3,
        defaults={"title": "Quantitative Photo-Electrodynamics, Laboratory Protocols, and Worked Examples", "status": "published", "version": 1}
    )
    lesson_3.blocks.all().delete()

    blocks_m93 = [
        # Page 1
        (1, "Governing Mathematics 1: Einstein's Energy Balance", "formula_breakdown", "formula_breakdown", 1, {
            "formula": "E = h f = \\Phi + K_{\\max} = h f_0 + e V_s = h f_0 + \\frac{1}{2} m_e v_{\\max}^2",
            "variables": {
                "E": "Incoming photon energy (Joules or eV)",
                "h": "Planck's constant (6.63 x 10^-34 J s)",
                "f": "Light frequency (Hertz)",
                "Phi": "Work function (Joules or eV)",
                "K_max": "Maximum kinetic energy (Joules)",
                "V_s": "Stopping potential (Volts)",
                "v_max": "Maximum photoelectron speed (m/s)"
            }
        }),
        (1, "Governing Mathematics 1: Einstein's Energy Balance", "suggested_diagram", "suggested_diagram", 2, {
            "text": "1-to-1 Photon-Electron Collision Energy Transfer Vector Diagram",
            "instruction": "Vector diagram showing single photon collision transferring total energy hf to bound electron."
        }),
        # Page 2
        (2, "Governing Mathematics 2: Work Function & Wavelength Conversions", "formula_breakdown", "formula_breakdown", 1, {
            "formula": "\\Phi = h f_0 = \\frac{h c}{\\lambda_0}, \\quad 1\\text{ eV} = 1.6 \\times 10^{-19}\\text{ Joules}",
            "variables": {
                "Phi": "Work function energy barrier",
                "f_0": "Threshold frequency (Hz)",
                "lambda_0": "Maximum threshold wavelength (m)",
                "c": "Speed of light (3.0 x 10^8 m/s)"
            }
        }),
        # Page 3
        (3, "Millikan Slope-Intercept Linear Equations", "concept_explanation", "concept_explanation", 1, {
            "text": "### Linear Plot Parameters:\nComparing $V_s = \\left(\\frac{h}{e}\\right) f - \\frac{\\Phi}{e}$ to $y = m x + c$:\n- **Vertical Axis ($y$)**: Stopping Potential $V_s$ (Volts).\n- **Horizontal Axis ($x$)**: Light Frequency $f$ (Hz).\n- **Slope ($m$)**: Constant ratio $\\frac{h}{e} = 4.14 \\times 10^{-15}\\text{ V s}$.\n- **X-Intercept ($y = 0$)**: Threshold Frequency $f_0$.\n- **Y-Intercept ($x = 0$)**: Negative potential $-\\frac{\\Phi}{e}$."
        }),
        # Page 4
        (4, "Worked Example Level 1 — Direct Work Function Calculation", "worked_example", "worked_example", 1, {
            "problem": "The threshold frequency of a clean potassium surface is $5.46 \\times 10^{14}\\text{ Hz}$. Calculate the work function of potassium in: 1. Joules, 2. Electron-volts (eV). (Take $h = 6.63 \\times 10^{-34}\\text{ J s}$, $1\\text{ eV} = 1.6 \\times 10^{-19}\\text{ J}$).",
            "steps": [
                "Step 1: Knowns: Threshold frequency $f_0 = 5.46 \\times 10^{14}\\text{ Hz}$, $h = 6.63 \\times 10^{-34}\\text{ J s}$.",
                "Step 2: Required: Work function $\\Phi$ in Joules and eV.",
                "Step 3: Equation: $\\Phi = h f_0$.",
                "Step 4: Calculation in Joules: $\\Phi = (6.63 \\times 10^{-34}) \\times (5.46 \\times 10^{14}) = 3.62 \\times 10^{-19}\\text{ Joules}$.",
                "Step 5: Convert to eV: $\\Phi = \\frac{3.62 \\times 10^{-19}\\text{ J}}{1.6 \\times 10^{-19}\\text{ J/eV}} = 2.26\\text{ eV}$."
            ]
        }),
        # Page 5
        (5, "Worked Example Level 2 — Maximum Kinetic Energy & Ejection Speed", "worked_example", "worked_example", 1, {
            "problem": "Ultraviolet light of wavelength $\\lambda = 250\\text{ nm}$ ($2.5 \\times 10^{-7}\\text{ m}$) illuminates a sodium surface having a work function of $2.28\\text{ eV}$ ($3.65 \\times 10^{-19}\\text{ J}$). Calculate the maximum kinetic energy $K_{\\max}$ of emitted photoelectrons.",
            "steps": [
                "Step 1: Knowns: $\\lambda = 2.5 \\times 10^{-7}\\text{ m}$, $\\Phi = 3.65 \\times 10^{-19}\\text{ J}$, $h = 6.63 \\times 10^{-34}\\text{ J s}$, $c = 3.0 \\times 10^8\\text{ m/s}$.",
                "Step 2: Calculate incoming photon energy $E = \\frac{h c}{\\lambda} = \\frac{(6.63 \\times 10^{-34}) \\times (3.0 \\times 10^8)}{2.5 \\times 10^{-7}} = 7.956 \\times 10^{-19}\\text{ Joules}$.",
                "Step 3: Calculate $K_{\\max} = E - \\Phi = 7.956 \\times 10^{-19} - 3.65 \\times 10^{-19} = 4.31 \\times 10^{-19}\\text{ Joules}$.",
                "Step 4: Convert to eV: $K_{\\max} = \\frac{4.31 \\times 10^{-19}}{1.6 \\times 10^{-19}} = 2.69\\text{ eV}$."
            ]
        }),
        # Page 6
        (6, "Worked Example Level 3 — Stopping Potential Determination", "worked_example", "worked_example", 1, {
            "problem": "Light of frequency $8.0 \\times 10^{14}\\text{ Hz}$ strikes a metal cathode having a work function of $2.0\\text{ eV}$ ($3.2 \\times 10^{-19}\\text{ J}$). Calculate the stopping potential $V_s$ required to reduce photoelectric current to zero.",
            "steps": [
                "Step 1: Knowns: $f = 8.0 \\times 10^{14}\\text{ Hz}$, $\\Phi = 3.2 \\times 10^{-19}\\text{ J}$, $e = 1.6 \\times 10^{-19}\\text{ C}$, $h = 6.63 \\times 10^{-34}\\text{ J s}$.",
                "Step 2: Incoming photon energy $E = h f = (6.63 \\times 10^{-34}) \\times (8.0 \\times 10^{14}) = 5.304 \\times 10^{-19}\\text{ Joules}$.",
                "Step 3: Maximum kinetic energy $K_{\\max} = E - \\Phi = 5.304 \\times 10^{-19} - 3.2 \\times 10^{-19} = 2.104 \\times 10^{-19}\\text{ Joules}$.",
                "Step 4: Stopping potential $V_s = \\frac{K_{\\max}}{e} = \\frac{2.104 \\times 10^{-19}\\text{ J}}{1.6 \\times 10^{-19}\\text{ C}} = 1.315\\text{ Volts}$."
            ]
        }),
        # Page 7
        (7, "Worked Example Level 4 — Millikan Graph Interpretation", "worked_example", "worked_example", 1, {
            "problem": "In a photoelectric experiment, a plot of stopping potential $V_s$ against frequency $f$ gives a straight line intersecting the frequency axis at $f_0 = 4.50 \\times 10^{14}\\text{ Hz}$ with a slope of $4.12 \\times 10^{-15}\\text{ V s}$. Determine: 1. Experimental value of Planck's constant $h$. 2. Work function $\\Phi$ of the metal.",
            "steps": [
                "Step 1: Slope $m = \\frac{h}{e} = 4.12 \\times 10^{-15}\\text{ V s}$.",
                "Step 2: Calculate $h = m \\times e = (4.12 \\times 10^{-15}) \\times (1.60 \\times 10^{-19}) = 6.59 \\times 10^{-34}\\text{ J s}$.",
                "Step 3: Calculate work function $\\Phi = h f_0 = (6.59 \\times 10^{-34}) \\times (4.50 \\times 10^{14}) = 2.97 \\times 10^{-19}\\text{ J} = 1.85\\text{ eV}$."
            ]
        }),
        # Page 8
        (8, "Worked Example Level 5 — Challenge Multi-Step (Photocell Current & Photons/sec)", "worked_example", "worked_example", 1, {
            "problem": "A photocell with a quantum efficiency of $5.0\\%$ is illuminated by monochromatic light of wavelength $\\lambda = 400\\text{ nm}$ ($4.0 \\times 10^{-7}\\text{ m}$) delivering a light power of $10.0\\text{ mW}$ ($0.010\\text{ W}$). Calculate: 1. Number of photons hitting the photocell per second. 2. Saturation photoelectric current produced.",
            "steps": [
                "Step 1: Single photon energy $E = \\frac{hc}{\\lambda} = \\frac{(6.63 \\times 10^{-34}) \\times (3.0 \\times 10^8)}{4.0 \\times 10^{-7}} = 4.9725 \\times 10^{-19}\\text{ Joules}$.",
                "Step 2: Number of incident photons per second $N_{\\text{photon}} = \\frac{P}{E} = \\frac{0.010\\text{ W}}{4.9725 \\times 10^{-19}\\text{ J}} = 2.011 \\times 10^{16}\\text{ photons/sec}$.",
                "Step 3: Number of emitted electrons per second ($5\\%$ efficiency): $N_e = 0.05 \\times (2.011 \\times 10^{16}) = 1.0055 \\times 10^{15}\\text{ electrons/sec}$.",
                "Step 4: Photoelectric current $I = N_e \\times e = (1.0055 \\times 10^{15}) \\times (1.6 \\times 10^{-19}\\text{ C}) = 1.61 \\times 10^{-4}\\text{ A} = 0.161\\text{ mA}$."
            ]
        }),
        # Page 9
        (9, "Laboratory Investigation: Zinc Plate Electroscope Setup", "concept_explanation", "concept_explanation", 1, {
            "text": "### Laboratory Protocol: Zinc Plate Discharge:\n1. **Polishing**: Polish a zinc plate with emery cloth to remove oxide coating.\n2. **Charging**: Touch the zinc plate with a negatively charged ebonite rod so electroscope leaves diverge.\n3. **UV Illumination**: Shine a UV lamp onto the zinc plate. Observe immediate leaf collapse.\n4. **Glass Filter Test**: Interpose a glass sheet between UV lamp and zinc plate. Leaf collapse stops immediately because glass absorbs UV radiation!"
        }),
        (9, "Laboratory Investigation: Zinc Plate Electroscope Setup", "suggested_diagram", "suggested_diagram", 2, {
            "text": "Laboratory Zinc Plate, Electroscope, and UV Lamp Apparatus Setup",
            "instruction": "Diagram showing polished zinc plate, electroscope, UV lamp, and glass filter test."
        }),
        # Page 10
        (10, "Addressing Key Student Misconceptions", "common_misconception", "common_misconception", 1, {
            "text": "### 4 Critical Misconceptions Clarified:\n1. **Intensity vs Frequency**: Intensity governs **how many** electrons escape per second; Frequency governs **how fast** they fly off!\n2. **Time Delay**: There is **NO** energy accumulation delay; photoelectron emission is instantaneous ($< 10^{-9}\\text{ s}$).\n3. **One Photon, One Electron**: One photon cannot split its energy between multiple electrons; it gives 100% to one electron or none.\n4. **Positive Electroscope**: If the zinc plate is positively charged, UV light ejects electrons, making the plate **MORE** positive and causing leaves to diverge further!"
        }),
        # Page 11
        (11, "Assessment Suite", "knowledge_check", "knowledge_check", 1, {
            "question": "A metal has a work function of 2.0 eV. What is the stopping potential when illuminated by photons of energy 3.5 eV?",
            "options": ["1.5 Volts", "5.5 Volts", "2.0 Volts", "0.75 Volts"],
            "answer": "1.5 Volts",
            "explanation": "K_max = E - Phi = 3.5 eV - 2.0 eV = 1.5 eV. Stopping potential V_s = K_max / e = 1.5 Volts."
        }),
        (12, "Assessment Suite", "knowledge_check", "knowledge_check", 2, {
            "question": "Why does interposing a clear glass plate between a UV lamp and a negatively charged zinc plate halt photoelectric discharge?",
            "options": ["Glass absorbs ultraviolet radiation", "Glass conducts electrons back to earth", "Glass reflects visible light", "Glass increases the work function of zinc"],
            "answer": "Glass absorbs ultraviolet radiation",
            "explanation": "Standard glass absorbs UV radiation. Blocking UV photons leaves only visible light, whose frequency is below the threshold frequency of zinc."
        }),
        # Page 13
        (13, "Module Summary", "summary", "summary", 1, {
            "text": "### Module 9.3 Key Takeaways:\n1. **Energy Balance**: $h f = \\Phi + K_{\\max} = h f_0 + e V_s$.\n2. **Linear Plot**: Slope of $V_s$ vs $f$ gives $\\frac{h}{e}$; horizontal intercept gives threshold frequency $f_0$.\n3. **Quantized Interaction**: 1-to-1 photon-electron collision with instantaneous ejection."
        }),
        (14, "Module Summary", "key_takeaway", "key_takeaway", 2, {
            "text": "Topic 9 Complete: The photoelectric effect provides conclusive empirical proof of light quantization, enabling solar panels, security alarms, and optical digital technology."
        })
    ]

    for p_num, title, btype, ctype, order, content in blocks_m93:
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
    print("TOPIC 9 INGESTION COMPLETED SUCCESSFULLY!")
    print("=" * 80)

if __name__ == "__main__":
    run_ingestion()
