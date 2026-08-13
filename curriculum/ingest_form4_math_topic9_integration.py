#!/usr/bin/env python3
"""
VLearn Form 4 Mathematics — Topic 9: Integration Ingestion Script
===================================================================
Curriculum: 844
Grade: Form 4 (level=1)
Subject: Mathematics
Topic: Topic 9: Integration (order=9)

Modules / LearningUnits:
  9.1 Antiderivatives, Reverse Differentiation, and Indefinite Integration
  9.2 Particular Solutions, Initial Boundary Conditions, and Curve Reconstruction
  9.3 Definite Integration, Area Under Curves, and Split-Region Integrals
  9.4 Area Between Intersecting Curves and Integration in Kinematics

Pedagogical Structure per Lesson: 11 Pages (44 blocks total)
  Page 1:  learning_goal (Student-friendly outcomes)
  Page 2:  concept_explanation (Real-world analogies: undo button, benchmark anchor, accumulating strips, rocket telemetry)
  Page 3:  formula_breakdown / definition_card (Word formulas, polynomial integration rules, definite limits, area between curves, kinematics)
  Page 4:  worked_example (Level 1: Easy / Foundation)
  Page 5:  worked_example (Level 2: Moderate / Multi-step)
  Page 6:  worked_example (Level 3: Difficult / Exam standard)
  Page 7:  worked_example (Level 4: Exam-Style / Real-World Synthesis)
  Page 8:  suggested_simulation (Interactive visual sandbox)
  Page 9:  common_misconception (Diagnostic error analysis & memory tips)
  Page 10: knowledge_check (MCQ / Short-answer with step-by-step solutions)
  Page 11: summary (Key takeaways & integration checklist)

Standards Enforced:
  - Clean responsive Markdown tables (zero raw \\begin{array} or \\hline).
  - Explicit bold labels on all formula breakdowns.
  - Correct normalized equations (fixing source text bugs: S = 40t - 5t^2, 5(5)^2 = 125, particular solution V = h^3 + 4h + 4).
  - Complete mathematical accuracy.
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


def get_topic9_data():
    """Returns the complete structured curriculum payload for Topic 9."""
    return [
        # =====================================================================
        # MODULE 9.1: Antiderivatives & Indefinite Integration
        # =====================================================================
        {
            "unit_order": 1,
            "unit_title": "Module 9.1: Antiderivatives, Reverse Differentiation, and Indefinite Integration",
            "lesson_title": "Antiderivatives, Reverse Differentiation, and Indefinite Integration",
            "lesson_blocks": [
                # PAGE 1 — learning_goal
                {
                    "page_number": 1,
                    "page_title": "Mastering Antiderivatives & Indefinite Integration",
                    "block_type": "learning_goal",
                    "component_type": "learning_goal",
                    "content": {
                        "title": "What You Will Master in This Lesson",
                        "goals": [
                            "Understand integration as the exact inverse (reverse) process of differentiation.",
                            "Apply the Polynomial Integration Rule $\\int a x^n dx = \\frac{a x^{n+1}}{n+1} + C$ for $n \\neq -1$.",
                            "Explain why the constant of integration $+C$ is required to represent a family of parallel curves.",
                            "Integrate multi-term polynomials, negative powers ($x^{-n}$), and fractional exponents ($x^{p/q}$)."
                        ]
                    }
                },

                # PAGE 2 — concept_explanation
                {
                    "page_number": 2,
                    "page_title": "The Undo Button Analogy: Why Integration Restores Parent Functions",
                    "block_type": "concept_explanation",
                    "component_type": "concept_explanation",
                    "content": {
                        "body": (
                            "Think of differentiation as a machine that takes a curve's elevation formula and calculates its slope function:\n\n"
                            "- $y = x^2 \\xrightarrow{\\text{Differentiate}} \\frac{dy}{dx} = 2x$\n"
                            "- $y = x^2 + 5 \\xrightarrow{\\text{Differentiate}} \\frac{dy}{dx} = 2x$\n"
                            "- $y = x^2 - 100 \\xrightarrow{\\text{Differentiate}} \\frac{dy}{dx} = 2x$\n\n"
                            "### The Constant of Integration $+C$\n\n"
                            "Integration is the **'undo' button** for differentiation. When we integrate $2x$, we get back $x^2$.\n"
                            "However, because any constant number differentiates to zero, the undo machine cannot know whether the original curve had a $+5$, a $-100$, or a $0$!\n\n"
                            "To account for all possibilities, we write the general antiderivative as **$y = x^2 + C$**, "
                            "where $C$ is the **constant of integration** representing an entire family of parallel curves."
                        )
                    }
                },

                # PAGE 3 — formula_breakdown
                {
                    "page_number": 3,
                    "page_title": "Master Formulas: Indefinite Integration Rules",
                    "block_type": "formula_breakdown",
                    "component_type": "formula_breakdown",
                    "content": {
                        "formula": (
                            "**Polynomial Integration Power Rule:**\n"
                            "$$\\int a x^n \\, dx = \\frac{a x^{n+1}}{n+1} + C \\quad (\\text{where } n \\neq -1)$$\n\n"
                            "**Integration of a Constant:**\n"
                            "$$\\int k \\, dx = k x + C$$\n\n"
                            "**Linear Sum & Difference Rule:**\n"
                            "$$\\int [f(x) \\pm g(x)] \\, dx = \\int f(x) \\, dx \\pm \\int g(x) \\, dx$$"
                        ),
                        "content": (
                            "### Integration vs. Differentiation Rule Comparison\n\n"
                            "| Operation | Differentiation Shortcut | Integration Shortcut |\n"
                            "|:---|:---|:---|\n"
                            "| **Power Term ($a x^n$)** | Multiply by power, subtract 1: $n a x^{n-1}$ | **Add 1 to power, divide by new power**: $\\frac{a x^{n+1}}{n+1} + C$ |\n"
                            "| **Linear Term ($k x$)** | Becomes constant: $k$ | Becomes quadratic: $\\frac{k x^2}{2} + C$ |\n"
                            "| **Constant ($k$)** | Becomes zero: $0$ | Becomes linear: $k x + C$ |\n"
                            "| **Negative Power ($x^{-2}$)** | $-2 x^{-3}$ | $\\frac{x^{-1}}{-1} + C = -\\frac{1}{x} + C$ |\n"
                            "| **Fractional Power ($x^{1/2}$)** | $\\frac{1}{2} x^{-1/2}$ | $\\frac{x^{3/2}}{3/2} + C = \\frac{2}{3} x^{3/2} + C$"
                        )
                    }
                },

                # PAGE 4 — worked_example (Level 1: Easy / Monomial & Polynomial Integration)
                {
                    "page_number": 4,
                    "page_title": "Example 1: Indefinite Integration of a Polynomial",
                    "block_type": "worked_example",
                    "component_type": "worked_example",
                    "content": {
                        "problem": (
                            "Evaluate the indefinite integrals:\n"
                            "(a) $\\int 2x^5 \\, dx$\n"
                            "(b) $\\int (5x^3 - 2x + 4) \\, dx$"
                        ),
                        "steps": [
                            "**What we need to find:** The antiderivative functions with $+C$.",
                            "**Step 1 — Part (a): Integrate $2x^5$:**\n"
                            "$$\\int 2x^5 \\, dx = \\frac{2 x^{5+1}}{5+1} + C = \\frac{2 x^6}{6} + C = \\frac{x^6}{3} + C$$",
                            "**Step 2 — Verify Part (a) by differentiation:**\n"
                            "$$\\frac{d}{dx}\\left(\\frac{x^6}{3} + C\\right) = \\frac{6x^5}{3} + 0 = 2x^5 \\quad (\\text{Verified!})$$",
                            "**Step 3 — Part (b): Integrate term-by-term:**\n"
                            "$$\\int (5x^3 - 2x + 4) \\, dx = \\frac{5 x^{3+1}}{3+1} - \\frac{2 x^{1+1}}{1+1} + 4x + C$$\n"
                            "$$= \\frac{5x^4}{4} - \\frac{2x^2}{2} + 4x + C = \\frac{5}{4}x^4 - x^2 + 4x + C$$\n\n"
                            "**Answer:** (a) $\\frac{x^6}{3} + C$; (b) $\\frac{5}{4}x^4 - x^2 + 4x + C$."
                        ]
                    }
                },

                # PAGE 5 — worked_example (Level 2: Moderate / Expansion & Division Before Integration)
                {
                    "page_number": 5,
                    "page_title": "Example 2: Integrating Products and Rational Expressions",
                    "block_type": "worked_example",
                    "component_type": "worked_example",
                    "content": {
                        "problem": (
                            "Evaluate the indefinite integrals:\n"
                            "(a) $\\int x(x^2 - 3) \\, dx$\n"
                            "(b) $\\int \\frac{x^3 + 4x^2}{x} \\, dx$"
                        ),
                        "steps": [
                            "**What we need to do:** Expand or simplify algebraically into standard polynomial terms BEFORE integrating.",
                            "**Step 1 — Part (a): Expand product:**\n"
                            "$$x(x^2 - 3) = x^3 - 3x$$",
                            "**Step 2 — Integrate Part (a):**\n"
                            "$$\\int (x^3 - 3x) \\, dx = \\frac{x^{3+1}}{3+1} - \\frac{3x^{1+1}}{1+1} + C = \\frac{x^4}{4} - \\frac{3}{2}x^2 + C$$",
                            "**Step 3 — Part (b): Simplify fraction by dividing terms:**\n"
                            "$$\\frac{x^3 + 4x^2}{x} = \\frac{x^3}{x} + \\frac{4x^2}{x} = x^2 + 4x \\quad (x \\neq 0)$$",
                            "**Step 4 — Integrate Part (b):**\n"
                            "$$\\int (x^2 + 4x) \\, dx = \\frac{x^3}{3} + \\frac{4x^2}{2} + C = \\frac{x^3}{3} + 2x^2 + C$$\n\n"
                            "**Answer:** (a) $\\frac{x^4}{4} - \\frac{3}{2}x^2 + C$; (b) $\\frac{x^3}{3} + 2x^2 + C$."
                        ]
                    }
                },

                # PAGE 6 — worked_example (Level 3: Difficult / Negative and Fractional Powers)
                {
                    "page_number": 6,
                    "page_title": "Example 3: Integrating Negative and Fractional Exponents",
                    "block_type": "worked_example",
                    "component_type": "worked_example",
                    "content": {
                        "problem": (
                            "Evaluate $\\int \\left( \\frac{2}{x^2} + 4\\sqrt{x} \\right) \\, dx$ for $x > 0$."
                        ),
                        "steps": [
                            "**What we need to find:** Indefinite integral using index notation.",
                            "**Step 1 — Convert terms to index form:**\n"
                            "$$\\frac{2}{x^2} = 2x^{-2}, \\qquad 4\\sqrt{x} = 4x^{1/2}$$",
                            "**Step 2 — Integrate $2x^{-2}$:**\n"
                            "$$\\int 2x^{-2} \\, dx = \\frac{2 x^{-2+1}}{-2+1} = \\frac{2 x^{-1}}{-1} = -2x^{-1} = -\\frac{2}{x}$$",
                            "**Step 3 — Integrate $4x^{1/2}$:**\n"
                            "$$\\int 4x^{1/2} \\, dx = \\frac{4 x^{1/2+1}}{\\frac{1}{2}+1} = \\frac{4 x^{3/2}}{\\frac{3}{2}} = 4 \\times \\frac{2}{3} x^{3/2} = \\frac{8}{3} x^{3/2}$$",
                            "**Step 4 — Combine and add constant $C$:**\n"
                            "$$\\int \\left( 2x^{-2} + 4x^{1/2} \\right) \\, dx = -\\frac{2}{x} + \\frac{8}{3}x^{3/2} + C$$\n\n"
                            "**Answer:** $-\\frac{2}{x} + \\frac{8}{3}x^{3/2} + C$."
                        ]
                    }
                },

                # PAGE 7 — worked_example (Level 4: Exam-Style / Multi-Term Rational Integration)
                {
                    "page_number": 7,
                    "page_title": "Example 4: Integrating Algebraic Quotients with Fractional Powers",
                    "block_type": "worked_example",
                    "component_type": "worked_example",
                    "content": {
                        "problem": (
                            "Evaluate $\\int \\frac{3x^2 - 5x + 2}{\\sqrt{x}} \\, dx$ for $x > 0$."
                        ),
                        "steps": [
                            "**What we need to do:** Split into separate fractional terms and apply index subtraction before integrating.",
                            "**Step 1 — Split terms over $\\sqrt{x} = x^{1/2}$:**\n"
                            "$$\\frac{3x^2}{x^{1/2}} - \\frac{5x}{x^{1/2}} + \\frac{2}{x^{1/2}} = 3x^{2 - 1/2} - 5x^{1 - 1/2} + 2x^{-1/2} = 3x^{3/2} - 5x^{1/2} + 2x^{-1/2}$$",
                            "**Step 2 — Integrate $3x^{3/2}$:**\n"
                            "$$\\int 3x^{3/2} \\, dx = \\frac{3 x^{5/2}}{\\frac{5}{2}} = 3 \\times \\frac{2}{5} x^{5/2} = \\frac{6}{5}x^{5/2}$$",
                            "**Step 3 — Integrate $-5x^{1/2}$:**\n"
                            "$$\\int -5x^{1/2} \\, dx = -\\frac{5 x^{3/2}}{\\frac{3}{2}} = -5 \\times \\frac{2}{3} x^{3/2} = -\\frac{10}{3}x^{3/2}$$",
                            "**Step 4 — Integrate $2x^{-1/2}$:**\n"
                            "$$\\int 2x^{-1/2} \\, dx = \\frac{2 x^{1/2}}{\\frac{1}{2}} = 2 \\times 2 x^{1/2} = 4x^{1/2} = 4\\sqrt{x}$$",
                            "**Step 5 — Combine final result:**\n"
                            "$$\\frac{6}{5}x^{5/2} - \\frac{10}{3}x^{3/2} + 4\\sqrt{x} + C$$\n\n"
                            "**Answer:** $\\frac{6}{5}x^{5/2} - \\frac{10}{3}x^{3/2} + 4\\sqrt{x} + C$."
                        ]
                    }
                },

                # PAGE 8 — suggested_simulation
                {
                    "page_number": 8,
                    "page_title": "Explore: Family of Curves (+C) Vertical Slider Sandbox",
                    "block_type": "suggested_simulation",
                    "component_type": "suggested_simulation",
                    "content": {
                        "purpose": (
                            "An interactive graphing simulator displaying the antiderivative family $y = x^2 + C$. "
                            "Students move a slider for $C$ from $-10$ to $+10$ and observe the curve sliding vertically while its gradient at every $x$ stays identical. "
                            "Placing a target pin on the grid highlights the unique value of $C$ required for the curve to pass through that exact point."
                        )
                    },
                    "asset_info": {
                        "asset_type": "simulation",
                        "archetype": "math_indefinite_integral_family_explorer",
                        "title": "Interactive Family of Curves (+C) Slider Sandbox"
                    }
                },

                # PAGE 9 — common_misconception
                {
                    "page_number": 9,
                    "page_title": "Common Error: The Vanishing Constant & Power Rule Inversion",
                    "block_type": "common_misconception",
                    "component_type": "common_misconception",
                    "content": {
                        "text": (
                            "### Common Indefinite Integration Traps\n\n"
                            "1. **Omitting the Constant of Integration $+C$:**\n"
                            "   Writing $\\int 2x \\, dx = x^2$ is incomplete! Because $y = x^2 + 7$ and $y = x^2 - 12$ both differentiate to $2x$, you must write $+C$ to represent all curves.\n"
                            "2. **Subtracting 1 Instead of Adding 1:**\n"
                            "   Confusing integration with differentiation. In integration, we **ADD $1$** to the exponent: $\\int x^3 \\, dx = \\frac{x^4}{4} + C$, NOT $\\frac{x^2}{2}$.\n"
                            "3. **Negative Index Power Addition Error:**\n"
                            "   When integrating $x^{-2}$, $-2 + 1 = -1$ (NOT $-3$). Thus, $\\int x^{-2} \\, dx = -\\frac{1}{x} + C$.\n\n"
                            "> **Memory Rule:** Integration builds up power ($n \\to n+1$) and requires $+C$!"
                        )
                    }
                },

                # PAGE 10 — knowledge_check (MCQ)
                {
                    "page_number": 10,
                    "page_title": "Check Your Understanding: Indefinite Integrals",
                    "block_type": "knowledge_check",
                    "component_type": "multiple_choice",
                    "content": {
                        "question": "What is the indefinite integral of y = 6x² - 4x + 3?",
                        "options": [
                            "A: 2x³ - 2x² + 3x + C",
                            "B: 12x - 4 + C",
                            "C: 3x³ - 4x² + 3x + C",
                            "D: 2x³ - 4x² + 3 + C"
                        ],
                        "answer": "A",
                        "explanation": (
                            "1. $\\int 6x^2 \\, dx = \\frac{6x^3}{3} = 2x^3$.\n"
                            "2. $\\int -4x \\, dx = -\\frac{4x^2}{2} = -2x^2$.\n"
                            "3. $\\int 3 \\, dx = 3x$.\n"
                            "4. Add constant $+C \\implies 2x^3 - 2x^2 + 3x + C$."
                        )
                    }
                },

                # PAGE 11 — summary
                {
                    "page_number": 11,
                    "page_title": "Key Takeaways: Indefinite Integration",
                    "block_type": "summary",
                    "component_type": "summary",
                    "content": {
                        "text": (
                            "### Master Summary: Indefinite Integration Protocol\n\n"
                            "| Step | Action | Key Check |\n"
                            "|:---|:---|:---|\n"
                            "| **1. Rewrite** | Convert roots/denominators to index form ($x^{-n}, x^{p/q}$) | Expand products and split fractions first. |\n"
                            "| **2. Add Power** | Add $+1$ to the exponent ($n \\to n+1$) | Watch out for negative numbers: $-2+1 = -1$. |\n"
                            "| **3. Divide** | Divide term by new exponent ($n+1$) | Multiply by reciprocal for fractions. |\n"
                            "| **4. Add Constant** | Append $+C$ to final expression | Essential for all indefinite integrals! |\n\n"
                            "**Verification Tip:** Differentiate your final answer to verify it returns the integrand exactly!"
                        )
                    }
                }
            ]
        },

        # =====================================================================
        # MODULE 9.2: Particular Solutions & Boundary Conditions
        # =====================================================================
        {
            "unit_order": 2,
            "unit_title": "Module 9.2: Particular Solutions, Initial Boundary Conditions, and Curve Reconstruction",
            "lesson_title": "Particular Solutions, Initial Boundary Conditions, and Curve Reconstruction",
            "lesson_blocks": [
                # PAGE 1 — learning_goal
                {
                    "page_number": 1,
                    "page_title": "Mastering Particular Solutions & Boundary Anchors",
                    "block_type": "learning_goal",
                    "component_type": "learning_goal",
                    "content": {
                        "title": "What You Will Master in This Lesson",
                        "goals": [
                            "Distinguish between a general solution family ($y = f(x) + C$) and a particular solution curve.",
                            "Use a given boundary point coordinate $(x_0, y_0)$ to solve for the exact numerical value of $C$.",
                            "Reconstruct the original curve equation $y(x)$ from its gradient function $\\frac{dy}{dx}$.",
                            "Determine the $x$-intercepts and key geometric properties of reconstructed curves."
                        ]
                    }
                },

                # PAGE 2 — concept_explanation
                {
                    "page_number": 2,
                    "page_title": "The Benchmark Anchor Analogy: Pinpointing the Exact Curve",
                    "block_type": "concept_explanation",
                    "component_type": "concept_explanation",
                    "content": {
                        "body": (
                            "Imagine a family of parallel roads moving up a hillside. The gradient function tells you the slope of the hill at every latitude, "
                            "so you know the shape of all the roads ($y = f(x) + C$).\n\n"
                            "### The Boundary Benchmark Anchor\n\n"
                            "To know **which exact road** you are standing on, a surveyor gives you a single **GPS coordinate point $(x_0, y_0)$** on your road.\n\n"
                            "1. You integrate the gradient function to get $y = f(x) + C$.\n"
                            "2. You plug in $x_0$ and $y_0$ to lock down the exact height of your road.\n"
                            "3. This isolates a single numerical value for **$C$**, converting the general family into a unique **particular solution**!"
                        )
                    }
                },

                # PAGE 3 — formula_breakdown
                {
                    "page_number": 3,
                    "page_title": "Master Protocol: Reconstructing Curves from Gradient Functions",
                    "block_type": "formula_breakdown",
                    "component_type": "formula_breakdown",
                    "content": {
                        "formula": (
                            "**General Solution Equation:**\n"
                            "$$y(x) = \\int \\frac{dy}{dx} \\, dx = F(x) + C$$\n\n"
                            "**Solving for Constant $C$ at Boundary Point $(x_0, y_0)$:**\n"
                            "$$y_0 = F(x_0) + C \\implies C = y_0 - F(x_0)$$\n\n"
                            "**Particular Solution Equation:**\n"
                            "$$y(x) = F(x) + [y_0 - F(x_0)]$$"
                        ),
                        "content": (
                            "### 4-Step Particular Solution Execution Protocol\n\n"
                            "| Step | Action | Key Check |\n"
                            "|:---|:---|:---|\n"
                            "| **1. Integrate** | Integrate $\\frac{dy}{dx}$ indefinitely | Do not forget to include $+C$ at this stage. |\n"
                            "| **2. Substitute** | Plug $x = x_0$ and $y = y_0$ into integrated equation | Ensure correct coordinate pairing. |\n"
                            "| **3. Solve $C$** | Isolate constant $C$ algebraically | Pay close attention to fraction signs. |\n"
                            "| **4. Final Equation** | Rewrite $y(x)$ replacing $C$ with its exact number | Verify by plugging $(x_0, y_0)$ back in. |"
                        )
                    }
                },

                # PAGE 4 — worked_example (Level 1: Easy / Quadratic Curve Reconstruction)
                {
                    "page_number": 4,
                    "page_title": "Example 1: Reconstructing a Curve passing through (-4, 6)",
                    "block_type": "worked_example",
                    "component_type": "worked_example",
                    "content": {
                        "problem": (
                            "The gradient function of a curve is given by $\\frac{dy}{dx} = 2x + 1$.\n"
                            "If the curve passes through the point $(-4, 6)$:\n"
                            "(a) Find the particular equation of the curve.\n"
                            "(b) Determine the coordinates of the points where the curve cuts the $x$-axis."
                        ),
                        "steps": [
                            "**What we need to find:** Particular equation $y(x)$ and $x$-intercepts ($y = 0$).",
                            "**Step 1 — Integrate gradient function:**\n"
                            "$$y = \\int (2x + 1) \\, dx = x^2 + x + C$$",
                            "**Step 2 — Substitute boundary point $x = -4, y = 6$:**\n"
                            "$$6 = (-4)^2 + (-4) + C \\implies 6 = 16 - 4 + C \\implies 6 = 12 + C$$",
                            "**Step 3 — Solve for $C$:**\n"
                            "$$C = 6 - 12 = -6$$",
                            "**Step 4 — Write particular curve equation:**\n"
                            "$$y = x^2 + x - 6$$",
                            "**Step 5 — Find $x$-intercepts ($y = 0$):**\n"
                            "$$x^2 + x - 6 = 0 \\implies (x + 3)(x - 2) = 0 \\implies x = -3 \\quad \\text{or} \\quad x = 2$$\n\n"
                            "**Answer:** (a) $y = x^2 + x - 6$; (b) $x$-intercepts at $(-3, 0)$ and $(2, 0)$."
                        ]
                    }
                },

                # PAGE 5 — worked_example (Level 2: Moderate / Cubic Curve through (2, 3))
                {
                    "page_number": 5,
                    "page_title": "Example 2: Cubic Curve Reconstruction with Fractional Constant",
                    "block_type": "worked_example",
                    "component_type": "worked_example",
                    "content": {
                        "problem": (
                            "A curve has gradient function $\\frac{dy}{dx} = 2x^2 - 5$ and passes through $(2, 3)$.\n"
                            "Find the exact equation of the curve."
                        ),
                        "steps": [
                            "**What we need to find:** $y(x)$ with exact fractional constant $C$.",
                            "**Step 1 — Integrate gradient function:**\n"
                            "$$y = \\int (2x^2 - 5) \\, dx = \\frac{2x^3}{3} - 5x + C$$",
                            "**Step 2 — Substitute point $x = 2, y = 3$:**\n"
                            "$$3 = \\frac{2(2)^3}{3} - 5(2) + C = \\frac{16}{3} - 10 + C$$",
                            "**Step 3 — Convert to common denominator and solve for $C$:**\n"
                            "$$3 = 5\\frac{1}{3} - 10 + C = -4\\frac{2}{3} + C$$\n"
                            "$$C = 3 + 4\\frac{2}{3} = 7\\frac{2}{3} = \\frac{23}{3}$$",
                            "**Step 4 — Write final particular equation:**\n"
                            "$$y = \\frac{2}{3}x^3 - 5x + \\frac{23}{3} \\quad \\text{(or } 3y = 2x^3 - 15x + 23\\text{)}$$\n\n"
                            "**Answer:** $y = \\frac{2}{3}x^3 - 5x + \\frac{23}{3}$ (or $3y = 2x^3 - 15x + 23$)."
                        ]
                    }
                },

                # PAGE 6 — worked_example (Level 3: Difficult / Rational Gradient Function Reconstruction)
                {
                    "page_number": 6,
                    "page_title": "Example 3: Reconstructing Curve with Rational Gradient Terms",
                    "block_type": "worked_example",
                    "component_type": "worked_example",
                    "content": {
                        "problem": (
                            "The gradient of a curve is given by $\\frac{dy}{dx} = 3x^2 - \\frac{2}{x^2}$ for $x > 0$.\n"
                            "If the curve passes through the point $(1, 4)$, find its equation."
                        ),
                        "steps": [
                            "**What we need to find:** $y(x)$ using index notation.",
                            "**Step 1 — Rewrite gradient in index form:**\n"
                            "$$\\frac{dy}{dx} = 3x^2 - 2x^{-2}$$",
                            "**Step 2 — Integrate to find general solution:**\n"
                            "$$y = \\int (3x^2 - 2x^{-2}) \\, dx = \\frac{3x^3}{3} - \\frac{2x^{-1}}{-1} + C = x^3 + \\frac{2}{x} + C$$",
                            "**Step 3 — Substitute point $x = 1, y = 4$:**\n"
                            "$$4 = (1)^3 + \\frac{2}{1} + C = 1 + 2 + C = 3 + C$$",
                            "**Step 4 — Solve for $C$:**\n"
                            "$$C = 4 - 3 = 1$$",
                            "**Step 5 — Write final equation:**\n"
                            "$$y = x^3 + \\frac{2}{x} + 1$$\n\n"
                            "**Answer:** $y = x^3 + \\frac{2}{x} + 1$."
                        ]
                    }
                },

                # PAGE 7 — worked_example (Level 4: Exam-Style / Container Volume Optimization Constant)
                {
                    "page_number": 7,
                    "page_title": "Example 4: Industrial Container Volume Reconstruction",
                    "block_type": "worked_example",
                    "component_type": "worked_example",
                    "content": {
                        "problem": (
                            "The rate of volume accumulation in an industrial storage tank with height $h$ is given by $\\frac{dV}{dh} = 3h^2 + 4$.\n"
                            "When the height is $h = 0\\text{ meters}$, the tank contains a residual volume of $4\\text{ m}^3$.\n"
                            "Find the exact volume function $V(h)$ and calculate the total volume when $h = 3\\text{ meters}$."
                        ),
                        "steps": [
                            "**What we need to find:** Particular function $V(h)$ and $V(3)$.",
                            "**Step 1 — Integrate rate function $\\frac{dV}{dh}$:**\n"
                            "$$V(h) = \\int (3h^2 + 4) \\, dh = h^3 + 4h + C$$",
                            "**Step 2 — Substitute initial boundary condition $h = 0, V = 4$:**\n"
                            "$$4 = (0)^3 + 4(0) + C \\implies C = 4$$",
                            "**Step 3 — Write particular volume function:**\n"
                            "$$V(h) = h^3 + 4h + 4$$",
                            "**Step 4 — Evaluate volume at height $h = 3\\text{ meters}$:**\n"
                            "$$V(3) = (3)^3 + 4(3) + 4 = 27 + 12 + 4 = 43\\text{ m}^3$$\n\n"
                            "**Answer:** Particular equation $V(h) = h^3 + 4h + 4$; volume at $h = 3\\text{ m}$ is $43\\text{ m}^3$."
                        ]
                    }
                },

                # PAGE 8 — suggested_simulation
                {
                    "page_number": 8,
                    "page_title": "Explore: Boundary Point Anchor Simulator",
                    "block_type": "suggested_simulation",
                    "component_type": "suggested_simulation",
                    "content": {
                        "purpose": (
                            "An interactive boundary anchor simulator where students drag a benchmark pin $(x_0, y_0)$ across a coordinate grid. "
                            "As the pin moves, the app automatically recalculates constant $C$ and animates the corresponding particular curve locking onto the pin."
                        )
                    },
                    "asset_info": {
                        "asset_type": "simulation",
                        "archetype": "math_particular_solution_boundary_anchor",
                        "title": "Interactive Particular Solution Boundary Anchor Sandbox"
                    }
                },

                # PAGE 9 — common_misconception
                {
                    "page_number": 9,
                    "page_title": "Common Error: Substituting x into Derivative to find C",
                    "block_type": "common_misconception",
                    "component_type": "common_misconception",
                    "content": {
                        "text": (
                            "### The Derivative Substitution Error\n\n"
                            "When given $\\frac{dy}{dx} = 2x + 1$ and boundary point $(-4, 6)$, students often plug $(-4, 6)$ directly into the derivative equation:\n"
                            "$$6 = 2(-4) + 1 + C \\implies 6 = -7 + C \\implies C = 13 \\quad (\\text{WRONG!})$$\n\n"
                            "### Why This Is False:\n\n"
                            "$\\frac{dy}{dx}$ is the **gradient rate**, NOT the elevation formula! You must **INTEGRATE FIRST** to obtain $y = x^2 + x + C$ BEFORE plugging in the coordinate $(x, y)$!"
                        )
                    }
                },

                # PAGE 10 — knowledge_check (MCQ)
                {
                    "page_number": 10,
                    "page_title": "Check Your Understanding: Particular Solutions",
                    "block_type": "knowledge_check",
                    "component_type": "multiple_choice",
                    "content": {
                        "question": "If dy/dx = 4x - 3 and the curve passes through (2, 5), what is the value of constant C?",
                        "options": [
                            "A: C = -1",
                            "B: C = 3",
                            "C: C = 5",
                            "D: C = -3"
                        ],
                        "answer": "B",
                        "explanation": (
                            "1. Integrate: $y = \\int (4x - 3) \\, dx = 2x^2 - 3x + C$.\n"
                            "2. Substitute $(2, 5)$: $5 = 2(2)^2 - 3(2) + C = 8 - 6 + C = 2 + C$.\n"
                            "3. Solve: $C = 5 - 2 = 3$."
                        )
                    }
                },

                # PAGE 11 — summary
                {
                    "page_number": 11,
                    "page_title": "Key Takeaways: Particular Solutions",
                    "block_type": "summary",
                    "component_type": "summary",
                    "content": {
                        "text": (
                            "### Master Summary: Particular Solutions Checklist\n\n"
                            "| Concept | Formula | Key Purpose |\n"
                            "|:---|:---|:---|\n"
                            "| **General Solution** | $y = F(x) + C$ | Represents family of all parallel antiderivatives. |\n"
                            "| **Boundary Anchor** | $(x_0, y_0)$ | Given coordinate point used to calculate $C$. |\n"
                            "| **Particular Solution** | $y = F(x) + C_{\\text{exact}}$ | Unique curve passing through $(x_0, y_0)$. |\n"
                            "| **$x$-Intercepts** | Set $y = 0$ | Solves where the curve cuts the horizontal axis. |\n\n"
                            "**Verification Rule:** Always plug $(x_0, y_0)$ back into your final equation to verify!"
                        )
                    }
                }
            ]
        },

        # =====================================================================
        # MODULE 9.3: Definite Integration & Area Under Curves
        # =====================================================================
        {
            "unit_order": 3,
            "unit_title": "Module 9.3: Definite Integration, Area Under Curves, and Split-Region Integrals",
            "lesson_title": "Definite Integration, Area Under Curves, and Split-Region Integrals",
            "lesson_blocks": [
                # PAGE 1 — learning_goal
                {
                    "page_number": 1,
                    "page_title": "Mastering Definite Integration & Area Accumulation",
                    "block_type": "learning_goal",
                    "component_type": "learning_goal",
                    "content": {
                        "title": "What You Will Master in This Lesson",
                        "goals": [
                            "Evaluate definite integrals between boundaries $\\int_a^b y \\, dx = [F(x)]_a^b = F(b) - F(a)$.",
                            "Explain why the constant $+C$ cancels out algebraically during definite boundary subtraction.",
                            "Calculate the exact physical area bounded by a curve, the $x$-axis, and vertical lines $x=a, x=b$.",
                            "Execute split-interval integration when a curve crosses the $x$-axis to prevent area cancellation."
                        ]
                    }
                },

                # PAGE 2 — concept_explanation
                {
                    "page_number": 2,
                    "page_title": "Infinitesimal Vertical Strips: How Integrals Calculate Exact Area",
                    "block_type": "concept_explanation",
                    "component_type": "concept_explanation",
                    "content": {
                        "body": (
                            "How do we measure the area of an irregular shape with a curved top boundary?\n\n"
                            "### The Accumulating Strips Model\n\n"
                            "1. Imagine dividing the region under curve $y = f(x)$ into thin vertical rectangular strips of width $\\delta x$ and height $y$.\n"
                            "2. The area of one strip is $y \\cdot \\delta x$.\n"
                            "3. As the strip width $\\delta x \\to 0$, the sum of these infinitely thin strips becomes the exact **Definite Integral**:\n"
                            "   $$\\text{Area} = \\lim_{\\delta x \\to 0} \\sum y \\cdot \\delta x = \\int_a^b y \\, dx$$\n\n"
                            "### Why $+C$ Cancels Out\n\n"
                            "$$\\int_a^b y \\, dx = [F(x) + C]_a^b = [F(b) + C] - [F(a) + C] = F(b) - F(a)$$\n"
                            "Because $+C$ is subtracted from itself, it vanishes completely from all definite integrals!"
                        )
                    }
                },

                # PAGE 3 — formula_breakdown
                {
                    "page_number": 3,
                    "page_title": "Master Formulas: Definite Integrals & Split Areas",
                    "block_type": "formula_breakdown",
                    "component_type": "formula_breakdown",
                    "content": {
                        "formula": (
                            "**Definite Integral Evaluation Formula:**\n"
                            "$$\\int_a^b y \\, dx = [F(x)]_a^b = F(b) - F(a)$$\n\n"
                            "**Area Above the x-axis ($y \\ge 0$):**\n"
                            "$$\\text{Area} = \\int_a^b y \\, dx$$\n\n"
                            "**Area Below the x-axis ($y < 0$):**\n"
                            "$$\\text{Area} = \\left\\vert \\int_a^b y \\, dx \\right\\vert$$\n\n"
                            "**Split-Interval Integration Across Root $x = c$:**\n"
                            "$$\\text{Total Area} = \\left\\vert \\int_a^c y \\, dx \\right\\vert + \\left\\vert \\int_c^b y \\, dx \\right\\vert$$"
                        ),
                        "content": (
                            "### Single-Interval vs. Split-Interval Area Reference Table\n\n"
                            "| Curve Behavior | Integration Method | Common Pitfall |\n"
                            "|:---|:---|:---|\n"
                            "| **Entirely Above Axis ($y \\ge 0$)** | Single integral $\\int_a^b y \\, dx$ | None (result is positive). |\n"
                            "| **Entirely Below Axis ($y \\le 0$)** | $|\\int_a^b y \\, dx|$ | Neglecting to discard negative sign. |\n"
                            "| **Crosses Axis at Root $c \\in [a, b]$** | **Split at $c$**: $|\\int_a^c y \\, dx| + |\\int_c^b y \\, dx|$ | **Chunking $\\int_a^b$ in one step causes positive & negative areas to cancel out!** |"
                        )
                    }
                },

                # PAGE 4 — worked_example (Level 1: Easy / Basic Definite Evaluation)
                {
                    "page_number": 4,
                    "page_title": "Example 1: Evaluating a Definite Integral",
                    "block_type": "worked_example",
                    "component_type": "worked_example",
                    "content": {
                        "problem": (
                            "Evaluate the definite integral $\\int_2^3 (3x^2 - 4x + 5) \\, dx$."
                        ),
                        "steps": [
                            "**What we need to calculate:** Exact numeric value of $[F(x)]_2^3 = F(3) - F(2)$.",
                            "**Step 1 — Find general antiderivative $F(x)$:**\n"
                            "$$F(x) = \\int (3x^2 - 4x + 5) \\, dx = \\frac{3x^3}{3} - \\frac{4x^2}{2} + 5x = x^3 - 2x^2 + 5x$$",
                            "**Step 2 — Evaluate $F(3)$ (Upper Limit):**\n"
                            "$$F(3) = (3)^3 - 2(3)^2 + 5(3) = 27 - 18 + 15 = 24$$",
                            "**Step 3 — Evaluate $F(2)$ (Lower Limit):**\n"
                            "$$F(2) = (2)^3 - 2(2)^2 + 5(2) = 8 - 8 + 10 = 10$$",
                            "**Step 4 — Subtract $F(3) - F(2)$:**\n"
                            "$$\\int_2^3 (3x^2 - 4x + 5) \\, dx = 24 - 10 = 14$$\n\n"
                            "**Answer:** $14$."
                        ]
                    }
                },

                # PAGE 5 — worked_example (Level 2: Moderate / Area Under Axis y = x² - 9)
                {
                    "page_number": 5,
                    "page_title": "Example 2: Calculating Area Bounded Below the x-axis",
                    "block_type": "worked_example",
                    "component_type": "worked_example",
                    "content": {
                        "problem": (
                            "Calculate the area bounded by the parabola $y = x^2 - 9$, the $x$-axis, and vertical lines $x = 0$ and $x = 3$."
                        ),
                        "steps": [
                            "**What we need to find:** Physical area bounded below the axis.",
                            "**Step 1 — Inspect curve position for $x \\in [0, 3]$:**\n"
                            "For $x \\in [0, 3]$, $y = x^2 - 9 \\le 0$ (lies entirely below the $x$-axis).",
                            "**Step 2 — Set up definite integral:**\n"
                            "$$\\int_0^3 (x^2 - 9) \\, dx = \\left[ \\frac{x^3}{3} - 9x \\right]_0^3$$",
                            "**Step 3 — Evaluate upper limit $x = 3$:**\n"
                            "$$F(3) = \\frac{3^3}{3} - 9(3) = 9 - 27 = -18$$",
                            "**Step 4 — Evaluate lower limit $x = 0$:**\n"
                            "$$F(0) = 0 - 0 = 0$$",
                            "**Step 5 — Subtract and apply absolute value:**\n"
                            "$$\\int_0^3 (x^2 - 9) \\, dx = -18 - 0 = -18 \\implies \\text{Area} = |-18| = 18\\text{ square units}$$\n\n"
                            "**Answer:** $18\\text{ square units}$."
                        ]
                    }
                },

                # PAGE 6 — worked_example (Level 3: Difficult / Full Split-Interval Integration)
                {
                    "page_number": 6,
                    "page_title": "Example 3: Area of Region Crossing the x-axis (Split Integration)",
                    "block_type": "worked_example",
                    "component_type": "worked_example",
                    "content": {
                        "problem": (
                            "Find the total area enclosed by the curve $y = x^2 - 10x + 9$, the $x$-axis, "
                            "and vertical lines $x = 4$ and $x = 10$."
                        ),
                        "steps": [
                            "**What we need to find:** Total physical area by identifying crossing roots.",
                            "**Step 1 — Find roots of curve ($y = 0$):**\n"
                            "$$x^2 - 10x + 9 = 0 \\implies (x - 1)(x - 9) = 0 \\implies x = 1 \\quad \\text{or} \\quad x = 9$$",
                            "**Step 2 — Identify split intervals:**\n"
                            "Root $x = 9$ lies inside $[4, 10]$.\n"
                            "- Interval 1 ($[4, 9]$): Below axis ($y \\le 0$).\n"
                            "- Interval 2 ($[9, 10]$): Above axis ($y \\ge 0$).",
                            "**Step 3 — General antiderivative $F(x)$:**\n"
                            "$$F(x) = \\frac{x^3}{3} - 5x^2 + 9x$$",
                            "**Step 4 — Evaluate Interval 1 ($[4, 9]$):**\n"
                            "$$F(9) = 243 - 405 + 81 = -81$$\n"
                            "$$F(4) = \\frac{64}{3} - 80 + 36 = 21\\frac{1}{3} - 44 = -22\\frac{2}{3}$$\n"
                            "$$\\text{Area}_1 = \\left| F(9) - F(4) \\right| = \\left| -81 - \\left(-22\\frac{2}{3}\\right) \\right| = \\left| -58\\frac{1}{3} \\right| = 58\\frac{1}{3}$$",
                            "**Step 5 — Evaluate Interval 2 ($[9, 10]$):**\n"
                            "$$F(10) = \\frac{1000}{3} - 500 + 90 = 333\\frac{1}{3} - 410 = -76\\frac{2}{3}$$\n"
                            "$$\\text{Area}_2 = F(10) - F(9) = -76\\frac{2}{3} - (-81) = 4\\frac{1}{3}$$",
                            "**Step 6 — Sum absolute areas:**\n"
                            "$$\\text{Total Area} = 58\\frac{1}{3} + 4\\frac{1}{3} = 62\\frac{2}{3}\\text{ square units}$$\n\n"
                            "**Answer:** Total area is $62\\frac{2}{3}\\text{ square units}$ (or $62.67$)."
                        ]
                    }
                },

                # PAGE 7 — worked_example (Level 4: Exam-Style / Civil Engineering River Plot Survey)
                {
                    "page_number": 7,
                    "page_title": "Example 4: Civil Engineering Curved Boundary Survey",
                    "block_type": "worked_example",
                    "component_type": "worked_example",
                    "content": {
                        "problem": (
                            "A real estate plot is bounded by a straight road along the $x$-axis, vertical boundary fences at $x = 1\\text{ km}$ and $x = 4\\text{ km}$, "
                            "and a curved river path modeled by $y = 3x^2 + 2x + 1$ (in km).\n"
                            "Calculate the exact land area of the plot in square kilometers."
                        ),
                        "steps": [
                            "**What we need to calculate:** Definite integral $\\int_1^4 (3x^2 + 2x + 1) \\, dx$.",
                            "**Step 1 — Set up definite integral:**\n"
                            "$$\\text{Area} = \\int_1^4 (3x^2 + 2x + 1) \\, dx = \\left[ x^3 + x^2 + x \\right]_1^4$$",
                            "**Step 2 — Evaluate upper limit $x = 4$:**\n"
                            "$$F(4) = 4^3 + 4^2 + 4 = 64 + 16 + 4 = 84$$",
                            "**Step 3 — Evaluate lower limit $x = 1$:**\n"
                            "$$F(1) = 1^3 + 1^2 + 1 = 1 + 1 + 1 = 3$$",
                            "**Step 4 — Subtract upper minus lower limit:**\n"
                            "$$\\text{Area} = F(4) - F(1) = 84 - 3 = 81\\text{ km}^2$$\n\n"
                            "**Answer:** Total land area is $81\\text{ square kilometers}$."
                        ]
                    }
                },

                # PAGE 8 — suggested_simulation
                {
                    "page_number": 8,
                    "page_title": "Explore: Definite Limits & Shaded Area Accumulator",
                    "block_type": "suggested_simulation",
                    "component_type": "suggested_simulation",
                    "content": {
                        "purpose": (
                            "An interactive definite area accumulator with draggable limit handles $a$ and $b$ on the $x$-axis. "
                            "When the user drags limit $b$ past a curve root, the app highlights positive regions in green and negative regions in red, "
                            "displaying both the Net Definite Integral (with cancellation) and the Total Physical Area side-by-side."
                        )
                    },
                    "asset_info": {
                        "asset_type": "simulation",
                        "archetype": "math_definite_integral_area_accumulator",
                        "title": "Interactive Definite Limits & Area Accumulator Sandbox"
                    }
                },

                # PAGE 9 — common_misconception
                {
                    "page_number": 9,
                    "page_title": "Common Error: Chunked Integration Across Axis Roots",
                    "block_type": "common_misconception",
                    "component_type": "common_misconception",
                    "content": {
                        "text": (
                            "### The Chunked Integration Area Error\n\n"
                            "When finding area under $y = x^2 - 10x + 9$ from $x=4$ to $x=10$, integrating as one chunk gives:\n"
                            "$$\\int_4^{10} (x^2 - 10x + 9) \\, dx = F(10) - F(4) = -76\\frac{2}{3} - \\left(-22\\frac{2}{3}\\right) = -54 \\implies \\text{Area} = 54\\text{ (WRONG!)}$$\n\n"
                            "### Why This Fails:\n\n"
                            "The region below the axis ($-58.33$) cancels out $+4.33$ of the positive region! "
                            "**Golden Rule:** Always split integrals at $x$-axis roots and sum their absolute values ($58.33 + 4.33 = 62.67$)!"
                        )
                    }
                },

                # PAGE 10 — knowledge_check (MCQ)
                {
                    "page_number": 10,
                    "page_title": "Check Your Understanding: Definite Integrals & Area",
                    "block_type": "knowledge_check",
                    "component_type": "multiple_choice",
                    "content": {
                        "question": "What is the area bounded by the curve y = x², the x-axis, and lines x = 1 and x = 3?",
                        "options": [
                            "A: 8.67 square units (26/3)",
                            "B: 9 square units",
                            "C: 12 square units",
                            "D: 26 square units"
                        ],
                        "answer": "A",
                        "explanation": (
                            "1. Antiderivative: $F(x) = \\frac{x^3}{3}$.\n"
                            "2. $F(3) = \\frac{27}{3} = 9$.\n"
                            "3. $F(1) = \\frac{1}{3}$.\n"
                            "4. Area $= 9 - \\frac{1}{3} = \\frac{26}{3} = 8.67\\text{ square units}$."
                        )
                    }
                },

                # PAGE 11 — summary
                {
                    "page_number": 11,
                    "page_title": "Key Takeaways: Definite Integration & Area",
                    "block_type": "summary",
                    "component_type": "summary",
                    "content": {
                        "text": (
                            "### Master Summary: Definite Area Protocol\n\n"
                            "| Step | Action | Purpose |\n"
                            "|:---|:---|:---|\n"
                            "| **1. Root Check** | Solve $y = 0$ to find roots in $[a, b]$ | Prevents area cancellation across axis. |\n"
                            "| **2. Integrate** | Find antiderivative $F(x)$ (no $+C$ needed) | Prepares upper/lower limit evaluation. |\n"
                            "| **3. Evaluate** | Compute $F(b) - F(a)$ for each interval | Measures net change per interval. |\n"
                            "| **4. Absolute Sum** | Add $|\\text{Area}_1| + |\\text{Area}_2|$ | Yields total physical enclosed area. |\n\n"
                            "**Golden Rule:** Physical area can NEVER be negative!"
                        )
                    }
                }
            ]
        },

        # =====================================================================
        # MODULE 9.4: Area Between Intersecting Curves & Kinematics
        # =====================================================================
        {
            "unit_order": 4,
            "unit_title": "Module 9.4: Area Between Intersecting Curves and Integration in Kinematics",
            "lesson_title": "Area Between Intersecting Curves and Integration in Kinematics",
            "lesson_blocks": [
                # PAGE 1 — learning_goal
                {
                    "page_number": 1,
                    "page_title": "Mastering Intersecting Area & Reverse Kinematics",
                    "block_type": "learning_goal",
                    "component_type": "learning_goal",
                    "content": {
                        "title": "What You Will Master in This Lesson",
                        "goals": [
                            "Find intersection limits of two curves by solving $y_1(x) = y_2(x)$.",
                            "Calculate the area enclosed between intersecting functions using $\\int_{a}^{b} (y_{\\text{upper}} - y_{\\text{lower}}) \\, dx$.",
                            "Apply reverse integration to kinematics: velocity $v(t) = \\int a \\, dt + v_0$ and displacement $S(t) = \\int v \\, dt + S_0$.",
                            "Analyze vertical motion under gravity ($a = -10\\text{ m/s}^2$) to calculate peak height and total flight time."
                        ]
                    }
                },

                # PAGE 2 — concept_explanation
                {
                    "page_number": 2,
                    "page_title": "Crosshair Area & Rocket Telemetry: Reverse Kinematics",
                    "block_type": "concept_explanation",
                    "component_type": "concept_explanation",
                    "content": {
                        "body": (
                            "### Area Between Intersecting Curves\n\n"
                            "When two curves intersect (e.g. parabola $y = 9x - x^2$ and line $y = x$), "
                            "the enclosed region is the space between them.\n"
                            "- The area under the top parabola is $117.33$.\n"
                            "- The area under the lower line triangle is $32.00$.\n"
                            "- The net enclosed area between them is **$117.33 - 32.00 = 85.33\\text{ square units}$**!\n\n"
                            "### Rocket Telemetry (Reverse Kinematics)\n\n"
                            "In physics, we measure an engine's acceleration force $a(t)$. "
                            "By integrating acceleration, we reconstruct velocity $v(t)$. "
                            "By integrating velocity, we reconstruct displacement $S(t)$!"
                        )
                    }
                },

                # PAGE 3 — formula_breakdown
                {
                    "page_number": 3,
                    "page_title": "Master Formulas: Intersecting Area & Kinematics",
                    "block_type": "formula_breakdown",
                    "component_type": "formula_breakdown",
                    "content": {
                        "formula": (
                            "**Area Between Intersecting Curves:**\n"
                            "$$\\text{Area} = \\int_a^b (y_{\\text{upper}} - y_{\\text{lower}}) \\, dx \\quad \\text{where } a, b \\text{ are roots of } y_{\\text{upper}} = y_{\\text{lower}}$$\n\n"
                            "**Reverse Kinematic Vectors:**\n"
                            "$$v(t) = \\int a(t) \\, dt + v_0, \\qquad S(t) = \\int v(t) \\, dt + S_0$$\n\n"
                            "**Vertical Projectile Motion Equations ($a = -10\\text{ m/s}^2$):**\n"
                            "$$v(t) = v_0 - 10t, \\qquad S(t) = v_0 t - 5t^2$$"
                        ),
                        "content": (
                            "### Kinematic Integration Summary\n\n"
                            "| Vector Stage | Forward (Differentiation) | Reverse (Integration) | Boundary Anchor |\n"
                            "|:---|:---|:---|:---|\n"
                            "| **Displacement $S(t)$** | $\\frac{dS}{dt} = v(t)$ | $S(t) = \\int v(t) \\, dt + S_0$ | Initial position $S(0) = S_0$ |\n"
                            "| **Velocity $v(t)$** | $\\frac{dv}{dt} = a(t)$ | $v(t) = \\int a(t) \\, dt + v_0$ | Initial velocity $v(0) = v_0$ |\n"
                            "| **Acceleration $a(t)$** | Base input | Given engine/gravity rate | Constant gravity $a = -10\\text{ m/s}^2$ |"
                        )
                    }
                },

                # PAGE 4 — worked_example (Level 1: Easy / Area Between y = 9x - x² and y = x)
                {
                    "page_number": 4,
                    "page_title": "Example 1: Area Enclosed Between a Parabola and a Line",
                    "block_type": "worked_example",
                    "component_type": "worked_example",
                    "content": {
                        "problem": (
                            "Find the area enclosed by the curve $y = 9x - x^2$ and the line $y = x$."
                        ),
                        "steps": [
                            "**What we need to find:** Intersection limits $a, b$ and enclosed area.",
                            "**Step 1 — Equate functions to find intersection limits:**\n"
                            "$$9x - x^2 = x \\implies 8x - x^2 = 0 \\implies x(8 - x) = 0 \\implies a = 0 \\quad \\text{and} \\quad b = 8$$",
                            "**Step 2 — Set up single difference integral ($y_{\\text{upper}} - y_{\\text{lower}}$):**\n"
                            "$$\\text{Area} = \\int_0^8 ((9x - x^2) - x) \\, dx = \\int_0^8 (8x - x^2) \\, dx$$",
                            "**Step 3 — Find antiderivative $F(x)$:**\n"
                            "$$F(x) = \\left[ 4x^2 - \\frac{x^3}{3} \\right]_0^8$$",
                            "**Step 4 — Evaluate at upper limit $x = 8$:**\n"
                            "$$F(8) = 4(8)^2 - \\frac{8^3}{3} = 256 - \\frac{512}{3} = 256 - 170\\frac{2}{3} = 85\\frac{1}{3}$$",
                            "**Step 5 — Evaluate at lower limit $x = 0$:**\n"
                            "$$F(0) = 0 \\implies \\text{Area} = 85\\frac{1}{3} - 0 = 85\\frac{1}{3}\\text{ square units}$$\n\n"
                            "**Answer:** $85\\frac{1}{3}\\text{ square units}$ (or $85.33$)."
                        ]
                    }
                },

                # PAGE 5 — worked_example (Level 2: Moderate / Area Between y = x² and Line y = 4)
                {
                    "page_number": 5,
                    "page_title": "Example 2: Area Enclosed Between Parabola y = x² and Line y = 4",
                    "block_type": "worked_example",
                    "component_type": "worked_example",
                    "content": {
                        "problem": (
                            "Calculate the area enclosed between the curve $y = x^2$ and the horizontal line $y = 4$."
                        ),
                        "steps": [
                            "**What we need to find:** Intersections and enclosed area.",
                            "**Step 1 — Find intersection limits:**\n"
                            "$$x^2 = 4 \\implies x = -2 \\quad \\text{and} \\quad x = 2$$",
                            "**Step 2 — Identify upper and lower functions:**\n"
                            "Line $y = 4$ is upper; parabola $y = x^2$ is lower.",
                            "**Step 3 — Set up difference integral:**\n"
                            "$$\\text{Area} = \\int_{-2}^2 (4 - x^2) \\, dx = \\left[ 4x - \\frac{x^3}{3} \\right]_{-2}^2$$",
                            "**Step 4 — Evaluate upper limit $x = 2$:**\n"
                            "$$F(2) = 4(2) - \\frac{8}{3} = 8 - 2\\frac{2}{3} = 5\\frac{1}{3}$$",
                            "**Step 5 — Evaluate lower limit $x = -2$:**\n"
                            "$$F(-2) = 4(-2) - \\frac{-8}{3} = -8 + 2\\frac{2}{3} = -5\\frac{1}{3}$$",
                            "**Step 6 — Subtract $F(2) - F(-2)$:**\n"
                            "$$\\text{Area} = 5\\frac{1}{3} - \\left(-5\\frac{1}{3}\\right) = 10\\frac{2}{3}\\text{ square units}$$\n\n"
                            "**Answer:** $10\\frac{2}{3}\\text{ square units}$ (or $10.67$)."
                        ]
                    }
                },

                # PAGE 6 — worked_example (Level 3: Difficult / Vertical Kinematic Motion under Gravity)
                {
                    "page_number": 6,
                    "page_title": "Example 3: Vertical Kinematics under Gravity (v₀ = 40 m/s)",
                    "block_type": "worked_example",
                    "component_type": "worked_example",
                    "content": {
                        "problem": (
                            "A ball is projected vertically upwards from the ground with initial velocity $v_0 = 40\\text{ m/s}$. "
                            "Taking gravity $a = -10\\text{ m/s}^2$:\n"
                            "(a) Derive functions for velocity $v(t)$ and height $S(t)$.\n"
                            "(b) Calculate height at $t = 2\\text{ s}$, $t = 5\\text{ s}$, and $t = 8\\text{ s}$.\n"
                            "(c) Find maximum height and total flight time."
                        ),
                        "steps": [
                            "**What we need to calculate:** $v(t), S(t)$, heights at times, $S_{\\max}$, and return time.",
                            "**Step 1 — Integrate acceleration $a = -10$ to find velocity $v(t)$:**\n"
                            "$$v(t) = \\int (-10) \\, dt = -10t + C_1 \\implies v(0) = 40 \\implies C_1 = 40 \\implies v(t) = 40 - 10t$$",
                            "**Step 2 — Integrate velocity $v(t)$ to find height $S(t)$:**\n"
                            "$$S(t) = \\int (40 - 10t) \\, dt = 40t - 5t^2 + C_2 \\implies S(0) = 0 \\implies C_2 = 0 \\implies S(t) = 40t - 5t^2$$",
                            "**Step 3 — Evaluate heights:**\n"
                            "- $S(2) = 40(2) - 5(4) = 80 - 20 = 60\\text{ m}$.\n"
                            "- $S(5) = 40(5) - 5(25) = 200 - 125 = 75\\text{ m}$ (falling downwards).\n"
                            "- $S(8) = 40(8) - 5(64) = 320 - 320 = 0\\text{ m}$ (lands on ground).",
                            "**Step 4 — Maximum height (at rest $v = 0$):**\n"
                            "$$40 - 10t = 0 \\implies t = 4\\text{ s} \\implies S_{\\max} = S(4) = 40(4) - 5(16) = 160 - 80 = 80\\text{ m}$$\n\n"
                            "**Answer:** (a) $v = 40 - 10t, S = 40t - 5t^2$; (b) $60\\text{ m}, 75\\text{ m}, 0\\text{ m}$; (c) Peak height $80\\text{ m}$ at $t = 4\\text{ s}$, total flight $8\\text{ s}$."
                        ]
                    }
                },

                # PAGE 7 — worked_example (Level 4: Exam-Style / Rocket Acceleration Integration)
                {
                    "page_number": 7,
                    "page_title": "Example 4: Rocket Telemetry Variable Acceleration Integration",
                    "block_type": "worked_example",
                    "component_type": "worked_example",
                    "content": {
                        "problem": (
                            "A research rocket launches from rest at $S = 0$ with variable acceleration $a(t) = 6t - 4$ (in $\\text{m/s}^2$).\n"
                            "Find:\n"
                            "(a) The velocity function $v(t)$.\n"
                            "(b) The displacement function $S(t)$.\n"
                            "(c) The velocity and displacement after $5\\text{ seconds}$."
                        ),
                        "steps": [
                            "**What we need to find:** $v(t), S(t), v(5), S(5)$.",
                            "**Step 1 — Integrate $a(t)$ to find $v(t)$:**\n"
                            "$$v(t) = \\int (6t - 4) \\, dt = 3t^2 - 4t + C_1$$\n"
                            "Since rocket launches from rest: $v(0) = 0 \\implies C_1 = 0 \\implies v(t) = 3t^2 - 4t$.",
                            "**Step 2 — Integrate $v(t)$ to find $S(t)$:**\n"
                            "$$S(t) = \\int (3t^2 - 4t) \\, dt = t^3 - 2t^2 + C_2$$\n"
                            "Since launch point is origin: $S(0) = 0 \\implies C_2 = 0 \\implies S(t) = t^3 - 2t^2$.",
                            "**Step 3 — Evaluate at $t = 5\\text{ seconds}$:**\n"
                            "$$v(5) = 3(5)^2 - 4(5) = 75 - 20 = 55\\text{ m/s}$$\n"
                            "$$S(5) = (5)^3 - 2(5)^2 = 125 - 50 = 75\\text{ m}$$\n\n"
                            "**Answer:** (a) $v(t) = 3t^2 - 4t$; (b) $S(t) = t^3 - 2t^2$; (c) Velocity $55\\text{ m/s}$, displacement $75\\text{ m}$."
                        ]
                    }
                },

                # PAGE 8 — suggested_simulation
                {
                    "page_number": 8,
                    "page_title": "Explore: Intersecting Curves & Kinematics Sandbox",
                    "block_type": "suggested_simulation",
                    "component_type": "suggested_simulation",
                    "content": {
                        "purpose": (
                            "An interactive dual-mode simulator. Mode 1 lets students adjust intersection limits between parabola and line to watch the shaded crosshair area compute dynamically. "
                            "Mode 2 lets students fire a projectile under gravity, animating real-time $a(t) \\to v(t) \\to S(t)$ graphs side-by-side."
                        )
                    },
                    "asset_info": {
                        "asset_type": "simulation",
                        "archetype": "math_intersecting_curves_kinematics_sandbox",
                        "title": "Interactive Intersecting Curves & Kinematics Sandbox"
                    }
                },

                # PAGE 9 — common_misconception
                {
                    "page_number": 9,
                    "page_title": "Common Error: Inverted Curve Subtraction Order",
                    "block_type": "common_misconception",
                    "component_type": "common_misconception",
                    "content": {
                        "text": (
                            "### Inverted Curve Subtraction Error\n\n"
                            "When calculating the area between curves, subtracting in the wrong order ($y_{\\text{lower}} - y_{\\text{upper}}$) gives a negative result:\n"
                            "$$\\int_0^8 (x - (9x - x^2)) \\, dx = \\int_0^8 (x^2 - 8x) \\, dx = -85\\frac{1}{3} \\quad (\\text{WRONG SIGN!})$$\n\n"
                            "### Correction:\n\n"
                            "Always subtract the lower curve from the upper curve: **$\\text{Area} = \\int_a^b (y_{\\text{upper}} - y_{\\text{lower}}) \\, dx$**!"
                        )
                    }
                },

                # PAGE 10 — knowledge_check (MCQ)
                {
                    "page_number": 10,
                    "page_title": "Check Your Understanding: Intersecting Area",
                    "block_type": "knowledge_check",
                    "component_type": "multiple_choice",
                    "content": {
                        "question": "What is the area enclosed between y = x and y = x²?",
                        "options": [
                            "A: 1/6 square units (0.167)",
                            "B: 1/3 square units",
                            "C: 1/2 square units",
                            "D: 1 square unit"
                        ],
                        "answer": "A",
                        "explanation": (
                            "1. Intersections: $x^2 = x \\implies x(x - 1) = 0 \\implies a = 0, b = 1$.\n"
                            "2. Integral: $\\int_0^1 (x - x^2) \\, dx = \\left[ \\frac{x^2}{2} - \\frac{x^3}{3} \\right]_0^1$.\n"
                            "3. Area $= \\frac{1}{2} - \\frac{1}{3} = \\frac{1}{6}\\text{ square units}$."
                        )
                    }
                },

                # PAGE 11 — summary
                {
                    "page_number": 11,
                    "page_title": "Key Takeaways: Intersecting Area & Kinematics",
                    "block_type": "summary",
                    "component_type": "summary",
                    "content": {
                        "text": (
                            "### Master Summary: Advanced Integration Checklist\n\n"
                            "| Application | Core Formula | Key Step |\n"
                            "|:---|:---|:---|\n"
                            "| **Intersecting Area** | $\\text{Area} = \\int_a^b (y_{\\text{upper}} - y_{\\text{lower}}) \\, dx$ | Solve $y_1 = y_2$ for limits $a, b$. |\n"
                            "| **Velocity Vector** | $v(t) = \\int a(t) \\, dt + v_0$ | Use initial velocity $v(0) = v_0$. |\n"
                            "| **Displacement Vector** | $S(t) = \\int v(t) \\, dt + S_0$ | Use initial position $S(0) = S_0$. |\n"
                            "| **Gravity Acceleration** | $a = -10\\text{ m/s}^2$ | Peak height occurs when $v(t) = 0$. |\n\n"
                            "**Form 4 Mathematics Integration Mastery Complete!**"
                        )
                    }
                }
            ]
        }
    ]


def ingest_topic9_integration():
    """Main ingestion runner for Topic 9: Integration."""
    print("=" * 80)
    print("VLearn Form 4 Mathematics — Topic 9: Integration")
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

    # 2. Get or create Topic 9
    topic_name = "Topic 9: Integration"
    topic, topic_created = Topic.objects.get_or_create(
        subject=subject,
        order=9,
        defaults={"name": topic_name}
    )
    if not topic_created and topic.name != topic_name:
        topic.name = topic_name
        topic.save()
    print(f"Found Topic: {topic.name} (ID: {topic.id})")

    modules_data = get_topic9_data()
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
    ingest_topic9_integration()
