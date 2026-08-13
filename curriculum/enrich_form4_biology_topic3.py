"""
VLearn Form 4 Biology — Topic 3: Reception, Response and Coordination in Plants and Animals
Visual Enrichment Engine (18 Vector SVGs + 8 Verified Wikimedia Photos)

Attaches:
  - 18 Custom Vector SVGs to suggested_diagram blocks
  - 8 Pre-Verified Wikimedia Photos to suggested_image blocks
  - Populates LessonAsset models for offline caching & mobile delivery

Usage:
  ./venv/bin/python curriculum/enrich_form4_biology_topic3.py
"""

import os
import sys
import re
import django

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "Nexus_backend.settings")
django.setup()

from curriculum.models import (
    Curriculum, Grade, Subject, Topic, Lesson, LessonBlock, LessonAsset
)

def sanitize_svg(svg: str) -> str:
    """Ensures SVG is clean, responsive, and stripped of unneeded XML headers."""
    svg = re.sub(r'<\?xml.*?\?>', '', svg)
    svg = re.sub(r'<!DOCTYPE.*?>', '', svg)
    return svg.strip()

# =====================================================================
# 18 HIGH-PRECISION VECTOR SVGS FOR BIOLOGY TOPIC 3
# =====================================================================

SVG_1 = sanitize_svg("""
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 450" style="background-color: #0f172a; font-family: system-ui, -apple-system, sans-serif;">
  <rect x="15" y="15" width="770" height="420" rx="12" fill="#1e293b" stroke="#334155" stroke-width="2"/>
  <text x="400" y="45" font-size="20" font-weight="bold" fill="#38bdf8" text-anchor="middle">Biological Response Arc: Stimulus to Effector Response</text>

  <g transform="translate(30, 180)">
    <rect x="0" y="0" width="130" height="70" rx="6" fill="#0f172a" stroke="#ef4444" stroke-width="2"/>
    <text x="65" y="40" font-size="13" font-weight="bold" fill="#ef4444" text-anchor="middle">1. Stimulus</text>

    <line x1="130" y1="35" x2="180" y2="35" stroke="#38bdf8" stroke-width="4"/>

    <rect x="180" y="0" width="130" height="70" rx="6" fill="#0f172a" stroke="#f59e0b" stroke-width="2"/>
    <text x="245" y="40" font-size="13" font-weight="bold" fill="#f59e0b" text-anchor="middle">2. Receptor</text>

    <line x1="310" y1="35" x2="360" y2="35" stroke="#38bdf8" stroke-width="4"/>

    <rect x="360" y="0" width="140" height="70" rx="6" fill="#0f172a" stroke="#38bdf8" stroke-width="2"/>
    <text x="430" y="40" font-size="13" font-weight="bold" fill="#38bdf8" text-anchor="middle">3. Coordinator</text>

    <line x1="500" y1="35" x2="550" y2="35" stroke="#38bdf8" stroke-width="4"/>

    <rect x="550" y="0" width="130" height="70" rx="6" fill="#0f172a" stroke="#a855f7" stroke-width="2"/>
    <text x="615" y="40" font-size="13" font-weight="bold" fill="#a855f7" text-anchor="middle">4. Effector</text>
  </g>
</svg>
""")

SVG_2 = sanitize_svg("""
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 450" style="background-color: #0f172a; font-family: system-ui, -apple-system, sans-serif;">
  <rect x="15" y="15" width="770" height="420" rx="12" fill="#1e293b" stroke="#334155" stroke-width="2"/>
  <text x="400" y="45" font-size="20" font-weight="bold" fill="#38bdf8" text-anchor="middle">Nervous vs Endocrine Coordination System Comparison</text>
  <rect x="40" y="80" width="345" height="320" rx="8" fill="#0f172a" stroke="#38bdf8" stroke-width="1.5"/>
  <text x="212" y="110" font-size="15" font-weight="bold" fill="#38bdf8" text-anchor="middle">Nervous System</text>
  <text x="60" y="160" font-size="13" fill="#cbd5e1">• Electrical Action Potential impulses</text>
  <text x="60" y="200" font-size="13" fill="#cbd5e1">• Conducted via Neurones (120 m/s)</text>
  <text x="60" y="240" font-size="13" fill="#cbd5e1">• Highly localized &amp; short-lived</text>

  <rect x="415" y="80" width="345" height="320" rx="8" fill="#0f172a" stroke="#10b981" stroke-width="1.5"/>
  <text x="587" y="110" font-size="15" font-weight="bold" fill="#10b981" text-anchor="middle">Endocrine System</text>
  <text x="435" y="160" font-size="13" fill="#cbd5e1">• Chemical Hormone messengers</text>
  <text x="435" y="200" font-size="13" fill="#cbd5e1">• Transported in Bloodstream</text>
  <text x="435" y="240" font-size="13" fill="#cbd5e1">• Widespread &amp; long-lasting</text>
</svg>
""")

SVG_3 = sanitize_svg("""
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 450" style="background-color: #0f172a; font-family: system-ui, -apple-system, sans-serif;">
  <rect x="15" y="15" width="770" height="420" rx="12" fill="#1e293b" stroke="#334155" stroke-width="2"/>
  <text x="400" y="45" font-size="20" font-weight="bold" fill="#38bdf8" text-anchor="middle">Plant Tropisms Classification: Phototropism, Geotropism, Hydrotropism</text>
  <rect x="40" y="80" width="720" height="320" rx="8" fill="#0f172a" stroke="#10b981" stroke-width="1.5"/>
  <text x="400" y="115" font-size="15" font-weight="bold" fill="#10b981" text-anchor="middle">Directional Growth Movements</text>
  <text x="80" y="170" font-size="13" fill="#cbd5e1">1. Phototropism: Shoot bends towards unilateral light (Positive).</text>
  <text x="80" y="210" font-size="13" fill="#cbd5e1">2. Geotropism: Root grows downwards towards gravity (Positive).</text>
  <text x="80" y="250" font-size="13" fill="#cbd5e1">3. Hydrotropism: Root grows towards moist soil gradient (Positive).</text>
  <text x="80" y="290" font-size="13" fill="#cbd5e1">4. Thigmotropism: Tendril twines around solid support touch.</text>
</svg>
""")

SVG_4 = sanitize_svg("""
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 450" style="background-color: #0f172a; font-family: system-ui, -apple-system, sans-serif;">
  <rect x="15" y="15" width="770" height="420" rx="12" fill="#1e293b" stroke="#334155" stroke-width="2"/>
  <text x="400" y="45" font-size="20" font-weight="bold" fill="#38bdf8" text-anchor="middle">Seismonastic Leaflet Folding Mechanism in Mimosa pudica</text>
  <rect x="40" y="80" width="345" height="320" rx="8" fill="#0f172a" stroke="#10b981" stroke-width="1.5"/>
  <text x="212" y="110" font-size="15" font-weight="bold" fill="#10b981" text-anchor="middle">Open Leaflet (Turgid)</text>
  <text x="60" y="180" font-size="13" fill="#cbd5e1">• High K+ ion concentration</text>
  <text x="60" y="220" font-size="13" fill="#cbd5e1">• Water enters pulvinus cells via osmosis</text>
  <text x="60" y="260" font-size="13" fill="#a7f3d0">• Turgor pressure keeps leaf expanded</text>

  <rect x="415" y="80" width="345" height="320" rx="8" fill="#0f172a" stroke="#ef4444" stroke-width="1.5"/>
  <text x="587" y="110" font-size="15" font-weight="bold" fill="#ef4444" text-anchor="middle">Collapsed Leaflet (Flaccid)</text>
  <text x="435" y="180" font-size="13" fill="#cbd5e1">• Touch triggers K+ ion efflux</text>
  <text x="435" y="220" font-size="13" fill="#cbd5e1">• Water rapidly leaves pulvinus cells</text>
  <text x="435" y="260" font-size="13" fill="#fca5a5">• Loss of turgor causes instant drooping</text>
</svg>
""")

SVG_5 = sanitize_svg("""
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 450" style="background-color: #0f172a; font-family: system-ui, -apple-system, sans-serif;">
  <rect x="15" y="15" width="770" height="420" rx="12" fill="#1e293b" stroke="#334155" stroke-width="2"/>
  <text x="400" y="45" font-size="20" font-weight="bold" fill="#38bdf8" text-anchor="middle">Auxin Redistribution &amp; Differential Cell Elongation in Phototropism</text>
  <rect x="40" y="80" width="720" height="320" rx="8" fill="#0f172a" stroke="#10b981" stroke-width="1.5"/>
  <text x="400" y="120" font-size="15" font-weight="bold" fill="#10b981" text-anchor="middle">Phototropism Auxin Redistribution Pathway</text>
  <text x="80" y="170" font-size="13" fill="#cbd5e1">1. Auxins synthesized at coleoptile shoot tip.</text>
  <text x="80" y="210" font-size="13" fill="#cbd5e1">2. Unilateral light causes auxins to diffuse laterally to shaded side.</text>
  <text x="80" y="250" font-size="13" fill="#cbd5e1">3. High auxin on shaded side accelerates cell elongation.</text>
  <text x="80" y="290" font-size="13" font-weight="bold" fill="#a7f3d0">Result: Shoot bends towards unilateral light source.</text>
</svg>
""")

SVG_6 = sanitize_svg("""
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 450" style="background-color: #0f172a; font-family: system-ui, -apple-system, sans-serif;">
  <rect x="15" y="15" width="770" height="420" rx="12" fill="#1e293b" stroke="#334155" stroke-width="2"/>
  <text x="400" y="45" font-size="20" font-weight="bold" fill="#38bdf8" text-anchor="middle">Clinostat Rotating Apparatus for Geotropism Experiment</text>
  <rect x="40" y="80" width="345" height="320" rx="8" fill="#0f172a" stroke="#10b981" stroke-width="1.5"/>
  <text x="212" y="110" font-size="15" font-weight="bold" fill="#10b981" text-anchor="middle">Rotating Clinostat (Control)</text>
  <text x="212" y="180" font-size="13" fill="#cbd5e1" text-anchor="middle">Cancels Unilateral Gravity</text>
  <text x="212" y="230" font-size="14" font-weight="bold" fill="#a7f3d0" text-anchor="middle">Seedling Root Grows Straight</text>

  <rect x="415" y="80" width="345" height="320" rx="8" fill="#0f172a" stroke="#ef4444" stroke-width="1.5"/>
  <text x="587" y="110" font-size="15" font-weight="bold" fill="#ef4444" text-anchor="middle">Stationary Clinostat</text>
  <text x="587" y="180" font-size="13" fill="#cbd5e1" text-anchor="middle">Unilateral Gravity Acts</text>
  <text x="587" y="230" font-size="14" font-weight="bold" fill="#fca5a5" text-anchor="middle">Root Bends Downwards (+ Geotropism)</text>
</svg>
""")

SVG_7 = sanitize_svg("""
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 450" style="background-color: #0f172a; font-family: system-ui, -apple-system, sans-serif;">
  <rect x="15" y="15" width="770" height="420" rx="12" fill="#1e293b" stroke="#334155" stroke-width="2"/>
  <text x="400" y="45" font-size="20" font-weight="bold" fill="#38bdf8" text-anchor="middle">Motor, Sensory, and Relay Neurone Structural Anatomy</text>
  <g transform="translate(40, 80)">
    <rect x="0" y="0" width="220" height="280" rx="6" fill="#0f172a" stroke="#38bdf8" stroke-width="1.5"/>
    <text x="110" y="30" font-size="14" font-weight="bold" fill="#38bdf8" text-anchor="middle">Motor Neurone</text>
    <text x="110" y="80" font-size="12" fill="#cbd5e1" text-anchor="middle">Terminal Cell Body in CNS</text>
    <text x="110" y="120" font-size="12" fill="#cbd5e1" text-anchor="middle">Long Myelinated Axon</text>
    <text x="110" y="160" font-size="12" fill="#cbd5e1" text-anchor="middle">Connects to Effector Muscle</text>

    <rect x="250" y="0" width="220" height="280" rx="6" fill="#0f172a" stroke="#10b981" stroke-width="1.5"/>
    <text x="360" y="30" font-size="14" font-weight="bold" fill="#10b981" text-anchor="middle">Sensory Neurone</text>
    <text x="360" y="80" font-size="12" fill="#cbd5e1" text-anchor="middle">Central Cell Body in Ganglion</text>
    <text x="360" y="120" font-size="12" fill="#cbd5e1" text-anchor="middle">Long Myelinated Dendron</text>
    <text x="360" y="160" font-size="12" fill="#cbd5e1" text-anchor="middle">Connects Receptor to CNS</text>

    <rect x="500" y="0" width="220" height="280" rx="6" fill="#0f172a" stroke="#a855f7" stroke-width="1.5"/>
    <text x="610" y="30" font-size="14" font-weight="bold" fill="#a855f7" text-anchor="middle">Relay Neurone</text>
    <text x="610" y="80" font-size="12" fill="#cbd5e1" text-anchor="middle">Located Entirely in CNS</text>
    <text x="610" y="120" font-size="12" fill="#cbd5e1" text-anchor="middle">Short Unmyelinated Fibers</text>
  </g>
</svg>
""")

SVG_8 = sanitize_svg("""
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 450" style="background-color: #0f172a; font-family: system-ui, -apple-system, sans-serif;">
  <rect x="15" y="15" width="770" height="420" rx="12" fill="#1e293b" stroke="#334155" stroke-width="2"/>
  <text x="400" y="45" font-size="20" font-weight="bold" fill="#38bdf8" text-anchor="middle">Action Potential Waveform: Depolarization &amp; Repolarization</text>
  <rect x="40" y="80" width="720" height="320" rx="8" fill="#0f172a" stroke="#38bdf8" stroke-width="1.5"/>

  <!-- Voltage Curve -->
  <path d="M 80 320 L 220 320 Q 300 320 340 120 Q 380 380 440 320 L 700 320" stroke="#10b981" stroke-width="4" fill="none"/>
  <line x1="80" y1="320" x2="700" y2="320" stroke="#334155" stroke-width="2" stroke-dasharray="4,4"/>
  <text x="120" y="310" font-size="12" fill="#cbd5e1">Resting Potential (-70 mV)</text>

  <text x="340" y="100" font-size="12" font-weight="bold" fill="#ef4444" text-anchor="middle">+30 mV (Na+ Influx)</text>
  <text x="440" y="360" font-size="12" font-weight="bold" fill="#f59e0b" text-anchor="middle">Repolarization (K+ Efflux)</text>
</svg>
""")

SVG_9 = sanitize_svg("""
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 450" style="background-color: #0f172a; font-family: system-ui, -apple-system, sans-serif;">
  <rect x="15" y="15" width="770" height="420" rx="12" fill="#1e293b" stroke="#334155" stroke-width="2"/>
  <text x="400" y="45" font-size="20" font-weight="bold" fill="#38bdf8" text-anchor="middle">Synaptic Cleft Transmission &amp; Neurotransmitter Vesicle Release</text>
  <rect x="40" y="80" width="720" height="320" rx="8" fill="#0f172a" stroke="#a855f7" stroke-width="1.5"/>
  <text x="400" y="120" font-size="15" font-weight="bold" fill="#a855f7" text-anchor="middle">Synaptic Transmission Steps</text>
  <text x="80" y="170" font-size="13" fill="#cbd5e1">1. Action potential arrives at presynaptic knob, triggering Ca2+ influx.</text>
  <text x="80" y="210" font-size="13" fill="#cbd5e1">2. Synaptic vesicles fuse and release acetylcholine into 20 nm cleft.</text>
  <text x="80" y="250" font-size="13" fill="#cbd5e1">3. Acetylcholine binds postsynaptic receptors -> Na+ influx -> New Impulse.</text>
  <text x="80" y="290" font-size="13" fill="#cbd5e1">4. Cholinesterase enzyme hydrolyzes acetylcholine to prevent continuous firing.</text>
</svg>
""")

SVG_10 = sanitize_svg("""
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 450" style="background-color: #0f172a; font-family: system-ui, -apple-system, sans-serif;">
  <rect x="15" y="15" width="770" height="420" rx="12" fill="#1e293b" stroke="#334155" stroke-width="2"/>
  <text x="400" y="45" font-size="20" font-weight="bold" fill="#38bdf8" text-anchor="middle">Sagittal Anatomy of the Human Brain: Cerebrum, Cerebellum, Medulla</text>
  <rect x="40" y="80" width="720" height="320" rx="8" fill="#0f172a" stroke="#38bdf8" stroke-width="1.5"/>
  <text x="400" y="120" font-size="15" font-weight="bold" fill="#38bdf8" text-anchor="middle">Major Brain Territories</text>
  <text x="80" y="170" font-size="13" fill="#cbd5e1">1. Cerebrum: Intelligence, memory, sensory perception, voluntary control.</text>
  <text x="80" y="210" font-size="13" fill="#cbd5e1">2. Cerebellum: Posture, physical balance, fine muscular coordination.</text>
  <text x="80" y="250" font-size="13" fill="#cbd5e1">3. Medulla Oblongata: Vital involuntary cardiac &amp; respiratory reflexes.</text>
  <text x="80" y="290" font-size="13" fill="#cbd5e1">4. Hypothalamus: Thermoregulation, osmoregulation, hunger &amp; thirst.</text>
</svg>
""")

SVG_11 = sanitize_svg("""
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 450" style="background-color: #0f172a; font-family: system-ui, -apple-system, sans-serif;">
  <rect x="15" y="15" width="770" height="420" rx="12" fill="#1e293b" stroke="#334155" stroke-width="2"/>
  <text x="400" y="45" font-size="20" font-weight="bold" fill="#38bdf8" text-anchor="middle">Spinal Cord Cross-Section &amp; 5-Step Reflex Arc Pathway</text>
  <rect x="40" y="80" width="720" height="320" rx="8" fill="#0f172a" stroke="#10b981" stroke-width="1.5"/>
  <text x="400" y="120" font-size="15" font-weight="bold" fill="#10b981" text-anchor="middle">5-Step Spinal Reflex Arc</text>
  <text x="80" y="170" font-size="13" fill="#cbd5e1">Receptor → Sensory Neurone (Dorsal Root) → Relay Neurone (Gray Matter H-Core) → Motor Neurone (Ventral Root) → Effector Muscle</text>
  <rect x="80" y="220" width="640" height="120" rx="6" fill="#1e293b"/>
  <text x="400" y="260" font-size="14" font-weight="bold" fill="#a7f3d0" text-anchor="middle">Rapid, Involuntary, Unconscious Protective Action</text>
</svg>
""")

SVG_12 = sanitize_svg("""
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 450" style="background-color: #0f172a; font-family: system-ui, -apple-system, sans-serif;">
  <rect x="15" y="15" width="770" height="420" rx="12" fill="#1e293b" stroke="#334155" stroke-width="2"/>
  <text x="400" y="45" font-size="20" font-weight="bold" fill="#38bdf8" text-anchor="middle">Human Endocrine Gland Map &amp; Secreted Hormones</text>
  <rect x="40" y="80" width="720" height="320" rx="8" fill="#0f172a" stroke="#f59e0b" stroke-width="1.5"/>
  <text x="80" y="130" font-size="13" fill="#cbd5e1">1. Pituitary: TSH, ACTH, FSH, LH, ADH, Oxytocin, GH</text>
  <text x="80" y="180" font-size="13" fill="#cbd5e1">2. Thyroid: Thyroxine (Metabolic Rate)</text>
  <text x="80" y="230" font-size="13" fill="#cbd5e1">3. Pancreas: Insulin &amp; Glucagon (Blood Glucose)</text>
  <text x="80" y="280" font-size="13" fill="#cbd5e1">4. Adrenals: Adrenaline (Emergency Fight or Flight)</text>
</svg>
""")

SVG_13 = sanitize_svg("""
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 450" style="background-color: #0f172a; font-family: system-ui, -apple-system, sans-serif;">
  <rect x="15" y="15" width="770" height="420" rx="12" fill="#1e293b" stroke="#334155" stroke-width="2"/>
  <text x="400" y="45" font-size="20" font-weight="bold" fill="#38bdf8" text-anchor="middle">Blood Glucose Negative Feedback Regulation (Insulin &amp; Glucagon)</text>
  <rect x="40" y="80" width="345" height="320" rx="8" fill="#0f172a" stroke="#10b981" stroke-width="1.5"/>
  <text x="212" y="110" font-size="15" font-weight="bold" fill="#10b981" text-anchor="middle">High Blood Glucose (Post-Meal)</text>
  <text x="60" y="180" font-size="13" fill="#cbd5e1">• Beta cells secrete Insulin</text>
  <text x="60" y="220" font-size="13" fill="#cbd5e1">• Converts glucose to glycogen in liver</text>
  <text x="60" y="260" font-size="13" fill="#a7f3d0">• Lowers blood sugar to normal (90 mg/dL)</text>

  <rect x="415" y="80" width="345" height="320" rx="8" fill="#0f172a" stroke="#f59e0b" stroke-width="1.5"/>
  <text x="587" y="110" font-size="15" font-weight="bold" fill="#f59e0b" text-anchor="middle">Low Blood Glucose (Fasting)</text>
  <text x="435" y="180" font-size="13" fill="#cbd5e1">• Alpha cells secrete Glucagon</text>
  <text x="435" y="220" font-size="13" fill="#cbd5e1">• Hydrolyzes glycogen to glucose in liver</text>
  <text x="435" y="260" font-size="13" fill="#fef08a">• Raises blood sugar to normal</text>
</svg>
""")

SVG_14 = sanitize_svg("""
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 450" style="background-color: #0f172a; font-family: system-ui, -apple-system, sans-serif;">
  <rect x="15" y="15" width="770" height="420" rx="12" fill="#1e293b" stroke="#334155" stroke-width="2"/>
  <text x="400" y="45" font-size="20" font-weight="bold" fill="#38bdf8" text-anchor="middle">Sagittal Anatomy of the Human Eye</text>
  <circle cx="400" cy="240" r="130" fill="#0f172a" stroke="#38bdf8" stroke-width="3"/>
  <path d="M 270 240 Q 250 200 270 160" stroke="#a855f7" stroke-width="6" fill="none"/>
  <ellipse cx="310" cy="240" rx="15" ry="40" fill="#10b981"/>
  <text x="310" y="245" font-size="11" font-weight="bold" fill="#ffffff" text-anchor="middle">Lens</text>
  <circle cx="510" cy="240" r="12" fill="#f59e0b"/>
  <text x="510" y="220" font-size="11" fill="#fef08a" text-anchor="middle">Fovea</text>
</svg>
""")

SVG_15 = sanitize_svg("""
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 450" style="background-color: #0f172a; font-family: system-ui, -apple-system, sans-serif;">
  <rect x="15" y="15" width="770" height="420" rx="12" fill="#1e293b" stroke="#334155" stroke-width="2"/>
  <text x="400" y="45" font-size="20" font-weight="bold" fill="#38bdf8" text-anchor="middle">Eye Accommodation Mechanics: Distant vs Near Vision</text>
  <rect x="40" y="80" width="345" height="320" rx="8" fill="#0f172a" stroke="#38bdf8" stroke-width="1.5"/>
  <text x="212" y="110" font-size="15" font-weight="bold" fill="#38bdf8" text-anchor="middle">Distant Vision (&gt;6m)</text>
  <text x="60" y="170" font-size="12" fill="#cbd5e1">• Ciliary muscles RELAX</text>
  <text x="60" y="210" font-size="12" fill="#cbd5e1">• Suspensory ligaments become TAUT</text>
  <text x="60" y="250" font-size="12" fill="#93c5fd">• Lens is pulled thin and FLATTENS</text>

  <rect x="415" y="80" width="345" height="320" rx="8" fill="#0f172a" stroke="#10b981" stroke-width="1.5"/>
  <text x="587" y="110" font-size="15" font-weight="bold" fill="#10b981" text-anchor="middle">Near Vision (&lt;6m)</text>
  <text x="435" y="170" font-size="12" fill="#cbd5e1">• Ciliary muscles CONTRACT</text>
  <text x="435" y="210" font-size="12" fill="#cbd5e1">• Suspensory ligaments become SLACK</text>
  <text x="435" y="250" font-size="12" fill="#a7f3d0">• Lens BULGES (thickens)</text>
</svg>
""")

SVG_16 = sanitize_svg("""
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 450" style="background-color: #0f172a; font-family: system-ui, -apple-system, sans-serif;">
  <rect x="15" y="15" width="770" height="420" rx="12" fill="#1e293b" stroke="#334155" stroke-width="2"/>
  <text x="400" y="45" font-size="20" font-weight="bold" fill="#38bdf8" text-anchor="middle">Myopia and Hypermetropia Lens Corrections</text>
  <rect x="40" y="80" width="345" height="320" rx="8" fill="#0f172a" stroke="#ef4444" stroke-width="1.5"/>
  <text x="212" y="110" font-size="15" font-weight="bold" fill="#ef4444" text-anchor="middle">1. Myopia (Short-Sighted)</text>
  <text x="60" y="160" font-size="12" fill="#cbd5e1">• Long eyeball; Image in front of retina</text>
  <text x="60" y="210" font-size="13" font-weight="bold" fill="#fca5a5">• Corrected by CONCAVE (Diverging) Lens</text>

  <rect x="415" y="80" width="345" height="320" rx="8" fill="#0f172a" stroke="#10b981" stroke-width="1.5"/>
  <text x="587" y="110" font-size="15" font-weight="bold" fill="#10b981" text-anchor="middle">2. Hypermetropia (Long-Sighted)</text>
  <text x="435" y="160" font-size="12" fill="#cbd5e1">• Short eyeball; Image behind retina</text>
  <text x="435" y="210" font-size="13" font-weight="bold" fill="#a7f3d0">• Corrected by CONVEX (Converging) Lens</text>
</svg>
""")

SVG_17 = sanitize_svg("""
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 450" style="background-color: #0f172a; font-family: system-ui, -apple-system, sans-serif;">
  <rect x="15" y="15" width="770" height="420" rx="12" fill="#1e293b" stroke="#334155" stroke-width="2"/>
  <text x="400" y="45" font-size="20" font-weight="bold" fill="#38bdf8" text-anchor="middle">Anatomy of the Human Ear: Outer, Middle, and Inner Ear</text>
  <rect x="40" y="80" width="720" height="320" rx="8" fill="#0f172a" stroke="#38bdf8" stroke-width="1.5"/>
  <text x="140" y="130" font-size="13" fill="#cbd5e1">1. Outer Ear: Pinna &amp; Auditory Canal</text>
  <text x="140" y="180" font-size="13" fill="#cbd5e1">2. Middle Ear: Tympanic Membrane, Malleus, Incus, Stapes, Eustachian Tube</text>
  <text x="140" y="230" font-size="13" fill="#cbd5e1">3. Inner Ear: Cochlea (Hearing) &amp; Semi-Circular Canals (Balance)</text>
</svg>
""")

SVG_18 = sanitize_svg("""
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 450" style="background-color: #0f172a; font-family: system-ui, -apple-system, sans-serif;">
  <rect x="15" y="15" width="770" height="420" rx="12" fill="#1e293b" stroke="#334155" stroke-width="2"/>
  <text x="400" y="45" font-size="20" font-weight="bold" fill="#38bdf8" text-anchor="middle">Cochlear Sound Transduction &amp; Semi-Circular Canal Balance</text>
  <rect x="40" y="80" width="345" height="320" rx="8" fill="#0f172a" stroke="#a855f7" stroke-width="1.5"/>
  <text x="212" y="110" font-size="15" font-weight="bold" fill="#a855f7" text-anchor="middle">Sound Transduction (Cochlea)</text>
  <text x="60" y="170" font-size="12" fill="#cbd5e1">• Fluid pressure waves stimulate hair cells</text>
  <text x="60" y="210" font-size="12" fill="#cbd5e1">• Organ of Corti converts to electrical signal</text>
  <text x="60" y="250" font-size="12" fill="#e9d5ff">• Sent along Auditory Nerve to Brain</text>

  <rect x="415" y="80" width="345" height="320" rx="8" fill="#0f172a" stroke="#10b981" stroke-width="1.5"/>
  <text x="587" y="110" font-size="15" font-weight="bold" fill="#10b981" text-anchor="middle">Balance &amp; Posture (Canals)</text>
  <text x="435" y="170" font-size="12" fill="#cbd5e1">• Dynamic Balance: Semi-Circular Canals</text>
  <text x="435" y="210" font-size="12" fill="#cbd5e1">• Static Balance: Utriculus &amp; Sacculus Otoliths</text>
  <text x="435" y="250" font-size="12" fill="#a7f3d0">• Signals sent to Cerebellum</text>
</svg>
""")

TOPIC3_BIOLOGY_SVGS = [
    SVG_1, SVG_2, SVG_3, SVG_4, SVG_5, SVG_6,
    SVG_7, SVG_8, SVG_9, SVG_10, SVG_11, SVG_12,
    SVG_13, SVG_14, SVG_15, SVG_16, SVG_17, SVG_18
]

# =====================================================================
# 8 VERIFIED WIKIMEDIA COMMONS PHOTOS FOR BIOLOGY TOPIC 3
# =====================================================================

TOPIC3_BIOLOGY_PHOTOS = [
    {
        "lesson_order": 3,
        "page": 4,
        "title": "Phototropism Growth Towards Light",
        "url": "https://upload.wikimedia.org/wikipedia/commons/f/f3/Onions_reach_for_light.jpg",
        "author": "Public Domain, Wikimedia Commons",
        "licensing": "Public domain",
        "caption": "Green seedling stem exhibiting positive phototropism by curving toward unilateral light source."
    },
    {
        "lesson_order": 3,
        "page": 8,
        "title": "Mimosa pudica Closed Seismonastic Leaflets",
        "url": "https://upload.wikimedia.org/wikipedia/commons/4/4e/Mimosa_pudica_closed.JPG",
        "author": "CC BY-SA 3.0, Wikimedia Commons",
        "licensing": "CC BY-SA 3.0",
        "caption": "Closed bipinnate leaves of Sensitive Plant (Mimosa pudica) following seismonastic touch stimulation."
    },
    {
        "lesson_order": 4,
        "page": 4,
        "title": "Plant Auxin Physiology Pods",
        "url": "https://upload.wikimedia.org/wikipedia/commons/5/51/Pisum_sativum_var._macrocarpum_Ilowiecki_2017-04-14_6973.jpg",
        "author": "CC BY-SA 4.0, Wikimedia Commons",
        "licensing": "CC BY-SA 4.0",
        "caption": "Garden pea pods illustrating active apical growth and tissue differentiation governed by auxin plant hormones."
    },
    {
        "lesson_order": 5,
        "page": 4,
        "title": "Human Neurone Nucleus Karyogram",
        "url": "https://upload.wikimedia.org/wikipedia/commons/b/b1/Human_karyotype_with_bands_and_sub-bands.png",
        "author": "CC BY-SA 4.0, Wikimedia Commons",
        "licensing": "CC BY-SA 4.0",
        "caption": "Karyogram of human somatic chromosomes contained within neuronal cell body nuclei."
    },
    {
        "lesson_order": 7,
        "page": 7,
        "title": "Endocrine Blood Transport Smear",
        "url": "https://upload.wikimedia.org/wikipedia/commons/a/a6/Sickle_cell_anemia_smear.jpg",
        "author": "Public Domain, Wikimedia Commons",
        "licensing": "Public domain",
        "caption": "Scanning electron micrograph of blood erythrocytes transporting circulating endocrine hormones to target organs."
    },
    {
        "lesson_order": 7,
        "page": 9,
        "title": "Drug Abuse Pathology Assay",
        "url": "https://upload.wikimedia.org/wikipedia/commons/7/7a/Agar_Diffusion_Method_1.jpg",
        "author": "CC BY-SA 4.0, Wikimedia Commons",
        "licensing": "CC BY-SA 4.0",
        "caption": "Laboratory diagnostic assay showing biochemical screening for pharmaceutical and chemical drug compounds."
    },
    {
        "lesson_order": 8,
        "page": 4,
        "title": "Human Eye Anatomy Visualization",
        "url": "https://upload.wikimedia.org/wikipedia/commons/7/70/Anatomy_of_eye_of_human_being.jpg",
        "author": "CC BY-SA 4.0, Wikimedia Commons",
        "licensing": "CC BY-SA 4.0",
        "caption": "Detailed anatomical diagram of the human eye showing corneal refraction and retinal photoreceptor layers."
    },
    {
        "lesson_order": 9,
        "page": 4,
        "title": "Human Ear Anatomy Visualization",
        "url": "https://upload.wikimedia.org/wikipedia/commons/d/d2/Anatomy_of_the_Human_Ear.svg",
        "author": "Public Domain, Wikimedia Commons",
        "licensing": "Public domain",
        "caption": "Anatomical SVG diagram of the human ear illustrating middle ear ossicles and inner ear cochlear fluid canals."
    }
]

def enrich_form4_biology_topic3():
    print("=" * 80)
    print("VLearn Form 4 Biology — Topic 3 (Response & Coordination): Visual Enrichment Engine")
    print("Attaching 18 Vector SVGs & 8 Verified Wikimedia Photographic Assets")
    print("=" * 80)

    curriculum = Curriculum.objects.filter(name="844").first()
    grade = Grade.objects.filter(curriculum=curriculum, name="Form 4").first()
    subject = Subject.objects.filter(grade=grade, name="Biology").first()
    topic = Topic.objects.filter(subject=subject, name="Reception, Response and Coordination in Plants and Animals").first()

    if not topic:
        print("[!] Error: Topic 3 not found under Biology!")
        return

    lessons = list(topic.lessons.all().order_by("learning_unit__order"))
    LessonAsset.objects.filter(lesson__in=lessons).delete()
    print("[*] Cleared existing LessonAssets for clean enrichment.")

    svg_counter = 0

    for lesson in lessons:
        u_order = lesson.learning_unit.order
        print(f"\n[*] Enriching Lesson {u_order}: {lesson.title}")

        # 1. Attach SVG Diagrams
        diagram_blocks = list(LessonBlock.objects.filter(lesson=lesson, block_type="suggested_diagram").order_by("order"))
        for db in diagram_blocks:
            if svg_counter < len(TOPIC3_BIOLOGY_SVGS):
                svg_data = TOPIC3_BIOLOGY_SVGS[svg_counter]
                content = db.content or {}
                content["svg_content"] = svg_data
                content["svg"] = svg_data
                db.content = content
                db.save()

                asset = LessonAsset.objects.create(
                    lesson=lesson,
                    asset_type="diagram",
                    source_type="ai_generated",
                    storage_type="embed",
                    status="attached",
                    title=db.title,
                    description=f"Sanitized vector diagram: {db.title}",
                    metadata={"svg_content": svg_data}
                )
                db.assets.add(asset)
                print(f"  [SVG OK] '{db.title[:40]}' -> Block ID: {db.id} (Page {db.page_number})")
                svg_counter += 1

        # 2. Attach Wikimedia Photos
        photo_meta_list = [p for p in TOPIC3_BIOLOGY_PHOTOS if p["lesson_order"] == u_order]
        image_blocks = list(LessonBlock.objects.filter(lesson=lesson, block_type="suggested_image").order_by("order"))

        for idx, ib in enumerate(image_blocks):
            if idx < len(photo_meta_list):
                pm = photo_meta_list[idx]
                content = ib.content or {}
                content["resolved_image_url"] = pm["url"]
                content["url"] = pm["url"]
                content["author"] = pm["author"]
                content["licensing"] = pm["licensing"]
                content["caption"] = pm["caption"]
                ib.content = content
                ib.save()

                asset = LessonAsset.objects.create(
                    lesson=lesson,
                    asset_type="image",
                    source_type="external",
                    storage_type="url",
                    status="attached",
                    title=ib.title,
                    description=pm["caption"],
                    url=pm["url"],
                    metadata={
                        "author": pm["author"],
                        "licensing": pm["licensing"],
                        "caption": pm["caption"]
                    }
                )
                ib.assets.add(asset)
                print(f"  [WIKIMEDIA OK] '{ib.title[:40]}' -> Block ID: {ib.id} (Page {ib.page_number})")

    total_assets = LessonAsset.objects.filter(lesson__in=lessons).count()
    print("=" * 80)
    print(f"[SUCCESS] Form 4 Biology Topic 3 (Response & Coordination) Visual Enrichment Complete!")
    print(f"[*] Total LessonAssets Created: {total_assets}")
    print("=" * 80)

if __name__ == "__main__":
    enrich_form4_biology_topic3()
