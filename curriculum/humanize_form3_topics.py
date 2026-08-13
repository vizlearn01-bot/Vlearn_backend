import os
import sys
import django
import uuid

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "Nexus_backend.settings")
django.setup()

from curriculum.models import Topic, Lesson, LessonBlock, LessonAsset

# ==============================================================================
# HUMANIZATION DATA FOR TOPIC 22: GAS LAWS (Lessons 159 - 163)
# ==============================================================================
topic_22_data = {
    159: {
        "title": "Introduction to the Gaseous State and Kinetic Theory",
        "cards": [
            {
                "page_number": 1,
                "page_title": "The Gaseous State",
                "block_type": "learning_goal",
                "component_type": "learning_goal",
                "content": {
                    "text": "By the end of this module, you will understand the physical nature of gases, explain the 5 principles of the Kinetic Theory of Matter using intuitive particle models, and explain how invisible particle collisions create measurable gas pressure ($P = \\frac{\\text{Force}}{\\text{Area}}$)."
                }
            },
            {
                "page_number": 1,
                "page_title": "The Invisible Ocean of Gas Around Us",
                "block_type": "concept_explanation",
                "component_type": "concept_explanation",
                "content": {
                    "text": "Right now, you are sitting at the bottom of an invisible ocean of gas particles. You cannot see the nitrogen ($\\text{N}_2$) and oxygen ($\\text{O}_2$) molecules around you, but you feel their powerful physical presence whenever wind pushes against you or an inflated football bounces off the ground.\n\nWhile solids have rigid shapes and liquids flow to take the shape of their container while keeping a fixed volume, **gases have no fixed shape and no fixed volume**.\n\nA gas expands to fill every corner of any container you place it in, whether it is a small test tube or a giant classroom. To understand why gases behave like this, we need to zoom in to the particle level where billions of tiny molecules are zipping around at hundreds of meters per second!"
                }
            },
            {
                "page_number": 2,
                "page_title": "States of Matter: A Particle Comparison",
                "block_type": "concept_explanation",
                "component_type": "concept_explanation",
                "content": {
                    "text": "Here is how the three states of matter compare at the particle level:\n\n* **Solids (Tightly Packed)**: Particles are locked in a fixed grid. They cannot move around; they can only vibrate in place. This gives solids a fixed shape and fixed volume.\n* **Liquids (Close but Flowing)**: Particles are touching, but they have enough energy to slide past one another. This gives liquids a fixed volume, but lets them change shape.\n* **Gases (Widely Separated & Free)**: Particles are separated by vast empty distances (over 10 times their own size). They fly freely in all directions with virtually zero attraction to one another. That is why gases are **easily compressed** and have **very low densities**!"
                }
            },
            {
                "page_number": 2,
                "page_title": "Diagram: States of Matter Particle Models",
                "block_type": "suggested_diagram",
                "component_type": "suggested_diagram",
                "content": {
                    "prompt": "Clear three-panel molecular comparison: Solid (tight regular grid vibrating in place), Liquid (closely packed particles sliding past each other), and Gas (widely spaced particles with high-speed motion arrows bouncing off container walls).",
                    "caption": "Particle Arrangements: In gases, particles are separated by vast empty spaces and move freely at high speeds."
                },
                "asset_info": {
                    "title": "States of Matter Particle Models",
                    "description": "Particle-level comparison of solids, liquids, and gases highlighting intermolecular spacing and kinetic velocity vectors.",
                    "ai_instruction": "Render three side-by-side particle boxes showing Solid (lattice), Liquid (condensed fluid), and Gas (widely spaced particles with collision vectors)."
                }
            },
            {
                "page_number": 3,
                "page_title": "The Kinetic Theory of Gases (In Plain English)",
                "block_type": "concept_explanation",
                "component_type": "concept_explanation",
                "content": {
                    "text": "To describe gas behavior accurately, scientists developed the **Kinetic Theory of Gases**, which is built on 5 straightforward rules:\n\n1. **Gases are Mostly Empty Space**: The actual gas particles are so tiny compared to the huge distances between them that their individual size is practically negligible.\n2. **No Sticky Forces**: Because particles are so far apart, they don't attract or repel each other under normal conditions.\n3. **Perpetual Motion**: Gas particles travel continuously in straight lines in all directions like tiny, super-fast bumper cars.\n4. **Bouncy Collisions (Elastic)**: When particles hit each other or the container walls, they bounce off cleanly without losing any total kinetic energy.\n5. **Pressure is Just Particle Bombardment**: Gas pressure ($P$) is simply the combined push of billions of particles slamming into the container walls every second:\n   $$P = \\frac{\\text{Total Force of Collisions}}{\\text{Area of Wall}}$$"
                }
            },
            {
                "page_number": 4,
                "page_title": "Gases in Everyday Kenyan Life",
                "block_type": "real_world_example",
                "component_type": "real_world_example",
                "content": {
                    "text": "### 1. Cooking Gas (LPG Cylinders)\nIn homes across Kenya, we use gas cylinders (like K-Gas, Total Gas, or Pro-Gas). Under heavy mechanical pressure, gas particles are squeezed so close together that they condense into a liquid. When you turn on the burner valve, you release that pressure—allowing the liquid to instantly vaporize into fast-moving gas for cooking!\n\n### 2. Farm Biogas Digesters\nOn dairy farms in **Meru, Eldoret, and Kiambu**, cow dung ferments inside sealed underground tanks. This produces methane gas ($\\text{CH}_4$). As more gas is produced, the particles crowd inside and push up against floating metal tank lids, providing clean fuel on tap for cooking and lighting."
                }
            },
            {
                "page_number": 5,
                "page_title": "Worked Example: Why Bicycle Tyres Get Hard When Pumped",
                "block_type": "worked_example",
                "component_type": "worked_example",
                "content": {
                    "problem": "Using the Kinetic Theory of Gases, explain step-by-step why pumping extra air into a bicycle tyre makes the tyre feel harder and increases internal pressure.",
                    "steps": [
                        "**1. What do we know? (Given Conditions)**\n- The tyre's volume ($V$) is fixed and enclosed by tough rubber.\n- The temperature ($T$) remains constant.\n- We are pumping in additional air molecules ($N$).",
                        "**2. What are we explaining?**\n- The physical particle-level cause of increased measured pressure ($P$).",
                        "**3. The Scientific Formula & Principle**\n$$\\text{Pressure } (P) = \\frac{\\text{Collision Force } (F)}{\\text{Surface Area } (A)}$$\n- Pressure comes entirely from gas particles striking the inner rubber walls.",
                        "**4. Step-by-Step Particle Explanation**\n- Pumping air crowds significantly more molecules into the exact same enclosed space.\n- With more particles packed together, each particle travels a shorter distance before hitting the inner rubber wall.\n- This dramatically increases the **collision frequency** (the number of particle impacts hitting each square centimeter of rubber every second).",
                        "**5. Meaning of the Result & Conclusion**\n- More collisions per second deliver a larger total outward force against the rubber.\n- Therefore, the measured pressure ($P = F/A$) goes up, making the tyre feel firm and rigid."
                    ]
                }
            },
            {
                "page_number": 6,
                "page_title": "Think About This: Common Gas Questions",
                "block_type": "common_misconception",
                "component_type": "common_misconception",
                "content": {
                    "text": "### Misconception 1: Is the space between gas particles filled with air?\n**Clarification**: Air is itself made of gas particles (mostly $\\text{N}_2$ and $\\text{O}_2$). The space between these particles has nothing in it at all—it is a **complete vacuum**!\n\n### Misconception 2: Do gas particles get heavier when heated?\n**Clarification**: No! The actual weight of a single atom never changes with temperature. Heating a gas only makes the particles move faster (higher kinetic energy); it does not change their atomic mass."
                }
            },
            {
                "page_number": 7,
                "page_title": "Practice Question 1: Gas Density",
                "block_type": "knowledge_check",
                "component_type": "knowledge_check",
                "content": {
                    "check_type": "multiple_choice",
                    "question": "Which of the following statements best explains why gases have a much lower density than solids under normal conditions?",
                    "options": [
                        "Gas particles are individually much lighter than solid atoms.",
                        "Gas particles experience negligible intermolecular attraction and are separated by vast empty distances, so there is very little mass per unit volume.",
                        "Gas particles are in constant, random straight-line motion.",
                        "Gas particles undergo perfectly elastic collisions with container walls."
                    ],
                    "answer": "B",
                    "explanation": "Density is mass divided by volume ($\\rho = \\frac{m}{V}$). Because gas particles are spaced very far apart with vast empty regions between them, there is very little mass contained in a given volume compared to tightly packed solids."
                }
            },
            {
                "page_number": 7,
                "page_title": "Practice Question 2: Temperature & Kinetic Energy",
                "block_type": "knowledge_check",
                "component_type": "knowledge_check",
                "content": {
                    "check_type": "multiple_choice",
                    "question": "According to the Kinetic Theory of Matter, which factor is directly proportional to the average kinetic energy of gas molecules?",
                    "options": [
                        "Volume of the gas container",
                        "Absolute temperature in Kelvin",
                        "Pressure in atmospheres",
                        "Density in grams per cubic centimeter"
                    ],
                    "answer": "B",
                    "explanation": "A core postulate of kinetic theory is that the average kinetic energy of gas particles is directly proportional to absolute temperature in Kelvin ($E_k \\propto T$). If you double the Kelvin temperature, you double the average kinetic energy."
                }
            },
            {
                "page_number": 8,
                "page_title": "Key Takeaways: The Gaseous State",
                "block_type": "summary",
                "component_type": "summary",
                "content": {
                    "text": "### Quick Recap: Introduction to Gases\n- **Gaseous State**: No fixed shape, no fixed volume, highly compressible, low density.\n- **Absolute Temperature & Energy**: Temperature in Kelvin directly measures the average kinetic energy of particles ($E_k \\propto T$).\n- **5 Postulates**: Vast spacing, negligible attraction, perpetual random motion, elastic collisions, collision-based pressure.\n- **Gas Pressure Formula**: $P = \\frac{\\text{Force}}{\\text{Area}}$ (arises from billions of wall impacts per second)."
                }
            }
        ]
    },

    160: {
        "title": "Boyle's Law (Pressure-Volume Relationship)",
        "cards": [
            {
                "page_number": 1,
                "page_title": "Pressure and Volume",
                "block_type": "learning_goal",
                "component_type": "learning_goal",
                "content": {
                    "text": "By the end of this module, you will state Boyle's Law in simple terms, understand the inverse seesaw relationship between pressure and volume at constant temperature, interpret pressure-volume graphs, and solve quantitative gas problems with complete step-by-step clarity."
                }
            },
            {
                "page_number": 1,
                "page_title": "The Trapped Air in a Syringe",
                "block_type": "concept_explanation",
                "component_type": "concept_explanation",
                "content": {
                    "text": "Take a plastic syringe (without a needle), pull the plunger halfway back to draw in air, and firmly seal the tip with your thumb so no air can escape.\n\nNow, try pushing the plunger in:\n* At first, it slides easily.\n* But as you squeeze the air into a smaller and smaller volume, the trapped air pushes back against your thumb with tremendous force!\n* If you let go of the plunger, it springs right back.\n\nWhy does trapped air resist being squeezed? Today we explore **Boyle's Law**, which explains exactly how pressure and volume interact when temperature stays constant."
                }
            },
            {
                "page_number": 2,
                "page_title": "How Boyle's Law Works at the Particle Level",
                "block_type": "concept_explanation",
                "component_type": "concept_explanation",
                "content": {
                    "text": "Think of Boyle's Law as a **seesaw** between pressure and volume:\n\n* **Halving the Volume ($V \\rightarrow \\frac{1}{2}V$)**:\n  When you compress the trapped gas into half its original space, the exact same number of particles are now crowded into half the room.\n* **Doubling the Collisions ($P \\rightarrow 2P$)**:\n  Because the walls are closer together, particles travel shorter distances between bounces. They hit the walls **twice as often** every second. Since pressure is simply the rate of wall impacts, doubling collision frequency **doubles the pressure**!\n\n* **The Mathematical Relationship**:\n  $$P \\propto \\frac{1}{V} \\quad \\implies \\quad P \\times V = \\text{constant}$$\n  $$\\mathbf{P_1 V_1 = P_2 V_2}$$"
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
                "page_title": "Boyle's Law & Pressure Units (In Plain English)",
                "block_type": "definition_card",
                "component_type": "definition_card",
                "content": {
                    "term": "Boyle's Law",
                    "content": "### What is Boyle's Law?\n*For a fixed mass of gas at constant temperature, pressure and volume are inversely proportional. Squeeze the volume, and pressure rises; expand the volume, and pressure falls.*\n\n### The Master Equation:\n$$\\mathbf{P_1 V_1 = P_2 V_2}$$\n\n### Units You Need to Know:\n- **Pressure ($P$)**: $1\\text{ atm} = 760\\text{ mmHg} = 101325\\text{ Pa} = 101.3\\text{ kPa}$\n- **Volume ($V$)**: $1\\text{ dm}^3 = 1000\\text{ cm}^3 = 1\\text{ Litre} = 1000\\text{ mL}$\n\n*Golden Rule*: As long as $P_1$ and $P_2$ have the same units, and $V_1$ and $V_2$ have the same units, the formula works seamlessly!"
                }
            },
            {
                "page_number": 4,
                "page_title": "Worked Example 1: Gas Volume Under Changing Pressure",
                "block_type": "worked_example",
                "component_type": "worked_example",
                "content": {
                    "problem": "A sample of trapped air occupies a volume of $500\\text{ cm}^3$ at a pressure of $760\\text{ mmHg}$. If the pressure is increased to $1520\\text{ mmHg}$ at constant temperature, what is the new volume of the gas?",
                    "steps": [
                        "**1. What do we know? (Given Data)**\n- Initial volume $V_1 = 500\\text{ cm}^3$\n- Initial pressure $P_1 = 760\\text{ mmHg}$\n- Final pressure $P_2 = 1520\\text{ mmHg}$\n- Temperature is constant.",
                        "**2. What are we finding? (Target Quantity)**\n- Final volume $V_2$ in $\\text{cm}^3$.",
                        "**3. Which formula applies and why?**\n- Temperature is constant, so we use Boyle's Law: $P_1V_1 = P_2V_2$.",
                        "**4. Step-by-Step Calculation**\n- Rearrange to solve for $V_2$:\n$$V_2 = \\frac{P_1 \\times V_1}{P_2}$$\n- Substitute the numbers:\n$$V_2 = \\frac{760\\text{ mmHg} \\times 500\\text{ cm}^3}{1520\\text{ mmHg}} = \\frac{380000}{1520} = 250\\text{ cm}^3$$",
                        "**5. Sanity Check & Meaning of the Result**\n- The pressure doubled ($760 \\rightarrow 1520\\text{ mmHg}$), so the volume was halved ($500 \\rightarrow 250\\text{ cm}^3$). This makes complete physical sense!"
                    ]
                }
            },
            {
                "page_number": 5,
                "page_title": "Worked Example 2: Converting Between Pressure Units",
                "block_type": "worked_example",
                "component_type": "worked_example",
                "content": {
                    "problem": "A mass of gas occupies $456\\text{ cm}^3$ at $750\\text{ mmHg}$. Find its volume if the pressure becomes $1.0 \\times 10^5\\text{ Pa}$ at constant temperature. (Standard equivalence: $760\\text{ mmHg} = 1.013 \\times 10^5\\text{ Pa}$).",
                    "steps": [
                        "**1. What do we know?**\n- $V_1 = 456\\text{ cm}^3$\n- $P_1 = 750\\text{ mmHg}$\n- $P_2 = 1.0 \\times 10^5\\text{ Pa}$",
                        "**2. Match the Units First!**\n- Let's convert $P_1$ into Pascals ($\\text{Pa}$) so both pressures match:\n$$P_1 = \\frac{750}{760} \\times 1.013 \\times 10^5\\text{ Pa} = 99967\\text{ Pa}$$",
                        "**3. Apply Boyle's Law**\n$$V_2 = \\frac{P_1 \\times V_1}{P_2}$$\n$$V_2 = \\frac{99967\\text{ Pa} \\times 456\\text{ cm}^3}{100000\\text{ Pa}} = 455.85\\text{ cm}^3 \\approx 456\\text{ cm}^3$$",
                        "**4. Conclusion**\n- Since $750\\text{ mmHg}$ is virtually identical to $1.0 \\times 10^5\\text{ Pa}$, the volume remains practically unchanged at $456\\text{ cm}^3$."
                    ]
                }
            },
            {
                "page_number": 6,
                "page_title": "Think About This: Why Scuba Divers Never Hold Their Breath",
                "block_type": "common_misconception",
                "component_type": "common_misconception",
                "content": {
                    "text": "### Why must scuba divers NEVER hold their breath while swimming to the surface?\nAt $20\\text{ meters}$ below the ocean surface, the water pressure is $3\\text{ atmospheres}$ (3 times normal surface pressure). A diver's lungs contain air compressed at $3\\text{ atm}$.\n\nIf the diver swims up to the surface ($1\\text{ atm}$) while holding their breath, the outside pressure drops by a factor of 3. By Boyle's Law ($P_1V_1 = P_2V_2$), the air trapped inside their lungs will **expand to 3 times its volume**, rupturing their lung tissue! That is why divers are trained to breathe out continuously as they ascend."
                }
            },
            {
                "page_number": 7,
                "page_title": "Practice Question 1: Squeezing a Syringe",
                "block_type": "knowledge_check",
                "component_type": "knowledge_check",
                "content": {
                    "check_type": "multiple_choice",
                    "question": "A syringe holds $60\\text{ cm}^3$ of air at $1.0\\text{ atm}$. If you push the plunger until the volume is reduced to $20\\text{ cm}^3$ at constant temperature, what is the new pressure inside?",
                    "options": [
                        "$0.33\\text{ atm}$",
                        "$2.0\\text{ atm}$",
                        "$3.0\\text{ atm}$",
                        "$6.0\\text{ atm}$"
                    ],
                    "answer": "C",
                    "explanation": "Using Boyle's Law: $P_1V_1 = P_2V_2 \\implies P_2 = \\frac{1.0\\text{ atm} \\times 60\\text{ cm}^3}{20\\text{ cm}^3} = 3.0\\text{ atm}$. Reducing the volume to $\\frac{1}{3}\\text{rd}$ triples the pressure."
                }
            },
            {
                "page_number": 7,
                "page_title": "Practice Question 2: Graphing Boyle's Law",
                "block_type": "knowledge_check",
                "component_type": "knowledge_check",
                "content": {
                    "check_type": "multiple_choice",
                    "question": "Which of the following graphs will yield a straight line passing through the origin for a fixed mass of gas at constant temperature?",
                    "options": [
                        "Pressure ($P$) plotted against Volume ($V$)",
                        "Pressure ($P$) plotted against inverse volume ($\\frac{1}{V}$)",
                        "Volume ($V$) plotted against Temperature in Celsius",
                        "Pressure ($P$) plotted against Temperature in Celsius"
                    ],
                    "answer": "B",
                    "explanation": "Because $P$ is inversely proportional to $V$ ($P \\propto \\frac{1}{V}$), plotting $P$ against $\\frac{1}{V}$ turns the curve into a direct linear relationship: $P = k(\\frac{1}{V})$, producing a straight line through the origin."
                }
            },
            {
                "page_number": 8,
                "page_title": "Key Takeaways: Boyle's Law",
                "block_type": "summary",
                "component_type": "summary",
                "content": {
                    "text": "### Summary: Boyle's Law\n- **The Rule**: When temperature is constant, pressure and volume are on a seesaw ($P \\propto \\frac{1}{V}$).\n- **The Equation**: $P_1V_1 = P_2V_2$.\n- **The Graphs**: $P$ vs $V$ is a downward curve (hyperbola); $P$ vs $\\frac{1}{V}$ is a straight line through the origin.\n- **The Particle Reason**: Squeezing gas into smaller volume crowds particles, doubling wall impacts per second."
                }
            }
        ]
    }
}

print("Topic 22 data structure ready.")
