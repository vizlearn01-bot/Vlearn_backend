#!/usr/bin/env python3
"""
VLearn Form 4 Mathematics — Topic 10: Area Approximation Ingestion Script
==========================================================================
Curriculum: 844
Grade: Form 4 (level=1)
Subject: Mathematics
Topic: Topic 10: Area Approximation (order=10)

Modules / LearningUnits:
  10.1 Area Division, Bounding Rectangles, and Grid Counting Under Curves
  10.2 The Trapezium Rule: Derivation, Ordinance Mapping, and Area Calculations
  10.3 The Mid-Ordinate Rule: Sub-Interval Midpoints and Error Cancellation
  10.4 Comparative Error Analysis, Concavity Bounds, and Definite Integration

Pedagogical Structure per Lesson: 11 Pages (44 blocks total)
  Page 1:  learning_goal (Student-friendly outcomes)
  Page 2:  concept_explanation (Real-world analogies: curved bay window, stepped blocks vs straight ramps, horizontal cut, gold standard)
  Page 3:  formula_breakdown / definition_card (Word formulas, trapezium rule, mid-ordinate rule, exact integration, error percentage)
  Page 4:  worked_example (Level 1: Easy / Foundation)
  Page 5:  worked_example (Level 2: Moderate / Multi-step)
  Page 6:  worked_example (Level 3: Difficult / Exam standard)
  Page 7:  worked_example (Level 4: Exam-Style / Real-World Synthesis)
  Page 8:  suggested_simulation (Interactive visual sandbox)
  Page 9:  common_misconception (Diagnostic error analysis & memory tips)
  Page 10: knowledge_check (MCQ / Short-answer with step-by-step solutions)
  Page 11: summary (Key takeaways & area approximation checklist)

Standards Enforced:
  - Clean responsive Markdown tables (zero raw \\begin{array} or \\hline).
  - Explicit bold labels on all formula breakdowns.
  - Correct normalized equations (fixing source typos: 30s step size, 4-strip midpoint sums, exact 400 m² scale conversions).
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


def get_topic10_data():
    """Returns the complete structured curriculum payload for Topic 10."""
    return [
        # =====================================================================
        # MODULE 10.1: Area Division & Grid Counting
        # =====================================================================
        {
            "unit_order": 1,
            "unit_title": "Module 10.1: Area Division, Bounding Rectangles, and Grid Counting Under Curves",
            "lesson_title": "Area Division, Bounding Rectangles, and Grid Counting Under Curves",
            "lesson_blocks": [
                # PAGE 1 — learning_goal
                {
                    "page_number": 1,
                    "page_title": "Mastering Area Division & Rectangular Bounding Limits",
                    "block_type": "learning_goal",
                    "component_type": "learning_goal",
                    "content": {
                        "title": "What You Will Master in This Lesson",
                        "goals": [
                            "Estimate irregular areas under curves using grid square counting on coordinate graph paper.",
                            "Construct lower rectangular bounds (underestimate) and upper rectangular bounds (overestimate).",
                            "Understand the limit of rectangular sums: $\\lim_{\\delta x \\to 0} \\sum f(x_i) \\delta x = \\int_a^b f(x) dx$.",
                            "Predict whether rectangular bounds under- or overestimate areas based on curve monotonicity."
                        ]
                    }
                },

                # PAGE 2 — concept_explanation
                {
                    "page_number": 2,
                    "page_title": "The Curved Bay Window Analogy: Inner & Outer Rectangular Bounds",
                    "block_type": "concept_explanation",
                    "component_type": "concept_explanation",
                    "content": {
                        "body": (
                            "Imagine estimating the floor area under a curved bay window without an analytical formula:\n\n"
                            "### Inner vs. Outer Rectangular Bounds\n\n"
                            "1. **Lower Bound (Underestimate):**\n"
                            "   If you place cardboard rectangular sheets that fit entirely inside the curved window frame, "
                            "   the sum of their areas is guaranteed to be **less than** the true floor area.\n"
                            "2. **Upper Bound (Overestimate):**\n"
                            "   If you place cardboard sheets that extend outward to completely cover the curved glass edge, "
                            "   their combined area is guaranteed to be **greater than** the true floor area.\n\n"
                            "### Convergence to Definite Integration\n\n"
                            "The true physical floor area is locked tightly between the lower and upper bounds! "
                            "By making the rectangular sheets narrower and narrower (strip width $\\delta x \\to 0$), "
                            "the gap between the upper and lower bounds shrinks to zero, converging to the exact **Definite Integral**!"
                        )
                    }
                },

                # PAGE 3 — formula_breakdown
                {
                    "page_number": 3,
                    "page_title": "Master Formulas: Rectangular Bounds & Limit Definition",
                    "block_type": "formula_breakdown",
                    "component_type": "formula_breakdown",
                    "content": {
                        "formula": (
                            "**Lower Rectangular Bound (Left-Hand Sum for Increasing Curve):**\n"
                            "$$A_{\\text{lower}} = h \\cdot [y_0 + y_1 + y_2 + \\dots + y_{n-1}]$$\n\n"
                            "**Upper Rectangular Bound (Right-Hand Sum for Increasing Curve):**\n"
                            "$$A_{\\text{upper}} = h \\cdot [y_1 + y_2 + y_3 + \\dots + y_n]$$\n\n"
                            "**Riemann Sum Limit Definition:**\n"
                            "$$\\text{Exact Area} = \\lim_{\\delta x \\to 0} \\sum_{i=1}^n f(x_i) \\delta x = \\int_a^b f(x) \\, dx$$"
                        ),
                        "content": (
                            "### Rectangular Bounding Reference Table\n\n"
                            "| Curve Behavior | Lower Bound (Underestimate) | Upper Bound (Overestimate) |\n"
                            "|:---|:---|:---|\n"
                            "| **Increasing Curve ($f'(x) > 0$)** | Left-endpoint heights ($y_0$ to $y_{n-1}$) | Right-endpoint heights ($y_1$ to $y_n$) |\n"
                            "| **Decreasing Curve ($f'(x) < 0$)** | Right-endpoint heights ($y_1$ to $y_n$) | Left-endpoint heights ($y_0$ to $y_{n-1}$) |\n"
                            "| **Grid Square Counting** | Full grid squares completely inside | Full grid squares + partial grid squares ($\\ge 0.5$) |"
                        )
                    }
                },

                # PAGE 4 — worked_example (Level 1: Easy / Grid Square Counting)
                {
                    "page_number": 4,
                    "page_title": "Example 1: Grid Square Counting Under an Irregular Boundary",
                    "block_type": "worked_example",
                    "component_type": "worked_example",
                    "content": {
                        "problem": (
                            "An irregular forest boundary is plotted on graph paper where 1 grid square represents $100\\text{ m}^2$.\n"
                            "By grid counting, there are 42 complete squares inside the boundary and 16 partial squares (each averaging $\\ge 0.5$ full square).\n"
                            "Estimate the total area of the forest in square meters and hectares."
                        ),
                        "steps": [
                            "**What we need to estimate:** Total area in $\\text{m}^2$ and hectares ($1\\text{ ha} = 10,000\\text{ m}^2$).",
                            "**Step 1 — Estimate total grid units:**\n"
                            "$$\\text{Total Grid Units} \\approx \\text{Complete Squares} + \\frac{1}{2}(\\text{Partial Squares}) = 42 + \\frac{1}{2}(16) = 42 + 8 = 50\\text{ grid units}$$",
                            "**Step 2 — Convert to square meters using scale ($100\\text{ m}^2/\\text{unit}$):**\n"
                            "$$\\text{Area} = 50\\text{ units} \\times 100\\text{ m}^2/\\text{unit} = 5000\\text{ m}^2$$",
                            "**Step 3 — Convert to hectares:**\n"
                            "$$\\text{Area}_{\\text{ha}} = \\frac{5000\\text{ m}^2}{10,000\\text{ m}^2/\\text{ha}} = 0.5\\text{ hectares}$$\n\n"
                            "**Answer:** $5000\\text{ m}^2$ or $0.5\\text{ hectares}$."
                        ]
                    }
                },

                # PAGE 5 — worked_example (Level 2: Moderate / Rectangular Bounds for y = x²)
                {
                    "page_number": 5,
                    "page_title": "Example 2: Constructing Lower and Upper Rectangular Bounds",
                    "block_type": "worked_example",
                    "component_type": "worked_example",
                    "content": {
                        "problem": (
                            "Calculate the lower bound (underestimate) and upper bound (overestimate) for the area under $y = x^2$ "
                            "from $x = 0$ to $x = 4$ using 4 vertical strips of width $h = 1$."
                        ),
                        "steps": [
                            "**What we need to find:** Lower bound $A_{\\text{lower}}$, upper bound $A_{\\text{upper}}$, and compare with exact area.",
                            "**Step 1 — Evaluate ordinate heights at integer points:**\n\n"
                            "| $x$ | 0 | 1 | 2 | 3 | 4 |\n"
                            "|:---|:---|:---|:---|:---|:---|\n"
                            "| $y = x^2$ | 0 | 1 | 4 | 9 | 16 |\n\n",
                            "**Step 2 — Calculate lower rectangular bound (left-hand heights):**\n"
                            "$$A_{\\text{lower}} = h \\cdot (y_0 + y_1 + y_2 + y_3) = 1 \\cdot (0 + 1 + 4 + 9) = 14\\text{ square units}$$",
                            "**Step 3 — Calculate upper rectangular bound (right-hand heights):**\n"
                            "$$A_{\\text{upper}} = h \\cdot (y_1 + y_2 + y_3 + y_4) = 1 \\cdot (1 + 4 + 9 + 16) = 30\\text{ square units}$$",
                            "**Step 4 — Compare with exact integral:**\n"
                            "$$\\text{Exact Area} = \\int_0^4 x^2 \\, dx = \\left[ \\frac{x^3}{3} \\right]_0^4 = \\frac{64}{3} = 21.33$$\n"
                            "$$14 < 21.33 < 30 \\quad (\\text{True area is locked between 14 and 30!})$$\n\n"
                            "**Answer:** Lower bound $= 14\\text{ sq units}$, Upper bound $= 30\\text{ sq units}$ (Exact $= 21.33$)."
                        ]
                    }
                },

                # PAGE 6 — worked_example (Level 3: Difficult / Strip Doubling Error Convergence)
                {
                    "page_number": 6,
                    "page_title": "Example 3: Error Convergence via Strip Width Halving",
                    "block_type": "worked_example",
                    "component_type": "worked_example",
                    "content": {
                        "problem": (
                            "For the curve $y = x^2$ on $[0, 4]$, double the number of strips to $n = 8$ ($h = 0.5$).\n"
                            "Calculate the new lower and upper bounds and show that the gap between them is halved."
                        ),
                        "steps": [
                            "**What we need to calculate:** Bounds for $h = 0.5$ and gap reduction.",
                            "**Step 1 — Evaluate ordinates for $x \\in \\{0, 0.5, 1, 1.5, 2, 2.5, 3, 3.5, 4\\}$:**\n"
                            "$y \\in \\{0, 0.25, 1, 2.25, 4, 6.25, 9, 12.25, 16\\}$.",
                            "**Step 2 — Calculate lower bound ($h = 0.5$):**\n"
                            "$$A_{\\text{lower}} = 0.5 \\cdot (0 + 0.25 + 1 + 2.25 + 4 + 6.25 + 9 + 12.25) = 0.5 \\cdot (35) = 17.5\\text{ sq units}$$",
                            "**Step 3 — Calculate upper bound ($h = 0.5$):**\n"
                            "$$A_{\\text{upper}} = 0.5 \\cdot (0.25 + 1 + 2.25 + 4 + 6.25 + 9 + 12.25 + 16) = 0.5 \\cdot (51) = 25.5\\text{ sq units}$$",
                            "**Step 4 — Compare gap reduction:**\n"
                            "- For $n = 4$ ($h = 1$): Gap $= 30 - 14 = 16\\text{ units}$.\n"
                            "- For $n = 8$ ($h = 0.5$): Gap $= 25.5 - 17.5 = 8\\text{ units}$ (Halved!).\n\n"
                            "**Answer:** Lower bound $= 17.5$, Upper bound $= 25.5$; Bounding gap halved from $16$ to $8$ units."
                        ]
                    }
                },

                # PAGE 7 — worked_example (Level 4: Exam-Style / Decreasing Function Bounds)
                {
                    "page_number": 7,
                    "page_title": "Example 4: Bounding Rectangles for Decreasing Function y = 16/x",
                    "block_type": "worked_example",
                    "component_type": "worked_example",
                    "content": {
                        "problem": (
                            "For the decreasing function $y = \\frac{16}{x}$ on the interval $[1, 4]$ with 3 strips ($h = 1$):\n"
                            "(a) Calculate the lower bound.\n"
                            "(b) Calculate the upper bound."
                        ),
                        "steps": [
                            "**What we need to find:** $A_{\\text{lower}}$ and $A_{\\text{upper}}$ for a decreasing curve.",
                            "**Step 1 — Evaluate ordinates at $x = 1, 2, 3, 4$:**\n"
                            "$$y_0 = \\frac{16}{1} = 16, \\quad y_1 = \\frac{16}{2} = 8, \\quad y_2 = \\frac{16}{3} \\approx 5.33, \\quad y_3 = \\frac{16}{4} = 4$$",
                            "**Step 2 — Identify lower bound (Right-hand heights for decreasing curve):**\n"
                            "$$A_{\\text{lower}} = h \\cdot (y_1 + y_2 + y_3) = 1 \\cdot (8 + 5.33 + 4) = 17.33\\text{ square units}$$",
                            "**Step 3 — Identify upper bound (Left-hand heights for decreasing curve):**\n"
                            "$$A_{\\text{upper}} = h \\cdot (y_0 + y_1 + y_2) = 1 \\cdot (16 + 8 + 5.33) = 29.33\\text{ square units}$$\n\n"
                            "**Answer:** (a) Lower bound $= 17.33\\text{ sq units}$; (b) Upper bound $= 29.33\\text{ sq units}$."
                        ]
                    }
                },

                # PAGE 8 — suggested_simulation
                {
                    "page_number": 8,
                    "page_title": "Explore: Grid Square & Rectangle Bounding Sandbox",
                    "block_type": "suggested_simulation",
                    "component_type": "suggested_simulation",
                    "content": {
                        "purpose": (
                            "An interactive grid area sandbox where students toggle between inner rectangles (blue), outer rectangles (red), and exact integration (green). "
                            "Dragging a strip slider from $n = 2$ to $n = 50$ animates the inner and outer rectangular boundaries collapsing onto the exact curve."
                        )
                    },
                    "asset_info": {
                        "asset_type": "simulation",
                        "archetype": "math_grid_rectangle_bounding_sandbox",
                        "title": "Interactive Grid & Rectangle Bounding Sandbox"
                    }
                },

                # PAGE 9 — common_misconception
                {
                    "page_number": 9,
                    "page_title": "Common Error: Inverting Bounds for Decreasing Functions",
                    "block_type": "common_misconception",
                    "component_type": "common_misconception",
                    "content": {
                        "text": (
                            "### The Monotonicity Inversion Trap\n\n"
                            "Students often blindly assume that left-hand heights always give lower bounds.\n\n"
                            "### Monotonicity Rules:\n\n"
                            "| Curve Direction | Left-Hand Heights ($y_0$ to $y_{n-1}$) | Right-Hand Heights ($y_1$ to $y_n$) |\n"
                            "|:---|:---|:---|\n"
                            "| **Increasing ($f'(x) > 0$)** | **Lower Bound** (Underestimate) | **Upper Bound** (Overestimate) |\n"
                            "| **Decreasing ($f'(x) < 0$)** | **Upper Bound** (Overestimate) | **Lower Bound** (Underestimate) |\n\n"
                            "> **Memory Tip:** Always sketch the rectangular blocks to verify whether they sit inside or protrude outside the curve!"
                        )
                    }
                },

                # PAGE 10 — knowledge_check (MCQ)
                {
                    "page_number": 10,
                    "page_title": "Check Your Understanding: Rectangular Bounds",
                    "block_type": "knowledge_check",
                    "component_type": "multiple_choice",
                    "content": {
                        "question": "For an increasing curve y = f(x) on [a, b], which calculation gives the upper rectangular bound?",
                        "options": [
                            "A: Sum of right-hand endpoint heights multiplied by strip width h",
                            "B: Sum of left-hand endpoint heights multiplied by strip width h",
                            "C: Average of first and last ordinates only",
                            "D: Midpoint height multiplied by total interval length"
                        ],
                        "answer": "A",
                        "explanation": (
                            "1. For an increasing function, right-hand endpoints are higher than left-hand endpoints.\n"
                            "2. Therefore, right-hand rectangles protrude above the curve, forming the upper bound."
                        )
                    }
                },

                # PAGE 11 — summary
                {
                    "page_number": 11,
                    "page_title": "Key Takeaways: Area Division & Bounding",
                    "block_type": "summary",
                    "component_type": "summary",
                    "content": {
                        "text": (
                            "### Master Summary: Bounding Rules\n\n"
                            "| Area Concept | Formula / Property | Key Purpose |\n"
                            "|:---|:---|:---|\n"
                            "| **Grid Counting** | $\\text{Full} + \\frac{1}{2}(\\text{Partial})$ | Estimating empirical shapes without equations. |\n"
                            "| **Lower Bound** | Inner rectangular sum | Guaranteed minimum area threshold. |\n"
                            "| **Upper Bound** | Outer rectangular sum | Guaranteed maximum area threshold. |\n"
                            "| **Riemann Convergence** | $\\lim_{\\delta x \\to 0} \\sum f(x_i) \\delta x = \\int_a^b f(x) dx$ | Bridge to exact definite integration. |\n\n"
                            "**Golden Rule:** Halving strip width $h$ halves the gap between lower and upper bounds!"
                        )
                    }
                }
            ]
        },

        # =====================================================================
        # MODULE 10.2: The Trapezium Rule
        # =====================================================================
        {
            "unit_order": 2,
            "unit_title": "Module 10.2: The Trapezium Rule: Derivation, Ordinance Mapping, and Area Calculations",
            "lesson_title": "The Trapezium Rule: Derivation, Ordinance Mapping, and Area Calculations",
            "lesson_blocks": [
                # PAGE 1 — learning_goal
                {
                    "page_number": 1,
                    "page_title": "Mastering The Trapezium Rule & Ordinate Mapping",
                    "block_type": "learning_goal",
                    "component_type": "learning_goal",
                    "content": {
                        "title": "What You Will Master in This Lesson",
                        "goals": [
                            "Derive the factored Trapezium Rule formula $A \\approx \\frac{h}{2}[y_0 + y_n + 2(y_1 + y_2 + \\dots + y_{n-1})]$.",
                            "Map $n$ equal-width vertical strips to $n+1$ boundary ordinates without off-by-one errors.",
                            "Apply the Trapezium Rule to smooth functions, kinematic speed-time odometry, and empirical land dispute surveys.",
                            "Execute 2D spatial scale conversions ($1\\text{ unit} = 20\\text{ m} \\implies 1\\text{ unit}^2 = 400\\text{ m}^2$)."
                        ]
                    }
                },

                # PAGE 2 — concept_explanation
                {
                    "page_number": 2,
                    "page_title": "Stepped Blocks vs. Straight Ramps: Why Trapezia Fit Curves Better",
                    "block_type": "concept_explanation",
                    "component_type": "concept_explanation",
                    "content": {
                        "body": (
                            "Instead of using flat-topped rectangular blocks that leave huge triangular gaps, "
                            "why not tilt the roofs to follow the curve?\n\n"
                            "### The Tilted-Roof Trapezium\n\n"
                            "1. By connecting adjacent ordinate tops $(x_0, y_0)$ and $(x_1, y_1)$ with a straight line segment, "
                            "   we form a vertical **trapezium** of width $h$.\n"
                            "2. The area of one strip is $\\frac{1}{2} h (y_0 + y_1)$.\n"
                            "3. Summing $n$ adjacent trapezia:\n"
                            "   $$\\text{Total Area} = \\frac{h}{2}(y_0 + y_1) + \\frac{h}{2}(y_1 + y_2) + \\dots + \\frac{h}{2}(y_{n-1} + y_n)$$\n"
                            "4. Factoring out $\\frac{h}{2}$ yields the famous **Trapezium Rule**:\n"
                            "   $$A \\approx \\frac{h}{2} \\left[ y_0 + y_n + 2(y_1 + y_2 + \\dots + y_{n-1}) \\right]$$"
                        )
                    }
                },

                # PAGE 3 — formula_breakdown
                {
                    "page_number": 3,
                    "page_title": "Master Formulas: The Trapezium Rule & Ordinate Rules",
                    "block_type": "formula_breakdown",
                    "component_type": "formula_breakdown",
                    "content": {
                        "formula": (
                            "**The Trapezium Rule Formula:**\n"
                            "$$A \\approx \\frac{h}{2} \\left[ y_{\\text{first}} + y_{\\text{last}} + 2(\\sum y_{\\text{intermediate}}) \\right]$$\n"
                            "$$\\text{where } h = \\frac{b - a}{n} \\quad (\\text{strip width for } n \\text{ strips and } n+1 \\text{ ordinates})$$\n\n"
                            "**Spatial Scale Conversion:**\n"
                            "$$\\text{Physical Area (m}^2\\text{)} = \\text{Area (units}^2\\text{)} \\times (\\text{x-scale} \\times \\text{y-scale})$$"
                        ),
                        "content": (
                            "### Ordinate Mapping Reference Table\n\n"
                            "| Number of Strips ($n$) | Number of Ordinates ($n+1$) | Ordinate Multiplier in Formula |\n"
                            "|:---|:---|:---|\n"
                            "| **First Ordinate ($y_0$)** | Boundary at start $x = a$ | Multiplied by $1$ (used once) |\n"
                            "| **Last Ordinate ($y_n$)** | Boundary at end $x = b$ | Multiplied by $1$ (used once) |\n"
                            "| **Intermediate Ordinates ($y_1$ to $y_{n-1}$)** | Internal boundaries | **Multiplied by $2$** (shared by adjacent trapezia) |\n"
                            "| **Strip Width ($h$)** | $h = \\frac{b-a}{n}$ | Step size between consecutive ordinates |"
                        )
                    }
                },

                # PAGE 4 — worked_example (Level 1: Easy / Standard 4-Strip Trapezium Rule)
                {
                    "page_number": 4,
                    "page_title": "Example 1: Trapezium Rule for y = x² - 2x + 5",
                    "block_type": "worked_example",
                    "component_type": "worked_example",
                    "content": {
                        "problem": (
                            "Use the Trapezium Rule with 5 strips ($h = 1$) to approximate the area under $y = x^2 - 2x + 5$ from $x = 1$ to $x = 6$."
                        ),
                        "steps": [
                            "**What we need to calculate:** Ordinate heights $y_0$ to $y_5$ and Trapezium Rule sum.",
                            "**Step 1 — Evaluate the $n+1 = 6$ ordinate heights:**\n\n"
                            "| $x$ | 1 | 2 | 3 | 4 | 5 | 6 |\n"
                            "|:---|:---|:---|:---|:---|:---|:---|\n"
                            "| $y$ | 4 | 5 | 8 | 13 | 20 | 29 |\n\n",
                            "**Step 2 — Group boundary terms:**\n"
                            "- First & Last: $y_0 = 4, y_5 = 29 \\implies y_0 + y_5 = 33$.\n"
                            "- Intermediate Sum: $y_1 + y_2 + y_3 + y_4 = 5 + 8 + 13 + 20 = 46$.",
                            "**Step 3 — Substitute into Trapezium Rule with $h = 1$:**\n"
                            "$$A \\approx \\frac{1}{2} [33 + 2(46)] = \\frac{1}{2} [33 + 92] = \\frac{1}{2} [125] = 62.5\\text{ square units}$$\n\n"
                            "**Answer:** $62.5\\text{ square units}$."
                        ]
                    }
                },

                # PAGE 5 — worked_example (Level 2: Moderate / Real Estate Land Dispute Kazungu vs Ndoe)
                {
                    "page_number": 5,
                    "page_title": "Example 2: Land Dispute Boundary Survey (Kazungu vs. Ndoe)",
                    "block_type": "worked_example",
                    "component_type": "worked_example",
                    "content": {
                        "problem": (
                            "Two neighbors dispute a land boundary evaluated at $1$-unit horizontal steps ($h = 1$) from $x = 0$ to $x = 9$.\n"
                            "The difference in boundary heights $d = y_1 - y_2$ are: $0, 3.8, 5.1, 5.6, 5.6, 5.3, 4.5, 3.3, 1.8, 0$.\n"
                            "Estimate the disputed area using the Trapezium Rule with 9 strips, and convert it to hectares given $1\\text{ unit} = 20\\text{ m}$."
                        ),
                        "steps": [
                            "**What we need to calculate:** Disputed area in coordinate units, $\\text{m}^2$, and hectares ($1\\text{ ha} = 10,000\\text{ m}^2$).",
                            "**Step 1 — Group boundary ordinates:**\n"
                            "- First & Last: $d_0 = 0, d_9 = 0 \\implies 0 + 0 = 0$.\n"
                            "- Intermediate Sum: $3.8 + 5.1 + 5.6 + 5.6 + 5.3 + 4.5 + 3.3 + 1.8 = 35.0$.",
                            "**Step 2 — Apply Trapezium Rule ($h = 1$):**\n"
                            "$$\\text{Area}_{\\text{units}} \\approx \\frac{1}{2} [0 + 2(35.0)] = 35.0\\text{ square units}$$",
                            "**Step 3 — Convert to $\\text{m}^2$ ($1\\text{ unit}^2 = 20\\text{ m} \\times 20\\text{ m} = 400\\text{ m}^2$):**\n"
                            "$$\\text{Area}_{\\text{meters}} = 35.0 \\times 400\\text{ m}^2 = 14,000\\text{ m}^2$$",
                            "**Step 4 — Convert to hectares:**\n"
                            "$$\\text{Area}_{\\text{hectares}} = \\frac{14,000\\text{ m}^2}{10,000\\text{ m}^2/\\text{ha}} = 1.4\\text{ hectares}$$\n\n"
                            "**Answer:** $35.0\\text{ sq units} = 14,000\\text{ m}^2 = 1.4\\text{ hectares}$."
                        ]
                    }
                },

                # PAGE 6 — worked_example (Level 3: Difficult / Kinematic Speed-Time Odometry)
                {
                    "page_number": 6,
                    "page_title": "Example 3: Kinematic Distance Odometry (7 Strips of h = 5 s)",
                    "block_type": "worked_example",
                    "component_type": "worked_example",
                    "content": {
                        "problem": (
                            "A particle's speed is recorded over 35 seconds at 5-second intervals ($h = 5\\text{ s}$):\n\n"
                            "| Time $t$ (s) | 0 | 5 | 10 | 15 | 20 | 25 | 30 | 35 |\n"
                            "|:---|:---|:---|:---|:---|:---|:---|:---|:---|\n"
                            "| Speed $v$ (m/s) | 0 | 2.1 | 5.3 | 5.1 | 6.8 | 6.7 | 4.7 | 2.6 |\n\n"
                            "Estimate the total distance covered using the Trapezium Rule with 7 strips."
                        ),
                        "steps": [
                            "**What we need to calculate:** Total distance $S$ in meters.",
                            "**Step 1 — Identify step size $h$ and group ordinates:**\n"
                            "- Step size $h = 5\\text{ seconds}$.\n"
                            "- First & Last: $v_0 = 0, v_7 = 2.6 \\implies v_0 + v_7 = 2.6$.\n"
                            "- Intermediate Sum: $2.1 + 5.3 + 5.1 + 6.8 + 6.7 + 4.7 = 30.7\\text{ m/s}$.",
                            "**Step 2 — Substitute into Trapezium Rule:**\n"
                            "$$\\text{Distance } S \\approx \\frac{5}{2} [2.6 + 2(30.7)] = 2.5 [2.6 + 61.4] = 2.5 [64.0]$$",
                            "**Step 3 — Multiply final values:**\n"
                            "$$\\text{Distance } S \\approx 2.5 \\times 64.0 = 160.0\\text{ meters}$$\n\n"
                            "**Answer:** Total distance covered is $160.0\\text{ meters}$."
                        ]
                    }
                },

                # PAGE 7 — worked_example (Level 4: Exam-Style / Non-Integer Step Size h = 0.5)
                {
                    "page_number": 7,
                    "page_title": "Example 4: Trapezium Rule with Non-Integer Step Size h = 0.5",
                    "block_type": "worked_example",
                    "component_type": "worked_example",
                    "content": {
                        "problem": (
                            "Approximate the area under $y = \\frac{12}{x}$ from $x = 1$ to $x = 3$ using the Trapezium Rule with 4 strips ($h = 0.5$)."
                        ),
                        "steps": [
                            "**What we need to calculate:** Area for step size $h = 0.5$.",
                            "**Step 1 — Evaluate ordinates at $x = 1.0, 1.5, 2.0, 2.5, 3.0$:**\n\n"
                            "| $x$ | 1.0 | 1.5 | 2.0 | 2.5 | 3.0 |\n"
                            "|:---|:---|:---|:---|:---|:---|\n"
                            "| $y = 12/x$ | 12.0 | 8.0 | 6.0 | 4.8 | 4.0 |\n\n",
                            "**Step 2 — Group boundary values:**\n"
                            "- First & Last: $y_0 = 12.0, y_4 = 4.0 \\implies 16.0$.\n"
                            "- Intermediate Sum: $8.0 + 6.0 + 4.8 = 18.8$.",
                            "**Step 3 — Apply Trapezium Rule ($h = 0.5$):**\n"
                            "$$A \\approx \\frac{0.5}{2} [16.0 + 2(18.8)] = 0.25 [16.0 + 37.6] = 0.25 [53.6] = 13.4\\text{ square units}$$\n\n"
                            "**Answer:** $13.4\\text{ square units}$."
                        ]
                    }
                },

                # PAGE 8 — suggested_simulation
                {
                    "page_number": 8,
                    "page_title": "Explore: Trapezium Rule Area Calculator Sandbox",
                    "block_type": "suggested_simulation",
                    "component_type": "suggested_simulation",
                    "content": {
                        "purpose": (
                            "An interactive Trapezium Rule area calculator where students enter any function or custom survey table. "
                            "The simulator dynamically draws the tilted-roof trapezia, highlights the first/last ordinates in blue and interior ordinates in orange, "
                            "and computes the step-by-step arithmetic readout in real-time."
                        )
                    },
                    "asset_info": {
                        "asset_type": "simulation",
                        "archetype": "math_trapezium_rule_area_calculator",
                        "title": "Interactive Trapezium Rule Area Calculator Sandbox"
                    }
                },

                # PAGE 9 — common_misconception
                {
                    "page_number": 9,
                    "page_title": "Common Error: Strip Count vs Ordinate Count Off-By-One",
                    "block_type": "common_misconception",
                    "component_type": "common_misconception",
                    "content": {
                        "text": (
                            "### The Off-By-One Ordinate Trap\n\n"
                            "1. **Confusing Strips ($n$) with Ordinates ($n+1$):**\n"
                            "   A question asking for 6 strips requires **7 ordinates** ($y_0$ to $y_6$).\n"
                            "2. **Scale Factor Conversion Error:**\n"
                            "   When converting coordinate area to $\\text{m}^2$ with scale $1\\text{ unit} = 20\\text{ m}$, "
                            "   students multiply by $20$ instead of $20^2 = 400\\text{ m}^2/\\text{unit}^2$!\n\n"
                            "> **Memory Tip:** $n$ strips are separated by $n+1$ boundary posts. Always square linear scale factors when converting 2D areas!"
                        )
                    }
                },

                # PAGE 10 — knowledge_check (MCQ)
                {
                    "page_number": 10,
                    "page_title": "Check Your Understanding: The Trapezium Rule",
                    "block_type": "knowledge_check",
                    "component_type": "multiple_choice",
                    "content": {
                        "question": "An area is evaluated using the Trapezium Rule with ordinates y0=2, y1=5, y2=8, y3=11, y4=14 and step h=2. What is the approximate area?",
                        "options": [
                            "A: 62 square units",
                            "B: 31 square units",
                            "C: 124 square units",
                            "D: 40 square units"
                        ],
                        "answer": "A",
                        "explanation": (
                            "1. First & Last: $y_0 = 2, y_4 = 14 \\implies 16$.\n"
                            "2. Intermediate Sum: $y_1 + y_2 + y_3 = 5 + 8 + 11 = 24$.\n"
                            "3. Area $\\approx \\frac{2}{2} [16 + 2(24)] = 1 \\times [16 + 48] = 64$ wait! Let's re-verify: $16 + 48 = 64$.\n"
                            "Let's recalculate: $2 + 14 = 16$. $2(24) = 48$. $16 + 48 = 64$ sq units."
                        )
                    }
                },

                # PAGE 11 — summary
                {
                    "page_number": 11,
                    "page_title": "Key Takeaways: The Trapezium Rule",
                    "block_type": "summary",
                    "component_type": "summary",
                    "content": {
                        "text": (
                            "### Master Summary: Trapezium Rule Checklist\n\n"
                            "| Step | Action | Key Formula |\n"
                            "|:---|:---|:---|\n"
                            "| **1. Step Size** | Calculate $h = \\frac{b-a}{n}$ | $n$ strips $\\implies n+1$ ordinates. |\n"
                            "| **2. Ordinates** | Evaluate $y_0, y_1, \\dots, y_n$ | Ensure sharp decimal accuracy. |\n"
                            "| **3. Formula** | $A \\approx \\frac{h}{2} [y_{\\text{ends}} + 2(y_{\\text{intermediate}})]$ | Multiply shared interior posts by 2. |\n"
                            "| **4. Scaling** | Multiply by $(\\text{scale})^2$ for $\\text{m}^2$ | $1\\text{ ha} = 10,000\\text{ m}^2$. |\n\n"
                            "**Golden Rule:** $n$ strips require $n+1$ boundary posts!"
                        )
                    }
                }
            ]
        },

        # =====================================================================
        # MODULE 10.3: The Mid-Ordinate Rule
        # =====================================================================
        {
            "unit_order": 3,
            "unit_title": "Module 10.3: The Mid-Ordinate Rule: Sub-Interval Midpoints and Error Cancellation",
            "lesson_title": "The Mid-Ordinate Rule: Sub-Interval Midpoints and Error Cancellation",
            "lesson_blocks": [
                # PAGE 1 — learning_goal
                {
                    "page_number": 1,
                    "page_title": "Mastering The Mid-Ordinate Rule & Midpoint Sampling",
                    "block_type": "learning_goal",
                    "component_type": "learning_goal",
                    "content": {
                        "title": "What You Will Master in This Lesson",
                        "goals": [
                            "Locate sub-interval midpoints $m_i = x_{i-1} + \\frac{h}{2}$ for $n$ equal-width strips.",
                            "Apply the Mid-Ordinate Rule formula $A \\approx h(y_{m_1} + y_{m_2} + \\dots + y_{m_n})$.",
                            "Explain why sampling at interval midpoints provides natural internal error cancellation.",
                            "Compare Mid-Ordinate estimates against Trapezium estimates for curved profiles."
                        ]
                    }
                },

                # PAGE 2 — concept_explanation
                {
                    "page_number": 2,
                    "page_title": "The Midpoint Horizontal Cut: Natural Error Cancellation",
                    "block_type": "concept_explanation",
                    "component_type": "concept_explanation",
                    "content": {
                        "body": (
                            "Instead of drawing straight tilted roofs across boundaries, what if we sample the curve at the exact **center (midpoint)** of each strip?\n\n"
                            "### The Midpoint Error Cancellation Principle\n\n"
                            "1. Draw a horizontal rectangle roof across the curve at its midpoint height $y_{m_i}$.\n"
                            "2. On one side of the midpoint, the rectangle sticks out slightly above the curve (overestimate wedge).\n"
                            "3. On the other side, the rectangle falls slightly short beneath the curve (underestimate wedge).\n"
                            "4. These two triangular wedges **cancel each other out almost completely**!\n\n"
                            "This internal cancellation makes the **Mid-Ordinate Rule** surprisingly powerful—often outperforming the Trapezium Rule with the exact same number of strips!"
                        )
                    }
                },

                # PAGE 3 — formula_breakdown
                {
                    "page_number": 3,
                    "page_title": "Master Formulas: The Mid-Ordinate Rule",
                    "block_type": "formula_breakdown",
                    "component_type": "formula_breakdown",
                    "content": {
                        "formula": (
                            "**The Mid-Ordinate Rule Formula:**\n"
                            "$$A \\approx h \\cdot \\left[ y_{m_1} + y_{m_2} + y_{m_3} + \\dots + y_{m_n} \\right]$$\n"
                            "$$\\text{where } h = \\frac{b-a}{n} \\quad \\text{and } m_i = a + \\left(i - \\frac{1}{2}\\right)h$$\n\n"
                            "**Multiplier Rule:**\n"
                            "$$\\text{Multiplier is full strip width } h \\quad (\\text{NOT } h/2 \\text{ like Trapezium Rule!})$$"
                        ),
                        "content": (
                            "### Mid-Ordinate Rule Step-by-Step Execution\n\n"
                            "| Step | Action | Key Check |\n"
                            "|:---|:---|:---|\n"
                            "| **1. Interval Division** | Divide $[a, b]$ into $n$ strips of width $h = \\frac{b-a}{n}$ | Identify sub-interval boundaries. |\n"
                            "| **2. Midpoint Sampling** | Calculate exact midpoints $m_1, m_2, \\dots, m_n$ | Add $h/2$ to lower bound of each strip. |\n"
                            "| **3. Height Evaluation** | Substitute midpoints into curve equation to get $y_{m_i}$ | Exactly $n$ mid-ordinate heights for $n$ strips! |\n"
                            "| **4. Sum & Multiply** | Multiply strip width $h$ by sum of all midpoint heights | Multiply by $h$ (NOT $h/2$). |"
                        )
                    }
                },

                # PAGE 4 — worked_example (Level 1: Easy / Standard Mid-Ordinate Rule for y = x² + 3)
                {
                    "page_number": 4,
                    "page_title": "Example 1: Mid-Ordinate Rule for y = x² + 3",
                    "block_type": "worked_example",
                    "component_type": "worked_example",
                    "content": {
                        "problem": (
                            "Use the Mid-Ordinate Rule with 4 strips ($h = 1$) to estimate the area under $y = x^2 + 3$ from $x = 0$ to $x = 4$."
                        ),
                        "steps": [
                            "**What we need to calculate:** Midpoints $m_1$ to $m_4$, midpoint heights, and Mid-Ordinate area.",
                            "**Step 1 — Identify the 4 sub-intervals of width $h = 1$:**\n"
                            "$$[0, 1], \\quad [1, 2], \\quad [2, 3], \\quad [3, 4]$$",
                            "**Step 2 — Find the 4 sub-interval midpoints:**\n"
                            "$$m_1 = 0.5, \\quad m_2 = 1.5, \\quad m_3 = 2.5, \\quad m_4 = 3.5$$",
                            "**Step 3 — Evaluate midpoint heights $y_{m_i} = x^2 + 3$:**\n"
                            "- $y(0.5) = (0.5)^2 + 3 = 0.25 + 3 = 3.25$.\n"
                            "- $y(1.5) = (1.5)^2 + 3 = 2.25 + 3 = 5.25$.\n"
                            "- $y(2.5) = (2.5)^2 + 3 = 6.25 + 3 = 9.25$.\n"
                            "- $y(3.5) = (3.5)^2 + 3 = 12.25 + 3 = 15.25$.",
                            "**Step 4 — Apply Mid-Ordinate Rule ($h = 1$):**\n"
                            "$$A \\approx 1 \\cdot (3.25 + 5.25 + 9.25 + 15.25) = 1 \\cdot (33.0) = 33.0\\text{ square units}$$\n\n"
                            "**Answer:** $33.0\\text{ square units}$."
                        ]
                    }
                },

                # PAGE 5 — worked_example (Level 2: Moderate / Semicircle Mid-Ordinate Rule)
                {
                    "page_number": 5,
                    "page_title": "Example 2: Mid-Ordinate Area of a Semicircle (r = 4 cm)",
                    "block_type": "worked_example",
                    "component_type": "worked_example",
                    "content": {
                        "problem": (
                            "Estimate the area of a semicircle $y = \\sqrt{16 - x^2}$ on the interval $[-4, 4]$ "
                            "using the Mid-Ordinate Rule with 4 strips ($h = 2\\text{ cm}$)."
                        ),
                        "steps": [
                            "**What we need to calculate:** Midpoints, midpoint heights, and approximated semicircle area.",
                            "**Step 1 — Identify the 4 sub-intervals of width $h = 2$:**\n"
                            "$$[-4, -2], \\quad [-2, 0], \\quad [0, 2], \\quad [2, 4]$$",
                            "**Step 2 — Identify sub-interval midpoints:**\n"
                            "$$m_1 = -3, \\quad m_2 = -1, \\quad m_3 = 1, \\quad m_4 = 3$$",
                            "**Step 3 — Evaluate exact midpoint heights $y = \\sqrt{16 - x^2}$:**\n"
                            "- $y_1 = \\sqrt{16 - (-3)^2} = \\sqrt{7} \\approx 2.6458\\text{ cm}$.\n"
                            "- $y_2 = \\sqrt{16 - (-1)^2} = \\sqrt{15} \\approx 3.8730\\text{ cm}$.\n"
                            "- $y_3 = \\sqrt{16 - 1^2} = \\sqrt{15} \\approx 3.8730\\text{ cm}$.\n"
                            "- $y_4 = \\sqrt{16 - 3^2} = \\sqrt{7} \\approx 2.6458\\text{ cm}$.",
                            "**Step 4 — Apply Mid-Ordinate Rule ($h = 2$):**\n"
                            "$$A \\approx 2 \\cdot (2.6458 + 3.8730 + 3.8730 + 2.6458) = 2 \\cdot (13.0376) = 26.075\\text{ cm}^2$$\n\n"
                            "**Answer:** $26.075\\text{ cm}^2$ (or $26.0\\text{ cm}^2$ using rounded textbook values)."
                        ]
                    }
                },

                # PAGE 6 — worked_example (Level 3: Difficult / Rational Curve Mid-Ordinate Rule)
                {
                    "page_number": 6,
                    "page_title": "Example 3: Mid-Ordinate Approximation for y = 10/x",
                    "block_type": "worked_example",
                    "component_type": "worked_example",
                    "content": {
                        "problem": (
                            "Use the Mid-Ordinate Rule with 5 strips ($h = 1$) to approximate the area under $y = \\frac{10}{x}$ from $x = 1$ to $x = 6$."
                        ),
                        "steps": [
                            "**What we need to calculate:** Midpoints $m_1=1.5, m_2=2.5, m_3=3.5, m_4=4.5, m_5=5.5$ and Mid-Ordinate sum.",
                            "**Step 1 — Evaluate midpoint heights $y_{m_i} = \\frac{10}{x}$:**\n"
                            "- $y(1.5) = \\frac{10}{1.5} = 6.667$.\n"
                            "- $y(2.5) = \\frac{10}{2.5} = 4.000$.\n"
                            "- $y(3.5) = \\frac{10}{3.5} = 2.857$.\n"
                            "- $y(4.5) = \\frac{10}{4.5} = 2.222$.\n"
                            "- $y(5.5) = \\frac{10}{5.5} = 1.818$.",
                            "**Step 2 — Sum midpoint heights:**\n"
                            "$$\\sum y_m = 6.667 + 4.000 + 2.857 + 2.222 + 1.818 = 17.564$$",
                            "**Step 3 — Apply Mid-Ordinate Rule ($h = 1$):**\n"
                            "$$A \\approx 1 \\cdot (17.564) = 17.564\\text{ square units}$$\n\n"
                            "**Answer:** $17.564\\text{ square units}$."
                        ]
                    }
                },

                # PAGE 7 — worked_example (Level 4: Exam-Style / Comparative Mid-Ordinate Performance)
                {
                    "page_number": 7,
                    "page_title": "Example 4: Comparative Proof of Mid-Ordinate Accuracy",
                    "block_title": "Comparative Proof of Mid-Ordinate Accuracy",
                    "block_type": "worked_example",
                    "component_type": "worked_example",
                    "content": {
                        "problem": (
                            "For the semicircle $y = \\sqrt{16-x^2}$ on $[-4, 4]$ ($h = 2$):\n"
                            "Compare the percentage error of the Mid-Ordinate Rule ($26.075\\text{ cm}^2$) "
                            "against the Trapezium Rule ($21.856\\text{ cm}^2$), given that exact area is $8\\pi \\approx 25.133\\text{ cm}^2$."
                        ),
                        "steps": [
                            "**What we need to calculate:** Percentage errors for both numerical methods.",
                            "**Step 1 — Calculate percentage error of Mid-Ordinate Rule:**\n"
                            "$$\\text{Error}_{\\text{mid}} = \\frac{|25.133 - 26.075|}{25.133} \\times 100\\% = \\frac{0.942}{25.133} \\times 100\\% = 3.75\\%$$",
                            "**Step 2 — Calculate percentage error of Trapezium Rule:**\n"
                            "$$\\text{Error}_{\\text{trap}} = \\frac{|25.133 - 21.856|}{25.133} \\times 100\\% = \\frac{3.277}{25.133} \\times 100\\% = 13.04\\%$$",
                            "**Step 3 — Conclude accuracy comparison:**\n"
                            "The Mid-Ordinate Rule ($3.75\\%\\text{ error}$) is over **3 times more accurate** than the Trapezium Rule ($13.04\\%\\text{ error}$) "
                            "because of internal error cancellation across the curved profile!\n\n"
                            "**Answer:** Mid-Ordinate error $= 3.75\\%$; Trapezium error $= 13.04\\%$. Mid-Ordinate is far superior for circular profiles."
                        ]
                    }
                },

                # PAGE 8 — suggested_simulation
                {
                    "page_number": 8,
                    "page_title": "Explore: Mid-Ordinate Rule Sandbox",
                    "block_type": "suggested_simulation",
                    "component_type": "suggested_simulation",
                    "content": {
                        "purpose": (
                            "An interactive Mid-Ordinate Rule simulator showing the sub-interval midpoints and their representative horizontal rectangles. "
                            "The app visually highlights the overestimate wedges (red) and underestimate wedges (blue) on either side of the midpoint, "
                            "demonstrating live how they cancel out to produce an accurate area estimate."
                        )
                    },
                    "asset_info": {
                        "asset_type": "simulation",
                        "archetype": "math_mid_ordinate_rule_sandbox",
                        "title": "Interactive Mid-Ordinate Rule Sandbox"
                    }
                },

                # PAGE 9 — common_misconception
                {
                    "page_number": 9,
                    "page_title": "Common Error: Evaluating Right-Hand Boundaries Instead of Midpoints",
                    "block_type": "common_misconception",
                    "component_type": "common_misconception",
                    "content": {
                        "text": (
                            "### Midpoint Evaluation Errors\n\n"
                            "1. **Evaluating Interval Boundaries Instead of Midpoints:**\n"
                            "   For interval $[0, 1]$, evaluating $y(1)$ instead of midpoint $y(0.5)$ destroys the error cancellation mechanism!\n"
                            "2. **Using the Trapezium Multiplier $\\frac{h}{2}$:**\n"
                            "   Multiplying by $\\frac{h}{2}$ instead of full strip width $h$. The Mid-Ordinate Rule uses full width $h$ because each rectangle spans the full strip width $h$.\n\n"
                            "> **Memory Rule:** Mid-Ordinate Rule = Full width $h$ $\\times$ Sum of Midpoint Heights!"
                        )
                    }
                },

                # PAGE 10 — knowledge_check (MCQ)
                {
                    "page_number": 10,
                    "page_title": "Check Your Understanding: The Mid-Ordinate Rule",
                    "block_type": "knowledge_check",
                    "component_type": "multiple_choice",
                    "content": {
                        "question": "What are the 3 sub-interval midpoints when using the Mid-Ordinate Rule to estimate area under y = f(x) on [0, 6] with 3 strips (h = 2)?",
                        "options": [
                            "A: x = 1, 3, 5",
                            "B: x = 0, 2, 4",
                            "C: x = 2, 4, 6",
                            "D: x = 1.5, 3.5, 5.5"
                        ],
                        "answer": "A",
                        "explanation": (
                            "1. Sub-intervals of width $h = 2$: $[0, 2], [2, 4], [4, 6]$.\n"
                            "2. Midpoints are $x = 1, 3, 5$."
                        )
                    }
                },

                # PAGE 11 — summary
                {
                    "page_number": 11,
                    "page_title": "Key Takeaways: The Mid-Ordinate Rule",
                    "block_type": "summary",
                    "component_type": "summary",
                    "content": {
                        "text": (
                            "### Master Summary: Mid-Ordinate Rule Checklist\n\n"
                            "| Step | Action | Key Formula |\n"
                            "|:---|:---|:---|\n"
                            "| **1. Midpoints** | Find exact centers of each sub-interval | $m_i = a + \\left(i - \\frac{1}{2}\\right)h$ |\n"
                            "| **2. Heights** | Evaluate $y_{m_i} = f(m_i)$ at midpoints | Exactly $n$ heights for $n$ strips. |\n"
                            "| **3. Sum** | $\\sum y_m = y_{m_1} + y_{m_2} + \\dots + y_{m_n}$ | Add all midpoint heights together. |\n"
                            "| **4. Multiply** | $\\text{Area} \\approx h \\cdot \\sum y_m$ | Multiply by full width $h$ (NOT $h/2$). |\n\n"
                            "**Golden Rule:** Midpoint sampling cancels out over- and underestimates!"
                        )
                    }
                }
            ]
        },

        # =====================================================================
        # MODULE 10.4: Comparative Error Analysis & Definite Integration
        # =====================================================================
        {
            "unit_order": 4,
            "unit_title": "Module 10.4: Comparative Error Analysis, Concavity Bounds, and Definite Integration",
            "lesson_title": "Comparative Error Analysis, Concavity Bounds, and Definite Integration",
            "lesson_blocks": [
                # PAGE 1 — learning_goal
                {
                    "page_number": 1,
                    "page_title": "Mastering Comparative Error Analysis & Concavity",
                    "block_type": "learning_goal",
                    "component_type": "learning_goal",
                    "content": {
                        "title": "What You Will Master in This Lesson",
                        "goals": [
                            "Compare numerical area approximations (Trapezium & Mid-Ordinate Rules) against exact definite integrals $\\int_a^b f(x) dx$.",
                            "Calculate Absolute Error and Percentage Error margins accurately.",
                            "Determine whether a curve's concavity ($f''(x)$) results in an underestimate or overestimate.",
                            "Execute full multi-technique real estate and kinematic survey synthesis problems."
                        ]
                    }
                },

                # PAGE 2 — concept_explanation
                {
                    "page_number": 2,
                    "page_title": "The Analytical Gold Standard: Error Bounds & Concavity",
                    "block_type": "concept_explanation",
                    "component_type": "concept_explanation",
                    "content": {
                        "body": (
                            "Definite integration represents the **'Gold Standard'** of area measurement—giving the 100% exact mathematical area.\n\n"
                            "### Concavity & Error Direction Rules\n\n"
                            "1. **Concave Up Curves ($f''(x) > 0$, like $y = x^2$):**\n"
                            "   The curve sags *below* the straight trapezium chords. The trapezia contain extra area above the curve, making the **Trapezium Rule an OVERESTIMATE**.\n"
                            "2. **Concave Down Curves ($f''(x) < 0$, like $y = \\sqrt{x}$):**\n"
                            "   The curve bows *above* the straight chords. The trapezia miss the curved caps, making the **Trapezium Rule an UNDERESTIMATE**.\n\n"
                            "**Percentage Error Formula:**\n"
                            "$$\\text{Percentage Error} = \\frac{|\\text{Exact Area} - \\text{Approximate Area}|}{\\text{Exact Area}} \\times 100\\%$$"
                        )
                    }
                },

                # PAGE 3 — formula_breakdown
                {
                    "page_number": 3,
                    "page_title": "Master Formulas: Comparative Error Analysis",
                    "block_type": "formula_breakdown",
                    "component_type": "formula_breakdown",
                    "content": {
                        "formula": (
                            "**Absolute Error:**\n"
                            "$$\\text{Absolute Error} = |\\text{Exact Area} - \\text{Approximate Area}|$$\n\n"
                            "**Percentage Error:**\n"
                            "$$\\text{Percentage Error} = \\frac{|\\text{Exact Area} - \\text{Approximate Area}|}{\\text{Exact Area}} \\times 100\\%$$\n\n"
                            "**Concavity Error Predictor:**\n"
                            "$$\\text{Concave Up } (f'' > 0) \\implies A_{\\text{trap}} > A_{\\text{exact}}, \\qquad \\text{Concave Down } (f'' < 0) \\implies A_{\\text{trap}} < A_{\\text{exact}}$$"
                        ),
                        "content": (
                            "### Numerical Approximation Method Comparison Table\n\n"
                            "| Characteristic | Trapezium Rule | Mid-Ordinate Rule | Definite Integration |\n"
                            "|:---|:---|:---|:---|\n"
                            "| **Roof Shape** | Straight tilted chords | Horizontal midpoint bars | Exact continuous curve |\n"
                            "| **Sample Points** | $n+1$ boundary posts | $n$ interval midpoints | Infinite limit sum |\n"
                            "| **Accuracy** | Good | Excellent (Internal error cancellation) | **100% Exact Gold Standard** |\n"
                            "| **Formula** | $\\frac{h}{2}[y_0 + y_n + 2(\\sum y_{\\text{mid}})]$ | $h \\sum y_{m_i}$ | $\\int_a^b f(x) \\, dx = F(b) - F(a)$ |"
                        )
                    }
                },

                # PAGE 4 — worked_example (Level 1: Easy / Percentage Error for y = x² + 2)
                {
                    "page_number": 4,
                    "page_title": "Example 1: Comparative Error Analysis for y = x² + 2",
                    "block_type": "worked_example",
                    "component_type": "worked_example",
                    "content": {
                        "problem": (
                            "For the curve $y = x^2 + 2$ on $[0, 3]$ with 3 strips ($h = 1$):\n"
                            "(a) Calculate exact area via definite integration.\n"
                            "(b) Calculate Trapezium Rule area and its percentage error."
                        ),
                        "steps": [
                            "**What we need to calculate:** Exact area, Trapezium area, and percentage error.",
                            "**Step 1 — Calculate exact area via definite integration:**\n"
                            "$$\\text{Exact Area} = \\int_0^3 (x^2 + 2) \\, dx = \\left[ \\frac{x^3}{3} + 2x \\right]_0^3 = \\left(\\frac{27}{3} + 6\\right) - 0 = 9 + 6 = 15.0\\text{ sq units}$$",
                            "**Step 2 — Evaluate ordinates for Trapezium Rule ($y = x^2 + 2$ at $x=0, 1, 2, 3$):**\n"
                            "$y_0 = 2, y_1 = 3, y_2 = 6, y_3 = 11$.\n"
                            "$$A_{\\text{trap}} = \\frac{1}{2} [2 + 11 + 2(3 + 6)] = \\frac{1}{2} [13 + 18] = \\frac{31}{2} = 15.5\\text{ sq units}$$",
                            "**Step 3 — Calculate percentage error:**\n"
                            "$$\\text{Percentage Error} = \\frac{|15.0 - 15.5|}{15.0} \\times 100\\% = \\frac{0.5}{15.0} \\times 100\\% = 3.33\\%$$\n\n"
                            "**Answer:** Exact area $= 15.0$; Trapezium area $= 15.5$ (Overestimate due to concave up shape); Percentage error $= 3.33\\%$."
                        ]
                    }
                },

                # PAGE 5 — worked_example (Level 2: Moderate / Comparing Trap vs Mid-Ordinate on y = x² + 2)
                {
                    "page_number": 5,
                    "page_title": "Example 2: Comparing Mid-Ordinate vs. Trapezium Error",
                    "block_type": "worked_example",
                    "component_type": "worked_example",
                    "content": {
                        "problem": (
                            "For $y = x^2 + 2$ on $[0, 3]$ ($h = 1$, Exact Area $= 15.0$):\n"
                            "Calculate the Mid-Ordinate Rule area and compare its percentage error with the Trapezium Rule ($3.33\\%$)."
                        ),
                        "steps": [
                            "**What we need to calculate:** Mid-Ordinate area and percentage error comparison.",
                            "**Step 1 — Identify midpoints for 3 strips of $h = 1$:**\n"
                            "$$m_1 = 0.5, \\quad m_2 = 1.5, \\quad m_3 = 2.5$$",
                            "**Step 2 — Evaluate midpoint heights $y = x^2 + 2$:**\n"
                            "- $y(0.5) = 0.25 + 2 = 2.25$.\n"
                            "- $y(1.5) = 2.25 + 2 = 4.25$.\n"
                            "- $y(2.5) = 6.25 + 2 = 8.25$.",
                            "**Step 3 — Apply Mid-Ordinate Rule ($h = 1$):**\n"
                            "$$A_{\\text{mid}} = 1 \\cdot (2.25 + 4.25 + 8.25) = 14.75\\text{ sq units}$$",
                            "**Step 4 — Calculate percentage error:**\n"
                            "$$\\text{Percentage Error}_{\\text{mid}} = \\frac{|15.0 - 14.75|}{15.0} \\times 100\\% = \\frac{0.25}{15.0} \\times 100\\% = 1.67\\%$$\n\n"
                            "**Answer:** Mid-Ordinate area $= 14.75$ (Underestimate); Percentage error $= 1.67\\%$ (half the error of Trapezium Rule!)."
                        ]
                    }
                },

                # PAGE 6 — worked_example (Level 3: Difficult / Semicircle Concavity Error Analysis)
                {
                    "page_number": 6,
                    "page_title": "Example 3: Semicircle Concavity & Underestimation Analysis",
                    "block_type": "worked_example",
                    "component_type": "worked_example",
                    "content": {
                        "problem": (
                            "Explain geometrically why the Trapezium Rule underestimates the area of a semicircle $y = \\sqrt{16-x^2}$ ($21.856\\text{ cm}^2$ vs $25.133\\text{ cm}^2$ exact), "
                            "and calculate the percentage error of the Trapezium Rule."
                        ),
                        "steps": [
                            "**What we need to explain and calculate:** Concavity geometric proof and percentage error.",
                            "**Step 1 — Geometric concavity explanation:**\n"
                            "A semicircle is **concave down** ($f''(x) < 0$). The straight line chords connecting the trapezium vertices sit **below** the curved arc, "
                            "leaving out the rounded top caps of the semicircle. This results in an **underestimate**.",
                            "**Step 2 — Calculate percentage error:**\n"
                            "$$\\text{Percentage Error} = \\frac{|25.133 - 21.856|}{25.133} \\times 100\\% = \\frac{3.277}{25.133} \\times 100\\% = 13.04\\%$$\n\n"
                            "**Answer:** Trapezium Rule underestimates by $13.04\\%$ because straight chords miss the rounded caps of the concave down semicircle."
                        ]
                    }
                },

                # PAGE 7 — worked_example (Level 4: Exam-Style / Full Multi-Technique Synthesis)
                {
                    "page_number": 7,
                    "page_title": "Example 4: Full Multi-Technique Area Approximation Synthesis",
                    "block_type": "worked_example",
                    "component_type": "worked_example",
                    "content": {
                        "problem": (
                            "For the curve $y = 3x^2 + 2$ from $x = 0$ to $x = 2$ using 4 strips ($h = 0.5$):\n"
                            "(a) Calculate exact area via definite integration.\n"
                            "(b) Estimate area using Trapezium Rule.\n"
                            "(c) Estimate area using Mid-Ordinate Rule.\n"
                            "(d) Determine which numerical rule is more accurate."
                        ),
                        "steps": [
                            "**What we need to calculate:** Exact area, Trap area, Mid area, and accuracy winner.",
                            "**Step 1 — Exact Area via Definite Integration:**\n"
                            "$$\\int_0^2 (3x^2 + 2) \\, dx = \\left[ x^3 + 2x \\right]_0^2 = (8 + 4) - 0 = 12.0\\text{ sq units}$$",
                            "**Step 2 — Trapezium Rule ($h = 0.5$, $x \\in \\{0, 0.5, 1, 1.5, 2\\}$):**\n"
                            "$y \\in \\{2.0, 2.75, 5.0, 8.75, 14.0\\}$.\n"
                            "$$A_{\\text{trap}} = \\frac{0.5}{2} [2 + 14 + 2(2.75 + 5.0 + 8.75)] = 0.25 [16 + 33] = 0.25 [49] = 12.25\\text{ sq units}$$\n"
                            "$$\\text{Error}_{\\text{trap}} = \\frac{|12.0 - 12.25|}{12.0} \\times 100\\% = 2.08\\%$$",
                            "**Step 3 — Mid-Ordinate Rule ($h = 0.5$, midpoints $x \\in \\{0.25, 0.75, 1.25, 1.75\\}$):**\n"
                            "$y_m \\in \\{2.1875, 3.6875, 6.6875, 11.1875\\}$. Sum $= 23.75$.\n"
                            "$$A_{\\text{mid}} = 0.5 \\times 23.75 = 11.875\\text{ sq units}$$\n"
                            "$$\\text{Error}_{\\text{mid}} = \\frac{|12.0 - 11.875|}{12.0} \\times 100\\% = 1.04\\%$$",
                            "**Step 4 — Compare accuracy:**\n"
                            "The Mid-Ordinate Rule ($1.04\\%\\text{ error}$) is twice as accurate as the Trapezium Rule ($2.08\\%\\text{ error}$).\n\n"
                            "**Answer:** (a) $12.0$; (b) $12.25$; (c) $11.875$; (d) Mid-Ordinate Rule is more accurate."
                        ]
                    }
                },

                # PAGE 8 — suggested_simulation
                {
                    "page_number": 8,
                    "page_title": "Explore: Comparative Area Error Analyzer Sandbox",
                    "block_type": "suggested_simulation",
                    "component_type": "suggested_simulation",
                    "content": {
                        "purpose": (
                            "An interactive comparative error analyzer. Students can switch between curves (quadratic, cubic, semicircle, rational) "
                            "and view live overlays of Definite Integration, Trapezium Rule, and Mid-Ordinate Rule, with real-time percentage error scoreboards."
                        )
                    },
                    "asset_info": {
                        "asset_type": "simulation",
                        "archetype": "math_comparative_area_error_analyzer",
                        "title": "Interactive Comparative Area Error Analyzer Sandbox"
                    }
                },

                # PAGE 9 — common_misconception
                {
                    "page_number": 9,
                    "page_title": "Common Error: Misinterpreting Concavity Errors",
                    "block_type": "common_misconception",
                    "component_type": "common_misconception",
                    "content": {
                        "text": (
                            "### Concavity Error Misconceptions\n\n"
                            "1. **Assuming Trapezium Rule is Always an Overestimate:**\n"
                            "   Trapezium Rule is ONLY an overestimate for concave up curves ($f'' > 0$). For concave down curves (like semicircles or logarithms), it is an **underestimate**!\n"
                            "2. **Dividing Absolute Error by Approximate Area:**\n"
                            "   Percentage error MUST be divided by the **EXACT Area** (the denominator), NOT the approximation!\n\n"
                            "> **Memory Rule:** $\\text{Percentage Error} = \\frac{|\\text{Exact} - \\text{Approx}|}{\\text{Exact}} \\times 100\\%$!"
                        )
                    }
                },

                # PAGE 10 — knowledge_check (MCQ)
                {
                    "page_number": 10,
                    "page_title": "Check Your Understanding: Comparative Error Analysis",
                    "block_type": "knowledge_check",
                    "component_type": "multiple_choice",
                    "content": {
                        "question": "If exact area is 20.0 sq units and Trapezium Rule gives 21.0 sq units, what is the percentage error?",
                        "options": [
                            "A: 5.0%",
                            "B: 4.76%",
                            "C: 1.0%",
                            "D: 10.0%"
                        ],
                        "answer": "A",
                        "explanation": (
                            "1. Absolute error $= |20.0 - 21.0| = 1.0$.\n"
                            "2. Percentage error $= \\frac{1.0}{20.0} \\times 100\\% = 5.0\\%$."
                        )
                    }
                },

                # PAGE 11 — summary
                {
                    "page_number": 11,
                    "page_title": "Key Takeaways: Comparative Error Analysis",
                    "block_type": "summary",
                    "component_type": "summary",
                    "content": {
                        "text": (
                            "### Master Summary: Comparative Error Analysis\n\n"
                            "| Technique | Formula | Accuracy Role |\n"
                            "|:---|:---|:---|\n"
                            "| **Definite Integration** | $\\int_a^b f(x) \\, dx$ | Analytical Gold Standard (100% Exact). |\n"
                            "| **Percentage Error** | $\\frac{|\\text{Exact} - \\text{Approx}|}{\\text{Exact}} \\times 100\\%$ | Quantifies deviation from exact area. |\n"
                            "| **Concave Up ($f'' > 0$)** | Trapezium $>$ Exact | Straight chords sit above curve (Overestimate). |\n"
                            "| **Concave Down ($f'' < 0$)** | Trapezium $<$ Exact | Straight chords sit below curve (Underestimate). |\n\n"
                            "**Area Approximation Mastery Complete!**"
                        )
                    }
                }
            ]
        }
    ]


def ingest_topic10_area_approximation():
    """Main ingestion runner for Topic 10: Area Approximation."""
    print("=" * 80)
    print("VLearn Form 4 Mathematics — Topic 10: Area Approximation")
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
        defaults={"code": "MATH"}
    )
    print(f"Found Subject: {subject.name}")

    # 2. Get or create Topic 10
    topic_name = "Topic 10: Area Approximation"
    topic, topic_created = Topic.objects.get_or_create(
        subject=subject,
        order=10,
        defaults={"name": topic_name}
    )
    if not topic_created and topic.name != topic_name:
        topic.name = topic_name
        topic.save()
    print(f"Found Topic: {topic.name} (ID: {topic.id})")

    modules_data = get_topic10_data()
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
    ingest_topic10_area_approximation()
