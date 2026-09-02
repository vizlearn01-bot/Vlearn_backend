"""
VLearn CBC Grade 10 English — Topic 1: Listening and Speaking
Direct Programmatic Ingestion Engine for Lessons 1, 2, and 3

Grade: Grade 10 (Grade ID: 5)
Subject: English
Topic 1: Listening and Speaking (Order: 1)
Lessons:
  1. Etiquette in Everyday and Service Encounters
  2. Pronunciation: Target Sounds and Minimal Pairs
  3. Extensive Listening for Gist and Main Ideas

Usage:
  ./venv/bin/python curriculum/ingest_cbc_grade10_english_topic1_lessons1_3.py
"""

import os
import sys
import re
import json
import xml.etree.ElementTree as ET
import django
from django.db import transaction

# Setup django environment
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "Nexus_backend.settings")
django.setup()

from curriculum.models import (
    Grade, Subject, Topic, LearningUnit, Lesson, LessonBlock, LessonAsset
)

def clean_text(raw_str: str) -> str:
    """Normalize text, fix bullet indentation, and remove bracket citations."""
    if not isinstance(raw_str, str):
        return raw_str
    text = re.sub(r'\[(?:\d+|image_\d+|S\d+.*?|[\d,\s]{2,})\]', '', raw_str)
    text = re.sub(r'^[ \t]*[•\u2022][ \t]*', '- ', text, flags=re.MULTILINE)
    text = re.sub(r'([^\n])[ \t]+[•\u2022][ \t]+', r'\1\n- ', text)
    return text.strip()

def clean_dict(data):
    """Recursively clean strings within nested dicts and lists."""
    if isinstance(data, str):
        return clean_text(data)
    elif isinstance(data, dict):
        return {k: clean_dict(v) for k, v in data.items()}
    elif isinstance(data, list):
        return [clean_dict(item) for item in data]
    return data

def validate_svg(svg_code: str, name: str = "SVG") -> str:
    """Validate SVG XML structure."""
    try:
        ET.fromstring(svg_code)
        return svg_code.strip()
    except ET.ParseError as e:
        raise ValueError(f"Invalid XML syntax in {name}: {e}")

# =============================================================================
# HIGH-FIDELITY RESPONSIVE SVGS (DARK THEME 960x520)
# =============================================================================

SVG_SERVICE_ETIQUETTE = validate_svg("""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 960 520" width="100%" height="100%">
  <defs>
    <linearGradient id="bgGrad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#0f172a" />
      <stop offset="100%" stop-color="#1e293b" />
    </linearGradient>
    <linearGradient id="rudeGrad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#3b151e" />
      <stop offset="100%" stop-color="#1f1118" />
    </linearGradient>
    <linearGradient id="politeGrad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#0e392b" />
      <stop offset="100%" stop-color="#0f2922" />
    </linearGradient>
    <linearGradient id="arrowGrad" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#f43f5e" />
      <stop offset="50%" stop-color="#38bdf8" />
      <stop offset="100%" stop-color="#10b981" />
    </linearGradient>
    <filter id="shadow" x="-5%" y="-5%" width="110%" height="110%">
      <feDropShadow dx="0" dy="4" stdDeviation="6" flood-color="#000000" flood-opacity="0.4"/>
    </filter>
  </defs>

  <!-- Canvas Background -->
  <rect width="960" height="520" rx="16" fill="url(#bgGrad)" stroke="#334155" stroke-width="2"/>

  <!-- Title Header -->
  <g transform="translate(480, 42)" text-anchor="middle">
    <text font-family="system-ui, -apple-system, sans-serif" font-size="22" font-weight="800" fill="#38bdf8" letter-spacing="0.5">Everyday &amp; Service Encounter Communication Matrix</text>
    <text y="24" font-family="system-ui, -apple-system, sans-serif" font-size="13" fill="#94a3b8">The Politeness Spectrum: From Direct Demands to Professional Formal Register</text>
  </g>

  <!-- Left Card: Informal / Direct Demands (To Avoid in Service) -->
  <g transform="translate(40, 95)" filter="url(#shadow)">
    <rect width="410" height="385" rx="12" fill="url(#rudeGrad)" stroke="#f43f5e" stroke-width="2"/>
    <rect width="410" height="42" rx="12" fill="#be123c"/>
    <rect y="30" width="410" height="12" fill="#be123c"/>
    <text x="205" y="27" font-family="system-ui, sans-serif" font-size="15" font-weight="700" fill="#ffffff" text-anchor="middle">⚠️ Direct / Blunt Register (Avoid in Service)</text>

    <!-- Point 1 -->
    <g transform="translate(20, 65)">
      <rect width="370" height="60" rx="8" fill="#181116" stroke="#e11d48" stroke-width="1"/>
      <text x="15" y="24" font-family="system-ui, sans-serif" font-size="12" font-weight="700" fill="#f87171">Imperative Demand:</text>
      <text x="15" y="44" font-family="system-ui, sans-serif" font-size="13" fill="#fda4af">&quot;Give me my room key right now.&quot;</text>
    </g>

    <!-- Point 2 -->
    <g transform="translate(20, 140)">
      <rect width="370" height="60" rx="8" fill="#181116" stroke="#e11d48" stroke-width="1"/>
      <text x="15" y="24" font-family="system-ui, sans-serif" font-size="12" font-weight="700" fill="#f87171">Childish Demand:</text>
      <text x="15" y="44" font-family="system-ui, sans-serif" font-size="13" fill="#fda4af">&quot;I want to talk to your manager.&quot;</text>
    </g>

    <!-- Point 3 -->
    <g transform="translate(20, 215)">
      <rect width="370" height="60" rx="8" fill="#181116" stroke="#e11d48" stroke-width="1"/>
      <text x="15" y="24" font-family="system-ui, sans-serif" font-size="12" font-weight="700" fill="#f87171">Blunt Interrogation:</text>
      <text x="15" y="44" font-family="system-ui, sans-serif" font-size="13" fill="#fda4af">&quot;Tell me where the washroom is.&quot;</text>
    </g>

    <!-- Impact Note -->
    <g transform="translate(20, 290)">
      <rect width="370" height="75" rx="8" fill="#0f172a" stroke="#475569" stroke-width="1"/>
      <text x="15" y="24" font-family="system-ui, sans-serif" font-size="11" font-weight="700" fill="#f43f5e">CONSEQUENCES &amp; TONE AUDIT:</text>
      <text x="15" y="44" font-family="system-ui, sans-serif" font-size="11.5" fill="#cbd5e1">• Creates defensiveness, friction, and tension</text>
      <text x="15" y="62" font-family="system-ui, sans-serif" font-size="11.5" fill="#cbd5e1">• Violates turn-taking and service social contract</text>
    </g>
  </g>

  <!-- Right Card: Professional Polite Register (Recommended) -->
  <g transform="translate(510, 95)" filter="url(#shadow)">
    <rect width="410" height="385" rx="12" fill="url(#politeGrad)" stroke="#10b981" stroke-width="2"/>
    <rect width="410" height="42" rx="12" fill="#047857"/>
    <rect y="30" width="410" height="12" fill="#047857"/>
    <text x="205" y="27" font-family="system-ui, sans-serif" font-size="15" font-weight="700" fill="#ffffff" text-anchor="middle">✨ Professional Polite Modals (Formal Register)</text>

    <!-- Point 1 -->
    <g transform="translate(20, 65)">
      <rect width="370" height="60" rx="8" fill="#0c231d" stroke="#059669" stroke-width="1"/>
      <text x="15" y="24" font-family="system-ui, sans-serif" font-size="12" font-weight="700" fill="#34d399">Modals &quot;Could / Would&quot; (Possibility &amp; Willingness):</text>
      <text x="15" y="44" font-family="system-ui, sans-serif" font-size="13" fill="#a7f3d0">&quot;Could you please help me check in?&quot;</text>
    </g>

    <!-- Point 2 -->
    <g transform="translate(20, 140)">
      <rect width="370" height="60" rx="8" fill="#0c231d" stroke="#059669" stroke-width="1"/>
      <text x="15" y="24" font-family="system-ui, sans-serif" font-size="12" font-weight="700" fill="#34d399">Conditional &quot;Would like&quot; &amp; Modal &quot;May&quot;:</text>
      <text x="15" y="44" font-family="system-ui, sans-serif" font-size="13" fill="#a7f3d0">&quot;May I please speak with the supervisor?&quot;</text>
    </g>

    <!-- Point 3 -->
    <g transform="translate(20, 215)">
      <rect width="370" height="60" rx="8" fill="#0c231d" stroke="#059669" stroke-width="1"/>
      <text x="15" y="24" font-family="system-ui, sans-serif" font-size="12" font-weight="700" fill="#34d399">Polite Softener &quot;Would you mind...&quot;:</text>
      <text x="15" y="44" font-family="system-ui, sans-serif" font-size="13" fill="#a7f3d0">&quot;Would you mind directing me to the restroom?&quot;</text>
    </g>

    <!-- Impact Note -->
    <g transform="translate(20, 290)">
      <rect width="370" height="75" rx="8" fill="#0f172a" stroke="#475569" stroke-width="1"/>
      <text x="15" y="24" font-family="system-ui, sans-serif" font-size="11" font-weight="700" fill="#10b981">BENEFITS &amp; PROFESSIONAL OUTCOMES:</text>
      <text x="15" y="44" font-family="system-ui, sans-serif" font-size="11.5" fill="#cbd5e1">• Inspires cooperation, warmth, and fast resolution</text>
      <text x="15" y="62" font-family="system-ui, sans-serif" font-size="11.5" fill="#cbd5e1">• Demonstrates mutual respect, empathy, and poise</text>
    </g>
  </g>

  <!-- Central Bridge Transformation Arrow -->
  <g transform="translate(450, 240)">
    <circle cx="30" cy="30" r="26" fill="#0f172a" stroke="#38bdf8" stroke-width="2"/>
    <path d="M 18 30 L 38 30 M 30 22 L 38 30 L 30 38" stroke="#38bdf8" stroke-width="3" stroke-linecap="round" stroke-linejoin="round" fill="none"/>
  </g>
</svg>""", "SVG_SERVICE_ETIQUETTE")

SVG_PRONUNCIATION_PAIRS = validate_svg("""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 960 520" width="100%" height="100%">
  <defs>
    <linearGradient id="bg2Grad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#090d16" />
      <stop offset="100%" stop-color="#1e1b4b" />
    </linearGradient>
    <linearGradient id="shortGrad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#1e1b4b" />
      <stop offset="100%" stop-color="#312e81" />
    </linearGradient>
    <linearGradient id="longGrad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#064e3b" />
      <stop offset="100%" stop-color="#065f46" />
    </linearGradient>
    <filter id="glow" x="-10%" y="-10%" width="120%" height="120%">
      <feDropShadow dx="0" dy="4" stdDeviation="6" flood-color="#000" flood-opacity="0.5"/>
    </filter>
  </defs>

  <!-- Canvas Background -->
  <rect width="960" height="520" rx="16" fill="url(#bg2Grad)" stroke="#312e81" stroke-width="2"/>

  <!-- Title Header -->
  <g transform="translate(480, 40)" text-anchor="middle">
    <text font-family="system-ui, -apple-system, sans-serif" font-size="22" font-weight="800" fill="#a5b4fc" letter-spacing="0.5">Vowel Articulation Anatomy: /ɒ/ vs /ɔː/</text>
    <text y="24" font-family="system-ui, -apple-system, sans-serif" font-size="13" fill="#cbd5e1">Acoustic Discrimination, Lip Geometry &amp; Minimal Pair Contrasts</text>
  </g>

  <!-- Left Column: Short Vowel /ɒ/ -->
  <g transform="translate(40, 85)" filter="url(#glow)">
    <rect width="410" height="395" rx="12" fill="url(#shortGrad)" stroke="#818cf8" stroke-width="2"/>
    <rect width="410" height="42" rx="12" fill="#4338ca"/>
    <rect y="30" width="410" height="12" fill="#4338ca"/>
    <text x="205" y="27" font-family="system-ui, sans-serif" font-size="16" font-weight="800" fill="#ffffff" text-anchor="middle">Short Vowel: /ɒ/ (Open Back Rounded)</text>

    <!-- Articulation Diagram Box -->
    <g transform="translate(20, 60)">
      <rect width="370" height="140" rx="8" fill="#0f172a" stroke="#6366f1" stroke-width="1"/>
      <!-- Lip Geometry Visualization -->
      <g transform="translate(30, 20)">
        <ellipse cx="40" cy="50" rx="36" ry="42" fill="#1e1b4b" stroke="#818cf8" stroke-width="2.5"/>
        <ellipse cx="40" cy="50" rx="20" ry="26" fill="#0f172a" stroke="#c7d2fe" stroke-width="1.5" stroke-dasharray="3,3"/>
        <text x="40" y="112" font-family="system-ui, sans-serif" font-size="11" font-weight="700" fill="#818cf8" text-anchor="middle">Open Jaw (Low)</text>
      </g>
      <g transform="translate(130, 25)">
        <text font-family="system-ui, sans-serif" font-size="12" font-weight="700" fill="#c7d2fe">• Jaw:</text>
        <text x="45" font-family="system-ui, sans-serif" font-size="12" fill="#e0e7ff">Dropped low, wide opening</text>
        <text y="24" font-family="system-ui, sans-serif" font-size="12" font-weight="700" fill="#c7d2fe">• Tongue:</text>
        <text x="65" y="24" font-family="system-ui, sans-serif" font-size="12" fill="#e0e7ff">Low / flat at back</text>
        <text y="48" font-family="system-ui, sans-serif" font-size="12" font-weight="700" fill="#c7d2fe">• Lips:</text>
        <text x="45" y="48" font-family="system-ui, sans-serif" font-size="12" fill="#e0e7ff">Slightly rounded, relaxed</text>
        <text y="72" font-family="system-ui, sans-serif" font-size="12" font-weight="700" fill="#c7d2fe">• Duration:</text>
        <text x="68" y="72" font-family="system-ui, sans-serif" font-size="12" fill="#fcd34d">Short acoustic pulse (⚡)</text>
      </g>
    </g>

    <!-- Word Bank -->
    <g transform="translate(20, 215)">
      <rect width="370" height="160" rx="8" fill="#0f172a" stroke="#475569" stroke-width="1"/>
      <text x="15" y="22" font-family="system-ui, sans-serif" font-size="11" font-weight="700" fill="#818cf8">STANDARD TARGET EXAMPLES:</text>
      <text x="25" y="50" font-family="system-ui, sans-serif" font-size="14" font-weight="700" fill="#ffffff">cot <tspan font-weight="normal" fill="#94a3b8">(/kɒt/ — small folding bed)</tspan></text>
      <text x="25" y="76" font-family="system-ui, sans-serif" font-size="14" font-weight="700" fill="#ffffff">pot <tspan font-weight="normal" fill="#94a3b8">(/pɒt/ — cooking vessel)</tspan></text>
      <text x="25" y="102" font-family="system-ui, sans-serif" font-size="14" font-weight="700" fill="#ffffff">not <tspan font-weight="normal" fill="#94a3b8">(/nɒt/ — negative particle)</tspan></text>
      <text x="25" y="128" font-family="system-ui, sans-serif" font-size="14" font-weight="700" fill="#ffffff">spot <tspan font-weight="normal" fill="#94a3b8">(/spɒt/ — specific location)</tspan></text>
      <text x="25" y="150" font-family="system-ui, sans-serif" font-size="14" font-weight="700" fill="#ffffff">don <tspan font-weight="normal" fill="#94a3b8">(/dɒn/ — to put on clothes)</tspan></text>
    </g>
  </g>

  <!-- Right Column: Long Vowel /ɔː/ -->
  <g transform="translate(510, 85)" filter="url(#glow)">
    <rect width="410" height="395" rx="12" fill="url(#longGrad)" stroke="#34d399" stroke-width="2"/>
    <rect width="410" height="42" rx="12" fill="#059669"/>
    <rect y="30" width="410" height="12" fill="#059669"/>
    <text x="205" y="27" font-family="system-ui, sans-serif" font-size="16" font-weight="800" fill="#ffffff" text-anchor="middle">Long Vowel: /ɔː/ (Mid-Low Back Rounded)</text>

    <!-- Articulation Diagram Box -->
    <g transform="translate(20, 60)">
      <rect width="370" height="140" rx="8" fill="#0f172a" stroke="#059669" stroke-width="1"/>
      <!-- Lip Geometry Visualization -->
      <g transform="translate(30, 20)">
        <ellipse cx="40" cy="50" rx="26" ry="26" fill="#064e3b" stroke="#34d399" stroke-width="3"/>
        <ellipse cx="40" cy="50" rx="12" ry="12" fill="#0f172a" stroke="#6ee7b7" stroke-width="1.5" stroke-dasharray="3,3"/>
        <text x="40" y="112" font-family="system-ui, sans-serif" font-size="11" font-weight="700" fill="#34d399" text-anchor="middle">Protruded / Pursed</text>
      </g>
      <g transform="translate(130, 25)">
        <text font-family="system-ui, sans-serif" font-size="12" font-weight="700" fill="#a7f3d0">• Jaw:</text>
        <text x="45" font-family="system-ui, sans-serif" font-size="12" fill="#ecfdf5">Mid-open, closer than /ɒ/</text>
        <text y="24" font-family="system-ui, sans-serif" font-size="12" font-weight="700" fill="#a7f3d0">• Tongue:</text>
        <text x="65" y="24" font-family="system-ui, sans-serif" font-size="12" fill="#ecfdf5">Raised higher at back</text>
        <text y="48" font-family="system-ui, sans-serif" font-size="12" font-weight="700" fill="#a7f3d0">• Lips:</text>
        <text x="45" y="48" font-family="system-ui, sans-serif" font-size="12" fill="#ecfdf5">Firm circle, pushed forward</text>
        <text y="72" font-family="system-ui, sans-serif" font-size="12" font-weight="700" fill="#a7f3d0">• Duration:</text>
        <text x="68" y="72" font-family="system-ui, sans-serif" font-size="12" fill="#fcd34d">Sustained tone (〰️〰️)</text>
      </g>
    </g>

    <!-- Word Bank -->
    <g transform="translate(20, 215)">
      <rect width="370" height="160" rx="8" fill="#0f172a" stroke="#475569" stroke-width="1"/>
      <text x="15" y="22" font-family="system-ui, sans-serif" font-size="11" font-weight="700" fill="#34d399">CONTRASTIVE MINIMAL PAIRS:</text>
      <text x="25" y="50" font-family="system-ui, sans-serif" font-size="14" font-weight="700" fill="#ffffff">caught <tspan font-weight="normal" fill="#94a3b8">(/kɔːt/ — past of catch)</tspan></text>
      <text x="25" y="76" font-family="system-ui, sans-serif" font-size="14" font-weight="700" fill="#ffffff">port <tspan font-weight="normal" fill="#94a3b8">(/pɔːt/ — harbor / seaport)</tspan></text>
      <text x="25" y="102" font-family="system-ui, sans-serif" font-size="14" font-weight="700" fill="#ffffff">naught <tspan font-weight="normal" fill="#94a3b8">(/nɔːt/ — nothing / zero)</tspan></text>
      <text x="25" y="128" font-family="system-ui, sans-serif" font-size="14" font-weight="700" fill="#ffffff">sport <tspan font-weight="normal" fill="#94a3b8">(/spɔːt/ — athletic game)</tspan></text>
      <text x="25" y="150" font-family="system-ui, sans-serif" font-size="14" font-weight="700" fill="#ffffff">dawn <tspan font-weight="normal" fill="#94a3b8">(/dɔːn/ — early morning sunrise)</tspan></text>
    </g>
  </g>
</svg>""", "SVG_PRONUNCIATION_PAIRS")

SVG_LISTENING_GIST_PYRAMID = validate_svg("""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 960 520" width="100%" height="100%">
  <defs>
    <linearGradient id="bg3Grad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#0f172a" />
      <stop offset="100%" stop-color="#1e293b" />
    </linearGradient>
    <linearGradient id="apexGrad" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#f59e0b" />
      <stop offset="100%" stop-color="#fbbf24" />
    </linearGradient>
    <linearGradient id="midGrad" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#0284c7" />
      <stop offset="100%" stop-color="#38bdf8" />
    </linearGradient>
    <linearGradient id="baseGrad" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#334155" />
      <stop offset="100%" stop-color="#475569" />
    </linearGradient>
    <filter id="pShadow" x="-5%" y="-5%" width="110%" height="110%">
      <feDropShadow dx="0" dy="4" stdDeviation="6" flood-color="#000" flood-opacity="0.4"/>
    </filter>
  </defs>

  <!-- Canvas Background -->
  <rect width="960" height="520" rx="16" fill="url(#bg3Grad)" stroke="#334155" stroke-width="2"/>

  <!-- Title Header -->
  <g transform="translate(480, 38)" text-anchor="middle">
    <text font-family="system-ui, -apple-system, sans-serif" font-size="22" font-weight="800" fill="#38bdf8" letter-spacing="0.5">The Extensive Listening Comprehension Hierarchy</text>
    <text y="24" font-family="system-ui, -apple-system, sans-serif" font-size="13" fill="#94a3b8">Filtering Global Gist &amp; Core Purpose from Supporting Details &amp; Acoustic Noise</text>
  </g>

  <!-- Left: Comprehension Pyramid Visual -->
  <g transform="translate(50, 90)" filter="url(#pShadow)">
    <!-- Level 1: Apex (Gist & Global Essence) -->
    <polygon points="210,10 80,100 340,100" fill="url(#apexGrad)" stroke="#d97706" stroke-width="2"/>
    <text x="210" y="65" font-family="system-ui, sans-serif" font-size="15" font-weight="900" fill="#78350f" text-anchor="middle">1. GIST / CORE ESSENCE</text>
    <text x="210" y="82" font-family="system-ui, sans-serif" font-size="11" font-weight="700" fill="#92400e" text-anchor="middle">&quot;What is the big picture?&quot;</text>

    <!-- Level 2: Middle (Main Ideas & Key Points) -->
    <polygon points="80,110 340,110 390,220 30,220" fill="url(#midGrad)" stroke="#0369a1" stroke-width="2"/>
    <text x="210" y="155" font-family="system-ui, sans-serif" font-size="15" font-weight="800" fill="#082f49" text-anchor="middle">2. PRIMARY MAIN IDEAS</text>
    <text x="210" y="175" font-family="system-ui, sans-serif" font-size="11.5" font-weight="600" fill="#0c4a6e" text-anchor="middle">Major thematic arguments &amp; 5Ws</text>
    <text x="210" y="195" font-family="system-ui, sans-serif" font-size="10.5" fill="#e0f2fe" text-anchor="middle">(Who, What, Where, When, Why)</text>

    <!-- Level 3: Base (Supporting Details & Minor Facts) -->
    <polygon points="30,230 390,230 430,370 -10,370" fill="url(#baseGrad)" stroke="#64748b" stroke-width="2"/>
    <text x="210" y="275" font-family="system-ui, sans-serif" font-size="14" font-weight="700" fill="#f8fafc" text-anchor="middle">3. SUPPORTING DETAILS &amp; DATA</text>
    <text x="210" y="298" font-family="system-ui, sans-serif" font-size="11" fill="#cbd5e1" text-anchor="middle">Statistics, individual names, timestamps,</text>
    <text x="210" y="318" font-family="system-ui, sans-serif" font-size="11" fill="#cbd5e1" text-anchor="middle">minor anecdotes, illustrative examples</text>
    <text x="210" y="342" font-family="system-ui, sans-serif" font-size="10" font-style="italic" fill="#94a3b8" text-anchor="middle">(Do not get blocked by unknown single words!)</text>
  </g>

  <!-- Right: Cognitive Listening Strategy Steps -->
  <g transform="translate(510, 95)">
    <!-- Strategy Step 1 -->
    <g transform="translate(0, 0)">
      <rect width="400" height="85" rx="10" fill="#1e293b" stroke="#f59e0b" stroke-width="1.5"/>
      <circle cx="30" cy="42" r="16" fill="#f59e0b"/>
      <text x="30" y="47" font-family="system-ui, sans-serif" font-size="14" font-weight="bold" fill="#78350f" text-anchor="middle">1</text>
      <text x="60" y="28" font-family="system-ui, sans-serif" font-size="13" font-weight="700" fill="#fbbf24">Relax &amp; Avoid Cognitive Freezing</text>
      <text x="60" y="48" font-family="system-ui, sans-serif" font-size="11.5" fill="#cbd5e1">Do not panic over unfamiliar vocabulary words.</text>
      <text x="60" y="66" font-family="system-ui, sans-serif" font-size="11" fill="#94a3b8">Let minor gaps pass and maintain continuous attention.</text>
    </g>

    <!-- Strategy Step 2 -->
    <g transform="translate(0, 98)">
      <rect width="400" height="85" rx="10" fill="#1e293b" stroke="#38bdf8" stroke-width="1.5"/>
      <circle cx="30" cy="42" r="16" fill="#38bdf8"/>
      <text x="30" y="47" font-family="system-ui, sans-serif" font-size="14" font-weight="bold" fill="#082f49" text-anchor="middle">2</text>
      <text x="60" y="28" font-family="system-ui, sans-serif" font-size="13" font-weight="700" fill="#38bdf8">Track Content Words &amp; Stress Patterns</text>
      <text x="60" y="48" font-family="system-ui, sans-serif" font-size="11.5" fill="#cbd5e1">Listen for repeated nouns, main verbs, and adjectives.</text>
      <text x="60" y="66" font-family="system-ui, sans-serif" font-size="11" fill="#94a3b8">English speakers naturally stress message-bearing words.</text>
    </g>

    <!-- Strategy Step 3 -->
    <g transform="translate(0, 196)">
      <rect width="400" height="85" rx="10" fill="#1e293b" stroke="#10b981" stroke-width="1.5"/>
      <circle cx="30" cy="42" r="16" fill="#10b981"/>
      <text x="30" y="47" font-family="system-ui, sans-serif" font-size="14" font-weight="bold" fill="#064e3b" text-anchor="middle">3</text>
      <text x="60" y="28" font-family="system-ui, sans-serif" font-size="13" font-weight="700" fill="#34d399">Synthesize 5 Ws into 1-Sentence Gist</text>
      <text x="60" y="48" font-family="system-ui, sans-serif" font-size="11.5" fill="#cbd5e1">Synthesize: Who is speaking? What happened? Why?</text>
      <text x="60" y="66" font-family="system-ui, sans-serif" font-size="11" fill="#94a3b8">Example: &quot;Athletics postponed due to heavy rainfall.&quot;</text>
    </g>

    <!-- Golden Rule Box -->
    <g transform="translate(0, 294)">
      <rect width="400" height="80" rx="10" fill="#0f172a" stroke="#a855f7" stroke-width="1.5"/>
      <text x="20" y="26" font-family="system-ui, sans-serif" font-size="11" font-weight="700" fill="#c084fc">KEY COGNITIVE DISTINCTION:</text>
      <text x="20" y="46" font-family="system-ui, sans-serif" font-size="12" fill="#e9d5ff">Main Idea = The umbrella purpose of the text.</text>
      <text x="20" y="64" font-family="system-ui, sans-serif" font-size="12" fill="#94a3b8">Supporting Detail = The bricks and mortar holding it up.</text>
    </g>
  </g>
</svg>""", "SVG_LISTENING_GIST_PYRAMID")

# =============================================================================
# CURRICULUM LESSON STRUCTURES (LESSONS 1, 2, AND 3)
# =============================================================================

LESSONS_DATA = [
    # -------------------------------------------------------------------------
    # LESSON 1: Etiquette in Everyday and Service Encounters
    # -------------------------------------------------------------------------
    {
        "unit_order": 1,
        "unit_name": "Etiquette in Everyday and Service Encounters",
        "unit_description": "Mastering formal registers, polite modal structures (could, would, may), cooperative turn-taking, and professional telephone etiquette in everyday and service situations.",
        "lesson_title": "Etiquette in Everyday and Service Encounters",
        "pages": [
            # Page 1: Discovery & Objectives (Learning goals, Scenario spark)
            {
                "page_number": 1,
                "page_title": "Discovery & Objectives",
                "blocks": [
                    {
                        "block_type": "suggested_image",
                        "component_type": "suggested_image",
                        "title": "Hospitality and Service Counter Encounter",
                        "content": {
                            "text": "A professional hotel reception desk setting demonstrating courteous greetings, formal registers, and polite customer service interactions.",
                            "url": "https://upload.wikimedia.org/wikipedia/commons/0/05/Entrance_lounge_and_reception_desks_of_the_Carlton_Hotel_Downtown_Core_Singapore.jpg",
                            "author": "Basile Morin / Wikimedia Commons",
                            "licensing": "CC BY-SA 4.0",
                            "commons_page_url": "https://commons.wikimedia.org/wiki/File:Entrance_lounge_and_reception_desks_of_the_Carlton_Hotel_Downtown_Core_Singapore.jpg"
                        },
                        "metadata": {
                            "caption": "A welcoming front desk reception area illustrating professional etiquette, respectful body language, and courtesy in public and service encounters.",
                            "role": "establishing_visual"
                        }
                    },
                    {
                        "block_type": "learning_goal",
                        "component_type": "learning_goal",
                        "title": "Lesson Objectives: Service & Everyday Etiquette",
                        "content": {
                            "text": (
                                "By the end of this lesson, you will be able to:\n\n"
                                "- Explain the concept of **etiquette** and formal register in everyday and service encounters\n"
                                "- Use **polite modals** (*could, would, may*) and softeners to convert direct commands into polite requests\n"
                                "- Apply cooperative **turn-taking**, active listening, and courteous phrasing during in-person and telephone interactions"
                            )
                        }
                    },
                    {
                        "block_type": "concept_explanation",
                        "component_type": "concept_explanation",
                        "title": "Scenario Spark: The Hotel Check-In Dilemma",
                        "content": {
                            "text": (
                                "Imagine arriving at a busy hotel reception desk after an exhausting 8-hour road trip. You are tired, hungry, and in a hurry to get to your room.\n\n"
                                "Consider these two ways to speak to the receptionist:\n\n"
                                "- **Option A:** You walk up, frown, and snap: *'Give me my room key. I am tired.'*\n"
                                "- **Option B:** You smile, establish eye contact, and say: *'Good afternoon. I have a reservation under the name John. Could you please help me check in?'*\n\n"
                                "Which approach produces a warm, helpful response and smooth service? Option B sets a cooperative tone immediately. Why? Because Option B uses a standard greeting, polite modal verbs, and respectful register rather than an aggressive imperative command."
                            )
                        }
                    }
                ]
            },

            # Page 2: Core Concepts & Terminology (Definition cards with structured terms)
            {
                "page_number": 2,
                "page_title": "Core Concepts & Terminology",
                "blocks": [
                    {
                        "block_type": "definition_card",
                        "component_type": "definition_card",
                        "title": "Core Linguistic Terminology",
                        "content": {
                            "term": "Etiquette",
                            "definition": "The customary code of polite, respectful behavior and conversational rules governing interactions in society, institutions, and professional environments."
                        }
                    },
                    {
                        "block_type": "definition_card",
                        "component_type": "definition_card",
                        "title": "Linguistic Register",
                        "content": {
                            "term": "Register",
                            "definition": "The degree of formality, style, and tone chosen in spoken or written language depending on the social context, audience, and relationship between speakers."
                        }
                    },
                    {
                        "block_type": "definition_card",
                        "component_type": "definition_card",
                        "title": "Conversational Turn-Taking",
                        "content": {
                            "term": "Turn-Taking",
                            "definition": "The orderly, cooperative exchange in spoken conversation where one participant speaks while the other actively listens, avoiding interruptions and respecting pauses."
                        }
                    },
                    {
                        "block_type": "concept_explanation",
                        "component_type": "concept_explanation",
                        "title": "The Grammar of Politeness: Modals & Softeners",
                        "content": {
                            "text": (
                                "In professional and service settings, direct imperative commands (*'Give me that', 'Come here'*) often sound rude and confrontational. English provides **polite modal auxiliaries** to soften language:\n\n"
                                "1. **Could (Possibility & Ability):** *'Could you please share the schedule with me?'* (Asks gently if the action is possible).\n"
                                "2. **Would (Willingness & Softening):** *'Would you mind checking my booking details?'* or *'I would like to order lunch, please.'* (Turns 'I want' into a gracious statement).\n"
                                "3. **May (Permission & Formal Request):** *'May I speak with the branch manager, please?'* (Highly formal and respectful)."
                            )
                        }
                    }
                ]
            },

            # Page 3: Model & Structured Analysis / Visual Diagram (Model dialogue, SVG diagram, Contrast table)
            {
                "page_number": 3,
                "page_title": "Model & Structured Analysis",
                "blocks": [
                    {
                        "block_type": "model_dialogue",
                        "component_type": "model_dialogue",
                        "title": "Model Encounter: At the Grand Plaza Reception Desk",
                        "content": {
                            "context": "A guest arrives at a hotel reception desk to check in and request a room upgrade.",
                            "dialogue": [
                                {"speaker": "Receptionist (Sarah)", "text": "Good morning! Welcome to the Grand Plaza Hotel. My name is Sarah. How may I assist you today?"},
                                {"speaker": "Guest (Leo)", "text": "Good morning, Sarah. I would like to check in, please. I have a reservation under the name Leo Mutua."},
                                {"speaker": "Receptionist (Sarah)", "text": "Thank you, Mr. Mutua. Could you please provide your booking confirmation number and a national identification card?"},
                                {"speaker": "Guest (Leo)", "text": "Certainly! Here is my ID. Would it be possible to get a quiet room facing the inner courtyard garden?"},
                                {"speaker": "Receptionist (Sarah)", "text": "Let me check our room allocations... Yes, we have a garden-facing deluxe room available on the second floor. Here is your keycard and Wi-Fi access code."},
                                {"speaker": "Guest (Leo)", "text": "Thank you so much for your assistance and kindness!"},
                                {"speaker": "Receptionist (Sarah)", "text": "It is my absolute pleasure, Mr. Mutua. Please let us know if you need anything else. Enjoy your stay!"}
                            ]
                        }
                    },
                    {
                        "block_type": "diagram",
                        "component_type": "diagram",
                        "title": "Everyday & Service Encounter Politeness Framework",
                        "content": {
                            "svg": SVG_SERVICE_ETIQUETTE,
                            "caption": "The Politeness Continuum: Comparing direct imperative commands with professional polite modals and cooperative turn-taking."
                        }
                    },
                    {
                        "block_type": "comparison_table",
                        "component_type": "comparison_table",
                        "title": "Register Contrast: Blunt Demands vs Polite Makeovers",
                        "content": {
                            "headers": ["Blunt Demand / Informal", "Polite Professional Makeover", "Underlying Modal / Tool"],
                            "rows": [
                                ["'Give me the menu.'", "'Could you please bring me the menu?'", "Modal 'Could' + 'please'"],
                                ["'I want a refund right now.'", "'I would appreciate it if you could look into a refund for this item.'", "Conditional 'Would' + softening verb"],
                                ["'Tell me where the manager is.'", "'May I please speak with the manager when they are available?'", "Permission modal 'May' + time softener"],
                                ["'Move your bag, I want to sit.'", "'Excuse me, would you mind if I took this seat?'", "Attention-getter + 'Would you mind'"]
                            ]
                        }
                    }
                ]
            },

            # Page 4: Media Integration & Listening Lab (YouTube video with pre-viewing and post-viewing tasks)
            {
                "page_number": 4,
                "page_title": "Media Integration & Listening Lab",
                "blocks": [
                    {
                        "block_type": "suggested_video",
                        "component_type": "suggested_video",
                        "title": "Professional Telephone & Service Etiquette Lab",
                        "content": {
                            "title": "Mastering Telephone Courtesy & Service Communication",
                            "youtube_id": "t0S9VyKypjs",
                            "url": "https://www.youtube.com/watch?v=t0S9VyKypjs",
                            "description": "An instructional guide illustrating professional telephone manners, greeting protocols, empathetic tone modulation, and active listening skills during customer service interactions."
                        }
                    },
                    {
                        "block_type": "listening_lab",
                        "component_type": "listening_lab",
                        "title": "Listening Comprehension & Acoustic Analysis Tasks",
                        "content": {
                            "pre_viewing_task": (
                                "**Pre-Viewing Objective**: Before playing the video clip, prepare a notepad. As you listen to the telephone agent, note down:\n\n"
                                "1. The exact formal greeting used in the opening 5 seconds.\n"
                                "2. At least three specific polite modal expressions (*could, would, may*) used to guide the caller.\n"
                                "3. How the speaker modulates their pitch and smiling tone when delivering difficult news."
                            ),
                            "post_viewing_discussion": (
                                "**Post-Viewing Analysis & Reflection**:\n\n"
                                "- **Voice Modulation**: Why does smiling while speaking on the phone noticeably alter the perceived warmth and resonance of your voice even though the caller cannot see your face?\n"
                                "- **Turn-Taking Etiquette**: What acoustic cue did the speaker use to signal that they were ready for the customer to speak without interrupting them?"
                            )
                        }
                    }
                ]
            },

            # Page 5: Common Mistakes & Guided Practice (Common mistakes, Guided exercises, Role-play prompt)
            {
                "page_number": 5,
                "page_title": "Common Mistakes & Guided Practice",
                "blocks": [
                    {
                        "block_type": "common_mistakes",
                        "component_type": "common_mistakes",
                        "title": "Frequent Pitfalls in Service Encounters",
                        "content": {
                            "mistakes": [
                                {
                                    "mistake": "Using 'I want...' or 'Give me...' in formal or customer service contexts.",
                                    "why_it_is_wrong": "It sounds demanding, entitled, and childish, triggering defensiveness in the other person.",
                                    "correction": "Replace 'I want' with 'I would like...' or 'Could I please have...'"
                                },
                                {
                                    "mistake": "Interrupting a customer or service provider mid-sentence.",
                                    "why_it_is_wrong": "Interrupting breaks the cooperative turn-taking cycle and signals a lack of respect and active listening.",
                                    "correction": "Wait for a natural 1-second pause before responding, or say 'Excuse me for interrupting, but...'"
                                },
                                {
                                    "mistake": "Using overly informal slang ('Hey man', 'Yo', 'Gimme that') with officials, elders, or clients.",
                                    "why_it_is_wrong": "It misjudges the communicative register and can be perceived as disrespectful or unprofessional.",
                                    "correction": "Adopt standard polite salutations: 'Good morning, Sir/Madam' or 'Hello, how may I help you?'"
                                }
                            ]
                        }
                    },
                    {
                        "block_type": "guided_practice",
                        "component_type": "guided_practice",
                        "title": "Guided Exercise: Polite Language Makeover",
                        "content": {
                            "instructions": "Transform the following direct demands into professional requests using the target modal provided:",
                            "exercises": [
                                {
                                    "prompt": "1. 'Give me the receipt for my purchase.' [Use: could]",
                                    "sample_answer": "Could you please provide me with the receipt for my purchase?"
                                },
                                {
                                    "prompt": "2. 'Tell me when the next bus to Nakuru leaves.' [Use: would mind]",
                                    "sample_answer": "Would you mind telling me what time the next bus to Nakuru departs?"
                                },
                                {
                                    "prompt": "3. 'I want to see the doctor right now.' [Use: may]",
                                    "sample_answer": "May I please see the doctor as soon as an opening is available?"
                                }
                            ]
                        }
                    },
                    {
                        "block_type": "role_play_activity",
                        "component_type": "role_play_activity",
                        "title": "Interactive Role-Play: Booking a Medical Appointment",
                        "content": {
                            "scenario": "You are calling an outpatient clinic to book an appointment with a dentist. Write a 6-turn dialogue between the Clinic Receptionist and yourself.",
                            "rubric_requirements": [
                                "Include a formal opening greeting and self-introduction",
                                "Use at least two different polite modals (*could, would, may*)",
                                "Demonstrate smooth turn-taking without aggressive demands",
                                "Conclude with a gracious closing appreciation ('Thank you for your assistance')"
                            ]
                        }
                    }
                ]
            },

            # Page 6: Knowledge Check & Summary (MCQ with full options and rich explanations, Key takeaway)
            {
                "page_number": 6,
                "page_title": "Knowledge Check & Summary",
                "blocks": [
                    {
                        "block_type": "knowledge_check",
                        "component_type": "knowledge_check",
                        "title": "Knowledge Check 1: Appropriate Service Encounter Register",
                        "content": {
                            "question": "A customer enters an electronics store and wants to know if a specific laptop model is currently in stock. Which of the following statements demonstrates the most appropriate polite register?",
                            "options": [
                                "A. 'Hey you, tell me if you have this laptop in the back.'",
                                "B. 'I want to buy this laptop immediately. Bring it out.'",
                                "C. 'Excuse me, could you please check if this laptop model is currently available in stock?'",
                                "D. 'Can you check the stock right now without making me wait?'"
                            ],
                            "correct": "C",
                            "explanation": "Option C is correct because it begins with a polite attention-getter ('Excuse me'), employs a courteous modal auxiliary ('could'), incorporates 'please', and maintains an objective, respectful formal register. Options A, B, and D use blunt imperatives and impatient demands."
                        }
                    },
                    {
                        "block_type": "knowledge_check",
                        "component_type": "knowledge_check",
                        "title": "Knowledge Check 2: Conversational Turn-Taking",
                        "content": {
                            "question": "During a customer service dispute over a billing error, what is the best turn-taking strategy to resolve the issue smoothly?",
                            "options": [
                                "A. Speak continuously over the representative so they cannot finish explaining the charges",
                                "B. Listen attentively without interrupting, wait for a natural pause, and state your concern politely using modal verbs",
                                "C. Immediately demand to speak with the highest executive using aggressive language",
                                "D. Hang up the phone abruptly whenever the agent takes a breath"
                            ],
                            "correct": "B",
                            "explanation": "Option B is correct because active listening and allowing the speaker to complete their turn maintains conversational cooperation and de-escalates conflict. Options A, C, and D violate turn-taking norms and damage effective communication."
                        }
                    },
                    {
                        "block_type": "key_takeaway",
                        "component_type": "key_takeaway",
                        "title": "Lesson 1 Summary: Core Takeaways",
                        "content": {
                            "text": (
                                "1. **Etiquette as Social Capital**: Courteous language and formal register build trust, de-escalate tension, and yield faster, friendlier service in everyday and professional life.\n"
                                "2. **The Modal Politeness Trio**: Replace demanding imperatives (*'I want', 'Give me'*) with polite modals (*'Could you please...', 'Would you mind...', 'May I...'*).\n"
                                "3. **Turn-Taking Mastery**: Practice active listening, observe vocal pauses, and avoid interrupting conversational partners.\n"
                                "4. **Telephone Poise**: Speak clearly, modulate your pitch, and maintain a pleasant, smiling tone to project warmth across distance."
                            )
                        }
                    }
                ]
            }
        ]
    },

    # -------------------------------------------------------------------------
    # LESSON 2: Pronunciation: Target Sounds and Minimal Pairs
    # -------------------------------------------------------------------------
    {
        "unit_order": 2,
        "unit_name": "Pronunciation: Target Sounds and Minimal Pairs",
        "unit_description": "Phonological discrimination and articulation of commonly confused English vowel sounds: short open back vowel /ɒ/ versus long back rounded vowel /ɔː/ using minimal pairs.",
        "lesson_title": "Pronunciation: Target Sounds and Minimal Pairs",
        "pages": [
            # Page 1: Discovery & Objectives
            {
                "page_number": 1,
                "page_title": "Discovery & Objectives",
                "blocks": [
                    {
                        "block_type": "suggested_image",
                        "component_type": "suggested_image",
                        "title": "Vocal Tract Anatomy and Speech Articulation",
                        "content": {
                            "text": "An anatomical sagittal diagram of the human vocal tract showing the lips, jaw, tongue positions, and vocal cords responsible for speech sound articulation.",
                            "url": "https://upload.wikimedia.org/wikipedia/commons/3/39/Neutral_Sagittal_Section.svg",
                            "author": "Wikimedia Commons",
                            "licensing": "CC BY-SA 3.0",
                            "commons_page_url": "https://commons.wikimedia.org/wiki/File:Neutral_Sagittal_Section.svg"
                        },
                        "metadata": {
                            "caption": "The human vocal tract: subtle changes in lip rounding, jaw height, and tongue positioning create distinct vowel phonemes.",
                            "role": "establishing_visual"
                        }
                    },
                    {
                        "block_type": "learning_goal",
                        "component_type": "learning_goal",
                        "title": "Lesson Objectives: Vowel Sounds /ɒ/ and /ɔː/",
                        "content": {
                            "text": (
                                "By the end of this lesson, you will be able to:\n\n"
                                "- Differentiate between the short open vowel **/ɒ/** and the long rounded vowel **/ɔː/** in listening and speech\n"
                                "- Explain the articulatory mechanics (lip rounding, jaw drop, tongue position) of both phonemes\n"
                                "- Accurately pronounce and discriminate **minimal pairs** (e.g., *cot* vs *caught*, *pot* vs *port*, *not* vs *naught*)"
                            )
                        }
                    },
                    {
                        "block_type": "concept_explanation",
                        "component_type": "concept_explanation",
                        "title": "Scenario Spark: The Case of the Cot and the Caught",
                        "content": {
                            "text": (
                                "Read these two sentences aloud to yourself:\n\n"
                                "1. *'The fisherman **caught** a giant fish in the river.'*\n"
                                "2. *'The baby is sleeping comfortably in the **cot**.'*\n\n"
                                "Did your lips and jaw move differently when pronouncing **caught** versus **cot**?\n\n"
                                "If you pronounce both words with the exact same vowel sound, your listener might wonder why a fisherman is putting fish into a baby cot! In English, changing a single vowel phoneme alters the entire meaning of a word. Today, we master the acoustic and anatomical contrast between **/ɒ/** and **/ɔː/**."
                            )
                        }
                    }
                ]
            },

            # Page 2: Core Concepts & Terminology
            {
                "page_number": 2,
                "page_title": "Core Concepts & Terminology",
                "blocks": [
                    {
                        "block_type": "definition_card",
                        "component_type": "definition_card",
                        "title": "Phonological Concepts",
                        "content": {
                            "term": "Phoneme",
                            "definition": "The smallest distinctive unit of sound in a language capable of distinguishing one word or meaning from another (e.g., /ɒ/ in 'spot' vs /ɔː/ in 'sport')."
                        }
                    },
                    {
                        "block_type": "definition_card",
                        "component_type": "definition_card",
                        "title": "Minimal Pair",
                        "content": {
                            "term": "Minimal Pair",
                            "definition": "Two words that differ by only a single phonological sound element in the same position, resulting in completely different meanings (e.g., 'pot' /pɒt/ and 'port' /pɔːt/)."
                        }
                    },
                    {
                        "block_type": "definition_card",
                        "component_type": "definition_card",
                        "title": "Speech Articulation",
                        "content": {
                            "term": "Articulation",
                            "definition": "The physical coordination and movement of the speech organs (lips, teeth, tongue, velum, jaw, and vocal cords) to shape airflow into distinct speech sounds."
                        }
                    },
                    {
                        "block_type": "concept_explanation",
                        "component_type": "concept_explanation",
                        "title": "Articulatory Mechanics: /ɒ/ vs /ɔː/",
                        "content": {
                            "text": (
                                "Let us examine the anatomical differences between these two sounds:\n\n"
                                "### 1. The Short Vowel: /ɒ/\n"
                                "- **Phonetic Description**: Short, open, back rounded vowel.\n"
                                "- **Mouth Mechanics**: Drop your jaw wide and low. Your tongue rests flat in the bottom back of your mouth. Your lips are slightly rounded but relaxed.\n"
                                "- **Acoustic Feel**: A rapid, crisp burst of sound (*hot, pot, clock, stop, lock*).\n\n"
                                "### 2. The Long Vowel: /ɔː/\n"
                                "- **Phonetic Description**: Long, mid-low, back rounded vowel.\n"
                                "- **Mouth Mechanics**: Close your jaw slightly higher than /ɒ/. Tightly round your lips forward into a firm circle (like preparing to whistle). The sound is held longer in duration.\n"
                                "- **Acoustic Feel**: A sustained, deep resonating sound (*caught, taught, port, dawn, law*)."
                            )
                        }
                    }
                ]
            },

            # Page 3: Model & Structured Analysis / Visual Diagram
            {
                "page_number": 3,
                "page_title": "Model & Structured Analysis",
                "blocks": [
                    {
                        "block_type": "diagram",
                        "component_type": "diagram",
                        "title": "Vowel Articulation Geometry: /ɒ/ vs /ɔː/",
                        "content": {
                            "svg": SVG_PRONUNCIATION_PAIRS,
                            "caption": "Anatomical comparison of lip rounding, jaw height, and duration between short /ɒ/ and long /ɔː/."
                        }
                    },
                    {
                        "block_type": "comparison_table",
                        "component_type": "comparison_table",
                        "title": "Comprehensive Minimal Pairs Master Matrix",
                        "content": {
                            "headers": ["Short Vowel /ɒ/ (Open, Short)", "Long Vowel /ɔː/ (Rounded, Long)", "Meaning Difference"],
                            "rows": [
                                ["cot (/kɒt/)", "caught (/kɔːt/)", "A portable bed vs. past tense of catch"],
                                ["pot (/pɒt/)", "port (/pɔːt/)", "A cooking vessel vs. a harbor for cargo ships"],
                                ["not (/nɒt/)", "naught (/nɔːt/)", "Negative adverb vs. nothing/zero"],
                                ["spot (/spɒt/)", "sport (/spɔːt/)", "A small mark/place vs. an athletic game"],
                                ["sock (/sɒk/)", "sought (/sɔːt/)", "Footwear vs. past tense of seek"],
                                ["don (/dɒn/)", "dawn (/dɔːn/)", "To put on clothing vs. daybreak sunrise"],
                                ["fox (/fɒks/)", "forks (/fɔːks/)", "Wild animal vs. dining utensils"],
                                ["shot (/ʃɒt/)", "short (/ʃɔːt/)", "Fired projectile vs. not tall/measuring little"]
                            ]
                        }
                    }
                ]
            },

            # Page 4: Media Integration & Listening Lab
            {
                "page_number": 4,
                "page_title": "Media Integration & Listening Lab",
                "blocks": [
                    {
                        "block_type": "suggested_video",
                        "component_type": "suggested_video",
                        "title": "Vowel Contrast Pronunciation Masterclass",
                        "content": {
                            "title": "Pronunciation Tutorial: Mastering /ɒ/ vs /ɔː/ Minimal Pairs",
                            "youtube_id": "EeToarNceeM",
                            "url": "https://www.youtube.com/watch?v=EeToarNceeM",
                            "description": "An interactive phonetic workshop demonstrating lip positioning, acoustic spectrogram differences, and practice drills for the /ɒ/ and /ɔː/ vowel sounds."
                        }
                    },
                    {
                        "block_type": "listening_lab",
                        "component_type": "listening_lab",
                        "title": "Audio Discrimination & Repetition Lab",
                        "content": {
                            "pre_viewing_task": (
                                "**Pre-Viewing Focus**: As you play the tutorial, observe the speaker's lips closely:\n\n"
                                "1. Watch how the jaw drops lower for /ɒ/ in words like *hot* and *spot*.\n"
                                "2. Watch how the lips push forward into a tight ring for /ɔː/ in words like *bought* and *port*.\n"
                                "3. Keep a tally of which words you find easiest to distinguish by ear alone."
                            ),
                            "post_viewing_discussion": (
                                "**Vocal Articulation Exercise**:\n\n"
                                "- Place your index finger and thumb lightly against your lips. Say *'pot'* then say *'port'*.\n"
                                "- Feel how your lips tighten and push outward into your fingers on *'port'*. Repeat this tactile check with *'cot'* vs *'caught'*."
                            )
                        }
                    }
                ]
            },

            # Page 5: Common Mistakes & Guided Practice
            {
                "page_number": 5,
                "page_title": "Common Mistakes & Guided Practice",
                "blocks": [
                    {
                        "block_type": "common_mistakes",
                        "component_type": "common_mistakes",
                        "title": "Pronunciation Pitfalls to Avoid",
                        "content": {
                            "mistakes": [
                                {
                                    "mistake": "Shortening the long /ɔː/ vowel, making 'sport' sound like 'spot'.",
                                    "why_it_is_wrong": "In English, vowel length is phonemic. Cutting /ɔː/ short changes the word into an entirely different concept.",
                                    "correction": "Hold the /ɔː/ sound for almost twice as long as /ɒ/ while keeping lips rounded: /spɔːt/."
                                },
                                {
                                    "mistake": "Pronouncing 'walk' (/wɔːk/) as 'work' (/wɜːk/) or 'wok' (/wɒk/).",
                                    "why_it_is_wrong": "Confusing central vowels with back rounded vowels leads to misunderstandings in travel and daily conversations.",
                                    "correction": "Round your lips firmly and use the back long vowel: /wɔːk/."
                                }
                            ]
                        }
                    },
                    {
                        "block_type": "guided_practice",
                        "component_type": "guided_practice",
                        "title": "Guided Exercise: Minimal Pair Discrimination",
                        "content": {
                            "instructions": "Select the correct word to complete each sentence based on the phonological clue provided:",
                            "exercises": [
                                {
                                    "prompt": "1. 'We set up our camping [cot / caught] inside the tent.' (Clue: uses the short open /ɒ/ sound)",
                                    "sample_answer": "cot"
                                },
                                {
                                    "prompt": "2. 'The cargo ship docked safely at the [pot / port] at sunrise.' (Clue: uses the long rounded /ɔː/ sound)",
                                    "sample_answer": "port"
                                },
                                {
                                    "prompt": "3. 'All our efforts came to [not / naught] when the rain started.' (Clue: uses the long rounded /ɔː/ sound meaning nothing)",
                                    "sample_answer": "naught"
                                },
                                {
                                    "prompt": "4. 'She woke up early at [don / dawn] to study.' (Clue: uses the long rounded /ɔː/ sound meaning sunrise)",
                                    "sample_answer": "dawn"
                                }
                            ]
                        }
                    },
                    {
                        "block_type": "tongue_twister_challenge",
                        "component_type": "tongue_twister_challenge",
                        "title": "Fluency Drill: Contrastive Tongue Twister",
                        "content": {
                            "drill_text": "“Paul bought a hot pot and brought it to the port at dawn.”",
                            "instructions": (
                                "1. First pass (Slow): Exaggerate your lip rounding on **Paul**, **bought**, **brought**, **port**, and **dawn** (/ɔː/), and drop your jaw open on **hot** and **pot** (/ɒ/).\n"
                                "2. Second pass (Medium speed): Maintain clear separation between the long and short vowels.\n"
                                "3. Third pass (Fast): Say the sentence three times rapidly without merging the vowel sounds!"
                            )
                        }
                    }
                ]
            },

            # Page 6: Knowledge Check & Summary
            {
                "page_number": 6,
                "page_title": "Knowledge Check & Summary",
                "blocks": [
                    {
                        "block_type": "knowledge_check",
                        "component_type": "knowledge_check",
                        "title": "Knowledge Check 1: Vowel Phoneme Identification",
                        "content": {
                            "question": "Which of the following words contains the long, back rounded vowel sound /ɔː/?",
                            "options": [
                                "A. dog",
                                "B. clock",
                                "C. stop",
                                "D. taught"
                            ],
                            "correct": "D",
                            "explanation": "Option D is correct because 'taught' (/tɔːt/) is pronounced with the long back rounded vowel /ɔː/. Options A (dog /dɒɡ/), B (clock /klɒk/), and C (stop /stɒp/) all feature the short open back vowel /ɒ/."
                        }
                    },
                    {
                        "block_type": "knowledge_check",
                        "component_type": "knowledge_check",
                        "title": "Knowledge Check 2: Articulatory Mechanics",
                        "content": {
                            "question": "What is the primary physical difference in lip shape and jaw position when transitioning from producing /ɒ/ (as in 'cot') to /ɔː/ (as in 'caught')?",
                            "options": [
                                "A. The lips spread into a wide smile and the tongue touches the front teeth",
                                "B. The lips become more tightly rounded and pursed forward while the sound is sustained longer",
                                "C. The jaw drops completely flat and the mouth opens wider",
                                "D. Airflow through the mouth is completely stopped by the vocal cords"
                            ],
                            "correct": "B",
                            "explanation": "Option B is correct because the production of the long vowel /ɔː/ requires tighter lip rounding (protrusion into an 'O' ring) and a slightly higher jaw elevation compared to the wide open jaw of /ɒ/."
                        }
                    },
                    {
                        "block_type": "key_takeaway",
                        "component_type": "key_takeaway",
                        "title": "Lesson 2 Summary: Core Takeaways",
                        "content": {
                            "text": (
                                "1. **Phonemic Precision Matters**: Vowel quality changes word identity. In English, /ɒ/ and /ɔː/ distinguish vital minimal pairs (*cot/caught, pot/port, spot/sport*).\n"
                                "2. **The Mechanics of /ɒ/**: Short duration, wide open jaw, relaxed open lips, flat tongue.\n"
                                "3. **The Mechanics of /ɔː/**: Longer duration, higher jaw, firmly rounded and pursed lips.\n"
                                "4. **Daily Practice**: Regular drilling with contrastive minimal pairs and tongue twisters builds strong phonological awareness and clear speech."
                            )
                        }
                    }
                ]
            }
        ]
    },

    # -------------------------------------------------------------------------
    # LESSON 3: Extensive Listening for Gist and Main Ideas
    # -------------------------------------------------------------------------
    {
        "unit_order": 3,
        "unit_name": "Extensive Listening for Gist and Main Ideas",
        "unit_description": "Developing global listening strategies to capture the core essence, main ideas, and purpose of spoken texts without getting bogged down by isolated unfamiliar words.",
        "lesson_title": "Extensive Listening for Gist and Main Ideas",
        "pages": [
            # Page 1: Discovery & Objectives
            {
                "page_number": 1,
                "page_title": "Discovery & Objectives",
                "blocks": [
                    {
                        "block_type": "suggested_image",
                        "component_type": "suggested_image",
                        "title": "Broadcast Listening and Spoken Message Processing",
                        "content": {
                            "text": "Students in a classroom engaged in active listening to a radio broadcast and speech presentation, capturing global information and key ideas.",
                            "url": "https://upload.wikimedia.org/wikipedia/commons/a/a3/Student_Listening_During_Study_Session.jpg",
                            "author": "Wikimedia Commons",
                            "licensing": "CC BY-SA 4.0",
                            "commons_page_url": "https://commons.wikimedia.org/wiki/File:Student_Listening_During_Study_Session.jpg"
                        },
                        "metadata": {
                            "caption": "Active listening in action: training the mind to distill overarching meaning and primary themes from continuous spoken discourse.",
                            "role": "establishing_visual"
                        }
                    },
                    {
                        "block_type": "learning_goal",
                        "component_type": "learning_goal",
                        "title": "Lesson Objectives: Extensive Listening for Gist",
                        "content": {
                            "text": (
                                "By the end of this lesson, you will be able to:\n\n"
                                "- Define **extensive listening** and distinguish the **gist / main idea** from supporting details\n"
                                "- Apply global listening techniques to overcome cognitive blockage caused by unfamiliar words\n"
                                "- Extract the core message of spoken announcements, interviews, and news reports in concise summary statements"
                            )
                        }
                    },
                    {
                        "block_type": "concept_explanation",
                        "component_type": "concept_explanation",
                        "title": "Scenario Spark: The Bustling Street Incident",
                        "content": {
                            "text": (
                                "Imagine your friend runs up to you after school, breathless and excited:\n\n"
                                "> *“Oh my goodness, you won't believe what happened! I was walking past the market on Kenyatta Avenue, right opposite the bakery around 3:30 PM, and suddenly there was this loud screech! A bicycle carrying three heavy crates of mangoes and oranges collided with a handcart! Fruit rolled everywhere across the tarmac. The vendors started yelling, but when they saw nobody was hurt, they both burst out laughing and everyone helped pack the fruit back into the crates!”*\n\n"
                                "When another friend asks you what happened, would you list every timestamp, fruit type, and street corner? No! You would say:\n\n"
                                "*“A bicycle collided with a fruit cart near the market, but nobody was hurt and the crowd helped clear up the fruit.”*\n\n"
                                "You just performed **listening for gist**! You captured the essential core meaning and disregarded unnecessary micro-details."
                            )
                        }
                    }
                ]
            },

            # Page 2: Core Concepts & Terminology
            {
                "page_number": 2,
                "page_title": "Core Concepts & Terminology",
                "blocks": [
                    {
                        "block_type": "definition_card",
                        "component_type": "definition_card",
                        "title": "Extensive Listening Concepts",
                        "content": {
                            "term": "Gist",
                            "definition": "The essential overarching meaning, central theme, or general purpose of a spoken speech, broadcast, or dialogue."
                        }
                    },
                    {
                        "block_type": "definition_card",
                        "component_type": "definition_card",
                        "title": "Main Idea vs Supporting Details",
                        "content": {
                            "term": "Main Idea",
                            "definition": "The primary thought, claim, or argument that the speaker intends to communicate to their audience."
                        }
                    },
                    {
                        "block_type": "definition_card",
                        "component_type": "definition_card",
                        "title": "Supporting Details",
                        "content": {
                            "term": "Supporting Details",
                            "definition": "Specific facts, statistics, names, timestamps, and secondary examples that reinforce, illustrate, or explain the main idea."
                        }
                    },
                    {
                        "block_type": "concept_explanation",
                        "component_type": "concept_explanation",
                        "title": "The Four Pillars of Global Listening Strategy",
                        "content": {
                            "text": (
                                "When listening to extensive spoken passages in English, expert listeners rely on four golden strategies:\n\n"
                                "1. **Overcome the 'Single-Word Panic Trap'**: If the speaker uses a word you do not recognize, do not stop to ponder it. Pausing your brain causes you to miss the next three sentences. Ignore the word and follow the flow of ideas.\n"
                                "2. **Tune into Content Words**: English is a stress-timed language. Nouns, main verbs, and key adjectives are spoken louder and longer. These carry 80% of the meaning.\n"
                                "3. **Identify Speaker Tone & Intonation**: A speaker's pitch and energy reveal whether they are announcing bad news, celebrating, warning, or explaining.\n"
                                "4. **Synthesize the 5 Ws**: Ask yourself: *Who is speaking? What happened? Where/When did it occur? Why does it matter?*"
                            )
                        }
                    }
                ]
            },

            # Page 3: Model & Structured Analysis / Visual Diagram
            {
                "page_number": 3,
                "page_title": "Model & Structured Analysis",
                "blocks": [
                    {
                        "block_type": "model_dialogue",
                        "component_type": "model_dialogue",
                        "title": "Model Analysis: School Assembly Emergency Announcement",
                        "content": {
                            "context": "A school principal makes an urgent announcement to students over the public address system.",
                            "dialogue": [
                                {
                                    "speaker": "Principal (Mr. Otieno)",
                                    "text": "Attention all students and faculty members. Due to unanticipated heavy rainfall overnight that caused waterlogging across the lower playing fields, the inter-school athletics championship scheduled for this Friday afternoon has been postponed. The event will now take place next Friday, October 24th, starting at 8:30 AM. All track team captains and coaches must report to the gymnasium during the 1:00 PM lunch break for a brief briefing."
                                }
                            ]
                        }
                    },
                    {
                        "block_type": "concept_explanation",
                        "component_type": "concept_explanation",
                        "title": "Gist Deconstruction Analysis",
                        "content": {
                            "text": (
                                "Let us break down this announcement to separate the core message from minor details:\n\n"
                                "- **Content Keywords**: *rainfall, waterlogging, athletics championship, postponed, next Friday, team meeting.*\n"
                                "- **Supporting Details (Disregarded for Gist)**: *overnight, lower playing fields, October 24th, 8:30 AM, gymnasium, 1:00 PM lunch break, Mr. Otieno.*\n"
                                "- **The Gist Summary Statement**: *'The inter-school athletics championship is postponed to next week due to flooded fields, and team leaders have a meeting today.'*\n\n"
                                "Notice how the gist summary captures the entire point in one sentence without losing essential meaning!"
                            )
                        }
                    },
                    {
                        "block_type": "diagram",
                        "component_type": "diagram",
                        "title": "Extensive Listening Comprehension Pyramid",
                        "content": {
                            "svg": SVG_LISTENING_GIST_PYRAMID,
                            "caption": "The Comprehension Hierarchy: Distilling global essence (apex) from main points and supporting factual details (base)."
                        }
                    }
                ]
            },

            # Page 4: Media Integration & Listening Lab
            {
                "page_number": 4,
                "page_title": "Media Integration & Listening Lab",
                "blocks": [
                    {
                        "block_type": "suggested_video",
                        "component_type": "suggested_video",
                        "title": "Listening Comprehension: Catching the Main Idea",
                        "content": {
                            "title": "Listening Skills: How to Catch the Main Idea in English Conversations",
                            "youtube_id": "CZNeLb3J3r4",
                            "url": "https://www.youtube.com/watch?v=CZNeLb3J3r4",
                            "description": "A comprehensive listening lab providing authentic audio dialogues, showing learners how to filter conversational filler and identify the primary purpose of spoken exchanges."
                        }
                    },
                    {
                        "block_type": "listening_lab",
                        "component_type": "listening_lab",
                        "title": "Global Listening Lab Tasks",
                        "content": {
                            "pre_viewing_task": (
                                "**Pre-Viewing Challenge**: Play the first audio conversation in the video once straight through. Do NOT write notes during the first pass.\n\n"
                                "As you listen, focus entirely on answering one fundamental question:\n"
                                "- *What is the primary reason the two people are having this conversation?*"
                            ),
                            "post_viewing_discussion": (
                                "**Post-Viewing Analysis**:\n\n"
                                "- What transitions (e.g., *'The thing is...', 'Anyway...', 'Basically...'*) did the speakers use right before stating their main point?\n"
                                "- Compare your 1-sentence gist summary with a partner to see if you both captured the same core message."
                            )
                        }
                    }
                ]
            },

            # Page 5: Common Mistakes & Guided Practice
            {
                "page_number": 5,
                "page_title": "Common Mistakes & Guided Practice",
                "blocks": [
                    {
                        "block_type": "common_mistakes",
                        "component_type": "common_mistakes",
                        "title": "Common Mistakes in Listening for Gist",
                        "content": {
                            "mistakes": [
                                {
                                    "mistake": "Fixating on a single unknown word while the audio continues playing.",
                                    "why_it_is_wrong": "Your working memory stalls on the unfamiliar word, causing you to lose the thread of subsequent sentences.",
                                    "correction": "Let unknown vocabulary go and rely on the surrounding context to understand the broader message."
                                },
                                {
                                    "mistake": "Confusing a narrow supporting example with the overarching main idea.",
                                    "why_it_is_wrong": "Supporting details illustrate a sub-point; they do not represent the central purpose of the speech.",
                                    "correction": "Ask yourself: 'Does this statement cover the entire talk, or is it just one piece of evidence?'"
                                }
                            ]
                        }
                    },
                    {
                        "block_type": "guided_practice",
                        "component_type": "guided_practice",
                        "title": "Guided Exercise: Distinguishing Gist from Details",
                        "content": {
                            "instructions": "Read the spoken passage below and classify each statement as either the 'Main Idea / Gist' or a 'Supporting Detail':",
                            "passage": (
                                "“Living and working in a major city like Nairobi certainly has its challenges, such as heavy morning traffic jams and high rental costs. However, the economic opportunities it provides are unmatched. Multinational corporations, tech innovation hubs, and financial institutions are expanding rapidly, creating thousands of high-quality employment positions for young university graduates.”"
                            ),
                            "exercises": [
                                {
                                    "statement": "Statement A: 'Nairobi has heavy morning traffic jams and expensive housing.'",
                                    "classification": "Supporting Detail (Illustrates the challenges)"
                                },
                                {
                                    "statement": "Statement B: 'Tech innovation hubs and multinational firms are hiring university graduates.'",
                                    "classification": "Supporting Detail (Specific evidence of job growth)"
                                },
                                {
                                    "statement": "Statement C: 'Despite urban challenges, major cities offer superior career and economic opportunities.'",
                                    "classification": "Main Idea / Gist (Encompasses the entire thesis)"
                                }
                            ]
                        }
                    },
                    {
                        "block_type": "mini_activity",
                        "component_type": "mini_activity",
                        "title": "Independent Challenge: The 20-Word News Summary",
                        "content": {
                            "activity_prompt": (
                                "Tune in to a 2-minute English radio news bulletin or podcast clip today.\n\n"
                                "1. Listen without writing.\n"
                                "2. Draft a single-sentence summary capturing the headline story in **under 20 words**.\n"
                                "3. Check: Did you include the *Who* and *What*, while eliminating trivial numbers or quotes?"
                            )
                        }
                    }
                ]
            },

            # Page 6: Knowledge Check & Summary
            {
                "page_number": 6,
                "page_title": "Knowledge Check & Summary",
                "blocks": [
                    {
                        "block_type": "knowledge_check",
                        "component_type": "knowledge_check",
                        "title": "Knowledge Check 1: Main Idea vs Supporting Detail",
                        "content": {
                            "question": "A guest speaker delivers a 30-minute lecture on climate change and environmental conservation in East Africa. During the presentation, she spends three minutes explaining how reusable bamboo straws reduce single-use plastic waste. In the context of the entire lecture, what does the bamboo straw topic represent?",
                            "options": [
                                "A. The overarching main idea of the lecture",
                                "B. A supporting detail / illustrative example",
                                "C. The global gist of the presentation",
                                "D. An acoustic prediction strategy"
                            ],
                            "correct": "B",
                            "explanation": "Option B is correct because bamboo straws serve as a specific, narrow example (a supporting detail) to illustrate the broader main theme of environmental conservation. Options A and C mistake a minor detail for the entire lecture's thesis."
                        }
                    },
                    {
                        "block_type": "knowledge_check",
                        "component_type": "knowledge_check",
                        "title": "Knowledge Check 2: Effective Listening Strategy",
                        "content": {
                            "question": "While listening to a fast-paced radio debate in English, you encounter an unfamiliar technical word in the second sentence. What is the most effective listening strategy to maintain comprehension?",
                            "options": [
                                "A. Stop listening immediately and search for the word in a dictionary",
                                "B. Keep repeating the unfamiliar word in your head until you deduce its root meaning",
                                "C. Ignore the isolated word, continue following the flow of the speaker's ideas, and deduce the general topic from context",
                                "D. Assume the entire broadcast is too difficult and stop listening"
                            ],
                            "correct": "C",
                            "explanation": "Option C is correct because extensive listening for gist prioritizes continuous global comprehension over word-for-word analysis. Dwelling on an unknown word causes cognitive blockage, resulting in missing key subsequent points."
                        }
                    },
                    {
                        "block_type": "key_takeaway",
                        "component_type": "key_takeaway",
                        "title": "Lesson 3 Summary: Core Takeaways",
                        "content": {
                            "text": (
                                "1. **Gist is the Big Picture**: Extensive listening focuses on the overarching purpose and main thesis of spoken communication.\n"
                                "2. **Don't Freeze on Single Words**: Let unfamiliar vocabulary flow past; stressed content words and context clues will provide the necessary meaning.\n"
                                "3. **Separate Gist from Details**: Identify whether a piece of information is the central argument or merely an illustrative supporting fact.\n"
                                "4. **Synthesize with the 5 Ws**: Active listening means continuously summarizing *who, what, where, when, and why* in your mind."
                            )
                        }
                    }
                ]
            }
        ]
    }
]

# =============================================================================
# INGESTION EXECUTION FUNCTION
# =============================================================================

def run_ingestion():
    print("=" * 80)
    print("Starting Ingestion for CBC Grade 10 English: Topic 1 (Lessons 1, 2, and 3)")
    print("=" * 80)

    with transaction.atomic():
        # 1. Verify / Link Grade (Grade 10, ID: 5)
        grade = Grade.objects.get(id=5)
        print(f"[✓] Grade Verified: [{grade.id}] {grade.name} (Level: {grade.level})")

        # 2. Verify / Create Subject 'English'
        subject, subj_created = Subject.objects.get_or_create(
            grade=grade,
            name="English",
            defaults={"description": "CBC Grade 10 English Language and Literature"}
        )
        print(f"[{'CREATED' if subj_created else 'VERIFIED'}] Subject: [{subject.id}] {subject.name} (Grade: {subject.grade.name})")

        # 3. Verify / Create Topic 'Listening and Speaking' (Order: 1)
        topic, top_created = Topic.objects.get_or_create(
            subject=subject,
            order=1,
            defaults={
                "name": "Listening and Speaking",
                "description": "Etiquette in service encounters, vowel pronunciation and minimal pairs, extensive listening for gist, critical listening, and public speaking."
            }
        )
        topic.name = "Listening and Speaking"
        topic.description = "Etiquette in service encounters, vowel pronunciation and minimal pairs, extensive listening for gist, critical listening, and public speaking."
        topic.save()
        print(f"[{'CREATED' if top_created else 'VERIFIED'}] Topic: [{topic.id}] Topic {topic.order}: {topic.name}")

        # 4. Ingest Lessons 1, 2, and 3
        total_blocks_created = 0
        total_assets_created = 0

        for les_data in LESSONS_DATA:
            u_order = les_data["unit_order"]
            u_name = clean_text(les_data["unit_name"])
            u_desc = clean_text(les_data.get("unit_description", f"Learning unit for {u_name}"))
            les_title = clean_text(les_data["lesson_title"])

            # LearningUnit
            unit, unit_created = LearningUnit.objects.get_or_create(
                topic=topic,
                order=u_order,
                defaults={"name": u_name, "description": u_desc}
            )
            unit.name = u_name
            unit.description = u_desc
            unit.save()

            # Lesson
            lesson, lesson_created = Lesson.objects.get_or_create(
                topic=topic,
                learning_unit=unit,
                defaults={
                    "title": les_title,
                    "status": "published",
                    "version": 1
                }
            )
            lesson.title = les_title
            lesson.status = "published"
            lesson.version = 1
            lesson.save()

            # Clean previous blocks & assets for idempotency
            lesson.blocks.all().delete()
            lesson.assets.all().delete()

            block_seq = 1
            for page in les_data["pages"]:
                p_num = page["page_number"]
                p_title = clean_text(page["page_title"])

                for comp_order, blk in enumerate(page["blocks"], start=1):
                    b_type = blk["block_type"]
                    c_type = blk.get("component_type", b_type)
                    b_title = clean_text(blk.get("title", p_title))
                    b_content = clean_dict(blk.get("content", {}))
                    b_meta = clean_dict(blk.get("metadata", {}))

                    # Create LessonBlock
                    block = LessonBlock.objects.create(
                        lesson=lesson,
                        page_number=p_num,
                        page_title=p_title,
                        order=block_seq,
                        component_order=comp_order,
                        block_type=b_type,
                        component_type=c_type,
                        title=b_title,
                        content=b_content,
                        metadata=b_meta
                    )
                    block_seq += 1
                    total_blocks_created += 1

                    # Attach LessonAsset if applicable
                    if b_type == "suggested_image" and "url" in b_content:
                        asset = LessonAsset.objects.create(
                            lesson=lesson,
                            title=b_title,
                            asset_type="image",
                            source_type="external",
                            storage_type="url",
                            status="attached",
                            url=b_content["url"],
                            description=b_content.get("text", b_title),
                            metadata={
                                "author": b_content.get("author", "Wikimedia Commons"),
                                "licensing": b_content.get("licensing", "CC BY-SA 4.0"),
                                "commons_page_url": b_content.get("commons_page_url", ""),
                                "caption": b_meta.get("caption", b_content.get("text", ""))
                            }
                        )
                        block.assets.add(asset)
                        total_assets_created += 1

                    elif (b_type in ["diagram", "suggested_diagram"]) and ("svg" in b_content or "svg_code" in b_content or "svg_content" in b_meta):
                        svg_data = b_content.get("svg") or b_content.get("svg_code") or b_meta.get("svg_content", "")
                        asset = LessonAsset.objects.create(
                            lesson=lesson,
                            title=b_title,
                            asset_type="diagram",
                            source_type="ai_generated",
                            storage_type="embed",
                            status="attached",
                            description=b_content.get("caption", b_title),
                            metadata={"svg_content": svg_data}
                        )
                        block.assets.add(asset)
                        total_assets_created += 1

                    elif b_type == "suggested_video" and "youtube_id" in b_content:
                        asset = LessonAsset.objects.create(
                            lesson=lesson,
                            title=b_title,
                            asset_type="youtube",
                            source_type="external",
                            storage_type="url",
                            status="attached",
                            url=b_content.get("url", f"https://www.youtube.com/watch?v={b_content['youtube_id']}"),
                            description=b_content.get("description", b_title),
                            metadata={"youtube_id": b_content["youtube_id"]}
                        )
                        block.assets.add(asset)
                        total_assets_created += 1

            print(f" -> [INGESTED] Unit {u_order}: '{les_title}' ({len(les_data['pages'])} pages, {block_seq - 1} blocks)")

    print("=" * 80)
    print(f"Ingestion Completed Successfully!")
    print(f"Total Blocks Ingested: {total_blocks_created}")
    print(f"Total Assets Attached: {total_assets_created}")
    print("=" * 80)

if __name__ == "__main__":
    run_ingestion()
