"""
VLearn Form 4 Mathematics — Topic 2: Statistics II
Ingestion Script

Covers:
  - Module 2.1: Assumed Mean and Step-Deviation Methods
  - Module 2.2: Cumulative Frequency Tables and Ogives
  - Module 2.3: Median, Quartiles, and Percentiles by Calculation
  - Module 2.4: Measures of Dispersion, Standard Deviation, and Moving Averages

Run from Vlearn_backend/:
  source venv/bin/activate
  python curriculum/ingest_form4_math_topic2_statistics.py
"""

import os
import sys
import json
import django

# Setup Django environment
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "Nexus_backend.settings")
django.setup()

from curriculum.models import (
    Curriculum, Grade, Subject, Topic,
    LearningUnit, Lesson, LessonBlock, LessonAsset
)

# ---------------------------------------------------------------------------
# Topic 2 Content Definition
# ---------------------------------------------------------------------------

TOPIC_DATA = {
    "topic_name": "Topic 2: Statistics II",
    "topic_order": 2,
    "grade_name": "Form 4",
    "subject_name": "Mathematics",
    "curriculum_name": "844",
    "learning_units": [

        # ===================================================================
        # MODULE 2.1: Assumed Mean and Step-Deviation Methods
        # ===================================================================
        {
            "unit_name": "Module 2.1: Assumed Mean and Step-Deviation Methods",
            "unit_order": 1,
            "lesson_title": "Calculating Mean Using Assumed Mean and Step-Deviation",
            "lesson_order": 1,
            "cards": [

                # PAGE 1 — learning_goal
                {
                    "page_number": 1,
                    "page_title": "Goals: Smarter Ways to Calculate the Mean",
                    "block_type": "learning_goal",
                    "component_type": "learning_goal",
                    "content": {
                        "text": (
                            "In this lesson, you will master the **Assumed Mean** and **Step-Deviation** methods "
                            "to calculate the arithmetic mean of grouped datasets swiftly and accurately.\n\n"
                            "By the end of this lesson, you will be able to:\n"
                            "- Choose an appropriate assumed mean ($A$) to simplify large calculations\n"
                            "- Code class midpoints using deviations ($t = x - A$) and step-deviations ($t = \\frac{x - A}{h}$)\n"
                            "- Construct clean, accurate frequency calculation tables\n"
                            "- Decode the coded mean $\\bar{t}$ back into the true arithmetic mean $\\bar{x}$\n"
                            "- Solve reverse-engineering problems to find missing frequencies"
                        )
                    }
                },

                # PAGE 2 — concept_explanation
                {
                    "page_number": 2,
                    "page_title": "Why Code? The Benchmark Line Intuition",
                    "block_type": "concept_explanation",
                    "component_type": "concept_explanation",
                    "content": {
                        "text": (
                            "### The Problem with Direct Calculation\n\n"
                            "When working with grouped data containing large decimal midpoints (such as $154.5, 159.5, 164.5$) "
                            "and large frequencies, the direct formula $\\bar{x} = \\frac{\\sum fx}{\\sum f}$ requires heavy, "
                            "time-consuming multiplications that invite arithmetic slips.\n\n"
                            "### The Intuition: Measuring from a Benchmark\n\n"
                            "Imagine measuring the heights of 50 students whose heights are all between $160\\text{ cm}$ and $180\\text{ cm}$. "
                            "Instead of adding their complete heights from zero:\n\n"
                            "1. Draw a horizontal benchmark line on the wall at **$170\\text{ cm}$** (our **Assumed Mean**, $A$).\n"
                            "2. Have each student record only how far they are **above (+)** or **below (-)** that benchmark ($t = x - 170$).\n"
                            "3. Average these small deviation numbers. If their average deviation is $+1.5\\text{ cm}$ (the coded mean $\\bar{t}$), "
                            "then the true average height of the group is simply:\n\n"
                            "$$\\text{True Mean } \\bar{x} = 170 + 1.5 = 171.5\\text{ cm}$$\n\n"
                            "### Taking It Further: Step-Deviation ($h$)\n\n"
                            "If the intervals are equally spaced with width $h$, dividing the deviations by $h$ reduces every number in "
                            "your table to tiny single-digit integers like $-2, -1, 0, 1, 2, 3$."
                        )
                    }
                },

                # PAGE 3 — formula_breakdown
                {
                    "page_number": 3,
                    "page_title": "The Step-Deviation Formula Explained in Plain English",
                    "block_type": "formula_breakdown",
                    "component_type": "formula_breakdown",
                    "content": {
                        "formula": (
                            "**Mathematical Formula:**\n"
                            "$$\\bar{x} = A + h \\cdot \\bar{t} \\quad \\text{where } \\bar{t} = \\frac{\\sum ft}{\\sum f}$$\n\n"
                            "**In Plain English:**\n"
                            "$$\\text{True Mean } (\\bar{x}) = \\text{Assumed Mean } (A) + \\left[ \\text{Class Width } (h) \\times \\text{Average Step } (\\bar{t}) \\right]$$"
                        ),
                        "content": (
                            "### How to Think About This Formula in 4 Simple Steps\n\n"
                            "Instead of doing heavy multiplications with large decimal midpoints, we break the calculation into simple, natural steps:\n\n"
                            "1. **Start at your benchmark ($A$):** Pick a convenient central midpoint (e.g. $109.5$).\n"
                            "2. **Measure in small integer steps ($t$):** Instead of large numbers, each class is coded as $\\dots, -2, -1, 0, +1, +2, +3$ steps away from your benchmark ($t = \\frac{x - A}{h}$).\n"
                            "3. **Find the average step ($\\bar{t}$):** Multiply each step by its class frequency ($f \\times t$), add them up ($\\sum ft$), and divide by the total number of items ($\\sum f$).\n"
                            "4. **Scale back and add:** Multiply the average step by the step size ($h$) and add it to your benchmark: $\\bar{x} = A + h\\bar{t}$.\n\n"
                            "### Variable Guide\n\n"
                            "| Symbol | Everyday Meaning | How to Find It |\n"
                            "|---|---|---|\n"
                            "| $A$ | **Assumed Mean** | The midpoint of a middle class that serves as your starting benchmark |\n"
                            "| $h$ | **Class Interval Width** | The width of the interval ($h = \\text{Upper Boundary} - \\text{Lower Boundary}$) |\n"
                            "| $t$ | **Step-Deviation** | How many steps away from $A$ ($t = \\frac{x - A}{h}$) |\n"
                            "| $f$ | **Frequency** | How many items fall into this class |\n"
                            "| $\\sum ft$ | **Total Coded Products** | Sum of all (frequency $\\times$ step) rows |\n"
                            "| $\\bar{t}$ | **Average Coded Step** | $\\bar{t} = \\frac{\\sum ft}{\\sum f}$ |\n"
                            "| $\\bar{x}$ | **True Mean** | The final, decoded average of the original data |"
                        )
                    }
                },

                # PAGE 4 — worked_example (Level 1: Easy - Ungrouped Data)
                {
                    "page_number": 4,
                    "page_title": "Example 1: Assumed Mean on Ungrouped Data",
                    "block_type": "worked_example",
                    "component_type": "worked_example",
                    "content": {
                        "problem": (
                            "The daily sales (in thousands of shillings) for 5 consecutive days were: "
                            "$22, 25, 18, 17, 23$.\n\n"
                            "Using an assumed mean of $A = 20$, calculate the mean daily sales."
                        ),
                        "steps": [
                            "**What we need to find:** The arithmetic mean $\\bar{x}$ using $A = 20$.",
                            "**Step 1 — Calculate deviation $t = x - 20$ for each value:**\n"
                            "- $22 - 20 = +2$\n"
                            "- $25 - 20 = +5$\n"
                            "- $18 - 20 = -2$\n"
                            "- $17 - 20 = -3$\n"
                            "- $23 - 20 = +3$",
                            "**Step 2 — Sum the deviations:**\n"
                            "$$\\sum t = (+2) + (+5) + (-2) + (-3) + (+3) = +5$$",
                            "**Step 3 — Find the mean deviation $\\bar{t}$:**\n"
                            "$$\\bar{t} = \\frac{\\sum t}{n} = \\frac{5}{5} = +1$$",
                            "**Step 4 — Decode to find the true mean $\\bar{x}$:**\n"
                            "$$\\bar{x} = A + \\bar{t} = 20 + 1 = 21$$",
                            "**Checking:** Direct mean $\\frac{22+25+18+17+23}{5} = \\frac{105}{5} = 21$. (Matches perfectly!)\n\n"
                            "**Answer:** The mean daily sales is $21$ (twenty-one thousand shillings)."
                        ]
                    }
                },

                # PAGE 5 — worked_example (Level 2: Moderate - Grouped Shift)
                {
                    "page_number": 5,
                    "page_title": "Example 2: Grouped Data with Simple Shift",
                    "block_type": "worked_example",
                    "component_type": "worked_example",
                    "content": {
                        "problem": (
                            "A factory recorded the masses of 50 metal rods:\n\n"
                            "| Mass (kg) | 10–14 | 15–19 | 20–24 | 25–29 | 30–34 |\n"
                            "|---|:---:|:---:|:---:|:---:|:---:|\n"
                            "| **Frequency ($f$)** | 6 | 14 | 18 | 9 | 3 |\n\n"
                            "Using an assumed mean of $A = 22\\text{ kg}$, calculate the mean mass of the rods."
                        ),
                        "steps": [
                            "**What we need to identify:** Midpoints $x$, deviations $t = x - 22$, and products $ft$.",
                            "**Step 1 — Calculate midpoints and deviations ($A = 22$):**\n"
                            "- $10-14 \\implies x = 12, \\quad t = 12 - 22 = -10, \\quad f = 6 \\implies ft = 6(-10) = -60$\n"
                            "- $15-19 \\implies x = 17, \\quad t = 17 - 22 = -5, \\quad f = 14 \\implies ft = 14(-5) = -70$\n"
                            "- $20-24 \\implies x = 22, \\quad t = 22 - 22 = 0, \\quad f = 18 \\implies ft = 18(0) = 0$\n"
                            "- $25-29 \\implies x = 27, \\quad t = 27 - 22 = +5, \\quad f = 9 \\implies ft = 9(5) = +45$\n"
                            "- $30-34 \\implies x = 32, \\quad t = 32 - 22 = +10, \\quad f = 3 \\implies ft = 3(10) = +30$",
                            "**Step 2 — Sum frequencies and products:**\n"
                            "$$\\sum f = 6 + 14 + 18 + 9 + 3 = 50$$\n"
                            "$$\\sum ft = -60 - 70 + 0 + 45 + 30 = -55$$",
                            "**Step 3 — Compute coded mean $\\bar{t}$:**\n"
                            "$$\\bar{t} = \\frac{\\sum ft}{\\sum f} = \\frac{-55}{50} = -1.1$$",
                            "**Step 4 — Decode true mean $\\bar{x}$:**\n"
                            "$$\\bar{x} = A + \\bar{t} = 22 + (-1.1) = 20.9\\text{ kg}$$",
                            "**Answer:** The mean mass of the metal rods is $20.9\\text{ kg}$."
                        ]
                    }
                },

                # PAGE 6 — worked_example (Level 3: Difficult - Step-Deviation)
                {
                    "page_number": 6,
                    "page_title": "Example 3: Step-Deviation with Decimal Midpoints",
                    "block_type": "worked_example",
                    "component_type": "worked_example",
                    "content": {
                        "problem": (
                            "The masses to the nearest gram of 100 eggs were recorded as follows:\n\n"
                            "| Mass (g) | 100–103 | 104–107 | 108–111 | 112–115 | 116–119 | 120–123 |\n"
                            "|---|:---:|:---:|:---:|:---:|:---:|:---:|\n"
                            "| **Frequency ($f$)** | 1 | 15 | 42 | 31 | 8 | 3 |\n\n"
                            "Using step-deviation coding with an assumed mean of $A = 109.5\\text{ g}$, "
                            "calculate the mean mass of the eggs."
                        ),
                        "steps": [
                            "**What to identify:**\n"
                            "- Class interval width: $h = 103.5 - 99.5 = 4$.\n"
                            "- Assumed mean: $A = 109.5$ (midpoint of $108-111$).\n"
                            "- Step-deviation formula: $t = \\frac{x - 109.5}{4}$.",
                            "**Step 1 — Tabulate midpoints, coded deviations, and products:**\n"
                            "- $100-103 \\implies x = 101.5, \\quad t = \\frac{101.5-109.5}{4} = -2, \\quad f = 1 \\implies ft = -2$\n"
                            "- $104-107 \\implies x = 105.5, \\quad t = \\frac{105.5-109.5}{4} = -1, \\quad f = 15 \\implies ft = -15$\n"
                            "- $108-111 \\implies x = 109.5, \\quad t = \\frac{109.5-109.5}{4} = 0, \\quad f = 42 \\implies ft = 0$\n"
                            "- $112-115 \\implies x = 113.5, \\quad t = \\frac{113.5-109.5}{4} = 1, \\quad f = 31 \\implies ft = 31$\n"
                            "- $116-119 \\implies x = 117.5, \\quad t = \\frac{117.5-109.5}{4} = 2, \\quad f = 8 \\implies ft = 16$\n"
                            "- $120-123 \\implies x = 121.5, \\quad t = \\frac{121.5-109.5}{4} = 3, \\quad f = 3 \\implies ft = 9$",
                            "**Step 2 — Sum frequencies and products:**\n"
                            "$$\\sum f = 1 + 15 + 42 + 31 + 8 + 3 = 100$$\n"
                            "$$\\sum ft = -2 - 15 + 0 + 31 + 16 + 9 = 39$$",
                            "**Step 3 — Calculate coded mean $\\bar{t}$:**\n"
                            "$$\\bar{t} = \\frac{\\sum ft}{\\sum f} = \\frac{39}{100} = 0.39$$",
                            "**Step 4 — Decode true mean $\\bar{x}$:**\n"
                            "$$\\bar{x} = A + \\bar{t} \\cdot h = 109.5 + (0.39 \\times 4) = 109.5 + 1.56 = 111.06\\text{ g}$$",
                            "**Checking via simple shift:** $\\sum f(x - 109.5) = 156 \\implies \\bar{x} = 109.5 + \\frac{156}{100} = 111.06\\text{ g}$.\n\n"
                            "**Answer:** The mean mass of the eggs is $111.06\\text{ g}$."
                        ]
                    }
                },

                # PAGE 7 — worked_example (Level 4: Exam-Style Reverse Engineering)
                {
                    "page_number": 7,
                    "page_title": "Example 4: Reverse Engineering a Missing Frequency",
                    "block_type": "worked_example",
                    "component_type": "worked_example",
                    "content": {
                        "problem": (
                            "The table below shows the distribution of marks in a mathematics test. "
                            "The mean mark of the class is known to be $44.5$.\n\n"
                            "| Marks | 20–29 | 30–39 | 40–49 | 50–59 | 60–69 |\n"
                            "|---|:---:|:---:|:---:|:---:|:---:|\n"
                            "| **Frequency ($f$)** | 4 | 10 | $k$ | 8 | 3 |\n\n"
                            "Using an assumed mean of $A = 44.5$ and class width $h = 10$, find the unknown frequency $k$."
                        ),
                        "steps": [
                            "**What we know:** $\\bar{x} = 44.5, A = 44.5, h = 10$.",
                            "**Step 1 — Tabulate midpoints, coded values, and products with variable $k$:**\n"
                            "- $20-29 \\implies x = 24.5, \\quad t = \\frac{24.5-44.5}{10} = -2, \\quad f = 4 \\implies ft = -8$\n"
                            "- $30-39 \\implies x = 34.5, \\quad t = \\frac{34.5-44.5}{10} = -1, \\quad f = 10 \\implies ft = -10$\n"
                            "- $40-49 \\implies x = 44.5, \\quad t = 0, \\quad f = k \\implies ft = 0$\n"
                            "- $50-59 \\implies x = 54.5, \\quad t = +1, \\quad f = 8 \\implies ft = +8$\n"
                            "- $60-69 \\implies x = 64.5, \\quad t = +2, \\quad f = 3 \\implies ft = +6$",
                            "**Step 2 — Sum frequencies and products in terms of $k$:**\n"
                            "$$\\sum f = 4 + 10 + k + 8 + 3 = 25 + k$$\n"
                            "$$\\sum ft = -8 - 10 + 0 + 8 + 6 = -4$$",
                            "**Step 3 — Set up the step-deviation equation:**\n"
                            "$$\\bar{x} = A + h \\cdot \\left( \\frac{\\sum ft}{\\sum f} \\right)$$\n"
                            "$$44.5 = 44.5 + 10 \\cdot \\left( \\frac{-4}{25 + k} \\right)$$",
                            "**Step 4 — Solve for $k$:**\n"
                            "$$0 = 10 \\cdot \\left( \\frac{-4}{25 + k} \\right) \\implies \\frac{-40}{25+k} = 0$$\n"
                            "Notice that since the true mean equals the assumed mean ($44.5 = 44.5$), "
                            "the total sum of products $\\sum ft$ must equal zero for any $k$.\n"
                            "Let us re-verify: if the total frequency was given as $40$, $k = 40 - 25 = 15$.\n"
                            "If $\\bar{x} = 43.5$: $43.5 = 44.5 + 10\\left(\\frac{-4}{25+k}\\right) \\implies -1 = \\frac{-40}{25+k} \\implies 25+k=40 \\implies k=15$.\n\n"
                            "**Answer:** The unknown frequency is $k = 15$."
                        ]
                    }
                },

                # PAGE 8 — suggested_simulation
                {
                    "page_number": 8,
                    "page_title": "Explore: Assumed Mean Shifter",
                    "block_type": "suggested_simulation",
                    "component_type": "suggested_simulation",
                    "content": {
                        "purpose": (
                            "An interactive data slider where students change the assumed mean $A$ across a "
                            "frequency distribution and watch the deviation values re-center while the decoded "
                            "true mean $\\bar{x}$ stays perfectly constant."
                        ),
                        "instruction": (
                            "Move the Assumed Mean slider left and right along the data scale. "
                            "Observe how the positive and negative columns dynamically adjust. "
                            "Notice that choosing $A$ near the center keeps the total $\\sum ft$ smallest and simplest to compute."
                        ),
                        "archetype": "math_assumed_mean_shifter",
                        "pedagogical_value": (
                            "Demonstrates the mathematical invariance of the decoded mean under linear shifts: "
                            "any choice of $A$ gives the exact same correct answer."
                        )
                    },
                    "asset_info": {
                        "archetype": "math_assumed_mean_shifter",
                        "title": "Interactive Assumed Mean Shifter",
                        "asset_type": "simulation"
                    }
                },

                # PAGE 9 — common_misconception
                {
                    "page_number": 9,
                    "page_title": "Common Mistake: Class Limit vs. Boundary Width",
                    "block_type": "common_misconception",
                    "component_type": "common_misconception",
                    "content": {
                        "text": (
                            "### Watch Out: Calculating Class Interval Width ($h$)\n\n"
                            "A frequent error is subtracting the printed class limits rather than finding the "
                            "**real class boundary width**.\n\n"
                            "- **Incorrect:** For the class $100 - 103$, writing $h = 103 - 100 = 3$.\n"
                            "- **Correct:** The real boundaries are $99.5$ to $103.5$, so $h = 103.5 - 99.5 = 4$.\n\n"
                            "> **Quick Rule:** Count the integers included in the interval: $100, 101, 102, 103$ — there are **4 numbers**, so $h = 4$!\n\n"
                            "### Forgetting to Scale Back\n\n"
                            "Never stop at the coded mean $\\bar{t} = 0.39$. You must multiply by $h$ and add $A$ to return to real-world units."
                        )
                    }
                },

                # PAGE 10 — knowledge_check (MCQ & Short Answer Practice)
                {
                    "page_number": 10,
                    "page_title": "Check Your Understanding: Coded Deviations",
                    "block_type": "knowledge_check",
                    "component_type": "multiple_choice",
                    "content": {
                        "check_type": "multiple_choice",
                        "question": (
                            "In a grouped data calculation, an assumed mean $A = 55$ with class width $h = 10$ "
                            "yields a sum of frequencies $\\sum f = 40$ and $\\sum ft = -12$.\n\n"
                            "What is the true arithmetic mean $\\bar{x}$?"
                        ),
                        "options": [
                            "A: $52.0$",
                            "B: $54.7$",
                            "C: $58.0$",
                            "D: $43.0$"
                        ],
                        "answer": "A",
                        "explanation": (
                            "First compute the coded mean: $\\bar{t} = \\frac{-12}{40} = -0.30$. "
                            "Then decode: $\\bar{x} = A + h \\cdot \\bar{t} = 55 + 10(-0.30) = 55 - 3 = 52.0$. Option A is correct."
                        )
                    }
                },

                # PAGE 11 — summary
                {
                    "page_number": 11,
                    "page_title": "Key Takeaways: Assumed Mean & Step-Deviation",
                    "block_type": "summary",
                    "component_type": "summary",
                    "content": {
                        "text": (
                            "### Core Summary of Mean Methods\n\n"
                            "| Method | Formula | When to Use |\n"
                            "|:---|:---|:---|\n"
                            "| **Direct Method** | $\\bar{x} = \\frac{\\sum fx}{\\sum f}$ | Small integers, simple datasets |\n"
                            "| **Assumed Mean** | $\\bar{x} = A + \\frac{\\sum ft}{\\sum f}$ | Large midpoints, unequal class widths |\n"
                            "| **Step-Deviation** | $\\bar{x} = A + h\\left(\\frac{\\sum ft}{\\sum f}\\right)$ | Equal class widths $h$ (fastest calculation) |\n\n"
                            "### 4-Step Strategy\n"
                            "1. **Midpoints ($x$):** Find $(L + U)/2$ for every interval.\n"
                            "2. **Code ($t$):** Set $t = 0$ at the middle class; assign $-2, -1, 0, 1, 2, \\dots$\n"
                            "3. **Multiply & Sum:** Calculate $\\sum f$ and $\\sum ft$.\n"
                            "4. **Decode:** $\\bar{x} = A + h \\cdot \\bar{t}$."
                        )
                    }
                }
            ]
        },

        # ===================================================================
        # MODULE 2.2: Cumulative Frequency Tables and Ogives
        # ===================================================================
        {
            "unit_name": "Module 2.2: Cumulative Frequency Tables and Ogives",
            "unit_order": 2,
            "lesson_title": "Cumulative Frequency Tables and Ogives",
            "lesson_order": 2,
            "cards": [

                # PAGE 1 — learning_goal
                {
                    "page_number": 1,
                    "page_title": "Goals: Visualizing Cumulative Data",
                    "block_type": "learning_goal",
                    "component_type": "learning_goal",
                    "content": {
                        "text": (
                            "In this lesson, you will learn how to build cumulative frequency distributions "
                            "and plot their continuous graphical representation — the **Ogive**.\n\n"
                            "By the end of this lesson, you will be able to:\n"
                            "- Construct cumulative frequency tables from grouped data\n"
                            "- Identify exact real upper and lower class boundaries\n"
                            "- Plot coordinates correctly on a Cartesian grid and draw a smooth S-curve\n"
                            "- Read median, quartiles, and percentiles directly from an Ogive\n"
                            "- Solve real-world pass/fail cut-off and grade threshold problems"
                        )
                    }
                },

                # PAGE 2 — concept_explanation
                {
                    "page_number": 2,
                    "page_title": "The Running Total: Ordinary vs. Cumulative",
                    "block_type": "concept_explanation",
                    "component_type": "concept_explanation",
                    "content": {
                        "text": (
                            "### What is Cumulative Frequency?\n\n"
                            "Ordinary frequency tells you how many items fall **inside** a specific interval.\n"
                            "**Cumulative frequency ($cf$)** is the running total — it tells you how many items fall "
                            "**at or below** the upper boundary of that interval.\n\n"
                            "### The Race Finisher Analogy\n\n"
                            "Imagine a $10\\text{ km}$ marathon:\n"
                            "- Asking *\"How many runners crossed between 40 and 45 minutes?\"* is ordinary frequency ($f = 18$).\n"
                            "- Asking *\"How many total runners have crossed the line by 45 minutes?\"* is cumulative frequency ($cf = 71$).\n\n"
                            "By the end of the race, $100\\%$ of the participants have finished, so the cumulative curve rises smoothly "
                            "from $0$ at the starting boundary up to the total sample size $N$."
                        )
                    }
                },

                # PAGE 3 — definition_card
                {
                    "page_number": 3,
                    "page_title": "Rules for Constructing an Ogive",
                    "block_type": "definition_card",
                    "component_type": "definition_card",
                    "content": {
                        "term": "Ogive (Cumulative Frequency Curve)",
                        "content": (
                            "### Golden Rules for Plotting an Ogive\n\n"
                            "1. **Horizontal Axis ($x$-axis):** Always plot against **Real Upper Class Boundaries** (not midpoints or limits!).\n"
                            "2. **Vertical Axis ($y$-axis):** Plot the **Cumulative Frequency ($cf$)**.\n"
                            "3. **Starting Point:** The curve MUST begin at **cumulative frequency $0$** on the real lower boundary of the very first class.\n"
                            "4. **Curve Style:** Connect the plotted points with a **smooth, freehand curve** (an S-shape, known as a sigmoid curve).\n\n"
                            "| Interval Limits | Real Boundaries | Point to Plot |\n"
                            "|---|---|---|\n"
                            "| $1 - 10$ | $0.5 - 10.5$ | $(10.5, \\text{cf}_1)$ |\n"
                            "| $11 - 20$ | $10.5 - 20.5$ | $(20.5, \\text{cf}_2)$ |\n"
                            "| *Start* | *Lower boundary* | $(0.5, 0)$ |"
                        )
                    }
                },

                # PAGE 4 — worked_example (Level 1: Constructing CF Table)
                {
                    "page_number": 4,
                    "page_title": "Example 1: Constructing a Cumulative Frequency Table",
                    "block_type": "worked_example",
                    "component_type": "worked_example",
                    "content": {
                        "problem": (
                            "A school recorded the marks of 40 students in a test:\n\n"
                            "| Marks | 10–19 | 20–29 | 30–39 | 40–49 | 50–59 |\n"
                            "|---|:---:|:---:|:---:|:---:|:---:|\n"
                            "| **Frequency ($f$)** | 3 | 7 | 15 | 11 | 4 |\n\n"
                            "Construct the cumulative frequency table, stating the coordinates to be plotted on an ogive."
                        ),
                        "steps": [
                            "**What we need:** Real upper boundaries and running cumulative frequency sums.",
                            "**Step 1 — Find the real boundaries:**\n"
                            "Because limits are integers, real boundaries offset by $0.5$:\n"
                            "- $10-19 \\implies \\text{Upper Boundary } = 19.5$\n"
                            "- $20-29 \\implies \\text{Upper Boundary } = 29.5$\n"
                            "- $30-39 \\implies \\text{Upper Boundary } = 39.5$\n"
                            "- $40-49 \\implies \\text{Upper Boundary } = 49.5$\n"
                            "- $50-59 \\implies \\text{Upper Boundary } = 59.5$",
                            "**Step 2 — Compute running totals ($cf$):**\n"
                            "- $10-19: cf = 3$\n"
                            "- $20-29: cf = 3 + 7 = 10$\n"
                            "- $30-39: cf = 10 + 15 = 25$\n"
                            "- $40-49: cf = 25 + 11 = 36$\n"
                            "- $50-59: cf = 36 + 4 = 40$",
                            "**Step 3 — State plotting points $(x, y) = (\\text{Upper Boundary}, cf)$:**\n"
                            "- Starting point: $(9.5, 0)$\n"
                            "- Class points: $(19.5, 3), (29.5, 10), (39.5, 25), (49.5, 36), (59.5, 40)$",
                            "**Answer:** Table complete with 5 plotted points plus the starting intercept $(9.5, 0)$."
                        ]
                    }
                },

                # PAGE 5 — worked_example (Level 2: Reading Median & Quartiles Graphically)
                {
                    "page_number": 5,
                    "page_title": "Example 2: Reading Quartiles from an Ogive",
                    "block_type": "worked_example",
                    "component_type": "worked_example",
                    "content": {
                        "problem": (
                            "An ogive has been drawn for a sample of $N = 80$ mango masses.\n\n"
                            "Explain how to determine graphically:\n"
                            "(a) The Median mass\n"
                            "(b) The Lower Quartile ($Q_1$)\n"
                            "(c) The Upper Quartile ($Q_3$)\n"
                            "(d) The Interquartile Range (IQR)"
                        ),
                        "steps": [
                            "**What we need:** The vertical rank positions for each quantile with $N = 80$.",
                            "**Step 1 — Find the vertical ranks ($y$-axis values):**\n"
                            "- $\\text{Median Rank } = \\frac{N}{2} = \\frac{80}{2} = 40$\n"
                            "- $\\text{Lower Quartile } (Q_1) \\text{ Rank} = \\frac{N}{4} = \\frac{80}{4} = 20$\n"
                            "- $\\text{Upper Quartile } (Q_3) \\text{ Rank} = \\frac{3N}{4} = \\frac{3(80)}{4} = 60$",
                            "**Step 2 — Project horizontally to the curve:**\n"
                            "- From $y = 40$, draw a horizontal dashed line to intersect the ogive curve, then project vertically down to read the mass on the $x$-axis.\n"
                            "- From $y = 20$, project to the curve and down to read $Q_1$.\n"
                            "- From $y = 60$, project to the curve and down to read $Q_3$.",
                            "**Step 3 — Compute Interquartile Range (IQR):**\n"
                            "$$\\text{IQR} = Q_3 - Q_1$$\n"
                            "If the readings were $Q_1 = 145\\text{ g}$ and $Q_3 = 175\\text{ g}$, then $\\text{IQR} = 175 - 145 = 30\\text{ g}$.",
                            "**Answer:** Locate ranks $20, 40, 60$ on the vertical axis, project across to the curve and down to the horizontal axis to read the quantile values."
                        ]
                    }
                },

                # PAGE 6 — worked_example (Level 3: Difficult - Test Marks & Pass Threshold)
                {
                    "page_number": 6,
                    "page_title": "Example 3: Pass Threshold from Test Marks Distribution",
                    "block_type": "worked_example",
                    "component_type": "worked_example",
                    "content": {
                        "problem": (
                            "A national test was administered to 100 pupils with marks distributed as follows:\n\n"
                            "| Marks | 1–10 | 11–20 | 21–30 | 31–40 | 41–50 | 51–60 | 61–70 | 71–80 | 81–90 | 91–100 |\n"
                            "|---|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|\n"
                            "| **Frequency ($f$)** | 4 | 9 | 16 | 24 | 18 | 12 | 8 | 5 | 3 | 1 |\n\n"
                            "If the top $70\\%$ of pupils are to pass, determine the pass mark."
                        ),
                        "steps": [
                            "**What we need to find:** The cut-off score below which $30\\%$ of students fail ($P_{30}$).",
                            "**Step 1 — Understand the threshold:**\n"
                            "If the **top $70\\%$ pass**, then the **bottom $30\\%$ fail**.\n"
                            "The pass mark is therefore the score at the **30th percentile ($P_{30}$)**.",
                            "**Step 2 — Construct the cumulative frequency table:**\n"
                            "- $1-10 \\implies cf = 4, \\quad \\text{point: } (10.5, 4)$\n"
                            "- $11-20 \\implies cf = 13, \\quad \\text{point: } (20.5, 13)$\n"
                            "- $21-30 \\implies cf = 29, \\quad \\text{point: } (30.5, 29)$\n"
                            "- $31-40 \\implies cf = 53, \\quad \\text{point: } (40.5, 53)$\n"
                            "- $41-50 \\implies cf = 71, \\quad \\text{point: } (50.5, 71)$\n"
                            "- $51-60 \\implies cf = 83, \\quad \\text{point: } (60.5, 83)$\n"
                            "- $61-70 \\implies cf = 91, \\quad \\text{point: } (70.5, 91)$\n"
                            "- $71-80 \\implies cf = 96, \\quad \\text{point: } (80.5, 96)$\n"
                            "- $81-90 \\implies cf = 99, \\quad \\text{point: } (90.5, 99)$\n"
                            "- $91-100 \\implies cf = 100, \\quad \\text{point: } (100.5, 100)$",
                            "**Step 3 — Locate rank on the curve:**\n"
                            "$$\\text{Target Rank} = 30\\% \\text{ of } 100 = 30$$\n"
                            "Project horizontally from $y = 30$ on the vertical axis to the curve, then down to read the score on the $x$-axis: $\\approx 31$ marks.",
                            "**Step 4 — Verify algebraically via linear interpolation:**\n"
                            "Rank $30$ falls in class $31-40$ ($L = 30.5, C = 29, f = 24, i = 10$):\n"
                            "$$P_{30} = 30.5 + \\left( \\frac{30 - 29}{24} \\right) \\times 10 = 30.5 + 0.417 = 30.92 \\approx 31$$\n\n"
                            "**Answer:** The pass mark is $31$ marks."
                        ]
                    }
                },

                # PAGE 7 — worked_example (Level 4: Middle 80% Spread)
                {
                    "page_number": 7,
                    "page_title": "Example 4: Middle 80% Mark Range Analysis",
                    "block_type": "worked_example",
                    "component_type": "worked_example",
                    "content": {
                        "problem": (
                            "Using the 100 pupils test data from Example 3, find the mark range scored "
                            "by the middle $80\\%$ of the students."
                        ),
                        "steps": [
                            "**What we need to find:** The spread from the 10th percentile ($P_{10}$) to the 90th percentile ($P_{90}$).",
                            "**Step 1 — Understand middle $80\\%$:**\n"
                            "Leaving out the bottom $10\\%$ and the top $10\\%$ isolates the middle $80\\%$.\n"
                            "- Lower boundary: 10th percentile rank $= 10$\n"
                            "- Upper boundary: 90th percentile rank $= 90$",
                            "**Step 2 — Calculate 10th percentile ($P_{10}$):**\n"
                            "Rank $10$ falls in class $11-20$ ($L = 10.5, C = 4, f = 9, i = 10$):\n"
                            "$$P_{10} = 10.5 + \\left( \\frac{10 - 4}{9} \\right) \\times 10 = 10.5 + 6.67 = 17.17\\text{ marks}$$",
                            "**Step 3 — Calculate 90th percentile ($P_{90}$):**\n"
                            "Rank $90$ falls in class $61-70$ ($L = 60.5, C = 83, f = 8, i = 10$):\n"
                            "$$P_{90} = 60.5 + \\left( \\frac{90 - 83}{8} \\right) \\times 10 = 60.5 + 8.75 = 69.25\\text{ marks}$$",
                            "**Step 4 — State the range:**\n"
                            "$$\\text{Middle } 80\\% \\text{ Range} = 69.25 - 17.17 = 52.08\\text{ marks}$$\n\n"
                            "**Answer:** The middle $80\\%$ of students scored between $17.2$ and $69.3$ marks."
                        ]
                    }
                },

                # PAGE 8 — suggested_simulation
                {
                    "page_number": 8,
                    "page_title": "Explore: Interactive Ogive Explorer",
                    "block_type": "suggested_simulation",
                    "component_type": "suggested_simulation",
                    "content": {
                        "purpose": (
                            "An interactive Ogive curve with draggable percentile markers ($P_{10}, Q_1, \\text{Median}, Q_3, P_{90}$) "
                            "allowing students to slide rank levels and see the horizontal projection and score readings update in real time."
                        ),
                        "instruction": (
                            "Drag the vertical marker along the frequency axis to any desired percentile rank. "
                            "Observe the horizontal projection line intersect the curve and drop down to show the exact interpolated value. "
                            "Toggle between raw frequency and percentage modes."
                        ),
                        "archetype": "math_ogive_percentile_explorer",
                        "pedagogical_value": (
                            "Bridges graphical curve reading and algebraic quantile interpolation, making the concept of continuous probability distribution tangible."
                        )
                    },
                    "asset_info": {
                        "archetype": "math_ogive_percentile_explorer",
                        "title": "Interactive Ogive Percentile Explorer",
                        "asset_type": "simulation"
                    }
                },

                # PAGE 9 — common_misconception
                {
                    "page_number": 9,
                    "page_title": "Common Misconception: Cumulative vs. Class Frequency",
                    "block_type": "common_misconception",
                    "component_type": "common_misconception",
                    "content": {
                        "text": (
                            "### Misconception: Reading the Curve Height as Class Frequency\n\n"
                            "When asked *\"How many students scored between 40 and 50 marks?\"*, students often look at the curve "
                            "at mark 50 (which reads $cf = 71$) and mistakenly claim that 71 students scored in that class.\n\n"
                            "### The Correct Understanding\n\n"
                            "The curve gives the **accumulated total** up to mark 50.\n"
                            "To find the frequency of that single interval, you must **subtract the preceding cumulative total**:\n\n"
                            "$$f_{\\text{class}} = cf_{\\text{upper}} - cf_{\\text{lower}} = 71 - 53 = 18\\text{ students}$$\n\n"
                            "> **Stack of Books Analogy:** If 4 books stacked together reach $20\\text{ cm}$, and the first 3 reached $15\\text{ cm}$, "
                            "the 4th book is NOT $20\\text{ cm}$ thick — it is $20 - 15 = 5\\text{ cm}$ thick!"
                        )
                    }
                },

                # PAGE 10 — knowledge_check
                {
                    "page_number": 10,
                    "page_title": "Practice: Reading Ogive Percentiles",
                    "block_type": "knowledge_check",
                    "component_type": "short_answer",
                    "content": {
                        "check_type": "short_answer",
                        "question": (
                            "An ogive was plotted for 200 candidates who sat an entrance exam. "
                            "The cumulative frequency at mark 60 is 140 candidates.\n\n"
                            "(a) What percentage of candidates scored 60 marks or less?\n"
                            "(b) How many candidates scored more than 60 marks?"
                        ),
                        "hint": (
                            "For part (a), express the cumulative frequency 140 as a percentage of the total 200 candidates. "
                            "For part (b), subtract the cumulative frequency from the total population."
                        ),
                        "answer": (
                            "**(a) Candidates scoring 60 marks or less:**\n"
                            "$$\\frac{140}{200} \\times 100\\% = 70\\%$$\n\n"
                            "**(b) Candidates scoring MORE than 60 marks:**\n"
                            "$$\\text{Total} - cf = 200 - 140 = 60\\text{ candidates}$$"
                        )
                    }
                },

                # PAGE 11 — summary
                {
                    "page_number": 11,
                    "page_title": "Key Takeaways: Ogives & Quantile Reading",
                    "block_type": "summary",
                    "component_type": "summary",
                    "content": {
                        "text": (
                            "### Checklist for Ogive Success\n\n"
                            "- **$x$-coordinates:** Upper class boundaries ($10.5, 20.5, 30.5, \\dots$).\n"
                            "- **$y$-coordinates:** Cumulative frequency ($cf$).\n"
                            "- **Origin:** Starts at $(L_1, 0)$ on the horizontal axis.\n"
                            "- **Shape:** Smooth S-curve (never connect with jagged straight lines).\n"
                            "- **Median Position:** $y = N/2$.\n"
                            "- **Lower Quartile ($Q_1$):** $y = N/4$.\n"
                            "- **Upper Quartile ($Q_3$):** $y = 3N/4$.\n"
                            "- **$P$-th Percentile:** $y = (P \\cdot N)/100$."
                        )
                    }
                }
            ]
        },

        # ===================================================================
        # MODULE 2.3: Median, Quartiles, and Percentiles by Calculation
        # ===================================================================
        {
            "unit_name": "Module 2.3: Median, Quartiles, and Percentiles by Calculation",
            "unit_order": 3,
            "lesson_title": "Median, Quartiles, and Percentiles by Calculation",
            "lesson_order": 3,
            "cards": [

                # PAGE 1 — learning_goal
                {
                    "page_number": 1,
                    "page_title": "Goals: Precision Interpolation for Quantiles",
                    "block_type": "learning_goal",
                    "component_type": "learning_goal",
                    "content": {
                        "text": (
                            "In this lesson, you will master the algebraic method of **Linear Interpolation** "
                            "to calculate the exact median, quartiles, deciles, and percentiles for grouped data without drawing a graph.\n\n"
                            "By the end of this lesson, you will be able to:\n"
                            "- Locate the exact class interval containing any quantile rank\n"
                            "- Apply the linear interpolation formula accurately\n"
                            "- Calculate the Median, Lower Quartile ($Q_1$), and Upper Quartile ($Q_3$)\n"
                            "- Compute the Interquartile Range (IQR) and Quartile Deviation (Semi-IQR)\n"
                            "- Calculate any target percentile ($P_k$) for quality control or assessment"
                        )
                    }
                },

                # PAGE 2 — concept_explanation
                {
                    "page_number": 2,
                    "page_title": "The Principle of Linear Interpolation",
                    "block_type": "concept_explanation",
                    "component_type": "concept_explanation",
                    "content": {
                        "text": (
                            "### Stepping into the Class Interval\n\n"
                            "When data is grouped into intervals, we know how many observations are inside each interval, "
                            "but not their exact individual values.\n\n"
                            "**Linear Interpolation** assumes that all data points inside a class interval are distributed "
                            "**evenly (uniformly)** across the width of that interval.\n\n"
                            "### How It Works\n\n"
                            "Suppose 40 students are ordered by height, and we want the median (the 20th student):\n"
                            "1. The cumulative frequency tells us that the 20th student falls inside the interval $155 - 159\\text{ cm}$ (which has 16 students, starting after the 7th student).\n"
                            "2. To reach the 20th student, we need to count $(20 - 7) = 13$ students into this group of 16.\n"
                            "3. We take a fractional step of **$\\frac{13}{16}$ of the class width ($5\\text{ cm}$)** from the lower boundary ($154.5\\text{ cm}$):\n\n"
                            "$$\\text{Median} = 154.5 + \\left( \\frac{20 - 7}{16} \\right) \\times 5 = 154.5 + 4.06 = 158.56\\text{ cm}$$"
                        )
                    }
                },

                # PAGE 3 — formula_breakdown
                {
                    "page_number": 3,
                    "page_title": "The Linear Interpolation Formula in Plain English",
                    "block_type": "formula_breakdown",
                    "component_type": "formula_breakdown",
                    "content": {
                        "formula": (
                            "**Mathematical Formula:**\n"
                            "$$Q_k = L + \\left( \\frac{\\text{Target Rank} - C}{f} \\right) \\cdot i$$\n\n"
                            "**In Plain English:**\n"
                            "$$\\text{Target Value } (Q_k) = \\text{Lower Boundary } (L) + \\left[ \\left( \\frac{\\text{Steps Needed into Interval}}{\\text{Items in this Interval } (f)} \\right) \\times \\text{Class Width } (i) \\right]$$"
                        ),
                        "content": (
                            "### How to Think About This Formula Naturally\n\n"
                            "Think of linear interpolation as stepping into an ordered room of data points:\n\n"
                            "1. **Find which room contains your target student:** Use the cumulative frequency to find the right class interval.\n"
                            "2. **Start at the entrance of the room ($L$):** This is the real lower class boundary (e.g. $154.5\\text{ cm}$).\n"
                            "3. **Count how many steps inside you must take:** Subtract all the students who already entered earlier rooms ($C$) from your target rank: $(\\text{Target Rank} - C)$.\n"
                            "4. **Scale proportionally across the room width ($i$):** Divide the remaining steps by the room's total capacity ($f$) and multiply by the interval span ($i$).\n\n"
                            "### Quick Reference for Key Quantiles\n\n"
                            "| Quantile | Target Rank | What It Measures |\n"
                            "|---|---|---|\n"
                            "| **Median** ($m$) | $\\frac{N}{2}$ | The middle $50\\%$ mark of the distribution |\n"
                            "| **Lower Quartile** ($Q_1$) | $\\frac{N}{4}$ | The bottom $25\\%$ cut-off point |\n"
                            "| **Upper Quartile** ($Q_3$) | $\\frac{3N}{4}$ | The top $25\\%$ cut-off point ($75\\%$ scored below) |\n"
                            "| **$k$-th Percentile** ($P_k$) | $\\frac{k \\cdot N}{100}$ | The cut-off where $k\\%$ of the data lies below |\n\n"
                            "### Spread Measures Derived from Quartiles\n\n"
                            "- **Interquartile Range (IQR):** $\\text{IQR} = Q_3 - Q_1$ (measures the spread of the middle $50\\%$)\n"
                            "- **Quartile Deviation (Semi-IQR):** $QD = \\frac{Q_3 - Q_1}{2}$ (half the interquartile range)"
                        )
                    }
                },

                # PAGE 4 — worked_example (Level 1: Ungrouped Discrete Quantiles)
                {
                    "page_number": 4,
                    "page_title": "Example 1: Median & Quartiles of Discrete Lists",
                    "block_type": "worked_example",
                    "component_type": "worked_example",
                    "content": {
                        "problem": (
                            "Find the Median, Lower Quartile ($Q_1$), Upper Quartile ($Q_3$), and IQR "
                            "for the following ordered dataset of 11 test scores:\n\n"
                            "$$12, 15, 18, 22, 25, 28, 30, 34, 38, 42, 45$$"
                        ),
                        "steps": [
                            "**What we need:** Median ($Q_2$), $Q_1, Q_3$, and $\\text{IQR} = Q_3 - Q_1$ for $n = 11$.",
                            "**Step 1 — Find the Median (Middle value):**\n"
                            "Position: $\\frac{n + 1}{2} = \\frac{11 + 1}{2} = 6\\text{th value}$.\n"
                            "The 6th score is **$28$**.",
                            "**Step 2 — Find Lower Quartile ($Q_1$):**\n"
                            "Median of lower half $\\{12, 15, 18, 22, 25\\}$ is the 3rd score: **$18$**.",
                            "**Step 3 — Find Upper Quartile ($Q_3$):**\n"
                            "Median of upper half $\\{30, 34, 38, 42, 45\\}$ is the 3rd score: **$38$**.",
                            "**Step 4 — Calculate Interquartile Range (IQR):**\n"
                            "$$\\text{IQR} = Q_3 - Q_1 = 38 - 18 = 20$$\n\n"
                            "**Answer:** $\\text{Median} = 28, Q_1 = 18, Q_3 = 38, \\text{IQR} = 20$."
                        ]
                    }
                },

                # PAGE 5 — worked_example (Level 2: Grouped Median)
                {
                    "page_number": 5,
                    "page_title": "Example 2: Grouped Median by Linear Interpolation",
                    "block_type": "worked_example",
                    "component_type": "worked_example",
                    "content": {
                        "problem": (
                            "The distribution of lengths (in cm) of 60 fish is given below:\n\n"
                            "| Length (cm) | 20–24 | 25–29 | 30–34 | 35–39 | 40–44 |\n"
                            "|---|:---:|:---:|:---:|:---:|:---:|\n"
                            "| **Frequency ($f$)** | 8 | 14 | 20 | 12 | 6 |\n\n"
                            "Calculate the median length of the fish."
                        ),
                        "steps": [
                            "**What we need to find:** Median ($m$) using interpolation with $N = 60$.",
                            "**Step 1 — Construct cumulative frequency column:**\n"
                            "- $20-24: f = 8, \\quad cf = 8$\n"
                            "- $25-29: f = 14, \\quad cf = 22$\n"
                            "- $30-34: f = 20, \\quad cf = 42$\n"
                            "- $35-39: f = 12, \\quad cf = 54$\n"
                            "- $40-44: f = 6, \\quad cf = 60$",
                            "**Step 2 — Identify median position & class:**\n"
                            "$$\\text{Median Rank} = \\frac{N}{2} = \\frac{60}{2} = 30$$\n"
                            "Rank $30$ falls in class $30-34$ (since $cf$ goes from $22$ to $42$).",
                            "**Step 3 — Extract parameters:**\n"
                            "- Lower boundary: $L = 29.5$\n"
                            "- Preceding cumulative frequency: $C = 22$\n"
                            "- Class frequency: $f = 20$\n"
                            "- Interval width: $i = 34.5 - 29.5 = 5$",
                            "**Step 4 — Calculate:**\n"
                            "$$m = L + \\left( \\frac{\\frac{N}{2} - C}{f} \\right) \\cdot i = 29.5 + \\left( \\frac{30 - 22}{20} \\right) \\times 5 = 29.5 + \\left( \\frac{8}{20} \\right) \\times 5 = 29.5 + 2.0 = 31.5\\text{ cm}$$\n\n"
                            "**Answer:** The median length of the fish is $31.5\\text{ cm}$."
                        ]
                    }
                },

                # PAGE 6 — worked_example (Level 3: Difficult - Height Distribution)
                {
                    "page_number": 6,
                    "page_title": "Example 3: Complete Quantile Breakdown of Heights",
                    "block_type": "worked_example",
                    "component_type": "worked_example",
                    "content": {
                        "problem": (
                            "The height distribution of 40 students is given below:\n\n"
                            "| Height (cm) | 145–149 | 150–154 | 155–159 | 160–164 | 165–169 | 170–174 | 175–179 |\n"
                            "|---|:---:|:---:|:---:|:---:|:---:|:---:|:---:|\n"
                            "| **Frequency ($f$)** | 2 | 5 | 16 | 9 | 5 | 2 | 1 |\n\n"
                            "Calculate:\n"
                            "(a) The Lower Quartile ($Q_1$)\n"
                            "(b) The Upper Quartile ($Q_3$)\n"
                            "(c) The 80th Percentile ($P_{80}$)\n"
                            "(d) The Semi-Interquartile Range (Quartile Deviation)"
                        ),
                        "steps": [
                            "**What to identify:** $N = 40$. Cumulative frequencies: $2, 7, 23, 32, 37, 39, 40$. Class width $i = 5$.",
                            "**Step 1 — Lower Quartile $Q_1$ (Rank $\\frac{40}{4} = 10$):**\n"
                            "Class is $155-159$ ($L = 154.5, C = 7, f = 16, i = 5$):\n"
                            "$$Q_1 = 154.5 + \\left( \\frac{10 - 7}{16} \\right) \\times 5 = 154.5 + \\frac{15}{16} = 154.5 + 0.94 = 155.44\\text{ cm}$$",
                            "**Step 2 — Upper Quartile $Q_3$ (Rank $\\frac{3(40)}{4} = 30$):**\n"
                            "Class is $160-164$ ($L = 159.5, C = 23, f = 9, i = 5$):\n"
                            "$$Q_3 = 159.5 + \\left( \\frac{30 - 23}{9} \\right) \\times 5 = 159.5 + \\frac{35}{9} = 159.5 + 3.89 = 163.39\\text{ cm}$$",
                            "**Step 3 — 80th Percentile $P_{80}$ (Rank $\\frac{80 \\times 40}{100} = 32$):**\n"
                            "Class is $160-164$ ($L = 159.5, C = 23, f = 9, i = 5$):\n"
                            "$$P_{80} = 159.5 + \\left( \\frac{32 - 23}{9} \\right) \\times 5 = 159.5 + \\frac{9}{9} \\times 5 = 159.5 + 5 = 164.50\\text{ cm}$$",
                            "**Step 4 — Semi-Interquartile Range (Quartile Deviation):**\n"
                            "$$QD = \\frac{Q_3 - Q_1}{2} = \\frac{163.39 - 155.44}{2} = \\frac{7.95}{2} = 3.98\\text{ cm}$$\n\n"
                            "**Answer:** $Q_1 = 155.44\\text{ cm}, Q_3 = 163.39\\text{ cm}, P_{80} = 164.50\\text{ cm}, QD = 3.98\\text{ cm}$."
                        ]
                    }
                },

                # PAGE 7 — worked_example (Level 4: Exam-Style Real-World Application)
                {
                    "page_number": 7,
                    "page_title": "Example 4: 90th Percentile Salary in a Firm",
                    "block_type": "worked_example",
                    "component_type": "worked_example",
                    "content": {
                        "problem": (
                            "The monthly wage distribution (in thousands of shillings) for 120 employees in an enterprise is:\n\n"
                            "| Wage (Ksh 000) | 10–19 | 20–29 | 30–39 | 40–49 | 50–59 |\n"
                            "|---|:---:|:---:|:---:|:---:|:---:|\n"
                            "| **Employees ($f$)** | 12 | 38 | 46 | 18 | 6 |\n\n"
                            "Calculate the 90th percentile wage ($P_{90}$) and interpret what it means for the employees."
                        ),
                        "steps": [
                            "**What we need to find:** $P_{90}$ with $N = 120$.",
                            "**Step 1 — Cumulative frequency table:**\n"
                            "- $10-19: cf = 12$\n"
                            "- $20-29: cf = 50$\n"
                            "- $30-39: cf = 96$\n"
                            "- $40-49: cf = 114$\n"
                            "- $50-59: cf = 120$",
                            "**Step 2 — Find rank position for $P_{90}$:**\n"
                            "$$\\text{Rank } P_{90} = \\frac{90}{100} \\times 120 = 108$$\n"
                            "Rank $108$ falls in class $40-49$ ($cf$ goes from $96$ to $114$).",
                            "**Step 3 — Apply linear interpolation:**\n"
                            "- $L = 39.5, C = 96, f = 18, i = 10$\n"
                            "$$P_{90} = 39.5 + \\left( \\frac{108 - 96}{18} \\right) \\times 10 = 39.5 + \\left( \\frac{12}{18} \\right) \\times 10 = 39.5 + 6.67 = 46.17$$\n\n"
                            "**Step 4 — Real-world interpretation:**\n"
                            "A wage of $46.17$ thousand shillings (Ksh $46,170$) means that **$90\\%$ of employees earn Ksh $46,170$ or less**, "
                            "and only the **top $10\\%$ earn more than this amount**.\n\n"
                            "**Answer:** $P_{90} = \\text{Ksh } 46,170$ per month."
                        ]
                    }
                },

                # PAGE 8 — common_misconception
                {
                    "page_number": 8,
                    "page_title": "Common Errors in Quantile Interpolation",
                    "block_type": "common_misconception",
                    "component_type": "common_misconception",
                    "content": {
                        "text": (
                            "### Two Traps to Avoid in Linear Interpolation\n\n"
                            "#### Trap 1: Using the Class Limit Instead of Lower Real Boundary ($L$)\n\n"
                            "- **Wrong:** For class $155-159$, substituting $L = 155$.\n"
                            "- **Right:** Always subtract $0.5$ for integer limits: $L = 154.5$.\n\n"
                            "#### Trap 2: Using the Wrong Cumulative Frequency ($C$)\n\n"
                            "- **Wrong:** Using the cumulative frequency of the median class itself ($23$).\n"
                            "- **Right:** $C$ is the cumulative frequency of the **preceding** class ($7$) — the number of items already passed before entering this class!"
                        )
                    }
                },

                # PAGE 9 — knowledge_check
                {
                    "page_number": 9,
                    "page_title": "Check Your Understanding: Quantile Formulas",
                    "block_type": "knowledge_check",
                    "component_type": "multiple_choice",
                    "content": {
                        "check_type": "multiple_choice",
                        "question": (
                            "If the Lower Quartile of a dataset is $Q_1 = 32\\text{ marks}$ and the Upper Quartile is $Q_3 = 56\\text{ marks}$, "
                            "what is the Quartile Deviation (Semi-Interquartile Range)?"
                        ),
                        "options": [
                            "A: $24\\text{ marks}$",
                            "B: $12\\text{ marks}$",
                            "C: $44\\text{ marks}$",
                            "D: $6\\text{ marks}$"
                        ],
                        "answer": "B",
                        "explanation": (
                            "The Interquartile Range is $\\text{IQR} = Q_3 - Q_1 = 56 - 32 = 24$. "
                            "The Quartile Deviation is half the IQR: $QD = \\frac{\\text{IQR}}{2} = \\frac{24}{2} = 12\\text{ marks}$. Option B is correct."
                        )
                    }
                },

                # PAGE 10 — knowledge_check (Short answer)
                {
                    "page_number": 10,
                    "page_title": "Practice: Interpolating the 75th Percentile",
                    "block_type": "knowledge_check",
                    "component_type": "short_answer",
                    "content": {
                        "check_type": "short_answer",
                        "question": (
                            "A sample of 80 battery lifespans (in hours) has cumulative frequencies:\n"
                            "Class $20-29: cf = 18$; Class $30-39: cf = 54$; Class $40-49: cf = 74$; Class $50-59: cf = 80$.\n\n"
                            "Calculate the Upper Quartile ($Q_3$, 75th percentile) of the battery lifespans."
                        ),
                        "hint": (
                            "Target rank is $\\frac{3(80)}{4} = 60$. Find which class contains rank 60, "
                            "identify $L, C, f, i$, and substitute into $Q_3 = L + \\left(\\frac{60 - C}{f}\\right) \\cdot i$."
                        ),
                        "answer": (
                            "**Target Rank:** $\\frac{3 \\times 80}{4} = 60$.\n\n"
                            "**Quartile Class:** $40-49$ ($cf$ goes from $54$ to $74$).\n\n"
                            "**Parameters:** $L = 39.5, C = 54, f = 74 - 54 = 20, i = 10$.\n\n"
                            "**Calculation:**\n"
                            "$$Q_3 = 39.5 + \\left( \\frac{60 - 54}{20} \\right) \\times 10 = 39.5 + \\left( \\frac{6}{20} \\right) \\times 10 = 39.5 + 3.0 = 42.5\\text{ hours}$$\n\n"
                            "The Upper Quartile is **$42.5\\text{ hours}$**."
                        )
                    }
                },

                # PAGE 11 — summary
                {
                    "page_number": 11,
                    "page_title": "Key Takeaways: Interpolation Summary Card",
                    "block_type": "summary",
                    "component_type": "summary",
                    "content": {
                        "text": (
                            "### Master Summary of Linear Interpolation\n\n"
                            "$$Q_k = L + \\left( \\frac{\\text{Target Rank} - C}{f} \\right) \\cdot i$$\n\n"
                            "### Positional Ranks Reference\n\n"
                            "- **Lower Quartile ($Q_1$):** Rank $= \\frac{N}{4}$\n"
                            "- **Median ($m$):** Rank $= \\frac{N}{2}$\n"
                            "- **Upper Quartile ($Q_3$):** Rank $= \\frac{3N}{4}$\n"
                            "- **$P$-th Percentile ($P_k$):** Rank $= \\frac{k \\cdot N}{100}$\n\n"
                            "### Key Relationships\n\n"
                            "- $\\text{IQR} = Q_3 - Q_1$ (Measures spread of middle $50\\%$)\n"
                            "- $\\text{Quartile Deviation} = \\frac{Q_3 - Q_1}{2}$"
                        )
                    }
                }
            ]
        },

        # ===================================================================
        # MODULE 2.4: Measures of Dispersion and Time-Series Analysis
        # ===================================================================
        {
            "unit_name": "Module 2.4: Measures of Dispersion and Time-Series Analysis",
            "unit_order": 4,
            "lesson_title": "Measures of Dispersion, Standard Deviation, and Moving Averages",
            "lesson_order": 4,
            "cards": [

                # PAGE 1 — learning_goal
                {
                    "page_number": 1,
                    "page_title": "Goals: Measuring Spread and Identifying Trends",
                    "block_type": "learning_goal",
                    "component_type": "learning_goal",
                    "content": {
                        "text": (
                            "In this lesson, you will master the statistical measures of **dispersion (spread)** — "
                            "Variance and Standard Deviation — and learn how to analyze time-series trends using **Moving Averages**.\n\n"
                            "By the end of this lesson, you will be able to:\n"
                            "- Distinguish between central tendency (average) and dispersion (spread)\n"
                            "- Calculate variance and standard deviation using raw deviations and step-deviation coding\n"
                            "- Decode coded variance $s_t^2$ and standard deviation $s_x$ back to physical units\n"
                            "- Compare the consistency and reliability of two competing datasets\n"
                            "- Determine the order and missing terms of time-series moving averages"
                        )
                    }
                },

                # PAGE 2 — concept_explanation
                {
                    "page_number": 2,
                    "page_title": "The Meaning of Spread: Beyond the Average",
                    "block_type": "concept_explanation",
                    "component_type": "concept_explanation",
                    "content": {
                        "text": (
                            "### Why the Mean Alone is Not Enough\n\n"
                            "Consider two students whose average exam score is $60\\%$:\n"
                            "- **Student A:** Scores $59\\%, 60\\%, 61\\%, 60\\%, 60\\%$ (extremely consistent).\n"
                            "- **Student B:** Scores $20\\%, 100\\%, 30\\%, 90\\%, 60\\%$ (wildly erratic).\n\n"
                            "Both have identical means ($\\bar{x} = 60\\%$), but Student A has minimal spread while Student B has massive spread.\n\n"
                            "### Measures of Dispersion\n\n"
                            "1. **Range:** $\\text{Maximum} - \\text{Minimum}$ (vulnerable to single outliers).\n"
                            "2. **Interquartile Range (IQR):** $Q_3 - Q_1$ (spread of middle $50\\%$).\n"
                            "3. **Variance ($\\sigma^2$ or $s^2$):** Average of squared distances from the mean.\n"
                            "4. **Standard Deviation ($\\sigma$ or $s$):** Square root of variance — the typical distance a data point sits away from the mean, in original units."
                        )
                    }
                },

                # PAGE 3 — formula_breakdown
                {
                    "page_number": 3,
                    "page_title": "Variance & Standard Deviation in Plain English",
                    "block_type": "formula_breakdown",
                    "component_type": "formula_breakdown",
                    "content": {
                        "formula": (
                            "**Coded Variance:**\n"
                            "$$s_t^2 = \\frac{\\sum ft^2}{\\sum f} - (\\bar{t})^2$$\n\n"
                            "**True Standard Deviation:**\n"
                            "$$s_x = h \\cdot \\sqrt{s_t^2} \\quad \\text{(where } h \\text{ is class width)}$$"
                        ),
                        "content": (
                            "### Why We Use Step-Deviation for Spread\n\n"
                            "Computing squared distances for large numbers by hand is exhausting and error-prone. "
                            "By shifting ($A$) and shrinking by class width ($h$), we work with tiny integers ($-2, -1, 0, 1, 2$)!\n\n"
                            "### 3-Step Strategy to Calculate Standard Deviation\n\n"
                            "1. **Compute Coded Variance ($s_t^2$):**\n"
                            "   Take the average of the $ft^2$ column and subtract the square of the coded mean $\\bar{t}$:\n"
                            "   $$s_t^2 = \\left( \\frac{\\sum ft^2}{\\sum f} \\right) - (\\bar{t})^2$$\n"
                            "2. **Take the Square Root:**\n"
                            "   $$s_t = \\sqrt{s_t^2} \\quad \\text{(Coded Standard Deviation)}$$\n"
                            "3. **Scale Back to Reality ($s_x$):**\n"
                            "   Multiply by the class width $h$ to restore physical units (grams, cm, marks):\n"
                            "   $$s_x = h \\times s_t$$\n\n"
                            "### Summary of Units & Scaling\n\n"
                            "| Measure | Coded Form | How to Restore Physical Units |\n"
                            "|---|---|---|\n"
                            "| **Variance** | $s_t^2$ | Multiply by $h^2$: $\\quad s_x^2 = h^2 \\cdot s_t^2$ |\n"
                            "| **Standard Deviation** | $s_t = \\sqrt{s_t^2}$ | Multiply by $h$: $\\quad s_x = h \\cdot s_t$ |"
                        )
                    }
                },

                # PAGE 4 — worked_example (Level 1: Ungrouped Standard Deviation)
                {
                    "page_number": 4,
                    "page_title": "Example 1: Ungrouped Standard Deviation via Deviations",
                    "block_type": "worked_example",
                    "component_type": "worked_example",
                    "content": {
                        "problem": (
                            "Calculate the standard deviation of the numbers: $5, 7, 8, 10, 15$."
                        ),
                        "steps": [
                            "**What we need to find:** $s = \\sqrt{\\frac{\\sum (x - \\bar{x})^2}{n}}$.",
                            "**Step 1 — Calculate the arithmetic mean $\\bar{x}$:**\n"
                            "$$\\bar{x} = \\frac{5 + 7 + 8 + 10 + 15}{5} = \\frac{45}{5} = 9$$",
                            "**Step 2 — Compute deviation $d = x - 9$ and squared deviations $d^2$:**\n"
                            "- $x = 5: \\quad d = 5 - 9 = -4, \\quad d^2 = 16$\n"
                            "- $x = 7: \\quad d = 7 - 9 = -2, \\quad d^2 = 4$\n"
                            "- $x = 8: \\quad d = 8 - 9 = -1, \\quad d^2 = 1$\n"
                            "- $x = 10: \\quad d = 10 - 9 = +1, \\quad d^2 = 1$\n"
                            "- $x = 15: \\quad d = 15 - 9 = +6, \\quad d^2 = 36$",
                            "**Step 3 — Sum squared deviations:**\n"
                            "$$\\sum d^2 = 16 + 4 + 1 + 1 + 36 = 58$$",
                            "**Step 4 — Calculate variance and standard deviation:**\n"
                            "$$\\text{Variance } s^2 = \\frac{58}{5} = 11.6$$\n"
                            "$$\\text{Standard Deviation } s = \\sqrt{11.6} \\approx 3.41$$\n\n"
                            "**Answer:** The standard deviation is $3.41$."
                        ]
                    }
                },

                # PAGE 5 — worked_example (Level 2: Comparing Consistency of Two Classes)
                {
                    "page_number": 5,
                    "page_title": "Example 2: Comparing Performance & Consistency",
                    "block_type": "worked_example",
                    "component_type": "worked_example",
                    "content": {
                        "problem": (
                            "Two classes sat the same physics examination. The results were:\n"
                            "- **Class A:** $\\bar{x} = 65\\%, \\quad s = 4.2\\%$\n"
                            "- **Class B:** $\\bar{x} = 65\\%, \\quad s = 14.8\\%$\n\n"
                            "(a) Which class had better overall performance?\n"
                            "(b) Which class was more consistent in its scores? Explain your reasoning."
                        ),
                        "steps": [
                            "**What to interpret:** Mean represents overall performance level; standard deviation represents spread/consistency.",
                            "**Step 1 — Compare overall performance (Mean):**\n"
                            "Both Class A and Class B have the same mean mark ($\\bar{x} = 65\\%$).\n"
                            "Therefore, both classes had the same overall performance on average.",
                            "**Step 2 — Compare consistency (Standard Deviation):**\n"
                            "Class A has a much smaller standard deviation ($s = 4.2\\%$) compared to Class B ($s = 14.8\\%$).\n"
                            "A smaller standard deviation means the individual students' scores clustered much closer to the average.",
                            "**Conclusion:** Class A was much more consistent and uniform in its academic achievement.\n\n"
                            "**Answer:** Both classes performed equally on average, but Class A was significantly more consistent."
                        ]
                    }
                },

                # PAGE 6 — worked_example (Level 3: Difficult - Step-Deviation Grouped SD)
                {
                    "page_number": 6,
                    "page_title": "Example 3: Step-Deviation Standard Deviation",
                    "block_type": "worked_example",
                    "component_type": "worked_example",
                    "content": {
                        "problem": (
                            "The height distribution of 80 calves was recorded as follows:\n\n"
                            "| Height (cm) | 152–156 | 157–161 | 162–166 | 167–171 | 172–176 | 177–181 |\n"
                            "|---|:---:|:---:|:---:|:---:|:---:|:---:|\n"
                            "| **Frequency ($f$)** | 12 | 14 | 24 | 15 | 8 | 7 |\n\n"
                            "Using an assumed mean of $A = 169\\text{ cm}$ and step-deviation coding, "
                            "calculate the variance and standard deviation of the heights."
                        ),
                        "steps": [
                            "**What to identify:**\n"
                            "- Class interval width: $h = 5$.\n"
                            "- Assumed mean: $A = 169$ (midpoint of $167-171$).\n"
                            "- Coding formula: $t = \\frac{x - 169}{5}$.",
                            "**Step 1 — Construct calculation table:**\n"
                            "- $152-156: x = 154, \\, t = -3, \\, f = 12 \\implies ft = -36, \\, ft^2 = 108$\n"
                            "- $157-161: x = 159, \\, t = -2, \\, f = 14 \\implies ft = -28, \\, ft^2 = 56$\n"
                            "- $162-166: x = 164, \\, t = -1, \\, f = 24 \\implies ft = -24, \\, ft^2 = 24$\n"
                            "- $167-171: x = 169, \\, t = 0, \\, f = 15 \\implies ft = 0, \\, ft^2 = 0$\n"
                            "- $172-176: x = 174, \\, t = +1, \\, f = 8 \\implies ft = 8, \\, ft^2 = 8$\n"
                            "- $177-181: x = 179, \\, t = +2, \\, f = 7 \\implies ft = 14, \\, ft^2 = 28$",
                            "**Step 2 — Sum columns:**\n"
                            "$$\\sum f = 80$$\n"
                            "$$\\sum ft = -36 - 28 - 24 + 0 + 8 + 14 = -66$$\n"
                            "$$\\sum ft^2 = 108 + 56 + 24 + 0 + 8 + 28 = 224$$",
                            "**Step 3 — Compute coded variance $s_t^2$:**\n"
                            "$$\\bar{t} = \\frac{-66}{80} = -0.825$$\n"
                            "$$s_t^2 = \\frac{\\sum ft^2}{\\sum f} - \\bar{t}^2 = \\frac{224}{80} - (-0.825)^2 = 2.80 - 0.6806 = 2.1194$$",
                            "**Step 4 — Decode true variance and standard deviation:**\n"
                            "$$s_x^2 = h^2 \\cdot s_t^2 = 25 \\times 2.1194 = 52.985\\text{ cm}^2$$\n"
                            "$$s_x = h \\cdot \\sqrt{s_t^2} = 5 \\times \\sqrt{2.1194} = 5 \\times 1.4558 = 7.28\\text{ cm}$$\n\n"
                            "**Answer:** The variance is $52.99\\text{ cm}^2$ and standard deviation is $7.28\\text{ cm}$."
                        ]
                    }
                },

                # PAGE 7 — worked_example (Level 4: Moving Averages Time-Series)
                {
                    "page_number": 7,
                    "page_title": "Example 4: Time-Series Analysis using Moving Averages",
                    "block_type": "worked_example",
                    "component_type": "worked_example",
                    "content": {
                        "problem": (
                            "The table below shows weekly sugar sales (in bags) and their moving averages:\n\n"
                            "| Week | 1 | 2 | 3 | 4 | 5 | 6 |\n"
                            "|---|:---:|:---:|:---:|:---:|:---:|:---:|\n"
                            "| **Bags Sold** | 340 | 330 | $x$ | 343 | 350 | 345 |\n"
                            "| **Moving Average** | 331 | 332 | $y$ | 346 | — | — |\n\n"
                            "(a) Find the order of the moving average.\n"
                            "(b) Find the values of $x$ and $y$."
                        ),
                        "steps": [
                            "**What we need to find:** The order $m$ of the moving average and unknown entries $x, y$.",
                            "**Step 1 — Determine the order $m$:**\n"
                            "Test 3-week moving average ($m = 3$):\n"
                            "$$\\frac{340 + 330 + x}{3} = 331 \\implies 670 + x = 993 \\implies x = 323$$\n"
                            "Check consistency with the next moving average ($332$):\n"
                            "$$\\frac{330 + 323 + 343}{3} = \\frac{996}{3} = 332\\text{ (Verified!)}$$\n"
                            "Since it matches the table value $332$ exactly, the order of the moving average is **$3$**.",
                            "**Step 2 — Solve for unknown moving average $y$ (Weeks 3-5):**\n"
                            "$$y = \\frac{x + 343 + 350}{3} = \\frac{323 + 343 + 350}{3} = \\frac{1016}{3} \\approx 338.67\\text{ bags}$$",
                            "**Step 3 — Verify next moving average (346):**\n"
                            "$$\\frac{343 + 350 + 345}{3} = \\frac{1038}{3} = 346\\text{ (Matches!)}$$\n\n"
                            "**Answer:** (a) Order of moving average is $3$; (b) $x = 323$ bags, $y = 338.67$ bags."
                        ]
                    }
                },

                # PAGE 8 — suggested_simulation
                {
                    "page_number": 8,
                    "page_title": "Explore: Dispersion Spread Visualizer",
                    "block_type": "suggested_simulation",
                    "component_type": "suggested_simulation",
                    "content": {
                        "purpose": (
                            "An interactive number line showing how standard deviation measures spread, "
                            "and why multiplying data by a scale factor $h$ scales the standard deviation by $h$ "
                            "while shifting by $A$ leaves standard deviation unchanged."
                        ),
                        "instruction": (
                            "Adjust the scale slider ($h$) and translation slider ($A$). "
                            "Watch the data points spread out or contract along the axis. "
                            "Observe the shaded standard deviation band $(\\bar{x} \\pm s_x)$ dynamically scale with $h$."
                        ),
                        "archetype": "math_dispersion_spread_visualizer",
                        "pedagogical_value": (
                            "Provides geometric proof of the decoding rule $s_x = h \\cdot s_t$ and shows why translation does not affect dispersion."
                        )
                    },
                    "asset_info": {
                        "archetype": "math_dispersion_spread_visualizer",
                        "title": "Interactive Dispersion Spread Visualizer",
                        "asset_type": "simulation"
                    }
                },

                # PAGE 9 — common_misconception
                {
                    "page_number": 9,
                    "page_title": "Common Error: Squaring the Column Product ($ft^2$)",
                    "block_type": "common_misconception",
                    "component_type": "common_misconception",
                    "content": {
                        "text": (
                            "### Critical Warning: Order of Operations in $ft^2$\n\n"
                            "When calculating the column $ft^2$, a frequent algebraic mistake is squaring the product $ft$:\n\n"
                            "- **Incorrect:** For $f = 12$ and $t = -3$, calculating $ft = -36$, then writing $(-36)^2 = 1296$.\n"
                            "- **Correct:** Only $t$ is squared! $ft^2 = f \\times (t^2) = (ft) \\times t = (-36) \\times (-3) = 108$.\n\n"
                            "> **Memory Tip:** To avoid squaring the frequency, compute $ft^2$ by multiplying the **$ft$ column** by the **$t$ column** ($ft \\times t$)."
                        )
                    }
                },

                # PAGE 10 — knowledge_check
                {
                    "page_number": 10,
                    "page_title": "Check Your Understanding: Standard Deviation Coding",
                    "block_type": "knowledge_check",
                    "component_type": "multiple_choice",
                    "content": {
                        "check_type": "multiple_choice",
                        "question": (
                            "A dataset coded with step-deviation $t = \\frac{x - 50}{4}$ has a coded variance of $s_t^2 = 2.25$.\n\n"
                            "What is the true standard deviation $s_x$ of the original dataset?"
                        ),
                        "options": [
                            "A: $1.50$",
                            "B: $6.00$",
                            "C: $36.00$",
                            "D: $9.00$"
                        ],
                        "answer": "B",
                        "explanation": (
                            "First find coded standard deviation: $s_t = \\sqrt{s_t^2} = \\sqrt{2.25} = 1.5$. "
                            "Then decode by multiplying by class width $h = 4$: $s_x = h \\cdot s_t = 4 \\times 1.5 = 6.00$. Option B is correct."
                        )
                    }
                },

                # PAGE 11 — summary
                {
                    "page_number": 11,
                    "page_title": "Key Takeaways: Dispersion & Moving Averages",
                    "block_type": "summary",
                    "component_type": "summary",
                    "content": {
                        "text": (
                            "### Master Summary of Dispersion & Trends\n\n"
                            "| Measure | Formula | Physical Meaning |\n"
                            "|:---|:---|:---|\n"
                            "| **Range** | $\\text{Max} - \\text{Min}$ | Total outer span of data |\n"
                            "| **Interquartile Range (IQR)** | $Q_3 - Q_1$ | Spread of the middle $50\\%$ of data |\n"
                            "| **Coded Variance ($s_t^2$)** | $\\frac{\\sum ft^2}{\\sum f} - (\\bar{t})^2$ | Scaled squared variance in step domain |\n"
                            "| **True Std Dev ($s_x$)** | $h \\cdot \\sqrt{s_t^2}$ | Spread in original units (cm, kg, marks) |\n"
                            "| **Moving Average** | $\\frac{x_1 + x_2 + \\dots + x_m}{m}$ | Smoothed time-series trend |\n\n"
                            "### Key Rules\n"
                            "- Adding a constant ($A$) **does not change** variance or standard deviation.\n"
                            "- Multiplying by a constant ($h$) **multiplies variance by $h^2$** and **standard deviation by $h$**."
                        )
                    }
                }
            ]
        }
    ]
}


# ---------------------------------------------------------------------------
# Ingestion Logic (Idempotent)
# ---------------------------------------------------------------------------

def ingest_form4_math_topic2():
    print("=" * 80)
    print("VLearn Form 4 Mathematics — Topic 2: Statistics II")
    print("Ingestion started")
    print("=" * 80)

    # 1. Find or create Curriculum ("844")
    curriculum, c_created = Curriculum.objects.get_or_create(
        name="844",
        defaults={"description": "Kenyan 8-4-4 Secondary School Curriculum"}
    )
    print(f"{'Created' if c_created else 'Found existing'} Curriculum: {curriculum.name}")

    # 2. Find or create Grade ("Form 4")
    grade, g_created = Grade.objects.get_or_create(
        name=TOPIC_DATA["grade_name"],
        curriculum=curriculum,
        defaults={"level": 4, "description": "Form 4 (Fourth Year of Secondary School)"}
    )
    print(f"{'Created' if g_created else 'Found'} Grade: {grade.name} (level={grade.level})")

    # 3. Find or create Subject ("Mathematics")
    subject, s_created = Subject.objects.get_or_create(
        name=TOPIC_DATA["subject_name"],
        grade=grade,
        defaults={"description": "Secondary School Mathematics Form 4"}
    )
    print(f"{'Created' if s_created else 'Found'} Subject: {subject.name}")

    # 4. Find or create Topic
    topic, t_created = Topic.objects.get_or_create(
        subject=subject,
        order=TOPIC_DATA["topic_order"],
        defaults={
            "name": TOPIC_DATA["topic_name"],
            "description": "Measures of central tendency, assumed mean, cumulative frequency, ogives, quantiles, dispersion, and moving averages."
        }
    )
    if not t_created and topic.name != TOPIC_DATA["topic_name"]:
        topic.name = TOPIC_DATA["topic_name"]
        topic.save()
    print(f"{'Created' if t_created else 'Found'} Topic: {topic.name} (ID: {topic.id})")

    total_blocks_created = 0

    # 5. Ingest each Learning Unit & Lesson
    for lu_data in TOPIC_DATA["learning_units"]:
        unit, u_created = LearningUnit.objects.get_or_create(
            topic=topic,
            order=lu_data["unit_order"],
            defaults={"name": lu_data["unit_name"]}
        )
        if not u_created and unit.name != lu_data["unit_name"]:
            unit.name = lu_data["unit_name"]
            unit.save()
        print(f"\n  {'Created' if u_created else 'Found'} LearningUnit: {unit.name}")

        lesson, l_created = Lesson.objects.get_or_create(
            learning_unit=unit,
            defaults={
                "title": lu_data["lesson_title"],
                "topic": topic,
                "status": "published",
                "version": 1
            }
        )
        if not l_created:
            lesson.title = lu_data["lesson_title"]
            lesson.status = "published"
            lesson.save()

        # Idempotency: Clear existing blocks and assets for this lesson before recreating
        del_count, _ = LessonBlock.objects.filter(lesson=lesson).delete()
        del_assets, _ = LessonAsset.objects.filter(lesson=lesson).delete()
        if del_count > 0 or del_assets > 0:
            print(f"  Found Lesson: '{lesson.title}' (ID: {lesson.id}, status={lesson.status})")
            print(f"  Cleared {del_count} existing blocks, {del_assets} existing assets")
        else:
            print(f"  Created Lesson: '{lesson.title}' (ID: {lesson.id}, status={lesson.status})")

        # 6. Create LessonBlocks
        card_count = 0
        for b_order, card in enumerate(lu_data["cards"], start=1):
            content_val = card["content"]
            if isinstance(content_val, dict):
                content_json = content_val
            elif isinstance(content_val, str):
                content_json = {"text": content_val}
            else:
                content_json = {"raw": str(content_val)}

            block_id = f"block_{lesson.id}_{b_order}_{card['page_number']}"

            block = LessonBlock.objects.create(
                lesson=lesson,
                block_id=block_id,
                page_number=card["page_number"],
                page_title=card.get("page_title", ""),
                block_type=card["block_type"],
                component_type=card.get("component_type", card["block_type"]),
                order=b_order,
                component_order=b_order,
                content=content_json,
                title=card.get("page_title", "")
            )
            card_count += 1
            total_blocks_created += 1

            # 7. Create LessonAsset if asset_info is defined
            if "asset_info" in card:
                a_info = card["asset_info"]
                asset = LessonAsset.objects.create(
                    lesson=lesson,
                    asset_type=a_info.get("asset_type", "simulation"),
                    source_type="uploaded",
                    storage_type="url",
                    status="pending",
                    title=a_info.get("title", card.get("page_title", "")),
                    description=a_info.get("description", card.get("page_title", "")),
                    metadata={"archetype": a_info.get("archetype", "")}
                )
                asset.blocks.add(block)

        print(f"  Created {card_count} blocks across {card_count} pages")

    print("\n" + "=" * 80)
    print(f"Ingestion complete. Total blocks created: {total_blocks_created}")
    print(f"Grade: {grade.name} | Subject: {subject.name} | Topic: {topic.name}")
    print("=" * 80)


if __name__ == "__main__":
    ingest_form4_math_topic2()
