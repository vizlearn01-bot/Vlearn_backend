"""
VLearn Form 4 Physics — Topic 3: Floating and Sinking
Ingestion Script

Source: Lessons.md (Topic 3)
Grade: Form 4
Subject: Physics
Curriculum: 844 (Kenyan 8-4-4 Secondary Curriculum)

Pedagogical Architecture:
  3 Learning Units / Modules:
  - Module 3.1: Upthrust, Archimedes' Principle, and Pressure Derivations (13 pages)
  - Module 3.2: The Law of Floatation and Relative Density (14 pages)
  - Module 3.3: Maritime Engineering, Weather Balloons, and Hydrometers (13 pages)

Features:
  - Adaptive 8-step analytical problem-solving framework
  - Multi-tier worked examples (Levels 1 to 5)
  - Full laboratory experimental setups (Eureka can, wooden block floatation, Cork and Sinker method)
  - Real-world engineering systems (Hollow hulls, Plimsoll marks, Submarines, Hydrometers, Balloons)
  - Purposeful interactions (prediction, simulation sandbox, reflections, knowledge checks)
  - Clean student-facing titles and zero developer terminology leaks
  - Idempotent safe updates (preserves enriched assets on rerun)

Usage:
  /home/jason-bitega/Desktop/VL/vlearn_repositories/Vlearn_backend/venv/bin/python curriculum/ingest_form4_physics_topic3.py
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
    """Remove source citation brackets like [65], [195], [image_0] and clean whitespace."""
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
# MODULE 3.1 DATA — Upthrust, Archimedes' Principle & Pressure Derivations
# =============================================================================
MODULE_3_1 = {
    "unit_name": "Module 3.1: Upthrust, Archimedes' Principle, and Pressure Derivations",
    "unit_order": 1,
    "lesson_title": "Upthrust, Archimedes' Principle, and Pressure Derivations",
    "cards": [
        # Page 1: Hook & Goals
        {
            "page_number": 1,
            "page_title": "Experiencing Buoyancy in Daily Life",
            "block_type": "learning_goal",
            "component_type": "learning_goal",
            "content": {
                "text": (
                    "Have you ever wondered why a tiny, solid steel sewing nail sinks instantly to the bottom of a bucket of water, "
                    "while a massive steel ship weighing tens of thousands of tonnes floats safely across the ocean? "
                    "Or why it feels remarkably easy to lift a heavy person inside a swimming pool, but the moment they step out into the air, "
                    "they suddenly feel heavy again?\n\n"
                    "These experiences occur because of **buoyancy**: any object submerged in a fluid experiences an upward pushing force called **upthrust** ($U$).\n\n"
                    "By the end of this lesson, you will be able to:\n"
                    "- Explain the physical origin of upthrust arising from fluid pressure differences with depth\n"
                    "- State and derive Archimedes' Principle mathematically ($U = \\rho_f V_d g$)\n"
                    "- Calculate apparent weight loss ($W_{\\text{apparent}} = W_{\\text{air}} - U$)\n"
                    "- Execute laboratory investigations using a Eureka overflow can and spring balance"
                )
            }
        },
        # Page 2: Theoretical Origin of Upthrust
        {
            "page_number": 2,
            "page_title": "The Origin of Upthrust: Pressure Gradient with Depth",
            "block_type": "concept_explanation",
            "component_type": "concept_explanation",
            "content": {
                "text": (
                    "### Why Does a Fluid Push an Object Upwards?\n"
                    "Recall that fluid pressure at depth $h$ is given by $P = \\rho g h$. "
                    "Because pressure increases steadily with depth, the liquid pushes harder on the bottom of a submerged block than on its top!\n\n"
                    "Let us analyze a submerged rectangular block of height $H$ and cross-sectional area $A$ immersed in a liquid of density $\\rho_f$:\n\n"
                    "1. **Downward Force on Top Face ($F_1$)** at depth $h_1$:\n"
                    "$$P_1 = \\rho_f g h_1 \\implies F_1 = P_1 \\cdot A = \\rho_f g h_1 A$$\n\n"
                    "2. **Upward Force on Bottom Face ($F_2$)** at depth $h_2 = h_1 + H$:\n"
                    "$$P_2 = \\rho_f g h_2 \\implies F_2 = P_2 \\cdot A = \\rho_f g h_2 A$$\n\n"
                    "3. **Net Vertical Buoyant Force ($F_{\\text{net}}$)**:\n"
                    "$$F_{\\text{net}} = F_2 - F_1 = \\rho_f g A (h_2 - h_1) = \\rho_f g A H$$\n\n"
                    "Since volume of the block is $V = A \\cdot H$, the net upward force is:\n"
                    "$$\\mathbf{U = \\rho_f V g}$$\n\n"
                    "Because $\\rho_f V = m_f$ (mass of displaced fluid), $\\rho_f V g$ is **identically equal to the weight of the displaced fluid**!"
                )
            }
        },
        {
            "page_number": 2,
            "page_title": "Fluid Pressure Gradient Creating Upthrust",
            "block_type": "suggested_diagram",
            "component_type": "suggested_diagram",
            "content": {
                "text": "Cross-sectional pressure gradient diagram of a submerged rectangular block showing downward force F1 on the top face at depth h1 and a strictly larger upward force F2 on the bottom face at depth h2, creating net upward force U = F2 - F1.",
                "instruction": (
                    "Draw a water container with a submerged rectangular block of height H and area A. "
                    "Draw depth markers h1 to top face and h2 to bottom face. "
                    "Draw downward red force arrow F1 = rho*g*h1*A on top face and larger upward green force arrow F2 = rho*g*h2*A on bottom face. "
                    "Annotate net resultant upward force U = rho*V*g."
                )
            }
        },
        # Page 3: Archimedes' Principle
        {
            "page_number": 3,
            "page_title": "Archimedes' Principle: Formal Definition",
            "block_type": "definition_card",
            "component_type": "definition_card",
            "content": {
                "term": "Archimedes' Principle",
                "definition": (
                    "**Archimedes' Principle** states that when a body is wholly or partially immersed in a fluid (liquid or gas), "
                    "it experiences an upward force (**upthrust**) that is **exactly equal to the weight of the fluid displaced by the body**.\n\n"
                    "$$\\mathbf{U = W_{\\text{displaced fluid}} = m_f \\cdot g = \\rho_f \\cdot V_d \\cdot g}$$\n\n"
                    "Where:\n"
                    "- $U$: Upthrust force in Newtons ($\\text{N}$)\n"
                    "- $\\rho_f$: Fluid density in $\\text{kg/m}^3$\n"
                    "- $V_d$: Volume of fluid displaced (equal to submerged volume of the object) in $\\text{m}^3$\n"
                    "- $g$: Gravitational acceleration ($10\\text{ m/s}^2$)"
                )
            }
        },
        # Page 4: Apparent Weight & Unit Conversions
        {
            "page_number": 4,
            "page_title": "Apparent Weight and Unit Conversions",
            "block_type": "formula_breakdown",
            "component_type": "formula_breakdown",
            "content": {
                "formula": "$$W_{\\text{apparent}} = W_{\\text{air}} - U \\qquad \\text{and} \\qquad U = W_{\\text{air}} - W_{\\text{apparent}}$$",
                "content": (
                    "Because upthrust directly opposes the downward pull of gravity, any submerged object appears lighter when weighed in a fluid.\n\n"
                    "### Mandatory SI Unit Conversions:\n"
                    "1. **Volume Conversion ($\\text{cm}^3$ to $\\text{m}^3$)**:\n"
                    "$$1\\text{ m}^3 = 1,000,000\\text{ cm}^3 = 10^6\\text{ cm}^3 \\implies 1\\text{ cm}^3 = 10^{-6}\\text{ m}^3$$\n"
                    "- Example: $60\\text{ cm}^3 = 60 \\times 10^{-6}\\text{ m}^3 = 6.0 \\times 10^{-5}\\text{ m}^3$\n\n"
                    "2. **Density Conversion ($\\text{g/cm}^3$ to $\\text{kg/m}^3$)**:\n"
                    "$$1\\text{ g/cm}^3 = 1,000\\text{ kg/m}^3$$\n"
                    "- Example: Water density $1.0\\text{ g/cm}^3 = 1,000\\text{ kg/m}^3$, Spirit $0.8\\text{ g/cm}^3 = 800\\text{ kg/m}^3$."
                )
            }
        },
        # Page 5: Worked Example Level 1
        {
            "page_number": 5,
            "page_title": "Example 1: Direct Calculation of Upthrust",
            "block_type": "worked_example",
            "component_type": "worked_example",
            "content": {
                "problem": (
                    "A metal block of volume $60\\text{ cm}^3$ weighs $4.80\\text{ N}$ in air. "
                    "Determine the upthrust acting on the block and its apparent weight when fully submerged in a liquid of density $1,200\\text{ kg/m}^3$. "
                    "(Take $g = 10\\text{ m/s}^2$)."
                ),
                "steps": [
                    "**Given & Required:** Weight in air $W_{\\text{air}} = 4.80\\text{ N}$, Volume $V = 60\\text{ cm}^3 = 6.0 \\times 10^{-5}\\text{ m}^3$, Liquid density $\\rho_f = 1,200\\text{ kg/m}^3$, $g = 10\\text{ m/s}^2$. Required: Upthrust $U$ and Apparent Weight $W_{\\text{apparent}}$.",
                    "**Upthrust Formula:** $$U = \\rho_f \\cdot V \\cdot g$$",
                    "**Substitution & Calculation:** $$U = 1200 \\times (6.0 \\times 10^{-5}) \\times 10 = 1200 \\times 6.0 \\times 10^{-4} = \\mathbf{0.72\\text{ N}}$$",
                    "**Apparent Submerged Weight:** $$W_{\\text{apparent}} = W_{\\text{air}} - U = 4.80\\text{ N} - 0.72\\text{ N} = \\mathbf{4.08\\text{ N}}$$",
                    "**Physical Reasonableness Check:** Upthrust ($0.72\\text{ N}$) is less than weight ($4.80\\text{ N}$), confirming the metal block will sink. Its measured weight underwater is reduced by exactly the weight of the liquid it displaces."
                ]
            }
        },
        # Page 6: Laboratory Experiment 1: Archimedes' Principle
        {
            "page_number": 6,
            "page_title": "Experimental Physics: Verifying Archimedes' Principle",
            "block_type": "step_process",
            "component_type": "step_process",
            "content": {
                "title": "Laboratory Investigation Protocol",
                "steps": [
                    "**Aim:** To prove experimentally that the upthrust acting on a submerged body equals the weight of the displaced liquid.",
                    "**Apparatus Required:** Eureka overflow can, spring balance, solid metal block, dry collecting beaker, triple-beam or digital balance, pure water.",
                    "**Procedure Stage 1:** Fill the Eureka can with water until it overflows through the spout. Wait until dripping stops completely. Place a clean, dry empty beaker of weight $W_3$ beneath the spout.",
                    "**Procedure Stage 2:** Weigh the metal block in air using the spring balance ($W_1$). Slowly lower the block into the Eureka can until fully submerged without touching the sides or bottom. Record the new apparent weight reading ($W_2$).",
                    "**Procedure Stage 3:** Allow all displaced overflow water to collect in the beaker. Weigh the beaker plus displaced water ($W_4$). Compare apparent loss in weight ($W_1 - W_2$) with displaced water weight ($W_4 - W_3$)."
                ]
            }
        },
        {
            "page_number": 6,
            "page_title": "Laboratory Setup for Demonstrating Archimedes' Principle",
            "block_type": "suggested_diagram",
            "component_type": "suggested_diagram",
            "content": {
                "text": "Laboratory apparatus diagram showing metal block suspended from a spring balance submerged in a Eureka overflow can, with displaced water overflowing through the spout into a collecting beaker on a balance.",
                "instruction": (
                    "Draw a Eureka can filled to spout level with water. Show metal block suspended from a spring balance lowered inside water. "
                    "Draw overflowing water exiting side spout into a collecting beaker placed on an electronic balance. "
                    "Label W1 (weight in air), W2 (weight in water), W3 (empty beaker), and W4 (beaker + displaced water)."
                )
            }
        },
        # Page 7: Experimental Data Verification
        {
            "page_number": 7,
            "page_title": "Data Collection & Mathematical Proof of Equivalence",
            "block_type": "comparison_table",
            "component_type": "comparison_table",
            "content": {
                "headers": ["Trial Parameter", "Measured Quantity", "Mathematical Symbol", "Experimental Value (Sample)"],
                "rows": [
                    ["Weight of Solid in Air", "Direct Spring Balance Reading", "$W_1$", "$2.50\\text{ N}$"],
                    ["Apparent Weight in Water", "Spring Balance with Submerged Block", "$W_2$", "$1.50\\text{ N}$"],
                    ["Calculated Upthrust", "Apparent Loss of Weight ($W_1 - W_2$)", "$U$", "$1.00\\text{ N}$"],
                    ["Weight of Empty Beaker", "Initial Dry Beaker Reading", "$W_3$", "$0.45\\text{ N}$"],
                    ["Weight of Beaker + Water", "Beaker with Displaced Overflow Water", "$W_4$", "$1.45\\text{ N}$"],
                    ["Weight of Displaced Water", "Difference ($W_4 - W_3$)", "$W_{\\text{displaced}}$", "$1.00\\text{ N}$"]
                ]
            }
        },
        # Page 8: Experimental Errors & Precautions
        {
            "page_number": 8,
            "page_title": "Sources of Error and Laboratory Precautions",
            "block_type": "common_misconception",
            "component_type": "common_misconception",
            "content": {
                "text": (
                    "### 1. Spout Surface Tension Adhesion\n"
                    "**Problem**: Surface tension can cause a few drops of water to cling to the lip of the Eureka can spout, causing the collected water weight ($W_4 - W_3$) to appear slightly lower than the true upthrust.\n"
                    "**Precaution**: Coat the spout lip with a trace of light silicone oil or gently tap the spout to release clinging drops.\n\n"
                    "### 2. Rapid Immersion and Splashing\n"
                    "**Problem**: Lowering the solid block too quickly causes surface turbulence and splashing, artificially increasing collected water.\n"
                    "**Precaution**: Lower the block smoothly and slowly using an adjustable lab jack.\n\n"
                    "### 3. Touching Container Walls\n"
                    "**Problem**: If the suspended block touches the base or walls of the Eureka can, normal reaction forces alter the spring balance reading.\n"
                    "**Precaution**: Ensure the block remains freely suspended in the centre of the fluid volume."
                )
            }
        },
        # Page 9: Interactive Simulation / Sandbox
        {
            "page_number": 9,
            "page_title": "Interactive Exploration: The Buoyancy Sandbox",
            "block_type": "prediction",
            "component_type": "prediction",
            "content": {
                "text": (
                    "**Think & Predict Before Simulating:**\n\n"
                    "A solid block of volume $500\\text{ cm}^3$ and mass $400\\text{ g}$ is placed in a tank of fresh water ($\\rho = 1.0\\text{ g/cm}^3$):\n"
                    "1. Will the block sink to the bottom or float on the surface?\n"
                    "2. What fraction of the block's total volume will be submerged beneath the water surface?"
                )
            }
        },
        {
            "page_number": 9,
            "page_title": "Interactive Buoyancy & Density Sandbox",
            "block_type": "suggested_simulation",
            "component_type": "suggested_simulation",
            "content": {
                "text": "Interactive buoyancy simulation allowing students to adjust object volume V (100-2000 cm^3), mass M (50-3000 g), and select fluid presets (Fresh Water 1.00 g/cm^3, Sea Water 1.03 g/cm^3, Kerosene 0.80 g/cm^3, Glycerin 1.26 g/cm^3) while observing real-time dynamic force vector arrows for Weight and Upthrust.",
                "instruction": "Simulation Key: buoyancy_sandbox. Real-time rendering of submerged fraction waterline and vector arrows."
            }
        },
        {
            "page_number": 9,
            "page_title": "Reflecting on Buoyancy Equilibrium",
            "block_type": "reflection",
            "component_type": "reflection",
            "content": {
                "text": (
                    "Because the block's average density is $\\rho = \\frac{400\\text{ g}}{500\\text{ cm}^3} = 0.80\\text{ g/cm}^3$, "
                    "which is less than water's density ($1.00\\text{ g/cm}^3$), the block floats with exactly $\\frac{0.80}{1.00} = 80\\%$ "
                    "of its volume submerged ($400\\text{ cm}^3$). The weight of $400\\text{ cm}^3$ of displaced water ($4.0\\text{ N}$) "
                    "perfectlies balances the block's weight ($4.0\\text{ N}$)."
                )
            }
        },
        # Page 10: Knowledge Check (MCQ)
        {
            "page_number": 10,
            "page_title": "Check Your Understanding: Upthrust in Liquids",
            "block_type": "knowledge_check",
            "component_type": "knowledge_check",
            "content": {
                "check_type": "multiple_choice",
                "question": "A stone of volume $50\\text{ cm}^3$ is completely submerged in sea water of density $1,030\\text{ kg/m}^3$. What is the upthrust acting on the stone? (Take $g = 10\\text{ m/s}^2$).",
                "options": [
                    "$U = 0.515\\text{ N}$",
                    "$U = 5.15\\text{ N}$",
                    "$U = 0.0515\\text{ N}$",
                    "$U = 51.5\\text{ N}$"
                ],
                "answer": "A",
                "explanation": (
                    "Volume in SI units: V = 50 * 10^-6 m^3 = 5.0 * 10^-5 m^3.\n"
                    "Upthrust U = rho_f * V * g = 1030 kg/m^3 * (5.0 * 10^-5 m^3) * 10 m/s^2 = 0.515 N."
                )
            }
        },
        # Page 11: Knowledge Check (True/False)
        {
            "page_number": 11,
            "page_title": "Check Your Understanding: Upthrust and Depth",
            "block_type": "knowledge_check",
            "component_type": "knowledge_check",
            "content": {
                "check_type": "true_false",
                "question": "Once a solid stone is completely submerged in an incompressible liquid, the upthrust acting on it continues to increase as it sinks deeper into the liquid.",
                "options": ["True", "False"],
                "answer": "False",
                "explanation": (
                    "False. Upthrust is given by U = rho_f * V_d * g. Once an object is fully submerged, its displaced volume V_d remains constant regardless of depth, so upthrust remains completely unchanged at any depth."
                )
            }
        },
        # Page 12: Summary & Key Takeaways
        {
            "page_number": 12,
            "page_title": "Module 3.1 Summary: Upthrust & Archimedes' Principle",
            "block_type": "summary",
            "component_type": "summary",
            "content": {
                "text": (
                    "### Key Physical Foundations:\n"
                    "- **Origin of Upthrust**: Arises from the fluid pressure difference between top and bottom faces ($P_2 > P_1$ because $P = \\rho g h$).\n"
                    "- **Archimedes' Principle**: $U = \\rho_f V_d g = W_{\\text{displaced fluid}}$\n"
                    "- **Apparent Weight**: $W_{\\text{apparent}} = W_{\\text{air}} - U$\n"
                    "- **Depth Independence**: Upthrust is constant once fully submerged because displaced volume $V_d$ is constant."
                )
            }
        },
        {
            "page_number": 12,
            "page_title": "Core Takeaways on Buoyant Forces",
            "block_type": "key_takeaway",
            "component_type": "key_takeaway",
            "content": {
                "text": "Upthrust is the direct mechanical consequence of fluid pressure increasing with depth, producing a net upward force equal to the weight of displaced fluid."
            }
        }
    ]
}


# =============================================================================
# MODULE 3.2 DATA — The Law of Floatation & Relative Density
# =============================================================================
MODULE_3_2 = {
    "unit_name": "Module 3.2: The Law of Floatation and Relative Density",
    "unit_order": 2,
    "lesson_title": "The Law of Floatation and Relative Density",
    "cards": [
        # Page 1: Hook & Goals
        {
            "page_number": 1,
            "page_title": "The Physics of Floating Bodies",
            "block_type": "learning_goal",
            "component_type": "learning_goal",
            "content": {
                "text": (
                    "When an object is placed on a liquid surface, it sinks into the liquid until the upthrust from the displaced liquid "
                    "grows large enough to balance the object's total downward weight. At this exact point of equilibrium, the object stops sinking and floats!\n\n"
                    "In this module, you will explore the Law of Floatation, derive the submerged volume fraction formula, define Relative Density, "
                    "and learn the ingenious **Cork and Sinker Method** used to measure the relative density of light floating objects in the lab.\n\n"
                    "By the end of this lesson, you will be able to:\n"
                    "- State and apply the Law of Floatation ($U = W_{\\text{body}}$)\n"
                    "- Relate the submerged volume fraction to the ratio of body density and liquid density ($\\frac{V_{\\text{sub}}}{V_{\\text{total}}} = \\frac{\\rho_b}{\\rho_l}$)\n"
                    "- Define Relative Density ($d$) and relate it to spring balance apparent weight losses\n"
                    "- Execute the 3-step Cork and Sinker experimental method to determine the relative density of a light cork"
                )
            }
        },
        # Page 2: The Law of Floatation
        {
            "page_number": 2,
            "page_title": "The Law of Floatation: Mathematical Derivation",
            "block_type": "formula_breakdown",
            "component_type": "formula_breakdown",
            "content": {
                "formula": "$$\\text{Upthrust } (U) = \\text{Total Weight } (W) \\implies \\rho_{\\text{liquid}} \\cdot V_{\\text{submerged}} \\cdot g = \\rho_{\\text{body}} \\cdot V_{\\text{total}} \\cdot g$$",
                "content": (
                    "**The Law of Floatation**: A floating body displaces its own weight of the liquid in which it floats.\n\n"
                    "### Deriving the Submerged Fraction Equation:\n"
                    "Dividing both sides by $\\rho_{\\text{liquid}} \\cdot V_{\\text{total}} \\cdot g$:\n\n"
                    "$$\\mathbf{\\frac{V_{\\text{submerged}}}{V_{\\text{total}}} = \\frac{\\rho_{\\text{body}}}{\\rho_{\\text{liquid}}}}$$\n\n"
                    "| Density Comparison | Physical Result | Volume Relationship |\n"
                    "|---|---|---|\n"
                    "| $\\rho_{\\text{body}} < \\rho_{\\text{liquid}}$ | **Floats partially submerged** | $V_{\\text{submerged}} < V_{\\text{total}}$ |\n"
                    "| $\\rho_{\\text{body}} = \\rho_{\\text{liquid}}$ | **Neutrally buoyant (floats just under surface)** | $V_{\\text{submerged}} = V_{\\text{total}}$ |\n"
                    "| $\\rho_{\\text{body}} > \\rho_{\\text{liquid}}$ | **Sinks completely to the bottom** | Maximum $U < W_{\\text{body}}$ |"
                )
            }
        },
        # Page 3: Comparison of Floating Conditions
        {
            "page_number": 3,
            "page_title": "Floating, Neutral Buoyancy, and Sinking Criteria",
            "block_type": "comparison_table",
            "component_type": "comparison_table",
            "content": {
                "headers": ["Physical State", "Density Relation", "Net Vertical Force", "Visual Appearance in Liquid"],
                "rows": [
                    ["Floating with Freeboard", "$\\rho_{\\text{body}} < \\rho_{\\text{liquid}}$", "Net Force = 0 (Equilibrium)", "Part of volume extends above liquid surface"],
                    ["Neutral Buoyancy", "$\\rho_{\\text{body}} = \\rho_{\\text{liquid}}$", "Net Force = 0 (Equilibrium)", "Suspended fully submerged at any depth"],
                    ["Sinking to Base", "$\\rho_{\\text{body}} > \\rho_{\\text{liquid}}$", "Net Force = Downward ($W > U$)", "Rests on bottom with normal reaction from base"]
                ]
            }
        },
        {
            "page_number": 3,
            "page_title": "Submerged Fraction and Density Ratios",
            "block_type": "suggested_diagram",
            "component_type": "suggested_diagram",
            "content": {
                "text": "Diagram showing 3 identical blocks of different densities in water: Block A (rho = 0.6 g/cm^3, 60% submerged), Block B (rho = 1.0 g/cm^3, neutral buoyancy 100% submerged), and Block C (rho = 2.5 g/cm^3, sinking to the tank bottom).",
                "instruction": (
                    "Draw a glass water tank. Show Block A floating with 60% under waterline and 40% above. "
                    "Show Block B hovering neutrally just beneath the surface. "
                    "Show Block C resting at the bottom of the tank with a normal reaction force R."
                )
            }
        },
        # Page 4: Worked Example Level 2
        {
            "page_number": 4,
            "page_title": "Example 2: Law of Floatation in Spirit",
            "block_type": "worked_example",
            "component_type": "worked_example",
            "content": {
                "problem": (
                    "A wooden block of dimensions $3\\text{ cm} \\times 3\\text{ cm} \\times 4\\text{ cm}$ floats vertically in methylated spirit "
                    "with its full length of $4\\text{ cm}$ submerged in the spirit. If the density of methylated spirit is $800\\text{ kg/m}^3$, "
                    "calculate the weight of the wooden block. (Take $g = 10\\text{ m/s}^2$)."
                ),
                "steps": [
                    "**Given & Submerged Volume:** Dimensions $= 3\\text{ cm} \\times 3\\text{ cm} \\times 4\\text{ cm}$. Submerged volume $V_d = 36\\text{ cm}^3 = 3.6 \\times 10^{-5}\\text{ m}^3$, Spirit density $\\rho_f = 800\\text{ kg/m}^3$, $g = 10\\text{ m/s}^2$. Required: Weight of block $W$.",
                    "**Governing Principle (Law of Floatation):** $$W = \\text{Upthrust } (U) = \\rho_f \\cdot V_d \\cdot g$$",
                    "**Substitution & Calculation:** $$W = 800 \\times (3.6 \\times 10^{-5}) \\times 10 = 8000 \\times 3.6 \\times 10^{-5} = \\mathbf{0.288\\text{ N}}$$",
                    "**Physical Reality Check:** The weight of the wooden block is $0.288\\text{ N}$ (mass $\\approx 28.8\\text{ g}$). Since it floats fully submerged in the spirit, the average density of the wood must equal the spirit density ($800\\text{ kg/m}^3$)."
                ]
            }
        },
        # Page 5: Relative Density Definition
        {
            "page_number": 5,
            "page_title": "Relative Density (RD): Definition and Formulas",
            "block_type": "definition_card",
            "component_type": "definition_card",
            "content": {
                "term": "Relative Density (d)",
                "definition": (
                    "**Relative Density ($d$)** is the ratio of the density of a substance to the density of pure water at $4^\\circ\\text{C}$. "
                    "Being a ratio of identical physical quantities, relative density is **dimensionless (has no units)**.\n\n"
                    "$$d = \\frac{\\rho_{\\text{substance}}}{\\rho_{\\text{water}}} = \\frac{\\text{Weight in air } (W_{\\text{air}})}{\\text{Upthrust in water } (U_w)} = \\mathbf{\\frac{W_{\\text{air}}}{W_{\\text{air}} - W_{\\text{water}}}}$$\n\n"
                    "### Finding Actual Density from Relative Density:\n"
                    "$$\\mathbf{\\rho_{\\text{substance}} = d \\times 1,000\\text{ kg/m}^3}$$"
                )
            }
        },
        # Page 6: Worked Example Level 3
        {
            "page_number": 6,
            "page_title": "Example 3: Relative Density of a Solid Sinker",
            "block_type": "worked_example",
            "component_type": "worked_example",
            "content": {
                "problem": (
                    "A solid metal sphere of mass $1.0\\text{ kg}$ is suspended from a spring balance and lowered completely into water. "
                    "If the spring balance reads $5.0\\text{ N}$ in water, calculate:\n"
                    "(a) The relative density ($d$) of the metal.\n"
                    "(b) The actual density ($\\rho_s$) of the metal in $\\text{kg/m}^3$. (Take $g = 10\\text{ m/s}^2$)."
                ),
                "steps": [
                    "**Given & Required:** Mass $m = 1.0\\text{ kg} \\implies W_{\\text{air}} = m \\cdot g = 10.0\\text{ N}$. Apparent weight in water $W_{\\text{water}} = 5.0\\text{ N}$. Required: Relative density $d$, actual density $\\rho_s$.",
                    "**Upthrust in Water ($U_w$):** $$U_w = W_{\\text{air}} - W_{\\text{water}} = 10.0\\text{ N} - 5.0\\text{ N} = 5.0\\text{ N}$$",
                    "**(a) Relative Density ($d$):** $$d = \\frac{W_{\\text{air}}}{U_w} = \\frac{10.0\\text{ N}}{5.0\\text{ N}} = \\mathbf{2} \\quad \\text{(no units)}$$",
                    "**(b) Actual Density ($\\rho_s$):** $$\\rho_s = d \\times 1,000\\text{ kg/m}^3 = 2 \\times 1000 = \\mathbf{2,000\\text{ kg/m}^3}$$",
                    "**Physical Reasonableness Check:** Relative density $2$ is twice as dense as water ($1,000\\text{ kg/m}^3$), so it sinks and loses exactly half of its weight in water, matching the spring balance reading."
                ]
            }
        },
        # Page 7: Laboratory Experiment 2: Law of Floatation
        {
            "page_number": 7,
            "page_title": "Experimental Physics: Verifying the Law of Floatation",
            "block_type": "step_process",
            "component_type": "step_process",
            "content": {
                "title": "Verification of Floatation Protocol",
                "steps": [
                    "**Aim:** To verify that a floating body displaces its own weight in different liquids (water and kerosene).",
                    "**Apparatus Required:** Eureka can, dry collecting beaker, wooden block, balance, water ($\\rho = 1000\\text{ kg/m}^3$), kerosene ($\\rho = 800\\text{ kg/m}^3$).",
                    "**Step 1:** Weigh the wooden block in air using an electronic balance ($W_1$). Fill the Eureka can until water overflows and stops dripping.",
                    "**Step 2:** Place an empty beaker of known weight ($W_2$) under the spout. Gently place the wooden block on the water surface so it floats freely.",
                    "**Step 3:** Weigh the beaker with the collected displaced water ($W_3$). Calculate displaced water weight $W_{\\text{disp}} = W_3 - W_2$. Verify $W_1 = W_{\\text{disp}}$.",
                    "**Step 4:** Repeat the experiment using kerosene. Observe that the block sinks deeper in kerosene, but displaced liquid weight still equals block weight $W_1$."
                ]
            }
        },
        {
            "page_number": 7,
            "page_title": "Experimental Setup for the Law of Floatation",
            "block_type": "suggested_diagram",
            "component_type": "suggested_diagram",
            "content": {
                "text": "Experimental comparison diagram showing a block of wood floating in water (shallow submersion) and in kerosene (deeper submersion), with displaced liquid collected in beakers showing equal weight.",
                "instruction": (
                    "Draw two Eureka cans side-by-side: Can 1 with water (wood floats higher, displacing smaller volume of dense liquid), "
                    "Can 2 with kerosene (wood floats lower, displacing larger volume of lighter liquid). "
                    "Show collected beakers with callout W_displaced = W_wood in both cases."
                )
            }
        },
        # Page 8: Laboratory Experiment 3: The Cork and Sinker Method
        {
            "page_number": 8,
            "page_title": "Experimental Physics: The Cork and Sinker Method",
            "block_type": "step_process",
            "component_type": "step_process",
            "content": {
                "title": "3-Stage Experimental Protocol for Floating Bodies",
                "steps": [
                    "**Problem Statement:** A light cork floats on water and cannot submerge itself. How do we measure its displaced volume and relative density?",
                    "**Stage (a) — Sinker Alone in Water:** Suspend a heavy metal sinker alone from the spring balance submerged in water. Record reading as **$W_1$** ($W_1 = W_{\\text{sinker, water}}$).",
                    "**Stage (b) — Cork in Air, Sinker in Water:** Tie the cork to the thread so it hangs in air while the sinker remains submerged beneath it in water. Record reading as **$W_2$** ($W_2 = W_1 + W_{\\text{cork, air}}$).",
                    "**Stage (c) — Both Cork and Sinker in Water:** Tie the cork and sinker close together and submerge both completely in water. Record reading as **$W_3$** ($W_3 = W_1 + W_{\\text{cork, water}}$)."
                ]
            }
        },
        {
            "page_number": 8,
            "page_title": "The 3 Stages of the Cork and Sinker Method",
            "block_type": "suggested_diagram",
            "component_type": "suggested_diagram",
            "content": {
                "text": "3-stage experimental diagram showing: (a) Sinker alone in water (W1), (b) Cork in air with sinker in water (W2), and (c) Both cork and sinker submerged in water (W3).",
                "instruction": (
                    "Draw 3 spring balance setups side by side in a single figure: "
                    "(a) Sinker submerged in beaker of water, spring balance reading W1. "
                    "(b) Cork in air above beaker, sinker in water, balance reading W2. "
                    "(c) Both cork and sinker submerged in water, balance reading W3. "
                    "Annotate formulas: Weight in air = W2 - W1, Upthrust = W2 - W3."
                )
            }
        },
        # Page 9: Cork Sinker Mathematical Derivation
        {
            "page_number": 9,
            "page_title": "Mathematical Derivation: Cork Relative Density",
            "block_type": "formula_breakdown",
            "component_type": "formula_breakdown",
            "content": {
                "formula": "$$\\text{Relative Density of Cork } (d) = \\frac{\\text{Weight of Cork in Air}}{\\text{Upthrust on Cork in Water}} = \\mathbf{\\frac{W_2 - W_1}{W_2 - W_3}}$$",
                "content": (
                    "### Step-by-Step Algebraic Proof:\n"
                    "1. Reading $W_1 = W_{\\text{sinker, water}}$\n"
                    "2. Reading $W_2 = W_{\\text{sinker, water}} + W_{\\text{cork, air}} = W_1 + W_{\\text{cork, air}}$\n"
                    "   $$\\implies \\mathbf{W_{\\text{cork, air}} = W_2 - W_1}$$\n"
                    "3. Reading $W_3 = W_{\\text{sinker, water}} + W_{\\text{cork, water}} = W_1 + W_{\\text{cork, water}}$\n"
                    "   $$\\implies W_{\\text{cork, water}} = W_3 - W_1$$\n"
                    "4. Upthrust on the cork alone in water ($U_{\\text{cork}}$):\n"
                    "   $$U_{\\text{cork}} = W_{\\text{cork, air}} - W_{\\text{cork, water}} = (W_2 - W_1) - (W_3 - W_1) = \\mathbf{W_2 - W_3}$$\n"
                    "5. Therefore:\n"
                    "   $$d = \\frac{W_{\\text{cork, air}}}{U_{\\text{cork}}} = \\mathbf{\\frac{W_2 - W_1}{W_2 - W_3}}$$"
                )
            }
        },
        # Page 10: Knowledge Check (MCQ)
        {
            "page_number": 10,
            "page_title": "Check Your Understanding: Submerged Fraction",
            "block_type": "knowledge_check",
            "component_type": "knowledge_check",
            "content": {
                "check_type": "multiple_choice",
                "question": "An iceberg of density $920\\text{ kg/m}^3$ floats in ocean water of density $1,025\\text{ kg/m}^3$. What percentage of the iceberg's total volume is submerged beneath the water?",
                "options": [
                    "$89.8\\%$",
                    "$92.0\\%$",
                    "$10.2\\%$",
                    "$75.0\\%$"
                ],
                "answer": "A",
                "explanation": (
                    "From the Law of Floatation: V_submerged / V_total = rho_ice / rho_water = 920 / 1025 = 0.89756 (approx 89.8%). "
                    "This explains why nearly 90% of an iceberg is hidden underwater!"
                )
            }
        },
        # Page 11: Knowledge Check (Calculation Check)
        {
            "page_number": 11,
            "page_title": "Check Your Understanding: Cork and Sinker Calculation",
            "block_type": "knowledge_check",
            "component_type": "knowledge_check",
            "content": {
                "check_type": "multiple_choice",
                "question": "In a cork-and-sinker experiment, the spring balance readings are: Sinker alone in water $W_1 = 1.20\\text{ N}$, Cork in air with sinker in water $W_2 = 1.60\\text{ N}$, and Both submerged in water $W_3 = 0.60\\text{ N}$. What is the relative density of the cork?",
                "options": [
                    "$d = 0.40$",
                    "$d = 0.25$",
                    "$d = 0.80$",
                    "$d = 2.50$"
                ],
                "answer": "A",
                "explanation": (
                    "Weight of cork in air = W2 - W1 = 1.60 - 1.20 = 0.40 N.\n"
                    "Upthrust on cork = W2 - W3 = 1.60 - 0.60 = 1.00 N.\n"
                    "Relative density d = (W2 - W1) / (W2 - W3) = 0.40 / 1.00 = 0.40."
                )
            }
        },
        # Page 12: Multi-Step Worked Example
        {
            "page_number": 12,
            "page_title": "Example: Floating in Two Different Liquids",
            "block_type": "worked_example",
            "component_type": "worked_example",
            "content": {
                "problem": (
                    "A block of wood floats in water with $\\frac{2}{3}$ of its volume submerged. "
                    "When placed in another liquid, it floats with $\\frac{3}{4}$ of its volume submerged. Calculate:\n"
                    "(a) The density of the wood in $\\text{g/cm}^3$.\n"
                    "(b) The density of the second liquid in $\\text{g/cm}^3$."
                ),
                "steps": [
                    "**Given & Principle:** In water ($\\rho_w = 1.0\\text{ g/cm}^3$), $\\frac{V_{\\text{sub}}}{V_{\\text{total}}} = \\frac{2}{3}$. In liquid 2, $\\frac{V_{\\text{sub}}}{V_{\\text{total}}} = \\frac{3}{4}$.",
                    "**(a) Finding Density of Wood:** $$\\frac{\\rho_{\\text{wood}}}{\\rho_{\\text{water}}} = \\frac{2}{3} \\implies \\rho_{\\text{wood}} = \\frac{2}{3} \\times 1.0\\text{ g/cm}^3 = \\mathbf{0.67\\text{ g/cm}^3} \\text{ (or } 667\\text{ kg/m}^3)$$",
                    "**(b) Finding Density of Second Liquid:** $$\\frac{\\rho_{\\text{wood}}}{\\rho_{\\text{liquid 2}}} = \\frac{3}{4} \\implies \\rho_{\\text{liquid 2}} = \\frac{4}{3} \\times \\rho_{\\text{wood}} = \\frac{4}{3} \\times 0.667 = \\mathbf{0.889\\text{ g/cm}^3} \\text{ (or } 889\\text{ kg/m}^3)$$",
                    "**Physical Reasonableness:** The second liquid is less dense than water ($0.889 < 1.00$), so the wood must sink deeper ($\\frac{3}{4} > \\frac{2}{3}$) to displace enough mass to equal its weight."
                ]
            }
        },
        # Page 13: Summary & Key Takeaways
        {
            "page_number": 13,
            "page_title": "Module 3.2 Summary: Floatation & Relative Density",
            "block_type": "summary",
            "component_type": "summary",
            "content": {
                "text": (
                    "### Key Relationships:\n"
                    "- **Law of Floatation**: Floating body displaces its own weight ($U = W_{\\text{body}}$)\n"
                    "- **Submerged Fraction**: $\\frac{V_{\\text{sub}}}{V_{\\text{total}}} = \\frac{\\rho_{\\text{body}}}{\\rho_{\\text{liquid}}}$\n"
                    "- **Relative Density (Solid)**: $d = \\frac{W_{\\text{air}}}{W_{\\text{air}} - W_{\\text{water}}}$\n"
                    "- **Cork and Sinker Method**: $d = \\frac{W_2 - W_1}{W_2 - W_3}$"
                )
            }
        },
        {
            "page_number": 13,
            "page_title": "Core Takeaways on Floating Bodies",
            "block_type": "key_takeaway",
            "component_type": "key_takeaway",
            "content": {
                "text": "Floating equilibrium requires the weight of displaced liquid to exactly equal the total weight of the floating body."
            }
        }
    ]
}


# =============================================================================
# MODULE 3.3 DATA — Maritime Systems, Balloons & Hydrometers
# =============================================================================
MODULE_3_3 = {
    "unit_name": "Module 3.3: Maritime Engineering, Weather Balloons, and Hydrometers",
    "unit_order": 3,
    "lesson_title": "Maritime Engineering, Weather Balloons, and Hydrometers",
    "cards": [
        # Page 1: Hook & Goals
        {
            "page_number": 1,
            "page_title": "Engineering with Buoyancy: Ships, Submarines & Instruments",
            "block_type": "learning_goal",
            "component_type": "learning_goal",
            "content": {
                "text": (
                    "Archimedes' Principle and the Law of Floatation are central to global maritime transport, oceanography, "
                    "meteorological atmospheric exploration, and industrial quality testing.\n\n"
                    "In this module, you will discover how hollow steel hulls keep ocean liners afloat, why ships have Plimsoll load lines, "
                    "how submarines control their diving depths, how hydrometers test battery acid and milk, and how weather balloons lift payloads into the stratosphere.\n\n"
                    "By the end of this lesson, you will be able to:\n"
                    "- Explain how hollow ship design lowers average density below that of water\n"
                    "- Interpret Plimsoll line marks across tropical, fresh, winter, and summer waters\n"
                    "- Describe submarine ballast tank mechanics during diving and surfacing\n"
                    "- Explain the construction and downward-graduated scale of standard hydrometers\n"
                    "- Calculate the net payload lifting capacity of gas-filled weather balloons"
                )
            }
        },
        # Page 2: Steel Ships & Hollow Hulls
        {
            "page_number": 2,
            "page_title": "Steel Ships and Hollow Hull Displacement",
            "block_type": "concept_explanation",
            "component_type": "concept_explanation",
            "content": {
                "text": (
                    "A solid block of steel has a density of about $7,800\\text{ kg/m}^3$, which is nearly $8\\times$ denser than water ($1,000\\text{ kg/m}^3$), so it sinks immediately.\n\n"
                    "### Why Does a Steel Ship Float?\n"
                    "- A ship is engineered with a **massive hollow hull** enclosing enormous volumes of air.\n"
                    "- **Average Density**: $$\\rho_{\\text{average}} = \\frac{\\text{Total Mass of Steel + Cargo + Air}}{\\text{Total External Enclosed Volume}}$$\n"
                    "- Because air density is only $\\approx 1.2\\text{ kg/m}^3$, the ship's overall average density is reduced to **far below $1,000\\text{ kg/m}^3$**.\n"
                    "- Consequently, the ship sinks only slightly until it displaces a volume of water whose weight equals the ship's entire mass!"
                )
            }
        },
        {
            "page_number": 2,
            "page_title": "Hollow Hull Cross-Section and Density Reduction",
            "block_type": "suggested_diagram",
            "component_type": "suggested_diagram",
            "content": {
                "text": "Cross-sectional comparison between a small solid steel block (sinks) and a large hollow steel ship hull enclosing air (floats with large displaced water volume creating huge upthrust).",
                "instruction": (
                    "Draw two illustrations side by side: "
                    "(1) Solid steel block at the bottom of water tank. "
                    "(2) Hollow ship hull floating with waterline, showing thin steel walls, large interior air cavity, and upward upthrust vector U balancing downward weight W."
                )
            }
        },
        # Page 3: Plimsoll Marks (Load Lines)
        {
            "page_number": 3,
            "page_title": "Plimsoll Marks: Maritime Load Lines",
            "block_type": "concept_explanation",
            "component_type": "concept_explanation",
            "content": {
                "text": (
                    "Because water density varies with **temperature** and **salinity (salt concentration)**, a ship sinks to different depths in different bodies of water:\n\n"
                    "- **Fresh Water** (rivers/lakes) is less dense than **Salt Water** (oceans), so a ship sinks deeper in fresh water.\n"
                    "- **Cold Winter Water** is denser than **Warm Tropical Water**, so a ship floats higher in cold seas.\n\n"
                    "### The Purpose of Plimsoll Marks:\n"
                    "Named after British reformer Samuel Plimsoll, **Plimsoll load lines** painted on a ship's hull indicate the maximum safe loading depth for:\n"
                    "- **TF**: Tropical Fresh Water (sinks deepest, highest mark)\n"
                    "- **F**: Fresh Water\n"
                    "- **T**: Tropical Salt Water\n"
                    "- **S**: Summer Temperate Salt Water\n"
                    "- **W**: Winter Salt Water\n"
                    "- **WNA**: Winter North Atlantic (densest water, lowest mark)"
                )
            }
        },
        {
            "page_number": 3,
            "page_title": "Plimsoll Load Line Markings on a Ship Hull",
            "block_type": "suggested_diagram",
            "component_type": "suggested_diagram",
            "content": {
                "text": "Technical maritime schematic of standard Plimsoll load line markings on a ship's hull showing the circle with horizontal bar and the stepped ladder of lines: TF, F, T, S, W, WNA.",
                "instruction": (
                    "Draw dark ship hull plate. Draw Plimsoll disc with horizontal bar across centre. "
                    "To the right, draw vertical line with horizontal stepped lines labeled TF (top), F, T, S, W, and WNA (bottom). "
                    "Annotate density trend: Denser Cold/Salt Water = Ship Floats Higher."
                )
            }
        },
        # Page 4: Submarines & Ballast Tanks
        {
            "page_number": 4,
            "page_title": "Submarines: Variable Buoyancy Depth Control",
            "block_type": "concept_explanation",
            "component_type": "concept_explanation",
            "content": {
                "text": (
                    "A submarine operates both on the surface and deep underwater by continuously altering its average density using **ballast tanks**:\n\n"
                    "### 1. Diving (Submerging):\n"
                    "- Top air vents are opened, allowing sea water to flood the ballast tanks.\n"
                    "- As air is displaced by heavy water, the submarine's total mass increases.\n"
                    "- Average density exceeds water density ($\\rho_{\\text{sub}} > \\rho_{\\text{water}}$), and the submarine sinks.\n\n"
                    "### 2. Neutral Depth Cruising:\n"
                    "- Ballast water is regulated until total weight exactly equals upthrust ($W = U$), maintaining stable cruising depth.\n\n"
                    "### 3. Surfacing (Rising):\n"
                    "- High-pressure **compressed air** is blown into the ballast tanks, forcing sea water out through bottom flood ports.\n"
                    "- The submarine's average density drops below water density ($\\rho_{\\text{sub}} < \\rho_{\\text{water}}$), and it ascends to float on the surface."
                )
            }
        },
        {
            "page_number": 4,
            "page_title": "Submarine Ballast Tank Operation Mechanism",
            "block_type": "suggested_diagram",
            "component_type": "suggested_diagram",
            "content": {
                "text": "Cross-sectional diagram of submarine ballast tanks showing: (1) Surface Cruising (tanks filled with air, W = U), (2) Diving (vents open, water floods tanks, W > U), and (3) Surfacing (compressed air blows water out, U > W).",
                "instruction": (
                    "Draw 3 cross sections of submarine hull with inner pressure hull and outer ballast tanks: "
                    "Panel 1: Tanks with air (Surface). "
                    "Panel 2: Tanks flooded with blue water (Diving). "
                    "Panel 3: High pressure air hose blowing water out through bottom ports (Surfacing)."
                )
            }
        },
        # Page 5: Hydrometers
        {
            "page_number": 5,
            "page_title": "Hydrometers: Construction and Inverted Scale",
            "block_type": "concept_explanation",
            "component_type": "concept_explanation",
            "content": {
                "text": (
                    "A **hydrometer** is a glass instrument used to measure the relative density of liquids directly and rapidly.\n\n"
                    "### Key Structural Features:\n"
                    "1. **Weighted Bottom Bulb (Lead Shots)**: Keeps the centre of gravity low so the hydrometer floats upright vertically without toppling over.\n"
                    "2. **Large Buoyancy Bulb**: Provides sufficient volume to displace liquid and create the necessary upthrust to keep the instrument afloat.\n"
                    "3. **Narrow Stem**: Maximizes sensitivity. A small change in liquid density causes a large change in the submerged stem height ($h$).\n\n"
                    "### Why is the Hydrometer Scale Numbered Downwards?\n"
                    "- In a **denser liquid**, more upthrust is generated per unit volume, so the hydrometer **sinks less** (floats high out of liquid).\n"
                    "- In a **less dense liquid**, the hydrometer must **sink deeper** to displace enough liquid to equal its weight.\n"
                    "- Therefore, **higher density readings ($1.200$) are located at the bottom of the stem**, while **lower density readings ($0.800$) are at the top**!"
                )
            }
        },
        {
            "page_number": 5,
            "page_title": "Hydrometer Construction & Downward Graduated Scale",
            "block_type": "suggested_diagram",
            "component_type": "suggested_diagram",
            "content": {
                "text": "Detailed anatomical diagram of a laboratory hydrometer showing narrow stem with downward-graduated scale (0.800 top, 1.000 middle, 1.200 bottom), large cylindrical buoyancy bulb, and weighted base bulb with lead shots.",
                "instruction": (
                    "Draw a glass hydrometer floating in liquid. Label narrow stem with tick marks 0.800 at top, 1.000 in middle, and 1.200 near base of stem. "
                    "Label large central bulb, and bottom spherical bulb containing dark grey lead shots. "
                    "Add callout: 'Denser liquid = Sinks less = Read lower on stem'."
                )
            }
        },
        # Page 6: Specialized Hydrometers
        {
            "page_number": 6,
            "page_title": "Specialized Hydrometers: Lactometer & Battery Tester",
            "block_type": "comparison_table",
            "component_type": "comparison_table",
            "content": {
                "headers": ["Instrument", "Measured Liquid", "Normal Operating Density Range", "Diagnostic Purpose"],
                "rows": [
                    ["Lactometer", "Cow / Goat Milk", "$1.015 - 1.045\\text{ g/cm}^3$", "Detects water adulteration. Adding water lowers density toward $1.000$."],
                    ["Battery Acid Tester", "Sulfuric Acid Electrolyte in Lead-Acid Battery", "$1.150 - 1.280\\text{ g/cm}^3$", "Measures state of battery charge. Fully charged $= 1.280$; Discharged $< 1.150$."]
                ]
            }
        },
        # Page 7: Worked Example Level 4 (Weather Balloon)
        {
            "page_number": 7,
            "page_title": "Example 4: Weather Balloon Payload Lift",
            "block_type": "worked_example",
            "component_type": "worked_example",
            "content": {
                "problem": (
                    "A meteorological weather balloon made of fabric weighing $80\\text{ N}$ has an inflated volume of $10\\text{ m}^3$. "
                    "The balloon is filled with hydrogen gas of density $0.09\\text{ kg/m}^3$. "
                    "Determine the maximum payload weight that this balloon can lift in air of average density $1.25\\text{ kg/m}^3$. "
                    "(Take $g = 10\\text{ m/s}^2$)."
                ),
                "steps": [
                    "**Given & Required:** Fabric weight $W_{\\text{fabric}} = 80\\text{ N}$, Volume $V = 10\\text{ m}^3$, Air density $\\rho_{\\text{air}} = 1.25\\text{ kg/m}^3$, Hydrogen density $\\rho_{\\text{gas}} = 0.09\\text{ kg/m}^3$, $g = 10\\text{ m/s}^2$. Required: Maximum payload weight $W_{\\text{payload}}$.",
                    "**Upthrust from Surrounding Air ($U$):** $$U = \\rho_{\\text{air}} \\cdot V \\cdot g = 1.25 \\times 10 \\times 10 = \\mathbf{125\\text{ N}}$$",
                    "**Weight of Enclosed Hydrogen Gas ($W_{\\text{gas}}$):** $$W_{\\text{gas}} = \\rho_{\\text{gas}} \\cdot V \\cdot g = 0.09 \\times 10 \\times 10 = \\mathbf{9\\text{ N}}$$",
                    "**Total Empty Balloon Weight ($W_{\\text{total}}$):** $$W_{\\text{empty}} = W_{\\text{fabric}} + W_{\\text{gas}} = 80\\text{ N} + 9\\text{ N} = 89\\text{ N}$$",
                    "**Payload Lifting Capacity ($W_{\\text{payload}}$):** $$W_{\\text{payload}} = U - W_{\\text{empty}} = 125\\text{ N} - 89\\text{ N} = \\mathbf{36\\text{ N}}$$",
                    "**Physical Reality Check:** The surrounding air exerts an upward buoyant force of $125\\text{ N}$. Since the balloon structure and hydrogen gas weigh $89\\text{ N}$, the remaining $36\\text{ N}$ of buoyant lift is available to carry scientific instruments."
                ]
            }
        },
        # Page 8: Worked Example Level 5 (Composite Body)
        {
            "page_number": 8,
            "page_title": "Example 5: Composite Submerged Body",
            "block_type": "worked_example",
            "component_type": "worked_example",
            "content": {
                "problem": (
                    "A heavy material of density $8.5\\text{ g/cm}^3$ is attached to a light wooden block of mass $100\\text{ g}$ and density $0.2\\text{ g/cm}^3$. "
                    "Calculate the volume $V$ of the heavy material that must be attached to the wood so that the composite body is just fully submerged "
                    "in a liquid of density $1.2\\text{ g/cm}^3$."
                ),
                "steps": [
                    "**Given & Required:** Wood mass $m_w = 100\\text{ g}$, Wood density $\\rho_w = 0.2\\text{ g/cm}^3$, Material density $\\rho_m = 8.5\\text{ g/cm}^3$, Liquid density $\\rho_l = 1.2\\text{ g/cm}^3$. Required: Volume of material $V$ in $\\text{cm}^3$.",
                    "**Volume of Wood:** $$V_w = \\frac{m_w}{\\rho_w} = \\frac{100\\text{ g}}{0.2\\text{ g/cm}^3} = 500\\text{ cm}^3$$",
                    "**Composite Equations:** Total Mass $M_{\\text{total}} = 100 + 8.5V$; Total Volume $V_{\\text{total}} = 500 + V$.",
                    "**Neutral Buoyancy Condition:** $$\\rho_{\\text{average}} = \\frac{M_{\\text{total}}}{V_{\\text{total}}} = \\rho_l \\implies \\frac{100 + 8.5V}{500 + V} = 1.2$$",
                    "**Algebraic Solution:** $$100 + 8.5V = 1.2(500 + V) = 600 + 1.2V$$ $$8.5V - 1.2V = 600 - 100 \\implies 7.3V = 500$$ $$V = \\frac{500}{7.3} \\approx \\mathbf{68.5\\text{ cm}^3}$$",
                    "**Physical Reality Check:** Total mass $= 100 + (68.5 \\times 8.5) = 682.25\\text{ g}$; Total volume $= 500 + 68.5 = 568.5\\text{ cm}^3$. Average density $= 682.25 / 568.5 = 1.20\\text{ g/cm}^3$, which matches the liquid density."
                ]
            }
        },
        # Page 9: Misconception Busting
        {
            "page_number": 9,
            "page_title": "Common Misconceptions in Floating and Sinking",
            "block_type": "common_misconception",
            "component_type": "common_misconception",
            "content": {
                "text": (
                    "### 1. The \"Weight Sinks Objects\" Myth\n"
                    "**The Misconception**: Heavy objects always sink, and light objects always float.\n"
                    "**The Physics Reality**: Sinking or floating is governed entirely by **average density**, not total mass! An ocean tanker weighing $100,000\\text{ tonnes}$ floats because its hollow hull encloses air, lowering its density to $< 1.0\\text{ g/cm}^3$. A $0.5\\text{ g}$ iron pin sinks because iron density ($7.8\\text{ g/cm}^3$) exceeds water.\n\n"
                    "### 2. The \"Upthrust Equals Object Weight\" Error\n"
                    "**The Misconception**: Upthrust is always equal to the weight of the object.\n"
                    "**The Physics Reality**: Upthrust is **always equal to the weight of displaced fluid**. Upthrust equals object weight *only* when the object is floating in equilibrium ($U = W$). For a sinking object resting on the base, $U < W$."
                )
            }
        },
        # Page 10: Knowledge Check: Hydrometers
        {
            "page_number": 10,
            "page_title": "Check Your Understanding: Hydrometer Calibration",
            "block_type": "knowledge_check",
            "component_type": "knowledge_check",
            "content": {
                "check_type": "multiple_choice",
                "question": "Why is the graduated scale on the stem of a hydrometer numbered downwards, with higher density readings at the bottom of the stem?",
                "options": [
                    "Because denser liquids provide greater upthrust per unit volume, causing the hydrometer to sink less into the liquid",
                    "Because denser liquids are always located at the bottom of the graduated cylinder",
                    "To account for the surface tension pulling the stem downwards",
                    "Because hydrometers operate in reverse when measuring battery acid"
                ],
                "answer": "A",
                "explanation": (
                    "According to the Law of Floatation, a hydrometer displaces an amount of liquid equal to its own weight. In a denser liquid, a smaller volume of liquid is needed, so the hydrometer sinks less and floats higher, exposing more of the stem. Hence, higher density values must be at the bottom of the stem."
                )
            }
        },
        # Page 11: Knowledge Check: Submarines
        {
            "page_number": 11,
            "page_title": "Check Your Understanding: Submarine Ballast Operation",
            "block_type": "knowledge_check",
            "component_type": "knowledge_check",
            "content": {
                "check_type": "multiple_choice",
                "question": "How does a submerged submarine return to the surface of the ocean?",
                "options": [
                    "By pumping high-pressure compressed air into its ballast tanks to expel sea water, reducing its average density",
                    "By opening the top vents to allow more sea water into the ballast tanks",
                    "By accelerating forward at maximum engine speed until dynamic lift pushes it upward",
                    "By dropping heavy lead sinkers to the ocean floor"
                ],
                "answer": "A",
                "explanation": (
                    "To surface, compressed air is blown into the ballast tanks, expelling the heavy sea water. This drastically lowers the total mass and average density of the submarine below that of water, generating a net upward buoyant force."
                )
            }
        },
        # Page 12: Challenge Worked Example
        {
            "page_number": 12,
            "page_title": "Challenge Problem: Sinking Solid Connected to Floating Cork",
            "block_type": "worked_example",
            "component_type": "worked_example",
            "content": {
                "problem": (
                    "A solid of mass $200\\text{ g}$ and density $8.0\\text{ g/cm}^3$ is completely submerged in water using a light thread. "
                    "If the block is also attached to a cork of mass $20\\text{ g}$ and density $0.2\\text{ g/cm}^3$ floating on the water surface, "
                    "calculate the net tension in the thread supporting the combination. (Take $g = 10\\text{ m/s}^2$)."
                ),
                "steps": [
                    "**Solid Forces (Submerged):** Mass $m_1 = 0.20\\text{ kg} \\implies W_1 = 2.00\\text{ N}$. Volume $V_1 = \\frac{200}{8} = 25\\text{ cm}^3 = 2.5 \\times 10^{-5}\\text{ m}^3$. Upthrust $U_1 = 1000 \\times (2.5 \\times 10^{-5}) \\times 10 = 0.25\\text{ N}$. Downward pull $= W_1 - U_1 = 2.00 - 0.25 = 1.75\\text{ N}$.",
                    "**Cork Forces (Fully Submerged Limit):** Mass $m_2 = 0.02\\text{ kg} \\implies W_2 = 0.20\\text{ N}$. Volume $V_2 = \\frac{20}{0.2} = 100\\text{ cm}^3 = 1.0 \\times 10^{-4}\\text{ m}^3$. Maximum Upthrust $U_2 = 1000 \\times 10^{-4} \\times 10 = 1.00\\text{ N}$. Surplus buoyant lift $= U_2 - W_2 = 1.00 - 0.20 = 0.80\\text{ N}$.",
                    "**Determining Submersion:** Since downward pull of solid ($1.75\\text{ N}$) exceeds maximum surplus lift of cork ($0.80\\text{ N}$), the cork is pulled completely underwater.",
                    "**Net Thread Tension:** $$T = (W_1 + W_2) - (U_1 + U_2) = (2.00 + 0.20) - (0.25 + 1.00) = 2.20\\text{ N} - 1.25\\text{ N} = \\mathbf{0.95\\text{ N}}$$",
                    "**Physical Conclusion:** The spring balance or supporting thread holds a net tension of $0.95\\text{ N}$, which exactly equals total weight minus total buoyant upthrust."
                ]
            }
        },
        # Page 13: Summary & Key Takeaways
        {
            "page_number": 13,
            "page_title": "Module 3.3 Summary: Maritime & Applied Buoyancy",
            "block_type": "summary",
            "component_type": "summary",
            "content": {
                "text": (
                    "### Key Applied Principles:\n"
                    "- **Hollow Ships**: Enclosing massive air volumes lowers average density below water.\n"
                    "- **Plimsoll Lines**: Adjust safe loading depths for water temperature and salinity variations.\n"
                    "- **Submarines**: Ballast tank water flooding for diving, compressed air expulsion for surfacing.\n"
                    "- **Hydrometer Calibration**: Inverted scale because denser liquids cause less submersion.\n"
                    "- **Gas Balloons**: Net lift $= U_{\\text{air}} - (W_{\\text{fabric}} + W_{\\text{gas}})$.\n"
                    "- **Average Density**: Controls floating and sinking across all composite engineering systems."
                )
            }
        },
        {
            "page_number": 13,
            "page_title": "Core Takeaways on Applied Buoyancy",
            "block_type": "key_takeaway",
            "component_type": "key_takeaway",
            "content": {
                "text": "By mastering average density and Archimedes' Principle, engineers design ocean ships, submarines, hydrometers, and stratospheric balloons."
            }
        }
    ]
}

ALL_MODULES_TOPIC3 = [MODULE_3_1, MODULE_3_2, MODULE_3_3]


# =============================================================================
# INGESTION EXECUTOR
# =============================================================================

def run_ingestion_topic3(replace_mode=False):
    print("=" * 80)
    print("VLEARN FORM 4 PHYSICS — TOPIC 3: FLOATING AND SINKING INGESTION")
    print(f"Mode: {'REPLACE (Destructive Fresh Ingestion)' if replace_mode else 'IDEMPOTENT SAFE UPDATE'}")
    print("=" * 80)

    curriculum = Curriculum.objects.filter(name="844").first()
    grade = Grade.objects.filter(curriculum=curriculum, name="Form 4").first()
    subject = Subject.objects.filter(grade=grade, name="Physics").first()

    topic, created = Topic.objects.get_or_create(
        subject=subject,
        name="Topic 3: Floating and Sinking",
        defaults={
            "description": (
                "Physical principles of upthrust, pressure derivations, Archimedes' Principle, the Law of Floatation, "
                "relative density determinations, laboratory experiments (Eureka can, cork and sinker method), "
                "maritime engineering of ships and submarines, Plimsoll load lines, hydrometers, and gas-filled weather balloons."
            ),
            "order": 3
        }
    )
    print(f"Topic verified: {topic.name} (ID: {topic.id}) under {subject.name}\n")

    total_blocks_created = 0
    total_blocks_updated = 0

    for m_idx, m_data in enumerate(ALL_MODULES_TOPIC3, start=1):
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
    print("TOPIC 3 INGESTION COMPLETED SUCCESSFULLY!")
    print(f"Total Blocks Created: {total_blocks_created} | Total Blocks Updated: {total_blocks_updated}")
    print(f"Topic: {topic.name} (ID: {topic.id}) under Subject: {subject.name}")
    print("=" * 80)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Form 4 Physics Topic 3 Ingestion")
    parser.add_argument("--replace", action="store_true", help="Purge and replace blocks fresh")
    args = parser.parse_args()
    run_ingestion_topic3(replace_mode=args.replace)
