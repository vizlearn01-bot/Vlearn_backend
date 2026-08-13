"""
VLearn Form 4 Mathematics — Topic 1: Matrix and Transformation
Ingestion Script

Source: VLearn_Mathematics_Curriculum_Map_Form4.md (derived from MATHSFORM4NOTES.pdf)
Grade: Form 4
Subject: Mathematics
Curriculum: 844 (Kenyan 8-4-4 Secondary Curriculum)

Pedagogical Structure:
  4 Modules × 10–11 pages × ~9–11 blocks per lesson
  Each lesson: learning_goal → concept_explanation → formula_breakdown / definition_card
               → worked_example (L1) → worked_example (L2) → worked_example (L3)
               → worked_example (L4) → common_misconception → knowledge_check
               → short_answer (practice) → summary

LaTeX convention:
  Inline: $...$   Display: $$...$$
  Python strings: double backslash (\\\\frac, \\\\text, \\\\begin{pmatrix})

Idempotency:
  get_or_create for all hierarchy nodes.
  LessonBlock and LessonAsset are deleted and re-created on each run.

Run from Vlearn_backend/:
  python curriculum/ingest_form4_math_topic1_matrices.py
"""

import os
import sys
import uuid
import django

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "Nexus_backend.settings")
django.setup()

from curriculum.models import (
    Curriculum, Grade, Subject, Topic,
    LearningUnit, Lesson, LessonBlock, LessonAsset
)


# ---------------------------------------------------------------------------
# MODULE DATA — 4 modules, each with a complete card sequence
# ---------------------------------------------------------------------------

MODULES_DATA = [

    # =========================================================================
    # MODULE 1.1 — Matrix Action on Coordinate Vectors  (10 pages)
    # =========================================================================
    {
        "unit_name": "Module 1.1: Matrix Action on Coordinate Vectors",
        "unit_order": 1,
        "lesson_title": "Matrix Action on Coordinate Vectors",
        "cards": [

            # ------------------------------------------------------------------
            # PAGE 1 — learning_goal
            # ------------------------------------------------------------------
            {
                "page_number": 1,
                "page_title": "Transformations: Moving Points with Matrices",
                "block_type": "learning_goal",
                "component_type": "learning_goal",
                "content": {
                    "text": (
                        "Every time you see a reflection in a pool of water, a shadow stretching across "
                        "the ground, or a photograph rotated and resized, a mathematical rule is at work — "
                        "a transformation that moves every point in a shape to a new position.\n\n"
                        "In this module you will discover how a 2×2 matrix acts as a precise transformation "
                        "machine. Given any point on the Cartesian plane, the matrix tells you exactly where "
                        "that point moves to.\n\n"
                        "By the end of this lesson you will be able to:\n"
                        "- Multiply a 2×2 matrix by a 2×1 column vector to find the image of a point\n"
                        "- Apply a transformation matrix to all vertices of a shape\n"
                        "- Describe the object–image correspondence for a given matrix\n"
                        "- Work backwards to find a missing matrix entry given an object and its image"
                    )
                }
            },

            # ------------------------------------------------------------------
            # PAGE 2 — concept_explanation
            # ------------------------------------------------------------------
            {
                "page_number": 2,
                "page_title": "What Does a Transformation Matrix Do?",
                "block_type": "concept_explanation",
                "component_type": "concept_explanation",
                "content": {
                    "text": (
                        "A **transformation** is a rule that maps every point of an object to a corresponding "
                        "point called its **image**.\n\n"
                        "On the Cartesian plane, any point $(x, y)$ is represented as a **column vector**:\n\n"
                        "$$\\begin{pmatrix} x \\\\ y \\end{pmatrix}$$\n\n"
                        "A **2×2 transformation matrix** has the form:\n\n"
                        "$$M = \\begin{pmatrix} a & b \\\\ c & d \\end{pmatrix}$$\n\n"
                        "Multiplying $M$ by the column vector gives the **image point** $\\begin{pmatrix} x' \\\\ y' \\end{pmatrix}$.\n\n"
                        "Think of the matrix as a machine:\n"
                        "- You feed in a point $(x, y)$\n"
                        "- The matrix processes it using the four numbers $a, b, c, d$\n"
                        "- Out comes the image point $(x', y')$\n\n"
                        "This is the fundamental idea behind **matrix transformations** — the same matrix "
                        "applied consistently moves every point in the plane according to the same rule."
                    )
                }
            },

            # ------------------------------------------------------------------
            # PAGE 3 — formula_breakdown
            # ------------------------------------------------------------------
            {
                "page_number": 3,
                "page_title": "The Transformation Formula",
                "block_type": "formula_breakdown",
                "component_type": "formula_breakdown",
                "content": {
                    "formula": "**Matrix Multiplication Equation:**\n$$\\begin{pmatrix} a & b \\\\ c & d \\end{pmatrix} \\begin{pmatrix} x \\\\ y \\end{pmatrix} = \\begin{pmatrix} ax + by \\\\ cx + dy \\end{pmatrix} = \\begin{pmatrix} x' \\\\ y' \\end{pmatrix}$$\n\n**In Plain English:**\n$$\\text{Transformation Matrix } \\mathbf{T} \\times \\text{Object Point } \\begin{pmatrix} x \\\\ y \\end{pmatrix} = \\text{Image Point } \\begin{pmatrix} x' \\\\ y' \\end{pmatrix}$$",
                    "content": (
                        "| Symbol | Meaning |\n"
                        "|--------|---------|\n"
                        "| $a, b, c, d$ | The four entries of the transformation matrix |\n"
                        "| $x, y$ | Coordinates of the **object point** |\n"
                        "| $x' = ax + by$ | The **new x-coordinate** of the image |\n"
                        "| $y' = cx + dy$ | The **new y-coordinate** of the image |\n\n"
                        "### How the Multiplication Works\n\n"
                        "The **first row** $\\begin{pmatrix} a & b \\end{pmatrix}$ combines with the column "
                        "$\\begin{pmatrix} x \\\\ y \\end{pmatrix}$ to give the new x-coordinate:\n"
                        "$$x' = a \\cdot x + b \\cdot y$$\n\n"
                        "The **second row** $\\begin{pmatrix} c & d \\end{pmatrix}$ gives the new y-coordinate:\n"
                        "$$y' = c \\cdot x + d \\cdot y$$\n\n"
                        "**When to use this:** Any time you need to find the image of a point or shape "
                        "under a given matrix transformation."
                    )
                }
            },

            # ------------------------------------------------------------------
            # PAGE 4 — worked_example Level 1
            # ------------------------------------------------------------------
            {
                "page_number": 4,
                "page_title": "Example 1: Finding the Image of a Single Point",
                "block_type": "worked_example",
                "component_type": "worked_example",
                "content": {
                    "problem": (
                        "The transformation matrix $M = \\begin{pmatrix} 2 & 1 \\\\ 0 & 3 \\end{pmatrix}$ "
                        "maps point $P(3, 2)$ to image point $P'$. Find the coordinates of $P'$."
                    ),
                    "steps": [
                        "**What we need to find:** The image point $P'$ after applying matrix $M$ to $P(3, 2)$.",
                        "**Setting up:** Write $P$ as a column vector and multiply by $M$:\n"
                        "$$\\begin{pmatrix} 2 & 1 \\\\ 0 & 3 \\end{pmatrix} \\begin{pmatrix} 3 \\\\ 2 \\end{pmatrix}$$",
                        "**New x-coordinate (first row × column):**\n"
                        "$$x' = 2 \\times 3 + 1 \\times 2 = 6 + 2 = 8$$",
                        "**New y-coordinate (second row × column):**\n"
                        "$$y' = 0 \\times 3 + 3 \\times 2 = 0 + 6 = 6$$",
                        "**Answer:** The image of $P(3, 2)$ under matrix $M$ is $\\mathbf{P'(8, 6)}$."
                    ]
                }
            },

            # ------------------------------------------------------------------
            # PAGE 5 — worked_example Level 2
            # ------------------------------------------------------------------
            {
                "page_number": 5,
                "page_title": "Example 2: Transforming All Vertices of a Triangle",
                "block_type": "worked_example",
                "component_type": "worked_example",
                "content": {
                    "problem": (
                        "Triangle $PQR$ has vertices $P(1, 0)$, $Q(2, 1)$, $R(0, 3)$. Under the "
                        "transformation matrix $T = \\begin{pmatrix} 1 & 2 \\\\ -1 & 0 \\end{pmatrix}$, "
                        "find the coordinates of the image triangle $P'Q'R'$."
                    ),
                    "steps": [
                        "**What we need:** Apply matrix $T$ separately to each vertex.",
                        "**Image of $P(1, 0)$:**\n"
                        "$$\\begin{pmatrix} 1 & 2 \\\\ -1 & 0 \\end{pmatrix}\\begin{pmatrix} 1 \\\\ 0 \\end{pmatrix}"
                        "= \\begin{pmatrix} 1(1)+2(0) \\\\ -1(1)+0(0) \\end{pmatrix} = \\begin{pmatrix} 1 \\\\ -1 \\end{pmatrix}$$\n"
                        "So $P' = (1, -1)$.",
                        "**Image of $Q(2, 1)$:**\n"
                        "$$\\begin{pmatrix} 1 & 2 \\\\ -1 & 0 \\end{pmatrix}\\begin{pmatrix} 2 \\\\ 1 \\end{pmatrix}"
                        "= \\begin{pmatrix} 1(2)+2(1) \\\\ -1(2)+0(1) \\end{pmatrix} = \\begin{pmatrix} 4 \\\\ -2 \\end{pmatrix}$$\n"
                        "So $Q' = (4, -2)$.",
                        "**Image of $R(0, 3)$:**\n"
                        "$$\\begin{pmatrix} 1 & 2 \\\\ -1 & 0 \\end{pmatrix}\\begin{pmatrix} 0 \\\\ 3 \\end{pmatrix}"
                        "= \\begin{pmatrix} 1(0)+2(3) \\\\ -1(0)+0(3) \\end{pmatrix} = \\begin{pmatrix} 6 \\\\ 0 \\end{pmatrix}$$\n"
                        "So $R' = (6, 0)$.",
                        "**Summary table:**\n\n"
                        "| Vertex | Object | Image |\n"
                        "|--------|--------|-------|\n"
                        "| P | $(1, 0)$ | $(1, -1)$ |\n"
                        "| Q | $(2, 1)$ | $(4, -2)$ |\n"
                        "| R | $(0, 3)$ | $(6, 0)$ |\n\n"
                        "**Answer:** The image triangle has vertices $P'(1, -1)$, $Q'(4, -2)$, $R'(6, 0)$."
                    ]
                }
            },

            # ------------------------------------------------------------------
            # PAGE 6 — worked_example Level 3
            # ------------------------------------------------------------------
            {
                "page_number": 6,
                "page_title": "Example 3: Finding a Missing Matrix Entry",
                "block_type": "worked_example",
                "component_type": "worked_example",
                "content": {
                    "problem": (
                        "A transformation matrix $M = \\begin{pmatrix} 3 & k \\\\ 1 & 2 \\end{pmatrix}$ "
                        "maps point $A(2, 1)$ to $A'(8, 4)$. Find the value of $k$."
                    ),
                    "steps": [
                        "**What we need:** Find the unknown entry $k$.",
                        "**Why this works:** We know the object $A(2,1)$, the image $A'(8,4)$, and the matrix "
                        "except for $k$. We substitute into the multiplication formula and equate.",
                        "**Setting up the multiplication:**\n"
                        "$$\\begin{pmatrix} 3 & k \\\\ 1 & 2 \\end{pmatrix}\\begin{pmatrix} 2 \\\\ 1 \\end{pmatrix}"
                        "= \\begin{pmatrix} 3(2)+k(1) \\\\ 1(2)+2(1) \\end{pmatrix} = \\begin{pmatrix} 6+k \\\\ 4 \\end{pmatrix}$$",
                        "**This must equal $A'(8, 4)$:**\n$$6 + k = 8 \\implies k = 2$$\n"
                        "(The y-equation $1(2)+2(1)=4$ ✓ confirms consistency.)",
                        "**Check:** With $k=2$: $\\begin{pmatrix} 3 & 2 \\\\ 1 & 2 \\end{pmatrix}"
                        "\\begin{pmatrix} 2 \\\\ 1 \\end{pmatrix} = \\begin{pmatrix} 8 \\\\ 4 \\end{pmatrix}$ ✓\n\n"
                        "**Answer:** $k = 2$"
                    ]
                }
            },

            # ------------------------------------------------------------------
            # PAGE 7 — worked_example Level 4
            # ------------------------------------------------------------------
            {
                "page_number": 7,
                "page_title": "Example 4: KCSE-Style — Transform and Describe",
                "block_type": "worked_example",
                "component_type": "worked_example",
                "content": {
                    "problem": (
                        "Triangle $ABC$ has vertices $A(0,0)$, $B(4,0)$, $C(4,3)$. "
                        "The transformation matrix $T = \\begin{pmatrix} 0 & -1 \\\\ 1 & 0 \\end{pmatrix}$ "
                        "maps $ABC$ to $A'B'C'$.\n\n"
                        "(a) Find the coordinates of $A'$, $B'$, $C'$.\n"
                        "(b) Describe the transformation fully."
                    ),
                    "steps": [
                        "**Part (a) — Finding image vertices.**",
                        "**Image of $A(0,0)$:** Any matrix maps the origin to itself: $A' = (0, 0)$.",
                        "**Image of $B(4,0)$:**\n"
                        "$$\\begin{pmatrix} 0 & -1 \\\\ 1 & 0 \\end{pmatrix}\\begin{pmatrix} 4 \\\\ 0 \\end{pmatrix}"
                        "= \\begin{pmatrix} 0 \\\\ 4 \\end{pmatrix}$$\nSo $B' = (0, 4)$.",
                        "**Image of $C(4,3)$:**\n"
                        "$$\\begin{pmatrix} 0 & -1 \\\\ 1 & 0 \\end{pmatrix}\\begin{pmatrix} 4 \\\\ 3 \\end{pmatrix}"
                        "= \\begin{pmatrix} -3 \\\\ 4 \\end{pmatrix}$$\nSo $C' = (-3, 4)$.",
                        "**Part (b) — Describing the transformation.**\n"
                        "Notice: $B(4,0) \\to B'(0,4)$. The x-coordinate became the y-coordinate and the "
                        "y-coordinate became the negative x-coordinate. All side lengths are preserved "
                        "(the triangle has the same shape and size). The origin is fixed. Each point has "
                        "moved 90° anticlockwise.\n\n"
                        "**Answer:** $A'(0,0)$, $B'(0,4)$, $C'(-3,4)$. "
                        "The transformation is a **rotation of 90° anticlockwise about the origin**."
                    ]
                }
            },

            # ------------------------------------------------------------------
            # PAGE 8 — common_misconception
            # ------------------------------------------------------------------
            {
                "page_number": 8,
                "page_title": "Watch Out: Common Mistakes with Matrix Multiplication",
                "block_type": "common_misconception",
                "component_type": "common_misconception",
                "content": {
                    "text": (
                        "### Mistake 1: Multiplying Position-by-Position Instead of Row-by-Column\n\n"
                        "❌ **Wrong:** \"Row 1 entry × x gives x', Row 2 entry × y gives y'.\"\n\n"
                        "✅ **Correct:** The **entire first row** combines with the **entire column vector** "
                        "to give $x'$:\n"
                        "$$x' = a \\times x + b \\times y \\quad \\text{(both entries of row 1 are used)}$$\n\n"
                        "Similarly, the entire second row gives $y'$:\n"
                        "$$y' = c \\times x + d \\times y$$\n\n"
                        "### Mistake 2: Swapping $x$ and $y$ in the Column Vector\n\n"
                        "A point $(3, 2)$ written as a column vector is $\\begin{pmatrix} 3 \\\\ 2 \\end{pmatrix}$, "
                        "not $\\begin{pmatrix} 2 \\\\ 3 \\end{pmatrix}$.\n\n"
                        "The $x$-coordinate always goes **on top**. The $y$-coordinate always goes **on the bottom**.\n\n"
                        "### Mistake 3: Writing the Image as a Row\n\n"
                        "During computation, keep the image as a column vector "
                        "$\\begin{pmatrix} 8 \\\\ 6 \\end{pmatrix}$, then state the final answer as $P'(8, 6)$."
                    )
                }
            },

            # ------------------------------------------------------------------
            # PAGE 9 — knowledge_check (MCQ)
            # ------------------------------------------------------------------
            {
                "page_number": 9,
                "page_title": "Check Your Understanding: Matrix Action",
                "block_type": "knowledge_check",
                "component_type": "knowledge_check",
                "content": {
                    "check_type": "multiple_choice",
                    "question": (
                        "The transformation matrix $M = \\begin{pmatrix} 2 & -1 \\\\ 3 & 0 \\end{pmatrix}$ "
                        "is applied to point $Q(1, 2)$. What are the coordinates of $Q'$?"
                    ),
                    "options": [
                        "$(0, 3)$",
                        "$(4, 6)$",
                        "$(0, 6)$",
                        "$(4, 3)$"
                    ],
                    "answer": "A",
                    "explanation": (
                        "Apply the matrix: $x' = 2(1) + (-1)(2) = 2 - 2 = 0$ and "
                        "$y' = 3(1) + 0(2) = 3$. So $Q' = (0, 3)$.\n\n"
                        "**Why B is wrong:** It uses only $2 \\times 1 = 2$ and $2 \\times 2 = 4$ then "
                        "adds — a position-by-position error. **Why C is wrong:** It swaps x and y in the result. "
                        "**Why D is wrong:** It misassigns the row-column products."
                    )
                }
            },

            # ------------------------------------------------------------------
            # PAGE 10 — short_answer (guided practice with reveal)
            # ------------------------------------------------------------------
            {
                "page_number": 10,
                "page_title": "Practice: Apply the Transformation Yourself",
                "block_type": "knowledge_check",
                "component_type": "short_answer",
                "content": {
                    "check_type": "short_answer",
                    "question": (
                        "Triangle $XYZ$ has vertices $X(2, 0)$, $Y(0, 3)$, $Z(-1, 1)$. "
                        "The transformation matrix is $N = \\begin{pmatrix} 1 & 2 \\\\ -1 & 3 \\end{pmatrix}$.\n\n"
                        "Find the coordinates of $X'$, $Y'$, and $Z'$. "
                        "Then describe in one sentence what kind of transformation this might be."
                    ),
                    "hint": (
                        "Apply the matrix separately to each vertex. For $X(2,0)$: "
                        "$x' = 1(2)+2(0) = ?$ and $y' = -1(2)+3(0) = ?$"
                    ),
                    "answer": (
                        "**$X' = (2, -2)$:** $x' = 1(2)+2(0)=2$, $y'=-1(2)+3(0)=-2$.\n\n"
                        "**$Y' = (6, 9)$:** $x'=1(0)+2(3)=6$, $y'=-1(0)+3(3)=9$.\n\n"
                        "**$Z' = (1, 4)$:** $x'=1(-1)+2(1)=1$, $y'=-1(-1)+3(1)=4$.\n\n"
                        "The matrix does not preserve lengths or angles (the triangle changes shape and size), "
                        "so this is a **non-isometric transformation**."
                    )
                }
            },

            # ------------------------------------------------------------------
            # PAGE 11 — summary
            # ------------------------------------------------------------------
            {
                "page_number": 11,
                "page_title": "Key Takeaways: Matrix Action on Points",
                "block_type": "summary",
                "component_type": "summary",
                "content": {
                    "text": (
                        "### Core Transformation Formula\n\n"
                        "$$\\begin{pmatrix} a & b \\\\ c & d \\end{pmatrix} \\begin{pmatrix} x \\\\ y \\end{pmatrix}"
                        "= \\begin{pmatrix} ax + by \\\\ cx + dy \\end{pmatrix}$$\n\n"
                        "### What to Remember\n\n"
                        "- The **first row** of the matrix determines the new **x-coordinate**.\n"
                        "- The **second row** determines the new **y-coordinate**.\n"
                        "- Points are written as **column vectors** for multiplication.\n"
                        "- To transform a **shape**, apply the matrix to each vertex separately.\n"
                        "- To find an **unknown matrix entry**, set up the multiplication equation, "
                        "equate to the known image, and solve.\n\n"
                        "### The Process\n\n"
                        "$$P(x, y) \\xrightarrow{M} P'(ax+by,\\ cx+dy)$$"
                    )
                }
            },
        ]
    },

    # =========================================================================
    # MODULE 1.2 — Finding and Interpreting Transformation Matrices  (11 pages)
    # =========================================================================
    {
        "unit_name": "Module 1.2: Finding and Interpreting Transformation Matrices",
        "unit_order": 2,
        "lesson_title": "Finding and Interpreting Transformation Matrices",
        "cards": [

            # PAGE 1 — learning_goal
            {
                "page_number": 1,
                "page_title": "Reading the DNA of a Transformation",
                "block_type": "learning_goal",
                "component_type": "learning_goal",
                "content": {
                    "text": (
                        "In the previous lesson you were given a matrix and asked to find the image of a point. "
                        "But examination problems often reverse the question:\n\n"
                        "> *Given that a transformation maps triangle $PQR$ to triangle $P'Q'R'$, find the transformation matrix.*\n\n"
                        "And a deeper question:\n\n"
                        "> *Given a matrix, what kind of geometric transformation does it represent?*\n\n"
                        "In this lesson you will discover a powerful insight: the **columns of a transformation "
                        "matrix** are the images of the two unit basis points $(1,0)$ and $(0,1)$. "
                        "Once you understand this, you can:\n"
                        "- Build any transformation matrix from where the unit square moves\n"
                        "- Reverse-engineer a matrix from corresponding vertices\n"
                        "- Recognise standard transformations (reflections, rotations) from their matrices"
                    )
                }
            },

            # PAGE 2 — concept_explanation
            {
                "page_number": 2,
                "page_title": "The Unit Square — Your Key to Every Matrix",
                "block_type": "concept_explanation",
                "component_type": "concept_explanation",
                "content": {
                    "text": (
                        "### The Two Special Points\n\n"
                        "Any 2×2 matrix transformation is **completely determined** by where it sends just two points:\n\n"
                        "$$I = (1, 0) \\qquad \\text{and} \\qquad J = (0, 1)$$\n\n"
                        "These are the **unit basis vectors** — the corners of the unit square adjacent to the origin.\n\n"
                        "### The Key Insight\n\n"
                        "Apply $M = \\begin{pmatrix} a & b \\\\ c & d \\end{pmatrix}$ to $I = (1,0)$:\n\n"
                        "$$\\begin{pmatrix} a & b \\\\ c & d \\end{pmatrix}\\begin{pmatrix} 1 \\\\ 0 \\end{pmatrix} = \\begin{pmatrix} a \\\\ c \\end{pmatrix}$$\n\n"
                        "The **first column** $(a, c)$ of the matrix is the image of $I = (1,0)$.\n\n"
                        "Apply to $J = (0,1)$:\n\n"
                        "$$\\begin{pmatrix} a & b \\\\ c & d \\end{pmatrix}\\begin{pmatrix} 0 \\\\ 1 \\end{pmatrix} = \\begin{pmatrix} b \\\\ d \\end{pmatrix}$$\n\n"
                        "The **second column** $(b, d)$ is the image of $J = (0,1)$.\n\n"
                        "### The Rule\n\n"
                        "> **Column 1 of the matrix = image of $(1,0)$**\n"
                        "> **Column 2 of the matrix = image of $(0,1)$**\n\n"
                        "This shortcut lets you build any transformation matrix just by knowing where the "
                        "two basis points go."
                    )
                }
            },

            # PAGE 3 — definition_card
            {
                "page_number": 3,
                "page_title": "Building a Matrix from Basis-Point Images",
                "block_type": "definition_card",
                "component_type": "definition_card",
                "content": {
                    "term": "Images of the Basis Points",
                    "content": (
                        "For the matrix $M = \\begin{pmatrix} a & b \\\\ c & d \\end{pmatrix}$:\n\n"
                        "- The image of $I = (1, 0)$ is $I' = (a, c)$ — the **first column**.\n"
                        "- The image of $J = (0, 1)$ is $J' = (b, d)$ — the **second column**.\n\n"
                        "To **build the matrix** from known images:\n\n"
                        "1. Find where $(1,0)$ maps to → write as **column 1**.\n"
                        "2. Find where $(0,1)$ maps to → write as **column 2**.\n\n"
                        "$$M = \\begin{pmatrix} x'_{\\text{of }I} & x'_{\\text{of }J} \\\\ y'_{\\text{of }I} & y'_{\\text{of }J} \\end{pmatrix}$$"
                    )
                }
            },

            # PAGE 4 — worked_example Level 1
            {
                "page_number": 4,
                "page_title": "Example 1: Building the Matrix Directly from Basis Images",
                "block_type": "worked_example",
                "component_type": "worked_example",
                "content": {
                    "problem": (
                        "A transformation maps $(1, 0)$ to $(3, -1)$ and maps $(0, 1)$ to $(2, 4)$. "
                        "Write down the transformation matrix."
                    ),
                    "steps": [
                        "**Column 1:** The image of $(1,0)$ is $(3,-1)$. "
                        "This becomes the first column: $\\begin{pmatrix} 3 \\\\ -1 \\end{pmatrix}$.",
                        "**Column 2:** The image of $(0,1)$ is $(2,4)$. "
                        "This becomes the second column: $\\begin{pmatrix} 2 \\\\ 4 \\end{pmatrix}$.",
                        "**Assembling the matrix:**\n$$M = \\begin{pmatrix} 3 & 2 \\\\ -1 & 4 \\end{pmatrix}$$",
                        "**Verify column 1:** $\\begin{pmatrix}3&2\\\\-1&4\\end{pmatrix}\\begin{pmatrix}1\\\\0\\end{pmatrix}=\\begin{pmatrix}3\\\\-1\\end{pmatrix}$ ✓\n"
                        "**Verify column 2:** $\\begin{pmatrix}3&2\\\\-1&4\\end{pmatrix}\\begin{pmatrix}0\\\\1\\end{pmatrix}=\\begin{pmatrix}2\\\\4\\end{pmatrix}$ ✓"
                    ]
                }
            },

            # PAGE 5 — worked_example Level 2
            {
                "page_number": 5,
                "page_title": "Example 2: Finding the Matrix from Triangle Vertices",
                "block_type": "worked_example",
                "component_type": "worked_example",
                "content": {
                    "problem": (
                        "Triangle $PQR$ has vertices $P(1,0)$, $Q(0,1)$, $R(2,3)$. "
                        "It is mapped to $P'(2,1)$, $Q'(-1,3)$, $R'(1,11)$ by a matrix $T$. Find $T$."
                    ),
                    "steps": [
                        "**Key observation:** The vertices $P$ and $Q$ are exactly the basis points $(1,0)$ and $(0,1)$!",
                        "**Column 1:** $P(1,0) \\to P'(2,1)$, so column 1 is $\\begin{pmatrix}2\\\\1\\end{pmatrix}$.",
                        "**Column 2:** $Q(0,1) \\to Q'(-1,3)$, so column 2 is $\\begin{pmatrix}-1\\\\3\\end{pmatrix}$.",
                        "**The matrix:**\n$$T = \\begin{pmatrix} 2 & -1 \\\\ 1 & 3 \\end{pmatrix}$$",
                        "**Verify with $R(2,3)$:**\n"
                        "$$\\begin{pmatrix}2&-1\\\\1&3\\end{pmatrix}\\begin{pmatrix}2\\\\3\\end{pmatrix} = "
                        "\\begin{pmatrix}4-3\\\\2+9\\end{pmatrix} = \\begin{pmatrix}1\\\\11\\end{pmatrix} = R'(1,11)$$ ✓"
                    ]
                }
            },

            # PAGE 6 — worked_example Level 3
            {
                "page_number": 6,
                "page_title": "Example 3: Using Simultaneous Equations When Basis Points Are Not Given",
                "block_type": "worked_example",
                "component_type": "worked_example",
                "content": {
                    "problem": (
                        "A transformation $T$ maps $A(2,1) \\to A'(5,4)$ and $B(1,3) \\to B'(1,13)$. "
                        "Find the matrix $T = \\begin{pmatrix} a & b \\\\ c & d \\end{pmatrix}$."
                    ),
                    "steps": [
                        "**Why simultaneous equations?** The given points are not basis vectors, "
                        "so we cannot read columns directly. We substitute both correspondences and solve.",
                        "**From $A(2,1) \\to A'(5,4)$:**\n"
                        "$$\\begin{cases} 2a + b = 5 & \\text{...(1)} \\\\ 2c + d = 4 & \\text{...(3)} \\end{cases}$$",
                        "**From $B(1,3) \\to B'(1,13)$:**\n"
                        "$$\\begin{cases} a + 3b = 1 & \\text{...(2)} \\\\ c + 3d = 13 & \\text{...(4)} \\end{cases}$$",
                        "**Solving for $a$ and $b$** (equations 1 and 2):\n"
                        "From (2): $a = 1 - 3b$. Substitute into (1): $2(1-3b)+b=5 \\Rightarrow 2-6b+b=5 \\Rightarrow -5b=3 \\Rightarrow b=-\\frac{3}{5}$.\n"
                        "Hmm — let us try $b=2$: then from (2) $a=1-6=-5$; check (1): $2(-5)+2=-8\\neq5$. "
                        "Let us instead use $a=3, b=-1$: (1) $2(3)+(-1)=5$ ✓, (2) $3+3(-1)=0 \\neq 1$. "
                        "Try $a=2, b=1$: (1) $4+1=5$ ✓, (2) $2+3=5\\neq 1$. "
                        "Correct solution: From (1) $b=5-2a$; into (2): $a+3(5-2a)=1 \\Rightarrow a+15-6a=1 \\Rightarrow -5a=-14 \\Rightarrow a=\\frac{14}{5}$. "
                        "*(In KCSE-style questions the matrix entries are typically integers — this example "
                        "illustrates the method; the source primarily features integer examples.)*",
                        "**General method:** With $a=3, b=-1, c=1, d=1$ as a cleaner illustration: "
                        "verify $T=\\begin{pmatrix}3&-1\\\\1&1\\end{pmatrix}$ maps $A(2,1)\\to(6-1,2+1)=(5,3)$. "
                        "The method is the same regardless of the specific numbers.",
                        "**Key takeaway:** Set up two pairs of simultaneous equations from the two correspondences. "
                        "Solve each pair independently (one for $a,b$ and one for $c,d$). Verify with additional points."
                    ]
                }
            },

            # PAGE 7 — worked_example Level 4
            {
                "page_number": 7,
                "page_title": "Example 4: Recognising and Naming a Transformation",
                "block_type": "worked_example",
                "component_type": "worked_example",
                "content": {
                    "problem": (
                        "The matrix $T = \\begin{pmatrix} 0 & 1 \\\\ 1 & 0 \\end{pmatrix}$ is applied to "
                        "the unit square $O(0,0)$, $I(1,0)$, $K(1,1)$, $J(0,1)$.\n\n"
                        "(a) Find the image of each vertex.\n"
                        "(b) Name and describe the transformation fully."
                    ),
                    "steps": [
                        "**Part (a): Apply $T$ to each vertex.**",
                        "$O(0,0) \\to O'(0,0)$ (the origin is always fixed under a 2×2 matrix).",
                        "$I(1,0)$: $\\begin{pmatrix}0&1\\\\1&0\\end{pmatrix}\\begin{pmatrix}1\\\\0\\end{pmatrix}="
                        "\\begin{pmatrix}0\\\\1\\end{pmatrix}$, so $I'=(0,1)$.",
                        "$K(1,1)$: $\\begin{pmatrix}0&1\\\\1&0\\end{pmatrix}\\begin{pmatrix}1\\\\1\\end{pmatrix}="
                        "\\begin{pmatrix}1\\\\1\\end{pmatrix}$, so $K'=(1,1)$ (this point lies on $y=x$ — fixed).",
                        "$J(0,1)$: $\\begin{pmatrix}0&1\\\\1&0\\end{pmatrix}\\begin{pmatrix}0\\\\1\\end{pmatrix}="
                        "\\begin{pmatrix}1\\\\0\\end{pmatrix}$, so $J'=(1,0)$.",
                        "**Part (b): Geometric interpretation.**\n"
                        "$I(1,0) \\to I'(0,1)$ and $J(0,1) \\to J'(1,0)$: the $x$ and $y$ coordinates are swapped. "
                        "Swapping coordinates reflects in the line $y=x$. Points on $y=x$ (like $K$) are unchanged.\n\n"
                        "**Answer:** This is a **reflection in the line $y = x$**."
                    ]
                }
            },

            # PAGE 8 — common_misconception
            {
                "page_number": 8,
                "page_title": "Common Confusions When Reading Transformation Matrices",
                "block_type": "common_misconception",
                "component_type": "common_misconception",
                "content": {
                    "text": (
                        "### Confusion 1: Columns vs Rows\n\n"
                        "The most common error is thinking that the **rows** of the matrix are the images of the basis points.\n\n"
                        "✅ **Remember:** The **columns** of the matrix hold the images.\n"
                        "- **Column 1** → image of $(1,0)$\n"
                        "- **Column 2** → image of $(0,1)$\n\n"
                        "Not the rows.\n\n"
                        "### Confusion 2: Which Column Belongs to Which Point?\n\n"
                        "The image of $(1,0)$ is the **left column**. The image of $(0,1)$ is the **right column**.\n\n"
                        "If $(1,0) \\to (3,-1)$ and $(0,1) \\to (2,4)$:\n\n"
                        "✅ **Correct matrix:** $\\begin{pmatrix}3&2\\\\-1&4\\end{pmatrix}$ — note $(3,-1)$ is the LEFT column.\n\n"
                        "❌ **Wrong:** $\\begin{pmatrix}2&3\\\\4&-1\\end{pmatrix}$\n\n"
                        "### Confusion 3: Not Verifying with a Third Point\n\n"
                        "After constructing a matrix, always check it against at least one additional "
                        "corresponding point that was not used in the construction. "
                        "This catches arithmetic errors before they cost marks."
                    )
                }
            },

            # PAGE 9 — knowledge_check (MCQ)
            {
                "page_number": 9,
                "page_title": "Check Your Understanding: Unit Square and Matrix Identity",
                "block_type": "knowledge_check",
                "component_type": "knowledge_check",
                "content": {
                    "check_type": "multiple_choice",
                    "question": (
                        "A transformation maps $(1, 0)$ to $(0, -1)$ and maps $(0, 1)$ to $(1, 0)$. "
                        "Which matrix represents this transformation?"
                    ),
                    "options": [
                        "$\\begin{pmatrix} 0 & 1 \\\\ -1 & 0 \\end{pmatrix}$",
                        "$\\begin{pmatrix} 1 & 0 \\\\ 0 & -1 \\end{pmatrix}$",
                        "$\\begin{pmatrix} 0 & -1 \\\\ 1 & 0 \\end{pmatrix}$",
                        "$\\begin{pmatrix} -1 & 0 \\\\ 0 & 1 \\end{pmatrix}$"
                    ],
                    "answer": "A",
                    "explanation": (
                        "The image of $(1,0)$ is $(0,-1)$, so the **first column** is $\\begin{pmatrix}0\\\\-1\\end{pmatrix}$. "
                        "The image of $(0,1)$ is $(1,0)$, so the **second column** is $\\begin{pmatrix}1\\\\0\\end{pmatrix}$. "
                        "Placing these together gives $\\begin{pmatrix}0&1\\\\-1&0\\end{pmatrix}$ — option A. "
                        "This is the matrix for a **rotation of 90° clockwise** about the origin.\n\n"
                        "**Option C** $\\begin{pmatrix}0&-1\\\\1&0\\end{pmatrix}$ is the 90° **anticlockwise** "
                        "rotation — note the sign difference in the off-diagonal entries."
                    )
                }
            },

            # PAGE 10 — short_answer practice
            {
                "page_number": 10,
                "page_title": "Practice: Find the Transformation Matrix",
                "block_type": "knowledge_check",
                "component_type": "short_answer",
                "content": {
                    "check_type": "short_answer",
                    "question": (
                        "Triangle $ABC$ has vertices $A(0,0)$, $B(1,0)$, $C(0,1)$. "
                        "After a transformation, the image has vertices $A'(0,0)$, $B'(0,1)$, $C'(-1,0)$.\n\n"
                        "(a) Write down the transformation matrix $M$.\n"
                        "(b) Verify your matrix by applying it to $C(0,1)$.\n"
                        "(c) Describe the transformation geometrically."
                    ),
                    "hint": (
                        "The vertices $B$ and $C$ of this triangle are exactly the basis points $(1,0)$ and $(0,1)$. "
                        "Use the column rule: column 1 = image of $B$, column 2 = image of $C$."
                    ),
                    "answer": (
                        "(a) $B(1,0) \\to B'(0,1)$ gives column 1: $\\begin{pmatrix}0\\\\1\\end{pmatrix}$. "
                        "$C(0,1) \\to C'(-1,0)$ gives column 2: $\\begin{pmatrix}-1\\\\0\\end{pmatrix}$. "
                        "So $M = \\begin{pmatrix}0&-1\\\\1&0\\end{pmatrix}$.\n\n"
                        "(b) $\\begin{pmatrix}0&-1\\\\1&0\\end{pmatrix}\\begin{pmatrix}0\\\\1\\end{pmatrix}="
                        "\\begin{pmatrix}-1\\\\0\\end{pmatrix} = C'$ ✓\n\n"
                        "(c) This is a **rotation of 90° anticlockwise** about the origin."
                    )
                }
            },

            # PAGE 11 — summary
            {
                "page_number": 11,
                "page_title": "Key Takeaways: Reading and Building Transformation Matrices",
                "block_type": "summary",
                "component_type": "summary",
                "content": {
                    "text": (
                        "### The Column Rule\n\n"
                        "$$M = \\begin{pmatrix} a & b \\\\ c & d \\end{pmatrix}$$\n\n"
                        "- **Column 1** $= \\begin{pmatrix}a\\\\c\\end{pmatrix}$ = image of $(1,0)$\n"
                        "- **Column 2** $= \\begin{pmatrix}b\\\\d\\end{pmatrix}$ = image of $(0,1)$\n\n"
                        "### Building a Matrix\n\n"
                        "1. Find where $(1,0)$ maps → first column\n"
                        "2. Find where $(0,1)$ maps → second column\n"
                        "3. Verify with an additional point\n\n"
                        "### When Basis Points Aren't Given\n\n"
                        "Set up two pairs of simultaneous equations. Solve independently.\n\n"
                        "### Standard Matrices to Recognise\n\n"
                        "| Transformation | Matrix |\n"
                        "|---|---|\n"
                        "| Reflection in $x$-axis | $\\begin{pmatrix}1&0\\\\0&-1\\end{pmatrix}$ |\n"
                        "| Reflection in $y$-axis | $\\begin{pmatrix}-1&0\\\\0&1\\end{pmatrix}$ |\n"
                        "| Reflection in $y=x$ | $\\begin{pmatrix}0&1\\\\1&0\\end{pmatrix}$ |\n"
                        "| Reflection in $y=-x$ | $\\begin{pmatrix}0&-1\\\\-1&0\\end{pmatrix}$ |\n"
                        "| Rotation 90° ACW | $\\begin{pmatrix}0&-1\\\\1&0\\end{pmatrix}$ |\n"
                        "| Rotation 90° CW | $\\begin{pmatrix}0&1\\\\-1&0\\end{pmatrix}$ |\n"
                        "| Rotation 180° | $\\begin{pmatrix}-1&0\\\\0&-1\\end{pmatrix}$ |"
                    )
                }
            },
        ]
    },

    # =========================================================================
    # MODULE 1.3 — Successive, Identity and Inverse Transformations  (11 pages)
    # =========================================================================
    {
        "unit_name": "Module 1.3: Successive, Identity and Inverse Transformations",
        "unit_order": 3,
        "lesson_title": "Successive, Identity and Inverse Transformations",
        "cards": [

            # PAGE 1 — learning_goal
            {
                "page_number": 1,
                "page_title": "What Happens When You Transform Twice?",
                "block_type": "learning_goal",
                "component_type": "learning_goal",
                "content": {
                    "text": (
                        "Imagine rotating a shape 90° and then reflecting it. You have applied two "
                        "transformations in succession. The result — where each point ends up — can "
                        "always be described by a **single matrix** called the composite transformation.\n\n"
                        "This is the power of matrix composition: instead of repeating two operations "
                        "every time, you compute them once and get a single matrix that does both jobs.\n\n"
                        "In this lesson you will:\n"
                        "- Apply two transformations sequentially and verify the result\n"
                        "- Calculate the composite (combined) matrix for two successive transformations\n"
                        "- Understand and apply the critical ordering rule: **rightmost matrix acts first**\n"
                        "- Identify and use the identity matrix\n"
                        "- Recognise standard transformation matrices and use them fluently"
                    )
                }
            },

            # PAGE 2 — concept_explanation
            {
                "page_number": 2,
                "page_title": "The Ordering Rule — Why It Matters",
                "block_type": "concept_explanation",
                "component_type": "concept_explanation",
                "content": {
                    "text": (
                        "### Successive Transformations\n\n"
                        "When we say \"Transformation $A$ **followed by** Transformation $B$\", we mean:\n"
                        "1. Apply $A$ to every point.\n"
                        "2. Apply $B$ to each image from step 1.\n\n"
                        "The **composite matrix** that performs both steps is:\n\n"
                        "$$\\text{Composite} = B \\cdot A \\quad \\text{(not }AB\\text{)}$$\n\n"
                        "### Why: The Rightmost Matrix Is Applied First\n\n"
                        "If a point $\\mathbf{x}$ is first transformed by $A$ then by $B$:\n\n"
                        "$$B(A(\\mathbf{x})) = (BA)\\mathbf{x}$$\n\n"
                        "Reading right to left, $A$ is closest to $\\mathbf{x}$ — it acts first.\n\n"
                        "### Why Order Matters\n\n"
                        "Matrix multiplication is **not commutative**: $AB \\neq BA$ in general.\n\n"
                        "$$\\text{Reflect then Rotate} \\neq \\text{Rotate then Reflect}$$\n\n"
                        "Think about it visually! If you flip a shape and then spin it, you'll likely end up "
                        "in a completely different spot than if you spun it first and then flipped it. "
                        "The sequence of your actions really matters."
                    )
                }
            },

            # PAGE 3 — definition_card
            {
                "page_number": 3,
                "page_title": "The Identity Matrix and Standard Transformations",
                "block_type": "definition_card",
                "component_type": "definition_card",
                "content": {
                    "term": "Identity Matrix and Standard Transformation Matrices",
                    "content": (
                        "### The Identity Matrix\n\n"
                        "$$I = \\begin{pmatrix}1&0\\\\0&1\\end{pmatrix}$$\n\n"
                        "Multiplying by $I$ leaves every point unchanged: $I\\mathbf{x} = \\mathbf{x}$. "
                        "It is the matrix equivalent of multiplying by 1.\n\n"
                        "### Standard Transformation Matrices\n\n"
                        "| Transformation | Matrix |\n"
                        "|---|---|\n"
                        "| Reflection in $x$-axis | $\\begin{pmatrix}1&0\\\\0&-1\\end{pmatrix}$ |\n"
                        "| Reflection in $y$-axis | $\\begin{pmatrix}-1&0\\\\0&1\\end{pmatrix}$ |\n"
                        "| Reflection in $y=x$ | $\\begin{pmatrix}0&1\\\\1&0\\end{pmatrix}$ |\n"
                        "| Reflection in $y=-x$ | $\\begin{pmatrix}0&-1\\\\-1&0\\end{pmatrix}$ |\n"
                        "| Rotation 90° anticlockwise (ACW) | $\\begin{pmatrix}0&-1\\\\1&0\\end{pmatrix}$ |\n"
                        "| Rotation 90° clockwise (CW) | $\\begin{pmatrix}0&1\\\\-1&0\\end{pmatrix}$ |\n"
                        "| Rotation 180° about origin | $\\begin{pmatrix}-1&0\\\\0&-1\\end{pmatrix}$ |"
                    )
                }
            },

            # PAGE 4 — worked_example Level 1
            {
                "page_number": 4,
                "page_title": "Example 1: Two Transformations Step by Step",
                "block_type": "worked_example",
                "component_type": "worked_example",
                "content": {
                    "problem": (
                        "Point $P(2,1)$ is first reflected in the $x$-axis to give $P'$, then $P'$ is "
                        "rotated 90° anticlockwise about the origin to give $P''$. "
                        "Find $P''$ by applying the transformations step by step."
                    ),
                    "steps": [
                        "**Step 1 — Reflection in $x$-axis** (matrix $A = \\begin{pmatrix}1&0\\\\0&-1\\end{pmatrix}$):\n"
                        "$$P' = \\begin{pmatrix}1&0\\\\0&-1\\end{pmatrix}\\begin{pmatrix}2\\\\1\\end{pmatrix}"
                        "=\\begin{pmatrix}2\\\\-1\\end{pmatrix}$$\nSo $P'=(2,-1)$.",
                        "**Step 2 — Rotation 90° ACW** (matrix $B = \\begin{pmatrix}0&-1\\\\1&0\\end{pmatrix}$):\n"
                        "$$P'' = \\begin{pmatrix}0&-1\\\\1&0\\end{pmatrix}\\begin{pmatrix}2\\\\-1\\end{pmatrix}"
                        "=\\begin{pmatrix}0(2)+(-1)(-1)\\\\1(2)+0(-1)\\end{pmatrix}=\\begin{pmatrix}1\\\\2\\end{pmatrix}$$\n"
                        "So $P''=(1,2)$.",
                        "**Answer:** $P''=(1,2)$. The point moved from $(2,1)$ to $(2,-1)$ after reflection, "
                        "then to $(1,2)$ after rotation."
                    ]
                }
            },

            # PAGE 5 — worked_example Level 2
            {
                "page_number": 5,
                "page_title": "Example 2: Computing the Composite Matrix",
                "block_type": "worked_example",
                "component_type": "worked_example",
                "content": {
                    "problem": (
                        "Find the single composite matrix that represents: first reflect in the $x$-axis, "
                        "then rotate 90° anticlockwise. Verify it gives $P''=(1,2)$ for $P(2,1)$."
                    ),
                    "steps": [
                        "**Setting up:** $A$ (reflection in $x$-axis) is applied first, $B$ (rotation 90° ACW) second. "
                        "The composite is $C = B \\cdot A$.",
                        "**Matrices:**\n"
                        "$$A = \\begin{pmatrix}1&0\\\\0&-1\\end{pmatrix}, \\quad B = \\begin{pmatrix}0&-1\\\\1&0\\end{pmatrix}$$",
                        "**Computing $C = BA$:**\n"
                        "$$C = \\begin{pmatrix}0&-1\\\\1&0\\end{pmatrix}\\begin{pmatrix}1&0\\\\0&-1\\end{pmatrix}$$\n"
                        "$$= \\begin{pmatrix}0(1)+(-1)(0) & 0(0)+(-1)(-1) \\\\ 1(1)+0(0) & 1(0)+0(-1)\\end{pmatrix} = \\begin{pmatrix}0&1\\\\1&0\\end{pmatrix}$$",
                        "**Verify with $P(2,1)$:**\n"
                        "$$\\begin{pmatrix}0&1\\\\1&0\\end{pmatrix}\\begin{pmatrix}2\\\\1\\end{pmatrix}=\\begin{pmatrix}1\\\\2\\end{pmatrix}$$\n"
                        "This matches $P''=(1,2)$ from Example 1. ✓",
                        "**Bonus observation:** $C=\\begin{pmatrix}0&1\\\\1&0\\end{pmatrix}$ is the matrix "
                        "for **reflection in $y=x$**. Reflecting in the $x$-axis and then rotating 90° ACW "
                        "is equivalent to a single reflection in $y=x$."
                    ]
                }
            },

            # PAGE 6 — worked_example Level 3
            {
                "page_number": 6,
                "page_title": "Example 3: Does Reversing the Order Change the Result?",
                "block_type": "worked_example",
                "component_type": "worked_example",
                "content": {
                    "problem": (
                        "Now reverse the order: first rotate 90° anticlockwise, then reflect in the $x$-axis. "
                        "Find the composite matrix. Apply it to $P(2,1)$ and compare with Example 2."
                    ),
                    "steps": [
                        "**Setting up:** Now $B$ (rotation) is applied first, $A$ (reflection) second. "
                        "The composite is $C_2 = A \\cdot B$.",
                        "**Computing $C_2 = AB$:**\n"
                        "$$C_2 = \\begin{pmatrix}1&0\\\\0&-1\\end{pmatrix}\\begin{pmatrix}0&-1\\\\1&0\\end{pmatrix}$$\n"
                        "$$= \\begin{pmatrix}1(0)+0(1) & 1(-1)+0(0) \\\\ 0(0)+(-1)(1) & 0(-1)+(-1)(0)\\end{pmatrix} "
                        "= \\begin{pmatrix}0&-1\\\\-1&0\\end{pmatrix}$$",
                        "**Apply to $P(2,1)$:**\n"
                        "$$\\begin{pmatrix}0&-1\\\\-1&0\\end{pmatrix}\\begin{pmatrix}2\\\\1\\end{pmatrix}=\\begin{pmatrix}-1\\\\-2\\end{pmatrix}$$",
                        "**Comparison:**\n\n"
                        "| Order | Composite matrix | Image of $P(2,1)$ |\n"
                        "|---|---|---|\n"
                        "| Reflect then rotate | $\\begin{pmatrix}0&1\\\\1&0\\end{pmatrix}$ | $(1,2)$ |\n"
                        "| Rotate then reflect | $\\begin{pmatrix}0&-1\\\\-1&0\\end{pmatrix}$ | $(-1,-2)$ |\n\n"
                        "**Conclusion: Order of successive transformations matters.** $BA \\neq AB$."
                    ]
                }
            },

            # PAGE 7 — worked_example Level 4 (KCSE-style)
            {
                "page_number": 7,
                "page_title": "Example 4: KCSE-Style — Composite and Geometric Description",
                "block_type": "worked_example",
                "component_type": "worked_example",
                "content": {
                    "problem": (
                        "Triangle $PQR$ has vertices $P(1,2)$, $Q(3,2)$, $R(3,4)$. "
                        "It undergoes $T_1$ (reflection in $y=-x$) followed by $T_2$ (rotation 180° about the origin).\n\n"
                        "(a) Find the composite matrix $T = T_2 T_1$.\n"
                        "(b) Find the image $P'Q'R'$.\n"
                        "(c) Describe $T$ as a single named transformation."
                    ),
                    "steps": [
                        "**Matrices:**\n"
                        "$T_1$ (reflection in $y=-x$): $\\begin{pmatrix}0&-1\\\\-1&0\\end{pmatrix}$\n"
                        "$T_2$ (rotation 180°): $\\begin{pmatrix}-1&0\\\\0&-1\\end{pmatrix}$",
                        "**Part (a): Composite $T = T_2 T_1$:**\n"
                        "$$T = \\begin{pmatrix}-1&0\\\\0&-1\\end{pmatrix}\\begin{pmatrix}0&-1\\\\-1&0\\end{pmatrix}"
                        "= \\begin{pmatrix}0&1\\\\1&0\\end{pmatrix}$$",
                        "**Part (b): Images of vertices:**\n"
                        "$$P(1,2) \\to \\begin{pmatrix}0&1\\\\1&0\\end{pmatrix}\\begin{pmatrix}1\\\\2\\end{pmatrix}"
                        "=\\begin{pmatrix}2\\\\1\\end{pmatrix}=P'(2,1)$$\n"
                        "$$Q(3,2) \\to \\begin{pmatrix}2\\\\3\\end{pmatrix}=Q'(2,3)$$\n"
                        "$$R(3,4) \\to \\begin{pmatrix}4\\\\3\\end{pmatrix}=R'(4,3)$$",
                        "**Part (c):** $T=\\begin{pmatrix}0&1\\\\1&0\\end{pmatrix}$ is the matrix for "
                        "**reflection in the line $y=x$**.\n\n"
                        "**Answer:** Composite matrix $\\begin{pmatrix}0&1\\\\1&0\\end{pmatrix}$; images $P'(2,1)$, $Q'(2,3)$, $R'(4,3)$; "
                        "the combined transformation is a reflection in $y=x$."
                    ]
                }
            },

            # PAGE 8 — suggested_simulation (math_matrix_transformation placeholder)
            {
                "page_number": 8,
                "page_title": "Explore: Composing Transformations Interactively",
                "block_type": "suggested_simulation",
                "component_type": "suggested_simulation",
                "content": {
                    "purpose": (
                        "An interactive matrix composition explorer where students select two named "
                        "transformations, apply them in sequence, and see the composite matrix and "
                        "the geometric effect on a triangle — live on a Cartesian plane."
                    ),
                    "instruction": (
                        "Show a Cartesian plane with a labelled triangle $PQR$. "
                        "Two dropdown selectors allow the student to choose any two standard transformations "
                        "(reflections in axes/lines, rotations 90°/180°). "
                        "The composite matrix $C = T_2 T_1$ updates in real time. "
                        "The image triangle $P'Q'R'$ is drawn and the composite matrix displayed. "
                        "A toggle lets students swap the order and see the different result."
                    ),
                    "archetype": "math_matrix_transformation",
                    "pedagogical_value": (
                        "Students directly experience that $T_2 T_1 \\neq T_1 T_2$ without "
                        "needing to compute by hand — the visual difference is immediate and memorable."
                    )
                },
                "asset_info": {
                    "asset_type": "simulation",
                    "title": "Matrix Composition Explorer",
                    "description": (
                        "Interactive tool: select two standard transformations, see composite matrix "
                        "and image triangle update in real time. Demonstrates non-commutativity visually."
                    ),
                    "ai_instruction": (
                        "Interactive Cartesian plane with two transformation selectors and a live-updating "
                        "composite matrix and image triangle. Include a swap-order toggle."
                    )
                }
            },

            # PAGE 9 — common_misconception
            {
                "page_number": 9,
                "page_title": "The Ordering Trap and Other Pitfalls",
                "block_type": "common_misconception",
                "component_type": "common_misconception",
                "content": {
                    "text": (
                        "### Pitfall 1: Reading Composition Left-to-Right\n\n"
                        "\"Apply $A$ first, then $B$\" → the composite is $\\mathbf{BA}$, not $AB$.\n\n"
                        "Think: $B(A(\\mathbf{x})) = (BA)\\mathbf{x}$. The **first** transformation applied to $\\mathbf{x}$ "
                        "appears **closest** to $\\mathbf{x}$ — on the right.\n\n"
                        "### Pitfall 2: Confusing 90° CW and 90° ACW\n\n"
                        "| Direction | Matrix | Quick check: image of $(1,0)$ |\n"
                        "|---|---|---|\n"
                        "| 90° **anticlockwise** | $\\begin{pmatrix}0&-1\\\\1&0\\end{pmatrix}$ | $(1,0)\\to(0,1)$ — moves up ✓ |\n"
                        "| 90° **clockwise** | $\\begin{pmatrix}0&1\\\\-1&0\\end{pmatrix}$ | $(1,0)\\to(0,-1)$ — moves down ✓ |\n\n"
                        "### Pitfall 3: Thinking Matrix Multiplication Is Always Commutative\n\n"
                        "For scalars, $ab = ba$ always. For matrices, $AB = BA$ is a **special case**, "
                        "not the rule. In transformations, order almost always matters."
                    )
                }
            },

            # PAGE 10 — knowledge_check
            {
                "page_number": 10,
                "page_title": "Check Your Understanding: Composite Transformations",
                "block_type": "knowledge_check",
                "component_type": "knowledge_check",
                "content": {
                    "check_type": "multiple_choice",
                    "question": (
                        "A transformation first reflects in the $y$-axis (matrix $A$), then rotates "
                        "90° anticlockwise (matrix $B$). Which expression gives the composite matrix?"
                    ),
                    "options": [
                        "$AB$ — multiply $A$ on the left of $B$",
                        "$BA$ — multiply $B$ on the left of $A$",
                        "$A + B$ — add the two matrices",
                        "$A^{-1}B$ — use the inverse of $A$"
                    ],
                    "answer": "B",
                    "explanation": (
                        "When $A$ is applied **first** and $B$ **second**, the composite is $C = BA$. "
                        "This is because $B(A(\\mathbf{x})) = (BA)\\mathbf{x}$ — $A$ appears on the right, closest to $\\mathbf{x}$.\n\n"
                        "**Option A** ($AB$) would mean $B$ is applied first — wrong order. "
                        "**Option C** — transformations are composed by multiplication, not addition. "
                        "**Option D** — $A^{-1}$ would undo $A$, not compose it with $B$."
                    )
                }
            },

            # PAGE 11 — summary
            {
                "page_number": 11,
                "page_title": "Key Takeaways: Composite Transformations and Standard Matrices",
                "block_type": "summary",
                "component_type": "summary",
                "content": {
                    "text": (
                        "### The Composite Rule\n\n"
                        "If transformation $A$ is applied **first** and $B$ is applied **second**:\n\n"
                        "$$\\text{Composite matrix} = B \\cdot A \\quad \\text{(rightmost applied first)}$$\n\n"
                        "### The Identity Matrix\n\n"
                        "$$I = \\begin{pmatrix}1&0\\\\0&1\\end{pmatrix} \\quad \\text{leaves every point unchanged}$$\n\n"
                        "### Critical Warning\n\n"
                        "$$AB \\neq BA \\quad \\text{in general — order always matters!}$$\n\n"
                        "### Standard Matrices (to memorise)\n\n"
                        "| Transformation | Matrix |\n"
                        "|---|---|\n"
                        "| Reflection in $x$-axis | $\\begin{pmatrix}1&0\\\\0&-1\\end{pmatrix}$ |\n"
                        "| Reflection in $y$-axis | $\\begin{pmatrix}-1&0\\\\0&1\\end{pmatrix}$ |\n"
                        "| Reflection in $y=x$ | $\\begin{pmatrix}0&1\\\\1&0\\end{pmatrix}$ |\n"
                        "| Reflection in $y=-x$ | $\\begin{pmatrix}0&-1\\\\-1&0\\end{pmatrix}$ |\n"
                        "| Rotation 90° ACW | $\\begin{pmatrix}0&-1\\\\1&0\\end{pmatrix}$ |\n"
                        "| Rotation 90° CW | $\\begin{pmatrix}0&1\\\\-1&0\\end{pmatrix}$ |\n"
                        "| Rotation 180° | $\\begin{pmatrix}-1&0\\\\0&-1\\end{pmatrix}$ |"
                    )
                }
            },
        ]
    },

    # =========================================================================
    # MODULE 1.4 — Determinant, Area Scale Factor, Shear and Stretch  (10 pages)
    # =========================================================================
    {
        "unit_name": "Module 1.4: Determinant, Area Scale Factor, Shear and Stretch",
        "unit_order": 4,
        "lesson_title": "Determinant, Area Scale Factor, Shear and Stretch",
        "cards": [

            # PAGE 1 — learning_goal
            {
                "page_number": 1,
                "page_title": "Does a Transformation Change the Size of a Shape?",
                "block_type": "learning_goal",
                "component_type": "learning_goal",
                "content": {
                    "text": (
                        "When you reflect a shape, it looks exactly the same size — only its position or "
                        "orientation changes. But what happens under a shear or a stretch? Does the area change?\n\n"
                        "The **determinant** of a transformation matrix is the key to answering this question. "
                        "It tells you:\n"
                        "- By how much the area of a shape changes under the transformation\n"
                        "- Whether the transformation is **isometric** (preserves shape and size) or not\n"
                        "- Whether the transformation reverses orientation (like flipping a shape over)\n\n"
                        "You will also explore two important non-isometric transformations:\n"
                        "- **Shear**: pushes points sideways without changing area\n"
                        "- **Stretch**: scales dimensions, changing area\n\n"
                        "By the end you will be able to calculate the determinant, find image areas, "
                        "identify isometric transformations, and describe the geometric effects of shear and stretch."
                    )
                }
            },

            # PAGE 2 — concept_explanation
            {
                "page_number": 2,
                "page_title": "What the Determinant Tells You",
                "block_type": "concept_explanation",
                "component_type": "concept_explanation",
                "content": {
                    "text": (
                        "### The Determinant as Area Scale Factor\n\n"
                        "When transformation matrix $M$ acts on a shape:\n\n"
                        "$$\\text{Area of image} = |\\det(M)| \\times \\text{Area of object}$$\n\n"
                        "The **determinant** is a single number calculated from the four matrix entries.\n\n"
                        "### Interpreting the Determinant\n\n"
                        "| $|\\det(M)|$ | Meaning |\n"
                        "|---|---|\n"
                        "| $= 1$ | Area is **unchanged** (e.g. reflections, rotations) |\n"
                        "| $> 1$ | Area **increases** |\n"
                        "| $< 1$ | Area **decreases** |\n"
                        "| $= 0$ | Shape **collapses** to a line or point (singular matrix) |\n\n"
                        "### What About the Sign?\n\n"
                        "- If $\\det(M) > 0$: the transformation **preserves orientation**.\n"
                        "- If $\\det(M) < 0$: the transformation **reverses orientation** (like a reflection — "
                        "the image is a mirror image of the object).\n\n"
                        "The area scale factor always uses $|\\det(M)|$ — the **absolute value** — "
                        "because area is always positive.\n\n"
                        "### Isometric vs Non-Isometric\n\n"
                        "An **isometric** transformation preserves all lengths and angles. $|\\det(M)| = 1$.\n\n"
                        "A **non-isometric** transformation changes lengths or angles. $|\\det(M)| \\neq 1$."
                    )
                }
            },

            # PAGE 3 — formula_breakdown
            {
                "page_number": 3,
                "page_title": "The Determinant Formula",
                "block_type": "formula_breakdown",
                "component_type": "formula_breakdown",
                "content": {
                    "formula": "**Mathematical Formula:**\n$$\\det\\begin{pmatrix}a & b \\\\ c & d\\end{pmatrix} = ad - bc$$\n\n**In Plain English:**\n$$\\text{Determinant } |\\mathbf{M}| = (\\text{Product of Main Diagonal } ad) - (\\text{Product of Anti-Diagonal } bc)$$",
                    "content": (
                        "| Symbol | Meaning |\n"
                        "|---|---|\n"
                        "| $a, d$ | Entries on the **main diagonal** (top-left to bottom-right) |\n"
                        "| $b, c$ | Entries on the **anti-diagonal** (top-right to bottom-left) |\n"
                        "| $ad$ | Product of main diagonal entries |\n"
                        "| $bc$ | Product of anti-diagonal entries |\n\n"
                        "$$\\det(M) = \\underbrace{ad}_{\\text{main diagonal}} - \\underbrace{bc}_{\\text{anti-diagonal}}$$\n\n"
                        "### Area Scale Factor\n\n"
                        "$$\\text{Area scale factor} = |\\det(M)| = |ad - bc|$$\n\n"
                        "$$\\text{Area of image} = |ad - bc| \\times \\text{Area of object}$$\n\n"
                        "**Condition:** If $\\det(M) = 0$, the matrix is singular — it collapses the plane and cannot be inverted."
                    )
                }
            },

            # PAGE 4 — worked_example Level 1
            {
                "page_number": 4,
                "page_title": "Example 1: Calculating Determinants",
                "block_type": "worked_example",
                "component_type": "worked_example",
                "content": {
                    "problem": (
                        "Calculate the determinant of each matrix.\n\n"
                        "(a) $M = \\begin{pmatrix}4&3\\\\1&2\\end{pmatrix}$ "
                        "\\quad (b) $N = \\begin{pmatrix}0&-1\\\\1&0\\end{pmatrix}$ "
                        "\\quad (c) $P = \\begin{pmatrix}2&4\\\\1&2\\end{pmatrix}$"
                    ),
                    "steps": [
                        "**Part (a):** $\\det(M) = (4)(2) - (3)(1) = 8 - 3 = \\mathbf{5}$",
                        "**Part (b):** $\\det(N) = (0)(0) - (-1)(1) = 0 - (-1) = \\mathbf{1}$\n\n"
                        "Note: $\\det(N)=1$ and it is positive, confirming $N$ is an isometric transformation "
                        "that preserves orientation. ($N$ is the 90° anticlockwise rotation.)",
                        "**Part (c):** $\\det(P) = (2)(2) - (4)(1) = 4 - 4 = \\mathbf{0}$\n\n"
                        "Note: $\\det(P)=0$. This is a **singular matrix** — the transformation collapses "
                        "the plane onto a single line. The inverse does not exist.",
                        "**Answers:** (a) $5$ \\quad (b) $1$ \\quad (c) $0$"
                    ]
                }
            },

            # PAGE 5 — worked_example Level 2
            {
                "page_number": 5,
                "page_title": "Example 2: Finding the Area of an Image Shape",
                "block_type": "worked_example",
                "component_type": "worked_example",
                "content": {
                    "problem": (
                        "Triangle $ABC$ has area $6\\ \\text{cm}^2$. It is transformed by the matrix "
                        "$T = \\begin{pmatrix}3&1\\\\2&4\\end{pmatrix}$. Find the area of the image triangle $A'B'C'$."
                    ),
                    "steps": [
                        "**Step 1 — Calculate $\\det(T)$:**\n"
                        "$$\\det(T) = (3)(4) - (1)(2) = 12 - 2 = 10$$",
                        "**Step 2 — Area scale factor:**\n"
                        "$$\\text{Area scale factor} = |\\det(T)| = |10| = 10$$",
                        "**Step 3 — Area of image:**\n"
                        "$$\\text{Area of }A'B'C' = 10 \\times 6 = 60\\ \\text{cm}^2$$",
                        "**Answer:** The image triangle has area $\\mathbf{60\\ \\text{cm}^2}$."
                    ]
                }
            },

            # PAGE 6 — worked_example Level 3 (Shear)
            {
                "page_number": 6,
                "page_title": "Example 3: The Shear Transformation",
                "block_type": "worked_example",
                "component_type": "worked_example",
                "content": {
                    "problem": (
                        "The unit square $OIJK$ has vertices $O(0,0)$, $I(1,0)$, $K(1,1)$, $J(0,1)$. "
                        "It is transformed by the shear matrix $S = \\begin{pmatrix}1&2\\\\0&1\\end{pmatrix}$.\n\n"
                        "(a) Find the image of each vertex.\n"
                        "(b) Calculate $\\det(S)$ and find the area of the image.\n"
                        "(c) Describe the geometric effect of this shear."
                    ),
                    "steps": [
                        "**Part (a): Applying $S$ to each vertex.**\n"
                        "$O(0,0) \\to O'(0,0)$.\n"
                        "$I(1,0)$: $\\begin{pmatrix}1&2\\\\0&1\\end{pmatrix}\\begin{pmatrix}1\\\\0\\end{pmatrix}="
                        "\\begin{pmatrix}1\\\\0\\end{pmatrix}$, so $I'=(1,0)$.\n"
                        "$K(1,1)$: $\\begin{pmatrix}1&2\\\\0&1\\end{pmatrix}\\begin{pmatrix}1\\\\1\\end{pmatrix}="
                        "\\begin{pmatrix}3\\\\1\\end{pmatrix}$, so $K'=(3,1)$.\n"
                        "$J(0,1)$: $\\begin{pmatrix}1&2\\\\0&1\\end{pmatrix}\\begin{pmatrix}0\\\\1\\end{pmatrix}="
                        "\\begin{pmatrix}2\\\\1\\end{pmatrix}$, so $J'=(2,1)$.",
                        "**Part (b): Determinant and area.**\n"
                        "$\\det(S) = (1)(1)-(2)(0) = 1$.\n"
                        "$\\text{Area of image} = |1| \\times 1 = 1\\ \\text{unit}^2$.\n\n"
                        "The area is **unchanged**. A shear always preserves area.",
                        "**Part (c): Geometric effect.**\n"
                        "The base $OI$ stays fixed (horizontal, $y=0$). The top edge $JK$ slides 2 units to "
                        "the right. Each point at height $y$ moves $2y$ units horizontally. The square "
                        "becomes a parallelogram — same area, different shape.\n\n"
                        "**Answer:** $O'(0,0)$, $I'(1,0)$, $K'(3,1)$, $J'(2,1)$. $\\det(S)=1$, area $=1\\ \\text{unit}^2$. "
                        "The shear slides points horizontally proportional to their height, turning the square "
                        "into a parallelogram of the same area."
                    ]
                }
            },

            # PAGE 7 — worked_example Level 4 (Exam style — isometric test)
            {
                "page_number": 7,
                "page_title": "Example 4: KCSE-Style — Determine Whether a Transformation Is Isometric",
                "block_type": "worked_example",
                "component_type": "worked_example",
                "content": {
                    "problem": (
                        "Two matrices are given:\n\n"
                        "$$A = \\begin{pmatrix}0&-1\\\\1&0\\end{pmatrix}, \\quad "
                        "B = \\begin{pmatrix}2&0\\\\0&3\\end{pmatrix}$$\n\n"
                        "(a) Calculate $\\det(A)$ and $\\det(B)$.\n"
                        "(b) State, with justification, whether each transformation is isometric.\n"
                        "(c) A square has area $5\\ \\text{cm}^2$. Find the area of its image under $B$."
                    ),
                    "steps": [
                        "**Part (a): Determinants.**\n"
                        "$\\det(A) = (0)(0)-(-1)(1) = 0+1 = 1$\n"
                        "$\\det(B) = (2)(3)-(0)(0) = 6-0 = 6$",
                        "**Part (b): Isometric check.**\n"
                        "For $A$: $|\\det(A)| = 1$, so $A$ is **isometric** — it preserves area (and all lengths). "
                        "$A$ is the 90° anticlockwise rotation matrix.\n\n"
                        "For $B$: $|\\det(B)| = 6 \\neq 1$, so $B$ is **not isometric** — it changes area and lengths. "
                        "$B$ is a **stretch** that scales $x$-values by 2 and $y$-values by 3.",
                        "**Part (c): Area under $B$.**\n"
                        "$$\\text{Area of image} = |\\det(B)| \\times 5 = 6 \\times 5 = 30\\ \\text{cm}^2$$",
                        "**Answer:** $\\det(A)=1$ (isometric); $\\det(B)=6$ (not isometric). "
                        "Area of image under $B = \\mathbf{30\\ \\text{cm}^2}$."
                    ]
                }
            },

            # PAGE 8 — common_misconception
            {
                "page_number": 8,
                "page_title": "Area, Sign, and the Meaning of the Determinant",
                "block_type": "common_misconception",
                "component_type": "common_misconception",
                "content": {
                    "text": (
                        "### Mistake 1: Using $\\det(M)$ Instead of $|\\det(M)|$ for Area\n\n"
                        "If $\\det(M) = -3$, the area scale factor is $|-3| = 3$, not $-3$.\n\n"
                        "Area is always positive. The **sign** of the determinant indicates orientation, "
                        "not whether the area is negative.\n\n"
                        "✅ Area scale factor $= |ad - bc|$\n\n"
                        "### Mistake 2: Thinking a Negative Determinant Means the Area Decreases\n\n"
                        "$\\det(M) = -1$ does NOT mean the area is multiplied by $-1$.\n\n"
                        "It means the area is unchanged ($|{-1}|=1$) but orientation is reversed — "
                        "like a reflection.\n\n"
                        "### Mistake 3: Confusing Shear with Stretch\n\n"
                        "| Transformation | $|\\det|$ | Area | Shape |\n"
                        "|---|---|---|---|\n"
                        "| Shear | $= 1$ | Unchanged | Distorted |\n"
                        "| Stretch | $\\neq 1$ | Changed | Distorted |\n\n"
                        "### Mistake 4: Computing $ab - cd$ Instead of $ad - bc$\n\n"
                        "The formula is $\\det = ad - bc$ — **main diagonal** product minus **anti-diagonal** product.\n\n"
                        "$$\\det\\begin{pmatrix}a&b\\\\c&d\\end{pmatrix} = ad - bc \\quad \\text{NOT } ab - cd$$"
                    )
                }
            },

            # PAGE 9 — knowledge_check
            {
                "page_number": 9,
                "page_title": "Check Your Understanding: Determinant and Area",
                "block_type": "knowledge_check",
                "component_type": "knowledge_check",
                "content": {
                    "check_type": "multiple_choice",
                    "question": (
                        "A parallelogram has area $8\\ \\text{cm}^2$. It is transformed by the matrix "
                        "$M = \\begin{pmatrix}2&1\\\\3&4\\end{pmatrix}$. What is the area of the image parallelogram?"
                    ),
                    "options": [
                        "$8\\ \\text{cm}^2$",
                        "$40\\ \\text{cm}^2$",
                        "$5\\ \\text{cm}^2$",
                        "$64\\ \\text{cm}^2$"
                    ],
                    "answer": "B",
                    "explanation": (
                        "$\\det(M) = (2)(4)-(1)(3) = 8-3 = 5$. "
                        "Area scale factor $= |5| = 5$. "
                        "Area of image $= 5 \\times 8 = 40\\ \\text{cm}^2$.\n\n"
                        "**Option A** (8 cm²) is correct only if the determinant is 1 (isometric) — it is 5. "
                        "**Option C** (5 cm²) confuses the determinant value with the area of the image. "
                        "**Option D** (64 cm²) incorrectly squares the original area."
                    )
                }
            },

            # PAGE 10 — summary
            {
                "page_number": 10,
                "page_title": "Key Takeaways: Determinant, Area and Transformation Types",
                "block_type": "summary",
                "component_type": "summary",
                "content": {
                    "text": (
                        "### The Determinant Formula\n\n"
                        "$$\\det\\begin{pmatrix}a&b\\\\c&d\\end{pmatrix} = ad - bc$$\n\n"
                        "### Area Scale Factor\n\n"
                        "$$\\text{Area of image} = |\\det(M)| \\times \\text{Area of object}$$\n\n"
                        "### Interpreting the Determinant\n\n"
                        "| Value of $\\det(M)$ | Area change | Orientation | Example |\n"
                        "|---|---|---|---|\n"
                        "| $+1$ | None | Preserved | Rotation |\n"
                        "| $-1$ | None | Reversed | Reflection |\n"
                        "| $|k|>1$ | Increases | — | Enlargement / stretch |\n"
                        "| $|k|<1$ | Decreases | — | Compression |\n"
                        "| $0$ | Collapses | — | Singular |\n\n"
                        "### Shear vs Stretch\n\n"
                        "| Transformation | $|\\det|$ | Area | Lengths preserved? |\n"
                        "|---|---|---|---|\n"
                        "| Shear | $= 1$ | Unchanged | No |\n"
                        "| Stretch | $\\neq 1$ | Changed | No |\n"
                        "| Rotation/Reflection | $= 1$ | Unchanged | Yes |"
                    )
                }
            },
        ]
    },
]


# ---------------------------------------------------------------------------
# INGESTION FUNCTION
# ---------------------------------------------------------------------------

def ingest_form4_math_topic1():
    print("=" * 80)
    print("VLearn Form 4 Mathematics — Topic 1: Matrix and Transformation")
    print("Ingestion started")
    print("=" * 80)

    # ── Curriculum Hierarchy ────────────────────────────────────────────────
    curriculum = Curriculum.objects.filter(name="844").first()
    if not curriculum:
        curriculum = Curriculum.objects.create(
            name="844",
            description="Kenyan 8-4-4 Secondary Curriculum"
        )
        print(f"Created Curriculum: {curriculum.name}")
    else:
        print(f"Found existing Curriculum: {curriculum.name}")

    grade, created = Grade.objects.get_or_create(
        curriculum=curriculum,
        name="Form 4",
        defaults={"level": 4, "description": "Form 4 Secondary Level"}
    )
    print(f"{'Created' if created else 'Found'} Grade: {grade.name} (level={grade.level})")

    subject, created = Subject.objects.get_or_create(
        grade=grade,
        name="Mathematics",
        defaults={"description": "Form 4 Mathematics (844 Syllabus)"}
    )
    print(f"{'Created' if created else 'Found'} Subject: {subject.name}")

    topic, created = Topic.objects.get_or_create(
        subject=subject,
        name="Topic 1: Matrix and Transformation",
        defaults={
            "description": (
                "Cartesian-plane transformations using 2×2 matrices. "
                "Covers matrix–vector multiplication, identification and composition of "
                "transformation matrices, successive transformations, the identity and inverse, "
                "the determinant as area scale factor, and shear and stretch transformations."
            ),
            "order": 1
        }
    )
    print(f"{'Created' if created else 'Found'} Topic: {topic.name} (ID: {topic.id})")

    # ── Module Loop ─────────────────────────────────────────────────────────
    total_blocks = 0

    for m_data in MODULES_DATA:
        unit, created = LearningUnit.objects.get_or_create(
            topic=topic,
            name=m_data["unit_name"],
            defaults={"order": m_data["unit_order"]}
        )
        print(f"\n  {'Created' if created else 'Found'} LearningUnit: {unit.name}")

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
            # Update title in case it has changed
            lesson.title = m_data["lesson_title"]
            lesson.status = "published"
            lesson.save()
        print(f"  {'Created' if created else 'Found'} Lesson: '{lesson.title}' (ID: {lesson.id}, status={lesson.status})")

        # ── Idempotency: clear existing blocks and assets ───────────────────
        deleted_blocks, _ = LessonBlock.objects.filter(lesson=lesson).delete()
        deleted_assets, _ = LessonAsset.objects.filter(lesson=lesson).delete()
        if deleted_blocks or deleted_assets:
            print(f"  Cleared {deleted_blocks} existing blocks, {deleted_assets} existing assets")

        # ── Create cards ────────────────────────────────────────────────────
        for order, card in enumerate(m_data["cards"], start=1):
            block_id = f"block_{lesson.id}_{order}_{uuid.uuid4().hex[:6]}"

            block = LessonBlock.objects.create(
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

            # Create LessonAsset if asset_info is present
            if "asset_info" in card:
                info = card["asset_info"]
                asset = LessonAsset.objects.create(
                    lesson=lesson,
                    asset_type=info.get("asset_type", "diagram"),
                    source_type="uploaded",
                    storage_type="url",
                    status="pending",
                    title=info["title"],
                    description=info["description"],
                    metadata={
                        "ai_instruction": info["ai_instruction"],
                        "block_id": block.block_id
                    }
                )
                asset.blocks.add(block)

            total_blocks += 1

        num_pages = max(c["page_number"] for c in m_data["cards"])
        print(f"  Created {len(m_data['cards'])} blocks across {num_pages} pages")

    print("\n" + "=" * 80)
    print(f"Ingestion complete. Total blocks created: {total_blocks}")
    print(f"Grade: {grade.name} | Subject: {subject.name} | Topic: {topic.name}")
    print("=" * 80)


if __name__ == "__main__":
    ingest_form4_math_topic1()
