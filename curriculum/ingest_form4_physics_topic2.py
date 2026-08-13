"""
VLearn Form 4 Physics — Topic 2: Uniform Circular Motion
Ingestion Script

Source: Lessons.md (Topic 2)
Grade: Form 4
Subject: Physics
Curriculum: 844 (Kenyan 8-4-4 Secondary Curriculum)

Pedagogical Architecture:
  3 Learning Units / Modules × 12–15 pages each:
  - Module 2.1: Kinematics of Circular Motion and Angular Quantities (12 pages)
  - Module 2.2: Centripetal Dynamics, Vertical Circles, and Laboratory Experiments (15 pages)
  - Module 2.3: Engineering Applications and Mechanics of Circular Motion (13 pages)

Features:
  - Adaptive 8-step analytical problem-solving framework
  - Multi-tier worked examples (Levels 1 to 5)
  - Full laboratory experimental setup, procedure, and T vs w^2 graph strategy
  - Purposeful interactions (prediction, simulation sandbox, reflections, knowledge checks)
  - Clean student-facing titles and zero developer terminology leaks
  - Idempotent safe updates (preserves enriched assets on rerun)

Usage:
  /home/jason-bitega/Desktop/VL/vlearn_repositories/Vlearn_backend/venv/bin/python curriculum/ingest_form4_physics_topic2.py
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
    """Remove source citation brackets like [52], [182, 191], [image_0] and clean whitespace."""
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
# MODULE 2.1 DATA — Kinematics of Circular Motion and Angular Quantities
# =============================================================================
MODULE_2_1 = {
    "unit_name": "Module 2.1: Kinematics of Circular Motion and Angular Quantities",
    "unit_order": 1,
    "lesson_title": "Kinematics of Circular Motion and Angular Quantities",
    "cards": [
        # Page 1: Hook & Goals
        {
            "page_number": 1,
            "page_title": "Experiencing Circular Motion in Daily Life",
            "block_type": "learning_goal",
            "component_type": "learning_goal",
            "content": {
                "text": (
                    "Have you ever ridden in a matatu or a boda boda negotiating a sharp bend at high speed? "
                    "You likely felt your body sliding outwards towards the vehicle door or side of the seat. "
                    "Similarly, when you whirl a stone tied to a string above your head, you feel a continuous pull in your hand.\n\n"
                    "In this module, you will discover the physics governing curved paths, make a crucial conceptual shift regarding acceleration, "
                    "and master the angular quantities used to measure rotations.\n\n"
                    "By the end of this lesson, you will be able to:\n"
                    "- Explain how an object can accelerate while maintaining a constant speed\n"
                    "- Represent linear velocity as instantaneous tangential vectors\n"
                    "- Define the radian ($\\text{rad}$) and convert fluently between degrees and radians\n"
                    "- Calculate angular velocity ($\\omega$) and relate it to linear speed ($v = r\\omega$)\n"
                    "- Define angular acceleration ($\\alpha$) and relate it to tangential acceleration ($a = r\\alpha$)"
                )
            }
        },
        # Page 2: Constant Speed but Changing Velocity
        {
            "page_number": 2,
            "page_title": "The Conceptual Shift: Acceleration at Constant Speed",
            "block_type": "concept_explanation",
            "component_type": "concept_explanation",
            "content": {
                "text": (
                    "### Speed vs. Velocity in Curved Motion\n"
                    "In linear motion, acceleration represents a change in speed—speeding up or slowing down. "
                    "In circular motion, we encounter a fundamental physical principle:\n\n"
                    "**An object moving along a circular path at a constant speed is continuously accelerating!**\n\n"
                    "- **Velocity is a Vector**: It possesses both **magnitude (speed)** and **direction**.\n"
                    "- A car travelling in a straight line at $60\\text{ km/h}$ has constant speed and constant velocity (acceleration $= 0$).\n"
                    "- A car negotiating a circular roundabout at a steady $60\\text{ km/h}$ has constant speed but **changing velocity**, "
                    "because its direction of motion is continuously changing at every fraction of a second.\n\n"
                    "Because its velocity vector is constantly changing direction, the car experiences continuous **centripetal acceleration**, "
                    "which is always directed radially towards the centre of the circular path."
                )
            }
        },
        {
            "page_number": 2,
            "page_title": "Tangential Velocity Vectors in Uniform Circular Motion",
            "block_type": "suggested_diagram",
            "component_type": "suggested_diagram",
            "content": {
                "text": "Geometric diagram showing an object moving in a circular path of radius r with tangential velocity vectors v perpendicular to the radius at multiple positions.",
                "instruction": (
                    "Draw a circular path with centre O and radius r. Place the moving object at 4 cardinal positions (Top, Right, Bottom, Left). "
                    "At each point, draw a velocity vector arrow v tangent to the circle, showing that velocity is perpendicular to the radius line."
                )
            }
        },
        # Page 3: The Radian
        {
            "page_number": 3,
            "page_title": "Defining the Radian: The Natural Unit of Angle",
            "block_type": "definition_card",
            "component_type": "definition_card",
            "content": {
                "term": "The Radian (rad)",
                "definition": (
                    "**One radian ($\\text{rad}$)** is the angle subtended at the centre of a circle by an arc whose length ($s$) "
                    "is exactly equal to the radius ($r$) of the circle.\n\n"
                    "$$\\theta = \\frac{\\text{Arc Length } (s)}{\\text{Radius } (r)}$$\n\n"
                    "When the arc length $s = r$, the angle $\\theta = 1\\text{ radian}$."
                )
            }
        },
        {
            "page_number": 3,
            "page_title": "Geometric Definition of 1 Radian",
            "block_type": "suggested_diagram",
            "component_type": "suggested_diagram",
            "content": {
                "text": "Geometric construction of a circle of radius r showing an arc length s equal to radius r, subtending an angle theta = 1 radian (approximately 57.3 degrees) at the centre.",
                "instruction": (
                    "Draw a circular sector with centre O and radius r. Highlight an arc of length s = r in green. "
                    "Label the central angle theta = 1 rad ≈ 57.3 degrees. Add dimension callout s = r."
                )
            }
        },
        # Page 4: Radian to Degree Conversions
        {
            "page_number": 4,
            "page_title": "Radian and Degree Conversions",
            "block_type": "comparison_table",
            "component_type": "comparison_table",
            "content": {
                "headers": ["Fraction of a Turn", "Angle in Degrees ($^\\circ$)", "Angle in Radians ($\\text{rad}$)", "Numerical Value ($\\text{rad}$)"],
                "rows": [
                    ["Quarter Turn", "$90^\\circ$", "$\\frac{\\pi}{2}$", "$\\approx 1.57\\text{ rad}$"],
                    ["Half Turn", "$180^\\circ$", "$\\pi$", "$\\approx 3.14\\text{ rad}$"],
                    ["Three-Quarter Turn", "$270^\\circ$", "$\\frac{3\\pi}{2}$", "$\\approx 4.71\\text{ rad}$"],
                    ["Full Turn (Complete Revolution)", "$360^\\circ$", "$2\\pi$", "$\\approx 6.28\\text{ rad}$"]
                ]
            }
        },
        {
            "page_number": 4,
            "page_title": "Conversion Rules for Angles",
            "block_type": "formula_breakdown",
            "component_type": "formula_breakdown",
            "content": {
                "formula": "$$\\text{Degrees to Radians: } \\theta = \\text{Angle in degrees} \\times \\frac{\\pi}{180^\\circ} \\qquad \\text{Radians to Degrees: } \\theta = \\text{Angle in radians} \\times \\frac{180^\\circ}{\\pi}$$",
                "content": (
                    "Since a complete circular revolution spans an arc length equal to its circumference ($s = 2\\pi r$):\n"
                    "$$\\theta_{\\text{full}} = \\frac{2\\pi r}{r} = 2\\pi\\text{ radians} = 360^\\circ$$\n\n"
                    "Therefore: $$\\pi\\text{ rad} = 180^\\circ \\implies 1\\text{ rad} = \\frac{180^\\circ}{\\pi} \\approx 57.296^\\circ \\approx 57.3^\\circ$$"
                )
            }
        },
        # Page 5: Angular Velocity (omega)
        {
            "page_number": 5,
            "page_title": "Angular Velocity ($\\omega$) and Linear Speed ($v$)",
            "block_type": "formula_breakdown",
            "component_type": "formula_breakdown",
            "content": {
                "formula": "$$\\omega = \\frac{\\theta}{t} = \\frac{2\\pi}{T} = 2\\pi f \\qquad \\text{and} \\qquad v = r\\omega$$",
                "content": (
                    "**Angular velocity ($\\omega$)** is the rate of change of angular displacement with time.\n\n"
                    "| Symbol | Meaning | SI Unit |\n"
                    "|---|---|---|\n"
                    "| $\\omega$ | Angular velocity | $\\text{rad s}^{-1}$ or $\\text{s}^{-1}$ |\n"
                    "| $\\theta$ | Angular displacement | Radians ($\\text{rad}$) |\n"
                    "| $t$ | Time taken | Seconds ($\\text{s}$) |\n"
                    "| $T$ | Periodic time for 1 complete revolution | Seconds ($\\text{s}$) |\n"
                    "| $f$ | Frequency of revolutions ($f = 1/T$) | $\\text{Hz}$ or $\\text{rev/s}$ |\n"
                    "| $v$ | Tangential linear speed | $\\text{m/s}$ |\n"
                    "| $r$ | Radius of circular path | Metres ($\\text{m}$) |\n\n"
                    "### Derivation of $v = r\\omega$:\n"
                    "Starting from arc length: $s = r\\theta$. Dividing both sides by time $t$:\n"
                    "$$\\frac{s}{t} = r \\left(\\frac{\\theta}{t}\\right) \\implies v = r\\omega$$"
                )
            }
        },
        # Page 6: Angular Acceleration (alpha)
        {
            "page_number": 6,
            "page_title": "Angular Acceleration ($\\alpha$)",
            "block_type": "formula_breakdown",
            "component_type": "formula_breakdown",
            "content": {
                "formula": "$$\\alpha = \\frac{\\omega_2 - \\omega_1}{t} \\qquad \\text{and} \\qquad a = r\\alpha$$",
                "content": (
                    "**Angular acceleration ($\\alpha$)** is the rate of change of angular velocity with time.\n\n"
                    "| Symbol | Meaning | SI Unit |\n"
                    "|---|---|---|\n"
                    "| $\\alpha$ | Angular acceleration | $\\text{rad s}^{-2}$ or $\\text{s}^{-2}$ |\n"
                    "| $\\omega_1, \\omega_2$ | Initial and final angular velocities | $\\text{rad s}^{-1}$ |\n"
                    "| $a$ | Tangential linear acceleration | $\\text{m/s}^2$ |\n\n"
                    "### Crucial Physical Distinction:\n"
                    "- In **Uniform Circular Motion**, the angular speed $\\omega$ is constant, so **angular acceleration $\\alpha = 0$** and tangential acceleration $a = 0$.\n"
                    "- However, the **centripetal acceleration** (directed towards the centre) is **non-zero** because velocity changes direction!"
                )
            }
        },
        # Page 7: Worked Example Level 1
        {
            "page_number": 7,
            "page_title": "Example 1: Radian & Distance Conversion",
            "block_type": "worked_example",
            "component_type": "worked_example",
            "content": {
                "problem": (
                    "A motorcycle wheel of radius $50\\text{ cm}$ rolls through a quarter turn ($90^\\circ$). Calculate:\n"
                    "(a) The angle rotated in radians.\n"
                    "(b) The distance moved by a point on the tyre's circumference in metres."
                ),
                "steps": [
                    "**Given & Required:** Radius $r = 50\\text{ cm} = 0.50\\text{ m}$; Fraction of turn $= 1/4\\text{ turn } (90^\\circ)$. Required: Angle $\\theta$ in radians, and arc distance $s$.",
                    "**(a) Angle in Radians:** $$\\theta = \\text{Turn fraction} \\times 2\\pi = \\frac{1}{4} \\times 2\\pi = \\frac{\\pi}{2} \\approx \\mathbf{1.57\\text{ rad}}$$",
                    "**(b) Linear Distance Moved ($s$):** $$s = r\\theta = 0.50\\text{ m} \\times 1.5708\\text{ rad} = \\mathbf{0.785\\text{ m}} \\text{ (or } 78.5\\text{ cm)}$$",
                    "**Physical Reasonableness Check:** A full circumference is $2\\pi r = 2 \\times 3.1416 \\times 50\\text{ cm} = 314.16\\text{ cm}$. One quarter of this is $314.16 / 4 = 78.54\\text{ cm}$, which confirms the result exactly."
                ]
            }
        },
        # Page 8: Unit Conversion Traps
        {
            "page_number": 8,
            "page_title": "Exam Traps: Radius & RPM Conversions",
            "block_type": "common_misconception",
            "component_type": "common_misconception",
            "content": {
                "text": (
                    "### 1. The Radius Trap (Centimetres to Metres)\n"
                    "Always convert radius $r$ to metres ($\\text{m}$) before substituting into circular motion equations. "
                    "Substituting $r = 80\\text{ cm}$ directly into $F_c = mr\\omega^2$ produces an answer that is $100\\times$ too large!\n\n"
                    "### 2. The RPM Trap (Revolutions Per Minute to Radians Per Second)\n"
                    "If an engine shaft rotates at $1200\\text{ RPM}$, this is frequency, not $\\omega$.\n"
                    "To convert to $\\omega$ ($\\text{rad/s}$):\n"
                    "$$\\omega = \\frac{\\text{Revolutions}}{60\\text{ s}} \\times 2\\pi = \\frac{1200}{60} \\times 2\\pi = 20 \\times 2\\pi \\approx 125.66\\text{ rad/s}$$"
                )
            }
        },
        # Page 9: Interactive Simulation / Sandbox
        {
            "page_number": 9,
            "page_title": "Interactive Exploration: The Circular Motion Sandbox",
            "block_type": "prediction",
            "component_type": "prediction",
            "content": {
                "text": (
                    "**Think & Predict Before Simulating:**\n\n"
                    "A stone of mass $m$ is tied to a string of radius $r$ and whirled in a horizontal circle at steady speed $v$. "
                    "If the string suddenly snaps when the stone is at the top of its circle:\n"
                    "1. Will the stone spiral outwards, fly radially outwards from the centre, or fly off in a straight line along the tangent?\n"
                    "2. What fundamental law of physics dictates this trajectory?"
                )
            }
        },
        {
            "page_number": 9,
            "page_title": "Interactive Circular Motion Sandbox",
            "block_type": "suggested_simulation",
            "component_type": "suggested_simulation",
            "content": {
                "text": "Interactive dynamic circular motion simulation allowing students to adjust mass m (0.05-2.0kg), radius r (0.2-2.5m), and velocity v (1-15m/s), toggle string materials (cotton/nylon/steel), visualize real-time tangential velocity and centripetal force vectors, and trigger string snap to observe tangential inertial escape.",
                "instruction": "Simulation Key: circular_motion. Real-time dynamic vector rendering of tangential velocity (red arrow) and centripetal force (blue arrow) with instant breaking alerts."
            }
        },
        {
            "page_number": 9,
            "page_title": "Reflecting on Tangential Inertia",
            "block_type": "reflection",
            "component_type": "reflection",
            "content": {
                "text": (
                    "According to Newton's First Law of Motion, matter naturally moves in a straight line at constant velocity. "
                    "The string continuously exerts an inward pull to bend this straight path into a circle. "
                    "The moment the string snaps, that inward force drops to zero, and the stone immediately continues along its instantaneous tangent line!"
                )
            }
        },
        # Page 10: Knowledge Check (MCQ)
        {
            "page_number": 10,
            "page_title": "Check Your Understanding: Angular Velocity Calculation",
            "block_type": "knowledge_check",
            "component_type": "knowledge_check",
            "content": {
                "check_type": "multiple_choice",
                "question": "A particle moves in a circular path of radius $0.40\\text{ m}$, taking $0.50\\text{ seconds}$ to complete one full revolution. What is its angular velocity ($\\omega$) and linear speed ($v$)?",
                "options": [
                    "$\\omega = 12.57\\text{ rad/s}$, $v = 5.03\\text{ m/s}$",
                    "$\\omega = 6.28\\text{ rad/s}$, $v = 2.51\\text{ m/s}$",
                    "$\\omega = 3.14\\text{ rad/s}$, $v = 1.26\\text{ m/s}$",
                    "$\\omega = 12.57\\text{ rad/s}$, $v = 12.57\\text{ m/s}$"
                ],
                "answer": "A",
                "explanation": (
                    "1. Angular velocity: omega = 2*pi / T = (2 * 3.1416) / 0.50 s = 12.566 rad/s (approx 12.57 rad/s).\n"
                    "2. Linear speed: v = r * omega = 0.40 m * 12.566 rad/s = 5.027 m/s (approx 5.03 m/s)."
                )
            }
        },
        # Page 11: Knowledge Check (True/False)
        {
            "page_number": 11,
            "page_title": "Check Your Understanding: Acceleration in Circular Paths",
            "block_type": "knowledge_check",
            "component_type": "knowledge_check",
            "content": {
                "check_type": "true_false",
                "question": "In uniform circular motion, because the speed of the body remains constant, its acceleration is exactly zero.",
                "options": ["True", "False"],
                "answer": "False",
                "explanation": (
                    "False. Velocity is a vector quantity with both magnitude (speed) and direction. Even though speed is constant, the direction of motion continuously changes at every instant, creating a continuous inward centripetal acceleration (a_c = v^2 / r)."
                )
            }
        },
        # Page 12: Summary & Key Takeaways
        {
            "page_number": 12,
            "page_title": "Module 2.1 Summary: Kinematics of Circular Motion",
            "block_type": "summary",
            "component_type": "summary",
            "content": {
                "text": (
                    "### Key Relationships:\n"
                    "- **Radian Definition**: $\\theta = \\frac{s}{r}$, where $2\\pi\\text{ rad} = 360^\\circ$ and $1\\text{ rad} \\approx 57.3^\\circ$\n"
                    "- **Linear vs. Angular Displacement**: $s = r\\theta$\n"
                    "- **Linear vs. Angular Velocity**: $v = r\\omega$, where $\\omega = \\frac{\\theta}{t} = \\frac{2\\pi}{T} = 2\\pi f$\n"
                    "- **Linear vs. Angular Acceleration**: $a = r\\alpha$, where $\\alpha = \\frac{\\Delta\\omega}{t}$ (and $\\alpha = 0$ for uniform motion)\n"
                    "- **Tangential Direction**: Instantaneous velocity is always directed along the tangent perpendicular to the radius."
                )
            }
        },
        {
            "page_number": 12,
            "page_title": "Core Takeaways on Angular Motion",
            "block_type": "key_takeaway",
            "component_type": "key_takeaway",
            "content": {
                "text": "Uniform circular motion combines constant linear speed with continuous inward acceleration due to relentless directional change."
            }
        }
    ]
}


# =============================================================================
# MODULE 2.2 DATA — Centripetal Dynamics, Vertical Circles & Experiments
# =============================================================================
MODULE_2_2 = {
    "unit_name": "Module 2.2: Centripetal Dynamics, Vertical Circles, and Laboratory Experiments",
    "unit_order": 2,
    "lesson_title": "Centripetal Dynamics, Vertical Circles, and Laboratory Experiments",
    "cards": [
        # Page 1: Hook & Goals
        {
            "page_number": 1,
            "page_title": "The Inward Pull: Dynamics of Circular Motion",
            "block_type": "learning_goal",
            "component_type": "learning_goal",
            "content": {
                "text": (
                    "According to Newton's Second Law of Motion ($F = ma$), any body that accelerates must experience a net external force "
                    "acting in the direction of that acceleration. Since centripetal acceleration is directed towards the centre of the circle, "
                    "there must be a net inward force sustaining the motion—the centripetal force ($F_c$).\n\n"
                    "In this module, you will master the dynamics of horizontal and vertical circular motion, understand why centripetal force is a 'role' "
                    "fulfilled by real physical forces, and learn how to determine centripetal relationships experimentally in the laboratory.\n\n"
                    "By the end of this lesson, you will be able to:\n"
                    "- Calculate centripetal acceleration ($a_c$) and centripetal force ($F_c$)\n"
                    "- Identify the real physical forces acting in the centripetal role across various situations\n"
                    "- Analyze string tension and critical slackening speeds in vertical circular motion\n"
                    "- Execute the laboratory experiment investigating centripetal force and interpret the $T$ vs $\\omega^2$ linear graph\n"
                    "- Apply the VLearn 8-step framework to multi-tier dynamic calculations"
                )
            }
        },
        # Page 2: Centripetal Acceleration Formulas
        {
            "page_number": 2,
            "page_title": "Centripetal Acceleration ($a_c$)",
            "block_type": "formula_breakdown",
            "component_type": "formula_breakdown",
            "content": {
                "formula": "$$a_c = \\frac{v^2}{r} = r\\omega^2$$",
                "content": (
                    "**Centripetal acceleration ($a_c$)** is the inward-directed acceleration that keeps an object in circular motion.\n\n"
                    "| Symbol | Meaning | SI Unit |\n"
                    "|---|---|---|\n"
                    "| $a_c$ | Centripetal acceleration | $\\text{m/s}^2$ |\n"
                    "| $v$ | Tangential linear speed | $\\text{m/s}$ |\n"
                    "| $r$ | Radius of circular path | $\\text{m}$ |\n"
                    "| $\\omega$ | Angular velocity | $\\text{rad/s}$ |\n\n"
                    "**Direction**: Always directed radially inwards, pointing directly toward the centre of the circular path."
                )
            }
        },
        # Page 3: Centripetal Force Formulas
        {
            "page_number": 3,
            "page_title": "Centripetal Force ($F_c$)",
            "block_type": "formula_breakdown",
            "component_type": "formula_breakdown",
            "content": {
                "formula": "$$F_c = m a_c = \\frac{mv^2}{r} = mr\\omega^2$$",
                "content": (
                    "**Centripetal force ($F_c$)** is the net inward force required to maintain circular motion.\n\n"
                    "| Symbol | Meaning | SI Unit |\n"
                    "|---|---|---|\n"
                    "| $F_c$ | Centripetal force | Newtons ($\\text{N}$) |\n"
                    "| $m$ | Mass of the revolving body | Kilograms ($\\text{kg}$) |\n"
                    "| $v$ | Linear speed | $\\text{m/s}$ |\n"
                    "| $r$ | Radius of path | $\\text{m}$ |\n"
                    "| $\\omega$ | Angular velocity | $\\text{rad/s}$ |"
                )
            }
        },
        # Page 4: Centripetal Force is a "Role", Not a New Force
        {
            "page_number": 4,
            "page_title": "The 'Role' Principle: Real Physical Forces in Action",
            "block_type": "comparison_table",
            "component_type": "comparison_table",
            "content": {
                "headers": ["Physical Scenario", "Moving Body", "Real Physical Force Acting as Centripetal Force", "Formula Expression"],
                "rows": [
                    ["Stone Whirled on a String", "The stone", "Tension ($T$) in the string", "$T = \\frac{mv^2}{r}$"],
                    ["Car Turning a Flat Road Bend", "The car", "Sideways static friction ($f$) between tyres and road", "$f = \\mu mg = \\frac{mv^2}{r}$"],
                    ["Planet Orbiting the Sun", "The planet", "Gravitational force ($F_g$) of the Sun", "$F_g = \\frac{GMm}{r^2} = \\frac{mv^2}{r}$"],
                    ["Electron Orbiting an Atomic Nucleus", "The electron", "Electrostatic attractive force ($F_e$)", "$F_e = \\frac{kq_1 q_2}{r^2} = \\frac{mv^2}{r}$"],
                    ["Spin Dryer Drum", "Water droplets", "Normal reaction ($R$) from the perforated drum wall", "$R = \\frac{mv^2}{r}$ (drops escape where holes exist)"]
                ]
            }
        },
        # Page 5: Worked Example Level 2
        {
            "page_number": 5,
            "page_title": "Example 2: Cornering Speed & Tyre Friction",
            "block_type": "worked_example",
            "component_type": "worked_example",
            "content": {
                "problem": (
                    "A car of mass $6.0 \\times 10^3\\text{ kg}$ is driven around a flat, horizontal curve of radius $250\\text{ m}$. "
                    "If the maximum safe static friction force between the tyres and the road is $21,000\\text{ N}$, "
                    "determine the maximum speed at which the car can negotiate the bend without skidding."
                ),
                "steps": [
                    "**Given & Required:** Mass $m = 6000\\text{ kg}$, Radius $r = 250\\text{ m}$, Maximum frictional force $F_c = 21,000\\text{ N}$. Required: Maximum linear speed $v$.",
                    "**Governing Formula:** $$F_c = \\frac{mv^2}{r}$$",
                    "**Rearranging for Unknown ($v$):** $$v^2 = \\frac{F_c \\cdot r}{m} \\implies v = \\sqrt{\\frac{F_c \\cdot r}{m}}$$",
                    "**Substitution & Calculation:** $$v = \\sqrt{\\frac{21000 \\times 250}{6000}} = \\sqrt{\\frac{5250000}{6000}} = \\sqrt{875} \\approx \\mathbf{29.58\\text{ m/s}}$$",
                    "**Answer & Physical Check:** $v = 29.58\\text{ m/s}$ (approximately $106.5\\text{ km/h}$). If the vehicle exceeds this speed, the road cannot supply sufficient centripetal friction, and the vehicle will skid outward off the bend."
                ]
            }
        },
        # Page 6: Vertical Circle Dynamics
        {
            "page_number": 6,
            "page_title": "Dynamics of Motion in a Vertical Circle",
            "block_type": "concept_explanation",
            "component_type": "concept_explanation",
            "content": {
                "text": (
                    "When an object is whirled in a vertical plane, gravity continuously alters the string tension ($T$) as the object ascends and descends:\n\n"
                    "### Position 1: The Top of the Circle\n"
                    "- Both the tension $T_1$ and weight $mg$ act **downwards towards the centre**:\n"
                    "$$T_1 + mg = \\frac{mv^2}{r} \\implies \\mathbf{T_1 = \\frac{mv^2}{r} - mg}$$\n\n"
                    "### Position 2: The Horizontal (Midpoint)\n"
                    "- Weight $mg$ acts perpendicular to the string, providing zero radial force. Centripetal force is supplied entirely by tension:\n"
                    "$$\\mathbf{T_2 = \\frac{mv^2}{r}}$$\n\n"
                    "### Position 3: The Bottom of the Circle\n"
                    "- Tension $T_3$ acts **upwards (towards centre)** while weight $mg$ acts **downwards (away from centre)**:\n"
                    "$$T_3 - mg = \\frac{mv^2}{r} \\implies \\mathbf{T_3 = \\frac{mv^2}{r} + mg}$$\n\n"
                    "**Critical Conclusion**: Tension is at its absolute maximum at the bottom of the circle ($T_3$). A whirled string is **most likely to snap at the lowest point** because it must fight against gravity while pulling the mass into the curve."
                )
            }
        },
        {
            "page_number": 6,
            "page_title": "Force Resolution in a Vertical Circle",
            "block_type": "suggested_diagram",
            "component_type": "suggested_diagram",
            "content": {
                "text": "Force diagrams comparing tension T and weight mg at the top, horizontal midpoint, and bottom of a vertical circular path.",
                "instruction": (
                    "Draw a vertical circle with centre O. Show whirled mass at Top (T1 down, mg down), Midpoint (T2 inward, mg downward), "
                    "and Bottom (T3 upward, mg downward). Annotate bottom as 'Maximum Tension - String Snaps Here'."
                )
            }
        },
        # Page 7: Slackening Limit at the Top
        {
            "page_number": 7,
            "page_title": "Critical Minimum Speed & String Slackening at the Top",
            "block_type": "formula_breakdown",
            "component_type": "formula_breakdown",
            "content": {
                "formula": "$$v_{\\text{min}} = \\sqrt{rg}$$",
                "content": (
                    "As the speed of the whirled object decreases at the top of the circle, the required centripetal force decreases. "
                    "Since weight $mg$ is fixed, string tension $T_1 = \\frac{mv^2}{r} - mg$ decreases.\n\n"
                    "### The Slackening Threshold ($T_1 = 0$):\n"
                    "If tension drops to zero ($T_1 = 0$), the string goes slack, and gravity alone provides the exact centripetal force required to prevent the object from falling inwards:\n"
                    "$$0 + mg = \\frac{m v_{\\text{min}}^2}{r} \\implies v_{\\text{min}}^2 = rg \\implies \\mathbf{v_{\\text{min}} = \\sqrt{rg}}$$\n\n"
                    "- If $v < \\sqrt{rg}$, the string collapses and the object falls out of its circular trajectory."
                )
            }
        },
        # Page 8: Worked Example Level 3
        {
            "page_number": 8,
            "page_title": "Example 3: Tension at the Bottom of a Vertical Circle",
            "block_type": "worked_example",
            "component_type": "worked_example",
            "content": {
                "problem": (
                    "A stone of mass $0.15\\text{ kg}$ is tied to a string of length $80\\text{ cm}$ and whirled in a vertical circle. "
                    "If the stone passes the lowest point of the circle at a speed of $6.0\\text{ m/s}$, "
                    "calculate the tension in the string at this lowest point. (Take $g = 10\\text{ m/s}^2$)."
                ),
                "steps": [
                    "**Given & Units:** Mass $m = 0.15\\text{ kg}$, Radius $r = 80\\text{ cm} = 0.80\\text{ m}$, Speed at bottom $v = 6.0\\text{ m/s}$, $g = 10\\text{ m/s}^2$. Required: Bottom tension $T_3$.",
                    "**Governing Formula:** $$T_3 = \\frac{mv^2}{r} + mg$$",
                    "**Centripetal Component:** $$F_c = \\frac{0.15 \\times 6.0^2}{0.80} = \\frac{0.15 \\times 36}{0.80} = \\frac{5.4}{0.80} = 6.75\\text{ N}$$",
                    "**Weight Component:** $$W = mg = 0.15 \\times 10 = 1.50\\text{ N}$$",
                    "**Total Bottom Tension:** $$T_3 = 6.75\\text{ N} + 1.50\\text{ N} = \\mathbf{8.25\\text{ N}}$$",
                    "**Physical Reasonableness Check:** Tension ($8.25\\text{ N}$) is greater than both the object's weight ($1.5\\text{ N}$) and the purely dynamic centripetal force ($6.75\\text{ N}$), matching physical theory."
                ]
            }
        },
        # Page 9: Worked Example Level 4
        {
            "page_number": 9,
            "page_title": "Example 4: Critical Minimum Speed at the Top",
            "block_type": "worked_example",
            "component_type": "worked_example",
            "content": {
                "problem": (
                    "Using the same apparatus ($m = 0.15\\text{ kg}$, string length $r = 80\\text{ cm}$), determine the minimum speed "
                    "at which the stone can pass the highest point of the vertical circle without the string collapsing. (Take $g = 10\\text{ m/s}^2$)."
                ),
                "steps": [
                    "**Given & Required:** Radius $r = 0.80\\text{ m}$, $g = 10\\text{ m/s}^2$. Required: Minimum speed $v_{\\text{min}}$ at $T_1 = 0$.",
                    "**Governing Formula:** $$v_{\\text{min}} = \\sqrt{rg}$$",
                    "**Substitution & Calculation:** $$v_{\\text{min}} = \\sqrt{0.80 \\times 10} = \\sqrt{8.0} \\approx \\mathbf{2.83\\text{ m/s}}$$",
                    "**Physical Reality & Syllabus Note:** At this critical speed of $2.83\\text{ m/s}$, tension is zero and the stone is momentarily in free fall around the top curve. Any speed below $2.83\\text{ m/s}$ will cause the string to go slack."
                ]
            }
        },
        # Page 10: Experimental Physics Setup
        {
            "page_number": 10,
            "page_title": "Experimental Physics: Investigating Centripetal Force",
            "block_type": "step_process",
            "component_type": "step_process",
            "content": {
                "title": "Laboratory Investigation Protocol",
                "steps": [
                    "**Aim:** To investigate the relationship between centripetal force ($F_c$), mass ($m$), radius ($r$), and angular velocity ($\\omega$).",
                    "**Apparatus Required:** Fire-polished glass tube ($15\\text{ cm}$), thick nylon string ($1.5\\text{ m}$), rubber bung of mass $m$, slotted mass hanger ($M$), paper clip marker, stopwatch, metre rule, triple-beam balance.",
                    "**Variable Identification:** Independent: Dangling mass $M$ (controlling tension $T = Mg$) and radius $r$. Dependent: Time for 10 revolutions ($t$), used to find $\\omega$. Controlled: Whirling rubber bung mass ($m$).",
                    "**Procedure:** Thread nylon string through glass tube. Tie rubber bung ($m$) to top end and suspend slotted weights ($M$) at bottom. Place paper clip marker $2\\text{ mm}$ below bottom of tube. Whirl bung in horizontal circle until marker stays stationary, then time 10 complete revolutions."
                ]
            }
        },
        {
            "page_number": 10,
            "page_title": "Laboratory Setup for Centripetal Force Investigation",
            "block_type": "suggested_diagram",
            "component_type": "suggested_diagram",
            "content": {
                "text": "Laboratory apparatus diagram showing rubber bung whirled in a horizontal circle at radius r via a nylon string threaded through a vertical glass tube, with paper clip marker and dangling slotted mass M providing tension T = Mg.",
                "instruction": (
                    "Draw a vertical glass tube held in hand. Show nylon string exiting top connected to a rubber bung of mass m whirling in a horizontal circle of radius r. "
                    "Show paper clip marker just below tube base, and dangling slotted weight M hanging from bottom of string providing tension T = Mg."
                )
            }
        },
        # Page 11: Experimental Data & Graph Analysis
        {
            "page_number": 11,
            "page_title": "Data Collection & Graphical Analysis: $T$ vs. $\\omega^2$",
            "block_type": "comparison_table",
            "component_type": "comparison_table",
            "content": {
                "headers": ["Trial", "Dangling Mass $M$ (kg)", "Tension $T = Mg$ (N)", "Radius $r$ (m)", "Time for 10 revs $t$ (s)", "Period $T_p = t/10$ (s)", "Angular Velocity $\\omega$ (rad/s)", "$\\omega^2$ ($\\text{rad}^2/\\text{s}^2$)"],
                "rows": [
                    ["1", "0.10", "1.00", "0.80", "11.20", "1.12", "5.61", "31.47"],
                    ["2", "0.15", "1.50", "0.80", "9.15", "0.915", "6.87", "47.20"],
                    ["3", "0.20", "2.00", "0.80", "7.92", "0.792", "7.93", "62.89"],
                    ["4", "0.25", "2.50", "0.80", "7.08", "0.708", "8.87", "78.68"]
                ]
            }
        },
        {
            "page_number": 11,
            "page_title": "Graph Interpretation: Linear $T$ against $\\omega^2$",
            "block_type": "suggested_graph",
            "component_type": "suggested_graph",
            "content": {
                "text": "Linear Cartesian graph plotting Tension force T on the y-axis against angular velocity squared w^2 on the x-axis, yielding a straight line through the origin with gradient = m * r.",
                "instruction": (
                    "Plot graph of Tension T (N) on y-axis vs omega^2 (rad^2/s^2) on x-axis. "
                    "Draw straight line passing through origin (0,0). "
                    "Annotate: Gradient = delta T / delta(omega^2) = m * r. Compare with product of bung mass and radius."
                )
            }
        },
        {
            "page_number": 11,
            "page_title": "Deriving the Experimental Graph Equation",
            "block_type": "concept_explanation",
            "component_type": "concept_explanation",
            "content": {
                "text": (
                    "### Derivation of the Linear Relationship:\n"
                    "The tension in the string equals the centripetal force required to keep the rubber bung revolving:\n"
                    "$$T = F_c = m r \\omega^2$$\n\n"
                    "Comparing this to the standard linear equation $y = mx + c$ where $y = T$ and $x = \\omega^2$:\n"
                    "$$T = (mr) \\cdot \\omega^2 + 0$$\n\n"
                    "- **Straight Line through Origin**: The y-intercept is zero ($c = 0$).\n"
                    "- **Gradient**: $$\\mathbf{\\text{Gradient} = m \\cdot r}$$\n"
                    "- By measuring the gradient from your experimental line and dividing by the known radius $r$, you can determine the unknown mass of the rubber bung ($m = \\frac{\\text{Gradient}}{r}$) with high precision!"
                )
            }
        },
        # Page 12: Sources of Laboratory Error
        {
            "page_number": 12,
            "page_title": "Sources of Laboratory Error and Improvements",
            "block_type": "common_misconception",
            "component_type": "common_misconception",
            "content": {
                "text": (
                    "### 1. Friction at the Glass Tube Rim\n"
                    "**Issue**: Friction between the nylon string and the glass lip opposes the tension force, requiring slightly higher angular speeds.\n"
                    "**Improvement**: Use a fire-polished glass tube with smooth rounded lips, or apply a drop of light silicone oil.\n\n"
                    "### 2. Paper Clip Marker Drift (Radius Instability)\n"
                    "**Issue**: Keeping the marker steady $2\\text{ mm}$ below the tube by eye during rapid rotation is challenging.\n"
                    "**Improvement**: Position an electronic light gate or mirror grid behind the tube to verify marker alignment continuously.\n\n"
                    "### 3. Human Reaction Time Uncertainty\n"
                    "**Issue**: Starting and stopping the manual stopwatch introduces a $\\approx 0.2\\text{ s}$ timing uncertainty.\n"
                    "**Improvement**: Time 10 or 20 complete revolutions rather than a single turn to minimize percentage error."
                )
            }
        },
        # Page 13: Knowledge Check: Vertical Circle
        {
            "page_number": 13,
            "page_title": "Check Your Understanding: Vertical Circle Mechanics",
            "block_type": "knowledge_check",
            "component_type": "knowledge_check",
            "content": {
                "check_type": "multiple_choice",
                "question": "A stone is whirled in a vertical circle. At which position is the string tension at its absolute maximum, and why?",
                "options": [
                    "At the bottom of the circle, because tension must provide centripetal force and support the object's weight ($T = mv^2/r + mg$)",
                    "At the top of the circle, because velocity is highest at the top ($T = mv^2/r - mg$)",
                    "At the horizontal midpoint, because weight acts perpendicular to the string ($T = mv^2/r$)",
                    "Tension remains completely uniform at all points along the circular path"
                ],
                "answer": "A",
                "explanation": (
                    "At the lowest point (bottom), tension acts upward towards the centre while weight mg pulls downward away from the centre. "
                    "The net inward centripetal force is T - mg = mv^2/r, making total tension T = mv^2/r + mg, which is the maximum value anywhere on the path."
                )
            }
        },
        # Page 14: Knowledge Check: Centripetal Force Calculation
        {
            "page_number": 14,
            "page_title": "Check Your Understanding: Centripetal Force Calculation",
            "block_type": "knowledge_check",
            "component_type": "knowledge_check",
            "content": {
                "check_type": "multiple_choice",
                "question": "A stone of mass $0.20\\text{ kg}$ is tied to a string of length $0.50\\text{ m}$ and whirled in a horizontal circle at an angular velocity of $6.0\\text{ rad/s}$. What is the tension ($T$) in the string?",
                "options": [
                    "$T = 3.60\\text{ N}$",
                    "$T = 7.20\\text{ N}$",
                    "$T = 1.80\\text{ N}$",
                    "$T = 0.60\\text{ N}$"
                ],
                "answer": "A",
                "explanation": (
                    "Tension T = F_c = m * r * omega^2 = 0.20 kg * 0.50 m * (6.0 rad/s)^2 = 0.10 * 36 = 3.60 N."
                )
            }
        },
        # Page 15: Summary & Key Takeaways
        {
            "page_number": 15,
            "page_title": "Module 2.2 Summary: Centripetal Dynamics & Experiments",
            "block_type": "summary",
            "component_type": "summary",
            "content": {
                "text": (
                    "### Key Formulas & Insights:\n"
                    "- **Centripetal Acceleration**: $a_c = \\frac{v^2}{r} = r\\omega^2$ (radially inward)\n"
                    "- **Centripetal Force**: $F_c = \\frac{mv^2}{r} = mr\\omega^2$\n"
                    "- **Vertical Circle Dynamics**: Top $T_1 = \\frac{mv^2}{r} - mg$; Midpoint $T_2 = \\frac{mv^2}{r}$; Bottom $T_3 = \\frac{mv^2}{r} + mg$\n"
                    "- **Slackening Limit**: $v_{\\text{min}} = \\sqrt{rg}$ at top ($T_1 = 0$)\n"
                    "- **Experimental Plot**: Graph of $T$ vs $\\omega^2$ is linear through origin with $\\text{Gradient} = m \\cdot r$."
                )
            }
        },
        {
            "page_number": 15,
            "page_title": "Core Takeaways on Circular Dynamics",
            "block_type": "key_takeaway",
            "component_type": "key_takeaway",
            "content": {
                "text": "Centripetal force is not an independent force of nature, but the net inward result of existing real forces maintaining an object in curved motion."
            }
        }
    ]
}


# =============================================================================
# MODULE 2.3 DATA — Applied Mechanical Systems & Engineering
# =============================================================================
MODULE_2_3 = {
    "unit_name": "Module 2.3: Engineering Applications and Mechanics of Circular Motion",
    "unit_order": 3,
    "lesson_title": "Engineering Applications and Mechanics of Circular Motion",
    "cards": [
        # Page 1: Hook & Goals
        {
            "page_number": 1,
            "page_title": "Harnessing Circular Motion in Engineering Systems",
            "block_type": "learning_goal",
            "component_type": "learning_goal",
            "content": {
                "text": (
                    "Circular motion principles are at the core of modern mechanical and civil engineering. "
                    "From laboratory centrifuges separating blood cells in medical clinics to banked highways that prevent high-speed vehicles "
                    "from skidding on wet asphalt, circular mechanics shape our physical world.\n\n"
                    "In this module, you will analyze the mechanics of conical pendulums, medical centrifuges, banked curves, and automatic speed governors.\n\n"
                    "By the end of this lesson, you will be able to:\n"
                    "- Resolve forces in a conical pendulum and relate semi-vertical angle $\\theta$ to angular speed $\\omega$\n"
                    "- Explain the separation mechanism of laboratory centrifuges based on particle mass and centripetal requirements\n"
                    "- Derive the banking angle equation $\\tan\\theta = \\frac{v^2}{rg}$ for curved roads and railway tracks\n"
                    "- Describe the automatic feedback regulation of a Watt mechanical speed governor\n"
                    "- Debunk the myth of 'centrifugal force' and explain why centripetal force does zero mechanical work"
                )
            }
        },
        # Page 2: The Conical Pendulum
        {
            "page_number": 2,
            "page_title": "The Conical Pendulum: 3D Circular Motion",
            "block_type": "concept_explanation",
            "component_type": "concept_explanation",
            "content": {
                "text": (
                    "A **conical pendulum** consists of a mass $M$ tied to a string of length $l$. Instead of oscillating in a 2D plane, "
                    "the bob is whirled in a horizontal circle of radius $r$ at steady angular speed $\\omega$, sweeping out a cone of semi-vertical angle $\\theta$.\n\n"
                    "### Vector Resolution of String Tension ($T$):\n"
                    "1. **Vertical Equilibrium**: The vertical component of tension balances the downward weight:\n"
                    "$$T \\cos\\theta = Mg$$\n\n"
                    "2. **Horizontal Centripetal Force**: The horizontal component of tension points towards the centre of the horizontal circle:\n"
                    "$$T \\sin\\theta = M r \\omega^2 = \\frac{M v^2}{r}$$\n\n"
                    "3. **Dividing Horizontal by Vertical Equation**:\n"
                    "$$\\frac{T \\sin\\theta}{T \\cos\\theta} = \\frac{M r \\omega^2}{Mg} \\implies \\mathbf{\\tan\\theta = \\frac{r\\omega^2}{g}}$$\n\n"
                    "- **Physical Behavior**: As angular speed $\\omega$ increases, $\\tan\\theta$ increases, causing the bob to rise and sweep out a wider circle of larger radius $r$."
                )
            }
        },
        {
            "page_number": 2,
            "page_title": "Vector Resolution of the Conical Pendulum",
            "block_type": "suggested_diagram",
            "component_type": "suggested_diagram",
            "content": {
                "text": "Vector resolution diagram of a conical pendulum showing string tension T resolved into vertical component T cos(theta) balancing gravity Mg and horizontal component T sin(theta) acting as centripetal force.",
                "instruction": (
                    "Draw a conical pendulum with string length l suspended from ceiling at angle theta to vertical. "
                    "Show bob of mass M revolving in horizontal circle of radius r. "
                    "Draw vector arrows: Tension T along string, T cos(theta) upward, Mg downward, and T sin(theta) pointing horizontally inward to circle centre."
                )
            }
        },
        # Page 3: Worked Example Level 5
        {
            "page_number": 3,
            "page_title": "Example 5: Conical Pendulum Dynamics",
            "block_type": "worked_example",
            "component_type": "worked_example",
            "content": {
                "problem": (
                    "A conical pendulum consists of a bob of mass $2.0\\text{ kg}$ whirled in a horizontal circle of radius $0.60\\text{ m}$ "
                    "at a constant angular velocity of $4.0\\text{ rad/s}$. (Take $g = 10\\text{ m/s}^2$). Calculate:\n"
                    "(a) The angle $\\theta$ that the string makes with the vertical.\n"
                    "(b) The tension $T$ in the string."
                ),
                "steps": [
                    "**Given & Required:** Mass $M = 2.0\\text{ kg}$, Radius $r = 0.60\\text{ m}$, Angular velocity $\\omega = 4.0\\text{ rad/s}$, $g = 10\\text{ m/s}^2$. Required: Angle $\\theta$ and tension $T$.",
                    "**(a) Finding Angle $\\theta$:** $$\\tan\\theta = \\frac{r\\omega^2}{g} = \\frac{0.60 \\times 4.0^2}{10} = \\frac{0.60 \\times 16}{10} = \\frac{9.60}{10} = 0.96$$ $$\\theta = \\tan^{-1}(0.96) \\approx \\mathbf{43.83^\\circ} \\text{ (or } 43.8^\\circ)$$",
                    "**(b) Finding String Tension $T$:** $$T \\cos\\theta = Mg \\implies T = \\frac{Mg}{\\cos\\theta}$$ $$T = \\frac{2.0 \\times 10}{\\cos(43.83^\\circ)} = \\frac{20}{0.7214} \\approx \\mathbf{27.72\\text{ N}}$$",
                    "**Physical Reality Check:** The string tension ($27.72\\text{ N}$) must be greater than the stationary weight ($20\\text{ N}$) because it simultaneously supports the bob's weight and supplies the inward centripetal acceleration."
                ]
            }
        },
        # Page 4: The Centrifuge
        {
            "page_number": 4,
            "page_title": "The Centrifuge: Rapid Particle Separation",
            "block_type": "concept_explanation",
            "component_type": "concept_explanation",
            "content": {
                "text": (
                    "A **centrifuge** is a high-speed rotating rotor containing test tube holders used in medical clinics and chemical laboratories "
                    "to separate suspended solid particles or blood cells from liquid plasma.\n\n"
                    "### Physical Mechanism of Separation:\n"
                    "- To keep any particle of mass $m$ rotating in a circle of radius $r$ at speed $v$, an inward centripetal force "
                    "$$F_c = \\frac{mv^2}{r}$$ must be supplied by the surrounding liquid pressure.\n"
                    "- **More massive solid particles ($m_1$)** require a vastly larger centripetal force to turn along the circular path than lighter liquid molecules ($m_2$).\n"
                    "- The liquid cannot provide sufficient inward force to turn the dense particles sharply.\n"
                    "- Consequently, the dense particles drift outward along straighter inertial paths to the bottom (outermost edge) of the centrifuge tubes.\n"
                    "- This process completes in minutes what would take hours or days under natural gravitational sedimentation."
                )
            }
        },
        {
            "page_number": 4,
            "page_title": "Centrifuge Separation Mechanism by Particle Mass",
            "block_type": "suggested_diagram",
            "component_type": "suggested_diagram",
            "content": {
                "text": "Cross-sectional diagram of a rotating centrifuge showing test tubes swung outwards into a horizontal plane, with heavy dense particles driven to the outer tube bottom while lighter liquid remains near the top.",
                "instruction": (
                    "Draw a central rotating spindle with two angled tube arms. Show tubes swung horizontally at high speed. "
                    "Illustrate red blood cells / heavy particles concentrated at outer tube tips (bottom) and clear supernatant fluid at inner top."
                )
            }
        },
        # Page 5: Banked Roads & Tracks
        {
            "page_number": 5,
            "page_title": "Banked Tracks: Civil Engineering for Safer Cornering",
            "block_type": "concept_explanation",
            "component_type": "concept_explanation",
            "content": {
                "text": (
                    "When a car turns a flat, unbanked corner, centripetal force relies solely on sideways tyre friction ($f = \\frac{mv^2}{r}$). "
                    "If the road is wet, icy, or muddy, friction drops and the vehicle skids off the road.\n\n"
                    "### The Engineering Solution: Road Banking\n"
                    "Civil engineers raise the outer edge of the road, tilting the surface at an angle $\\theta$ to the horizontal.\n\n"
                    "### Physics of the Banked Road (Without Relying on Friction):\n"
                    "- The normal reaction force ($R$) from the road tilts inward at angle $\\theta$ to the vertical.\n"
                    "- **Vertical Balance**: $R \\cos\\theta = mg$\n"
                    "- **Horizontal Centripetal Force**: $R \\sin\\theta = \\frac{mv^2}{r}$\n"
                    "- **Dividing Equations**:\n"
                    "$$\\frac{R \\sin\\theta}{R \\cos\\theta} = \\frac{\\frac{mv^2}{r}}{mg} \\implies \\mathbf{\\tan\\theta = \\frac{v^2}{rg}}$$\n\n"
                    "**Key Takeaway**: At the design speed $v = \\sqrt{rg \\tan\\theta}$, a vehicle can negotiate the curve perfectly safely even on frictionless ice!"
                )
            }
        },
        {
            "page_number": 5,
            "page_title": "Normal Reaction Force Resolution on a Banked Road",
            "block_type": "suggested_diagram",
            "component_type": "suggested_diagram",
            "content": {
                "text": "Cross-sectional force diagram of a car on a road banked at angle theta to the horizontal, showing normal reaction R resolved into R cos(theta) vertically balancing gravity mg, and R sin(theta) horizontally supplying centripetal force.",
                "instruction": (
                    "Draw an inclined road surface at angle theta to horizontal. Place a vehicle rear cross-section on the slope. "
                    "Draw normal reaction vector R perpendicular to road. Draw R cos(theta) upward, mg downward, and horizontal vector R sin(theta) pointing to curve centre."
                )
            }
        },
        # Page 6: Mechanical Speed Governor
        {
            "page_number": 6,
            "page_title": "The Mechanical Speed Governor: Automatic Feedback Control",
            "block_type": "concept_explanation",
            "component_type": "concept_explanation",
            "content": {
                "text": (
                    "Invented by James Watt to regulate steam engines, the **centrifugal speed governor** uses rotating flyball masses "
                    "to automatically throttle engine fuel intake:\n\n"
                    "### How the Mechanism Operates:\n"
                    "1. The central vertical spindle is geared to the rotating engine shaft.\n"
                    "2. Two heavy metallic flyballs ($m$) are hinged to arms connected to a sliding collar.\n"
                    "3. **If Engine Speeds Up ($+\\omega$)**: The flyballs require greater centripetal force and swing outwards to a larger radius. "
                    "This motion lifts the sliding collar upwards.\n"
                    "4. The rising collar pushes a mechanical linkage that **narrows the steam/fuel throttle valve**, reducing engine speed.\n"
                    "5. **If Engine Slows Down ($-\\omega$)**: The flyballs drop inward, lowering the collar, opening the valve, and restoring speed."
                )
            }
        },
        {
            "page_number": 6,
            "page_title": "Watt Centrifugal Mechanical Speed Governor",
            "block_type": "suggested_diagram",
            "component_type": "suggested_diagram",
            "content": {
                "text": "Engineering schematic of a James Watt centrifugal flyball speed governor showing central rotating spindle, hinged flyball masses, sliding collar, and mechanical linkage to the steam throttle valve.",
                "instruction": (
                    "Draw vertical central spindle with bevel drive gear at base. Draw two symmetrical heavy spherical flyballs on hinged arms. "
                    "Show lower links connecting balls to sliding collar on spindle, and linkage arm connecting collar to steam valve butterfly disc."
                )
            }
        },
        # Page 7: Engineering Systems Comparison
        {
            "page_number": 7,
            "page_title": "Comparative Matrix: Applied Circular Motion Systems",
            "block_type": "comparison_table",
            "component_type": "comparison_table",
            "content": {
                "headers": ["Engineering System", "Primary Mechanism", "Centripetal Force Source", "Key Governing Equation"],
                "rows": [
                    ["Conical Pendulum", "Mass whirled in horizontal circle sweeping out 3D cone", "Horizontal component of string tension ($T \\sin\\theta$)", "$\\tan\\theta = \\frac{r\\omega^2}{g}$"],
                    ["Laboratory Centrifuge", "High-speed spinning rotor for mixture separation", "Inward liquid pressure gradient", "$F_c = \\frac{mv^2}{r}$"],
                    ["Banked Track / Highway", "Tilted roadway surface eliminating sideways skid", "Horizontal component of normal reaction ($R \\sin\\theta$)", "$\\tan\\theta = \\frac{v^2}{rg}$"],
                    ["Speed Governor", "Rotating flyballs regulating fuel throttle via sliding collar", "Component of hinged arm tension", "Spindle speed $\\omega \\propto$ collar lift"]
                ]
            }
        },
        # Page 8: Misconception: Centrifugal Force Myth
        {
            "page_number": 8,
            "page_title": "The Myth of 'Centrifugal Force'",
            "block_type": "common_misconception",
            "component_type": "common_misconception",
            "content": {
                "text": (
                    "### The Common Student Myth:\n"
                    "\"When an object moves in a circle, there is an outward 'centrifugal force' balancing the inward centripetal force to keep it in equilibrium.\"\n\n"
                    "### The Rigorous Scientific Reality:\n"
                    "**Centrifugal force does not exist as a real physical force!** It is an imaginary 'pseudo-force' (apparent force) felt only from inside a rotating, non-inertial frame of reference.\n\n"
                    "- In the real inertial world (viewed from outside), there is **only one radial force acting**: the inward **centripetal force**.\n"
                    "- The outward sensation you feel in a turning matatu is simply your body's **inertia** (Newton's First Law) attempting to continue traveling in a straight line while the car seat pulls you inward into the curve."
                )
            }
        },
        # Page 9: Misconception: Zero Work Done by Centripetal Force
        {
            "page_number": 9,
            "page_title": "Why Centripetal Force Does Zero Mechanical Work",
            "block_type": "common_misconception",
            "component_type": "common_misconception",
            "content": {
                "text": (
                    "### Why Work Done is Exactly Zero:\n"
                    "In physics, mechanical work is defined as: $$W = F \\cdot d \\cdot \\cos\\theta$$\n"
                    "where $\\theta$ is the angle between the applied force and the displacement direction.\n\n"
                    "- Centripetal force acts **radially inwards** toward the centre ($90^\\circ$ to the instantaneous velocity tangent).\n"
                    "- The displacement of the body at any millisecond is **along the tangent**.\n"
                    "- Since $\\theta = 90^\\circ$, we have $\\cos(90^\\circ) = 0$.\n"
                    "- Therefore: $$\\mathbf{W = F_c \\cdot d \\cdot \\cos(90^\\circ) = 0\\text{ Joules}}$$\n\n"
                    "**Physical Conclusion**: Centripetal force changes the **direction** of motion, but never changes the **speed** or **kinetic energy** of the body in uniform circular motion!"
                )
            }
        },
        # Page 10: Knowledge Check: Conical Pendulum
        {
            "page_number": 10,
            "page_title": "Check Your Understanding: Conical Pendulum Angle",
            "block_type": "knowledge_check",
            "component_type": "knowledge_check",
            "content": {
                "check_type": "multiple_choice",
                "question": "A conical pendulum bob is whirled at an increasing angular velocity ($\\omega$). What happens to the semi-vertical angle $\\theta$ and the radius of rotation $r$?",
                "options": [
                    "Both the angle $\\theta$ and radius $r$ increase ($\tan\\theta = r\\omega^2 / g$)",
                    "The angle $\\theta$ increases but radius $r$ decreases",
                    "The angle $\\theta$ decreases and radius $r$ decreases",
                    "The angle $\\theta$ remains constant regardless of angular velocity"
                ],
                "answer": "A",
                "explanation": (
                    "From the conical pendulum equation tan(theta) = r*omega^2 / g, as angular velocity omega increases, "
                    "the bob swings higher, increasing both the semi-vertical angle theta and the horizontal circular radius r."
                )
            }
        },
        # Page 11: Knowledge Check: Banked Curves
        {
            "page_number": 11,
            "page_title": "Check Your Understanding: Banked Curve Physics",
            "block_type": "knowledge_check",
            "component_type": "knowledge_check",
            "content": {
                "check_type": "multiple_choice",
                "question": "On a banked road with angle $\\theta$, what physical force provides the necessary centripetal force when a car travels at the design speed without relying on tyre friction?",
                "options": [
                    "The horizontal component of the normal reaction force ($R \\sin\\theta$)",
                    "The vertical component of the normal reaction force ($R \\cos\\theta$)",
                    "The downward force of gravity ($mg$)",
                    "Outward centrifugal force balancing friction"
                ],
                "answer": "A",
                "explanation": (
                    "When a track is banked, the normal reaction force R tilts inward at angle theta to the vertical. "
                    "Its horizontal component R sin(theta) points directly towards the centre of the curve, providing the exact centripetal force required (R sin(theta) = mv^2 / r)."
                )
            }
        },
        # Page 12: Challenge Worked Example
        {
            "page_number": 12,
            "page_title": "Challenge Problem: Cornering Friction Limits",
            "block_type": "worked_example",
            "component_type": "worked_example",
            "content": {
                "problem": (
                    "A vehicle of mass $1.2 \\times 10^3\\text{ kg}$ travels around a flat, unbanked curved track of radius $80\\text{ m}$. "
                    "If the coefficient of static friction between the tyres and the asphalt is $\\mu = 0.60$, "
                    "calculate the maximum speed the car can achieve without skidding. (Take $g = 10\\text{ m/s}^2$)."
                ),
                "steps": [
                    "**Given & Required:** Mass $m = 1200\\text{ kg}$, Radius $r = 80\\text{ m}$, Friction coefficient $\\mu = 0.60$, $g = 10\\text{ m/s}^2$. Required: Maximum safe speed $v$.",
                    "**Linking Friction and Centripetal Force:** $$F_{\\text{friction}} = \\mu N = \\mu mg$$ $$F_c = \\frac{mv^2}{r}$$",
                    "**Equating & Cancelling Mass ($m$):** $$\\frac{mv^2}{r} = \\mu mg \\implies v^2 = \\mu r g \\implies v = \\sqrt{\\mu r g}$$",
                    "**Substitution & Calculation:** $$v = \\sqrt{0.60 \\times 80 \\times 10} = \\sqrt{480} \\approx \\mathbf{21.91\\text{ m/s}} \\text{ (or } 78.9\\text{ km/h)}$$",
                    "**Physical Conclusion:** Notice that the vehicle mass $m$ cancelled completely! The safe cornering speed depends only on the curvature radius $r$, the friction coefficient $\\mu$, and gravity $g$."
                ]
            }
        },
        # Page 13: Summary & Key Takeaways
        {
            "page_number": 13,
            "page_title": "Module 2.3 Summary: Applied Circular Mechanics",
            "block_type": "summary",
            "component_type": "summary",
            "content": {
                "text": (
                    "### Key Takeaways in Applied Mechanics:\n"
                    "- **Conical Pendulum**: $T \\cos\\theta = mg$, $T \\sin\\theta = mr\\omega^2$, $\\tan\\theta = \\frac{r\\omega^2}{g}$\n"
                    "- **Centrifuge Separation**: Denser particles require larger centripetal forces and drift to outer tube tips\n"
                    "- **Banked Road Design**: $\\tan\\theta = \\frac{v^2}{rg}$, where normal reaction $R \\sin\\theta$ supplies centripetal force\n"
                    "- **Speed Governor**: Centrifugal flyballs lift a sliding collar to automatically throttle engine valves\n"
                    "- **Centrifugal Force Reality**: An apparent inertial pseudo-force, not a real force\n"
                    "- **Zero Work Done**: Centripetal force acts perpendicular to velocity ($W = 0$), preserving kinetic energy."
                )
            }
        },
        {
            "page_number": 13,
            "page_title": "Core Takeaways on Applied Circular Motion",
            "block_type": "key_takeaway",
            "component_type": "key_takeaway",
            "content": {
                "text": "By mastering vector force resolution, engineers design centrifuges, banked highways, and automatic governors that harness the physics of circular motion."
            }
        }
    ]
}

ALL_MODULES_TOPIC2 = [MODULE_2_1, MODULE_2_2, MODULE_2_3]


# =============================================================================
# INGESTION EXECUTOR
# =============================================================================

def run_ingestion_topic2(replace_mode=False):
    print("=" * 80)
    print("VLEARN FORM 4 PHYSICS — TOPIC 2: UNIFORM CIRCULAR MOTION INGESTION")
    print(f"Mode: {'REPLACE (Destructive Fresh Ingestion)' if replace_mode else 'IDEMPOTENT SAFE UPDATE'}")
    print("=" * 80)

    curriculum = Curriculum.objects.filter(name="844").first()
    grade = Grade.objects.filter(curriculum=curriculum, name="Form 4").first()
    subject = Subject.objects.filter(grade=grade, name="Physics").first()

    topic, created = Topic.objects.get_or_create(
        subject=subject,
        name="Topic 2: Uniform Circular Motion",
        defaults={
            "description": (
                "Principles of uniform circular motion, angular displacement in radians, angular velocity and acceleration, "
                "centripetal acceleration and force dynamics, vertical circular paths, laboratory experimental verification, "
                "conical pendulums, laboratory centrifuges, banked tracks, and mechanical speed governors."
            ),
            "order": 2
        }
    )
    print(f"Topic verified: {topic.name} (ID: {topic.id}) under {subject.name}\n")

    total_blocks_created = 0
    total_blocks_updated = 0

    for m_idx, m_data in enumerate(ALL_MODULES_TOPIC2, start=1):
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
    print("TOPIC 2 INGESTION COMPLETED SUCCESSFULLY!")
    print(f"Total Blocks Created: {total_blocks_created} | Total Blocks Updated: {total_blocks_updated}")
    print(f"Topic: {topic.name} (ID: {topic.id}) under Subject: {subject.name}")
    print("=" * 80)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Form 4 Physics Topic 2 Ingestion")
    parser.add_argument("--replace", action="store_true", help="Purge and replace blocks fresh")
    args = parser.parse_args()
    run_ingestion_topic2(replace_mode=args.replace)
