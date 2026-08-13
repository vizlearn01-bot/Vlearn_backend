#!/usr/bin/env python3
"""
VLearn Form 4 Mathematics — Topic 4: Trigonometry III Ingestion Script
========================================================================
Curriculum: 844
Grade: Form 4 (level=1)
Subject: Mathematics
Topic: Topic 4: Trigonometry III (order=4)

Modules / LearningUnits:
  4.1 Derivation & Application of the Pythagorean Identity
  4.2 Graphing Trigonometric Functions & Wave Parameters (Amplitude and Period)
  4.3 Advanced Wave Transformations and Phase Shifts (y = a sin(bx ± θ))
  4.4 Analytical and Graphical Solution of Trigonometric Equations

Pedagogical Structure per Lesson: 11 Pages
  Page 1:  learning_goal (Student-friendly outcomes)
  Page 2:  concept_explanation (Real-world analogies & intuition)
  Page 3:  formula_breakdown / definition_card (Core identities & parameter tables)
  Page 4:  worked_example (Level 1: Easy / Foundation)
  Page 5:  worked_example (Level 2: Moderate / Multi-step)
  Page 6:  worked_example (Level 3: Difficult / Exam standard)
  Page 7:  worked_example (Level 4: Exam-Style / Real-World Synthesis)
  Page 8:  suggested_simulation (Interactive visual sandbox)
  Page 9:  common_misconception (Diagnostic error analysis & memory tips)
  Page 10: knowledge_check (MCQ / Short-answer with delayed revelation)
  Page 11: summary (Key takeaways & formula checklist)

All content is humanized:
  - Clean responsive Markdown tables (zero raw \\begin{array} or \\hline).
  - Humanized formulas alongside KaTeX notation.
  - Rigorous mathematical accuracy (recovering textbook missing roots, correcting typos).
  - status="published" throughout.
"""

import os
import sys
import django

# Setup Django environment
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "Nexus_backend.settings")
django.setup()

from curriculum.models import (
    Curriculum, Grade, Subject, Topic,
    LearningUnit, Lesson, LessonBlock, LessonAsset
)


def get_topic4_data():
    """Returns the complete structured curriculum payload for Topic 4."""
    return [
        # =====================================================================
        # MODULE 4.1: The Fundamental Pythagorean Trigonometric Identity
        # =====================================================================
        {
            "unit_order": 1,
            "unit_title": "Module 4.1: Derivation and Application of the Pythagorean Identity",
            "lesson_title": "The Pythagorean Trigonometric Identity and Algebraic Substitution",
            "lesson_blocks": [
                # PAGE 1 — learning_goal
                {
                    "page_number": 1,
                    "page_title": "Mastering the Pythagorean Trigonometric Identity",
                    "block_type": "learning_goal",
                    "component_type": "learning_goal",
                    "content": {
                        "title": "What You Will Master in This Lesson",
                        "goals": [
                            "Derive the fundamental Pythagorean identity $\\sin^2 \\theta + \\cos^2 \\theta = 1$ geometrically from right-angled triangles and the unit circle.",
                            "Express $\\tan \\theta$ in terms of sine and cosine ratios ($\\tan \\theta = \\frac{\\sin \\theta}{\\cos \\theta}$).",
                            "Calculate exact trigonometric values without tables or calculators using right-triangle models and complementary relationships.",
                            "Use trigonometric substitution to simplify algebraic radical expressions (e.g. $\\sqrt{a^2 - x^2}$)."
                        ]
                    }
                },

                # PAGE 2 — concept_explanation
                {
                    "page_number": 2,
                    "page_title": "The Circle-Triangle Connection: Why Sine and Cosine Are Bound Together",
                    "block_type": "concept_explanation",
                    "component_type": "concept_explanation",
                    "content": {
                        "body": (
                            "In basic trigonometry, we define sine and cosine as simple fractions of triangle sides. "
                            "However, on the Cartesian coordinate plane, they are deeply connected coordinates of a rotating point.\n\n"
                            "### The Rotating Clock-Hand Analogy\n\n"
                            "Imagine a clock-hand of length $r$ pinned at the origin $O(0,0)$ on a coordinate grid:\n\n"
                            "- As the hand rotates by an angle $\\theta$, its tip reaches coordinates $(x, y)$.\n"
                            "- The horizontal distance along the ground is $x = r \\cos \\theta$.\n"
                            "- The vertical height above the center is $y = r \\sin \\theta$.\n\n"
                            "By Pythagoras' Theorem on the right-angled triangle formed by this point:\n"
                            "$$(\\text{horizontal base})^2 + (\\text{vertical height})^2 = (\\text{hypotenuse})^2$$\n"
                            "$$(r \\cos \\theta)^2 + (r \\sin \\theta)^2 = r^2$$\n"
                            "$$r^2 \\cos^2 \\theta + r^2 \\sin^2 \\theta = r^2$$\n\n"
                            "Dividing every single term by $r^2$ reveals the eternal circle identity:\n"
                            "$$\\sin^2 \\theta + \\cos^2 \\theta = 1$$\n\n"
                            "This equation is true for **every possible angle $\\theta$** across all $360^\\circ$."
                        )
                    }
                },

                # PAGE 3 — formula_breakdown
                {
                    "page_number": 3,
                    "page_title": "Core Trigonometric Identities & Conversion Rules",
                    "block_type": "formula_breakdown",
                    "component_type": "formula_breakdown",
                    "content": {
                        "formula": "**Mathematical Identity:**\n$$\\sin^2 \\theta + \\cos^2 \\theta = 1$$\n\n**In Plain English:**\n$$(\\text{Vertical Ratio})^2 + (\\text{Horizontal Ratio})^2 = 1$$",
                        "content": (
                            "### Fundamental Identities & Word Rules\n\n"
                            "| Identity Name | Symbolic Formula | Plain-English Meaning |\n"
                            "|:---|:---|:---|\n"
                            "| **Pythagorean Identity** | $\\sin^2 \\theta + \\cos^2 \\theta = 1$ | The squared vertical ratio plus the squared horizontal ratio always equals exactly $1$. |\n"
                            "| **Sine from Cosine** | $\\sin^2 \\theta = 1 - \\cos^2 \\theta$ | You can find sine directly if you know cosine. |\n"
                            "| **Cosine from Sine** | $\\cos^2 \\theta = 1 - \\sin^2 \\theta$ | You can find cosine directly if you know sine. |\n"
                            "| **Tangent Quotient Rule** | $\\tan \\theta = \\frac{\\sin \\theta}{\\cos \\theta}$ | Tangent is the ratio of vertical height to horizontal base. |\n"
                            "| **Complementary Rule** | $\\sin(90^\\circ - x) = \\cos x$ | The sine of an acute angle is the cosine of its complementary partner. |\n"
                            "| **Complementary Rule** | $\\cos(90^\\circ - x) = \\sin x$ | The cosine of an acute angle is the sine of its complementary partner. |\n\n"
                            "> **Human Rule:** When an exam says *'without using mathematical tables or a calculator'*, "
                            "draw a right-angled triangle, label the two given sides, find the third side using Pythagoras, and read off the required ratio directly."
                        )
                    }
                },

                # PAGE 4 — worked_example (Level 1: Easy / Complementary Angles Without Tables)
                {
                    "page_number": 4,
                    "page_title": "Example 1: Solving Complementary Ratios Without Tables",
                    "block_type": "worked_example",
                    "component_type": "worked_example",
                    "content": {
                        "problem": (
                            "Given that $\\sin(90^\\circ - x) = 0.8$, where $x$ is an acute angle, find the value of $\\tan x$ "
                            "without using mathematical tables or a calculator."
                        ),
                        "steps": [
                            "**What we need to find:** The exact value of $\\tan x$ as a fraction or exact decimal.",
                            "**Step 1 — Apply the complementary angle identity:**\n"
                            "We know that $\\sin(90^\\circ - x) = \\cos x$.\n"
                            "Therefore: $$\\cos x = 0.8$$",
                            "**Step 2 — Convert decimal to a simple vulgar fraction:**\n"
                            "$$\\cos x = \\frac{8}{10} = \\frac{4}{5}$$",
                            "**Step 3 — Model as a right-angled triangle:**\n"
                            "By definition: $\\cos x = \\frac{\\text{Adjacent}}{\\text{Hypotenuse}} = \\frac{4}{5}$.\n"
                            "- Adjacent side $= 4$\n"
                            "- Hypotenuse $= 5$",
                            "**Step 4 — Find the opposite side ($k$) using Pythagoras:**\n"
                            "$$k^2 + 4^2 = 5^2$$\n"
                            "$$k^2 + 16 = 25 \\implies k^2 = 9 \\implies k = 3$$",
                            "**Step 5 — Compute $\\tan x$:**\n"
                            "$$\\tan x = \\frac{\\text{Opposite}}{\\text{Adjacent}} = \\frac{3}{4} = 0.75$$\n\n"
                            "**Answer:** $\\tan x = \\frac{3}{4}$ (or $0.75$)."
                        ]
                    }
                },

                # PAGE 5 — worked_example (Level 2: Moderate / Finding Ratios via Pythagorean Identity)
                {
                    "page_number": 5,
                    "page_title": "Example 2: Finding Exact Ratios via Identity Substitution",
                    "block_type": "worked_example",
                    "component_type": "worked_example",
                    "content": {
                        "problem": (
                            "Given that $\\sin \\theta = \\frac{3}{5}$ and $\\theta$ is an acute angle, calculate the exact values of "
                            "$\\cos \\theta$ and $\\tan \\theta$ using the Pythagorean identity."
                        ),
                        "steps": [
                            "**What we need to find:** Exact values of $\\cos \\theta$ and $\\tan \\theta$.",
                            "**Step 1 — State the Pythagorean identity:**\n"
                            "$$\\cos^2 \\theta = 1 - \\sin^2 \\theta$$",
                            "**Step 2 — Substitute $\\sin \\theta = \\frac{3}{5}$:**\n"
                            "$$\\cos^2 \\theta = 1 - \\left(\\frac{3}{5}\\right)^2 = 1 - \\frac{9}{25} = \\frac{16}{25}$$",
                            "**Step 3 — Take the square root (noting $\\theta$ is acute $\\implies \\cos \\theta > 0$):**\n"
                            "$$\\cos \\theta = \\sqrt{\\frac{16}{25}} = \\frac{4}{5}$$",
                            "**Step 4 — Calculate $\\tan \\theta$ using the quotient identity:**\n"
                            "$$\\tan \\theta = \\frac{\\sin \\theta}{\\cos \\theta} = \\frac{3/5}{4/5} = \\frac{3}{4}$$\n\n"
                            "**Answer:** $\\cos \\theta = \\frac{4}{5}$ and $\\tan \\theta = \\frac{3}{4}$."
                        ]
                    }
                },

                # PAGE 6 — worked_example (Level 3: Difficult / Algebraic Radical Simplification)
                {
                    "page_number": 6,
                    "page_title": "Example 3: Simplifying Algebraic Radicals via Trigonometric Substitution",
                    "block_type": "worked_example",
                    "component_type": "worked_example",
                    "content": {
                        "problem": (
                            "Simplify the algebraic expression $\\frac{\\sqrt{9 - y^2}}{y}$ given that $y = 3 \\cos \\theta$ "
                            "and $\\theta$ is an acute angle ($0^\\circ < \\theta < 90^\\circ$)."
                        ),
                        "steps": [
                            "**What we need to simplify:** Replace variable $y$ with $3\\cos\\theta$ and simplify the radical completely.",
                            "**Step 1 — Substitute $y = 3\\cos\\theta$ into the numerator radical:**\n"
                            "$$\\sqrt{9 - y^2} = \\sqrt{9 - (3\\cos\\theta)^2} = \\sqrt{9 - 9\\cos^2\\theta}$$",
                            "**Step 2 — Factor out $9$ under the radical:**\n"
                            "$$\\sqrt{9(1 - \\cos^2\\theta)}$$",
                            "**Step 3 — Apply the Pythagorean identity $1 - \\cos^2\\theta = \\sin^2\\theta$:**\n"
                            "$$\\sqrt{9 \\sin^2 \\theta} = 3 \\sin \\theta$$"
                            "\n*(Since $\\theta$ is acute, $\\sin\\theta > 0$, so the positive square root is taken)*.",
                            "**Step 4 — Substitute back into the full fraction:**\n"
                            "$$\\frac{\\sqrt{9 - y^2}}{y} = \\frac{3\\sin\\theta}{3\\cos\\theta}$$",
                            "**Step 5 — Cancel common factor $3$ and apply $\\frac{\\sin\\theta}{\\cos\\theta} = \\tan\\theta$:**\n"
                            "$$\\frac{\\sin\\theta}{\\cos\\theta} = \\tan\\theta$$\n\n"
                            "**Answer:** $\\tan \\theta$."
                        ]
                    }
                },

                # PAGE 7 — worked_example (Level 4: Exam-Style / Proving Algebraic Identities)
                {
                    "page_number": 7,
                    "page_title": "Example 4: Proving Trigonometric Identities",
                    "block_type": "worked_example",
                    "component_type": "worked_example",
                    "content": {
                        "problem": (
                            "Prove the following trigonometric identity:\n"
                            "$$\\frac{(1 - \\cos\\theta)(1 + \\cos\\theta)}{(1 - \\sin\\theta)(1 + \\sin\\theta)} = \\tan^2\\theta$$\n"
                            "Hence evaluate the expression when $\\theta = 45^\\circ$ without using mathematical tables."
                        ),
                        "steps": [
                            "**What we need to do:** Transform the Left-Hand Side (LHS) using difference of two squares and Pythagorean identities to match the Right-Hand Side (RHS).",
                            "**Step 1 — Expand the numerator and denominator using difference of squares $(a-b)(a+b) = a^2 - b^2$:**\n"
                            "- Numerator: $(1 - \\cos\\theta)(1 + \\cos\\theta) = 1 - \\cos^2\\theta$\n"
                            "- Denominator: $(1 - \\sin\\theta)(1 + \\sin\\theta) = 1 - \\sin^2\\theta$",
                            "**Step 2 — Apply the Pythagorean identities to both parts:**\n"
                            "- Numerator: $1 - \\cos^2\\theta = \\sin^2\\theta$\n"
                            "- Denominator: $1 - \\sin^2\\theta = \\cos^2\\theta$",
                            "**Step 3 — Combine into a single fraction:**\n"
                            "$$\\frac{\\sin^2\\theta}{\\cos^2\\theta} = \\left(\\frac{\\sin\\theta}{\\cos\\theta}\\right)^2 = (\\tan\\theta)^2 = \\tan^2\\theta$$\n"
                            "**LHS = RHS** (Proved!).",
                            "**Step 4 — Evaluate at $\\theta = 45^\\circ$:**\n"
                            "We know $\\tan 45^\\circ = 1$.\n"
                            "$$\\tan^2(45^\\circ) = (1)^2 = 1$$\n\n"
                            "**Answer:** Proved; Value at $\\theta = 45^\\circ$ is $1$."
                        ]
                    }
                },

                # PAGE 8 — suggested_simulation
                {
                    "page_number": 8,
                    "page_title": "Explore: Unit Circle & Pythagorean Coordinate Explorer",
                    "block_type": "suggested_simulation",
                    "component_type": "suggested_simulation",
                    "content": {
                        "purpose": (
                            "An interactive unit circle where students can drag a rotating radius arm $OP=1$ across all four quadrants. "
                            "The simulation dynamically draws the right-angled triangle, displays $(x, y) = (\\cos\\theta, \\sin\\theta)$, "
                            "and shows the live calculation $\\cos^2\\theta + \\sin^2\\theta = 1.000$ at every angle."
                        )
                    },
                    "asset_info": {
                        "asset_type": "simulation",
                        "archetype": "math_unit_circle_pythagorean_explorer",
                        "title": "Interactive Unit Circle & Pythagorean Identity Sandbox"
                    }
                },

                # PAGE 9 — common_misconception
                {
                    "page_number": 9,
                    "page_title": "Common Error: The Square Index Fallacy",
                    "block_type": "common_misconception",
                    "component_type": "common_misconception",
                    "content": {
                        "text": (
                            "### The Index Placement Confusion\n\n"
                            "Many students mistakenly write $\\sin^2 \\theta = \\sin \\theta^2$ or think that squaring a ratio squares the angle inside.\n\n"
                            "| Notation | What It Actually Means | Test at $\\theta = 30^\\circ$ |\n"
                            "|:---|:---|:---|\n"
                            "| **$\\sin^2 \\theta$** | $(\\sin \\theta) \\times (\\sin \\theta)$ — compute sine first, then square the result. | $(\\sin 30^\\circ)^2 = (0.5)^2 = 0.25$ |\n"
                            "| **$\\sin(\\theta^2)$** | Square the angle first, then find the sine of that huge angle. | $\\sin(30^2) = \\sin(900^\\circ) = 0$ |\n\n"
                            "> **Memory Tip:** $\\sin^2 \\theta$ is just shorthand for $(\\sin \\theta)^2$. The exponent belongs to the **entire function ratio**, never to the angle alone!"
                        )
                    }
                },

                # PAGE 10 — knowledge_check (MCQ)
                {
                    "page_number": 10,
                    "page_title": "Check Your Understanding: Identity Calculations",
                    "block_type": "knowledge_check",
                    "component_type": "multiple_choice",
                    "content": {
                        "question": "Given that $\\cos(90^\\circ - \\theta) = \\frac{5}{13}$ and $\\theta$ is acute, what is the exact value of $\\tan \\theta$ without using a calculator?",
                        "options": [
                            "A: $\\frac{5}{12}$",
                            "B: $\\frac{12}{5}$",
                            "C: $\\frac{5}{13}$",
                            "D: $\\frac{12}{13}$"
                        ],
                        "answer": "A",
                        "explanation": (
                            "1. By complementary identity: $\\sin \\theta = \\cos(90^\\circ - \\theta) = \\frac{5}{13}$.\n"
                            "2. In a right triangle with opposite side $= 5$ and hypotenuse $= 13$, the adjacent side is:\n"
                            "   $$\\text{Adj} = \\sqrt{13^2 - 5^2} = \\sqrt{169 - 25} = \\sqrt{144} = 12$$\n"
                            "3. Therefore: $\\tan \\theta = \\frac{\\text{Opposite}}{\\text{Adjacent}} = \\frac{5}{12}$."
                        )
                    }
                },

                # PAGE 11 — summary
                {
                    "page_number": 11,
                    "page_title": "Key Takeaways: Pythagorean Trigonometric Identities",
                    "block_type": "summary",
                    "component_type": "summary",
                    "content": {
                        "text": (
                            "### Master Summary: Pythagorean & Complementary Identities\n\n"
                            "| Rule | Formula | Key Application |\n"
                            "|:---|:---|:---|\n"
                            "| **Fundamental Identity** | $\\sin^2 \\theta + \\cos^2 \\theta = 1$ | Express $\\sin$ in terms of $\\cos$ and vice-versa. |\n"
                            "| **Tangent Quotient** | $\\tan \\theta = \\frac{\\sin \\theta}{\\cos \\theta}$ | Convert fractional ratios to tangent without tables. |\n"
                            "| **Complementary Shift** | $\\sin(90^\\circ - x) = \\cos x$ | Swap between acute complementary angles. |\n"
                            "| **Radical Substitution** | $\\sqrt{a^2 - x^2} = a\\sin\\theta$ | Substitute $x = a\\cos\\theta$ to eliminate algebraic square roots cleanly. |\n\n"
                            "**Exam Checklist:**\n"
                            "- [x] Always write down $(\\text{Opp})^2 + (\\text{Adj})^2 = (\\text{Hyp})^2$ when solving without tables.\n"
                            "- [x] Remember that $\\cos \\theta$ is positive for acute angles ($0^\\circ < \\theta < 90^\\circ$).\n"
                            "- [x] Distinguish $(\\sin \\theta)^2 = \\sin^2 \\theta$ from $\\sin(\\theta^2)$."
                        )
                    }
                }
            ]
        },

        # =====================================================================
        # MODULE 4.2: Graphing Trigonometric Functions & Wave Parameters
        # =====================================================================
        {
            "unit_order": 2,
            "unit_title": "Module 4.2: Graphing Trigonometric Functions and Wave Parameters",
            "lesson_title": "Graphing Sine, Cosine, and Tangent Functions: Amplitude and Period",
            "lesson_blocks": [
                # PAGE 1 — learning_goal
                {
                    "page_number": 1,
                    "page_title": "Mastering Wave Parameters: Amplitude and Period",
                    "block_type": "learning_goal",
                    "component_type": "learning_goal",
                    "content": {
                        "title": "What You Will Master in This Lesson",
                        "goals": [
                            "Plot standard trigonometric graphs for $y = \\sin x$, $y = \\cos x$, and $y = \\tan x$ on grid paper.",
                            "Determine the amplitude $|a|$ of scaled functions $y = a \\sin bx$ and $y = a \\cos bx$.",
                            "Calculate the period of periodic waves using the master rule $\\text{Period} = \\frac{360^\\circ}{b}$ (or $\\frac{2\\pi}{b}$).",
                            "Recognize horizontal and vertical stretches as geometric matrix transformations."
                        ]
                    }
                },

                # PAGE 2 — concept_explanation
                {
                    "page_number": 2,
                    "page_title": "Understanding Wave Motion: The Bobbing Ocean Buoy",
                    "block_type": "concept_explanation",
                    "component_type": "concept_explanation",
                    "content": {
                        "body": (
                            "Trigonometric graphs are not just abstract curves — they are the universal language of physical waves, sound, light, and ocean tides.\n\n"
                            "### The Bobbing Buoy Analogy\n\n"
                            "Imagine a yellow buoy floating in the ocean at Mombasa:\n\n"
                            "- When water is calm, the buoy sits at height $y = 0$ (the **equilibrium center line**).\n"
                            "- As waves roll past, the buoy bobs up to a peak height and down into a trough.\n"
                            "- The maximum height it reaches above calm water is its **Amplitude ($A$)**.\n"
                            "- The horizontal distance or time it takes to complete one full up-and-down cycle is its **Period ($T$)**.\n\n"
                            "### The Three Fundamental Waves\n\n"
                            "1. **$y = \\sin x$**: Starts at $(0, 0)$, climbs to peak $(90^\\circ, 1)$, crosses center $(180^\\circ, 0)$, dips to trough $(270^\\circ, -1)$, returns to $(360^\\circ, 0)$. **Amplitude = 1, Period = $360^\\circ$**.\n"
                            "2. **$y = \\cos x$**: Starts at top peak $(0, 1)$, crosses center $(90^\\circ, 0)$, dips to trough $(180^\\circ, -1)$, climbs back to peak $(360^\\circ, 1)$. **Amplitude = 1, Period = $360^\\circ$**.\n"
                            "3. **$y = \\tan x$**: Repeats every $180^\\circ$ with vertical asymptotes (unbounded lines) at $x = 90^\\circ, 270^\\circ$. **Period = $180^\\circ$, No defined amplitude**."
                        )
                    }
                },

                # PAGE 3 — formula_breakdown
                {
                    "page_number": 3,
                    "page_title": "Master Formulas for Amplitude, Period, and Frequency",
                    "block_type": "formula_breakdown",
                    "component_type": "formula_breakdown",
                    "content": {
                        "formula": "**Mathematical Wave Model:**\n$$y = a \\sin bx \\quad \\text{or} \\quad y = a \\cos bx$$\n\n**Wave Parameter Relationships:**\n$$\\text{Amplitude} = |a| \\quad \\text{and} \\quad \\text{Period} = \\frac{360^\\circ}{b}$$",
                        "content": (
                            "### Wave Parameter Rules\n\n"
                            "| Wave Parameter | Formula (Degrees) | Formula (Radians) | Physical Effect |\n"
                            "|:---|:---|:---|:---|\n"
                            "| **Amplitude** | $\\text{Amplitude} = |a|$ | $\\text{Amplitude} = |a|$ | Vertical stretch by factor $|a|$. If $a < 0$, the wave is also reflected vertically across the x-axis. |\n"
                            "| **Period (Sine/Cosine)** | $\\text{Period} = \\frac{360^\\circ}{b}$ | $\\text{Period} = \\frac{2\\pi}{b}$ | Horizontal compression: wave repeats $b$ times within $360^\\circ$. |\n"
                            "| **Period (Tangent)** | $\\text{Period} = \\frac{180^\\circ}{b}$ | $\\text{Period} = \\frac{\\pi}{b}$ | Tangent naturally repeats twice as fast as sine and cosine. |\n\n"
                            "> **Cross-Topic Matrix Connection:** A wave $y = a\\sin(bx)$ is created by mapping the parent coordinates $(x, y)$ "
                            "via the transformation matrix:\n"
                            "$$\\begin{pmatrix} x' \\\\ y' \\end{pmatrix} = \\begin{pmatrix} \\frac{1}{b} & 0 \\\\ 0 & a \\end{pmatrix} \\begin{pmatrix} x \\\\ y \\end{pmatrix}$$"
                        )
                    }
                },

                # PAGE 4 — worked_example (Level 1: Easy / Plotting Parent Sine Wave)
                {
                    "page_number": 4,
                    "page_title": "Example 1: Plotting the Standard Wave $y = \\sin x$",
                    "block_type": "worked_example",
                    "component_type": "worked_example",
                    "content": {
                        "problem": (
                            "Complete a table of values for $y = \\sin x$ in intervals of $30^\\circ$ from $0^\\circ$ to $360^\\circ$, "
                            "and state its maximum value, minimum value, amplitude, and period."
                        ),
                        "steps": [
                            "**What we need to do:** Construct the coordinate table and extract wave parameters.",
                            "**Step 1 — Calculate coordinate table values:**\n\n"
                            "| $x$ | $0^\\circ$ | $30^\\circ$ | $60^\\circ$ | $90^\\circ$ | $120^\\circ$ | $150^\\circ$ | $180^\\circ$ | $210^\\circ$ | $240^\\circ$ | $270^\\circ$ | $300^\\circ$ | $330^\\circ$ | $360^\\circ$ |\n"
                            "|:---|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|\n"
                            "| **$y$** | $0.00$ | $0.50$ | $0.87$ | $1.00$ | $0.87$ | $0.50$ | $0.00$ | $-0.50$ | $-0.87$ | $-1.00$ | $-0.87$ | $-0.50$ | $0.00$ |",
                            "**Step 2 — Identify key peaks, troughs, and equilibrium points:**\n"
                            "- Maximum value: $y = 1.00$ at $x = 90^\\circ$\n"
                            "- Minimum value: $y = -1.00$ at $x = 270^\\circ$\n"
                            "- Equilibrium zero crossings: $x = 0^\\circ, 180^\\circ, 360^\\circ$",
                            "**Step 3 — State wave parameters:**\n"
                            "- **Amplitude:** $|a| = |1| = 1$\n"
                            "- **Period:** $360^\\circ$\n\n"
                            "**Answer:** Maximum $= 1$, Minimum $= -1$, Amplitude $= 1$, Period $= 360^\\circ$."
                        ]
                    }
                },

                # PAGE 5 — worked_example (Level 2: Moderate / Scaling Amplitude & Period)
                {
                    "page_number": 5,
                    "page_title": "Example 2: Analyzing Scaled Waves $y = 2 \\cos \\frac{1}{2} x$",
                    "block_type": "worked_example",
                    "component_type": "worked_example",
                    "content": {
                        "problem": (
                            "For the trigonometric function $y = 2 \\cos \\left(\\frac{1}{2} x\\right)$:\n"
                            "(a) State the amplitude.\n"
                            "(b) Calculate the period of the wave.\n"
                            "(c) State the maximum and minimum values of $y$."
                        ),
                        "steps": [
                            "**What we need to find:** Amplitude, period, and range of $y = 2\\cos\\left(\\frac{1}{2}x\\right)$.",
                            "**Step 1 — Identify coefficients $a$ and $b$:**\n"
                            "Comparing with $y = a \\cos bx$:\n"
                            "- Vertical scaling coefficient: $a = 2$\n"
                            "- Horizontal frequency coefficient: $b = \\frac{1}{2}$",
                            "**Step 2 — Calculate the amplitude:**\n"
                            "$$\\text{Amplitude} = |a| = |2| = 2$$",
                            "**Step 3 — Calculate the period:**\n"
                            "$$\\text{Period} = \\frac{360^\\circ}{b} = \\frac{360^\\circ}{1/2} = 360^\\circ \\times 2 = 720^\\circ$$"
                            "\n*(The wave takes $720^\\circ$ to complete one single cycle)*.",
                            "**Step 4 — Determine range of $y$:**\n"
                            "- Maximum value: $+2$\n"
                            "- Minimum value: $-2$\n\n"
                            "**Answer:** (a) Amplitude $= 2$; (b) Period $= 720^\\circ$; (c) Max $= 2$, Min $= -2$."
                        ]
                    }
                },

                # PAGE 6 — worked_example (Level 3: Difficult / Inverted Fast Wave)
                {
                    "page_number": 6,
                    "page_title": "Example 3: Transformations and Parameters of $y = -3 \\cos 2x$",
                    "block_type": "worked_example",
                    "component_type": "worked_example",
                    "content": {
                        "problem": (
                            "Describe the exact sequence of geometric transformations mapping $y = \\cos x$ onto $y = -3 \\cos 2x$, "
                            "and state its amplitude and period."
                        ),
                        "steps": [
                            "**What we need to determine:** Geometric transformation steps, amplitude, and period.",
                            "**Step 1 — Analyze horizontal coefficient $b = 2$:**\n"
                            "$$\\text{Period} = \\frac{360^\\circ}{2} = 180^\\circ$$\n"
                            "Geometric transformation: **Horizontal compression** towards the y-axis by a scale factor of $\\frac{1}{2}$.",
                            "**Step 2 — Analyze vertical coefficient $a = -3$:**\n"
                            "$$\\text{Amplitude} = |-3| = 3$$\n"
                            "Geometric transformation: **Vertical stretch** away from the x-axis by a scale factor of $3$.",
                            "**Step 3 — Account for the negative sign ($a < 0$):**\n"
                            "The negative multiplier reflects the curve across the **x-axis** (peaks become troughs and troughs become peaks).",
                            "**Step 4 — Complete sequence summary:**\n"
                            "1. Horizontal compression by factor $\\frac{1}{2}$ (Period becomes $180^\\circ$).\n"
                            "2. Vertical stretch by factor $3$ (Amplitude becomes $3$).\n"
                            "3. Reflection in the x-axis.\n\n"
                            "**Answer:** Amplitude $= 3$, Period $= 180^\\circ$."
                        ]
                    }
                },

                # PAGE 7 — worked_example (Level 4: Exam-Style / Reverse Engineering Wave Equations)
                {
                    "page_number": 7,
                    "page_title": "Example 4: Reconstructing a Wave Equation from Grid Features",
                    "block_type": "worked_example",
                    "component_type": "worked_example",
                    "content": {
                        "problem": (
                            "A sine curve passing through $(0, 0)$ reaches its first maximum peak of $y = 4$ at $x = 45^\\circ$ "
                            "and its first minimum trough of $y = -4$ at $x = 135^\\circ$.\n\n"
                            "Determine the equation of the wave in the form $y = a \\sin bx$."
                        ),
                        "steps": [
                            "**What we need to find:** Values of constants $a$ and $b$.",
                            "**Step 1 — Determine the amplitude $a$:**\n"
                            "The peak height is $4$ and the trough depth is $-4$.\n"
                            "Since the curve starts at $(0,0)$ and climbs to positive $4$, $a = +4$.",
                            "**Step 2 — Determine the period:**\n"
                            "A quarter of the sine cycle occurs from $x = 0^\\circ$ to the first peak at $x = 45^\\circ$.\n"
                            "$$\\text{Full Period} = 4 \\times 45^\\circ = 180^\\circ$$\n"
                            "*(Alternatively: half cycle from peak to trough $= 135^\\circ - 45^\\circ = 90^\\circ \\implies \\text{Period} = 2 \\times 90^\\circ = 180^\\circ$)*.",
                            "**Step 3 — Calculate the frequency coefficient $b$:**\n"
                            "$$\\text{Period} = \\frac{360^\\circ}{b} = 180^\\circ \\implies b = \\frac{360^\\circ}{180^\\circ} = 2$$",
                            "**Step 4 — Assemble the wave equation:**\n"
                            "$$y = 4 \\sin 2x$$\n\n"
                            "**Answer:** $y = 4 \\sin 2x$."
                        ]
                    }
                },

                # PAGE 8 — suggested_simulation
                {
                    "page_number": 8,
                    "page_title": "Explore: Trigonometric Wave Parameter Slider",
                    "block_type": "suggested_simulation",
                    "component_type": "suggested_simulation",
                    "content": {
                        "purpose": (
                            "An interactive 2D wave simulator allowing students to slide amplitude $a \\in [-5, 5]$ and frequency $b \\in [0.5, 4]$. "
                            "As sliders move, the sine/cosine wave updates on a labeled Cartesian grid with live readouts of Amplitude, Period, and Wavelength."
                        )
                    },
                    "asset_info": {
                        "asset_type": "simulation",
                        "archetype": "math_trig_wave_parameter_slider",
                        "title": "Interactive Wave Parameter & Transformation Sandbox"
                    }
                },

                # PAGE 9 — common_misconception
                {
                    "page_number": 9,
                    "page_title": "Common Error: The Linearity Illusion (sin 2x ≠ 2 sin x)",
                    "block_type": "common_misconception",
                    "component_type": "common_misconception",
                    "content": {
                        "text": (
                            "### The Multiplier Placement Fallacy\n\n"
                            "Students frequently assume that multiplying the angle by $2$ doubles the height of the wave:\n"
                            "$$\\sin 2x = 2\\sin x \\quad \\text{❌ (Completely False!)}$$\n\n"
                            "Let's test this mathematically at $x = 30^\\circ$:\n"
                            "- **LHS (Angle Doubled):** $\\sin(2 \\times 30^\\circ) = \\sin 60^\\circ = \\frac{\\sqrt{3}}{2} \\approx 0.866$\n"
                            "- **RHS (Height Doubled):** $2 \\times \\sin 30^\\circ = 2 \\times 0.5 = 1.000$\n\n"
                            "Since $0.866 \\neq 1.000$, they are completely different operations:\n"
                            "- **$y = \\sin 2x$**: The wave completes **2 cycles** in $360^\\circ$ (Period $= 180^\\circ$). Height is still $1$.\n"
                            "- **$y = 2\\sin x$**: The wave reaches **height 2**. Period is still $360^\\circ$."
                        )
                    }
                },

                # PAGE 10 — knowledge_check (MCQ)
                {
                    "page_number": 10,
                    "page_title": "Check Your Understanding: Wave Parameter Extraction",
                    "block_type": "knowledge_check",
                    "component_type": "multiple_choice",
                    "content": {
                        "question": "What are the amplitude and period of the trigonometric function $y = -4 \\sin 3x$?",
                        "options": [
                            "A: Amplitude = -4, Period = 120°",
                            "B: Amplitude = 4, Period = 120°",
                            "C: Amplitude = 4, Period = 1080°",
                            "D: Amplitude = 12, Period = 360°"
                        ],
                        "answer": "B",
                        "explanation": (
                            "1. **Amplitude** is always a positive physical distance: $|a| = |-4| = 4$.\n"
                            "2. **Period** for sine is: $\\frac{360^\\circ}{b} = \\frac{360^\\circ}{3} = 120^\\circ$."
                        )
                    }
                },

                # PAGE 11 — summary
                {
                    "page_number": 11,
                    "page_title": "Key Takeaways: Wave Graphs and Parameters",
                    "block_type": "summary",
                    "component_type": "summary",
                    "content": {
                        "text": (
                            "### Master Summary: Trigonometric Wave Functions\n\n"
                            "| Function | Amplitude | Period | Key Feature |\n"
                            "|:---|:---:|:---:|:---|\n"
                            "| **$y = a \\sin bx$** | $|a|$ | $\\frac{360^\\circ}{b}$ | Starts at origin $(0, 0)$, bobs up first if $a > 0$. |\n"
                            "| **$y = a \\cos bx$** | $|a|$ | $\\frac{360^\\circ}{b}$ | Starts at top peak $(0, a)$, dips through center. |\n"
                            "| **$y = a \\tan bx$** | None (Unbounded) | $\\frac{180^\\circ}{b}$ | Repeated S-curves separated by vertical asymptotes. |\n\n"
                            "**Rules of Thumb:**\n"
                            "- [x] Inside multiplier ($b$) $\\implies$ Horizontal compression (affects **Period**).\n"
                            "- [x] Outside multiplier ($a$) $\\implies$ Vertical stretch (affects **Amplitude**).\n"
                            "- [x] Negative sign outside $\\implies$ Flip upside down across the $x$-axis."
                        )
                    }
                }
            ]
        },

        # =====================================================================
        # MODULE 4.3: Advanced Wave Transformations and Phase Shifts
        # =====================================================================
        {
            "unit_order": 3,
            "unit_title": "Module 4.3: Advanced Wave Transformations and Phase Shifts",
            "lesson_title": "Wave Transformations and Phase Shifts",
            "lesson_blocks": [
                # PAGE 1 — learning_goal
                {
                    "page_number": 1,
                    "page_title": "Mastering Phase Shifts & Multi-Wave Curves",
                    "block_type": "learning_goal",
                    "component_type": "learning_goal",
                    "content": {
                        "title": "What You Will Master in This Lesson",
                        "goals": [
                            "Analyze the general wave model $y = a \\sin(bx \\pm \\theta)$ and $y = a \\cos(bx \\pm \\theta)$.",
                            "Calculate exact horizontal phase shifts using the Zero-Point Tracker rule ($bx \\pm \\theta = 0$).",
                            "Construct accurate values tables and plot multiple transformed trigonometric curves on the same axes.",
                            "Determine wave intersection points and phase differences graphically."
                        ]
                    }
                },

                # PAGE 2 — concept_explanation
                {
                    "page_number": 2,
                    "page_title": "Understanding Phase Angles: The Delayed Recording Analogy",
                    "block_type": "concept_explanation",
                    "component_type": "concept_explanation",
                    "content": {
                        "body": (
                            "When an angle is added or subtracted inside the parentheses of a trigonometric function, the wave does not change shape or height — "
                            "it **slides horizontally** along the coordinate axis. This displacement is called a **phase shift**.\n\n"
                            "### The Late Video Recording Analogy\n\n"
                            "Imagine filming a cyclist riding past a checkpoint:\n\n"
                            "- If you start your recording $30^\\circ$ late, the cyclist's peak position appears **shifted backward** in your footage.\n"
                            "- Adding an angle inside ($bx + \\theta$) shifts the wave **LEFT** (the wave started earlier).\n"
                            "- Subtracting an angle inside ($bx - \\theta$) shifts the wave **RIGHT** (the wave started late).\n\n"
                            "### The Zero-Point Tracker Rule\n\n"
                            "To find exactly where a transformed wave begins its cycle, set the entire inside expression (the argument) equal to zero:\n"
                            "$$bx \\pm \\theta = 0 \\implies x = \\mp \\frac{\\theta}{b}$$\n\n"
                            "This tells you the exact coordinate on the $x$-axis where the origin point of the parent wave has moved!"
                        )
                    }
                },

                # PAGE 3 — definition_card
                {
                    "page_number": 3,
                    "page_title": "Core Rules for Phase Shift Analysis",
                    "block_type": "definition_card",
                    "component_type": "definition_card",
                    "content": {
                        "term": "Phase Shift & Wave Translation",
                        "body": (
                            "### General Parametric Form: $y = a \\sin(bx \\pm \\theta)$\n\n"
                            "| Parameter | Formula | Physical Meaning & Direction |\n"
                            "|:---|:---|:---|\n"
                            "| **Amplitude** | $|a|$ | Peak height above equilibrium center. |\n"
                            "| **Period** | $\\frac{360^\\circ}{b}$ | Domain length for one full cycle. |\n"
                            "| **Phase Shift ($bx + \\theta$)** | $\\text{Shift} = -\\frac{\\theta}{b}$ | **Translate LEFT** by $\\frac{\\theta}{b}$ units. |\n"
                            "| **Phase Shift ($bx - \\theta$)** | $\\text{Shift} = +\\frac{\\theta}{b}$ | **Translate RIGHT** by $\\frac{\\theta}{b}$ units. |\n\n"
                            "> **Key Procedural Step:** When drawing transformed waves, calculate the phase shift first to establish "
                            "where the first crest, zero crossing, and trough will land on your grid paper."
                        )
                    }
                },

                # PAGE 4 — worked_example (Level 1: Easy / Basic Phase Shift)
                {
                    "page_number": 4,
                    "page_title": "Example 1: Identifying the Phase Shift of $y = \\sin(x - 30^\\circ)$",
                    "block_type": "worked_example",
                    "component_type": "worked_example",
                    "content": {
                        "problem": (
                            "Describe how the graph of $y = \\sin(x - 30^\\circ)$ differs from the parent graph $y = \\sin x$, "
                            "and state its amplitude, period, and the coordinates of its first maximum peak."
                        ),
                        "steps": [
                            "**What we need to find:** Transformation difference, amplitude, period, and peak location.",
                            "**Step 1 — Calculate the phase shift:**\n"
                            "Set the argument to zero: $$x - 30^\\circ = 0 \\implies x = +30^\\circ$$\n"
                            "The entire wave is translated **$30^\\circ$ to the right**.",
                            "**Step 2 — State amplitude and period:**\n"
                            "- Amplitude: $|a| = 1$\n"
                            "- Period: $\\frac{360^\\circ}{1} = 360^\\circ$",
                            "**Step 3 — Find the first maximum peak:**\n"
                            "In $y = \\sin x$, the peak occurs at $x = 90^\\circ$.\n"
                            "In $y = \\sin(x - 30^\\circ)$, set $x - 30^\\circ = 90^\\circ \\implies x = 120^\\circ$.\n"
                            "The peak coordinate is **$(120^\\circ, 1)$**.\n\n"
                            "**Answer:** The wave is translated $30^\\circ$ right; Amplitude $= 1$; Period $= 360^\\circ$; First peak is at $(120^\\circ, 1)$."
                        ]
                    }
                },

                # PAGE 5 — worked_example (Level 2: Moderate / Compound Shift $y = 2\\sin(1.5x + 30^\\circ)$)
                {
                    "page_number": 5,
                    "page_title": "Example 2: Analyzing $y = 2 \\sin\\left(\\frac{3}{2}x + 30^\\circ\\right)$",
                    "block_type": "worked_example",
                    "component_type": "worked_example",
                    "content": {
                        "problem": (
                            "For the function $y = 2 \\sin\\left(\\frac{3}{2}x + 30^\\circ\\right)$:\n"
                            "(a) Find the amplitude.\n"
                            "(b) Find the period.\n"
                            "(c) Determine the exact phase shift and direction of translation."
                        ),
                        "steps": [
                            "**What we need to find:** Amplitude, period, and phase shift.",
                            "**Step 1 — Identify parameters:**\n"
                            "- $a = 2$\n"
                            "- $b = \\frac{3}{2} = 1.5$\n"
                            "- $\\theta = 30^\\circ$",
                            "**Step 2 — Calculate amplitude and period:**\n"
                            "- **Amplitude:** $|a| = 2$\n"
                            "- **Period:** $\\frac{360^\\circ}{1.5} = 240^\\circ$",
                            "**Step 3 — Calculate phase shift using the Zero-Point rule:**\n"
                            "$$\\frac{3}{2}x + 30^\\circ = 0 \\implies \\frac{3}{2}x = -30^\\circ \\implies x = -30^\\circ \\times \\frac{2}{3} = -20^\\circ$$\n\n"
                            "**Answer:** (a) Amplitude $= 2$; (b) Period $= 240^\\circ$; (c) Phase shift is $20^\\circ$ to the left."
                        ]
                    }
                },

                # PAGE 6 — worked_example (Level 3: Difficult / Simultaneous Multi-Wave Plotting)
                {
                    "page_number": 6,
                    "page_title": "Example 3: Plotting Two Transformed Waves on the Same Grid",
                    "block_type": "worked_example",
                    "component_type": "worked_example",
                    "content": {
                        "problem": (
                            "Complete the table of values below for $y_1 = -3\\cos 2x$ and $y_2 = 2\\sin(1.5x + 30^\\circ)$ for "
                            "$0^\\circ \\le x \\le 180^\\circ$, and identify where the two curves intersect."
                        ),
                        "steps": [
                            "**What we need to do:** Construct the simultaneous coordinate table and locate intersections.",
                            "**Step 1 — Calculate coordinate table values:**\n\n"
                            "| $x$ | $0^\\circ$ | $30^\\circ$ | $60^\\circ$ | $90^\\circ$ | $120^\\circ$ | $150^\\circ$ | $180^\\circ$ |\n"
                            "|:---|:---:|:---:|:---:|:---:|:---:|:---:|:---:|\n"
                            "| **$y_1 = -3\\cos 2x$** | $-3.00$ | $-1.50$ | $+1.50$ | $+3.00$ | $+1.50$ | $-1.50$ | $-3.00$ |\n"
                            "| **$y_2 = 2\\sin(1.5x + 30^\\circ)$** | $+1.00$ | $+1.93$ | $+1.73$ | $+0.52$ | $-1.00$ | $-2.00$ | $-1.73$ |",
                            "**Step 2 — Identify sign changes and intersection regions:**\n"
                            "- Between $x = 30^\\circ$ and $x = 60^\\circ$: $y_1$ climbs from $-1.50$ to $+1.50$ while $y_2$ stays high ($1.93 \\to 1.73$). Intersect near $x \\approx 55^\\circ$.\n"
                            "- Between $x = 90^\\circ$ and $x = 120^\\circ$: $y_1$ drops from $+3.00$ to $+1.50$ while $y_2$ drops from $+0.52$ to $-1.00$.\n"
                            "- Between $x = 120^\\circ$ and $x = 150^\\circ$: $y_1$ drops below $y_2$ with an exact intersection at $x = 150^\\circ$ ($y_1 = -1.50$ and $y_2 = -2.00$ cross nearby at $x \\approx 132^\\circ$).\n\n"
                            "**Answer:** Table complete; curves cross at $x \\approx 55^\\circ$ and $x \\approx 132^\\circ$."
                        ]
                    }
                },

                # PAGE 7 — worked_example (Level 4: Exam-Style / Full Matrix Geometric Synthesis)
                {
                    "page_number": 7,
                    "page_title": "Example 4: Complete Geometric Transformation Mapping",
                    "block_type": "worked_example",
                    "component_type": "worked_example",
                    "content": {
                        "problem": (
                            "Describe fully the single sequence of geometric transformations that maps the parent wave $y = \\sin x$ "
                            "onto the curve $y = 3 \\sin(2x - 60^\\circ)$."
                        ),
                        "steps": [
                            "**What we need to describe:** Complete transformation sequence in correct mathematical order.",
                            "**Step 1 — Factor out the frequency coefficient $b = 2$ from the argument:**\n"
                            "$$y = 3 \\sin\\left[2(x - 30^\\circ)\\right]$$",
                            "**Step 2 — Identify the horizontal transformations:**\n"
                            "1. **Horizontal compression** towards the y-axis by a scale factor of $\\frac{1}{2}$ (compresses the period to $180^\\circ$).\n"
                            "2. **Horizontal translation (Phase shift)** by $+30^\\circ$ to the right.",
                            "**Step 3 — Identify the vertical transformation:**\n"
                            "3. **Vertical stretch** away from the x-axis by a scale factor of $3$ (scales the amplitude to $3$).",
                            "**Step 4 — Express as a matrix-vector mapping:**\n"
                            "$$\\begin{pmatrix} x' \\\\ y' \\end{pmatrix} = \\begin{pmatrix} 0.5 & 0 \\\\ 0 & 3 \\end{pmatrix} \\begin{pmatrix} x \\\\ y \\end{pmatrix} + \\begin{pmatrix} 30^\\circ \\\\ 0 \\end{pmatrix}$$\n\n"
                            "**Answer:** Horizontal compression by factor $\\frac{1}{2}$, translation $30^\\circ$ right, vertical stretch by factor $3$."
                        ]
                    }
                },

                # PAGE 8 — suggested_simulation
                {
                    "page_number": 8,
                    "page_title": "Explore: Phase Shift & Dual-Wave Harmonizer",
                    "block_type": "suggested_simulation",
                    "component_type": "suggested_simulation",
                    "content": {
                        "purpose": (
                            "An interactive dual-wave sandbox where students can manipulate amplitude, period, and phase shift angle $\\theta$. "
                            "The simulator plots both waves simultaneously, displays real-time intersection points, and highlights phase lead/lag."
                        )
                    },
                    "asset_info": {
                        "asset_type": "simulation",
                        "archetype": "math_phase_shift_wave_harmonizer",
                        "title": "Interactive Phase Shift & Dual-Wave Harmonizer Sandbox"
                    }
                },

                # PAGE 9 — common_misconception
                {
                    "page_number": 9,
                    "page_title": "Common Error: The Phase Shift Sign Trap",
                    "block_type": "common_misconception",
                    "component_type": "common_misconception",
                    "content": {
                        "text": (
                            "### Why Positive Means Left and Negative Means Right\n\n"
                            "Many students believe that $y = \\sin(x + 30^\\circ)$ must shift to the right because $+30^\\circ$ is in the positive direction.\n\n"
                            "### The Mathematical Truth:\n"
                            "- To get the peak value of $y = 1$, the parent wave needs $x = 90^\\circ$.\n"
                            "- For $y = \\sin(x + 30^\\circ)$, we need $(x + 30^\\circ) = 90^\\circ \\implies x = 60^\\circ$.\n"
                            "- Notice that $x = 60^\\circ$ occurs **earlier (further to the left)** than $90^\\circ$!\n\n"
                            "> **Memory Rule:** An addition inside the function is a *time head-start* — the wave reaches every peak earlier, shifting it to the **LEFT**."
                        )
                    }
                },

                # PAGE 10 — knowledge_check (MCQ)
                {
                    "page_number": 10,
                    "page_title": "Check Your Understanding: Phase Shift Calculation",
                    "block_type": "knowledge_check",
                    "component_type": "multiple_choice",
                    "content": {
                        "question": "What is the phase shift and direction of translation for the curve $y = \\cos(2x + 90^\\circ)$ relative to $y = \\cos 2x$?",
                        "options": [
                            "A: 90° to the right",
                            "B: 90° to the left",
                            "C: 45° to the left",
                            "D: 45° to the right"
                        ],
                        "answer": "C",
                        "explanation": (
                            "1. Set the argument to zero: $2x + 90^\\circ = 0$.\n"
                            "2. Solve for $x$: $2x = -90^\\circ \\implies x = -45^\\circ$.\n"
                            "3. The negative sign represents a shift of **$45^\\circ$ to the left**."
                        )
                    }
                },

                # PAGE 11 — summary
                {
                    "page_number": 11,
                    "page_title": "Key Takeaways: Wave Transformations and Phase Shifts",
                    "block_type": "summary",
                    "component_type": "summary",
                    "content": {
                        "text": (
                            "### Master Summary: Advanced Wave Model $y = a \\sin(bx \\pm \\theta) + c$\n\n"
                            "| Parameter | Calculation | Geometric Effect |\n"
                            "|:---|:---|:---|\n"
                            "| **$a$ (Amplitude)** | $|a|$ | Vertical stretch by $|a|$; if $a < 0$, reflect in $x$-axis. |\n"
                            "| **$b$ (Frequency)** | $\\text{Period} = \\frac{360^\\circ}{b}$ | Horizontal compression by factor $\\frac{1}{b}$. |\n"
                            "| **$\\theta$ (Phase Shift)** | $\\Delta x = \\mp \\frac{\\theta}{b}$ | Horizontal shift: $+ \\implies$ Left, $- \\implies$ Right. |\n"
                            "| **$c$ (Vertical Shift)** | Equilibrium line $y = c$ | Translates entire wave up ($+c$) or down ($-c$). |\n\n"
                            "**Zero-Point Tracker Formula:**\n"
                            "$$bx \\pm \\theta = 0 \\implies x_{\\text{start}} = \\mp \\frac{\\theta}{b}$$"
                        )
                    }
                }
            ]
        },

        # =====================================================================
        # MODULE 4.4: Analytical & Graphical Solution of Trig Equations
        # =====================================================================
        {
            "unit_order": 4,
            "unit_title": "Module 4.4: Analytical and Graphical Solution of Trigonometric Equations",
            "lesson_title": "Solving Trigonometric Equations Analytically and Graphically",
            "lesson_blocks": [
                # PAGE 1 — learning_goal
                {
                    "page_number": 1,
                    "page_title": "Mastering Trigonometric Equations & Intersection Roots",
                    "block_type": "learning_goal",
                    "component_type": "learning_goal",
                    "content": {
                        "title": "What You Will Master in This Lesson",
                        "goals": [
                            "Solve linear trigonometric equations across specified domain intervals (e.g. $0^\\circ \\le x \\le 360^\\circ$).",
                            "Solve multi-frequency equations (e.g. $\\tan 3x = 2$) using domain expansion and quadrant rules.",
                            "Solve mixed-ratio and quadratic trigonometric equations ($A\\cos^2 x + B\\cos x + C = 0$) with rigorous domain filtering.",
                            "Read intersection roots and solve periodic equations graphically from plotted wave curves."
                        ]
                    }
                },

                # PAGE 2 — concept_explanation
                {
                    "page_number": 2,
                    "page_title": "The Wave Cutting Principle: Why Trig Equations Have Multiple Roots",
                    "block_type": "concept_explanation",
                    "component_type": "concept_explanation",
                    "content": {
                        "body": (
                            "In basic algebra, linear equations like $2x = 4$ have exactly one single solution. "
                            "In trigonometry, because waves repeat periodically, a horizontal line cuts the wave multiple times across its domain.\n\n"
                            "### The Ocean Net Analogy\n\n"
                            "Imagine casting a horizontal net at height $y = 0.5$ across ocean waves ($y = \\sin x$):\n\n"
                            "- In one complete cycle ($0^\\circ$ to $360^\\circ$), the wave rises through the net at $x = 30^\\circ$ and falls back through it at $x = 150^\\circ$.\n"
                            "- Both angles are equally valid solutions!\n\n"
                            "### The 4-Quadrant CAST Rule:\n\n"
                            "| Quadrant | Angle Range | Positive Ratios | Reference Angle Formula |\n"
                            "|:---:|:---:|:---:|:---|\n"
                            "| **I** | $0^\\circ < x < 90^\\circ$ | **All** ($\\sin, \\cos, \\tan$) | $x = \\alpha$ |\n"
                            "| **II** | $90^\\circ < x < 180^\\circ$ | **Sine only** | $x = 180^\\circ - \\alpha$ |\n"
                            "| **III** | $180^\\circ < x < 270^\\circ$ | **Tangent only** | $x = 180^\\circ + \\alpha$ |\n"
                            "| **IV** | $270^\\circ < x < 360^\\circ$ | **Cosine only** | $x = 360^\\circ - \\alpha$ |\n\n"
                            "> **Memory Word:** **CAST** (starting in Quadrant IV and rotating counter-clockwise: **C**osine, **A**ll, **S**ine, **T**angent)."
                        )
                    }
                },

                # PAGE 3 — formula_breakdown
                {
                    "page_number": 3,
                    "page_title": "Master Strategy for Solving Trigonometric Equations",
                    "block_type": "formula_breakdown",
                    "component_type": "formula_breakdown",
                    "content": {
                        "formula": "**4-Step Universal Solving Sequence:**\n$$\\text{1. Isolate Ratio } (\\sin x = k) \\implies \\text{2. Reference Angle } (\\alpha) \\implies \\text{3. CAST Quadrants} \\implies \\text{4. Filter Domain}$$",
                        "content": (
                            "### The 4-Step Universal Solving Strategy\n\n"
                            "1. **Isolate the trigonometric term:** Reduce equation to $\\sin \\theta = k$, $\\cos \\theta = k$, or $\\tan \\theta = k$.\n"
                            "2. **Find the acute reference angle $\\alpha$:** Calculate $\\alpha = \\arcsin(|k|)$ using the positive magnitude.\n"
                            "3. **Locate valid quadrants using the sign of $k$:**\n"
                            "   - If positive $\\implies$ Quadrants where that ratio is positive.\n"
                            "   - If negative $\\implies$ Quadrants where that ratio is negative.\n"
                            "4. **Expand search domain for multi-frequency arguments:**\n"
                            "   - For $3x$ on $[0^\\circ, 360^\\circ]$, search domain is $[0^\\circ, 1080^\\circ]$ before dividing by 3.\n"
                            "5. **Physical Boundary Gatekeeper:** Reject any intermediate root with $|\\sin x| > 1$ or $|\\cos x| > 1$."
                        )
                    }
                },

                # PAGE 4 — worked_example (Level 1: Easy / Linear Shifted Equation)
                {
                    "page_number": 4,
                    "page_title": "Example 1: Solving $\\sin(x + 30^\\circ) = 0.5$",
                    "block_type": "worked_example",
                    "component_type": "worked_example",
                    "content": {
                        "problem": (
                            "Solve the trigonometric equation $\\sin(x + 30^\\circ) = 0.5$ for the domain $0^\\circ \\le x \\le 360^\\circ$."
                        ),
                        "steps": [
                            "**What we need to find:** All values of $x \\in [0^\\circ, 360^\\circ]$ satisfying the equation.",
                            "**Step 1 — Let argument $\\theta = x + 30^\\circ$ and find domain for $\\theta$:**\n"
                            "Since $0^\\circ \\le x \\le 360^\\circ$, adding $30^\\circ$ gives: $$30^\\circ \\le \\theta \\le 390^\\circ$$",
                            "**Step 2 — Find solutions for $\\sin \\theta = 0.5$:**\n"
                            "Reference angle $\\alpha = \\arcsin(0.5) = 30^\\circ$.\n"
                            "Sine is positive in Quadrants I and II:\n"
                            "- Quadrant I: $\\theta = 30^\\circ$\n"
                            "- Quadrant II: $\\theta = 180^\\circ - 30^\\circ = 150^\\circ$\n"
                            "- Next Cycle (Quadrant I $+ 360^\\circ$): $\\theta = 30^\\circ + 360^\\circ = 390^\\circ$",
                            "**Step 3 — Solve for $x = \\theta - 30^\\circ$:**\n"
                            "- $x_1 = 30^\\circ - 30^\\circ = 0^\\circ$\n"
                            "- $x_2 = 150^\\circ - 30^\\circ = 120^\\circ$\n"
                            "- $x_3 = 390^\\circ - 30^\\circ = 360^\\circ$\n\n"
                            "**Answer:** $x = 0^\\circ, 120^\\circ, 360^\\circ$."
                        ]
                    }
                },

                # PAGE 5 — worked_example (Level 2: Moderate / Multi-Frequency Argument $\\tan 3x = 2$)
                {
                    "page_number": 5,
                    "page_title": "Example 2: Solving Multi-Frequency Equation $\\tan 3x = 2$",
                    "block_type": "worked_example",
                    "component_type": "worked_example",
                    "content": {
                        "problem": (
                            "Solve the equation $\\tan 3x = 2$ for $0^\\circ \\le x \\le 360^\\circ$, giving answers to 2 decimal places."
                        ),
                        "steps": [
                            "**What we need to find:** All valid solutions for $x \\in [0^\\circ, 360^\\circ]$.",
                            "**Step 1 — Expand the search domain for the argument $3x$:**\n"
                            "Since $0^\\circ \\le x \\le 360^\\circ$, multiplying by $3$ yields: $$0^\\circ \\le 3x \\le 1080^\\circ$$",
                            "**Step 2 — Find principal angle $\\alpha$:**\n"
                            "$$\\alpha = \\arctan(2) \\approx 63.43^\\circ$$",
                            "**Step 3 — Generate all 6 roots by adding $180^\\circ$ periods within $[0^\\circ, 1080^\\circ]$:**\n"
                            "- $3x_1 = 63.43^\\circ$\n"
                            "- $3x_2 = 63.43^\\circ + 180^\\circ = 243.43^\\circ$\n"
                            "- $3x_3 = 243.43^\\circ + 180^\\circ = 423.43^\\circ$\n"
                            "- $3x_4 = 423.43^\\circ + 180^\\circ = 603.43^\\circ$\n"
                            "- $3x_5 = 603.43^\\circ + 180^\\circ = 783.43^\\circ$\n"
                            "- $3x_6 = 783.43^\\circ + 180^\\circ = 963.43^\\circ$",
                            "**Step 4 — Divide each value by 3 to obtain $x$:**\n"
                            "- $x_1 = 63.43^\\circ / 3 \\approx 21.14^\\circ$\n"
                            "- $x_2 = 243.43^\\circ / 3 \\approx 81.14^\\circ$\n"
                            "- $x_3 = 423.43^\\circ / 3 \\approx 141.14^\\circ$\n"
                            "- $x_4 = 603.43^\\circ / 3 \\approx 201.14^\\circ$\n"
                            "- $x_5 = 783.43^\\circ / 3 \\approx 261.14^\\circ$\n"
                            "- $x_6 = 963.43^\\circ / 3 \\approx 321.14^\\circ$\n\n"
                            "**Answer:** $x = 21.14^\\circ, 81.14^\\circ, 141.14^\\circ, 201.14^\\circ, 261.14^\\circ, 321.14^\\circ$."
                        ]
                    }
                },

                # PAGE 6 — worked_example (Level 3: Difficult / Mixed Ratio Factorization $\\sin 2x = \\cos x$)
                {
                    "page_number": 6,
                    "page_title": "Example 3: Solving Mixed-Ratio Equations by Factorization",
                    "block_type": "worked_example",
                    "component_type": "worked_example",
                    "content": {
                        "problem": (
                            "Solve the equation $\\sin 2x = \\cos x$ for $0^\\circ \\le x \\le 360^\\circ$."
                        ),
                        "steps": [
                            "**What we need to find:** All solutions in $[0^\\circ, 360^\\circ]$ without missing root branches.",
                            "**Step 1 — Use double-angle expansion $\\sin 2x = 2\\sin x \\cos x$:**\n"
                            "$$2\\sin x \\cos x = \\cos x$$",
                            "**Step 2 — Move all terms to LHS and factorize (NEVER divide by $\\cos x$, which loses roots!):**\n"
                            "$$2\\sin x \\cos x - \\cos x = 0$$\n"
                            "$$\\cos x (2\\sin x - 1) = 0$$",
                            "**Step 3 — Branch 1: Solve $\\cos x = 0$:**\n"
                            "On $[0^\\circ, 360^\\circ]$, $\\cos x = 0$ at:\n"
                            "$$x = 90^\\circ \\quad \\text{and} \\quad x = 270^\\circ$$",
                            "**Step 4 — Branch 2: Solve $2\\sin x - 1 = 0 \\implies \\sin x = 0.5$:**\n"
                            "$$\\alpha = 30^\\circ \\implies x = 30^\\circ \\quad \\text{and} \\quad x = 180^\\circ - 30^\\circ = 150^\\circ$$",
                            "**Step 5 — Combine and order all 4 distinct roots:**\n"
                            "$$x = 30^\\circ, 90^\\circ, 150^\\circ, 270^\\circ$$\n\n"
                            "**Answer:** $x = 30^\\circ, 90^\\circ, 150^\\circ, 270^\\circ$."
                        ]
                    }
                },

                # PAGE 7 — worked_example (Level 4: Exam-Style / Quadratic-in-Cosine with Domain Filtering)
                {
                    "page_number": 7,
                    "page_title": "Example 4: Quadratic Trigonometric Equations with Domain Filtering",
                    "block_type": "worked_example",
                    "component_type": "worked_example",
                    "content": {
                        "problem": (
                            "Solve the quadratic trigonometric equation $3\\cos^2 x - 7\\cos x = 6$ for the domain $0^\\circ \\le x \\le 360^\\circ$, "
                            "giving answers to 2 decimal places."
                        ),
                        "steps": [
                            "**What we need to find:** All valid solutions for $x \\in [0^\\circ, 360^\\circ]$.",
                            "**Step 1 — Rearrange into standard quadratic form and substitute $u = \\cos x$:**\n"
                            "$$3\\cos^2 x - 7\\cos x - 6 = 0 \\implies 3u^2 - 7u - 6 = 0$$",
                            "**Step 2 — Factorize by grouping (numbers multiplying to $-18$ and adding to $-7$ are $-9$ and $+2$):**\n"
                            "$$3u^2 - 9u + 2u - 6 = 0$$\n"
                            "$$3u(u - 3) + 2(u - 3) = 0 \\implies (3u + 2)(u - 3) = 0$$",
                            "**Step 3 — Solve for intermediate roots $u$:**\n"
                            "$$u = -\\frac{2}{3} \\quad \\text{or} \\quad u = 3$$",
                            "**Step 4 — Apply the Physical Domain Gatekeeper ($-1 \\le \\cos x \\le 1$):**\n"
                            "$$\\text{Reject } u = 3 \\quad \\text{because } \\cos x \\text{ cannot exceed } 1.$$",
                            "**Step 5 — Solve remaining valid branch $\\cos x = -\\frac{2}{3}$:**\n"
                            "Reference angle $\\alpha = \\arccos\\left(\\frac{2}{3}\\right) \\approx 48.19^\\circ$.\n"
                            "Since cosine is negative, solutions lie in Quadrants II and III:\n"
                            "- Quadrant II: $x = 180^\\circ - 48.19^\\circ = 131.81^\\circ$\n"
                            "- Quadrant III: $x = 180^\\circ + 48.19^\\circ = 228.19^\\circ$\n\n"
                            "**Answer:** $x = 131.81^\\circ$ and $x = 228.19^\\circ$."
                        ]
                    }
                },

                # PAGE 8 — suggested_simulation
                {
                    "page_number": 8,
                    "page_title": "Explore: Interactive Graphical Equation Solver",
                    "block_type": "suggested_simulation",
                    "component_type": "suggested_simulation",
                    "content": {
                        "purpose": (
                            "An interactive graphing tool where students can enter any two trigonometric curves (e.g. $y_1 = 3\\cos^2 x - 7\\cos x$ and $y_2 = 6$). "
                            "The app displays the curves, automatically highlights all intersection points with coordinate callouts, "
                            "and shows the step-by-step algebraic reduction alongside the graph."
                        )
                    },
                    "asset_info": {
                        "asset_type": "simulation",
                        "archetype": "math_graphical_equation_solver",
                        "title": "Interactive Graphical Trigonometric Equation Solver Sandbox"
                    }
                },

                # PAGE 9 — common_misconception
                {
                    "page_number": 9,
                    "page_title": "Common Error: The Single-Root Calculator Trap",
                    "block_type": "common_misconception",
                    "component_type": "common_misconception",
                    "content": {
                        "text": (
                            "### Why Your Calculator Only Gives Half the Answer\n\n"
                            "When you type $\\arccos(-2/3)$ on a scientific calculator, it displays `131.81°`.\n\n"
                            "Many students write down $131.81^\\circ$ and stop, losing half the marks! "
                            "Because calculators are programmed to return only the principal value, they will **never** automatically show the third quadrant solution ($228.19^\\circ$).\n\n"
                            "### The 2-Step Defense Routine:\n"
                            "1. Calculate reference angle $\\alpha = \\arccos(|k|)$ (use positive value).\n"
                            "2. Use the **CAST quadrant rule** to write down both angles explicitly:\n"
                            "   - Quadrant II: $180^\\circ - \\alpha$\n"
                            "   - Quadrant III: $180^\\circ + \\alpha$"
                        )
                    }
                },

                # PAGE 10 — knowledge_check (MCQ)
                {
                    "page_number": 10,
                    "page_title": "Check Your Understanding: Quadratic Trig Equation",
                    "block_type": "knowledge_check",
                    "component_type": "multiple_choice",
                    "content": {
                        "question": "How many distinct solutions exist for the equation $2\\sin^2 x - \\sin x - 1 = 0$ in the domain $0^\\circ \\le x \\le 360^\\circ$?",
                        "options": [
                            "A: 1 solution",
                            "B: 2 solutions",
                            "C: 3 solutions",
                            "D: 4 solutions"
                        ],
                        "answer": "C",
                        "explanation": (
                            "1. Factorize: $(2\\sin x + 1)(\\sin x - 1) = 0$.\n"
                            "2. Branch 1: $\\sin x = 1 \\implies x = 90^\\circ$ (1 solution).\n"
                            "3. Branch 2: $\\sin x = -0.5 \\implies x = 180^\\circ + 30^\\circ = 210^\\circ$ and $x = 360^\\circ - 30^\\circ = 330^\\circ$ (2 solutions).\n"
                            "4. Total distinct solutions: $90^\\circ, 210^\\circ, 330^\\circ$ (exactly 3 solutions)."
                        )
                    }
                },

                # PAGE 11 — summary
                {
                    "page_number": 11,
                    "page_title": "Key Takeaways: Solving Trigonometric Equations",
                    "block_type": "summary",
                    "component_type": "summary",
                    "content": {
                        "text": (
                            "### Master Checklist for Solving Trigonometric Equations\n\n"
                            "| Equation Type | Solving Method | Critical Watch-Out |\n"
                            "|:---|:---|:---|\n"
                            "| **Linear ($a\\sin x = c$)** | Isolate ratio, find $\\alpha$, use CAST. | Always check both positive/negative quadrants. |\n"
                            "| **Multi-Frequency ($a\\tan bx = c$)** | Expand domain to $[0, b \\times 360^\\circ]$, solve for $bx$, divide by $b$. | Don't divide by $b$ before generating all cycle roots! |\n"
                            "| **Mixed Ratio ($\\sin 2x = \\cos x$)** | Expand $\\sin 2x = 2\\sin x\\cos x$, factorize $\\cos x(2\\sin x - 1) = 0$. | **Never divide by $\\cos x$** (you will lose $90^\\circ, 270^\\circ$). |\n"
                            "| **Quadratic ($A\\cos^2 x + B\\cos x + C = 0$)** | Substitute $u = \\cos x$, factorize, solve for $u$. | Reject $|u| > 1$ immediately before quadrant solving. |\n\n"
                            "**Radian Equivalence Note:**\n"
                            "In KCSE examinations, circular measure is denoted as $\\pi_c$, where $\\pi_c = \\pi\\text{ radians} = 180^\\circ$."
                        )
                    }
                }
            ]
        }
    ]


def ingest_topic4_trigonometry():
    """Main ingestion runner for Topic 4: Trigonometry III."""
    print("=" * 80)
    print("VLearn Form 4 Mathematics — Topic 4: Trigonometry III")
    print("Ingestion started")
    print("=" * 80)

    # 1. Fetch Curriculum, Grade, Subject
    curriculum, _ = Curriculum.objects.get_or_create(
        name="844",
        defaults={"description": "Kenya 8-4-4 Education System"}
    )
    print(f"Found existing Curriculum: {curriculum.name}")

    grade = Grade.objects.filter(name="Form 4").first()
    if not grade:
        grade = Grade.objects.create(
            name="Form 4",
            level=1,
            curriculum=curriculum
        )
    print(f"Found Grade: {grade.name} (level={grade.level})")

    subject, _ = Subject.objects.get_or_create(
        name="Mathematics",
        grade=grade,
    )
    print(f"Found Subject: {subject.name}")

    # 2. Get or create Topic 4
    topic_name = "Topic 4: Trigonometry III"
    topic, topic_created = Topic.objects.get_or_create(
        subject=subject,
        order=4,
        defaults={"name": topic_name}
    )
    if not topic_created and topic.name != topic_name:
        topic.name = topic_name
        topic.save()
    print(f"Found Topic: {topic.name} (ID: {topic.id})")

    modules_data = get_topic4_data()
    total_blocks_created = 0

    for m_idx, m_data in enumerate(modules_data, 1):
        # 1. Get or create LearningUnit
        unit, unit_created = LearningUnit.objects.get_or_create(
            topic=topic,
            order=m_data["unit_order"],
            defaults={"name": m_data["unit_title"]}
        )
        if not unit_created and unit.name != m_data["unit_title"]:
            unit.name = m_data["unit_title"]
            unit.save()

        # 2. Get or create Lesson (status="published")
        lesson, lesson_created = Lesson.objects.get_or_create(
            learning_unit=unit,
            defaults={
                "title": m_data["lesson_title"],
                "topic": topic,
                "status": "published",
                "version": 1
            }
        )
        if not lesson_created:
            lesson.title = m_data["lesson_title"]
            lesson.status = "published"
            lesson.save()

        # 3. Idempotent cleanup of old blocks & assets
        existing_blocks = LessonBlock.objects.filter(lesson=lesson)
        existing_block_count = existing_blocks.count()
        existing_assets = LessonAsset.objects.filter(lesson=lesson)
        existing_asset_count = existing_assets.count()

        existing_blocks.delete()
        existing_assets.delete()

        print(f"\n  Found LearningUnit: {unit.name}")
        print(f"  Found Lesson: '{lesson.title}' (ID: {lesson.id}, status={lesson.status})")
        print(f"  Cleared {existing_block_count} existing blocks, {existing_asset_count} existing assets")

        # 4. Create new LessonBlocks
        blocks_created = 0
        for block_idx, b_data in enumerate(m_data["lesson_blocks"], 1):
            block = LessonBlock.objects.create(
                lesson=lesson,
                page_number=b_data["page_number"],
                page_title=b_data["page_title"],
                block_type=b_data["block_type"],
                component_type=b_data["component_type"],
                content=b_data["content"],
                order=block_idx
            )
            blocks_created += 1

            # Handle simulation asset link if present
            if "asset_info" in b_data:
                asset_info = b_data["asset_info"]
                asset = LessonAsset.objects.create(
                    lesson=lesson,
                    asset_type=asset_info.get("asset_type", "simulation"),
                    source_type="uploaded",
                    storage_type="url",
                    status="pending",
                    title=asset_info.get("title", b_data.get("page_title", "")),
                    description=b_data["content"].get("purpose", b_data.get("page_title", "")),
                    metadata={"archetype": asset_info.get("archetype", "")}
                )
                asset.blocks.add(block)

        total_blocks_created += blocks_created
        print(f"  Created {blocks_created} blocks across {len(m_data['lesson_blocks'])} pages")

    print("\n" + "=" * 80)
    print(f"Ingestion complete. Total blocks created: {total_blocks_created}")
    print(f"Grade: {grade.name} | Subject: {subject.name} | Topic: {topic.name}")
    print("=" * 80)


if __name__ == "__main__":
    ingest_topic4_trigonometry()
