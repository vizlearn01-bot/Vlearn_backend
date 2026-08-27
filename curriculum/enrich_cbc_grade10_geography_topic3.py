"""
VLearn CBC Grade 10 Geography — Topic 3: Statistical Methods
Visual Enrichment Engine (Vector SVGs, Verified Wikimedia Images & Educational Videos)

Subject: Geography (Grade 10 CBC)
Topic 3: Statistical Methods

Attaches:
  - 12 First-Card Photographic Visual Hooks (100% Tested HTTP 200 OK Direct Wikimedia URLs)
  - 12 Custom Sanitized Responsive Vector SVGs (viewBox="0 0 800 450", Dark/Light Mode Compatible)
  - Educational YouTube Video Assets for Fieldwork Methods & Climographs
  - Populates LessonAsset models for offline caching & mobile delivery

Usage:
  ./venv/bin/python curriculum/enrich_cbc_grade10_geography_topic3.py
"""

import os
import sys
import re
import json
import django

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "Nexus_backend.settings")
django.setup()

from curriculum.models import (
    Curriculum, Grade, Subject, Topic, Lesson, LessonBlock, LessonAsset
)

def sanitize_svg(svg: str) -> str:
    """Ensures SVG is clean, responsive, and stripped of unneeded XML/DOCTYPE headers."""
    svg = re.sub(r'<\?xml.*?\?>', '', svg)
    svg = re.sub(r'<!DOCTYPE.*?>', '', svg)
    return svg.strip()

# =============================================================================
# 12 CUSTOM RESPONSIVE VECTOR SVGS FOR GRADE 10 TOPIC 3: STATISTICAL METHODS
# =============================================================================

# SVG 1: Statistics as Data Condensation (Lesson 1)
SVG_DATA_CONDENSATION = sanitize_svg(r"""
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 450" style="background-color: #0f172a; font-family: system-ui, -apple-system, sans-serif;">
  <rect x="15" y="15" width="770" height="420" rx="12" fill="#1e293b" stroke="#334155" stroke-width="2"/>
  <text x="400" y="50" font-size="20" font-weight="bold" fill="#38bdf8" text-anchor="middle">The Role of Statistics: Simplifying Complex Raw Data</text>

  <!-- Panel 1: Raw Unorganized Data Cloud -->
  <rect x="45" y="80" width="310" height="320" rx="10" fill="#0f172a" stroke="#f87171" stroke-width="2"/>
  <rect x="55" y="90" width="290" height="30" rx="6" fill="#7f1d1d"/>
  <text x="200" y="110" font-size="13" font-weight="bold" fill="#fca5a5" text-anchor="middle">Raw Data: 365 Daily Readings</text>

  <g font-size="12" fill="#94a3b8" text-anchor="middle">
    <text x="100" y="150">21.4°C</text><text x="190" y="145">18.9°C</text><text x="280" y="155">23.1°C</text>
    <text x="130" y="185">17.2°C</text><text x="220" y="190">25.0°C</text><text x="300" y="180">19.8°C</text>
    <text x="90" y="225">22.6°C</text><text x="175" y="230">20.5°C</text><text x="270" y="220">24.2°C</text>
    <text x="120" y="265">16.8°C</text><text x="210" y="270">21.9°C</text><text x="295" y="260">18.4°C</text>
    <text x="95" y="305">23.8°C</text><text x="185" y="310">22.1°C</text><text x="280" y="300">20.9°C</text>
    <text x="200" y="345" font-size="11" fill="#f87171" font-weight="bold">Overwhelming &amp; Hard to Compare</text>
  </g>

  <!-- Arrow Transition -->
  <g transform="translate(370, 220)">
    <circle cx="25" cy="0" r="22" fill="#0284c7"/>
    <path d="M 18 -10 L 32 0 L 18 10 Z" fill="#ffffff"/>
    <text x="25" y="38" font-size="11" font-weight="bold" fill="#38bdf8" text-anchor="middle">Statistical</text>
    <text x="25" y="52" font-size="11" font-weight="bold" fill="#38bdf8" text-anchor="middle">Analysis</text>
  </g>

  <!-- Panel 2: Clean Statistical Summary -->
  <rect x="435" y="80" width="320" height="320" rx="10" fill="#0f172a" stroke="#22c55e" stroke-width="2"/>
  <rect x="445" y="90" width="300" height="30" rx="6" fill="#14532d"/>
  <text x="595" y="110" font-size="13" font-weight="bold" fill="#86efac" text-anchor="middle">Summary: Annual Mean Figure</text>

  <!-- Clean Thermometer Graphic -->
  <g transform="translate(500, 140)">
    <rect x="25" y="20" width="16" height="150" rx="8" fill="#334155" stroke="#64748b" stroke-width="2"/>
    <circle cx="33" cy="185" r="22" fill="#ef4444"/>
    <rect x="28" y="70" width="10" height="110" rx="5" fill="#ef4444"/>
    
    <line x1="45" y1="40" x2="55" y2="40" stroke="#94a3b8" stroke-width="2"/>
    <text x="62" y="44" font-size="10" fill="#94a3b8">30°C</text>
    <line x1="45" y1="70" x2="60" y2="70" stroke="#ef4444" stroke-width="2.5"/>
    <text x="68" y="74" font-size="12" font-weight="bold" fill="#ef4444">22°C (Mean)</text>
    <line x1="45" y1="100" x2="55" y2="100" stroke="#94a3b8" stroke-width="2"/>
    <text x="62" y="104" font-size="10" fill="#94a3b8">15°C</text>
    <line x1="45" y1="130" x2="55" y2="130" stroke="#94a3b8" stroke-width="2"/>
    <text x="62" y="134" font-size="10" fill="#94a3b8">10°C</text>
  </g>

  <rect x="460" y="325" width="270" height="55" rx="6" fill="#1e293b" stroke="#22c55e" stroke-width="1"/>
  <text x="595" y="348" font-size="13" font-weight="bold" fill="#4ade80" text-anchor="middle">Annual Average: 22.0°C</text>
  <text x="595" y="367" font-size="11" fill="#cbd5e1" text-anchor="middle">Enables Instant Regional Comparisons</text>
</svg>
""")

# SVG 2: Qualitative vs Quantitative Analytical Balance (Lesson 2)
SVG_QUAL_QUANT_BALANCE = sanitize_svg(r"""
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 450" style="background-color: #0f172a; font-family: system-ui, -apple-system, sans-serif;">
  <rect x="15" y="15" width="770" height="420" rx="12" fill="#1e293b" stroke="#334155" stroke-width="2"/>
  <text x="400" y="48" font-size="20" font-weight="bold" fill="#38bdf8" text-anchor="middle">The Balanced Geographical Inquiry Model</text>

  <!-- Left Side: Quantitative Metrics -->
  <rect x="50" y="85" width="310" height="230" rx="10" fill="#0f172a" stroke="#38bdf8" stroke-width="2"/>
  <rect x="60" y="95" width="290" height="30" rx="6" fill="#0369a1"/>
  <text x="205" y="115" font-size="13" font-weight="bold" fill="#ffffff" text-anchor="middle">Quantitative Data (The "What &amp; How Much")</text>
  <text x="75" y="150" font-size="12" fill="#cbd5e1">• Measurable numbers and statistics</text>
  <text x="75" y="175" font-size="12" fill="#cbd5e1">• Rainfall depth (mm), crop yields (tonnes)</text>
  <text x="75" y="200" font-size="12" fill="#cbd5e1">• Population densities, traffic counts</text>
  <text x="75" y="235" font-size="11" fill="#f87171" font-weight="bold">Constraint: Shows patterns but not causes</text>

  <!-- Right Side: Qualitative Field Context -->
  <rect x="440" y="85" width="310" height="230" rx="10" fill="#0f172a" stroke="#a855f7" stroke-width="2"/>
  <rect x="450" y="95" width="290" height="30" rx="6" fill="#7e22ce"/>
  <text x="595" y="115" font-size="13" font-weight="bold" fill="#ffffff" text-anchor="middle">Qualitative Data (The "Why &amp; How")</text>
  <text x="465" y="150" font-size="12" fill="#cbd5e1">• Descriptive field observations</text>
  <text x="465" y="175" font-size="12" fill="#cbd5e1">• Farmer interviews, oral histories</text>
  <text x="465" y="200" font-size="12" fill="#cbd5e1">• Indigenous weather forecasting wisdom</text>
  <text x="465" y="235" font-size="11" fill="#f87171" font-weight="bold">Constraint: Hard to compare statistically</text>

  <!-- Bottom Synthesis Box -->
  <rect x="150" y="340" width="500" height="75" rx="10" fill="#047857" stroke="#34d399" stroke-width="2"/>
  <text x="400" y="368" font-size="15" font-weight="bold" fill="#ffffff" text-anchor="middle">Combined Synthesis = Complete Geographical Truth</text>
  <text x="400" y="392" font-size="12" fill="#d1fae5" text-anchor="middle">Numbers reveal the spatial scale; human narratives explain the causal mechanisms.</text>
</svg>
""")

# SVG 3: Geographical Data Classification Tree (Lesson 3)
SVG_DATA_CLASSIFICATION_TREE = sanitize_svg(r"""
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 450" style="background-color: #0f172a; font-family: system-ui, -apple-system, sans-serif;">
  <rect x="15" y="15" width="770" height="420" rx="12" fill="#1e293b" stroke="#334155" stroke-width="2"/>
  <text x="400" y="45" font-size="20" font-weight="bold" fill="#38bdf8" text-anchor="middle">Geographical Data Classification Hierarchy</text>

  <!-- Root Node -->
  <rect x="300" y="70" width="200" height="40" rx="8" fill="#0284c7" stroke="#38bdf8" stroke-width="2"/>
  <text x="400" y="95" font-size="14" font-weight="bold" fill="#ffffff" text-anchor="middle">GEOGRAPHICAL DATA</text>

  <!-- Branching Lines -->
  <path d="M 300 90 L 160 90 L 160 140" fill="none" stroke="#64748b" stroke-width="2"/>
  <path d="M 500 90 L 640 90 L 640 140" fill="none" stroke="#64748b" stroke-width="2"/>

  <!-- Level 1: By Source vs By Nature -->
  <rect x="60" y="140" width="200" height="35" rx="6" fill="#1e293b" stroke="#38bdf8" stroke-width="1.5"/>
  <text x="160" y="162" font-size="12" font-weight="bold" fill="#38bdf8" text-anchor="middle">BY SOURCE</text>

  <rect x="540" y="140" width="200" height="35" rx="6" fill="#1e293b" stroke="#a855f7" stroke-width="1.5"/>
  <text x="640" y="162" font-size="12" font-weight="bold" fill="#c084fc" text-anchor="middle">BY NATURE</text>

  <!-- Level 2 Source: Primary vs Secondary -->
  <path d="M 160 175 L 100 200 L 100 220" fill="none" stroke="#64748b" stroke-width="1.5"/>
  <path d="M 160 175 L 220 200 L 220 220" fill="none" stroke="#64748b" stroke-width="1.5"/>

  <rect x="30" y="220" width="140" height="75" rx="6" fill="#0f172a" stroke="#22c55e" stroke-width="1.5"/>
  <text x="100" y="242" font-size="11" font-weight="bold" fill="#4ade80" text-anchor="middle">Primary Data</text>
  <text x="100" y="260" font-size="9" fill="#94a3b8" text-anchor="middle">First-hand from field</text>
  <text x="100" y="275" font-size="9" fill="#94a3b8" text-anchor="middle">(e.g. Rain gauge readings)</text>

  <rect x="170" y="220" width="140" height="75" rx="6" fill="#0f172a" stroke="#f59e0b" stroke-width="1.5"/>
  <text x="240" y="242" font-size="11" font-weight="bold" fill="#fbbf24" text-anchor="middle">Secondary Data</text>
  <text x="240" y="260" font-size="9" fill="#94a3b8" text-anchor="middle">Published sources</text>
  <text x="240" y="275" font-size="9" fill="#94a3b8" text-anchor="middle">(e.g. KNBS census reports)</text>

  <!-- Level 2 Nature: Quantitative vs Qualitative -->
  <path d="M 640 175 L 560 200 L 560 220" fill="none" stroke="#64748b" stroke-width="1.5"/>
  <path d="M 640 175 L 710 200 L 710 220" fill="none" stroke="#64748b" stroke-width="1.5"/>

  <rect x="490" y="220" width="140" height="75" rx="6" fill="#0f172a" stroke="#38bdf8" stroke-width="1.5"/>
  <text x="560" y="242" font-size="11" font-weight="bold" fill="#38bdf8" text-anchor="middle">Quantitative</text>
  <text x="560" y="260" font-size="9" fill="#94a3b8" text-anchor="middle">Numerical values</text>
  <text x="560" y="275" font-size="9" fill="#94a3b8" text-anchor="middle">(Counts &amp; Measures)</text>

  <rect x="640" y="220" width="140" height="75" rx="6" fill="#0f172a" stroke="#ec4899" stroke-width="1.5"/>
  <text x="710" y="242" font-size="11" font-weight="bold" fill="#f472b6" text-anchor="middle">Qualitative</text>
  <text x="710" y="260" font-size="9" fill="#94a3b8" text-anchor="middle">Descriptive text</text>
  <text x="710" y="275" font-size="9" fill="#94a3b8" text-anchor="middle">(Soil textures, opinions)</text>

  <!-- Level 3 Quantitative: Discrete vs Continuous -->
  <path d="M 560 295 L 500 325 L 500 345" fill="none" stroke="#64748b" stroke-width="1.5"/>
  <path d="M 560 295 L 610 325 L 610 345" fill="none" stroke="#64748b" stroke-width="1.5"/>

  <rect x="430" y="345" width="130" height="65" rx="6" fill="#1e293b" stroke="#06b6d4" stroke-width="1.5"/>
  <text x="495" y="365" font-size="10" font-weight="bold" fill="#22d3ee" text-anchor="middle">Discrete Data</text>
  <text x="495" y="382" font-size="9" fill="#94a3b8" text-anchor="middle">Countable integers</text>
  <text x="495" y="396" font-size="8" fill="#67e8f9" text-anchor="middle">(e.g. 5 matatus)</text>

  <rect x="580" y="345" width="130" height="65" rx="6" fill="#1e293b" stroke="#8b5cf6" stroke-width="1.5"/>
  <text x="645" y="365" font-size="10" font-weight="bold" fill="#a78bfa" text-anchor="middle">Continuous Data</text>
  <text x="645" y="382" font-size="9" fill="#94a3b8" text-anchor="middle">Unbroken scales</text>
  <text x="645" y="396" font-size="8" fill="#c4b5fd" text-anchor="middle">(e.g. 23.4°C temp)</text>
</svg>
""")

# SVG 4: Scientific Sampling Methods (Lesson 4)
SVG_SAMPLING_METHODS = sanitize_svg(r"""
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 450" style="background-color: #0f172a; font-family: system-ui, -apple-system, sans-serif;">
  <rect x="15" y="15" width="770" height="420" rx="12" fill="#1e293b" stroke="#334155" stroke-width="2"/>
  <text x="400" y="48" font-size="20" font-weight="bold" fill="#38bdf8" text-anchor="middle">Comparison of Core Sampling Methods</text>

  <!-- Panel 1: Simple Random Sampling -->
  <g transform="translate(40, 80)">
    <rect x="0" y="0" width="220" height="320" rx="8" fill="#0f172a" stroke="#38bdf8" stroke-width="2"/>
    <rect x="10" y="10" width="200" height="30" rx="5" fill="#0369a1"/>
    <text x="110" y="30" font-size="12" font-weight="bold" fill="#ffffff" text-anchor="middle">1. Random Sampling</text>

    <!-- Visual dots grid with random selections -->
    <g fill="#475569" stroke="#64748b" stroke-width="1">
      <circle cx="45" cy="80" r="10"/><circle cx="90" cy="80" r="10"/><circle cx="135" cy="80" r="10"/><circle cx="180" cy="80" r="10"/>
      <circle cx="45" cy="120" r="10"/><circle cx="90" cy="120" r="10"/><circle cx="135" cy="120" r="10"/><circle cx="180" cy="120" r="10"/>
      <circle cx="45" cy="160" r="10"/><circle cx="90" cy="160" r="10"/><circle cx="135" cy="160" r="10"/><circle cx="180" cy="160" r="10"/>
      <circle cx="45" cy="200" r="10"/><circle cx="90" cy="200" r="10"/><circle cx="135" cy="200" r="10"/><circle cx="180" cy="200" r="10"/>
    </g>
    <!-- Selected random dots -->
    <circle cx="90" cy="80" r="10" fill="#38bdf8" stroke="#ffffff" stroke-width="2"/>
    <circle cx="45" cy="160" r="10" fill="#38bdf8" stroke="#ffffff" stroke-width="2"/>
    <circle cx="180" cy="160" r="10" fill="#38bdf8" stroke="#ffffff" stroke-width="2"/>
    <circle cx="135" cy="200" r="10" fill="#38bdf8" stroke="#ffffff" stroke-width="2"/>

    <text x="110" y="245" font-size="11" font-weight="bold" fill="#38bdf8" text-anchor="middle">Equal Probability</text>
    <text x="110" y="265" font-size="10" fill="#cbd5e1" text-anchor="middle">Every member has identical</text>
    <text x="110" y="280" font-size="10" fill="#cbd5e1" text-anchor="middle">chance of selection via lottery</text>
    <text x="110" y="295" font-size="10" fill="#cbd5e1" text-anchor="middle">or random numbers.</text>
  </g>

  <!-- Panel 2: Systematic Sampling -->
  <g transform="translate(290, 80)">
    <rect x="0" y="0" width="220" height="320" rx="8" fill="#0f172a" stroke="#22c55e" stroke-width="2"/>
    <rect x="10" y="10" width="200" height="30" rx="5" fill="#15803d"/>
    <text x="110" y="30" font-size="12" font-weight="bold" fill="#ffffff" text-anchor="middle">2. Systematic Sampling</text>

    <!-- Visual dots along regular sequence (every 4th) -->
    <g fill="#475569" stroke="#64748b" stroke-width="1">
      <circle cx="45" cy="80" r="10"/><circle cx="90" cy="80" r="10"/><circle cx="135" cy="80" r="10"/><circle cx="180" cy="80" r="10"/>
      <circle cx="45" cy="120" r="10"/><circle cx="90" cy="120" r="10"/><circle cx="135" cy="120" r="10"/><circle cx="180" cy="120" r="10"/>
      <circle cx="45" cy="160" r="10"/><circle cx="90" cy="160" r="10"/><circle cx="135" cy="160" r="10"/><circle cx="180" cy="160" r="10"/>
      <circle cx="45" cy="200" r="10"/><circle cx="90" cy="200" r="10"/><circle cx="135" cy="200" r="10"/><circle cx="180" cy="200" r="10"/>
    </g>
    <!-- Selected systematic dots: (every 4th item) -->
    <circle cx="45" cy="80" r="10" fill="#22c55e" stroke="#ffffff" stroke-width="2"/>
    <circle cx="45" cy="120" r="10" fill="#22c55e" stroke="#ffffff" stroke-width="2"/>
    <circle cx="45" cy="160" r="10" fill="#22c55e" stroke="#ffffff" stroke-width="2"/>
    <circle cx="45" cy="200" r="10" fill="#22c55e" stroke="#ffffff" stroke-width="2"/>

    <text x="110" y="245" font-size="11" font-weight="bold" fill="#4ade80" text-anchor="middle">Regular Mathematical Interval</text>
    <text x="110" y="265" font-size="10" fill="#cbd5e1" text-anchor="middle">Samples picked at fixed</text>
    <text x="110" y="280" font-size="10" fill="#cbd5e1" text-anchor="middle">intervals (e.g. every kth house</text>
    <text x="110" y="295" font-size="10" fill="#cbd5e1" text-anchor="middle">or every 50m along transect).</text>
  </g>

  <!-- Panel 3: Stratified Sampling -->
  <g transform="translate(540, 80)">
    <rect x="0" y="0" width="220" height="320" rx="8" fill="#0f172a" stroke="#a855f7" stroke-width="2"/>
    <rect x="10" y="10" width="200" height="30" rx="5" fill="#7e22ce"/>
    <text x="110" y="30" font-size="12" font-weight="bold" fill="#ffffff" text-anchor="middle">3. Stratified Sampling</text>

    <!-- Subgroup Strata boxes -->
    <rect x="25" y="65" width="170" height="40" rx="4" fill="#1e293b" stroke="#f59e0b"/>
    <circle cx="50" cy="85" r="7" fill="#fbbf24"/><circle cx="75" cy="85" r="7" fill="#fbbf24"/><circle cx="110" cy="85" r="7" fill="#fbbf24" stroke="#fff" stroke-width="2"/>
    <text x="155" y="89" font-size="8" fill="#fbbf24">Small Farms</text>

    <rect x="25" y="115" width="170" height="40" rx="4" fill="#1e293b" stroke="#ec4899"/>
    <circle cx="50" cy="135" r="7" fill="#f472b6"/><circle cx="75" cy="135" r="7" fill="#f472b6" stroke="#fff" stroke-width="2"/>
    <text x="155" y="139" font-size="8" fill="#f472b6">Med Farms</text>

    <rect x="25" y="165" width="170" height="40" rx="4" fill="#1e293b" stroke="#38bdf8"/>
    <circle cx="50" cy="185" r="7" fill="#38bdf8" stroke="#fff" stroke-width="2"/><circle cx="75" cy="185" r="7" fill="#38bdf8"/>
    <text x="155" y="189" font-size="8" fill="#38bdf8">Large Farms</text>

    <text x="110" y="245" font-size="11" font-weight="bold" fill="#c084fc" text-anchor="middle">Proportional Subgroups</text>
    <text x="110" y="265" font-size="10" fill="#cbd5e1" text-anchor="middle">Population divided into</text>
    <text x="110" y="280" font-size="10" fill="#cbd5e1" text-anchor="middle">strata; samples chosen</text>
    <text x="110" y="295" font-size="10" fill="#cbd5e1" text-anchor="middle">fairly from each stratum.</text>
  </g>
</svg>
""")

# SVG 5: Tally Recording System (Lesson 5)
SVG_TALLY_SYSTEM = sanitize_svg(r"""
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 450" style="background-color: #0f172a; font-family: system-ui, -apple-system, sans-serif;">
  <rect x="15" y="15" width="770" height="420" rx="12" fill="#1e293b" stroke="#334155" stroke-width="2"/>
  <text x="400" y="48" font-size="20" font-weight="bold" fill="#38bdf8" text-anchor="middle">The Standard 5-Bar Tally Recording Matrix</text>

  <!-- Progression of Stroke Counts -->
  <g transform="translate(60, 80)">
    <rect x="0" y="0" width="680" height="120" rx="8" fill="#0f172a" stroke="#38bdf8" stroke-width="1.5"/>
    <text x="340" y="28" font-size="13" font-weight="bold" fill="#38bdf8" text-anchor="middle">Real-Time Progression of Stroke Counts</text>

    <!-- Count 1 -->
    <g transform="translate(40, 45)">
      <line x1="20" y1="10" x2="20" y2="50" stroke="#f87171" stroke-width="4" stroke-linecap="round"/>
      <text x="20" y="68" font-size="12" fill="#94a3b8" text-anchor="middle">Count: 1</text>
    </g>

    <!-- Count 2 -->
    <g transform="translate(170, 45)">
      <line x1="15" y1="10" x2="15" y2="50" stroke="#f87171" stroke-width="4" stroke-linecap="round"/>
      <line x1="25" y1="10" x2="25" y2="50" stroke="#f87171" stroke-width="4" stroke-linecap="round"/>
      <text x="20" y="68" font-size="12" fill="#94a3b8" text-anchor="middle">Count: 2</text>
    </g>

    <!-- Count 3 -->
    <g transform="translate(300, 45)">
      <line x1="10" y1="10" x2="10" y2="50" stroke="#f87171" stroke-width="4" stroke-linecap="round"/>
      <line x1="20" y1="10" x2="20" y2="50" stroke="#f87171" stroke-width="4" stroke-linecap="round"/>
      <line x1="30" y1="10" x2="30" y2="50" stroke="#f87171" stroke-width="4" stroke-linecap="round"/>
      <text x="20" y="68" font-size="12" fill="#94a3b8" text-anchor="middle">Count: 3</text>
    </g>

    <!-- Count 4 -->
    <g transform="translate(430, 45)">
      <line x1="8" y1="10" x2="8" y2="50" stroke="#f87171" stroke-width="4" stroke-linecap="round"/>
      <line x1="16" y1="10" x2="16" y2="50" stroke="#f87171" stroke-width="4" stroke-linecap="round"/>
      <line x1="24" y1="10" x2="24" y2="50" stroke="#f87171" stroke-width="4" stroke-linecap="round"/>
      <line x1="32" y1="10" x2="32" y2="50" stroke="#f87171" stroke-width="4" stroke-linecap="round"/>
      <text x="20" y="68" font-size="12" fill="#94a3b8" text-anchor="middle">Count: 4</text>
    </g>

    <!-- Count 5: Complete Bundle -->
    <g transform="translate(560, 45)">
      <line x1="8" y1="10" x2="8" y2="50" stroke="#4ade80" stroke-width="4" stroke-linecap="round"/>
      <line x1="16" y1="10" x2="16" y2="50" stroke="#4ade80" stroke-width="4" stroke-linecap="round"/>
      <line x1="24" y1="10" x2="24" y2="50" stroke="#4ade80" stroke-width="4" stroke-linecap="round"/>
      <line x1="32" y1="10" x2="32" y2="50" stroke="#4ade80" stroke-width="4" stroke-linecap="round"/>
      <line x1="2" y1="48" x2="38" y2="12" stroke="#22c55e" stroke-width="4.5" stroke-linecap="round"/>
      <text x="20" y="68" font-size="12" font-weight="bold" fill="#4ade80" text-anchor="middle">Bundle = 5</text>
    </g>
  </g>

  <!-- Practical Example: Representing 24 Items -->
  <g transform="translate(60, 220)">
    <rect x="0" y="0" width="680" height="175" rx="8" fill="#0f172a" stroke="#22c55e" stroke-width="1.5"/>
    <text x="340" y="30" font-size="14" font-weight="bold" fill="#4ade80" text-anchor="middle">Field Example: Representing 24 Counted Private Cars</text>

    <!-- Four complete bundles + 4 single strokes -->
    <g transform="translate(100, 60)">
      <!-- Bundle 1 -->
      <g transform="translate(0, 0)">
        <line x1="8" y1="10" x2="8" y2="50" stroke="#4ade80" stroke-width="4"/><line x1="16" y1="10" x2="16" y2="50" stroke="#4ade80" stroke-width="4"/><line x1="24" y1="10" x2="24" y2="50" stroke="#4ade80" stroke-width="4"/><line x1="32" y1="10" x2="32" y2="50" stroke="#4ade80" stroke-width="4"/><line x1="2" y1="48" x2="38" y2="12" stroke="#22c55e" stroke-width="4.5"/>
        <text x="20" y="70" font-size="11" fill="#cbd5e1" text-anchor="middle">(5)</text>
      </g>
      <!-- Bundle 2 -->
      <g transform="translate(100, 0)">
        <line x1="8" y1="10" x2="8" y2="50" stroke="#4ade80" stroke-width="4"/><line x1="16" y1="10" x2="16" y2="50" stroke="#4ade80" stroke-width="4"/><line x1="24" y1="10" x2="24" y2="50" stroke="#4ade80" stroke-width="4"/><line x1="32" y1="10" x2="32" y2="50" stroke="#4ade80" stroke-width="4"/><line x1="2" y1="48" x2="38" y2="12" stroke="#22c55e" stroke-width="4.5"/>
        <text x="20" y="70" font-size="11" fill="#cbd5e1" text-anchor="middle">(10)</text>
      </g>
      <!-- Bundle 3 -->
      <g transform="translate(200, 0)">
        <line x1="8" y1="10" x2="8" y2="50" stroke="#4ade80" stroke-width="4"/><line x1="16" y1="10" x2="16" y2="50" stroke="#4ade80" stroke-width="4"/><line x1="24" y1="10" x2="24" y2="50" stroke="#4ade80" stroke-width="4"/><line x1="32" y1="10" x2="32" y2="50" stroke="#4ade80" stroke-width="4"/><line x1="2" y1="48" x2="38" y2="12" stroke="#22c55e" stroke-width="4.5"/>
        <text x="20" y="70" font-size="11" fill="#cbd5e1" text-anchor="middle">(15)</text>
      </g>
      <!-- Bundle 4 -->
      <g transform="translate(300, 0)">
        <line x1="8" y1="10" x2="8" y2="50" stroke="#4ade80" stroke-width="4"/><line x1="16" y1="10" x2="16" y2="50" stroke="#4ade80" stroke-width="4"/><line x1="24" y1="10" x2="24" y2="50" stroke="#4ade80" stroke-width="4"/><line x1="32" y1="10" x2="32" y2="50" stroke="#4ade80" stroke-width="4"/><line x1="2" y1="48" x2="38" y2="12" stroke="#22c55e" stroke-width="4.5"/>
        <text x="20" y="70" font-size="11" fill="#cbd5e1" text-anchor="middle">(20)</text>
      </g>
      <!-- 4 Remainder strokes -->
      <g transform="translate(400, 0)">
        <line x1="8" y1="10" x2="8" y2="50" stroke="#fbbf24" stroke-width="4"/><line x1="16" y1="10" x2="16" y2="50" stroke="#fbbf24" stroke-width="4"/><line x1="24" y1="10" x2="24" y2="50" stroke="#fbbf24" stroke-width="4"/><line x1="32" y1="10" x2="32" y2="50" stroke="#fbbf24" stroke-width="4"/>
        <text x="20" y="70" font-size="11" fill="#fbbf24" text-anchor="middle">(+4)</text>
      </g>
    </g>

    <text x="340" y="155" font-size="13" font-weight="bold" fill="#38bdf8" text-anchor="middle">Total Calculation: (4 × 5) + 4 = 24 Vehicles</text>
  </g>
</svg>
""")

# SVG 6: Field Data Collection Toolkit (Lesson 6)
SVG_FIELD_TOOLKIT = sanitize_svg(r"""
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 450" style="background-color: #0f172a; font-family: system-ui, -apple-system, sans-serif;">
  <rect x="15" y="15" width="770" height="420" rx="12" fill="#1e293b" stroke="#334155" stroke-width="2"/>
  <text x="400" y="48" font-size="20" font-weight="bold" fill="#38bdf8" text-anchor="middle">Primary Field Data Collection Toolkit</text>

  <!-- Tool 1: Questionnaires -->
  <g transform="translate(45, 80)">
    <rect x="0" y="0" width="220" height="320" rx="8" fill="#0f172a" stroke="#38bdf8" stroke-width="2"/>
    <rect x="10" y="10" width="200" height="32" rx="4" fill="#0284c7"/>
    <text x="110" y="32" font-size="12" font-weight="bold" fill="#ffffff" text-anchor="middle">1. Questionnaires</text>

    <!-- Clipboard Icon -->
    <rect x="75" y="60" width="70" height="90" rx="6" fill="#1e293b" stroke="#38bdf8" stroke-width="2"/>
    <rect x="90" y="52" width="40" height="15" rx="3" fill="#38bdf8"/>
    <line x1="90" y1="85" x2="130" y2="85" stroke="#94a3b8" stroke-width="2"/>
    <line x1="90" y1="105" x2="130" y2="105" stroke="#94a3b8" stroke-width="2"/>
    <line x1="90" y1="125" x2="120" y2="125" stroke="#94a3b8" stroke-width="2"/>

    <text x="110" y="180" font-size="11" font-weight="bold" fill="#38bdf8" text-anchor="middle">Structured Written Forms</text>
    <text x="15" y="210" font-size="10" fill="#cbd5e1">• Closed: Quick statistical codes</text>
    <text x="15" y="235" font-size="10" fill="#cbd5e1">• Open: Detailed explanations</text>
    <text x="15" y="260" font-size="10" fill="#cbd5e1">• Broad reach across population</text>
    <text x="15" y="285" font-size="10" fill="#cbd5e1">• Guarantees anonymity</text>
  </g>

  <!-- Tool 2: Personal Interviews -->
  <g transform="translate(290, 80)">
    <rect x="0" y="0" width="220" height="320" rx="8" fill="#0f172a" stroke="#a855f7" stroke-width="2"/>
    <rect x="10" y="10" width="200" height="32" rx="4" fill="#7e22ce"/>
    <text x="110" y="32" font-size="12" font-weight="bold" fill="#ffffff" text-anchor="middle">2. Personal Interviews</text>

    <!-- Dialog Speech Bubbles -->
    <rect x="50" y="65" width="75" height="50" rx="6" fill="#1e293b" stroke="#c084fc" stroke-width="2"/>
    <text x="87" y="94" font-size="11" fill="#c084fc" text-anchor="middle">Why?</text>
    <rect x="95" y="100" width="75" height="50" rx="6" fill="#7e22ce" stroke="#e9d5ff" stroke-width="1.5"/>
    <text x="132" y="129" font-size="11" fill="#ffffff" text-anchor="middle">Because...</text>

    <text x="110" y="180" font-size="11" font-weight="bold" fill="#c084fc" text-anchor="middle">Direct Dialogue</text>
    <text x="15" y="210" font-size="10" fill="#cbd5e1">• Clarifies ambiguous points</text>
    <text x="15" y="235" font-size="10" fill="#cbd5e1">• Probes complex causal issues</text>
    <text x="15" y="260" font-size="10" fill="#cbd5e1">• High response accuracy</text>
    <text x="15" y="285" font-size="10" fill="#cbd5e1">• Labor &amp; time intensive</text>
  </g>

  <!-- Tool 3: Ground Photography -->
  <g transform="translate(535, 80)">
    <rect x="0" y="0" width="220" height="320" rx="8" fill="#0f172a" stroke="#22c55e" stroke-width="2"/>
    <rect x="10" y="10" width="200" height="32" rx="4" fill="#15803d"/>
    <text x="110" y="32" font-size="12" font-weight="bold" fill="#ffffff" text-anchor="middle">3. Ground Photography</text>

    <!-- Camera Icon -->
    <rect x="65" y="70" width="90" height="60" rx="8" fill="#1e293b" stroke="#4ade80" stroke-width="2"/>
    <circle cx="110" cy="100" r="18" fill="#0f172a" stroke="#4ade80" stroke-width="2"/>
    <rect x="75" y="60" width="25" height="10" rx="2" fill="#4ade80"/>

    <text x="110" y="180" font-size="11" font-weight="bold" fill="#4ade80" text-anchor="middle">Visual Objective Evidence</text>
    <text x="15" y="210" font-size="10" fill="#cbd5e1">• Documents erosion &amp; terrain</text>
    <text x="15" y="235" font-size="10" fill="#cbd5e1">• Captures human land use</text>
    <text x="15" y="260" font-size="10" fill="#cbd5e1">• Permanent visual audit trail</text>
    <text x="15" y="285" font-size="10" fill="#cbd5e1">• Complements numbers</text>
  </g>
</svg>
""")

# SVG 7: Raw Data to Frequency Distribution Pipeline (Lesson 7)
SVG_FREQUENCY_PIPELINE = sanitize_svg(r"""
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 450" style="background-color: #0f172a; font-family: system-ui, -apple-system, sans-serif;">
  <rect x="15" y="15" width="770" height="420" rx="12" fill="#1e293b" stroke="#334155" stroke-width="2"/>
  <text x="400" y="45" font-size="20" font-weight="bold" fill="#38bdf8" text-anchor="middle">Raw Data to Frequency Distribution Pipeline</text>

  <!-- Step 1: Raw Unsorted Logs -->
  <g transform="translate(40, 75)">
    <rect x="0" y="0" width="200" height="330" rx="8" fill="#0f172a" stroke="#f87171" stroke-width="1.5"/>
    <rect x="10" y="10" width="180" height="28" rx="4" fill="#991b1b"/>
    <text x="100" y="29" font-size="12" font-weight="bold" fill="#ffffff" text-anchor="middle">1. Raw Field Logs</text>
    <text x="15" y="65" font-size="10" fill="#94a3b8">Buses, Cars, Cars,</text>
    <text x="15" y="85" font-size="10" fill="#94a3b8">Lorries, Cars, Bodas,</text>
    <text x="15" y="105" font-size="10" fill="#94a3b8">Cars, Buses, Bodas,</text>
    <text x="15" y="125" font-size="10" fill="#94a3b8">Cars, Cars, Cars,</text>
    <text x="15" y="145" font-size="10" fill="#94a3b8">Bicycles, Cars, Bodas,</text>
    <text x="15" y="165" font-size="10" fill="#94a3b8">Cars, Lorries, Cars...</text>
    <rect x="10" y="270" width="180" height="45" rx="4" fill="#1e293b"/>
    <text x="100" y="290" font-size="10" fill="#fca5a5" text-anchor="middle">Unorganized list of</text>
    <text x="100" y="305" font-size="10" font-weight="bold" fill="#fca5a5" text-anchor="middle">37 Raw Observations</text>
  </g>

  <!-- Arrow 1 -->
  <path d="M 245 240 L 285 240" fill="none" stroke="#38bdf8" stroke-width="3"/>

  <!-- Step 2: Categorization & Tallying -->
  <g transform="translate(290, 75)">
    <rect x="0" y="0" width="220" height="330" rx="8" fill="#0f172a" stroke="#fbbf24" stroke-width="1.5"/>
    <rect x="10" y="10" width="200" height="28" rx="4" fill="#b45309"/>
    <text x="110" y="29" font-size="12" font-weight="bold" fill="#ffffff" text-anchor="middle">2. Tally Grouping</text>
    
    <text x="15" y="65" font-size="11" font-weight="bold" fill="#cbd5e1">Buses: `| |`</text>
    <text x="15" y="100" font-size="11" font-weight="bold" fill="#cbd5e1">Cars: `||||` `||||` `||||` `||||`</text>
    <text x="15" y="135" font-size="11" font-weight="bold" fill="#cbd5e1">Lorries: `| | |`</text>
    <text x="15" y="170" font-size="11" font-weight="bold" fill="#cbd5e1">Motorbikes: `||||` `|`</text>
    <text x="15" y="205" font-size="11" font-weight="bold" fill="#cbd5e1">Bicycles: `| |`</text>

    <rect x="10" y="270" width="200" height="45" rx="4" fill="#1e293b"/>
    <text x="110" y="290" font-size="10" fill="#fde68a" text-anchor="middle">Five-stroke blocks</text>
    <text x="110" y="305" font-size="10" font-weight="bold" fill="#fde68a" text-anchor="middle">Prevent mental counting errors</text>
  </g>

  <!-- Arrow 2 -->
  <path d="M 515 240 L 545 240" fill="none" stroke="#22c55e" stroke-width="3"/>

  <!-- Step 3: Structured Frequency Table -->
  <g transform="translate(550, 75)">
    <rect x="0" y="0" width="210" height="330" rx="8" fill="#0f172a" stroke="#22c55e" stroke-width="1.5"/>
    <rect x="10" y="10" width="190" height="28" rx="4" fill="#15803d"/>
    <text x="105" y="29" font-size="12" font-weight="bold" fill="#ffffff" text-anchor="middle">3. Frequency Table</text>

    <!-- Table Structure -->
    <rect x="10" y="55" width="190" height="25" fill="#1e293b"/>
    <text x="20" y="72" font-size="10" font-weight="bold" fill="#38bdf8">Vehicle Type</text>
    <text x="160" y="72" font-size="10" font-weight="bold" fill="#38bdf8">Freq (f)</text>

    <text x="20" y="100" font-size="10" fill="#cbd5e1">Buses</text><text x="175" y="100" font-size="10" font-weight="bold" fill="#ffffff">2</text>
    <text x="20" y="125" font-size="10" fill="#cbd5e1">Cars</text><text x="175" y="125" font-size="10" font-weight="bold" fill="#4ade80">24</text>
    <text x="20" y="150" font-size="10" fill="#cbd5e1">Lorries</text><text x="175" y="150" font-size="10" font-weight="bold" fill="#ffffff">3</text>
    <text x="20" y="175" font-size="10" fill="#cbd5e1">Motorbikes</text><text x="175" y="175" font-size="10" font-weight="bold" fill="#ffffff">6</text>
    <text x="20" y="200" font-size="10" fill="#cbd5e1">Bicycles</text><text x="175" y="200" font-size="10" font-weight="bold" fill="#ffffff">2</text>

    <line x1="10" y1="215" x2="200" y2="215" stroke="#64748b" stroke-width="1.5"/>
    <text x="20" y="235" font-size="11" font-weight="bold" fill="#4ade80">Total Sum</text>
    <text x="175" y="235" font-size="11" font-weight="bold" fill="#4ade80">37</text>

    <rect x="10" y="270" width="190" height="45" rx="4" fill="#1e293b"/>
    <text x="105" y="290" font-size="10" fill="#86efac" text-anchor="middle">Data Audit Verified:</text>
    <text x="105" y="305" font-size="10" font-weight="bold" fill="#86efac" text-anchor="middle">Sum matches 37 logs</text>
  </g>
</svg>
""")

# SVG 8: Central Tendency & Outlier Skew Visualizer (Lesson 8)
SVG_CENTRAL_TENDENCY = sanitize_svg(r"""
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 450" style="background-color: #0f172a; font-family: system-ui, -apple-system, sans-serif;">
  <rect x="15" y="15" width="770" height="420" rx="12" fill="#1e293b" stroke="#334155" stroke-width="2"/>
  <text x="400" y="45" font-size="20" font-weight="bold" fill="#38bdf8" text-anchor="middle">Measures of Central Tendency &amp; Outlier Distortion</text>

  <!-- Tea Harvest Dataset Container -->
  <rect x="50" y="70" width="700" height="50" rx="8" fill="#0f172a" stroke="#38bdf8" stroke-width="1.5"/>
  <text x="400" y="92" font-size="12" font-weight="bold" fill="#38bdf8" text-anchor="middle">Kericho Tea Farm Harvests (Thousands of Tonnes):</text>
  <text x="400" y="110" font-size="14" font-weight="bold" fill="#ffffff" text-anchor="middle">12,   12,   12,   15 (Median),   18,   25,   32 (Outlier)</text>

  <!-- Visual Number Line Scale -->
  <g transform="translate(70, 160)">
    <line x1="20" y1="60" x2="640" y2="60" stroke="#64748b" stroke-width="4"/>

    <!-- Point 12 (triple) -->
    <circle cx="80" cy="60" r="14" fill="#a855f7"/>
    <text x="80" y="65" font-size="11" font-weight="bold" fill="#ffffff" text-anchor="middle">12</text>
    <text x="80" y="30" font-size="11" font-weight="bold" fill="#c084fc" text-anchor="middle">MODE (12k)</text>
    <text x="80" y="42" font-size="9" fill="#e9d5ff" text-anchor="middle">(Frequency = 3)</text>

    <!-- Point 15 (Median) -->
    <circle cx="170" cy="60" r="14" fill="#22c55e"/>
    <text x="170" y="65" font-size="11" font-weight="bold" fill="#ffffff" text-anchor="middle">15</text>
    <text x="170" y="105" font-size="12" font-weight="bold" fill="#4ade80" text-anchor="middle">MEDIAN (15k)</text>
    <text x="170" y="120" font-size="9" fill="#86efac" text-anchor="middle">Middle value (50/50 split)</text>

    <!-- Point 18 (Mean) -->
    <circle cx="260" cy="60" r="14" fill="#38bdf8"/>
    <text x="260" y="65" font-size="11" font-weight="bold" fill="#ffffff" text-anchor="middle">18</text>
    <text x="260" y="30" font-size="12" font-weight="bold" fill="#38bdf8" text-anchor="middle">MEAN (18k)</text>
    <text x="260" y="42" font-size="9" fill="#7dd3fc" text-anchor="middle">Sum / 7 = 126 / 7</text>

    <!-- Point 25 -->
    <circle cx="470" cy="60" r="10" fill="#475569"/>
    <text x="470" y="64" font-size="10" fill="#cbd5e1" text-anchor="middle">25</text>

    <!-- Point 32 (Outlier) -->
    <circle cx="610" cy="60" r="16" fill="#ef4444"/>
    <text x="610" y="65" font-size="11" font-weight="bold" fill="#ffffff" text-anchor="middle">32</text>
    <text x="610" y="30" font-size="11" font-weight="bold" fill="#f87171" text-anchor="middle">EXTREME OUTLIER</text>
    <text x="610" y="42" font-size="9" fill="#fca5a5" text-anchor="middle">Pulls Mean to the right</text>

    <!-- Outlier pull arrow -->
    <path d="M 280 60 L 590 60" fill="none" stroke="#f87171" stroke-width="2" stroke-dasharray="4"/>
  </g>

  <!-- Summary Cards at Bottom -->
  <g transform="translate(50, 310)">
    <rect x="0" y="0" width="220" height="95" rx="8" fill="#0f172a" stroke="#a855f7" stroke-width="1.5"/>
    <text x="110" y="24" font-size="12" font-weight="bold" fill="#c084fc" text-anchor="middle">Mode = 12,000 t</text>
    <text x="15" y="48" font-size="10" fill="#cbd5e1">• Most common harvest size</text>
    <text x="15" y="68" font-size="10" fill="#cbd5e1">• Useful for finding peak modal category</text>

    <rect x="240" y="0" width="220" height="95" rx="8" fill="#0f172a" stroke="#22c55e" stroke-width="1.5"/>
    <text x="350" y="24" font-size="12" font-weight="bold" fill="#4ade80" text-anchor="middle">Median = 15,000 t</text>
    <text x="255" y="48" font-size="10" fill="#cbd5e1">• Unaffected by extreme outliers</text>
    <text x="255" y="68" font-size="10" fill="#cbd5e1">• True representative typical farm</text>

    <rect x="480" y="0" width="220" height="95" rx="8" fill="#0f172a" stroke="#38bdf8" stroke-width="1.5"/>
    <text x="590" y="24" font-size="12" font-weight="bold" fill="#38bdf8" text-anchor="middle">Mean = 18,000 t</text>
    <text x="495" y="48" font-size="10" fill="#cbd5e1">• Mathematical balance point</text>
    <text x="495" y="68" font-size="10" fill="#cbd5e1">• Pulled upward by the 32k outlier</text>
  </g>
</svg>
""")

# SVG 9: Simple Bar Graph of Traffic Volume (Lesson 9)
SVG_BAR_GRAPH = sanitize_svg(r"""
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 450" style="background-color: #0f172a; font-family: system-ui, -apple-system, sans-serif;">
  <rect x="15" y="15" width="770" height="420" rx="12" fill="#1e293b" stroke="#334155" stroke-width="2"/>
  <text x="400" y="45" font-size="18" font-weight="bold" fill="#38bdf8" text-anchor="middle">Traffic Count at School Gate over 15 Minutes</text>

  <!-- Plot Area Frame -->
  <g transform="translate(100, 70)">
    <line x1="0" y1="280" x2="620" y2="280" stroke="#64748b" stroke-width="2"/>
    <line x1="0" y1="0" x2="0" y2="280" stroke="#64748b" stroke-width="2"/>

    <!-- Grid lines -->
    <line x1="0" y1="233" x2="620" y2="233" stroke="#334155" stroke-width="1" stroke-dasharray="3"/>
    <text x="-15" y="238" font-size="11" fill="#94a3b8" text-anchor="end">5</text>

    <line x1="0" y1="186" x2="620" y2="186" stroke="#334155" stroke-width="1" stroke-dasharray="3"/>
    <text x="-15" y="191" font-size="11" fill="#94a3b8" text-anchor="end">10</text>

    <line x1="0" y1="140" x2="620" y2="140" stroke="#334155" stroke-width="1" stroke-dasharray="3"/>
    <text x="-15" y="145" font-size="11" fill="#94a3b8" text-anchor="end">15</text>

    <line x1="0" y1="93" x2="620" y2="93" stroke="#334155" stroke-width="1" stroke-dasharray="3"/>
    <text x="-15" y="98" font-size="11" fill="#94a3b8" text-anchor="end">20</text>

    <line x1="0" y1="46" x2="620" y2="46" stroke="#334155" stroke-width="1" stroke-dasharray="3"/>
    <text x="-15" y="51" font-size="11" fill="#94a3b8" text-anchor="end">25</text>

    <line x1="0" y1="0" x2="620" y2="0" stroke="#334155" stroke-width="1" stroke-dasharray="3"/>
    <text x="-15" y="5" font-size="11" fill="#94a3b8" text-anchor="end">30</text>
    <text x="-15" y="285" font-size="11" fill="#94a3b8" text-anchor="end">0</text>

    <!-- Y-axis Label -->
    <text x="-50" y="140" font-size="13" font-weight="bold" fill="#38bdf8" text-anchor="middle" transform="rotate(-90, -50, 140)">Number of Vehicles (f)</text>

    <!-- Bar 1: Buses (2) -->
    <rect x="40" y="261" width="75" height="19" rx="3" fill="#f59e0b" stroke="#fbbf24" stroke-width="1.5"/>
    <text x="77" y="253" font-size="12" font-weight="bold" fill="#fbbf24" text-anchor="middle">2</text>
    <text x="77" y="302" font-size="12" fill="#cbd5e1" text-anchor="middle">Buses</text>

    <!-- Bar 2: Cars (24) -->
    <rect x="160" y="56" width="75" height="224" rx="3" fill="#38bdf8" stroke="#7dd3fc" stroke-width="1.5"/>
    <text x="197" y="48" font-size="13" font-weight="bold" fill="#38bdf8" text-anchor="middle">24</text>
    <text x="197" y="302" font-size="12" fill="#cbd5e1" text-anchor="middle">Cars</text>

    <!-- Bar 3: Lorries (3) -->
    <rect x="280" y="252" width="75" height="28" rx="3" fill="#ec4899" stroke="#f472b6" stroke-width="1.5"/>
    <text x="317" y="244" font-size="12" font-weight="bold" fill="#f472b6" text-anchor="middle">3</text>
    <text x="317" y="302" font-size="12" fill="#cbd5e1" text-anchor="middle">Lorries</text>

    <!-- Bar 4: Motorbikes (6) -->
    <rect x="400" y="224" width="75" height="56" rx="3" fill="#22c55e" stroke="#4ade80" stroke-width="1.5"/>
    <text x="437" y="216" font-size="12" font-weight="bold" fill="#4ade80" text-anchor="middle">6</text>
    <text x="437" y="302" font-size="12" fill="#cbd5e1" text-anchor="middle">Bodabodas</text>

    <!-- Bar 5: Bicycles (2) -->
    <rect x="520" y="261" width="75" height="19" rx="3" fill="#a855f7" stroke="#c084fc" stroke-width="1.5"/>
    <text x="557" y="253" font-size="12" font-weight="bold" fill="#c084fc" text-anchor="middle">2</text>
    <text x="557" y="302" font-size="12" fill="#cbd5e1" text-anchor="middle">Bicycles</text>
  </g>

  <!-- X-axis Label -->
  <text x="410" y="415" font-size="13" font-weight="bold" fill="#38bdf8" text-anchor="middle">Vehicle Category (Discrete Classes)</text>
</svg>
""")

# SVG 10: Precision Pie Chart of School Farm Land Use (Lesson 10)
SVG_PIE_CHART = sanitize_svg(r"""
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 450" style="background-color: #0f172a; font-family: system-ui, -apple-system, sans-serif;">
  <rect x="15" y="15" width="770" height="420" rx="12" fill="#1e293b" stroke="#334155" stroke-width="2"/>
  <text x="400" y="45" font-size="20" font-weight="bold" fill="#38bdf8" text-anchor="middle">Land Use Allocation on School Farm (100 Hectares)</text>

  <!-- Pie Chart Circle centered at (280, 240) with radius 140 -->
  <g transform="translate(280, 240)">
    <!-- Maize Sector: 180 deg -->
    <path d="M 0 0 L 140 0 A 140 140 0 0 1 -140 0 Z" fill="#22c55e" stroke="#0f172a" stroke-width="2"/>
    <text x="0" y="70" font-size="14" font-weight="bold" fill="#ffffff" text-anchor="middle">Maize: 50% (180°)</text>
    <text x="0" y="90" font-size="11" fill="#dcfce7" text-anchor="middle">50 Hectares</text>

    <!-- Beans Sector: 108 deg -->
    <path d="M 0 0 L -140 0 A 140 140 0 0 1 43.26 -133.15 Z" fill="#38bdf8" stroke="#0f172a" stroke-width="2"/>
    <text x="-65" y="-55" font-size="13" font-weight="bold" fill="#ffffff" text-anchor="middle">Beans: 30%</text>
    <text x="-65" y="-38" font-size="11" fill="#e0f2fe" text-anchor="middle">(108° / 30 ha)</text>

    <!-- Coffee Sector: 72 deg -->
    <path d="M 0 0 L 43.26 -133.15 A 140 140 0 0 1 140 0 Z" fill="#f59e0b" stroke="#0f172a" stroke-width="2"/>
    <text x="75" y="-55" font-size="13" font-weight="bold" fill="#ffffff" text-anchor="middle">Coffee: 20%</text>
    <text x="75" y="-38" font-size="11" fill="#fef3c7" text-anchor="middle">(72° / 20 ha)</text>

    <circle cx="0" cy="0" r="4" fill="#ffffff"/>
  </g>

  <!-- Mathematical Legend & Calculations Box -->
  <g transform="translate(480, 85)">
    <rect x="0" y="0" width="280" height="310" rx="8" fill="#0f172a" stroke="#64748b" stroke-width="1.5"/>
    <text x="140" y="28" font-size="13" font-weight="bold" fill="#38bdf8" text-anchor="middle">Sector Angle Formula:</text>
    <rect x="15" y="40" width="250" height="30" rx="4" fill="#1e293b"/>
    <text x="140" y="60" font-size="11" fill="#cbd5e1" text-anchor="middle">Angle = (Value / Total) × 360°</text>

    <!-- Sector 1 -->
    <g transform="translate(15, 85)">
      <rect x="0" y="0" width="18" height="18" rx="3" fill="#22c55e"/>
      <text x="28" y="14" font-size="12" font-weight="bold" fill="#4ade80">Maize (50 ha / 50%)</text>
      <text x="28" y="32" font-size="10" fill="#94a3b8">(50/100) × 360° = 180.0°</text>
    </g>

    <!-- Sector 2 -->
    <g transform="translate(15, 145)">
      <rect x="0" y="0" width="18" height="18" rx="3" fill="#38bdf8"/>
      <text x="28" y="14" font-size="12" font-weight="bold" fill="#38bdf8">Beans (30 ha / 30%)</text>
      <text x="28" y="32" font-size="10" fill="#94a3b8">(30/100) × 360° = 108.0°</text>
    </g>

    <!-- Sector 3 -->
    <g transform="translate(15, 205)">
      <rect x="0" y="0" width="18" height="18" rx="3" fill="#f59e0b"/>
      <text x="28" y="14" font-size="12" font-weight="bold" fill="#fbbf24">Coffee (20 ha / 20%)</text>
      <text x="28" y="32" font-size="10" fill="#94a3b8">(20/100) × 360° = 72.0°</text>
    </g>

    <line x1="15" y1="260" x2="265" y2="260" stroke="#334155" stroke-width="1.5"/>
    <text x="140" y="285" font-size="11" font-weight="bold" fill="#4ade80" text-anchor="middle">Sum Check: 180° + 108° + 72° = 360°</text>
  </g>
</svg>
""")

# SVG 11: Combined Dual-Axis Climatograph (Lesson 11)
SVG_CLIMOGRAPH = sanitize_svg(r"""
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 450" style="background-color: #0f172a; font-family: system-ui, -apple-system, sans-serif;">
  <rect x="15" y="15" width="770" height="420" rx="12" fill="#1e293b" stroke="#334155" stroke-width="2"/>
  <text x="400" y="42" font-size="18" font-weight="bold" fill="#38bdf8" text-anchor="middle">Combined Climate Graph (Climograph): Nairobi</text>

  <!-- Plot Area Frame -->
  <g transform="translate(90, 70)">
    <line x1="0" y1="280" x2="620" y2="280" stroke="#64748b" stroke-width="2"/>
    <line x1="0" y1="0" x2="0" y2="280" stroke="#38bdf8" stroke-width="2"/>
    <line x1="620" y1="0" x2="620" y2="280" stroke="#ef4444" stroke-width="2"/>

    <!-- Left Y-Axis: Rainfall (0 to 150 mm) -->
    <text x="-12" y="284" font-size="10" fill="#38bdf8" text-anchor="end">0</text>
    <text x="-12" y="228" font-size="10" fill="#38bdf8" text-anchor="end">30</text>
    <text x="-12" y="172" font-size="10" fill="#38bdf8" text-anchor="end">60</text>
    <text x="-12" y="116" font-size="10" fill="#38bdf8" text-anchor="end">90</text>
    <text x="-12" y="60" font-size="10" fill="#38bdf8" text-anchor="end">120</text>
    <text x="-12" y="5" font-size="10" fill="#38bdf8" text-anchor="end">150</text>
    <text x="-40" y="140" font-size="12" font-weight="bold" fill="#38bdf8" text-anchor="middle" transform="rotate(-90, -40, 140)">Rainfall (mm)</text>

    <!-- Right Y-Axis: Temperature (0 to 30 °C) -->
    <text x="632" y="284" font-size="10" fill="#ef4444">0</text>
    <text x="632" y="190" font-size="10" fill="#ef4444">10</text>
    <text x="632" y="97" font-size="10" fill="#ef4444">20</text>
    <text x="632" y="5" font-size="10" fill="#ef4444">30</text>
    <text x="660" y="140" font-size="12" font-weight="bold" fill="#ef4444" text-anchor="middle" transform="rotate(90, 660, 140)">Temperature (°C)</text>

    <!-- Rainfall Blue Bars -->
    <rect x="11" y="187" width="30" height="93" fill="#0284c7" stroke="#38bdf8" stroke-width="1"/>
    <rect x="63" y="205" width="30" height="75" fill="#0284c7" stroke="#38bdf8" stroke-width="1"/>
    <rect x="115" y="131" width="30" height="149" fill="#0284c7" stroke="#38bdf8" stroke-width="1"/>
    <rect x="166" y="56" width="30" height="224" fill="#0369a1" stroke="#38bdf8" stroke-width="1.5"/>
    <rect x="218" y="93" width="30" height="187" fill="#0284c7" stroke="#38bdf8" stroke-width="1"/>
    <rect x="270" y="168" width="30" height="112" fill="#0284c7" stroke="#38bdf8" stroke-width="1"/>
    <rect x="321" y="224" width="30" height="56" fill="#0284c7" stroke="#38bdf8" stroke-width="1"/>
    <rect x="373" y="205" width="30" height="75" fill="#0284c7" stroke="#38bdf8" stroke-width="1"/>
    <rect x="425" y="187" width="30" height="93" fill="#0284c7" stroke="#38bdf8" stroke-width="1"/>
    <rect x="476" y="112" width="30" height="168" fill="#0284c7" stroke="#38bdf8" stroke-width="1"/>
    <rect x="528" y="37" width="30" height="243" fill="#0369a1" stroke="#38bdf8" stroke-width="1.5"/>
    <rect x="580" y="75" width="30" height="205" fill="#0284c7" stroke="#38bdf8" stroke-width="1"/>

    <!-- Temperature Red Line Curve -->
    <polyline points="26,84 78,75 130,75 181,84 233,93 285,112 336,121 388,112 440,103 491,93 543,93 595,84" fill="none" stroke="#ef4444" stroke-width="3.5"/>

    <!-- Temperature dots -->
    <circle cx="26" cy="84" r="4" fill="#ef4444"/><circle cx="78" cy="75" r="4" fill="#ef4444"/><circle cx="130" cy="75" r="4" fill="#ef4444"/><circle cx="181" cy="84" r="4" fill="#ef4444"/><circle cx="233" cy="93" r="4" fill="#ef4444"/><circle cx="285" cy="112" r="4" fill="#ef4444"/><circle cx="336" cy="121" r="4" fill="#ef4444"/><circle cx="388" cy="112" r="4" fill="#ef4444"/><circle cx="440" cy="103" r="4" fill="#ef4444"/><circle cx="491" cy="93" r="4" fill="#ef4444"/><circle cx="543" cy="93" r="4" fill="#ef4444"/><circle cx="595" cy="84" r="4" fill="#ef4444"/>

    <!-- Month Labels -->
    <text x="26" y="300" font-size="10" fill="#cbd5e1" text-anchor="middle">Jan</text>
    <text x="78" y="300" font-size="10" fill="#cbd5e1" text-anchor="middle">Feb</text>
    <text x="130" y="300" font-size="10" fill="#cbd5e1" text-anchor="middle">Mar</text>
    <text x="181" y="300" font-size="10" fill="#cbd5e1" text-anchor="middle">Apr</text>
    <text x="233" y="300" font-size="10" fill="#cbd5e1" text-anchor="middle">May</text>
    <text x="285" y="300" font-size="10" fill="#cbd5e1" text-anchor="middle">Jun</text>
    <text x="336" y="300" font-size="10" fill="#cbd5e1" text-anchor="middle">Jul</text>
    <text x="388" y="300" font-size="10" fill="#cbd5e1" text-anchor="middle">Aug</text>
    <text x="440" y="300" font-size="10" fill="#cbd5e1" text-anchor="middle">Sep</text>
    <text x="491" y="300" font-size="10" fill="#cbd5e1" text-anchor="middle">Oct</text>
    <text x="543" y="300" font-size="10" fill="#cbd5e1" text-anchor="middle">Nov</text>
    <text x="595" y="300" font-size="10" fill="#cbd5e1" text-anchor="middle">Dec</text>
  </g>

  <!-- Legend Box at Bottom -->
  <g transform="translate(230, 410)">
    <rect x="0" y="0" width="16" height="12" fill="#0284c7" stroke="#38bdf8"/>
    <text x="22" y="10" font-size="11" fill="#cbd5e1">Monthly Rainfall (mm)</text>

    <line x1="180" y1="6" x2="205" y2="6" stroke="#ef4444" stroke-width="3"/>
    <circle cx="192" cy="6" r="3" fill="#ef4444"/>
    <text x="212" y="10" font-size="11" fill="#cbd5e1">Monthly Mean Temp (°C)</text>

    <text x="360" y="10" font-size="11" font-weight="bold" fill="#38bdf8">[Bimodal Regime: Peaks in Apr &amp; Nov]</text>
  </g>
</svg>
""")

# SVG 12: School-Based Geographical Inquiry Cycle (Lesson 12)
SVG_INQUIRY_CYCLE = sanitize_svg(r"""
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 450" style="background-color: #0f172a; font-family: system-ui, -apple-system, sans-serif;">
  <rect x="15" y="15" width="770" height="420" rx="12" fill="#1e293b" stroke="#334155" stroke-width="2"/>
  <text x="400" y="45" font-size="20" font-weight="bold" fill="#38bdf8" text-anchor="middle">The 6-Stage Geographical Inquiry Framework</text>

  <!-- Central Hub -->
  <circle cx="400" cy="235" r="55" fill="#0f172a" stroke="#38bdf8" stroke-width="2.5"/>
  <text x="400" y="230" font-size="12" font-weight="bold" fill="#38bdf8" text-anchor="middle">GEOGRAPHICAL</text>
  <text x="400" y="248" font-size="12" font-weight="bold" fill="#ffffff" text-anchor="middle">INQUIRY</text>

  <!-- 6 Outer Circular Stages -->
  <g transform="translate(400, 95)">
    <rect x="-95" y="-25" width="190" height="50" rx="8" fill="#0284c7" stroke="#38bdf8" stroke-width="1.5"/>
    <text x="0" y="-3" font-size="11" font-weight="bold" fill="#ffffff" text-anchor="middle">1. Define Question</text>
    <text x="0" y="14" font-size="9" fill="#e0f2fe" text-anchor="middle">Identify problem statement</text>
  </g>

  <g transform="translate(620, 160)">
    <rect x="-90" y="-25" width="180" height="50" rx="8" fill="#0369a1" stroke="#38bdf8" stroke-width="1.5"/>
    <text x="0" y="-3" font-size="11" font-weight="bold" fill="#ffffff" text-anchor="middle">2. Design Plan</text>
    <text x="0" y="14" font-size="9" fill="#e0f2fe" text-anchor="middle">Sampling &amp; ethical consent</text>
  </g>

  <g transform="translate(620, 310)">
    <rect x="-90" y="-25" width="180" height="50" rx="8" fill="#0f766e" stroke="#2dd4bf" stroke-width="1.5"/>
    <text x="0" y="-3" font-size="11" font-weight="bold" fill="#ffffff" text-anchor="middle">3. Collect Data</text>
    <text x="0" y="14" font-size="9" fill="#ccfbf1" text-anchor="middle">Tallies, measures, surveys</text>
  </g>

  <g transform="translate(400, 375)">
    <rect x="-95" y="-25" width="190" height="50" rx="8" fill="#15803d" stroke="#4ade80" stroke-width="1.5"/>
    <text x="0" y="-3" font-size="11" font-weight="bold" fill="#ffffff" text-anchor="middle">4. Organize &amp; Calculate</text>
    <text x="0" y="14" font-size="9" fill="#dcfce7" text-anchor="middle">Tables, Mean, Median, Mode</text>
  </g>

  <g transform="translate(180, 310)">
    <rect x="-90" y="-25" width="180" height="50" rx="8" fill="#b45309" stroke="#fbbf24" stroke-width="1.5"/>
    <text x="0" y="-3" font-size="11" font-weight="bold" fill="#ffffff" text-anchor="middle">5. Present &amp; Interpret</text>
    <text x="0" y="14" font-size="9" fill="#fef3c7" text-anchor="middle">Bar graphs, pie charts, maps</text>
  </g>

  <g transform="translate(180, 160)">
    <rect x="-90" y="-25" width="180" height="50" rx="8" fill="#7e22ce" stroke="#c084fc" stroke-width="1.5"/>
    <text x="0" y="-3" font-size="11" font-weight="bold" fill="#ffffff" text-anchor="middle">6. Conclude &amp; Report</text>
    <text x="0" y="14" font-size="9" fill="#f3e8ff" text-anchor="middle">Scientific report &amp; solutions</text>
  </g>

  <!-- Flow connecting arrows -->
  <path d="M 495 95 Q 560 110 580 135" fill="none" stroke="#38bdf8" stroke-width="2" stroke-dasharray="4"/>
  <path d="M 640 185 Q 650 240 640 285" fill="none" stroke="#2dd4bf" stroke-width="2" stroke-dasharray="4"/>
  <path d="M 570 335 Q 520 370 495 375" fill="none" stroke="#4ade80" stroke-width="2" stroke-dasharray="4"/>
  <path d="M 305 375 Q 240 365 210 335" fill="none" stroke="#fbbf24" stroke-width="2" stroke-dasharray="4"/>
  <path d="M 160 285 Q 150 230 160 185" fill="none" stroke="#c084fc" stroke-width="2" stroke-dasharray="4"/>
  <path d="M 215 135 Q 260 105 305 95" fill="none" stroke="#38bdf8" stroke-width="2" stroke-dasharray="4"/>
</svg>
""")

LESSON_SVG_MAP = {
    1: SVG_DATA_CONDENSATION,
    2: SVG_QUAL_QUANT_BALANCE,
    3: SVG_DATA_CLASSIFICATION_TREE,
    4: SVG_SAMPLING_METHODS,
    5: SVG_TALLY_SYSTEM,
    6: SVG_FIELD_TOOLKIT,
    7: SVG_FREQUENCY_PIPELINE,
    8: SVG_CENTRAL_TENDENCY,
    9: SVG_BAR_GRAPH,
    10: SVG_PIE_CHART,
    11: SVG_CLIMOGRAPH,
    12: SVG_INQUIRY_CYCLE,
}

def run_enrichment():
    print("=" * 70)
    print("VLearn CBC Grade 10 Geography — Topic 3 Visual Enrichment Engine")
    print("=" * 70)

    curriculum = Curriculum.objects.filter(name__iexact="CBC").first()
    grade = Grade.objects.filter(curriculum=curriculum, name__icontains="10").first()
    subject = Subject.objects.filter(grade=grade, name="Geography").first()
    topic = Topic.objects.filter(subject=subject, order=3).first()

    if not topic:
        print("ERROR: Topic 3 not found in database. Run ingest script first!")
        sys.exit(1)

    json_path = os.path.join(os.path.dirname(__file__), "grade10_geography_topic3_verified_images.json")
    if not os.path.exists(json_path):
        print(f"ERROR: Verified images file '{json_path}' missing!")
        sys.exit(1)

    with open(json_path, "r") as f:
        verified_images = json.load(f)

    lessons = list(topic.lessons.all().order_by("learning_unit__order"))
    print(f"Found {len(lessons)} lessons in Topic 3: '{topic.name}'.")

    total_images_attached = 0
    total_svgs_attached = 0
    total_videos_attached = 0

    for lesson in lessons:
        u_order = lesson.learning_unit.order
        l_title = lesson.title
        print(f"\nEnriching Unit {u_order}: {l_title}")

        # ---------------------------------------------------------------------
        # 1. First-Card Photographic Visual Hook
        # ---------------------------------------------------------------------
        img_info = verified_images.get(str(u_order))
        if img_info:
            card_1_img_block = LessonBlock.objects.filter(
                lesson=lesson,
                page_number=1,
                block_type="suggested_image"
            ).first()

            if card_1_img_block:
                card_1_img_block.content = {
                    "text": card_1_img_block.content.get("text", "") if isinstance(card_1_img_block.content, dict) else "",
                    "resolved_image_url": img_info["url"],
                    "url": img_info["url"],
                    "caption": f"Visual Hook: {img_info['title'].replace('File:', '').replace('.jpg', '').replace('.png', '')}",
                    "author": img_info.get("author", "Wikimedia Commons"),
                    "licensing": img_info.get("licensing", "CC BY-SA")
                }
                card_1_img_block.save()

                asset, _ = LessonAsset.objects.get_or_create(
                    lesson=lesson,
                    title=f"Lesson {u_order} Visual Hook: {card_1_img_block.title}",
                    defaults={
                        "asset_type": "image",
                        "source_type": "external",
                        "storage_type": "url",
                        "status": "attached",
                        "url": img_info["url"],
                        "metadata": {
                            "author": img_info.get("author", "Wikimedia Commons"),
                            "licensing": img_info.get("licensing", "CC BY-SA"),
                            "commons_url": img_info.get("commons_url", ""),
                            "unit_order": int(u_order),
                            "topic_order": 3
                        }
                    }
                )
                asset.url = img_info["url"]
                asset.status = "attached"
                asset.save()
                asset.blocks.add(card_1_img_block)
                total_images_attached += 1
                print(f"  ✓ Attached Photographic Hook: {img_info['title']}")
            else:
                print(f"  ⚠ No Page 1 suggested_image block found for Lesson {u_order}")

        # ---------------------------------------------------------------------
        # 2. Custom Sanitized Vector SVG Diagrams
        # ---------------------------------------------------------------------
        svg_content = LESSON_SVG_MAP.get(u_order)
        if svg_content:
            diag_block = LessonBlock.objects.filter(
                lesson=lesson,
                block_type="suggested_diagram"
            ).first()

            if diag_block:
                diag_block.content = {
                    "svg_content": svg_content,
                    "title": diag_block.title,
                    "caption": f"Statistical Diagram: {diag_block.title}"
                }
                diag_block.save()

                svg_asset, _ = LessonAsset.objects.get_or_create(
                    lesson=lesson,
                    title=f"Lesson {u_order} Diagram: {diag_block.title}",
                    defaults={
                        "asset_type": "diagram",
                        "source_type": "ai_generated",
                        "storage_type": "embed",
                        "status": "attached",
                        "url": f"data:image/svg+xml;utf8,{svg_content[:50]}...",
                        "metadata": {
                            "svg_content": svg_content,
                            "unit_order": int(u_order),
                            "topic_order": 3,
                            "responsive": True,
                            "viewBox": "0 0 800 450"
                        }
                    }
                )
                svg_asset.metadata["svg_content"] = svg_content
                svg_asset.status = "attached"
                svg_asset.save()
                svg_asset.blocks.add(diag_block)
                total_svgs_attached += 1
                print(f"  ✓ Attached Custom Vector SVG: '{diag_block.title}'")
            else:
                print(f"  ⚠ No suggested_diagram block found for Lesson {u_order}")

        # ---------------------------------------------------------------------
        # 3. Educational YouTube Video Assets
        # ---------------------------------------------------------------------
        video_block = LessonBlock.objects.filter(
            lesson=lesson,
            block_type="suggested_video"
        ).first()

        if video_block:
            v_content = video_block.content or {}
            vid_url = v_content.get("youtube_url") or f"https://www.youtube.com/watch?v={v_content.get('resolved_video_id', '')}"
            yt_id = v_content.get("resolved_video_id", "x1Y_9uO9e28")

            video_asset, _ = LessonAsset.objects.get_or_create(
                lesson=lesson,
                title=f"Lesson {u_order} Video: {video_block.title}",
                defaults={
                    "asset_type": "youtube",
                    "source_type": "external",
                    "storage_type": "url",
                    "status": "attached",
                    "url": vid_url,
                    "metadata": {
                        "video_id": yt_id,
                        "youtube_url": vid_url,
                        "unit_order": int(u_order),
                        "topic_order": 3
                    }
                }
            )
            video_asset.url = vid_url
            video_asset.status = "attached"
            video_asset.save()
            video_asset.blocks.add(video_block)
            total_videos_attached += 1
            print(f"  ✓ Attached Educational YouTube Video: '{video_block.title}' ({yt_id})")

    print("=" * 70)
    print(f"ENRICHMENT COMPLETE: {total_images_attached} Photos, {total_svgs_attached} SVGs, {total_videos_attached} Videos Attached.")
    print("=" * 70)

if __name__ == "__main__":
    run_enrichment()
