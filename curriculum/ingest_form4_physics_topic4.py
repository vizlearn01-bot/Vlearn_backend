"""
VLearn Form 4 Physics — Topic 4: Electromagnetic Spectrum
Ingestion Script

Source: Lessons.md (Topic 4)
Grade: Form 4
Subject: Physics
Curriculum: 844 (Kenyan 8-4-4 Secondary Curriculum)

Pedagogical Architecture:
  3 Learning Units / Modules:
  - Module 4.1: Nature of EM Waves, Wave Equation, and Propagation (13 pages)
  - Module 4.2: Experimental Speed of Light and Spectral Band Analysis (14 pages)
  - Module 4.3: Technological Applications, Radiation Hazards, and Shielding (13 pages)

Features:
  - Adaptive 8-step analytical problem-solving framework
  - Multi-tier worked examples (Levels 1 to 5)
  - Microwave oven standing wave speed of light experimental protocol
  - Full 7-band comprehensive spectral mapping (Radio to Gamma rays)
  - Purposeful interactions (prediction, simulation sandbox, reflections, knowledge checks)
  - Clean student-facing titles and zero developer terminology leaks
  - Idempotent safe updates (preserves enriched assets on rerun)

Usage:
  /home/jason-bitega/Desktop/VL/vlearn_repositories/Vlearn_backend/venv/bin/python curriculum/ingest_form4_physics_topic4.py
  Optional flag: --replace
"""

import os
import sys
import uuid
import re
import argparse
import django

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "Nexus_backend.settings")
django.setup()

from django.db import transaction
from curriculum.models import (
    Curriculum, Grade, Subject, Topic,
    LearningUnit, Lesson, LessonBlock, LessonAsset
)

def clean_text(raw_str):
    """Remove source citation brackets like [80], [201], [image_0] and clean whitespace."""
    if not isinstance(raw_str, str):
        return raw_str
    cleaned = re.sub(r'\[(?:\d+|image_\d+|[\d,\s]+)\]', '', raw_str)
    cleaned = re.sub(r'[ \t]+', ' ', cleaned)
    return cleaned.strip()

def clean_content_dict(data):
    """Recursively clean text within content dicts or lists."""
    if isinstance(data, str):
        return clean_text(data)
    elif isinstance(data, list):
        return [clean_content_dict(item) for item in data]
    elif isinstance(data, dict):
        return {k: clean_content_dict(v) for k, v in data.items()}
    return data


# =============================================================================
# MODULE 4.1 DATA — Nature of EM Waves, Wave Equation & Propagation
# =============================================================================
MODULE_4_1 = {
    "unit_name": "Module 4.1: Nature of EM Waves, Wave Equation, and Propagation",
    "unit_order": 1,
    "lesson_title": "Nature of EM Waves, Wave Equation, and Propagation",
    "cards": [
        # Page 1: Hook & Goals
        {
            "page_number": 1,
            "page_title": "From Ripples on Water to Waves in a Vacuum",
            "block_type": "learning_goal",
            "component_type": "learning_goal",
            "content": {
                "text": (
                    "When you drop a stone into a puddle, circular ripples spread outward across the water surface. "
                    "These are mechanical waves that require water molecules to oscillate.\n\n"
                    "Now think about sitting near an open campfire: you immediately feel heat on your face, even though hot air currents rise upward. "
                    "What travels across the air to warm your skin? It is **infrared radiation**—an invisible wave traveling at the speed of light!\n\n"
                    "Unlike mechanical waves, **electromagnetic waves require no material medium and travel freely through a vacuum**. "
                    "This is why sunlight travels across 150 million kilometers of empty space to reach Earth.\n\n"
                    "By the end of this lesson, you will be able to:\n"
                    "- Describe the 3D structure of electromagnetic waves with perpendicular electric and magnetic fields\n"
                    "- State the common physical properties shared by all electromagnetic waves\n"
                    "- Master the wave equation ($c = f\\lambda$) and metric conversions ($\\text{kHz}, \\text{MHz}, \\text{GHz}, \\text{nm}$)\n"
                    "- Calculate wavelengths and frequencies of radio broadcasts and cellular transmissions"
                )
            }
        },
        # Page 2: 3D Vector Geometry
        {
            "page_number": 2,
            "page_title": "The 3D Geometry of Propagating Electromagnetic Waves",
            "block_type": "concept_explanation",
            "component_type": "concept_explanation",
            "content": {
                "text": (
                    "### How Do Electromagnetic Waves Travel?\n"
                    "An electromagnetic wave is a transverse wave consisting of mutually perpendicular, oscillating **electric** ($\\vec{E}$) "
                    "and **magnetic** ($\\vec{B}$) fields:\n\n"
                    "1. **Electric Field ($\\vec{E}$)**: Oscillates in a vertical plane (along the $y$-axis).\n"
                    "2. **Magnetic Field ($\\vec{B}$)**: Oscillates in a horizontal plane (along the $z$-axis), at exactly $90^\\circ$ to the electric field.\n"
                    "3. **Direction of Travel (Propagation)**: Perpendicular to both fields, moving forward along the $x$-axis at the speed of light ($c$).\n\n"
                    "### The Self-Sustaining Cycle:\n"
                    "A vibrating electrical charge produces a changing electric field. This changing electric field induces a changing magnetic field, "
                    "which in turn induces an electric field. This continuous, self-sustaining loop radiates outward through space as an electromagnetic wave."
                )
            }
        },
        {
            "page_number": 2,
            "page_title": "3D Perpendicular Electric and Magnetic Fields",
            "block_type": "suggested_diagram",
            "component_type": "suggested_diagram",
            "content": {
                "text": "3D vector diagram of an electromagnetic wave showing sinusoidal electric field E oscillating vertically on y-axis in red and sinusoidal magnetic field B oscillating horizontally on z-axis in blue, propagating forward along x-axis at speed c.",
                "instruction": (
                    "Draw 3D coordinate axes (x, y, z). Draw vertical red sinusoidal wave for Electric Field E(y). "
                    "Draw horizontal blue sinusoidal wave for Magnetic Field B(z) at 90 degrees. "
                    "Draw green arrow along x-axis showing wave propagation direction at speed c = 3.0 x 10^8 m/s. "
                    "Label wavelength lambda between consecutive peaks."
                )
            }
        },
        # Page 3: Shared Properties
        {
            "page_number": 3,
            "page_title": "Fundamental Properties of All Electromagnetic Waves",
            "block_type": "comparison_table",
            "component_type": "comparison_table",
            "content": {
                "headers": ["Property", "Physical Description", "Governing Principle / Value"],
                "rows": [
                    ["Medium-free Propagation", "Can travel through a complete vacuum without physical matter", "Permits sunlight and star radiation to reach Earth across space"],
                    ["Universal Speed in Vacuum", "All EM waves travel at the exact same speed in vacuum or air", "$$c = 3.0 \\times 10^8\\text{ m/s}$$ ($300,000\\text{ km/s}$)"],
                    ["Transverse Nature", "Field oscillations are perpendicular to the direction of wave travel", "Can be polarized (unlike longitudinal sound waves)"],
                    ["Charge Neutrality", "Carry zero net electrical charge", "Not deflected by external electric or magnetic fields"],
                    ["Wave Behaviors", "Obey fundamental wave optics laws", "Undergo reflection, refraction, and diffraction"],
                    ["Energy Transport", "Transfer energy from source to receiver", "Carried by photon packets of energy $$E = hf$$"]
                ]
            }
        },
        # Page 4: Wave Equation & Prefixes
        {
            "page_number": 4,
            "page_title": "The Wave Equation and SI Metric Prefixes",
            "block_type": "formula_breakdown",
            "component_type": "formula_breakdown",
            "content": {
                "formula": "$$\\mathbf{c = f\\lambda} \\qquad \\implies \\qquad f = \\frac{c}{\\lambda} \\qquad \\text{and} \\qquad \\lambda = \\frac{c}{f}$$",
                "content": (
                    "Where:\n"
                    "- $c$: Speed of light in vacuum or air ($3.0 \\times 10^8\\text{ m/s}$)\n"
                    "- $f$: Frequency in Hertz ($\\text{Hz}$)\n"
                    "- $\\lambda$: Wavelength in meters ($\\text{m}$)\n\n"
                    "### Mandatory Metric Conversions:\n"
                    "- **Kilohertz ($\\text{kHz}$)**: $1\\text{ kHz} = 10^3\\text{ Hz}$\n"
                    "- **Megahertz ($\\text{MHz}$)**: $1\\text{ MHz} = 10^6\\text{ Hz}$ (e.g., $96.0\\text{ MHz} = 9.6 \\times 10^7\\text{ Hz}$)\n"
                    "- **Gigahertz ($\\text{GHz}$)**: $1\\text{ GHz} = 10^9\\text{ Hz}$ (e.g., $2.4\\text{ GHz} = 2.4 \\times 10^9\\text{ Hz}$)\n"
                    "- **Centimeter ($\\text{cm}$)**: $1\\text{ cm} = 10^{-2}\\text{ m}$\n"
                    "- **Millimeter ($\\text{mm}$)**: $1\\text{ mm} = 10^{-3}\\text{ m}$\n"
                    "- **Micrometer ($\\mu\\text{m}$)**: $1\\mu\\text{m} = 10^{-6}\\text{ m}$\n"
                    "- **Nanometer ($\\text{nm}$)**: $1\\text{ nm} = 10^{-9}\\text{ m}$ (e.g., $600\\text{ nm} = 6.0 \\times 10^{-7}\\text{ m}$)"
                )
            }
        },
        # Page 5: Worked Example Level 1
        {
            "page_number": 5,
            "page_title": "Example 1: Shortwave Radio Transmission",
            "block_type": "worked_example",
            "component_type": "worked_example",
            "content": {
                "problem": (
                    "A shortwave radio station broadcasts its carrier signal at a frequency of $6.0\\text{ MHz}$. "
                    "Calculate the wavelength of these radio waves. (Take $c = 3.0 \\times 10^8\\text{ m/s}$)."
                ),
                "steps": [
                    "**Given & Required:** Frequency $f = 6.0\\text{ MHz} = 6.0 \\times 10^6\\text{ Hz}$, Wave speed $c = 3.0 \\times 10^8\\text{ m/s}$. Required: Wavelength $\\lambda$.",
                    "**Governing Equation:** $$c = f\\lambda \\implies \\lambda = \\frac{c}{f}$$",
                    "**Substitution & Calculation:** $$\\lambda = \\frac{3.0 \\times 10^8\\text{ m/s}}{6.0 \\times 10^6\\text{ Hz}} = 0.5 \\times 10^2 = \\mathbf{50.0\\text{ m}}$$",
                    "**Attach Unit:** $\\lambda = 50.0\\text{ m}$",
                    "**Physical Reasonableness Check:** Shortwave radio waves typically have wavelengths between $10\\text{ m}$ and $100\\text{ m}$. An answer of $50\\text{ m}$ is physically sound."
                ]
            }
        },
        # Page 6: Worked Example Level 2
        {
            "page_number": 6,
            "page_title": "Example 2: Cellular Mobile Signal Frequency",
            "block_type": "worked_example",
            "component_type": "worked_example",
            "content": {
                "problem": (
                    "A cellular mobile phone network in Kenya transmits signals with a wavelength of $30.0\\text{ cm}$. "
                    "Determine the frequency of these electromagnetic waves."
                ),
                "steps": [
                    "**Given & Conversion:** Wavelength $\\lambda = 30.0\\text{ cm} = 30.0 \\times 10^{-2}\\text{ m} = 0.30\\text{ m}$, Wave speed $c = 3.0 \\times 10^8\\text{ m/s}$. Required: Frequency $f$.",
                    "**Governing Equation:** $$c = f\\lambda \\implies f = \\frac{c}{\\lambda}$$",
                    "**Substitution & Calculation:** $$f = \\frac{3.0 \\times 10^8\\text{ m/s}}{0.30\\text{ m}} = 1.0 \\times 10^9\\text{ Hz}$$",
                    "**Attach Unit:** $f = 1.0 \\times 10^9\\text{ Hz} = \\mathbf{1.0\\text{ GHz}}$",
                    "**Physical Reasonableness Check:** Modern cellular networks operate in the Gigahertz band ($10^9\\text{ Hz}$), confirming the validity of this result."
                ]
            }
        },
        # Page 7: Common Misconception / Discrepancy Note
        {
            "page_number": 7,
            "page_title": "Exam Tip: Avoiding Textbook Transcription Traps",
            "block_type": "common_misconception",
            "component_type": "common_misconception",
            "content": {
                "text": (
                    "### The 30 MHz vs 300 MHz Discrepancy Alert\n"
                    "In some standard physics notes, questions asking for a $30\\text{ MHz}$ signal have mistakenly substituted $300 \\times 10^6\\text{ Hz}$ into the denominator.\n\n"
                    "- **Case A: If $f = 30\\text{ MHz}$ (VHF Radio)**:\n"
                    "  $$\\lambda = \\frac{3.0 \\times 10^8}{30 \\times 10^6} = \\mathbf{10.0\\text{ m}}$$\n\n"
                    "- **Case B: If $f = 300\\text{ MHz}$ (UHF Television)**:\n"
                    "  $$\\lambda = \\frac{3.0 \\times 10^8}{300 \\times 10^6} = \\mathbf{1.0\\text{ m}}$$\n\n"
                    "**Exam Strategy**: Always verify your question values carefully during substitutions, and never blindly memorize numerical answers without checking given parameters!"
                )
            }
        },
        # Page 8: Interactive Wave Builder Sandbox
        {
            "page_number": 8,
            "page_title": "Interactive Exploration: The EM Wave Builder",
            "block_type": "prediction",
            "component_type": "prediction",
            "content": {
                "text": (
                    "**Think & Predict Before Simulating:**\n\n"
                    "If you increase the frequency of an electromagnetic wave by a factor of $1,000$ (from $1\\text{ MHz}$ to $1\\text{ GHz}$):\n"
                    "1. What happens to the speed of the wave in a vacuum?\n"
                    "2. What happens to its physical wavelength?"
                )
            }
        },
        {
            "page_number": 8,
            "page_title": "Interactive Wave Simulation Sandbox",
            "block_type": "suggested_simulation",
            "component_type": "suggested_simulation",
            "content": {
                "text": "Interactive 3D wave sandbox allowing students to adjust frequency f (10^3 to 10^22 Hz) and amplitude, observing real-time wavelength compression, spectral band classification, and photon energy E = hf calculation.",
                "instruction": "Simulation Key: em_wave_builder. Real-time rendering of 3D electric (red) and magnetic (blue) sinusoidal fields."
            }
        },
        {
            "page_number": 8,
            "page_title": "Reflecting on Wave Invariance and Energy",
            "block_type": "reflection",
            "component_type": "reflection",
            "content": {
                "text": (
                    "Because wave speed is constant ($c = 3.0 \\times 10^8\\text{ m/s}$), increasing frequency by $1,000\\times$ compresses the wavelength "
                    "by exactly $1,000\\times$ (from $300\\text{ m}$ to $0.3\\text{ m}$). Higher frequency waves carry greater photon energy ($E = hf$)."
                )
            }
        },
        # Page 9: Knowledge Check (MCQ)
        {
            "page_number": 9,
            "page_title": "Check Your Understanding: EM Wave Speed",
            "block_type": "knowledge_check",
            "component_type": "knowledge_check",
            "content": {
                "check_type": "multiple_choice",
                "question": "Which of the following electromagnetic waves travels fastest in a vacuum?",
                "options": [
                    "All electromagnetic waves travel at the exact same speed ($3.0 \\times 10^8\\text{ m/s}$)",
                    "Gamma rays because they carry the highest energy",
                    "Radio waves because they have the longest wavelength",
                    "Visible light because human eyes can perceive it"
                ],
                "answer": "A",
                "explanation": (
                    "In a vacuum or air, all electromagnetic waves—from long radio waves to high-energy gamma rays—travel at the identical universal speed c = 3.0 * 10^8 m/s."
                )
            }
        },
        # Page 10: Knowledge Check (Calculation)
        {
            "page_number": 10,
            "page_title": "Check Your Understanding: FM Radio Wavelength",
            "block_type": "knowledge_check",
            "component_type": "knowledge_check",
            "content": {
                "check_type": "multiple_choice",
                "question": "A FM radio station in Nairobi broadcasts at $96.0\\text{ MHz}$. What is the wavelength of its broadcast signal? (Take $c = 3.0 \\times 10^8\\text{ m/s}$).",
                "options": [
                    "$\\lambda = 3.125\\text{ m}$",
                    "$\\lambda = 0.320\\text{ m}$",
                    "$\\lambda = 31.25\\text{ m}$",
                    "$\\lambda = 312.5\\text{ m}$"
                ],
                "answer": "A",
                "explanation": (
                    "Frequency in SI units: f = 96.0 MHz = 9.6 * 10^7 Hz.\n"
                    "Wavelength lambda = c / f = (3.0 * 10^8) / (9.6 * 10^7) = 3.125 m."
                )
            }
        },
        # Page 11: Summary & Key Takeaways
        {
            "page_number": 11,
            "page_title": "Module 4.1 Summary: EM Waves & Wave Equation",
            "block_type": "summary",
            "component_type": "summary",
            "content": {
                "text": (
                    "### Key Physical Foundations:\n"
                    "- **Structure**: Mutually perpendicular oscillating electric ($\\vec{E}$) and magnetic ($\\vec{B}$) fields propagating transverse to each other.\n"
                    "- **Medium-free**: Propagates through vacuum at speed $c = 3.0 \\times 10^8\\text{ m/s}$.\n"
                    "- **Wave Equation**: $c = f\\lambda \\implies f = \\frac{c}{\\lambda}$ and $\\lambda = \\frac{c}{f}$.\n"
                    "- **Metric Conversions**: Always convert $\\text{MHz} \\rightarrow 10^6\\text{ Hz}$, $\\text{GHz} \\rightarrow 10^9\\text{ Hz}$, and $\\text{nm} \\rightarrow 10^{-9}\\text{ m}$ before calculating."
                )
            }
        },
        {
            "page_number": 11,
            "page_title": "Core Takeaways on Wave Propagation",
            "block_type": "key_takeaway",
            "component_type": "key_takeaway",
            "content": {
                "text": "Electromagnetic waves are self-sustaining oscillating fields that travel through a vacuum at the universal speed of light, obeying c = f*lambda."
            }
        }
    ]
}


# =============================================================================
# MODULE 4.2 DATA — Experimental Speed of Light & Spectral Band Analysis
# =============================================================================
MODULE_4_2 = {
    "unit_name": "Module 4.2: Experimental Speed of Light and Spectral Band Analysis",
    "unit_order": 2,
    "lesson_title": "Experimental Speed of Light and Spectral Band Analysis",
    "cards": [
        # Page 1: Hook & Goals
        {
            "page_number": 1,
            "page_title": "Measuring the Speed of Light in the Laboratory",
            "block_type": "learning_goal",
            "component_type": "learning_goal",
            "content": {
                "text": (
                    "How do physicists prove that electromagnetic waves travel at $300,000\\text{ km/s}$? "
                    "Surprisingly, you can measure the speed of light right in a school lab using a household microwave oven and a tray of chocolate chips!\n\n"
                    "In this module, you will explore the standing wave microwave experiment, analyze waveform traces, and master the complete 7-band "
                    "electromagnetic spectrum from long radio waves to ultra-high-energy gamma rays.\n\n"
                    "By the end of this lesson, you will be able to:\n"
                    "- Describe the standing wave microwave method to determine the speed of light ($c = f \\cdot 2d$)\n"
                    "- Analyze waveform crest-to-crest traces to calculate wave frequency\n"
                    "- Map the seven spectral bands by wavelength, frequency, and photon energy\n"
                    "- Identify the production mechanisms and laboratory detectors for each electromagnetic wave band"
                )
            }
        },
        # Page 2: Microwave Oven Experiment
        {
            "page_number": 2,
            "page_title": "Laboratory Experiment: Speed of Light via Microwaves",
            "block_type": "step_process",
            "component_type": "step_process",
            "content": {
                "title": "Standing Wave Microwave Protocol",
                "steps": [
                    "**Aim:** To measure the speed of electromagnetic waves in air using standing wave hot spots in a microwave oven.",
                    "**Apparatus Required:** Microwave oven (rotating plate removed), flat tray, meltable substance (chocolate chips, mini-marshmallows, or cheese), millimeter ruler.",
                    "**Theory:** Stationary standing waves form inside the metallic oven cavity with nodes and antinodes. Food melts first at the antinodes (energy peaks). The distance between two consecutive melted hot spots ($d$) equals half a wavelength ($\\frac{\\lambda}{2}$), so $$\\mathbf{\\lambda = 2d}$$",
                    "**Procedure:** Spread an even layer of chocolate chips on the stationary tray. Heat on high power for $15-25$ seconds until the first distinct melt spots appear. Stop immediately.",
                    "**Measurement:** Measure the distance ($d$) between the centers of adjacent melted spots in meters. Read oven frequency from back label ($f = 2450\\text{ MHz} = 2.45 \\times 10^9\\text{ Hz}$). Calculate $c = f \\cdot (2d)$."
                ]
            }
        },
        {
            "page_number": 2,
            "page_title": "Standing Wave Hot Spots in Microwave Cavity",
            "block_type": "suggested_diagram",
            "component_type": "suggested_diagram",
            "content": {
                "text": "Experimental diagram showing a stationary tray in a microwave oven with standing wave antinodes melting chocolate spots at distance d = lambda/2, demonstrating speed of light calculation c = f * 2d.",
                "instruction": (
                    "Draw microwave oven cross section with stationary flat tray. "
                    "Draw sinusoidal standing wave inside cavity with nodes and antinodes. "
                    "Show melted chocolate circles directly beneath antinodes separated by distance d. "
                    "Annotate formula: lambda = 2*d and c = f*lambda."
                )
            }
        },
        # Page 3: Experimental Data Table & Error Analysis
        {
            "page_number": 3,
            "page_title": "Data Collection and Sources of Experimental Error",
            "block_type": "comparison_table",
            "component_type": "comparison_table",
            "content": {
                "headers": ["Trial", "Measured Hot Spot Distance (d)", "Calculated Wavelength ($\\lambda = 2d$)", "Calculated Speed of Light ($c = f\\lambda$)"],
                "rows": [
                    ["Trial 1", "$6.1\\text{ cm} = 0.061\\text{ m}$", "$0.122\\text{ m}$", "$$c = (2.45 \\times 10^9) \\times 0.122 = 2.99 \\times 10^8\\text{ m/s}$$"],
                    ["Trial 2", "$6.2\\text{ cm} = 0.062\\text{ m}$", "$0.124\\text{ m}$", "$$c = (2.45 \\times 10^9) \\times 0.124 = 3.04 \\times 10^8\\text{ m/s}$$"],
                    ["Trial 3", "$6.0\\text{ cm} = 0.060\\text{ m}$", "$0.120\\text{ m}$", "$$c = (2.45 \\times 10^9) \\times 0.120 = 2.94 \\times 10^8\\text{ m/s}$$"],
                    ["Average", "$6.1\\text{ cm} = 0.061\\text{ m}$", "$0.122\\text{ m}$", "$$\\mathbf{c_{\\text{avg}} = 2.99 \\times 10^8\\text{ m/s}}$$ (Matches theoretical $3.0 \\times 10^8\\text{ m/s}$)"]
                ]
            }
        },
        # Page 4: Worked Example Level 3
        {
            "page_number": 4,
            "page_title": "Example 3: Frequency of Red Visible Light",
            "block_type": "worked_example",
            "component_type": "worked_example",
            "content": {
                "problem": (
                    "Red visible light has a wavelength of approximately $600\\text{ nm}$. "
                    "Calculate the frequency of this red light. (Take $c = 3.0 \\times 10^8\\text{ m/s}$)."
                ),
                "steps": [
                    "**Given & Conversion:** Wavelength $\\lambda = 600\\text{ nm} = 600 \\times 10^{-9}\\text{ m} = 6.0 \\times 10^{-7}\\text{ m}$, Wave speed $c = 3.0 \\times 10^8\\text{ m/s}$. Required: Frequency $f$.",
                    "**Governing Equation:** $$c = f\\lambda \\implies f = \\frac{c}{\\lambda}$$",
                    "**Substitution & Calculation:** $$f = \\frac{3.0 \\times 10^8\\text{ m/s}}{6.0 \\times 10^{-7}\\text{ m}} = 0.5 \\times 10^{15}\\text{ Hz} = \\mathbf{5.0 \\times 10^{14}\\text{ Hz}}$$",
                    "**Attach Unit:** $f = 5.0 \\times 10^{14}\\text{ Hz}$ (or $500\\text{ THz}$)",
                    "**Physical Reasonableness Check:** Visible light occupies frequencies in the hundred-terahertz range ($10^{14}\\text{ Hz}$), verifying accuracy."
                ]
            }
        },
        # Page 5: Worked Example Level 4
        {
            "page_number": 5,
            "page_title": "Example 4: Waveform Trace Crest Analysis",
            "block_type": "worked_example",
            "component_type": "worked_example",
            "content": {
                "problem": (
                    "A student views an electromagnetic wave trace on an oscilloscope screen. "
                    "The wave travels through air at $3.0 \\times 10^8\\text{ m/s}$. The physical distance between the first crest "
                    "and the third crest is measured to be $12.0\\text{ mm}$. Determine the frequency of the wave."
                ),
                "steps": [
                    "**Waveform Analysis:** Distance from 1st to 2nd crest is $1\\lambda$; distance from 2nd to 3rd crest is another $1\\lambda$. Total distance represents $2\\lambda$: $$2\\lambda = 12.0\\text{ mm} \\implies \\lambda = 6.0\\text{ mm} = 6.0 \\times 10^{-3}\\text{ m}$$",
                    "**Governing Equation:** $$c = f\\lambda \\implies f = \\frac{c}{\\lambda}$$",
                    "**Substitution & Calculation:** $$f = \\frac{3.0 \\times 10^8\\text{ m/s}}{6.0 \\times 10^{-3}\\text{ m}} = 0.5 \\times 10^{11} = \\mathbf{5.0 \\times 10^{10}\\text{ Hz}}$$",
                    "**Attach Unit:** $f = 5.0 \\times 10^{10}\\text{ Hz} = \\mathbf{50\\text{ GHz}}$",
                    "**Spectral Classification:** A wavelength of $6\\text{ mm}$ and frequency of $50\\text{ GHz}$ belongs to the microwave band, confirming physical realism."
                ]
            }
        },
        {
            "page_number": 5,
            "page_title": "Oscilloscope Waveform Trace and Crest Analysis",
            "block_type": "suggested_diagram",
            "component_type": "suggested_diagram",
            "content": {
                "text": "Waveform trace diagram showing 3 consecutive wave crests with dimension line spanning from Crest 1 to Crest 3 indicating 2*lambda = 12.0 mm, yielding lambda = 6.0 mm.",
                "instruction": (
                    "Draw dark oscilloscope grid. Draw sinusoidal wave trace with 3 marked crests. "
                    "Add dimension arrows showing 1st to 3rd crest = 2*lambda = 12 mm. "
                    "Add calculation callout: lambda = 6 mm, f = c/lambda = 50 GHz."
                )
            }
        },
        # Page 6: The Complete EM Spectrum (Horizontal)
        {
            "page_number": 6,
            "page_title": "The Complete Electromagnetic Spectrum Scale",
            "block_type": "concept_explanation",
            "component_type": "concept_explanation",
            "content": {
                "text": (
                    "### The Continuous Continuum\n"
                    "The electromagnetic spectrum is an unbroken continuous range divided into seven main regions:\n\n"
                    "$$\\text{Radio} \\longrightarrow \\text{Microwaves} \\longrightarrow \\text{Infrared} \\longrightarrow \\text{Visible Light} \\longrightarrow \\text{Ultraviolet} \\longrightarrow \\text{X-Rays} \\longrightarrow \\text{Gamma Rays}$$\n\n"
                    "- **From Left to Right**:\n"
                    "  - **Wavelength ($\\lambda$) decreases**: from $> 10^4\\text{ m}$ (radio) down to $< 10^{-12}\\text{ m}$ (gamma rays).\n"
                    "  - **Frequency ($f$) increases**: from $< 10^5\\text{ Hz}$ to $> 10^{21}\\text{ Hz}$.\n"
                    "  - **Photon Energy ($E = hf$) increases**: from low-energy harmless radio waves to lethal ionizing radiation!"
                )
            }
        },
        {
            "page_number": 6,
            "page_title": "Horizontal Electromagnetic Spectrum Continuum",
            "block_type": "suggested_diagram",
            "component_type": "suggested_diagram",
            "content": {
                "text": "Horizontal continuous spectrum diagram mapping the 7 bands (Radio, Microwaves, Infrared, Visible ROYGBIV, Ultraviolet, X-Rays, Gamma Rays) with increasing frequency and decreasing wavelength scales.",
                "instruction": (
                    "Draw horizontal gradient band showing 7 regions: Radio (left, red/grey) to Gamma (right, purple). "
                    "Show expanded narrow visible light spectrum in center with rainbow colors ROYGBIV (700 nm to 400 nm). "
                    "Draw top arrow: Frequency & Energy Increasing. Draw bottom arrow: Wavelength Increasing to the left."
                )
            }
        },
        # Page 7: Vertical Spectrum Scale
        {
            "page_number": 7,
            "page_title": "Vertical Frequency vs. Wavelength Mapping",
            "block_type": "concept_explanation",
            "component_type": "concept_explanation",
            "content": {
                "text": (
                    "### Exact Quantitative Ranges of the 7 Bands:\n\n"
                    "1. **Radio Waves**: $\\lambda > 0.1\\text{ m}$, $f < 3.0 \\times 10^9\\text{ Hz}$\n"
                    "2. **Microwaves**: $\\lambda = 1.0 \\times 10^{-3} - 0.1\\text{ m}$, $f = 3.0 \\times 10^9 - 3.0 \\times 10^{11}\\text{ Hz}$\n"
                    "3. **Infrared Radiation**: $\\lambda = 7.0 \\times 10^{-7} - 1.0 \\times 10^{-3}\\text{ m}$, $f = 3.0 \\times 10^{11} - 4.3 \\times 10^{14}\\text{ Hz}$\n"
                    "4. **Visible Light**: $\\lambda = 4.0 \\times 10^{-7} - 7.0 \\times 10^{-7}\\text{ m}$ ($400 - 700\\text{ nm}$), $f = 4.3 \\times 10^{14} - 7.5 \\times 10^{14}\\text{ Hz}$\n"
                    "5. **Ultraviolet (UV)**: $\\lambda = 1.0 \\times 10^{-8} - 4.0 \\times 10^{-7}\\text{ m}$, $f = 7.5 \\times 10^{14} - 3.0 \\times 10^{16}\\text{ Hz}$\n"
                    "6. **X-Rays**: $\\lambda = 1.0 \\times 10^{-11} - 1.0 \\times 10^{-8}\\text{ m}$, $f = 3.0 \\times 10^{16} - 3.0 \\times 10^{19}\\text{ Hz}$\n"
                    "7. **Gamma Rays**: $\\lambda < 1.0 \\times 10^{-11}\\text{ m}$, $f > 3.0 \\times 10^{19}\\text{ Hz}$"
                )
            }
        },
        {
            "page_number": 7,
            "page_title": "Vertical Scale: Frequency vs. Wavelength Mapping",
            "block_type": "suggested_diagram",
            "component_type": "suggested_diagram",
            "content": {
                "text": "Vertical scale diagram mapping frequency in Hz on the left axis and wavelength in meters on the right axis for all 7 electromagnetic spectral bands.",
                "instruction": (
                    "Draw vertical ladder diagram. Left scale: Frequency 10^3 Hz to 10^23 Hz. "
                    "Right scale: Wavelength 10^6 m to 10^-14 m. "
                    "Mark 7 colored blocks in between: Radio, Microwave, IR, Visible, UV, X-Ray, Gamma Ray."
                )
            }
        },
        # Page 8: 7-Band Master Table
        {
            "page_number": 8,
            "page_title": "Master Analysis of the Seven Spectral Regions",
            "block_type": "comparison_table",
            "component_type": "comparison_table",
            "content": {
                "headers": ["Band", "Wavelength (m)", "Frequency (Hz)", "Production Source", "Detection Methods", "Unique Property"],
                "rows": [
                    ["Radio Waves", "$> 0.1$", "$< 3.0 \\times 10^9$", "Oscillating electrical circuits", "Aerials connected to radio receivers", "Easily diffracted around hills and buildings"],
                    ["Microwaves", "$10^{-3} - 0.1$", "$3 \\times 10^9 - 3 \\times 10^{11}$", "Special aerials / magnetrons", "Dish receivers, silicon diodes", "Penetrates atmosphere; absorbed by water molecules"],
                    ["Infrared", "$7 \\times 10^{-7} - 10^{-3}$", "$3 \\times 10^{11} - 4.3 \\times 10^{14}$", "Thermal vibration of hot atoms (Sun, jiko)", "Skin, thermopiles, photographic film", "Heats matter directly via thermal radiation"],
                    ["Visible Light", "$4 \\times 10^{-7} - 7 \\times 10^{-7}$", "$4.3 \\times 10^{14} - 7.5 \\times 10^{14}$", "Excited outer electrons in glowing objects", "Human eye, photocells, photographic film", "Narrow visible band (ROYGBIV: Red to Violet)"],
                    ["Ultraviolet", "$10^{-8} - 4 \\times 10^{-7}$", "$7.5 \\times 10^{14} - 3 \\times 10^{16}$", "Inner electron transitions (welding, Sun)", "Photographic film, fluorescent dyes", "Causes fluorescence; highly ionizing to skin/eyes"],
                    ["X-Rays", "$10^{-11} - 10^{-8}$", "$3 \\times 10^{16} - 3 \\times 10^{19}$", "Fast electrons striking heavy metal target", "Photographic plates, GM tubes", "Penetrates soft flesh but absorbed by dense bone"],
                    ["Gamma Rays", "$< 10^{-11}$", "$> 3 \\times 10^{19}$", "Spontaneous radioactive nuclear decay", "Geiger-Muller tubes, cloud chambers", "Highest penetration and destructive photon energy"]
                ]
            }
        },
        # Page 9: Knowledge Check (MCQ)
        {
            "page_number": 9,
            "page_title": "Check Your Understanding: Infrared Detection",
            "block_type": "knowledge_check",
            "component_type": "knowledge_check",
            "content": {
                "check_type": "multiple_choice",
                "question": "Which of the following devices is specifically used to detect infrared radiation in physics laboratories?",
                "options": [
                    "Thermopile and blackened thermometer bulb",
                    "Geiger-Muller tube and ratemeter",
                    "Fluorescent zinc sulfide screen",
                    "Radio dipole aerial and tuner"
                ],
                "answer": "A",
                "explanation": (
                    "Infrared radiation produces thermal heating effects and is detected using thermopiles, blackened bulb thermometers, or thermal camera sensors."
                )
            }
        },
        # Page 10: Knowledge Check (MCQ)
        {
            "page_number": 10,
            "page_title": "Check Your Understanding: X-Ray vs Gamma Ray Origin",
            "block_type": "knowledge_check",
            "component_type": "knowledge_check",
            "content": {
                "check_type": "multiple_choice",
                "question": "What is the primary physical difference in how X-rays and gamma rays are produced?",
                "options": [
                    "X-rays originate from electron decelerations and atomic transitions, while gamma rays originate from atomic nuclear disintegrations",
                    "X-rays travel slower than gamma rays in a vacuum",
                    "X-rays are longitudinal waves while gamma rays are transverse waves",
                    "X-rays carry positive electric charge while gamma rays are neutral"
                ],
                "answer": "A",
                "explanation": (
                    "X-rays are produced extra-nuclearly when high-speed electrons strike a metal target, whereas gamma rays are emitted directly from the unstable nucleus during radioactive decay."
                )
            }
        },
        # Page 11: Summary & Key Takeaways
        {
            "page_number": 11,
            "page_title": "Module 4.2 Summary: Spectral Bands & Detection",
            "block_type": "summary",
            "component_type": "summary",
            "content": {
                "text": (
                    "### Key Physical Takeaways:\n"
                    "- **Speed of Light Measurement**: Standing wave hot spots in microwave ovens occur at intervals of $\\frac{\\lambda}{2}$, allowing $c = f(2d)$ determination.\n"
                    "- **Order of 7 Bands**: Radio $\\rightarrow$ Microwaves $\\rightarrow$ Infrared $\\rightarrow$ Visible $\\rightarrow$ UV $\\rightarrow$ X-Rays $\\rightarrow$ Gamma Rays.\n"
                    "- **Frequency & Wavelength Inversion**: Higher frequency corresponds to shorter wavelength and greater photon energy ($E = hf$)."
                )
            }
        },
        {
            "page_number": 11,
            "page_title": "Core Takeaways on the Spectrum",
            "block_type": "key_takeaway",
            "component_type": "key_takeaway",
            "content": {
                "text": "The electromagnetic spectrum spans from long, diffractive radio waves to energetic nuclear gamma rays, all propagating at the universal speed of light."
            }
        }
    ]
}


# =============================================================================
# MODULE 4.3 DATA — Applications, Biological Hazards & Shielding
# =============================================================================
MODULE_4_3 = {
    "unit_name": "Module 4.3: Technological Applications, Radiation Hazards, and Shielding",
    "unit_order": 3,
    "lesson_title": "Technological Applications, Radiation Hazards, and Shielding",
    "cards": [
        # Page 1: Hook & Goals
        {
            "page_number": 1,
            "page_title": "Applied Electromagnetic Radiation and Safety",
            "block_type": "learning_goal",
            "component_type": "learning_goal",
            "content": {
                "text": (
                    "Electromagnetic waves power global telecommunications, guide aircraft in bad weather, power greenhouse horticulture, "
                    "reveal internal bone fractures, and sterilize surgical equipment without heat!\n\n"
                    "However, as we move into the high-frequency regions of the spectrum, radiation becomes **ionizing** and poses serious biological hazards.\n\n"
                    "By the end of this lesson, you will be able to:\n"
                    "- Detail the technological, industrial, and medical applications of all 7 spectral bands\n"
                    "- Differentiate clearly between non-ionizing (thermal) and ionizing (DNA damaging) radiation\n"
                    "- Explain the biological hazards of UV, X-rays, and gamma rays\n"
                    "- Apply lead shielding and radiation protection protocols in radiography and nuclear physics"
                )
            }
        },
        # Page 2: Radio & Microwaves Applications
        {
            "page_number": 2,
            "page_title": "Telecommunications, RADAR, and Microwave Heating",
            "block_type": "concept_explanation",
            "component_type": "concept_explanation",
            "content": {
                "text": (
                    "### 1. Radio Waves Applications:\n"
                    "- **Broadcasting & Telephony**: Long-range AM, FM radio, television broadcasts, and cellular mobile phone networks.\n"
                    "- **Diffraction Advantage**: Long wavelengths allow radio waves to diffract around hills and buildings for reliable reception.\n\n"
                    "### 2. Microwaves Applications:\n"
                    "- **RADAR Systems (Radio Detection and Ranging)**: Short pulses are bounced off distant aircraft/ships to calculate position and velocity.\n"
                    "- **Police Speed Guns**: Use the Doppler frequency shift of reflected microwaves to measure vehicle velocity.\n"
                    "- **Domestic Microwave Ovens**: Microwaves at $2.45\\text{ GHz}$ are strongly absorbed by water molecules in food, converting electromagnetic energy directly into thermal agitation."
                )
            }
        },
        {
            "page_number": 2,
            "page_title": "Radar Ranging and Microwave Doppler Speed Gun",
            "block_type": "suggested_diagram",
            "component_type": "suggested_diagram",
            "content": {
                "text": "Technical diagram showing a radar antenna emitting pulsed microwaves towards an aircraft, reflecting an echo back to calculate range s = c*t/2, alongside a police Doppler speed gun detecting frequency shifts.",
                "instruction": (
                    "Draw radar dish sending pulsed blue microwave waves to airplane. Show reflected echo returning to dish. "
                    "Annotate range formula: Distance = (c * t) / 2. "
                    "Draw police speed gun on side emitting microwave to oncoming car with Doppler shifted return wave."
                )
            }
        },
        # Page 3: Infrared & Visible Light Applications
        {
            "page_number": 3,
            "page_title": "Infrared Thermal Imaging and Greenhouse Trapping",
            "block_type": "concept_explanation",
            "component_type": "concept_explanation",
            "content": {
                "text": (
                    "### 3. Infrared Radiation Applications:\n"
                    "- **Naivasha Greenhouse Agriculture**: Glass allows high-frequency solar visible light to enter; plants absorb it and re-radiate longer wavelength infrared, which cannot pass through glass, trapping thermal energy for rapid crop growth.\n"
                    "- **Thermal Diagnostic Imaging**: Medical thermograms map heat dissipation across patient bodies to locate inflammation and circulatory disorders.\n"
                    "- **Night-Vision & Remote Sensing**: Thermal sensors detect heat signatures of people and vehicles in total darkness.\n\n"
                    "### 4. Visible Light Applications:\n"
                    "- **Photosynthesis**: Chlorophyll captures visible light wavelengths ($400 - 700\\text{ nm}$) to convert carbon dioxide and water into glucose.\n"
                    "- **Satellite Optical Earth Observation**: High-resolution photography monitoring urban planning and forestry."
                )
            }
        },
        {
            "page_number": 3,
            "page_title": "Greenhouse Infrared Trapping Mechanism",
            "block_type": "suggested_diagram",
            "component_type": "suggested_diagram",
            "content": {
                "text": "Cross-sectional diagram of a greenhouse showing short-wavelength solar light entering through glass, warming plants and soil, and re-radiated long-wavelength infrared heat being trapped inside the glass structure.",
                "instruction": (
                    "Draw glass greenhouse structure. Draw incoming high-frequency solar rays (yellow) penetrating glass. "
                    "Show plants absorbing light and emitting long-wavelength infrared rays (red wiggly lines) reflecting back off glass walls. "
                    "Label: Trapped Infrared Thermal Energy."
                )
            }
        },
        # Page 4: UV & X-Ray Applications
        {
            "page_number": 4,
            "page_title": "Ultraviolet Security and Medical X-Ray Radiographs",
            "block_type": "concept_explanation",
            "component_type": "concept_explanation",
            "content": {
                "text": (
                    "### 5. Ultraviolet (UV) Applications:\n"
                    "- **Currency Forgery Detection**: Banknote security threads contain fluorescent dyes that glow brightly under UV light, detecting counterfeits instantly.\n"
                    "- **Reflective Highway Signage**: Absorbs invisible UV radiation and re-emits visible light to enhance nighttime visibility.\n\n"
                    "### 6. X-Rays Applications:\n"
                    "- **Medical Diagnostic Radiography**: High penetration allows X-rays to pass through soft flesh, but dense bone calcium absorbs them, creating sharp shadows on photographic film.\n"
                    "- **Industrial Flaw Detection**: Used to inspect welded joints on oil pipelines and turbine castings for invisible internal cracks.\n"
                    "- **Radiotherapy**: Focused narrow X-ray beams target and kill malignant cancer tumors."
                )
            }
        },
        {
            "page_number": 4,
            "page_title": "UV Fluorescent Note Verification & Skeletal X-Ray",
            "block_type": "suggested_diagram",
            "component_type": "suggested_diagram",
            "content": {
                "text": "Dual application diagram showing UV lamp revealing glowing fluorescent security watermark on a bank note, alongside an X-ray beam penetrating human hand flesh to cast skeletal bone shadows on photographic film.",
                "instruction": (
                    "Left Panel: Bank note illuminated by UV lamp with glowing fluorescent emblem. "
                    "Right Panel: X-ray source emitting rays through human hand onto film plate, showing light soft tissue transmission and dark bone absorption."
                )
            }
        },
        # Page 5: Gamma Rays Applications
        {
            "page_number": 5,
            "page_title": "Gamma Rays: Cold Sterilization & Grain Preservation",
            "block_type": "concept_explanation",
            "component_type": "concept_explanation",
            "content": {
                "text": (
                    "### 7. Gamma Rays Applications:\n"
                    "- **Cold Medical Sterilization**: Gamma rays destroy all bacteria and viruses on delicate syringes, plastic catheters, and surgical scalpels inside sealed packaging without requiring destructive heat.\n"
                    "- **Agricultural Pest Eradication & Food Preservation**: Harvested grain (maize, wheat) is irradiated with low-dose gamma rays, killing weevils, fungal spores, and insect larvae for safe multi-year storage in national silos.\n"
                    "- **Gamma Knife Cancer Surgery**: Cross-firing multiple fine cobalt-60 gamma beams at brain tumors with millimeter precision."
                )
            }
        },
        # Page 6: Non-Ionizing vs Ionizing Radiation
        {
            "page_number": 6,
            "page_title": "Non-Ionizing vs. Ionizing Radiation Hazards",
            "block_type": "comparison_table",
            "component_type": "comparison_table",
            "content": {
                "headers": ["Radiation Class", "Spectral Bands Included", "Photon Energy Level", "Biological Interaction", "Primary Hazards"],
                "rows": [
                    ["Non-Ionizing Radiation", "Radio, Microwaves, Infrared, Visible Light", "Low to Moderate ($E < 3.1\\text{ eV}$)", "Vibrates and excites molecules thermally without stripping electrons", "Excessive localized heating and thermal burns"],
                    ["Ionizing Radiation", "High-frequency UV, X-Rays, Gamma Rays", "Extremely High ($E > 10\\text{ eV}$)", "Strips electrons from atoms, creating reactive free radicals that break DNA bonds", "Cellular death, genetic mutations, cataracts, and cancer"]
                ]
            }
        },
        # Page 7: Radiation Protection & Shielding
        {
            "page_number": 7,
            "page_title": "Radiation Protection and Lead Shielding Physics",
            "block_type": "concept_explanation",
            "component_type": "concept_explanation",
            "content": {
                "text": (
                    "### Principles of Radiation Protection:\n\n"
                    "1. **Time**: Minimize the duration of exposure to ionizing sources.\n"
                    "2. **Distance**: Maintain maximum distance (intensity drops as $\\frac{1}{r^2}$ by the Inverse Square Law).\n"
                    "3. **Shielding**: Use dense absorbing materials:\n"
                    "   - **Ultraviolet**: Polycarbonate safety goggles and dark welding helmets.\n"
                    "   - **X-Rays**: Radiographers wear **lead aprons** ($0.5\\text{ mm}$ lead equivalent) and stand behind lead glass viewing screens.\n"
                    "   - **Gamma Rays**: Stored in **thick-walled lead castles** or heavy concrete bunkers and manipulated exclusively using remote robotic arms."
                )
            }
        },
        {
            "page_number": 7,
            "page_title": "Lead Shielding and Radiation Protection Protocols",
            "block_type": "suggested_diagram",
            "component_type": "suggested_diagram",
            "content": {
                "text": "Safety diagram illustrating radiation penetration and shielding: UV blocked by glass/plastic, X-rays absorbed by lead apron, and Gamma rays absorbed only by thick lead block and concrete walls.",
                "instruction": (
                    "Draw 3 rays from left to right: "
                    "(1) UV ray stopped by thin glass sheet. "
                    "(2) X-ray penetrating human body but fully stopped by lead sheet. "
                    "(3) Gamma ray penetrating body and thin lead, stopped only by thick lead castle and concrete bunker."
                )
            }
        },
        # Page 8: Worked Example Level 5 (Satellite Delay)
        {
            "page_number": 8,
            "page_title": "Example 5: Geostationary Satellite Transmission Delay",
            "block_type": "worked_example",
            "component_type": "worked_example",
            "content": {
                "problem": (
                    "A communications satellite in geostationary orbit is located $3.6 \\times 10^4\\text{ km}$ directly above a transceiver in Nairobi. "
                    "The station transmits a radio carrier at $150\\text{ MHz}$.\n"
                    "(a) Calculate the wavelength of the transmission.\n"
                    "(b) Determine the time taken for the radio signal to travel from Nairobi to the satellite. (Take $c = 3.0 \\times 10^8\\text{ m/s}$)."
                ),
                "steps": [
                    "**Given Data & Conversions:** Frequency $f = 150\\text{ MHz} = 1.5 \\times 10^8\\text{ Hz}$, Distance $s = 3.6 \\times 10^4\\text{ km} = 3.6 \\times 10^7\\text{ m}$, Wave speed $c = 3.0 \\times 10^8\\text{ m/s}$.",
                    "**(a) Wavelength Calculation:** $$\\lambda = \\frac{c}{f} = \\frac{3.0 \\times 10^8\\text{ m/s}}{1.5 \\times 10^8\\text{ Hz}} = \\mathbf{2.0\\text{ m}}$$",
                    "**(b) Travel Time Equation:** $$t = \\frac{\\text{Distance } (s)}{\\text{Speed } (c)} = \\frac{3.6 \\times 10^7\\text{ m}}{3.0 \\times 10^8\\text{ m/s}}$$",
                    "**Calculate Time:** $$t = 1.2 \\times 10^{-1}\\text{ s} = \\mathbf{0.12\\text{ s}} \\text{ (or } 120\\text{ ms)}$$",
                    "**Physical Reasonableness Check:** Electromagnetic waves travel $300,000\\text{ km/s}$, taking approximately $120\\text{ ms}$ to cross $36,000\\text{ km}$ of space, which matches real-world satellite telecommunication delays."
                ]
            }
        },
        # Page 9: Common Misconceptions
        {
            "page_number": 9,
            "page_title": "Common Misconceptions in Electromagnetic Radiation",
            "block_type": "common_misconception",
            "component_type": "common_misconception",
            "content": {
                "text": (
                    "### 1. The \"All Radiation is Radioactive\" Myth\n"
                    "**The Misconception**: Many students assume that any radiation is nuclear and deadly.\n"
                    "**The Physics Reality**: Radiation simply means energy emitted as waves. Visible light, Wi-Fi radio waves, and infrared heat from a stove are non-ionizing radiation. Only high-energy ionizing radiation (UV, X-rays, Gamma rays) damages cells.\n\n"
                    "### 2. The Sound Wave Error\n"
                    "**The Misconception**: Listing sound or ultrasound as an electromagnetic wave.\n"
                    "**The Physics Reality**: Sound waves are **mechanical longitudinal waves** requiring physical particles (air, water) to vibrate. They cannot travel through a vacuum, whereas EM waves travel freely across space at $3.0 \\times 10^8\\text{ m/s}$."
                )
            }
        },
        # Page 10: Knowledge Check: Ionization
        {
            "page_number": 10,
            "page_title": "Check Your Understanding: Biological Hazards",
            "block_type": "knowledge_check",
            "component_type": "knowledge_check",
            "content": {
                "check_type": "multiple_choice",
                "question": "Why do high-frequency ultraviolet, X-rays, and gamma rays cause cancer while radio waves and visible light do not?",
                "options": [
                    "Because their high photon energy enables them to ionize atoms and break chemical bonds in DNA molecules",
                    "Because they travel at faster speeds through living tissue",
                    "Because they carry negative electrical charge that shocks human cells",
                    "Because they are longitudinal waves that compress cell membranes"
                ],
                "answer": "A",
                "explanation": (
                    "Ionizing radiation carries sufficient photon energy (E = hf) to strip electrons from biological atoms, producing reactive free radicals that damage DNA structures and induce cancerous mutations."
                )
            }
        },
        # Page 11: Knowledge Check: Radiation Shielding
        {
            "page_number": 11,
            "page_title": "Check Your Understanding: Lead Shielding",
            "block_type": "knowledge_check",
            "component_type": "knowledge_check",
            "content": {
                "check_type": "multiple_choice",
                "question": "Why is lead widely used as the standard protective shielding material in medical X-ray facilities?",
                "options": [
                    "Lead has high atomic density and large atomic mass, making it highly effective at absorbing high-energy penetrating photons",
                    "Lead is completely transparent to X-rays, allowing them to pass safely into the floor",
                    "Lead carries an electrical charge that repels incoming X-ray photons",
                    "Lead reflects X-rays like a mirror back into the X-ray tube"
                ],
                "answer": "A",
                "explanation": (
                    "Lead (Pb) has a very high atomic number (Z=82) and high physical density (11,340 kg/m^3), providing dense electron clouds that efficiently absorb penetrating X-ray and gamma radiation via photoelectric and Compton interactions."
                )
            }
        },
        # Page 12: Challenge Worked Example (Radar Echo & Cycles)
        {
            "page_number": 12,
            "page_title": "Challenge Problem: Coastal Radar Echo & Cycle Count",
            "block_type": "worked_example",
            "component_type": "worked_example",
            "content": {
                "problem": (
                    "A coastal radar station transmits a microwave pulse of frequency $10.0\\text{ GHz}$ towards an incoming cargo vessel located $45.0\\text{ km}$ away.\n"
                    "(a) Calculate the total round-trip time delay between pulse transmission and echo detection.\n"
                    "(b) Calculate the total number of complete wave cycles contained in the one-way travel path between the radar and the ship. (Take $c = 3.0 \\times 10^8\\text{ m/s}$)."
                ),
                "steps": [
                    "**Given Data & Conversions:** One-way distance $s = 45.0\\text{ km} = 45,000\\text{ m}$, Frequency $f = 10.0\\text{ GHz} = 1.0 \\times 10^{10}\\text{ Hz}$, Wave speed $c = 3.0 \\times 10^8\\text{ m/s}$.",
                    "**(a) Round-Trip Time Delay:** Total round-trip distance is $s_{\\text{total}} = 2s = 90,000\\text{ m}$. $$t = \\frac{s_{\\text{total}}}{c} = \\frac{9.0 \\times 10^4\\text{ m}}{3.0 \\times 10^8\\text{ m/s}} = \\mathbf{3.0 \\times 10^{-4}\\text{ s}} \\text{ (or } 300\\mu\\text{s)}$$",
                    "**(b) Wavelength of Microwave:** $$\\lambda = \\frac{c}{f} = \\frac{3.0 \\times 10^8\\text{ m/s}}{1.0 \\times 10^{10}\\text{ Hz}} = 0.03\\text{ m} = 3.0\\text{ cm}$$",
                    "**Number of Wave Cycles in One-Way Path:** $$N = \\frac{s}{\\lambda} = \\frac{45,000\\text{ m}}{0.03\\text{ m}} = \\mathbf{1.5 \\times 10^6\\text{ cycles}} \\text{ (1.5 million cycles)}$$",
                    "**Physical Conclusion:** In the $0.15\\text{ ms}$ it takes for the pulse to reach the ship, exactly 1.5 million complete microwave oscillations span the 45-kilometer distance."
                ]
            }
        },
        # Page 13: Summary & Key Takeaways
        {
            "page_number": 13,
            "page_title": "Module 4.3 Summary: Applications & Safety",
            "block_type": "summary",
            "component_type": "summary",
            "content": {
                "text": (
                    "### Key Applied Takeaways:\n"
                    "- **Communication & Radar**: Radio waves for long-range broadcasts; microwaves for high-bandwidth cellular, radar, and heating.\n"
                    "- **Thermal & Optical**: Infrared for greenhouse trapping and thermal imaging; visible light for photosynthesis and vision.\n"
                    "- **Security & Medicine**: UV for counterfeit detection; X-rays for bone imaging and tumor radiotherapy.\n"
                    "- **Nuclear Radiation**: Gamma rays for cold sterilization of medical equipment and silo grain preservation.\n"
                    "- **Shielding**: Time, Distance, and Lead shielding protect against hazardous ionizing radiation."
                )
            }
        },
        {
            "page_number": 13,
            "page_title": "Core Takeaways on Applied EM Radiation",
            "block_type": "key_takeaway",
            "component_type": "key_takeaway",
            "content": {
                "text": "Harnessing the electromagnetic spectrum drives modern communication and medicine, while proper lead shielding ensures biological safety."
            }
        }
    ]
}

ALL_MODULES_TOPIC4 = [MODULE_4_1, MODULE_4_2, MODULE_4_3]


# =============================================================================
# INGESTION EXECUTOR
# =============================================================================

def run_ingestion_topic4(replace_mode=False):
    print("=" * 80)
    print("VLEARN FORM 4 PHYSICS — TOPIC 4: ELECTROMAGNETIC SPECTRUM INGESTION")
    print(f"Mode: {'REPLACE (Destructive Fresh Ingestion)' if replace_mode else 'IDEMPOTENT SAFE UPDATE'}")
    print("=" * 80)

    curriculum = Curriculum.objects.filter(name="844").first()
    grade = Grade.objects.filter(curriculum=curriculum, name="Form 4").first()
    subject = Subject.objects.filter(grade=grade, name="Physics").first()

    topic, created = Topic.objects.get_or_create(
        subject=subject,
        name="Topic 4: Electromagnetic Spectrum",
        defaults={
            "description": (
                "Physical nature of electromagnetic waves, 3D perpendicular oscillating fields, wave equation c = f*lambda, "
                "standing wave microwave speed of light experiment, comprehensive 7-band spectral mapping, "
                "telecommunications, radar, medical radiography, cold sterilization, ionizing radiation hazards, and lead shielding."
            ),
            "order": 4
        }
    )
    print(f"Topic verified: {topic.name} (ID: {topic.id}) under {subject.name}\n")

    total_blocks_created = 0
    total_blocks_updated = 0

    for m_idx, m_data in enumerate(ALL_MODULES_TOPIC4, start=1):
        unit, created = LearningUnit.objects.get_or_create(
            topic=topic,
            name=m_data["unit_name"],
            defaults={"order": m_data["unit_order"]}
        )
        print(f"[{m_idx}/3] Learning Unit: '{unit.name}' ({'Created' if created else 'Found'})")

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
            lesson.title = m_data["lesson_title"]
            lesson.status = "published"
            lesson.save()
        print(f"     Lesson: '{lesson.title}' (ID: {lesson.id}, status={lesson.status})")

        with transaction.atomic():
            if replace_mode:
                del_blocks, _ = LessonBlock.objects.filter(lesson=lesson).delete()
                del_assets, _ = LessonAsset.objects.filter(lesson=lesson).delete()
                if del_blocks or del_assets:
                    print(f"     [Replace Mode] Purged {del_blocks} existing blocks, {del_assets} existing assets")

            for order, card in enumerate(m_data["cards"], start=1):
                clean_card = clean_content_dict(card)
                block_id = f"block_{lesson.id}_p{clean_card['page_number']}_{order}_{uuid.uuid4().hex[:6]}"

                if replace_mode:
                    LessonBlock.objects.create(
                        lesson=lesson,
                        block_id=block_id,
                        order=order,
                        page_number=clean_card["page_number"],
                        page_title=clean_card["page_title"],
                        block_type=clean_card["block_type"],
                        component_type=clean_card["component_type"],
                        component_order=order,
                        title=clean_card["page_title"],
                        content=clean_card["content"]
                    )
                    total_blocks_created += 1
                else:
                    existing_block = LessonBlock.objects.filter(
                        lesson=lesson,
                        page_number=clean_card["page_number"],
                        block_type=clean_card["block_type"]
                    ).first()

                    if existing_block:
                        existing_block.order = order
                        existing_block.page_title = clean_card["page_title"]
                        existing_block.component_type = clean_card["component_type"]
                        existing_block.component_order = order
                        existing_block.title = clean_card["page_title"]
                        
                        if isinstance(existing_block.content, dict) and 'svg_content' in existing_block.content:
                            clean_card["content"]["svg_content"] = existing_block.content["svg_content"]
                            clean_card["content"]["svg"] = existing_block.content.get("svg")
                        
                        existing_block.content = clean_card["content"]
                        existing_block.save()
                        total_blocks_updated += 1
                    else:
                        LessonBlock.objects.create(
                            lesson=lesson,
                            block_id=block_id,
                            order=order,
                            page_number=clean_card["page_number"],
                            page_title=clean_card["page_title"],
                            block_type=clean_card["block_type"],
                            component_type=clean_card["component_type"],
                            component_order=order,
                            title=clean_card["page_title"],
                            content=clean_card["content"]
                        )
                        total_blocks_created += 1

        num_pages = max(c["page_number"] for c in m_data["cards"])
        print(f"     Processed {len(m_data['cards'])} cards across {num_pages} pages.\n")

    print("=" * 80)
    print("TOPIC 4 INGESTION COMPLETED SUCCESSFULLY!")
    print(f"Total Blocks Created: {total_blocks_created} | Total Blocks Updated: {total_blocks_updated}")
    print(f"Topic: {topic.name} (ID: {topic.id}) under Subject: {subject.name}")
    print("=" * 80)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Form 4 Physics Topic 4 Ingestion")
    parser.add_argument("--replace", action="store_true", help="Purge and replace blocks fresh")
    args = parser.parse_args()
    run_ingestion_topic4(replace_mode=args.replace)
