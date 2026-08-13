#!/usr/bin/env python3
"""
VLearn Form 4 Mathematics — Topic 8: Differentiation Ingestion Script
======================================================================
Curriculum: 844
Grade: Form 4 (level=1)
Subject: Mathematics
Topic: Topic 8: Differentiation (order=8)

Modules / LearningUnits:
  8.1 Rates of Change, Delta Notation, and Derivative from First Principles (h-method)
  8.2 Polynomial Differentiation Mechanics and the Power Rule Shortcut
  8.3 Tangents, Normals, and Stationary Turning Points of Curves
  8.4 Kinematics Applications and Real-World Optimization

Pedagogical Structure per Lesson: 11 Pages (44 blocks total)
  Page 1:  learning_goal (Student-friendly outcomes)
  Page 2:  concept_explanation (Real-world analogies: speedometer vs trip average, factory shortcuts, ball on a string)
  Page 3:  formula_breakdown / definition_card (Word formulas, limits, power rules, tangent/normal equations, kinematics)
  Page 4:  worked_example (Level 1: Easy / Foundation)
  Page 5:  worked_example (Level 2: Moderate / Multi-step)
  Page 6:  worked_example (Level 3: Difficult / Exam standard)
  Page 7:  worked_example (Level 4: Exam-Style / Real-World Synthesis)
  Page 8:  suggested_simulation (Interactive visual sandbox)
  Page 9:  common_misconception (Diagnostic error analysis & memory tips)
  Page 10: knowledge_check (MCQ / Short-answer with step-by-step solutions)
  Page 11: summary (Key takeaways & differentiation checklist)

Standards Enforced:
  - Clean responsive Markdown tables (zero raw \\begin{array} or \\hline).
  - Explicit bold labels on all formula breakdowns.
  - Correct normalized equations (fixing source text bugs: y = x^3 - 3x + 2, v = 3 + 10t - t^2, normal y = -1/5 x + 21/5).
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


def get_topic8_data():
    """Returns the complete structured curriculum payload for Topic 8."""
    return [
        # =====================================================================
        # MODULE 8.1: Rates of Change, Delta Notation, and First Principles
        # =====================================================================
        {
            "unit_order": 1,
            "unit_title": "Module 8.1: Rates of Change, Delta Notation, and Derivative from First Principles",
            "lesson_title": "Rates of Change, Delta Notation, and Derivative from First Principles (h-method)",
            "lesson_blocks": [
                # PAGE 1 — learning_goal
                {
                    "page_number": 1,
                    "page_title": "Mastering Rates of Change & The First Principles Limit Concept",
                    "block_type": "learning_goal",
                    "component_type": "learning_goal",
                    "content": {
                        "title": "What You Will Master in This Lesson",
                        "goals": [
                            "Distinguish between average rate of change (secant slope) and instantaneous rate of change (tangent slope).",
                            "Relate delta notation ($\\Delta x, \\Delta y$) to small coordinate increments on a curved graph.",
                            "Derive gradient functions from first principles using the algebraic $h$-method.",
                            "Understand the limit definition $\\frac{dy}{dx} = \\lim_{h \\to 0} \\frac{f(x+h) - f(x)}{h}$."
                        ]
                    }
                },

                # PAGE 2 — concept_explanation
                {
                    "page_number": 2,
                    "page_title": "The Speedometer vs. Trip Average Analogy",
                    "block_type": "concept_explanation",
                    "component_type": "concept_explanation",
                    "content": {
                        "body": (
                            "Imagine driving a car from Nairobi to Nakuru ($160\\text{ km}$) in $2\\text{ hours}$:\n\n"
                            "### Average Rate vs. Instantaneous Rate\n\n"
                            "- **Average Speed (Secant Slope):**\n"
                            "  Total Distance $\\div$ Total Time $= \\frac{160}{2} = 80\\text{ km/h}$. "
                            "  This connects the trip start and endpoint with a straight **secant line**.\n"
                            "- **Instantaneous Speed (Tangent Slope):**\n"
                            "  At exactly $1\\text{ hour}$ and $15\\text{ minutes}$, your speedometer reads $110\\text{ km/h}$ while passing a lorry! "
                            "  This is your **instantaneous rate of change** at that exact micro-second.\n\n"
                            "### Zooming in on a Curved Graph\n\n"
                            "If you zoom in extremely close to any point $P$ on a smooth curve, the curve starts to look like a straight line! "
                            "By taking a neighboring point $Q(x+h, f(x+h))$ and shrinking the gap $h \\to 0$, the secant line $PQ$ rotates into the exact **tangent line** at $P$."
                        )
                    }
                },

                # PAGE 3 — formula_breakdown
                {
                    "page_number": 3,
                    "page_title": "Master Formulas: First Principles & Delta Notation",
                    "block_type": "formula_breakdown",
                    "component_type": "formula_breakdown",
                    "content": {
                        "formula": (
                            "**First Principles Derivative Definition (h-method):**\n"
                            "$$\\frac{dy}{dx} = \\lim_{h \\to 0} \\frac{f(x+h) - f(x)}{h}$$\n\n"
                            "**Delta Notation Gradient:**\n"
                            "$$\\frac{dy}{dx} = \\lim_{\\Delta x \\to 0} \\frac{\\Delta y}{\\Delta x}$$\n\n"
                            "**Secant Slope to Tangent Gradient Conversion:**\n"
                            "$$\\text{Secant Slope } m_{PQ} = \\frac{(x+h)^2 - x^2}{h} = 2x + h \\xrightarrow{h \\to 0} \\text{Tangent Slope } m = 2x$$"
                        ),
                        "content": (
                            "### Step-by-Step $h$-Method Derivation Protocol\n\n"
                            "| Step | Algebraic Action | Reason |\n"
                            "|:---|:---|:---|\n"
                            "| **1. Define Points** | Set $P(x, f(x))$ and $Q(x+h, f(x+h))$ | Establish endpoints of the secant line. |\n"
                            "| **2. Calculate $\\Delta y$** | $\\Delta y = f(x+h) - f(x)$ | Measure vertical rise between $P$ and $Q$. |\n"
                            "| **3. Expand & Simplify** | Expand binomial terms and subtract $f(x)$ | Isolate terms containing $h$. |\n"
                            "| **4. Form Secant Ratio** | $\\frac{\\Delta y}{\\Delta x} = \\frac{f(x+h) - f(x)}{h}$ | Divide vertical rise by horizontal run $h$. |\n"
                            "| **5. Factor & Cancel $h$** | Factor out $h$ from numerator and cancel | Divide out common factor $h$ ($h \\neq 0$). |\n"
                            "| **6. Take Limit $h \\to 0$** | Let $h \\to 0$ to obtain $\\frac{dy}{dx}$ | Shrink gap to 0 to yield exact tangent slope. |"
                        )
                    }
                },

                # PAGE 4 — worked_example (Level 1: Easy / Gradient of y = x² at (3, 9))
                {
                    "page_number": 4,
                    "page_title": "Example 1: Gradient of y = x² from First Principles",
                    "block_type": "worked_example",
                    "component_type": "worked_example",
                    "content": {
                        "problem": (
                            "Derive the gradient function of the curve $y = x^2$ using first principles (the $h$-method), "
                            "and calculate the exact gradient at the point $(3, 9)$."
                        ),
                        "steps": [
                            "**What we need to find:** The derived function $\\frac{dy}{dx}$ and its value at $x = 3$.",
                            "**Step 1 — Set up point coordinates:**\n"
                            "Let $P = (x, x^2)$ and neighboring point $Q = (x+h, (x+h)^2)$.",
                            "**Step 2 — Calculate vertical change $\\Delta y$:**\n"
                            "$$\\Delta y = (x+h)^2 - x^2 = (x^2 + 2xh + h^2) - x^2 = 2xh + h^2$$",
                            "**Step 3 — Form the secant slope fraction:**\n"
                            "$$\\frac{\\Delta y}{\\Delta x} = \\frac{2xh + h^2}{h} = \\frac{h(2x + h)}{h} = 2x + h \\quad (h \\neq 0)$$",
                            "**Step 4 — Apply the limit $h \\to 0$:**\n"
                            "$$\\frac{dy}{dx} = \\lim_{h \\to 0} (2x + h) = 2x$$",
                            "**Step 5 — Evaluate at $x = 3$:**\n"
                            "$$\\text{At } x = 3, \\quad m = 2(3) = 6$$\n\n"
                            "**Answer:** Gradient function is $\\frac{dy}{dx} = 2x$, and the gradient at $(3, 9)$ is $6$."
                        ]
                    }
                },

                # PAGE 5 — worked_example (Level 2: Moderate / Gradient of y = 3x² + 4x)
                {
                    "page_number": 5,
                    "page_title": "Example 2: First Principles Derivation of a Quadratic Function",
                    "block_type": "worked_example",
                    "component_type": "worked_example",
                    "content": {
                        "problem": (
                            "Use the first-principles limit definition to find the derivative of $f(x) = 3x^2 + 4x$."
                        ),
                        "steps": [
                            "**What we need to find:** $\\frac{df}{dx}$ using $\\lim_{h \\to 0} \\frac{f(x+h) - f(x)}{h}$.",
                            "**Step 1 — Evaluate $f(x+h)$:**\n"
                            "$$f(x+h) = 3(x+h)^2 + 4(x+h) = 3(x^2 + 2xh + h^2) + 4x + 4h = 3x^2 + 6xh + 3h^2 + 4x + 4h$$",
                            "**Step 2 — Calculate $f(x+h) - f(x)$:**\n"
                            "$$f(x+h) - f(x) = (3x^2 + 6xh + 3h^2 + 4x + 4h) - (3x^2 + 4x) = 6xh + 3h^2 + 4h$$",
                            "**Step 3 — Divide by $h$:**\n"
                            "$$\\frac{f(x+h) - f(x)}{h} = \\frac{h(6x + 3h + 4)}{h} = 6x + 3h + 4$$",
                            "**Step 4 — Take the limit as $h \\to 0$:**\n"
                            "$$\\frac{df}{dx} = \\lim_{h \\to 0} (6x + 3h + 4) = 6x + 4$$\n\n"
                            "**Answer:** Derivative is $\\frac{df}{dx} = 6x + 4$."
                        ]
                    }
                },

                # PAGE 6 — worked_example (Level 3: Difficult / First Principles of a Cubic Curve)
                {
                    "page_number": 6,
                    "page_title": "Example 3: First Principles Derivation of y = x³",
                    "block_type": "worked_example",
                    "component_type": "worked_example",
                    "content": {
                        "problem": (
                            "Derive the gradient function of $y = x^3$ from first principles using binomial expansion."
                        ),
                        "steps": [
                            "**What we need to find:** $\\frac{dy}{dx}$ for $y = x^3$.",
                            "**Step 1 — Set up point coordinates and $\\Delta y$:**\n"
                            "$$\\Delta y = (x+h)^3 - x^3$$",
                            "**Step 2 — Expand $(x+h)^3$ via binomial expansion:**\n"
                            "$$(x+h)^3 = x^3 + 3x^2h + 3xh^2 + h^3$$",
                            "**Step 3 — Subtract $x^3$:**\n"
                            "$$\\Delta y = (x^3 + 3x^2h + 3xh^2 + h^3) - x^3 = 3x^2h + 3xh^2 + h^3$$",
                            "**Step 4 — Divide by $h$:**\n"
                            "$$\\frac{\\Delta y}{\\Delta x} = \\frac{h(3x^2 + 3xh + h^2)}{h} = 3x^2 + 3xh + h^2$$",
                            "**Step 5 — Take the limit as $h \\to 0$:**\n"
                            "$$\\frac{dy}{dx} = \\lim_{h \\to 0} (3x^2 + 3xh + h^2) = 3x^2 + 0 + 0 = 3x^2$$\n\n"
                            "**Answer:** Gradient function is $\\frac{dy}{dx} = 3x^2$."
                        ]
                    }
                },

                # PAGE 7 — worked_example (Level 4: Exam-Style / Rational Function First Principles)
                {
                    "page_number": 7,
                    "page_title": "Example 4: First Principles Derivation of a Rational Curve y = 1/x",
                    "block_type": "worked_example",
                    "component_type": "worked_example",
                    "content": {
                        "problem": (
                            "Find the derivative of $y = \\frac{1}{x}$ from first principles for $x \\neq 0$."
                        ),
                        "steps": [
                            "**What we need to find:** $\\frac{dy}{dx}$ for $y = \\frac{1}{x}$.",
                            "**Step 1 — Set up $f(x+h) - f(x)$:**\n"
                            "$$\\Delta y = \\frac{1}{x+h} - \\frac{1}{x}$$",
                            "**Step 2 — Combine into a single fraction over common denominator:**\n"
                            "$$\\Delta y = \\frac{x - (x+h)}{x(x+h)} = \\frac{-h}{x(x+h)}$$",
                            "**Step 3 — Divide by $h$:**\n"
                            "$$\\frac{\\Delta y}{\\Delta x} = \\frac{-h}{h \\cdot x(x+h)} = \\frac{-1}{x(x+h)}$$",
                            "**Step 4 — Take the limit as $h \\to 0$:**\n"
                            "$$\\frac{dy}{dx} = \\lim_{h \\to 0} \\left( \\frac{-1}{x(x+h)} \\right) = \\frac{-1}{x(x+0)} = -\\frac{1}{x^2}$$\n\n"
                            "**Answer:** $\\frac{dy}{dx} = -\\frac{1}{x^2}$ (or $-x^{-2}$)."
                        ]
                    }
                },

                # PAGE 8 — suggested_simulation
                {
                    "page_number": 8,
                    "page_title": "Explore: Secant-to-Tangent Interactive Animator",
                    "block_type": "suggested_simulation",
                    "component_type": "suggested_simulation",
                    "content": {
                        "purpose": (
                            "An interactive graphic simulator where students drag a slider reducing $h$ from $2.0$ down to $0.001$. "
                            "The app displays the rotating secant line $PQ$ smoothly merging onto the tangent line at $P(2, 4)$, "
                            "showing the numerical secant slope converging from $6.0$ to $4.000$ in real-time."
                        )
                    },
                    "asset_info": {
                        "asset_type": "simulation",
                        "archetype": "math_secant_to_tangent_animator",
                        "title": "Interactive Secant-to-Tangent Animator Sandbox"
                    }
                },

                # PAGE 9 — common_misconception
                {
                    "page_number": 9,
                    "page_title": "Common Error: Binomial Expansion Distribution Trap",
                    "block_type": "common_misconception",
                    "component_type": "common_misconception",
                    "content": {
                        "text": (
                            "### The Missing Middle Term Error\n\n"
                            "Students frequently expand $(x+h)^2$ as $x^2 + h^2$, ignoring the middle term $2xh$.\n\n"
                            "### Why This Breaks the $h$-Method:\n\n"
                            "$$\\Delta y = (x^2 + h^2) - x^2 = h^2 \\implies \\frac{\\Delta y}{\\Delta x} = \\frac{h^2}{h} = h \\xrightarrow{h \\to 0} 0$$\n"
                            "This results in a derivative of zero for *all* quadratic curves, which is completely false!\n\n"
                            "> **Memory Tip:** Always expand binomials completely: $(a+b)^2 = a^2 + 2ab + b^2$. The middle term $2xh$ is the exact term that gives rise to the derivative $2x$!"
                        )
                    }
                },

                # PAGE 10 — knowledge_check (MCQ)
                {
                    "page_number": 10,
                    "page_title": "Check Your Understanding: First Principles",
                    "block_type": "knowledge_check",
                    "component_type": "multiple_choice",
                    "content": {
                        "question": "What is the gradient of the curve y = x² at the point (-4, 16)?",
                        "options": [
                            "A: 16",
                            "B: -8",
                            "C: 8",
                            "D: -4"
                        ],
                        "answer": "B",
                        "explanation": (
                            "1. The gradient function of $y = x^2$ is $\\frac{dy}{dx} = 2x$.\n"
                            "2. At $x = -4$, the gradient is $m = 2(-4) = -8$."
                        )
                    }
                },

                # PAGE 11 — summary
                {
                    "page_number": 11,
                    "page_title": "Key Takeaways: First Principles & Rates of Change",
                    "block_type": "summary",
                    "component_type": "summary",
                    "content": {
                        "text": (
                            "### Master Summary: First Principles Concepts\n\n"
                            "| Concept | Formula | Key Insight |\n"
                            "|:---|:---|:---|\n"
                            "| **Secant Slope** | $\\frac{f(x+h) - f(x)}{h}$ | Average rate of change across interval $h$. |\n"
                            "| **Tangent Slope** | $\\frac{dy}{dx} = \\lim_{h \\to 0} \\frac{f(x+h) - f(x)}{h}$ | Instantaneous rate of change at point $x$. |\n"
                            "| **Delta Notation** | $\\frac{dy}{dx} = \\lim_{\\Delta x \\to 0} \\frac{\\Delta y}{\\Delta x}$ | Ratio of infinitesimal coordinate changes. |\n\n"
                            "**Limit Rule:** Always simplify algebraically and cancel $h$ from the denominator BEFORE letting $h \\to 0$!"
                        )
                    }
                }
            ]
        },

        # =====================================================================
        # MODULE 8.2: Polynomial Differentiation Mechanics & Power Rule
        # =====================================================================
        {
            "unit_order": 2,
            "unit_title": "Module 8.2: Polynomial Differentiation Mechanics and the Power Rule Shortcut",
            "lesson_title": "Polynomial Differentiation Mechanics and the Power Rule Shortcut",
            "lesson_blocks": [
                # PAGE 1 — learning_goal
                {
                    "page_number": 1,
                    "page_title": "Mastering Polynomial Differentiation & Power Rules",
                    "block_type": "learning_goal",
                    "component_type": "learning_goal",
                    "content": {
                        "title": "What You Will Master in This Lesson",
                        "goals": [
                            "Apply the Polynomial Power Rule shortcut $\\frac{d}{dx}(a x^n) = n a x^{n-1}$ to differentiate terms rapidly.",
                            "Understand why the derivative of any constant $C$ is strictly $0$.",
                            "Differentiate multi-term polynomials term-by-term using the Linearity Sum Rule.",
                            "Differentiate terms with negative powers ($x^{-n}$) and fractional powers ($x^{p/q}$)."
                        ]
                    }
                },

                # PAGE 2 — concept_explanation
                {
                    "page_number": 2,
                    "page_title": "The Factory Shortcut: Why Power Rules Work",
                    "block_type": "concept_explanation",
                    "component_type": "concept_explanation",
                    "content": {
                        "body": (
                            "Going through the first-principles $h$-method every single time would take hours for long formulas!\n\n"
                            "### The Power Rule Shortcut\n\n"
                            "Mathematicians observed a clear algebraic pattern across all first-principles derivations:\n"
                            "- $y = x^2 \\implies \\frac{dy}{dx} = 2x^1$\n"
                            "- $y = x^3 \\implies \\frac{dy}{dx} = 3x^2$\n"
                            "- $y = x^4 \\implies \\frac{dy}{dx} = 4x^3$\n\n"
                            "**The Power Rule Recipe:**\n"
                            "1. **Multiply** the front coefficient by the current exponent $n$.\n"
                            "2. **Subtract $1$** from the exponent ($n - 1$).\n"
                            "3. **Constants vanish** because a constant function $y = C$ is a flat horizontal line with slope $0$!"
                        )
                    }
                },

                # PAGE 3 — formula_breakdown
                {
                    "page_number": 3,
                    "page_title": "Master Formulas: Polynomial Power Rules & Operations",
                    "block_type": "formula_breakdown",
                    "component_type": "formula_breakdown",
                    "content": {
                        "formula": (
                            "**The Polynomial Power Rule:**\n"
                            "$$\\frac{d}{dx}\\left( a x^n \\right) = n \\cdot a x^{n-1}$$\n\n"
                            "**Derivative of a Constant:**\n"
                            "$$\\frac{d}{dx}(C) = 0 \\quad \\text{(where } C \\text{ is any constant real number)}$$\n\n"
                            "**Linearity / Sum Rule:**\n"
                            "$$\\frac{d}{dx}\\left[ f(x) + g(x) - h(x) \\right] = f'(x) + g'(x) - h'(x)$$"
                        ),
                        "content": (
                            "### Power Rule Quick Reference Table\n\n"
                            "| Term Type | Original Function $y(x)$ | Derivative $\\frac{dy}{dx}$ | Example |\n"
                            "|:---|:---|:---|:---|\n"
                            "| **Standard Power** | $a x^n$ | $n a x^{n-1}$ | $\\frac{d}{dx}(5x^3) = 15x^2$ |\n"
                            "| **Linear Term** | $k x$ | $k$ | $\\frac{d}{dx}(7x) = 7$ |\n"
                            "| **Constant** | $C$ | $0$ | $\\frac{d}{dx}(12) = 0$ |\n"
                            "| **Negative Power** | $a x^{-n} = \\frac{a}{x^n}$ | $-n a x^{-n-1} = -\\frac{n a}{x^{n+1}}$ | $\\frac{d}{dx}\\left(\\frac{2}{x^2}\\right) = -\\frac{4}{x^3}$ |\n"
                            "| **Radical / Fractional** | $a \\sqrt{x} = a x^{1/2}$ | $\\frac{a}{2} x^{-1/2} = \\frac{a}{2\\sqrt{x}}$ | $\\frac{d}{dx}(4\\sqrt{x}) = \\frac{2}{\\sqrt{x}}$ |"
                        )
                    }
                },

                # PAGE 4 — worked_example (Level 1: Easy / Polynomial Differentiation)
                {
                    "page_number": 4,
                    "page_title": "Example 1: Differentiating a Standard Polynomial",
                    "block_type": "worked_example",
                    "component_type": "worked_example",
                    "content": {
                        "problem": (
                            "Differentiate the polynomial $y = 5x^3 + 9x^2 + 7x + 3$ with respect to $x$."
                        ),
                        "steps": [
                            "**What we need to find:** $\\frac{dy}{dx}$ term-by-term.",
                            "**Step 1 — Apply power rule to $5x^3$:**\n"
                            "$$\\frac{d}{dx}(5x^3) = 3 \\cdot 5 x^{3-1} = 15x^2$$",
                            "**Step 2 — Apply power rule to $9x^2$:**\n"
                            "$$\\frac{d}{dx}(9x^2) = 2 \\cdot 9 x^{2-1} = 18x$$",
                            "**Step 3 — Apply power rule to linear term $7x$:**\n"
                            "$$\\frac{d}{dx}(7x) = 1 \\cdot 7 x^{1-1} = 7x^0 = 7$$",
                            "**Step 4 — Apply derivative of constant $3$:**\n"
                            "$$\\frac{d}{dx}(3) = 0$$",
                            "**Step 5 — Combine terms:**\n"
                            "$$\\frac{dy}{dx} = 15x^2 + 18x + 7$$\n\n"
                            "**Answer:** $\\frac{dy}{dx} = 15x^2 + 18x + 7$."
                        ]
                    }
                },

                # PAGE 5 — worked_example (Level 2: Moderate / Differentiation of Expansion Terms)
                {
                    "page_number": 5,
                    "page_title": "Example 2: Differentiating Product and Division Polynomials",
                    "block_type": "worked_example",
                    "component_type": "worked_example",
                    "content": {
                        "problem": (
                            "Find $\\frac{dy}{dx}$ for:\n"
                            "(a) $y = (2x + 1)(x - 3)$\n"
                            "(b) $y = \\frac{x^3 + 4x^2}{x}$"
                        ),
                        "steps": [
                            "**What we need to do:** Expand or simplify expressions into polynomial form BEFORE applying the power rule.",
                            "**Step 1 — Part (a): Expand the product:**\n"
                            "$$y = 2x^2 - 6x + x - 3 = 2x^2 - 5x - 3$$",
                            "**Step 2 — Differentiate Part (a):**\n"
                            "$$\\frac{dy}{dx} = 4x - 5$$",
                            "**Step 3 — Part (b): Divide each term by $x$:**\n"
                            "$$y = \\frac{x^3}{x} + \\frac{4x^2}{x} = x^2 + 4x \\quad (x \\neq 0)$$",
                            "**Step 4 — Differentiate Part (b):**\n"
                            "$$\\frac{dy}{dx} = 2x + 4$$\n\n"
                            "**Answer:** (a) $\\frac{dy}{dx} = 4x - 5$; (b) $\\frac{dy}{dx} = 2x + 4$."
                        ]
                    }
                },

                # PAGE 6 — worked_example (Level 3: Difficult / Negative and Fractional Exponents)
                {
                    "page_number": 6,
                    "page_title": "Example 3: Differentiating Negative & Fractional Exponents",
                    "block_type": "worked_example",
                    "component_type": "worked_example",
                    "content": {
                        "problem": (
                            "Differentiate $y = \\frac{2}{x^2} + 4\\sqrt{x} - \\frac{5}{x}$ with respect to $x$."
                        ),
                        "steps": [
                            "**What we need to find:** $\\frac{dy}{dx}$ using index laws.",
                            "**Step 1 — Rewrite all terms using index notation:**\n"
                            "$$y = 2x^{-2} + 4x^{1/2} - 5x^{-1}$$",
                            "**Step 2 — Differentiate $2x^{-2}$:**\n"
                            "$$\\frac{d}{dx}(2x^{-2}) = (-2) \\cdot 2 x^{-2-1} = -4x^{-3} = -\\frac{4}{x^3}$$",
                            "**Step 3 — Differentiate $4x^{1/2}$:**\n"
                            "$$\\frac{d}{dx}(4x^{1/2}) = \\left(\\frac{1}{2}\\right) \\cdot 4 x^{1/2 - 1} = 2x^{-1/2} = \\frac{2}{\\sqrt{x}}$$",
                            "**Step 4 — Differentiate $-5x^{-1}$:**\n"
                            "$$\\frac{d}{dx}(-5x^{-1}) = (-1) \\cdot (-5) x^{-1-1} = 5x^{-2} = \\frac{5}{x^2}$$",
                            "**Step 5 — Combine final result:**\n"
                            "$$\\frac{dy}{dx} = -\\frac{4}{x^3} + \\frac{2}{\\sqrt{x}} + \\frac{5}{x^2}$$\n\n"
                            "**Answer:** $\\frac{dy}{dx} = -\\frac{4}{x^3} + \\frac{2}{\\sqrt{x}} + \\frac{5}{x^2}$."
                        ]
                    }
                },

                # PAGE 7 — worked_example (Level 4: Exam-Style / Solving Unknown Constants)
                {
                    "page_number": 7,
                    "page_title": "Example 4: Solving Constants a and b from Gradient Data",
                    "block_type": "worked_example",
                    "component_type": "worked_example",
                    "content": {
                        "problem": (
                            "The curve $y = a x^3 + b x$ passes through the point $(1, 1)$, "
                            "and the gradient of the curve at this point is $-5$.\n"
                            "Calculate the numerical values of constants $a$ and $b$."
                        ),
                        "steps": [
                            "**What we need to find:** Numerical values of $a$ and $b$.",
                            "**Step 1 — Use point substitution $(1, 1)$:**\n"
                            "Since $(1, 1)$ lies on the curve:\n"
                            "$$1 = a(1)^3 + b(1) \\implies a + b = 1 \\quad \\text{(Equation 1)}$$",
                            "**Step 2 — Differentiate curve to find gradient function:**\n"
                            "$$\\frac{dy}{dx} = 3a x^2 + b$$",
                            "**Step 3 — Substitute $x = 1$ and gradient $m = -5$:**\n"
                            "$$3a(1)^2 + b = -5 \\implies 3a + b = -5 \\quad \\text{(Equation 2)}$$",
                            "**Step 4 — Solve simultaneous system (Eq 2 - Eq 1):**\n"
                            "$$(3a + b) - (a + b) = -5 - 1 \\implies 2a = -6 \\implies a = -3$$",
                            "**Step 5 — Substitute $a = -3$ into Eq 1:**\n"
                            "$$-3 + b = 1 \\implies b = 4$$\n\n"
                            "**Answer:** $a = -3$ and $b = 4$."
                        ]
                    }
                },

                # PAGE 8 — suggested_simulation
                {
                    "page_number": 8,
                    "page_title": "Explore: Power Rule & Polynomial Mechanics Sandbox",
                    "block_type": "suggested_simulation",
                    "component_type": "suggested_simulation",
                    "content": {
                        "purpose": (
                            "An interactive polynomial derivative builder where students enter coefficients and powers. "
                            "The simulator dynamically displays the step-by-step power rule multiplication and exponent reduction, "
                            "rendering both the original curve and its derivative graph side-by-side."
                        )
                    },
                    "asset_info": {
                        "asset_type": "simulation",
                        "archetype": "math_power_rule_polynomial_mechanics",
                        "title": "Interactive Power Rule Polynomial Mechanics Sandbox"
                    }
                },

                # PAGE 9 — common_misconception
                {
                    "page_number": 9,
                    "page_title": "Common Error: Differentiating Constants and Linear Terms",
                    "block_type": "common_misconception",
                    "component_type": "common_misconception",
                    "content": {
                        "text": (
                            "### Constant & Linear Term Errors\n\n"
                            "1. **Treating Constants like Variables:**\n"
                            "   Students often write $\\frac{d}{dx}(7) = 7$. Constants have **zero slope** (horizontal lines), so $\\frac{d}{dx}(C) = 0$.\n"
                            "2. **Forgetting $x^0 = 1$ in Linear Terms:**\n"
                            "   When differentiating $7x$, applying the rule gives $1 \\cdot 7 x^{1-1} = 7x^0 = 7$. Do not leave the $x$ behind as $7x$!\n\n"
                            "> **Memory Tip:** Constant numbers drop to zero; linear terms $kx$ drop their $x$ and leave just coefficient $k$!"
                        )
                    }
                },

                # PAGE 10 — knowledge_check (MCQ)
                {
                    "page_number": 10,
                    "page_title": "Check Your Understanding: Power Rules",
                    "block_type": "knowledge_check",
                    "component_type": "multiple_choice",
                    "content": {
                        "question": "What is the derivative of y = 4x³ - 6x² + 5x - 9?",
                        "options": [
                            "A: 12x² - 12x + 5",
                            "B: 12x² - 12x + 5 - 9",
                            "C: 4x² - 6x + 5",
                            "D: 12x³ - 12x² + 5x"
                        ],
                        "answer": "A",
                        "explanation": (
                            "1. $\\frac{d}{dx}(4x^3) = 12x^2$.\n"
                            "2. $\\frac{d}{dx}(-6x^2) = -12x$.\n"
                            "3. $\\frac{d}{dx}(5x) = 5$.\n"
                            "4. $\\frac{d}{dx}(-9) = 0$.\n"
                            "Result: $12x^2 - 12x + 5$."
                        )
                    }
                },

                # PAGE 11 — summary
                {
                    "page_number": 11,
                    "page_title": "Key Takeaways: Polynomial Power Rules",
                    "block_type": "summary",
                    "component_type": "summary",
                    "content": {
                        "text": (
                            "### Master Summary: Power Rule Rules & Shortcuts\n\n"
                            "| Operation | Algebraic Formula | Example |\n"
                            "|:---|:---|:---|\n"
                            "| **Power Rule** | $\\frac{d}{dx}(a x^n) = n a x^{n-1}$ | $\\frac{d}{dx}(4x^5) = 20x^4$ |\n"
                            "| **Linear Term** | $\\frac{d}{dx}(k x) = k$ | $\\frac{d}{dx}(-8x) = -8$ |\n"
                            "| **Constant** | $\\frac{d}{dx}(C) = 0$ | $\\frac{d}{dx}(15) = 0$ |\n"
                            "| **Index Rewrite** | $\\frac{a}{x^n} = a x^{-n}, \\quad \\sqrt[q]{x^p} = x^{p/q}$ | Prepare terms BEFORE differentiating! |\n\n"
                            "**Golden Rule:** Multiply by power, then subtract 1 from power!"
                        )
                    }
                }
            ]
        },

        # =====================================================================
        # MODULE 8.3: Tangents, Normals & Turning Points
        # =====================================================================
        {
            "unit_order": 3,
            "unit_title": "Module 8.3: Tangents, Normals, and Stationary Turning Points of Curves",
            "lesson_title": "Tangents, Normals, and Stationary Turning Points of Curves",
            "lesson_blocks": [
                # PAGE 1 — learning_goal
                {
                    "page_number": 1,
                    "page_title": "Mastering Tangents, Normals & Turning Points",
                    "block_type": "learning_goal",
                    "component_type": "learning_goal",
                    "content": {
                        "title": "What You Will Master in This Lesson",
                        "goals": [
                            "Find the exact gradient and equation of the tangent line to a curve at a contact point $(x_1, y_1)$.",
                            "Construct the equation of the normal line using the perpendicular gradient $m_n = -\\frac{1}{m_t}$.",
                            "Locate stationary turning points by solving $\\frac{dy}{dx} = 0$.",
                            "Classify turning points as local maxima, local minima, or points of inflection using derivative sign tables."
                        ]
                    }
                },

                # PAGE 2 — concept_explanation
                {
                    "page_number": 2,
                    "page_title": "The Ball on a String & Rollercoaster Analogy",
                    "block_type": "concept_explanation",
                    "component_type": "concept_explanation",
                    "content": {
                        "body": (
                            "### The Ball on a String (Tangent & Normal)\n\n"
                            "- **Tangent:** If you whirl a stone on a string in a circle and cut the string, the stone flies off in a straight line touching the circle at that instant. This trajectory is the **tangent line**.\n"
                            "- **Normal:** The string itself, which points directly to the center and meets the tangent line at a $90^\\circ$ right angle, is the **normal line** ($m_t \\cdot m_n = -1$).\n\n"
                            "### The Rollercoaster Peak (Stationary Turning Points)\n\n"
                            "At the absolute top of a hill (maximum) or the bottom of a dip (minimum) on a rollercoaster, "
                            "your car is level for a split second. The slope is flat: **$\\frac{dy}{dx} = 0$**!"
                        )
                    }
                },

                # PAGE 3 — formula_breakdown
                {
                    "page_number": 3,
                    "page_title": "Master Formulas: Tangents, Normals & Turning Points",
                    "block_type": "formula_breakdown",
                    "component_type": "formula_breakdown",
                    "content": {
                        "formula": (
                            "**Tangent Line Equation:**\n"
                            "$$y - y_1 = m_t (x - x_1) \\quad \\text{where } m_t = \\left. \\frac{dy}{dx} \\right|_{x = x_1}$$\n\n"
                            "**Normal Line Equation:**\n"
                            "$$y - y_1 = m_n (x - x_1) \\quad \\text{where } m_n = -\\frac{1}{m_t} \\quad (m_t \\neq 0)$$\n\n"
                            "**Stationary Turning Point Condition:**\n"
                            "$$\\frac{dy}{dx} = 0 \\implies \\text{Solve for } x \\text{ to locate flat spots}$$"
                        ),
                        "content": (
                            "### Classification of Stationary Points Table\n\n"
                            "| Type of Turning Point | Left Slope ($x < x_0$) | At Point ($x = x_0$) | Right Slope ($x > x_0$) | Visual Shape |\n"
                            "|:---|:---|:---|:---|:---|\n"
                            "| **Local Maximum** | Positive ($/$) | Flat ($0$) | Negative ($\\backslash$) | **Hill Peak** ($\\cap$) |\n"
                            "| **Local Minimum** | Negative ($\\backslash$) | Flat ($0$) | Positive ($/$) | **Valley Trough** ($\\cup$) |\n"
                            "| **Inflection Point** | Positive ($/$) | Flat ($0$) | Positive ($/$) | **Terrace Step** |"
                        )
                    }
                },

                # PAGE 4 — worked_example (Level 1: Easy / Tangent and Normal to y = x³ + 2x + 1)
                {
                    "page_number": 4,
                    "page_title": "Example 1: Equations of Tangent and Normal",
                    "block_type": "worked_example",
                    "component_type": "worked_example",
                    "content": {
                        "problem": (
                            "Find the equations of the tangent and the normal to the curve $y = x^3 + 2x + 1$ at the point $(1, 4)$."
                        ),
                        "steps": [
                            "**What we need to find:** Equations of tangent line and perpendicular normal line at $(1, 4)$.",
                            "**Step 1 — Differentiate curve to find gradient function:**\n"
                            "$$\\frac{dy}{dx} = 3x^2 + 2$$",
                            "**Step 2 — Evaluate tangent gradient $m_t$ at $x = 1$:**\n"
                            "$$m_t = 3(1)^2 + 2 = 5$$",
                            "**Step 3 — Construct tangent line equation:**\n"
                            "$$y - 4 = 5(x - 1) \\implies y - 4 = 5x - 5 \\implies y = 5x - 1$$",
                            "**Step 4 — Calculate normal gradient $m_n$:**\n"
                            "$$m_n = -\\frac{1}{m_t} = -\\frac{1}{5}$$",
                            "**Step 5 — Construct normal line equation:**\n"
                            "$$5(y - 4) = -1(x - 1) \\implies 5y - 20 = -x + 1 \\implies y = -\\frac{1}{5}x + \\frac{21}{5} \\quad \\text{(or } x + 5y = 21\\text{)}$$\n\n"
                            "**Answer:** Tangent equation is $y = 5x - 1$; Normal equation is $y = -\\frac{1}{5}x + \\frac{21}{5}$."
                        ]
                    }
                },

                # PAGE 5 — worked_example (Level 2: Moderate / Stationary Points of y = x³ - 3x + 2)
                {
                    "page_number": 5,
                    "page_title": "Example 2: Locating and Classifying Stationary Points",
                    "block_type": "worked_example",
                    "component_type": "worked_example",
                    "content": {
                        "problem": (
                            "Identify the stationary points on the curve $y = x^3 - 3x + 2$. "
                            "For each point, determine its nature (maximum, minimum, or point of inflection)."
                        ),
                        "steps": [
                            "**What we need to find:** Stationary coordinates and their classification.",
                            "**Step 1 — Differentiate curve equation:**\n"
                            "$$\\frac{dy}{dx} = 3x^2 - 3$$",
                            "**Step 2 — Set derivative to zero and solve for $x$:**\n"
                            "$$3x^2 - 3 = 0 \\implies 3(x^2 - 1) = 0 \\implies (x-1)(x+1) = 0 \\implies x = 1 \\quad \\text{or} \\quad x = -1$$",
                            "**Step 3 — Find corresponding $y$-coordinates on original curve:**\n"
                            "- At $x = -1$: $y = (-1)^3 - 3(-1) + 2 = -1 + 3 + 2 = 4 \\implies (-1, 4)$.\n"
                            "- At $x = 1$: $y = (1)^3 - 3(1) + 2 = 1 - 3 + 2 = 0 \\implies (1, 0)$.",
                            "**Step 4 — Classify point $(-1, 4)$ via sign table:**\n"
                            "- Left ($x = -2$): $\\frac{dy}{dx} = 3(4) - 3 = +9$ (Positive $/$).\n"
                            "- Right ($x = 0$): $\\frac{dy}{dx} = 3(0) - 3 = -3$ (Negative $\\backslash$).\n"
                            "- Slope goes $/ \\to 0 \\to \\backslash \\implies (-1, 4)$ is a **Local Maximum**.",
                            "**Step 5 — Classify point $(1, 0)$ via sign table:**\n"
                            "- Left ($x = 0$): $\\frac{dy}{dx} = -3$ (Negative $\\backslash$).\n"
                            "- Right ($x = 2$): $\\frac{dy}{dx} = +9$ (Positive $/$).\n"
                            "- Slope goes $\\backslash \\to 0 \\to / \\implies (1, 0)$ is a **Local Minimum**.\n\n"
                            "**Answer:** $(-1, 4)$ is a Local Maximum; $(1, 0)$ is a Local Minimum."
                        ]
                    }
                },

                # PAGE 6 — worked_example (Level 3: Difficult / Normal Axis Crossing Point)
                {
                    "page_number": 6,
                    "page_title": "Example 3: Normal Line Axis Intersections",
                    "block_type": "worked_example",
                    "component_type": "worked_example",
                    "content": {
                        "problem": (
                            "The curve $y = \\frac{1}{3}x^3 - x^2 + 2$ has a normal line drawn at point $(3, y_0)$.\n"
                            "Find the coordinate where this normal line crosses the $x$-axis ($y = 0$)."
                        ),
                        "steps": [
                            "**What we need to find:** $y_0$, normal equation, and $x$-intercept.",
                            "**Step 1 — Evaluate $y_0$ at $x = 3$:**\n"
                            "$$y_0 = \\frac{1}{3}(3)^3 - (3)^2 + 2 = 9 - 9 + 2 = 2 \\implies \\text{Contact point } (3, 2)$$",
                            "**Step 2 — Differentiate curve:**\n"
                            "$$\\frac{dy}{dx} = x^2 - 2x$$",
                            "**Step 3 — Evaluate tangent slope at $x = 3$:**\n"
                            "$$m_t = (3)^2 - 2(3) = 9 - 6 = 3$$",
                            "**Step 4 — Calculate normal slope $m_n$ and equation:**\n"
                            "$$m_n = -\\frac{1}{3} \\implies y - 2 = -\\frac{1}{3}(x - 3) \\implies 3y - 6 = -x + 3 \\implies x + 3y = 9$$",
                            "**Step 5 — Find $x$-intercept ($y = 0$):**\n"
                            "$$x + 3(0) = 9 \\implies x = 9 \\implies (9, 0)$$\n\n"
                            "**Answer:** Normal line crosses the $x$-axis at $(9, 0)$."
                        ]
                    }
                },

                # PAGE 7 — worked_example (Level 4: Exam-Style / Curve Sketching with Stationary Points)
                {
                    "page_number": 7,
                    "page_title": "Example 4: Complete Cubic Curve Sketching",
                    "block_type": "worked_example",
                    "component_type": "worked_example",
                    "content": {
                        "problem": (
                            "Sketch the curve $y = x^3 - 3x^2$ by identifying its intercepts, stationary points, and turning behavior."
                        ),
                        "steps": [
                            "**What we need to find:** Intercepts, stationary points, and sketch.",
                            "**Step 1 — Find $y$-intercept ($x = 0$):**\n"
                            "$$y = 0^3 - 3(0)^2 = 0 \\implies (0, 0)$$",
                            "**Step 2 — Find $x$-intercepts ($y = 0$):**\n"
                            "$$x^3 - 3x^2 = 0 \\implies x^2(x - 3) = 0 \\implies x = 0 \\quad \\text{or} \\quad x = 3$$",
                            "**Step 3 — Find stationary points ($\\frac{dy}{dx} = 0$):**\n"
                            "$$\\frac{dy}{dx} = 3x^2 - 6x = 0 \\implies 3x(x - 2) = 0 \\implies x = 0 \\quad \\text{or} \\quad x = 2$$",
                            "**Step 4 — Evaluate $y$-values for stationary points:**\n"
                            "- At $x = 0$: $y = 0 \\implies (0, 0)$ [Local Maximum].\n"
                            "- At $x = 2$: $y = 2^3 - 3(2)^2 = 8 - 12 = -4 \\implies (2, -4)$ [Local Minimum].",
                            "**Step 5 — Sketch description:**\n"
                            "Curve rises from negative infinity, touches $x$-axis at $(0, 0)$ (maximum), dips down to valley $(2, -4)$ (minimum), and rises up through $(3, 0)$ to positive infinity.\n\n"
                            "**Answer:** Curve with local maximum at $(0, 0)$, local minimum at $(2, -4)$, and $x$-intercept at $(3, 0)$."
                        ]
                    }
                },

                # PAGE 8 — suggested_simulation
                {
                    "page_number": 8,
                    "page_title": "Explore: Tangents, Normals & Turning Points Sandbox",
                    "block_type": "suggested_simulation",
                    "component_type": "suggested_simulation",
                    "content": {
                        "purpose": (
                            "An interactive graphic explorer showing a cubic curve with live tangent (green) and normal (purple) vectors. "
                            "Students can drag the contact cursor $P$ across the curve and watch the tangent slope turn horizontal (0) at peaks and valleys, "
                            "while the lower split-screen plots the matching quadratic derivative graph in sync."
                        )
                    },
                    "asset_info": {
                        "asset_type": "simulation",
                        "archetype": "math_tangent_normal_turning_point_explorer",
                        "title": "Interactive Tangents, Normals & Turning Points Sandbox"
                    }
                },

                # PAGE 9 — common_misconception
                {
                    "page_number": 9,
                    "page_title": "Common Error: Derivative Substitution Inversion",
                    "block_type": "common_misconception",
                    "component_type": "common_misconception",
                    "content": {
                        "text": (
                            "### Substitution Inversion Errors\n\n"
                            "1. **Substituting $x$ into $\\frac{dy}{dx}$ to find $y$:**\n"
                            "   When finding a stationary point's coordinates, students solve $\\frac{dy}{dx} = 0 \\implies x = 1$, then plug $x = 1$ back into $\\frac{dy}{dx}$, getting $y = 0$ every time!\n"
                            "   **Correction:** Plug $x = 1$ into the ORIGINAL curve equation $y(x)$ to get the true coordinate height!\n"
                            "2. **Leaving variables in tangent equations:**\n"
                            "   Writing $y - y_1 = (3x^2 + 2)(x - x_1)$ instead of calculating the numerical slope $m_t = 5$.\n\n"
                            "> **Memory Tip:** $\\frac{dy}{dx}$ gives slope numbers; the original formula $y(x)$ gives elevation coordinates!"
                        )
                    }
                },

                # PAGE 10 — knowledge_check (MCQ)
                {
                    "page_number": 10,
                    "page_title": "Check Your Understanding: Turning Points",
                    "block_type": "knowledge_check",
                    "component_type": "multiple_choice",
                    "content": {
                        "question": "What is the equation of the tangent line to y = x² - 4x + 3 at the point (3, 0)?",
                        "options": [
                            "A: y = 2x - 6",
                            "B: y = 2x + 6",
                            "C: y = -0.5x + 1.5",
                            "D: y = 3x - 9"
                        ],
                        "answer": "A",
                        "explanation": (
                            "1. Derivative: $\\frac{dy}{dx} = 2x - 4$.\n"
                            "2. At $x = 3$, $m_t = 2(3) - 4 = 2$.\n"
                            "3. Tangent line: $y - 0 = 2(x - 3) \\implies y = 2x - 6$."
                        )
                    }
                },

                # PAGE 11 — summary
                {
                    "page_number": 11,
                    "page_title": "Key Takeaways: Tangents, Normals & Flat Spots",
                    "block_type": "summary",
                    "component_type": "summary",
                    "content": {
                        "text": (
                            "### Master Summary: Tangent, Normal & Turning Point Rules\n\n"
                            "| Concept | Condition / Equation | Action |\n"
                            "|:---|:---|:---|\n"
                            "| **Tangent Line** | $y - y_1 = m_t (x - x_1)$ | $m_t = \\frac{dy}{dx}$ evaluated at contact point. |\n"
                            "| **Normal Line** | $y - y_1 = m_n (x - x_1)$ | $m_n = -\\frac{1}{m_t}$ (perpendicular slope). |\n"
                            "| **Stationary Points** | $\\frac{dy}{dx} = 0$ | Solve for $x$, substitute into $y(x)$ for height. |\n"
                            "| **Maximum** | Slope goes $+ \\to 0 \\to -$ | Peak of hill ($\\cap$). |\n"
                            "| **Minimum** | Slope goes $- \\to 0 \\to +$ | Trough of valley ($\\cup$). |\n\n"
                            "**Checklist:** Always double check normal slope signs ($m_n = -1/m_t$)!"
                        )
                    }
                }
            ]
        },

        # =====================================================================
        # MODULE 8.4: Kinematics Applications & Optimization
        # =====================================================================
        {
            "unit_order": 4,
            "unit_title": "Module 8.4: Kinematics Applications and Real-World Optimization",
            "lesson_title": "Kinematics Applications and Real-World Optimization",
            "lesson_blocks": [
                # PAGE 1 — learning_goal
                {
                    "page_number": 1,
                    "page_title": "Mastering Calculus in Motion & Optimization",
                    "block_type": "learning_goal",
                    "component_type": "learning_goal",
                    "content": {
                        "title": "What You Will Master in This Lesson",
                        "goals": [
                            "Relate displacement ($S$), velocity ($v$), and acceleration ($a$) via time derivatives ($v = \\frac{dS}{dt}, a = \\frac{dv}{dt}$).",
                            "Calculate instantaneous velocity, time at rest ($v = 0$), and maximum displacement.",
                            "Formulate single-variable objective functions for real-world geometric optimization problems.",
                            "Minimize production material (surface area) and maximize enclosed capacity (volume/area)."
                        ]
                    }
                },

                # PAGE 2 — concept_explanation
                {
                    "page_number": 2,
                    "page_title": "Kinematics & Soda Can Economics: Calculus in Action",
                    "block_type": "concept_explanation",
                    "component_type": "concept_explanation",
                    "content": {
                        "body": (
                            "### Kinematics: Rates of Motion\n\n"
                            "- **Displacement $S(t)$:** Where an object is located at time $t$.\n"
                            "- **Velocity $v(t) = \\frac{dS}{dt}$:** How fast position is changing (speedometer reading with direction).\n"
                            "- **Acceleration $a(t) = \\frac{dv}{dt} = \\frac{d^2S}{dt^2}$:** How fast velocity is changing.\n\n"
                            "### Soda Can Economics (Optimization)\n\n"
                            "A beverage manufacturer wants to make a $250\\pi\\text{ ml}$ soda tin using as little aluminum sheet metal as possible.\n"
                            "- If the can is super tall and thin $\\implies$ top/bottom are small, but side wall is huge!\n"
                            "- If the can is a flat disk $\\implies$ side wall is small, but top/bottom lids are huge!\n"
                            "By setting $\\frac{dA}{dr} = 0$, calculus finds the exact optimal dimensions ($r = 5\\text{ cm}, h = 10\\text{ cm}$) to minimize cost!"
                        )
                    }
                },

                # PAGE 3 — formula_breakdown
                {
                    "page_number": 3,
                    "page_title": "Master Formulas: Kinematics & Optimization",
                    "block_type": "formula_breakdown",
                    "component_type": "formula_breakdown",
                    "content": {
                        "formula": (
                            "**Kinematics Derivatives:**\n"
                            "$$v = \\frac{dS}{dt}, \\qquad a = \\frac{dv}{dt} = \\frac{d^2S}{dt^2}$$\n\n"
                            "**Particle at Rest Condition:**\n"
                            "$$v = 0 \\implies \\text{Solve } \\frac{dS}{dt} = 0 \\text{ for time } t$$\n\n"
                            "**Cylinder Packaging Formulas:**\n"
                            "$$V = \\pi r^2 h, \\qquad A = 2\\pi r^2 + 2\\pi r h \\implies A(r) = 2\\pi r^2 + \\frac{2V}{r} \\implies \\frac{dA}{dr} = 0$$"
                        ),
                        "content": (
                            "### Optimization Step-by-Step Sequence\n\n"
                            "| Step | Action | Practical Example |\n"
                            "|:---|:---|:---|\n"
                            "| **1. Identify Objective** | Write formula for target quantity | Surface Area $A = 2\\pi r^2 + 2\\pi rh$ |\n"
                            "| **2. Express Constraints** | Use fixed condition to eliminate 1 variable | Fixed Volume $V = 250\\pi \\implies h = \\frac{250}{r^2}$ |\n"
                            "| **3. Substitute & Reduce** | Write single-variable target function | $A(r) = 2\\pi r^2 + 500\\pi r^{-1}$ |\n"
                            "| **4. Differentiate** | Find derivative function | $\\frac{dA}{dr} = 4\\pi r - 500\\pi r^{-2}$ |\n"
                            "| **5. Solve Zero Rate** | Set $\\frac{dA}{dr} = 0$ and solve for variable | $4\\pi r^3 = 500\\pi \\implies r = 5\\text{ cm}$ |\n"
                            "| **6. Final Check** | Calculate remaining dimensions | $h = \\frac{250}{25} = 10\\text{ cm}$ |"
                        )
                    }
                },

                # PAGE 4 — worked_example (Level 1: Easy / Particle Velocity and Rest Time)
                {
                    "page_number": 4,
                    "page_title": "Example 1: Kinematic Velocity & Particle Rest Instant",
                    "block_type": "worked_example",
                    "component_type": "worked_example",
                    "content": {
                        "problem": (
                            "A particle's displacement is modeled by $S = 2t^3 + 4t^2 - 8t + 3$ (in meters, $t \\ge 0$ in seconds).\n"
                            "Find:\n"
                            "(a) The velocity at $t = 2\\text{ s}$.\n"
                            "(b) The instant when the particle is momentarily at rest."
                        ),
                        "steps": [
                            "**What we need to find:** $v(2)$ and time $t$ when $v(t) = 0$.",
                            "**Step 1 — Differentiate $S(t)$ to find velocity $v(t)$:**\n"
                            "$$v = \\frac{dS}{dt} = 6t^2 + 8t - 8$$",
                            "**Step 2 — Evaluate velocity at $t = 2\\text{ s}$:**\n"
                            "$$v(2) = 6(2)^2 + 8(2) - 8 = 6(4) + 16 - 8 = 24 + 8 = 32\\text{ m/s}$$",
                            "**Step 3 — Set velocity to zero to find rest time:**\n"
                            "$$6t^2 + 8t - 8 = 0 \\implies 2(3t^2 + 4t - 4) = 0$$",
                            "**Step 4 — Factorize quadratic equation:**\n"
                            "$$2(3t - 2)(t + 2) = 0 \\implies t = \\frac{2}{3}\\text{ s} \\quad \\text{or} \\quad t = -2\\text{ s}$$",
                            "**Step 5 — Reject negative time ($t \\ge 0$):**\n"
                            "$$t = \\frac{2}{3}\\text{ s}$$\n\n"
                            "**Answer:** (a) $32\\text{ m/s}$; (b) At rest at $t = \\frac{2}{3}\\text{ s}$."
                        ]
                    }
                },

                # PAGE 5 — worked_example (Level 2: Moderate / Acceleration and Maximum Velocity)
                {
                    "page_number": 5,
                    "page_title": "Example 2: Kinematic Acceleration & Maximum Speed",
                    "block_type": "worked_example",
                    "component_type": "worked_example",
                    "content": {
                        "problem": (
                            "The velocity of a car is modeled by $v = 3 + 10t - t^2$ (for $t \\ge 0$).\n"
                            "Calculate:\n"
                            "(a) The acceleration of the car at $t = 3\\text{ s}$.\n"
                            "(b) The maximum velocity reached by the car."
                        ),
                        "steps": [
                            "**What we need to find:** $a(3)$ and maximum velocity $v_{\\max}$.",
                            "**Step 1 — Differentiate velocity $v(t)$ to find acceleration $a(t)$:**\n"
                            "$$a = \\frac{dv}{dt} = 10 - 2t$$",
                            "**Step 2 — Evaluate acceleration at $t = 3\\text{ s}$:**\n"
                            "$$a(3) = 10 - 2(3) = 10 - 6 = 4\\text{ m/s}^2$$",
                            "**Step 3 — Find time for maximum velocity ($a = 0$):**\n"
                            "$$10 - 2t = 0 \\implies 2t = 10 \\implies t = 5\\text{ s}$$",
                            "**Step 4 — Calculate maximum velocity at $t = 5\\text{ s}$:**\n"
                            "$$v_{\\max} = 3 + 10(5) - (5)^2 = 3 + 50 - 25 = 28\\text{ m/s}$$\n\n"
                            "**Answer:** (a) $4\\text{ m/s}^2$; (b) Maximum velocity is $28\\text{ m/s}$."
                        ]
                    }
                },

                # PAGE 6 — worked_example (Level 3: Difficult / Enclosed Area Optimization)
                {
                    "page_number": 6,
                    "page_title": "Example 3: Rectangular Mesh Area Optimization",
                    "block_type": "worked_example",
                    "component_type": "worked_example",
                    "content": {
                        "problem": (
                            "A farmer has $120\\text{ meters}$ of wire mesh to build a rectangular chicken run against an existing straight brick wall "
                            "(so no fencing is needed along the wall).\n"
                            "Find the dimensions of the run that maximize the enclosed area, and calculate this maximum area."
                        ),
                        "steps": [
                            "**What we need to find:** Dimensions $x, y$ and maximum area $A_{\\max}$.",
                            "**Step 1 — Define variables and perimeter constraint:**\n"
                            "Let $x$ be the width perpendicular to the wall (2 sides), and $y$ be the length parallel to the wall (1 side).\n"
                            "$$\\text{Perimeter } 2x + y = 120 \\implies y = 120 - 2x$$",
                            "**Step 2 — Form single-variable area function $A(x)$:**\n"
                            "$$A = x \\cdot y = x(120 - 2x) = 120x - 2x^2$$",
                            "**Step 3 — Differentiate area function:**\n"
                            "$$\\frac{dA}{dx} = 120 - 4x$$",
                            "**Step 4 — Set derivative to zero for maximum area:**\n"
                            "$$120 - 4x = 0 \\implies 4x = 120 \\implies x = 30\\text{ meters}$$",
                            "**Step 5 — Calculate length $y$ and maximum area:**\n"
                            "$$y = 120 - 2(30) = 60\\text{ meters}$$\n"
                            "$$A_{\\max} = 30 \\times 60 = 1800\\text{ m}^2$$\n\n"
                            "**Answer:** Dimensions $30\\text{ m} \\times 60\\text{ m}$, maximum area is $1800\\text{ m}^2$."
                        ]
                    }
                },

                # PAGE 7 — worked_example (Level 4: Exam-Style / Cylindrical Packaging Optimization)
                {
                    "page_number": 7,
                    "page_title": "Example 4: Minimizing Surface Area of a Cylindrical Can",
                    "block_type": "worked_example",
                    "component_type": "worked_example",
                    "content": {
                        "problem": (
                            "A closed cylindrical tin must hold a volume of $250\\pi\\text{ cm}^3$.\n"
                            "Show that the radius $r$ which minimizes total surface area is $r = 5\\text{ cm}$, "
                            "and calculate the minimum area of sheet metal required."
                        ),
                        "steps": [
                            "**What we need to prove and calculate:** $r = 5\\text{ cm}$ and minimum surface area $A_{\\min}$.",
                            "**Step 1 — Express volume constraint:**\n"
                            "$$V = \\pi r^2 h = 250\\pi \\implies h = \\frac{250}{r^2}$$",
                            "**Step 2 — Write surface area formula and substitute $h$:**\n"
                            "$$A = 2\\pi r^2 + 2\\pi r h = 2\\pi r^2 + 2\\pi r \\left(\\frac{250}{r^2}\\right) = 2\\pi r^2 + \\frac{500\\pi}{r} = 2\\pi r^2 + 500\\pi r^{-1}$$",
                            "**Step 3 — Differentiate surface area with respect to $r$:**\n"
                            "$$\\frac{dA}{dr} = 4\\pi r - 500\\pi r^{-2} = 4\\pi r - \\frac{500\\pi}{r^2}$$",
                            "**Step 4 — Set derivative to zero to optimize:**\n"
                            "$$4\\pi r - \\frac{500\\pi}{r^2} = 0 \\implies 4\\pi r^3 = 500\\pi \\implies r^3 = 125 \\implies r = 5\\text{ cm}$$\n"
                            "*(Proved!)*",
                            "**Step 5 — Calculate minimum area:**\n"
                            "$$A_{\\min} = 2\\pi(5)^2 + \\frac{500\\pi}{5} = 50\\pi + 100\\pi = 150\\pi \\approx 471.24\\text{ cm}^2$$\n\n"
                            "**Answer:** Optimal radius $r = 5\\text{ cm}$ ($h = 10\\text{ cm}$), minimum surface area is $150\\pi \\approx 471.24\\text{ cm}^2$."
                        ]
                    }
                },

                # PAGE 8 — suggested_simulation
                {
                    "page_number": 8,
                    "page_title": "Explore: Kinematics & Packaging Optimization Sandbox",
                    "block_type": "suggested_simulation",
                    "component_type": "suggested_simulation",
                    "content": {
                        "purpose": (
                            "An interactive 3D packaging optimizer and kinematics simulator. "
                            "Students can drag a radius slider $r$ from $1\\text{ cm}$ to $12\\text{ cm}$ while holding volume at $250\\pi\\text{ ml}$. "
                            "The simulator dynamically recalculates height $h$ and displays a surface area curve graph, highlighting the exact cost-saving minimum at $r = 5\\text{ cm}$."
                        )
                    },
                    "asset_info": {
                        "asset_type": "simulation",
                        "archetype": "math_kinematics_optimization_sandbox",
                        "title": "Interactive Kinematics & Optimization Sandbox"
                    }
                },

                # PAGE 9 — common_misconception
                {
                    "page_number": 9,
                    "page_title": "Common Error: Confusing Velocity Zero with Acceleration Zero",
                    "block_type": "common_misconception",
                    "component_type": "common_misconception",
                    "content": {
                        "text": (
                            "### Physical Kinematic Misconceptions\n\n"
                            "1. **Assuming $v = 0$ means $a = 0$:**\n"
                            "   When a ball thrown straight up reaches its peak height, its velocity is zero ($v = 0$), but its acceleration is NOT zero—gravity is still pulling it down at $a = -9.8\\text{ m/s}^2$!\n"
                            "2. **Confusing Maximum Displacement with Maximum Velocity:**\n"
                            "   - Maximum Displacement occurs when velocity is zero ($v = \\frac{dS}{dt} = 0$).\n"
                            "   - Maximum Velocity occurs when acceleration is zero ($a = \\frac{dv}{dt} = 0$).\n\n"
                            "> **Memory Tip:** Velocity is the rate of position; acceleration is the rate of velocity!"
                        )
                    }
                },

                # PAGE 10 — knowledge_check (MCQ)
                {
                    "page_number": 10,
                    "page_title": "Check Your Understanding: Kinematics",
                    "block_type": "knowledge_check",
                    "component_type": "multiple_choice",
                    "content": {
                        "question": "A particle moves with displacement S = t³ - 6t² + 9t + 2. At what time t is the particle momentarily at rest?",
                        "options": [
                            "A: t = 1 s and t = 3 s",
                            "B: t = 2 s only",
                            "C: t = 6 s only",
                            "D: t = 0 s and t = 4 s"
                        ],
                        "answer": "A",
                        "explanation": (
                            "1. Derivative $v = \\frac{dS}{dt} = 3t^2 - 12t + 9$.\n"
                            "2. Set $v = 0 \\implies 3(t^2 - 4t + 3) = 0 \\implies 3(t - 1)(t - 3) = 0$.\n"
                            "3. Rest times: $t = 1\\text{ s}$ and $t = 3\\text{ s}$."
                        )
                    }
                },

                # PAGE 11 — summary
                {
                    "page_number": 11,
                    "page_title": "Key Takeaways: Kinematics & Optimization",
                    "block_type": "summary",
                    "component_type": "summary",
                    "content": {
                        "text": (
                            "### Master Summary: Kinematics & Optimization Checklist\n\n"
                            "| Physics / Economics Scenario | Rate Condition | Key Action |\n"
                            "|:---|:---|:---|\n"
                            "| **Instantaneous Velocity** | $v = \\frac{dS}{dt}$ | Differentiate displacement equation $S(t)$. |\n"
                            "| **Instantaneous Acceleration** | $a = \\frac{dv}{dt} = \\frac{d^2S}{dt^2}$ | Differentiate velocity equation $v(t)$. |\n"
                            "| **Particle at Rest** | $v = 0$ | Set $\\frac{dS}{dt} = 0$ and solve for time $t$. |\n"
                            "| **Max / Min Optimization** | $\\frac{d(\\text{Target})}{d(\\text{Variable})} = 0$ | Express target in 1 variable and solve zero derivative. |\n\n"
                            "**Differentiation Mastery Complete!**"
                        )
                    }
                }
            ]
        }
    ]


def ingest_topic8_differentiation():
    """Main ingestion runner for Topic 8: Differentiation."""
    print("=" * 80)
    print("VLearn Form 4 Mathematics — Topic 8: Differentiation")
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

    # 2. Get or create Topic 8
    topic_name = "Topic 8: Differentiation"
    topic, topic_created = Topic.objects.get_or_create(
        subject=subject,
        order=8,
        defaults={"name": topic_name}
    )
    if not topic_created and topic.name != topic_name:
        topic.name = topic_name
        topic.save()
    print(f"Found Topic: {topic.name} (ID: {topic.id})")

    modules_data = get_topic8_data()
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
    ingest_topic8_differentiation()
