#!/usr/bin/env python3
"""
VLearn Form 4 Mathematics — Topic 7: Loci Ingestion Script
===========================================================
Curriculum: 844
Grade: Form 4 (level=1)
Subject: Mathematics
Topic: Topic 7: Loci (order=7)

Modules / LearningUnits:
  7.1 Foundational 2D and 3D Loci: Definitions, Bisectors, and Distance Boundaries
  7.2 Conditional Loci and Geometric Inequalities: Shading Regions on Construction Grids
  7.3 Constant Angle Loci and Circle Arc Constructions
  7.4 Intersecting Loci, Intersecting Chords Theorem, and Multi-Step Constructions

Pedagogical Structure per Lesson: 11 Pages (44 blocks total)
  Page 1:  learning_goal (Student-friendly outcomes)
  Page 2:  concept_explanation (Real-world analogies: tethered goat, theater seating, crosshair navigation)
  Page 3:  formula_breakdown / definition_card (Word formulas, construction steps, algebraic theorems)
  Page 4:  worked_example (Level 1: Easy / Foundation)
  Page 5:  worked_example (Level 2: Moderate / Multi-step)
  Page 6:  worked_example (Level 3: Difficult / Exam standard)
  Page 7:  worked_example (Level 4: Exam-Style / Real-World Synthesis)
  Page 8:  suggested_simulation (Interactive visual sandbox)
  Page 9:  common_misconception (Diagnostic error analysis & memory tips)
  Page 10: knowledge_check (MCQ / Short-answer with step-by-step solutions)
  Page 11: summary (Key takeaways & construction checklist)

Standards Enforced:
  - Clean responsive Markdown tables (zero raw \\begin{array} or \\hline).
  - Explicit bold labels on all formula breakdowns.
  - Kenyan KCSE convention: Shading the UNWANTED region, leaving the target region clean/white.
  - Complete mathematical accuracy (exact radii, heights, and areas).
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


def get_topic7_data():
    """Returns the complete structured curriculum payload for Topic 7."""
    return [
        # =====================================================================
        # MODULE 7.1: Foundational 2D and 3D Loci
        # =====================================================================
        {
            "unit_order": 1,
            "unit_title": "Module 7.1: Foundational 2D and 3D Loci: Definitions, Bisectors, and Distance Boundaries",
            "lesson_title": "Foundational 2D and 3D Loci: Definitions, Bisectors, and Distance Boundaries",
            "lesson_blocks": [
                # PAGE 1 — learning_goal
                {
                    "page_number": 1,
                    "page_title": "Mastering Foundational Loci & Standard Geometric Rules",
                    "block_type": "learning_goal",
                    "component_type": "learning_goal",
                    "content": {
                        "title": "What You Will Master in This Lesson",
                        "goals": [
                            "Define a locus as a path or region traced by a point moving according to fixed geometric rules.",
                            "Construct the 4 fundamental 2D loci: concentric circle, perpendicular bisector, parallel lines with semicircular caps, and angle bisector pair.",
                            "Execute precise compass-and-ruler constructions without protractors.",
                            "Generalize 2D plane loci into 3D spatial solids (spheres, cylinders, planes)."
                        ]
                    }
                },

                # PAGE 2 — concept_explanation
                {
                    "page_number": 2,
                    "page_title": "The Tethered Goat & Highway Centerline: What is a Locus?",
                    "block_type": "concept_explanation",
                    "component_type": "concept_explanation",
                    "content": {
                        "body": (
                            "In geometry, a **locus** (plural: *loci*) is the path, line, curve, or region formed by all points "
                            "that satisfy one or more specific geometric rules.\n\n"
                            "### Intuitive Everyday Analogies\n\n"
                            "1. **The Tethered Goat (Circle Locus):**\n"
                            "   A goat tied to a stake by a $4\\text{ m}$ rope can walk anywhere inside a circle. "
                            "   The boundary of maximum reach is a **circle of radius $4\\text{ m}$** centered at the stake ($x^2 + y^2 = 16$).\n\n"
                            "2. **The Center Line of a Two-Lane Road (Perpendicular / Parallel Locus):**\n"
                            "   A car driving down the exact center of a road stays equidistant from both road shoulders at all times. "
                            "   This continuous midline is the **locus of points equidistant from two parallel lines**.\n\n"
                            "3. **Fair Boundary Between Two Cities (Perpendicular Bisector):**\n"
                            "   If two towns $A$ and $B$ agree to place a regional cell tower where residents of both towns have equal signal strength, "
                            "   the tower must be placed somewhere along the **perpendicular bisector of segment $AB$**!"
                        )
                    }
                },

                # PAGE 3 — formula_breakdown
                {
                    "page_number": 3,
                    "page_title": "Master Catalogue of Standard 2D and 3D Loci",
                    "block_type": "formula_breakdown",
                    "component_type": "formula_breakdown",
                    "content": {
                        "formula": (
                            "**Perpendicular Bisector Locus:**\n"
                            "$$\\text{dist}(P, A) = \\text{dist}(P, B) \\implies P \\text{ lies on the perpendicular bisector of } AB$$\n\n"
                            "**Circle Locus:**\n"
                            "$$\\text{dist}(P, O) = r \\implies x^2 + y^2 = r^2 \\quad \\text{(Circle of radius } r \\text{ centered at } O\\text{)}$$\n\n"
                            "**Angle Bisector Locus:**\n"
                            "$$\\text{dist}(P, L_1) = \\text{dist}(P, L_2) \\implies P \\text{ lies on the bisectors of the angles between } L_1 \\text{ and } L_2$$"
                        ),
                        "content": (
                            "### 2D vs. 3D Loci Comparison Reference\n\n"
                            "| Geometric Rule | 2D Plane Result | 3D Spatial Extension |\n"
                            "|:---|:---|:---|\n"
                            "| **At distance $r$ from fixed point $O$** | **Circle** of radius $r$ centered at $O$ | **Spherical Surface** of radius $r$ centered at $O$ |\n"
                            "| **Equidistant from two points $A$ and $B$** | **Perpendicular Bisector Line** of segment $AB$ | **Perpendicular Bisecting Plane** of segment $AB$ |\n"
                            "| **At distance $d$ from straight line $L$** | **Two Parallel Lines** at distance $d$ on either side | **Cylindrical Shell** of radius $d$ with axis $L$ |\n"
                            "| **Equidistant from two intersecting lines** | **Two Perpendicular Lines** (bisecting acute & obtuse angles) | **Two Perpendicular Planes** bisecting dihedral angles |\n"
                            "| **At distance $d$ from finite segment $AB$** | **Stadium/Capsule Track** (2 parallel lines + 2 semicircular caps) | **Cylinder with Hemispherical Ends** |"
                        )
                    }
                },

                # PAGE 4 — worked_example (Level 1: Easy / Perpendicular Bisector Construction)
                {
                    "page_number": 4,
                    "page_title": "Example 1: Constructing a Perpendicular Bisector with Ruler & Compasses",
                    "block_type": "worked_example",
                    "component_type": "worked_example",
                    "content": {
                        "problem": (
                            "Using a ruler and a pair of compasses only, construct a line segment $AB = 6\\text{ cm}$ "
                            "and draw the locus of points equidistant from $A$ and $B$."
                        ),
                        "steps": [
                            "**What we need to construct:** The perpendicular bisector of segment $AB = 6\\text{ cm}$.",
                            "**Step 1 — Draw the base segment:**\n"
                            "Draw a straight horizontal line segment $AB = 6\\text{ cm}$ using a sharp pencil and ruler.",
                            "**Step 2 — Set the compass radius:**\n"
                            "Open the compass to any radius strictly greater than half the length of $AB$ (e.g., $r = 4\\text{ cm} > 3\\text{ cm}$).",
                            "**Step 3 — Strike intersecting arcs from both endpoints:**\n"
                            "- Place the compass spike at $A$ and strike two arcs: one above and one below segment $AB$.\n"
                            "- Without altering the compass radius, place the compass spike at $B$ and strike two arcs crossing the first pair at points $P$ and $Q$.",
                            "**Step 4 — Join the arc intersections:**\n"
                            "Draw a straight line passing through $P$ and $Q$. This line $PQ$ is perpendicular to $AB$ and bisects it at the midpoint $M(3\\text{ cm}, 0)$.\n\n"
                            "**Answer:** Line $PQ$ is the required locus of all points equidistant from $A$ and $B$."
                        ]
                    }
                },

                # PAGE 5 — worked_example (Level 2: Moderate / Capsule Locus of a Finite Segment)
                {
                    "page_number": 5,
                    "page_title": "Example 2: Constructing the Full 2D Boundary Locus of a Line Segment",
                    "block_type": "worked_example",
                    "component_type": "worked_example",
                    "content": {
                        "problem": (
                            "A straight electrical cable is laid along line segment $MN = 8\\text{ cm}$. "
                            "Construct the complete locus of points that lie exactly $2.5\\text{ cm}$ away from the cable."
                        ),
                        "steps": [
                            "**What we need to construct:** The complete 2D boundary locus at distance $d = 2.5\\text{ cm}$ from segment $MN$.",
                            "**Step 1 — Construct parallel boundary lines above and below:**\n"
                            "- Erect perpendiculars at $M$ and $N$, and measure $2.5\\text{ cm}$ above and below the segment.\n"
                            "- Draw two straight parallel segments of length $8\\text{ cm}$ at distance $2.5\\text{ cm}$ on either side of $MN$.",
                            "**Step 2 — Construct rounded semicircular end caps:**\n"
                            "- Place the compass point at endpoint $M$, open radius to $2.5\\text{ cm}$, and draw a semicircle connecting the upper and lower parallel lines.\n"
                            "- Place the compass point at endpoint $N$, open radius to $2.5\\text{ cm}$, and draw a semicircle connecting the other ends.",
                            "**Step 3 — Inspect the complete boundary:**\n"
                            "The complete locus forms a continuous **stadium track (capsule)** consisting of $2$ parallel lines of length $8\\text{ cm}$ and $2$ semicircles of radius $2.5\\text{ cm}$.\n\n"
                            "**Answer:** A stadium-shaped closed boundary comprising two $8\\text{ cm}$ straight segments and two $2.5\\text{ cm}$ radius semicircles."
                        ]
                    }
                },

                # PAGE 6 — worked_example (Level 3: Difficult / Angle Bisector Pair of Intersecting Lines)
                {
                    "page_number": 6,
                    "page_title": "Example 3: Constructing the Complete Angle Bisector Locus",
                    "block_type": "worked_example",
                    "component_type": "worked_example",
                    "content": {
                        "problem": (
                            "Two straight drainage pipes $L_1$ and $L_2$ intersect at an acute angle of $60^\\circ$ at vertex $V$.\n"
                            "Construct the complete locus of points equidistant from both pipes."
                        ),
                        "steps": [
                            "**What we need to construct:** The complete locus of points equidistant from two intersecting lines.",
                            "**Step 1 — Understand the geometry of intersecting lines:**\n"
                            "Two intersecting lines form **two pairs of vertically opposite angles**: an acute pair ($60^\\circ$) and an obtuse pair ($180^\\circ - 60^\\circ = 120^\\circ$).\n"
                            "Therefore, the complete locus consists of **two perpendicular straight lines**.",
                            "**Step 2 — Construct the acute angle bisector ($B_1$):**\n"
                            "- Place the compass point at $V$ and strike arcs cutting $L_1$ and $L_2$ at $X$ and $Y$.\n"
                            "- From $X$ and $Y$, strike equal arcs intersecting at $P$.\n"
                            "- Draw line $VP$ extending indefinitely in both directions. This bisects the $60^\\circ$ angle into two $30^\\circ$ angles.",
                            "**Step 3 — Construct the obtuse angle bisector ($B_2$):**\n"
                            "- Repeat the construction on the adjacent $120^\\circ$ angle to produce line $VQ$.\n"
                            "- Line $VQ$ bisects the $120^\\circ$ angle into two $60^\\circ$ angles.",
                            "**Step 4 — Verify perpendicularity:**\n"
                            "$$\\text{Angle between } B_1 \\text{ and } B_2 = 30^\\circ + 60^\\circ = 90^\\circ$$\n\n"
                            "**Answer:** Two perpendicular straight lines intersecting at $V$, bisecting both the $60^\\circ$ and $120^\\circ$ angles."
                        ]
                    }
                },

                # PAGE 7 — worked_example (Level 4: Exam-Style / 3D Spatial Locus Generalization)
                {
                    "page_number": 7,
                    "page_title": "Example 4: Describing and Proving 3D Spatial Loci",
                    "block_type": "worked_example",
                    "component_type": "worked_example",
                    "content": {
                        "problem": (
                            "Describe accurately the locus of a point $P$ in three-dimensional space such that:\n"
                            "(a) $P$ is at a constant distance $k$ from a fixed line segment $AB$.\n"
                            "(b) $P$ is equidistant from two fixed points $A$ and $B$.\n"
                            "(c) $P$ is at a constant distance $r$ from a fixed flat plane $\\Pi$."
                        ),
                        "steps": [
                            "**What we need to describe:** The 3D geometric surfaces for each spatial locus condition.",
                            "**Step 1 — Part (a): Distance $k$ from line segment $AB$:**\n"
                            "- In 2D, the locus is a capsule (2 parallel lines + 2 semicircles).\n"
                            "- Rotating this 2D shape in 3D around the axis $AB$ generates a **cylindrical surface of radius $k$** along the length of $AB$, capped at each end by a **hemisphere of radius $k$** centered at $A$ and $B$.",
                            "**Step 2 — Part (b): Equidistant from two points $A$ and $B$ in 3D:**\n"
                            "- In 2D, the locus is the perpendicular bisector line.\n"
                            "- In 3D, all lines perpendicular to $AB$ passing through its midpoint form a complete flat plane.\n"
                            "- Therefore, the 3D locus is the **perpendicular bisecting plane** of segment $AB$.",
                            "**Step 3 — Part (c): Distance $r$ from flat plane $\\Pi$ in 3D:**\n"
                            "- In 3D, all points at distance $r$ from a plane form **two parallel planes** situated at distance $r$ above and below plane $\\Pi$.\n\n"
                            "**Answer:** (a) Cylinder of radius $k$ with hemispherical ends; (b) Perpendicular bisecting plane; (c) Two parallel planes at distance $r$ on either side."
                        ]
                    }
                },

                # PAGE 8 — suggested_simulation
                {
                    "page_number": 8,
                    "page_title": "Explore: Foundational 2D & 3D Locus Sandbox",
                    "block_type": "suggested_simulation",
                    "component_type": "suggested_simulation",
                    "content": {
                        "purpose": (
                            "An interactive 2D/3D geometry sandbox where students can drag points, lines, and segments, "
                            "and toggle locus rules (equidistant points, circles, parallel lines, angle bisectors). "
                            "A 3D rotation switch spins the 2D cross-section into its spatial 3D solid (cylinder, sphere, bisecting plane) in real-time."
                        )
                    },
                    "asset_info": {
                        "asset_type": "simulation",
                        "archetype": "math_foundational_locus_constructor",
                        "title": "Interactive Foundational 2D & 3D Locus Sandbox"
                    }
                },

                # PAGE 9 — common_misconception
                {
                    "page_number": 9,
                    "page_title": "Common Error: Stopping Angle Bisectors as Single Rays",
                    "block_type": "common_misconception",
                    "component_type": "common_misconception",
                    "content": {
                        "text": (
                            "### The Single Ray Angle Bisector Trap\n\n"
                            "When asked for the locus of points equidistant from two intersecting lines $L_1$ and $L_2$, "
                            "students often construct only **one ray** inside the acute angle.\n\n"
                            "### Why This is Incomplete:\n\n"
                            "| Characteristic | Single Ray (Incomplete) | Full Angle Bisector Locus (Correct) |\n"
                            "|:---|:---|:---|\n"
                            "| **Scope** | Only covers acute sector | Covers both acute and obtuse sectors |\n"
                            "| **Number of Lines** | 1 finite ray ❌ | **2 perpendicular infinite lines** ✓ |\n"
                            "| **Geometry** | Ignores obtuse angle | Bisects both $60^\\circ$ and $120^\\circ$ ($30^\\circ + 60^\\circ = 90^\\circ$) |\n\n"
                            "> **Rule:** The complete locus of points equidistant from two intersecting lines consists of **TWO perpendicular straight lines**."
                        )
                    }
                },

                # PAGE 10 — knowledge_check (MCQ)
                {
                    "page_number": 10,
                    "page_title": "Check Your Understanding: Loci Definitions",
                    "block_type": "knowledge_check",
                    "component_type": "multiple_choice",
                    "content": {
                        "question": "What geometric shape represents the complete 2D locus of points exactly 3 cm away from a finite straight line segment AB of length 10 cm?",
                        "options": [
                            "A: A single circle of radius 3 cm",
                            "B: Two parallel lines of length 10 cm without ends",
                            "C: A closed stadium/capsule shape consisting of two 10 cm parallel lines and two 3 cm radius semicircular caps",
                            "D: A rectangle of dimensions 10 cm by 6 cm"
                        ],
                        "answer": "C",
                        "explanation": (
                            "1. Points along the body of segment $AB$ form two parallel line segments of length $10\\text{ cm}$ at distance $3\\text{ cm}$.\n"
                            "2. Points near endpoints $A$ and $B$ sweep out two semicircular caps of radius $3\\text{ cm}$, creating a complete stadium/capsule curve."
                        )
                    }
                },

                # PAGE 11 — summary
                {
                    "page_number": 11,
                    "page_title": "Key Takeaways: Standard Loci",
                    "block_type": "summary",
                    "component_type": "summary",
                    "content": {
                        "text": (
                            "### Master Summary: 4 Fundamental 2D Loci\n\n"
                            "| Locus Description | 2D Geometry Result | Compass Construction Method |\n"
                            "|:---|:---|:---|\n"
                            "| **Distance $r$ from Point $O$** | Circle of radius $r$ | Compass on $O$, open to radius $r$. |\n"
                            "| **Equidistant from Points $A, B$** | Perpendicular bisector of $AB$ | Equal arcs from $A$ and $B$ intersecting above/below. |\n"
                            "| **Distance $d$ from Line $L$** | Two parallel lines at distance $d$ | Drop perpendiculars of length $d$ and connect. |\n"
                            "| **Equidistant from Lines $L_1, L_2$** | Two perpendicular bisecting lines | Arc from vertex cutting lines, then crossing arcs. |\n\n"
                            "**Compass Rule:** Always keep compass joints tight and pencil leads sharp for precise intersections!"
                        )
                    }
                }
            ]
        },

        # =====================================================================
        # MODULE 7.2: Conditional Loci & Geometric Inequalities
        # =====================================================================
        {
            "unit_order": 2,
            "unit_title": "Module 7.2: Conditional Loci and Geometric Inequalities: Shading Regions on Construction Grids",
            "lesson_title": "Conditional Loci and Geometric Inequalities: Shading Regions on Construction Grids",
            "lesson_blocks": [
                # PAGE 1 — learning_goal
                {
                    "page_number": 1,
                    "page_title": "Mastering Geometric Inequalities & Construction Shading",
                    "block_type": "learning_goal",
                    "component_type": "learning_goal",
                    "content": {
                        "title": "What You Will Master in This Lesson",
                        "goals": [
                            "Interpret geometric inequality expressions (e.g. $AP \\le BP$, $OP > r$, $\\text{dist}(P, AB) \\le d$).",
                            "Construct solid boundary lines/arcs for non-strict inequalities ($\\le, \\ge$) and dashed lines for strict inequalities ($<, >$).",
                            "Apply the Kenyan KCSE convention of shading the UNWANTED region to leave the target region clean and labeled.",
                            "Determine the boundaries and area of compound feasible regions on construction grids."
                        ]
                    }
                },

                # PAGE 2 — concept_explanation
                {
                    "page_number": 2,
                    "page_title": "The Exclusion Zone Analogy: Why Inequalities Are 2D Areas",
                    "block_type": "concept_explanation",
                    "component_type": "concept_explanation",
                    "content": {
                        "body": (
                            "While an **equality locus** produces a 1D line or curve, an **inequality locus** describes a full **2D region (area)** on a plane.\n\n"
                            "### The Exclusion Zone Analogy\n\n"
                            "- **'Stay at least 3 meters away from the fire ($OP \\ge 3\\text{ m}$)':**\n"
                            "  The boundary is a circle of radius $3\\text{ m}$. The valid area is the infinite sheet *outside* the circle.\n"
                            "- **'Stay closer to Town A than to Town B ($AP \\le BP$)' :**\n"
                            "  The boundary is the perpendicular bisector of $AB$. The valid area is the entire half-plane on $A$'s side of the line.\n\n"
                            "### KCSE Shading Protocol for Loci\n\n"
                            "Just like in Linear Programming, when multiple geometric inequality constraints overlap inside a polygon, "
                            "we **shade the UNWANTED region** (the side that violates the condition). "
                            "This leaves the valid target region $R$ completely clean, white, and unshaded!"
                        )
                    }
                },

                # PAGE 3 — formula_breakdown
                {
                    "page_number": 3,
                    "page_title": "Master Translation Guide: Geometric Inequalities to Shading Rules",
                    "block_type": "formula_breakdown",
                    "component_type": "formula_breakdown",
                    "content": {
                        "formula": (
                            "**Closer to Point A than Point B:**\n"
                            "$$AP \\le BP \\implies \\text{Shade } B\\text{'s side of the perpendicular bisector of } AB$$\n\n"
                            "**Outside a Distance Boundary:**\n"
                            "$$OP > r \\implies \\text{Draw dashed circle of radius } r \\text{ and shade the INSIDE (unwanted)}$$\n\n"
                            "**Closer to Line } L_1 \\text{ than Line } L_2:\n"
                            "$$\\text{dist}(P, L_1) \\le \\text{dist}(P, L_2) \\implies \\text{Shade } L_2\\text{'s side of the angle bisector}$$"
                        ),
                        "content": (
                            "### Geometric Inequality Action Reference Table\n\n"
                            "| Algebraic Inequality | Boundary Curve to Construct | KCSE Shading Action |\n"
                            "|:---|:---|:---|\n"
                            "| **$AP \\le BP$** | Perpendicular bisector of $AB$ (Solid) | Shade the half-plane on **$B$'s side** |\n"
                            "| **$AP \\ge BP$** | Perpendicular bisector of $AB$ (Solid) | Shade the half-plane on **$A$'s side** |\n"
                            "| **$OP \\le r$** | Circle radius $r$ centered at $O$ (Solid) | Shade the region **outside** the circle |\n"
                            "| **$OP > r$** | Circle radius $r$ centered at $O$ (Dashed) | Shade the region **inside** the circle |\n"
                            "| **$\\text{dist}(P, AB) \\le d$** | Parallel line at distance $d$ (Solid) | Shade the region **beyond** distance $d$ |\n"
                            "| **$\\text{dist}(P, AB) < \\text{dist}(P, BC)$** | Angle bisector of $\\angle ABC$ (Dashed) | Shade the side closer to line $BC$ |"
                        )
                    }
                },

                # PAGE 4 — worked_example (Level 1: Easy / Shading Point-Proximity in a Triangle)
                {
                    "page_number": 4,
                    "page_title": "Example 1: Shading a Simple Point-Distance Inequality",
                    "block_type": "worked_example",
                    "component_type": "worked_example",
                    "content": {
                        "problem": (
                            "In triangle $ABC$, $AB = 8\\text{ cm}$, $BC = 6\\text{ cm}$, and $\\angle ABC = 90^\\circ$.\n"
                            "Construct the locus of points $P$ inside the triangle such that $AP \\le BP$ by shading the unwanted region."
                        ),
                        "steps": [
                            "**What we need to construct:** The region inside $\\triangle ABC$ where $AP \\le BP$.",
                            "**Step 1 — Construct right-angled triangle $ABC$:**\n"
                            "Draw base $AB = 8\\text{ cm}$. Erect a $90^\\circ$ perpendicular at $B$ of length $BC = 6\\text{ cm}$. Join $AC = 10\\text{ cm}$.",
                            "**Step 2 — Identify the boundary of $AP \\le BP$:**\n"
                            "The equality boundary $AP = BP$ is the **perpendicular bisector of segment $AB$**.",
                            "**Step 3 — Construct the perpendicular bisector:**\n"
                            "From $A$ and $B$, strike intersecting arcs of radius $r > 4\\text{ cm}$. "
                            "Draw a solid vertical line through the midpoint $M(4\\text{ cm}, 0)$ parallel to $BC$.",
                            "**Step 4 — Shade the UNWANTED region:**\n"
                            "- $AP \\le BP$ means points must be closer to $A$ than to $B$.\n"
                            "- Therefore, the region on $B$'s side of the perpendicular bisector ($x > 4\\text{ cm}$) is **UNWANTED**.\n"
                            "- Shade the entire right half of triangle $ABC$, leaving the left half clean and labeled $P$.\n\n"
                            "**Answer:** The unshaded left region of $\\triangle ABC$ (between $x = 0$ and $x = 4\\text{ cm}$) represents locus $P$."
                        ]
                    }
                },

                # PAGE 5 — worked_example (Level 2: Moderate / Compound Triangle Inequality Region)
                {
                    "page_number": 5,
                    "page_title": "Example 2: Constructing a Compound Two-Condition Inequality Region",
                    "block_type": "worked_example",
                    "component_type": "worked_example",
                    "content": {
                        "problem": (
                            "Within triangle $ABC$ where $AB = 8\\text{ cm}$, $BC = 7.5\\text{ cm}$, and $AC = 7\\text{ cm}$, "
                            "shade the region $P$ such that:\n"
                            "(a) $AP \\le BP$\n"
                            "(b) $AP > 3\\text{ cm}$"
                        ),
                        "steps": [
                            "**What we need to construct:** The compound region $P$ satisfying both $AP \\le BP$ and $AP > 3\\text{ cm}$.",
                            "**Step 1 — Construct triangle $ABC$:**\n"
                            "Draw $AB = 8\\text{ cm}$. With compass set to $7.5\\text{ cm}$ from $B$ and $7\\text{ cm}$ from $A$, strike arcs to locate $C$. Join $AC$ and $BC$.",
                            "**Step 2 — Construct Boundary 1 ($AP \\le BP$):**\n"
                            "- Construct the perpendicular bisector of segment $AB$.\n"
                            "- Since $AP \\le BP$, points closer to $B$ are unwanted. Shade the half-plane on **$B$'s side** of the line.",
                            "**Step 3 — Construct Boundary 2 ($AP > 3\\text{ cm}$):**\n"
                            "- Place the compass at $A$, open radius to $3\\text{ cm}$, and draw a **dashed circular arc** inside the triangle.\n"
                            "- Since $AP > 3\\text{ cm}$, points inside the circle ($AP \\le 3\\text{ cm}$) are unwanted.\n"
                            "- Shade the interior of the circular sector at vertex $A$.",
                            "**Step 4 — Label the feasible region:**\n"
                            "The remaining unshaded, clean white zone between the $3\\text{ cm}$ circular arc and the perpendicular bisector is labeled **$P$**.\n\n"
                            "**Answer:** The unshaded region $P$ is bounded by the $3\\text{ cm}$ dashed arc and the solid perpendicular bisector."
                        ]
                    }
                },

                # PAGE 6 — worked_example (Level 3: Difficult / Line Proximity & Area Constraints)
                {
                    "page_number": 6,
                    "page_title": "Example 3: Inequality Involving Angle Bisectors and Height Limits",
                    "block_type": "worked_example",
                    "component_type": "worked_example",
                    "content": {
                        "problem": (
                            "In a parallelogram $ABCD$ with $AB = 10\\text{ cm}$, $BC = 6\\text{ cm}$, and $\\angle DAB = 60^\\circ$:\n"
                            "Construct the region $R$ inside the parallelogram such that:\n"
                            "(a) $\\text{dist}(P, AB) \\le \\text{dist}(P, AD)$\n"
                            "(b) $\\text{dist}(P, AB) \\le 3\\text{ cm}$"
                        ),
                        "steps": [
                            "**What we need to construct:** The feasible region $R$ satisfying both line-proximity and height inequalities.",
                            "**Step 1 — Construct parallelogram $ABCD$:**\n"
                            "Draw $AB = 10\\text{ cm}$. At $A$, construct a $60^\\circ$ angle and mark $AD = 6\\text{ cm}$. Complete the parallelogram.",
                            "**Step 2 — Construct Boundary 1 (Angle Bisector):**\n"
                            "- $\\text{dist}(P, AB) \\le \\text{dist}(P, AD) \\implies P$ must lie closer to line $AB$ than to line $AD$.\n"
                            "- Construct the angle bisector of $\\angle DAB = 60^\\circ$ (dividing it into two $30^\\circ$ angles).\n"
                            "- Shade the unwanted region above the bisector (closer to $AD$).",
                            "**Step 3 — Construct Boundary 2 (Parallel Line at $3\\text{ cm}$):**\n"
                            "- Drop a perpendicular from $AB$ of height $3\\text{ cm}$ and construct a line parallel to $AB$.\n"
                            "- Since $\\text{dist}(P, AB) \\le 3\\text{ cm}$, shade the unwanted region above this parallel line.",
                            "**Step 4 — Label the feasible region $R$:**\n"
                            "Label the clean, unshaded quadrilateral region near base $AB$ as **$R$**.\n\n"
                            "**Answer:** The unshaded region $R$ below both the $30^\\circ$ angle bisector and the $3\\text{ cm}$ parallel line."
                        ]
                    }
                },

                # PAGE 7 — worked_example (Level 4: Exam-Style / Full 10-Mark Multi-Locus Plot)
                {
                    "page_number": 7,
                    "page_title": "Example 4: Real Estate Estate Boundary Construction (KCSE Standard)",
                    "block_type": "worked_example",
                    "component_type": "worked_example",
                    "content": {
                        "problem": (
                            "A ranch is modeled by quadrilateral $ABCD$ where $AB = 9\\text{ cm}$, $BC = 7\\text{ cm}$, $CD = 6\\text{ cm}$, $\\angle ABC = 120^\\circ$, and $\\angle DAB = 90^\\circ$.\n"
                            "Construct the ranch and locate the shaded region $T$ for a water borehole such that:\n"
                            "(a) $T$ is closer to boundary $AB$ than to boundary $BC$.\n"
                            "(b) $T$ is at a distance of at least $4\\text{ cm}$ from corner $A$.\n"
                            "(c) $T$ is not more than $5\\text{ cm}$ from boundary $AB$.\n"
                            "Shade the unwanted region and label $T$."
                        ),
                        "steps": [
                            "**What we need to construct:** Full quadrilateral and 3-constraint feasible region $T$.",
                            "**Step 1 — Construct quadrilateral $ABCD$:**\n"
                            "Draw $AB = 9\\text{ cm}$. Construct $120^\\circ$ at $B$ and measure $BC = 7\\text{ cm}$. Erect $90^\\circ$ at $A$, swing $6\\text{ cm}$ from $C$ to find $D$.",
                            "**Step 2 — Apply Condition (a) (Closer to $AB$ than $BC$):**\n"
                            "Construct the angle bisector of $\\angle ABC = 120^\\circ$ ($60^\\circ$ each). Shade the unwanted region closer to $BC$.",
                            "**Step 3 — Apply Condition (b) (At least $4\\text{ cm}$ from $A$):**\n"
                            "Draw a circular arc of radius $4\\text{ cm}$ centered at $A$. Since distance must be $\\ge 4\\text{ cm}$, shade the inside of the circle (unwanted).",
                            "**Step 4 — Apply Condition (c) (Not more than $5\\text{ cm}$ from $AB$):**\n"
                            "Draw a parallel line $5\\text{ cm}$ above $AB$. Shade the unwanted region above this line.",
                            "**Step 5 — Label feasible zone $T$:**\n"
                            "Label the clear unshaded zone satisfying all 3 conditions as **$T$**.\n\n"
                            "**Answer:** Unshaded region $T$ bounded by the $60^\\circ$ angle bisector, the $4\\text{ cm}$ circle arc, and the $5\\text{ cm}$ parallel line."
                        ]
                    }
                },

                # PAGE 8 — suggested_simulation
                {
                    "page_number": 8,
                    "page_title": "Explore: Geometric Inequality Shading Sandbox",
                    "block_type": "suggested_simulation",
                    "component_type": "suggested_simulation",
                    "content": {
                        "purpose": (
                            "An interactive tethered grazing simulator where students can move boundary sliders "
                            "(distance from stake, perpendicular bisector offset, and angle bisectors). "
                            "Students can drag a virtual test point across the plane to watch it turn green inside the feasible zone "
                            "and red inside the shaded unwanted zone."
                        )
                    },
                    "asset_info": {
                        "asset_type": "simulation",
                        "archetype": "math_geometric_inequality_shading_sandbox",
                        "title": "Interactive Geometric Inequality Shading Sandbox"
                    }
                },

                # PAGE 9 — common_misconception
                {
                    "page_number": 9,
                    "page_title": "Common Error: Shading the Target Region in Loci",
                    "block_type": "common_misconception",
                    "component_type": "common_misconception",
                    "content": {
                        "text": (
                            "### The Inverted Shading Error in KCSE Loci\n\n"
                            "Students frequently shade the *valid* region, making the target area completely dark.\n\n"
                            "### Why KCSE Penalizes This:\n\n"
                            "- When multiple loci overlap, shading wanted areas creates an ungradable dark patch.\n"
                            "- **The KCSE Standard:** Always shade the **UNWANTED region** so that the final target region $R$ is left **clean, white, and unshaded**.\n\n"
                            "> **Memory Tip:** Think of your pencil shading as building a fence to lock out the invalid territory — keep the pasture inside clean and open!"
                        )
                    }
                },

                # PAGE 10 — knowledge_check (MCQ)
                {
                    "page_number": 10,
                    "page_title": "Check Your Understanding: Inequality Shading",
                    "block_type": "knowledge_check",
                    "component_type": "multiple_choice",
                    "content": {
                        "question": "In a construction problem, you are given the condition: 'Point P is closer to vertex X than to vertex Y (XP <= YP)'. Which side of the perpendicular bisector of XY should you shade under the KCSE convention?",
                        "options": [
                            "A: The side containing vertex X",
                            "B: The side containing vertex Y",
                            "C: Both sides of the line",
                            "D: Only the endpoints X and Y"
                        ],
                        "answer": "B",
                        "explanation": (
                            "1. $XP \\le YP$ means points must be closer to $X$ (the wanted region is on $X$'s side).\n"
                            "2. Under KCSE rules, we shade the UNWANTED region. Therefore, we shade $Y$'s side of the perpendicular bisector."
                        )
                    }
                },

                # PAGE 11 — summary
                {
                    "page_number": 11,
                    "page_title": "Key Takeaways: Conditional Loci & Shading",
                    "block_type": "summary",
                    "component_type": "summary",
                    "content": {
                        "text": (
                            "### Master Summary: Inequality Loci Protocol\n\n"
                            "| Step | Action | Key Check |\n"
                            "|:---|:---|:---|\n"
                            "| **1. Boundary** | Draw equality boundary | Solid for $\\le, \\ge$; Dashed for $<, >$. |\n"
                            "| **2. Test** | Check a known vertex/point | Determine which half-plane satisfies the rule. |\n"
                            "| **3. Shade** | Shade the UNWANTED side | Leave the valid region clean and white. |\n"
                            "| **4. Label** | Label target region boldly (e.g. $R$, $P$, $T$) | Ensure all boundary labels are legible. |\n\n"
                            "**Golden Rule:** The final solution region must always be the clean white polygon inside the construction boundaries!"
                        )
                    }
                }
            ]
        },

        # =====================================================================
        # MODULE 7.3: Constant Angle Loci & Circle Arc Constructions
        # =====================================================================
        {
            "unit_order": 3,
            "unit_title": "Module 7.3: Constant Angle Loci and Circle Arc Constructions",
            "lesson_title": "Constant Angle Loci and Circle Arc Constructions",
            "lesson_blocks": [
                # PAGE 1 — learning_goal
                {
                    "page_number": 1,
                    "page_title": "Mastering Constant Angle Loci & Circle Arc Geometry",
                    "block_type": "learning_goal",
                    "component_type": "learning_goal",
                    "content": {
                        "title": "What You Will Master in This Lesson",
                        "goals": [
                            "Define a constant angle locus as the circular arc subtended by a fixed chord $AB$ at angle $\\theta$.",
                            "Derive and apply the radius formula $R = \\frac{L}{2\\sin\\theta}$ and midpoint-to-center distance $d = \\frac{L}{2\\tan\\theta}$.",
                            "Execute the 5-step Tangent-Perpendicular compass construction to accurately locate circle center $O$.",
                            "Optimize triangle geometry (e.g., finding the position of $P$ that maximizes triangle area)."
                        ]
                    }
                },

                # PAGE 2 — concept_explanation
                {
                    "page_number": 2,
                    "page_title": "The Theater Stage Analogy: Why Constant Angle is a Circular Arc",
                    "block_type": "concept_explanation",
                    "component_type": "concept_explanation",
                    "content": {
                        "body": (
                            "Imagine watching a theater performance from the audience seats:\n\n"
                            "- The left and right edges of the stage are fixed points $A$ and $B$.\n"
                            "- If you want your viewing angle $\\angle APB$ between the two stage edges to be **exactly $70^\\circ$**, "
                            "where can you sit?\n"
                            "- If you move forward, the angle widens; if you move backward, it narrows.\n"
                            "- All seats giving the exact same viewing angle form a **smooth circular arc** passing through $A$ and $B$!\n\n"
                            "### Why Circle Geometry Proves This\n\n"
                            "By the **Angles in the Same Segment Theorem**, any chord $AB$ subtends equal angles at every point on the major arc of its circle. "
                            "Therefore, the locus of a constant subtended angle is simply a **circular arc**!"
                        )
                    }
                },

                # PAGE 3 — formula_breakdown
                {
                    "page_number": 3,
                    "page_title": "Master Formulas for Constant Angle Circle Geometry",
                    "block_type": "formula_breakdown",
                    "component_type": "formula_breakdown",
                    "content": {
                        "formula": (
                            "**Circle Radius for Subtended Angle } \\theta:\n"
                            "$$R = \\frac{L}{2\\sin\\theta} \\quad \\text{(where } L \\text{ is chord length and } \\theta \\text{ is subtended angle)}$$\n\n"
                            "**Midpoint-to-Center Distance (Offset } d):\n"
                            "$$d = \\frac{L}{2\\tan\\theta} = R\\cos\\theta \\quad \\text{(Distance center } O \\text{ lies below chord } AB\\text{)}$$\n\n"
                            "**Maximum Triangle Height & Area:**\n"
                            "$$h_{\\max} = R + d = \\frac{L}{2\\sin\\theta} + \\frac{L}{2\\tan\\theta} \\implies \\text{Area}_{\\max} = \\frac{1}{2} L \\cdot h_{\\max}$$"
                        ),
                        "content": (
                            "### 5-Step Construction Protocol for Constant Angle $\\theta$ on Chord $AB$\n\n"
                            "1. **Draw the base chord $AB$:** Measure length $L$ and mark the midpoint $M$.\n"
                            "2. **Construct tangent angle $\\theta$ at $A$:** Draw ray $AT$ below (or opposite) $AB$ such that $\\angle BAT = \\theta$.\n"
                            "3. **Erect normal line at $A$:** Construct a perpendicular line to $AT$ at point $A$ ($90^\\circ - \\theta$).\n"
                            "4. **Construct perpendicular bisector of $AB$:** The intersection of this bisector with the normal line is the circle's center $O$.\n"
                            "5. **Draw the circular arc:** Place compass point at $O$, set radius $OA = R$, and draw the major arc from $A$ to $B$."
                        )
                    }
                },

                # PAGE 4 — worked_example (Level 1: Easy / Semicircle Locus for 90° Angle)
                {
                    "page_number": 4,
                    "page_title": "Example 1: The Semicircle Locus (Subtended Angle θ = 90°)",
                    "block_type": "worked_example",
                    "component_type": "worked_example",
                    "content": {
                        "problem": (
                            "Construct the locus of points $P$ on one side of a line segment $AB = 8\\text{ cm}$ "
                            "such that $\\angle APB = 90^\\circ$."
                        ),
                        "steps": [
                            "**What we need to construct:** The locus of points where $\\angle APB = 90^\\circ$.",
                            "**Step 1 — Recognize the angle-in-a-semicircle theorem:**\n"
                            "By Thales' Theorem, the angle subtended by a diameter at any point on a semicircle is always $90^\\circ$.\n"
                            "Therefore, when $\\theta = 90^\\circ$, chord $AB$ is the **diameter** of the circle!",
                            "**Step 2 — Locate the center $O$:**\n"
                            "- Draw horizontal segment $AB = 8\\text{ cm}$.\n"
                            "- The center $O$ is simply the midpoint $M$ of $AB$: $R = \\frac{AB}{2} = 4\\text{ cm}$.",
                            "**Step 3 — Draw the locus arc:**\n"
                            "Place compass point at $O(4\\text{ cm}, 0)$, open radius to $OA = 4\\text{ cm}$, and draw a semicircle above $AB$.\n\n"
                            "**Answer:** A semicircle of diameter $AB = 8\\text{ cm}$ (radius $4\\text{ cm}$) centered at the midpoint of $AB$."
                        ]
                    }
                },

                # PAGE 5 — worked_example (Level 2: Moderate / Constructing a 70° Constant Angle Locus)
                {
                    "page_number": 5,
                    "page_title": "Example 2: Constructing a 70° Angle Locus on a 5 cm Chord",
                    "block_type": "worked_example",
                    "component_type": "worked_example",
                    "content": {
                        "problem": (
                            "Construct the locus of points $P$ on one side of segment $PQ = 5\\text{ cm}$ such that $\\angle PRQ = 70^\\circ$.\n"
                            "Calculate the theoretical radius $R$ and midpoint-center distance $d$."
                        ),
                        "steps": [
                            "**What we need to calculate and construct:** $R$, $d$, and the $70^\\circ$ circular arc.",
                            "**Step 1 — Pre-calculate the theoretical parameters:**\n"
                            "$$R = \\frac{L}{2\\sin(70^\\circ)} = \\frac{5}{2(0.9397)} = \\frac{5}{1.8794} \\approx 2.66\\text{ cm}$$\n"
                            "$$d = \\frac{L}{2\\tan(70^\\circ)} = \\frac{5}{2(2.7475)} = \\frac{5}{5.495} \\approx 0.91\\text{ cm}$$",
                            "**Step 2 — Construct tangent and normal at $P$:**\n"
                            "- Draw $PQ = 5\\text{ cm}$. At $P$, construct tangent angle $\\angle QPT = 70^\\circ$ below $PQ$.\n"
                            "- Construct a perpendicular line to $PT$ at point $P$ ($20^\\circ$ to $PQ$).",
                            "**Step 3 — Intersect with perpendicular bisector:**\n"
                            "- Construct the perpendicular bisector of $PQ$.\n"
                            "- Mark the intersection of this bisector with the normal line as center $O$ ($0.91\\text{ cm}$ below midpoint).",
                            "**Step 4 — Draw the arc:**\n"
                            "Place compass at $O$, open radius to $OP = 2.66\\text{ cm}$, and draw the major arc from $P$ to $Q$ above the segment.\n\n"
                            "**Answer:** Major circular arc of radius $R = 2.66\\text{ cm}$ passing through $P$ and $Q$."
                        ]
                    }
                },

                # PAGE 6 — worked_example (Level 3: Difficult / Constant Angle Locus with Maximum Area)
                {
                    "page_number": 6,
                    "page_title": "Example 3: Constructing 45° Locus and Maximizing Triangle Area",
                    "block_type": "worked_example",
                    "component_type": "worked_example",
                    "content": {
                        "problem": (
                            "On a line $AB = 10\\text{ cm}$, construct the locus of $P$ such that $\\angle APB = 45^\\circ$.\n"
                            "Locate the exact position of $P$ that maximizes the area of triangle $APB$ and calculate this maximum area."
                        ),
                        "steps": [
                            "**What we need to calculate and construct:** $45^\\circ$ arc, maximum height $h_{\\max}$, and maximum area.",
                            "**Step 1 — Calculate radius $R$ and center offset $d$:**\n"
                            "$$R = \\frac{10}{2\\sin(45^\\circ)} = \\frac{10}{\\sqrt{2}} = 5\\sqrt{2} \\approx 7.071\\text{ cm}$$\n"
                            "$$d = \\frac{10}{2\\tan(45^\\circ)} = \\frac{10}{2(1)} = 5.000\\text{ cm}$$",
                            "**Step 2 — Construct center $O$ and draw the $45^\\circ$ arc:**\n"
                            "- At $A$, construct tangent angle $45^\\circ$ below $AB$, and erect a perpendicular normal.\n"
                            "- The normal meets the perpendicular bisector of $AB$ at center $O$ ($5\\text{ cm}$ below midpoint $M$).\n"
                            "- With compass at $O$ and radius $OA = 5\\sqrt{2} \\approx 7.07\\text{ cm}$, draw the major circular arc.",
                            "**Step 3 — Locate $P$ for maximum triangle height:**\n"
                            "The highest point on the arc lies directly on the perpendicular bisector at the apex:\n"
                            "$$h_{\\max} = R + d = 5\\sqrt{2} + 5 \\approx 7.071 + 5 = 12.071\\text{ cm}$$",
                            "**Step 4 — Calculate maximum area:**\n"
                            "$$\\text{Area}_{\\max} = \\frac{1}{2} \\times \\text{base} \\times h_{\\max} = \\frac{1}{2} \\times 10 \\times 12.071 = 60.36\\text{ cm}^2$$\n\n"
                            "**Answer:** Maximum area is $60.36\\text{ cm}^2$ at the apex of the major arc ($h = 12.07\\text{ cm}$)."
                        ]
                    }
                },

                # PAGE 7 — worked_example (Level 4: Exam-Style / Fixed Area and 90° Angle Triangle)
                {
                    "page_number": 7,
                    "page_title": "Example 4: Dual Loci Construction for Triangle ACB (Area 20 cm² and 90° Angle)",
                    "block_type": "worked_example",
                    "component_type": "worked_example",
                    "content": {
                        "problem": (
                            "On base $AB = 10\\text{ cm}$, use ruler and compasses only to construct triangle $ABC$ such that:\n"
                            "(a) The area of triangle $ABC = 20\\text{ cm}^2$.\n"
                            "(b) $\\angle ACB = 90^\\circ$.\n"
                            "Show all possible positions of vertex $C$."
                        ),
                        "steps": [
                            "**What we need to construct:** Intersecting loci for fixed area ($20\\text{ cm}^2$) and right angle ($90^\\circ$).",
                            "**Step 1 — Determine the height requirement from area:**\n"
                            "$$\\text{Area} = \\frac{1}{2} \\times AB \\times h = 20 \\implies \\frac{1}{2} \\times 10 \\times h = 20 \\implies 5h = 20 \\implies h = 4\\text{ cm}$$\n"
                            "Locus 1: A line parallel to $AB$ at a perpendicular distance of $4\\text{ cm}$.",
                            "**Step 2 — Determine the right-angle requirement:**\n"
                            "$\\angle ACB = 90^\\circ \\implies C$ must lie on a **semicircle of diameter $AB = 10\\text{ cm}$** (radius $r = 5\\text{ cm}$).",
                            "**Step 3 — Construct both loci:**\n"
                            "- Draw base $AB = 10\\text{ cm}$. Mark midpoint $M$ and draw a semicircle of radius $5\\text{ cm}$ above $AB$.\n"
                            "- Construct a line parallel to $AB$ at height $4\\text{ cm}$.",
                            "**Step 4 — Find intersection points:**\n"
                            "Since the height ($4\\text{ cm}$) is strictly less than the semicircle radius ($5\\text{ cm}$), "
                            "the parallel line cuts the semicircle at **exactly two points** $C_1$ and $C_2$.\n\n"
                            "**Answer:** Two possible triangles $ABC_1$ and $ABC_2$ satisfying both Area $= 20\\text{ cm}^2$ and $\\angle ACB = 90^\\circ$."
                        ]
                    }
                },

                # PAGE 8 — suggested_simulation
                {
                    "page_number": 8,
                    "page_title": "Explore: Constant Angle Locus & Sextant Sandbox",
                    "block_type": "suggested_simulation",
                    "component_type": "suggested_simulation",
                    "content": {
                        "purpose": (
                            "An interactive harbor navigation simulator where students adjust a subtended angle slider from 10° to 170°. "
                            "The simulator dynamically recalculates and displays the theoretical radius R, center offset d, "
                            "and shows how the locus transitions from a huge flat arc to a semicircle at 90°, and shrinks to a minor arc beyond 90°."
                        )
                    },
                    "asset_info": {
                        "asset_type": "simulation",
                        "archetype": "math_constant_angle_locus_navigator",
                        "title": "Interactive Constant Angle Locus Navigator Sandbox"
                    }
                },

                # PAGE 9 — common_misconception
                {
                    "page_number": 9,
                    "page_title": "Common Error: Scribing the Arc on the Wrong Side",
                    "block_type": "common_misconception",
                    "component_type": "common_misconception",
                    "content": {
                        "text": (
                            "### The Inverted Center Placement Error\n\n"
                            "When constructing a constant angle $\\theta = 70^\\circ$ locus above chord $AB$, students often place the center $O$ above $AB$.\n\n"
                            "### The Circle Geometry Rule:\n\n"
                            "| Subtended Angle $\\theta$ | Center Location Relative to Chord | Resulting Arc Shape |\n"
                            "|:---|:---|:---|\n"
                            "| **Acute Angle ($\\theta < 90^\\circ$)** | Center $O$ lies on the **OPPOSITE side** (below chord) | **Major Arc** (tall, expansive curve) |\n"
                            "| **Right Angle ($\\theta = 90^\\circ$)** | Center $O$ lies **ON the chord** (midpoint $M$) | **Semicircle** ($R = L/2$) |\n"
                            "| **Obtuse Angle ($\\theta > 90^\\circ$)** | Center $O$ lies on the **SAME side** (above chord) | **Minor Arc** (shallow, compressed curve) |\n\n"
                            "> **Memory Tip:** An acute angle requires a large, spacious major arc, so the center must drop down below the base chord!"
                        )
                    }
                },

                # PAGE 10 — knowledge_check (MCQ)
                {
                    "page_number": 10,
                    "page_title": "Check Your Understanding: Constant Angle Loci",
                    "block_type": "knowledge_check",
                    "component_type": "multiple_choice",
                    "content": {
                        "question": "What is the radius of the circular arc on which a chord AB of length 12 cm subtends an angle of 30°?",
                        "options": [
                            "A: 6 cm",
                            "B: 12 cm",
                            "C: 24 cm",
                            "D: 10.39 cm"
                        ],
                        "answer": "B",
                        "explanation": (
                            "1. Apply the constant angle radius formula: $R = \\frac{L}{2\\sin\\theta}$.\n"
                            "2. $R = \\frac{12}{2\\sin(30^\\circ)} = \\frac{12}{2(0.5)} = \\frac{12}{1} = 12\\text{ cm}$."
                        )
                    }
                },

                # PAGE 11 — summary
                {
                    "page_number": 11,
                    "page_title": "Key Takeaways: Constant Angle Loci",
                    "block_type": "summary",
                    "component_type": "summary",
                    "content": {
                        "text": (
                            "### Master Summary: Constant Angle Formula Reference\n\n"
                            "| Parameter | Formula | Key Application |\n"
                            "|:---|:---|:---|\n"
                            "| **Radius $R$** | $R = \\frac{L}{2\\sin\\theta}$ | Setting compass radius for drawing arc. |\n"
                            "| **Center Offset $d$** | $d = \\frac{L}{2\\tan\\theta} = R\\cos\\theta$ | Verifying distance of center below midpoint. |\n"
                            "| **Maximum Height** | $h_{\\max} = R + d$ | Peak altitude of the constant angle arc. |\n"
                            "| **Maximum Area** | $\\text{Area}_{\\max} = \\frac{1}{2} L (R + d)$ | Optimizing triangle area on base $L$. |\n\n"
                            "**Construction Checklist:**\n"
                            "- [x] Measure chord $L$ and mark midpoint $M$.\n"
                            "- [x] Lay off tangent angle $\\theta$ below chord.\n"
                            "- [x] Erect $90^\\circ$ normal to meet perpendicular bisector at center $O$."
                        )
                    }
                }
            ]
        },

        # =====================================================================
        # MODULE 7.4: Intersecting Loci & Intersecting Chords Theorem
        # =====================================================================
        {
            "unit_order": 4,
            "unit_title": "Module 7.4: Intersecting Loci, Intersecting Chords Theorem, and Multi-Step Constructions",
            "lesson_title": "Intersecting Loci, Intersecting Chords Theorem, and Multi-Step Constructions",
            "lesson_blocks": [
                # PAGE 1 — learning_goal
                {
                    "page_number": 1,
                    "page_title": "Mastering Intersecting Loci & Circle Theorems",
                    "block_type": "learning_goal",
                    "component_type": "learning_goal",
                    "content": {
                        "title": "What You Will Master in This Lesson",
                        "goals": [
                            "Locate unique coordinate points satisfying multiple intersecting loci simultaneously ($L_1 \\cap L_2$).",
                            "Construct circumscribed circles (circumcenter via perpendicular bisectors) and inscribed circles (incenter via angle bisectors).",
                            "State and apply the Intersecting Chords Theorem ($AO \\cdot BO = CO \\cdot DO$) algebraically.",
                            "Execute full 10-mark multi-step KCSE geometric construction synthesis problems."
                        ]
                    }
                },

                # PAGE 2 — concept_explanation
                {
                    "page_number": 2,
                    "page_title": "The Crosshair Navigation Principle: Pinpointing Intersections",
                    "block_type": "concept_explanation",
                    "component_type": "concept_explanation",
                    "content": {
                        "body": (
                            "In navigation, surveying, and aviation, a single rule is rarely enough to find an exact location. "
                            "For example, knowing you are '$5\\text{ km}$ from airport $A$' leaves you anywhere on a large circle.\n\n"
                            "### The Crosshair Principle\n\n"
                            "- When you combine **two independent geometric rules**:\n"
                            "  - Rule 1: '$5\\text{ km}$ from airport $A$' (Circle $L_1$)\n"
                            "  - Rule 2: 'Equidistant from highways $M$ and $N$' (Angle Bisector $L_2$)\n"
                            "- The exact target location is the **intersection point $L_1 \\cap L_2$** where both crosshairs meet!\n\n"
                            "### The Intersecting Chords Theorem\n\n"
                            "When two straight chords $AB$ and $CD$ cross inside a circle at point $O$, "
                            "the products of their divided segments are always strictly equal: $$AO \\times BO = CO \\times DO$$"
                        )
                    }
                },

                # PAGE 3 — formula_breakdown
                {
                    "page_number": 3,
                    "page_title": "Master Formulas for Intersecting Loci & Chords",
                    "block_type": "formula_breakdown",
                    "component_type": "formula_breakdown",
                    "content": {
                        "formula": (
                            "**Intersecting Chords Theorem (Internal Intersection):**\n"
                            "$$AO \\times BO = CO \\times DO$$\n\n"
                            "**Circumcenter Locus (Circumscribed Circle):**\n"
                            "$$\\text{Perpendicular Bisector}(AB) \\cap \\text{Perpendicular Bisector}(BC) = \\text{Circumcenter } O \\quad (OA = OB = OC = R)$$\n\n"
                            "**Incenter Locus (Inscribed Circle):**\n"
                            "$$\\text{Angle Bisector}(\\angle A) \\cap \\text{Angle Bisector}(\\angle B) = \\text{Incenter } I \\quad (r = \\text{perpendicular distance to sides})$$"
                        ),
                        "content": (
                            "### Circle Centers & Intersection Summary\n\n"
                            "| Target Point | Construction Intersection | Physical Property |\n"
                            "|:---|:---|:---|\n"
                            "| **Circumcenter ($O$)** | Intersection of **Perpendicular Bisectors** of sides | Center of circle passing through all 3 vertices ($OA=OB=OC$) |\n"
                            "| **Incenter ($I$)** | Intersection of **Angle Bisectors** of interior angles | Center of circle touching all 3 sides internally |\n"
                            "| **Centroid ($G$)** | Intersection of **Medians** (midpoint to opposite vertex) | Center of mass / gravity ($2:1$ ratio along median) |\n"
                            "| **Orthocenter ($H$)** | Intersection of **Altitudes** (perpendicular heights) | Concurrence of perpendicular drops from vertices |"
                        )
                    }
                },

                # PAGE 4 — worked_example (Level 1: Easy / Applying Intersecting Chords Theorem)
                {
                    "page_number": 4,
                    "page_title": "Example 1: Calculating Segment Lengths via Intersecting Chords",
                    "block_type": "worked_example",
                    "component_type": "worked_example",
                    "content": {
                        "problem": (
                            "Two chords $AB$ and $CD$ intersect inside a circle at point $O$.\n"
                            "Given that $AO = 6\\text{ cm}$, $BO = 4\\text{ cm}$, and $CO = 3\\text{ cm}$, calculate the length of segment $DO$."
                        ),
                        "steps": [
                            "**What we need to find:** Length of segment $DO$.",
                            "**Step 1 — State the Intersecting Chords Theorem:**\n"
                            "$$AO \\times BO = CO \\times DO$$",
                            "**Step 2 — Substitute known lengths:**\n"
                            "$$6 \\times 4 = 3 \\times DO$$\n"
                            "$$24 = 3 \\cdot DO$$",
                            "**Step 3 — Solve for $DO$:**\n"
                            "$$DO = \\frac{24}{3} = 8\\text{ cm}$$\n\n"
                            "**Answer:** $DO = 8\\text{ cm}$."
                        ]
                    }
                },

                # PAGE 5 — worked_example (Level 2: Moderate / Circumscribed Circle Construction)
                {
                    "page_number": 5,
                    "page_title": "Example 2: Constructing the Circumscribed Circle of a Triangle",
                    "block_type": "worked_example",
                    "component_type": "worked_example",
                    "content": {
                        "problem": (
                            "Using a ruler and compasses only, construct triangle $ABC$ with $AB = 7\\text{ cm}$, $BC = 6\\text{ cm}$, and $AC = 5\\text{ cm}$.\n"
                            "Construct the circumscribed circle passing through all three vertices and measure its radius $R$."
                        ),
                        "steps": [
                            "**What we need to construct:** Circumscribed circle and measure radius $R$.",
                            "**Step 1 — Construct triangle $ABC$:**\n"
                            "Draw $AB = 7\\text{ cm}$. Strike $6\\text{ cm}$ from $B$ and $5\\text{ cm}$ from $A$ to locate $C$. Join $AC$ and $BC$.",
                            "**Step 2 — Construct perpendicular bisectors of any two sides:**\n"
                            "- Construct the perpendicular bisector of segment $AB$.\n"
                            "- Construct the perpendicular bisector of segment $BC$.",
                            "**Step 3 — Locate the circumcenter $O$:**\n"
                            "Mark the intersection of the two perpendicular bisectors as **$O$**.",
                            "**Step 4 — Draw the circumscribed circle:**\n"
                            "Place compass point at $O$, open radius to $OA$ (or $OB$, $OC$), and draw the complete circle.\n"
                            "Measure radius $R \\approx 3.57\\text{ cm}$.\n\n"
                            "**Answer:** The circumcenter $O$ is the intersection of perpendicular bisectors, with circumradius $R \\approx 3.57\\text{ cm}$."
                        ]
                    }
                },

                # PAGE 6 — worked_example (Level 3: Difficult / Intersection of Angle and Perpendicular Bisectors)
                {
                    "page_number": 6,
                    "page_title": "Example 3: Intersection of Bisectors in an Oblique Triangle (Angle 135°)",
                    "block_type": "worked_example",
                    "component_type": "worked_example",
                    "content": {
                        "problem": (
                            "Using ruler and compasses only:\n"
                            "(a) Construct triangle $ABC$ such that $\\angle ABC = 135^\\circ$, $AB = 8.2\\text{ cm}$, and $BC = 9.6\\text{ cm}$.\n"
                            "(b) Locate point $D$ such that it is equidistant from lines $AB$ and $BC$, and also equidistant from vertices $B$ and $C$.\n"
                            "(c) Calculate the area of triangle $DBC$."
                        ),
                        "steps": [
                            "**What we need to construct and calculate:** Triangle $ABC$, point $D$, and area of $\\triangle DBC$.",
                            "**Step 1 — Construct triangle $ABC$ with $135^\\circ$ angle:**\n"
                            "- Draw base $BC = 9.6\\text{ cm}$. At $B$, construct $90^\\circ + 45^\\circ = 135^\\circ$.\n"
                            "- Measure $AB = 8.2\\text{ cm}$ along the ray and join $AC$.",
                            "**Step 2 — Construct Locus 1 (Angle Bisector):**\n"
                            "- Equidistant from lines $AB$ and $BC \\implies$ angle bisector of $\\angle ABC = 135^\\circ$.\n"
                            "- Bisect $135^\\circ$ into two $67.5^\\circ$ angles and extend the ray.",
                            "**Step 3 — Construct Locus 2 (Perpendicular Bisector):**\n"
                            "- Equidistant from vertices $B$ and $C \\implies$ perpendicular bisector of segment $BC$.\n"
                            "- Strike arcs from $B$ and $C$ to draw the vertical bisector at midpoint $M(4.8\\text{ cm}, 0)$.",
                            "**Step 4 — Mark intersection $D$ and calculate height:**\n"
                            "- The vertical line $x = 4.8\\text{ cm}$ meets the angle bisector ray at $D$.\n"
                            "- Vertical height: $h = 4.8 \\times \\tan(67.5^\\circ) = 4.8 \\times 2.4142 \\approx 11.59\\text{ cm}$.",
                            "**Step 5 — Calculate area of triangle $DBC$:**\n"
                            "$$\\text{Area} = \\frac{1}{2} \\times \\text{base } BC \\times \\text{height} = \\frac{1}{2} \\times 9.6 \\times 11.59 \\approx 55.62\\text{ cm}^2$$\n\n"
                            "**Answer:** Point $D$ is at height $11.59\\text{ cm}$, giving $\\text{Area}(\\triangle DBC) = 55.62\\text{ cm}^2$."
                        ]
                    }
                },

                # PAGE 7 — worked_example (Level 4: Exam-Style / Full 10-Mark Multi-Locus Survey Synthesis)
                {
                    "page_number": 7,
                    "page_title": "Example 4: Surveying Plot Planning Synthesis (KCSE Standard)",
                    "block_type": "worked_example",
                    "component_type": "worked_example",
                    "content": {
                        "problem": (
                            "In a plot $PQR$, $PQ = 10\\text{ cm}$, $QR = 8\\text{ cm}$, and $\\angle PQR = 60^\\circ$.\n"
                            "(a) Construct plot $PQR$.\n"
                            "(b) Construct the locus of points $S$ such that $\\angle PSR = 60^\\circ$ on the same side of $PR$ as $Q$.\n"
                            "(c) Construct the locus of points equidistant from $PQ$ and $QR$.\n"
                            "(d) Locate point $T$, the intersection of the angle bisector and the constant angle arc, and measure the distance $QT$."
                        ),
                        "steps": [
                            "**What we need to construct:** Plot $PQR$, constant angle arc $60^\\circ$, angle bisector, and measure $QT$.",
                            "**Step 1 — Construct triangle $PQR$:**\n"
                            "Draw $PQ = 10\\text{ cm}$, construct $60^\\circ$ at $Q$, measure $QR = 8\\text{ cm}$, and join $PR$.",
                            "**Step 2 — Construct Constant Angle Locus ($60^\\circ$ on $PR$):**\n"
                            "- At $P$, lay off tangent angle $60^\\circ$ below $PR$ and erect a $90^\\circ$ normal.\n"
                            "- Intersect normal with perpendicular bisector of $PR$ to find circle center $O$.\n"
                            "- Draw circular arc of radius $OP$ passing through $P, Q, R$ (since $\\angle PQR = 60^\\circ$, $Q$ naturally lies on this arc!).",
                            "**Step 3 — Construct Angle Bisector of $\\angle PQR$:**\n"
                            "Bisect the $60^\\circ$ angle at $Q$ into two $30^\\circ$ angles and extend the ray across the triangle.",
                            "**Step 4 — Mark intersection $T$ and measure distance:**\n"
                            "The extended angle bisector intersects the circular arc at point $T$.\n"
                            "Measure distance $QT$ with a ruler: **$QT \\approx 9.2\\text{ cm}$**.\n\n"
                            "**Answer:** Point $T$ located at the intersection of the $30^\\circ$ bisector and circular arc, with $QT \\approx 9.2\\text{ cm}$."
                        ]
                    }
                },

                # PAGE 8 — suggested_simulation
                {
                    "page_number": 8,
                    "page_title": "Explore: Intersecting Loci & Circle Theorems Sandbox",
                    "block_type": "suggested_simulation",
                    "component_type": "suggested_simulation",
                    "content": {
                        "purpose": (
                            "An interactive multi-locus construction sandbox where students can toggle perpendicular bisectors, "
                            "angle bisectors, and intersecting chords inside a circle. The app dynamically computes chord product segments "
                            "(AO × BO = CO × DO) and displays the concurrent circumcenter and incenter in real time."
                        )
                    },
                    "asset_info": {
                        "asset_type": "simulation",
                        "archetype": "math_intersecting_loci_chords_sandbox",
                        "title": "Interactive Intersecting Loci & Chords Sandbox"
                    }
                },

                # PAGE 9 — common_misconception
                {
                    "page_number": 9,
                    "page_title": "Common Error: Confusing Incenter with Circumcenter",
                    "block_type": "common_misconception",
                    "component_type": "common_misconception",
                    "content": {
                        "text": (
                            "### The Triangle Center Confusion\n\n"
                            "Students frequently confuse which bisectors produce the **circumcenter** versus the **incenter**.\n\n"
                            "### The Memory Rule Table:\n\n"
                            "| Center Name | Bisectors Used | Circle Created | Key Memory Hint |\n"
                            "|:---|:---|:---|:---|\n"
                            "| **Circumcenter ($O$)** | **Perpendicular Bisectors of SIDES** | Passes through all 3 **vertices** | **Sides $\\implies$ Outside circle** |\n"
                            "| **Incenter ($I$)** | **Angle Bisectors of ANGLES** | Touches all 3 **sides internally** | **Angles $\\implies$ Inside circle** |\n\n"
                            "> **Memory Tip:** **A**ngles make the **In**center (**A-I**), while **S**ides make the **Out**side circumcenter (**S-O**)!"
                        )
                    }
                },

                # PAGE 10 — knowledge_check (MCQ)
                {
                    "page_number": 10,
                    "page_title": "Check Your Understanding: Intersecting Chords",
                    "block_type": "knowledge_check",
                    "component_type": "multiple_choice",
                    "content": {
                        "question": "Two chords AB and CD intersect at X inside a circle. If AX = 4 cm, XB = 9 cm, and CX = 6 cm, what is the length of chord CD?",
                        "options": [
                            "A: 6 cm",
                            "B: 10 cm",
                            "C: 12 cm",
                            "D: 15 cm"
                        ],
                        "answer": "C",
                        "explanation": (
                            "1. Apply the Intersecting Chords Theorem: $AX \\times XB = CX \\times XD$.\n"
                            "2. $4 \\times 9 = 6 \\times XD \\implies 36 = 6 \\cdot XD \\implies XD = 6\\text{ cm}$.\n"
                            "3. Total chord length $CD = CX + XD = 6 + 6 = 12\\text{ cm}$."
                        )
                    }
                },

                # PAGE 11 — summary
                {
                    "page_number": 11,
                    "page_title": "Key Takeaways: Intersecting Loci & Circle Theorems",
                    "block_type": "summary",
                    "component_type": "summary",
                    "content": {
                        "text": (
                            "### Master Summary: Advanced Loci & Circle Theorems\n\n"
                            "| Concept | Mathematical Equation | Key Construction Tip |\n"
                            "|:---|:---|:---|\n"
                            "| **Intersecting Chords** | $AO \\cdot BO = CO \\cdot DO$ | Product of divided parts are equal. |\n"
                            "| **Circumcenter** | $\\perp\\text{ Bisectors of Sides}$ | Equidistant from all 3 vertices ($OA=OB=OC$). |\n"
                            "| **Incenter** | $\\angle\\text{ Bisectors of Angles}$ | Equidistant from all 3 sides (radius $r$). |\n"
                            "| **Unique Crosshair** | $L_1 \\cap L_2$ | The intersection point satisfies both rules simultaneously. |\n\n"
                            "**Construction Mastery Complete:**\n"
                            "- [x] 4 Fundamental Loci mastered.\n"
                            "- [x] KCSE Unwanted Shading applied.\n"
                            "- [x] Constant Angle circular arcs constructed.\n"
                            "- [x] Intersecting Chords Theorem verified."
                        )
                    }
                }
            ]
        }
    ]


def ingest_topic7_loci():
    """Main ingestion runner for Topic 7: Loci."""
    print("=" * 80)
    print("VLearn Form 4 Mathematics — Topic 7: Loci")
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

    # 2. Get or create Topic 7
    topic_name = "Topic 7: Loci"
    topic, topic_created = Topic.objects.get_or_create(
        subject=subject,
        order=7,
        defaults={"name": topic_name}
    )
    if not topic_created and topic.name != topic_name:
        topic.name = topic_name
        topic.save()
    print(f"Found Topic: {topic.name} (ID: {topic.id})")

    modules_data = get_topic7_data()
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
    ingest_topic7_loci()
