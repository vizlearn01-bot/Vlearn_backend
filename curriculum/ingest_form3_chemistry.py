import os
import sys
import uuid
import django

# Setup Django environment
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "Nexus_backend.settings")
django.setup()

from curriculum.models import Curriculum, Grade, Subject, Topic, LearningUnit, Lesson, LessonBlock, LessonAsset

def ingest_form3_gas_laws():
    print("================================================================================")
    print("Starting VLearn Form 3 Chemistry Ingestion: Natural Presentation & Abstraction")
    print("================================================================================")

    # 1. Setup Curriculum Hierarchy
    curriculum = Curriculum.objects.filter(name="844").first()
    if not curriculum:
        curriculum = Curriculum.objects.create(name="844", description="Kenyan 8-4-4 Secondary Curriculum")
        print(f"Created Curriculum: {curriculum.name}")
    else:
        print(f"Found Curriculum: {curriculum.name}")

    grade, _ = Grade.objects.get_or_create(
        curriculum=curriculum,
        name="Form 3",
        defaults={"level": 3, "description": "Form 3 Secondary Level"}
    )
    print(f"Grade verified: {grade.name} (Curriculum: {curriculum.name}, Level: {grade.level})")

    subject, _ = Subject.objects.get_or_create(
        grade=grade,
        name="Chemistry",
        defaults={"description": "Form 3 Chemistry (KLB Syllabus)"}
    )
    print(f"Subject verified: {subject.name} under {grade.name}")

    topic, _ = Topic.objects.get_or_create(
        subject=subject,
        name="Topic 1: Gas Laws",
        defaults={
            "description": "Comprehensive study of the kinetic theory of matter, Boyle's Law, Charles's Law, Combined Gas Law, and Graham's Law of Diffusion.",
            "order": 1
        }
    )
    print(f"Topic verified: {topic.name} (ID: {topic.id}) under {subject.name}")

    # 2. Define Natural, Student-Facing Content Data Dictionary (Modules 1.1 - 1.5)
    modules_data = [
        {
            "unit_name": "Module 1.1: Introduction to the Gaseous State and Kinetic Theory",
            "unit_order": 1,
            "lesson_title": "Introduction to the Gaseous State and Kinetic Theory",
            "cards": [
                {
                    "page_number": 1,
                    "page_title": "Understanding the Gaseous State",
                    "block_type": "learning_goal",
                    "component_type": "learning_goal",
                    "content": {
                        "text": "In this module, you will explore the physical nature of gases at macroscopic, microscopic (particle), and symbolic levels, discover the 5 core principles of the Kinetic Theory of Matter, and see how gas particles exert pressure on the walls of their container."
                    }
                },
                {
                    "page_number": 1,
                    "page_title": "Why Do Heated Gases Expand?",
                    "block_type": "concept_explanation",
                    "component_type": "concept_explanation",
                    "content": {
                        "text": "On a hot afternoon in **Machakos, Garissa, or Mombasa**, have you ever noticed how firm—or even over-inflated—a bicycle or vehicle tyre becomes? Or perhaps you have watched a colourful weather balloon soaring high into the East African sky.\n\nIf we pump too much air into a tyre on a boiling hot day, the tyre can violently burst!\n\nWhy does this happen? The rubber doesn't break spontaneously. Inside that tyre, billions of invisible, microscopic gas particles are performing a frantic, high-speed dance. When heated, their movements become so energetic that they smash against the inner walls of the tyre with immense force, eventually tearing the rubber apart. Let's look behind the curtain of the invisible world of gases to understand what drives this behavior."
                    }
                },
                {
                    "page_number": 2,
                    "page_title": "Three Levels of Chemical Understanding",
                    "block_type": "concept_explanation",
                    "component_type": "concept_explanation",
                    "content": {
                        "text": "To truly master Chemistry, we always connect three complementary viewpoints:\n\n1. **What You Observe (Macroscopic)**:\n   Unlike solids (like an iron nail) or liquids (like water in a glass), gases have **no fixed shape and no fixed volume**. If you uncork a perfume bottle in one corner of a room, the scent quickly fills the entire room. Furthermore, gases can be easily **compressed** into a tiny fraction of their original volume.\n\n2. **What Happens at the Particle Level (Microscopic)**:\n   In solids, particles vibrate in fixed crystal lattice positions. In liquids, particles remain close but slide past one another. In gases, particles are **widely separated by vast empty spaces (a vacuum)**. They move in constant, rapid, random straight lines until they collide with each other or the container walls.\n\n3. **How We Represent This (Symbolic)**:\n   In Chemistry, the average energy of moving particles is their **Kinetic Energy** ($E_k$). The absolute temperature of a gas in Kelvin ($T$) is a direct measure of this average kinetic energy:\n   $$E_k \\propto T$$"
                    }
                },
                {
                    "page_number": 2,
                    "page_title": "States of Matter Comparison",
                    "block_type": "suggested_diagram",
                    "component_type": "suggested_diagram",
                    "content": {
                        "purpose": "Molecular models comparing solid, liquid, and gaseous particle arrangements.",
                        "instruction": "Three side-by-side molecular models: Solid (tightly packed regular lattice), Liquid (close, random packing), and Gas (widely spaced particles with velocity vectors colliding with walls).",
                        "resolved_image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/6/6d/States_of_matter_En.svg/800px-States_of_matter_En.svg.png"
                    },
                    "asset_info": {
                        "title": "Molecular Models of States of Matter",
                        "description": "Particle arrangement comparing solids, liquids, and gases.",
                        "url": "https://upload.wikimedia.org/wikipedia/commons/thumb/6/6d/States_of_matter_En.svg/800px-States_of_matter_En.svg.png"
                    }
                },
                {
                    "page_number": 3,
                    "page_title": "The Kinetic Theory of Matter",
                    "block_type": "concept_explanation",
                    "component_type": "concept_explanation",
                    "content": {
                        "text": "To explain gas behavior quantitatively, scientists formulated the **Kinetic Theory of Matter** for ideal gases based on five fundamental postulates:\n\n* **1. Vast Intermolecular Distances**: Gases consist of extremely small particles separated by distances vastly larger than their own sizes. Thus, the actual volume of the gas particles is negligible compared to the container volume.\n* **2. Negligible Intermolecular Forces**: Because particles are so far apart, forces of attraction or repulsion between them are negligible under normal conditions.\n* **3. Constant, Random Motion**: Gas particles are in perpetual, rapid, random, straight-line motion in all directions.\n* **4. Perfectly Elastic Collisions**: When gas particles collide with each other or container walls, no kinetic energy is lost ($E_{k,\\text{total}} = \\text{constant}$).\n* **5. Origin of Gas Pressure**: When billions of particles collide against the container walls every second, they exert an outward force. Gas Pressure ($P$) is the cumulative force per unit area:\n  $$P = \\frac{\\text{Force}}{\\text{Area}}$$"
                    }
                },
                {
                    "page_number": 4,
                    "page_title": "Gases in Everyday Life",
                    "block_type": "real_world_example",
                    "component_type": "real_world_example",
                    "content": {
                        "text": "### Liquefied Petroleum Gas (LPG Cylinders)\nIn homes across Kenya, we use gas cylinders (like K-Gas, Total Gas, or Pro-Gas). Under high mechanical pressure, gas particles are compressed so close together that they overcome negligible attractive forces and condense into a liquid. Opening the valve releases the pressure, allowing the liquid to instantly vaporize into a fast-moving gas for cooking.\n\n### Agricultural Biogas Digesters\nIn farming communities in **Meru, Eldoret, and Kiambu**, organic waste and cow dung undergo anaerobic fermentation inside sealed digesters. This generates methane gas ($CH_4$), which expands and exerts pressure against floating metal digester lids, indicating available fuel capacity for lighting and cooking."
                    }
                },
                {
                    "page_number": 5,
                    "page_title": "Applying the Kinetic Model to Compressed Air",
                    "block_type": "worked_example",
                    "component_type": "worked_example",
                    "content": {
                        "problem": "Using the Kinetic Theory of Matter, explain why pumping additional air into a fixed-volume car tyre increases the internal pressure.",
                        "steps": [
                            "**Given & Constants**: Constant tyre volume ($V$), constant temperature ($T$), increased quantity of gas particles ($N$).",
                            "**Governing Principle**: Gas Pressure ($P$) is the cumulative force per unit area exerted by colliding gas particles on container walls.",
                            "**Particle Behavior**: Introducing more gas particles into the same fixed volume crowds the particles together, shortening the distance between collisions.",
                            "**Collision Frequency**: The rate of molecular collisions against the inner tyre walls per unit area per second increases substantially.",
                            "**Conclusion**: The higher rate of particle-wall collisions produces a greater cumulative outward force, resulting in a higher measured pressure inside the tyre."
                        ]
                    }
                },
                {
                    "page_number": 6,
                    "page_title": "Think About This: Common Questions on Gases",
                    "block_type": "common_misconception",
                    "component_type": "common_misconception",
                    "content": {
                        "text": "### Is the space between gas particles filled with air?\nAir is itself a mixture of gas particles (primarily $N_2$ and $O_2$). The space between these individual particles contains nothing at all—it is a **complete vacuum**.\n\n### Do cold gas particles weigh more than hot gas particles?\nThe mass of an individual atom or molecule remains perfectly constant regardless of temperature. Cooling a gas only reduces the velocity and kinetic energy of the particles, causing them to move more slowly, not changing their actual mass."
                    }
                },
                {
                    "page_number": 7,
                    "page_title": "Practice Question: Gas Density",
                    "block_type": "knowledge_check",
                    "component_type": "knowledge_check",
                    "content": {
                        "check_type": "multiple_choice",
                        "question": "Which of the following statements best explains why gases have a much lower density than solids under normal conditions?",
                        "options": [
                            "Gas particles have much less mass than solid particles",
                            "Gas particles are separated by vast intermolecular spaces compared to their size",
                            "Gas particles lose energy when they collide with container walls",
                            "Gas particles exert strong repulsive forces on each other"
                        ],
                        "answer": "B",
                        "explanation": "According to the Kinetic Theory of Matter, gas particles are separated by very large empty spaces (vacuums), meaning a given volume of gas contains far fewer particles (and thus far less mass) than the same volume of a tightly packed solid."
                    }
                },
                {
                    "page_number": 7,
                    "page_title": "Practice Question: Absolute Temperature",
                    "block_type": "knowledge_check",
                    "component_type": "knowledge_check",
                    "content": {
                        "check_type": "multiple_choice",
                        "question": "According to the Kinetic Theory of Matter, what happens to the particles of a gas when its temperature increases from $300\\text{ K}$ to $600\\text{ K}$?",
                        "options": [
                            "Their average kinetic energy doubles",
                            "The individual mass of each particle doubles",
                            "The particles stop moving randomly and move in circles",
                            "The particles expand in physical size"
                        ],
                        "answer": "A",
                        "explanation": "The absolute temperature of a gas in Kelvin ($T$) is directly proportional to the average kinetic energy ($E_k$) of its particles ($E_k \\propto T$). Doubling the Kelvin temperature doubles their average kinetic energy."
                    }
                },
                {
                    "page_number": 8,
                    "page_title": "Key Takeaways: Kinetic Theory",
                    "block_type": "summary",
                    "component_type": "summary",
                    "content": {
                        "text": "### Core Principles: Kinetic Theory of Gases\n- **Particle Arrangement**: Particles are widely spaced with negligible intermolecular forces and volumes.\n- **Motion & Collisions**: Particles move in rapid, random, straight-line motion undergoing perfectly elastic collisions.\n- **Gas Pressure ($P$)**: Arises from billions of particle collisions against the container walls per second ($P = \\frac{F}{A}$).\n- **Temperature ($T$)**: Absolute temperature in Kelvin is a direct measure of average particle kinetic energy ($E_k \\propto T$)."
                    }
                }
            ]
        },

        {
            "unit_name": "Module 1.2: Boyle's Law (Pressure-Volume Relationship)",
            "unit_order": 2,
            "lesson_title": "Boyle's Law (Pressure-Volume Relationship)",
            "cards": [
                {
                    "page_number": 1,
                    "page_title": "Pressure and Volume in Gases",
                    "block_type": "learning_goal",
                    "component_type": "learning_goal",
                    "content": {
                        "text": "In this module, you will master Boyle's Law, understand the inverse seesaw relationship between gas pressure and volume ($P_1V_1 = P_2V_2$), and calculate volume changes when pressure shifts."
                    }
                },
                {
                    "page_number": 1,
                    "page_title": "The Trapped Air in a Bicycle Pump",
                    "block_type": "concept_explanation",
                    "component_type": "concept_explanation",
                    "content": {
                        "text": "Imagine placing your thumb tightly over the nozzle of a bicycle pump and pushing the handle down as hard as you can.\n\nAt first, the handle glides smoothly. But the further you push, the harder it becomes to compress the trapped air. If you let go of the handle, it **springs right back up**!\n\nWhat is going on inside the barrel? By pushing the handle down, you forced the same number of air particles into a much smaller volume. Trapped in a tight space, the particles collide with the walls and your thumb far more frequently, creating a massive pushback pressure. This inverse relationship between pressure and volume is known as **Boyle's Law**."
                    }
                },
                {
                    "page_number": 2,
                    "page_title": "Formal Statement & Mathematical Formula",
                    "block_type": "concept_explanation",
                    "component_type": "concept_explanation",
                    "content": {
                        "text": "### Boyle's Law Statement:\n**The volume of a fixed mass of gas is inversely proportional to its pressure, provided the temperature remains constant.**\n\n### Mathematical Formulation:\n$$V \\propto \\frac{1}{P} \\quad (\\text{at constant } T)$$\n$$V = \\frac{k}{P} \\quad \\implies \\quad P \\times V = k \\quad (\\text{where } k \\text{ is a constant})$$\n\nFor a gas sample changing from state 1 ($P_1, V_1$) to state 2 ($P_2, V_2$) at constant temperature:\n$$P_1V_1 = P_2V_2$$\n\n### Pressure Units in Secondary Chemistry:\n- **Pascals ($\\text{Pa}$)**: $1\\text{ kPa} = 1000\\text{ Pa} = 1000\\text{ N m}^{-2}$\n- **Atmospheres ($\\text{atm}$)**: $1\\text{ atm} = 1.01325 \\times 10^5\\text{ Pa} = 101.325\\text{ kPa}$\n- **Millimetres of Mercury ($\\text{mmHg}$)**: $1\\text{ atm} = 760\\text{ mmHg}$"
                    }
                },
                {
                    "page_number": 2,
                    "page_title": "Graphical Representations of Boyle's Law",
                    "block_type": "suggested_diagram",
                    "component_type": "suggested_diagram",
                    "content": {
                        "purpose": "Comparison of Boyle's Law graphs: P vs V (hyperbola), P vs 1/V (straight line through origin), and PV vs P (horizontal line).",
                        "instruction": "Three graphs: (1) Graph of P against V showing a downward smooth curve (rectangular hyperbola). (2) Graph of P against 1/V showing a direct straight line starting at origin. (3) Graph of PV against P showing a horizontal straight line.",
                        "resolved_image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/1/15/Boyles_Law_animated.gif/800px-Boyles_Law_animated.gif"
                    },
                    "asset_info": {
                        "title": "Boyle's Law Graphs & Animation",
                        "description": "Visualizing P-V inverse curve and P vs 1/V linear relationship.",
                        "url": "https://upload.wikimedia.org/wikipedia/commons/thumb/1/15/Boyles_Law_animated.gif/800px-Boyles_Law_animated.gif"
                    }
                },
                {
                    "page_number": 3,
                    "page_title": "Deep-Sea Scuba Diving & Ear Barotrauma",
                    "block_type": "real_world_example",
                    "component_type": "real_world_example",
                    "content": {
                        "text": "### Scuba Diving in Watamu & Diani\nWhen a scuba diver explores the coral reefs of the Kenyan coast at a depth of $20\\text{ metres}$, the water pressure triples from $1\\text{ atm}$ to $3\\text{ atm}$.\n\nAccording to Boyle's Law ($P_1V_1 = P_2V_2$), the volume of air inside the diver's lungs and middle ear shrinks to one-third ($1/3$) of its surface volume. Divers must frequently \"equalize\" their ears by gently blowing with a pinched nose to force air back into the eustachian tubes and prevent ear drum rupture.\n\nWhen ascending to the surface, the diver **must never hold their breath**. As pressure drops from $3\\text{ atm}$ back to $1\\text{ atm}$, trapped air in the lungs expands 3-fold. Holding one's breath would cause the lungs to over-expand and tear!"
                    }
                },
                {
                    "page_number": 4,
                    "page_title": "Calculating Gas Volume Under Changing Pressure",
                    "block_type": "worked_example",
                    "component_type": "worked_example",
                    "content": {
                        "problem": "A sample of hydrogen gas occupies a volume of $250\\text{ cm}^3$ at a pressure of $750\\text{ mmHg}$. Calculate the volume the gas will occupy if the pressure is increased to $1000\\text{ mmHg}$ at constant temperature.",
                        "steps": [
                            "**Identify Given Values**: Initial pressure $P_1 = 750\\text{ mmHg}$, Initial volume $V_1 = 250\\text{ cm}^3$, Final pressure $P_2 = 1000\\text{ mmHg}$, Final volume $V_2 = ?$",
                            "**State the Governing Formula**: $P_1V_1 = P_2V_2$",
                            "**Substitute Values into Formula**: $750\\text{ mmHg} \\times 250\\text{ cm}^3 = 1000\\text{ mmHg} \\times V_2$",
                            "**Solve for $V_2$**:\n$$187,500 = 1000 \\times V_2$$\n$$V_2 = \\frac{187,500}{1000} = 187.5\\text{ cm}^3$$",
                            "**Scientific Sense Check**: The pressure increased from $750$ to $1000\\text{ mmHg}$ (factor of $1.33$), so the volume must decrease from $250$ to $187.5\\text{ cm}^3$. The result is scientifically consistent."
                        ]
                    }
                },
                {
                    "page_number": 5,
                    "page_title": "Converting Between Pressure Units in Boyle's Law",
                    "block_type": "worked_example",
                    "component_type": "worked_example",
                    "content": {
                        "problem": "A gas cylinder contains $0.05\\text{ m}^3$ of oxygen gas at a pressure of $2.0\\text{ atmospheres}$. What volume will this gas occupy at standard atmospheric pressure of $101.325\\text{ kPa}$ at constant temperature? ($1\\text{ atm} = 101.325\\text{ kPa}$)",
                        "steps": [
                            "**Convert Units to Consistent Scale**:\n- Initial Pressure $P_1 = 2.0\\text{ atm} = 2.0 \\times 101.325\\text{ kPa} = 202.65\\text{ kPa}$\n- Initial Volume $V_1 = 0.05\\text{ m}^3$\n- Final Pressure $P_2 = 101.325\\text{ kPa}$",
                            "**State the Formula**: $P_1V_1 = P_2V_2$",
                            "**Substitute and Calculate**:\n$$202.65\\text{ kPa} \\times 0.05\\text{ m}^3 = 101.325\\text{ kPa} \\times V_2$$\n$$10.1325 = 101.325 \\times V_2$$\n$$V_2 = \\frac{10.1325}{101.325} = 0.10\\text{ m}^3$$",
                            "**Conclusion**: When the pressure is halved from $2\\text{ atm}$ to $1\\text{ atm}$, the gas volume doubles to $0.10\\text{ m}^3$ ($100\\text{ dm}^3$)."
                        ]
                    }
                },
                {
                    "page_number": 6,
                    "page_title": "Think About This: Pressure-Volume Pitfalls",
                    "block_type": "common_misconception",
                    "component_type": "common_misconception",
                    "content": {
                        "text": "### Does doubling the pressure double the volume?\nNo! Pressure and volume have an **inverse** relationship, not a direct one. If you double the pressure ($2 \\times P$), the volume is cut in half ($\\frac{1}{2} V$).\n\n### Does Boyle's Law apply if temperature changes?\nNo. Boyle's Law is strictly valid only when the temperature remains perfectly constant. If the gas heats up while being compressed, temperature expansion will interfere with the pressure-volume ratio."
                    }
                },
                {
                    "page_number": 7,
                    "page_title": "Practice Question: P-V Calculation",
                    "block_type": "knowledge_check",
                    "component_type": "knowledge_check",
                    "content": {
                        "check_type": "multiple_choice",
                        "question": "A syringe contains $60\\text{ cm}^3$ of air at a pressure of $1.0\\text{ atm}$. If the plunger is pressed until the volume decreases to $15\\text{ cm}^3$ at constant temperature, what is the new pressure inside the syringe?",
                        "options": [
                            "$0.25\\text{ atm}$",
                            "$2.0\\text{ atm}$",
                            "$4.0\\text{ atm}$",
                            "$0.50\\text{ atm}$"
                        ],
                        "answer": "C",
                        "explanation": "Using Boyle's Law $P_1V_1 = P_2V_2$: $(1.0\\text{ atm}) \\times (60\\text{ cm}^3) = P_2 \\times (15\\text{ cm}^3) \\implies P_2 = \\frac{60}{15} = 4.0\\text{ atm}$. The volume decreased by a factor of 4, so the pressure increased 4-fold."
                    }
                },
                {
                    "page_number": 7,
                    "page_title": "Practice Question: Graphical Interpretation",
                    "block_type": "knowledge_check",
                    "component_type": "knowledge_check",
                    "content": {
                        "check_type": "multiple_choice",
                        "question": "Which of the following plots will produce a straight line passing through the origin for an ideal gas at constant temperature?",
                        "options": [
                            "Pressure ($P$) against Volume ($V$)",
                            "Pressure ($P$) against $\\frac{1}{\\text{Volume}} \\left(\\frac{1}{V}\\right)$",
                            "$PV$ against Pressure ($P$)",
                            "Volume ($V$) against Temperature in $^\\circ\\text{C}$"
                        ],
                        "answer": "B",
                        "explanation": "Since $P \\propto \\frac{1}{V}$, a plot of $P$ on the y-axis against $\\frac{1}{V}$ on the x-axis yields a straight line with a constant gradient ($k$) passing directly through the origin $(0,0)$."
                    }
                },
                {
                    "page_number": 8,
                    "page_title": "Key Takeaways: Boyle's Law",
                    "block_type": "summary",
                    "component_type": "summary",
                    "content": {
                        "text": "### Core Principles: Boyle's Law\n- **Statement**: Volume is inversely proportional to pressure at constant temperature ($V \\propto \\frac{1}{P}$).\n- **Equation**: $P_1V_1 = P_2V_2 = \\text{constant } (k)$.\n- **Microscopic Mechanism**: Halving container volume doubles particle collision frequency against the walls, doubling the pressure.\n- **Key Graphs**: $P$ vs $V$ is a hyperbolic curve; $P$ vs $\\frac{1}{V}$ is a direct linear graph through $(0,0)$."
                    }
                }
            ]
        },

        {
            "unit_name": "Module 1.3: Charles's Law (Temperature-Volume Relationship)",
            "unit_order": 3,
            "lesson_title": "Charles's Law (Temperature-Volume Relationship)",
            "cards": [
                {
                    "page_number": 1,
                    "page_title": "Temperature and Volume in Gases",
                    "block_type": "learning_goal",
                    "component_type": "learning_goal",
                    "content": {
                        "text": "In this module, you will discover Charles's Law, explore why gas volume expands when temperature rises, master the Absolute Temperature (Kelvin) scale, and solve thermal expansion problems using $\\frac{V_1}{T_1} = \\frac{V_2}{T_2}$."
                    }
                },
                {
                    "page_number": 1,
                    "page_title": "The Ping-Pong Ball Recovery Trick",
                    "block_type": "concept_explanation",
                    "component_type": "concept_explanation",
                    "content": {
                        "text": "Have you ever stepped on a table tennis (ping-pong) ball during a games lesson at school, denting it inwards without puncturing the plastic?\n\nDon't throw it in the dustbin! Drop the dented ball into a cup of boiling water.\n\nWithin seconds, the dent pops back out, restoring the ball to a smooth sphere! Why? When the trapped air inside heats up, the particles gain kinetic energy, moving faster and colliding harder against the inner walls, pushing the dented plastic outward. This direct relationship between temperature and volume is known as **Charles's Law**."
                    }
                },
                {
                    "page_number": 2,
                    "page_title": "Absolute Zero & The Kelvin Temperature Scale",
                    "block_type": "concept_explanation",
                    "component_type": "concept_explanation",
                    "content": {
                        "text": "### The Celsius vs. Kelvin Scale Discovery:\nIf we measure the volume of a gas at different Celsius temperatures and plot volume $V$ against Celsius temperature $t$ ($^\\circ\\text{C}$), the straight line intercepts the temperature axis at exactly **$-273.15^\\circ\\text{C}$** when extrapolated to zero volume.\n\nThis theoretical temperature where all molecular motion ceases and gas volume hypothetically becomes zero is called **Absolute Zero ($0\\text{ K}$)**.\n\nTo make temperature directly proportional to gas volume, British physicist Lord Kelvin established the **Absolute Temperature Scale** in Kelvin ($\\text{K}$):\n$$T\\text{ (in Kelvin)} = t\\text{ (in }^\\circ\\text{C)} + 273$$\n\n### CRITICAL EXAM RULE:\n**You MUST ALWAYS convert temperatures to Kelvin ($T = t + 273$) before using any gas law equation! Calculating with Celsius yields completely incorrect answers.**"
                    }
                },
                {
                    "page_number": 2,
                    "page_title": "Charles's Law Graph and Absolute Zero",
                    "block_type": "suggested_diagram",
                    "component_type": "suggested_diagram",
                    "content": {
                        "purpose": "Graph of Volume against Temperature in Celsius showing extrapolation to -273 °C (Absolute Zero), compared with Volume against Kelvin temperature passing through origin.",
                        "instruction": "Two graphs: (1) Volume (y-axis) vs Temperature in Celsius (x-axis) showing a straight line intersecting the x-axis at -273 °C. (2) Volume vs Temperature in Kelvin showing a straight line passing through (0,0).",
                        "resolved_image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/a/a4/Charles_and_Gay-Lussac%27s_Law_animated.gif/800px-Charles_and_Gay-Lussac%27s_Law_animated.gif"
                    },
                    "asset_info": {
                        "title": "Charles's Law Thermal Expansion & Graphs",
                        "description": "Visualizing V-T linear relationship and Absolute Zero extrapolation.",
                        "url": "https://upload.wikimedia.org/wikipedia/commons/thumb/a/a4/Charles_and_Gay-Lussac%27s_Law_animated.gif/800px-Charles_and_Gay-Lussac%27s_Law_animated.gif"
                    }
                },
                {
                    "page_number": 3,
                    "page_title": "Formal Statement & Mathematical Equation",
                    "block_type": "concept_explanation",
                    "component_type": "concept_explanation",
                    "content": {
                        "text": "### Charles's Law Statement:\n**The volume of a fixed mass of gas is directly proportional to its absolute temperature (in Kelvin), provided the pressure remains constant.**\n\n### Mathematical Formulation:\n$$V \\propto T \\quad (\\text{at constant } P)$$\n$$V = k \\times T \\quad \\implies \\quad \\frac{V}{T} = k \\quad (\\text{where } k \\text{ is a constant})$$\n\nFor a gas sample changing from state 1 ($V_1, T_1$) to state 2 ($V_2, T_2$) at constant pressure:\n$$\\frac{V_1}{T_1} = \\frac{V_2}{T_2}$$"
                    }
                },
                {
                    "page_number": 4,
                    "page_title": "Hot-Air Ballooning Across the Masai Mara",
                    "block_type": "real_world_example",
                    "component_type": "real_world_example",
                    "content": {
                        "text": "### Tourism Flights Over the Masai Mara\nEvery morning at sunrise in the **Masai Mara National Reserve**, giant hot-air balloons carry tourists high above roaming herds of wildebeest and zebras.\n\nThe pilot ignites powerful propane burners at the mouth of the balloon envelope. As the trapped air heats up, it expands according to Charles's Law ($\\frac{V_1}{T_1} = \\frac{V_2}{T_2}$). Because the envelope has fixed volume, excess expanding air spills out the bottom.\n\nThe remaining heated air inside has fewer particles per unit volume, making it **less dense than the surrounding cold morning air**. This density difference generates a buoyant upward lift, carrying the balloon into the sky."
                    }
                },
                {
                    "page_number": 4,
                    "page_title": "Calculating Volume Expansion with Temperature",
                    "block_type": "worked_example",
                    "component_type": "worked_example",
                    "content": {
                        "problem": "A sample of nitrogen gas has a volume of $450\\text{ cm}^3$ at $27^\\circ\\text{C}$. Calculate its volume if the temperature is increased to $127^\\circ\\text{C}$ while the pressure remains constant.",
                        "steps": [
                            "**Convert Temperatures to Kelvin**:\n- $T_1 = 27^\\circ\\text{C} + 273 = 300\\text{ K}$\n- $T_2 = 127^\\circ\\text{C} + 273 = 400\\text{ K}$",
                            "**Identify Volumes**: $V_1 = 450\\text{ cm}^3$, $V_2 = ?$",
                            "**State the Formula**: $\\frac{V_1}{T_1} = \\frac{V_2}{T_2}$",
                            "**Substitute Values**:\n$$\\frac{450\\text{ cm}^3}{300\\text{ K}} = \\frac{V_2}{400\\text{ K}}$$",
                            "**Solve for $V_2$**:\n$$1.5 = \\frac{V_2}{400} \\implies V_2 = 1.5 \\times 400 = 600\\text{ cm}^3$$",
                            "**Scientific Reflection**: The absolute temperature increased from $300\\text{ K}$ to $400\\text{ K}$ (a factor of $1.33$), so the volume expanded from $450\\text{ cm}^3$ to $600\\text{ cm}^3$."
                        ]
                    }
                },
                {
                    "page_number": 5,
                    "page_title": "Determining Final Temperature in Celsius",
                    "block_type": "worked_example",
                    "component_type": "worked_example",
                    "content": {
                        "problem": "A gas occupies $200\\text{ cm}^3$ at $0^\\circ\\text{C}$. To what temperature in $^\\circ\\text{C}$ must it be heated at constant pressure for its volume to double to $400\\text{ cm}^3$?",
                        "steps": [
                            "**Convert Initial Temperature**: $T_1 = 0^\\circ\\text{C} + 273 = 273\\text{ K}$.",
                            "**Identify Given Values**: $V_1 = 200\\text{ cm}^3$, $V_2 = 400\\text{ cm}^3$.",
                            "**State Formula**: $\\frac{V_1}{T_1} = \\frac{V_2}{T_2}$",
                            "**Substitute Values**:\n$$\\frac{200}{273} = \\frac{400}{T_2} \\implies T_2 = \\frac{400 \\times 273}{200} = 2 \\times 273 = 546\\text{ K}$$",
                            "**Convert Final Temperature to Celsius**:\n$$t_2 = 546 - 273 = 273^\\circ\\text{C}$$",
                            "**Common Exam Trap**: Doubling the volume from $0^\\circ\\text{C}$ requires doubling the *Kelvin* temperature ($273\\text{ K} \\rightarrow 546\\text{ K}$), which corresponds to $273^\\circ\\text{C}$, NOT $0^\\circ\\text{C} \\times 2 = 0^\\circ\\text{C}$!"
                        ]
                    }
                },
                {
                    "page_number": 6,
                    "page_title": "Think About This: Why Celsius Fails in Gas Laws",
                    "block_type": "common_misconception",
                    "component_type": "common_misconception",
                    "content": {
                        "text": "### Why can't we use Celsius directly in Charles's Law calculations?\nThe Celsius scale sets its zero at the arbitrary freezing point of water ($0^\\circ\\text{C}$), which is not the point of zero kinetic energy. If you calculated $\\frac{V_1}{0^\\circ\\text{C}}$, you would be dividing by zero, which is mathematically undefined!\n\nOnly the Kelvin scale starts at true physical zero energy ($0\\text{ K}$), making $V$ directly proportional to $T$."
                    }
                },
                {
                    "page_number": 7,
                    "page_title": "Practice Question: Absolute Zero Definition",
                    "block_type": "knowledge_check",
                    "component_type": "knowledge_check",
                    "content": {
                        "check_type": "multiple_choice",
                        "question": "What is the physical significance of Absolute Zero ($-273.15^\\circ\\text{C}$ or $0\\text{ K}$) in the Kinetic Theory of Matter?",
                        "options": [
                            "It is the temperature at which water freezes into ice",
                            "It is the theoretical temperature at which all molecular kinetic energy ceases and gas volume becomes zero",
                            "It is the boiling point of liquid nitrogen",
                            "It is the temperature where gas particles reach maximum speed"
                        ],
                        "answer": "B",
                        "explanation": "Absolute Zero ($0\\text{ K}$) is the lowest possible theoretical temperature where all thermal kinetic energy of particles ceases and the volume of an ideal gas extrapolates to zero."
                    }
                },
                {
                    "page_number": 7,
                    "page_title": "Practice Question: Thermal Expansion",
                    "block_type": "knowledge_check",
                    "component_type": "knowledge_check",
                    "content": {
                        "check_type": "multiple_choice",
                        "question": "A balloon has a volume of $2.0\\text{ dm}^3$ at $20^\\circ\\text{C}$. If it is placed in a refrigerator at $-10^\\circ\\text{C}$ at constant pressure, what is the new volume of the balloon?",
                        "options": [
                            "$-1.0\\text{ dm}^3$",
                            "$1.80\\text{ dm}^3$",
                            "$1.50\\text{ dm}^3$",
                            "$2.20\\text{ dm}^3$"
                        ],
                        "answer": "B",
                        "explanation": "Convert temperatures to Kelvin: $T_1 = 20 + 273 = 293\\text{ K}$, $T_2 = -10 + 273 = 263\\text{ K}$. Using Charles's Law: $\\frac{2.0}{293} = \\frac{V_2}{263} \\implies V_2 = \\frac{2.0 \\times 263}{293} \\approx 1.795\\text{ dm}^3 \\approx 1.80\\text{ dm}^3$."
                    }
                },
                {
                    "page_number": 8,
                    "page_title": "Key Takeaways: Charles's Law",
                    "block_type": "summary",
                    "component_type": "summary",
                    "content": {
                        "text": "### Core Principles: Charles's Law\n- **Statement**: Volume is directly proportional to absolute Kelvin temperature at constant pressure ($V \\propto T$).\n- **Formula**: $\\frac{V_1}{T_1} = \\frac{V_2}{T_2} = k$.\n- **Kelvin Conversion**: Always add 273 to Celsius ($T = t + 273$).\n- **Absolute Zero**: $0\\text{ K} = -273^\\circ\\text{C}$, the point of zero particle kinetic motion."
                    }
                }
            ]
        },

        {
            "unit_name": "Module 1.4: The Combined Gas Law and Standard Conditions (S.T.P. & R.T.P.)",
            "unit_order": 4,
            "lesson_title": "The Combined Gas Law and Standard Conditions (S.T.P. & R.T.P.)",
            "cards": [
                {
                    "page_number": 1,
                    "page_title": "Combining the Gas Laws",
                    "block_type": "learning_goal",
                    "component_type": "learning_goal",
                    "content": {
                        "text": "In this module, you will bring Boyle's and Charles's laws together into one combined equation ($\\frac{P_1V_1}{T_1} = \\frac{P_2V_2}{T_2}$), master standard temperature and pressure conditions (s.t.p. and r.t.p.), and solve multi-variable gas problems where pressure, volume, and temperature change simultaneously."
                    }
                },
                {
                    "page_number": 1,
                    "page_title": "Weather Balloons in the Upper Atmosphere",
                    "block_type": "concept_explanation",
                    "component_type": "concept_explanation",
                    "content": {
                        "text": "At the Kenya Meteorological Department in **Dagoretti, Nairobi**, meteorologists launch helium-filled latex weather balloons into the upper atmosphere. When launched, the balloon is only partially inflated.\n\nAs the balloon ascends high into the stratosphere, two opposing environmental shifts occur simultaneously:\n1. **Surrounding atmospheric pressure drops dramatically** (Boyle's Law indicates this should expand the balloon).\n2. **Surrounding air temperature plunges to $-50^\\circ\\text{C}$** (Charles's Law indicates this should shrink the balloon).\n\nHow do scientists calculate the final balloon volume when both pressure and temperature are changing at the same time? Today we combine our gas laws into a unified equation: the **Combined Gas Law**."
                    }
                },
                {
                    "page_number": 2,
                    "page_title": "Deriving the Unified Equation",
                    "block_type": "concept_explanation",
                    "component_type": "concept_explanation",
                    "content": {
                        "text": "Boyle's and Charles's laws can be combined into one equation for a fixed mass of gas:\n\n* **Boyle's Law**: $V \\propto \\frac{1}{P}$ (at constant $T$)\n* **Charles's Law**: $V \\propto T$ (at constant $P$)\n\nCombining both relationships:\n$$V \\propto \\frac{T}{P} \\quad \\implies \\quad V = k \\frac{T}{P} \\quad \\implies \\quad \\frac{PV}{T} = k$$\n\nFor a gas sample changing between two states $(P_1, V_1, T_1)$ and $(P_2, V_2, T_2)$:\n$$\\frac{P_1V_1}{T_1} = \\frac{P_2V_2}{T_2}$$\n\n### Self-Consistency:\n- If temperature is constant ($T_1 = T_2$), the equation simplifies to $P_1V_1 = P_2V_2$ (Boyle's Law).\n- If pressure is constant ($P_1 = P_2$), the equation simplifies to $\\frac{V_1}{T_1} = \\frac{V_2}{T_2}$ (Charles's Law)."
                    }
                },
                {
                    "page_number": 3,
                    "page_title": "Standard Laboratory Conditions",
                    "block_type": "definition_card",
                    "component_type": "definition_card",
                    "content": {
                        "term": "Standard Gas Conditions",
                        "content": "Because gas volume depends heavily on ambient pressure and temperature, gas measurements are standardized internationally:\n\n### 1. Standard Temperature and Pressure (s.t.p.)\n* **Standard Temperature**: $0^\\circ\\text{C} = 273\\text{ K}$\n* **Standard Pressure**: $1\\text{ atm} = 760\\text{ mmHg} = 1.01325 \\times 10^5\\text{ Pa} = 101.325\\text{ kPa}$\n\n### 2. Room Temperature and Pressure (r.t.p.)\n* **Room Temperature**: $25^\\circ\\text{C} = 298\\text{ K}$\n* **Room Pressure**: $1\\text{ atm} = 760\\text{ mmHg} = 1.01325 \\times 10^5\\text{ Pa}$\n\n*Note*: When a problem specifies \"at s.t.p.\" or \"at r.t.p.\", it provides $T_2$ and $P_2$ values directly!"
                    }
                },
                {
                    "page_number": 3,
                    "page_title": "Stratospheric Expansion of Weather Balloons",
                    "block_type": "suggested_diagram",
                    "component_type": "suggested_diagram",
                    "content": {
                        "purpose": "Illustration of weather balloon expansion at high altitude under simultaneous P and T variations.",
                        "instruction": "Weather balloon launch at sea level (r.t.p., 1 atm, 298 K, compact volume) compared to stratospheric altitude (0.1 atm, 223 K, expanded volume).",
                        "resolved_image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/a/a4/NOAA_weather_balloon_launch.jpg/800px-NOAA_weather_balloon_launch.jpg"
                    },
                    "asset_info": {
                        "title": "Weather Balloon Stratospheric Expansion",
                        "description": "Meteorological balloon launch showing Combined Gas Law in action.",
                        "url": "https://upload.wikimedia.org/wikipedia/commons/thumb/a/a4/NOAA_weather_balloon_launch.jpg/800px-NOAA_weather_balloon_launch.jpg"
                    }
                },
                {
                    "page_number": 4,
                    "page_title": "Aircraft Cabin Pressurization Systems",
                    "block_type": "real_world_example",
                    "component_type": "real_world_example",
                    "content": {
                        "text": "### Commercial Aircraft Cabin Engineering\nJet airliners cruise at altitudes above $10,000\\text{ metres}$, where ambient outside conditions are extreme: atmospheric pressure drops to $\\approx 0.25\\text{ atm}$ and temperature plunges to $-50^\\circ\\text{C}$. Aeronautical engineers use the Combined Gas Law to design cabin air compression and heating systems, ensuring passengers breathe air at comfortable physiological pressure and temperature."
                    }
                },
                {
                    "page_number": 5,
                    "page_title": "Calculating Gas Volume at Standard Conditions (s.t.p.)",
                    "block_type": "worked_example",
                    "component_type": "worked_example",
                    "content": {
                        "problem": "At $27^\\circ\\text{C}$ and $740\\text{ mmHg}$ pressure, a sample of nitrogen gas occupies $30\\text{ cm}^3$. Calculate its volume at s.t.p.",
                        "steps": [
                            "**Given Data**: $P_1 = 740\\text{ mmHg}$, $V_1 = 30\\text{ cm}^3$, $T_1 = 27 + 273 = 300\\text{ K}$.",
                            "**Conditions at s.t.p.**: $P_2 = 760\\text{ mmHg}$, $T_2 = 273\\text{ K}$.",
                            "**Formula**: $\\frac{P_1V_1}{T_1} = \\frac{P_2V_2}{T_2}$",
                            "**Substitution**: $\\frac{740 \\times 30}{300} = \\frac{760 \\times V_2}{273}$",
                            "**Calculation**:\n$$\\frac{22,200}{300} = 74$$\n$$74 = \\frac{760 V_2}{273} \\implies V_2 = \\frac{74 \\times 273}{760} = \\frac{20,202}{760} \\approx 26.58\\text{ cm}^3$$",
                            "**Scientific Meaning**: The volume at s.t.p. is $26.58\\text{ cm}^3$ (or $26.6\\text{ cm}^3$)."
                        ]
                    }
                },
                {
                    "page_number": 5,
                    "page_title": "Determining Final Temperature Under Dual Changes",
                    "block_type": "worked_example",
                    "component_type": "worked_example",
                    "content": {
                        "problem": "A gas occupies $100\\text{ cm}^3$ at $-15^\\circ\\text{C}$ and $650\\text{ mmHg}$. At what temperature in $^\\circ\\text{C}$ will it occupy $150\\text{ cm}^3$ at $680\\text{ mmHg}$?",
                        "steps": [
                            "**Given Data**: $V_1 = 100\\text{ cm}^3$, $T_1 = -15 + 273 = 258\\text{ K}$, $P_1 = 650\\text{ mmHg}$, $V_2 = 150\\text{ cm}^3$, $P_2 = 680\\text{ mmHg}$.",
                            "**Formula**: $\\frac{P_1V_1}{T_1} = \\frac{P_2V_2}{T_2}$",
                            "**Substitution**: $\\frac{650 \\times 100}{258} = \\frac{680 \\times 150}{T_2}$",
                            "**Calculation**:\n$$251.938 = \\frac{102,000}{T_2} \\implies T_2 = \\frac{102,000}{251.938} \\approx 404.86\\text{ K}$$",
                            "**Convert to Celsius**: $t_2 = 404.86 - 273 = 131.86^\\circ\\text{C}$",
                            "**Scientific Meaning**: The gas reaches $150\\text{ cm}^3$ at a temperature of $131.86^\\circ\\text{C}$."
                        ]
                    }
                },
                {
                    "page_number": 6,
                    "page_title": "Think About This: Pressure Units in Calculations",
                    "block_type": "common_misconception",
                    "component_type": "common_misconception",
                    "content": {
                        "text": "### How do we handle different pressure units?\n$760\\text{ mmHg}$, $1\\text{ atm}$, and $1.01325 \\times 10^5\\text{ Pa}$ all describe identical standard atmospheric pressure. When solving gas equations, you must always ensure $P_1$ and $P_2$ share the same unit before substituting them into formulas!"
                    }
                },
                {
                    "page_number": 7,
                    "page_title": "Practice Question: Stratospheric Expansion",
                    "block_type": "knowledge_check",
                    "component_type": "knowledge_check",
                    "content": {
                        "check_type": "multiple_choice",
                        "question": "A weather balloon contains $80.0\\text{ m}^3$ of helium at launch ($27^\\circ\\text{C}$ and $1.0\\text{ atm}$). In the stratosphere, temperature drops to $-23^\\circ\\text{C}$ and pressure drops to $0.2\\text{ atm}$. What is the final helium volume?",
                        "options": [
                            "$400.0\\text{ m}^3$",
                            "$333.3\\text{ m}^3$",
                            "$250.0\\text{ m}^3$",
                            "$160.0\\text{ m}^3$"
                        ],
                        "answer": "B",
                        "explanation": "Convert temperatures to Kelvin: $T_1 = 27 + 273 = 300\\text{ K}$, $T_2 = -23 + 273 = 250\\text{ K}$. Apply Combined Gas Law: $\\frac{1.0 \\times 80.0}{300} = \\frac{0.2 \\times V_2}{250} \\implies 0.2667 = \\frac{0.2 V_2}{250} \\implies V_2 = \\frac{0.2667 \\times 250}{0.2} = 333.3\\text{ m}^3$."
                    }
                },
                {
                    "page_number": 7,
                    "page_title": "Practice Question: Converting to S.T.P.",
                    "block_type": "knowledge_check",
                    "component_type": "knowledge_check",
                    "content": {
                        "check_type": "multiple_choice",
                        "question": "What is the standard temperature and standard pressure defined internationally at s.t.p.?",
                        "options": [
                            "$25^\\circ\\text{C} \\text{ (298 K)}$ and $1\\text{ atm} \\text{ (760 mmHg)}$",
                            "$0^\\circ\\text{C} \\text{ (273 K)}$ and $1\\text{ atm} \\text{ (760 mmHg)}$",
                            "$100^\\circ\\text{C} \\text{ (373 K)}$ and $1\\text{ kPa}$",
                            "$0^\\circ\\text{C} \\text{ (273 K)}$ and $0\\text{ atm}$"
                        ],
                        "answer": "B",
                        "explanation": "Standard Temperature and Pressure (s.t.p.) is defined internationally as $0^\\circ\\text{C}$ ($273\\text{ K}$) and $1\\text{ atmosphere}$ ($760\\text{ mmHg}$ or $101.325\\text{ kPa}$)."
                    }
                },
                {
                    "page_number": 8,
                    "page_title": "Key Takeaways: Combined Gas Law",
                    "block_type": "summary",
                    "component_type": "summary",
                    "content": {
                        "text": "### Core Principles: Combined Gas Law\n- **Formula**: $\\frac{P_1V_1}{T_1} = \\frac{P_2V_2}{T_2} = k$.\n- **Standard Conditions (s.t.p.)**: $T = 273\\text{ K } (0^\\circ\\text{C}), P = 760\\text{ mmHg } (1\\text{ atm})$.\n- **Room Conditions (r.t.p.)**: $T = 298\\text{ K } (25^\\circ\\text{C}), P = 760\\text{ mmHg } (1\\text{ atm})$.\n- **Calculation Rule**: Always use absolute temperatures in Kelvin ($T = t + 273$)."
                    }
                }
            ]
        },

        {
            "unit_name": "Module 1.5: Graham's Law of Diffusion and Kinetic Theory",
            "unit_order": 5,
            "lesson_title": "Graham's Law of Diffusion and Kinetic Theory",
            "cards": [
                {
                    "page_number": 1,
                    "page_title": "Diffusion and Molecular Speeds",
                    "block_type": "learning_goal",
                    "component_type": "learning_goal",
                    "content": {
                        "text": "In this module, you will explore Graham's Law of Diffusion, discover why lighter gas molecules travel faster than heavier ones, and calculate relative rates of diffusion from molecular masses."
                    }
                },
                {
                    "page_number": 1,
                    "page_title": "The Aroma of Fresh Coffee Across the Room",
                    "block_type": "concept_explanation",
                    "component_type": "concept_explanation",
                    "content": {
                        "text": "When a barista in a cafe on **Kenyatta Avenue in Nairobi** grinds fresh roasted coffee beans, the rich aroma reaches customers seated at the far end of the room within seconds.\n\nYet no one physically carries the scent across the cafe. The volatile aroma molecules spontaneously spread through the air from an area of high concentration to an area of low concentration.\n\nThis spontaneous spreading of particles is called **Diffusion**. But why do some gas aromas travel noticeably faster than others? Today we explore **Graham's Law of Diffusion**."
                    }
                },
                {
                    "page_number": 2,
                    "page_title": "Graham's Law Statement & Mathematical Formula",
                    "block_type": "concept_explanation",
                    "component_type": "concept_explanation",
                    "content": {
                        "text": "### Graham's Law Statement:\n**Under identical conditions of temperature and pressure, the rate of diffusion ($R$) of a gas is inversely proportional to the square root of its density ($\\rho$) or relative molecular mass ($M_r$).**\n\n### Mathematical Formulation:\n$$R \\propto \\frac{1}{\\sqrt{\\rho}} \\quad \\text{and} \\quad R \\propto \\frac{1}{\\sqrt{M_r}}$$\n\nFor two gases ($A$ and $B$) diffusing under identical conditions:\n$$\\frac{R_A}{R_B} = \\sqrt{\\frac{\\rho_B}{\\rho_A}} = \\sqrt{\\frac{M_B}{M_A}}$$\n\n### Time and Rate Inversion:\nSince rate is inversely proportional to time taken ($R = \\frac{V}{t}$ or $R \\propto \\frac{1}{t}$):\n$$\\frac{R_A}{R_B} = \\frac{t_B}{t_A} = \\sqrt{\\frac{M_B}{M_A}}$$\n*Note*: A lighter gas diffuses **faster** ($R_A > R_B$) and therefore takes **less time** ($t_A < t_B$) to travel the same distance."
                    }
                },
                {
                    "page_number": 3,
                    "page_title": "The Ammonia and Hydrogen Chloride Tube Experiment",
                    "block_type": "suggested_diagram",
                    "component_type": "suggested_diagram",
                    "content": {
                        "purpose": "Experimental setup of diffusion tube showing cotton wool soaked in conc. NH3 at one end, and conc. HCl at the other, with white ammonium chloride ring forming closer to the HCl end.",
                        "instruction": "Long glass tube clamped horizontally. Left end has cotton wool soaked in concentrated ammonia (NH3, Mr=17). Right end has cotton wool soaked in concentrated hydrochloric acid (HCl, Mr=36.5). A dense white ring of NH4Cl forms at approximately 2/3 distance from the NH3 end (closer to HCl).",
                        "resolved_image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/e/e4/Diffusion_of_ammonia_and_hydrogen_chloride.jpg/800px-Diffusion_of_ammonia_and_hydrogen_chloride.jpg"
                    },
                    "asset_info": {
                        "title": "Classic NH3 and HCl Diffusion Experiment",
                        "description": "Demonstration of Graham's Law showing the formation of a white NH4Cl ring closer to the heavier HCl source.",
                        "url": "https://upload.wikimedia.org/wikipedia/commons/thumb/e/e4/Diffusion_of_ammonia_and_hydrogen_chloride.jpg/800px-Diffusion_of_ammonia_and_hydrogen_chloride.jpg"
                    }
                },
                {
                    "page_number": 3,
                    "page_title": "The Classic Diffusion Tube Experiment Explained",
                    "block_type": "concept_explanation",
                    "component_type": "concept_explanation",
                    "content": {
                        "text": "When cotton wool soaked in concentrated ammonia solution ($NH_3$) is placed at one end of a glass tube and cotton wool soaked in concentrated hydrochloric acid ($HCl$) is placed at the other end:\n\n1. **Ammonia Gas ($NH_3$)**: Relative Molecular Mass $M_r = 14 + 3(1) = 17\\text{ g mol}^{-1}$.\n2. **Hydrogen Chloride Gas ($HCl$)**: Relative Molecular Mass $M_r = 1 + 35.5 = 36.5\\text{ g mol}^{-1}$.\n\n### Observation:\nAfter a few minutes, a **dense white ring of solid ammonium chloride ($NH_4Cl$)** forms inside the tube:\n$$\\text{NH}_3(g) + \\text{HCl}(g) \\rightarrow \\text{NH}_4\\text{Cl}(s)$$\n\n### Scientific Explanation:\nBecause ammonia is lighter ($M_r = 17$) than hydrogen chloride ($M_r = 36.5$), its particles travel faster ($\\approx 1.47\\text{ times faster}$). Consequently, the white ring forms **much closer to the $HCl$ end** of the glass tube."
                    }
                },
                {
                    "page_number": 4,
                    "page_title": "Calculating Molecular Mass from Diffusion Time",
                    "block_type": "worked_example",
                    "component_type": "worked_example",
                    "content": {
                        "problem": "$100\\text{ cm}^3$ of sulphur(IV) oxide gas ($SO_2$) diffuses through a porous plug in $40\\text{ seconds}$. Under the same conditions, $100\\text{ cm}^3$ of an unknown gas $X$ takes $20\\text{ seconds}$ to diffuse through the same plug. Calculate the Relative Molecular Mass of gas $X$. ($S = 32.0, O = 16.0$)",
                        "steps": [
                            "**Calculate Molecular Mass of $SO_2$**:\n$$M_r(\\text{SO}_2) = 32.0 + 2(16.0) = 64.0\\text{ g mol}^{-1}$$",
                            "**Identify Given Times**:\n- Time for $\\text{SO}_2$: $t_{\\text{SO}_2} = 40\\text{ s}$\n- Time for gas $X$: $t_X = 20\\text{ s}$",
                            "**State Graham's Law in terms of Time**:\n$$\\frac{t_X}{t_{\\text{SO}_2}} = \\sqrt{\\frac{M_X}{M_{\\text{SO}_2}}}$$",
                            "**Substitute Values**:\n$$\\frac{20}{40} = \\sqrt{\\frac{M_X}{64.0}} \\implies 0.5 = \\sqrt{\\frac{M_X}{64.0}}$$",
                            "**Square Both Sides and Solve**:\n$$(0.5)^2 = \\frac{M_X}{64.0} \\implies 0.25 = \\frac{M_X}{64.0}$$\n$$M_X = 0.25 \\times 64.0 = 16.0\\text{ g mol}^{-1}$$",
                            "**Scientific Conclusion**: The relative molecular mass of unknown gas $X$ is $16.0$ (gas $X$ could be methane, $CH_4$)."
                        ]
                    }
                },
                {
                    "page_number": 5,
                    "page_title": "Comparing Diffusion Rates of Ammonia and HCl",
                    "block_type": "worked_example",
                    "component_type": "worked_example",
                    "content": {
                        "problem": "Calculate the relative rate of diffusion of ammonia ($NH_3$) compared to hydrogen chloride ($HCl$). ($N = 14.0, H = 1.0, Cl = 35.5$)",
                        "steps": [
                            "**Determine Molecular Masses**:\n- $M(\\text{NH}_3) = 14.0 + 3(1.0) = 17.0\\text{ g mol}^{-1}$\n- $M(\\text{HCl}) = 1.0 + 35.5 = 36.5\\text{ g mol}^{-1}$",
                            "**Apply Graham's Law Ratio**:\n$$\\frac{R_{\\text{NH}_3}}{R_{\\text{HCl}}} = \\sqrt{\\frac{M_{\\text{HCl}}}{M_{\\text{NH}_3}}} = \\sqrt{\\frac{36.5}{17.0}}$$",
                            "**Calculate Ratio**:\n$$\\frac{R_{\\text{NH}_3}}{R_{\\text{HCl}}} = \\sqrt{2.147} \\approx 1.465$$",
                            "**Scientific Interpretation**: Ammonia gas diffuses approximately **$1.47\\text{ times faster}$** than hydrogen chloride gas under identical conditions."
                        ]
                    }
                },
                {
                    "page_number": 6,
                    "page_title": "Think About This: Misconceptions on Gas Diffusion",
                    "block_type": "common_misconception",
                    "component_type": "common_misconception",
                    "content": {
                        "text": "### Does a gas with twice the mass take twice as long to diffuse?\nNo! Diffusion rates depend on the **square root** of the molecular mass ($\\sqrt{M_r}$), not a direct linear ratio. If gas $A$ has 4 times the mass of gas $B$, it diffuses $\\sqrt{4} = 2\\text{ times slower}$ (taking twice as long), not 4 times slower!"
                    }
                },
                {
                    "page_number": 7,
                    "page_title": "Practice Question: Diffusion Rates",
                    "block_type": "knowledge_check",
                    "component_type": "knowledge_check",
                    "content": {
                        "check_type": "multiple_choice",
                        "question": "Which of the following gases will diffuse the fastest through a porous membrane under identical conditions of temperature and pressure? ($H=1, C=12, N=14, O=16, S=32$)",
                        "options": [
                            "Carbon(IV) oxide ($CO_2$, $M_r = 44$)",
                            "Oxygen gas ($O_2$, $M_r = 32$)",
                            "Methane gas ($CH_4$, $M_r = 16$)",
                            "Sulphur(IV) oxide ($SO_2$, $M_r = 64$)"
                        ],
                        "answer": "C",
                        "explanation": "According to Graham's Law ($R \\propto \\frac{1}{\\sqrt{M_r}}$), the gas with the lowest relative molecular mass diffuses fastest. Methane ($CH_4$, $M_r = 16$) is the lightest of the four gases."
                    }
                },
                {
                    "page_number": 7,
                    "page_title": "Practice Question: Diffusion Tube Geometry",
                    "block_type": "knowledge_check",
                    "component_type": "knowledge_check",
                    "content": {
                        "check_type": "multiple_choice",
                        "question": "In the reaction between $NH_3(g)$ and $HCl(g)$ in a glass tube, why does the white ammonium chloride ring form closer to the $HCl$ end?",
                        "options": [
                            "Ammonia particles are heavier and move slower",
                            "Hydrogen chloride particles are heavier ($M_r = 36.5$) and move slower than lighter ammonia particles ($M_r = 17$)",
                            "Ammonia gas is acidic and attracts HCl",
                            "Hydrochloric acid is more concentrated than ammonia"
                        ],
                        "answer": "B",
                        "explanation": "Hydrogen chloride has a higher molecular mass ($36.5\\text{ g/mol}$) than ammonia ($17\\text{ g/mol}$). Lighter ammonia molecules diffuse faster and cover a greater distance in the same time, so they meet the slower HCl molecules closer to the HCl end."
                    }
                },
                {
                    "page_number": 8,
                    "page_title": "Key Takeaways: Graham's Law",
                    "block_type": "summary",
                    "component_type": "summary",
                    "content": {
                        "text": "### Core Principles: Graham's Law\n- **Statement**: Rate of diffusion is inversely proportional to square root of density or molecular mass ($R \\propto \\frac{1}{\\sqrt{M_r}}$).\n- **Rate Equation**: $\\frac{R_A}{R_B} = \\sqrt{\\frac{M_B}{M_A}}$.\n- **Time Equation**: $\\frac{t_A}{t_B} = \\sqrt{\\frac{M_A}{M_B}}$ (lighter gas takes less time).\n- **Experimental Proof**: White $NH_4Cl$ ring in $NH_3-HCl$ tube forms closer to the heavier $HCl$ end."
                    }
                }
            ]
        }
    ]

    # 3. Execute Ingestion & Publishing for Each Module
    for m_data in modules_data:
        unit_name = m_data["unit_name"]
        unit_order = m_data["unit_order"]
        lesson_title = m_data["lesson_title"]
        cards = m_data["cards"]

        print(f"\n--- Ingesting {unit_name} ---")

        # Create or update LearningUnit
        unit, unit_created = LearningUnit.objects.get_or_create(
            topic=topic,
            name=unit_name,
            defaults={"order": unit_order, "description": f"Curriculum module for {lesson_title}"}
        )
        if not unit_created:
            unit.order = unit_order
            unit.save()
        print(f"  Learning Unit: {unit.name} (ID: {unit.id})")

        # Create or retrieve Lesson
        lesson, lesson_created = Lesson.objects.get_or_create(
            topic=topic,
            learning_unit=unit,
            defaults={
                "title": lesson_title,
                "status": "published",
                "version": 1
            }
        )
        lesson.title = lesson_title
        lesson.status = "published"
        lesson.save()
        print(f"  Lesson: {lesson.title} (ID: {lesson.id}, Status: {lesson.status})")

        # Clean existing blocks and assets for this lesson to prevent duplicates
        LessonBlock.objects.filter(lesson=lesson).delete()
        LessonAsset.objects.filter(lesson=lesson).delete()

        # Ingest each block
        for order, card in enumerate(cards, start=1):
            block_id = f"f3_chem_t1_l{lesson.id}_b{order}_{uuid.uuid4().hex[:6]}"
            block = LessonBlock.objects.create(
                lesson=lesson,
                block_id=block_id,
                order=order,
                page_number=card["page_number"],
                page_title=card["page_title"],
                block_type=card["block_type"],
                component_type=card["component_type"],
                component_order=order,
                title=card["page_title"],
                content=card["content"]
            )

            # Ingest attached LessonAsset if specified
            if "asset_info" in card:
                info = card["asset_info"]
                asset = LessonAsset.objects.create(
                    lesson=lesson,
                    title=info["title"],
                    description=info["description"],
                    asset_type="image",
                    source_type="external",
                    storage_type="url",
                    url=info.get("url", ""),
                    status="attached"
                )
                asset.blocks.add(block)

        print(f"  Successfully created {len(cards)} structured LessonBlocks across 8 natural concept pages.")

    print("\n================================================================================")
    print("Ingestion Completed Successfully! All 5 Modules Published to Form 3 Topic 1.")
    print("================================================================================")

if __name__ == "__main__":
    ingest_form3_gas_laws()
