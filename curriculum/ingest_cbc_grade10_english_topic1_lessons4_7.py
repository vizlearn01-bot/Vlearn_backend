"""
VLearn CBC Grade 10 English — Topic 1: Listening and Speaking
Direct Programmatic Ingestion Engine for Lessons 4, 5, 6, and 7

Grade: Grade 10 (Grade ID: 5)
Subject: English
Topic 1: Listening and Speaking (Order: 1)
Lessons:
  4. Critical Listening: Fact, Opinion, Evidence, and Bias
  5. Intensive Listening and Viewing for Details
  6. Non-verbal Communication and Conversational Skills
  7. Interactive and Responsive Listening

Usage:
  ./venv/bin/python curriculum/ingest_cbc_grade10_english_topic1_lessons4_7.py
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

SVG_CRITICAL_LISTENING = validate_svg("""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 960 520" width="100%" height="100%">
  <defs>
    <linearGradient id="bgGrad4" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#090d16" />
      <stop offset="100%" stop-color="#1e293b" />
    </linearGradient>
    <linearGradient id="factBg" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#064e3b" />
      <stop offset="100%" stop-color="#022c22" />
    </linearGradient>
    <linearGradient id="opinionBg" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#78350f" />
      <stop offset="100%" stop-color="#451a03" />
    </linearGradient>
    <linearGradient id="evidenceBg" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#1e3a8a" />
      <stop offset="100%" stop-color="#0f172a" />
    </linearGradient>
    <linearGradient id="biasBg" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#881337" />
      <stop offset="100%" stop-color="#4c0519" />
    </linearGradient>
    <filter id="shadow4" x="-5%" y="-5%" width="110%" height="110%">
      <feDropShadow dx="0" dy="4" stdDeviation="6" flood-color="#000" flood-opacity="0.5"/>
    </filter>
  </defs>

  <rect width="960" height="520" rx="16" fill="url(#bgGrad4)" stroke="#334155" stroke-width="2"/>

  <g transform="translate(480, 42)" text-anchor="middle">
    <text font-family="system-ui, -apple-system, sans-serif" font-size="22" font-weight="800" fill="#38bdf8" letter-spacing="0.5">Critical Listening &amp; Discourse Analysis Matrix</text>
    <text y="24" font-family="system-ui, -apple-system, sans-serif" font-size="13" fill="#94a3b8">The 4 Pillars of Evaluative Listening: Fact vs. Opinion vs. Evidence vs. Bias</text>
  </g>

  <!-- 1. FACT -->
  <g transform="translate(30, 95)" filter="url(#shadow4)">
    <rect width="210" height="385" rx="12" fill="url(#factBg)" stroke="#10b981" stroke-width="2"/>
    <rect width="210" height="40" rx="12" fill="#059669"/>
    <rect y="28" width="210" height="12" fill="#059669"/>
    <text x="105" y="26" font-family="system-ui, sans-serif" font-size="14" font-weight="800" fill="#ffffff" text-anchor="middle">1. FACT</text>
    
    <g transform="translate(15, 55)">
      <text font-family="system-ui, sans-serif" font-size="11" font-weight="700" fill="#34d399">NATURE:</text>
      <text y="18" font-family="system-ui, sans-serif" font-size="11.5" fill="#ecfdf5">Objective &amp; verifiable.</text>
      <text y="34" font-family="system-ui, sans-serif" font-size="11.5" fill="#ecfdf5">Free from personal bias.</text>
      
      <text y="62" font-family="system-ui, sans-serif" font-size="11" font-weight="700" fill="#34d399">VERIFICATION:</text>
      <text y="80" font-family="system-ui, sans-serif" font-size="11" fill="#a7f3d0">• Historical dates</text>
      <text y="96" font-family="system-ui, sans-serif" font-size="11" fill="#a7f3d0">• Empirical counts</text>
      <text y="112" font-family="system-ui, sans-serif" font-size="11" fill="#a7f3d0">• Direct observation</text>
      
      <rect y="130" width="180" height="180" rx="8" fill="#062e24" stroke="#059669" stroke-width="1"/>
      <text x="10" y="22" font-family="system-ui, sans-serif" font-size="10" font-weight="700" fill="#6ee7b7">SPOKEN EXAMPLE:</text>
      <text x="10" y="44" font-family="system-ui, sans-serif" font-size="11" font-style="italic" fill="#ffffff">&quot;Kenya attained</text>
      <text x="10" y="62" font-family="system-ui, sans-serif" font-size="11" font-style="italic" fill="#ffffff">internal self-rule on</text>
      <text x="10" y="80" font-family="system-ui, sans-serif" font-size="11" font-style="italic" fill="#ffffff">June 1, 1963.&quot;</text>
      <text x="10" y="115" font-family="system-ui, sans-serif" font-size="10" font-weight="700" fill="#6ee7b7">KEY MARKER:</text>
      <text x="10" y="135" font-family="system-ui, sans-serif" font-size="10.5" fill="#d1fae5">100% Proven</text>
    </g>
  </g>

  <!-- 2. OPINION -->
  <g transform="translate(260, 95)" filter="url(#shadow4)">
    <rect width="210" height="385" rx="12" fill="url(#opinionBg)" stroke="#f59e0b" stroke-width="2"/>
    <rect width="210" height="40" rx="12" fill="#d97706"/>
    <rect y="28" width="210" height="12" fill="#d97706"/>
    <text x="105" y="26" font-family="system-ui, sans-serif" font-size="14" font-weight="800" fill="#ffffff" text-anchor="middle">2. OPINION</text>
    
    <g transform="translate(15, 55)">
      <text font-family="system-ui, sans-serif" font-size="11" font-weight="700" fill="#fcd34d">NATURE:</text>
      <text y="18" font-family="system-ui, sans-serif" font-size="11.5" fill="#fef3c7">Subjective belief,</text>
      <text y="34" font-family="system-ui, sans-serif" font-size="11.5" fill="#fef3c7">taste, or value judgment.</text>
      
      <text y="62" font-family="system-ui, sans-serif" font-size="11" font-weight="700" fill="#fcd34d">VERIFICATION:</text>
      <text y="80" font-family="system-ui, sans-serif" font-size="11" fill="#fde68a">• Cannot be proven</text>
      <text y="96" font-family="system-ui, sans-serif" font-size="11" fill="#fde68a">• Uses value words</text>
      <text y="112" font-family="system-ui, sans-serif" font-size="11" fill="#fde68a">• Differs per person</text>
      
      <rect y="130" width="180" height="180" rx="8" fill="#451a03" stroke="#d97706" stroke-width="1"/>
      <text x="10" y="22" font-family="system-ui, sans-serif" font-size="10" font-weight="700" fill="#fde68a">SPOKEN EXAMPLE:</text>
      <text x="10" y="44" font-family="system-ui, sans-serif" font-size="11" font-style="italic" fill="#ffffff">&quot;Nairobi is the most</text>
      <text x="10" y="62" font-family="system-ui, sans-serif" font-size="11" font-style="italic" fill="#ffffff">vibrant and exciting</text>
      <text x="10" y="80" font-family="system-ui, sans-serif" font-size="11" font-style="italic" fill="#ffffff">city in Africa.&quot;</text>
      <text x="10" y="115" font-family="system-ui, sans-serif" font-size="10" font-weight="700" fill="#fde68a">KEY MARKER:</text>
      <text x="10" y="135" font-family="system-ui, sans-serif" font-size="10.5" fill="#fef3c7">Value Adjectives</text>
    </g>
  </g>

  <!-- 3. EVIDENCE -->
  <g transform="translate(490, 95)" filter="url(#shadow4)">
    <rect width="210" height="385" rx="12" fill="url(#evidenceBg)" stroke="#3b82f6" stroke-width="2"/>
    <rect width="210" height="40" rx="12" fill="#2563eb"/>
    <rect y="28" width="210" height="12" fill="#2563eb"/>
    <text x="105" y="26" font-family="system-ui, sans-serif" font-size="14" font-weight="800" fill="#ffffff" text-anchor="middle">3. EVIDENCE</text>
    
    <g transform="translate(15, 55)">
      <text font-family="system-ui, sans-serif" font-size="11" font-weight="700" fill="#93c5fd">NATURE:</text>
      <text y="18" font-family="system-ui, sans-serif" font-size="11.5" fill="#eff6ff">Substantiating proof</text>
      <text y="34" font-family="system-ui, sans-serif" font-size="11.5" fill="#eff6ff">supporting a claim.</text>
      
      <text y="62" font-family="system-ui, sans-serif" font-size="11" font-weight="700" fill="#93c5fd">VERIFICATION:</text>
      <text y="80" font-family="system-ui, sans-serif" font-size="11" fill="#bfdbfe">• Census reports</text>
      <text y="96" font-family="system-ui, sans-serif" font-size="11" fill="#bfdbfe">• Research surveys</text>
      <text y="112" font-family="system-ui, sans-serif" font-size="11" fill="#bfdbfe">• Expert testimony</text>
      
      <rect y="130" width="180" height="180" rx="8" fill="#0f224a" stroke="#2563eb" stroke-width="1"/>
      <text x="10" y="22" font-family="system-ui, sans-serif" font-size="10" font-weight="700" fill="#bfdbfe">SPOKEN EXAMPLE:</text>
      <text x="10" y="44" font-family="system-ui, sans-serif" font-size="11" font-style="italic" fill="#ffffff">&quot;KNBS 2024 survey</text>
      <text x="10" y="62" font-family="system-ui, sans-serif" font-size="11" font-style="italic" fill="#ffffff">indicates tourism</text>
      <text x="10" y="80" font-family="system-ui, sans-serif" font-size="11" font-style="italic" fill="#ffffff">grew by 14.2%.&quot;</text>
      <text x="10" y="115" font-family="system-ui, sans-serif" font-size="10" font-weight="700" fill="#bfdbfe">KEY MARKER:</text>
      <text x="10" y="135" font-family="system-ui, sans-serif" font-size="10.5" fill="#dbeafe">Attributed Source</text>
    </g>
  </g>

  <!-- 4. BIAS -->
  <g transform="translate(720, 95)" filter="url(#shadow4)">
    <rect width="210" height="385" rx="12" fill="url(#biasBg)" stroke="#f43f5e" stroke-width="2"/>
    <rect width="210" height="40" rx="12" fill="#e11d48"/>
    <rect y="28" width="210" height="12" fill="#e11d48"/>
    <text x="105" y="26" font-family="system-ui, sans-serif" font-size="14" font-weight="800" fill="#ffffff" text-anchor="middle">4. BIAS</text>
    
    <g transform="translate(15, 55)">
      <text font-family="system-ui, sans-serif" font-size="11" font-weight="700" fill="#fda4af">NATURE:</text>
      <text y="18" font-family="system-ui, sans-serif" font-size="11.5" fill="#fff1f2">One-sided slant</text>
      <text y="34" font-family="system-ui, sans-serif" font-size="11.5" fill="#fff1f2">distorting objectivity.</text>
      
      <text y="62" font-family="system-ui, sans-serif" font-size="11" font-weight="700" fill="#fda4af">VERIFICATION:</text>
      <text y="80" font-family="system-ui, sans-serif" font-size="11" fill="#fecdd3">• Loaded wording</text>
      <text y="96" font-family="system-ui, sans-serif" font-size="11" fill="#fecdd3">• Omitted drawbacks</text>
      <text y="112" font-family="system-ui, sans-serif" font-size="11" fill="#fecdd3">• Commercial motive</text>
      
      <rect y="130" width="180" height="180" rx="8" fill="#3b0816" stroke="#e11d48" stroke-width="1"/>
      <text x="10" y="22" font-family="system-ui, sans-serif" font-size="10" font-weight="700" fill="#fecdd3">SPOKEN EXAMPLE:</text>
      <text x="10" y="44" font-family="system-ui, sans-serif" font-size="11" font-style="italic" fill="#ffffff">&quot;Our network is</text>
      <text x="10" y="62" font-family="system-ui, sans-serif" font-size="11" font-style="italic" fill="#ffffff">flawless; rivals are</text>
      <text x="10" y="80" font-family="system-ui, sans-serif" font-size="11" font-style="italic" fill="#ffffff">terrible &amp; slow.&quot;</text>
      <text x="10" y="115" font-family="system-ui, sans-serif" font-size="10" font-weight="700" fill="#fecdd3">KEY MARKER:</text>
      <text x="10" y="135" font-family="system-ui, sans-serif" font-size="10.5" fill="#ffe4e6">Loaded / Slanted</text>
    </g>
  </g>
</svg>""", "SVG_CRITICAL_LISTENING")

SVG_INTENSIVE_LISTENING = validate_svg("""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 960 520" width="100%" height="100%">
  <defs>
    <linearGradient id="bgGrad5" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#081b1b" />
      <stop offset="100%" stop-color="#0f2b2b" />
    </linearGradient>
    <linearGradient id="cardGrad5" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#134e4a" />
      <stop offset="100%" stop-color="#042f2e" />
    </linearGradient>
    <filter id="shadow5" x="-5%" y="-5%" width="110%" height="110%">
      <feDropShadow dx="0" dy="4" stdDeviation="6" flood-color="#000" flood-opacity="0.4"/>
    </filter>
  </defs>

  <rect width="960" height="520" rx="16" fill="url(#bgGrad5)" stroke="#115e59" stroke-width="2"/>

  <g transform="translate(480, 42)" text-anchor="middle">
    <text font-family="system-ui, -apple-system, sans-serif" font-size="22" font-weight="800" fill="#2dd4bf" letter-spacing="0.5">Intensive Listening &amp; Multi-Modal Viewing Protocol</text>
    <text y="24" font-family="system-ui, -apple-system, sans-serif" font-size="13" fill="#99f6e4">4-Stage Precision Detail Extraction &amp; Visual Triangulation</text>
  </g>

  <!-- Step 1 -->
  <g transform="translate(40, 95)" filter="url(#shadow5)">
    <rect width="415" height="175" rx="12" fill="url(#cardGrad5)" stroke="#14b8a6" stroke-width="2"/>
    <circle cx="35" cy="35" r="18" fill="#14b8a6"/>
    <text x="35" y="41" font-family="system-ui, sans-serif" font-size="14" font-weight="800" fill="#ffffff" text-anchor="middle">1</text>
    <text x="68" y="32" font-family="system-ui, sans-serif" font-size="15" font-weight="700" fill="#5eead4">Active Sound Filtering</text>
    <text x="68" y="48" font-family="system-ui, sans-serif" font-size="11" fill="#99f6e4">Isolating Target Speech from Noise</text>
    <line x1="20" y1="65" x2="395" y2="65" stroke="#0f766e" stroke-width="1.5"/>
    <text x="20" y="90" font-family="system-ui, sans-serif" font-size="12" fill="#ccfbf1">• Block ambient background acoustic noise</text>
    <text x="20" y="114" font-family="system-ui, sans-serif" font-size="12" fill="#ccfbf1">• Focus cognitive bandwidth on core keywords</text>
    <text x="20" y="138" font-family="system-ui, sans-serif" font-size="12" fill="#ccfbf1">• Discriminate subtle minimal pair vowel contrasts</text>
  </g>

  <!-- Step 2 -->
  <g transform="translate(505, 95)" filter="url(#shadow5)">
    <rect width="415" height="175" rx="12" fill="url(#cardGrad5)" stroke="#38bdf8" stroke-width="2"/>
    <circle cx="35" cy="35" r="18" fill="#0284c7"/>
    <text x="35" y="41" font-family="system-ui, sans-serif" font-size="14" font-weight="800" fill="#ffffff" text-anchor="middle">2</text>
    <text x="68" y="32" font-family="system-ui, sans-serif" font-size="15" font-weight="700" fill="#7dd3fc">Sequence &amp; Action Tracking</text>
    <text x="68" y="48" font-family="system-ui, sans-serif" font-size="11" fill="#bae6fd">Capturing Multiword Units &amp; Steps</text>
    <line x1="20" y1="65" x2="395" y2="65" stroke="#0369a1" stroke-width="1.5"/>
    <text x="20" y="90" font-family="system-ui, sans-serif" font-size="12" fill="#e0f2fe">• Track markers: &quot;First, Next, Prior to, Finally&quot;</text>
    <text x="20" y="114" font-family="system-ui, sans-serif" font-size="12" fill="#e0f2fe">• Lock onto action imperatives (&quot;Press, connect, mix&quot;)</text>
    <text x="20" y="138" font-family="system-ui, sans-serif" font-size="12" fill="#e0f2fe">• Highlight safety caveats and explicit warnings</text>
  </g>

  <!-- Step 3 -->
  <g transform="translate(40, 295)" filter="url(#shadow5)">
    <rect width="415" height="175" rx="12" fill="url(#cardGrad5)" stroke="#818cf8" stroke-width="2"/>
    <circle cx="35" cy="35" r="18" fill="#4f46e5"/>
    <text x="35" y="41" font-family="system-ui, sans-serif" font-size="14" font-weight="800" fill="#ffffff" text-anchor="middle">3</text>
    <text x="68" y="32" font-family="system-ui, sans-serif" font-size="15" font-weight="700" fill="#a5b4fc">Selective Shorthand Note-Taking</text>
    <text x="68" y="48" font-family="system-ui, sans-serif" font-size="11" fill="#c7d2fe">Capturing Micro-Units &amp; Metrics</text>
    <line x1="20" y1="65" x2="395" y2="65" stroke="#3730a3" stroke-width="1.5"/>
    <text x="20" y="90" font-family="system-ui, sans-serif" font-size="12" fill="#e0e7ff">• Record precise numbers, units, times, and codes</text>
    <text x="20" y="114" font-family="system-ui, sans-serif" font-size="12" fill="#e0e7ff">• Use shorthand symbols: (&amp;, -&gt;, w/, @, #, %)</text>
    <text x="20" y="138" font-family="system-ui, sans-serif" font-size="12" fill="#e0e7ff">• Avoid full sentences to maintain real-time pace</text>
  </g>

  <!-- Step 4 -->
  <g transform="translate(505, 295)" filter="url(#shadow5)">
    <rect width="415" height="175" rx="12" fill="url(#cardGrad5)" stroke="#fbbf24" stroke-width="2"/>
    <circle cx="35" cy="35" r="18" fill="#d97706"/>
    <text x="35" y="41" font-family="system-ui, sans-serif" font-size="14" font-weight="800" fill="#ffffff" text-anchor="middle">4</text>
    <text x="68" y="32" font-family="system-ui, sans-serif" font-size="15" font-weight="700" fill="#fde68a">Multi-Modal Triangulation</text>
    <text x="68" y="48" font-family="system-ui, sans-serif" font-size="11" fill="#fef3c7">Cross-Checking Audio with Screen Visuals</text>
    <line x1="20" y1="65" x2="395" y2="65" stroke="#92400e" stroke-width="1.5"/>
    <text x="20" y="90" font-family="system-ui, sans-serif" font-size="12" fill="#fffbeb">• Correlate spoken commands with on-screen graphics</text>
    <text x="20" y="114" font-family="system-ui, sans-serif" font-size="12" fill="#fffbeb">• Track presenter gestures and pointer arrows</text>
    <text x="20" y="138" font-family="system-ui, sans-serif" font-size="12" fill="#fffbeb">• Confirm exact spelling of technical terms &amp; formulas</text>
  </g>
</svg>""", "SVG_INTENSIVE_LISTENING")

SVG_NONVERBAL_REPAIR = validate_svg("""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 960 520" width="100%" height="100%">
  <defs>
    <linearGradient id="bgGrad6" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#180e29" />
      <stop offset="100%" stop-color="#2a1b4e" />
    </linearGradient>
    <linearGradient id="nvCardBg" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#3b1d6e" />
      <stop offset="100%" stop-color="#1e0f38" />
    </linearGradient>
    <linearGradient id="repairCardBg" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#064e3b" />
      <stop offset="100%" stop-color="#022c22" />
    </linearGradient>
    <filter id="shadow6" x="-5%" y="-5%" width="110%" height="110%">
      <feDropShadow dx="0" dy="4" stdDeviation="6" flood-color="#000" flood-opacity="0.4"/>
    </filter>
  </defs>

  <rect width="960" height="520" rx="16" fill="url(#bgGrad6)" stroke="#7c3aed" stroke-width="2"/>

  <g transform="translate(480, 42)" text-anchor="middle">
    <text font-family="system-ui, -apple-system, sans-serif" font-size="22" font-weight="800" fill="#c084fc" letter-spacing="0.5">Non-Verbal Channels &amp; Conversational Repair Engine</text>
    <text y="24" font-family="system-ui, -apple-system, sans-serif" font-size="13" fill="#e9d5ff">Harmonizing Kinesics, Vocalics, and Real-Time Misunderstanding Resolution</text>
  </g>

  <!-- Left: Non-Verbal Channels -->
  <g transform="translate(40, 95)" filter="url(#shadow6)">
    <rect width="420" height="385" rx="12" fill="url(#nvCardBg)" stroke="#a855f7" stroke-width="2"/>
    <rect width="420" height="42" rx="12" fill="#7e22ce"/>
    <rect y="30" width="420" height="12" fill="#7e22ce"/>
    <text x="210" y="27" font-family="system-ui, sans-serif" font-size="15" font-weight="800" fill="#ffffff" text-anchor="middle">4 Primary Non-Verbal Channels</text>

    <g transform="translate(20, 60)">
      <!-- Channel 1 -->
      <rect width="380" height="60" rx="8" fill="#2e1065" stroke="#9333ea" stroke-width="1"/>
      <text x="15" y="22" font-family="system-ui, sans-serif" font-size="12" font-weight="700" fill="#d8b4fe">1. Oculesics (Eye Contact):</text>
      <text x="15" y="42" font-family="system-ui, sans-serif" font-size="11.5" fill="#f3e8ff">Maintains trust &amp; rapport; soft 4–5 sec intervals.</text>
      
      <!-- Channel 2 -->
      <g transform="translate(0, 70)">
        <rect width="380" height="60" rx="8" fill="#2e1065" stroke="#9333ea" stroke-width="1"/>
        <text x="15" y="22" font-family="system-ui, sans-serif" font-size="12" font-weight="700" fill="#d8b4fe">2. Kinesics (Body &amp; Gestures):</text>
        <text x="15" y="42" font-family="system-ui, sans-serif" font-size="11.5" fill="#f3e8ff">Upright posture, open hands; avoids defensive arms.</text>
      </g>

      <!-- Channel 3 -->
      <g transform="translate(0, 140)">
        <rect width="380" height="60" rx="8" fill="#2e1065" stroke="#9333ea" stroke-width="1"/>
        <text x="15" y="22" font-family="system-ui, sans-serif" font-size="12" font-weight="700" fill="#d8b4fe">3. Paralanguage / Vocalics:</text>
        <text x="15" y="42" font-family="system-ui, sans-serif" font-size="11.5" fill="#f3e8ff">Pitch modulation, dynamic pace, expressive pauses.</text>
      </g>

      <!-- Channel 4 -->
      <g transform="translate(0, 210)">
        <rect width="380" height="60" rx="8" fill="#2e1065" stroke="#9333ea" stroke-width="1"/>
        <text x="15" y="22" font-family="system-ui, sans-serif" font-size="12" font-weight="700" fill="#d8b4fe">4. Proxemics (Conversational Space):</text>
        <text x="15" y="42" font-family="system-ui, sans-serif" font-size="11.5" fill="#f3e8ff">Maintains respectful social distance (0.5m – 1.2m).</text>
      </g>
    </g>
  </g>

  <!-- Right: Conversational Repair Engine -->
  <g transform="translate(500, 95)" filter="url(#shadow6)">
    <rect width="420" height="385" rx="12" fill="url(#repairCardBg)" stroke="#10b981" stroke-width="2"/>
    <rect width="420" height="42" rx="12" fill="#047857"/>
    <rect y="30" width="420" height="12" fill="#047857"/>
    <text x="210" y="27" font-family="system-ui, sans-serif" font-size="15" font-weight="800" fill="#ffffff" text-anchor="middle">Conversational Repair Engine</text>

    <g transform="translate(20, 60)">
      <!-- Repair 1 -->
      <rect width="380" height="85" rx="8" fill="#062e24" stroke="#059669" stroke-width="1"/>
      <text x="15" y="22" font-family="system-ui, sans-serif" font-size="12" font-weight="700" fill="#34d399">1. Acoustic Repair (Repetition Request):</text>
      <text x="15" y="40" font-family="system-ui, sans-serif" font-size="11" fill="#a7f3d0">When speech is muffled or drowned by noise:</text>
      <text x="15" y="60" font-family="system-ui, sans-serif" font-size="11.5" font-style="italic" fill="#ffffff">&quot;I beg your pardon, could you repeat that last point?&quot;</text>

      <!-- Repair 2 -->
      <g transform="translate(0, 95)">
        <rect width="380" height="85" rx="8" fill="#062e24" stroke="#059669" stroke-width="1"/>
        <text x="15" y="22" font-family="system-ui, sans-serif" font-size="12" font-weight="700" fill="#34d399">2. Semantic Repair (Clarification Request):</text>
        <text x="15" y="40" font-family="system-ui, sans-serif" font-size="11" fill="#a7f3d0">When terminology or meaning is ambiguous:</text>
        <text x="15" y="60" font-family="system-ui, sans-serif" font-size="11.5" font-style="italic" fill="#ffffff">&quot;Could you clarify what you mean by 'ad hoc committee'?&quot;</text>
      </g>

      <!-- Repair 3 -->
      <g transform="translate(0, 190)">
        <rect width="380" height="85" rx="8" fill="#062e24" stroke="#059669" stroke-width="1"/>
        <text x="15" y="22" font-family="system-ui, sans-serif" font-size="12" font-weight="700" fill="#34d399">3. Speaker Self-Correction:</text>
        <text x="15" y="40" font-family="system-ui, sans-serif" font-size="11" fill="#a7f3d0">When a factual slip or misstatement occurs:</text>
        <text x="15" y="60" font-family="system-ui, sans-serif" font-size="11.5" font-style="italic" fill="#ffffff">&quot;The exam is on Monday—pardon me, I meant Tuesday.&quot;</text>
      </g>
    </g>
  </g>
</svg>""", "SVG_NONVERBAL_REPAIR")

SVG_INTERACTIVE_LOOP = validate_svg("""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 960 520" width="100%" height="100%">
  <defs>
    <linearGradient id="bgGrad7" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#1c0f05" />
      <stop offset="100%" stop-color="#381a07" />
    </linearGradient>
    <filter id="shadow7" x="-5%" y="-5%" width="110%" height="110%">
      <feDropShadow dx="0" dy="4" stdDeviation="6" flood-color="#000" flood-opacity="0.4"/>
    </filter>
  </defs>

  <rect width="960" height="520" rx="16" fill="url(#bgGrad7)" stroke="#ea580c" stroke-width="2"/>

  <g transform="translate(480, 42)" text-anchor="middle">
    <text font-family="system-ui, -apple-system, sans-serif" font-size="22" font-weight="800" fill="#fb923c" letter-spacing="0.5">5-Stage Interactive &amp; Responsive Listening Loop</text>
    <text y="24" font-family="system-ui, -apple-system, sans-serif" font-size="13" fill="#fed7aa">Closing the Interpersonal Feedback Loop via Paraphrasing &amp; Validation</text>
  </g>

  <!-- 5 Nodes in a Dynamic Flow -->

  <!-- Node 1: Receive -->
  <g transform="translate(35, 105)" filter="url(#shadow7)">
    <rect width="165" height="230" rx="12" fill="#1e293b" stroke="#38bdf8" stroke-width="2"/>
    <circle cx="82" cy="45" r="28" fill="#0369a1"/>
    <text x="82" y="52" font-family="system-ui, sans-serif" font-size="16" font-weight="800" fill="#ffffff" text-anchor="middle">1</text>
    <text x="82" y="95" font-family="system-ui, sans-serif" font-size="14" font-weight="700" fill="#7dd3fc" text-anchor="middle">RECEIVE</text>
    <text x="82" y="115" font-family="system-ui, sans-serif" font-size="11" fill="#94a3b8" text-anchor="middle">Hear &amp; Observe</text>
    <line x1="15" y1="130" x2="150" y2="130" stroke="#334155" stroke-width="1"/>
    <text x="15" y="152" font-family="system-ui, sans-serif" font-size="10.5" fill="#e2e8f0">• Full attention</text>
    <text x="15" y="172" font-family="system-ui, sans-serif" font-size="10.5" fill="#e2e8f0">• Watch posture</text>
    <text x="15" y="192" font-family="system-ui, sans-serif" font-size="10.5" fill="#e2e8f0">• Maintain eye gaze</text>
  </g>

  <!-- Node 2: Process -->
  <g transform="translate(215, 105)" filter="url(#shadow7)">
    <rect width="165" height="230" rx="12" fill="#1e293b" stroke="#a855f7" stroke-width="2"/>
    <circle cx="82" cy="45" r="28" fill="#7e22ce"/>
    <text x="82" y="52" font-family="system-ui, sans-serif" font-size="16" font-weight="800" fill="#ffffff" text-anchor="middle">2</text>
    <text x="82" y="95" font-family="system-ui, sans-serif" font-size="14" font-weight="700" fill="#d8b4fe" text-anchor="middle">PROCESS</text>
    <text x="82" y="115" font-family="system-ui, sans-serif" font-size="11" fill="#94a3b8" text-anchor="middle">Analyze &amp; Feel</text>
    <line x1="15" y1="130" x2="150" y2="130" stroke="#334155" stroke-width="1"/>
    <text x="15" y="152" font-family="system-ui, sans-serif" font-size="10.5" fill="#e2e8f0">• Decode core point</text>
    <text x="15" y="172" font-family="system-ui, sans-serif" font-size="10.5" fill="#e2e8f0">• Detect emotions</text>
    <text x="15" y="192" font-family="system-ui, sans-serif" font-size="10.5" fill="#e2e8f0">• Identify intent</text>
  </g>

  <!-- Node 3: Paraphrase -->
  <g transform="translate(395, 105)" filter="url(#shadow7)">
    <rect width="165" height="230" rx="12" fill="#1e293b" stroke="#10b981" stroke-width="2"/>
    <circle cx="82" cy="45" r="28" fill="#047857"/>
    <text x="82" y="52" font-family="system-ui, sans-serif" font-size="16" font-weight="800" fill="#ffffff" text-anchor="middle">3</text>
    <text x="82" y="95" font-family="system-ui, sans-serif" font-size="13" font-weight="700" fill="#6ee7b7" text-anchor="middle">PARAPHRASE</text>
    <text x="82" y="115" font-family="system-ui, sans-serif" font-size="11" fill="#94a3b8" text-anchor="middle">Reflect Meaning</text>
    <line x1="15" y1="130" x2="150" y2="130" stroke="#334155" stroke-width="1"/>
    <text x="15" y="152" font-family="system-ui, sans-serif" font-size="10.5" fill="#e2e8f0">• &quot;So you mean...&quot;</text>
    <text x="15" y="172" font-family="system-ui, sans-serif" font-size="10.5" fill="#e2e8f0">• In your own words</text>
    <text x="15" y="192" font-family="system-ui, sans-serif" font-size="10.5" fill="#e2e8f0">• Verify accuracy</text>
  </g>

  <!-- Node 4: Clarify -->
  <g transform="translate(575, 105)" filter="url(#shadow7)">
    <rect width="165" height="230" rx="12" fill="#1e293b" stroke="#f59e0b" stroke-width="2"/>
    <circle cx="82" cy="45" r="28" fill="#b45309"/>
    <text x="82" y="52" font-family="system-ui, sans-serif" font-size="16" font-weight="800" fill="#ffffff" text-anchor="middle">4</text>
    <text x="82" y="95" font-family="system-ui, sans-serif" font-size="14" font-weight="700" fill="#fcd34d" text-anchor="middle">CLARIFY</text>
    <text x="82" y="115" font-family="system-ui, sans-serif" font-size="11" fill="#94a3b8" text-anchor="middle">Probe Ambiguity</text>
    <line x1="15" y1="130" x2="150" y2="130" stroke="#334155" stroke-width="1"/>
    <text x="15" y="152" font-family="system-ui, sans-serif" font-size="10.5" fill="#e2e8f0">• Open questions</text>
    <text x="15" y="172" font-family="system-ui, sans-serif" font-size="10.5" fill="#e2e8f0">• Clear confusion</text>
    <text x="15" y="192" font-family="system-ui, sans-serif" font-size="10.5" fill="#e2e8f0">• No interruption</text>
  </g>

  <!-- Node 5: Respond -->
  <g transform="translate(755, 105)" filter="url(#shadow7)">
    <rect width="165" height="230" rx="12" fill="#1e293b" stroke="#f43f5e" stroke-width="2"/>
    <circle cx="82" cy="45" r="28" fill="#be123c"/>
    <text x="82" y="52" font-family="system-ui, sans-serif" font-size="16" font-weight="800" fill="#ffffff" text-anchor="middle">5</text>
    <text x="82" y="95" font-family="system-ui, sans-serif" font-size="14" font-weight="700" fill="#fda4af" text-anchor="middle">RESPOND</text>
    <text x="82" y="115" font-family="system-ui, sans-serif" font-size="11" fill="#94a3b8" text-anchor="middle">Validate &amp; Act</text>
    <line x1="15" y1="130" x2="150" y2="130" stroke="#334155" stroke-width="1"/>
    <text x="15" y="152" font-family="system-ui, sans-serif" font-size="10.5" fill="#e2e8f0">• Empathetic closure</text>
    <text x="15" y="172" font-family="system-ui, sans-serif" font-size="10.5" fill="#e2e8f0">• Shared solutions</text>
    <text x="15" y="192" font-family="system-ui, sans-serif" font-size="10.5" fill="#e2e8f0">• Affirm bond</text>
  </g>

  <!-- Bottom Synthesis Banner -->
  <g transform="translate(35, 360)" filter="url(#shadow7)">
    <rect width="885" height="115" rx="12" fill="#0f172a" stroke="#ea580c" stroke-width="1.5"/>
    <text x="25" y="32" font-family="system-ui, sans-serif" font-size="14" font-weight="800" fill="#fb923c">THE GOLDEN AXIOM OF RESPONSIVE LISTENING:</text>
    <text x="25" y="58" font-family="system-ui, sans-serif" font-size="13" font-style="italic" fill="#f8fafc">&quot;Listen with the conscious intent to understand and validate, rather than merely waiting for your turn to speak.&quot;</text>
    <text x="25" y="84" font-family="system-ui, sans-serif" font-size="11.5" fill="#94a3b8">Effective paraphrasing prevents costly errors, builds psychological safety, and elevates interpersonal relationships.</text>
  </g>
</svg>""", "SVG_INTERACTIVE_LOOP")

# =============================================================================
# CURRICULUM LESSON DATA (LESSONS 4, 5, 6, 7)
# =============================================================================

LESSONS_DATA = [
    # -------------------------------------------------------------------------
    # LESSON 4: Critical Listening: Fact, Opinion, Evidence, and Bias
    # -------------------------------------------------------------------------
    {
        "unit_order": 4,
        "unit_name": "Critical Listening: Fact, Opinion, Evidence, and Bias",
        "unit_description": "Techniques for evaluating spoken arguments, distinguishing verifiable facts from subjective opinions, examining evidence, and identifying speaker bias.",
        "lesson_title": "Critical Listening: Fact, Opinion, Evidence, and Bias",
        "pages": [
            {
                "page_number": 1,
                "page_title": "Discovery & Objectives",
                "blocks": [
                    {
                        "block_type": "suggested_image",
                        "component_type": "suggested_image",
                        "title": "Debaters Presenting Arguments in Formal Competition",
                        "content": {
                            "text": "Secondary school debaters presenting competing claims, requiring listeners to critically test evidence and evaluate bias.",
                            "url": "https://upload.wikimedia.org/wikipedia/commons/4/4f/2019_SSSDC_Division_2_Finals.jpg",
                            "author": "Wikimedia Commons",
                            "licensing": "CC BY-SA 4.0",
                            "commons_page_url": "https://commons.wikimedia.org/wiki/File:2019_SSSDC_Division_2_Finals.jpg"
                        },
                        "metadata": {
                            "caption": "Secondary school debaters presenting competing claims, requiring listeners to critically test evidence and evaluate bias."
                        }
                    },
                    {
                        "block_type": "learning_goal",
                        "component_type": "learning_goal",
                        "title": "Lesson Objectives: Critical Discourse Analysis",
                        "content": {
                            "text": "By the end of this lesson, you will be able to:\n- Distinguish between verifiable facts and subjective opinions in spoken discourse.\n- Evaluate the relevance, authority, and validity of supporting evidence.\n- Identify linguistic markers and logical fallacies that signal speaker bias.\n- Apply a 4-pillar critical listening framework to media broadcasts, debates, and advertisements."
                        }
                    },
                    {
                        "block_type": "concept_explanation",
                        "component_type": "concept_explanation",
                        "title": "Scenario Spark: The Post-Match Football Debate",
                        "content": {
                            "text": "Imagine two students discussing a tournament match:\n\n- **Speaker A:** *\"That game was incredible! Our team is the absolute best in the county, and the referee was completely corrupt!\"*\n- **Speaker B:** *\"Our team maintained 60% possession and made five shots on goal, but lost 1-0 after conceding a penalty in the 88th minute.\"*\n\n**Which speaker provides objective truth?** Speaker B shares verifiable data. Speaker A provides emotional judgments. Critical listening enables you to separate facts from feelings."
                        }
                    }
                ]
            },
            {
                "page_number": 2,
                "page_title": "Core Concepts & Terminology",
                "blocks": [
                    {
                        "block_type": "definition_card",
                        "component_type": "definition_card",
                        "title": "Critical Listening",
                        "content": {
                            "term": "Critical Listening",
                            "definition": "The active process of analyzing, evaluating, and judging the accuracy, logic, and truthfulness of a spoken message before accepting or rejecting its claims."
                        }
                    },
                    {
                        "block_type": "definition_card",
                        "component_type": "definition_card",
                        "title": "Fact vs. Opinion",
                        "content": {
                            "term": "Fact vs. Opinion",
                            "definition": "A **Fact** is an objective statement verifiable by empirical evidence or records. An **Opinion** is a subjective belief, feeling, or value judgment that cannot be proven true or false."
                        }
                    },
                    {
                        "block_type": "definition_card",
                        "component_type": "definition_card",
                        "title": "Evidence and Bias",
                        "content": {
                            "term": "Evidence & Bias",
                            "definition": "**Evidence** comprises specific data, statistics, or expert citations backing a claim. **Bias** is a one-sided preference or prejudice that distorts fair consideration through loaded language or omitted facts."
                        }
                    },
                    {
                        "block_type": "comparison_table",
                        "component_type": "comparison_table",
                        "title": "The Four Analytical Pillars Compared",
                        "content": {
                            "headers": ["Pillar", "Core Definition", "Linguistic Clues", "Verification Method"],
                            "rows": [
                                ["Fact", "Objective, empirical reality.", "Dates, measurements, proper nouns.", "Check official records / archives."],
                                ["Opinion", "Subjective value judgment.", "Adjectives: 'best', 'terrible', 'should'.", "Cannot be proven; personal perspective."],
                                ["Evidence", "Concrete supporting proof.", "\"According to...\", \"data shows...\"", "Verify source methodology and authority."],
                                ["Bias", "One-sided ideological slant.", "Loaded words, omission of counterarguments.", "Identify commercial / political motivation."]
                            ]
                        }
                    }
                ]
            },
            {
                "page_number": 3,
                "page_title": "Model & Structured Analysis",
                "blocks": [
                    {
                        "block_type": "diagram",
                        "component_type": "suggested_diagram",
                        "title": "Critical Listening Framework Architecture",
                        "content": {
                            "svg_code": SVG_CRITICAL_LISTENING,
                            "title": "Critical Listening Framework Architecture",
                            "caption": "The 4-pillar analysis matrix illustrating Fact, Opinion, Evidence, and Bias with evaluation criteria and spoken models."
                        },
                        "metadata": {"svg_content": SVG_CRITICAL_LISTENING}
                    },
                    {
                        "block_type": "model_dialogue",
                        "component_type": "model_dialogue",
                        "title": "Model Analysis: Deconstructing a Radio Advertisement",
                        "content": {
                            "intro": "Examine this spoken radio commercial transcript and note how critical listening exposes commercial persuasion:",
                            "dialogue": [
                                {"speaker": "Voiceover", "text": "\"Are you tired of slow internet? TurboNet is the ultimate internet provider in the country! Our fiber network is 10 times faster than standard connections, as certified by the National Telecom Authority. Switch to TurboNet today—the only smart choice for intelligent people!\""},
                                {"speaker": "Critical Breakdown 1 (Fact & Evidence)", "text": "\"Our fiber network is 10 times faster... as certified by the National Telecom Authority\" is a verifiable claim backed by an independent government regulator."},
                                {"speaker": "Critical Breakdown 2 (Opinion)", "text": "\"TurboNet is the ultimate provider\" and \"the only smart choice\" are subjective marketing claims designed to flatter the listener."},
                                {"speaker": "Critical Breakdown 3 (Detected Bias)", "text": "The ad uses loaded emotional words ('terrible', 'ultimate', 'smart') and conceals monthly subscription costs, installation fees, and coverage boundaries."}
                            ]
                        }
                    }
                ]
            },
            {
                "page_number": 4,
                "page_title": "Media Integration & Listening Lab",
                "blocks": [
                    {
                        "block_type": "suggested_video",
                        "component_type": "suggested_video",
                        "title": "Facts vs. Opinions in Media Discussions",
                        "content": {
                            "youtube_id": "LrHhkfkNdqE",
                            "url": "https://www.youtube.com/watch?v=LrHhkfkNdqE",
                            "title": "Distinguishing Fact from Opinion in Broadcast Media",
                            "description": "Video tutorial examining how news panels, speeches, and advertisements blend factual evidence with persuasive rhetorical opinions."
                        }
                    },
                    {
                        "block_type": "listening_lab",
                        "component_type": "listening_lab",
                        "title": "Media Literacy Lab: Detecting Rhetorical Slant",
                        "content": {
                            "intro": "Master the art of isolating data from rhetorical persuasion during spoken presentations.",
                            "pre_viewing_task": "**Pre-Viewing Objective**: Listen for qualifying phrases such as 'In my perspective', 'Research confirms', or 'It is widely believed'. Prepare a two-column chart: Column 1 for Objective Evidence, Column 2 for Subjective Interpretations.",
                            "post_viewing_discussion": "**Post-Viewing Analysis & Discussion**: Why do speakers in media debates often present opinions with high vocal confidence? Does speaker volume change the factual validity of an argument?",
                            "exercises": [
                                {
                                    "task": "Pre-Viewing Task",
                                    "instruction": "Listen for qualifying phrases such as 'In my perspective', 'Research confirms', or 'It is widely believed'."
                                },
                                {
                                    "task": "Post-Viewing Analysis & Discussion",
                                    "instruction": "Why do speakers in debates often present opinions with high vocal confidence? Does speaker volume change the factual validity of an argument?"
                                }
                            ]
                        }
                    }
                ]
            },
            {
                "page_number": 5,
                "page_title": "Common Mistakes & Guided Practice",
                "blocks": [
                    {
                        "block_type": "common_mistakes",
                        "component_type": "common_mistakes",
                        "title": "Frequent Pitfalls in Critical Listening",
                        "content": {
                            "mistakes": [
                                {
                                    "mistake": "Confusing Speaker Confidence with Factual Truth",
                                    "why_it_happens": "Listeners often assume charismatic, loud, or passionate speakers are stating undeniable facts.",
                                    "correction": "Always decouple delivery style from empirical evidence. Demand citations, verifiable data, and logical consistency."
                                },
                                {
                                    "mistake": "Dismissing All Opinions as Worthless",
                                    "why_it_happens": "Assuming only hard numbers have value in academic discourse.",
                                    "correction": "Informed opinions backed by expert reasoning and corroborating evidence are crucial for decision-making."
                                }
                            ]
                        }
                    },
                    {
                        "block_type": "guided_practice",
                        "component_type": "guided_practice",
                        "title": "Guided Exercise: Discourse Classification",
                        "content": {
                            "instruction": "Classify each spoken statement below as Fact, Opinion, or Evidence-backed claim:",
                            "items": [
                                {"prompt": "1. \"Mathematics is the most difficult subject in high school.\"", "answer": "**OPINION** (Difficulty is subjective and varies by individual learner)."},
                                {"prompt": "2. \"The school science laboratory contains exactly 24 light microscopes.\"", "answer": "**FACT** (Objective and verifiable through physical inventory)."},
                                {"prompt": "3. \"According to the KNBS 2024 survey, agricultural exports increased by 8.5%.\"", "answer": "**FACT WITH EVIDENCE** (Verifiable empirical claim supported by official source attribution)."},
                                {"prompt": "4. \"He is an incompetent student leader because he rarely speaks at assemblies.\"", "answer": "**OPINION / BIAS** (Subjective value judgment equating public speaking frequency with leadership quality)."}
                            ]
                        }
                    },
                    {
                        "block_type": "mini_activity",
                        "component_type": "mini_activity",
                        "title": "Independent Analysis Drill",
                        "content": {
                            "task": "Listen to a radio editorial, podcast debate, or school assembly speech today. Write down 1 stated fact, 1 personal opinion, and any detected one-sided bias."
                        }
                    }
                ]
            },
            {
                "page_number": 6,
                "page_title": "Knowledge Check & Summary",
                "blocks": [
                    {
                        "block_type": "knowledge_check",
                        "component_type": "knowledge_check",
                        "title": "Knowledge Check 1: Identifying Objective Facts",
                        "content": {
                            "question": "Which of the following spoken statements represents an objective Fact?",
                            "options": [
                                "The guest speaker gave an exceptionally inspiring speech yesterday.",
                                "The school board meeting lasted for two hours and forty-five minutes.",
                                "Students who take humanities courses are naturally friendlier than science students.",
                                "Our high school offers the absolute best learning environment in the county."
                            ],
                            "correct": "B",
                            "correct_answer": "B",
                            "explanation": "Option B is correct because the duration of a meeting can be objectively measured with a clock and confirmed independently. Options A, C, and D contain subjective evaluations ('exceptionally inspiring', 'naturally friendlier', 'absolute best') which cannot be empirically proven."
                        }
                    },
                    {
                        "block_type": "knowledge_check",
                        "component_type": "knowledge_check",
                        "title": "Knowledge Check 2: Recognizing Bias",
                        "content": {
                            "question": "Which of the following spoken features most strongly indicates the presence of Bias in a speech?",
                            "options": [
                                "Citing data from multiple independent research institutions.",
                                "Presenting both the advantages and disadvantages of a proposed policy.",
                                "Using loaded, emotional language while completely ignoring counter-evidence.",
                                "Speaking in a calm, moderate tone with clear enunciation."
                            ],
                            "correct": "C",
                            "correct_answer": "C",
                            "explanation": "Option C is correct because relying on loaded words and deliberately omitting contrary evidence are classic hallmarks of biased discourse. Options A and B represent balanced, objective analysis."
                        }
                    },
                    {
                        "block_type": "key_takeaway",
                        "component_type": "key_takeaway",
                        "title": "Lesson 4 Summary: Critical Listening Mastery",
                        "content": {
                            "summary": "- **Facts** are objective, empirical, and verifiable independently of feelings.\n- **Opinions** reflect personal values, emotions, and interpretations.\n- **Evidence** validates claims through data, surveys, and expert citations.\n- **Bias** skews objective understanding through loaded phrasing and omissions.\n- **Axiom:** Always evaluate the merit of the argument, not merely the charm of the speaker."
                        }
                    }
                ]
            }
        ]
    },

    # -------------------------------------------------------------------------
    # LESSON 5: Intensive Listening and Viewing for Details
    # -------------------------------------------------------------------------
    {
        "unit_order": 5,
        "unit_name": "Intensive Listening and Viewing for Details",
        "unit_description": "Techniques for extracting specific data, following multi-step instructional sequences, and correlating audio speech with visual cues and screen diagrams.",
        "lesson_title": "Intensive Listening and Viewing for Details",
        "pages": [
            {
                "page_number": 1,
                "page_title": "Discovery & Objectives",
                "blocks": [
                    {
                        "block_type": "suggested_image",
                        "component_type": "suggested_image",
                        "title": "Focused Note-Taking in Academic Setting",
                        "content": {
                            "text": "A student demonstrating intensive listening and structured note-taking during a technical instructional presentation.",
                            "url": "https://upload.wikimedia.org/wikipedia/commons/9/9c/African_Girl_at_Work.jpg",
                            "author": "Wikimedia Commons",
                            "licensing": "CC BY-SA 4.0",
                            "commons_page_url": "https://commons.wikimedia.org/wiki/File:African_Girl_at_Work.jpg"
                        },
                        "metadata": {
                            "caption": "A student demonstrating intensive listening and structured note-taking during a technical instructional presentation."
                        }
                    },
                    {
                        "block_type": "learning_goal",
                        "component_type": "learning_goal",
                        "title": "Lesson Objectives: Precision Listening & Viewing",
                        "content": {
                            "text": "By the end of this lesson, you will be able to:\n- Differentiate intensive listening from extensive listening based on cognitive focus.\n- Extract exact numerical data, technical terminology, and multi-step procedures from audio.\n- Cross-check and synthesize spoken instructions with on-screen visual diagrams.\n- Implement selective shorthand note-taking during rapid instructional presentations."
                        }
                    },
                    {
                        "block_type": "concept_explanation",
                        "component_type": "concept_explanation",
                        "title": "Scenario Spark: Following Complex Directions",
                        "content": {
                            "text": "Imagine asking a stranger for directions to a hospital in an unfamiliar town:\n\n> *\"Walk straight for 200 meters. When you see the red brick pharmacy on your left, turn right onto Tembo Lane. Pass the supermarket, and the hospital emergency gate is the third gate on your right, directly opposite the post office.\"*\n\nCan you reach your destination with only 'gist' listening? **No!** If you only recall *'walk straight and turn somewhere'*, you will get lost. Intensive listening requires locking onto every precise detail: **200m, red brick on left, turn right, Tembo Lane, pass supermarket, 3rd gate on right, opposite post office**."
                        }
                    }
                ]
            },
            {
                "page_number": 2,
                "page_title": "Core Concepts & Terminology",
                "blocks": [
                    {
                        "block_type": "definition_card",
                        "component_type": "definition_card",
                        "title": "Intensive Listening & Viewing",
                        "content": {
                            "term": "Intensive Listening",
                            "definition": "The focused, analytical processing of short spoken or audiovisual texts to extract precise details, sequential instructions, and specific grammatical or technical data."
                        }
                    },
                    {
                        "block_type": "definition_card",
                        "component_type": "definition_card",
                        "title": "Visual Cues & Triangulation",
                        "content": {
                            "term": "Visual Triangulation",
                            "definition": "The cognitive process of correlating spoken commentary with on-screen diagrams, facial expressions, slide bullet points, and presenter gestures to ensure 100% accuracy."
                        }
                    },
                    {
                        "block_type": "definition_card",
                        "component_type": "definition_card",
                        "title": "Discourse Sequence Markers",
                        "content": {
                            "term": "Sequence Markers",
                            "definition": "Structural transition words (*'First', 'Subsequently', 'Prior to', 'Finally'*) that signal chronological steps and procedural relationships in instructional speech."
                        }
                    },
                    {
                        "block_type": "comparison_table",
                        "component_type": "comparison_table",
                        "title": "Intensive vs. Extensive Listening Comparison",
                        "content": {
                            "headers": ["Feature", "Intensive Listening", "Extensive Listening"],
                            "rows": [
                                ["Primary Purpose", "Extract exact details, numbers, and sequence steps.", "Grasp overall gist, main themes, and general narrative."],
                                ["Text Length", "Short, dense passages (30 sec – 3 min).", "Longer audio/video passages (5 – 30 min)."],
                                ["Attention Focus", "Micro-units: specific nouns, numbers, connectors.", "Macro-units: general context, speaker attitude."],
                                ["Visual Integration", "Scrutinizing technical charts, code, and slide text.", "General environmental and situational awareness."]
                            ]
                        }
                    }
                ]
            },
            {
                "page_number": 3,
                "page_title": "Model & Structured Analysis",
                "blocks": [
                    {
                        "block_type": "diagram",
                        "component_type": "suggested_diagram",
                        "title": "Intensive Detail Extraction Protocol",
                        "content": {
                            "svg_code": SVG_INTENSIVE_LISTENING,
                            "title": "Intensive Detail Extraction Protocol",
                            "caption": "4-stage workflow covering Sound Filtering, Sequence Tracking, Shorthand Recording, and Multi-Modal Triangulation."
                        },
                        "metadata": {"svg_content": SVG_INTENSIVE_LISTENING}
                    },
                    {
                        "block_type": "model_dialogue",
                        "component_type": "model_dialogue",
                        "title": "Model Analysis: Digital Portal Setup Instructions",
                        "content": {
                            "intro": "Analyze how an intensive listener decodes this technical IT instruction:",
                            "dialogue": [
                                {"speaker": "IT Instructor", "text": "\"To log in, open your browser and navigate to the portal address. First, type your student admission number. Next, enter the temporary password 'Learn2026' with a capital 'L'. Finally, click the blue 'Submit' button on-screen. Do not press 'Enter' on your physical keyboard.\""},
                                {"speaker": "Listener Step 1", "text": "Extracted Action 1: Navigate to portal via browser."},
                                {"speaker": "Listener Step 2", "text": "Extracted Action 2: Username = Admission Number."},
                                {"speaker": "Listener Step 3", "text": "Extracted Action 3: Password = 'Learn2026' (Precision check: Capital 'L')."},
                                {"speaker": "Listener Critical Caveat", "text": "Mandatory Warning: Click the blue on-screen button; do NOT press keyboard Enter."}
                            ]
                        }
                    }
                ]
            },
            {
                "page_number": 4,
                "page_title": "Media Integration & Listening Lab",
                "blocks": [
                    {
                        "block_type": "suggested_video",
                        "component_type": "suggested_video",
                        "title": "Intensive vs. Extensive Listening in Practice",
                        "content": {
                            "youtube_id": "p8lQ_40tq_c",
                            "url": "https://www.youtube.com/watch?v=p8lQ_40tq_c",
                            "title": "Mastering Detail Extraction in English Audio",
                            "description": "Educational guide detailing strategies for training your ear to capture micro-details, grammatical markers, and fast-paced speech."
                        }
                    },
                    {
                        "block_type": "listening_lab",
                        "component_type": "listening_lab",
                        "title": "Detail Extraction Lab: Emergency Protocol",
                        "content": {
                            "intro": "Practice selective shorthand note-taking for high-stakes instructions.",
                            "pre_viewing_task": "**Pre-Viewing Objective**: Prepare your notebook with four discrete columns: Step Number, Action Verb, Metric / Value, and Safety Warning before the audio begins.",
                            "post_viewing_discussion": "**Post-Viewing Analysis & Discussion**: Compare your extracted notes with a partner. Did both of you record the exact same sequence numbers and caveat warnings without omission?",
                            "exercises": [
                                {
                                    "task": "Pre-Viewing Preparation",
                                    "instruction": "Prepare your notebook with columns for: Step Number, Action Verb, Metric / Value, and Safety Warning."
                                },
                                {
                                    "task": "Active Audio Processing",
                                    "instruction": "Listen to a fast instructional recording once. Record only keywords, numbers, and symbols without pausing the track."
                                },
                                {
                                    "task": "Post-Viewing Analysis & Discussion",
                                    "instruction": "Compare your extracted notes with a partner. Did both of you record the exact same sequence numbers and caveat warnings without omission?"
                                }
                            ]
                        }
                    }
                ]
            },
            {
                "page_number": 5,
                "page_title": "Common Mistakes & Guided Practice",
                "blocks": [
                    {
                        "block_type": "common_mistakes",
                        "component_type": "common_mistakes",
                        "title": "Frequent Intensive Listening Errors",
                        "content": {
                            "mistakes": [
                                {
                                    "mistake": "Attempting Verbatim Word-for-Word Transcription",
                                    "why_it_happens": "Learners try to write full sentences, falling behind the speaker's natural delivery rate.",
                                    "correction": "Use shorthand notation, standard abbreviations (&, ->, w/, min), and focus strictly on content nouns and numerals."
                                },
                                {
                                    "mistake": "Ignoring On-Screen Graphics During Video Lectures",
                                    "why_it_happens": "Focusing solely on the acoustic voice while missing visual confirmations on slides.",
                                    "correction": "Synchronize visual slides with spoken words to verify spelling, code syntax, and spatial relations."
                                }
                            ]
                        }
                    },
                    {
                        "block_type": "guided_practice",
                        "component_type": "guided_practice",
                        "title": "Guided Exercise: First Aid Shorthand Notes",
                        "content": {
                            "instruction": "Read the spoken emergency first aid transcript and examine the extracted precision notes:",
                            "items": [
                                {"prompt": "\"If someone cuts their finger, first, wash the wound under cool running water for exactly 2 minutes. Next, apply gentle pressure with a clean cloth. Then apply antiseptic cream and wrap firmly with a sterile bandage. If bleeding continues past 10 minutes, seek urgent medical help.\"", "answer": "1. Wash: 2 min cool water.\n2. Pressure: Clean cloth.\n3. Medicate: Antiseptic cream.\n4. Dress: Sterile bandage firmly.\n5. Warning: Hospital if bleeding > 10 min."}
                            ]
                        }
                    }
                ]
            },
            {
                "page_number": 6,
                "page_title": "Knowledge Check & Summary",
                "blocks": [
                    {
                        "block_type": "knowledge_check",
                        "component_type": "knowledge_check",
                        "title": "Knowledge Check 1: Sequence Markers",
                        "content": {
                            "question": "Which of the following transition markers explicitly introduces the final, concluding step in a multi-step spoken procedure?",
                            "options": [
                                "First and foremost",
                                "Meanwhile",
                                "Consequently",
                                "Finally"
                            ],
                            "correct": "D",
                            "correct_answer": "D",
                            "explanation": "Option D ('Finally') is the standard discourse marker signaling the terminal step of an instructional sequence. 'First' signals the opening, 'Meanwhile' signals concurrent events, and 'Consequently' denotes causality."
                        }
                    },
                    {
                        "block_type": "knowledge_check",
                        "component_type": "knowledge_check",
                        "title": "Knowledge Check 2: Effective Note-Taking",
                        "content": {
                            "question": "What is the most effective strategy when taking notes during an intensive listening session?",
                            "options": [
                                "Attempt to write down every single word the speaker utters.",
                                "Record only key content nouns, action verbs, numbers, and sequence symbols.",
                                "Ignore numerical values and record only broad generalizations.",
                                "Stop listening completely whenever an unfamiliar word is spoken."
                            ],
                            "correct": "B",
                            "correct_answer": "B",
                            "explanation": "Option B is correct because capturing content words and numbers using shorthand allows your note-taking speed to match natural speech while preserving critical technical details."
                        }
                    },
                    {
                        "block_type": "key_takeaway",
                        "component_type": "key_takeaway",
                        "title": "Lesson 5 Summary: Intensive Listening Essentials",
                        "content": {
                            "summary": "- **Intensive listening** targets micro-level accuracy: figures, proper nouns, and sequential rules.\n- **Discourse markers** (*First, Next, Prior to, Finally*) provide the procedural skeleton of spoken text.\n- **Shorthand note-taking** captures essential data points without falling behind speaker pace.\n- **Multi-modal viewing** fuses acoustic words with on-screen visual graphics for zero ambiguity."
                        }
                    }
                ]
            }
        ]
    },

    # -------------------------------------------------------------------------
    # LESSON 6: Non-verbal Communication and Conversational Skills
    # -------------------------------------------------------------------------
    {
        "unit_order": 6,
        "unit_name": "Non-verbal Communication and Conversational Skills",
        "unit_description": "Mastery of body language, paralanguage, kinesics, proxemics, eye contact, and conversational repair techniques to resolve communication breakdowns.",
        "lesson_title": "Non-verbal Communication and Conversational Skills",
        "pages": [
            {
                "page_number": 1,
                "page_title": "Discovery & Objectives",
                "blocks": [
                    {
                        "block_type": "suggested_image",
                        "component_type": "suggested_image",
                        "title": "Interpersonal Discourse and Body Language Cues",
                        "content": {
                            "text": "Two communicators demonstrating dynamic non-verbal interaction: attentive posture, open hand gestures, and steady eye contact.",
                            "url": "https://upload.wikimedia.org/wikipedia/commons/5/5c/TwoWomenTalkingBodyLanguage.jpg",
                            "author": "Wikimedia Commons",
                            "licensing": "CC BY 2.0",
                            "commons_page_url": "https://commons.wikimedia.org/wiki/File:TwoWomenTalkingBodyLanguage.jpg"
                        },
                        "metadata": {
                            "caption": "Two communicators demonstrating dynamic non-verbal interaction: attentive posture, open hand gestures, and steady eye contact."
                        }
                    },
                    {
                        "block_type": "learning_goal",
                        "component_type": "learning_goal",
                        "title": "Lesson Objectives: Non-Verbal Mastery & Repair",
                        "content": {
                            "text": "By the end of this lesson, you will be able to:\n- Identify and interpret the four non-verbal communication channels (kinesics, oculesics, paralanguage, proxemics).\n- Demonstrate active backchanneling through subtle head nods, facial signals, and verbal tokens.\n- Deploy 3 professional conversational repair formulas to resolve misunderstandings in real time.\n- Align your body language with spoken words to communicate with confidence and poise."
                        }
                    },
                    {
                        "block_type": "concept_explanation",
                        "component_type": "concept_explanation",
                        "title": "Scenario Spark: The Assembly Address",
                        "content": {
                            "text": "Imagine two student leaders presenting during a school assembly:\n\n- **Speaker A:** Stands slumped over the podium, fixes eyes on the floor, mumbles in a flat monotone, and keeps hands shoved inside trouser pockets.\n- **Speaker B:** Stands tall, smiles warmly, maintains natural eye contact across the auditorium, uses open hand gestures for emphasis, and speaks with varied pitch and pace.\n\nEven if their written speeches were identical, **Speaker B** captivates and persuades the audience. Non-verbal signals either amplify or undermine spoken messages."
                        }
                    }
                ]
            },
            {
                "page_number": 2,
                "page_title": "Core Concepts & Terminology",
                "blocks": [
                    {
                        "block_type": "definition_card",
                        "component_type": "definition_card",
                        "title": "Non-Verbal Communication",
                        "content": {
                            "term": "Non-Verbal Communication",
                            "definition": "The transfer of information and emotional nuance through body posture, facial expressions, eye movements, voice characteristics, and physical distance."
                        }
                    },
                    {
                        "block_type": "definition_card",
                        "component_type": "definition_card",
                        "title": "Paralanguage (Vocalics)",
                        "content": {
                            "term": "Paralanguage",
                            "definition": "The non-lexical vocal elements of speech—including pitch, volume, cadence, intonation, and strategic pauses—that convey mood, emphasis, and intent."
                        }
                    },
                    {
                        "block_type": "definition_card",
                        "component_type": "definition_card",
                        "title": "Conversational Repair",
                        "content": {
                            "term": "Conversational Repair",
                            "definition": "The set of communicative techniques used by speakers and listeners to fix breakdowns in hearing, pronunciation, vocabulary, or comprehension during live dialogue."
                        }
                    },
                    {
                        "block_type": "comparison_table",
                        "component_type": "comparison_table",
                        "title": "The Four Channels of Non-Verbal Communication",
                        "content": {
                            "headers": ["Channel / Term", "Scientific Domain", "Physical Manifestation", "Positive Conversational Impact"],
                            "rows": [
                                ["Kinesics", "Body Movement & Posture", "Open hand gestures, erect posture, nodding.", "Builds rapport, projects confidence, reinforces key words."],
                                ["Oculesics", "Eye Gaze Behavior", "Comfortable direct eye contact (4–5 sec intervals).", "Signifies honesty, active engagement, and mutual respect."],
                                ["Paralanguage", "Vocal Inflection & Pace", "Dynamic pitch range, clear volume, timed pauses.", "Prevents monotone delivery and conveys emotional warmth."],
                                ["Proxemics", "Personal Space", "Culturally appropriate distance (0.5m – 1.2m).", "Respects personal boundaries and professional decorum."]
                            ]
                        }
                    }
                ]
            },
            {
                "page_number": 3,
                "page_title": "Model & Structured Analysis",
                "blocks": [
                    {
                        "block_type": "diagram",
                        "component_type": "suggested_diagram",
                        "title": "Non-Verbal Channels & Repair Engine",
                        "content": {
                            "svg_code": SVG_NONVERBAL_REPAIR,
                            "title": "Non-Verbal Channels & Repair Engine",
                            "caption": "Comprehensive architecture showing the 4 non-verbal channels on the left and the 3-step Conversational Repair Engine on the right."
                        },
                        "metadata": {"svg_content": SVG_NONVERBAL_REPAIR}
                    },
                    {
                        "block_type": "model_dialogue",
                        "component_type": "model_dialogue",
                        "title": "Model Dialogue: Deploying Conversational Repair",
                        "content": {
                            "intro": "Study how communicators gracefully resolve conversational friction using formal repair strategies:",
                            "dialogue": [
                                {"speaker": "Speaker 1 (Ambiguous term)", "text": "\"We need to expedite the logistical disbursement before the symposium tomorrow.\""},
                                {"speaker": "Speaker 2 (Semantic Clarification)", "text": "\"I apologize, could you please clarify what you mean by 'logistical disbursement'? Are we printing the schedule or preparing the hall?\""},
                                {"speaker": "Speaker 1 (Speaker Self-Correction)", "text": "\"Thank you for asking—pardon my jargon, I meant we must print and distribute the event schedules to all delegates by 4:00 PM today.\""},
                                {"speaker": "Speaker 2 (Backchannel Affirmation)", "text": "\"Ah, I see! Perfect. I will handle the printing right away.\""}
                            ]
                        }
                    }
                ]
            },
            {
                "page_number": 4,
                "page_title": "Media Integration & Listening Lab",
                "blocks": [
                    {
                        "block_type": "suggested_video",
                        "component_type": "suggested_video",
                        "title": "Body Language & Active Listening in Practice",
                        "content": {
                            "youtube_id": "_vhQBFf4z3E",
                            "url": "https://www.youtube.com/watch?v=_vhQBFf4z3E",
                            "title": "Non-Verbal Dynamics and Rapport Building",
                            "description": "Video tutorial exploring the profound impact of eye contact, body orientation, and backchanneling in interpersonal and group conversations."
                        }
                    },
                    {
                        "block_type": "listening_lab",
                        "component_type": "listening_lab",
                        "title": "Backchanneling & Feedback Lab",
                        "content": {
                            "intro": "Train yourself to provide continuous, supportive non-verbal feedback without interrupting the speaker.",
                            "pre_viewing_task": "**Pre-Viewing Objective**: Watch the speaker's body posture, eye movements, and facial micro-expressions. Identify three subtle non-verbal signals that communicate openness.",
                            "post_viewing_discussion": "**Post-Viewing Reflection & Discussion**: How does active backchanneling (nodding, smiling, subtle vocal tokens) alter the speaker's confidence and fluency during a conversation?",
                            "exercises": [
                                {
                                    "task": "Pre-Viewing Task",
                                    "instruction": "Watch the speaker's body posture, eye movements, and facial micro-expressions. Identify three subtle non-verbal signals that communicate openness."
                                },
                                {
                                    "task": "Non-Verbal Tokens",
                                    "instruction": "Practice gentle head nods, warm facial expressions, and leaning slightly forward while someone speaks."
                                },
                                {
                                    "task": "Verbal Tokens",
                                    "instruction": "Incorporate subtle low-volume markers: 'Mm-hmm', 'I see', 'Right', 'Understood', 'Indeed'."
                                },
                                {
                                    "task": "Post-Viewing Reflection & Discussion",
                                    "instruction": "How does active backchanneling (nodding, smiling, subtle vocal tokens) alter the speaker's confidence and fluency during a conversation?"
                                }
                            ]
                        }
                    }
                ]
            },
            {
                "page_number": 5,
                "page_title": "Common Mistakes & Guided Practice",
                "blocks": [
                    {
                        "block_type": "common_mistakes",
                        "component_type": "common_mistakes",
                        "title": "Non-Verbal Pitfalls to Avoid",
                        "content": {
                            "mistakes": [
                                {
                                    "mistake": "Crossing Arms Defensively Across the Chest",
                                    "why_it_happens": "People often cross their arms when cold or resting, unaware of the negative social signal.",
                                    "correction": "Crossed arms subconsciously signal defensiveness, stubbornness, or closed-mindedness. Rest hands openly at sides or on the desk."
                                },
                                {
                                    "mistake": "Unblinking Stare or Constant Floor Gazing",
                                    "why_it_happens": "Nervousness causes people to either stare aggressively without blinking or look down at the floor.",
                                    "correction": "Maintain comfortable, intermittent eye contact (holding for 4-5 seconds, looking away briefly, and returning gaze)."
                                }
                            ]
                        }
                    },
                    {
                        "block_type": "guided_practice",
                        "component_type": "guided_practice",
                        "title": "Guided Exercise: Body Language Interpretation",
                        "content": {
                            "instruction": "Match each physical cue with its most accurate conversational interpretation:",
                            "items": [
                                {"prompt": "1. Listener leans forward slightly and nods head periodically.", "answer": "**HIGH ENGAGEMENT & AGREEMENT** (Demonstrates active processing and encouragement)."},
                                {"prompt": "2. Student avoids eye contact and hunches shoulders when questioned.", "answer": "**APPREHENSION / UNPREPAREDNESS** (Desire to remain unnoticed or uncertainty)."},
                                {"prompt": "3. Rapid tapping of fingers on table while repeatedly glancing at wrist clock.", "answer": "**IMPATIENCE / RESTLESSNESS** (Urge to end the interaction quickly)."}
                            ]
                        }
                    },
                    {
                        "block_type": "role_play_activity",
                        "component_type": "role_play_activity",
                        "title": "Interactive Role-Play: The Repair Drill",
                        "content": {
                            "scenario": "With a peer, simulate a phone call with poor reception. Practice using formal repair phrases: 'Could you please repeat that?', 'What do you mean by...?', and 'Pardon me, I meant...'."
                        }
                    }
                ]
            },
            {
                "page_number": 6,
                "page_title": "Knowledge Check & Summary",
                "blocks": [
                    {
                        "block_type": "knowledge_check",
                        "component_type": "knowledge_check",
                        "title": "Knowledge Check 1: Positive Non-Verbal Signals",
                        "content": {
                            "question": "Which of the following behaviors is universally recognized as a positive, encouraging non-verbal signal during a formal interview?",
                            "options": [
                                "Checking your watch periodically to monitor meeting duration.",
                                "Maintaining gentle, intermittent eye contact while nodding in agreement.",
                                "Slumping deeply into the chair with arms tightly folded.",
                                "Staring intently at the ceiling while the interviewer explains a question."
                            ],
                            "correct": "B",
                            "correct_answer": "B",
                            "explanation": "Option B is correct because soft, steady eye contact combined with affirmative nodding communicates undivided attention, respect, and confidence. Options A, C, and D exhibit disengaged or defensive body language."
                        }
                    },
                    {
                        "block_type": "knowledge_check",
                        "component_type": "knowledge_check",
                        "title": "Knowledge Check 2: Conversational Repair",
                        "content": {
                            "question": "If you mispronounce a date or name during a formal presentation, what is the best conversational repair technique?",
                            "options": [
                                "Pretend nothing happened and continue without correcting the error.",
                                "Stop the entire presentation and apologize profusely for five minutes.",
                                "Execute a quick self-correction: 'Excuse me, I meant Friday at 10:00 AM' and proceed smoothly.",
                                "Blame the audience for misunderstanding your initial statement."
                            ],
                            "correct": "C",
                            "correct_answer": "C",
                            "explanation": "Option C is correct because an immediate, concise self-correction eliminates factual confusion without derailing the presentation flow or undermining your confidence."
                        }
                    },
                    {
                        "block_type": "key_takeaway",
                        "component_type": "key_takeaway",
                        "title": "Lesson 6 Summary: Non-Verbal & Conversational Mastery",
                        "content": {
                            "summary": "- **Non-verbal communication** comprises kinesics (body), oculesics (eyes), vocalics (voice), and proxemics (space).\n- **Active backchanneling** (nodding, 'I see') encourages the speaker and verifies listener presence.\n- **Conversational repair** provides diplomatic formulas to request repetition, clarify terms, and self-correct slips.\n- **Harmony:** Great communicators align vocal tone, posture, and facial expression with their words."
                        }
                    }
                ]
            }
        ]
    },

    # -------------------------------------------------------------------------
    # LESSON 7: Interactive and Responsive Listening
    # -------------------------------------------------------------------------
    {
        "unit_order": 7,
        "unit_name": "Interactive and Responsive Listening",
        "unit_description": "Advanced interpersonal communication skills: paraphrasing, formulating clarifying questions, empathetic validation, and closing the communication loop.",
        "lesson_title": "Interactive and Responsive Listening",
        "pages": [
            {
                "page_number": 1,
                "page_title": "Discovery & Objectives",
                "blocks": [
                    {
                        "block_type": "suggested_image",
                        "component_type": "suggested_image",
                        "title": "Collaborative Dialogue and Responsive Listening",
                        "content": {
                            "text": "A high-level collaborative meeting illustrating interactive listening: paraphrasing ideas, validating concerns, and asking clarifying questions.",
                            "url": "https://upload.wikimedia.org/wikipedia/commons/a/a5/Dean_Rusk%2C_Lyndon_B._Johnson_and_Robert_McNamara_in_Cabinet_Room_meeting_February_1968.jpg",
                            "author": "Wikimedia Commons / National Archives",
                            "licensing": "Public domain",
                            "commons_page_url": "https://commons.wikimedia.org/wiki/File:Dean_Rusk,_Lyndon_B._Johnson_and_Robert_McNamara_in_Cabinet_Room_meeting_February_1968.jpg"
                        },
                        "metadata": {
                            "caption": "A high-level collaborative meeting illustrating interactive listening: paraphrasing ideas, validating concerns, and asking clarifying questions."
                        }
                    },
                    {
                        "block_type": "learning_goal",
                        "component_type": "learning_goal",
                        "title": "Lesson Objectives: Responsive Interpersonal Listening",
                        "content": {
                            "text": "By the end of this lesson, you will be able to:\n- Differentiate passive listening from interactive and responsive listening.\n- Formulate accurate, respectful paraphrasing stems to confirm mutual comprehension.\n- Construct targeted clarifying questions without disrupting speaker momentum.\n- Execute the 5-stage interactive listening feedback loop in academic, family, and workplace settings."
                        }
                    },
                    {
                        "block_type": "concept_explanation",
                        "component_type": "concept_explanation",
                        "title": "Scenario Spark: A Classmate in Distress",
                        "content": {
                            "text": "Imagine a classmate rushes up to you in panic:\n\n> *\"I spent three hours finishing my English project, and then my laptop crashed and corrupted the document! The deadline is in two hours and I don't know what to do!\"*\n\n- **Passive Response:** *\"That's too bad. Are you coming to basketball practice later?\"*\n- **Responsive / Interactive Response:** *\"Oh no, I am so sorry to hear that! So, if I understand correctly, your draft was deleted and you're worried about missing the 2:00 PM deadline? Let's go explain the situation to Mr. Omondi together right now.\"*\n\nNotice how the responsive listener **restates the core problem**, **validates the emotion**, and **collaborates on a constructive solution**."
                        }
                    }
                ]
            },
            {
                "page_number": 2,
                "page_title": "Core Concepts & Terminology",
                "blocks": [
                    {
                        "block_type": "definition_card",
                        "component_type": "definition_card",
                        "title": "Interactive and Responsive Listening",
                        "content": {
                            "term": "Responsive Listening",
                            "definition": "A cooperative communication process where the listener actively reflects, checks, clarifies, and responds to both the factual content and emotional subtext of the speaker."
                        }
                    },
                    {
                        "block_type": "definition_card",
                        "component_type": "definition_card",
                        "title": "Paraphrasing",
                        "content": {
                            "term": "Paraphrasing",
                            "definition": "Restating the speaker's core message in your own fresh words (*'So, what you are essentially saying is...'*) to verify comprehension and prove attentive engagement."
                        }
                    },
                    {
                        "block_type": "definition_card",
                        "component_type": "definition_card",
                        "title": "The Feedback Loop",
                        "content": {
                            "term": "Feedback Loop",
                            "definition": "The continuous two-way cycle of sending, receiving, interpreting, reflecting, and validating messages between dialogue partners until mutual understanding is achieved."
                        }
                    },
                    {
                        "block_type": "comparison_table",
                        "component_type": "comparison_table",
                        "title": "Passive vs. Interactive Responsive Listening",
                        "content": {
                            "headers": ["Dimension", "Passive Listening", "Interactive Responsive Listening"],
                            "rows": [
                                ["Listener Role", "Silent, inert sponge absorbing sound waves.", "Active conversational partner in a two-way feedback loop."],
                                ["Cognitive Processing", "Minimal; merely waiting for one's turn to talk.", "Deep; decodes facts, subtext, and emotional tone."],
                                ["Comprehension Check", "Assumes understanding without verification.", "Uses paraphrasing: 'So if I understand correctly...'"],
                                ["Emotional Impact", "Leaves speaker feeling unheard and isolated.", "Fosters psychological safety, trust, and alignment."]
                            ]
                        }
                    }
                ]
            },
            {
                "page_number": 3,
                "page_title": "Model & Structured Analysis",
                "blocks": [
                    {
                        "block_type": "diagram",
                        "component_type": "suggested_diagram",
                        "title": "5-Stage Interactive Feedback Loop",
                        "content": {
                            "svg_code": SVG_INTERACTIVE_LOOP,
                            "title": "5-Stage Interactive Feedback Loop",
                            "caption": "The continuous 5-stage loop: Receive -> Process -> Paraphrase -> Clarify -> Respond with Validation."
                        },
                        "metadata": {"svg_content": SVG_INTERACTIVE_LOOP}
                    },
                    {
                        "block_type": "model_dialogue",
                        "component_type": "model_dialogue",
                        "title": "Model Dialogue: Academic Project Negotiation",
                        "content": {
                            "intro": "Observe how a student and teacher use the responsive listening loop to eliminate assignment ambiguity:",
                            "dialogue": [
                                {"speaker": "Teacher", "text": "\"For your term history project, you must submit a concise analytical summary of a national monument, supplemented by a creative visual aid.\""},
                                {"speaker": "Student (Stage 4: Clarify)", "text": "\"Excuse me, Teacher. Could you please clarify what you mean by a 'concise summary'? How many words should it be?\""},
                                {"speaker": "Teacher", "text": "\"Excellent question! It should be strictly between 150 and 200 words.\""},
                                {"speaker": "Student (Stage 3: Paraphrase)", "text": "\"So, if I understand correctly, we are to write a one-page summary under 200 words and bring in either an original drawing, model, or photograph of the monument?\""},
                                {"speaker": "Teacher (Stage 5: Validate)", "text": "\"Exactly! That is precisely what is required. Well done.\""}
                            ]
                        }
                    }
                ]
            },
            {
                "page_number": 4,
                "page_title": "Media Integration & Listening Lab",
                "blocks": [
                    {
                        "block_type": "suggested_video",
                        "component_type": "suggested_video",
                        "title": "The Art of Active & Responsive Listening",
                        "content": {
                            "youtube_id": "aCutWBCCMaA",
                            "url": "https://www.youtube.com/watch?v=aCutWBCCMaA",
                            "title": "Responsive Listening & Empathy in Dialogue",
                            "description": "Video guide analyzing the cognitive architecture of responsive listening, empathetic reflection, and avoiding conversational narcissism."
                        }
                    },
                    {
                        "block_type": "listening_lab",
                        "component_type": "listening_lab",
                        "title": "Paraphrasing Formula Lab",
                        "content": {
                            "intro": "Master standard conversational sentence stems to reframe complex ideas respectfully without sounding robotic:",
                            "pre_viewing_task": "**Pre-Viewing Objective**: Observe how the listeners in the dialogue refrain from offering premature solutions, focusing first on verifying the speaker's core message.",
                            "post_viewing_discussion": "**Post-Viewing Analysis & Discussion**: Why is empathetic paraphrasing more effective at resolving conflict than immediately defending your own position?",
                            "exercises": [
                                {
                                    "task": "Pre-Viewing Task",
                                    "instruction": "Observe how the listeners in the dialogue refrain from offering premature solutions, focusing first on verifying the speaker's core message."
                                },
                                {
                                    "task": "Verification Stem 1",
                                    "instruction": "\"So, what you are essentially saying is that [core idea]... Is that accurate?\""
                                },
                                {
                                    "task": "Verification Stem 2",
                                    "instruction": "\"If I understand your main perspective correctly, you feel that [emotion + situation]...\""
                                },
                                {
                                    "task": "Verification Stem 3",
                                    "instruction": "\"In other words, from your vantage point, the priority should be [action item]...\""
                                },
                                {
                                    "task": "Post-Viewing Discussion",
                                    "instruction": "Why is empathetic paraphrasing more effective at resolving conflict than immediately defending your own position?"
                                }
                            ]
                        }
                    }
                ]
            },
            {
                "page_number": 5,
                "page_title": "Common Mistakes & Guided Practice",
                "blocks": [
                    {
                        "block_type": "common_mistakes",
                        "component_type": "common_mistakes",
                        "title": "Pitfalls in Responsive Listening",
                        "content": {
                            "mistakes": [
                                {
                                    "mistake": "Conversational Hijacking (Me-First Listening)",
                                    "why_it_happens": "Responding to someone's distress by immediately launching into a personal story ('Oh, you think that's bad? Wait until you hear what happened to me!').",
                                    "correction": "Keep the spotlight on the speaker until their message and emotions are fully explored and validated."
                                },
                                {
                                    "mistake": "Robotic or Parrot-like Repetition",
                                    "why_it_happens": "Repeating the speaker's exact phrases back to them word-for-word without synthesizing the meaning.",
                                    "correction": "Translate the speaker's thoughts into your own fresh vocabulary to demonstrate genuine cognitive comprehension."
                                }
                            ]
                        }
                    },
                    {
                        "block_type": "guided_practice",
                        "component_type": "guided_practice",
                        "title": "Guided Exercise: Paraphrasing Makeovers",
                        "content": {
                            "instruction": "Transform these raw speaker statements into professional, empathetic paraphrases:",
                            "items": [
                                {
                                    "prompt": "Statement 1: \"I really want to go to university, but my family's income is very low and I'm deeply worried about tuition fees.\"",
                                    "answer": "Paraphrase: *\"So, if I understand correctly, you are strongly motivated to pursue higher education, but you feel anxious about the financial burden of tuition on your family.\"*"
                                },
                                {
                                    "prompt": "Statement 2: \"The school computer lab is always packed after classes, and I can never complete my programming assignments on time.\"",
                                    "answer": "Paraphrase: *\"So what you're saying is that high lab congestion after hours is preventing you from getting the computer access you need to finish your schoolwork.\"*"
                                }
                            ]
                        }
                    }
                ]
            },
            {
                "page_number": 6,
                "page_title": "Knowledge Check & Summary",
                "blocks": [
                    {
                        "block_type": "knowledge_check",
                        "component_type": "knowledge_check",
                        "title": "Knowledge Check 1: Formulating Paraphrases",
                        "content": {
                            "question": "Which of the following phrases is the most effective and polite way to begin a paraphrase to verify your understanding of a speaker's point?",
                            "options": [
                                "You are completely wrong about that, because in my view...",
                                "Let me tell you how I solved a much worse problem...",
                                "So, if I understand you correctly, what you are saying is that...",
                                "Why would you ever believe something like that?"
                            ],
                            "correct": "C",
                            "correct_answer": "C",
                            "explanation": "Option C is correct because it introduces a polite, objective restatement of the speaker's idea for verification without judgment. Option A is confrontational, Option B hijacks the conversation, and Option D is an aggressive challenge."
                        }
                    },
                    {
                        "block_type": "knowledge_check",
                        "component_type": "knowledge_check",
                        "title": "Knowledge Check 2: Active Feedback Loop",
                        "content": {
                            "question": "What is the primary objective of the 'Feedback Loop' in interpersonal communication?",
                            "options": [
                                "To allow the listener to dominate the talking time.",
                                "To verify mutual understanding between speaker and listener before acting.",
                                "To identify every minor grammatical mistake made by the speaker.",
                                "To speed up the conversation by avoiding all questions."
                            ],
                            "correct": "B",
                            "correct_answer": "B",
                            "explanation": "Option B is correct because the feedback loop ensures both participants share identical comprehension of facts and feelings, preventing costly errors and building trust."
                        }
                    },
                    {
                        "block_type": "key_takeaway",
                        "component_type": "key_takeaway",
                        "title": "Lesson 7 Summary: Interactive Listening Principles",
                        "content": {
                            "summary": "- **Interactive listening** transforms a one-way monologue into a shared understanding.\n- **The 5-Stage Feedback Loop:** 1. Receive -> 2. Process -> 3. Paraphrase -> 4. Clarify -> 5. Respond.\n- **Paraphrasing formulas** (*'If I understand correctly...'*) verify facts and establish psychological safety.\n- **Empathetic validation** acknowledges speaker emotions before jumping to advice or solutions."
                        }
                    }
                ]
            }
        ]
    }
]

# =============================================================================
# INGESTION PIPELINE EXECUTION
# =============================================================================

def run_ingestion():
    print("=" * 80)
    print("VLearn Production Ingestion: Grade 10 English (Topic 1: Lessons 4 to 7)")
    print("=" * 80)

    # 1. Resolve Grade 10 CBC
    grade = Grade.objects.filter(id=5).first() or Grade.objects.filter(curriculum__name="CBC", level=10).first()
    if not grade:
        raise ValueError("Grade ID 5 (Grade 10 CBC) not found!")

    # 2. Resolve / Create Subject: English
    subject, s_created = Subject.objects.get_or_create(
        grade=grade,
        name="English",
        defaults={"description": "Senior Secondary English Curriculum (Grade 10 CBC)"}
    )
    print(f"[*] Subject: '{subject.name}' (ID: {subject.id}, Created: {s_created}) in Grade: '{grade.name}' (ID: {grade.id})")

    # 3. Resolve / Create Topic 1: Listening and Speaking
    topic, t_created = Topic.objects.get_or_create(
        subject=subject,
        order=1,
        defaults={
            "name": "Listening and Speaking",
            "description": "Mastery of oral communication, pronunciation, critical and intensive listening, non-verbal cues, and responsive dialogue."
        }
    )
    if not t_created:
        topic.name = "Listening and Speaking"
        topic.description = "Mastery of oral communication, pronunciation, critical and intensive listening, non-verbal cues, and responsive dialogue."
        topic.save()
    print(f"[*] Topic 1: '{topic.name}' (ID: {topic.id}, Created: {t_created})")

    total_units_created = 0
    total_lessons_created = 0
    total_blocks_created = 0
    total_assets_created = 0

    with transaction.atomic():
        for les_data in LESSONS_DATA:
            u_order = les_data["unit_order"]
            u_name = clean_text(les_data["unit_name"])
            u_desc = clean_text(les_data["unit_description"])
            les_title = clean_text(les_data["lesson_title"])

            # 4. LearningUnit (Order matches lesson unit_order: 4, 5, 6, 7)
            unit, u_created = LearningUnit.objects.get_or_create(
                topic=topic,
                order=u_order,
                defaults={
                    "name": u_name,
                    "description": u_desc
                }
            )
            unit.name = u_name
            unit.description = u_desc
            unit.save()
            total_units_created += 1

            # 5. Lesson
            lesson, l_created = Lesson.objects.get_or_create(
                topic=topic,
                learning_unit=unit,
                defaults={
                    "title": les_title,
                    "status": "published",
                    "version": 1,
                    "immutable_metadata": {
                        "author": "VLearn Senior English Curriculum Specialist",
                        "grade": "Grade 10",
                        "subject": "English",
                        "topic_order": 1,
                        "unit_order": u_order
                    }
                }
            )
            lesson.title = les_title
            lesson.status = "published"
            lesson.version = 1
            lesson.immutable_metadata = {
                "author": "VLearn Senior English Curriculum Specialist",
                "grade": "Grade 10",
                "subject": "English",
                "topic_order": 1,
                "unit_order": u_order
            }
            lesson.save()
            total_lessons_created += 1

            # Clean previous blocks & assets for this lesson for idempotency
            LessonAsset.objects.filter(lesson=lesson).delete()
            lesson.blocks.all().delete()

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

                    elif (b_type in ["diagram", "suggested_diagram"]) and ("svg_code" in b_content or "svg_content" in b_meta):
                        svg_data = b_content.get("svg_code") or b_meta.get("svg_content", "")
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
    print("Ingestion Completed Successfully!")
    print(f"  Subject:          {subject.name} (Grade 10 CBC, ID: {subject.id})")
    print(f"  Topic:            {topic.name} (Order: {topic.order}, ID: {topic.id})")
    print(f"  Units Ingested:   {total_units_created}")
    print(f"  Lessons Ingested: {total_lessons_created}")
    print(f"  Blocks Created:   {total_blocks_created}")
    print(f"  Assets Attached:  {total_assets_created}")
    print("=" * 80)

    return {
        "subject_id": subject.id,
        "topic_id": topic.id,
        "units": total_units_created,
        "lessons": total_lessons_created,
        "blocks": total_blocks_created,
        "assets": total_assets_created
    }

if __name__ == "__main__":
    run_ingestion()
