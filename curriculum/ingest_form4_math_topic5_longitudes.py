#!/usr/bin/env python3
"""
VLearn Form 4 Mathematics — Topic 5: Longitudes and Latitudes Ingestion Script
================================================================================
Curriculum: 844
Grade: Form 4 (level=1)
Subject: Mathematics
Topic: Topic 5: Longitudes and Latitudes (order=5)

Modules / LearningUnits:
  5.1 Earth Coordinates, Great Circles, and Small Circle Radii (r = R cos α)
  5.2 Distance Calculation Along Great Circles (Kilometers & Nautical Miles)
  5.3 Distance Along Parallels of Latitude (Small Circles) & Routing Optimization
  5.4 Earth Rotation, Longitude-Time Relationships, and Speed in Knots

Pedagogical Structure per Lesson: 11 Pages
  Page 1:  learning_goal (Student-friendly outcomes)
  Page 2:  concept_explanation (Real-world analogies: orange slicing, spinning globe)
  Page 3:  formula_breakdown / definition_card (Word formulas, CAST/coordinate charts)
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
  - Humanized word formulas alongside KaTeX notation.
  - Rigorous mathematical accuracy (reconstructed parameters, standardized units).
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


def get_topic5_data():
    """Returns the complete structured curriculum payload for Topic 5."""
    return [
        # =====================================================================
        # MODULE 5.1: Earth Coordinates & Radii of Great and Small Circles
        # =====================================================================
        {
            "unit_order": 1,
            "unit_title": "Module 5.1: Earth Coordinates, Great Circles, and Small Circle Radii",
            "lesson_title": "Earth Coordinates and Radii of Great and Small Circles",
            "lesson_blocks": [
                # PAGE 1 — learning_goal
                {
                    "page_number": 1,
                    "page_title": "Mastering Earth Coordinates & Circle Radii",
                    "block_type": "learning_goal",
                    "component_type": "learning_goal",
                    "content": {
                        "title": "What You Will Master in This Lesson",
                        "goals": [
                            "Locate points on the Earth's spherical surface using $(\\text{Latitude } \\alpha^\\circ\\text{N/S}, \\text{Longitude } \\beta^\\circ\\text{E/W})$.",
                            "Determine the coordinates of antipodal (diametrically opposite) points on Earth.",
                            "Distinguish between Great Circles (passing through Earth's center) and Small Circles (parallels of latitude).",
                            "Derive and apply the small circle radius formula $r = R \\cos \\alpha$, where $\\alpha$ is the latitude."
                        ]
                    }
                },

                # PAGE 2 — concept_explanation
                {
                    "page_number": 2,
                    "page_title": "The Sliced Orange Analogy: Great vs. Small Circles",
                    "block_type": "concept_explanation",
                    "component_type": "concept_explanation",
                    "content": {
                        "body": (
                            "To navigate the Earth, we model it as a sphere of radius $R \\approx 6370\\text{ km}$. "
                            "Every point on Earth is fixed by two perpendicular angular measurements: **Latitude** and **Longitude**.\n\n"
                            "### The Sliced Orange Analogy\n\n"
                            "Imagine slicing a round orange with a knife:\n\n"
                            "- **The Great Circle:** If you slice the orange **directly through the exact center**, you get the largest possible circular cross-section. "
                            "Its radius is equal to the Earth's full radius ($R$). Examples include the **Equator ($0^\\circ$)** and all **Longitude Meridians**.\n"
                            "- **The Small Circle:** If you slice the orange **above or below the center**, you get a smaller circular cross-section. "
                            "As you slice closer to the top (the North Pole) or bottom (the South Pole), the slices shrink rapidly!\n\n"
                            "### Why Latitude Circles Shrink ($r = R \\cos \\alpha$)\n\n"
                            "Consider a point $P$ on latitude $\\alpha$:\n"
                            "- The distance from the Earth's center $O$ to point $P$ is the full Earth radius ($R$).\n"
                            "- In the right-angled triangle formed between the Earth's axis, the center, and point $P$, the horizontal radius of the latitude circle is the adjacent side:\n"
                            "$$\\cos \\alpha = \\frac{\\text{Small Circle Radius } (r)}{\\text{Earth Radius } (R)} \\implies r = R \\cos \\alpha$$"
                        )
                    }
                },

                # PAGE 3 — formula_breakdown
                {
                    "page_number": 3,
                    "page_title": "Core Formulas for Earth Coordinates and Radii",
                    "block_type": "formula_breakdown",
                    "component_type": "formula_breakdown",
                    "content": {
                        "formula": "**Small Circle Radius Formula:**\n$$r = R \\cos \\alpha \\quad \\text{(where } R = 6370\\text{ km and } \\alpha = \\text{Latitude)}$$\n\n**In Plain English:**\n$$\\text{Small Circle Radius } (r) = \\text{Earth Radius } (R) \\times \\cos(\\text{Latitude } \\alpha)$$",
                        "content": (
                            "### Fundamental Earth Geometry Reference\n\n"
                            "| Geometry Feature | Type of Circle | Radius ($r$) | Key Example |\n"
                            "|:---|:---:|:---:|:---|\n"
                            "| **Equator ($0^\\circ$)** | Great Circle | $R = 6370\\text{ km}$ | Divides Northern & Southern Hemispheres. |\n"
                            "| **Meridians (Longitudes)** | Great Circle Semicircles | $R = 6370\\text{ km}$ | Run from North Pole to South Pole (Prime Meridian $= 0^\\circ$). |\n"
                            "| **Parallels of Latitude ($\\alpha$)** | Small Circles | $r = R \\cos \\alpha$ | Horizontal rings parallel to Equator ($60^\\circ\\text{N} \\implies r = 0.5R$). |\n"
                            "| **Poles ($90^\\circ\\text{N/S}$)** | Single Points | $r = 0\\text{ km}$ | Top and bottom rotation points ($r = R \\cos 90^\\circ = 0$). |\n\n"
                            "> **Antipodal Rule:** The antipodal (diametrically opposite) point of $(\\alpha^\\circ\\text{N}, \\beta^\\circ\\text{W})$ is "
                            "$(\\alpha^\\circ\\text{S}, (180^\\circ - \\beta^\\circ)\\text{E})$."
                        )
                    }
                },

                # PAGE 4 — worked_example (Level 1: Easy / Reading Coordinates and Antipodes)
                {
                    "page_number": 4,
                    "page_title": "Example 1: Finding Coordinate Positions and Antipodal Points",
                    "block_type": "worked_example",
                    "component_type": "worked_example",
                    "content": {
                        "problem": (
                            "A weather station $P$ is located at $(40^\\circ\\text{N}, 30^\\circ\\text{W})$.\n"
                            "(a) State whether the latitude circle at $P$ is a great circle or a small circle.\n"
                            "(b) Determine the exact geographic coordinates of the point $Q$ diametrically opposite to $P$ on the Earth (the antipode of $P$)."
                        ),
                        "steps": [
                            "**What we need to find:** Circle classification and antipodal coordinates of $P(40^\\circ\\text{N}, 30^\\circ\\text{W})$.",
                            "**Step 1 — Classify the circle:**\n"
                            "The latitude of $P$ is $40^\\circ\\text{N} \\neq 0^\\circ$. "
                            "Only the Equator ($0^\\circ$) is a Great Circle latitude. "
                            "Therefore, the parallel of latitude $40^\\circ\\text{N}$ is a **Small Circle**.",
                            "**Step 2 — Determine the antipodal latitude:**\n"
                            "The diametrically opposite point has the same angular distance from the Equator but in the opposite hemisphere:\n"
                            "$$\\text{Antipodal Latitude} = 40^\\circ\\text{S}$$",
                            "**Step 3 — Determine the antipodal longitude:**\n"
                            "The opposite longitude lies on the meridian that completes a straight $180^\\circ$ circle through the poles:\n"
                            "$$\\text{Antipodal Longitude} = 180^\\circ - 30^\\circ = 150^\\circ\\text{E}$$",
                            "**Step 4 — Assemble the coordinate pair:**\n"
                            "$$Q = (40^\\circ\\text{S}, 150^\\circ\\text{E})$$\n\n"
                            "**Answer:** (a) Small Circle; (b) Antipodal position is $(40^\\circ\\text{S}, 150^\\circ\\text{E})$."
                        ]
                    }
                },

                # PAGE 5 — worked_example (Level 2: Moderate / Calculating Parallel Radius)
                {
                    "page_number": 5,
                    "page_title": "Example 2: Calculating the Radius of a Parallel of Latitude",
                    "block_type": "worked_example",
                    "component_type": "worked_example",
                    "content": {
                        "problem": (
                            "Calculate the radius of the parallel of latitude $60^\\circ\\text{N}$, taking the Earth's radius as $R = 6370\\text{ km}$."
                        ),
                        "steps": [
                            "**What we need to find:** The small circle radius $r$ at latitude $\\alpha = 60^\\circ\\text{N}$.",
                            "**Step 1 — State the small circle radius formula:**\n"
                            "$$r = R \\cos \\alpha$$",
                            "**Step 2 — Substitute $R = 6370\\text{ km}$ and $\\alpha = 60^\\circ$:**\n"
                            "$$r = 6370 \\times \\cos(60^\\circ)$$",
                            "**Step 3 — Compute the exact value (noting $\\cos 60^\\circ = 0.5$):**\n"
                            "$$r = 6370 \\times 0.5 = 3185\\text{ km}$$\n\n"
                            "**Answer:** $r = 3185\\text{ km}$ (the parallel at $60^\\circ\\text{N}$ is exactly half the width of the Equator)."
                        ]
                    }
                },

                # PAGE 6 — worked_example (Level 3: Difficult / Radius Ratios and Unknown Latitudes)
                {
                    "page_number": 6,
                    "page_title": "Example 3: Determining Unknown Latitudes from Radius Ratios",
                    "block_type": "worked_example",
                    "component_type": "worked_example",
                    "content": {
                        "problem": (
                            "Find the latitude $\\alpha$ (in the Southern Hemisphere) of a parallel whose circumference is "
                            "$\\frac{\\sqrt{3}}{2}$ times the circumference of the Equator."
                        ),
                        "steps": [
                            "**What we need to find:** Southern latitude angle $\\alpha$.",
                            "**Step 1 — Express circumference relationship algebraically:**\n"
                            "Circumference of parallel: $C_{\\text{parallel}} = 2\\pi r = 2\\pi R \\cos \\alpha$\n"
                            "Circumference of Equator: $C_{\\text{equator}} = 2\\pi R$",
                            "**Step 2 — Set up the ratio:**\n"
                            "$$\\frac{2\\pi R \\cos \\alpha}{2\\pi R} = \\frac{\\sqrt{3}}{2} \\implies \\cos \\alpha = \\frac{\\sqrt{3}}{2}$$",
                            "**Step 3 — Solve for latitude angle $\\alpha$:**\n"
                            "$$\\alpha = \\arccos\\left(\\frac{\\sqrt{3}}{2}\\right) = 30^\\circ$$",
                            "**Step 4 — State the coordinate latitude:**\n"
                            "Since the problem specifies the Southern Hemisphere, the latitude is **$30^\\circ\\text{S}$**.\n\n"
                            "**Answer:** $30^\\circ\\text{S}$."
                        ]
                    }
                },

                # PAGE 7 — worked_example (Level 4: Exam-Style / 3D Spatial Chord Length)
                {
                    "page_number": 7,
                    "page_title": "Example 4: 3D Spatial Chord Distance Between Points on a Parallel",
                    "block_type": "worked_example",
                    "component_type": "worked_example",
                    "content": {
                        "problem": (
                            "Two towns $A(60^\\circ\\text{N}, 20^\\circ\\text{W})$ and $B(60^\\circ\\text{N}, 40^\\circ\\text{E})$ lie on the same parallel of latitude.\n"
                            "Calculate the straight-line tunnel (chord) distance through the Earth connecting $A$ and $B$, taking $R = 6370\\text{ km}$."
                        ),
                        "steps": [
                            "**What we need to calculate:** The direct straight-line distance (chord) inside the small circle slice.",
                            "**Step 1 — Find the radius of the $60^\\circ\\text{N}$ parallel circle:**\n"
                            "$$r = R \\cos(60^\\circ) = 6370 \\times 0.5 = 3185\\text{ km}$$",
                            "**Step 2 — Find the angular longitude difference $\\theta$ between $A$ and $B$:**\n"
                            "Since $A$ is $20^\\circ\\text{W}$ and $B$ is $40^\\circ\\text{E}$, they span across the Prime Meridian:\n"
                            "$$\\theta = 20^\\circ + 40^\\circ = 60^\\circ$$",
                            "**Step 3 — Apply the isosceles triangle chord formula on the small circle slice:**\n"
                            "In $\\triangle C AB$ (where $C$ is the center of the parallel slice, with $CA = CB = r = 3185\\text{ km}$ and $\\angle ACB = 60^\\circ$):\n"
                            "$$\\text{Chord } AB = 2 r \\sin\\left(\\frac{\\theta}{2}\\right) = 2 \\times 3185 \\times \\sin(30^\\circ)$$",
                            "**Step 4 — Compute the result:**\n"
                            "$$\\text{Chord } AB = 2 \\times 3185 \\times 0.5 = 3185\\text{ km}$$\n"
                            "*(Because $\\triangle C AB$ is equilateral with $60^\\circ$ vertex angle)*.\n\n"
                            "**Answer:** $3185\\text{ km}$."
                        ]
                    }
                },

                # PAGE 8 — suggested_simulation
                {
                    "page_number": 8,
                    "page_title": "Explore: 3D Earth Coordinate & Slicing Explorer",
                    "block_type": "suggested_simulation",
                    "component_type": "suggested_simulation",
                    "content": {
                        "purpose": (
                            "An interactive 3D transparent globe where students can rotate the Earth, input latitude and longitude, "
                            "and move a horizontal cutting plane from the Equator to the Poles. "
                            "The simulator dynamically reveals the right triangle $OBC$ inside the sphere and calculates $r = R \\cos \\alpha$ in real-time."
                        )
                    },
                    "asset_info": {
                        "asset_type": "simulation",
                        "archetype": "math_earth_coordinate_slicing_explorer",
                        "title": "Interactive 3D Earth Coordinate & Slicing Sandbox"
                    }
                },

                # PAGE 9 — common_misconception
                {
                    "page_number": 9,
                    "page_title": "Common Error: The Polar Radius Assumption",
                    "block_type": "common_misconception",
                    "component_type": "common_misconception",
                    "content": {
                        "text": (
                            "### Why You Must Never Use $R$ on a Parallel of Latitude\n\n"
                            "Many students assume that because the Earth has radius $R = 6370\\text{ km}$, every circle on Earth has radius $6370\\text{ km}$.\n\n"
                            "| Path Type | Circle Geometry | Correct Radius to Use |\n"
                            "|:---|:---|:---|\n"
                            "| **Meridian / Equator** | Great Circle | **Full Radius $R = 6370\\text{ km}$** |\n"
                            "| **Parallel of Latitude ($\\alpha$)** | Small Circle | **Reduced Radius $r = R \\cos \\alpha$** |\n\n"
                            "> **Memory Tip:** Moving along a parallel of latitude is walking around a smaller horizontal ring! "
                            "Always multiply the Earth radius by $\\cos \\alpha$ to shrink it down to the true circle size."
                        )
                    }
                },

                # PAGE 10 — knowledge_check (MCQ)
                {
                    "page_number": 10,
                    "page_title": "Check Your Understanding: Earth Coordinates & Radii",
                    "block_type": "knowledge_check",
                    "component_type": "multiple_choice",
                    "content": {
                        "question": "What is the radius of the parallel of latitude at $45^\\circ\\text{S}$, taking $R = 6370\\text{ km}$?",
                        "options": [
                            "A: 6370.0 km",
                            "B: 4504.3 km",
                            "C: 3185.0 km",
                            "D: 5516.6 km"
                        ],
                        "answer": "B",
                        "explanation": (
                            "1. Apply small circle radius formula: $r = R \\cos \\alpha$.\n"
                            "2. $r = 6370 \\times \\cos(45^\\circ) = 6370 \\times 0.7071 \\approx 4504.3\\text{ km}$."
                        )
                    }
                },

                # PAGE 11 — summary
                {
                    "page_number": 11,
                    "page_title": "Key Takeaways: Earth Coordinates & Circle Radii",
                    "block_type": "summary",
                    "component_type": "summary",
                    "content": {
                        "text": (
                            "### Master Summary: Earth Geometry Reference\n\n"
                            "| Concept | Formula | Key Application |\n"
                            "|:---|:---|:---|\n"
                            "| **Coordinate Format** | $(\\alpha^\\circ\\text{N/S}, \\beta^\\circ\\text{E/W})$ | Latitude first, Longitude second. |\n"
                            "| **Antipode Coordinates** | $(\\alpha^\\circ\\text{N}, \\beta^\\circ\\text{W}) \\to (\\alpha^\\circ\\text{S}, (180-\\beta)^\\circ\\text{E})$ | Opposite point through center of Earth. |\n"
                            "| **Great Circle Radius** | $R = 6370\\text{ km}$ | Equator and all Longitude Meridians. |\n"
                            "| **Small Circle Radius** | $r = R \\cos \\alpha$ | All Parallels of Latitude except Equator. |\n\n"
                            "**Rules of Thumb:**\n"
                            "- [x] North & South $\\implies$ Move along Great Circle meridians ($R$).\n"
                            "- [x] East & West $\\implies$ Move along Small Circle parallels ($r = R\\cos\\alpha$)."
                        )
                    }
                }
            ]
        },

        # =====================================================================
        # MODULE 5.2: Great Circle Distance (Kilometers & Nautical Miles)
        # =====================================================================
        {
            "unit_order": 2,
            "unit_title": "Module 5.2: Distance Calculation Along Great Circles",
            "lesson_title": "Distance Calculation Along Great Circles",
            "lesson_blocks": [
                # PAGE 1 — learning_goal
                {
                    "page_number": 1,
                    "page_title": "Mastering Great Circle Navigation Distances",
                    "block_type": "learning_goal",
                    "component_type": "learning_goal",
                    "content": {
                        "title": "What You Will Master in This Lesson",
                        "goals": [
                            "Calculate angular latitude differences ($\\theta$) along meridians spanning the same or opposite hemispheres.",
                            "Calculate Great Circle distances in kilometers using $D_{\\text{GC}} = \\frac{\\theta}{360^\\circ} \\times 2\\pi R$.",
                            "Calculate Great Circle distances in Nautical Miles (nm) using the master conversion rule $D = 60\\theta\\text{ nm}$.",
                            "Calculate shortest flight paths over the North and South Poles."
                        ]
                    }
                },

                # PAGE 2 — concept_explanation
                {
                    "page_number": 2,
                    "page_title": "The 1-Minute-of-Arc Nautical Mile Principle",
                    "block_type": "concept_explanation",
                    "component_type": "concept_explanation",
                    "content": {
                        "body": (
                            "In global maritime navigation and international aviation, distances are measured using a special unit called the **Nautical Mile (nm)**.\n\n"
                            "### Why Sailors Invented the Nautical Mile\n\n"
                            "The nautical mile is defined directly from the curvature of the Earth:\n\n"
                            "- $1\\text{ Nautical Mile}$ is exactly the arc distance subtended by **$1\\text{ minute of arc } (1')$** at the center of a Great Circle!\n"
                            "- Since there are $60\\text{ minutes}$ in $1\\text{ degree}$ ($1^\\circ = 60'$):\n"
                            "$$\\text{Every } 1^\\circ \\text{ of Great Circle arc} = 60\\text{ nautical miles (nm)}$$\n\n"
                            "### Finding the Angular Difference ($\\theta$):\n\n"
                            "- **Same Hemisphere (e.g. $10^\\circ\\text{N}$ and $45^\\circ\\text{N}$):** Subtract the angles $\\implies \\theta = 45^\\circ - 10^\\circ = 35^\\circ$.\n"
                            "- **Opposite Hemispheres (e.g. $15^\\circ\\text{S}$ and $25^\\circ\\text{N}$):** Add across the Equator $\\implies \\theta = 15^\\circ + 25^\\circ = 40^\\circ$."
                        )
                    }
                },

                # PAGE 3 — formula_breakdown
                {
                    "page_number": 3,
                    "page_title": "Master Formulas for Great Circle Distances",
                    "block_type": "formula_breakdown",
                    "component_type": "formula_breakdown",
                    "content": {
                        "formula": "**Distance in Nautical Miles (nm):**\n$$D_{\\text{GC}} = 60 \\times \\theta \\quad \\text{(where } \\theta \\text{ is angular distance in degrees)}$$\n\n**Distance in Kilometers (km):**\n$$D_{\\text{GC}} = \\frac{\\theta}{360^\\circ} \\times 2\\pi R \\quad (R = 6370\\text{ km})$$",
                        "content": (
                            "### Great Circle Distance Reference Chart\n\n"
                            "| Unit System | Formula | Constants Used | Typical Application |\n"
                            "|:---|:---|:---|:---|\n"
                            "| **Nautical Miles (nm)** | $D = 60 \\times \\theta$ | $1^\\circ = 60\\text{ nm}$ | Ship navigation, flight logging, knots speed calculations. |\n"
                            "| **Kilometers (km)** | $D = \\frac{\\theta}{360^\\circ} \\times 2\\pi R$ | $R = 6370\\text{ km}, \\pi = \\frac{22}{7}$ | Metric road/air transport, international standard specs. |\n"
                            "| **Conversion Factor** | $1\\text{ nm} \\approx 1.852\\text{ km}$ | $\\frac{40040\\text{ km}}{21600\\text{ nm}} \\approx 1.8537\\text{ km/nm}$ | Direct conversion between metric and nautical units. |\n\n"
                            "> **Over-the-Pole Rule:** If two points have longitudes summing to $180^\\circ$ (e.g. $36^\\circ\\text{E}$ and $144^\\circ\\text{W}$), "
                            "the shortest Great Circle path flies directly over the pole: $\\theta = (90^\\circ - \\alpha_1) + (90^\\circ - \\alpha_2)$."
                        )
                    }
                },

                # PAGE 4 — worked_example (Level 1: Easy / Meridian Distance in Nautical Miles)
                {
                    "page_number": 4,
                    "page_title": "Example 1: Calculating Meridian Distance in Nautical Miles",
                    "block_type": "worked_example",
                    "component_type": "worked_example",
                    "content": {
                        "problem": (
                            "Find the distance in nautical miles between port $P(10^\\circ\\text{S}, 40^\\circ\\text{E})$ and port $Q(35^\\circ\\text{N}, 40^\\circ\\text{E})$."
                        ),
                        "steps": [
                            "**What we need to find:** Great circle distance in nautical miles (nm).",
                            "**Step 1 — Verify the path is a Great Circle:**\n"
                            "Both ports share the same longitude ($40^\\circ\\text{E}$). Traveling due North/South along a longitude meridian is a **Great Circle** path.",
                            "**Step 2 — Calculate angular latitude difference $\\theta$:**\n"
                            "Since $P$ is in the Southern Hemisphere ($10^\\circ\\text{S}$) and $Q$ is in the Northern Hemisphere ($35^\\circ\\text{N}$), add the angles across the Equator:\n"
                            "$$\\theta = 10^\\circ + 35^\\circ = 45^\\circ$$",
                            "**Step 3 — Apply the Great Circle nautical miles formula:**\n"
                            "$$D = 60 \\times \\theta = 60 \\times 45 = 2700\\text{ nm}$$\n\n"
                            "**Answer:** $2700\\text{ nm}$."
                        ]
                    }
                },

                # PAGE 5 — worked_example (Level 2: Moderate / Meridian Flight Distance in Kilometers)
                {
                    "page_number": 5,
                    "page_title": "Example 2: Calculating Flight Distance in Kilometers",
                    "block_type": "worked_example",
                    "component_type": "worked_example",
                    "content": {
                        "problem": (
                            "An aircraft leaves airport $A(38.5^\\circ\\text{N}, 37.05^\\circ\\text{W})$ and flies due North along its meridian to point $B(52^\\circ\\text{N}, 37.05^\\circ\\text{W})$.\n"
                            "Calculate the distance covered in kilometers, taking $\\pi = \\frac{22}{7}$ and $R = 6370\\text{ km}$."
                        ),
                        "steps": [
                            "**What we need to find:** Metric distance in km.",
                            "**Step 1 — Calculate angular latitude difference $\\theta$:**\n"
                            "Both airports are in the Northern Hemisphere:\n"
                            "$$\\theta = 52^\\circ - 38.5^\\circ = 13.5^\\circ$$",
                            "**Step 2 — State the Great Circle metric arc formula:**\n"
                            "$$D = \\frac{\\theta}{360^\\circ} \\times 2\\pi R$$",
                            "**Step 3 — Substitute the parameters:**\n"
                            "$$D = \\frac{13.5}{360} \\times 2 \\times \\frac{22}{7} \\times 6370$$\n"
                            "$$D = \\frac{13.5}{360} \\times 40040 = 1501.5\\text{ km}$$\n\n"
                            "**Answer:** $1501.5\\text{ km}$."
                        ]
                    }
                },

                # PAGE 6 — worked_example (Level 3: Difficult / Over-the-Pole Polar Flight Path)
                {
                    "page_number": 6,
                    "page_title": "Example 3: Flight Route Over the North Pole",
                    "block_type": "worked_example",
                    "component_type": "worked_example",
                    "content": {
                        "problem": (
                            "Two international airports are located at $M(30^\\circ\\text{N}, 36^\\circ\\text{E})$ and $N(30^\\circ\\text{N}, 144^\\circ\\text{W})$.\n"
                            "Calculate the distance in nautical miles for a flight traveling directly over the North Pole connecting $M$ and $N$."
                        ),
                        "steps": [
                            "**What we need to calculate:** Polar Great Circle distance in nm.",
                            "**Step 1 — Check the longitude sum:**\n"
                            "$$\\text{Sum} = 36^\\circ\\text{E} + 144^\\circ\\text{W} = 180^\\circ$$\n"
                            "Since the longitudes sum to $180^\\circ$, $M$ and $N$ lie on opposite halves of the same Great Circle meridian passing directly through the North Pole ($90^\\circ\\text{N}$).",
                            "**Step 2 — Calculate total angular degrees $\\theta$ over the pole:**\n"
                            "- Leg 1 (from $M$ up to North Pole): $90^\\circ - 30^\\circ = 60^\\circ$\n"
                            "- Leg 2 (from North Pole down to $N$): $90^\\circ - 30^\\circ = 60^\\circ$\n"
                            "$$\\theta_{\\text{total}} = 60^\\circ + 60^\\circ = 120^\\circ$$",
                            "**Step 3 — Compute distance in nautical miles:**\n"
                            "$$D = 60 \\times \\theta = 60 \\times 120 = 7200\\text{ nm}$$\n\n"
                            "**Answer:** $7200\\text{ nm}$."
                        ]
                    }
                },

                # PAGE 7 — worked_example (Level 4: Exam-Style / Fuel Optimization & Unit Conversion)
                {
                    "page_number": 7,
                    "page_title": "Example 4: Fuel Consumption and Metric-Nautical Conversion",
                    "block_type": "worked_example",
                    "component_type": "worked_example",
                    "content": {
                        "problem": (
                            "A cargo jet flies along a Great Circle route spanning an angular distance of $\\theta = 42^\\circ$.\n"
                            "(a) Calculate the flight distance in nautical miles.\n"
                            "(b) Calculate the flight distance in kilometers (take $R = 6370\\text{ km}$, $\\pi = 22/7$).\n"
                            "(c) Given that the jet burns $3.2\\text{ kg}$ of aviation fuel per kilometer, calculate the total fuel needed in metric tonnes."
                        ),
                        "steps": [
                            "**What we need to calculate:** Distance in nm, distance in km, and total fuel in metric tonnes.",
                            "**Step 1 — Calculate distance in nautical miles:**\n"
                            "$$D_{\\text{nm}} = 60 \\times 42 = 2520\\text{ nm}$$",
                            "**Step 2 — Calculate distance in kilometers:**\n"
                            "$$D_{\\text{km}} = \\frac{42}{360} \\times 2 \\times \\frac{22}{7} \\times 6370 = \\frac{42}{360} \\times 40040 = 4671.33\\text{ km}$$",
                            "**Step 3 — Calculate total fuel burn:**\n"
                            "$$\\text{Fuel in kg} = 4671.33\\text{ km} \\times 3.2\\text{ kg/km} = 14948.27\\text{ kg}$$",
                            "**Step 4 — Convert to metric tonnes ($1\\text{ tonne} = 1000\\text{ kg}$):**\n"
                            "$$\\text{Total Fuel} = \\frac{14948.27}{1000} \\approx 14.95\\text{ tonnes}$$\n\n"
                            "**Answer:** (a) $2520\\text{ nm}$; (b) $4671.33\\text{ km}$; (c) $14.95\\text{ tonnes}$."
                        ]
                    }
                },

                # PAGE 8 — suggested_simulation
                {
                    "page_number": 8,
                    "page_title": "Explore: Great Circle Distance Navigator",
                    "block_type": "suggested_simulation",
                    "component_type": "suggested_simulation",
                    "content": {
                        "purpose": (
                            "An interactive 3D navigation simulator allowing students to drag start and end pins along any meridian or equator. "
                            "The app displays the live subtended central angle $\\theta$, step-by-step angle addition across the equator, "
                            "and instant side-by-side readouts of Distance in Nautical Miles and Kilometers."
                        )
                    },
                    "asset_info": {
                        "asset_type": "simulation",
                        "archetype": "math_great_circle_distance_navigator",
                        "title": "Interactive Great Circle Distance Navigator Sandbox"
                    }
                },

                # PAGE 9 — common_misconception
                {
                    "page_number": 9,
                    "page_title": "Common Error: Subtracting Across the Equator",
                    "block_type": "common_misconception",
                    "component_type": "common_misconception",
                    "content": {
                        "text": (
                            "### The Hemisphere Boundary Sign Error\n\n"
                            "When finding the angular distance between $A(10^\\circ\\text{S})$ and $B(35^\\circ\\text{N})$, students often subtract: $35^\\circ - 10^\\circ = 25^\\circ$.\n\n"
                            "### Why This Fails:\n"
                            "- To travel from $10^\\circ\\text{S}$ to $35^\\circ\\text{N}$, you must first cover **$10^\\circ$ to reach the Equator ($0^\\circ$)**.\n"
                            "- Then you must cover another **$35^\\circ$ from the Equator up to $35^\\circ\\text{N}$**.\n"
                            "- Total angular travel: $10^\\circ + 35^\\circ = 45^\\circ$.\n\n"
                            "> **Memory Rule:**\n"
                            "> - **Different Hemispheres (N and S) $\\implies$ ADD angles.**\n"
                            "> - **Same Hemisphere (N and N or S and S) $\\implies$ SUBTRACT angles.**"
                        )
                    }
                },

                # PAGE 10 — knowledge_check (MCQ)
                {
                    "page_number": 10,
                    "page_title": "Check Your Understanding: Great Circle Distances",
                    "block_type": "knowledge_check",
                    "component_type": "multiple_choice",
                    "content": {
                        "question": "What is the Great Circle distance in nautical miles between $P(24^\\circ\\text{S}, 15^\\circ\\text{E})$ and $Q(16^\\circ\\text{N}, 15^\\circ\\text{E})$?",
                        "options": [
                            "A: 480 nm",
                            "B: 960 nm",
                            "C: 2400 nm",
                            "D: 4440 nm"
                        ],
                        "answer": "C",
                        "explanation": (
                            "1. Since longitudes match ($15^\\circ\\text{E}$), points lie on a Great Circle meridian.\n"
                            "2. Opposite hemispheres $\\implies \\theta = 24^\\circ + 16^\\circ = 40^\\circ$.\n"
                            "3. Distance in nm: $D = 60 \\times \\theta = 60 \\times 40 = 2400\\text{ nm}$."
                        )
                    }
                },

                # PAGE 11 — summary
                {
                    "page_number": 11,
                    "page_title": "Key Takeaways: Great Circle Navigation",
                    "block_type": "summary",
                    "component_type": "summary",
                    "content": {
                        "text": (
                            "### Master Summary: Great Circle Distance Formulas\n\n"
                            "| Target Unit | Formula | Memory Key |\n"
                            "|:---|:---|:---|\n"
                            "| **Nautical Miles (nm)** | $D = 60 \\times \\theta$ | $1^\\circ = 60\\text{ nm}$ (instant multiplication). |\n"
                            "| **Kilometers (km)** | $D = \\frac{\\theta}{360^\\circ} \\times 2\\pi R$ | Standard arc length with $R = 6370\\text{ km}$. |\n"
                            "| **Over-the-Pole (nm)** | $D = 60 \\times [(90-\\alpha_1) + (90-\\alpha_2)]$ | Used when longitudes sum to $180^\\circ$. |\n\n"
                            "**Standard Values Checklist:**\n"
                            "- [x] Earth Radius: $R = 6370\\text{ km}$ (unless exam specifies $6371\\text{ km}$).\n"
                            "- [x] Equatorial Circumference: $2\\pi R \\approx 40040\\text{ km}$ (with $\\pi = 22/7$).\n"
                            "- [x] Metric Conversion: $1\\text{ nm} \\approx 1.853\\text{ km}$."
                        )
                    }
                }
            ]
        },

        # =====================================================================
        # MODULE 5.3: Small Circle Distances & Routing Optimization
        # =====================================================================
        {
            "unit_order": 3,
            "unit_title": "Module 5.3: Distance Along Parallels of Latitude and Route Comparison",
            "lesson_title": "Distance Calculation Along Parallels of Latitude and Route Comparison",
            "lesson_blocks": [
                # PAGE 1 — learning_goal
                {
                    "page_number": 1,
                    "page_title": "Mastering Small Circle Distances & Route Optimization",
                    "block_type": "learning_goal",
                    "component_type": "learning_goal",
                    "content": {
                        "title": "What You Will Master in This Lesson",
                        "goals": [
                            "Calculate longitude differences ($\\Delta \\lambda$) for points on the same parallel of latitude.",
                            "Calculate Small Circle distances in kilometers using $D_{\\text{SC}} = \\frac{\\theta}{360^\\circ} \\times 2\\pi R \\cos \\alpha$.",
                            "Calculate Small Circle distances in nautical miles using $D_{\\text{SC}} = 60 \\theta \\cos \\alpha$.",
                            "Compare Great Circle and Small Circle routing options to explain why aircraft fly polar routes."
                        ]
                    }
                },

                # PAGE 2 — concept_explanation
                {
                    "page_number": 2,
                    "page_title": "Why Moving Along a Latitude Circle Scales by cos α",
                    "block_type": "concept_explanation",
                    "component_type": "concept_explanation",
                    "content": {
                        "body": (
                            "When traveling due East or due West between two points having the same latitude $\\alpha$, "
                            "you are moving along a **parallel of latitude (a Small Circle)**.\n\n"
                            "### The Scaling Factor $\\cos \\alpha$\n\n"
                            "- On the Equator ($0^\\circ$), $1^\\circ$ of longitude covers a full $60\\text{ nm}$.\n"
                            "- But at latitude $\\alpha$, the circle is physically smaller by the scale factor $\\cos \\alpha$.\n"
                            "- Therefore, every $1^\\circ$ of longitude turn at latitude $\\alpha$ covers only:\n"
                            "$$60 \\times \\cos \\alpha\\text{ nautical miles}$$\n\n"
                            "### Why Aircraft Fly Curved Paths (The Great Circle Secret)\n\n"
                            "On a flat map, traveling along a parallel of latitude appears as a straight line. "
                            "However, on a 3D curved sphere, flying straight along a parallel is **NOT** the shortest route! "
                            "Arching upwards toward the pole along a Great Circle path cuts through a tighter arc, saving thousands of kilometers."
                        )
                    }
                },

                # PAGE 3 — formula_breakdown
                {
                    "page_number": 3,
                    "page_title": "Master Formulas for Small Circle Distances",
                    "block_type": "formula_breakdown",
                    "component_type": "formula_breakdown",
                    "content": {
                        "formula": "**Distance in Nautical Miles (nm):**\n$$D_{\\text{SC}} = 60 \\times \\theta \\times \\cos \\alpha \\quad \\text{(where } \\alpha = \\text{Latitude)}$$\n\n**Distance in Kilometers (km):**\n$$D_{\\text{SC}} = \\frac{\\theta}{360^\\circ} \\times 2\\pi R \\cos \\alpha \\quad (R = 6370\\text{ km})$$",
                        "content": (
                            "### Small Circle vs. Great Circle Comparison Chart\n\n"
                            "| Path Traveled | Circle Type | Distance in Nautical Miles (nm) | Distance in Kilometers (km) |\n"
                            "|:---|:---:|:---|:---|\n"
                            "| **Along Meridian (North-South)** | Great Circle | $D = 60 \\theta$ | $D = \\frac{\\theta}{360^\\circ} \\times 2\\pi R$ |\n"
                            "| **Along Equator (East-West at $0^\\circ$)** | Great Circle | $D = 60 \\theta$ | $D = \\frac{\\theta}{360^\\circ} \\times 2\\pi R$ |\n"
                            "| **Along Parallel (East-West at $\\alpha$)** | Small Circle | $D = 60 \\theta \\cos \\alpha$ | $D = \\frac{\\theta}{360^\\circ} \\times 2\\pi R \\cos \\alpha$ |\n\n"
                            "> **Key Procedural Step:** When finding longitude difference $\\theta$:\n"
                            "> - **Same Longitude Hemisphere (E and E or W and W) $\\implies$ SUBTRACT.**\n"
                            "> - **Opposite Longitude Hemispheres (E and W) $\\implies$ ADD.**"
                        )
                    }
                },

                # PAGE 4 — worked_example (Level 1: Easy / Small Circle Distance in Nautical Miles)
                {
                    "page_number": 4,
                    "page_title": "Example 1: Small Circle Distance in Nautical Miles",
                    "block_type": "worked_example",
                    "component_type": "worked_example",
                    "content": {
                        "problem": (
                            "Find the distance in nautical miles between town $X(40^\\circ\\text{N}, 20^\\circ\\text{E})$ and town $Y(40^\\circ\\text{N}, 50^\\circ\\text{E})$ along their parallel of latitude."
                        ),
                        "steps": [
                            "**What we need to find:** Small circle distance in nm.",
                            "**Step 1 — Calculate the longitude difference $\\theta$:**\n"
                            "Both towns lie in the Eastern Hemisphere on latitude $40^\\circ\\text{N}$:\n"
                            "$$\\theta = 50^\\circ - 20^\\circ = 30^\\circ$$",
                            "**Step 2 — Apply the Small Circle nautical miles formula:**\n"
                            "$$D = 60 \\times \\theta \\times \\cos \\alpha$$",
                            "**Step 3 — Substitute $\\theta = 30^\\circ$ and $\\alpha = 40^\\circ$:**\n"
                            "$$D = 60 \\times 30 \\times \\cos(40^\\circ) = 1800 \\times 0.76604 \\approx 1378.88\\text{ nm}$$\n\n"
                            "**Answer:** $1378.88\\text{ nm}$ (or $1379\\text{ nm}$ to the nearest mile)."
                        ]
                    }
                },

                # PAGE 5 — worked_example (Level 2: Moderate / Small Circle Distance in Kilometers)
                {
                    "page_number": 5,
                    "page_title": "Example 2: Small Circle Distance Across Prime Meridian in Kilometers",
                    "block_type": "worked_example",
                    "component_type": "worked_example",
                    "content": {
                        "problem": (
                            "Find the distance in kilometers between $X(45^\\circ\\text{N}, 20^\\circ\\text{W})$ and $Y(45^\\circ\\text{N}, 10^\\circ\\text{E})$ along latitude $45^\\circ\\text{N}$.\n"
                            "(Take $R = 6370\\text{ km}$ and $\\pi = 22/7$)."
                        ),
                        "steps": [
                            "**What we need to find:** Small circle distance in km.",
                            "**Step 1 — Calculate the longitude difference $\\theta$:**\n"
                            "Since $X$ is West and $Y$ is East, add across the Prime Meridian ($0^\\circ$):\n"
                            "$$\\theta = 20^\\circ + 10^\\circ = 30^\\circ$$",
                            "**Step 2 — Apply the Small Circle metric distance formula:**\n"
                            "$$D = \\frac{\\theta}{360^\\circ} \\times 2\\pi R \\cos \\alpha$$",
                            "**Step 3 — Substitute the constants:**\n"
                            "$$D = \\frac{30}{360} \\times 2 \\times \\frac{22}{7} \\times 6370 \\times \\cos(45^\\circ)$$\n"
                            "$$D = \\frac{1}{12} \\times 40040 \\times 0.70711 \\approx 2359.50\\text{ km}$$\n\n"
                            "**Answer:** $2359.50\\text{ km}$."
                        ]
                    }
                },

                # PAGE 6 — worked_example (Level 3: Difficult / Solving for Unknown Longitude)
                {
                    "page_number": 6,
                    "page_title": "Example 3: Determining Intermediate Coordinates from Flight Distance",
                    "block_type": "worked_example",
                    "component_type": "worked_example",
                    "content": {
                        "problem": (
                            "A plane leaves point $B(52^\\circ\\text{N}, 37.05^\\circ\\text{W})$ and flies due East along its parallel of latitude for $2400\\text{ km}$ to point $C$.\n"
                            "Determine the exact geographic coordinates of $C$, taking $\\pi = 22/7$ and $R = 6370\\text{ km}$."
                        ),
                        "steps": [
                            "**What we need to find:** Geographic coordinates of $C(52^\\circ\\text{N}, \\lambda^\\circ)$.",
                            "**Step 1 — State the Small Circle distance equation:**\n"
                            "$$D = \\frac{\\Delta \\lambda}{360^\\circ} \\times 2\\pi R \\cos(52^\\circ)$$",
                            "**Step 2 — Substitute known distance $2400\\text{ km}$ and constants:**\n"
                            "$$2400 = \\frac{\\Delta \\lambda}{360} \\times 40040 \\times \\cos(52^\\circ)$$\n"
                            "$$40040 \\times \\cos(52^\\circ) = 40040 \\times 0.61566 = 24651.05\\text{ km}$$",
                            "**Step 3 — Solve for longitude difference $\\Delta \\lambda$:**\n"
                            "$$\\Delta \\lambda = \\frac{2400 \\times 360}{24651.05} = \\frac{864000}{24651.05} \\approx 35.05^\\circ$$",
                            "**Step 4 — Calculate longitude of $C$:**\n"
                            "Point $B$ is at $37.05^\\circ\\text{W}$. Flying due East moves toward $0^\\circ$, decreasing West longitude:\n"
                            "$$\\text{Longitude of } C = 37.05^\\circ\\text{W} - 35.05^\\circ = 2.00^\\circ\\text{W}$$\n\n"
                            "**Answer:** $C = (52^\\circ\\text{N}, 2^\\circ\\text{W})$."
                        ]
                    }
                },

                # PAGE 7 — worked_example (Level 4: Exam-Style / Route Comparison Mastery)
                {
                    "page_number": 7,
                    "page_title": "Example 4: Comparing Great Circle vs. Small Circle Routing",
                    "block_type": "worked_example",
                    "component_type": "worked_example",
                    "content": {
                        "problem": (
                            "An airliner needs to travel between $M(30^\\circ\\text{N}, 36^\\circ\\text{E})$ and $N(30^\\circ\\text{N}, 144^\\circ\\text{W})$.\n"
                            "(a) Calculate the distance in nautical miles along Route 1 (over the North Pole).\n"
                            "(b) Calculate the distance in nautical miles along Route 2 (along latitude $30^\\circ\\text{N}$).\n"
                            "(c) Determine which route is shorter and calculate the distance saved."
                        ),
                        "steps": [
                            "**What we need to calculate:** Polar Great Circle distance, Small Circle distance, and difference.",
                            "**Step 1 — Route 1 (Over the North Pole):**\n"
                            "Longitudes sum to $36^\\circ + 144^\\circ = 180^\\circ$.\n"
                            "Total angular degrees: $\\theta = (90^\\circ - 30^\\circ) + (90^\\circ - 30^\\circ) = 120^\\circ$.\n"
                            "$$D_{\\text{Route 1}} = 60 \\times 120 = 7200\\text{ nm}$$",
                            "**Step 2 — Route 2 (Along the parallel of latitude $30^\\circ\\text{N}$):**\n"
                            "Longitude difference $\\theta = 36^\\circ + 144^\\circ = 180^\\circ$.\n"
                            "$$D_{\\text{Route 2}} = 60 \\times \\theta \\times \\cos(30^\\circ) = 60 \\times 180 \\times 0.86603 = 9353.12\\text{ nm}$$",
                            "**Step 3 — Compare the routes:**\n"
                            "$$\\text{Savings} = 9353.12 - 7200 = 2153.12\\text{ nm}$$\n\n"
                            "**Answer:** Route 1 (Over the Pole) is shorter by $2153\\text{ nm}$ (saving over $3980\\text{ km}$ of flight path)."
                        ]
                    }
                },

                # PAGE 8 — suggested_simulation
                {
                    "page_number": 8,
                    "page_title": "Explore: Great vs. Small Circle Route Comparator",
                    "block_type": "suggested_simulation",
                    "component_type": "suggested_simulation",
                    "content": {
                        "purpose": (
                            "An interactive 3D globe allowing students to select any two cities on the same latitude and toggle between "
                            "the 'Flat Parallel Route' and the 'Great Circle Polar Route'. "
                            "The simulation visualizes the shorter geodesic curve and shows live fuel/distance comparison gauges."
                        )
                    },
                    "asset_info": {
                        "asset_type": "simulation",
                        "archetype": "math_small_vs_great_circle_route_comparator",
                        "title": "Interactive Great vs Small Circle Route Comparator Sandbox"
                    }
                },

                # PAGE 9 — common_misconception
                {
                    "page_number": 9,
                    "page_title": "Common Error: Forgetting the cos α Multiplier",
                    "block_type": "common_misconception",
                    "component_type": "common_misconception",
                    "content": {
                        "text": (
                            "### The Missing Latitude Factor\n\n"
                            "Students frequently calculate distance along a parallel using $D = 60 \\theta$ instead of $D = 60 \\theta \\cos \\alpha$.\n\n"
                            "### Why $\\cos \\alpha$ is Essential:\n"
                            "- $D = 60 \\theta$ is valid **only on the Equator** or along a meridian Great Circle.\n"
                            "- At $60^\\circ\\text{N}$, $\\cos(60^\\circ) = 0.5$. If you forget $\\cos \\alpha$, your answer will be **exactly double** the true distance!\n\n"
                            "> **Memory Rule:**\n"
                            "> - Walking North/South $\\implies$ No cosine needed ($D = 60\\theta$).\n"
                            "> - Walking East/West (off Equator) $\\implies$ **MUST include $\\cos \\alpha$** ($D = 60\\theta \\cos \\alpha$)."
                        )
                    }
                },

                # PAGE 10 — knowledge_check (MCQ)
                {
                    "page_number": 10,
                    "page_title": "Check Your Understanding: Small Circle Distance",
                    "block_type": "knowledge_check",
                    "component_type": "multiple_choice",
                    "content": {
                        "question": "What is the distance in nautical miles between $A(60^\\circ\\text{S}, 10^\\circ\\text{W})$ and $B(60^\\circ\\text{S}, 50^\\circ\\text{E})$ along latitude $60^\\circ\\text{S}$?",
                        "options": [
                            "A: 3600 nm",
                            "B: 1800 nm",
                            "C: 3118 nm",
                            "D: 2400 nm"
                        ],
                        "answer": "B",
                        "explanation": (
                            "1. Longitude difference $\\theta = 10^\\circ + 50^\\circ = 60^\\circ$.\n"
                            "2. $D = 60 \\times \\theta \\times \\cos(60^\\circ) = 60 \\times 60 \\times 0.5 = 1800\\text{ nm}$."
                        )
                    }
                },

                # PAGE 11 — summary
                {
                    "page_number": 11,
                    "page_title": "Key Takeaways: Small Circle Calculations",
                    "block_type": "summary",
                    "component_type": "summary",
                    "content": {
                        "text": (
                            "### Master Summary: Parallel of Latitude Navigation\n\n"
                            "| Formula | Value in nm | Value in km |\n"
                            "|:---|:---|:---|\n"
                            "| **Small Circle Distance** | $D = 60 \\theta \\cos \\alpha$ | $D = \\frac{\\theta}{360^\\circ} \\times 2\\pi R \\cos \\alpha$ |\n"
                            "| **At Equator ($\\alpha=0^\\circ$)** | $D = 60 \\theta$ | $D = \\frac{\\theta}{360^\\circ} \\times 2\\pi R$ |\n"
                            "| **At Latitude $60^\\circ$** | $D = 30 \\theta$ (half size) | $D = \\frac{\\theta}{360^\\circ} \\times \\pi R$ |\n\n"
                            "**Routing Strategy Checklist:**\n"
                            "- [x] Great Circle route is always the shortest path on a sphere.\n"
                            "- [x] Over-the-Pole path beats parallel route when longitude sum $= 180^\\circ$."
                        )
                    }
                }
            ]
        },

        # =====================================================================
        # MODULE 5.4: Longitude-Time Relationships & Speed in Knots
        # =====================================================================
        {
            "unit_order": 4,
            "unit_title": "Module 5.4: Earth Rotation, Longitude-Time Relationships, and Speed in Knots",
            "lesson_title": "Longitude-Time Calculations and Speed in Knots",
            "lesson_blocks": [
                # PAGE 1 — learning_goal
                {
                    "page_number": 1,
                    "page_title": "Mastering Longitude-Time Calculations & Knots",
                    "block_type": "learning_goal",
                    "component_type": "learning_goal",
                    "content": {
                        "title": "What You Will Master in This Lesson",
                        "goals": [
                            "Convert longitude differences into time differences using $15^\\circ = 1\\text{ hour}$ and $1^\\circ = 4\\text{ minutes}$.",
                            "Calculate local clock times in Eastern (ahead) and Western (behind) time zones.",
                            "Calculate speed in knots ($1\\text{ knot} = 1\\text{ nautical mile per hour}$) and convert to km/h.",
                            "Reconstruct unknown latitudes from time differences and physical flight distances."
                        ]
                    }
                },

                # PAGE 2 — concept_explanation
                {
                    "page_number": 2,
                    "page_title": "The Spinning Earth: Why 15° of Longitude Equals 1 Hour",
                    "block_type": "concept_explanation",
                    "component_type": "concept_explanation",
                    "content": {
                        "body": (
                            "The Earth is a giant spinning clock that rotates $360^\\circ$ on its axis once every $24\\text{ hours}$.\n\n"
                            "### The 15° per Hour Golden Rule\n\n"
                            "Dividing full rotation by the hours in a day:\n"
                            "$$\\text{Rotation Rate} = \\frac{360^\\circ}{24\\text{ hours}} = 15^\\circ\\text{ per hour}$$\n"
                            "$$\\text{For } 1^\\circ\\text{ of rotation} = \\frac{60\\text{ minutes}}{15} = 4\\text{ minutes of time}$$\n\n"
                            "### The Sun-Rise Direction Rule (East is Ahead)\n\n"
                            "Because the Earth rotates from **West to East**:\n"
                            "- Towns located to the **East** rotate into the sunlight first, so their local clocks are **AHEAD (ADD time)**.\n"
                            "- Towns located to the **West** see the sunrise later, so their local clocks are **BEHIND (SUBTRACT time)**.\n\n"
                            "### Speed in Knots\n\n"
                            "In navigation, speed is measured in **knots**:\n"
                            "$$1\\text{ knot} = 1\\text{ nautical mile per hour (nm/h)}$$"
                        )
                    }
                },

                # PAGE 3 — formula_breakdown
                {
                    "page_number": 3,
                    "page_title": "Master Formulas for Time, Speed, and Knots",
                    "block_type": "formula_breakdown",
                    "component_type": "formula_breakdown",
                    "content": {
                        "formula": "**Longitude to Time Conversion:**\n$$\\Delta t = \\frac{\\text{Longitude Difference in Degrees } (\\Delta \\lambda)}{15^\\circ/\\text{hour}} \\quad \\text{(or } 1^\\circ = 4\\text{ minutes)}$$\n\n**Speed in Knots:**\n$$\\text{Speed (knots)} = \\frac{\\text{Distance in Nautical Miles (nm)}}{\\text{Time in Hours (h)}} \\quad (1\\text{ knot} = 1\\text{ nm/h} \\approx 1.852\\text{ km/h})$$",
                        "content": (
                            "### Longitude & Kinematic Conversion Table\n\n"
                            "| Conversion Rule | Formula | Key Application |\n"
                            "|:---|:---|:---|\n"
                            "| **Degrees to Hours** | $\\text{Hours} = \\frac{\\Delta \\lambda}{15}$ | Converting longitude difference to whole/fractional hours. |\n"
                            "| **Degrees to Minutes** | $\\text{Minutes} = \\Delta \\lambda \\times 4$ | Precise minute offsets for small longitude differences. |\n"
                            "| **Local Time East** | $\\text{Time}_{\\text{East}} = \\text{Time}_{\\text{West}} + \\Delta t$ | East of Prime Meridian or reference town (add time). |\n"
                            "| **Local Time West** | $\\text{Time}_{\\text{West}} = \\text{Time}_{\\text{East}} - \\Delta t$ | West of Prime Meridian or reference town (subtract time). |\n"
                            "| **Kinematic Speed** | $\\text{Speed (knots)} = \\frac{D_{\\text{nm}}}{t_{\\text{hours}}}$ | Calculating flight or ship speed directly in nautical units. |\n\n"
                            "> **Unit Consistency Rule:** Never divide kilometers by knots! Always pair **nm with knots** and **km with km/h**."
                        )
                    }
                },

                # PAGE 4 — worked_example (Level 1: Easy / Finding Local Time from Longitude)
                {
                    "page_number": 4,
                    "page_title": "Example 1: Calculating Local Time Across Longitudes",
                    "block_type": "worked_example",
                    "component_type": "worked_example",
                    "content": {
                        "problem": (
                            "When the local time at town $A(0^\\circ, 15^\\circ\\text{E})$ is $9:00\\text{ am}$, determine the local time at town $B(0^\\circ, 60^\\circ\\text{E})$."
                        ),
                        "steps": [
                            "**What we need to find:** Local clock time at town $B$.",
                            "**Step 1 — Calculate the longitude difference $\\Delta \\lambda$:**\n"
                            "Both towns lie in the Eastern Hemisphere:\n"
                            "$$\\Delta \\lambda = 60^\\circ - 15^\\circ = 45^\\circ$$",
                            "**Step 2 — Convert longitude difference into hours:**\n"
                            "$$\\Delta t = \\frac{45^\\circ}{15^\\circ/\\text{hour}} = 3\\text{ hours}$$",
                            "**Step 3 — Determine whether to add or subtract:**\n"
                            "Town $B$ ($60^\\circ\\text{E}$) is to the **East** of town $A$ ($15^\\circ\\text{E}$), so $B$ is **ahead** in time.",
                            "**Step 4 — Compute local time at $B$:**\n"
                            "$$\\text{Time at } B = 9:00\\text{ am} + 3\\text{ hours} = 12:00\\text{ noon}$$\n\n"
                            "**Answer:** $12:00\\text{ noon}$."
                        ]
                    }
                },

                # PAGE 5 — worked_example (Level 2: Moderate / Ship Travel Duration in Knots)
                {
                    "page_number": 5,
                    "page_title": "Example 2: Travel Time and Distance at Sea in Knots",
                    "block_type": "worked_example",
                    "component_type": "worked_example",
                    "content": {
                        "problem": (
                            "A ship sails from island $X(4^\\circ\\text{S}, 39^\\circ\\text{E})$ due South at a constant speed of $20\\text{ knots}$ to port $Y(9^\\circ\\text{S}, 39^\\circ\\text{E})$.\n"
                            "Calculate:\n"
                            "(a) The distance covered in nautical miles.\n"
                            "(b) The time taken in hours."
                        ),
                        "steps": [
                            "**What we need to calculate:** Nautical distance and travel time.",
                            "**Step 1 — Calculate angular latitude difference along the meridian:**\n"
                            "Both ports are in the Southern Hemisphere on longitude $39^\\circ\\text{E}$:\n"
                            "$$\\theta = 9^\\circ - 4^\\circ = 5^\\circ$$",
                            "**Step 2 — Calculate distance in nautical miles ($D = 60\\theta$):**\n"
                            "$$D = 60 \\times 5 = 300\\text{ nm}$$",
                            "**Step 3 — Calculate travel time using speed $s = 20\\text{ knots}$:**\n"
                            "$$\\text{Time} = \\frac{\\text{Distance in nm}}{\\text{Speed in knots}} = \\frac{300\\text{ nm}}{20\\text{ nm/h}} = 15\\text{ hours}$$\n\n"
                            "**Answer:** (a) $300\\text{ nm}$; (b) $15\\text{ hours}$."
                        ]
                    }
                },

                # PAGE 6 — worked_example (Level 3: Difficult / Reconstructing Unknown Latitude)
                {
                    "page_number": 6,
                    "page_title": "Example 3: Reconstructing Unknown Latitude from Time and Distance",
                    "block_type": "worked_example",
                    "component_type": "worked_example",
                    "content": {
                        "problem": (
                            "Two towns $A(15^\\circ\\text{E})$ and $B$ lie on the same parallel of latitude in the Northern Hemisphere.\n"
                            "When the local time at $A$ is $8:00\\text{ am}$, the local time at $B$ is $11:00\\text{ am}$.\n"
                            "(a) Find the longitude of $B$.\n"
                            "(b) Given that the distance between $A$ and $B$ along their parallel of latitude is $2500\\text{ km}$, find to the nearest degree the latitude on which they lie.\n"
                            "(Take $R = 6370\\text{ km}$ and $\\pi = 22/7$)."
                        ),
                        "steps": [
                            "**What we need to find:** Longitude of $B$ and latitude $\\alpha^\\circ\\text{N}$.",
                            "**Step 1 — Calculate time difference:**\n"
                            "$$\\Delta t = 11:00\\text{ am} - 8:00\\text{ am} = 3\\text{ hours}$$",
                            "**Step 2 — Convert time difference to longitude difference:**\n"
                            "$$\\Delta \\lambda = 3\\text{ hours} \\times 15^\\circ/\\text{hour} = 45^\\circ$$\n"
                            "Since $B$ is ahead ($11:00\\text{ am}$), $B$ is East of $A$:\n"
                            "$$\\text{Longitude of } B = 15^\\circ\\text{E} + 45^\\circ = 60^\\circ\\text{E}$$",
                            "**Step 3 — Set up Small Circle distance equation for $2500\\text{ km}$:**\n"
                            "$$D = \\frac{\\Delta \\lambda}{360^\\circ} \\times 2\\pi R \\cos \\alpha$$\n"
                            "$$2500 = \\frac{45}{360} \\times 40040 \\times \\cos \\alpha$$\n"
                            "$$2500 = \\frac{1}{8} \\times 40040 \\times \\cos \\alpha = 5005 \\cos \\alpha$$",
                            "**Step 4 — Solve for $\\cos \\alpha$ and latitude angle $\\alpha$:**\n"
                            "$$\\cos \\alpha = \\frac{2500}{5005} \\approx 0.4995$$\n"
                            "$$\\alpha = \\arccos(0.4995) \\approx 60.03^\\circ \\approx 60^\\circ\\text{N}$$\n\n"
                            "**Answer:** (a) Longitude of $B$ is $60^\\circ\\text{E}$; (b) Latitude is $60^\\circ\\text{N}$."
                        ]
                    }
                },

                # PAGE 7 — worked_example (Level 4: Exam-Style / Flight Itinerary Across Time Zones)
                {
                    "page_number": 7,
                    "page_title": "Example 4: Complete Flight Schedule with Time Zone Offsets",
                    "block_type": "worked_example",
                    "component_type": "worked_example",
                    "content": {
                        "problem": (
                            "An aircraft departs Nairobi $(1.3^\\circ\\text{S}, 36.8^\\circ\\text{E})$ on Monday at $10:30\\text{ am}$ local time.\n"
                            "It flies due West along latitude $1.3^\\circ\\text{S}$ at a constant speed of $450\\text{ knots}$ to an airport in West Africa at $(1.3^\\circ\\text{S}, 15.2^\\circ\\text{W})$.\n"
                            "Calculate:\n"
                            "(a) The flight distance in nautical miles (take $\\cos 1.3^\\circ \\approx 0.9997$).\n"
                            "(b) The flight duration in hours and minutes.\n"
                            "(c) The local time and day of arrival at the destination airport."
                        ),
                        "steps": [
                            "**What we need to calculate:** Distance in nm, duration, and local arrival time.",
                            "**Step 1 — Calculate longitude difference $\\Delta \\lambda$:**\n"
                            "Adding across the Prime Meridian ($0^\\circ$):\n"
                            "$$\\Delta \\lambda = 36.8^\\circ\\text{E} + 15.2^\\circ\\text{W} = 52.0^\\circ$$",
                            "**Step 2 — Calculate flight distance in nautical miles:**\n"
                            "$$D = 60 \\times \\Delta \\lambda \\times \\cos(1.3^\\circ) = 60 \\times 52 \\times 0.9997 = 3120 \\times 0.9997 \\approx 3119\\text{ nm}$$",
                            "**Step 3 — Calculate flight duration:**\n"
                            "$$\\text{Duration} = \\frac{3119\\text{ nm}}{450\\text{ knots}} \\approx 6.931\\text{ hours}$$\n"
                            "$$0.931 \\times 60 \\approx 56\\text{ minutes} \\implies \\text{Duration} = 6\\text{ hours } 56\\text{ minutes}$$",
                            "**Step 4 — Calculate local time difference between Nairobi and West Africa:**\n"
                            "$$\\text{Time offset} = \\frac{52^\\circ}{15^\\circ/\\text{hour}} = 3.467\\text{ hours} = 3\\text{ hours } 28\\text{ minutes}$$\n"
                            "Since West Africa is **West** of Nairobi, its clock is **3 hours 28 minutes behind** Nairobi.",
                            "**Step 5 — Determine arrival local time:**\n"
                            "- Departure in Nairobi time: $10:30\\text{ am}$\n"
                            "- Arrival in Nairobi time: $10:30\\text{ am} + 6\\text{h } 56\\text{m} = 17:26\\text{ (5:26 pm)}$\n"
                            "- Adjust to destination local time (subtract 3h 28m):\n"
                            "$$\\text{Destination Local Time} = 17:26 - 3:28 = 13:58\\text{ (1:58 pm)}$$\n\n"
                            "**Answer:** (a) $3119\\text{ nm}$; (b) $6\\text{ hours } 56\\text{ minutes}$; (c) $1:58\\text{ pm}$ on Monday."
                        ]
                    }
                },

                # PAGE 8 — suggested_simulation
                {
                    "page_number": 8,
                    "page_title": "Explore: Earth Time Zone & Speed Simulator",
                    "block_type": "suggested_simulation",
                    "component_type": "suggested_simulation",
                    "content": {
                        "purpose": (
                            "An interactive Earth rotation simulator featuring a live day/night terminator line, movable city clock pins, "
                            "and an aircraft speed controller in knots. "
                            "Students can simulate trans-continental flights and watch local clocks tick forward or backward in real-time."
                        )
                    },
                    "asset_info": {
                        "asset_type": "simulation",
                        "archetype": "math_earth_time_zone_speed_simulator",
                        "title": "Interactive Earth Time Zone & Speed Sandbox"
                    }
                },

                # PAGE 9 — common_misconception
                {
                    "page_number": 9,
                    "page_title": "Common Error: Speed Unit Mismatch (km vs. Knots)",
                    "block_type": "common_misconception",
                    "component_type": "common_misconception",
                    "content": {
                        "text": (
                            "### The Dangerous Unit Mixing Error\n\n"
                            "Students often calculate a distance of $1500\\text{ kilometers}$ and then divide by $200\\text{ knots}$ to find time:\n"
                            "$$\\text{Time} = \\frac{1500\\text{ km}}{200\\text{ knots}} = 7.5\\text{ hours} \\quad \\text{❌ (Completely Wrong!)}$$\n\n"
                            "### The Unit Pairing Rule:\n\n"
                            "| Distance Unit | Speed Unit | Time Result |\n"
                            "|:---|:---|:---|\n"
                            "| **Nautical Miles (nm)** | **Knots (nm/h)** | **Hours (Correct!)** |\n"
                            "| **Kilometers (km)** | **Kilometers per hour (km/h)** | **Hours (Correct!)** |\n\n"
                            "> **Memory Tip:** A knot is **already** nautical miles per hour ($1\\text{ knot} = 1\\text{ nm/h}$). "
                            "Never pair knots with kilometers unless you convert units first ($1\\text{ knot} \\approx 1.852\\text{ km/h}$)."
                        )
                    }
                },

                # PAGE 10 — knowledge_check (MCQ)
                {
                    "page_number": 10,
                    "page_title": "Check Your Understanding: Longitude and Time",
                    "block_type": "knowledge_check",
                    "component_type": "multiple_choice",
                    "content": {
                        "question": "When the local time at town $P(0^\\circ, 45^\\circ\\text{W})$ is $14:00\\text{ (2:00 pm)}$, what is the local time at town $Q(0^\\circ, 30^\\circ\\text{E})$?",
                        "options": [
                            "A: 09:00 (9:00 am)",
                            "B: 15:00 (3:00 pm)",
                            "C: 19:00 (7:00 pm)",
                            "D: 21:00 (9:00 pm)"
                        ],
                        "answer": "C",
                        "explanation": (
                            "1. Longitude difference $\\Delta \\lambda = 45^\\circ + 30^\\circ = 75^\\circ$.\n"
                            "2. Time difference $\\Delta t = \\frac{75^\\circ}{15^\\circ/\\text{h}} = 5\\text{ hours}$.\n"
                            "3. Since $Q$ is East of $P$, $Q$ is ahead: $14:00 + 5\\text{ hours} = 19:00\\text{ (7:00 pm)}$."
                        )
                    }
                },

                # PAGE 11 — summary
                {
                    "page_number": 11,
                    "page_title": "Key Takeaways: Longitude-Time & Spherical Kinematics",
                    "block_type": "summary",
                    "component_type": "summary",
                    "content": {
                        "text": (
                            "### Master Summary: Longitude, Time, and Speed\n\n"
                            "| Concept | Formula / Rule | Practical Tip |\n"
                            "|:---|:---|:---|\n"
                            "| **Earth Rotation** | $15^\\circ = 1\\text{ hour}, \\quad 1^\\circ = 4\\text{ minutes}$ | $\\Delta t = \\frac{\\Delta \\lambda}{15}$ |\n"
                            "| **Clock Adjustment** | East $\\implies$ Add time; West $\\implies$ Subtract time | The sun rises in the East first. |\n"
                            "| **Speed in Knots** | $\\text{Knots} = \\frac{\\text{Distance in nm}}{\\text{Time in hours}}$ | $1\\text{ knot} = 1\\text{ nm/h}$ |\n"
                            "| **Speed Conversion** | $1\\text{ knot} \\approx 1.852\\text{ km/h}$ | $1\\text{ nm} \\approx 1.853\\text{ km}$ |\n\n"
                            "**Exam Checklist:**\n"
                            "- [x] Always pair Nautical Miles with Knots.\n"
                            "- [x] Add longitudes across Prime Meridian ($0^\\circ$); add latitudes across Equator ($0^\\circ$).\n"
                            "- [x] Keep track of day rollovers when crossing midnight in time zone arithmetic."
                        )
                    }
                }
            ]
        }
    ]


def ingest_topic5_longitudes():
    """Main ingestion runner for Topic 5: Longitudes and Latitudes."""
    print("=" * 80)
    print("VLearn Form 4 Mathematics — Topic 5: Longitudes and Latitudes")
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

    # 2. Get or create Topic 5
    topic_name = "Topic 5: Longitudes and Latitudes"
    topic, topic_created = Topic.objects.get_or_create(
        subject=subject,
        order=5,
        defaults={"name": topic_name}
    )
    if not topic_created and topic.name != topic_name:
        topic.name = topic_name
        topic.save()
    print(f"Found Topic: {topic.name} (ID: {topic.id})")

    modules_data = get_topic5_data()
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
    ingest_topic5_longitudes()
