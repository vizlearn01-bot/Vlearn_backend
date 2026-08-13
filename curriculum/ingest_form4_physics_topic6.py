"""
VLearn Form 4 Physics — Topic 6: Mains Electricity
Ingestion Script

Grade: Form 4
Subject: Physics
Curriculum: 844 (Kenyan 8-4-4 Secondary Curriculum)

Pedagogical Architecture:
  3 Learning Units / Modules:
  - Module 6.1: Grid Supply, High-Voltage Transmission, and Substation Distribution (12 pages)
  - Module 6.2: Electrical Power, Energy Consumption, and Utility Billing Costing (13 pages)
  - Module 6.3: Domestic Circuit Wiring, Fuses, Earthing, and Electrical Safety (13 pages)

Features:
  - Adaptive 8-step analytical problem-solving framework
  - Multi-tier worked examples (Levels 1 to 5)
  - Full laboratory experimental protocols (Low-voltage transmission model & meter reading)
  - Real-world engineering systems (National grid, ring main circuit, utility billing, BS 1363 plugs)
  - Purposeful interactions (prediction, simulation sandbox, reflections, knowledge checks)
  - Clean student-facing titles and zero developer terminology leaks
  - Idempotent safe updates (preserves enriched assets on rerun)

Usage:
  /home/jason-bitega/Desktop/VL/vlearn_repositories/Vlearn_backend/venv/bin/python curriculum/ingest_form4_physics_topic6.py
  Optional flag: --replace
"""

import os
import sys
import uuid
import re
import argparse
import django

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "Nexus_backend.settings")
django.setup()

from django.db import transaction
from curriculum.models import (
    Curriculum, Grade, Subject, Topic,
    LearningUnit, Lesson, LessonBlock, LessonAsset
)

def clean_text(raw_str):
    """Remove source citation brackets like [89], [90], [image_0] and clean whitespace."""
    if not isinstance(raw_str, str):
        return raw_str
    cleaned = re.sub(r'\[(?:\d+|image_\d+|[\d,\s]+)\]', '', raw_str)
    cleaned = re.sub(r'[ \t]+', ' ', cleaned)
    return cleaned.strip()

def clean_content_dict(data):
    """Recursively clean text within content dicts or lists."""
    if isinstance(data, str):
        return clean_text(data)
    elif isinstance(data, list):
        return [clean_content_dict(item) for item in data]
    elif isinstance(data, dict):
        return {k: clean_content_dict(v) for k, v in data.items()}
    return data


# =============================================================================
# MODULE 6.1 DATA — Grid Supply, Transmission & Substation Distribution
# =============================================================================
MODULE_6_1 = {
    "unit_name": "Module 6.1: Grid Supply, High-Voltage Transmission, and Substation Distribution",
    "unit_order": 1,
    "lesson_title": "Grid Supply, High-Voltage Transmission, and Substation Distribution",
    "cards": [
        # Page 1: Hook & Goals
        {
            "page_number": 1,
            "page_title": "From Power Stations to Your Wall Socket",
            "block_type": "learning_goal",
            "component_type": "learning_goal",
            "content": {
                "text": (
                    "Where does the electricity in your home come from? "
                    "In Kenya, electricity is generated at power stations—such as hydroelectric dams along the Tana River, "
                    "geothermal plants at Olkaria, or wind farms at Lake Turkana—generating voltage at $25\\text{ kV}$. "
                    "How does this energy travel hundreds of kilometers across the country to power a tiny $240\\text{ V}$ phone charger without melting cables?\n\n"
                    "By the end of this lesson, you will be able to:\n"
                    "- Explain the physical necessity of stepping up voltage for long-distance grid transmission\n"
                    "- Prove mathematically why high voltage minimizes $I^2R$ power line heat losses ($P_{\\text{loss}} \\propto \\frac{1}{V^2}$)\n"
                    "- Trace the substation voltage drop chain ($400\\text{ kV} \\rightarrow 132\\text{ kV} \\rightarrow 33\\text{ kV} \\rightarrow 11\\text{ kV} \\rightarrow 240\\text{ V}$)\n"
                    "- Identify the roles, insulation colors, and voltage potentials of Live (Phase), Neutral, and Earth conductors"
                )
            }
        },
        # Page 2: High-Voltage Transmission Physics
        {
            "page_number": 2,
            "page_title": "High-Voltage Transmission Physics",
            "block_type": "concept_explanation",
            "component_type": "concept_explanation",
            "content": {
                "text": (
                    "### The $I^2R$ Heat Loss Problem:\n"
                    "Long-distance transmission wires have a fixed electrical resistance ($R_{\\text{line}}$). "
                    "When current $I$ flows through these cables, electrical power is converted into heat at the rate:\n\n"
                    "$$P_{\\text{loss}} = I^2 \\cdot R_{\\text{line}}$$\n\n"
                    "Since the transmitted power is $P = V \\cdot I$, the current flowing through the line is:\n\n"
                    "$$I = \\frac{P}{V} \\qquad \\implies \\qquad \\mathbf{P_{\\text{loss}} = \\left(\\frac{P}{V}\\right)^2 \\cdot R_{\\text{line}} = \\frac{P^2 \\cdot R_{\\text{line}}}{V^2}}$$\n\n"
                    "### The Mathematical Insight:\n"
                    "- Heat loss is **inversely proportional to the square of transmission voltage ($V^2$)**!\n"
                    "- Stepping up transmission voltage by a factor of $10\\times$ drops current by $10\\times$, which reduces line heat losses by **$100\\times$** ($10^2$).\n"
                    "- Stepping up voltage to $400\\text{ kV}$ reduces line losses by **$10,000\\times$** compared to transmitting at low voltage!"
                )
            }
        },
        {
            "page_number": 2,
            "page_title": "Transmission Voltage vs I^2R Line Loss Derivation",
            "block_type": "suggested_diagram",
            "component_type": "suggested_diagram",
            "content": {
                "text": "Mathematical derivation diagram showing how stepping up transmission voltage V drops current I = P/V and reduces P_loss = I^2 R by the square of voltage.",
                "instruction": (
                    "Draw formula derivation flowchart: P = V * I -> I = P / V -> P_loss = I^2 * R = (P/V)^2 * R = P^2 * R / V^2. "
                    "Show callout comparing 2.4 kV vs 24 kV line losses."
                )
            }
        },
        # Page 3: Substation Voltage Drop Chain
        {
            "page_number": 3,
            "page_title": "The National Grid Substation Voltage Drop Chain",
            "block_type": "step_process",
            "component_type": "step_process",
            "content": {
                "title": "Grid Power Distribution Sequence",
                "steps": [
                    "**1. Power Generation (25 kV):** Alternators at hydro, geothermal, or wind stations generate 3-phase A.C. electricity at $25\\text{ kV}$.",
                    "**2. Grid Step-Up Substation (132 kV – 400 kV):** Step-up transformers raise voltage to $132\\text{ kV}, 220\\text{ kV},$ or $400\\text{ kV}$ for long-distance pylon grid transmission.",
                    "**3. Primary Substation (132 kV to 33 kV):** Near regional towns, step-down transformers reduce voltage to $33\\text{ kV}$ for heavy industrial factories.",
                    "**4. Secondary Substation (33 kV to 11 kV):** Step-down transformers lower voltage to $11\\text{ kV}$ for light commercial areas and institutional campuses.",
                    "**5. Local Pole Transformer (11 kV to 240 V):** Neighbourhood step-down transformers lower voltage to $240\\text{ V}$ single-phase A.C. for domestic homes."
                ]
            }
        },
        {
            "page_number": 3,
            "page_title": "National Substation Distribution Sequence Diagram",
            "block_type": "suggested_diagram",
            "component_type": "suggested_diagram",
            "content": {
                "text": "Block diagram of national grid distribution showing step-up transformer at generator, pylon lines, primary substation, secondary substation, and local 240 V pole transformer.",
                "instruction": (
                    "Draw 5 sequential stages from Power Station (25 kV) -> Step-Up (400 kV) -> Primary Substation (33 kV) -> Secondary Substation (11 kV) -> Consumer Pole Transformer (240 V). "
                    "Label transformer step-up and step-down ratios."
                )
            }
        },
        # Page 4: Three-Wire Conductor System
        {
            "page_number": 4,
            "page_title": "The Three-Wire Service Cable Conductors",
            "block_type": "comparison_table",
            "component_type": "comparison_table",
            "content": {
                "headers": ["Conductor Name", "Standard International Color Code", "Voltage Potential Relative to Earth", "Primary Function"],
                "rows": [
                    ["Live (Phase) Wire", "Brown", "240 V A.C. (Oscillates +340 V to -340 V)", "Carries current from the local transformer to the appliance"],
                    ["Neutral Wire", "Blue", "0 V (Grounded at local substation)", "Completes the circuit, providing the return path for current"],
                    ["Earth (Ground) Wire", "Green with Yellow stripes", "0 V (Connected to metal earth rod in ground)", "Protective safety wire; channels fault currents safely to ground"]
                ]
            }
        },
        # Page 5: Laboratory Low-Voltage Transmission Model
        {
            "page_number": 5,
            "page_title": "Laboratory Investigation: Low-Voltage Transmission Model",
            "block_type": "concept_explanation",
            "component_type": "concept_explanation",
            "content": {
                "text": (
                    "### Simulating Grid Efficiency in the Lab:\n"
                    "In a classroom laboratory, we model national grid transmission using a low-voltage A.C. supply ($12\\text{ V}$), "
                    "two identical transformers ($1:10$ step-up and $10:1$ step-down), thin resistance wires ($10\\ \\Omega$ total line resistance), and a $12\\text{ V}$ lamp.\n\n"
                    "**Scenario A (Direct Transmission at 12 V):**\n"
                    "Connecting the $12\\text{ V}$ supply directly through the resistance wires causes the lamp to glow very dimly or not at all. "
                    "Most voltage is lost across the line resistance ($I^2R$ heat loss).\n\n"
                    "**Scenario B (Stepped-Up Transmission at 120 V):**\n"
                    "Using a step-up transformer ($12\\text{ V} \\rightarrow 120\\text{ V}$) before the line wires and a step-down transformer ($120\\text{ V} \\rightarrow 12\\text{ V}$) at the lamp causes the lamp to shine at full brightness! "
                    "Current in the long lines drops by $10\\times$, reducing line loss by $100\\times$!"
                )
            }
        },
        {
            "page_number": 5,
            "page_title": "Laboratory Low-Voltage Transmission Model Schematic",
            "block_type": "suggested_diagram",
            "component_type": "suggested_diagram",
            "content": {
                "text": "Laboratory schematic showing 12V AC power supply, 1:10 step-up transformer, thin long resistance lines, 10:1 step-down transformer, and 12V bulb.",
                "instruction": (
                    "Draw 12V AC supply connected to 1:10 step-up transformer. "
                    "Draw long resistance wires (labeled 10 ohms). "
                    "Draw 10:1 step-down transformer connected to bright 12V lamp."
                )
            }
        },
        # Page 6: Common Misconceptions (Neutral vs Earth)
        {
            "page_number": 6,
            "page_title": "Neutral Wire vs. Earth Wire",
            "block_type": "common_misconception",
            "component_type": "common_misconception",
            "content": {
                "text": (
                    "### Neutral vs. Earth: Understanding the Difference\n"
                    "**The Misconception**: Neutral and Earth wires are identical because both operate at $0\\text{ V}$ potential.\n\n"
                    "**The Physics Reality**:\n"
                    "1. **The Neutral Wire (Blue)** is an active current-carrying conductor! During normal appliance operation, the full operating current flows through the Neutral wire back to the substation.\n"
                    "2. **The Earth Wire (Green/Yellow)** carries **ZERO current during normal operation**! It is purely a safety ground path connected to the appliance metal casing. It only carries current during a fault (e.g., when a loose Live wire touches the metal casing)."
                )
            }
        },
        # Page 7: Interactive Grid Sandbox
        {
            "page_number": 7,
            "page_title": "Interactive Exploration: Grid Transmission Sandbox",
            "block_type": "prediction",
            "component_type": "prediction",
            "content": {
                "text": (
                    "**Think & Predict Before Simulating:**\n\n"
                    "A power station transmits $100\\text{ kW}$ over a line of resistance $5.0\\ \\Omega$:\n"
                    "1. If transmission voltage is increased from $10\\text{ kV}$ to $100\\text{ kV}$, how many times does line current drop?\n"
                    "2. By what percentage does total power loss along the wires decrease?"
                )
            }
        },
        {
            "page_number": 7,
            "page_title": "Interactive Grid Transmission Sandbox",
            "block_type": "suggested_simulation",
            "component_type": "suggested_simulation",
            "content": {
                "text": "Interactive transmission line simulation allowing students to vary transmitted power P, line resistance R, and step-up voltage V while observing live current I, line loss P_loss, and efficiency percentage.",
                "instruction": "Simulation Key: grid_transmission_sandbox. Real-time rendering of line loss and voltage drops."
            }
        },
        {
            "page_number": 7,
            "page_title": "Reflecting on Transmission Voltage Efficiency",
            "block_type": "reflection",
            "component_type": "reflection",
            "content": {
                "text": (
                    "Increasing transmission voltage by 10x drops current by 10x (from 10A to 1A). "
                    "Since power loss P_loss = I^2 R depends on current squared, line loss drops by 100x (from 500W to 5W), reducing wasted energy by 99%!"
                )
            }
        },
        # Page 8: Knowledge Check (MCQ)
        {
            "page_number": 8,
            "page_title": "Check Your Understanding: High-Voltage Transmission",
            "block_type": "knowledge_check",
            "component_type": "knowledge_check",
            "content": {
                "check_type": "multiple_choice",
                "question": "Why is electrical power transmitted over long distance grid lines at extremely high voltages (up to 400 kV)?",
                "options": [
                    "To reduce current I, which drastically minimizes I^2R heat losses along the transmission lines",
                    "To increase the speed at which electrons travel through the wires",
                    "To make the electricity safer for domestic home appliances",
                    "To prevent transformers from overheating"
                ],
                "answer": "A",
                "explanation": (
                    "Transmitting power P = VI at high voltage V reduces current I proportionally. Because heat loss P_loss = I^2 R depends on current squared, lower current drastically minimizes wasted heat."
                )
            }
        },
        # Page 9: Knowledge Check (MCQ)
        {
            "page_number": 9,
            "page_title": "Check Your Understanding: Conductor Insulation Colors",
            "block_type": "knowledge_check",
            "component_type": "knowledge_check",
            "content": {
                "check_type": "multiple_choice",
                "question": "Which conductor wire in standard domestic wiring carries current at a potential of 240 V relative to Earth and is color-coded Brown?",
                "options": [
                    "Live (Phase) Wire",
                    "Neutral Wire",
                    "Earth Wire",
                    "Fuse Wire"
                ],
                "answer": "A",
                "explanation": (
                    "The Live (Phase) wire carries current from the local transformer at 240 V relative to Earth and is color-coded Brown under international IEC standards."
                )
            }
        },
        # Page 10: Summary & Key Takeaways
        {
            "page_number": 10,
            "page_title": "Module 6.1 Summary: Grid Supply & Distribution",
            "block_type": "summary",
            "component_type": "summary",
            "content": {
                "text": (
                    "### Key Grid Principles:\n"
                    "- **Generation**: Power stations generate 3-phase A.C. at $25\\text{ kV}$.\n"
                    "- **Stepping Up**: Voltage raised to $400\\text{ kV}$ to drop current $I$ and minimize $I^2R$ heat loss ($P_{\\text{loss}} \\propto 1/V^2$).\n"
                    "- **Substation Drop**: $400\\text{ kV} \\rightarrow 132\\text{ kV} \\rightarrow 33\\text{ kV} \\rightarrow 11\\text{ kV} \\rightarrow 240\\text{ V}$.\n"
                    "- **Three Conductors**: Live (Brown, $240\\text{ V}$), Neutral (Blue, $0\\text{ V}$ return), Earth (Green/Yellow, $0\\text{ V}$ safety ground)."
                )
            }
        },
        {
            "page_number": 10,
            "page_title": "Core Takeaways on Grid Supply",
            "block_type": "key_takeaway",
            "component_type": "key_takeaway",
            "content": {
                "text": "High-voltage grid transmission reduces line current, minimizing I^2R heat losses across long distances before stepping down to 240 V for safe home use."
            }
        }
    ]
}


# =============================================================================
# MODULE 6.2 DATA — Power, Energy Consumption & Utility Billing Costing
# =============================================================================
MODULE_6_2 = {
    "unit_name": "Module 6.2: Electrical Power, Energy Consumption, and Utility Billing Costing",
    "unit_order": 2,
    "lesson_title": "Electrical Power, Energy Consumption, and Utility Billing Costing",
    "cards": [
        # Page 1: Hook & Goals
        {
            "page_number": 1,
            "page_title": "Quantifying Electrical Power and Monthly Bills",
            "block_type": "learning_goal",
            "component_type": "learning_goal",
            "content": {
                "text": (
                    "Have you ever looked at a monthly Kenya Power electricity bill? "
                    "What does a 'unit' of electricity mean? Why does running a $3,000\\text{ W}$ electric heater for 1 hour cost far more than running a $10\\text{ W}$ LED bulb for a whole week?\n\n"
                    "In this module, you will master electrical power and energy equations, "
                    "define the commercial **Kilowatt-Hour ($\\text{kWh}$)**, read utility meters, "
                    "calculate electricity billing costs, and analyze non-linear power drops ($P \\propto V^2$) during voltage brownouts.\n\n"
                    "By the end of this lesson, you will be able to:\n"
                    "- Apply electrical power ($P = VI = I^2 R = \\frac{V^2}{R}$) and energy ($E = Pt = VIt$) equations\n"
                    "- Convert between Joules ($\\text{J}$) and Kilowatt-Hours ($\\text{kWh}$) ($1\\text{ kWh} = 3.6 \\times 10^6\\text{ J}$)\n"
                    "- Calculate household electricity consumption and monthly billing costs based on tariffs\n"
                    "- Explain why a $25\\%$ voltage drop causes a $43.75\\%$ drop in heating power output"
                )
            }
        },
        # Page 2: Electrical Power & Energy Equations
        {
            "page_number": 2,
            "page_title": "Electrical Power and Energy Equations",
            "block_type": "formula_breakdown",
            "component_type": "formula_breakdown",
            "content": {
                "formula": "$$\\mathbf{P = V \\cdot I = I^2 \\cdot R = \\frac{V^2}{R}} \\qquad \\text{and} \\qquad \\mathbf{E = P \\cdot t = V \\cdot I \\cdot t = I^2 \\cdot R \\cdot t}$$",
                "content": (
                    "### Governing Electrical Equations:\n"
                    "1. **Electrical Power ($P$)**: The rate of doing electrical work, measured in Watts ($\\text{W}$) or Kilowatts ($\\text{kW}$).\n"
                    "2. **Joule's Law Heating ($P = I^2R$)**: Used when current $I$ and resistance $R$ are known.\n"
                    "3. **Voltage-Dependent Power ($P = \\frac{V^2}{R}$)**: Critical for fixed-resistance heating appliances (kettles, irons, ovens) operating on changing supply voltages.\n"
                    "4. **Electrical Energy ($E$)**: Work done by current over time $t$, measured in Joules ($\\text{J}$) or Kilowatt-Hours ($\\text{kWh}$)."
                )
            }
        },
        # Page 3: Kilowatt-Hour Commercial Unit
        {
            "page_number": 3,
            "page_title": "The Commercial Energy Unit: Kilowatt-Hour (kWh)",
            "block_type": "definition_card",
            "component_type": "definition_card",
            "content": {
                "term": "Kilowatt-Hour (kWh)",
                "definition": (
                    "**One Kilowatt-Hour (1 kWh)**—commonly called 'one unit' of electricity—is the electrical energy consumed by a $1\\text{ kW}$ ($1,000\\text{ W}$) appliance operating continuously for $1\\text{ hour}$ ($3,600\\text{ seconds}$).\n\n"
                    "$$\\mathbf{1\\text{ kWh} = 1,000\\text{ W} \\times 3,600\\text{ s} = 3,600,000\\text{ J} = 3.6 \\times 10^6\\text{ J} = 3.6\\text{ MJ}}$$\n\n"
                    "### How to Calculate Energy in kWh:\n"
                    "$$\\text{Energy (kWh)} = \\text{Power in kW} \\times \\text{Time in hours} = \\frac{\\text{Power in Watts}}{1,000} \\times \\text{Time in hours}$$"
                )
            }
        },
        # Page 4: Appliance Rating Labels & Meters
        {
            "page_number": 4,
            "page_title": "Appliance Rating Labels and Electricity Meters",
            "block_type": "concept_explanation",
            "component_type": "concept_explanation",
            "content": {
                "text": (
                    "### Reading Electrical Ratings:\n"
                    "Every electrical appliance carries a mandatory rating plate specifying its operating voltage and power (e.g., **240 V, 1500 W**).\n\n"
                    "- **Operating Voltage ($240\\text{ V}$)**: The required mains potential difference for safe operation.\n"
                    "- **Power Rating ($1500\\text{ W} = 1.5\\text{ kW}$)**: The rate at which the appliance converts electrical energy into heat, light, or mechanical work.\n"
                    "- **Operating Current**: Derived via $I = \\frac{P}{V} = \\frac{1500}{240} = 6.25\\text{ A}$.\n\n"
                    "### Electricity Metering:\n"
                    "Utility meters (digital smart meters or analog rotating disc meters) record the cumulative energy ($\text{kWh}$) passing from service lines into consumer consumer units."
                )
            }
        },
        {
            "page_number": 4,
            "page_title": "Appliance Rating Label and Digital Utility Meter",
            "block_type": "suggested_diagram",
            "component_type": "suggested_diagram",
            "content": {
                "text": "Diagram showing an electrical appliance rating plate (240V, 1500W, 50Hz) alongside a digital household kWh energy meter display.",
                "instruction": (
                    "Draw appliance rating plate: 240V AC, 1500W, 50Hz, Model No. KB-200. "
                    "Draw digital electricity meter displaying cumulative reading: 04182.5 kWh."
                )
            }
        },
        # Page 5: Voltage Fluctuation Physics (P = V^2 / R)
        {
            "page_number": 5,
            "page_title": "Voltage Fluctuation Physics: The P = V^2 / R Effect",
            "block_type": "concept_explanation",
            "component_type": "concept_explanation",
            "content": {
                "text": (
                    "### Why Power Drops Non-Linearly During Brownouts:\n"
                    "Heating elements (ovens, irons, kettles) have a fixed internal electrical resistance ($R$). "
                    "Because power is $P = \\frac{V^2}{R}$, power output depends on the **square of supply voltage**!\n\n"
                    "### Mathematical Example:\n"
                    "An electric oven element is rated $3,600\\text{ W}$ at $240\\text{ V}$:\n"
                    "1. Element Resistance: $R = \\frac{V^2}{P} = \\frac{240^2}{3600} = \\frac{57600}{3600} = 16\\ \\Omega$.\n"
                    "2. **Voltage Brownout ($180\\text{ V}$)**: During grid brownouts, supply voltage drops by $25\\%$ to $180\\text{ V}$.\n"
                    "3. **New Power Output**: $P_{\\text{new}} = \\frac{V_{\\text{new}}^2}{R} = \\frac{180^2}{16} = \\frac{32400}{16} = \\mathbf{2,025\\text{ W}}$!\n"
                    "4. **Power Loss Percentage**: Power dropped from $3,600\\text{ W}$ to $2,025\\text{ W}$—a massive **$43.75\\%$ drop**!"
                )
            }
        },
        {
            "page_number": 5,
            "page_title": "Non-Linear Power Drop Graph (P vs V^2)",
            "block_type": "suggested_diagram",
            "component_type": "suggested_diagram",
            "content": {
                "text": "Parabolic graph showing heating power output P on y-axis against supply voltage V on x-axis, illustrating why 180V drops power to 2025W (a 43.75% drop).",
                "instruction": (
                    "Draw graph with y-axis Power (0 to 4000 W) and x-axis Voltage (0 to 300 V). "
                    "Draw quadratic curve P = V^2 / 16. Mark 240V -> 3600W and 180V -> 2025W."
                )
            }
        },
        # Page 6: Worked Example Level 1
        {
            "page_number": 6,
            "page_title": "Example 1: Appliance Operating Current",
            "block_type": "worked_example",
            "component_type": "worked_example",
            "content": {
                "problem": (
                    "An electric iron is rated at $1,200\\text{ W}, 240\\text{ V}$. "
                    "Calculate the normal operating current flowing through the iron."
                ),
                "steps": [
                    "**Given & Required:** Power $P = 1200\\text{ W}$, Supply voltage $V = 240\\text{ V}$. Required: Current $I$.",
                    "**Governing Equation:** $$P = V \\cdot I \\implies I = \\frac{P}{V}$$",
                    "**Substitution & Calculation:** $$I = \\frac{1200}{240} = \\mathbf{5.0\\text{ A}}$$",
                    "**Attach Unit:** $I = 5.0\\text{ A}$",
                    "**Physical Reasonableness Check:** A $1.2\\text{ kW}$ heating appliance on $240\\text{ V}$ mains typically draws $5\\text{ A}$, requiring a $13\\text{ A}$ plug fuse."
                ]
            }
        },
        # Page 7: Worked Example Level 2
        {
            "page_number": 7,
            "page_title": "Example 2: Energy in Joules and Kilowatt-Hours",
            "block_type": "worked_example",
            "component_type": "worked_example",
            "content": {
                "problem": (
                    "An electric space heater rated at $1.5\\text{ kW}$ is operated continuously for $4.0\\text{ hours}$. "
                    "Calculate the total energy consumed in:\n"
                    "(a) Kilowatt-Hours ($\\text{kWh}$)\n"
                    "(b) Joules ($\\text{J}$)"
                ),
                "steps": [
                    "**Given & Required:** Power $P = 1.5\\text{ kW}$, Time $t = 4.0\\text{ hours} = 14,400\\text{ seconds}$.",
                    "**(a) Energy in Kilowatt-Hours:** $$E_{\\text{kWh}} = P_{\\text{kW}} \\times t_{\\text{hours}} = 1.5 \\times 4.0 = \\mathbf{6.0\\text{ kWh}}$$",
                    "**(b) Energy in Joules:** $$E_{\\text{J}} = 6.0\\text{ kWh} \\times (3.6 \\times 10^6\\text{ J/kWh}) = \\mathbf{2.16 \\times 10^7\\text{ J}} \\text{ (or } 21.6\\text{ MJ)}$$",
                    "**Attach Units:** $E = 6.0\\text{ kWh} = 2.16 \\times 10^7\\text{ J}$"
                ]
            }
        },
        # Page 8: Worked Example Level 3 (Utility Billing Costing)
        {
            "page_number": 8,
            "page_title": "Example 3: Household Monthly Electricity Costing",
            "block_type": "worked_example",
            "component_type": "worked_example",
            "content": {
                "problem": (
                    "A home runs the following appliances daily:\n"
                    "- Four $20\\text{ W}$ LED bulbs for $5.0\\text{ hours/day}$\n"
                    "- One $1.5\\text{ kW}$ cooker for $2.0\\text{ hours/day}$\n"
                    "Calculate the total electricity bill for a $30\\text{-day}$ month if the energy tariff rate is $\\text{Ksh } 20.00\\text{ per kWh}$."
                ),
                "steps": [
                    "**Part A — Daily LED Bulb Energy:** $$P_{\\text{bulbs}} = 4 \\times 20\\text{ W} = 80\\text{ W} = 0.08\\text{ kW}$$ $$E_{\\text{bulbs}} = 0.08\\text{ kW} \\times 5.0\\text{ h} = 0.40\\text{ kWh/day}$$",
                    "**Part B — Daily Cooker Energy:** $$E_{\\text{cooker}} = 1.5\\text{ kW} \\times 2.0\\text{ h} = 3.0\\text{ kWh/day}$$",
                    "**Part C — Total Monthly Energy:** $$E_{\\text{daily}} = 0.40 + 3.0 = 3.40\\text{ kWh/day}$$ $$E_{\\text{monthly}} = 3.40\\text{ kWh/day} \\times 30\\text{ days} = \\mathbf{102.0\\text{ kWh}}$$",
                    "**Part D — Cost Calculation:** $$\\text{Total Cost} = 102.0\\text{ kWh} \\times \\text{Ksh } 20.00 = \\mathbf{\\text{Ksh } 2,040.00}$$",
                    "**Physical Reasonableness Check:** Ksh 2,040.00 is a standard realistic monthly domestic bill for lighting and daily cooking."
                ]
            }
        },
        # Page 9: Worked Example Level 4 (Kettle Heating & Efficiency)
        {
            "page_number": 9,
            "page_title": "Example 4: Electric Kettle Thermal Energy & Time",
            "block_type": "worked_example",
            "component_type": "worked_example",
            "content": {
                "problem": (
                    "An electric kettle of element resistance $48\\ \\Omega$ is connected to a $240\\text{ V}$ mains supply. "
                    "It contains $1.2\\text{ kg}$ of water initially at $20^\\circ\\text{C}$. "
                    "If the kettle is $80\\%$ efficient, calculate the time required to heat the water to boiling point ($100^\\circ\\text{C}$). "
                    "(Take specific heat capacity of water $c = 4,200\\text{ J/(kg}\\cdot^\\circ\\text{C)}$)."
                ),
                "steps": [
                    "**Part A — Kettle Power Rating:** $$P = \\frac{V^2}{R} = \\frac{240^2}{48} = \\frac{57600}{48} = 1,200\\text{ W}$$",
                    "**Part B — Useful Thermal Energy Required ($Q$):** $$Q = m \\cdot c \\cdot \\Delta \\theta = 1.2 \\times 4200 \\times (100 - 20) = 1.2 \\times 4200 \\times 80 = 403,200\\text{ J}$$",
                    "**Part C — Total Electrical Energy Supplied ($E$):** Since efficiency $\\eta = 80\\%$: $$E = \\frac{Q}{0.80} = \\frac{403200}{0.80} = 504,000\\text{ J}$$",
                    "**Part D — Time Calculation ($t$):** $$E = P \\cdot t \\implies t = \\frac{E}{P} = \\frac{504000}{1200} = \\mathbf{420\\text{ seconds}} \\text{ (}7.0\\text{ minutes})$$",
                    "**Physical Reasonableness Check:** 7 minutes is a realistic time for a 1.2 kW kettle to boil 1.2 liters of water."
                ]
            }
        },
        # Page 10: Worked Example Level 5 (Brownout Power Drop Challenge)
        {
            "page_number": 10,
            "page_title": "Challenge Problem: Brownout Power Loss Percentage",
            "block_type": "worked_example",
            "component_type": "worked_example",
            "content": {
                "problem": (
                    "An electric oven rated at $3,600\\text{ W}, 240\\text{ V}$ experiences a supply voltage drop to $180\\text{ V}$ during a peak grid brownout. "
                    "Determine:\n"
                    "(a) The new power output of the oven\n"
                    "(b) The percentage reduction in heating power output"
                ),
                "steps": [
                    "**Part A — Element Resistance ($R$):** $$R = \\frac{V^2}{P} = \\frac{240^2}{3600} = \\frac{57600}{3600} = 16\\ \\Omega$$",
                    "**Part B — New Power Output at 180 V ($P_2$):** $$P_2 = \\frac{V_2^2}{R} = \\frac{180^2}{16} = \\frac{32400}{16} = \\mathbf{2,025\\text{ W}}$$",
                    "**Part C — Power Reduction:** $$\\text{Reduction} = 3600\\text{ W} - 2025\\text{ W} = 1,575\\text{ W}$$",
                    "**Part D — Percentage Reduction:** $$\\%\\text{ Reduction} = \\frac{1575}{3600} \\times 100\\% = \\mathbf{43.75\\%}$$",
                    "**Physical Explanation:** Although voltage dropped by only $25\\%$, power dropped by $43.75\\%$ because $P \\propto V^2$. Cooking times will nearly double!"
                ]
            }
        },
        # Page 11: Knowledge Check (MCQ)
        {
            "page_number": 11,
            "page_title": "Check Your Understanding: Kilowatt-Hours to Joules",
            "block_type": "knowledge_check",
            "component_type": "knowledge_check",
            "content": {
                "check_type": "multiple_choice",
                "question": "How many Joules of energy are equivalent to 1 Kilowatt-Hour (1 kWh)?",
                "options": [
                    "3,600,000 J (3.6 MJ)",
                    "1,000 J",
                    "3,600 J",
                    "60,000 J"
                ],
                "answer": "A",
                "explanation": (
                    "1 kWh = 1,000 W x 3,600 seconds = 3,600,000 Joules = 3.6 x 10^6 J (3.6 MJ)."
                )
            }
        },
        # Page 12: Knowledge Check (MCQ)
        {
            "page_number": 12,
            "page_title": "Check Your Understanding: Non-Linear Voltage Drop",
            "block_type": "knowledge_check",
            "component_type": "knowledge_check",
            "content": {
                "check_type": "multiple_choice",
                "question": "If the mains supply voltage to a resistive water heater is halved (reduced to 50%), what happens to the power output of the heater?",
                "options": [
                    "Power output drops to 25% (one-quarter of original power)",
                    "Power output is halved to 50%",
                    "Power output drops to zero",
                    "Power output remains unchanged"
                ],
                "answer": "A",
                "explanation": (
                    "Because P = V^2 / R, halving voltage V to (0.5V) reduces power to (0.5)^2 = 0.25 (25% of original power)."
                )
            }
        },
        # Page 13: Summary & Key Takeaways
        {
            "page_number": 13,
            "page_title": "Module 6.2 Summary: Power, Energy & Costing",
            "block_type": "summary",
            "component_type": "summary",
            "content": {
                "text": (
                    "### Key Formulas & Concepts:\n"
                    "- **Power**: $P = VI = I^2 R = \\frac{V^2}{R}$\n"
                    "- **Energy**: $E = Pt = VIt = I^2 Rt$\n"
                    "- **Kilowatt-Hour**: $1\\text{ kWh} = 3.6 \\times 10^6\\text{ J}$\n"
                    "- **Costing**: $\\text{Cost} = \\text{Energy in kWh} \\times \\text{Tariff Rate per unit}$\n"
                    "- **Voltage Non-Linearity**: $P \\propto V^2 \\implies 180\\text{ V}$ brownout drops power by $43.75\\%$."
                )
            }
        },
        {
            "page_number": 13,
            "page_title": "Core Takeaways on Energy Costing",
            "block_type": "key_takeaway",
            "component_type": "key_takeaway",
            "content": {
                "text": "Electricity bills are based on energy consumed in kilowatt-hours (kWh), while heating appliance power output depends quadratically on supply voltage."
            }
        }
    ]
}


# =============================================================================
# MODULE 6.3 DATA — Domestic Wiring, Fuses, Earthing & Safety
# =============================================================================
MODULE_6_3 = {
    "unit_name": "Module 6.3: Domestic Circuit Wiring, Fuses, Earthing, and Electrical Safety",
    "unit_order": 3,
    "lesson_title": "Domestic Circuit Wiring, Fuses, Earthing, and Electrical Safety",
    "cards": [
        # Page 1: Hook & Goals
        {
            "page_number": 1,
            "page_title": "Domestic Wiring and Electrical Protection",
            "block_type": "learning_goal",
            "component_type": "learning_goal",
            "content": {
                "text": (
                    "Why are household socket outlets wired in parallel rather than in series? "
                    "Why does a three-pin plug have a top pin that is longer than the other two? "
                    "How does an earthing wire prevent fatal electric shocks when an appliance develops a internal fault?\n\n"
                    "In this module, you will analyze domestic parallel wiring, study the **Ring Main Circuit**, "
                    "examine three-pin BS 1363 plugs, select proper cartridge fuse ratings, and master earthing fault protection.\n\n"
                    "By the end of this lesson, you will be able to:\n"
                    "- Explain the structural advantages of parallel domestic household circuits\n"
                    "- Detail the ring main circuit loop and explain how dual parallel paths split current\n"
                    "- Wire a three-pin BS 1363 plug correctly (Live = Brown, Neutral = Blue, Earth = Green/Yellow)\n"
                    "- Calculate operating current ($I = P/V$) to select standard fuse ratings ($3\\text{ A}, 5\\text{ A}, 13\\text{ A}$)\n"
                    "- Explain how earthing metal casings provides low-resistance fault protection that blows fuses instantly"
                )
            }
        },
        # Page 2: Parallel Domestic Wiring Layout
        {
            "page_number": 2,
            "page_title": "Parallel Domestic Household Wiring",
            "block_type": "concept_explanation",
            "component_type": "concept_explanation",
            "content": {
                "text": (
                    "### Why Household Appliances Are Wired in Parallel:\n"
                    "Domestic circuits connect all appliances in parallel across the Live and Neutral consumer unit busbars:\n\n"
                    "1. **Independent Control**: Each appliance can be switched ON or OFF independently without affecting others.\n"
                    "2. **Constant Supply Voltage**: Every appliance receives the full $240\\text{ V}$ mains potential difference.\n"
                    "3. **Lower Total Resistance**: Adding more appliances in parallel decreases total equivalent resistance ($1/R_T = 1/R_1 + 1/R_2$), maintaining full power delivery."
                )
            }
        },
        {
            "page_number": 2,
            "page_title": "Parallel Household Circuit Wiring Schematic",
            "block_type": "suggested_diagram",
            "component_type": "suggested_diagram",
            "content": {
                "text": "Circuit schematic of domestic parallel wiring showing Live (Brown) and Neutral (Blue) busbars feeding lamps and sockets in parallel.",
                "instruction": (
                    "Draw Live busbar (Brown, 240V) and Neutral busbar (Blue, 0V). "
                    "Draw 3 parallel branches: Lamp 1 with switch, Lamp 2 with switch, and Socket Outlet with Earth line."
                )
            }
        },
        # Page 3: Ring Main Circuit
        {
            "page_number": 3,
            "page_title": "The Domestic Ring Main Circuit",
            "block_type": "concept_explanation",
            "component_type": "concept_explanation",
            "content": {
                "text": (
                    "A **Ring Main Circuit** is a closed loop of three-core cable originating from the consumer unit, "
                    "passing through multiple socket outlets in a room, and returning back to the exact same consumer unit terminals:\n\n"
                    "### Physical Engineering Advantages:\n"
                    "1. **Dual Current Path**: Current to any socket flows along two parallel paths (left and right arms of the ring). "
                    "This splits the total current in half ($I/2$), permitting thinner, cheaper copper cables to be used safely!\n"
                    "2. **Fail-Safe Redundancy**: If a cable breaks at one point, all sockets continue receiving full power from the other side of the ring."
                )
            }
        },
        {
            "page_number": 3,
            "page_title": "Ring Main Closed Loop Circuit Diagram",
            "block_type": "suggested_diagram",
            "component_type": "suggested_diagram",
            "content": {
                "text": "Diagram showing a Ring Main Circuit loop starting at consumer unit, passing through 4 socket outlets, and returning to consumer unit.",
                "instruction": (
                    "Draw Consumer Unit with 30A circuit breaker. "
                    "Draw closed ring loop wire feeding 4 socket outlets around a room and returning to consumer unit terminals. "
                    "Show current splitting into two parallel ring paths."
                )
            }
        },
        # Page 4: Three-Pin BS 1363 Plug Wiring
        {
            "page_number": 4,
            "page_title": "Three-Pin BS 1363 Plug Internal Wiring",
            "block_type": "concept_explanation",
            "component_type": "concept_explanation",
            "content": {
                "text": (
                    "### Internal Wiring Standards (BS 1363):\n"
                    "- **Live Wire (Brown)**: Connected to the right-hand terminal pin via a cartridge fuse.\n"
                    "- **Neutral Wire (Blue)**: Connected to the left-hand terminal pin.\n"
                    "- **Earth Wire (Green/Yellow)**: Connected to the top central terminal pin.\n"
                    "- **Cord Grip**: Clamps outer cable insulation firmly to prevent wires pulling out of terminals.\n"
                    "- **Longer Earth Pin**: The top Earth pin is longer than the Live/Neutral pins so that when plugged in, it opens the internal safety shutter doors covering Live and Neutral socket slots!"
                )
            }
        },
        {
            "page_number": 4,
            "page_title": "Three-Pin Plug Internal Wiring Layout",
            "block_type": "suggested_diagram",
            "component_type": "suggested_diagram",
            "content": {
                "text": "Internal anatomical diagram of a three-pin BS 1363 plug showing Live (Brown) with cartridge fuse, Neutral (Blue), Earth (Green/Yellow), and cable cord grip.",
                "instruction": (
                    "Draw three-pin plug interior. Top pin: Earth (Green/Yellow stripes). Left pin: Neutral (Blue). Right pin: Live (Brown) with cartridge fuse connected. "
                    "Show cable cord clamp at bottom."
                )
            }
        },
        # Page 5: Fuses & Circuit Breakers
        {
            "page_number": 5,
            "page_title": "Fuses and Miniature Circuit Breakers (MCBs)",
            "block_type": "concept_explanation",
            "component_type": "concept_explanation",
            "content": {
                "text": (
                    "### Protective Safety Devices:\n"
                    "1. **Cartridge Fuse**: A thin tinned-copper wire sealed in a ceramic tube. "
                    "If current exceeds its rated limit, $I^2R$ heating melts the wire, breaking the circuit instantly.\n"
                    "2. **Fuse Rating Rule**: Calculate appliance operating current ($I = P/V$) and select the **next available standard fuse rating above $I$** ($3\\text{ A}, 5\\text{ A}, 13\\text{ A}$).\n"
                    "3. **Miniature Circuit Breakers (MCBs)**: Electromagnetic switches that trip open during overcurrent. Unlike fuses, MCBs can be reset easily without replacement."
                )
            }
        },
        {
            "page_number": 5,
            "page_title": "Cartridge Fuse and Miniature Circuit Breaker Construction",
            "block_type": "suggested_diagram",
            "component_type": "suggested_diagram",
            "content": {
                "text": "Diagram showing cartridge fuse construction (glass tube, metal end caps, thin fuse wire) alongside a Miniature Circuit Breaker (MCB) magnetic trip coil mechanism.",
                "instruction": (
                    "Left: Cartridge fuse showing ceramic body, end caps, and internal fuse element. "
                    "Right: MCB showing bi-metallic strip and magnetic trip coil."
                )
            }
        },
        # Page 6: Earthing Protection Mechanism
        {
            "page_number": 6,
            "page_title": "Earthing Safety Protection Mechanism",
            "block_type": "concept_explanation",
            "component_type": "concept_explanation",
            "content": {
                "text": (
                    "### How Earthing Prevents Fatal Electric Shocks:\n"
                    "Consider a metal-cased electric cooker:\n\n"
                    "1. **The Fault**: Suppose a loose Live wire touches the metal outer casing inside the cooker.\n"
                    "2. **Without Earthing**: The casing becomes live at $240\\text{ V}$. If a person touches the cooker, current flows through their body to ground, causing a fatal electric shock!\n"
                    "3. **With Earthing**: The Earth wire connects the metal casing directly to ground ($0\\ \Omega$ resistance).\n"
                    "4. **Instant Fuse Blow**: The short circuit creates a massive surge current down the Earth wire ($I > 50\\text{ A}$), which instantly melts the Live plug fuse, isolating the power in $< 0.1\\text{ seconds}$!"
                )
            }
        },
        {
            "page_number": 6,
            "page_title": "Earthing Fault Current Path and Fuse Protection",
            "block_type": "suggested_diagram",
            "component_type": "suggested_diagram",
            "content": {
                "text": "Diagram showing fault condition where Live wire touches metal appliance casing, causing high fault current down Green/Yellow Earth wire to blow the Live fuse instantly.",
                "instruction": (
                    "Draw metal appliance casing. Show loose Live wire touching casing. "
                    "Draw Green/Yellow Earth wire connected from casing to ground. "
                    "Show high fault current path blowing Live fuse, saving user from shock."
                )
            }
        },
        # Page 7: Electrical Safety Hazards
        {
            "page_number": 7,
            "page_title": "Electrical Safety Hazards and Prevention",
            "block_type": "comparison_table",
            "component_type": "comparison_table",
            "content": {
                "headers": ["Electrical Hazard", "Physical Risk Factor", "Consequence / Danger", "Preventive Safety Action"],
                "rows": [
                    ["Damaged Insulation", "Exposed bare copper wires", "Electric shock or short circuit fire", "Replace worn cables immediately; never use insulation tape for permanent repair"],
                    ["Double Adapter Overload", "Drawing combined current exceeding socket rating ($>13\\text{ A}$)", "Overheating socket contacts and electrical fires", "Limit appliances per socket; use fused multi-socket extension strips"],
                    ["Damp / Wet Environments", "Water contains dissolved ions, dramatically lowering skin resistance", "Fatal electric shock from tiny voltages", "Never operate switches or appliances with wet hands; install RCD protection in bathrooms"],
                    ["Incorrect Fuse Rating", "Installing a $13\\text{ A}$ fuse on a $3\\text{ A}$ appliance", "Fuse fails to blow during fault, melting appliance wiring", "Always calculate $I = P/V$ and install the correct rated fuse"]
                ]
            }
        },
        # Page 8: Worked Example Level 1 (Fuse Selection)
        {
            "page_number": 8,
            "page_title": "Example 1: Fuse Rating Selection",
            "block_type": "worked_example",
            "component_type": "worked_example",
            "content": {
                "problem": (
                    "An electric toaster rated at $1,200\\text{ W}$ is connected to a $240\\text{ V}$ mains supply. "
                    "Available standard cartridge fuse ratings are $3\\text{ A}, 5\\text{ A},$ and $13\\text{ A}$. "
                    "Determine the correct fuse rating for the toaster plug."
                ),
                "steps": [
                    "**Step 1 — Identify Given Data:** Power $P = 1200\\text{ W}$, Mains voltage $V = 240\\text{ V}$.",
                    "**Step 2 — Calculate Operating Current ($I$):** $$I = \\frac{P}{V} = \\frac{1200}{240} = \\mathbf{5.0\\text{ A}}$$",
                    "**Step 3 — Apply Fuse Selection Rule:** Select the next available standard fuse rating **above** the normal operating current.",
                    "**Step 4 — Evaluate Options:** A $5\\text{ A}$ fuse will blow under normal load ($5.0\\text{ A}$ is right at the limit). Therefore, we select the **$13\\text{ A}$ fuse** to allow normal operation while protecting against fault overcurrents ($> 13\\text{ A}$)."
                ]
            }
        },
        # Page 9: Worked Example Level 2 (Ring Main Current)
        {
            "page_number": 9,
            "page_title": "Example 2: Ring Main Load Current",
            "block_type": "worked_example",
            "component_type": "worked_example",
            "content": {
                "problem": (
                    "A domestic ring main circuit operating at $240\\text{ V}$ is protected by a $30\\text{ A}$ circuit breaker. "
                    "The following appliances are plugged into the ring simultaneously:\n"
                    "- A $2.4\\text{ kW}$ electric heater\n"
                    "- A $1.2\\text{ kW}$ electric kettle\n"
                    "- A $600\\text{ W}$ microwave oven\n"
                    "Determine whether the circuit breaker will trip."
                ),
                "steps": [
                    "**Step 1 — Calculate Total Power ($P_{\\text{total}}$):** $$P_{\\text{total}} = 2400\\text{ W} + 1200\\text{ W} + 600\\text{ W} = \\mathbf{4,200\\text{ W}}$$",
                    "**Step 2 — Calculate Total Operating Current ($I_{\\text{total}}$):** $$I_{\\text{total}} = \\frac{P_{\\text{total}}}{V} = \\frac{4200}{240} = \\mathbf{17.5\\text{ A}}$$",
                    "**Step 3 — Compare with Breaker Rating:** Total current ($17.5\\text{ A}$) is well below the $30\\text{ A}$ circuit breaker rating ($17.5\\text{ A} < 30\\text{ A}$).",
                    "**Conclusion:** The circuit breaker will **NOT trip**, and the appliances will operate safely."
                ]
            }
        },
        # Page 10: Knowledge Check (MCQ)
        {
            "page_number": 10,
            "page_title": "Check Your Understanding: Earth Wire Function",
            "block_type": "knowledge_check",
            "component_type": "knowledge_check",
            "content": {
                "check_type": "multiple_choice",
                "question": "What is the primary physical function of the Green/Yellow Earth wire in a domestic appliance?",
                "options": [
                    "To provide a low-resistance path to ground for fault currents, blowing the fuse if a Live wire touches metal casing",
                    "To provide the normal return path for electric current back to the substation",
                    "To increase the operating voltage of the appliance to 240 V",
                    "To prevent voltage fluctuations during grid brownouts"
                ],
                "answer": "A",
                "explanation": (
                    "The Earth wire connects metal casings to ground. If a Live fault touches casing, high fault current down Earth wire instantly blows the fuse, protecting users from fatal shocks."
                )
            }
        },
        # Page 11: Knowledge Check (MCQ)
        {
            "page_number": 11,
            "page_title": "Check Your Understanding: Fuse Selection",
            "block_type": "knowledge_check",
            "component_type": "knowledge_check",
            "content": {
                "check_type": "multiple_choice",
                "question": "An electric heater rated at 2,000 W operates on a 240 V mains supply. Which standard fuse rating (3 A, 5 A, 13 A) should be installed in its three-pin plug?",
                "options": [
                    "13 A fuse",
                    "5 A fuse",
                    "3 A fuse",
                    "30 A fuse"
                ],
                "answer": "A",
                "explanation": (
                    "Operating current I = P/V = 2000 / 240 = 8.33 A. The next standard fuse rating above 8.33 A is 13 A."
                )
            }
        },
        # Page 12: Summary & Key Takeaways
        {
            "page_number": 12,
            "page_title": "Module 6.3 Summary: Domestic Wiring & Safety",
            "block_type": "summary",
            "component_type": "summary",
            "content": {
                "text": (
                    "### Key Safety Principles:\n"
                    "- **Parallel Circuits**: Equal $240\\text{ V}$ supply and independent appliance control.\n"
                    "- **Ring Main**: Closed loop dual path splits current, enabling thinner copper cables.\n"
                    "- **Three-Pin Plug**: Live (Brown, fused), Neutral (Blue), Earth (Green/Yellow).\n"
                    "- **Fuse Selection**: Select next standard rating above normal current ($I = P/V$).\n"
                    "- **Earthing Protection**: Fault current down Earth wire blows Live fuse instantly."
                )
            }
        },
        {
            "page_number": 13,
            "page_title": "Core Takeaways on Mains Safety",
            "block_type": "key_takeaway",
            "component_type": "key_takeaway",
            "content": {
                "text": "Domestic ring main circuits deliver 240 V in parallel, while earthing and correctly rated fuses isolate electrical faults to protect human life."
            }
        }
    ]
}

ALL_MODULES_TOPIC6 = [MODULE_6_1, MODULE_6_2, MODULE_6_3]


# =============================================================================
# INGESTION EXECUTOR
# =============================================================================

def run_ingestion_topic6(replace_mode=False):
    print("=" * 80)
    print("VLEARN FORM 4 PHYSICS — TOPIC 6: MAINS ELECTRICITY INGESTION")
    print(f"Mode: {'REPLACE (Destructive Fresh Ingestion)' if replace_mode else 'IDEMPOTENT SAFE UPDATE'}")
    print("=" * 80)

    curriculum = Curriculum.objects.filter(name="844").first()
    grade = Grade.objects.filter(curriculum=curriculum, name="Form 4").first()
    subject = Subject.objects.filter(grade=grade, name="Physics").first()

    topic, created = Topic.objects.get_or_create(
        subject=subject,
        name="Topic 6: Mains Electricity",
        defaults={
            "description": (
                "National grid supply, high-voltage transmission physics, substation distribution, "
                "three-conductor cables, electrical power and energy equations, commercial kilowatt-hours (kWh), "
                "utility bill costing, non-linear voltage drops, domestic parallel circuits, ring main loops, "
                "three-pin plug wiring, fuse selection, earthing fault protection, and safety hazards."
            ),
            "order": 6
        }
    )
    print(f"Topic verified: {topic.name} (ID: {topic.id}) under {subject.name}\n")

    total_blocks_created = 0
    total_blocks_updated = 0

    for m_idx, m_data in enumerate(ALL_MODULES_TOPIC6, start=1):
        unit, created = LearningUnit.objects.get_or_create(
            topic=topic,
            name=m_data["unit_name"],
            defaults={"order": m_data["unit_order"]}
        )
        print(f"[{m_idx}/3] Learning Unit: '{unit.name}' ({'Created' if created else 'Found'})")

        lesson, created = Lesson.objects.get_or_create(
            learning_unit=unit,
            defaults={
                "title": m_data["lesson_title"],
                "topic": topic,
                "status": "published",
                "version": 1
            }
        )
        if not created:
            lesson.title = m_data["lesson_title"]
            lesson.status = "published"
            lesson.save()
        print(f"     Lesson: '{lesson.title}' (ID: {lesson.id}, status={lesson.status})")

        with transaction.atomic():
            if replace_mode:
                del_blocks, _ = LessonBlock.objects.filter(lesson=lesson).delete()
                del_assets, _ = LessonAsset.objects.filter(lesson=lesson).delete()
                if del_blocks or del_assets:
                    print(f"     [Replace Mode] Purged {del_blocks} existing blocks, {del_assets} existing assets")

            for order, card in enumerate(m_data["cards"], start=1):
                clean_card = clean_content_dict(card)
                block_id = f"block_{lesson.id}_p{clean_card['page_number']}_{order}_{uuid.uuid4().hex[:6]}"

                if replace_mode:
                    LessonBlock.objects.create(
                        lesson=lesson,
                        block_id=block_id,
                        order=order,
                        page_number=clean_card["page_number"],
                        page_title=clean_card["page_title"],
                        block_type=clean_card["block_type"],
                        component_type=clean_card["component_type"],
                        component_order=order,
                        title=clean_card["page_title"],
                        content=clean_card["content"]
                    )
                    total_blocks_created += 1
                else:
                    existing_block = LessonBlock.objects.filter(
                        lesson=lesson,
                        page_number=clean_card["page_number"],
                        block_type=clean_card["block_type"]
                    ).first()

                    if existing_block:
                        existing_block.order = order
                        existing_block.page_title = clean_card["page_title"]
                        existing_block.component_type = clean_card["component_type"]
                        existing_block.component_order = order
                        existing_block.title = clean_card["page_title"]
                        
                        if isinstance(existing_block.content, dict) and 'svg_content' in existing_block.content:
                            clean_card["content"]["svg_content"] = existing_block.content["svg_content"]
                            clean_card["content"]["svg"] = existing_block.content.get("svg")
                        
                        existing_block.content = clean_card["content"]
                        existing_block.save()
                        total_blocks_updated += 1
                    else:
                        LessonBlock.objects.create(
                            lesson=lesson,
                            block_id=block_id,
                            order=order,
                            page_number=clean_card["page_number"],
                            page_title=clean_card["page_title"],
                            block_type=clean_card["block_type"],
                            component_type=clean_card["component_type"],
                            component_order=order,
                            title=clean_card["page_title"],
                            content=clean_card["content"]
                        )
                        total_blocks_created += 1

        num_pages = max(c["page_number"] for c in m_data["cards"])
        print(f"     Processed {len(m_data['cards'])} cards across {num_pages} pages.\n")

    print("=" * 80)
    print("TOPIC 6 INGESTION COMPLETED SUCCESSFULLY!")
    print(f"Total Blocks Created: {total_blocks_created} | Total Blocks Updated: {total_blocks_updated}")
    print(f"Topic: {topic.name} (ID: {topic.id}) under Subject: {subject.name}")
    print("=" * 80)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Form 4 Physics Topic 6 Ingestion")
    parser.add_argument("--replace", action="store_true", help="Purge and replace blocks fresh")
    args = parser.parse_args()
    run_ingestion_topic6(replace_mode=args.replace)
