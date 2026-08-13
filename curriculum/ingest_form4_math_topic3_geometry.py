"""
VLearn Form 4 Mathematics — Topic 3: Three-Dimensional Geometry
Ingestion Script

Covers:
  - Module 3.1: Geometric Properties of 3D Solids, Skew Lines, and Projections
  - Module 3.2: Calculating 3D Lengths and Angles Between Lines
  - Module 3.3: Angle Between a Line and a Plane
  - Module 3.4: Angle Between Two Planes (Dihedral Angle)

Run from Vlearn_backend/:
  source venv/bin/activate
  python curriculum/ingest_form4_math_topic3_geometry.py
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


def get_or_create_hierarchy():
    """Ensure Curriculum, Grade, Subject, and Topic records exist."""
    curriculum, _ = Curriculum.objects.get_or_create(
        name="844",
        defaults={"description": "Kenya 8-4-4 Education System"}
    )

    grade = Grade.objects.filter(name="Form 4").first()
    if not grade:
        grade = Grade.objects.create(
            name="Form 4",
            level=1,
            curriculum=curriculum
        )

    subject, _ = Subject.objects.get_or_create(
        name="Mathematics",
        grade=grade,
    )

    topic, _ = Topic.objects.get_or_create(
        name="Topic 3: Three Dimensional Geometry",
        subject=subject,
        defaults={"order": 3}
    )
    if topic.order != 3:
        topic.order = 3
        topic.save()

    return curriculum, grade, subject, topic


def ingest_topic3_geometry():
    """Ingest Topic 3 (Three-Dimensional Geometry) into VLearn database."""
    print("=" * 80)
    print("VLearn Form 4 Mathematics — Topic 3: Three-Dimensional Geometry")
    print("Ingestion started")
    print("=" * 80)

    curriculum, grade, subject, topic = get_or_create_hierarchy()
    print(f"Found existing Curriculum: {curriculum.name}")
    print(f"Found Grade: {grade.name} (level={grade.level})")
    print(f"Found Subject: {subject.name}")
    print(f"Found Topic: {topic.name} (ID: {topic.id})")

    # 4 Modules / Learning Units
    modules_data = [
        # ===================================================================
        # MODULE 3.1: Geometric Properties of 3D Solids, Skew Lines, and Projections
        # ===================================================================
        {
            "unit_order": 1,
            "unit_title": "Module 3.1: Geometric Properties of 3D Solids, Skew Lines, and Projections",
            "lesson_title": "Geometric Properties of 3D Solids, Skew Lines, and Projections",
            "lesson_blocks": [
                # PAGE 1 — learning_goal
                {
                    "page_number": 1,
                    "page_title": "Mastering 3D Geometry: Solids, Skew Lines, and Shadows",
                    "block_type": "learning_goal",
                    "component_type": "learning_goal",
                    "content": {
                        "title": "What You Will Master in This Lesson",
                        "goals": [
                            "Identify vertices, edges, and faces of common 3D solids (cuboids, prisms, pyramids, tetrahedra).",
                            "Distinguish between parallel lines, intersecting lines, and skew lines in three-dimensional space.",
                            "Determine the orthogonal projection of a point and a line onto any given plane.",
                            "Visualize flat 2D nets that fold into 3D geometric shapes."
                        ]
                    }
                },

                # PAGE 2 — concept_explanation
                {
                    "page_number": 2,
                    "page_title": "Understanding 3D Space: Beyond Flat Paper",
                    "block_type": "concept_explanation",
                    "component_type": "concept_explanation",
                    "content": {
                        "title": "Why 3D Geometry Requires a New Way of Seeing",
                        "body": (
                            "In flat 2D geometry, two straight lines that never meet are always parallel. "
                            "In three-dimensional space, however, lines can run in completely different directions "
                            "without ever intersecting—because they sit on entirely different flat planes!\n\n"
                            "### Relatable Real-World Analogies\n\n"
                            "1. **The Highway Overpass (Skew Lines):**\n"
                            "   Imagine a highway flyover running East–West while a local street below runs North–South. "
                            "   They never cross each other, yet they are not pointing in the same direction. "
                            "   In mathematics, non-intersecting and non-parallel lines in 3D are called **skew lines**.\n\n"
                            "2. **The Flashlight Shadow (Orthogonal Projection):**\n"
                            "   Hold a pencil tilted above a flat table. If a strong light shines directly overhead, "
                            "   the shadow cast on the table by the pencil is its **orthogonal projection**.\n"
                            "   To find the shadow of any 3D line segment, drop a vertical line straight down from each endpoint to the floor plane and connect their landing spots!"
                        )
                    }
                },

                # PAGE 3 — definition_card
                {
                    "page_number": 3,
                    "page_title": "Core Rules: Line Types and Orthogonal Projections",
                    "block_type": "definition_card",
                    "component_type": "definition_card",
                    "content": {
                        "title": "Line Relationships & Projection Rules",
                        "body": (
                            "### Types of Line Pairs in 3D Space\n\n"
                            "| Relationship | Do They Meet? | Same Plane (Coplanar)? | Direction |\n"
                            "|:---|:---:|:---:|:---|\n"
                            "| **Intersecting Lines** | Yes (at 1 point) | Yes | Different directions |\n"
                            "| **Parallel Lines** | No | Yes | Exactly the same direction |\n"
                            "| **Skew Lines** | No | No (Different planes) | Different directions |\n\n"
                            "### How to Find an Orthogonal Projection on a Plane\n\n"
                            "To project a line segment $VC$ onto a flat plane $ABCD$:\n"
                            "1. **Find the intersection point:** Locate where the line touches the plane (point $C$).\n"
                            "2. **Drop a perpendicular:** Drop a straight plumb-line from the top vertex $V$ perpendicular to plane $ABCD$, landing at point $O$ (the foot of the perpendicular).\n"
                            "3. **Join the feet:** The straight segment $OC$ on the plane is the **orthogonal projection** of $VC$."
                        )
                    }
                },

                # PAGE 4 — worked_example (Level 1: Vertex & Edge Identification)
                {
                    "page_number": 4,
                    "page_title": "Example 1: Identifying Line Relationships in a Cuboid",
                    "block_type": "worked_example",
                    "component_type": "worked_example",
                    "content": {
                        "problem": (
                            "In the cuboid $ABCDEFGH$ shown below, $ABCD$ is the bottom horizontal base and $EFGH$ is the top horizontal face "
                            "(with vertical edges $AE, BF, CG, DH$).\n\n"
                            "State the geometric relationship (Intersecting, Parallel, or Skew) between edge $AB$ and each of the following edges:\n"
                            "(a) Edge $EF$\n"
                            "(b) Edge $BC$\n"
                            "(c) Edge $CG$\n"
                            "(d) Edge $EH$"
                        ),
                        "steps": [
                            "**What we need to determine:** Whether the two lines intersect, run parallel in the same plane, or lie in different planes without meeting.",
                            "**Step 1 — Edge $AB$ and Edge $EF$:**\n"
                            "- Both edges run horizontally along the front face $ABFE$.\n"
                            "- They point in the same direction and never meet.\n"
                            "- **Relationship:** **Parallel lines**.",
                            "**Step 2 — Edge $AB$ and Edge $BC$:**\n"
                            "- Both edges lie in the bottom base plane $ABCD$ and meet at vertex $B$ at an angle of $90^\\circ$.\n"
                            "- **Relationship:** **Intersecting (perpendicular) lines**.",
                            "**Step 3 — Edge $AB$ and Edge $CG$:**\n"
                            "- Edge $AB$ is a horizontal front edge; edge $CG$ is a vertical back corner edge.\n"
                            "- They never meet, and no single flat plane contains both lines.\n"
                            "- **Relationship:** **Skew lines**.",
                            "**Step 4 — Edge $AB$ and Edge $EH$:**\n"
                            "- Edge $AB$ runs along the front length; edge $EH$ runs along the top width.\n"
                            "- They never meet and point in perpendicular directions across different planes.\n"
                            "- **Relationship:** **Skew lines**.",
                            "**Answer:** (a) Parallel; (b) Intersecting; (c) Skew; (d) Skew."
                        ]
                    }
                },

                # PAGE 5 — worked_example (Level 2: Slant Edge Projections in a Pyramid)
                {
                    "page_number": 5,
                    "page_title": "Example 2: Orthogonal Projections in a Square Pyramid",
                    "block_type": "worked_example",
                    "component_type": "worked_example",
                    "content": {
                        "problem": (
                            "A right pyramid $VABCD$ has a square base $ABCD$ with center $O$. "
                            "The apex $V$ sits vertically directly above $O$.\n\n"
                            "Identify the orthogonal projection of:\n"
                            "(a) The slant edge $VA$ onto the base plane $ABCD$.\n"
                            "(b) The slant edge $VB$ onto the base plane $ABCD$.\n"
                            "(c) The altitude $VO$ onto the base plane $ABCD$."
                        ),
                        "steps": [
                            "**What we need to identify:** The line segments formed by joining the base intersection point to the foot of the perpendicular dropped from $V$.",
                            "**Step 1 — Projection of slant edge $VA$ on base $ABCD$:**\n"
                            "- Slant edge $VA$ touches the base plane at vertex $A$.\n"
                            "- The perpendicular from apex $V$ to the base lands at the center $O$.\n"
                            "- Joining $O$ to $A$ gives the half-diagonal segment $OA$.\n"
                            "- **Projection:** The line segment **$OA$** (or $AO$).",
                            "**Step 2 — Projection of slant edge $VB$ on base $ABCD$:**\n"
                            "- Slant edge $VB$ touches the base plane at vertex $B$.\n"
                            "- The foot of the perpendicular from $V$ is center $O$.\n"
                            "- **Projection:** The line segment **$OB$**.",
                            "**Step 3 — Projection of altitude $VO$ on base $ABCD$:**\n"
                            "- Since $VO$ is already perpendicular to the base, all points along $VO$ project directly straight down onto point $O$.\n"
                            "- **Projection:** The single **point $O$**.",
                            "**Answer:** (a) Segment $OA$; (b) Segment $OB$; (c) Point $O$."
                        ]
                    }
                },

                # PAGE 6 — worked_example (Level 3: Diagonal Projections in a Cuboid)
                {
                    "page_number": 6,
                    "page_title": "Example 3: Space Diagonal Projections onto Faces",
                    "block_type": "worked_example",
                    "component_type": "worked_example",
                    "content": {
                        "problem": (
                            "In a cuboid $ABCDEFGH$, $ABCD$ is the horizontal base and $EFGH$ is the top face. "
                            "A space diagonal connects vertex $B$ (front-right bottom) to vertex $H$ (back-left top).\n\n"
                            "State the orthogonal projection of space diagonal $BH$ onto:\n"
                            "(a) The bottom base plane $ABCD$.\n"
                            "(b) The vertical side face $CDHG$.\n"
                            "(c) The vertical front face $ABFE$."
                        ),
                        "steps": [
                            "**What to identify:** For each target plane, locate where $BH$ touches the plane and drop a perpendicular from the opposite vertex.",
                            "**Step 1 — Projection of $BH$ onto base plane $ABCD$:**\n"
                            "- Vertex $B$ already lies in plane $ABCD$.\n"
                            "- From top vertex $H$, the vertical edge dropped perpendicular to the base is $HD$, landing at vertex $D$.\n"
                            "- Connect $B$ and $D$ on the base floor.\n"
                            "- **Projection:** The base face diagonal **$BD$**.",
                            "**Step 2 — Projection of $BH$ onto vertical side face $CDHG$:**\n"
                            "- Vertex $H$ already lies in face $CDHG$.\n"
                            "- From vertex $B$, the edge perpendicular to side face $CDHG$ is $BC$, landing at vertex $C$.\n"
                            "- Connect $C$ and $H$ on that face.\n"
                            "- **Projection:** The side face diagonal **$CH$** (or $HC$).",
                            "**Step 3 — Projection of $BH$ onto vertical front face $ABFE$:**\n"
                            "- Vertex $B$ already lies in front face $ABFE$.\n"
                            "- From vertex $H$, the perpendicular to face $ABFE$ is $HE$, landing at vertex $E$.\n"
                            "- Connect $B$ and $E$ on the front face.\n"
                            "- **Projection:** The front face diagonal **$BE$**.",
                            "**Answer:** (a) Face diagonal $BD$; (b) Face diagonal $CH$; (c) Face diagonal $BE$."
                        ]
                    }
                },

                # PAGE 7 — worked_example (Level 4: Exam-Style Shortest Surface Path via Nets)
                {
                    "page_number": 7,
                    "page_title": "Example 4: Shortest Surface Crawling Path via 2D Nets",
                    "block_type": "worked_example",
                    "component_type": "worked_example",
                    "content": {
                        "problem": (
                            "A closed rectangular box has dimensions: Length $AB = 8\\text{ cm}$, Width $BC = 6\\text{ cm}$, and Height $AE = 5\\text{ cm}$.\n\n"
                            "An insect crawls along the outer surface of the box from bottom corner $A$ to the opposite top corner $G$.\n\n"
                            "By unfolding the relevant faces into a flat 2D net, calculate the shortest surface distance the insect can travel."
                        ),
                        "steps": [
                            "**What we need to understand:** Walking along a 3D surface becomes a straight line when adjacent faces are unfolded flat into a 2D net.",
                            "**Step 1 — Route Option 1 (Across Front Face $ABFE$ then Top Face $EFGH$):**\n"
                            "- Unfold front face ($8 \\times 5$) and top face ($8 \\times 6$) along hinge $EF$.\n"
                            "- Horizontal span $= AB = 8\\text{ cm}$.\n"
                            "- Vertical unfolded span $= AE + EF_{\\text{top}} = 5 + 6 = 11\\text{ cm}$.\n"
                            "- Shortest straight-line distance $d_1 = \\sqrt{8^2 + 11^2} = \\sqrt{64 + 121} = \\sqrt{185} \\approx 13.60\\text{ cm}$.",
                            "**Step 2 — Route Option 2 (Across Bottom Face $ABCD$ then Right Side Face $BCGF$):**\n"
                            "- Unfold base ($8 \\times 6$) and right side face ($6 \\times 5$) along hinge $BC$.\n"
                            "- Total length span $= AB + BF = 8 + 5 = 13\\text{ cm}$.\n"
                            "- Total width span $= BC = 6\\text{ cm}$.\n"
                            "- Distance $d_2 = \\sqrt{13^2 + 6^2} = \\sqrt{169 + 36} = \\sqrt{205} \\approx 14.32\\text{ cm}$.",
                            "**Step 3 — Route Option 3 (Across Left Face $ADHE$ then Top Face $EFGH$):**\n"
                            "- Unfold left face ($6 \\times 5$) and top face ($8 \\times 6$) along hinge $EH$.\n"
                            "- Total unfolded span $= AD + HG = 6 + 8 = 14\\text{ cm}$ with height $= 5\\text{ cm}$.\n"
                            "- Distance $d_3 = \\sqrt{14^2 + 5^2} = \\sqrt{196 + 25} = \\sqrt{221} \\approx 14.87\\text{ cm}$.",
                            "**Step 4 — Select the absolute shortest path:**\n"
                            "- Minimum distance is $\\sqrt{185} \\approx 13.60\\text{ cm}$ (Route Option 1).\n\n"
                            "**Answer:** The shortest surface crawling distance is $\\sqrt{185} \\approx 13.60\\text{ cm}$."
                        ]
                    }
                },

                # PAGE 8 — suggested_simulation
                {
                    "page_number": 8,
                    "page_title": "Explore: 3D Orthogonal Shadow Sandbox",
                    "block_type": "suggested_simulation",
                    "component_type": "suggested_simulation",
                    "content": {
                        "purpose": (
                            "An interactive 3D solid viewer demonstrating how shifting light angles "
                            "casts orthogonal shadows (projections) of edges and diagonals onto base and lateral planes."
                        ),
                        "instruction": (
                            "Rotate the 3D cuboid and pyramid in real-time. "
                            "Click on any slant edge (highlighted in red) to see its perpendicular drop lines (dashed blue) "
                            "and its flat orthogonal projection shadow (highlighted in emerald green) on the base floor."
                        ),
                        "archetype": "math_orthogonal_projection_shadow_sandbox",
                        "pedagogical_value": (
                            "Bridges the critical cognitive gap between flat 2D textbook drawings and true 3D spatial visualization."
                        )
                    },
                    "asset_info": {
                        "archetype": "math_orthogonal_projection_shadow_sandbox",
                        "title": "Interactive 3D Orthogonal Shadow Sandbox",
                        "asset_type": "simulation"
                    }
                },

                # PAGE 9 — common_misconception
                {
                    "page_number": 9,
                    "page_title": "Common Error: 'Non-Intersecting Lines are Always Parallel'",
                    "block_type": "common_misconception",
                    "component_type": "common_misconception",
                    "content": {
                        "text": (
                            "### The 2D-to-3D Generalization Trap\n\n"
                            "A frequent mistake in secondary school geometry is assuming that if two lines never cross, they must be parallel.\n\n"
                            "- **Incorrect Student Thought:** 'Edges $AB$ and $CG$ in a cuboid never meet, so $AB$ is parallel to $CG$.'\n"
                            "- **Why This is Wrong:** $AB$ runs horizontally East–West on the front floor, while $CG$ runs vertically straight up the back corner! They point in perpendicular directions.\n"
                            "- **The Key Test for Parallel Lines:** For lines to be parallel, they must point in the **exact same direction** and be capable of lying together on a single flat sheet of paper (**coplanar**).\n"
                            "- **The Definition of Skew Lines:** If lines never cross and cannot lie on the same flat plane, they are **skew**."
                        )
                    }
                },

                # PAGE 10 — knowledge_check
                {
                    "page_number": 10,
                    "page_title": "Check Your Understanding: Skew Lines & Projections",
                    "block_type": "knowledge_check",
                    "component_type": "multiple_choice",
                    "content": {
                        "check_type": "multiple_choice",
                        "question": (
                            "In a cuboid $ABCDEFGH$, which of the following pairs of lines are **skew lines**?"
                        ),
                        "options": [
                            "A: Edge $AB$ and Edge $CD$",
                            "B: Edge $AE$ and Edge $CG$",
                            "C: Edge $AB$ and Edge $DH$",
                            "D: Edge $EF$ and Edge $GH$"
                        ],
                        "answer": "C",
                        "explanation": (
                            "Edge $AB$ (horizontal front base) and Edge $DH$ (vertical back-left corner) never meet "
                            "and do not lie in the same plane; therefore, they are skew lines. "
                            "Options A, B, and D are all pairs of parallel lines."
                        )
                    }
                },

                # PAGE 11 — summary
                {
                    "page_number": 11,
                    "page_title": "Key Takeaways: 3D Solids and Projections",
                    "block_type": "summary",
                    "component_type": "summary",
                    "content": {
                        "text": (
                            "### Master Summary: Solids & Lines in 3D Space\n\n"
                            "| Concept | Definition | Everyday Visual |\n"
                            "|:---|:---|:---|\n"
                            "| **Intersecting Lines** | Lines in the same plane meeting at a point | Crossroads intersection |\n"
                            "| **Parallel Lines** | Lines in the same plane with equal direction | Train tracks |\n"
                            "| **Skew Lines** | Non-intersecting, non-coplanar lines | Overpass bridge vs. road below |\n"
                            "| **Orthogonal Projection** | The straight-down shadow of a line on a plane | Overhead light shadow on the floor |\n\n"
                            "### Checklist for Finding Projections\n"
                            "1. Locate where the line meets the plane.\n"
                            "2. Drop a $90^\\circ$ perpendicular from the other end of the line to the plane.\n"
                            "3. Connect the intersection point to the foot of the perpendicular."
                        )
                    }
                }
            ]
        },

        # ===================================================================
        # MODULE 3.2: Calculating 3D Lengths and Angles Between Lines
        # ===================================================================
        {
            "unit_order": 2,
            "unit_title": "Module 3.2: Calculating 3D Lengths and Angles Between Lines",
            "lesson_title": "Calculating 3D Lengths and Angles Between Lines",
            "lesson_blocks": [
                # PAGE 1 — learning_goal
                {
                    "page_number": 1,
                    "page_title": "Mastering 3D Lengths and Inter-Line Angles",
                    "block_type": "learning_goal",
                    "component_type": "learning_goal",
                    "content": {
                        "title": "What You Will Master in This Lesson",
                        "goals": [
                            "Calculate face diagonals and space diagonals of 3D solids using compounded Pythagoras Theorem.",
                            "Determine the angle between two intersecting lines in three dimensions.",
                            "Calculate the angle between skew lines by translating one line parallel to itself.",
                            "Extract 3D cross-sections into flat 2D right-angled and oblique triangles to apply trigonometric rules."
                        ]
                    }
                },

                # PAGE 2 — concept_explanation
                {
                    "page_number": 2,
                    "page_title": "Compounding Pythagoras & Translating Skew Lines",
                    "block_type": "concept_explanation",
                    "component_type": "concept_explanation",
                    "content": {
                        "title": "How to Measure Distances and Angles in 3D",
                        "body": (
                            "Calculating lengths and angles inside a 3D solid is done by cutting the solid into **2D triangular cross-sections**.\n\n"
                            "### 1. The 3D Pythagoras Theorem\n"
                            "To find the distance from the bottom-front-left corner of a room to the opposite top-back-right corner:\n"
                            "- First, walk diagonally across the floor: $d_{\\text{floor}}^2 = x^2 + y^2$.\n"
                            "- Then, climb straight up the vertical wall height: $d_{\\text{space}}^2 = d_{\\text{floor}}^2 + z^2$.\n"
                            "- Combining them gives the master 3D distance formula: **$d = \\sqrt{x^2 + y^2 + z^2}$**.\n\n"
                            "### 2. How to Measure the Angle Between Skew Lines\n"
                            "Skew lines never touch, so how can they have an angle? "
                            "We simply slide (translate) one of the lines parallel to itself until it intersects the second line at a common vertex! "
                            "The angle between them is the angle formed at that meeting point."
                        )
                    }
                },

                # PAGE 3 — formula_breakdown
                {
                    "page_number": 3,
                    "page_title": "The Master Formulas for 3D Lengths and Angles",
                    "block_type": "formula_breakdown",
                    "component_type": "formula_breakdown",
                    "content": {
                        "formula": (
                            "**3D Space Diagonal Formula:**\n"
                            "$$d = \\sqrt{x^2 + y^2 + z^2} = \\sqrt{\\text{Length}^2 + \\text{Width}^2 + \\text{Height}^2}$$\n\n"
                            "**Cosine Rule for Oblique 3D Triangles:**\n"
                            "$$\\cos \\theta = \\frac{a^2 + b^2 - c^2}{2ab}$$"
                        ),
                        "content": (
                            "### 3-Step Strategy for Angle Calculations\n\n"
                            "1. **Isolate the triangle:** Identify the three vertices that form the triangle containing the angle.\n"
                            "2. **Calculate all side lengths:** Use 2D Pythagoras ($a^2 + b^2 = c^2$) on the relevant faces.\n"
                            "3. **Choose the trigonometric tool:**\n"
                            "   - If the extracted triangle has a **$90^\\circ$ right angle**, use SOH-CAH-TOA ($\\sin, \\cos, \\tan$).\n"
                            "   - If the triangle is **oblique (non-right)**, use the **Cosine Rule**: $\\cos \\theta = \\frac{a^2 + b^2 - c^2}{2ab}$."
                        )
                    }
                },

                # PAGE 4 — worked_example (Level 1: Space Diagonal of a Cuboid)
                {
                    "page_number": 4,
                    "page_title": "Example 1: Calculating the Space Diagonal of a Hall",
                    "block_type": "worked_example",
                    "component_type": "worked_example",
                    "content": {
                        "problem": (
                            "A school hall has the shape of a rectangular cuboid with length $12\\text{ m}$, width $9\\text{ m}$, and vertical height $8\\text{ m}$.\n\n"
                            "Calculate:\n"
                            "(a) The diagonal length across the floor.\n"
                            "(b) The space diagonal connecting a bottom corner to the opposite top corner."
                        ),
                        "steps": [
                            "**What we need to find:** Floor diagonal $d_{\\text{floor}}$ and 3D space diagonal $d_{\\text{space}}$.",
                            "**Step 1 — Calculate floor diagonal using 2D Pythagoras:**\n"
                            "$$d_{\\text{floor}} = \\sqrt{\\text{length}^2 + \\text{width}^2} = \\sqrt{12^2 + 9^2} = \\sqrt{144 + 81} = \\sqrt{225} = 15\\text{ m}$$",
                            "**Step 2 — Calculate 3D space diagonal:**\n"
                            "$$d_{\\text{space}} = \\sqrt{d_{\\text{floor}}^2 + \\text{height}^2} = \\sqrt{15^2 + 8^2} = \\sqrt{225 + 64} = \\sqrt{289} = 17\\text{ m}$$",
                            "**Checking with 3D Pythagoras directly:**\n"
                            "$$d = \\sqrt{12^2 + 9^2 + 8^2} = \\sqrt{144 + 81 + 64} = \\sqrt{289} = 17\\text{ m}$$\n\n"
                            "**Answer:** (a) Floor diagonal is $15\\text{ m}$; (b) Space diagonal is $17\\text{ m}$."
                        ]
                    }
                },

                # PAGE 5 — worked_example (Level 2: Angle Between Skew Lines via Translation)
                {
                    "page_number": 5,
                    "page_title": "Example 2: Angle Between Skew Lines in a Cuboid",
                    "block_type": "worked_example",
                    "component_type": "worked_example",
                    "content": {
                        "problem": (
                            "The diagram represents a cuboid $ABCDEFGH$ where base length $AB = 8\\text{ cm}$, "
                            "width $BC = FG = 4.5\\text{ cm}$, and vertical height $DH = AE = BF = 6\\text{ cm}$.\n\n"
                            "Calculate the size of the angle between the skew lines $AB$ (bottom front edge) and $FH$ (top face diagonal)."
                        ),
                        "steps": [
                            "**What we need to understand:** $AB$ and $FH$ are skew lines. We must translate edge $AB$ parallel to itself until it meets $FH$.",
                            "**Step 1 — Translate edge $AB$:**\n"
                            "- In the cuboid, the top front edge $EF$ is parallel and equal in length to bottom edge $AB$ ($AB \\parallel EF$).\n"
                            "- Therefore, the angle between skew lines $AB$ and $FH$ is equal to the angle between lines **$EF$ and $FH$** meeting at vertex $F$ in the top face.",
                            "**Step 2 — Identify the right-angled triangle on the top face:**\n"
                            "- In rectangle $EFGH$, the corner angle $\\angle FEH = 90^\\circ$.\n"
                            "- Side adjacent to angle $F$: $EF = 8\\text{ cm}$.\n"
                            "- Side opposite to angle $F$: $EH = FG = 4.5\\text{ cm}$.",
                            "**Step 3 — Calculate using tangent ratio:**\n"
                            "$$\\tan(\\angle EFH) = \\frac{\\text{Opposite}}{\\text{Adjacent}} = \\frac{EH}{EF} = \\frac{4.5}{8} = 0.5625$$\n"
                            "$$\\angle EFH = \\arctan(0.5625) \\approx 29.36^\\circ$$\n\n"
                            "**Answer:** The angle between the skew lines $AB$ and $FH$ is $29.36^\\circ$."
                        ]
                    }
                },

                # PAGE 6 — worked_example (Level 3: Angle Between Face Diagonals via Cosine Rule)
                {
                    "page_number": 6,
                    "page_title": "Example 3: Angle Between Face Diagonals in a Cuboid",
                    "block_type": "worked_example",
                    "component_type": "worked_example",
                    "content": {
                        "problem": (
                            "In the same cuboid $ABCDEFGH$ ($AB = 8\\text{ cm}, FG = 4.5\\text{ cm}, BF = CG = DH = 6\\text{ cm}$):\n\n"
                            "Calculate the size of the acute angle between face diagonal $FC$ (on front-right face) and face diagonal $FH$ (on top face)."
                        ),
                        "steps": [
                            "**What we need to find:** The angle $\\angle CFH$ in the oblique cross-sectional triangle $\\triangle FCH$.",
                            "**Step 1 — Calculate side $FC$ (hypotenuse of right triangle $\\triangle FBC$):**\n"
                            "$$FC = \\sqrt{BC^2 + BF^2} = \\sqrt{4.5^2 + 6^2} = \\sqrt{20.25 + 36} = \\sqrt{56.25} = 7.5\\text{ cm}$$",
                            "**Step 2 — Calculate side $FH$ (hypotenuse of right triangle $\\triangle FEH$):**\n"
                            "$$FH = \\sqrt{EF^2 + EH^2} = \\sqrt{8^2 + 4.5^2} = \\sqrt{64 + 20.25} = \\sqrt{84.25} \\approx 9.179\\text{ cm}$$",
                            "**Step 3 — Calculate opposite side $HC$ (hypotenuse of right triangle $\\triangle CDH$):**\n"
                            "$$HC = \\sqrt{CD^2 + DH^2} = \\sqrt{8^2 + 6^2} = \\sqrt{64 + 36} = \\sqrt{100} = 10\\text{ cm}$$",
                            "**Step 4 — Apply the Cosine Rule in oblique triangle $\\triangle FCH$:**\n"
                            "$$\\cos(\\angle CFH) = \\frac{FC^2 + FH^2 - HC^2}{2 \\cdot FC \\cdot FH}$$\n"
                            "$$\\cos(\\angle CFH) = \\frac{7.5^2 + 84.25 - 10^2}{2 \\times 7.5 \\times 9.1788} = \\frac{56.25 + 84.25 - 100}{15 \\times 9.1788} = \\frac{40.5}{137.682} \\approx 0.29416$$\n"
                            "$$\\angle CFH = \\arccos(0.29416) \\approx 72.89^\\circ$$\n\n"
                            "**Answer:** The angle between face diagonals $FC$ and $FH$ is $72.89^\\circ$."
                        ]
                    }
                },

                # PAGE 7 — worked_example (Level 4: Geometry of a Regular Tetrahedron)
                {
                    "page_number": 7,
                    "page_title": "Example 4: Altitude and Height of a Regular Tetrahedron",
                    "block_type": "worked_example",
                    "component_type": "worked_example",
                    "content": {
                        "problem": (
                            "A regular tetrahedron $VABC$ has all 6 edges of length $6\\text{ cm}$. "
                            "The apex $V$ is directly above the centroid $O$ of the equilateral base $ABC$.\n\n"
                            "Calculate:\n"
                            "(a) The altitude of the base equilateral triangle $ABC$.\n"
                            "(b) The distance from base vertex $A$ to the centroid $O$ ($OA$).\n"
                            "(c) The true vertical height $VO$ of the tetrahedron."
                        ),
                        "steps": [
                            "**What to identify:** All faces are identical equilateral triangles with side $a = 6\\text{ cm}$.",
                            "**Step 1 — Calculate altitude of base equilateral triangle $AM$ ($M$ is midpoint of $BC$):**\n"
                            "$$AM = a \\cdot \\sin(60^\\circ) = 6 \\times \\frac{\\sqrt{3}}{2} = 3\\sqrt{3} \\approx 5.196\\text{ cm}$$",
                            "**Step 2 — Calculate distance from vertex $A$ to centroid $O$:**\n"
                            "The centroid divides the median in the ratio $2:1$, so:\n"
                            "$$OA = \\frac{2}{3} AM = \\frac{2}{3} (3\\sqrt{3}) = 2\\sqrt{3} \\approx 3.464\\text{ cm}$$",
                            "**Step 3 — Calculate vertical height $VO$ using right triangle $\\triangle VOA$:**\n"
                            "$$VO = \\sqrt{VA^2 - OA^2} = \\sqrt{6^2 - (2\\sqrt{3})^2} = \\sqrt{36 - 12} = \\sqrt{24} = 2\\sqrt{6} \\approx 4.899\\text{ cm}$$\n\n"
                            "**Answer:** (a) Face altitude $AM = 5.20\\text{ cm}$; (b) Centroid distance $OA = 3.46\\text{ cm}$; (c) Height $VO = 4.90\\text{ cm}$."
                        ]
                    }
                },

                # PAGE 8 — suggested_simulation
                {
                    "page_number": 8,
                    "page_title": "Explore: 3D Pythagoras & Skew Line Angle Explorer",
                    "block_type": "suggested_simulation",
                    "component_type": "suggested_simulation",
                    "content": {
                        "purpose": (
                            "An interactive 3D box model where students can drag dimensions, rotate viewing angles, "
                            "and translate skew lines to visualize how 2D cross-sectional triangles are extracted."
                        ),
                        "instruction": (
                            "Adjust the Length, Width, and Height sliders. "
                            "Toggle 'Show Space Diagonal' to watch the floor triangle and vertical wall triangle compound in real time. "
                            "Select any two skew lines and click 'Translate Parallel' to watch them slide into a common vertex and reveal the extracted angle."
                        ),
                        "archetype": "math_3d_pythagoras_and_skew_lines_explorer",
                        "pedagogical_value": (
                            "Provides immediate visual proof that space diagonals follow $d = \\sqrt{x^2+y^2+z^2}$ and that skew lines can be measured via parallel shifting."
                        )
                    },
                    "asset_info": {
                        "archetype": "math_3d_pythagoras_and_skew_lines_explorer",
                        "title": "Interactive 3D Pythagoras & Skew Line Angle Explorer",
                        "asset_type": "simulation"
                    }
                },

                # PAGE 9 — common_misconception
                {
                    "page_number": 9,
                    "page_title": "Common Error: Using SOH-CAH-TOA on Non-Right Triangles",
                    "block_type": "common_misconception",
                    "component_type": "common_misconception",
                    "content": {
                        "text": (
                            "### The Oblique Triangle Fallacy\n\n"
                            "A very common error in 3D geometry is applying simple right-triangle formulas ($\\sin = \\text{Opp}/\\text{Hyp}$) "
                            "to triangles inside a solid that are **not** right-angled.\n\n"
                            "- **Incorrect Example:** In $\\triangle FCH$ (where sides are $7.5, 9.18, 10$), assuming $\\angle FCH = 90^\\circ$ and writing $\\cos(\\angle CFH) = \\frac{7.5}{10} = 0.75 \\implies 41.4^\\circ$.\n"
                            "- **Why This is Wrong:** None of the angles in $\\triangle FCH$ are $90^\\circ$! It is an oblique triangle slicing diagonally through the cuboid.\n"
                            "- **The Rule:** You can only use SOH-CAH-TOA if you have verified that one angle is strictly $90^\\circ$. For oblique triangles where all 3 sides are known, you **must use the Cosine Rule**."
                        )
                    }
                },

                # PAGE 10 — knowledge_check
                {
                    "page_number": 10,
                    "page_title": "Check Your Understanding: Space Diagonals",
                    "block_type": "knowledge_check",
                    "component_type": "multiple_choice",
                    "content": {
                        "check_type": "multiple_choice",
                        "question": (
                            "A cube has an edge length of $5\\text{ cm}$. What is the exact length of its internal 3D space diagonal?"
                        ),
                        "options": [
                            "A: $5\\sqrt{2}\\text{ cm}$",
                            "B: $5\\sqrt{3}\\text{ cm}$",
                            "C: $10\\text{ cm}$",
                            "D: $15\\text{ cm}$"
                        ],
                        "answer": "B",
                        "explanation": (
                            "Using 3D Pythagoras: $d = \\sqrt{5^2 + 5^2 + 5^2} = \\sqrt{25 + 25 + 25} = \\sqrt{75} = \\sqrt{25 \\times 3} = 5\\sqrt{3}\\text{ cm}$. "
                            "Option B is correct."
                        )
                    }
                },

                # PAGE 11 — summary
                {
                    "page_number": 11,
                    "page_title": "Key Takeaways: 3D Lengths and Inter-Line Angles",
                    "block_type": "summary",
                    "component_type": "summary",
                    "content": {
                        "text": (
                            "### Master Summary: Lengths & Angles Between Lines\n\n"
                            "| Measurement | Master Formula | Key Condition |\n"
                            "|:---|:---|:---|\n"
                            "| **3D Space Diagonal** | $d = \\sqrt{x^2 + y^2 + z^2}$ | Cuboid with orthogonal dimensions $x, y, z$ |\n"
                            "| **Angle Between Skew Lines** | $\\theta = \\angle(L_1', L_2)$ | Shift $L_1$ parallel to itself until it touches $L_2$ |\n"
                            "| **Angle in Oblique Triangle** | $\\cos \\theta = \\frac{a^2 + b^2 - c^2}{2ab}$ | Three known side lengths $a, b, c$ |\n\n"
                            "### 3-Step Problem Solving Rule\n"
                            "1. Sketch and extract the 2D cross-sectional triangle.\n"
                            "2. Calculate all edge lengths using 2D Pythagoras on the respective faces.\n"
                            "3. Use SOH-CAH-TOA for right triangles or Cosine Rule for oblique triangles."
                        )
                    }
                }
            ]
        },

        # ===================================================================
        # MODULE 3.3: Angle Between a Line and a Plane
        # ===================================================================
        {
            "unit_order": 3,
            "unit_title": "Module 3.3: Angle Between a Line and a Plane",
            "lesson_title": "Angle Between a Line and a Plane",
            "lesson_blocks": [
                # PAGE 1 — learning_goal
                {
                    "page_number": 1,
                    "page_title": "Mastering Line-to-Plane Inclination Angles",
                    "block_type": "learning_goal",
                    "component_type": "learning_goal",
                    "content": {
                        "title": "What You Will Master in This Lesson",
                        "goals": [
                            "Define the angle between a line and a plane using the orthogonal projection (shadow) principle.",
                            "Calculate line-plane angles in pyramids, cones, cuboids, and regular tetrahedra.",
                            "Avoid the common error of measuring angles against arbitrary base edges.",
                            "Decompose 3D solids into right-angled vertical cross-sections containing the line, its projection, and the altitude."
                        ]
                    }
                },

                # PAGE 2 — concept_explanation
                {
                    "page_number": 2,
                    "page_title": "The Shadow Principle of Line-to-Plane Angles",
                    "block_type": "concept_explanation",
                    "component_type": "concept_explanation",
                    "content": {
                        "title": "How to Find the Angle with a Flat Plane",
                        "body": (
                            "When a line is tilted relative to a flat plane (such as a slant tent pole resting on the ground), "
                            "it can form different angles with different lines drawn on the floor.\n\n"
                            "### Which Angle is the TRUE Angle with the Plane?\n"
                            "The **angle between a line and a plane** is strictly defined as the angle between the line and its **orthogonal projection (shadow)** on that plane!\n\n"
                            "### The 3-Step Extraction Procedure\n"
                            "1. **Intersection ($A$):** Find where the slant line pierces the plane.\n"
                            "2. **Plumb-Line Drop ($VO$):** From the top of the line ($V$), drop a line straight down at $90^\\circ$ to the plane, landing at foot $O$.\n"
                            "3. **Extract Right Triangle $\\triangle VOA$:** The angle between the slant line $VA$ and the plane is the angle **$\\angle VAO$** inside the vertical right-angled triangle $\\triangle VOA$."
                        )
                    }
                },

                # PAGE 3 — formula_breakdown
                {
                    "page_number": 3,
                    "page_title": "Formulas for Line-to-Plane Inclinations",
                    "block_type": "formula_breakdown",
                    "component_type": "formula_breakdown",
                    "content": {
                        "formula": (
                            "**Method 1 (Using Base Projection & Slant Line):**\n"
                            "$$\\cos \\theta = \\frac{\\text{Projection Length } (OA)}{\\text{Slant Line Length } (VA)} = \\frac{\\text{Adjacent}}{\\text{Hypotenuse}}$$\n\n"
                            "**Method 2 (Using Vertical Height & Base Projection):**\n"
                            "$$\\tan \\theta = \\frac{\\text{Vertical Height } (VO)}{\\text{Projection Length } (OA)} = \\frac{\\text{Opposite}}{\\text{Adjacent}}$$"
                        ),
                        "content": (
                            "### Projections for Common Solids at a Glance\n\n"
                            "| Solid | Slant Line | Base Landing Point ($O$) | Projection Segment ($L'$) |\n"
                            "|:---|:---|:---|:---|\n"
                            "| **Square Pyramid** | Slant edge $VA$ | Center of square base | Half-diagonal $OA = \\frac{1}{2}\\sqrt{2} s$ |\n"
                            "| **Regular Tetrahedron** | Slant edge $VA$ | Centroid of equilateral base | Centroid radius $OA = \\frac{\\sqrt{3}}{3} a$ |\n"
                            "| **Right Cone** | Slant generator $VP$ | Center of circular base | Base radius $r$ |\n"
                            "| **Cuboid** | Space diagonal $BH$ | Corner below top vertex | Base face diagonal $BD$ |"
                        )
                    }
                },

                # PAGE 4 — worked_example (Level 1: Slant Edge in Square Pyramid)
                {
                    "page_number": 4,
                    "page_title": "Example 1: Slant Edge to Base Angle in a Square Pyramid",
                    "block_type": "worked_example",
                    "component_type": "worked_example",
                    "content": {
                        "problem": (
                            "A right pyramid $VABCD$ has a square base $ABCD$ of side $6\\text{ cm}$. "
                            "Each slant edge is $10\\text{ cm}$ long. The apex $V$ sits directly above the center $O$ of the base.\n\n"
                            "Calculate the angle between the slant edge $VA$ and the base plane $ABCD$."
                        ),
                        "steps": [
                            "**What we need to find:** The angle $\\angle VAO$ in the right-angled triangle $\\triangle VOA$.",
                            "**Step 1 — Calculate the base diagonal $AC$:**\n"
                            "$$AC = \\sqrt{AB^2 + BC^2} = \\sqrt{6^2 + 6^2} = \\sqrt{72} = 6\\sqrt{2} \\approx 8.485\\text{ cm}$$",
                            "**Step 2 — Calculate projection length $OA$ (half-diagonal):**\n"
                            "$$OA = \\frac{AC}{2} = \\frac{6\\sqrt{2}}{2} = 3\\sqrt{2} \\approx 4.243\\text{ cm}$$",
                            "**Step 3 — Extract right triangle $\\triangle VOA$ ($VO \\perp OA$):**\n"
                            "Hypotenuse $VA = 10\\text{ cm}$, Adjacent $OA = 3\\sqrt{2}\\text{ cm}$.\n"
                            "$$\\cos(\\angle VAO) = \\frac{OA}{VA} = \\frac{3\\sqrt{2}}{10} = \\frac{4.2426}{10} = 0.42426$$",
                            "**Step 4 — Calculate the angle:**\n"
                            "$$\\angle VAO = \\arccos(0.42426) \\approx 64.89^\\circ$$\n\n"
                            "**Answer:** The angle between slant edge $VA$ and the base plane is $64.89^\\circ$."
                        ]
                    }
                },

                # PAGE 5 — worked_example (Level 2: Slant Edge in a Regular Tetrahedron)
                {
                    "page_number": 5,
                    "page_title": "Example 2: Slant Edge to Base Angle in a Regular Tetrahedron",
                    "block_type": "worked_example",
                    "component_type": "worked_example",
                    "content": {
                        "problem": (
                            "A regular tetrahedron $VABC$ has edges of length $4\\text{ cm}$. "
                            "Calculate the angle between any slant edge (e.g., $VA$) and the base plane $ABC$."
                        ),
                        "steps": [
                            "**What we need to find:** The angle $\\angle VAO$ where $O$ is the centroid of the equilateral base $ABC$.",
                            "**Step 1 — Find the altitude of the base equilateral triangle $AM$:**\n"
                            "$$AM = 4 \\cdot \\sin(60^\\circ) = 4 \\times \\frac{\\sqrt{3}}{2} = 2\\sqrt{3} \\approx 3.464\\text{ cm}$$",
                            "**Step 2 — Find the projection length $OA$ (centroid distance):**\n"
                            "$$OA = \\frac{2}{3} AM = \\frac{2}{3}(2\\sqrt{3}) = \\frac{4\\sqrt{3}}{3} \\approx 2.3094\\text{ cm}$$",
                            "**Step 3 — Extract right triangle $\\triangle VOA$ ($VO \\perp OA$):**\n"
                            "$$\\cos(\\angle VAO) = \\frac{OA}{VA} = \\frac{2.3094}{4} = 0.57735$$",
                            "**Step 4 — Calculate the angle:**\n"
                            "$$\\angle VAO = \\arccos(0.57735) \\approx 54.74^\\circ$$\n\n"
                            "**Answer:** The angle between any slant edge and the base plane is $54.74^\\circ$."
                        ]
                    }
                },

                # PAGE 6 — worked_example (Level 3: Space Diagonal Angles in a Cuboid)
                {
                    "page_number": 6,
                    "page_title": "Example 3: Space Diagonal Inclinations in a Cuboid",
                    "block_type": "worked_example",
                    "component_type": "worked_example",
                    "content": {
                        "problem": (
                            "In a cuboid $ABCDEFGH$, the dimensions are $AB = 8\\text{ cm}$, $BC = 4.5\\text{ cm}$, and $AE = 6\\text{ cm}$.\n\n"
                            "Calculate:\n"
                            "(a) The angle between space diagonal $BH$ and the bottom base plane $ABCD$.\n"
                            "(b) The angle between space diagonal $BH$ and the vertical side face $CDHG$."
                        ),
                        "steps": [
                            "**What to identify:** Find the projection for each plane and isolate the corresponding right triangle.",
                            "**Step 1 — Angle of $BH$ with base plane $ABCD$:**\n"
                            "- The projection of $BH$ on the base is $BD$.\n"
                            "- Base diagonal $BD = \\sqrt{8^2 + 4.5^2} = \\sqrt{64 + 20.25} = \\sqrt{84.25} \\approx 9.179\\text{ cm}$.\n"
                            "- Vertical height $HD = 6\\text{ cm}$.\n"
                            "- In right triangle $\\triangle BDH$ ($HD \\perp BD$):\n"
                            "$$\\tan(\\angle HBD) = \\frac{HD}{BD} = \\frac{6}{9.1788} \\approx 0.6537$$\n"
                            "$$\\angle HBD = \\arctan(0.6537) \\approx 33.17^\\circ$$.",
                            "**Step 2 — Angle of $BH$ with side face $CDHG$:**\n"
                            "- The projection of $BH$ on face $CDHG$ is $CH$.\n"
                            "- Face diagonal $CH = \\sqrt{CD^2 + DH^2} = \\sqrt{8^2 + 6^2} = \\sqrt{100} = 10\\text{ cm}$.\n"
                            "- Perpendicular edge from $B$ to face $CDHG$ is $BC = 4.5\\text{ cm}$.\n"
                            "- In right triangle $\\triangle BCH$ ($BC \\perp CH$):\n"
                            "$$\\tan(\\angle BHC) = \\frac{BC}{CH} = \\frac{4.5}{10} = 0.45$$\n"
                            "$$\\angle BHC = \\arctan(0.45) \\approx 24.23^\\circ$$.\n\n"
                            "**Answer:** (a) $33.17^\\circ$ with base plane; (b) $24.23^\\circ$ with side face $CDHG$."
                        ]
                    }
                },

                # PAGE 7 — worked_example (Level 4: Slant Generator in a Conical Frustum)
                {
                    "page_number": 7,
                    "page_title": "Example 4: Slant Generator Angle in a Truncated Cone",
                    "block_type": "worked_example",
                    "component_type": "worked_example",
                    "content": {
                        "problem": (
                            "A bucket has the shape of a truncated cone (frustum). "
                            "The bottom circular base has radius $r_1 = 6\\text{ cm}$, the top circular opening has radius $r_2 = 10\\text{ cm}$, "
                            "and the vertical depth of the bucket is $h = 12\\text{ cm}$.\n\n"
                            "Calculate the angle of inclination of the slant side (generator) with the horizontal base."
                        ),
                        "steps": [
                            "**What we need to find:** The angle $\\theta$ in the right-angled cross-section of the frustum.",
                            "**Step 1 — Determine the horizontal offset (radial projection):**\n"
                            "$$\\Delta r = r_2 - r_1 = 10 - 6 = 4\\text{ cm}$$",
                            "**Step 2 — Extract the vertical right-angled cross-section:**\n"
                            "- Vertical height: $\\text{Opposite} = 12\\text{ cm}$.\n"
                            "- Horizontal projection: $\\text{Adjacent} = \\Delta r = 4\\text{ cm}$.",
                            "**Step 3 — Calculate inclination angle using tangent:**\n"
                            "$$\\tan \\theta = \\frac{\\text{Height}}{\\Delta r} = \\frac{12}{4} = 3.0$$\n"
                            "$$\\theta = \\arctan(3.0) \\approx 71.57^\\circ$$\n\n"
                            "**Answer:** The angle of inclination of the slant side with the base is $71.57^\\circ$."
                        ]
                    }
                },

                # PAGE 8 — suggested_simulation
                {
                    "page_number": 8,
                    "page_title": "Explore: Line-Plane Inclination Visualizer",
                    "block_type": "suggested_simulation",
                    "component_type": "suggested_simulation",
                    "content": {
                        "purpose": (
                            "An interactive 3D solid visualizer showing the relationship between a slant line, "
                            "its orthogonal shadow on the floor, and the extracted right-angled cross-section."
                        ),
                        "instruction": (
                            "Select between a Pyramid, Cone, and Cuboid. "
                            "Adjust the Height slider and Base Width slider to see how the inclination angle $\\theta$ dynamically updates. "
                            "Click 'Extract 2D Triangle' to animate the cross-section pulling out onto a flat plane."
                        ),
                        "archetype": "math_line_plane_inclination_visualizer",
                        "pedagogical_value": (
                            "Directly reinforces that the angle with a plane is always measured against the orthogonal projection."
                        )
                    },
                    "asset_info": {
                        "archetype": "math_line_plane_inclination_visualizer",
                        "title": "Interactive Line-Plane Inclination Visualizer",
                        "asset_type": "simulation"
                    }
                },

                # PAGE 9 — common_misconception
                {
                    "page_number": 9,
                    "page_title": "Common Error: Measuring to the Wrong Base Line",
                    "block_type": "common_misconception",
                    "component_type": "common_misconception",
                    "content": {
                        "text": (
                            "### The Face-Edge Trap\n\n"
                            "When asked for the angle between a slant edge $VC$ of a pyramid and the base plane $ABCD$, "
                            "many students mistakenly calculate the angle **$\\angle VCB$** (along the side triangular face).\n\n"
                            "- **Why This is Wrong:** Edge $BC$ is just a perimeter boundary line; it is **not** the shadow of $VC$ directly beneath the apex.\n"
                            "- **The Correct Procedure:** The apex $V$ drops vertically straight down to the base center $O$. The true shadow is the half-diagonal $OC$.\n"
                            "- **The Rule:** The angle with the base is **strictly $\\angle VCO$**, never $\\angle VCB$."
                        )
                    }
                },

                # PAGE 10 — knowledge_check
                {
                    "page_number": 10,
                    "page_title": "Check Your Understanding: Line-Plane Angle",
                    "block_type": "knowledge_check",
                    "component_type": "multiple_choice",
                    "content": {
                        "check_type": "multiple_choice",
                        "question": (
                            "In a pyramid $VABCD$ with apex $V$ directly above base center $O$, "
                            "which angle represents the angle between slant edge $VB$ and the base plane $ABCD$?"
                        ),
                        "options": [
                            "A: $\\angle VBC$",
                            "B: $\\angle VBA$",
                            "C: $\\angle VBO$",
                            "D: $\\angle VBD$"
                        ],
                        "answer": "C",
                        "explanation": (
                            "The orthogonal projection of $VB$ onto the base plane is the half-diagonal segment $OB$. "
                            "Therefore, the angle between $VB$ and the base plane is $\\angle VBO$. Option C is correct."
                        )
                    }
                },

                # PAGE 11 — summary
                {
                    "page_number": 11,
                    "page_title": "Key Takeaways: Line-to-Plane Angles",
                    "block_type": "summary",
                    "component_type": "summary",
                    "content": {
                        "text": (
                            "### Master Summary: Line-to-Plane Angles\n\n"
                            "| Step | Action | Mathematical Rule |\n"
                            "|:---|:---|:---|\n"
                            "| **1. Identify Intersection** | Find where the line meets the plane | Vertex $A$ |\n"
                            "| **2. Drop Perpendicular** | Drop vertical height from top to plane | Foot $O$ ($VO \\perp \\text{Plane}$) |\n"
                            "| **3. Extract Triangle** | Form right triangle $\\triangle VOA$ | $\\angle VOA = 90^\\circ$ |\n"
                            "| **4. Calculate Angle** | Use $\\cos \\theta = \\frac{OA}{VA}$ or $\\tan \\theta = \\frac{VO}{OA}$ | $\\theta = \\angle VAO$ |\n\n"
                            "> **Golden Rule:** The angle with a plane is always measured against its **orthogonal projection (shadow)**, never against a random boundary edge!"
                        )
                    }
                }
            ]
        },

        # ===================================================================
        # MODULE 3.4: Angle Between Two Planes (Dihedral Angle)
        # ===================================================================
        {
            "unit_order": 4,
            "unit_title": "Module 3.4: Angle Between Two Planes (Dihedral Angle)",
            "lesson_title": "Angle Between Two Planes (Dihedral Angle)",
            "lesson_blocks": [
                # PAGE 1 — learning_goal
                {
                    "page_number": 1,
                    "page_title": "Mastering Dihedral Angles Between Planes",
                    "block_type": "learning_goal",
                    "component_type": "learning_goal",
                    "content": {
                        "title": "What You Will Master in This Lesson",
                        "goals": [
                            "Define and identify the dihedral angle between two intersecting planes using the perpendicular spine rule.",
                            "Calculate the angle between a slant face and the base plane in pyramids and prisms.",
                            "Calculate the angle between two adjacent slant faces in a regular tetrahedron.",
                            "Determine angles between diagonal cross-sectional planes in cuboids."
                        ]
                    }
                },

                # PAGE 2 — concept_explanation
                {
                    "page_number": 2,
                    "page_title": "The Book Spine Rule: Defining Dihedral Angles",
                    "block_type": "concept_explanation",
                    "component_type": "concept_explanation",
                    "content": {
                        "title": "How to Measure the Angle Between Two Flat Surfaces",
                        "body": (
                            "Two planes meet along a straight line of intersection (like the spine of a book or the ridge of a roof).\n\n"
                            "### The Partially Opened Book Analogy\n"
                            "Take a book open on your desk. The front cover is Plane 1, the back cover is Plane 2, and the spine is the intersection line.\n\n"
                            "- If you draw two random diagonal lines on the covers that meet at the spine, the angle between them changes depending on their slant.\n"
                            "- To get the **true measurement of how far open the book is**, you must draw lines that are strictly **perpendicular ($90^\\circ$) to the spine** on both covers, meeting at the exact same point!\n\n"
                            "### Formal Definition of a Dihedral Angle\n"
                            "The **dihedral angle** between two planes $P_1$ and $P_2$ intersecting along line $AB$ is the angle $\\angle XMY$, where:\n"
                            "1. Point $M$ is a common point on the intersection line $AB$.\n"
                            "2. Line $MX$ lies in plane $P_1$ and is **perpendicular to $AB$** ($MX \\perp AB$).\n"
                            "3. Line $MY$ lies in plane $P_2$ and is **perpendicular to $AB$** ($MY \\perp AB$)."
                        )
                    }
                },

                # PAGE 3 — formula_breakdown
                {
                    "page_number": 3,
                    "page_title": "Formulas & Methods for Dihedral Angles",
                    "block_type": "formula_breakdown",
                    "component_type": "formula_breakdown",
                    "content": {
                        "formula": (
                            "**Perpendicular Construction Condition:**\n"
                            "$$\\text{Dihedral Angle } \\theta = \\angle XMY \\quad \\text{where } MX \\perp AB \\text{ and } MY \\perp AB$$\n\n"
                            "**Cosine Rule Calculation on $\\triangle XMY$:**\n"
                            "$$\\cos \\theta = \\frac{MX^2 + MY^2 - XY^2}{2 \\cdot MX \\cdot MY}$$"
                        ),
                        "content": (
                            "### 3 Standard Dihedral Cases in Form 4 Math\n\n"
                            "| Scenario | Meeting Line | Perpendicular Lines | Solving Tool |\n"
                            "|:---|:---|:---|:---|\n"
                            "| **Slant Face to Base** (Pyramid) | Base edge $AB$ | Slant height $VM \\perp AB$, Base apothem $OM \\perp AB$ | Right $\\triangle VOM$: $\\tan \\theta = \\frac{VO}{OM}$ |\n"
                            "| **Adjacent Faces** (Tetrahedron) | Meeting edge $AB$ | Face medians $VM \\perp AB$, $CM \\perp AB$ | Oblique $\\triangle VMC$: Cosine Rule |\n"
                            "| **Diagonal Plane** (Cuboid) | Top edge $GH$ | Front diagonal $AH \\perp GH$, Top edge $EH \\perp GH$ | Right $\\triangle AEH$: $\\tan \\theta = \\frac{AE}{EH}$ |"
                        )
                    }
                },

                # PAGE 4 — worked_example (Level 1: Diagonal Plane in a Cuboid)
                {
                    "page_number": 4,
                    "page_title": "Example 1: Diagonal Plane Angle with Top Face in a Cuboid",
                    "block_type": "worked_example",
                    "component_type": "worked_example",
                    "content": {
                        "problem": (
                            "In the cuboid $ABCDEFGH$, the dimensions are $FG = 4.5\\text{ cm}$, $GH = 8\\text{ cm}$, and vertical height $AE = BF = CG = DH = 6\\text{ cm}$.\n\n"
                            "Calculate the size of the dihedral angle between the diagonal plane $ABGH$ and the top horizontal plane $FGHE$."
                        ),
                        "steps": [
                            "**What we need to identify:** The intersection line of the two planes and perpendiculars drawn to it from both planes.",
                            "**Step 1 — Identify the intersection line:**\n"
                            "The tilted plane $ABGH$ and the top plane $FGHE$ meet along the top edge **$GH$**.",
                            "**Step 2 — Construct perpendiculars to $GH$ at point $H$:**\n"
                            "- In rectangle $FGHE$: edge $EH \\perp GH$ at point $H$.\n"
                            "- In diagonal plane $ABGH$: line $AH \\perp GH$ at point $H$ (since $AH$ lies in the vertical $yz$-plane cross-section).\n"
                            "- Therefore, the dihedral angle between the planes is the angle **$\\angle AHE$**.",
                            "**Step 3 — Extract right triangle $\\triangle AEH$ ($AE \\perp EH$):**\n"
                            "- Opposite side (vertical height): $AE = 6\\text{ cm}$.\n"
                            "- Adjacent side (top face width): $EH = 4.5\\text{ cm}$.",
                            "**Step 4 — Calculate angle using tangent:**\n"
                            "$$\\tan(\\angle AHE) = \\frac{AE}{EH} = \\frac{6}{4.5} = \\frac{4}{3} \\approx 1.3333$$\n"
                            "$$\\angle AHE = \\arctan(1.3333) \\approx 53.13^\\circ$$\n\n"
                            "**Answer:** The angle between plane $ABGH$ and plane $FGHE$ is $53.13^\\circ$."
                        ]
                    }
                },

                # PAGE 5 — worked_example (Level 2: Slant Face to Base in a Square Pyramid)
                {
                    "page_number": 5,
                    "page_title": "Example 2: Slant Face to Base Angle in a Square Pyramid",
                    "block_type": "worked_example",
                    "component_type": "worked_example",
                    "content": {
                        "problem": (
                            "A right pyramid $VABCD$ has a square base $ABCD$ of side $10\\text{ cm}$ and a vertical height $VO = 12\\text{ cm}$ "
                            "(where $O$ is the center of the square base).\n\n"
                            "Calculate the angle between the slant face $VAB$ and the base plane $ABCD$."
                        ),
                        "steps": [
                            "**What we need to find:** The angle between face $VAB$ and base $ABCD$ meeting at edge $AB$.",
                            "**Step 1 — Identify the intersection line and midpoint $M$:**\n"
                            "- The planes intersect along base edge $AB$.\n"
                            "- Let $M$ be the midpoint of edge $AB$.",
                            "**Step 2 — Construct perpendiculars to $AB$ at $M$:**\n"
                            "- In isosceles triangle $VAB$: slant height $VM \\perp AB$.\n"
                            "- In square base $ABCD$: line $OM \\perp AB$ (where $OM = \\frac{1}{2} \\text{side} = \\frac{10}{2} = 5\\text{ cm}$).\n"
                            "- The dihedral angle is **$\\angle VMO$**.",
                            "**Step 3 — Extract right triangle $\\triangle VOM$ ($VO \\perp OM$):**\n"
                            "- Opposite side (height): $VO = 12\\text{ cm}$.\n"
                            "- Adjacent side (base apothem): $OM = 5\\text{ cm}$.",
                            "**Step 4 — Calculate using tangent ratio:**\n"
                            "$$\\tan(\\angle VMO) = \\frac{VO}{OM} = \\frac{12}{5} = 2.4$$\n"
                            "$$\\angle VMO = \\arctan(2.4) \\approx 67.38^\\circ$$\n\n"
                            "**Answer:** The angle between slant face $VAB$ and the base plane is $67.38^\\circ$."
                        ]
                    }
                },

                # PAGE 6 — worked_example (Level 3: Dihedral Angle of a Regular Tetrahedron)
                {
                    "page_number": 6,
                    "page_title": "Example 3: Dihedral Angle Between Faces of a Tetrahedron",
                    "block_type": "worked_example",
                    "component_type": "worked_example",
                    "content": {
                        "problem": (
                            "A regular tetrahedron $VABC$ has edges of length $4\\text{ cm}$. "
                            "Calculate the dihedral angle between any two adjacent triangular faces (e.g., face $VAB$ and base face $CAB$)."
                        ),
                        "steps": [
                            "**What we need to find:** The angle between faces $VAB$ and $CAB$ meeting along edge $AB$.",
                            "**Step 1 — Construct perpendiculars to meeting edge $AB$:**\n"
                            "- Let $M$ be the midpoint of edge $AB$.\n"
                            "- In equilateral face $VAB$: median $VM \\perp AB$ with length $VM = 4\\sin(60^\\circ) = 2\\sqrt{3}\\text{ cm}$.\n"
                            "- In equilateral face $CAB$: median $CM \\perp AB$ with length $CM = 4\\sin(60^\\circ) = 2\\sqrt{3}\\text{ cm}$.\n"
                            "- The dihedral angle is the angle **$\\angle VMC$** in $\\triangle VMC$.",
                            "**Step 2 — Tabulate side lengths of $\\triangle VMC$:**\n"
                            "- $VM = 2\\sqrt{3}\\text{ cm}$\n"
                            "- $MC = 2\\sqrt{3}\\text{ cm}$\n"
                            "- $VC = 4\\text{ cm}$ (opposite edge length)",
                            "**Step 3 — Apply the Cosine Rule in $\\triangle VMC$:**\n"
                            "$$VC^2 = VM^2 + MC^2 - 2(VM)(MC)\\cos(\\angle VMC)$$\n"
                            "$$4^2 = (2\\sqrt{3})^2 + (2\\sqrt{3})^2 - 2(2\\sqrt{3})(2\\sqrt{3})\\cos(\\angle VMC)$$\n"
                            "$$16 = 12 + 12 - 24\\cos(\\angle VMC) \\implies 16 = 24 - 24\\cos(\\angle VMC)$$",
                            "**Step 4 — Solve for $\\cos(\\angle VMC)$:**\n"
                            "$$24\\cos(\\angle VMC) = 24 - 16 = 8$$\n"
                            "$$\\cos(\\angle VMC) = \\frac{8}{24} = \\frac{1}{3} \\approx 0.3333$$\n"
                            "$$\\angle VMC = \\arccos\\left(\\frac{1}{3}\\right) \\approx 70.53^\\circ$$\n\n"
                            "**Answer:** The dihedral angle between any two adjacent faces of a regular tetrahedron is $70.53^\\circ$."
                        ]
                    }
                },

                # PAGE 7 — worked_example (Level 4: Exam-Style Angle Between Slant Faces at a Slant Edge)
                {
                    "page_number": 7,
                    "page_title": "Example 4: Angle Between Adjacent Slant Faces at an Edge",
                    "block_type": "worked_example",
                    "component_type": "worked_example",
                    "content": {
                        "problem": (
                            "A right pyramid $VABCD$ has a square base $ABCD$ of side $8\\text{ cm}$ and slant edges of length $VA = VB = VC = VD = 10\\text{ cm}$.\n\n"
                            "Calculate the dihedral angle between the two adjacent slant faces $VAB$ and $VBC$ that meet at the slant edge $VB$."
                        ),
                        "steps": [
                            "**What we need to find:** The angle between faces $VAB$ and $VBC$ meeting along slant edge $VB$.",
                            "**Step 1 — Drop perpendiculars from $A$ and $C$ to meeting edge $VB$:**\n"
                            "- In $\\triangle VAB$, drop an altitude from vertex $A$ perpendicular to $VB$, landing at point $K$ ($AK \\perp VB$).\n"
                            "- By symmetry, in $\\triangle VBC$, the line $CK \\perp VB$ at the exact same point $K$.\n"
                            "- The required dihedral angle is **$\\angle AKC$** in $\\triangle AKC$.",
                            "**Step 2 — Calculate the length $AK$ using the area of $\\triangle VAB$:**\n"
                            "- In isosceles $\\triangle VAB$ (sides $10, 10, 8$), midpoint of $AB$ is $M$ ($AM = 4$).\n"
                            "- Slant height $VM = \\sqrt{10^2 - 4^2} = \\sqrt{84} = 2\\sqrt{21} \\approx 9.165\\text{ cm}$.\n"
                            "- Area of $\\triangle VAB = \\frac{1}{2} \\times \\text{base} \\times \\text{height} = \\frac{1}{2} \\times 8 \\times 2\\sqrt{21} = 8\\sqrt{21}$.\n"
                            "- Equating area using base $VB$: $\\frac{1}{2} \\times VB \\times AK = \\text{Area} \\implies \\frac{1}{2} \\times 10 \\times AK = 8\\sqrt{21} \\implies AK = \\frac{16\\sqrt{21}}{10} = 1.6\\sqrt{21} \\approx 7.332\\text{ cm}$.\n"
                            "- By symmetry: $CK = AK = 7.332\\text{ cm}$.",
                            "**Step 3 — Calculate base diagonal $AC$:**\n"
                            "$$AC = \\sqrt{8^2 + 8^2} = 8\\sqrt{2} \\approx 11.314\\text{ cm}$$",
                            "**Step 4 — Apply Cosine Rule in $\\triangle AKC$:**\n"
                            "$$\\cos(\\angle AKC) = \\frac{AK^2 + CK^2 - AC^2}{2 \\cdot AK \\cdot CK} = \\frac{7.332^2 + 7.332^2 - (8\\sqrt{2})^2}{2 \\times 7.332 \\times 7.332}$$\n"
                            "$$\\cos(\\angle AKC) = \\frac{53.76 + 53.76 - 128}{107.52} = \\frac{-20.48}{107.52} \\approx -0.19048$$\n"
                            "$$\\angle AKC = \\arccos(-0.19048) \\approx 100.98^\\circ$$\n\n"
                            "**Answer:** The dihedral angle between adjacent slant faces $VAB$ and $VBC$ is $100.98^\\circ$."
                        ]
                    }
                },

                # PAGE 8 — suggested_simulation
                {
                    "page_number": 8,
                    "page_title": "Explore: Dihedral Angle Hinged Planes Visualizer",
                    "block_type": "suggested_simulation",
                    "component_type": "suggested_simulation",
                    "content": {
                        "purpose": (
                            "An interactive 3D solid and hinged planes simulator demonstrating why dihedral angles "
                            "must be measured perpendicular to the intersection line."
                        ),
                        "instruction": (
                            "Drag the angle slider to open or close the hinged planes. "
                            "Observe the two red perpendicular vectors meet at $90^\\circ$ to the hinge spine. "
                            "Toggle between Roof Truss, Pyramid Slant Faces, and Tetrahedron modes to view extracted 2D cross-sections."
                        ),
                        "archetype": "math_dihedral_angle_book_visualizer",
                        "pedagogical_value": (
                            "Visually embeds the Book Spine Rule and helps students construct correct altitude lines $AK \\perp VB$."
                        )
                    },
                    "asset_info": {
                        "archetype": "math_dihedral_angle_book_visualizer",
                        "title": "Interactive Dihedral Angle Hinged Planes Visualizer",
                        "asset_type": "simulation"
                    }
                },

                # PAGE 9 — common_misconception
                {
                    "page_number": 9,
                    "page_title": "Common Error: Measuring Plane Angles with Oblique Corner Lines",
                    "block_type": "common_misconception",
                    "component_type": "common_misconception",
                    "content": {
                        "text": (
                            "### The Corner Angle Fallacy\n\n"
                            "In a regular tetrahedron $VABC$, many students mistakenly think the angle between face $VAB$ and base $ABC$ "
                            "is the face corner angle **$\\angle VAC = 60^\\circ$**.\n\n"
                            "- **Why This is Wrong:** Edge $VA$ and edge $CA$ meet at vertex $A$ at an oblique angle ($60^\\circ$); neither line is perpendicular to edge $AB$!\n"
                            "- **The True Measurement:** You must construct lines from the midpoint $M$ of $AB$ ($VM \\perp AB$ and $CM \\perp AB$).\n"
                            "- **The Result:** The true dihedral angle is $\\angle VMC \\approx 70.53^\\circ$, which is significantly steeper than the $60^\\circ$ face angle."
                        )
                    }
                },

                # PAGE 10 — knowledge_check
                {
                    "page_number": 10,
                    "page_title": "Check Your Understanding: Dihedral Angle Rules",
                    "block_type": "knowledge_check",
                    "component_type": "multiple_choice",
                    "content": {
                        "check_type": "multiple_choice",
                        "question": (
                            "Two planes $P_1$ and $P_2$ intersect along a line $L$. "
                            "To measure the true dihedral angle between them, which condition must the two measuring lines $M_1$ and $M_2$ satisfy?"
                        ),
                        "options": [
                            "A: They must both be parallel to the intersection line $L$.",
                            "B: They must lie in their respective planes and meet at a common point on $L$, both perpendicular to $L$.",
                            "C: They can be any two diagonal lines drawn on the two planes.",
                            "D: One line must be vertical and the other horizontal."
                        ],
                        "answer": "B",
                        "explanation": (
                            "By definition, the dihedral angle is measured between two lines drawn in the respective planes "
                            "that meet at a common point on the intersection line $L$ and are both strictly perpendicular to $L$. "
                            "Option B is correct."
                        )
                    }
                },

                # PAGE 11 — summary
                {
                    "page_number": 11,
                    "page_title": "Key Takeaways: Dihedral Angles",
                    "block_type": "summary",
                    "component_type": "summary",
                    "content": {
                        "text": (
                            "### Master Summary: Angle Between Two Planes\n\n"
                            "| Step | Action | Practical Tip |\n"
                            "|:---|:---|:---|\n"
                            "| **1. Find Intersection Line** | Identify where the two planes meet | The hinge line (e.g. edge $AB$) |\n"
                            "| **2. Construct Perpendiculars** | Draw lines in each plane meeting at $90^\\circ$ to the hinge at point $M$ | Use face medians or altitudes ($VM \\perp AB$) |\n"
                            "| **3. Extract Triangle** | Form $\\triangle XMY$ containing both perpendiculars | Check side lengths |\n"
                            "| **4. Calculate Angle** | Use SOH-CAH-TOA if right-angled, or Cosine Rule if oblique | $\\cos \\theta = \\frac{MX^2 + MY^2 - XY^2}{2 \\cdot MX \\cdot MY}$ |\n\n"
                            "> **Memory Rule:** Think of opening a book! The angle is always measured straight across the pages, perpendicular to the spine."
                        )
                    }
                }
            ]
        }
    ]

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
    ingest_topic3_geometry()
