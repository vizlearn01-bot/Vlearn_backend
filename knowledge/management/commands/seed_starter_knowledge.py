import uuid
from django.core.management.base import BaseCommand
from django.utils import timezone
from django.db import transaction

from knowledge.models import Article, ArticleCategory, ArticleTag
from curriculum.models import (
    Curriculum,
    Grade,
    Subject,
    SubjectDomain,
    Topic,
    LearningUnit,
    Simulation,
    SimulationStatus,
    Concept,
    Misconception,
)


class Command(BaseCommand):
    help = "Seeds 7 authentic, KCSE-aligned starter articles across Chemistry, Physics, and Biology with simulations, concepts, and misconceptions."

    def add_arguments(self, parser):
        parser.add_argument(
            "--clean-test-data",
            action="store_true",
            default=True,
            help="Remove synthetic performance test dummy articles before seeding.",
        )

    def handle(self, *args, **options):
        self.stdout.write("Starting VizLearn Knowledge Platform starter content seeding...")

        if options.get("clean_test_data"):
            deleted_count, _ = Article.objects.filter(title__startswith="Article 89577121").delete()
            if deleted_count > 0:
                self.stdout.write(f"Cleaned up {deleted_count} legacy performance test articles.")

        with transaction.atomic():
            # 1. Categories
            categories_data = [
                {
                    "name": "Chemistry",
                    "slug": "chemistry",
                    "order": 1,
                    "linked_subject_name": "Chemistry",
                    "description": "Explore fundamental principles of chemical reactions, kinetic molecular theory, gas laws, and electrochemistry.",
                },
                {
                    "name": "Physics",
                    "slug": "physics",
                    "order": 2,
                    "linked_subject_name": "Physics",
                    "description": "Master classical mechanics, fluid dynamics, wave behavior, and geometric optics with real-time simulations.",
                },
                {
                    "name": "Biology",
                    "slug": "biology",
                    "order": 3,
                    "linked_subject_name": "Biology",
                    "description": "Investigate cellular physiology, plant transport mechanisms, human sensory systems, and biological adaptations.",
                },
            ]

            categories = {}
            for cat_dict in categories_data:
                cat, _ = ArticleCategory.objects.update_or_create(
                    slug=cat_dict["slug"],
                    defaults=cat_dict,
                )
                categories[cat.slug] = cat
                self.stdout.write(f"Category: {cat.name}")

            # 2. Tags
            tags_data = [
                ("Gas Laws", "gas-laws"),
                ("Kinetic Theory", "kinetic-theory"),
                ("Fluid Mechanics", "fluid-mechanics"),
                ("Buoyancy", "buoyancy"),
                ("Plant Physiology", "plant-physiology"),
                ("Transpiration", "transpiration"),
                ("Acids and Bases", "acids-and-bases"),
                ("Chemical Equilibrium", "chemical-equilibrium"),
                ("Optics", "optics"),
                ("Thin Lenses", "thin-lenses"),
                ("Human Biology", "human-biology"),
                ("Sensory Organs", "sensory-organs"),
                ("Chemical Kinetics", "chemical-kinetics"),
                ("Activation Energy", "activation-energy"),
                ("KCSE Revision", "kcse-revision"),
            ]

            tags = {}
            for name, slug in tags_data:
                tag, _ = ArticleTag.objects.update_or_create(
                    slug=slug,
                    defaults={"name": name},
                )
                tags[slug] = tag

            # 3. Articles Data Specification
            articles_specs = [
                # -----------------------------------------------------------
                # Article 1: Boyle's Law (Chemistry)
                # -----------------------------------------------------------
                {
                    "slug": "understanding-boyles-law-pressure-volume-relationship",
                    "title": "Understanding Boyle's Law: Kinetic Theory, Pressure-Volume Invariance, and Gas Compression",
                    "category": categories["chemistry"],
                    "sim_key": "chem_boyles_law",
                    "topic_kw": "Gas Laws",
                    "unit_kw": "Boyle",
                    "tags": ["gas-laws", "kinetic-theory", "kcse-revision"],
                    "meta_title": "Boyle's Law Explained: Pressure-Volume Relationship & Kinetic Theory",
                    "meta_description": "Master Boyle's Law for KCSE Chemistry. Understand the inverse pressure-volume relationship, kinetic molecular derivations, and interactive gas simulations.",
                    "summary": "At constant temperature, the volume of a fixed mass of an ideal gas is inversely proportional to its pressure. Explore the microscopic collision physics that govern gas compression.",
                    "featured_image_url": None,
                    "featured_image_alt": "",
                    "concepts": [
                        {
                            "name": "Boyle's Law Formulation",
                            "description": "The volume of a fixed mass of gas is inversely proportional to its pressure provided temperature remains constant: P ∝ 1/V or P₁V₁ = P₂V₂.",
                            "misconceptions": [
                                (
                                    "When a gas is compressed, the individual gas molecules shrink in physical volume.",
                                    "Individual gas molecules have a constant size. Compression merely reduces the intermolecular empty space between freely moving particles, raising collision frequency per unit container surface area."
                                ),
                                (
                                    "Boyle's law applies accurately even if the temperature changes during compression.",
                                    "Boyle's law strictly requires isothermal conditions (T = constant). If temperature changes, the average molecular kinetic energy alters, changing pressure independently of volume changes."
                                )
                            ]
                        }
                    ],
                    "body": """## The Kinetic Reality of Gas Compression

When you press down on the plunger of a sealed bicycle pump or medical syringe, the resistance you feel pushes back with increasing force. This everyday observation is the direct macroscopic expression of **Boyle's Law**, first formulated by Robert Boyle in 1662.

In secondary school chemistry and physics, Boyle's Law is not simply a mathematical formula to memorize—it is a window into the **Kinetic Molecular Theory of Matter**.

> **Boyle's Law**: The volume ($V$) of a fixed mass of gas is inversely proportional to its applied pressure ($P$), provided the temperature ($T$) remains strictly constant.

---

## Mathematical Formulation

Mathematically, this inverse relationship is written as:

$$P \\propto \\frac{1}{V} \\quad \\text{(at constant } T \\text{ and fixed mass } m\\text{)}$$

Introducing a proportionality constant $k$:

$$P \\cdot V = k$$

When comparing an initial state (State 1) to a compressed or expanded state (State 2):

$$P_1 V_1 = P_2 V_2$$

Where:
* $P_1$ = Initial pressure ($\text{N/m}^2$, $\text{Pa}$, or $\text{atm}$)
* $V_1$ = Initial volume ($\text{cm}^3$, $\text{dm}^3$, or $\text{m}^3$)
* $P_2$ = Final pressure
* $V_2$ = Final volume

---

## Microscopic Mechanism: Why Does Pressure Rise?

To truly grasp Boyle's Law, imagine the gas inside a rigid container at the atomic scale:

1. **Continuous Random Motion**: Gas molecules are in constant, high-speed, chaotic motion, frequently colliding with each other and with the inner walls of the container.
2. **Origin of Gas Pressure**: Every collision against the wall exerts an infinitesimal impulse force ($F = \\frac{\\Delta p}{\\Delta t}$). The sum of these billions of impacts divided by the container surface area constitutes **gas pressure** ($P = \\frac{F}{A}$).
3. **Volume Halving**: If you compress the gas so that the volume is halved ($V_2 = \\frac{1}{2} V_1$), the same number of molecules are now crowded into half the space.
4. **Doubled Collision Frequency**: Because the distance between opposing walls is reduced, each molecule hits the walls twice as often per second. 
5. **Doubled Pressure**: Double the collision frequency per unit area yields exactly double the pressure ($P_2 = 2 P_1$).

| Parameter | Initial State ($1$) | Compressed State ($2$) | Expanded State ($3$) |
| :--- | :---: | :---: | :---: |
| **Volume ($V$)** | $1.00\\text{ dm}^3$ | $0.50\\text{ dm}^3$ | $2.00\\text{ dm}^3$ |
| **Pressure ($P$)** | $100\\text{ kPa}$ | $200\\text{ kPa}$ | $50\\text{ kPa}$ |
| **Product ($P \\cdot V$)** | $100\\text{ kPa}\\cdot\\text{dm}^3$ | $100\\text{ kPa}\\cdot\\text{dm}^3$ | $100\\text{ kPa}\\cdot\\text{dm}^3$ |
| **Collision Frequency** | Baseline ($1\\times$) | Doubled ($2\\times$) | Halved ($0.5\\times$) |

---

## Graphical Relationships in KCSE Examinations

In KCSE practical and theory papers, examiners frequently test graphical representations of Boyle's Law:

* **$P$ versus $V$**: Yields a smooth downward curve called a **rectangular hyperbola** or **isotherm**.
* **$P$ versus $\\frac{1}{V}$**: Yields a straight line passing directly through the origin $(0,0)$, confirming exact direct proportionality with inverse volume.
* **$PV$ versus $P$**: Yields a horizontal straight line parallel to the pressure axis, illustrating the constant invariance of the product $PV$.

---

## Worked KCSE Example

**Question**: A gas cylinder holds $0.40\\text{ m}^3$ of oxygen gas at a pressure of $2.50 \\times 10^5\\text{ Pa}$. If the gas is allowed to expand into an evacuated chamber until the pressure drops to $1.00 \\times 10^5\\text{ Pa}$ at constant temperature, calculate the final volume of the gas.

**Solution**:
1. State given quantities:
   * $P_1 = 2.50 \\times 10^5\\text{ Pa}$
   * $V_1 = 0.40\\text{ m}^3$
   * $P_2 = 1.00 \\times 10^5\\text{ Pa}$
   * $V_2 = ?$
2. Apply Boyle's Law formula:
   $$P_1 V_1 = P_2 V_2 \\implies V_2 = \\frac{P_1 V_1}{P_2}$$
3. Substitute and compute:
   $$V_2 = \\frac{(2.50 \\times 10^5\\text{ Pa})(0.40\\text{ m}^3)}{1.00 \\times 10^5\\text{ Pa}} = 1.00\\text{ m}^3$$

The final volume of the oxygen gas is **$1.00\\text{ m}^3$**.
"""
                },

                # -----------------------------------------------------------
                # Article 2: Archimedes' Principle (Physics)
                # -----------------------------------------------------------
                {
                    "slug": "archimedes-principle-upthrust-buoyancy-physics",
                    "title": "Archimedes' Principle & Upthrust: The Physics of Buoyancy, Density, and Flotation",
                    "category": categories["physics"],
                    "sim_key": "archimedes_principle_buoyancy",
                    "topic_kw": "Floating and Sinking",
                    "unit_kw": "Archimedes",
                    "tags": ["fluid-mechanics", "buoyancy", "kcse-revision"],
                    "meta_title": "Archimedes' Principle & Upthrust Explained: Physics of Buoyancy",
                    "meta_description": "Master Archimedes' Principle, upthrust derivations, and the Law of Flotation for KCSE Physics. Visual explanations and interactive buoyancy balance.",
                    "summary": "When a body is partially or completely immersed in a fluid, it experiences an upward force equal to the weight of fluid displaced. Unpack hydrostatic pressure gradients and flotation mechanics.",
                    "featured_image_url": None,
                    "featured_image_alt": "",
                    "concepts": [
                        {
                            "name": "Archimedes' Principle & Buoyancy",
                            "description": "When a body is totally or partially submerged in a fluid, it experiences an upward buoyant force (upthrust) equal to the weight of the fluid displaced by the body.",
                            "misconceptions": [
                                (
                                    "Heavy objects always sink while light objects always float, regardless of size or geometry.",
                                    "Flotation depends strictly on average density relative to the surrounding fluid. A massive cargo ship made of dense steel floats because its hollow shape displaces a weight of water equal to the vessel's entire weight."
                                ),
                                (
                                    "Upthrust increases continuously as a submarine dives deeper into ocean water.",
                                    "Once completely submerged, the volume of fluid displaced remains constant. Because U = ρ·g·V, upthrust stays constant at any depth as long as water density remains essentially uniform."
                                )
                            ]
                        }
                    ],
                    "body": """## Why Do Giant Steel Ships Float While Tiny Pebbles Sink?

A small pebble dropped into Lake Victoria drops straight to the bottom within seconds, yet massive cargo freighters loaded with hundreds of tonnes of containers float effortlessly.

The governing physics behind this apparent paradox was uncovered over two millennia ago by the Greek mathematician Archimedes and constitutes one of the most vital chapters in secondary school mechanics.

> **Archimedes' Principle**: When a body is completely or partially immersed in a fluid (liquid or gas), it experiences an upward force (**upthrust**) equal to the weight of the fluid displaced by the body.

---

## The Physical Origin of Upthrust: Hydrostatic Pressure Gradients

Upthrust is not a mystical anti-gravity force; it is the natural consequence of fluid pressure increasing with depth.

Recall the liquid pressure formula:

$$P = \\rho g h$$

Where:
* $\\rho$ = Density of the fluid ($\text{kg/m}^3$)
* $g$ = Acceleration due to gravity ($9.81\\text{ m/s}^2$ or $10\\text{ m/s}^2$)
* $h$ = Depth below the fluid surface ($\text{m}$)

Consider a solid rectangular block of height $H$ submerged in water:
1. The **top face** of the block is at shallow depth $h_1$, experiencing downward pressure $P_1 = \\rho g h_1$.
2. The **bottom face** is at greater depth $h_2 = h_1 + H$, experiencing upward pressure $P_2 = \\rho g h_2$.
3. Since $h_2 > h_1$, the upward force on the bottom ($F_{\\text{bottom}} = P_2 \\cdot A$) is strictly greater than the downward force on the top ($F_{\\text{top}} = P_1 \\cdot A$).
4. The net upward resultant force is the **Upthrust** ($U$):

$$U = F_{\\text{bottom}} - F_{\\text{top}} = \\rho g A (h_2 - h_1) = \\rho g (A \\cdot H)$$

Because the block's volume $V = A \\cdot H$:

$$U = \\rho_{\\text{fluid}} \\cdot g \\cdot V_{\\text{displaced}}$$

Since mass $m_{\\text{displaced}} = \\rho \\cdot V$, and weight $W = m \\cdot g$:

$$U = W_{\\text{fluid displaced}}$$

This proves Archimedes' Principle directly from first principles!

---

## Apparent Weight vs. True Weight

When an object is suspended in fluid from a spring balance, the scale reading drops:

$$\\text{Apparent Weight} = \\text{True Weight in Air} - \\text{Upthrust}$$

$$W_{\\text{apparent}} = W_{\\text{air}} - U$$

---

## Sinking, Floating, and Neutral Buoyancy

The fate of any submerged object is governed by the contest between its downward true weight ($W$) and the upward buoyant force ($U$):

| Condition | Force Comparison | Density Comparison | Net Acceleration | Example |
| :--- | :---: | :---: | :---: | :--- |
| **Sinking** | $W > U$ | $\\rho_{\\text{object}} > \\rho_{\\text{fluid}}$ | Downward | Stone in water, lead sinker |
| **Neutral Buoyancy** | $W = U$ | $\\rho_{\\text{object}} = \\rho_{\\text{fluid}}$ | Zero (remains stationary) | Submarine maintaining level depth |
| **Floating** | $W = U$ (partially submerged) | $\\rho_{\\text{average}} < \\rho_{\\text{fluid}}$ | Zero (at rest on surface) | Wooden block, ice on water, ocean liner |

---

## The Law of Flotation

A floating body does not displace its entire volume—only a fraction:

> **Law of Flotation**: A floating body displaces its own weight of the fluid in which it floats.

$$\\frac{V_{\\text{submerged}}}{V_{\\text{total}}} = \\frac{\\rho_{\\text{object}}}{\\rho_{\\text{fluid}}}$$

For an iceberg or wooden log with density $900\\text{ kg/m}^3$ floating in pure water ($1000\\text{ kg/m}^3$), exactly $90\\%$ of its volume is submerged beneath the surface, with only $10\\%$ visible above water.
"""
                },

                # -----------------------------------------------------------
                # Article 3: Transpiration Pull (Biology)
                # -----------------------------------------------------------
                {
                    "slug": "cohesion-tension-theory-transpiration-water-ascent",
                    "title": "Cohesion-Tension Theory: How Transpiration Pull Drives Water Ascent in Tall Plants",
                    "category": categories["biology"],
                    "sim_key": "transpiration_pull_cohesion",
                    "topic_kw": "Plant Transport",
                    "unit_kw": "Upward Movement",
                    "tags": ["plant-physiology", "transpiration", "kcse-revision"],
                    "meta_title": "Cohesion-Tension Theory: How Water Climbs 100m Tall Trees",
                    "meta_description": "Understand Cohesion-Tension Theory, transpiration pull, and xylem adaptations for KCSE Biology. Explore water potential gradients and stomatal regulation.",
                    "summary": "How do 100-meter-tall eucalyptus and cedar trees transport hundreds of liters of water daily without mechanical pumps? Explore the physics of transpiration pull and hydrogen bonding.",
                    "featured_image_url": None,
                    "featured_image_alt": "",
                    "concepts": [
                        {
                            "name": "Cohesion-Tension Mechanism",
                            "description": "The transpiration stream is maintained through negative hydrostatic pressure generated in leaf mesophyll, supported by high cohesion between water molecules and adhesion to xylem walls.",
                            "misconceptions": [
                                (
                                    "Root pressure is the primary mechanism pumping water up to the leaves of tall forest trees.",
                                    "Root pressure only develops 1–2 atmospheres of pressure, sufficient to lift water just a few meters. Tall trees rely on transpiration pull, which creates negative pressures exceeding -15 atmospheres."
                                ),
                                (
                                    "Transpiration is purely harmful water loss that plants try to prevent at all times.",
                                    "While excessive transpiration risks wilting, baseline transpiration is biologically vital: it creates the suction force that pulls dissolved nitrates, phosphates, and minerals from soil to leaves, and provides essential evaporative cooling."
                                )
                            ]
                        }
                    ],
                    "body": """## The Botanical Pump That Defies Gravity

In Kenya's Mau Forest and Mount Kenya slopes, mature cedar and eucalyptus trees regularly stand over 60 meters tall. On a warm sunny day, a single large tree can lift over 400 liters of water from the soil to its crown leaves without a single mechanical pump, muscle contraction, or active ATP engine.

How is this hydraulic feat accomplished? The answer lies in the **Cohesion-Tension Theory**, first proposed by botanists Henry Dixon and John Joly in 1894.

---

## The Three Pillar Forces of Water Ascent

The ascent of sap up the plant stem is driven by three coordinated physical forces:

### 1. Transpiration Pull (The Driving Suction)
* Sunlight warms leaf cells, causing water to evaporate from wet mesophyll cell walls into intercellular air spaces.
* Water vapor diffuses out through open **stomata** into the drier atmosphere down a steep water potential gradient ($\\Psi$).
* As mesophyll cells lose water, their osmotic pressure rises (more negative water potential), pulling water from adjacent xylem vessels in leaf veins.
* This microscopic evaporation generates massive **negative tension** (suction) at the top of the plant's plumbing system.

### 2. Cohesion (Water-to-Water Tensile Strength)
* Water ($H_2O$) is a strongly polar molecule. The electronegative oxygen atom forms persistent **hydrogen bonds** with the electropositive hydrogen atoms of neighboring water molecules.
* This mutual attraction gives liquid water extraordinary **tensile strength**—comparable to thin steel wires of the same diameter.
* Under negative pressure, the continuous water column in the xylem does not snap or break into droplets.

### 3. Adhesion (Water-to-Cell-Wall Attraction)
* Water molecules form electrostatic attractions with the hydrophilic **cellulose** and **lignin** lining the inner walls of xylem tracheids and vessels.
* Adhesion prevents the water column from slipping downward under the gravitational pull when transpiration slows or ceases at night.

> **Key Rule**: Transpiration Pull provides the **lifting tension**; Cohesion maintains the **unbroken liquid chain**; Adhesion anchors the **column against gravity**.

---

## Structural Adaptations of Xylem Vessels

For water columns to withstand negative pressures of $-15\\text{ to }-30\\text{ atmospheres}$ without collapsing, xylem tissues have evolved specialized structural features:

1. **Dead, Hollow Tubes at Maturity**: Lacking living cytoplasm, nuclei, and end walls, xylem vessels form unobstructed continuous capillary pipelines.
2. **Lignified Walls**: Thick deposits of impermeable lignin provide high compressive hoop strength, preventing the tubes from imploding under intense negative pressure.
3. **Pits in Lateral Walls**: Microscopic unlignified regions allow lateral water cross-flow if a localized air bubble (embolism) blocks an individual vessel.
4. **Narrow Lumina**: Narrow capillary diameters maximize the adhesion contact surface area per unit volume of water.

---

## Environmental Factors Controlling Transpiration Rate

| Factor | Change in Factor | Effect on Transpiration | Biological Mechanism |
| :--- | :---: | :---: | :--- |
| **Light Intensity** | Increase | Increases | Stimulates stomatal opening via guard cell potassium ion influx. |
| **Temperature** | Increase | Increases | Supplies latent heat of vaporization; widens vapor pressure deficit. |
| **Humidity** | Increase | Decreases | Flattens the water vapor diffusion gradient between leaf interior and exterior air. |
| **Wind Velocity** | Increase | Increases | Blows away the saturated boundary layer of humid air resting on the leaf surface. |
"""
                },

                # -----------------------------------------------------------
                # Article 4: Acids, Bases and pH (Chemistry)
                # -----------------------------------------------------------
                {
                    "slug": "acids-bases-ph-strong-weak-electrolytes-dissociation",
                    "title": "Acids, Bases, and pH: Understanding Strong vs. Weak Electrolytes and Dynamic Dissociation",
                    "category": categories["chemistry"],
                    "sim_key": "chem_acid_base_dissociation",
                    "topic_kw": "Acids, Bases and Salts",
                    "unit_kw": "Acids",
                    "tags": ["acids-and-bases", "chemical-equilibrium", "kcse-revision"],
                    "meta_title": "Acids, Bases & pH: Strong vs Weak Electrolytes Explained",
                    "meta_description": "Master acid-base ionization, dynamic dissociation, and pH calculations for KCSE Chemistry. Understand the difference between strength and concentration.",
                    "summary": "Explore the critical chemical distinction between acid strength and concentration. Unpack reversible ionization equilibria and the logarithmic pH scale.",
                    "featured_image_url": None,
                    "featured_image_alt": "",
                    "concepts": [
                        {
                            "name": "Acid-Base Dissociation & Strength",
                            "description": "Acid strength is defined by the degree of ionization in aqueous solution. Strong acids fully dissociate into ions, while weak acids establish a dynamic equilibrium.",
                            "misconceptions": [
                                (
                                    "'Strong acid' and 'concentrated acid' are synonymous terms describing dangerous chemical solutions.",
                                    "Strength refers strictly to the percentage of ionization (complete vs partial dissociation into ions). Concentration refers to the quantity of solute per unit volume of solution. Dilute 0.001 M HCl is still a strong acid; pure glacial ethanoic acid is highly concentrated but fundamentally a weak acid."
                                ),
                                (
                                    "A neutral aqueous solution at pH 7 contains zero hydrogen ions and zero hydroxide ions.",
                                    "Pure water undergoes self-ionization (H₂O ⇌ H⁺ + OH⁻). At 25°C, neutral water contains equal concentrations of both ions: [H⁺] = [OH⁻] = 1.0 × 10⁻⁷ M, which logarithmically equals pH 7."
                                )
                            ]
                        }
                    ],
                    "body": """## Beyond the Litmus Paper: What Defines an Acid?

In introductory junior secondary science, acids are often introduced simply as sour substances that turn blue litmus paper red. In senior secondary school and KCSE Chemistry, we transition from descriptive observations to rigorous **ionic dynamics**.

According to the Arrhenius and Brønsted-Lowry definitions:
* An **acid** is a substance that donates hydrogen ions (protons, $H^+$) in aqueous solution.
* A **base** is a substance that accepts protons, or produces hydroxide ions ($OH^-$) in aqueous solution.

---

## Acid Strength vs. Solution Concentration

One of the most frequent errors in secondary chemistry examinations is conflating **acid strength** with **acid concentration**:

* **Strength**: Governed by the **degree of ionization** ($\\alpha$)—how readily molecules split into ions when dissolved in water.
* **Concentration**: Governed by the **molarity**—the number of moles of acid dissolved per cubic decimeter (liter) of solvent ($M = \\frac{n}{V}$).

> **Golden Distinction**:
> * **$0.01\\text{ M } HCl$**: A *dilute* solution of a *strong* acid (100% dissociated).
> * **$17.4\\text{ M } CH_3COOH$** (Glacial Ethanoic Acid): A *concentrated* solution of a *weak* acid (<1% dissociated).

---

## Ionization Dynamics: Complete vs. Reversible Equilibrium

### Strong Acids (Complete Dissociation)
Strong acids like hydrochloric acid ($HCl$), nitric acid ($HNO_3$), and sulfuric acid ($H_2SO_4$) dissociate completely in water:

$$HCl_{(aq)} \\longrightarrow H^+_{(aq)} + Cl^-_{(aq)}$$

Because dissociation is essentially irreversible, the concentration of free $H^+$ ions equals the nominal acid concentration:

$$[H^+] = [HCl]$$

### Weak Acids (Partial Dynamic Equilibrium)
Weak acids like ethanoic acid ($CH_3COOH$), carbonic acid ($H_2CO_3$), and citric acid only partially ionize:

$$CH_3COOH_{(aq)} \\rightleftharpoons H^+_{(aq)} + CH_3COO^-_{(aq)}$$

At any moment, over $98\\%$ of the molecules remain intact in covalent form ($CH_3COOH$). The forward dissociation and reverse recombination occur at equal rates, establishing a **dynamic chemical equilibrium**.

---

## The Logarithmic pH Scale

The concentration of hydrogen ions in everyday solutions spans over 14 orders of magnitude. In 1909, Danish biochemist Søren Sørensen devised the **pH scale** to compress this enormous range into an intuitive 0–14 index:

$$\\text{pH} = -\\log_{10}[H^+]$$

$$[H^+] = 10^{-\\text{pH}}$$

Because the scale is **base-10 logarithmic**:
* A solution at $\\text{pH } 3$ has $[H^+] = 10^{-3}\\text{ M}$.
* A solution at $\\text{pH } 2$ has $[H^+] = 10^{-2}\\text{ M}$.
* **Every 1-unit decrease in pH represents a 10-fold increase in hydrogen ion acidity!**

| Solution | Nominal Molarity | Degree of Dissociation ($\\alpha$) | $[H^+]$ Concentration | Measured pH |
| :--- | :---: | :---: | :---: | :---: |
| Hydrochloric Acid ($HCl$) | $0.10\\text{ M}$ | $100\\%$ ($1.0$) | $0.10\\text{ M}$ | $\\mathbf{1.0}$ |
| Ethanoic Acid ($CH_3COOH$) | $0.10\\text{ M}$ | $\\approx 1.3\\%$ ($0.013$) | $0.0013\\text{ M}$ | $\\mathbf{2.9}$ |
| Pure Distilled Water | Neutral | Auto-ionization | $1.0 \\times 10^{-7}\\text{ M}$ | $\\mathbf{7.0}$ |
| Sodium Hydroxide ($NaOH$) | $0.10\\text{ M}$ | $100\\%$ ($1.0$) | $1.0 \\times 10^{-13}\\text{ M}$ | $\\mathbf{13.0}$ |
"""
                },

                # -----------------------------------------------------------
                # Article 5: Convex Thin Lenses (Physics)
                # -----------------------------------------------------------
                {
                    "slug": "convex-thin-lenses-ray-diagrams-image-formation",
                    "title": "Ray Diagrams and Image Formation in Convex Lenses: Real vs. Virtual Images",
                    "category": categories["physics"],
                    "sim_key": "convex_lens_image_formation",
                    "topic_kw": "Thin Lenses",
                    "unit_kw": "Lens Types",
                    "tags": ["optics", "thin-lenses", "kcse-revision"],
                    "meta_title": "Convex Thin Lenses: Ray Diagrams & Image Formation Physics",
                    "meta_description": "Master ray tracing, lens formula calculations, and real vs virtual image characteristics for KCSE Physics. Interactive optical simulations and diagrams.",
                    "summary": "Master the geometry of converging lenses. Learn how three principal rays predict exact image positions, sizes, and natures for cameras, projectors, and magnifying glasses.",
                    "featured_image_url": None,
                    "featured_image_alt": "",
                    "concepts": [
                        {
                            "name": "Convex Lens Image Formation",
                            "description": "Biconvex lenses converge parallel incident rays at the principal focus. The position of an object relative to focal points determines whether the formed image is real or virtual.",
                            "misconceptions": [
                                (
                                    "If you cover the top half of a convex lens with black paper, only the bottom half of the object will appear on the image screen.",
                                    "Light rays diverge from every single point on the object across the entire surface of the lens. Covering half the lens reduces the light-gathering capacity, making the entire image dimmer, but no part of the image is cut off."
                                ),
                                (
                                    "A virtual image produced by a magnifying glass can be captured directly on a white paper screen.",
                                    "Virtual images are formed where diverging refracted rays appear to originate when traced backward; no actual light photons converge at that point. They can be seen by the eye or refocused, but cannot be projected onto a physical screen."
                                )
                            ]
                        }
                    ],
                    "body": """## The Geometry of Refraction

From smartphone camera lenses to corrective spectacles, microscopes, and the human eye, curved transparent optical media form the foundation of imaging technology.

A **convex (converging) lens** is thicker at the center than at its edges. When parallel rays of light pass through a convex lens, refraction at the curved surfaces bends the rays inward, focusing them toward a single point on the principal axis known as the **principal focus** ($F$).

---

## The Three Principal Construction Rays

To predict the exact position, size, and nature of an image without complex trigonometry, optical physics uses **ray tracing** with three standard principal rays:

1. **Ray 1 (Parallel-to-Focal)**: A ray incident parallel to the principal axis refracts through the lens and passes directly through the principal focus ($F$) on the opposite side.
2. **Ray 2 (Central Optical Center)**: A ray passing straight through the optical center ($C$) of the lens emerges undeflected in a straight line without deviation.
3. **Ray 3 (Focal-to-Parallel)**: A ray passing through the principal focus ($F$) on the object side refracts through the lens and emerges parallel to the principal axis.

> **Intersection Rule**: The point where at least two refracted rays intersect defines the position of the corresponding image point.

---

## Summary of Image Characteristics Across Object Positions

The position of the object relative to the focal length ($f$) completely dictates the nature of the image:

| Object Position ($u$) | Image Position ($v$) | Real / Virtual | Inverted / Upright | Magnification ($m$) | Practical Application |
| :--- | :---: | :---: | :---: | :---: | :--- |
| **At Infinity** ($u = \\infty$) | At $F$ ($v = f$) | Real | Inverted | Highly Diminished | Objective lens of astronomical telescope |
| **Beyond $2F$** ($u > 2f$) | Between $F$ and $2F$ | Real | Inverted | Diminished ($m < 1$) | Photographic camera, human eye |
| **Exactly at $2F$** ($u = 2f$) | Exactly at $2F$ | Real | Inverted | Same Size ($m = 1$) | Photocopying machine ($1:1$ reproduction) |
| **Between $F$ and $2F$** | Beyond $2F$ ($v > 2f$) | Real | Inverted | Magnified ($m > 1$) | Classroom cinema projector, slide viewer |
| **Exactly at $F$** ($u = f$) | At Infinity ($v = \\infty$) | Parallel rays | — | — | Searchlight, automobile headlight colimator |
| **Between Lens & $F$** ($u < f$) | Behind object ($v < 0$) | **Virtual** | **Upright** | Magnified ($m > 1$) | Simple microscope / Magnifying glass |

---

## The Thin Lens Equation and Linear Magnification

In quantitative physics calculations, geometric ray diagrams are verified using the **Thin Lens Equation**:

$$\\frac{1}{f} = \\frac{1}{u} + \\frac{1}{v}$$

And **Linear Magnification** ($m$):

$$m = \\frac{h_i}{h_o} = \\frac{v}{u}$$

### Standard Cartesian Sign Convention
* **Focal length ($f$)**: Positive ($+f$) for converging convex lenses; negative ($-f$) for diverging concave lenses.
* **Object distance ($u$)**: Always positive ($+u$) for real objects.
* **Image distance ($v$)**: Positive ($+v$) for real images formed on the opposite side; negative ($-v$) for virtual images formed on the same side as the object.
"""
                },

                # -----------------------------------------------------------
                # Article 6: Human Eye Optics & Defects (Biology & Physics)
                # -----------------------------------------------------------
                {
                    "slug": "human-eye-accommodation-refractive-defects-vision",
                    "title": "The Human Eye as an Optical Instrument: Accommodation, Refractive Defects, and Corrective Lenses",
                    "category": categories["biology"],
                    "sim_key": "human_eye_accommodation_defects_3d",
                    "topic_kw": "Reception",
                    "unit_kw": "Sensory",
                    "tags": ["human-biology", "sensory-organs", "optics", "kcse-revision"],
                    "meta_title": "Human Eye Optics: Accommodation, Myopia & Corrective Lenses",
                    "meta_description": "Explore human eye optics: master ciliary accommodation, myopia, hypermetropia, and corrective lens ray diagrams for KCSE Biology and Physics.",
                    "summary": "Discover how the human eye dynamically changes its focal length to focus near and far. Understand the physiological causes of myopia and hypermetropia and their corrective lenses.",
                    "featured_image_url": None,
                    "featured_image_alt": "",
                    "concepts": [
                        {
                            "name": "Eye Accommodation & Refraction",
                            "description": "Accommodation is the active adjustment of crystalline lens curvature by ciliary muscles and suspensory ligaments to focus light sharply onto the retinal fovea.",
                            "misconceptions": [
                                (
                                    "The eye's ciliary muscles contract tightly when viewing distant objects across a landscape.",
                                    "Viewing distant objects is the eye's resting state: ciliary muscles relax, suspensory ligaments become taut, and the lens is pulled into its flattest, least refractive shape. Ciliary muscles contract actively only during near accommodation."
                                ),
                                (
                                    "Short-sighted (myopic) individuals cannot see distant objects because their crystalline lens is too weak or flat.",
                                    "In myopia, the eye's refractive power is actually too strong or the eyeball is too long. Light rays converge prematurely, focusing in front of the retina before spreading out into a blurry spot."
                                )
                            ]
                        }
                    ],
                    "body": """## Biological Precision: The Living Camera

The mammalian eye is a marvel of evolutionary optical engineering. Operating much like a digital camera, it possesses:
* An adjustable aperture (the **pupil** regulated by the **iris**)
* A dual refractive lens system (the fixed **cornea** providing $\\approx 70\\%$ of refraction, and the flexible **crystalline lens** providing variable fine-tuning)
* A high-resolution photosensitive sensor array (the **retina** containing over 120 million rods and 6 million cones).

Unlike man-made cameras that focus by physically moving rigid glass elements forward and backward, the human eye accomplishes sharp focusing through a dynamic biological process known as **accommodation**.

---

## The Mechanism of Accommodation

**Accommodation** is the reflex process by which the curvature and refractive power of the crystalline lens are dynamically altered to maintain sharp retinal focus as object distances change.

This mechanism is governed by the coordinated action of the circular **ciliary muscles** and the fibrous **suspensory ligaments**:

### 1. Focusing on Distant Objects (Far Vision > 6 meters)
* The ciliary muscles **relax**, expanding into a wider circular diameter.
* This relaxation pulls the suspensory ligaments **taut** (tight).
* The taut ligaments exert radial tension on the elastic lens capsule, **flattening the lens**.
* The lens becomes thinner with increased radius of curvature, **increasing its focal length** ($f$) and decreasing converging power.
* Parallel light rays converge precisely onto the **fovea centralis** of the retina with zero muscular fatigue.

### 2. Focusing on Near Objects (Reading Distance $\\approx 25\\text{ cm}$)
* The circular ciliary muscles **contract**, reducing the diameter of the ciliary ring.
* Tension on the suspensory ligaments is **released** (ligaments become slack).
* Due to its intrinsic elasticity, the crystalline lens rebounds into a **thicker, more spherical, highly convex shape**.
* The increased curvature **shortens the focal length** ($f$) and increases refractive power.
* Diverging light rays from the close object are refracted sharply onto the retina.

> **Key Takeaway**: 
> * **Distant Vision** = Relaxed Ciliary Muscles + Taut Ligaments + Flat Lens (Resting state).
> * **Near Vision** = Contracted Ciliary Muscles + Slack Ligaments + Thick Rounded Lens (Active work).

---

## Common Refractive Vision Defects & Optical Corrections

When the physical dimensions of the eyeball fail to match the refractive power of the lens, refractive errors occur:

### 1. Myopia (Short-Sightedness)
* **Symptom**: Near objects are seen with razor-sharp clarity; distant objects appear blurry and out of focus.
* **Underlying Causes**:
  1. The eyeball is **too long** from front to back (axial myopia).
  2. The cornea or crystalline lens has **excessive converging power** (too convex).
* **Ray Behavior**: Light rays from distant objects converge and focus **in front of the retina**, intersecting too early and forming a blur circle on the retinal surface.
* **Optical Correction**: Corrected using a **diverging (concave) lens** (negative diopters). The concave lens diverges incoming parallel rays slightly before entering the eye, pushing the final focal plane back onto the retina.

### 2. Hypermetropia (Long-Sightedness)
* **Symptom**: Distant objects are seen clearly; near objects cannot be brought into sharp focus.
* **Underlying Causes**:
  1. The eyeball is **too short** from front to back.
  2. The crystalline lens is **too flat** or lacks sufficient converging power.
* **Ray Behavior**: Diverging rays from nearby objects do not bend enough; they would converge at a virtual point **behind the retina**.
* **Optical Correction**: Corrected using a **converging (convex) lens** (positive diopters). The convex lens adds preliminary converging power, bringing the final image forward onto the retina.

---

## KCSE Examination Comparison Table

| Feature | Myopia (Short-Sightedness) | Hypermetropia (Long-Sightedness) |
| :--- | :--- | :--- |
| **Near Point** | Normal ($< 25\\text{ cm}$) | Receded beyond normal ($> 25\\text{ cm}$) |
| **Far Point** | Brought closer than infinity | At infinity (normal) |
| **Focal Plane (Uncorrected)** | In front of the retina | Behind the retina |
| **Eyeball Morphology** | Eyeball is too long | Eyeball is too short |
| **Lens Curvature** | Too convex / too thick | Too flat / insufficient curvature |
| **Corrective Lens** | **Concave (Diverging) Lens** | **Convex (Converging) Lens** |
"""
                },

                # -----------------------------------------------------------
                # Article 7: Collision Theory & Reaction Rates (Chemistry)
                # -----------------------------------------------------------
                {
                    "slug": "collision-theory-reaction-rates-activation-energy",
                    "title": "Collision Theory and Chemical Kinetics: Activation Energy, Catalysts, and Reaction Rates",
                    "category": categories["chemistry"],
                    "sim_key": "chem_collision_theory_kinetics",
                    "topic_kw": "Reaction Rates",
                    "unit_kw": "Collision Theory",
                    "tags": ["chemical-kinetics", "activation-energy", "kcse-revision"],
                    "meta_title": "Collision Theory & Reaction Rates: Activation Energy Explained",
                    "meta_description": "Understand collision theory, activation energy barriers, and Maxwell-Boltzmann distributions for KCSE Chemistry. Interactive rate of reaction simulations.",
                    "summary": "Why do some chemical reactions occur in microseconds while others take centuries? Explore the molecular collision criteria, activation energy barriers, and catalytic pathways.",
                    "featured_image_url": None,
                    "featured_image_alt": "",
                    "concepts": [
                        {
                            "name": "Collision Theory & Kinetics",
                            "description": "Chemical reactions occur when reactant particles collide with energy equal to or greater than the activation energy threshold and in the correct steric orientation.",
                            "misconceptions": [
                                (
                                    "Increasing temperature speeds up chemical reactions primarily because particles collide much more frequently.",
                                    "While collision frequency increases slightly (by roughly 2-3% per 10°C rise), the exponential surge in reaction rate is driven by the dramatic increase in the fraction of colliding particles with kinetic energy exceeding the activation energy barrier (E ≥ Ea)."
                                ),
                                (
                                    "A catalyst speeds up reactions by transferring thermal or kinetic energy to reacting particles.",
                                    "Catalysts do not provide energy to reactants. Instead, they provide an alternative reaction mechanism with a lower activation energy barrier, enabling a larger fraction of ordinary collisions to be successful."
                                )
                            ]
                        }
                    ],
                    "body": """## The Microscopic Dynamics of Chemical Change

In a room-temperature mixture of hydrogen gas ($H_2$) and oxygen gas ($O_2$), billions of molecular collisions occur every microsecond, yet the mixture can sit harmlessly in a glass bulb for centuries without reacting. Touch a single spark to the mixture, however, and an explosive chemical reaction takes place in a fraction of a millisecond:

$$2H_{2(g)} + O_{2(g)} \\longrightarrow 2H_2O_{(l)} + \\text{Heat}$$

Why did the molecules fail to react during billions of baseline collisions, and why did a tiny spark unlock instant chemical conversion?

The answer lies in **Collision Theory**, formulated by Max Trautz and William Lewis between 1916 and 1918.

---

## The Two Criteria for an Effective Collision

Under Collision Theory, simply bumping into another particle is not enough. For a collision to result in chemical bond rearrangement and product formation (an **effective collision**), it must satisfy two strict criteria:

### 1. The Energy Criterion (Activation Energy, $E_a$)
The colliding particles must possess a total kinetic energy equal to or greater than a critical threshold known as the **Activation Energy** ($E_a$):

$$E_{\\text{collision}} \\ge E_a$$

If the combined kinetic energy is less than $E_a$, the molecules gently bounce off each other like billiard balls with their electron clouds intact and no bonds broken.

### 2. The Orientation Criterion (Steric Alignment)
The particles must collide in a spatial geometry that brings the reactive atoms directly into contact. If an electrophilic center collides against a shielded non-reactive group, repulsion occurs and no reaction takes place regardless of kinetic energy.

---

## The Maxwell-Boltzmann Energy Distribution

In any gas or liquid at temperature $T$, not all molecules move at the same speed. Their kinetic energies follow the **Maxwell-Boltzmann distribution curve**:

* The area under the curve represents the total number of particles.
* Most molecules possess an average intermediate kinetic energy.
* Only a tiny fraction in the high-energy "tail" to the right of the $E_a$ line possess enough energy to react.

When temperature is raised by just $10^\\circ\\text{C}$ (e.g., from $298\\text{ K}$ to $308\\text{ K}$):
* The average molecular speed increases by less than $2\\%$.
* The collision frequency rises by only $\\approx 2\\%$.
* **However, the area under the curve beyond $E_a$ nearly doubles!**

This explains why a modest temperature increase of $10^\\circ\\text{C}$ typically doubles or triples the rate of a chemical reaction.

---

## How Catalysts Accelerate Reactions

A **catalyst** is a substance that increases the rate of a chemical reaction without itself undergoing permanent chemical change.

> **Crucial Concept**: Catalysts **do not add energy** to reactant particles. Instead, they provide an **alternative reaction pathway** that has a significantly lower activation energy barrier ($E_{a,\\text{cat}} < E_{a,\\text{uncat}}$).

By lowering the barrier:
1. The threshold line on the Maxwell-Boltzmann distribution shifts to the left.
2. A much larger percentage of collisions in the existing population now possess sufficient energy to overcome the lowered barrier.
3. Reaction rate accelerates exponentially at the exact same temperature.

---

## Key Factors Influencing Reaction Rates in KCSE Chemistry

| Factor | Effect on Reaction Rate | Kinetic Explanation | Everyday / Industrial Example |
| :--- | :---: | :--- | :--- |
| **Concentration / Pressure** | Increases rate | More particles per unit volume $\\to$ increased collision frequency per second. | Dilute vs. concentrated hydrochloric acid reacting with zinc granules. |
| **Surface Area** | Increases rate | Subdividing a solid exposes more surface atoms to colliding reactant particles. | Powdered calcium carbonate reacts much faster than large marble chips. |
| **Temperature** | Increases rate | Drastically increases the fraction of particles possessing kinetic energy $E \\ge E_a$. | Food spoiling rapidly at room temperature vs. preserved in a refrigerator. |
| **Catalyst** | Increases rate | Introduces an alternative mechanism with lower activation energy threshold. | Finely divided iron catalyst in the industrial Haber Process ($N_2 + 3H_2 \\to 2NH_3$). |
"""
                },
            ]

            # 4. Seed Articles, Concepts, Misconceptions, and Relationships
            now = timezone.now()
            created_articles = []

            for spec in articles_specs:
                self.stdout.write(f"\nProcessing article: {spec['title']}")

                # Find or ensure Topic, LearningUnit & Simulation safely
                topic, unit, sim = self._ensure_curriculum_anchor(spec, spec["category"])

                # Create / update Article
                article, created = Article.objects.update_or_create(
                    slug=spec["slug"],
                    defaults={
                        "title": spec["title"],
                        "category": spec["category"],
                        "article_type": "educational",
                        "summary": spec["summary"],
                        "body": spec["body"].strip(),
                        "status": "published",
                        "published_at": now,
                        "meta_title": spec["meta_title"],
                        "meta_description": spec["meta_description"],
                        "featured_image_url": spec["featured_image_url"],
                        "featured_image_alt": spec["featured_image_alt"],
                        "linked_topic": topic,
                        "linked_learning_unit": unit,
                        "linked_simulation": sim,
                    }
                )

                # Assign tags
                article_tags = [tags[t_slug] for t_slug in spec["tags"] if t_slug in tags]
                article.tags.set(article_tags)

                # Seed concepts and misconceptions on the linked unit
                if unit and "concepts" in spec:
                    for c_idx, c_spec in enumerate(spec["concepts"]):
                        concept, _ = Concept.objects.update_or_create(
                            learning_unit=unit,
                            name=c_spec["name"],
                            defaults={
                                "description": c_spec["description"],
                                "version": 1,
                            }
                        )

                        for m_desc, m_corr in c_spec.get("misconceptions", []):
                            Misconception.objects.update_or_create(
                                concept=concept,
                                description=m_desc,
                                defaults={
                                    "correction": m_corr,
                                    "version": 1,
                                }
                            )

                created_articles.append(article)
                action = "Created" if created else "Updated"
                self.stdout.write(
                    f"  ✓ {action} article '{article.title}' | Topic: {topic.name if topic else 'N/A'} | Unit: {unit.name if unit else 'N/A'} | Sim: {sim.title if sim else 'N/A'}"
                )

            # 5. Cross-link Related Articles
            # Cross link Chemistry: Boyle's Law <-> Acids/Bases <-> Collision Theory
            # Cross link Physics: Archimedes <-> Convex Lens <-> Eye
            # Cross link Biology: Transpiration <-> Eye <-> Boyle's Law
            boyles = next((a for a in created_articles if "boyle" in a.slug), None)
            archimedes = next((a for a in created_articles if "archimedes" in a.slug), None)
            transpiration = next((a for a in created_articles if "transpiration" in a.slug), None)
            acids = next((a for a in created_articles if "acid" in a.slug), None)
            lens = next((a for a in created_articles if "lens" in a.slug), None)
            eye = next((a for a in created_articles if "eye" in a.slug), None)
            kinetics = next((a for a in created_articles if "collision" in a.slug), None)

            if boyles and kinetics and acids:
                boyles.related_articles.add(kinetics, acids)
                kinetics.related_articles.add(boyles, acids)
                acids.related_articles.add(boyles, kinetics)

            if archimedes and lens and eye:
                archimedes.related_articles.add(lens, boyles)
                lens.related_articles.add(eye, archimedes)
                eye.related_articles.add(lens, transpiration)

            if transpiration and eye and boyles:
                transpiration.related_articles.add(boyles, eye)

            self.stdout.write(self.style.SUCCESS(
                f"\nSuccessfully seeded {len(created_articles)} high-quality KCSE starter articles across Chemistry, Physics, and Biology!"
            ))

    def _ensure_curriculum_anchor(self, spec, category):
        """
        Locates existing Topic, LearningUnit, and Simulation records.
        If missing (e.g. running in an empty test database), provisions valid
        baseline entities so the command remains completely self-contained.
        """
        topic = Topic.objects.filter(name__icontains=spec["topic_kw"]).first()
        if not topic:
            curriculum, _ = Curriculum.objects.get_or_create(
                name="KCSE Secondary Curriculum",
            )
            grade, _ = Grade.objects.get_or_create(
                name="Secondary Form 1-4",
                curriculum=curriculum,
            )
            subject, _ = Subject.objects.get_or_create(
                name=category.linked_subject_name or category.name,
                grade=grade,
            )
            topic, _ = Topic.objects.get_or_create(
                name=f"Topic: {spec['topic_kw']}",
                subject=subject,
                defaults={"order": 1},
            )

        unit = LearningUnit.objects.filter(name__icontains=spec["unit_kw"]).first()
        if not unit:
            unit = topic.learning_units.first()
        if not unit:
            unit, _ = LearningUnit.objects.get_or_create(
                name=f"Unit: {spec['unit_kw']}",
                topic=topic,
                defaults={"order": 1},
            )

        sim = Simulation.objects.filter(key=spec["sim_key"]).first()
        if not sim:
            cat_name = category.name.upper()
            if hasattr(SubjectDomain, cat_name):
                subj_domain = getattr(SubjectDomain, cat_name)
            else:
                subj_domain = SubjectDomain.CHEMISTRY
            sim, _ = Simulation.objects.get_or_create(
                key=spec["sim_key"],
                defaults={
                    "title": spec["title"].split(":")[0],
                    "subject": subj_domain,
                    "topic": topic.name,
                    "status": SimulationStatus.ACTIVE,
                    "description": f"Interactive simulation for {spec['title']}",
                    "archetype": spec["sim_key"],
                }
            )

        return topic, unit, sim
