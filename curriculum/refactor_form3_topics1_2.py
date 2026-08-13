import os
import sys
import django
import uuid

# Setup Django environment
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "Nexus_backend.settings")
django.setup()

from curriculum.models import Topic, Lesson, LessonBlock, LessonAsset

def run_refactor():
    print("Executing full pedagogical refactoring for Form 3 Topics 1 & 2 (All 14 Lessons)...")

    topic_22 = Topic.objects.get(id=22)
    topic_23 = Topic.objects.get(id=23)

    lessons_data = {
        # =========================================================================
        # TOPIC 22: GAS LAWS (Lessons 159 - 163)
        # =========================================================================
        159: {
            "topic": topic_22,
            "title": "Introduction to the Gaseous State and Kinetic Theory",
            "cards": [
                {
                    "page_number": 1,
                    "page_title": "The Gaseous State",
                    "block_type": "learning_goal",
                    "component_type": "learning_goal",
                    "content": {
                        "text": "By the end of this module, you will explain the macroscopic properties of gases, understand the five fundamental postulates of the Kinetic Theory of Matter, and explain how microscopic particle collisions generate macroscopic gas pressure ($P = \\frac{\\text{Force}}{\\text{Area}}$)."
                    }
                },
                {
                    "page_number": 1,
                    "page_title": "The Invisible Ocean of Air Around Us",
                    "block_type": "concept_explanation",
                    "component_type": "concept_explanation",
                    "content": {
                        "text": "Every second, we move through an invisible ocean of gas particles. You cannot see the nitrogen and oxygen molecules around you, yet you feel their immense physical presence when a gust of wind pushes against your body or when an inflated football rebounds off your foot.\n\nOf the three common states of matter (solids, liquids, and gases), gases are unique in their ability to expand indefinitely to fill any container, flow effortlessly, and compress into a fraction of their original volume.\n\nTo understand why gases behave this way, we must look beyond what we can see with our eyes and journey into the submicroscopic realm where billions of tiny particles move at incredible speeds!"
                    }
                },
                {
                    "page_number": 2,
                    "page_title": "Macroscopic Properties of the Gaseous State",
                    "block_type": "concept_explanation",
                    "component_type": "concept_explanation",
                    "content": {
                        "text": "Let's connect what we observe in the laboratory (macroscopic) with the particle world (submicroscopic):\n\n* **Indefinite Shape & Volume**: Unlike a solid block of iron with fixed boundaries, a gas has neither a fixed shape nor a fixed volume. It spreads out instantly to occupy the entire volume of whichever container it is placed in.\n* **High Compressibility**: If you trap gas in a syringe, pushing the plunger squeezes the gas into a remarkably smaller space because the particles are separated by vast empty distances.\n* **Low Density**: Gases have exceptionally low densities (about $\\frac{1}{1000}$ the density of liquids or solids) because there are very few particles per unit volume.\n* **Thermal Expansion**: Heating a gas causes it to expand significantly more than solids or liquids because heat energy directly increases the kinetic energy and velocity of the particles."
                    }
                },
                {
                    "page_number": 2,
                    "page_title": "Diagram: States of Matter Molecular Comparison",
                    "block_type": "suggested_diagram",
                    "component_type": "suggested_diagram",
                    "content": {
                        "prompt": "Side-by-side molecular diagrams comparing particle arrangements in Solid (tightly packed regular lattice), Liquid (close random arrangement with sliding particles), and Gas (widely spaced particles with high-speed velocity arrows colliding with container walls).",
                        "caption": "Molecular Comparison: Gas particles are separated by vast empty spaces and move in rapid, random straight-line paths."
                    },
                    "asset_info": {
                        "title": "States of Matter Particle Models",
                        "description": "Particle-level comparison of solids, liquids, and gases highlighting intermolecular spacing and kinetic velocity vectors.",
                        "ai_instruction": "Render three side-by-side particle boxes showing Solid (lattice), Liquid (condensed fluid), and Gas (widely spaced particles with collision vectors)."
                    }
                },
                {
                    "page_number": 3,
                    "page_title": "The Kinetic Theory of Matter (5 Postulates)",
                    "block_type": "concept_explanation",
                    "component_type": "concept_explanation",
                    "content": {
                        "text": "To describe gas behavior quantitatively, scientists developed the **Kinetic Theory of Gases**, built upon five universal principles:\n\n1. **Vast Intermolecular Distances**: Gas particles are so tiny compared to the enormous distances between them that the actual volume of the particles themselves is negligible compared to the total volume of the container.\n2. **Negligible Intermolecular Forces**: Because particles are so far apart, forces of attraction or repulsion between them are negligible under normal conditions.\n3. **Constant, Rapid, Random Motion**: Gas particles travel continuously in straight lines in all directions until they collide with other particles or the container walls.\n4. **Perfecty Elastic Collisions**: Collisions between particles or against container walls are perfectly elastic—no overall kinetic energy is lost ($E_{k,\\text{total}} = \\text{constant}$).\n5. **Origin of Gas Pressure**: Billions of particles strike the inner container walls every microsecond. Gas Pressure ($P$) is the cumulative force exerted by these collisions per unit area:\n   $$P = \\frac{\\text{Force}}{\\text{Area}}$$"
                    }
                },
                {
                    "page_number": 4,
                    "page_title": "Gases in Everyday Kenyan Life",
                    "block_type": "real_world_example",
                    "component_type": "real_world_example",
                    "content": {
                        "text": "### 1. Liquefied Petroleum Gas (LPG Cylinders)\nIn households across Kenya, we use gas cylinders (like K-Gas, Total Gas, or Afrigas). Under intense mechanical pressure, propane and butane particles are compressed so tightly that they condense into liquid. Opening the valve releases the pressure, allowing the liquid to instantly vaporize into fast-moving gas for cooking!\n\n### 2. Agricultural Biogas Digesters\nIn farming communities in **Meru, Eldoret, and Kiambu**, organic cow manure undergoes anaerobic fermentation inside sealed digesters. This generates methane gas ($\\text{CH}_4$), which exerts outward pressure against floating digester covers, storing clean renewable fuel for lighting and cooking."
                    }
                },
                {
                    "page_number": 5,
                    "page_title": "Worked Example: Explaining Tyre Pressure",
                    "block_type": "worked_example",
                    "component_type": "worked_example",
                    "content": {
                        "problem": "Using the Kinetic Theory of Matter, explain step-by-step why pumping additional air into a fixed-volume bicycle or car tyre causes the measured internal pressure to rise.",
                        "steps": [
                            "**1. What do we know? (Given Conditions)**\n- Tyre volume ($V$) is fixed and constant.\n- Temperature ($T$) is constant.\n- Additional air is injected, meaning the total number of gas particles ($N$) inside the tyre increases.",
                            "**2. What are we finding? (Target Question)**\n- The physical particle-level mechanism that causes the measured pressure ($P$) to increase.",
                            "**3. Governing Formula & Principle**\n$$\\text{Pressure } (P) = \\frac{\\text{Cumulative Collision Force } (F)}{\\text{Surface Area } (A)}$$\n- Pressure is directly caused by gas particles colliding against the inner tyre walls.",
                            "**4. Step-by-Step Particle Reasoning**\n- Pumping in more air packs significantly more gas molecules into the exact same enclosed volume ($V$).\n- With more particles crowded together, the distance a particle travels before striking a wall becomes much shorter.\n- As a result, the **collision frequency** (the number of particle impacts against the inner wall per square centimeter per second) increases substantially.",
                            "**5. Meaning of the Result & Conclusion**\n- A higher rate of wall collisions delivers a greater total outward force against the rubber walls.\n- Therefore, the measured pressure ($P = F/A$) inside the tyre rises proportionally."
                        ]
                    }
                },
                {
                    "page_number": 6,
                    "page_title": "Think About This: Common Questions on Gases",
                    "block_type": "common_misconception",
                    "component_type": "common_misconception",
                    "content": {
                        "text": "### Question: Is the space between gas particles filled with air?\n**Clarification**: Air is itself a mixture of gas particles (mostly $\\text{N}_2$ and $\\text{O}_2$). The space between these individual particles contains nothing at all—it is a **complete physical vacuum**!\n\n### Question: Do cold gas particles weigh more than hot gas particles?\n**Clarification**: The mass of an individual atom or molecule remains perfectly constant regardless of temperature. Cooling a gas only reduces the average velocity and kinetic energy of the particles, causing them to move more slowly, without altering their actual atomic mass."
                    }
                },
                {
                    "page_number": 7,
                    "page_title": "Practice Question: Gas Density",
                    "block_type": "knowledge_check",
                    "component_type": "knowledge_check",
                    "content": {
                        "check_type": "multiple_choice",
                        "question": "Which of the following statements best explains why gases have a much lower density than solids under standard room conditions?",
                        "options": [
                            "Gas particles are individually much lighter than solid atoms.",
                            "Gas particles experience negligible intermolecular attraction and are separated by vast empty distances, so there is very little mass per unit volume.",
                            "Gas particles are in constant, random straight-line motion.",
                            "Gas particles undergo perfectly elastic collisions with container walls."
                        ],
                        "answer": "B",
                        "explanation": "Density is mass divided by volume ($\\rho = \\frac{m}{V}$). Because gas particles have negligible attractive forces, they spread out to occupy the entire volume, leaving enormous empty spaces between particles. Hence, the mass of gas in a given volume is very small compared to tightly packed solids."
                    }
                },
                {
                    "page_number": 8,
                    "page_title": "Key Takeaways: The Gaseous State",
                    "block_type": "summary",
                    "component_type": "summary",
                    "content": {
                        "text": "### Summary: Introduction to Gases & Kinetic Theory\n- **Gaseous State**: Indefinite shape, indefinite volume, highly compressible, low density.\n- **Absolute Temperature & Kinetic Energy**: Temperature in Kelvin is directly proportional to average kinetic energy ($E_k \\propto T$).\n- **Kinetic Theory Postulates**: Negligible particle volume, negligible intermolecular forces, perpetual random straight-line motion, perfectly elastic collisions.\n- **Origin of Pressure**: Cumulative bombardment of gas molecules on container walls ($P = \\frac{F}{A}$)."
                    }
                }
            ]
        },

        160: {
            "topic": topic_22,
            "title": "Boyle's Law (Pressure-Volume Relationship)",
            "cards": [
                {
                    "page_number": 1,
                    "page_title": "Pressure and Volume",
                    "block_type": "learning_goal",
                    "component_type": "learning_goal",
                    "content": {
                        "text": "By the end of this module, you will state Boyle's Law, explain the inverse pressure-volume relationship using kinetic theory, interpret hyperbolic ($P$ vs $V$) and linear ($P$ vs $1/V$) graphs, and solve quantitative gas problems with full step-by-step reasoning."
                    }
                },
                {
                    "page_number": 1,
                    "page_title": "The Trapped Air in a Syringe",
                    "block_type": "concept_explanation",
                    "component_type": "concept_explanation",
                    "content": {
                        "text": "Imagine holding a plastic syringe and pulling the plunger back to draw in air. Now, press your thumb firmly against the tip so no air can escape. What happens when you push the plunger inward?\n\nAt first, it moves easily. But as you squeeze the air into a smaller volume, it becomes increasingly difficult to push. The trapped air pushes back against your thumb with an invisible, powerful force! If you release the plunger, it springs right back.\n\nWhy does trapped air resist compression? Today we investigate **Boyle's Law**, which describes the exact mathematical relationship between the pressure and volume of a gas at constant temperature."
                    }
                },
                {
                    "page_number": 2,
                    "page_title": "How Particle Collisions Create Boyle's Law",
                    "block_type": "concept_explanation",
                    "component_type": "concept_explanation",
                    "content": {
                        "text": "Let's examine what happens when gas volume is changed at constant temperature:\n\n* **Macroscopic Observation**:\n  Compressing trapped air into half its original volume ($V \\rightarrow \\frac{1}{2}V$) causes the measured pressure to double ($P \\rightarrow 2P$).\n\n* **Microscopic Particle Model**:\n  When volume is halved, the exact same number of gas particles are crowded into half the physical space. Because the container walls are closer together, particles travel shorter distances between wall impacts. Consequently, the frequency of wall collisions doubles (twice as many impacts per unit area per second). Since pressure is collision force per area, doubling collision frequency **doubles the pressure**!\n\n* **Symbolic Representation**:\n  $$P \\propto \\frac{1}{V} \\quad (\\text{at constant } T)$$\n  $$P \\times V = k \\quad \\implies \\quad P_1V_1 = P_2V_2$$"
                    }
                },
                {
                    "page_number": 2,
                    "page_title": "Diagram: Boyle's Law Apparatus & Graphical Curves",
                    "block_type": "suggested_diagram",
                    "component_type": "suggested_diagram",
                    "content": {
                        "prompt": "Diagram showing Boyle's Law apparatus with trapped air column and pressure gauge, alongside two graphs: Graph A (hyperbolic curve of P vs V) and Graph B (straight line through origin of P vs 1/V).",
                        "caption": "Boyle's Law Relationships: P is inversely proportional to V (hyperbola), yielding a straight line when plotted against 1/V."
                    },
                    "asset_info": {
                        "title": "Boyle's Law Graphical Analysis",
                        "description": "Apparatus diagram and comparative graphs showing P vs V hyperbola and P vs 1/V linear plot.",
                        "ai_instruction": "Create a diagram showing Boyle's Law apparatus with pressure gauge, alongside P vs V hyperbolic curve and P vs 1/V straight line."
                    }
                },
                {
                    "page_number": 3,
                    "page_title": "Boyle's Law & Units of Pressure",
                    "block_type": "definition_card",
                    "component_type": "definition_card",
                    "content": {
                        "term": "Boyle's Law",
                        "content": "### Definition\n*The volume of a fixed mass of gas is inversely proportional to its pressure, provided the temperature remains constant.*\n\n### Mathematical Formulation:\n$$P_1V_1 = P_2V_2 \\quad (\\text{at constant } T)$$\n\n### Units & Conversion Standards:\n- **Pressure ($P$)**: $1\\text{ atm} = 760\\text{ mmHg} = 101325\\text{ Pa} = 101.325\\text{ kPa} = 1.013 \\times 10^5\\text{ N/m}^2$\n- **Volume ($V$)**: $1\\text{ dm}^3 = 1000\\text{ cm}^3 = 1\\text{ Litre} = 1000\\text{ mL}$"
                    }
                },
                {
                    "page_number": 4,
                    "page_title": "Worked Example 1: Gas Volume Under Changing Pressure",
                    "block_type": "worked_example",
                    "component_type": "worked_example",
                    "content": {
                        "problem": "A mass of gas occupies a volume of $500\\text{ cm}^3$ at a pressure of $760\\text{ mmHg}$. If the pressure is doubled to $1520\\text{ mmHg}$ while temperature remains constant, calculate the new volume of the gas.",
                        "steps": [
                            "**1. What do we know? (Given Data)**\n- Initial volume $V_1 = 500\\text{ cm}^3$\n- Initial pressure $P_1 = 760\\text{ mmHg}$\n- Final pressure $P_2 = 1520\\text{ mmHg}$\n- Temperature ($T$) is constant.",
                            "**2. What are we finding? (Target Quantity)**\n- Final volume of the gas ($V_2$) in $\\text{cm}^3$.",
                            "**3. Governing Formula & Principle**\n$$P_1V_1 = P_2V_2$$\n- We apply Boyle's Law because temperature remains constant.",
                            "**4. Step-by-Step Calculation**\n- Rearrange the formula to solve for $V_2$:\n$$V_2 = \\frac{P_1 \\times V_1}{P_2}$$\n- Substitute the known values:\n$$V_2 = \\frac{760\\text{ mmHg} \\times 500\\text{ cm}^3}{1520\\text{ mmHg}}$$\n$$V_2 = \\frac{380000}{1520} = 250\\text{ cm}^3$$",
                            "**5. Meaning of the Result & Sanity Check**\n- Because the pressure doubled ($760 \\rightarrow 1520\\text{ mmHg}$), the volume must halve ($500 \\rightarrow 250\\text{ cm}^3$). This confirms the inverse pressure-volume relationship."
                        ]
                    }
                },
                {
                    "page_number": 5,
                    "page_title": "Worked Example 2: Converting Between Pressure Units",
                    "block_type": "worked_example",
                    "component_type": "worked_example",
                    "content": {
                        "problem": "A sample of gas has a volume of $456\\text{ cm}^3$ at a pressure of $750\\text{ mmHg}$. Calculate the volume of this gas if the pressure is changed to $1.0 \\times 10^5\\text{ Pa}$ at constant temperature. (Standard atmospheric pressure: $760\\text{ mmHg} = 1.013 \\times 10^5\\text{ Pa}$).",
                        "steps": [
                            "**1. What do we know? (Given Data)**\n- $V_1 = 456\\text{ cm}^3$\n- $P_1 = 750\\text{ mmHg}$\n- $P_2 = 1.0 \\times 10^5\\text{ Pa}$\n- Conversion standard: $760\\text{ mmHg} = 1.013 \\times 10^5\\text{ Pa}$",
                            "**2. What are we finding?**\n- Final volume $V_2$ in $\\text{cm}^3$.",
                            "**3. Unit Conversion Step**\n- Convert $P_1$ from $\\text{mmHg}$ to $\\text{Pa}$ so that units are identical:\n$$P_1 = \\frac{750}{760} \\times 1.013 \\times 10^5\\text{ Pa} = 99967.1\\text{ Pa}$$",
                            "**4. Step-by-Step Calculation using Boyle's Law**\n$$P_1V_1 = P_2V_2 \\quad \\implies \\quad V_2 = \\frac{P_1 V_1}{P_2}$$\n$$V_2 = \\frac{99967.1\\text{ Pa} \\times 456\\text{ cm}^3}{1.0 \\times 10^5\\text{ Pa}} = \\frac{45585000}{100000} = 455.85\\text{ cm}^3 \\approx 456\\text{ cm}^3$$",
                            "**5. Meaning of the Result**\n- Since $750\\text{ mmHg}$ is almost identical to $1.0 \\times 10^5\\text{ Pa}$ (only a $0.03\\%$ difference), the volume remains virtually unchanged at $456\\text{ cm}^3$."
                        ]
                    }
                },
                {
                    "page_number": 6,
                    "page_title": "Think About This: Why Scuba Divers Never Hold Their Breath",
                    "block_type": "common_misconception",
                    "component_type": "common_misconception",
                    "content": {
                        "text": "### Why must scuba divers NEVER hold their breath while ascending to the surface?\nAt a depth of $20\\text{ metres}$ underwater, the water pressure is $3\\text{ atmospheres}$ ($3\\text{ times}$ surface pressure). A diver's lungs hold air compressed at $3\\text{ atm}$.\n\nIf the diver ascends to the surface ($1\\text{ atm}$) while holding their breath, the ambient pressure drops by a factor of 3. According to Boyle's Law ($P_1V_1 = P_2V_2$), the volume of air trapped inside the lungs will **triple ($3 \\times V$)**, causing the delicate lung tissues to rupture (pulmonary barotrauma)! Divers are trained to exhale continuously during ascent."
                    }
                },
                {
                    "page_number": 7,
                    "page_title": "Practice Question: Interpreting Boyle's Law",
                    "block_type": "knowledge_check",
                    "component_type": "knowledge_check",
                    "content": {
                        "check_type": "multiple_choice",
                        "question": "A syringe contains $60\\text{ cm}^3$ of air at $1.0\\text{ atm}$. The plunger is pushed until the volume is reduced to $20\\text{ cm}^3$ at constant temperature. What is the new pressure inside the syringe?",
                        "options": [
                            "$0.33\\text{ atm}$",
                            "$2.0\\text{ atm}$",
                            "$3.0\\text{ atm}$",
                            "$6.0\\text{ atm}$"
                        ],
                        "answer": "C",
                        "explanation": "Using Boyle's Law: $P_1V_1 = P_2V_2 \\implies P_2 = \\frac{P_1V_1}{V_2} = \\frac{1.0\\text{ atm} \\times 60\\text{ cm}^3}{20\\text{ cm}^3} = 3.0\\text{ atm}$. Reducing the volume to one-third triples the pressure."
                    }
                },
                {
                    "page_number": 8,
                    "page_title": "Key Takeaways: Boyle's Law",
                    "block_type": "summary",
                    "component_type": "summary",
                    "content": {
                        "text": "### Summary: Boyle's Law\n- **Statement**: Volume is inversely proportional to pressure at constant temperature ($P \\propto \\frac{1}{V}$).\n- **Equation**: $P_1V_1 = P_2V_2 = k$.\n- **Graphs**: $P$ vs $V$ gives a rectangular hyperbola; $P$ vs $\\frac{1}{V}$ gives a straight line passing through the origin.\n- **Molecular Basis**: Reducing volume crowds particles, doubling wall collision frequency per unit area, thereby doubling pressure."
                    }
                }
            ]
        },

        161: {
            "topic": topic_22,
            "title": "Charles's Law (Temperature-Volume Relationship)",
            "cards": [
                {
                    "page_number": 1,
                    "page_title": "Temperature and Volume",
                    "block_type": "learning_goal",
                    "component_type": "learning_goal",
                    "content": {
                        "text": "By the end of this module, you will state Charles's Law, explain the concept of Absolute Zero ($-273^\\circ\\text{C} = 0\\text{ K}$), convert between Celsius and Kelvin temperature scales, and solve quantitative Charles's Law problems."
                    }
                },
                {
                    "page_number": 1,
                    "page_title": "The Balloon Left in the Midday Sun",
                    "block_type": "concept_explanation",
                    "component_type": "concept_explanation",
                    "content": {
                        "text": "Have you ever inflated an ordinary party balloon inside a cool room in the morning and then left it sitting on sunlit grass at midday? Within an hour, you will notice the balloon has expanded significantly, or may even pop with a loud bang!\n\nConversely, if you place a slightly inflated balloon inside a refrigerator, it visibly shrinks and wrinkles. Why do gases expand when warmed and shrink when cooled? Today we explore **Charles's Law**, which governs the direct relationship between gas volume and temperature."
                    }
                },
                {
                    "page_number": 2,
                    "page_title": "Absolute Zero & The Kelvin Temperature Scale",
                    "block_type": "concept_explanation",
                    "component_type": "concept_explanation",
                    "content": {
                        "text": "When scientists plot gas volume against temperature in degrees Celsius ($^\\circ\\text{C}$), the straight-line graph intercepts the temperature axis at exactly **$-273.15^\\circ\\text{C}$** when extrapolated to zero volume.\n\n* **What is Absolute Zero ($0\\text{ K}$)?**\n  At $-273^\\circ\\text{C}$, the kinetic energy of all gas particles theoretically drops to zero. All molecular motion ceases completely! Because it is impossible to have less than zero kinetic energy, $-273^\\circ\\text{C}$ represents the lowest possible temperature in the universe.\n\n* **The Kelvin Temperature Scale ($T$)**:\n  To ensure that temperature is directly proportional to kinetic energy ($E_k \\propto T$), chemists use the **Kelvin scale (Absolute scale)**:\n  $$T\\text{ (in Kelvin)} = t\\text{ (in }^\\circ\\text{C)} + 273$$\n\n*Golden Rule of Gas Laws*: In all gas law calculations, **temperatures MUST ALWAYS be converted to Kelvin** before substitution!"
                    }
                },
                {
                    "page_number": 2,
                    "page_title": "Diagram: Charles's Law Graphical Extrapolation",
                    "block_type": "suggested_diagram",
                    "component_type": "suggested_diagram",
                    "content": {
                        "prompt": "Graph showing Volume vs Temperature in Celsius with multiple straight lines extrapolating back to zero volume at exactly -273 degrees Celsius (Absolute Zero).",
                        "caption": "Charles's Law Extrapolation: Volume-temperature lines for all gases converge to zero volume at -273°C (0 Kelvin)."
                    },
                    "asset_info": {
                        "title": "Charles's Law Absolute Zero Plot",
                        "description": "Graphical plot of volume versus Celsius temperature demonstrating extrapolation to Absolute Zero (-273°C).",
                        "ai_instruction": "Create a graph of Volume (y-axis) vs Temperature in Celsius (x-axis), with experimental lines extrapolating backwards to intercept the axis at -273°C."
                    }
                },
                {
                    "page_number": 3,
                    "page_title": "Charles's Law Formulation",
                    "block_type": "definition_card",
                    "component_type": "definition_card",
                    "content": {
                        "term": "Charles's Law",
                        "content": "### Definition\n*The volume of a fixed mass of gas is directly proportional to its absolute temperature (in Kelvin), provided the pressure remains constant.*\n\n### Mathematical Formulation:\n$$V \\propto T \\quad (\\text{at constant } P)$$\n$$\\frac{V}{T} = k \\quad \\implies \\quad \\frac{V_1}{T_1} = \\frac{V_2}{T_2}$$\nWhere $T_1$ and $T_2$ are absolute temperatures in **Kelvin** ($T = t^\\circ\\text{C} + 273$)."
                    }
                },
                {
                    "page_number": 4,
                    "page_title": "Worked Example 1: Volume Change with Temperature",
                    "block_type": "worked_example",
                    "component_type": "worked_example",
                    "content": {
                        "problem": "A gas occupies a volume of $450\\text{ cm}^3$ at a temperature of $27^\\circ\\text{C}$. Calculate its volume if the temperature is raised to $177^\\circ\\text{C}$ while the pressure is kept constant.",
                        "steps": [
                            "**1. What do we know? (Given Data)**\n- Initial volume $V_1 = 450\\text{ cm}^3$\n- Initial temperature $t_1 = 27^\\circ\\text{C}$\n- Final temperature $t_2 = 177^\\circ\\text{C}$\n- Pressure is constant.",
                            "**2. What are we finding?**\n- Final volume $V_2$ in $\\text{cm}^3$.",
                            "**3. Convert Temperatures to Absolute Scale (Kelvin)**:\n$$T_1 = 27 + 273 = 300\\text{ K}$$\n$$T_2 = 177 + 273 = 450\\text{ K}$$",
                            "**4. Step-by-Step Calculation using Charles's Law**:\n$$\\frac{V_1}{T_1} = \\frac{V_2}{T_2} \\quad \\implies \\quad V_2 = \\frac{V_1 \\times T_2}{T_1}$$\n$$V_2 = \\frac{450\\text{ cm}^3 \\times 450\\text{ K}}{300\\text{ K}}$$\n$$V_2 = \\frac{202500}{300} = 675\\text{ cm}^3$$",
                            "**5. Meaning of the Result & Sanity Check**\n- Temperature increased from $300\\text{ K}$ to $450\\text{ K}$ (a factor of $1.5$). The volume expanded proportionally from $450\\text{ cm}^3$ to $675\\text{ cm}^3$ ($450 \\times 1.5$)."
                        ]
                    }
                },
                {
                    "page_number": 5,
                    "page_title": "Worked Example 2: Determining Final Temperature in Celsius",
                    "block_type": "worked_example",
                    "component_type": "worked_example",
                    "content": {
                        "problem": "A fixed mass of gas occupies $750\\text{ cm}^3$ at $57^\\circ\\text{C}$. At what Celsius temperature will the volume reduce to $100\\text{ cm}^3$ if pressure remains constant?",
                        "steps": [
                            "**1. What do we know? (Given Data)**\n- $V_1 = 750\\text{ cm}^3$\n- $t_1 = 57^\\circ\\text{C} \\implies T_1 = 57 + 273 = 330\\text{ K}$\n- $V_2 = 100\\text{ cm}^3$",
                            "**2. What are we finding?**\n- Final temperature in degrees Celsius ($t_2$).",
                            "**3. Calculation in Kelvin using Charles's Law**:\n$$\\frac{V_1}{T_1} = \\frac{V_2}{T_2} \\quad \\implies \\quad T_2 = \\frac{V_2 \\times T_1}{V_1}$$\n$$T_2 = \\frac{100\\text{ cm}^3 \\times 330\\text{ K}}{750\\text{ cm}^3} = \\frac{33000}{750} = 44\\text{ K}$$",
                            "**4. Convert Final Temperature back to Celsius**:\n$$t_2 = T_2 - 273 = 44 - 273 = -229^\\circ\\text{C}$$",
                            "**5. Meaning of the Result**\n- To shrink the volume dramatically from $750\\text{ cm}^3$ down to $100\\text{ cm}^3$, the gas must be cooled to an extreme cryogenic temperature of $-229^\\circ\\text{C}$."
                        ]
                    }
                },
                {
                    "page_number": 6,
                    "page_title": "Think About This: Why Celsius Cannot Be Substituted Directly",
                    "block_type": "common_misconception",
                    "component_type": "common_misconception",
                    "content": {
                        "text": "### Why does substituting $0^\\circ\\text{C}$ into Charles's Law produce a mathematical error?\nIf you tried to calculate with Celsius at freezing point ($t = 0^\\circ\\text{C}$):\n$$\\frac{V}{0} = \\text{Undefined!}$$\nFurthermore, at $-10^\\circ\\text{C}$, the formula would predict a negative volume, which is physically impossible!\n\nThe Kelvin scale solves this because temperature starts at absolute zero ($0\\text{ K}$), where kinetic energy is zero, ensuring all temperatures are positive and proportional to particle energy."
                    }
                },
                {
                    "page_number": 7,
                    "page_title": "Practice Question: Temperature Conversion & Charles's Law",
                    "block_type": "knowledge_check",
                    "component_type": "knowledge_check",
                    "content": {
                        "check_type": "multiple_choice",
                        "question": "A balloon with a volume of $2.0\\text{ dm}^3$ at $20^\\circ\\text{C}$ is heated to $40^\\circ\\text{C}$ at constant pressure. What is the new volume of the balloon?",
                        "options": [
                            "$4.0\\text{ dm}^3$",
                            "$2.14\\text{ dm}^3$",
                            "$1.0\\text{ dm}^3$",
                            "$2.50\\text{ dm}^3$"
                        ],
                        "answer": "B",
                        "explanation": "Remember to convert to Kelvin: $T_1 = 20 + 273 = 293\\text{ K}$ and $T_2 = 40 + 273 = 313\\text{ K}$. Applying Charles's Law: $V_2 = V_1 \\times \\frac{T_2}{T_1} = 2.0\\text{ dm}^3 \\times \\frac{313\\text{ K}}{293\\text{ K}} = 2.1365\\text{ dm}^3 \\approx 2.14\\text{ dm}^3$."
                    }
                },
                {
                    "page_number": 8,
                    "page_title": "Key Takeaways: Charles's Law",
                    "block_type": "summary",
                    "component_type": "summary",
                    "content": {
                        "text": "### Summary: Charles's Law\n- **Statement**: Volume is directly proportional to absolute temperature at constant pressure ($V \\propto T$).\n- **Equation**: $\\frac{V_1}{T_1} = \\frac{V_2}{T_2}$.\n- **Absolute Zero**: $-273^\\circ\\text{C} = 0\\text{ K}$ (theoretical point of zero kinetic energy and zero volume).\n- **Kelvin Conversion**: Always use $T\\text{ (K)} = t\\text{ (}^\\circ\\text{C)} + 273$."
                    }
                }
            ]
        },

        162: {
            "topic": topic_22,
            "title": "The Combined Gas Law and Standard Conditions (S.T.P. & R.T.P.)",
            "cards": [
                {
                    "page_number": 1,
                    "page_title": "The Master Gas Law",
                    "block_type": "learning_goal",
                    "component_type": "learning_goal",
                    "content": {
                        "text": "By the end of this module, you will derive and apply the Combined Gas Law equation ($\\frac{P_1V_1}{T_1} = \\frac{P_2V_2}{T_2}$), state standard conditions (s.t.p. and r.t.p.), and solve simultaneous multi-variable gas problems."
                    }
                },
                {
                    "page_number": 1,
                    "page_title": "When Both Pressure and Temperature Change",
                    "block_type": "concept_explanation",
                    "component_type": "concept_explanation",
                    "content": {
                        "text": "In real-world chemistry and meteorology, pressure and temperature rarely change in isolation. Consider a weather balloon launched in Nairobi:\n* As the balloon ascends to high altitudes in the atmosphere, the external pressure **decreases** (which makes the balloon expand, per Boyle's Law).\n* At the same time, the surrounding atmospheric temperature **drops** drastically below freezing (which makes the balloon shrink, per Charles's Law)!\n\nWhich effect wins? To calculate the final volume accurately, we combine Boyle's Law and Charles's Law into a single unified equation: **The Combined Gas Law**."
                    }
                },
                {
                    "page_number": 2,
                    "page_title": "Deriving the Combined Gas Law",
                    "block_type": "concept_explanation",
                    "component_type": "concept_explanation",
                    "content": {
                        "text": "Let's combine our two fundamental gas relationships:\n1. From Boyle's Law: $V \\propto \\frac{1}{P} \\quad (\\text{at constant } T)$\n2. From Charles's Law: $V \\propto T \\quad (\\text{at constant } P)$\n\nCombining both proportionalities yields:\n$$V \\propto \\frac{T}{P} \\quad \\implies \\quad \\frac{PV}{T} = \\text{constant} \\ (k)$$\n\nFor a fixed mass of gas changing from initial state $(P_1, V_1, T_1)$ to final state $(P_2, V_2, T_2)$:\n$$\\mathbf{\\frac{P_1 V_1}{T_1} = \\frac{P_2 V_2}{T_2}}$$\n*Note*: If temperature is held constant ($T_1 = T_2$), the equation simplifies to Boyle's Law ($P_1V_1 = P_2V_2$). If pressure is held constant ($P_1 = P_2$), it simplifies to Charles's Law ($\\frac{V_1}{T_1} = \\frac{V_2}{T_2}$)."
                    }
                },
                {
                    "page_number": 2,
                    "page_title": "Diagram: Standard Gas Reference Conditions",
                    "block_type": "suggested_diagram",
                    "component_type": "suggested_diagram",
                    "content": {
                        "prompt": "Infographic comparing Standard Temperature and Pressure (s.t.p.: 0°C/273K, 760 mmHg, molar volume 22.4 dm3) versus Room Temperature and Pressure (r.t.p.: 25°C/298K, 760 mmHg, molar volume 24.0 dm3).",
                        "caption": "Standard Reference Conditions: s.t.p. (273 K, 1 atm) and r.t.p. (298 K, 1 atm) provide universal benchmarks for comparing gas volumes."
                    },
                    "asset_info": {
                        "title": "Standard Gas Conditions Reference Chart",
                        "description": "Comparative matrix contrasting temperature, pressure, and molar volume at s.t.p. and r.t.p.",
                        "ai_instruction": "Create a 2-panel reference card comparing s.t.p. (273K, 1atm, 22.4L) on the left and r.t.p. (298K, 1atm, 24.0L) on the right."
                    }
                },
                {
                    "page_number": 3,
                    "page_title": "Standard Laboratory Conditions (S.T.P. & R.T.P.)",
                    "block_type": "definition_card",
                    "component_type": "definition_card",
                    "content": {
                        "term": "Standard Gas Conditions",
                        "content": "### 1. Standard Temperature and Pressure (s.t.p.)\n- **Standard Temperature**: $0^\\circ\\text{C} = 273\\text{ K}$\n- **Standard Pressure**: $1\\text{ atm} = 760\\text{ mmHg} = 101325\\text{ Pa} = 1.013 \\times 10^5\\text{ N/m}^2$\n\n### 2. Room Temperature and Pressure (r.t.p.)\n- **Room Temperature**: $25^\\circ\\text{C} = 298\\text{ K}$\n- **Room Pressure**: $1\\text{ atm} = 760\\text{ mmHg} = 101325\\text{ Pa} = 1.013 \\times 10^5\\text{ N/m}^2$"
                    }
                },
                {
                    "page_number": 4,
                    "page_title": "Worked Example 1: Calculating Gas Volume at S.T.P.",
                    "block_type": "worked_example",
                    "component_type": "worked_example",
                    "content": {
                        "problem": "A gas occupies $30.0\\text{ cm}^3$ at $27^\\circ\\text{C}$ and $740\\text{ mmHg}$ pressure. Calculate the volume this gas would occupy at standard temperature and pressure (s.t.p.).",
                        "steps": [
                            "**1. What do we know? (Initial State Data)**\n- $P_1 = 740\\text{ mmHg}$\n- $V_1 = 30.0\\text{ cm}^3$\n- $T_1 = 27 + 273 = 300\\text{ K}$",
                            "**2. Conditions at s.t.p. (Final State Data)**\n- $P_2 = 760\\text{ mmHg}$\n- $T_2 = 273\\text{ K}$\n- $V_2 = \\text{Target Quantity}$",
                            "**3. Governing Formula**\n$$\\frac{P_1 V_1}{T_1} = \\frac{P_2 V_2}{T_2} \\quad \\implies \\quad V_2 = \\frac{P_1 V_1 T_2}{P_2 T_1}$$",
                            "**4. Step-by-Step Calculation**\n$$V_2 = \\frac{740\\text{ mmHg} \\times 30.0\\text{ cm}^3 \\times 273\\text{ K}}{760\\text{ mmHg} \\times 300\\text{ K}}$$\n$$V_2 = \\frac{6060600}{228000} = 26.58\\text{ cm}^3$$",
                            "**5. Meaning of the Result & Sanity Check**\n- At s.t.p., the pressure increased slightly ($740 \\rightarrow 760\\text{ mmHg}$) and temperature cooled ($300 \\rightarrow 273\\text{ K}$). Both factors work together to compress the gas, reducing volume from $30.0\\text{ cm}^3$ to $26.58\\text{ cm}^3$."
                        ]
                    }
                },
                {
                    "page_number": 5,
                    "page_title": "Worked Example 2: Determining Final Temperature Under Dual Changes",
                    "block_type": "worked_example",
                    "component_type": "worked_example",
                    "content": {
                        "problem": "A gas occupies $100\\text{ cm}^3$ at $-15^\\circ\\text{C}$ and $650\\text{ mmHg}$ pressure. If the gas is allowed to expand to $150\\text{ cm}^3$ at a pressure of $680\\text{ mmHg}$, calculate the final temperature of the gas in degrees Celsius.",
                        "steps": [
                            "**1. What do we know? (Given Data)**\n- $V_1 = 100\\text{ cm}^3, T_1 = -15 + 273 = 258\\text{ K}, P_1 = 650\\text{ mmHg}$\n- $V_2 = 150\\text{ cm}^3, P_2 = 680\\text{ mmHg}$",
                            "**2. What are we finding?**\n- Final temperature in degrees Celsius ($t_2$).",
                            "**3. Calculation in Kelvin using Combined Gas Law**:\n$$\\frac{P_1 V_1}{T_1} = \\frac{P_2 V_2}{T_2} \\quad \\implies \\quad T_2 = \\frac{P_2 V_2 T_1}{P_1 V_1}$$\n$$T_2 = \\frac{680\\text{ mmHg} \\times 150\\text{ cm}^3 \\times 258\\text{ K}}{650\\text{ mmHg} \\times 100\\text{ cm}^3}$$\n$$T_2 = \\frac{26316000}{65000} = 404.86\\text{ K}$$",
                            "**4. Convert Final Temperature to Celsius**:\n$$t_2 = T_2 - 273 = 404.86 - 273 = 131.86^\\circ\\text{C} \\approx 132^\\circ\\text{C}$$",
                            "**5. Meaning of the Result**\n- To expand from $100\\text{ cm}^3$ to $150\\text{ cm}^3$ while simultaneously increasing pressure, the gas had to be heated vigorously from $-15^\\circ\\text{C}$ to $+132^\\circ\\text{C}$."
                        ]
                    }
                },
                {
                    "page_number": 6,
                    "page_title": "Think About This: High-Altitude Baking and Boiling",
                    "block_type": "common_misconception",
                    "component_type": "common_misconception",
                    "content": {
                        "text": "### Why does water boil at only $95^\\circ\\text{C}$ in Nairobi and $88^\\circ\\text{C}$ at the peak of Mt. Kenya?\nBoiling occurs when the vapor pressure of water equals atmospheric pressure. At high altitudes (Nairobi is $1795\\text{ m}$ above sea level), the air column above us is shorter, so atmospheric pressure is lower ($\approx 630\\text{ mmHg}$ vs $760\\text{ mmHg}$ at the coast in Mombasa).\n\nBecause external pressure is lower, water molecules escape into steam at a lower temperature ($95^\\circ\\text{C}$). Cooking beans at high altitudes takes much longer because boiling water is cooler, which is why pressure cookers are essential in highland regions!"
                    }
                },
                {
                    "page_number": 7,
                    "page_title": "Practice Question: Combined Gas Law Calculation",
                    "block_type": "knowledge_check",
                    "component_type": "knowledge_check",
                    "content": {
                        "check_type": "multiple_choice",
                        "question": "A cylinder holds $200\\text{ cm}^3$ of oxygen gas at $27^\\circ\\text{C}$ and $750\\text{ mmHg}$. If the volume is compressed to $100\\text{ cm}^3$ while temperature is raised to $127^\\circ\\text{C}$, what is the new pressure?",
                        "options": [
                            "$1000\\text{ mmHg}$",
                            "$1500\\text{ mmHg}$",
                            "$2000\\text{ mmHg}$",
                            "$750\\text{ mmHg}$"
                        ],
                        "answer": "C",
                        "explanation": "Convert to Kelvin: $T_1 = 27 + 273 = 300\\text{ K}$, $T_2 = 127 + 273 = 400\\text{ K}$. Rearranging Combined Gas Law: $P_2 = \\frac{P_1 V_1 T_2}{V_2 T_1} = \\frac{750\\text{ mmHg} \\times 200\\text{ cm}^3 \\times 400\\text{ K}}{100\\text{ cm}^3 \\times 300\\text{ K}} = \\frac{60000000}{30000} = 2000\\text{ mmHg}$."
                    }
                },
                {
                    "page_number": 8,
                    "page_title": "Key Takeaways: Combined Gas Law",
                    "block_type": "summary",
                    "component_type": "summary",
                    "content": {
                        "text": "### Summary: Combined Gas Law & Standard Conditions\n- **Combined Gas Law**: $\\frac{P_1V_1}{T_1} = \\frac{P_2V_2}{T_2}$.\n- **s.t.p.**: $0^\\circ\\text{C} = 273\\text{ K}$, $760\\text{ mmHg} = 101325\\text{ Pa}$.\n- **r.t.p.**: $25^\\circ\\text{C} = 298\\text{ K}$, $760\\text{ mmHg} = 101325\\text{ Pa}$.\n- **Rule**: Temperatures must always be in Kelvin."
                    }
                }
            ]
        },

        163: {
            "topic": topic_22,
            "title": "Graham's Law of Diffusion and Kinetic Theory",
            "cards": [
                {
                    "page_number": 1,
                    "page_title": "Diffusion in Gases",
                    "block_type": "learning_goal",
                    "component_type": "learning_goal",
                    "content": {
                        "text": "By the end of this module, you will state Graham's Law of Diffusion, explain why lighter gas particles diffuse faster than heavier ones using kinetic energy principles ($E_k = \\frac{1}{2}mv^2$), and solve diffusion rate and diffusion time calculations."
                    }
                },
                {
                    "page_number": 1,
                    "page_title": "The Spreading Scent of Perfume",
                    "block_type": "concept_explanation",
                    "component_type": "concept_explanation",
                    "content": {
                        "text": "If someone opens a bottle of perfume in one corner of a classroom, students in the front row smell it within seconds. A few moments later, students at the back of the room smell it too.\n\nThis spontaneous spreading of gas particles from a region of higher concentration to a region of lower concentration is called **Diffusion**.\n\nDo all gases diffuse at the exact same speed? If we release light ammonia gas ($\\text{NH}_3$) and heavy hydrogen chloride gas ($\\text{HCl}$) at opposite ends of a glass tube, which gas travels faster? Today we examine **Graham's Law of Diffusion**!"
                    }
                },
                {
                    "page_number": 2,
                    "page_title": "Molecular Mass and Velocity: Why Lighter Means Faster",
                    "block_type": "concept_explanation",
                    "component_type": "concept_explanation",
                    "content": {
                        "text": "At a given temperature, all gas molecules have the **exact same average kinetic energy** ($E_k$):\n$$E_k = \\frac{1}{2} m v^2$$\nWhere $m$ is molecular mass and $v$ is particle velocity.\n\n* **The Mathematical Balance**:\n  For two gases ($A$ and $B$) at the same temperature:\n  $$\\frac{1}{2} m_A v_A^2 = \\frac{1}{2} m_B v_B^2 \\quad \\implies \\quad \\frac{v_A}{v_B} = \\sqrt{\\frac{m_B}{m_A}}$$\n\n* **Physical Meaning**:\n  To possess the exact same kinetic energy as a heavy particle, a lighter particle **must move at a substantially higher velocity**! Therefore, lighter gas molecules travel faster and diffuse much more rapidly than heavier, sluggish molecules."
                    }
                },
                {
                    "page_number": 2,
                    "page_title": "Diagram: The Classic NH3 vs HCl Diffusion Tube",
                    "block_type": "suggested_diagram",
                    "component_type": "suggested_diagram",
                    "content": {
                        "prompt": "Diagram of a horizontal glass tube sealed at both ends with cotton wool plugs: Cotton wool soaked in concentrated Ammonia solution (NH3, Mr=17) at left, and Cotton wool soaked in concentrated Hydrochloric acid (HCl, Mr=36.5) at right. A white ring of solid Ammonium Chloride (NH4Cl) forms closer to the HCl end.",
                        "caption": "Diffusion Tube Experiment: Ammonia (Mr = 17) diffuses faster than HCl (Mr = 36.5), forming a white ring of NH4Cl closer to the HCl end."
                    },
                    "asset_info": {
                        "title": "Ammonia and HCl Diffusion Tube Diagram",
                        "description": "Schematic of laboratory diffusion tube demonstration showing unequal diffusion rates and formation of ammonium chloride solid ring.",
                        "ai_instruction": "Create a clear glass tube diagram showing NH3 cotton wool on left, HCl on right, and white precipitate ring forming much closer to the HCl end."
                    }
                },
                {
                    "page_number": 3,
                    "page_title": "Graham's Law Formulation",
                    "block_type": "definition_card",
                    "component_type": "definition_card",
                    "content": {
                        "term": "Graham's Law of Diffusion",
                        "content": "### Definition\n*The rate of diffusion of a gas is inversely proportional to the square root of its density or relative molecular mass ($M_r$), provided temperature and pressure remain constant.*\n\n### Mathematical Formulation:\n$$\\text{Rate of Diffusion } (R) \\propto \\frac{1}{\\sqrt{M_r}} \\propto \\frac{1}{\\sqrt{\\rho}}$$\n\n### Comparing Two Gases ($1$ and $2$):\n$$\\mathbf{\\frac{R_1}{R_2} = \\sqrt{\\frac{M_2}{M_1}} = \\sqrt{\\frac{\\rho_2}{\\rho_1}}}$$\n\n### In Terms of Diffusion Time ($t$):\nBecause Rate is inversely proportional to Time ($R = \\frac{\\text{Volume}}{t}$):\n$$\\mathbf{\\frac{t_2}{t_1} = \\sqrt{\\frac{M_2}{M_1}} = \\frac{R_1}{R_2}}$$"
                    }
                },
                {
                    "page_number": 4,
                    "page_title": "Worked Example 1: Finding Molecular Mass from Diffusion Time",
                    "block_type": "worked_example",
                    "component_type": "worked_example",
                    "content": {
                        "problem": "$100\\text{ cm}^3$ of oxygen gas ($\\text{O}_2$) takes $125\\text{ seconds}$ to diffuse through a porous plug. Under identical conditions, $100\\text{ cm}^3$ of an unknown gas $X$ takes $100\\text{ seconds}$. Calculate the Relative Molecular Mass ($M_r$) of gas $X$. ($A_r$: $\\text{O}=16.0$).",
                        "steps": [
                            "**1. What do we know? (Given Data)**\n- Gas 1 (Oxygen, $\\text{O}_2$): $M_1 = 2(16.0) = 32.0\\text{ g/mol}$, $t_1 = 125\\text{ s}$\n- Gas 2 (Unknown $X$): $M_2 = \\text{Target } M_r$, $t_2 = 100\\text{ s}$",
                            "**2. Governing Formula connecting Time and Molecular Mass**\n$$\\frac{t_2}{t_1} = \\sqrt{\\frac{M_2}{M_1}}$$",
                            "**3. Step-by-Step Substitution**:\n$$\\frac{100}{125} = \\sqrt{\\frac{M_2}{32.0}}$$\n$$0.8 = \\sqrt{\\frac{M_2}{32.0}}$$",
                            "**4. Square both sides to eliminate square root**:\n$$(0.8)^2 = \\frac{M_2}{32.0} \\implies 0.64 = \\frac{M_2}{32.0}$$\n$$M_2 = 0.64 \\times 32.0 = 20.48$$",
                            "**5. Meaning of the Result & Sanity Check**\n- Because gas $X$ took less time ($100\\text{ s}$ vs $125\\text{ s}$), it diffused faster and must be lighter than oxygen ($M_r = 20.48 < 32.0$)."
                        ]
                    }
                },
                {
                    "page_number": 5,
                    "page_title": "Worked Example 2: Calculating Relative Rates of Diffusion",
                    "block_type": "worked_example",
                    "component_type": "worked_example",
                    "content": {
                        "problem": "In a laboratory experiment, ammonia gas ($\\text{NH}_3$) traveled $12.0\\text{ cm}$ in $5.0\\text{ minutes}$, while hydrogen chloride gas ($\\text{HCl}$) traveled $8.0\\text{ cm}$ in the same time. (a) Calculate the diffusion rate of each gas. (b) Compare the ratio of rates to the theoretical Graham's Law value. ($A_r$: $\\text{N}=14.0, \\text{H}=1.0, \\text{Cl}=35.5$).",
                        "steps": [
                            "**1. Part (a): Calculate Diffusion Rates ($R = \\frac{\\text{Distance}}{\\text{Time}}$)**\n- Rate of $\\text{NH}_3$: $R_{\\text{NH}_3} = \\frac{12.0\\text{ cm}}{5.0\\text{ min}} = 2.4\\text{ cm/min}$\n- Rate of $\\text{HCl}$: $R_{\\text{HCl}} = \\frac{8.0\\text{ cm}}{5.0\\text{ min}} = 1.6\\text{ cm/min}$",
                            "**2. Part (b): Experimental Rate Ratio**\n$$\\frac{R_{\\text{NH}_3}}{R_{\\text{HCl}}} = \\frac{2.4}{1.6} = 1.50$$",
                            "**3. Theoretical Ratio from Molecular Masses**\n- $M_r(\\text{NH}_3) = 14.0 + 3(1.0) = 17.0$\n- $M_r(\\text{HCl}) = 1.0 + 35.5 = 36.5$\n$$\\text{Theoretical Ratio} = \\sqrt{\\frac{M_r(\\text{HCl})}{M_r(\\text{NH}_3)}} = \\sqrt{\\frac{36.5}{17.0}} = \\sqrt{2.147} = 1.465 \\approx 1.47$$",
                            "**4. Conclusion**\n- The experimental ratio ($1.50$) closely matches the theoretical Graham's Law prediction ($1.47$), confirming that ammonia diffuses roughly $1.5\\text{ times}$ faster than $\\text{HCl}$."
                        ]
                    }
                },
                {
                    "page_number": 6,
                    "page_title": "Think About This: Why Diffusion is Slower in Air Than in a Vacuum",
                    "block_type": "common_misconception",
                    "component_type": "common_misconception",
                    "content": {
                        "text": "### Why does perfume take several seconds to cross a room if molecules travel at $500\\text{ m/s}$?\nAt room temperature, an ammonia or perfume molecule moves at supersonic speed ($> 500\\text{ m/s}$ or $1800\\text{ km/h}$). If the room were a total vacuum, the scent would reach you in $\\frac{1}{100}\\text{th}$ of a second!\n\nHowever, in a normal room, air contains billions of nitrogen and oxygen molecules. The perfume molecule collides with air molecules over **$5\\text{ billion times every second}$**, bouncing in a chaotic zig-zag random walk. This constant collision slows down its net forward progress across the room."
                    }
                },
                {
                    "page_number": 7,
                    "page_title": "Practice Question: Comparing Diffusion Rates",
                    "block_type": "knowledge_check",
                    "component_type": "knowledge_check",
                    "content": {
                        "check_type": "multiple_choice",
                        "question": "Which of the following gases will diffuse the fastest through a porous partition under identical temperature and pressure conditions? ($A_r$: $\\text{H}=1, \\text{He}=4, \\text{C}=12, \\text{N}=14, \\text{O}=16, \\text{S}=32$).",
                        "options": [
                            "Carbon dioxide ($\\text{CO}_2$)",
                            "Helium ($\\text{He}$)",
                            "Methane ($\\text{CH}_4$)",
                            "Sulfur dioxide ($\\text{SO}_2$)"
                        ],
                        "answer": "B",
                        "explanation": "Calculate molecular masses ($M_r$): $\\text{SO}_2 = 64.0$, $\\text{CO}_2 = 44.0$, $\\text{CH}_4 = 16.0$, $\\text{He} = 4.0$. According to Graham's Law, diffusion rate is inversely proportional to $\\sqrt{M_r}$. Helium has the lowest molecular mass ($4.0\\text{ g/mol}$) and therefore diffuses the fastest."
                    }
                },
                {
                    "page_number": 8,
                    "page_title": "Key Takeaways: Graham's Law",
                    "block_type": "summary",
                    "component_type": "summary",
                    "content": {
                        "text": "### Summary: Graham's Law of Diffusion\n- **Diffusion**: Spontaneous movement of particles from high to low concentration.\n- **Graham's Law**: Rate is inversely proportional to square root of molecular mass ($R \\propto \\frac{1}{\\sqrt{M_r}}$).\n- **Equations**:\n  $$\\frac{R_1}{R_2} = \\sqrt{\\frac{M_2}{M_1}} = \\frac{t_2}{t_1}$$\n- **Kinetic Energy Equivalence**: $\\frac{1}{2}m_1v_1^2 = \\frac{1}{2}m_2v_2^2$ (lighter particles move with higher velocities)."
                    }
                }
            ]
        }
    }

    # Execute database updates for Topic 22 lessons
    for lesson_id, data in lessons_data.items():
        try:
            lesson = Lesson.objects.get(id=lesson_id)
            print(f"Updating Lesson {lesson.id}: \"{lesson.title}\" in {data['topic'].name}...")
            
            LessonBlock.objects.filter(lesson=lesson).delete()
            LessonAsset.objects.filter(lesson=lesson).delete()
            
            for order, card in enumerate(data["cards"], start=1):
                block_id = f"block_{lesson.id}_{order}_{uuid.uuid4().hex[:6]}"
                b = LessonBlock.objects.create(
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
                
                if "asset_info" in card:
                    info = card["asset_info"]
                    LessonAsset.objects.create(
                        lesson=lesson,
                        asset_type="diagram",
                        source_type="uploaded",
                        storage_type="local",
                        status="pending",
                        title=info["title"],
                        description=info["description"],
                        metadata={"ai_instruction": info["ai_instruction"], "block_id": b.block_id}
                    )
            
            lesson.status = "published"
            lesson.save()
            print(f"  Successfully refactored Lesson {lesson.id} with {len(data['cards'])} cards.")
        except Lesson.DoesNotExist:
            print(f"Lesson ID {lesson_id} not found in database!")

if __name__ == "__main__":
    run_refactor()
