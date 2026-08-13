import os
import sys
import django
import uuid

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "Nexus_backend.settings")
django.setup()

from curriculum.models import Topic, Lesson, LessonBlock, LessonAsset

def run_comprehensive_humanization():
    print("Executing comprehensive humanization across Form 3 Chemistry...")

    topic_22 = Topic.objects.get(id=22) # Gas Laws
    topic_23 = Topic.objects.get(id=23) # The Mole
    topic_24 = Topic.objects.get(id=24) # Organic Chemistry I

    lessons_payload = {}

    # =========================================================================
    # TOPIC 22: GAS LAWS (Refining Lessons 161, 162, 163)
    # =========================================================================
    lessons_payload[161] = {
        "topic": topic_22,
        "title": "Charles's Law (Temperature-Volume Relationship)",
        "cards": [
            {
                "page_number": 1,
                "page_title": "Temperature and Volume",
                "block_type": "learning_goal",
                "component_type": "learning_goal",
                "content": {
                    "text": "By the end of this module, you will understand Charles's Law in simple terms, explain why gas volume expands when heated using particle kinetic energy, master the Kelvin temperature scale, and solve quantitative volume-temperature calculations."
                }
            },
            {
                "page_number": 1,
                "page_title": "The Balloon Left in the Midday Sun",
                "block_type": "concept_explanation",
                "component_type": "concept_explanation",
                "content": {
                    "text": "Have you ever inflated a party balloon inside a cool house in the morning and then left it sitting on sunlit grass at midday? Within an hour, the balloon expands noticeably, and may even pop with a loud bang!\n\nConversely, if you put a balloon into a refrigerator, it visibly shrinks and wrinkles. Why do gases expand when warmed and shrink when cooled? Today we explore **Charles's Law**, which explains how heat directly expands gas volume."
                }
            },
            {
                "page_number": 2,
                "page_title": "Absolute Zero & The Kelvin Temperature Scale",
                "block_type": "concept_explanation",
                "component_type": "concept_explanation",
                "content": {
                    "text": "When scientists cool a gas and plot volume against Celsius temperature, the straight-line graph points directly to **$-273.15^\\circ\\text{C}$** when volume reaches zero.\n\n* **What is Absolute Zero ($0\\text{ K}$)?**\n  At $-273^\\circ\\text{C}$, the kinetic energy of all gas particles theoretically drops to zero. All molecular motion stops completely! Because it is impossible to have less than zero movement, $-273^\\circ\\text{C}$ is the absolute coldest temperature in the universe.\n\n* **The Kelvin Scale ($T$)**:\n  To make temperature directly proportional to particle energy ($E_k \\propto T$), chemists use the Kelvin scale:\n  $$\\mathbf{T\\text{ (Kelvin)} = t\\text{ (}^\\circ\\text{C)} + 273}$$\n\n*Golden Rule of Gas Laws*: **Always convert temperatures to Kelvin ($+273$) before doing any gas math!**"
                }
            },
            {
                "page_number": 2,
                "page_title": "Diagram: Charles's Law Graphical Extrapolation",
                "block_type": "suggested_diagram",
                "component_type": "suggested_diagram",
                "content": {
                    "prompt": "Graph showing Volume vs Temperature in Celsius with experimental lines extrapolating backwards to intercept the horizontal axis at exactly -273°C (Absolute Zero, 0 Kelvin).",
                    "caption": "Charles's Law Extrapolation: Volume lines for all gases point to zero volume at -273°C (0 Kelvin)."
                },
                "asset_info": {
                    "title": "Charles's Law Absolute Zero Plot",
                    "description": "Graphical plot of volume versus Celsius temperature demonstrating extrapolation to Absolute Zero (-273°C).",
                    "ai_instruction": "Create a graph of Volume (y-axis) vs Temperature in Celsius (x-axis), with experimental lines extrapolating backwards to intercept the axis at -273°C."
                }
            },
            {
                "page_number": 3,
                "page_title": "Charles's Law (In Plain English)",
                "block_type": "definition_card",
                "component_type": "definition_card",
                "content": {
                    "term": "Charles's Law",
                    "content": "### What is Charles's Law?\n*When you heat a gas at constant pressure, its particles gain kinetic energy, move faster, and push outward—causing the volume to expand. Warm it up $\\rightarrow$ it expands; cool it down $\\rightarrow$ it shrinks.*\n\n---\n\n### The Master Equation:\n$$\\mathbf{\\frac{V_1}{T_1} = \\frac{V_2}{T_2}}$$\n\n* **$V_1$** = Initial volume (in $\\text{cm}^3$ or $\\text{dm}^3$)\n* **$T_1$** = Initial absolute temperature in **Kelvin** ($t_1 + 273$)\n* **$V_2$** = Final volume (in $\\text{cm}^3$ or $\\text{dm}^3$)\n* **$T_2$** = Final absolute temperature in **Kelvin** ($t_2 + 273$)"
                }
            },
            {
                "page_number": 4,
                "page_title": "Worked Example 1: Volume Change with Temperature",
                "block_type": "worked_example",
                "component_type": "worked_example",
                "content": {
                    "problem": "A gas occupies $450\\text{ cm}^3$ at $27^\\circ\\text{C}$. Calculate its volume if heated to $177^\\circ\\text{C}$ at constant pressure.",
                    "steps": [
                        "**1. What do we know? (Given Data)**\n- Initial volume $V_1 = 450\\text{ cm}^3$\n- Initial temperature $t_1 = 27^\\circ\\text{C}$\n- Final temperature $t_2 = 177^\\circ\\text{C}$",
                        "**2. What are we finding?**\n- Final volume $V_2$ in $\\text{cm}^3$.",
                        "**3. Convert Temperatures to Kelvin FIRST!**\n$$T_1 = 27 + 273 = 300\\text{ K}$$\n$$T_2 = 177 + 273 = 450\\text{ K}$$",
                        "**4. Apply Charles's Law & Calculate**:\n$$\\frac{V_1}{T_1} = \\frac{V_2}{T_2} \\quad \\implies \\quad V_2 = \\frac{V_1 \\times T_2}{T_1}$$\n$$V_2 = \\frac{450\\text{ cm}^3 \\times 450\\text{ K}}{300\\text{ K}} = \\frac{202500}{300} = 675\\text{ cm}^3$$",
                        "**5. Sanity Check & Meaning of the Result**\n- The Kelvin temperature increased by a factor of $1.5$ ($300 \\rightarrow 450\\text{ K}$). The volume expanded by the exact same factor ($450 \\times 1.5 = 675\\text{ cm}^3$)!"
                    ]
                }
            },
            {
                "page_number": 5,
                "page_title": "Worked Example 2: Determining Final Temperature in Celsius",
                "block_type": "worked_example",
                "component_type": "worked_example",
                "content": {
                    "problem": "A mass of gas occupies $750\\text{ cm}^3$ at $57^\\circ\\text{C}$. At what Celsius temperature will its volume shrink to $100\\text{ cm}^3$ if pressure is constant?",
                    "steps": [
                        "**1. What do we know?**\n- $V_1 = 750\\text{ cm}^3$\n- $T_1 = 57 + 273 = 330\\text{ K}$\n- $V_2 = 100\\text{ cm}^3$",
                        "**2. Calculate Final Temperature in Kelvin ($T_2$)**:\n$$T_2 = \\frac{V_2 \\times T_1}{V_1} = \\frac{100\\text{ cm}^3 \\times 330\\text{ K}}{750\\text{ cm}^3} = 44\\text{ K}$$",
                        "**3. Convert Kelvin Back to Celsius**:\n$$t_2 = T_2 - 273 = 44 - 273 = -229^\\circ\\text{C}$$",
                        "**4. Conclusion**\n- To compress the volume down to $100\\text{ cm}^3$, the gas must be cooled to an extreme $-229^\\circ\\text{C}$."
                    ]
                }
            },
            {
                "page_number": 6,
                "page_title": "Think About This: Why Celsius Cannot Be Used in Formulas",
                "block_type": "common_misconception",
                "component_type": "common_misconception",
                "content": {
                    "text": "### Why does substituting Celsius into Charles's Law break the math?\nIf you used $0^\\circ\\text{C}$ in the formula, you would be dividing by zero ($\frac{V}{0} = \\text{Math Error!}$). At negative Celsius temperatures, the formula would predict negative volume, which is physically impossible!\n\nThe Kelvin scale solves this because $0\\text{ K}$ is the true zero-energy floor, making all temperature numbers positive and directly proportional to energy."
                }
            },
            {
                "page_number": 7,
                "page_title": "Practice Question 1: Heating a Balloon",
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
                    "explanation": "Convert to Kelvin: $T_1 = 20 + 273 = 293\\text{ K}$, $T_2 = 40 + 273 = 313\\text{ K}$. $V_2 = 2.0 \\times \\frac{313}{293} = 2.14\\text{ dm}^3$."
                }
            },
            {
                "page_number": 7,
                "page_title": "Practice Question 2: Finding Final Temperature",
                "block_type": "knowledge_check",
                "component_type": "knowledge_check",
                "content": {
                    "check_type": "multiple_choice",
                    "question": "A sample of gas occupies $300\\text{ cm}^3$ at $27^\\circ\\text{C}$. If the volume expands to $600\\text{ cm}^3$ at constant pressure, what is the final Celsius temperature?",
                    "options": [
                        "$54^\\circ\\text{C}$",
                        "$327^\\circ\\text{C}$",
                        "$600^\\circ\\text{C}$",
                        "$300^\\circ\\text{C}$"
                    ],
                    "answer": "B",
                    "explanation": "In Kelvin: $T_1 = 27 + 273 = 300\\text{ K}$. Doubling volume doubles Kelvin temperature: $T_2 = 300 \\times 2 = 600\\text{ K}$. In Celsius: $t_2 = 600 - 273 = 327^\\circ\\text{C}$."
                }
            },
            {
                "page_number": 8,
                "page_title": "Key Takeaways: Charles's Law",
                "block_type": "summary",
                "component_type": "summary",
                "content": {
                    "text": "### Summary: Charles's Law\n- **The Rule**: Heating a gas makes it expand ($V \\propto T$ at constant pressure).\n- **The Equation**: $\\frac{V_1}{T_1} = \\frac{V_2}{T_2}$.\n- **Absolute Zero**: $-273^\\circ\\text{C} = 0\\text{ K}$ (zero molecular motion).\n- **Kelvin Conversion**: Always use $T\\text{ (K)} = t^\\circ\\text{C} + 273$."
                }
            }
        ]
    }

    # =========================================================================
    # LESSON 162: THE COMBINED GAS LAW
    # =========================================================================
    lessons_payload[162] = {
        "topic": topic_22,
        "title": "The Combined Gas Law and Standard Conditions (S.T.P. & R.T.P.)",
        "cards": [
            {
                "page_number": 1,
                "page_title": "The Master Gas Law",
                "block_type": "learning_goal",
                "component_type": "learning_goal",
                "content": {
                    "text": "By the end of this module, you will combine Boyle's and Charles's laws into one Master Gas Equation ($\\frac{P_1V_1}{T_1} = \\frac{P_2V_2}{T_2}$), understand standard reference conditions (s.t.p. and r.t.p.), and solve multi-variable gas problems."
                }
            },
            {
                "page_number": 1,
                "page_title": "When Both Pressure and Temperature Change",
                "block_type": "concept_explanation",
                "component_type": "concept_explanation",
                "content": {
                    "text": "In the real world, pressure and temperature often change at the same time. Consider a weather balloon launched in Nairobi:\n* As it rises into the upper atmosphere, outside pressure **drops** (which makes the balloon expand, per Boyle's Law).\n* But the high-altitude air is **freezing cold** (which makes the balloon shrink, per Charles's Law)!\n\nWhich effect wins? To calculate the true final volume, we combine both laws into a single unified equation: **The Combined Gas Law**."
                }
            },
            {
                "page_number": 2,
                "page_title": "Deriving the Master Gas Equation",
                "block_type": "concept_explanation",
                "component_type": "concept_explanation",
                "content": {
                    "text": "Combining our two gas proportionalities:\n1. $V \\propto \\frac{1}{P}$ (Boyle's Law)\n2. $V \\propto T$ (Charles's Law)\n\nYields the Master Gas Equation:\n$$\\mathbf{\\frac{P_1 V_1}{T_1} = \\frac{P_2 V_2}{T_2}}$$\n\n*Notice the beauty of this formula*:\n- If temperature is constant ($T_1 = T_2$), it becomes Boyle's Law: $P_1V_1 = P_2V_2$.\n- If pressure is constant ($P_1 = P_2$), it becomes Charles's Law: $\\frac{V_1}{T_1} = \\frac{V_2}{T_2}$."
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
                "page_title": "Standard Laboratory Conditions (In Plain English)",
                "block_type": "definition_card",
                "component_type": "definition_card",
                "content": {
                    "term": "Standard Gas Conditions",
                    "content": "### Why do chemists have standard conditions?\nBecause gas volume expands with heat and shrinks with pressure, stating \"I have $100\\text{ mL}$ of gas\" is meaningless unless you state the temperature and pressure! International science created two agreed benchmarks:\n\n---\n\n### 1. Standard Temperature & Pressure (s.t.p.)\n* **Temperature**: Freezing point of water ($0^\\circ\\text{C} = \\mathbf{273\\text{ K}}$)\n* **Pressure**: Normal sea-level atmospheric pressure ($1\\text{ atm} = \\mathbf{760\\text{ mmHg}} = \\mathbf{101325\\text{ Pa}}$)\n\n### 2. Room Temperature & Pressure (r.t.p.)\n* **Temperature**: Comfortable room temperature ($25^\\circ\\text{C} = \\mathbf{298\\text{ K}}$)\n* **Pressure**: Normal atmospheric pressure ($1\\text{ atm} = \\mathbf{760\\text{ mmHg}} = \\mathbf{101325\\text{ Pa}}$)"
                }
            },
            {
                "page_number": 4,
                "page_title": "Worked Example 1: Calculating Gas Volume at S.T.P.",
                "block_type": "worked_example",
                "component_type": "worked_example",
                "content": {
                    "problem": "A gas occupies $30.0\\text{ cm}^3$ at $27^\\circ\\text{C}$ and $740\\text{ mmHg}$ pressure. Calculate its volume at standard temperature and pressure (s.t.p.).",
                    "steps": [
                        "**1. What do we know? (Initial State Data)**\n- $P_1 = 740\\text{ mmHg}, V_1 = 30.0\\text{ cm}^3, T_1 = 27 + 273 = 300\\text{ K}$",
                        "**2. Conditions at s.t.p. (Final State Data)**\n- $P_2 = 760\\text{ mmHg}, T_2 = 273\\text{ K}, V_2 = \\text{Target Volume}$",
                        "**3. Apply the Combined Gas Law**:\n$$\\frac{P_1 V_1}{T_1} = \\frac{P_2 V_2}{T_2} \\quad \\implies \\quad V_2 = \\frac{P_1 V_1 T_2}{P_2 T_1}$$",
                        "**4. Calculate Step-by-Step**:\n$$V_2 = \\frac{740\\text{ mmHg} \\times 30.0\\text{ cm}^3 \\times 273\\text{ K}}{760\\text{ mmHg} \\times 300\\text{ K}} = \\frac{6060600}{228000} = 26.58\\text{ cm}^3$$",
                        "**5. Sanity Check**\n- Pressure increased slightly and temperature cooled down. Both compress the gas, reducing volume from $30.0\\text{ cm}^3$ to $26.58\\text{ cm}^3$."
                    ]
                }
            },
            {
                "page_number": 5,
                "page_title": "Worked Example 2: Determining Final Temperature Under Dual Changes",
                "block_type": "worked_example",
                "component_type": "worked_example",
                "content": {
                    "problem": "A gas occupies $100\\text{ cm}^3$ at $-15^\\circ\\text{C}$ and $650\\text{ mmHg}$. If allowed to expand to $150\\text{ cm}^3$ at $680\\text{ mmHg}$, find its final Celsius temperature.",
                    "steps": [
                        "**1. What do we know?**\n- $V_1 = 100\\text{ cm}^3, T_1 = -15 + 273 = 258\\text{ K}, P_1 = 650\\text{ mmHg}$\n- $V_2 = 150\\text{ cm}^3, P_2 = 680\\text{ mmHg}$",
                        "**2. Calculate $T_2$ in Kelvin**:\n$$T_2 = \\frac{P_2 V_2 T_1}{P_1 V_1} = \\frac{680 \\times 150 \\times 258}{650 \\times 100} = \\frac{26316000}{65000} = 404.86\\text{ K}$$",
                        "**3. Convert to Celsius**:\n$$t_2 = 404.86 - 273 = 131.86^\\circ\\text{C} \\approx 132^\\circ\\text{C}$$",
                        "**4. Conclusion**\n- The gas was heated vigorously from $-15^\\circ\\text{C}$ up to $+132^\\circ\\text{C}$."
                    ]
                }
            },
            {
                "page_number": 6,
                "page_title": "Think About This: High-Altitude Baking and Boiling",
                "block_type": "common_misconception",
                "component_type": "common_misconception",
                "content": {
                    "text": "### Why does water boil at only $95^\\circ\\text{C}$ in Nairobi?\nIn Nairobi ($1795\\text{ m}$ above sea level), the air column above us is thinner, so atmospheric pressure is lower ($630\\text{ mmHg}$ vs $760\\text{ mmHg}$ in Mombasa).\n\nBecause external pressure is lower, water molecules escape into steam at a lower temperature ($95^\\circ\\text{C}$). Cooking food takes longer in highlands because boiling water is cooler, which is why pressure cookers are so helpful!"
                }
            },
            {
                "page_number": 7,
                "page_title": "Practice Question 1: Combined Gas Law Calculation",
                "block_type": "knowledge_check",
                "component_type": "knowledge_check",
                "content": {
                    "check_type": "multiple_choice",
                    "question": "A cylinder holds $200\\text{ cm}^3$ of gas at $27^\\circ\\text{C}$ and $750\\text{ mmHg}$. If volume is compressed to $100\\text{ cm}^3$ while temperature is raised to $127^\\circ\\text{C}$, what is the new pressure?",
                    "options": [
                        "$1000\\text{ mmHg}$",
                        "$1500\\text{ mmHg}$",
                        "$2000\\text{ mmHg}$",
                        "$750\\text{ mmHg}$"
                    ],
                    "answer": "C",
                    "explanation": "$T_1 = 27 + 273 = 300\\text{ K}$, $T_2 = 127 + 273 = 400\\text{ K}$. $P_2 = \\frac{750 \\times 200 \\times 400}{100 \\times 300} = 2000\\text{ mmHg}$."
                }
            },
            {
                "page_number": 7,
                "page_title": "Practice Question 2: Values of STP",
                "block_type": "knowledge_check",
                "component_type": "knowledge_check",
                "content": {
                    "check_type": "multiple_choice",
                    "question": "What are the standard values for temperature and pressure at s.t.p. in Chemistry?",
                    "options": [
                        "$25^\\circ\\text{C}$ and $760\\text{ mmHg}$",
                        "$0^\\circ\\text{C}$ ($273\\text{ K}$) and $760\\text{ mmHg}$ ($101.3\\text{ kPa}$)",
                        "$100^\\circ\\text{C}$ and $1.0\\text{ atm}$",
                        "$0\\text{ K}$ and $101.3\\text{ kPa}$"
                    ],
                    "answer": "B",
                    "explanation": "Standard Temperature and Pressure (s.t.p.) is internationally defined as $0^\\circ\\text{C}$ ($273\\text{ K}$) and $1\\text{ atm}$ ($760\\text{ mmHg}$ or $101.3\\text{ kPa}$)."
                }
            },
            {
                "page_number": 8,
                "page_title": "Key Takeaways: Combined Gas Law",
                "block_type": "summary",
                "component_type": "summary",
                "content": {
                    "text": "### Summary: Combined Gas Law & Standard Conditions\n- **Combined Gas Law**: $\\frac{P_1V_1}{T_1} = \\frac{P_2V_2}{T_2}$.\n- **s.t.p.**: $0^\\circ\\text{C} = 273\\text{ K}$, $760\\text{ mmHg} = 101.3\\text{ kPa}$.\n- **r.t.p.**: $25^\\circ\\text{C} = 298\\text{ K}$, $760\\text{ mmHg} = 101.3\\text{ kPa}$."
                }
            }
        ]
    }

    # =========================================================================
    # LESSON 163: GRAHAM'S LAW OF DIFFUSION
    # =========================================================================
    lessons_payload[163] = {
        "topic": topic_22,
        "title": "Graham's Law of Diffusion and Kinetic Theory",
        "cards": [
            {
                "page_number": 1,
                "page_title": "Diffusion in Gases",
                "block_type": "learning_goal",
                "component_type": "learning_goal",
                "content": {
                    "text": "By the end of this module, you will understand Graham's Law of Diffusion in plain English, explain why lighter gas particles move faster than heavy ones ($E_k = \\frac{1}{2}mv^2$), and solve diffusion rate and time calculations."
                }
            },
            {
                "page_number": 1,
                "page_title": "The Spreading Scent of Perfume",
                "block_type": "concept_explanation",
                "component_type": "concept_explanation",
                "content": {
                    "text": "If someone opens a bottle of perfume in the front row of a classroom, students nearby smell it in seconds, and soon the scent reaches the very back.\n\nThis natural spreading of gas particles from where they are crowded to where they are scarce is called **Diffusion**.\n\nDo all gases diffuse at the exact same speed? If we release lightweight ammonia gas ($\\text{NH}_3$) and heavy hydrogen chloride gas ($\\text{HCl}$) at opposite ends of a glass tube, which gas wins the race? Today we discover **Graham's Law of Diffusion**!"
                }
            },
            {
                "page_number": 2,
                "page_title": "The Sprinter vs The Sumo Wrestler Analogy",
                "block_type": "concept_explanation",
                "component_type": "concept_explanation",
                "content": {
                    "text": "At the same room temperature, all gas particles have the **exact same kinetic energy** ($E_k$):\n$$E_k = \\frac{1}{2} m v^2$$\nWhere $m$ is mass and $v$ is velocity.\n\n* **The Physical Intuition**:\n  Think of a lightweight sprinter and a heavy sumo wrestler given the exact same push of energy. To have the same kinetic energy, the lightweight sprinter **must run much faster** than the heavy wrestler!\n\nTherefore, **lighter gas molecules zip through the air much faster than heavy, sluggish molecules**!"
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
                "page_title": "Graham's Law Formulas (In Plain English)",
                "block_type": "definition_card",
                "component_type": "definition_card",
                "content": {
                    "term": "Graham's Law of Diffusion",
                    "content": "### What is Graham's Law?\n*Light gases diffuse fast; heavy gases diffuse slowly. Specifically, diffusion speed is inversely proportional to the square root of molecular weight ($M_r$).*\n\n---\n\n### 1. Comparing Diffusion Rates ($R$):\n$$\\mathbf{\\frac{R_1}{R_2} = \\sqrt{\\frac{M_2}{M_1}}}$$\n*(Notice: Gas 1 is on top on the left, but its molecular mass $M_1$ is on the bottom inside the square root because lighter means faster!)*\n\n### 2. Comparing Diffusion Times ($t$):\nBecause a faster gas takes **less time** to travel the distance, the time ratio flips:\n$$\\mathbf{\\frac{t_2}{t_1} = \\sqrt{\\frac{M_2}{M_1}} = \\frac{R_1}{R_2}}$$"
                }
            },
            {
                "page_number": 4,
                "page_title": "Worked Example 1: Finding Molecular Mass from Diffusion Time",
                "block_type": "worked_example",
                "component_type": "worked_example",
                "content": {
                    "problem": "$100\\text{ cm}^3$ of oxygen gas ($\\text{O}_2$) takes $125\\text{ seconds}$ to diffuse through a plug. Under identical conditions, $100\\text{ cm}^3$ of unknown gas $X$ takes $100\\text{ seconds}$. Find the Relative Molecular Mass ($M_r$) of gas $X$. ($A_r$: $\\text{O}=16.0$).",
                    "steps": [
                        "**1. What do we know?**\n- Oxygen ($\\text{O}_2$): $M_1 = 32.0\\text{ g/mol}, t_1 = 125\\text{ s}$\n- Gas $X$: $M_2 = \\text{Target } M_r, t_2 = 100\\text{ s}$",
                        "**2. Apply Time Formula**:\n$$\\frac{t_2}{t_1} = \\sqrt{\\frac{M_2}{M_1}} \\implies \\frac{100}{125} = \\sqrt{\\frac{M_2}{32.0}}$$\n$$0.8 = \\sqrt{\\frac{M_2}{32.0}}$$",
                        "**3. Square both sides**:\n$$(0.8)^2 = \\frac{M_2}{32.0} \\implies 0.64 = \\frac{M_2}{32.0}$$\n$$M_2 = 0.64 \\times 32.0 = 20.48$$",
                        "**4. Sanity Check**\n- Gas $X$ took less time ($100\\text{ s}$ vs $125\\text{ s}$), so it is lighter than oxygen ($M_r = 20.48 < 32.0$)."
                    ]
                }
            },
            {
                "page_number": 5,
                "page_title": "Worked Example 2: Calculating Relative Rates of Diffusion",
                "block_type": "worked_example",
                "component_type": "worked_example",
                "content": {
                    "problem": "Ammonia ($\\text{NH}_3$) traveled $12.0\\text{ cm}$ in $5.0\\text{ min}$, while hydrogen chloride ($\\text{HCl}$) traveled $8.0\\text{ cm}$ in the same time. (a) Calculate the diffusion rate of each gas. (b) Compare the ratio of rates to the theoretical Graham's Law value. ($A_r$: $\\text{N}=14.0, \\text{H}=1.0, \\text{Cl}=35.5$).",
                    "steps": [
                        "**1. Step 1: Calculate Experimental Rates ($R = \\frac{\\text{Distance}}{\\text{Time}}$)**\n- Rate of $\\text{NH}_3$: $R_1 = \\frac{12.0\\text{ cm}}{5.0\\text{ min}} = 2.4\\text{ cm/min}$\n- Rate of $\\text{HCl}$: $R_2 = \\frac{8.0\\text{ cm}}{5.0\\text{ min}} = 1.6\\text{ cm/min}$",
                        "**2. Step 2: Experimental Rate Ratio**\n$$\\frac{R_{\\text{NH}_3}}{R_{\\text{HCl}}} = \\frac{2.4}{1.6} = 1.50$$",
                        "**3. Step 3: Theoretical Ratio from Molecular Masses**\n- $M_r(\\text{NH}_3) = 17.0, M_r(\\text{HCl}) = 36.5$\n$$\\text{Theoretical Ratio} = \\sqrt{\\frac{36.5}{17.0}} = \\sqrt{2.147} = 1.47$$",
                        "**4. Conclusion**\n- The experimental ratio ($1.50$) matches the theoretical prediction ($1.47$), proving ammonia moves $1.5\\text{ times}$ faster than $\\text{HCl}$."
                    ]
                }
            },
            {
                "page_number": 6,
                "page_title": "Think About This: Why Perfume Takes Time Across a Room",
                "block_type": "common_misconception",
                "component_type": "common_misconception",
                "content": {
                    "text": "### If gas molecules travel at $500\\text{ m/s}$, why doesn't perfume cross the room instantly?\nIn a vacuum, it would! But a room is crowded with air molecules. A perfume molecule collides over **5 billion times every second**, bouncing in a chaotic zig-zag random walk that slows down its forward trip across the room."
                }
            },
            {
                "page_number": 7,
                "page_title": "Practice Question 1: Who Diffuses Fastest?",
                "block_type": "knowledge_check",
                "component_type": "knowledge_check",
                "content": {
                    "check_type": "multiple_choice",
                    "question": "Which of the following gases will diffuse fastest through a porous partition under identical conditions? ($A_r$: $\\text{H}=1, \\text{He}=4, \\text{C}=12, \\text{N}=14, \\text{O}=16, \\text{S}=32$).",
                    "options": [
                        "Carbon dioxide ($\\text{CO}_2, M_r=44$)",
                        "Helium ($\\text{He}, M_r=4$)",
                        "Methane ($\\text{CH}_4, M_r=16$)",
                        "Sulfur dioxide ($\\text{SO}_2, M_r=64$)"
                    ],
                    "answer": "B",
                    "explanation": "Helium has the lowest molecular mass ($M_r = 4$) and therefore travels at the highest velocity, diffusing the fastest."
                }
            },
            {
                "page_number": 7,
                "page_title": "Practice Question 2: Comparing Methane and SO2",
                "block_type": "knowledge_check",
                "component_type": "knowledge_check",
                "content": {
                    "check_type": "multiple_choice",
                    "question": "How many times faster will methane gas ($\\text{CH}_4, M_r = 16$) diffuse compared to sulfur dioxide gas ($\\text{SO}_2, M_r = 64$)?",
                    "options": [
                        "2 times faster",
                        "4 times faster",
                        "16 times faster",
                        "0.5 times as fast"
                    ],
                    "answer": "A",
                    "explanation": "Applying Graham's Law: $\\frac{R_{\\text{CH}_4}}{R_{\\text{SO}_2}} = \\sqrt{\\frac{64}{16}} = \\sqrt{4} = 2$. Methane diffuses exactly twice as fast."
                }
            },
            {
                "page_number": 8,
                "page_title": "Key Takeaways: Graham's Law",
                "block_type": "summary",
                "component_type": "summary",
                "content": {
                    "text": "### Summary: Graham's Law\n- **Principle**: Lighter gas molecules move faster than heavy ones ($R \\propto \\frac{1}{\\sqrt{M_r}}$).\n- **Formulas**: $\\frac{R_1}{R_2} = \\sqrt{\\frac{M_2}{M_1}} = \\frac{t_2}{t_1}$."
                }
            }
        ]
    }

    # =========================================================================
    # LESSON 169: MOLAR GAS VOLUME OVERHAUL (The exact card flagged by user)
    # =========================================================================
    lessons_payload[169] = {
        "topic": topic_23,
        "title": "Stoichiometry of Chemical Equations (Reacting Masses and Volumes)",
        "cards": [
            {
                "page_number": 1,
                "page_title": "Chemical Recipes & Stoichiometry",
                "block_type": "learning_goal",
                "component_type": "learning_goal",
                "content": {
                    "text": "By the end of this module, you will read balanced chemical equations as nature's exact recipe ratios, understand the physical size of Molar Gas Volume ($22.4\\text{ dm}^3$ at s.t.p. and $24.0\\text{ dm}^3$ at r.t.p.), and calculate reacting gas volumes with confidence."
                }
            },
            {
                "page_number": 1,
                "page_title": "Nature's Perfect Recipes",
                "block_type": "concept_explanation",
                "component_type": "concept_explanation",
                "content": {
                    "text": "When baking mandazis or a cake, you must follow an exact recipe: 2 cups of flour + 1 cup of milk + 2 eggs. If you add too much flour, the dough is ruined!\n\nChemical reactions follow nature's exact quantitative recipes. A balanced chemical equation tells us the precise recipe ratio in which atoms and molecules combine. In Chemistry, the study of these quantitative mass and volume relationships is called **Stoichiometry**."
                }
            },
            {
                "page_number": 2,
                "page_title": "Reading a Chemical Equation Like a Recipe",
                "block_type": "concept_explanation",
                "component_type": "concept_explanation",
                "content": {
                    "text": "Consider the combustion of methane gas:\n$$\\mathbf{1\\text{CH}_{4(g)} + 2\\text{O}_{2(g)} \\rightarrow 1\\text{CO}_{2(g)} + 2\\text{H}_2\\text{O}_{(l)}}$$\n\nLook at the numbers (coefficients) in front of each formula:\n* **Mole Recipe Ratio**: $1\\text{ mole of } \\text{CH}_4$ needs **$2\\text{ moles of } \\text{O}_2$** to make **$1\\text{ mole of } \\text{CO}_2$** and **$2\\text{ moles of } \\text{H}_2\\text{O}$**.\n* **Mass Check**: $16.0\\text{ g of } \\text{CH}_4 + 64.0\\text{ g of } \\text{O}_2 = 80.0\\text{ g of reactants} \\rightarrow 44.0\\text{ g of } \\text{CO}_2 + 36.0\\text{ g of } \\text{H}_2\\text{O} = 80.0\\text{ g of products}$. Mass is completely conserved!"
                }
            },
            {
                "page_number": 2,
                "page_title": "Diagram: Molar Gas Volume Reference Cubes",
                "block_type": "suggested_diagram",
                "component_type": "suggested_diagram",
                "content": {
                    "prompt": "Diagram showing 1 mole of any gas (Helium, Oxygen, Carbon Dioxide) occupying a cube of 22.4 dm3 at s.t.p. and a cube of 24.0 dm3 at r.t.p., with a 20L water jerrican shown alongside for real-world size comparison.",
                    "caption": "Avogadro's Gas Law: 1 mole of ANY gas occupies 22.4 dm3 at s.t.p. and 24.0 dm3 at r.t.p. (roughly the size of a large 20L water jerrican plus a kettle)."
                },
                "asset_info": {
                    "title": "Molar Gas Volume Comparison Diagram",
                    "description": "Visual comparison of 1 mole of gas occupying 22.4L at s.t.p. and 24.0L at r.t.p. against everyday container volumes.",
                    "ai_instruction": "Create an illustration comparing two transparent gas cubes labeled 22.4 dm3 (s.t.p., 0°C) and 24.0 dm3 (r.t.p., 25°C) holding 1 mole of gas alongside a familiar 20-litre water container."
                }
            },
            {
                "page_number": 3,
                "page_title": "Molar Gas Volume (In Plain English)",
                "block_type": "definition_card",
                "component_type": "definition_card",
                "content": {
                    "term": "Molar Gas Volume",
                    "content": "### What is Molar Gas Volume ($V_m$)?\n*Imagine an invisible universal container. If you fill it with **exactly 1 mole of ANY gas** on Earth, this is the exact volume it takes up!*\n\n---\n\n### The Two Standard Volume Benchmarks:\n1. **At Standard Temperature & Pressure (s.t.p., $0^\\circ\\text{C}$)**:\n   $$\\mathbf{V_m = 22.4\\text{ dm}^3\\text{ (or } 22400\\text{ cm}^3\\text{)}}$$\n\n2. **At Room Temperature & Pressure (r.t.p., $25^\\circ\\text{C}$)**:\n   $$\\mathbf{V_m = 24.0\\text{ dm}^3\\text{ (or } 24000\\text{ cm}^3\\text{)}}$$\n   *(Real-world picture: $24\\text{ dm}^3$ is roughly the size of a standard **$20\\text{-litre}$ water jerrican plus a $4\\text{-litre}$ kettle**!)*\n\n---\n\n### How to Use the Gas Formulas in Lab Math:\n\n* **If you know the Moles $\\rightarrow$ Find the Gas Volume**:\n  $$\\mathbf{\\text{Volume } (V) = \\text{Moles } (n) \\times V_m}$$\n  *(Multiply moles by $22.4$ at s.t.p. or by $24.0$ at r.t.p.)*\n\n* **If you measured the Gas Volume in a syringe $\\rightarrow$ Find the Moles**:\n  $$\\mathbf{\\text{Moles } (n) = \\frac{\\text{Volume in dm}^3}{V_m}}$$\n  *(Divide the volume by $22.4$ at s.t.p. or by $24.0$ at r.t.p.)*"
                }
            },
            {
                "page_number": 4,
                "page_title": "Worked Example: Reacting Mass & Gas Volume",
                "block_type": "worked_example",
                "component_type": "worked_example",
                "content": {
                    "problem": "Calculate the volume of carbon dioxide gas ($\\text{CO}_2$) produced at r.t.p. when $10.0\\text{ g}$ of pure calcium carbonate ($\\text{CaCO}_3$) reacts with excess dilute hydrochloric acid.\n$$\\text{CaCO}_{3(s)} + 2\\text{HCl}_{(aq)} \\rightarrow \\text{CaCl}_{2(aq)} + \\text{H}_2\\text{O}_{(l)} + \\text{CO}_{2(g)}$$\n(Given $A_r$: $\\text{Ca}=40.0, \\text{C}=12.0, \\text{O}=16.0$; $V_m$ at r.t.p. = $24.0\\text{ dm}^3\\text{/mol}$).",
                    "steps": [
                        "**1. Step 1: Find Moles of the Given Reactant ($\\text{CaCO}_3$)**\n- Molar mass of $\\text{CaCO}_3 = 40.0 + 12.0 + 3(16.0) = 100.0\\text{ g/mol}$\n$$n = \\frac{10.0\\text{ g}}{100.0\\text{ g/mol}} = 0.10\\text{ moles of } \\text{CaCO}_3$$",
                        "**2. Step 2: Use the Equation Mole Ratio**\n- Equation shows: $1\\text{ mole of } \\text{CaCO}_3 \\rightarrow 1\\text{ mole of } \\text{CO}_2$\n$$\\implies n(\\text{CO}_2) = 0.10\\text{ moles of } \\text{CO}_2$$",
                        "**3. Step 3: Convert Moles to Gas Volume at r.t.p.**\n$$V(\\text{CO}_2) = n \\times V_m = 0.10\\text{ mol} \\times 24.0\\text{ dm}^3\\text{/mol} = 2.40\\text{ dm}^3$$\n$$V = 2.40 \\times 1000 = 2400\\text{ cm}^3$$\n- **Result**: Exactly $2.40\\text{ dm}^3$ ($2400\\text{ cm}^3$) of $\\text{CO}_2$ gas is collected."
                    ]
                }
            },
            {
                "page_number": 5,
                "page_title": "Think About This: Why All Gases Have the Same Volume",
                "block_type": "common_misconception",
                "component_type": "common_misconception",
                "content": {
                    "text": "### Why does 1 mole of heavy CO2 (44g) fill the same volume as 1 mole of light H2 (2g)?\nIn a gas, molecules are separated by massive empty spaces. The physical size of the actual molecule is negligible.\n\nThink of 100 flying bees spaced 10 meters apart versus 100 flying birds spaced 10 meters apart—both flocks occupy the exact same cloud volume! At the same temperature and pressure, volume depends strictly on the **count of particles ($6.022 \\times 10^{23}$)**, not their weight."
                }
            },
            {
                "page_number": 6,
                "page_title": "Practice Question 1: Hydrogen Gas at STP",
                "block_type": "knowledge_check",
                "component_type": "knowledge_check",
                "content": {
                    "check_type": "multiple_choice",
                    "question": "What volume of hydrogen gas at s.t.p. is liberated when $2.4\\text{ g}$ of magnesium reacts completely with excess dilute hydrochloric acid? ($A_r$: $\\text{Mg}=24.0, V_m = 22.4\\text{ dm}^3\\text{/mol}$).\n$$\\text{Mg} + 2\\text{HCl} \\rightarrow \\text{MgCl}_2 + \\text{H}_2$$",
                    "options": [
                        "$2.24\\text{ dm}^3$",
                        "$22.4\\text{ dm}^3$",
                        "$4.48\\text{ dm}^3$",
                        "$1.12\\text{ dm}^3$"
                    ],
                    "answer": "A",
                    "explanation": "Moles of $\\text{Mg} = \\frac{2.4}{24.0} = 0.10\\text{ mol}$. Mole ratio $\\text{Mg} : \\text{H}_2 = 1 : 1 \\implies 0.10\\text{ mol } \\text{H}_2$. Volume at s.t.p. $= 0.10\\text{ mol} \\times 22.4\\text{ dm}^3\\text{/mol} = 2.24\\text{ dm}^3$."
                }
            },
            {
                "page_number": 6,
                "page_title": "Practice Question 2: Gay-Lussac Combining Volumes",
                "block_type": "knowledge_check",
                "component_type": "knowledge_check",
                "content": {
                    "check_type": "multiple_choice",
                    "question": "What volume of oxygen gas is needed for complete combustion of $40.0\\text{ cm}^3$ of propane ($\\text{C}_3\\text{H}_8$) at constant temperature and pressure?\n$$\\text{C}_3\\text{H}_{8(g)} + 5\\text{O}_{2(g)} \\rightarrow 3\\text{CO}_{2(g)} + 4\\text{H}_2\\text{O}_{(l)}$$",
                    "options": [
                        "$40.0\\text{ cm}^3$",
                        "$120.0\\text{ cm}^3$",
                        "$200.0\\text{ cm}^3$",
                        "$8.0\\text{ cm}^3$"
                    ],
                    "answer": "C",
                    "explanation": "By Gay-Lussac's Law, gas volume ratio matches equation coefficients: $\\text{C}_3\\text{H}_8 : \\text{O}_2 = 1 : 5$. Volume of $\\text{O}_2 = 5 \\times 40.0\\text{ cm}^3 = 200.0\\text{ cm}^3$."
                }
            },
            {
                "page_number": 7,
                "page_title": "Key Takeaways: Stoichiometry",
                "block_type": "summary",
                "component_type": "summary",
                "content": {
                    "text": "### Summary: Stoichiometry\n- **Mole Ratio**: Read directly from balanced equation coefficients.\n- **Molar Gas Volumes**: $1\\text{ mole} = 22.4\\text{ dm}^3$ at s.t.p.; $24.0\\text{ dm}^3$ at r.t.p.\n- **3-Step Workflow**: Known Grams $\\rightarrow$ Moles of Known $\\rightarrow$ Target Moles (Mole Ratio) $\\rightarrow$ Target Grams or Gas Volume."
                }
            }
        ]
    }

    # Execute update for Lessons 161, 162, 163, 169
    for lesson_id, data in lessons_payload.items():
        try:
            lesson = Lesson.objects.get(id=lesson_id)
            print(f"Humanizing Lesson {lesson.id}: \"{lesson.title}\" in {data['topic'].name}...")
            
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
            print(f"  Refactored Lesson {lesson.id} successfully.")
        except Lesson.DoesNotExist:
            print(f"Lesson {lesson_id} not found!")

if __name__ == "__main__":
    run_comprehensive_humanization()
