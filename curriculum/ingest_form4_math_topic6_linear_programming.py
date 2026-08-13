#!/usr/bin/env python3
"""
VLearn Form 4 Mathematics — Topic 6: Linear Programming Ingestion Script
========================================================================
Curriculum: 844
Grade: Form 4 (level=1)
Subject: Mathematics
Topic: Topic 6: Linear Programming (order=6)

Modules / LearningUnits:
  6.1 Formulating Linear Inequalities and Systems of Constraints
  6.2 Graphical Representation of Inequalities and the KCSE Feasible Region Shading Convention
  6.3 Optimization via Algebraic Corner-Point Evaluation and Discrete Lattice Solutions
  6.4 Optimization via the Graphical Search-Line (Objective Line / Parallel Ruler) Method

Pedagogical Structure per Lesson: 11 Pages (44 blocks total)
  Page 1:  learning_goal (Student-friendly outcomes)
  Page 2:  concept_explanation (Intuitive real-world analogies: packing limits, sweeping trash, tilted board)
  Page 3:  formula_breakdown / definition_card (Labeled mathematical equations, word translations, strategy tables)
  Page 4:  worked_example (Level 1: Easy / Foundation)
  Page 5:  worked_example (Level 2: Moderate / Multi-step)
  Page 6:  worked_example (Level 3: Difficult / Exam standard)
  Page 7:  worked_example (Level 4: Exam-Style / Real-World Synthesis)
  Page 8:  suggested_simulation (Interactive visual sandbox)
  Page 9:  common_misconception (Diagnostic error analysis & memory tips)
  Page 10: knowledge_check (MCQ / Short-answer with step-by-step solutions)
  Page 11: summary (Key takeaways & optimization checklist)

Standards Enforced:
  - Clean responsive Markdown tables (zero raw \\begin{array} or \\hline).
  - Explicit bold labels on all formula breakdowns.
  - Kenyan KCSE convention: Shading the UNWANTED region, leaving the feasible region clean/white.
  - Rigorous corrections of source typos (e.g. x >= 0 instead of x < 0).
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


def get_topic6_data():
    """Returns the complete structured curriculum payload for Topic 6."""
    return [
        # =====================================================================
        # MODULE 6.1: Formulating Linear Inequalities & Systems of Constraints
        # =====================================================================
        {
            "unit_order": 1,
            "unit_title": "Module 6.1: Formulating Linear Inequalities and Systems of Constraints",
            "lesson_title": "Formulating Linear Inequalities and Systems of Constraints",
            "lesson_blocks": [
                # PAGE 1 — learning_goal
                {
                    "page_number": 1,
                    "page_title": "Mastering Verbal-to-Algebraic Constraint Modeling",
                    "block_type": "learning_goal",
                    "component_type": "learning_goal",
                    "content": {
                        "title": "What You Will Master in This Lesson",
                        "goals": [
                            "Identify independent decision variables ($x$ and $y$) from real-world scenarios.",
                            "Translate verbal resource limits (budgets, capacities, labor hours, minimum outputs) into linear inequalities.",
                            "Formulate non-negativity constraints ($x \\ge 0, y \\ge 0$) representing physical quantities.",
                            "Construct objective functions ($P = ax + by$ or $C = ax + by$) to maximize profit or minimize cost."
                        ]
                    }
                },

                # PAGE 2 — concept_explanation
                {
                    "page_number": 2,
                    "page_title": "The Suitcase Packing Analogy: Why Constraints Are Walls",
                    "block_type": "concept_explanation",
                    "component_type": "concept_explanation",
                    "content": {
                        "body": (
                            "In business, engineering, and everyday life, we want to achieve the best possible result (maximum profit or minimum expense), "
                            "but we are always restricted by real-world limitations: limited budgets, finite machine hours, storage space, and available staff.\n\n"
                            "### The Suitcase Packing Analogy\n\n"
                            "Imagine packing a travel suitcase:\n\n"
                            "- Let $x$ be the number of shirts and $y$ be the number of pairs of shoes.\n"
                            "- **Weight Wall:** Your airline allows a maximum of $20\\text{ kg}$. If a shirt weighs $0.5\\text{ kg}$ and shoes weigh $2\\text{ kg}$, "
                            "the total weight cannot exceed $20\\text{ kg}$: $$0.5x + 2y \\le 20$$\n"
                            "- **Space Wall:** You must pack at least $4$ shirts: $$x \\ge 4$$\n"
                            "- **Physical Reality:** You cannot pack negative items: $$x \\ge 0, \\quad y \\ge 0$$\n\n"
                            "Linear Programming is the mathematics of writing down these 'walls' as linear inequalities, creating a safe zone (feasible region), "
                            "and finding the exact combination of $(x, y)$ that gives the best outcome!"
                        )
                    }
                },

                # PAGE 3 — formula_breakdown
                {
                    "page_number": 3,
                    "page_title": "Master Translation Guide: Verbal Phrases to Algebraic Inequalities",
                    "block_type": "formula_breakdown",
                    "component_type": "formula_breakdown",
                    "content": {
                        "formula": (
                            "**Standard Linear Constraint Format:**\n"
                            "$$a_1 x + b_1 y \\le C \\quad \\text{(Maximum Limit / Ceiling)} \\qquad a_2 x + b_2 y \\ge M \\quad \\text{(Minimum Requirement / Floor)}$$\n\n"
                            "**Linear Objective Function:**\n"
                            "$$\\text{Optimize } z = ax + by \\quad \\text{(Maximize Profit } P \\text{ or Minimize Cost } C\\text{)}$$"
                        ),
                        "content": (
                            "### Key Translation Vocabulary\n\n"
                            "| English Everyday Phrase | Mathematical Symbol | Example Formulation |\n"
                            "|:---|:---:|:---|\n"
                            "| **At most**, **not exceeding**, **maximum of** | $\\le$ | Total cost cannot exceed Sh $18,000 \\implies 30x + 20y \\le 18000$ |\n"
                            "| **At least**, **minimum of**, **not less than** | $\\ge$ | Must transport at least $1000$ bags $\\implies 100x + 25y \\ge 1000$ |\n"
                            "| **Strictly more than**, **greater than** | $>$ | Type Y trips exceed twice Type X trips $\\implies y > 2x$ |\n"
                            "| **Strictly less than**, **under** | $<$ | Combined workers must be under $50 \\implies x + y < 50$ |\n"
                            "| **Non-negativity condition** | $x \\ge 0, y \\ge 0$ | Physical items (buses, shirts, trips) cannot be negative |\n"
                            "| **Comparative ratio** | $y \\ge kx$ | 'At least twice as many $y$ as $x$' $\\implies y \\ge 2x$ |"
                        )
                    }
                },

                # PAGE 4 — worked_example (Level 1: Easy / Basic Manufacturing Constraints)
                {
                    "page_number": 4,
                    "page_title": "Example 1: Formulating Production Constraints for a Bakery",
                    "block_type": "worked_example",
                    "component_type": "worked_example",
                    "content": {
                        "problem": (
                            "A baker produces two types of bread: Brown Bread ($x$) and White Bread ($y$).\n"
                            "- Making one loaf of Brown Bread requires $200\\text{ g}$ of flour and $50\\text{ g}$ of sugar.\n"
                            "- Making one loaf of White Bread requires $300\\text{ g}$ of flour and $20\\text{ g}$ of sugar.\n"
                            "- The baker has $6000\\text{ g}$ of flour and $800\\text{ g}$ of sugar available daily.\n"
                            "- The profit is Sh $15$ on Brown Bread and Sh $20$ on White Bread.\n\n"
                            "Formulate all the linear inequalities and the objective profit function."
                        ),
                        "steps": [
                            "**What we need to formulate:** Decision variables, resource constraints, non-negativity, and objective function.",
                            "**Step 1 — Identify the decision variables:**\n"
                            "Let $x = \\text{number of loaves of Brown Bread}$, $y = \\text{number of loaves of White Bread}$.",
                            "**Step 2 — Write the Flour constraint:**\n"
                            "Total flour consumed cannot exceed the $6000\\text{ g}$ available:\n"
                            "$$200x + 300y \\le 6000$$\n"
                            "Dividing by $100$ simplifies the inequality: **$2x + 3y \\le 60$**.",
                            "**Step 3 — Write the Sugar constraint:**\n"
                            "Total sugar consumed cannot exceed the $800\\text{ g}$ available:\n"
                            "$$50x + 20y \\le 800$$\n"
                            "Dividing by $10$ simplifies the inequality: **$5x + 2y \\le 80$**.",
                            "**Step 4 — State the Non-negativity constraints:**\n"
                            "Physical bread cannot be negative: **$x \\ge 0, \\quad y \\ge 0$**.",
                            "**Step 5 — Write the Objective Profit function:**\n"
                            "$$\\text{Maximize Profit } P = 15x + 20y$$\n\n"
                            "**Answer:** Constraints: $2x + 3y \\le 60$, $5x + 2y \\le 80$, $x \\ge 0$, $y \\ge 0$; Objective: $\\text{Maximize } P = 15x + 20y$."
                        ]
                    }
                },

                # PAGE 5 — worked_example (Level 2: Moderate / Multi-Resource Transport Modeling)
                {
                    "page_number": 5,
                    "page_title": "Example 2: School Bus Transport Hire Inequalities",
                    "block_type": "worked_example",
                    "component_type": "worked_example",
                    "content": {
                        "problem": (
                            "A school needs to transport $384$ students for an educational tour. Two types of buses are available:\n"
                            "- Type X carries $64$ students and costs Sh $25,000$ to hire.\n"
                            "- Type Y carries $48$ students and costs Sh $20,000$ to hire.\n"
                            "- The school must hire at least $7$ buses in total.\n"
                            "Let $x$ be the number of Type X buses and $y$ be the number of Type Y buses.\n"
                            "Write down all inequalities and the objective cost function."
                        ),
                        "steps": [
                            "**What we need to formulate:** System of inequalities and cost objective.",
                            "**Step 1 — Passenger capacity constraint:**\n"
                            "Total seats provided must be at least $384$:\n"
                            "$$64x + 48y \\ge 384$$\n"
                            "Divide by $16$ to simplify:\n"
                            "$$4x + 3y \\ge 24$$",
                            "**Step 2 — Total fleet size constraint:**\n"
                            "At least $7$ buses must be hired combined:\n"
                            "$$x + y \\ge 7$$",
                            "**Step 3 — Non-negativity constraints:**\n"
                            "$$x \\ge 0, \\quad y \\ge 0$$",
                            "**Step 4 — Objective cost function:**\n"
                            "$$\\text{Minimize Cost } C = 25000x + 20000y$$\n\n"
                            "**Answer:** Constraints: $4x + 3y \\ge 24$, $x + y \\ge 7$, $x \\ge 0$, $y \\ge 0$; Objective: $\\text{Minimize } C = 25000x + 20000y$."
                        ]
                    }
                },

                # PAGE 6 — worked_example (Level 3: Difficult / Comparative Ratio & Limit Constraints)
                {
                    "page_number": 6,
                    "page_title": "Example 3: Formulating Cement Logistics with Comparative Trips",
                    "block_type": "worked_example",
                    "component_type": "worked_example",
                    "content": {
                        "problem": (
                            "A contractor transports at least $1000$ bags of cement using a lorry ($x$ trips) and a pickup truck ($y$ trips).\n"
                            "- The lorry carries $100$ bags per trip; the pickup carries $25$ bags per trip.\n"
                            "- The lorry must make at least $7$ trips.\n"
                            "- The pickup must make at least twice as many trips as the lorry.\n"
                            "- The total number of trips made by both vehicles must not exceed $30$.\n"
                            "- The operating cost is Sh $2000$ per lorry trip and Sh $900$ per pickup trip.\n\n"
                            "Formulate all linear inequalities and the cost function."
                        ),
                        "steps": [
                            "**What we need to formulate:** Full inequality system including comparative constraints.",
                            "**Step 1 — Capacity constraint:**\n"
                            "$$100x + 25y \\ge 1000 \\implies 4x + y \\ge 40$$",
                            "**Step 2 — Minimum lorry trips constraint:**\n"
                            "$$x \\ge 7$$",
                            "**Step 3 — Comparative trips constraint:**\n"
                            "'Pickup trips ($y$) must be at least twice the lorry trips ($x$)':\n"
                            "$$y \\ge 2x$$",
                            "**Step 4 — Maximum combined trips constraint:**\n"
                            "'Must not exceed 30 trips':\n"
                            "$$x + y \\le 30$$",
                            "**Step 5 — Non-negativity requirement:**\n"
                            "$$x \\ge 0, \\quad y \\ge 0$$",
                            "**Step 6 — Objective cost function:**\n"
                            "$$\\text{Minimize Cost } C = 2000x + 900y$$\n\n"
                            "**Answer:** $4x + y \\ge 40$, $x \\ge 7$, $y \\ge 2x$, $x + y \\le 30$, $x, y \\ge 0$; $\\text{Minimize } C = 2000x + 900y$."
                        ]
                    }
                },

                # PAGE 7 — worked_example (Level 4: Exam-Style / Compound Multi-Resource Factory)
                {
                    "page_number": 7,
                    "page_title": "Example 4: Factory Production with Raw Materials and Labor Limits",
                    "block_type": "worked_example",
                    "component_type": "worked_example",
                    "content": {
                        "problem": (
                            "A workshop manufactures Red ($x_1$) and Blue ($x_2$) gadgets:\n"
                            "- Red gadgets require $1\\text{ kg}$ steel, $0\\text{ m}$ wood, and $3\\text{ hours}$ labor; sell for Sh $30$ each.\n"
                            "- Blue gadgets require $0\\text{ kg}$ steel, $2\\text{ m}$ wood, and $2\\text{ hours}$ labor; sell for Sh $50$ each.\n"
                            "- Available weekly resources: $50\\text{ kg}$ steel, $120\\text{ m}$ wood, and $180\\text{ hours}$ labor.\n\n"
                            "Formulate the mathematical model to maximize weekly revenue."
                        ),
                        "steps": [
                            "**What we need to formulate:** 3 resource constraints, non-negativity, and revenue objective.",
                            "**Step 1 — Steel resource constraint:**\n"
                            "$$1 \\cdot x_1 + 0 \\cdot x_2 \\le 50 \\implies x_1 \\le 50$$",
                            "**Step 2 — Wood resource constraint:**\n"
                            "$$0 \\cdot x_1 + 2 \\cdot x_2 \\le 120 \\implies 2x_2 \\le 120 \\implies x_2 \\le 60$$",
                            "**Step 3 — Labor hours constraint:**\n"
                            "$$3x_1 + 2x_2 \\le 180$$",
                            "**Step 4 — Non-negativity constraints:**\n"
                            "$$x_1 \\ge 0, \\quad x_2 \\ge 0$$",
                            "**Step 5 — Objective revenue function:**\n"
                            "$$\\text{Maximize Revenue } R = 30x_1 + 50x_2$$\n\n"
                            "**Answer:** Constraints: $x_1 \\le 50$, $x_2 \\le 60$, $3x_1 + 2x_2 \\le 180$, $x_1 \\ge 0$, $x_2 \\ge 0$; Objective: $\\text{Maximize } R = 30x_1 + 50x_2$."
                        ]
                    }
                },

                # PAGE 8 — suggested_simulation
                {
                    "page_number": 8,
                    "page_title": "Explore: The Verbal Constraint Constructor",
                    "block_type": "suggested_simulation",
                    "component_type": "suggested_simulation",
                    "content": {
                        "purpose": (
                            "An interactive constraint-building sandbox where students drag and drop inequality symbols (≤, ≥, <, >) "
                            "to match verbal phrases. The simulator displays instant dynamic feedback, highlighting how changing 'at least' "
                            "to 'at most' flips the inequality direction and alters the physical boundary limits."
                        )
                    },
                    "asset_info": {
                        "asset_type": "simulation",
                        "archetype": "math_verbal_constraint_builder",
                        "title": "Interactive Verbal Constraint Constructor Sandbox"
                    }
                },

                # PAGE 9 — common_misconception
                {
                    "page_number": 9,
                    "page_title": "Common Error: Confusing 'At Least' and 'At Most'",
                    "block_type": "common_misconception",
                    "component_type": "common_misconception",
                    "content": {
                        "text": (
                            "### The Inequality Sign Inversion Error\n\n"
                            "Students frequently confuse **'at least'** and **'at most'**, writing $\\le$ when $\\ge$ is required.\n\n"
                            "### The Memory Translation Key:\n\n"
                            "| Everyday Phrase | Meaning | Correct Symbol | Dangerous Wrong Sign |\n"
                            "|:---|:---|:---:|:---:|\n"
                            "| **At least $10$** | $10$ or more (Floor) | **$\\ge 10$** | $\\le 10$ ❌ |\n"
                            "| **At most $10$** | $10$ or less (Ceiling) | **$\\le 10$** | $\\ge 10$ ❌ |\n"
                            "| **Not more than $10$** | $10$ or less (Ceiling) | **$\\le 10$** | $\\ge 10$ ❌ |\n"
                            "| **Not less than $10$** | $10$ or more (Floor) | **$\\ge 10$** | $\\le 10$ ❌ |\n\n"
                            "> **Memory Tip:** Think of **'at least'** as the minimum grade you need to pass — you want that score or higher ($\\ge$)!"
                        )
                    }
                },

                # PAGE 10 — knowledge_check (MCQ)
                {
                    "page_number": 10,
                    "page_title": "Check Your Understanding: Verbal Formulation",
                    "block_type": "knowledge_check",
                    "component_type": "multiple_choice",
                    "content": {
                        "question": "A hotel requires that the number of chefs ($x$) must be at least twice the number of managers ($y$), and the total staff must not exceed $45$. Which pair of inequalities correctly models this?",
                        "options": [
                            "A: x <= 2y and x + y >= 45",
                            "B: x >= 2y and x + y <= 45",
                            "C: y >= 2x and x + y <= 45",
                            "D: x > 2y and x + y < 45"
                        ],
                        "answer": "B",
                        "explanation": (
                            "1. 'Chefs ($x$) must be at least twice managers ($y$)' $\\implies x \\ge 2y$.\n"
                            "2. 'Total staff must not exceed $45$' $\\implies x + y \\le 45$."
                        )
                    }
                },

                # PAGE 11 — summary
                {
                    "page_number": 11,
                    "page_title": "Key Takeaways: Formulating Linear Constraints",
                    "block_type": "summary",
                    "component_type": "summary",
                    "content": {
                        "text": (
                            "### Master Summary: Constraint Modeling Workflow\n\n"
                            "| Step | Action | Key Check |\n"
                            "|:---|:---|:---|\n"
                            "| **1. Variables** | Define $x$ and $y$ clearly | State units (e.g., $x = \\text{buses}$, $y = \\text{trips}$). |\n"
                            "| **2. Constraints** | Set up inequalities for each resource | Simplify coefficients by dividing by common factors. |\n"
                            "| **3. Non-negativity** | Always include $x \\ge 0, y \\ge 0$ | Physical goods cannot be negative. |\n"
                            "| **4. Objective** | Formulate $P = ax + by$ or $C = ax + by$ | Clearly state whether to Maximize or Minimize. |\n\n"
                            "**Formula Checklist:**\n"
                            "- [x] 'At most' $\\implies \\le$\n"
                            "- [x] 'At least' $\\implies \\ge$\n"
                            "- [x] Always simplify coefficients (e.g. $64x + 48y \\ge 384 \\implies 4x + 3y \\ge 24$)."
                        )
                    }
                }
            ]
        },

        # =====================================================================
        # MODULE 6.2: Feasible Region Construction & KCSE Shading Convention
        # =====================================================================
        {
            "unit_order": 2,
            "unit_title": "Module 6.2: Feasible Region Construction and the KCSE Shading Convention",
            "lesson_title": "Graphical Representation of Inequalities and the KCSE Feasible Region Shading Convention",
            "lesson_blocks": [
                # PAGE 1 — learning_goal
                {
                    "page_number": 1,
                    "page_title": "Mastering Graphical Inequalities & Feasible Regions",
                    "block_type": "learning_goal",
                    "component_type": "learning_goal",
                    "content": {
                        "title": "What You Will Master in This Lesson",
                        "goals": [
                            "Plot straight boundary lines using the double-intercept method ($x=0$ and $y=0$).",
                            "Use test points (e.g., origin $(0,0)$) to determine which half-plane satisfies each inequality.",
                            "Apply the Kenyan KCSE convention of shading the UNWANTED region to leave the feasible region completely white.",
                            "Locate and identify the corner vertices of the bounded/unbounded feasible polygon."
                        ]
                    }
                },

                # PAGE 2 — concept_explanation
                {
                    "page_number": 2,
                    "page_title": "The 'Sweeping the Trash' Analogy: Why We Shade the Unwanted Region",
                    "block_type": "concept_explanation",
                    "component_type": "concept_explanation",
                    "content": {
                        "body": (
                            "When graphing systems of multiple linear inequalities, you divide the Cartesian coordinate plane into valid zones and invalid zones.\n\n"
                            "### The 'Sweeping the Trash' Analogy\n\n"
                            "Imagine cleaning a room with several walls:\n\n"
                            "- If you shade the **wanted** regions, every overlapping constraint layers more dark ink on top of another. "
                            "The result is a dark, messy, unreadable blob where grid lines, coordinates, and intersection vertices disappear!\n"
                            "- In the **Kenyan KCSE standard**, we do the opposite: we **shade the UNWANTED region** (the side of the line that breaks the rule).\n"
                            "- This is like sweeping all the trash out of the room, leaving the **feasible region (R)** as a clean, bright, white polygon in the center where every grid point is crystal clear!"
                        )
                    }
                },

                # PAGE 3 — formula_breakdown
                {
                    "page_number": 3,
                    "page_title": "Master Rules for Line Plotting and KCSE Shading",
                    "block_type": "formula_breakdown",
                    "component_type": "formula_breakdown",
                    "content": {
                        "formula": (
                            "**Double-Intercept Line Formula:**\n"
                            "$$ax + by = c \\implies \\text{When } x = 0, y = \\frac{c}{b} \\quad \\text{and} \\quad \\text{When } y = 0, x = \\frac{c}{a}$$\n\n"
                            "**KCSE Shading Protocol:**\n"
                            "$$\\text{Test Point } (0,0) \\implies \\begin{cases} \\text{If True: Shade the side AWAY from } (0,0) \\\\ \\text{If False: Shade the side CONTAINING } (0,0) \\end{cases}$$"
                        ),
                        "content": (
                            "### Line Styling & Boundary Rules\n\n"
                            "| Inequality Type | Boundary Line Style | Meaning on Boundary | KCSE Shading Action |\n"
                            "|:---|:---:|:---|:---|\n"
                            "| **Non-strict ($\\le$ or $\\ge$)** | **Solid Line** (—) | Points on the line **are included** in solution | Shade unwanted side |\n"
                            "| **Strict ($<$ or $>$)** | **Dashed/Dotted Line** (- - -) | Points on the line **are excluded** from solution | Shade unwanted side |\n"
                            "| **Line through Origin ($y = kx$)** | Passes $(0,0)$ | Cannot test $(0,0)$; test $(1,0)$ or $(0,1)$ instead | Shade unwanted side |\n"
                            "| **Non-negativity ($x \\ge 0, y \\ge 0$)** | Axes ($x=0, y=0$) | Quadrants II, III, IV are invalid | Shade left of $y$-axis & below $x$-axis |"
                        )
                    }
                },

                # PAGE 4 — worked_example (Level 1: Easy / Graphing Single Line and Half-Plane Shading)
                {
                    "page_number": 4,
                    "page_title": "Example 1: Plotting and Shading a Single Linear Inequality",
                    "block_type": "worked_example",
                    "component_type": "worked_example",
                    "content": {
                        "problem": (
                            "On a Cartesian grid, plot the inequality $2x + 3y \\le 12$ by shading the unwanted region."
                        ),
                        "steps": [
                            "**What we need to do:** Find intercepts, plot solid boundary line, test origin, and shade unwanted half-plane.",
                            "**Step 1 — Find the intercepts of the boundary line $2x + 3y = 12$:**\n"
                            "- Set $x = 0 \\implies 3y = 12 \\implies y = 4$. Intercept is $(0, 4)$.\n"
                            "- Set $y = 0 \\implies 2x = 12 \\implies x = 6$. Intercept is $(6, 0)$.",
                            "**Step 2 — Draw the boundary line:**\n"
                            "Since the inequality has '$\\le$', draw a **solid straight line** passing through $(0, 4)$ and $(6, 0)$.",
                            "**Step 3 — Test the origin $(0, 0)$:**\n"
                            "Substitute $(0, 0)$ into $2x + 3y \\le 12$:\n"
                            "$$2(0) + 3(0) = 0 \\le 12 \\quad \\text{(TRUE)}$$\n"
                            "Since the origin $(0,0)$ satisfies the inequality, the region containing $(0,0)$ is **WANTED**.",
                            "**Step 4 — Shade the UNWANTED region:**\n"
                            "Shade the region **above and to the right** of the line $2x + 3y = 12$, leaving the region below clean and white.\n\n"
                            "**Answer:** Solid line through $(0,4)$ and $(6,0)$, with upper right half-plane shaded."
                        ]
                    }
                },

                # PAGE 5 — worked_example (Level 2: Moderate / Boundary Line Passing Through the Origin)
                {
                    "page_number": 5,
                    "page_title": "Example 2: Shading an Origin-Passing Inequality (y ≥ 2x)",
                    "block_type": "worked_example",
                    "component_type": "worked_example",
                    "content": {
                        "problem": (
                            "Represent the inequality $y \\ge 2x$ graphically on the Cartesian plane by shading the unwanted region."
                        ),
                        "steps": [
                            "**What we need to do:** Plot line through origin, select non-origin test point, and shade unwanted half-plane.",
                            "**Step 1 — Plot the boundary line $y = 2x$:**\n"
                            "Generate 3 coordinate points:\n"
                            "- $x = 0 \\implies y = 0 \\implies (0, 0)$\n"
                            "- $x = 2 \\implies y = 4 \\implies (2, 4)$\n"
                            "- $x = 4 \\implies y = 8 \\implies (4, 8)$\n"
                            "Draw a solid straight line through $(0,0)$, $(2,4)$, and $(4,8)$.",
                            "**Step 2 — Select a non-origin test point:**\n"
                            "Since the line passes directly through $(0,0)$, we CANNOT use $(0,0)$ as a test point.\n"
                            "Choose a point clearly off the line, such as $(2, 0)$ on the positive $x$-axis.",
                            "**Step 3 — Test $(2, 0)$ in $y \\ge 2x$:**\n"
                            "$$0 \\ge 2(2) \\implies 0 \\ge 4 \\quad \\text{(FALSE)}$$\n"
                            "Since $(2, 0)$ does NOT satisfy the inequality, the region containing $(2, 0)$ is **UNWANTED**.",
                            "**Step 4 — Shade the UNWANTED region:**\n"
                            "Shade the entire region below/right of the line $y = 2x$, leaving the upper left region clean and white.\n\n"
                            "**Answer:** Solid line through $(0,0)$ and $(2,4)$, with region below the line shaded."
                        ]
                    }
                },

                # PAGE 6 — worked_example (Level 3: Difficult / Constructing a 4-Sided Feasible Region)
                {
                    "page_number": 6,
                    "page_title": "Example 3: Constructing a Feasible Region from a 4-Constraint System",
                    "block_type": "worked_example",
                    "component_type": "worked_example",
                    "content": {
                        "problem": (
                            "Construct the feasible region $R$ by shading the unwanted regions for the system:\n"
                            "$$x + y \\le 8, \\quad 2x + y \\ge 4, \\quad x \\le 5, \\quad y \\ge 0$$\n"
                            "Identify all vertices of the feasible region $R$."
                        ),
                        "steps": [
                            "**What we need to do:** Graph 4 boundary lines, shade unwanted half-planes, and find polygon vertices.",
                            "**Step 1 — Graph and shade $x + y \\le 8$:**\n"
                            "Intercepts: $(0, 8)$ and $(8, 0)$. Test $(0,0) \\implies 0 \\le 8$ (True). Shade above the line.",
                            "**Step 2 — Graph and shade $2x + y \\ge 4$:**\n"
                            "Intercepts: $(0, 4)$ and $(2, 0)$. Test $(0,0) \\implies 0 \\ge 4$ (False). Shade below the line (towards origin).",
                            "**Step 3 — Graph and shade $x \\le 5$ and $y \\ge 0$:**\n"
                            "- Vertical line at $x = 5$: shade to the right ($x > 5$).\n"
                            "- Horizontal line at $y = 0$ ($x$-axis): shade below the $x$-axis ($y < 0$).",
                            "**Step 4 — Determine the vertices of the unshaded feasible region $R$:**\n"
                            "- Vertex 1: $x$-intercept of $2x + y = 4 \\implies (2, 0)$\n"
                            "- Vertex 2: $x$-intercept of $x = 5 \\implies (5, 0)$\n"
                            "- Vertex 3: Intersection of $x = 5$ and $x + y = 8 \\implies (5, 3)$\n"
                            "- Vertex 4: Intersection of $y$-axis ($x=0$) is bounded by $x+y=8$ at $(0,8)$ and $2x+y=4$ at $(0,4)$.\n\n"
                            "**Answer:** Vertices of $R$ are $(0, 4), (2, 0), (5, 0), (5, 3), (0, 8)$."
                        ]
                    }
                },

                # PAGE 7 — worked_example (Level 4: Exam-Style / Full 5-Boundary Feasible Polygon)
                {
                    "page_number": 7,
                    "page_title": "Example 4: Complete KCSE Feasible Region Construction (Gadgets Factory)",
                    "block_type": "worked_example",
                    "component_type": "worked_example",
                    "content": {
                        "problem": (
                            "Graph the following factory constraints and identify the vertices of the unshaded feasible polygon $R$:\n"
                            "$$x_1 \\le 50, \\quad x_2 \\le 60, \\quad 3x_1 + 2x_2 \\le 180, \\quad x_1 \\ge 0, \\quad x_2 \\ge 0$$"
                        ),
                        "steps": [
                            "**What we need to do:** Graph all 5 lines, shade unwanted regions, and find all 5 corner vertices.",
                            "**Step 1 — Boundary Line 1 ($x_1 \\le 50$):**\n"
                            "Draw vertical solid line at $x_1 = 50$. Shade unwanted region to the right ($x_1 > 50$).",
                            "**Step 2 — Boundary Line 2 ($x_2 \\le 60$):**\n"
                            "Draw horizontal solid line at $x_2 = 60$. Shade unwanted region above ($x_2 > 60$).",
                            "**Step 3 — Boundary Line 3 ($3x_1 + 2x_2 \\le 180$):**\n"
                            "Intercepts: $(0, 90)$ and $(60, 0)$. Test $(0,0) \\implies 0 \\le 180$ (True). Shade upper right side.",
                            "**Step 4 — Non-negativity lines ($x_1 \\ge 0, x_2 \\ge 0$):**\n"
                            "Shade left of $x_2$-axis and below $x_1$-axis.",
                            "**Step 5 — Find all corner vertices of $R$ algebraically:**\n"
                            "- Vertex 1: Origin $(0, 0)$\n"
                            "- Vertex 2: $(0, 60)$\n"
                            "- Vertex 3: Intersection of $x_2 = 60$ and $3x_1 + 2x_2 = 180 \\implies 3x_1 + 120 = 180 \\implies x_1 = 20 \\implies (20, 60)$\n"
                            "- Vertex 4: Intersection of $x_1 = 50$ and $3x_1 + 2x_2 = 180 \\implies 150 + 2x_2 = 180 \\implies x_2 = 15 \\implies (50, 15)$\n"
                            "- Vertex 5: $(50, 0)$\n\n"
                            "**Answer:** Feasible polygon vertices are $(0,0), (0,60), (20,60), (50,15), (50,0)$."
                        ]
                    }
                },

                # PAGE 8 — suggested_simulation
                {
                    "page_number": 8,
                    "page_title": "Explore: 2D Feasible Region & Shading Sandbox",
                    "block_type": "suggested_simulation",
                    "component_type": "suggested_simulation",
                    "content": {
                        "purpose": (
                            "An interactive 2D Cartesian graphing sandbox where students can toggle individual linear inequality boundaries, "
                            "switch between 'Shade Wanted' and 'KCSE Shade Unwanted' modes, and hover over vertices to view exact algebraic coordinates."
                        )
                    },
                    "asset_info": {
                        "asset_type": "simulation",
                        "archetype": "math_feasible_region_shading_explorer",
                        "title": "Interactive Feasible Region & Shading Sandbox"
                    }
                },

                # PAGE 9 — common_misconception
                {
                    "page_number": 9,
                    "page_title": "Common Error: Shading the Wanted Side in KCSE",
                    "block_type": "common_misconception",
                    "component_type": "common_misconception",
                    "content": {
                        "text": (
                            "### The Ink Overload Error\n\n"
                            "In some international textbooks, students shade the *true* half-plane. In KCSE national exams, this results in **zero marks for the graphical region**.\n\n"
                            "### Why KCSE Requires Shading the UNWANTED Region:\n\n"
                            "| Method | Result of 4 Overlapping Constraints | Usability for Optimization |\n"
                            "|:---|:---|:---|\n"
                            "| **Shading Wanted** | Dark overlapping ink blot | Unusable — cannot see grid lines or vertices ❌ |\n"
                            "| **KCSE Shading Unwanted** | Clean white polygon in center | Perfect — grid coordinates and vertices are crystal clear ✓ |\n\n"
                            "> **Rule of Thumb:** Always shade out the side that violates the rule, leaving the valid feasible region clean and unshaded!"
                        )
                    }
                },

                # PAGE 10 — knowledge_check (MCQ)
                {
                    "page_number": 10,
                    "page_title": "Check Your Understanding: Shading Convention",
                    "block_type": "knowledge_check",
                    "component_type": "multiple_choice",
                    "content": {
                        "question": "When graphing $x + y \\ge 6$ under the KCSE convention, which region should you shade?",
                        "options": [
                            "A: The region above the line (containing (10, 10))",
                            "B: The region below the line (containing the origin (0, 0))",
                            "C: The boundary line itself",
                            "D: Both sides of the line"
                        ],
                        "answer": "B",
                        "explanation": (
                            "1. Test the origin $(0, 0)$: $0 + 0 = 0 \\ge 6$ is FALSE.\n"
                            "2. Under KCSE rules, we shade the UNWANTED region. Since $(0, 0)$ is false, we shade the region below the line containing $(0, 0)$."
                        )
                    }
                },

                # PAGE 11 — summary
                {
                    "page_number": 11,
                    "page_title": "Key Takeaways: Feasible Region Construction",
                    "block_type": "summary",
                    "component_type": "summary",
                    "content": {
                        "text": (
                            "### Master Summary: Graphical Feasible Regions\n\n"
                            "| Step | Action | Common Pitfall |\n"
                            "|:---|:---|:---|\n"
                            "| **1. Intercepts** | Calculate $(0, c/b)$ and $(c/a, 0)$ | Dividing by wrong coefficient. |\n"
                            "| **2. Boundary Line** | Solid for $\\le, \\ge$; Dotted for $<, >$ | Using solid line for strict inequality. |\n"
                            "| **3. Test Point** | Use $(0,0)$ or $(1,0)$ for origin lines | Testing $(0,0)$ when line passes $(0,0)$. |\n"
                            "| **4. KCSE Shading** | Shade the UNWANTED side | Shading wanted side by mistake. |\n"
                            "| **5. Feasible Polygon** | Label clean white region $R$ | Forgetting non-negativity axes boundaries. |\n\n"
                            "**Checklist for KCSE Full Marks:**\n"
                            "- [x] All axes clearly scaled and labeled.\n"
                            "- [x] All boundary equations written along lines.\n"
                            "- [x] Feasible region $R$ left completely unshaded."
                        )
                    }
                }
            ]
        },

        # =====================================================================
        # MODULE 6.3: Optimization via Algebraic Corner-Point Evaluation
        # =====================================================================
        {
            "unit_order": 3,
            "unit_title": "Module 6.3: Optimization via Algebraic Corner-Point Evaluation",
            "lesson_title": "Optimization via Algebraic Corner-Point Evaluation and Discrete Lattice Solutions",
            "lesson_blocks": [
                # PAGE 1 — learning_goal
                {
                    "page_number": 1,
                    "page_title": "Mastering Corner-Point Optimization & Discrete Coordinates",
                    "block_type": "learning_goal",
                    "component_type": "learning_goal",
                    "content": {
                        "title": "What You Will Master in This Lesson",
                        "goals": [
                            "Apply the Fundamental Theorem of Linear Programming: optimal solutions always lie at feasible vertices.",
                            "Solve simultaneous linear equations to determine the exact coordinates of corner vertices.",
                            "Evaluate the objective function ($P = ax + by$ or $C = ax + by$) in a structured corner-point comparison table.",
                            "Identify integer lattice points inside the feasible region when decision variables represent discrete items."
                        ]
                    }
                },

                # PAGE 2 — concept_explanation
                {
                    "page_number": 2,
                    "page_title": "The Mountain Peak Analogy: Why the Best Point is Always at a Corner",
                    "block_type": "concept_explanation",
                    "component_type": "concept_explanation",
                    "content": {
                        "body": (
                            "Why don't we have to test every single one of the infinite points inside the feasible region to find the maximum profit?\n\n"
                            "### The Fundamental Theorem of Linear Programming\n\n"
                            "Because both the objective function ($P = ax + by$) and the constraint boundaries are straight lines, "
                            "the profit surface is a flat, tilted plane.\n\n"
                            "- Imagine walking on a tilted roof: the highest and lowest points are never in the middle of a flat roof section — they are always at the **outer corners (vertices)**!\n"
                            "- Therefore, we only need to test the **corners of the unshaded feasible polygon**.\n\n"
                            "### The Discrete Integer Challenge\n\n"
                            "In real life, you cannot hire $3.4$ buses or make $7.8$ lorry trips. When an optimal vertex has decimal coordinates, "
                            "we inspect the nearby **integer lattice coordinates** that lie strictly inside the unshaded feasible region."
                        )
                    }
                },

                # PAGE 3 — formula_breakdown
                {
                    "page_number": 3,
                    "page_title": "Master Workflow for Algebraic Corner-Point Optimization",
                    "block_type": "formula_breakdown",
                    "component_type": "formula_breakdown",
                    "content": {
                        "formula": (
                            "**Linear Objective Evaluation:**\n"
                            "$$P(x_i, y_i) = ax_i + by_i \\quad \\text{for each vertex } (x_i, y_i) \\in R$$\n\n"
                            "**Simultaneous Intersection Solver:**\n"
                            "$$\\begin{cases} a_1 x + b_1 y = c_1 \\\\ a_2 x + b_2 y = c_2 \\end{cases} \\implies (x_{\\text{vertex}}, y_{\\text{vertex}})$$",
                        ),
                        "content": (
                            "### 4-Step Corner-Point Optimization Sequence\n\n"
                            "1. **Identify all polygon vertices:** Find the coordinates of all intersection corners bounding the unshaded region $R$.\n"
                            "2. **Solve intersecting lines algebraically:** If a vertex is not directly on an axis intercept, solve the two intersecting boundary equations simultaneously.\n"
                            "3. **Compile the comparison table:** Substitute each vertex $(x, y)$ into the objective function ($P = ax + by$ or $C = ax + by$).\n"
                            "4. **Select the optimum:**\n"
                            "   - For **Maximization:** Choose the vertex giving the **largest** value.\n"
                            "   - For **Minimization:** Choose the vertex giving the **smallest** value."
                        )
                    }
                },

                # PAGE 4 — worked_example (Level 1: Easy / Revenue Maximization with 3 Vertices)
                {
                    "page_number": 4,
                    "page_title": "Example 1: Maximizing Profit on a Simple Bounded Polygon",
                    "block_type": "worked_example",
                    "component_type": "worked_example",
                    "content": {
                        "problem": (
                            "A feasible region $R$ is bounded by vertices $A(0, 0)$, $B(0, 4)$, $C(3, 2)$, and $D(4, 0)$.\n"
                            "Find the maximum value of the objective profit function $P = 40x + 30y$."
                        ),
                        "steps": [
                            "**What we need to find:** The maximum value of $P$ across the given vertices.",
                            "**Step 1 — List all corner vertices:**\n"
                            "Vertices are $A(0, 0)$, $B(0, 4)$, $C(3, 2)$, $D(4, 0)$.",
                            "**Step 2 — Evaluate $P = 40x + 30y$ at each vertex:**\n"
                            "- $P(A) = 40(0) + 30(0) = 0$\n"
                            "- $P(B) = 40(0) + 30(4) = 120$\n"
                            "- $P(C) = 40(3) + 30(2) = 120 + 60 = 180$ (Maximum!)\n"
                            "- $P(D) = 40(4) + 30(0) = 160$",
                            "**Step 3 — Identify the optimal point:**\n"
                            "The maximum profit is **$180$**, occurring at point **$(3, 2)$**.\n\n"
                            "**Answer:** Maximum profit is $180$ at $x = 3, y = 2$."
                        ]
                    }
                },

                # PAGE 5 — worked_example (Level 2: Moderate / School Bus Cost Minimization)
                {
                    "page_number": 5,
                    "page_title": "Example 2: School Tour Bus Hire Optimization",
                    "block_type": "worked_example",
                    "component_type": "worked_example",
                    "content": {
                        "problem": (
                            "A school transports $384$ students using Type X ($64$ seats, Sh $25,000$) and Type Y ($48$ seats, Sh $20,000$) buses.\n"
                            "Constraints: $4x + 3y \\ge 24$, $x + y \\ge 7$, $x \\ge 0$, $y \\ge 0$.\n"
                            "Find the number of buses of each type to minimize the total hire cost $C = 25000x + 20000y$."
                        ),
                        "steps": [
                            "**What we need to find:** Minimum cost and optimal combination of $(x, y)$.",
                            "**Step 1 — Solve the intersection vertex of the two boundary lines:**\n"
                            "$$\\begin{cases} 4x + 3y = 24 \\\\ x + y = 7 \\implies x = 7 - y \\end{cases}$$\n"
                            "Substitute into equation 1:\n"
                            "$$4(7 - y) + 3y = 24 \\implies 28 - 4y + 3y = 24 \\implies y = 4$$\n"
                            "$$x = 7 - 4 = 3 \\implies \\text{Intersection Vertex is } (3, 4)$$",
                            "**Step 2 — Identify all corner vertices of the feasible region:**\n"
                            "- Vertex 1: $y$-intercept of $4x + 3y = 24 \\implies (0, 8)$ (since $0 + 8 = 8 \\ge 7$)\n"
                            "- Vertex 2: Intersection point $(3, 4)$\n"
                            "- Vertex 3: $x$-intercept of $x + y = 7 \\implies (7, 0)$ (since $4(7) + 3(0) = 28 \\ge 24$)",
                            "**Step 3 — Substitute vertices into the cost function $C = 25000x + 20000y$:**\n"
                            "- $C(0, 8) = 25000(0) + 20000(8) = \\text{Sh } 160,000$\n"
                            "- $C(3, 4) = 25000(3) + 20000(4) = 75000 + 80000 = \\text{Sh } 155,000$ (Minimum!)\n"
                            "- $C(7, 0) = 25000(7) + 20000(0) = \\text{Sh } 175,000$\n\n"
                            "**Answer:** Hire $3$ Type X buses and $4$ Type Y buses for a minimum cost of Sh $155,000$."
                        ]
                    }
                },

                # PAGE 6 — worked_example (Level 3: Difficult / Discrete Integer Lattice Optimization)
                {
                    "page_number": 6,
                    "page_title": "Example 3: Discrete Cement Transport Optimization",
                    "block_type": "worked_example",
                    "component_type": "worked_example",
                    "content": {
                        "problem": (
                            "A contractor transports cement using a lorry ($x$) and pickup ($y$) under constraints:\n"
                            "$$4x + y \\ge 40, \\quad x \\ge 7, \\quad y \\ge 2x, \\quad x + y \\le 30$$\n"
                            "Cost function: $C = 2000x + 900y$.\n"
                            "Because trips must be integers, evaluate the feasible lattice points to find the minimum cost."
                        ),
                        "steps": [
                            "**What we need to find:** Integer coordinate pair $(x, y)$ that minimizes $C = 2000x + 900y$.",
                            "**Step 1 — Identify the discrete integer points inside the unshaded feasible zone:**\n"
                            "From the intersection of $x \\ge 7, y \\ge 2x, 4x+y \\ge 40, x+y \\le 30$, the feasible integer points are:\n"
                            "$$(7, 22), \\quad (8, 18), \\quad (8, 19), \\quad (8, 20), \\quad (8, 21), \\quad (9, 19), \\quad (9, 20)$$",
                            "**Step 2 — Calculate cost for each candidate:**\n"
                            "- $C(7, 22) = 2000(7) + 900(22) = 14000 + 19800 = \\text{Sh } 33,800$\n"
                            "- $C(8, 18) = 2000(8) + 900(18) = 16000 + 16200 = \\text{Sh } 32,200$ (Cheapest!)\n"
                            "- $C(8, 19) = 2000(8) + 900(19) = 16000 + 17100 = \\text{Sh } 33,100$\n"
                            "- $C(8, 20) = 2000(8) + 900(20) = 16000 + 18000 = \\text{Sh } 34,000$\n"
                            "- $C(8, 21) = 2000(8) + 900(21) = 16000 + 18900 = \\text{Sh } 34,900$\n"
                            "- $C(9, 19) = 2000(9) + 900(19) = 18000 + 17100 = \\text{Sh } 35,100$\n"
                            "- $C(9, 20) = 2000(9) + 900(20) = 18000 + 18000 = \\text{Sh } 36,000$",
                            "**Step 3 — State the optimal solution:**\n"
                            "Minimum cost is **Sh $32,200$** achieved with **$8$ lorry trips** and **$18$ pickup trips**.\n\n"
                            "**Answer:** $8$ lorry trips and $18$ pickup trips for a minimum cost of Sh $32,200$."
                        ]
                    }
                },

                # PAGE 7 — worked_example (Level 4: Exam-Style / Full 5-Vertex Revenue Maximization)
                {
                    "page_number": 7,
                    "page_title": "Example 4: Factory Revenue Maximization (Steel & Wood Gadgets)",
                    "block_type": "worked_example",
                    "component_type": "worked_example",
                    "content": {
                        "problem": (
                            "Maximize weekly revenue $R = 30x_1 + 50x_2$ across the feasible polygon vertices:\n"
                            "$$(0, 0), \\quad (0, 60), \\quad (20, 60), \\quad (50, 15), \\quad (50, 0)$$"
                        ),
                        "steps": [
                            "**What we need to calculate:** Revenue at all 5 vertices and select maximum.",
                            "**Step 1 — Substitute each vertex into $R = 30x_1 + 50x_2$:**\n"
                            "- $R(0, 0) = 30(0) + 50(0) = \\text{Sh } 0$\n"
                            "- $R(0, 60) = 30(0) + 50(60) = \\text{Sh } 3,000$\n"
                            "- $R(20, 60) = 30(20) + 50(60) = 600 + 3000 = \\text{Sh } 3,600$ (Maximum!)\n"
                            "- $R(50, 15) = 30(50) + 50(15) = 1500 + 750 = \\text{Sh } 2,250$\n"
                            "- $R(50, 0) = 30(50) + 50(0) = \\text{Sh } 1,500$",
                            "**Step 2 — Verify resource feasibility at optimal point $(20, 60)$:**\n"
                            "- Steel used: $1(20) = 20\\text{ kg} \\le 50\\text{ kg}$ (Feasible)\n"
                            "- Wood used: $2(60) = 120\\text{ m} \\le 120\\text{ m}$ (Feasible)\n"
                            "- Labor used: $3(20) + 2(60) = 60 + 120 = 180\\text{ hours} \\le 180\\text{ hours}$ (Feasible)\n\n"
                            "**Answer:** Produce $20$ Red gadgets and $60$ Blue gadgets for a maximum revenue of Sh $3,600$."
                        ]
                    }
                },

                # PAGE 8 — suggested_simulation
                {
                    "page_number": 8,
                    "page_title": "Explore: Corner-Point Evaluator Sandbox",
                    "block_type": "suggested_simulation",
                    "component_type": "suggested_simulation",
                    "content": {
                        "purpose": (
                            "An interactive optimization sandbox where students can click any corner vertex of a feasible polygon "
                            "to see instant step-by-step arithmetic substitution into the objective equation, complete with an active leaderboard "
                            "ranking all corners from best to worst."
                        )
                    },
                    "asset_info": {
                        "asset_type": "simulation",
                        "archetype": "math_corner_point_evaluator",
                        "title": "Interactive Corner-Point Evaluator Sandbox"
                    }
                },

                # PAGE 9 — common_misconception
                {
                    "page_number": 9,
                    "page_title": "Common Error: Blind Decimal Rounding",
                    "block_type": "common_misconception",
                    "component_type": "common_misconception",
                    "content": {
                        "text": (
                            "### The Infeasible Rounding Trap\n\n"
                            "If the theoretical continuous optimal vertex is $(5.4, 2.8)$, students often blindly round up to $(5, 3)$.\n\n"
                            "### Why Blind Rounding Fails:\n"
                            "- Rounding $(5.4, 2.8)$ to $(5, 3)$ might push the point **outside the feasible region**, violating a critical capacity constraint!\n"
                            "- You must always test the nearby integer points: $(5, 2), (5, 3), (6, 2)$ against **all** inequality constraints to verify they are feasible before evaluating profit.\n\n"
                            "> **Memory Tip:** A point is only a valid solution if it lies **inside the white unshaded zone**!"
                        )
                    }
                },

                # PAGE 10 — knowledge_check (MCQ)
                {
                    "page_number": 10,
                    "page_title": "Check Your Understanding: Corner-Point Optimization",
                    "block_type": "knowledge_check",
                    "component_type": "multiple_choice",
                    "content": {
                        "question": "A profit function is $P = 50x + 80y$. The feasible vertices are $(0, 0)$, $(0, 5)$, $(4, 3)$, and $(6, 0)$. Which vertex yields the maximum profit?",
                        "options": [
                            "A: (0, 5) with P = 400",
                            "B: (6, 0) with P = 300",
                            "C: (4, 3) with P = 440",
                            "D: (0, 0) with P = 0"
                        ],
                        "answer": "C",
                        "explanation": (
                            "1. $P(0, 5) = 50(0) + 80(5) = 400$.\n"
                            "2. $P(4, 3) = 50(4) + 80(3) = 200 + 240 = 440$.\n"
                            "3. $P(6, 0) = 50(6) + 80(0) = 300$.\n"
                            "4. Maximum is $440$ at $(4, 3)$."
                        )
                    }
                },

                # PAGE 11 — summary
                {
                    "page_number": 11,
                    "page_title": "Key Takeaways: Corner-Point Optimization",
                    "block_type": "summary",
                    "component_type": "summary",
                    "content": {
                        "text": (
                            "### Master Summary: Corner-Point Method\n\n"
                            "| Procedure | Formula / Tool | Goal |\n"
                            "|:---|:---|:---|\n"
                            "| **1. Find Corners** | Simultaneous equations | Get exact $(x, y)$ of all boundary intersections. |\n"
                            "| **2. Test Table** | $P = ax + by$ or $C = ax + by$ | Compute numerical value for each vertex. |\n"
                            "| **3. Select Best** | Highest $P$ / Lowest $C$ | Identify the optimal operational configuration. |\n"
                            "| **4. Check Integers** | Verify integer feasibility | Required for discrete items (buses, trips, people). |\n\n"
                            "**Key Insight:** You never need to test points inside the interior of the polygon — the optimal answer is guaranteed to be on the boundary corners!"
                        )
                    }
                }
            ]
        },

        # =====================================================================
        # MODULE 6.4: Optimization via the Graphical Search-Line Method
        # =====================================================================
        {
            "unit_order": 4,
            "unit_title": "Module 6.4: Optimization via the Graphical Search-Line Method",
            "lesson_title": "Optimization via the Graphical Search-Line (Objective Line) Method",
            "lesson_blocks": [
                # PAGE 1 — learning_goal
                {
                    "page_number": 1,
                    "page_title": "Mastering the Search-Line (Parallel Ruler) Method",
                    "block_type": "learning_goal",
                    "component_type": "learning_goal",
                    "content": {
                        "title": "What You Will Master in This Lesson",
                        "goals": [
                            "Formulate a trial search-line equation $ax + by = k$ by selecting a convenient constant $k = \\text{LCM}(a, b)$.",
                            "Calculate the constant gradient $m = -\\frac{a}{b}$ of the objective function family.",
                            "Slide a parallel ruler across the feasible region to identify extreme contact points (first contact $\\implies$ minimum, last contact $\\implies$ maximum).",
                            "Recognize parallel boundary cases with infinite optimal solutions along a segment."
                        ]
                    }
                },

                # PAGE 2 — concept_explanation
                {
                    "page_number": 2,
                    "page_title": "The Tilted Board Analogy: How Parallel Sliding Finds the Optimum",
                    "block_type": "concept_explanation",
                    "component_type": "concept_explanation",
                    "content": {
                        "body": (
                            "The **Search-Line Method** (also called the *Objective Line* or *Parallel Ruler* method) is a fast graphical technique "
                            "that finds the optimal point without testing every corner algebraically.\n\n"
                            "### The Tilted Board Analogy\n\n"
                            "Imagine the objective function $P = ax + by$ as a flat, tilted board held at a fixed slope:\n\n"
                            "- Every parallel line $ax + by = k$ represents a line of constant profit on this board.\n"
                            "- As you push the board across the unshaded feasible region (the floor):\n"
                            "  - **For Minimization:** The **very first point** of the white region the ruler touches is the minimum cost point!\n"
                            "  - **For Maximization:** The **absolute last point** the ruler touches before leaving the white region completely is the maximum profit point!\n\n"
                            "This gives an instant visual confirmation of the optimal solution."
                        )
                    }
                },

                # PAGE 3 — formula_breakdown
                {
                    "page_number": 3,
                    "page_title": "Master Rules for Constructing and Sliding the Search-Line",
                    "block_type": "formula_breakdown",
                    "component_type": "formula_breakdown",
                    "content": {
                        "formula": (
                            "**Search-Line Equation Template:**\n"
                            "$$ax + by = k_{\\text{trial}} \\quad \\text{where } k_{\\text{trial}} = \\text{LCM}(a, b)$$\n\n"
                            "**Search-Line Constant Gradient:**\n"
                            "$$m = -\\frac{a}{b} \\quad \\text{(Slope remains constant during parallel sliding)}$$"
                        ),
                        "content": (
                            "### 4-Step Search-Line Protocol\n\n"
                            "1. **Set a baseline trial constant ($k$):** Choose $k = a \\times b$ (or their LCM) so that the $x$-intercept $(k/a, 0)$ and $y$-intercept $(0, k/b)$ are clean, easy-to-plot integers.\n"
                            "2. **Draw the trial line:** Plot the line with a dotted/dashed line and label it as the search line ($l_1$).\n"
                            "3. **Position your parallel ruler:** Align a ruler along $l_1$ and slide it parallel in the direction of increasing or decreasing objective value.\n"
                            "4. **Identify the optimal contact point:**\n"
                            "   - **Minimum:** First feasible coordinate touched.\n"
                            "   - **Maximum:** Last feasible coordinate touched before leaving region $R$."
                        )
                    }
                },

                # PAGE 4 — worked_example (Level 1: Easy / Choosing k and Drawing the Baseline)
                {
                    "page_number": 4,
                    "page_title": "Example 1: Formulating and Plotting a Trial Search-Line",
                    "block_type": "worked_example",
                    "component_type": "worked_example",
                    "content": {
                        "problem": (
                            "Given an objective profit function $P = 30x + 50y$:\n"
                            "(a) Choose a suitable trial constant $k$ to draw a baseline search line.\n"
                            "(b) Find its $x$- and $y$-intercepts and state its gradient."
                        ),
                        "steps": [
                            "**What we need to find:** Trial constant $k$, intercepts, and slope.",
                            "**Step 1 — Simplify the coefficient ratio:**\n"
                            "Divide coefficients by $10 \\implies 3x + 5y$.",
                            "**Step 2 — Choose trial constant $k$ using LCM:**\n"
                            "$$\\text{LCM}(3, 5) = 15 \\implies 3x + 5y = 15 \\quad (\\text{or } 30x + 50y = 1500)$$",
                            "**Step 3 — Find the intercepts of $3x + 5y = 15$:**\n"
                            "- When $y = 0 \\implies 3x = 15 \\implies x = 5$. Intercept is $(5, 0)$.\n"
                            "- When $x = 0 \\implies 5y = 15 \\implies y = 3$. Intercept is $(0, 3)$.",
                            "**Step 4 — Calculate the gradient $m$:**\n"
                            "$$5y = -3x + 15 \\implies y = -\\frac{3}{5}x + 3 \\implies m = -\\frac{3}{5} = -0.6$$\n\n"
                            "**Answer:** Trial line is $3x + 5y = 15$ through $(5, 0)$ and $(0, 3)$, with gradient $m = -0.6$."
                        ]
                    }
                },

                # PAGE 5 — worked_example (Level 2: Moderate / Search-Line Minimization for Bus Transport)
                {
                    "page_number": 5,
                    "page_title": "Example 2: Minimizing Transport Cost via Parallel Sliding",
                    "block_type": "worked_example",
                    "component_type": "worked_example",
                    "content": {
                        "problem": (
                            "Use the search-line method to minimize $C = 25000x + 20000y$ over the feasible region bounded by vertices $(0, 8)$, $(3, 4)$, and $(7, 0)$."
                        ),
                        "steps": [
                            "**What we need to do:** Set up search line, determine direction of sliding, and identify the first contact point.",
                            "**Step 1 — Simplify the objective ratio:**\n"
                            "$$\\frac{25000}{5000}x + \\frac{20000}{5000}y = 5x + 4y$$",
                            "**Step 2 — Draw trial search line:**\n"
                            "Set $5x + 4y = 20 \\implies$ Intercepts are $(4, 0)$ and $(0, 5)$. Draw as dotted line $l_1$.",
                            "**Step 3 — Slide the parallel ruler into the feasible region:**\n"
                            "Since the feasible region lies in the upper right, slide the ruler outward from the origin toward increasing $x$ and $y$.\n"
                            "- The **very first vertex** the sliding ruler touches is **$(3, 4)$**.",
                            "**Step 4 — Evaluate minimum cost at $(3, 4)$:**\n"
                            "$$C = 25000(3) + 20000(4) = 75000 + 80000 = \\text{Sh } 155,000$$\n\n"
                            "**Answer:** Optimal minimum point is $(3, 4)$ with cost Sh $155,000$."
                        ]
                    }
                },

                # PAGE 6 — worked_example (Level 3: Difficult / Search-Line on Discrete Integer Grid)
                {
                    "page_number": 6,
                    "page_title": "Example 3: Search-Line Optimization on a Discrete Cement Grid",
                    "block_type": "worked_example",
                    "component_type": "worked_example",
                    "content": {
                        "problem": (
                            "Minimize cost $C = 2000x + 900y$ over the cement transport feasible region using the search-line method."
                        ),
                        "steps": [
                            "**What we need to do:** Construct search line with slope $-20/9$ and slide it to find the first integer point touched.",
                            "**Step 1 — Formulate trial search line:**\n"
                            "Divide coefficients by $100 \\implies 20x + 9y$.\n"
                            "Set trial line: $20x + 9y = 180$. Intercepts are $(9, 0)$ and $(0, 20)$.",
                            "**Step 2 — Calculate slope:**\n"
                            "$$m = -\\frac{20}{9} \\approx -2.22$$",
                            "**Step 3 — Slide parallel ruler into the feasible region:**\n"
                            "Slide the ruler parallel to $20x + 9y = 180$ into the unshaded feasible region.\n"
                            "The very first integer coordinate touched by the sliding ruler is **$(8, 18)$**.",
                            "**Step 4 — Compute minimum cost:**\n"
                            "$$C = 2000(8) + 900(18) = 16000 + 16200 = \\text{Sh } 32,200$$\n\n"
                            "**Answer:** Optimal discrete solution is $x = 8, y = 18$ with minimum cost Sh $32,200$."
                        ]
                    }
                },

                # PAGE 7 — worked_example (Level 4: Exam-Style / Full 10-Mark KCSE Synthesis)
                {
                    "page_number": 7,
                    "page_title": "Example 4: Complete KCSE Exam Synthesis with Economic Change",
                    "block_type": "worked_example",
                    "component_type": "worked_example",
                    "content": {
                        "problem": (
                            "A factory produces gadgets under constraints: $x_1 \\le 50$, $x_2 \\le 60$, $3x_1 + 2x_2 \\le 180$, $x_1, x_2 \\ge 0$.\n"
                            "(a) Use a search line to find the maximum weekly revenue under $R_1 = 30x_1 + 50x_2$.\n"
                            "(b) If the market price changes so that the revenue becomes $R_2 = 60x_1 + 40x_2$, use the search line method to find the new optimal production plan."
                        ),
                        "steps": [
                            "**What we need to do:** Apply search line under two different objective slopes and compare results.",
                            "**Step 1 — Part (a): Search Line for $R_1 = 30x_1 + 50x_2$:**\n"
                            "- Slope: $m_1 = -\\frac{30}{50} = -0.6$.\n"
                            "- Sliding ruler to the upper right: the last point touched before exiting the region is **$(20, 60)$**.\n"
                            "- Maximum Revenue $R_1 = 30(20) + 50(60) = \\text{Sh } 3,600$.",
                            "**Step 2 — Part (b): Search Line for $R_2 = 60x_1 + 40x_2$:**\n"
                            "- Simplify ratio: $3x_1 + 2x_2$.\n"
                            "- Slope: $m_2 = -\\frac{60}{40} = -1.5$.\n"
                            "- Notice that the slope $m_2 = -1.5$ is **identical** to the slope of the labor constraint boundary line $3x_1 + 2x_2 = 180$!\n"
                            "- When the search line is parallel to a boundary edge, **every point along that boundary segment** is optimal!",
                            "**Step 3 — Evaluate the two boundary segment endpoints:**\n"
                            "- At $(20, 60)$: $R_2 = 60(20) + 40(60) = 1200 + 2400 = \\text{Sh } 3,600$.\n"
                            "- At $(50, 15)$: $R_2 = 60(50) + 40(15) = 3000 + 600 = \\text{Sh } 3,600$.\n\n"
                            "**Answer:** (a) $(20, 60)$ with $R_1 = \\text{Sh } 3,600$; (b) Any integer point along the segment from $(20, 60)$ to $(50, 15)$ gives maximum revenue Sh $3,600$."
                        ]
                    }
                },

                # PAGE 8 — suggested_simulation
                {
                    "page_number": 8,
                    "page_title": "Explore: The Interactive Parallel Ruler Sandbox",
                    "block_type": "suggested_simulation",
                    "component_type": "suggested_simulation",
                    "content": {
                        "purpose": (
                            "An interactive parallel ruler simulator where students can grab and drag a dotted objective line across "
                            "a 2D feasible region. The simulator displays dynamic slope readouts ($m = -a/b$), snaps to extreme contact vertices, "
                            "and visually proves how changing the objective coefficients tilts the search line to select different optimal corners."
                        )
                    },
                    "asset_info": {
                        "asset_type": "simulation",
                        "archetype": "math_search_line_parallel_ruler",
                        "title": "Interactive Parallel Ruler Sandbox"
                    }
                },

                # PAGE 9 — common_misconception
                {
                    "page_number": 9,
                    "page_title": "Common Error: Sliding in the Wrong Direction",
                    "block_type": "common_misconception",
                    "component_type": "common_misconception",
                    "content": {
                        "text": (
                            "### The Optimization Direction Inversion\n\n"
                            "Students often confuse which extreme contact point represents the maximum versus the minimum.\n\n"
                            "### The Golden Sliding Rule:\n\n"
                            "| Optimization Goal | Ruler Movement Direction | Optimal Contact Point |\n"
                            "|:---|:---|:---|\n"
                            "| **Minimization (Cost/Loss)** | Moving from origin *into* region | **FIRST point touched** enters feasible zone ✓ |\n"
                            "| **Maximization (Profit/Revenue)** | Moving from origin *through* region | **LAST point touched** before exiting region ✓ |\n\n"
                            "> **Memory Tip:** You want to pay the minimum immediately (first touch), but stretch your profit as far as possible (last touch)!"
                        )
                    }
                },

                # PAGE 10 — knowledge_check (MCQ)
                {
                    "page_number": 10,
                    "page_title": "Check Your Understanding: Search-Line Method",
                    "block_type": "knowledge_check",
                    "component_type": "multiple_choice",
                    "content": {
                        "question": "What is the gradient of the search line for the objective function $P = 4x + 6y$?",
                        "options": [
                            "A: -2/3",
                            "B: -3/2",
                            "C: 2/3",
                            "D: 4/6"
                        ],
                        "answer": "A",
                        "explanation": (
                            "1. Rearrange $4x + 6y = k$ into slope-intercept form $y = mx + c$:\n"
                            "2. $6y = -4x + k \\implies y = -\\frac{4}{6}x + \\frac{k}{6} = -\\frac{2}{3}x + \\frac{k}{6}$.\n"
                            "3. The gradient is $m = -\\frac{2}{3}$."
                        )
                    }
                },

                # PAGE 11 — summary
                {
                    "page_number": 11,
                    "page_title": "Key Takeaways: Search-Line Optimization",
                    "block_type": "summary",
                    "component_type": "summary",
                    "content": {
                        "text": (
                            "### Master Summary: Search-Line Optimization\n\n"
                            "| Tool | Formula | Key Insight |\n"
                            "|:---|:---|:---|\n"
                            "| **Trial Equation** | $ax + by = \\text{LCM}(a, b)$ | Gives clean whole-number intercepts. |\n"
                            "| **Gradient** | $m = -\\frac{a}{b}$ | Stays constant as ruler slides across the grid. |\n"
                            "| **Minimization** | First contact vertex | Lowest cost / resource usage. |\n"
                            "| **Maximization** | Last contact vertex | Highest profit / production output. |\n"
                            "| **Parallel Boundary** | Slope matches constraint | Infinite optimal solutions along boundary edge. |\n\n"
                            "**Linear Programming Mastery Complete:**\n"
                            "- [x] Word problems $\\to$ Inequalities\n"
                            "- [x] Graphing $\\to$ KCSE Unwanted Shading\n"
                            "- [x] Optimizing $\\to$ Corner Point & Search Line"
                        )
                    }
                }
            ]
        }
    ]


def ingest_topic6_linear_programming():
    """Main ingestion runner for Topic 6: Linear Programming."""
    print("=" * 80)
    print("VLearn Form 4 Mathematics — Topic 6: Linear Programming")
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

    # 2. Get or create Topic 6
    topic_name = "Topic 6: Linear Programming"
    topic, topic_created = Topic.objects.get_or_create(
        subject=subject,
        order=6,
        defaults={"name": topic_name}
    )
    if not topic_created and topic.name != topic_name:
        topic.name = topic_name
        topic.save()
    print(f"Found Topic: {topic.name} (ID: {topic.id})")

    modules_data = get_topic6_data()
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
    ingest_topic6_linear_programming()
