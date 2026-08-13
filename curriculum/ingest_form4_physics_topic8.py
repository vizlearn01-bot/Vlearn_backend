"""
VLearn Form 4 Physics — Topic 8: X-Rays
Comprehensive Ingestion Engine (Enriched Deep Text & Visual Architecture)

Modules:
  8.1 Production, Construction, and Properties of X-Rays (10 Pages, 17 Blocks)
  8.2 X-Ray Spectra, Attenuation, and Industrial/Medical Applications (12 Pages, 18 Blocks)
  8.3 Quantitative X-Ray Electrodynamics, Radiation Safety, and Worked Examples (14 Pages, 20 Blocks)

Usage:
  /home/jason-bitega/Desktop/VL/vlearn_repositories/Vlearn_backend/venv/bin/python curriculum/ingest_form4_physics_topic8.py
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
    print("VLEARN FORM 4 PHYSICS — TOPIC 8 INGESTION")
    print("=" * 80)

    curriculum = Curriculum.objects.filter(name="844").first()
    grade = Grade.objects.filter(curriculum=curriculum, name="Form 4").first()
    subject = Subject.objects.filter(grade=grade, name="Physics").first()

    topic, _ = Topic.objects.get_or_create(
        subject=subject,
        order=8,
        defaults={"name": "Topic 8: X-Rays — Production Mechanics, Spectral Analysis, and Applications"}
    )
    topic.name = "Topic 8: X-Rays — Production Mechanics, Spectral Analysis, and Applications"
    topic.save()
    print(f"Topic 8: '{topic.name}' (ID: {topic.id}) ready.")

    # -------------------------------------------------------------------------
    # MODULE 8.1: Production, Construction, and Properties of X-Rays
    # -------------------------------------------------------------------------
    unit_1, _ = LearningUnit.objects.get_or_create(
        topic=topic, order=1,
        defaults={"name": "Module 8.1: Production, Construction, and Properties of X-Rays"}
    )
    lesson_1, _ = Lesson.objects.get_or_create(
        topic=topic,
        learning_unit=unit_1,
        defaults={"title": "Production, Construction, and Properties of X-Rays", "status": "published", "version": 1}
    )
    lesson_1.blocks.all().delete()

    blocks_m81 = [
        # Page 1
        (1, "Physical Intuition: Röntgen's Mysterious Rays", "learning_goal", "learning_goal", 1, {
            "goals": [
                "Understand X-rays as high-frequency electromagnetic radiation produced by fast electron deceleration",
                "Identify the structural components of the modern Coolidge X-ray tube",
                "Differentiate X-ray tube voltage (hardness/quality) from filament current (beam intensity/quantity)"
            ]
        }),
        (1, "Physical Intuition: Röntgen's Mysterious Rays", "concept_explanation", "concept_explanation", 2, {
            "text": "### The Discovery of X-Rays (1895):\nIn November 1895, German physicist Wilhelm Röntgen was experimenting with high-voltage discharge tubes in a darkened laboratory. Although the discharge tube was wrapped in thick black cardboard, a nearby cardboard screen coated with barium platinocyanide began glowing brightly. Röntgen realized that invisible rays emitted from the tube were penetrating solid cardboard.\n\n### Why Are They Called 'X-Rays'?\nBecause their nature was initially unknown, Röntgen called them **X-rays** (where 'X' stands for the unknown mathematical variable). He soon produced the world's first medical radiography image—a shadowgraph showing the bone structure of his wife Bertha's hand!"
        }),
        (1, "Physical Intuition: Röntgen's Mysterious Rays", "suggested_image", "suggested_image", 3, {
            "text": "Historical Röntgen X-Ray Shadowgraph of Bertha Röntgen's Hand (1895)"
        }),
        # Page 2
        (2, "The Modern Coolidge X-Ray Tube", "definition_card", "definition_card", 1, {
            "term": "Coolidge X-Ray Tube",
            "definition": "A highly evacuated glass tube equipped with a thermionic filament cathode and a heavy metal target anode used to produce controllable X-ray beams."
        }),
        (2, "The Modern Coolidge X-Ray Tube", "concept_explanation", "concept_explanation", 2, {
            "text": "### Construction of the Coolidge Tube:\n1. **Evacuated Glass Envelope**: Maintained at ultra-high vacuum ($< 10^{-6}\\text{ mmHg}$) so accelerated electrons travel unimpeded without colliding with air molecules.\n2. **Cathode Assembly**: A tungsten filament enclosed in a concave focusing cup. When heated by a low-voltage supply ($6-12\\text{ V}$), it liberates free electrons via thermionic emission.\n3. **Anode Target**: A slanted block of tungsten or molybdenum embedded in a heavy copper stem. Accelerated electrons strike the tungsten target at a $45^\\circ$ angle, emitting X-rays out of a side window."
        }),
        (2, "The Modern Coolidge X-Ray Tube", "suggested_diagram", "suggested_diagram", 3, {
            "text": "Complete Construction Schematic of the Modern Coolidge X-Ray Tube",
            "instruction": "Diagram showing Coolidge tube with filament cathode, tungsten target anode, copper block, cooling fins, and high-voltage supply."
        }),
        (2, "The Modern Coolidge X-Ray Tube", "suggested_image", "suggested_image", 4, {
            "text": "Coolidge X-Ray Tube Glass Hardware Construction Unit"
        }),
        # Page 3
        (3, "Anode Target Physics & Thermal Dissipation", "concept_explanation", "concept_explanation", 1, {
            "text": "### Why Tungsten and Copper Are Used:\n- **Tungsten Target Target Material**: Tungsten has an extremely high melting point ($3,422^\\circ\\text{C}$) and a high atomic number ($Z = 74$). High atomic mass maximizes electron deceleration, producing intense X-rays without melting the anode.\n- **Copper Cooling Stem & Radiator Fins**: Over $99\\%$ of electron kinetic energy hitting the target converts into thermal heat energy, while **less than $1\\%$** converts into useful X-rays! Solid copper is an excellent thermal conductor, conducting heat rapidly away to external cooling fins or oil circulators."
        }),
        (3, "Anode Target Physics & Thermal Dissipation", "suggested_diagram", "suggested_diagram", 2, {
            "text": "Anode Target Energy Conversion and Copper Thermal Conduction Cooling Mechanism",
            "instruction": "Diagram showing tungsten target embedded in copper block with oil cooling circulator and radiator fins."
        }),
        # Page 4
        (4, "Energy Conversion Physics ($99\\%$ Heat vs $1\\%$ X-Rays)", "concept_explanation", "concept_explanation", 1, {
            "text": "### Energy Conservation in the X-Ray Tube:\n1. **Electrical Potential Work**: Electrostatic acceleration gives electrons kinetic energy: $$E_k = e V_{\\text{acc}}$$\n2. **Target Collision Energy Partition**: Upon striking the tungsten target:\n   - **$> 99\\%$ of $E_k$** $\\rightarrow$ Converted into lattice thermal vibrations (Heat energy).\n   - **$< 1\\%$ of $E_k$** $\\rightarrow$ Converted into high-frequency X-ray electromagnetic photons ($E = h f$).\n\n### Maximum X-Ray Photon Energy:\nWhen an electron loses ALL its kinetic energy in a single collision with a target nucleus: $$e V_{\\text{acc}} = h f_{\\max} = \\frac{h c}{\\lambda_{\\min}}$$"
        }),
        (4, "Energy Conversion Physics ($99\\%$ Heat vs $1\\%$ X-Rays)", "suggested_diagram", "suggested_diagram", 2, {
            "text": "X-Ray Anode Energy Partition: 99% Thermal Heat vs 1% X-Ray Photon Generation",
            "instruction": "Pie chart and energy transformation flow diagram illustrating 99% heat loss vs 1% X-ray conversion."
        }),
        # Page 5
        (5, "The Eight Fundamental Properties of X-Rays", "step_process", "step_process", 1, {
            "steps": [
                "**1. Electromagnetic Nature**: X-rays are high-frequency electromagnetic waves with zero rest mass and zero electrical charge ($\lambda \\approx 10^{-10}\\text{ m} = 0.1\\text{ nm}$).",
                "**2. Speed of Light**: X-rays travel through vacuum at the speed of light ($c = 3.0 \\times 10^8\\text{ m/s}$).",
                "**3. Unaffected by Fields**: Because X-rays carry no electrical charge, they pass through electric and magnetic fields in straight lines without any deflection.",
                "**4. High Penetrating Power**: X-rays penetrate opaque solid matter (soft tissue, wood, thin metal) that blocks visible light.",
                "**5. High Ionizing Ability**: X-ray photons knock electrons out of gas atoms, turning neutral air molecules into positive ions and free electrons.",
                "**6. Fluorescence**: X-rays cause materials like zinc sulphide and barium platinocyanide to glow brightly with visible light.",
                "**7. Photographic Exposure**: X-rays fog photographic film and digital detector plates upon impact.",
                "**8. Biological Hazard**: X-rays break chemical bonds in DNA molecules, posing radiation risks (tissue damage, cell mutation, and cancer)."
            ]
        }),
        # Page 6
        (6, "Hard X-Rays vs. Soft X-Rays", "concept_explanation", "concept_explanation", 1, {
            "text": "### Categorizing X-Rays by Energy & Penetration:\n- **Hard X-Rays**: Produced at very high accelerating voltages ($> 50\\text{ kV}$). They have high frequencies ($f$), short wavelengths ($\lambda$), and high photon energies ($E = hf$). They possess **high penetrating power**, passing easily through soft tissue and bone, making them ideal for radiotherapy and industrial weld testing.\n- **Soft X-Rays**: Produced at lower accelerating voltages ($10-30\\text{ kV}$). They have longer wavelengths, lower energies, and **low penetrating power**. They are easily absorbed by skin and soft tissue, making them useful for mammography and surface tissue imaging."
        }),
        # Page 7
        (7, "Control Mechanisms: Hardness vs. Intensity", "concept_explanation", "concept_explanation", 1, {
            "text": "### How to Control an X-Ray Machine:\nTwo independent controls govern the output of a Coolidge X-ray tube:\n\n1. **Quality / Hardness (Penetrating Power)**: Controlled by adjusting the **High Accelerating Voltage ($V_{\\text{acc}}$)** across the tube. Higher voltage increases electron kinetic energy, producing shorter minimum wavelengths ($\\lambda_{\\min} = \\frac{hc}{eV}$) and harder X-rays.\n2. **Quantity / Intensity (Brightness / Beam Density)**: Controlled by adjusting the **Filament Heating Current ($I_f$)**. Higher filament current increases cathode temperature, releasing more electrons per second via thermionic emission, creating a denser beam of X-rays without altering their individual photon energy!"
        }),
        (7, "Control Mechanisms: Hardness vs. Intensity", "suggested_diagram", "suggested_diagram", 2, {
            "text": "Independent Control Mechanisms: Accelerating Voltage (Hardness) vs. Filament Current (Intensity)",
            "instruction": "Diagram showing dual control knobs: voltage controlling wavelength hardness vs filament current controlling photon flux intensity."
        }),
        # Page 8
        (8, "Interactive X-Ray Tube Sandbox", "suggested_simulation", "suggested_simulation", 1, {
            "text": "Interactive X-Ray Tube Sandbox: Parameter Controls and Real-Time Energy Spectrum"
        }),
        # Page 9
        (9, "Knowledge Check: X-Ray Fundamentals", "knowledge_check", "knowledge_check", 1, {
            "question": "Which adjustment increases the PENETRATING POWER (hardness) of an X-ray beam without altering photon quantity?",
            "options": ["Increasing the filament heating current", "Increasing the high accelerating anode potential (V_acc)", "Increasing the target cooling oil flow rate", "Decreasing cathode temperature"],
            "answer": "Increasing the high accelerating anode potential (V_acc)",
            "explanation": "Increasing accelerating voltage V_acc gives electrons higher kinetic energy (e V_acc), creating higher-frequency, shorter-wavelength X-rays with greater penetrating power."
        }),
        (9, "Knowledge Check: X-Ray Fundamentals", "knowledge_check", "knowledge_check", 2, {
            "question": "Why is solid copper used as the anode stem in an X-ray tube?",
            "options": ["To focus the electron beam", "To absorb high-energy X-rays", "To rapidly conduct away the 99% thermal heat generated at the target", "To increase X-ray frequency"],
            "answer": "To rapidly conduct away the 99% thermal heat generated at the target",
            "explanation": "Over 99% of electron energy converts to heat. Copper's high thermal conductivity rapidly transfers heat to external cooling radiators."
        }),
        # Page 10
        (10, "Module Summary", "summary", "summary", 1, {
            "text": "### Module 8.1 Key Takeaways:\n1. **X-Ray Production**: High-speed thermionic electrons strike a high-melting-point tungsten target in vacuum.\n2. **Heat Loss**: $> 99\\%$ of kinetic energy becomes heat; $< 1\\%$ becomes X-ray photons.\n3. **Properties**: High frequency, zero charge, un-deflected by E & B fields, ionizing, fluorescing.\n4. **Controls**: Voltage controls hardness ($\lambda_{\\min}$); Filament current controls intensity (photon quantity)."
        }),
        (10, "Module Summary", "key_takeaway", "key_takeaway", 2, {
            "text": "X-rays are high-frequency EM waves produced by rapid electron deceleration, with voltage controlling hardness and filament current controlling intensity."
        })
    ]

    for p_num, title, btype, ctype, order, content in blocks_m81:
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
    # MODULE 8.2: X-Ray Spectra, Attenuation, and Industrial/Medical Applications
    # -------------------------------------------------------------------------
    unit_2, _ = LearningUnit.objects.get_or_create(
        topic=topic, order=2,
        defaults={"name": "Module 8.2: X-Ray Spectra, Attenuation, and Industrial/Medical Applications"}
    )
    lesson_2, _ = Lesson.objects.get_or_create(
        topic=topic,
        learning_unit=unit_2,
        defaults={"title": "X-Ray Spectra, Attenuation, and Industrial/Medical Applications", "status": "published", "version": 1}
    )
    lesson_2.blocks.all().delete()

    blocks_m82 = [
        # Page 1
        (1, "Continuous X-Ray Spectrum (Bremsstrahlung)", "learning_goal", "learning_goal", 1, {
            "goals": [
                "Explain the origin of the continuous X-ray spectrum as Bremsstrahlung (braking radiation)",
                "Calculate minimum cutoff wavelength $\\lambda_{\\min}$ using the Duane-Hunt law",
                "Describe industrial non-destructive testing and diagnostic medical radiography applications"
            ]
        }),
        (1, "Continuous X-Ray Spectrum (Bremsstrahlung)", "concept_explanation", "concept_explanation", 2, {
            "text": "### Origin of the Continuous Spectrum:\nWhen high-speed electrons penetrate the tungsten target, they pass close to positively charged tungsten atomic nuclei. Electrostatic attraction decelerates (brakes) the electrons, causing them to lose kinetic energy. The lost energy is emitted as X-ray photons.\n\n### Bremsstrahlung ('Braking Radiation'):\nBecause different electrons undergo varying degrees of deceleration in multiple random collisions, they emit photons over a continuous band of wavelengths. This forms a smooth background curve known as the **Continuous X-Ray Spectrum**."
        }),
        (1, "Continuous X-Ray Spectrum (Bremsstrahlung)", "suggested_diagram", "suggested_diagram", 3, {
            "text": "Bremsstrahlung Continuous X-Ray Intensity vs Wavelength Graph Showing Cutoff Wavelength",
            "instruction": "Graph of X-ray intensity against wavelength showing a smooth continuous curve with sharp minimum cutoff wavelength lambda_min."
        }),
        # Page 2
        (2, "Characteristic X-Ray Spectrum & Atomic Transitions", "concept_explanation", "concept_explanation", 1, {
            "text": "### Origin of Characteristic X-Ray Peaks:\nWhen accelerating voltage is sufficiently high, an incoming electron collides directly with an inner-shell electron (such as the K-shell or L-shell) of a target tungsten atom, knocking it out of the atom.\n\n### Electronic Relaxation:\nAn electron from an outer shell (L-shell or M-shell) immediately drops down to fill the vacant inner orbital. As it transitions to a lower energy state, it emits a photon with an exact discrete energy equal to the energy gap between the two shells ($h f = E_{\\text{outer}} - E_{\\text{inner}}$). These produce sharp intensity spikes superimposed on the continuous spectrum called **Characteristic X-Rays**!"
        }),
        (2, "Characteristic X-Ray Spectrum & Atomic Transitions", "suggested_diagram", "suggested_diagram", 2, {
            "text": "Inner Shell K-Shell and L-Shell Electronic Transition Energy Level Diagram",
            "instruction": "Diagram showing electron ejection from K-shell and outer electron falling down to emit characteristic X-ray photon."
        }),
        # Page 3
        (3, "Duane-Hunt Law & Cutoff Wavelength Mechanics", "formula_breakdown", "formula_breakdown", 1, {
            "formula": "\\lambda_{\\min} = \\frac{h c}{e V_{\\text{acc}}} = \\frac{1.24 \\times 10^{-6}}{V_{\\text{acc}}} \\text{ meters}",
            "variables": {
                "lambda_min": "Minimum cutoff wavelength of X-ray spectrum (meters)",
                "h": "Planck's constant (6.63 x 10^-34 J s)",
                "c": "Speed of light (3.0 x 10^8 m/s)",
                "e": "Electron charge (1.6 x 10^-19 C)",
                "V_acc": "Accelerating voltage applied across X-ray tube (Volts)"
            }
        }),
        (3, "Duane-Hunt Law & Cutoff Wavelength Mechanics", "concept_explanation", "concept_explanation", 2, {
            "text": "### The Duane-Hunt Cutoff Limit:\nNotice that every X-ray spectral curve drops abruptly to zero intensity at a sharp lower wavelength limit called **\\$\\lambda_{\\min}\\$**.\n- **Physics Meaning**: $\\lambda_{\\min}$ corresponds to a maximum energy photon ($E_{\\max} = h f_{\\max}$) produced when an electron transfers **100% of its kinetic energy** in a single head-on collision!\n- **Key Relationship**: $\\lambda_{\\min}$ depends **ONLY** on the accelerating voltage $V_{\\text{acc}}$. It is independent of the target material!"
        }),
        # Page 4
        (4, "X-Ray Attenuation & Linear Absorption ($I = I_0 e^{-\\mu x}$)", "concept_explanation", "concept_explanation", 1, {
            "text": "### How X-Rays Interact with Matter:\nAs an X-ray beam passes through a medium, its intensity decreases exponentially due to photoelectric absorption and Compton scattering.\n\n### The Exponential Attenuation Law:\n$$I = I_0 e^{-\\mu x}$$\n- $I_0$: Initial un-attenuated X-ray intensity entering material.\n- $I$: Transmitted intensity after passing through thickness $x$.\n- $\\mu$: **Linear Attenuation Coefficient** of the material (depends on material density $\\rho$ and atomic number $Z$). Bone ($Z_{\\text{effective}} \\approx 13.8$) has a much higher $\\mu$ than soft muscle tissue ($Z_{\\text{effective}} \\approx 7.4$), creating high contrast on radiograph film!"
        }),
        (4, "X-Ray Attenuation & Linear Absorption ($I = I_0 e^{-\\mu x}$)", "suggested_diagram", "suggested_diagram", 2, {
            "text": "Exponential X-Ray Beam Attenuation Graph for Soft Tissue, Bone, and Lead Shielding",
            "instruction": "Diagram showing exponential decay curve of X-ray intensity passing through lead, bone, and soft tissue."
        }),
        # Page 5
        (5, "Diagnostic Medical Radiography", "concept_explanation", "concept_explanation", 1, {
            "text": "### Medical Applications of X-Rays:\n1. **Bone Fracture Detection**: Dense bone tissue contains calcium ($Z = 20$), which absorbs X-rays strongly. Soft tissue passes most X-rays. Unexposed film behind bones remains dark/white, while exposed film behind soft tissue turns black, revealing fracture lines sharply.\n2. **Barium Meal Examinations**: To visualize the digestive tract (stomach/intestines), a patient swallows a insoluble barium sulphate suspension ($Z = 56$). Barium absorbs X-rays strongly, highlighting ulcers and tumors on radiographs.\n3. **Dental Radiography**: Inspects tooth decay, root canal structures, and jawbone density."
        }),
        (5, "Diagnostic Medical Radiography", "suggested_image", "suggested_image", 2, {
            "text": "Medical Chest Radiography X-Ray Film Image"
        }),
        # Page 6
        (6, "Computed Tomography (CT Scans)", "concept_explanation", "concept_explanation", 1, {
            "text": "### 3D Cross-Sectional Imaging:\nStandard 2D radiography overlaps anatomical structures. A **Computed Tomography (CT) Scanner** rotates an X-ray tube and digital detector array $360^\\circ$ around the patient.\n\nA computer processes thousands of narrow 2D attenuation measurements to reconstruct detailed 3D cross-sectional slice images of internal organs, brain tissue, blood vessels, and soft tissue tumors with millimeter precision."
        }),
        # Page 7
        (7, "Industrial Non-Destructive Testing (NDT)", "concept_explanation", "concept_explanation", 1, {
            "text": "### Industrial Applications:\n1. **Weld & Casting Inspection**: High-energy hard X-rays penetrate thick steel pipes and aircraft wing joints to detect internal microscopic air bubbles, cracks, and metal fatigue without damaging the structure.\n2. **Airport Security Luggage Scanners**: Multi-energy X-rays scan baggage to distinguish dense metallic weapons from organic explosives based on differential atomic number absorption.\n3. **Thickness Control**: Metal rolling mills use X-ray transmission gauges to monitor and maintain uniform steel sheet thickness in real time."
        }),
        # Page 8
        (8, "Crystallography & Bragg's Law ($2d \\sin\\theta = n\\lambda$)", "concept_explanation", "concept_explanation", 1, {
            "text": "### X-Ray Diffraction in Crystals:\nBecause X-ray wavelengths ($\lambda \\approx 0.1\\text{ nm}$) match atomic spacing in crystal lattices, crystals act as natural 3D diffraction gratings.\n\n### Bragg's Law of Diffraction:\nWhen X-rays reflect off parallel crystal planes separated by interplanar distance $d$:\n$$2 d \\sin\\theta = n \\lambda$$\nMeasuring diffraction angle $\\theta$ allows scientists to determine the precise 3D atomic arrangement of molecules (used by Rosalind Franklin, Watson, and Crick to discover DNA double helix structure!)."
        }),
        (8, "Crystallography & Bragg's Law ($2d \\sin\\theta = n\\lambda$)", "suggested_diagram", "suggested_diagram", 2, {
            "text": "Bragg's Law X-Ray Crystal Lattice Diffraction Geometry",
            "instruction": "Diagram showing X-rays reflecting off parallel atomic crystal planes separated by distance d with path difference 2d sin theta."
        }),
        # Page 9
        (9, "Knowledge Check: X-Ray Spectra", "knowledge_check", "knowledge_check", 1, {
            "question": "What determines the MINIMUM CUTOFF WAVELENGTH (lambda_min) in a continuous X-ray spectrum?",
            "options": ["Target material atomic number", "Filament heating current", "Accelerating anode voltage (V_acc)", "Tube glass envelope thickness"],
            "answer": "Accelerating anode voltage (V_acc)",
            "explanation": "According to the Duane-Hunt law, lambda_min = hc / (e V_acc). It depends exclusively on accelerating voltage V_acc."
        }),
        (10, "Knowledge Check: Attenuation", "knowledge_check", "knowledge_check", 2, {
            "question": "Why do bones appear bright white on a standard medical radiography X-ray film?",
            "options": ["Bones emit visible light when struck by X-rays", "Bones absorb X-rays strongly due to high calcium density, leaving film unexposed", "Bones reflect X-rays back to the source", "Bones accelerate X-rays through tissue"],
            "answer": "Bones absorb X-rays strongly due to high calcium density, leaving film unexposed",
            "explanation": "Calcium in bones absorbs X-rays via photoelectric effect, preventing them from reaching the photographic film behind, leaving a bright unexposed region."
        }),
        # Page 11
        (11, "Module Summary", "summary", "summary", 1, {
            "text": "### Module 8.2 Key Takeaways:\n1. **Continuous Spectrum**: Bremsstrahlung braking radiation with cutoff $\\lambda_{\\min} = \\frac{hc}{eV}$.\n2. **Characteristic Spectrum**: Discrete spectral peaks caused by inner shell electron knockouts and outer electron relaxation.\n3. **Attenuation**: Exponential absorption $I = I_0 e^{-\\mu x}$ based on density $\\rho$ and atomic number $Z$.\n4. **Applications**: Medical radiography, CT scans, industrial NDT weld testing, Bragg crystallography."
        }),
        (12, "Module Summary", "key_takeaway", "key_takeaway", 2, {
            "text": "X-ray spectra feature continuous braking radiation bounded by Duane-Hunt cutoff wavelength, alongside sharp characteristic atomic peaks."
        })
    ]

    for p_num, title, btype, ctype, order, content in blocks_m82:
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
    # MODULE 8.3: Quantitative X-Ray Electrodynamics, Radiation Safety, and Worked Examples
    # -------------------------------------------------------------------------
    unit_3, _ = LearningUnit.objects.get_or_create(
        topic=topic, order=3,
        defaults={"name": "Module 8.3: Quantitative X-Ray Electrodynamics, Radiation Safety, and Worked Examples"}
    )
    lesson_3, _ = Lesson.objects.get_or_create(
        topic=topic,
        learning_unit=unit_3,
        defaults={"title": "Quantitative X-Ray Electrodynamics, Radiation Safety, and Worked Examples", "status": "published", "version": 1}
    )
    lesson_3.blocks.all().delete()

    blocks_m83 = [
        # Page 1
        (1, "Governing Mathematics 1: Duane-Hunt Law", "formula_breakdown", "formula_breakdown", 1, {
            "formula": "e V_{\\text{acc}} = h f_{\\max} = \\frac{h c}{\\lambda_{\\min}} \\implies \\lambda_{\\min} = \\frac{h c}{e V_{\\text{acc}}}",
            "variables": {
                "e": "Electron charge (1.6 x 10^-19 Coulombs)",
                "V_acc": "Accelerating tube voltage (Volts)",
                "h": "Planck's constant (6.63 x 10^-34 J s)",
                "c": "Speed of light (3.0 x 10^8 m/s)",
                "lambda_min": "Minimum cutoff wavelength (meters)",
                "f_max": "Maximum X-ray photon frequency (Hertz)"
            }
        }),
        (1, "Governing Mathematics 1: Duane-Hunt Law", "suggested_diagram", "suggested_diagram", 2, {
            "text": "Inverse Relationship Graph Between Accelerating Voltage and Minimum Cutoff Wavelength",
            "instruction": "Graph showing inverse curve of minimum cutoff wavelength lambda_min vs accelerating voltage V_acc."
        }),
        # Page 2
        (2, "Governing Mathematics 2: Tube Power & Thermal Heat Loss Rate", "formula_breakdown", "formula_breakdown", 1, {
            "formula": "P_{\\text{input}} = I_{\\text{tube}} \\times V_{\\text{acc}}, \\quad P_{\\text{heat}} \\approx 0.99 \\times P_{\\text{input}}",
            "variables": {
                "P_input": "Total electrical power supplied to X-ray tube (Watts)",
                "I_tube": "Anode electron beam current (Amperes or mA)",
                "V_acc": "Accelerating anode voltage (Volts)",
                "P_heat": "Thermal heat generation rate at tungsten target (Watts)"
            }
        }),
        # Page 3
        (3, "X-Ray Tube Energy Conversion Efficiency ($\eta < 1\%$)", "concept_explanation", "concept_explanation", 1, {
            "text": "### Low Efficiency Equation:\nThe fractional conversion efficiency $\\eta$ of an X-ray tube is empirically given by:\n$$\\eta = \\frac{P_{\\text{xray}}}{P_{\\text{input}}} = k \\times Z \\times V_{\\text{acc}}$$\n- $k \\approx 1 \\times 10^{-9}\\text{ V}^{-1}$: Empirical constant.\n- $Z$: Atomic number of target material ($Z = 74$ for tungsten).\n- $V_{\\text{acc}}$: Accelerating voltage ($80\\text{ kV} = 80,000\\text{ V}$).\nFor tungsten at $80\\text{ kV}$, $\\eta = (10^{-9}) \\times 74 \\times 80,000 \\approx 0.0059 = 0.59\\%$. Over **$99.4\\%$ of electrical power is wasted as heat**!"
        }),
        # Page 4
        (4, "Worked Example Level 1 — Direct Cutoff Wavelength", "worked_example", "worked_example", 1, {
            "problem": "An X-ray tube operates at an accelerating potential difference of $50.0\\text{ kV}$. Calculate the minimum cutoff wavelength $\\lambda_{\\min}$ of the emitted X-rays. (Take $h = 6.63 \\times 10^{-34}\\text{ J s}$, $c = 3.0 \\times 10^8\\text{ m/s}$, $e = 1.6 \\times 10^{-19}\\text{ C}$).",
            "steps": [
                "Step 1: Identify knowns: Accelerating voltage $V_{\\text{acc}} = 50.0\\text{ kV} = 50,000\\text{ V}$, $h = 6.63 \\times 10^{-34}\\text{ J s}$, $c = 3.0 \\times 10^8\\text{ m/s}$, $e = 1.6 \\times 10^{-19}\\text{ C}$.",
                "Step 2: Required: Minimum cutoff wavelength $\\lambda_{\\min}$.",
                "Step 3: Equation: $\\lambda_{\\min} = \\frac{h c}{e V_{\\text{acc}}}$.",
                "Step 4: Substitute values: $\\lambda_{\\min} = \\frac{(6.63 \\times 10^{-34}) \\times (3.0 \\times 10^8)}{(1.6 \\times 10^{-19}) \\times 50,000}$.",
                "Step 5: Calculate numerator and denominator: $\\text{Numerator} = 1.989 \\times 10^{-25}$, $\\text{Denominator} = 8.0 \\times 10^{-15}$.",
                "Step 6: Compute final value: $\\lambda_{\\min} = \\frac{1.989 \\times 10^{-25}}{8.0 \\times 10^{-15}} = 2.486 \\times 10^{-11}\\text{ m} = 0.0249\\text{ nm}$.",
                "Step 7: Physical check: Cutoff wavelength is in the hard X-ray picometer range ($10^{-11}\\text{ m}$), which is physically accurate."
            ]
        }),
        # Page 5
        (5, "Worked Example Level 2 — Maximum Frequency", "worked_example", "worked_example", 1, {
            "problem": "Calculate the maximum frequency $f_{\\max}$ of X-rays produced when an electron beam is accelerated through a potential difference of $80.0\\text{ kV}$.",
            "steps": [
                "Step 1: Knowns: $V_{\\text{acc}} = 80.0\\text{ kV} = 80,000\\text{ V}$, $e = 1.6 \\times 10^{-19}\\text{ C}$, $h = 6.63 \\times 10^{-34}\\text{ J s}$.",
                "Step 2: Required: Maximum frequency $f_{\\max}$.",
                "Step 3: Equation: $e V_{\\text{acc}} = h f_{\\max} \\implies f_{\\max} = \\frac{e V_{\\text{acc}}}{h}$.",
                "Step 4: Substitute: $f_{\\max} = \\frac{(1.6 \\times 10^{-19}) \\times 80,000}{6.63 \\times 10^{-34}}$.",
                "Step 5: Calculate: $f_{\\max} = \\frac{1.28 \\times 10^{-14}}{6.63 \\times 10^{-34}} = 1.93 \times 10^{19}\\text{ Hz}$.",
                "Step 6: Attach unit: $f_{\\max} = 1.93 \\times 10^{19}\\text{ Hz}$."
            ]
        }),
        # Page 6
        (6, "Worked Example Level 3 — Target Heat Generation & Oil Cooling", "worked_example", "worked_example", 1, {
            "problem": "An X-ray tube operates at $60.0\\text{ kV}$ with a tube current of $20.0\\text{ mA}$. Assuming $99.0\\%$ of the input electrical power is converted into heat, calculate the rate of heat generation at the anode target in Watts.",
            "steps": [
                "Step 1: Knowns: $V_{\\text{acc}} = 60,000\\text{ V}$, Tube current $I = 20.0\\text{ mA} = 0.020\\text{ A}$, Heat fraction $= 0.99$.",
                "Step 2: Required: Heat generation rate $P_{\\text{heat}}$.",
                "Step 3: Total input power: $P_{\\text{input}} = I \\times V_{\\text{acc}} = 0.020\\text{ A} \\times 60,000\\text{ V} = 1,200\\text{ Watts}$.",
                "Step 4: Thermal heat loss rate: $P_{\\text{heat}} = 0.99 \\times 1,200\\text{ W} = 1,188\\text{ Watts}$.",
                "Step 5: Physical check: Nearly $1.2\\text{ kW}$ of heat is generated continuously at the tungsten target tip, requiring oil circulators."
            ]
        }),
        (6, "Worked Example Level 3 — Target Heat Generation & Oil Cooling", "suggested_diagram", "suggested_diagram", 2, {
            "text": "Anode Target Water/Oil Thermal Heat Exchanger Calculation Diagram",
            "instruction": "Diagram showing anode heat transfer rate into circulating cooling oil."
        }),
        # Page 7
        (7, "Worked Example Level 4 — Minimum Voltage Required for Specific Wavelength", "worked_example", "worked_example", 1, {
            "problem": "To examine a metallic casting defect, a radiographer requires X-rays with a minimum cutoff wavelength of at least $0.015\\text{ nm}$ ($1.5 \\times 10^{-11}\\text{ m}$). Calculate the minimum accelerating voltage required.",
            "steps": [
                "Step 1: Knowns: Target minimum cutoff $\\lambda_{\\min} = 1.5 \\times 10^{-11}\\text{ m}$, $h = 6.63 \\times 10^{-34}\\text{ J s}$, $c = 3.0 \\times 10^8\\text{ m/s}$, $e = 1.6 \\times 10^{-19}\\text{ C}$.",
                "Step 2: Required: Accelerating voltage $V_{\\text{acc}}$.",
                "Step 3: Equation: $V_{\\text{acc}} = \\frac{h c}{e \\lambda_{\\min}}$.",
                "Step 4: Substitute: $V_{\\text{acc}} = \\frac{(6.63 \\times 10^{-34}) \\times (3.0 \\times 10^8)}{(1.6 \\times 10^{-19}) \\times (1.5 \\times 10^{-11})}$.",
                "Step 5: Calculate: $V_{\\text{acc}} = \\frac{1.989 \\times 10^{-25}}{2.4 \\times 10^{-30}} = 82,875\\text{ V} = 82.9\\text{ kV}$.",
                "Step 6: Conclusion: An accelerating voltage of at least $82.9\\text{ kV}$ must be applied."
            ]
        }),
        # Page 8
        (8, "Worked Example Level 5 — Challenge Multi-Step (Tube Current & Photon Flux)", "worked_example", "worked_example", 1, {
            "problem": "An X-ray tube operates at $100\\text{ kV}$ with a tube current of $15.0\\text{ mA}$. Calculate: 1. Number of electrons striking the target per second. 2. Total electrical power input.",
            "steps": [
                "Step 1: Knowns: $V_{\\text{acc}} = 100,000\\text{ V}$, $I = 15.0\\text{ mA} = 0.015\\text{ A}$, $e = 1.6 \\times 10^{-19}\\text{ C}$.",
                "Step 2: Number of electrons per second: $N_e = \\frac{I}{e} = \\frac{0.015\\text{ A}}{1.6 \\times 10^{-19}\\text{ C}} = 9.375 \\times 10^{16}\\text{ electrons/second}$.",
                "Step 3: Input electrical power: $P_{\\text{input}} = I \\times V_{\\text{acc}} = 0.015\\text{ A} \\times 100,000\\text{ V} = 1,500\\text{ W}$ ($1.5\\text{ kW}$)."
            ]
        }),
        # Page 9
        (9, "Biological Radiation Hazards", "concept_explanation", "concept_explanation", 1, {
            "text": "### Biological Hazards of Ionizing Radiation:\nBecause X-ray photons possess high energy, they knock electrons out of living biological molecules, creating reactive free radicals.\n\n### Radiation Damage Mechanism:\n1. **Somatic Damage (Cell Injury)**: High doses cause skin burns, radiation sickness, hair loss, and destruction of blood-forming bone marrow cells.\n2. **Genetic Damage (DNA Mutation)**: Lower doses alter DNA nucleotide sequences in reproductive cells, resulting in hereditary genetic mutations or cancer (leukemia)."
        }),
        # Page 10
        (10, "Radiation Protection & Shielding Measures", "concept_explanation", "concept_explanation", 1, {
            "text": "### Three Fundamental Principles of Radiation Safety:\n1. **Distance (Inverse-Square Law)**: Radiation intensity drops with the square of distance ($I \\propto \\frac{1}{r^2}$). Operating personnel should stand behind shielding barriers or at least $2\\text{ meters}$ away.\n2. **Shielding**: X-ray rooms are built with thick **lead-lined walls** and heavy **lead-glass viewing windows**. Radiographers wear lead-lined rubber aprons ($0.5\\text{ mm lead equivalent}$).\n3. **Dosimetry Monitoring**: Radiographers wear **film badge dosimeters** containing photographic film that records cumulative monthly radiation exposure."
        }),
        (10, "Radiation Protection & Shielding Measures", "suggested_diagram", "suggested_diagram", 2, {
            "text": "Medical Radiation Safety: Lead Apron, Lead-Glass Viewing Window, and Film Badge Dosimeter Construction",
            "instruction": "Diagram showing lead-lined protective apron, lead-glass viewing screen, and film badge dosimeter internal construction."
        }),
        # Page 11
        (11, "Addressing Common Misconceptions", "common_misconception", "common_misconception", 1, {
            "text": "### 4 Critical Misconceptions Clarified:\n1. **X-Rays vs. Cathode Rays**: Cathode rays are streams of charged material particles (electrons); X-rays are uncharged electromagnetic photons!\n2. **Hardness vs. Intensity**: Hardness is controlled by accelerating voltage ($V_{\\text{acc}}$); Intensity is controlled by filament heating current ($I_f$).\n3. **Deflection in Fields**: X-rays are **NOT** deflected by electric or magnetic fields because they carry zero electrical charge.\n4. **Heat vs. X-Ray Production**: Over $99\\%$ of electron energy in an X-ray tube produces heat; less than $1\\%$ produces useful X-rays."
        }),
        # Page 12
        (12, "Knowledge Check: Calculations & Safety", "knowledge_check", "knowledge_check", 1, {
            "question": "An X-ray tube operates at 40 kV. What is the minimum cutoff wavelength of the emitted X-rays?",
            "options": ["0.0311 nm", "0.0249 nm", "0.124 nm", "0.005 nm"],
            "answer": "0.0311 nm",
            "explanation": "lambda_min = hc / (e V_acc) = (6.63 x 10^-34 x 3.0 x 10^8) / (1.6 x 10^-19 x 40,000) = 1.989 x 10^-25 / 6.4 x 10^-15 = 3.108 x 10^-11 m = 0.0311 nm."
        }),
        (12, "Knowledge Check: Calculations & Safety", "knowledge_check", "knowledge_check", 2, {
            "question": "What is the primary material used for personal protective aprons in diagnostic X-ray rooms?",
            "options": ["Aluminum alloy", "Solid copper", "Lead-lined rubber", "Tungsten mesh"],
            "answer": "Lead-lined rubber",
            "explanation": "Lead has a very high atomic number (Z = 82) and high density, providing excellent photoelectric attenuation of diagnostic X-rays."
        }),
        # Page 13
        (13, "Module Summary", "summary", "summary", 1, {
            "text": "### Module 8.3 Key Takeaways:\n1. **Duane-Hunt Law**: $\\lambda_{\\min} = \\frac{hc}{eV_{\\text{acc}}}$.\n2. **Efficiency**: $\\eta < 1\\%$; over $99\\%$ of input electrical energy becomes heat at the anode target.\n3. **Safety**: Lead aprons, lead-glass windows, inverse-square distance, and film badge dosimeter monitoring."
        }),
        (14, "Module Summary", "key_takeaway", "key_takeaway", 2, {
            "text": "Topic 8 Complete: X-ray electrodynamics links high-voltage electron kinetic energy to photon mechanics, diagnostic medical imaging, and lead radiation protection."
        })
    ]

    for p_num, title, btype, ctype, order, content in blocks_m83:
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
    print("TOPIC 8 INGESTION COMPLETED SUCCESSFULLY!")
    print("=" * 80)

if __name__ == "__main__":
    run_ingestion()
