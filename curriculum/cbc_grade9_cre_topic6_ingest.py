"""
VLearn CBC Grade 9 CRE — Topic 6: Healing of the Ten Lepers
Complete Topic Ingestion Script (All 6 Lessons)

Grade: Grade 9 (ID: 18)
Subject: CRE (ID: 50)
Topic: Healing of the Ten Lepers (Order: 6)

Lessons:
1. Lesson 1: Understanding Leprosy and Social Outcasts (Leviticus 13-14, Luke 17:11-12)
2. Lesson 2: The Cry for Mercy and the Command of Faith (Luke 17:12-14)
3. Lesson 3: The Miracle of Healing and the Outcast's Return (Luke 17:14-16)
4. Lesson 4: Jesus' Profound Questions and Teachings (Luke 17:17-19)
5. Lesson 5: Faith and Gratitude: Lessons for Teenagers (1 Thessalonians 5:16-18, Psalm 103:1-5)
6. Lesson 6: Practicing Gratitude in Daily Life (Colossians 3:15-17)

Every lesson contains:
- 6 Cards/Pages
- 13 Blocks (standardized block_type)
- 3 LessonAssets (Image, SVG Diagram, YouTube Video)
"""

import os
import sys
import re
import django
from django.db import transaction

# Setup Django Environment
sys.path.append("/home/jason-bitega/Desktop/VL/vlearn_repositories/Vlearn_backend")
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "Nexus_backend.settings")
django.setup()

from curriculum.models import (
    Grade, Subject, Topic, LearningUnit, Lesson, LessonBlock, LessonAsset
)


def clean_text(text: str) -> str:
    """Removes bracket citations, internal tags, and cleans formatting."""
    if not text:
        return ""
    # Strip bracket citations e.g. [841], [841, 842], [841-845]
    text = re.sub(r'\[(?:\d+(?:\.\d+)?(?:,\s*\d+(?:\.\d+)?)*|[\d,\s\-]{2,})\]', '', text)
    # Strip internal pedagogical tags
    text = re.sub(
        r'\[(VISUAL|BIBLE REFERENCE|BIBLE PASSAGE|REAL WORLD APPLICATION|REFLECTION|CRITICAL THINKING|VALUES|MISCONCEPTION|INTERACTION|ETHICAL SCENARIO|KEY VERSE|BIBLICAL CONTEXT|PEDAGOGICAL ARCHITECTURE|PROJECT TITLE)[^\]]*\]',
        '', text, flags=re.IGNORECASE
    )
    # Normalize list bullet points
    text = re.sub(r'^[ \t]*[•\u2022][ \t]*', '- ', text, flags=re.MULTILINE)
    text = re.sub(r'([^\n])[ \t]+[•\u2022][ \t]+', r'\1\n- ', text)
    # Clean redundant spaces around punctuation
    text = re.sub(r' +([,.;:!?])', r'\1', text)
    return text.strip()


def clean_dict(data):
    if isinstance(data, str):
        return clean_text(data)
    elif isinstance(data, dict):
        return {k: clean_dict(v) for k, v in data.items()}
    elif isinstance(data, list):
        return [clean_dict(item) for item in data]
    return data


# ─── CUSTOM RESPONSIVE VECTOR SVGS (viewBox="0 0 800 450", #0f172a theme) ─────

def get_svg_lesson1():
    return """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 450" width="100%" height="100%">
  <defs>
    <linearGradient id="bgGrad1" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#0f172a"/>
      <stop offset="50%" stop-color="#1e293b"/>
      <stop offset="100%" stop-color="#0f172a"/>
    </linearGradient>
    <linearGradient id="roseGrad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#e11d48"/>
      <stop offset="100%" stop-color="#be123c"/>
    </linearGradient>
    <linearGradient id="amberGrad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#d97706"/>
      <stop offset="100%" stop-color="#b45309"/>
    </linearGradient>
    <linearGradient id="cyanGrad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#0284c7"/>
      <stop offset="100%" stop-color="#0369a1"/>
    </linearGradient>
    <linearGradient id="slateGrad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#475569"/>
      <stop offset="100%" stop-color="#334155"/>
    </linearGradient>
  </defs>

  <rect width="800" height="450" fill="url(#bgGrad1)" rx="14"/>
  <rect x="15" y="15" width="770" height="420" fill="none" stroke="#334155" stroke-width="1.5" stroke-dasharray="6 4" rx="10"/>

  <text x="400" y="44" fill="#38bdf8" font-family="system-ui, -apple-system, sans-serif" font-size="18" font-weight="800" text-anchor="middle" letter-spacing="0.5">THE REALITY OF LEPROSY: PATHOLOGY &amp; LEVITICAL QUARANTINE</text>
  <text x="400" y="66" fill="#94a3b8" font-family="system-ui, -apple-system, sans-serif" font-size="12" text-anchor="middle">Understanding the Physical Suffering, Ritual Uncleanliness, and Absolute Social Exclusion</text>

  <path d="M 195 210 L 225 210 M 385 210 L 415 210 M 575 210 L 605 210" stroke="#64748b" stroke-width="3" stroke-dasharray="4 4"/>
  <polygon points="228,210 220,205 220,215" fill="#f43f5e"/>
  <polygon points="418,210 410,205 410,215" fill="#fbbf24"/>
  <polygon points="608,210 600,205 600,215" fill="#38bdf8"/>

  <!-- CARD 1: Physical Suffering -->
  <g transform="translate(30, 90)">
    <rect width="165" height="250" rx="10" fill="#1e293b" stroke="#f43f5e" stroke-width="1.5"/>
    <rect width="165" height="34" rx="10" fill="url(#roseGrad)"/>
    <text x="82" y="22" fill="#ffffff" font-family="system-ui, sans-serif" font-size="12" font-weight="700" text-anchor="middle">1. PHYSICAL TOLL</text>
    <rect x="18" y="44" width="130" height="20" rx="10" fill="#e11d48" fill-opacity="0.25"/>
    <text x="82" y="58" fill="#fda4af" font-family="system-ui, sans-serif" font-size="10" font-weight="600" text-anchor="middle">Bacterial Infection</text>
    <text x="12" y="90" fill="#f8fafc" font-family="system-ui, sans-serif" font-size="11" font-weight="700">• Symptoms:</text>
    <text x="12" y="106" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10">Nerve damage, white</text>
    <text x="12" y="120" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10">lesions, loss of feeling.</text>
    <text x="12" y="146" fill="#f8fafc" font-family="system-ui, sans-serif" font-size="11" font-weight="700">• Deformities:</text>
    <text x="12" y="162" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10">Decay of extremities,</text>
    <text x="12" y="176" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10">open chronic sores.</text>
    <text x="12" y="202" fill="#f8fafc" font-family="system-ui, sans-serif" font-size="11" font-weight="700">• Status:</text>
    <text x="12" y="218" fill="#fda4af" font-family="system-ui, sans-serif" font-size="10">Living death in antiquity.</text>
  </g>

  <!-- CARD 2: Levitical Law -->
  <g transform="translate(220, 90)">
    <rect width="165" height="250" rx="10" fill="#1e293b" stroke="#f59e0b" stroke-width="1.5"/>
    <rect width="165" height="34" rx="10" fill="url(#amberGrad)"/>
    <text x="82" y="22" fill="#ffffff" font-family="system-ui, sans-serif" font-size="12" font-weight="700" text-anchor="middle">2. LEVITICUS 13-14</text>
    <rect x="18" y="44" width="130" height="20" rx="10" fill="#d97706" fill-opacity="0.25"/>
    <text x="82" y="58" fill="#fde68a" font-family="system-ui, sans-serif" font-size="10" font-weight="600" text-anchor="middle">Priestly Diagnosis</text>
    <text x="12" y="90" fill="#f8fafc" font-family="system-ui, sans-serif" font-size="11" font-weight="700">• Ritual State:</text>
    <text x="12" y="106" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10">Declared 'Unclean'</text>
    <text x="12" y="120" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10">by Aaron's priests.</text>
    <text x="12" y="146" fill="#f8fafc" font-family="system-ui, sans-serif" font-size="11" font-weight="700">• Religious Ban:</text>
    <text x="12" y="162" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10">Barred from Temple,</text>
    <text x="12" y="176" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10">sacrifices &amp; feasts.</text>
    <text x="12" y="202" fill="#f8fafc" font-family="system-ui, sans-serif" font-size="11" font-weight="700">• Legal Authority:</text>
    <text x="12" y="218" fill="#fde68a" font-family="system-ui, sans-serif" font-size="10">Priests alone certify cure.</text>
  </g>

  <!-- CARD 3: Social Quarantine -->
  <g transform="translate(410, 90)">
    <rect width="165" height="250" rx="10" fill="#1e293b" stroke="#38bdf8" stroke-width="1.5"/>
    <rect width="165" height="34" rx="10" fill="url(#cyanGrad)"/>
    <text x="82" y="22" fill="#ffffff" font-family="system-ui, sans-serif" font-size="12" font-weight="700" text-anchor="middle">3. SOCIAL EXCLUSION</text>
    <rect x="18" y="44" width="130" height="20" rx="10" fill="#0284c7" fill-opacity="0.25"/>
    <text x="82" y="58" fill="#7dd3fc" font-family="system-ui, sans-serif" font-size="10" font-weight="600" text-anchor="middle">Complete Isolation</text>
    <text x="12" y="90" fill="#f8fafc" font-family="system-ui, sans-serif" font-size="11" font-weight="700">• Eviction:</text>
    <text x="12" y="106" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10">Forced outside city</text>
    <text x="12" y="120" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10">walls to live in caves.</text>
    <text x="12" y="146" fill="#f8fafc" font-family="system-ui, sans-serif" font-size="11" font-weight="700">• Family Severance:</text>
    <text x="12" y="162" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10">No contact with</text>
    <text x="12" y="176" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10">spouses, children, kin.</text>
    <text x="12" y="202" fill="#f8fafc" font-family="system-ui, sans-serif" font-size="11" font-weight="700">• Outcast Camps:</text>
    <text x="12" y="218" fill="#7dd3fc" font-family="system-ui, sans-serif" font-size="10">Lepers banded together.</text>
  </g>

  <!-- CARD 4: The Warning Cry -->
  <g transform="translate(600, 90)">
    <rect width="170" height="250" rx="10" fill="#1e293b" stroke="#94a3b8" stroke-width="1.5"/>
    <rect width="170" height="34" rx="10" fill="url(#slateGrad)"/>
    <text x="85" y="22" fill="#ffffff" font-family="system-ui, sans-serif" font-size="12" font-weight="700" text-anchor="middle">4. THE MANDATE</text>
    <rect x="20" y="44" width="130" height="20" rx="10" fill="#475569" fill-opacity="0.25"/>
    <text x="85" y="58" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10" font-weight="600" text-anchor="middle">'Unclean! Unclean!'</text>
    <text x="12" y="90" fill="#f8fafc" font-family="system-ui, sans-serif" font-size="11" font-weight="700">• Dress Code:</text>
    <text x="12" y="106" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10">Torn clothes, unkempt</text>
    <text x="12" y="120" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10">hair, covering mouth.</text>
    <text x="12" y="146" fill="#f8fafc" font-family="system-ui, sans-serif" font-size="11" font-weight="700">• Distance Rule:</text>
    <text x="12" y="162" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10">Must stay 100 paces</text>
    <text x="12" y="176" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10">away from clean people.</text>
    <text x="12" y="202" fill="#f8fafc" font-family="system-ui, sans-serif" font-size="11" font-weight="700">• Humiliation:</text>
    <text x="12" y="218" fill="#e2e8f0" font-family="system-ui, sans-serif" font-size="10">Perpetual public shame.</text>
  </g>

  <!-- Bottom Insight Banner -->
  <rect x="30" y="360" width="740" height="56" rx="8" fill="#1e293b" stroke="#334155" stroke-width="1"/>
  <text x="400" y="384" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="12" font-weight="700" text-anchor="middle">THEOLOGICAL SIGNIFICANCE: TOTAL HELPLESSNESS MEETS DIVINE GRACE</text>
  <text x="400" y="402" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="11" text-anchor="middle">Leprosy in Scripture symbolizes the devastating alienation of sin—only Jesus can bridge the distance and restore communion.</text>
</svg>"""


def get_svg_lesson2():
    return """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 450" width="100%" height="100%">
  <defs>
    <linearGradient id="bgGrad2" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#0f172a"/>
      <stop offset="50%" stop-color="#1e293b"/>
      <stop offset="100%" stop-color="#0f172a"/>
    </linearGradient>
    <linearGradient id="step1Grad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#0284c7"/>
      <stop offset="100%" stop-color="#0369a1"/>
    </linearGradient>
    <linearGradient id="step2Grad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#d97706"/>
      <stop offset="100%" stop-color="#b45309"/>
    </linearGradient>
    <linearGradient id="step3Grad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#7c3aed"/>
      <stop offset="100%" stop-color="#6d28d9"/>
    </linearGradient>
    <linearGradient id="step4Grad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#059669"/>
      <stop offset="100%" stop-color="#047857"/>
    </linearGradient>
  </defs>

  <rect width="800" height="450" fill="url(#bgGrad2)" rx="14"/>
  <rect x="15" y="15" width="770" height="420" fill="none" stroke="#334155" stroke-width="1.5" stroke-dasharray="6 4" rx="10"/>

  <text x="400" y="44" fill="#38bdf8" font-family="system-ui, -apple-system, sans-serif" font-size="18" font-weight="800" text-anchor="middle" letter-spacing="0.5">THE PATHWAY OF ACTIVE FAITH: CRY, COMMAND &amp; OBEDIENCE</text>
  <text x="400" y="66" fill="#94a3b8" font-family="system-ui, -apple-system, sans-serif" font-size="12" text-anchor="middle">How the Ten Lepers Moved from Desperate Isolation to Healing Through Obedient Steps</text>

  <!-- Connecting Pathway Lines -->
  <path d="M 195 210 L 225 210 M 385 210 L 415 210 M 575 210 L 605 210" stroke="#475569" stroke-width="3" stroke-dasharray="6 4"/>
  <polygon points="228,210 218,204 218,216" fill="#38bdf8"/>
  <polygon points="418,210 408,204 408,216" fill="#fbbf24"/>
  <polygon points="608,210 598,204 598,216" fill="#a78bfa"/>

  <!-- STEP 1: Standing at Distance -->
  <g transform="translate(30, 90)">
    <rect width="165" height="250" rx="10" fill="#1e293b" stroke="#38bdf8" stroke-width="1.5"/>
    <rect width="165" height="34" rx="10" fill="url(#step1Grad)"/>
    <text x="82" y="22" fill="#ffffff" font-family="system-ui, sans-serif" font-size="12" font-weight="700" text-anchor="middle">1. STANDING FAR OFF</text>
    <rect x="18" y="44" width="130" height="20" rx="10" fill="#0284c7" fill-opacity="0.25"/>
    <text x="82" y="58" fill="#7dd3fc" font-family="system-ui, sans-serif" font-size="10" font-weight="600" text-anchor="middle">Border of Samaria</text>
    <text x="12" y="90" fill="#f8fafc" font-family="system-ui, sans-serif" font-size="11" font-weight="700">• Context:</text>
    <text x="12" y="106" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10">Ten outcasts united</text>
    <text x="12" y="120" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10">across ethnic lines.</text>
    <text x="12" y="146" fill="#f8fafc" font-family="system-ui, sans-serif" font-size="11" font-weight="700">• Legal Boundary:</text>
    <text x="12" y="162" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10">Obeyed quarantine;</text>
    <text x="12" y="176" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10">did not mob Jesus.</text>
    <text x="12" y="202" fill="#f8fafc" font-family="system-ui, sans-serif" font-size="11" font-weight="700">• Common Pain:</text>
    <text x="12" y="218" fill="#7dd3fc" font-family="system-ui, sans-serif" font-size="10">Suffering broke prejudice.</text>
  </g>

  <!-- STEP 2: The Cry for Mercy -->
  <g transform="translate(220, 90)">
    <rect width="165" height="250" rx="10" fill="#1e293b" stroke="#f59e0b" stroke-width="1.5"/>
    <rect width="165" height="34" rx="10" fill="url(#step2Grad)"/>
    <text x="82" y="22" fill="#ffffff" font-family="system-ui, sans-serif" font-size="12" font-weight="700" text-anchor="middle">2. THE CRY OF FAITH</text>
    <rect x="18" y="44" width="130" height="20" rx="10" fill="#d97706" fill-opacity="0.25"/>
    <text x="82" y="58" fill="#fde68a" font-family="system-ui, sans-serif" font-size="10" font-weight="600" text-anchor="middle">'Master, Have Mercy!'</text>
    <text x="12" y="90" fill="#f8fafc" font-family="system-ui, sans-serif" font-size="11" font-weight="700">• Title 'Master':</text>
    <text x="12" y="106" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10">Recognized Christ's</text>
    <text x="12" y="120" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10">sovereign authority.</text>
    <text x="12" y="146" fill="#f8fafc" font-family="system-ui, sans-serif" font-size="11" font-weight="700">• Cry for Pity:</text>
    <text x="12" y="162" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10">Asked not for money,</text>
    <text x="12" y="176" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10">but divine restoration.</text>
    <text x="12" y="202" fill="#f8fafc" font-family="system-ui, sans-serif" font-size="11" font-weight="700">• Unity in Voice:</text>
    <text x="12" y="218" fill="#fde68a" font-family="system-ui, sans-serif" font-size="10">Shouted in unison.</text>
  </g>

  <!-- STEP 3: The Testing Command -->
  <g transform="translate(410, 90)">
    <rect width="165" height="250" rx="10" fill="#1e293b" stroke="#a78bfa" stroke-width="1.5"/>
    <rect width="165" height="34" rx="10" fill="url(#step3Grad)"/>
    <text x="82" y="22" fill="#ffffff" font-family="system-ui, sans-serif" font-size="12" font-weight="700" text-anchor="middle">3. THE COMMAND</text>
    <rect x="18" y="44" width="130" height="20" rx="10" fill="#7c3aed" fill-opacity="0.25"/>
    <text x="82" y="58" fill="#c4b5fd" font-family="system-ui, sans-serif" font-size="10" font-weight="600" text-anchor="middle">'Go Show the Priests'</text>
    <text x="12" y="90" fill="#f8fafc" font-family="system-ui, sans-serif" font-size="11" font-weight="700">• No Immediate Touch:</text>
    <text x="12" y="106" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10">Sores remained visible</text>
    <text x="12" y="120" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10">when Jesus spoke.</text>
    <text x="12" y="146" fill="#f8fafc" font-family="system-ui, sans-serif" font-size="11" font-weight="700">• Legal Protocol:</text>
    <text x="12" y="162" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10">Priests inspected</text>
    <text x="12" y="176" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10">healed persons only.</text>
    <text x="12" y="202" fill="#f8fafc" font-family="system-ui, sans-serif" font-size="11" font-weight="700">• The Test:</text>
    <text x="12" y="218" fill="#c4b5fd" font-family="system-ui, sans-serif" font-size="10">Act before seeing result.</text>
  </g>

  <!-- STEP 4: Obedient Walking -->
  <g transform="translate(600, 90)">
    <rect width="170" height="250" rx="10" fill="#1e293b" stroke="#34d399" stroke-width="1.5"/>
    <rect width="170" height="34" rx="10" fill="url(#step4Grad)"/>
    <text x="85" y="22" fill="#ffffff" font-family="system-ui, sans-serif" font-size="12" font-weight="700" text-anchor="middle">4. OBEDIENCE ON ROAD</text>
    <rect x="20" y="44" width="130" height="20" rx="10" fill="#059669" fill-opacity="0.25"/>
    <text x="85" y="58" fill="#6ee7b7" font-family="system-ui, sans-serif" font-size="10" font-weight="600" text-anchor="middle">Miracle on the Journey</text>
    <text x="12" y="90" fill="#f8fafc" font-family="system-ui, sans-serif" font-size="11" font-weight="700">• Step of Trust:</text>
    <text x="12" y="106" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10">They turned and walked</text>
    <text x="12" y="120" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10">while still leprous.</text>
    <text x="12" y="146" fill="#f8fafc" font-family="system-ui, sans-serif" font-size="11" font-weight="700">• The Transformation:</text>
    <text x="12" y="162" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10">'As they went, they</text>
    <text x="12" y="176" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10">were cleansed!'</text>
    <text x="12" y="202" fill="#f8fafc" font-family="system-ui, sans-serif" font-size="11" font-weight="700">• Principle:</text>
    <text x="12" y="218" fill="#6ee7b7" font-family="system-ui, sans-serif" font-size="10">Action releases power.</text>
  </g>

  <!-- Bottom Banner -->
  <rect x="30" y="360" width="740" height="56" rx="8" fill="#1e293b" stroke="#334155" stroke-width="1"/>
  <text x="400" y="384" fill="#34d399" font-family="system-ui, sans-serif" font-size="12" font-weight="700" text-anchor="middle">FAITH IS AN ACTIVE VERB: OBEYING BEFORE THE VISIBLE RESULT</text>
  <text x="400" y="402" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="11" text-anchor="middle">The ten lepers did not wait to feel better; they stepped out in obedience to Christ's word, and the miracle happened mid-journey.</text>
</svg>"""


def get_svg_lesson3():
    return """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 450" width="100%" height="100%">
  <defs>
    <linearGradient id="bgGrad3" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#0f172a"/>
      <stop offset="50%" stop-color="#1e293b"/>
      <stop offset="100%" stop-color="#0f172a"/>
    </linearGradient>
    <linearGradient id="nineGrad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#64748b"/>
      <stop offset="100%" stop-color="#475569"/>
    </linearGradient>
    <linearGradient id="oneGrad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#059669"/>
      <stop offset="100%" stop-color="#047857"/>
    </linearGradient>
  </defs>

  <rect width="800" height="450" fill="url(#bgGrad3)" rx="14"/>
  <rect x="15" y="15" width="770" height="420" fill="none" stroke="#334155" stroke-width="1.5" stroke-dasharray="6 4" rx="10"/>

  <text x="400" y="44" fill="#38bdf8" font-family="system-ui, -apple-system, sans-serif" font-size="18" font-weight="800" text-anchor="middle" letter-spacing="0.5">THE DIVERGENT RESPONSES: THE NINE VS. THE ONE SAMARITAN</text>
  <text x="400" y="66" fill="#94a3b8" font-family="system-ui, -apple-system, sans-serif" font-size="12" text-anchor="middle">Physical Cleansing on the Road and the Shocking Return of the Despised Foreigner</text>

  <!-- Split Comparison Layout -->
  <!-- Left Side: The Nine Jewish Lepers -->
  <g transform="translate(40, 95)">
    <rect width="340" height="245" rx="10" fill="#1e293b" stroke="#64748b" stroke-width="1.5"/>
    <rect width="340" height="38" rx="10" fill="url(#nineGrad)"/>
    <text x="170" y="24" fill="#ffffff" font-family="system-ui, sans-serif" font-size="14" font-weight="700" text-anchor="middle">THE NINE: RUSHING TO PRIESTS</text>
    
    <text x="20" y="66" fill="#f8fafc" font-family="system-ui, sans-serif" font-size="12" font-weight="700">• Identity:</text>
    <text x="20" y="84" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="11.5">Likely Jewish insiders who knew the Law.</text>

    <text x="20" y="112" fill="#f8fafc" font-family="system-ui, sans-serif" font-size="12" font-weight="700">• Action:</text>
    <text x="20" y="130" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="11.5">Kept running forward to secure ritual clearance.</text>

    <text x="20" y="158" fill="#f8fafc" font-family="system-ui, sans-serif" font-size="12" font-weight="700">• Focus:</text>
    <text x="20" y="176" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="11.5">The GIFT rather than the GIVER (self-restoration).</text>

    <text x="20" y="204" fill="#f8fafc" font-family="system-ui, sans-serif" font-size="12" font-weight="700">• Result:</text>
    <text x="20" y="222" fill="#94a3b8" font-family="system-ui, sans-serif" font-size="11.5">Physical skin cured; no personal fellowship with Jesus.</text>
  </g>

  <!-- Right Side: The One Grateful Samaritan -->
  <g transform="translate(420, 95)">
    <rect width="340" height="245" rx="10" fill="#1e293b" stroke="#10b981" stroke-width="2"/>
    <rect width="340" height="38" rx="10" fill="url(#oneGrad)"/>
    <text x="170" y="24" fill="#ffffff" font-family="system-ui, sans-serif" font-size="14" font-weight="700" text-anchor="middle">THE ONE: THE RETURNING SAMARITAN</text>
    
    <text x="20" y="66" fill="#f8fafc" font-family="system-ui, sans-serif" font-size="12" font-weight="700">• Identity:</text>
    <text x="20" y="84" fill="#6ee7b7" font-family="system-ui, sans-serif" font-size="11.5">A Samaritan foreigner, despised and outcast by Jews.</text>

    <text x="20" y="112" fill="#f8fafc" font-family="system-ui, sans-serif" font-size="12" font-weight="700">• Action:</text>
    <text x="20" y="130" fill="#a7f3d0" font-family="system-ui, sans-serif" font-size="11.5">Turned back immediately with a loud voice of praise.</text>

    <text x="20" y="158" fill="#f8fafc" font-family="system-ui, sans-serif" font-size="12" font-weight="700">• Posture:</text>
    <text x="20" y="176" fill="#a7f3d0" font-family="system-ui, sans-serif" font-size="11.5">Fell flat at Jesus' feet in profound humility &amp; worship.</text>

    <text x="20" y="204" fill="#f8fafc" font-family="system-ui, sans-serif" font-size="12" font-weight="700">• Result:</text>
    <text x="20" y="222" fill="#34d399" font-family="system-ui, sans-serif" font-size="11.5">Physical healing + Whole spiritual salvation (Sozo).</text>
  </g>

  <!-- Bottom Takeaway Banner -->
  <rect x="40" y="360" width="720" height="56" rx="8" fill="#1e293b" stroke="#334155" stroke-width="1"/>
  <text x="400" y="384" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="12" font-weight="700" text-anchor="middle">CULTURAL REVERSAL: THE OUTSIDER BECOMES THE HERO OF FAITH</text>
  <text x="400" y="402" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="11" text-anchor="middle">Luke highlights that ethnic privilege does not guarantee gratitude; true worship springs from a humble, thankful heart.</text>
</svg>"""


def get_svg_lesson4():
    return """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 450" width="100%" height="100%">
  <defs>
    <linearGradient id="bgGrad4" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#0f172a"/>
      <stop offset="50%" stop-color="#1e293b"/>
      <stop offset="100%" stop-color="#0f172a"/>
    </linearGradient>
    <linearGradient id="qGrad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#0284c7"/>
      <stop offset="100%" stop-color="#0369a1"/>
    </linearGradient>
    <linearGradient id="sozoGrad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#7c3aed"/>
      <stop offset="100%" stop-color="#6d28d9"/>
    </linearGradient>
  </defs>

  <rect width="800" height="450" fill="url(#bgGrad4)" rx="14"/>
  <rect x="15" y="15" width="770" height="420" fill="none" stroke="#334155" stroke-width="1.5" stroke-dasharray="6 4" rx="10"/>

  <text x="400" y="44" fill="#38bdf8" font-family="system-ui, -apple-system, sans-serif" font-size="18" font-weight="800" text-anchor="middle" letter-spacing="0.5">JESUS' THREE PENETRATING QUESTIONS &amp; THE SOZO MIRACLE</text>
  <text x="400" y="66" fill="#94a3b8" font-family="system-ui, -apple-system, sans-serif" font-size="12" text-anchor="middle">Distinguishing Between Mere Physical Cleansing (Catharizo) and Complete Spiritual Wholeness (Sozo)</text>

  <!-- Left: 3 Penetrating Questions -->
  <g transform="translate(30, 95)">
    <rect width="350" height="245" rx="10" fill="#1e293b" stroke="#38bdf8" stroke-width="1.5"/>
    <rect width="350" height="38" rx="10" fill="url(#qGrad)"/>
    <text x="175" y="24" fill="#ffffff" font-family="system-ui, sans-serif" font-size="13" font-weight="700" text-anchor="middle">JESUS' 3 QUESTIONS (LUKE 17:17-18)</text>

    <text x="16" y="68" fill="#fde047" font-family="system-ui, sans-serif" font-size="12" font-weight="700">1. 'Were not all ten cleansed?'</text>
    <text x="16" y="86" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="11">Jesus knows the full scope of His sovereign mercy.</text>

    <text x="16" y="122" fill="#fde047" font-family="system-ui, sans-serif" font-size="12" font-weight="700">2. 'Where are the other nine?'</text>
    <text x="16" y="140" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="11">Reveals God's emotional sensitivity to human ingratitude.</text>

    <text x="16" y="176" fill="#fde047" font-family="system-ui, sans-serif" font-size="12" font-weight="700">3. 'Has no one returned except this foreigner?'</text>
    <text x="16" y="194" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="11">Exposes the tragedy of religious complacency.</text>

    <text x="16" y="226" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="10.5" font-weight="600">-> God desires reciprocal relationship, not mere transactions.</text>
  </g>

  <!-- Right: Cleansing vs. Wholeness Comparison -->
  <g transform="translate(410, 95)">
    <rect width="360" height="245" rx="10" fill="#1e293b" stroke="#a78bfa" stroke-width="1.5"/>
    <rect width="360" height="38" rx="10" fill="url(#sozoGrad)"/>
    <text x="180" y="24" fill="#ffffff" font-family="system-ui, sans-serif" font-size="13" font-weight="700" text-anchor="middle">PHYSICAL CLEANSING VS. SOZO SALVATION</text>

    <!-- Top Half: Physical -->
    <rect x="15" y="50" width="330" height="75" rx="6" fill="#334155" fill-opacity="0.6"/>
    <text x="25" y="70" fill="#f8fafc" font-family="system-ui, sans-serif" font-size="11.5" font-weight="700">Physical Cleansing (Catharizo) — Received by 10</text>
    <text x="25" y="88" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10.5">• Skin lesions healed; bodily symptoms erased.</text>
    <text x="25" y="104" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10.5">• Temporary earthly benefit; soul remains unregenerate.</text>

    <!-- Bottom Half: Sozo -->
    <rect x="15" y="135" width="330" height="90" rx="6" fill="#4c1d95" fill-opacity="0.6" stroke="#8b5cf6" stroke-width="1"/>
    <text x="25" y="156" fill="#e9d5ff" font-family="system-ui, sans-serif" font-size="11.5" font-weight="700">Spiritual Wholeness (Sozo) — Received by 1</text>
    <text x="25" y="174" fill="#c4b5fd" font-family="system-ui, sans-serif" font-size="10.5">• 'Rise and go; your faith has made you well (saved you).'</text>
    <text x="25" y="190" fill="#c4b5fd" font-family="system-ui, sans-serif" font-size="10.5">• Eternal peace with God, reconciled soul, true discipleship.</text>
    <text x="25" y="206" fill="#c4b5fd" font-family="system-ui, sans-serif" font-size="10.5">• Gratitude unlocked the higher dimension of the miracle!</text>
  </g>

  <!-- Bottom Banner -->
  <rect x="30" y="360" width="740" height="56" rx="8" fill="#1e293b" stroke="#334155" stroke-width="1"/>
  <text x="400" y="384" fill="#a78bfa" font-family="system-ui, sans-serif" font-size="12" font-weight="700" text-anchor="middle">SOZO: TOTAL RECONCILIATION OF BODY, MIND, AND SPIRIT</text>
  <text x="400" y="402" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="11" text-anchor="middle">Ingratitude leaves us with partial blessings, while thanksgiving brings us into the fullness of Christ's saving presence.</text>
</svg>"""


def get_svg_lesson5():
    return """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 450" width="100%" height="100%">
  <defs>
    <linearGradient id="bgGrad5" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#0f172a"/>
      <stop offset="50%" stop-color="#1e293b"/>
      <stop offset="100%" stop-color="#0f172a"/>
    </linearGradient>
    <linearGradient id="shieldGrad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#059669"/>
      <stop offset="50%" stop-color="#0284c7"/>
      <stop offset="100%" stop-color="#7c3aed"/>
    </linearGradient>
  </defs>

  <rect width="800" height="450" fill="url(#bgGrad5)" rx="14"/>
  <rect x="15" y="15" width="770" height="420" fill="none" stroke="#334155" stroke-width="1.5" stroke-dasharray="6 4" rx="10"/>

  <text x="400" y="44" fill="#38bdf8" font-family="system-ui, -apple-system, sans-serif" font-size="18" font-weight="800" text-anchor="middle" letter-spacing="0.5">THE ADOLESCENT GRATITUDE SHIELD: MENTAL &amp; SPIRITUAL HEALTH</text>
  <text x="400" y="66" fill="#94a3b8" font-family="system-ui, -apple-system, sans-serif" font-size="12" text-anchor="middle">How Daily Thanksgiving (1 Thess 5:18, Ps 103) Protects the Teen Heart Against Toxic Pressures</text>

  <!-- Left: Toxins Gratitude Deflects -->
  <g transform="translate(30, 95)">
    <rect width="220" height="245" rx="10" fill="#1e293b" stroke="#f43f5e" stroke-width="1.5"/>
    <rect width="220" height="34" rx="10" fill="#be123c"/>
    <text x="110" y="22" fill="#ffffff" font-family="system-ui, sans-serif" font-size="12" font-weight="700" text-anchor="middle">DEFLECTED TOXINS</text>
    
    <text x="12" y="65" fill="#fda4af" font-family="system-ui, sans-serif" font-size="11" font-weight="700">1. Chronic Anxiety &amp; Stress</text>
    <text x="12" y="80" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10">Worrying over future exams &amp; status.</text>

    <text x="12" y="110" fill="#fda4af" font-family="system-ui, sans-serif" font-size="11" font-weight="700">2. Envy &amp; Social Comparison</text>
    <text x="12" y="125" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10">Coveting peers' gadgets &amp; popularity.</text>

    <text x="12" y="155" fill="#fda4af" font-family="system-ui, sans-serif" font-size="11" font-weight="700">3. Low Self-Esteem &amp; Emptiness</text>
    <text x="12" y="170" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10">Feeling unworthy or unblessed.</text>

    <text x="12" y="200" fill="#fda4af" font-family="system-ui, sans-serif" font-size="11" font-weight="700">4. Entitlement &amp; Bitterness</text>
    <text x="12" y="215" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10">Resentment toward parents &amp; school.</text>
  </g>

  <!-- Center: The Central Shield SVG -->
  <g transform="translate(275, 95)">
    <path d="M 125 10 Q 240 10 240 100 Q 240 190 125 240 Q 10 190 10 100 Q 10 10 125 10 Z" fill="url(#shieldGrad)" stroke="#38bdf8" stroke-width="2"/>
    <text x="125" y="70" fill="#ffffff" font-family="system-ui, sans-serif" font-size="14" font-weight="800" text-anchor="middle">GRATITUDE</text>
    <text x="125" y="90" fill="#fde047" font-family="system-ui, sans-serif" font-size="13" font-weight="800" text-anchor="middle">SHIELD</text>
    <line x1="50" y1="105" x2="200" y2="105" stroke="#ffffff" stroke-width="1.5" stroke-opacity="0.6"/>
    <text x="125" y="125" fill="#ffffff" font-family="system-ui, sans-serif" font-size="10" font-weight="700" text-anchor="middle">1 THESSALONIANS 5:18</text>
    <text x="125" y="142" fill="#e2e8f0" font-family="system-ui, sans-serif" font-size="9" text-anchor="middle">"Give thanks in all</text>
    <text x="125" y="156" fill="#e2e8f0" font-family="system-ui, sans-serif" font-size="9" text-anchor="middle">circumstances; for this</text>
    <text x="125" y="170" fill="#e2e8f0" font-family="system-ui, sans-serif" font-size="9" text-anchor="middle">is God's will for you."</text>
    <text x="125" y="195" fill="#fde047" font-family="system-ui, sans-serif" font-size="10" font-weight="700" text-anchor="middle">PSALM 103:2</text>
    <text x="125" y="210" fill="#e2e8f0" font-family="system-ui, sans-serif" font-size="8.5" text-anchor="middle">"Forget not all His benefits"</text>
  </g>

  <!-- Right: Positive Virtues Generated -->
  <g transform="translate(550, 95)">
    <rect width="220" height="245" rx="10" fill="#1e293b" stroke="#34d399" stroke-width="1.5"/>
    <rect width="220" height="34" rx="10" fill="#047857"/>
    <text x="110" y="22" fill="#ffffff" font-family="system-ui, sans-serif" font-size="12" font-weight="700" text-anchor="middle">EMPOWERED VIRTUES</text>
    
    <text x="12" y="65" fill="#6ee7b7" font-family="system-ui, sans-serif" font-size="11" font-weight="700">1. Deep Inner Contentment</text>
    <text x="12" y="80" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10">Appreciating daily blessings.</text>

    <text x="12" y="110" fill="#6ee7b7" font-family="system-ui, sans-serif" font-size="11" font-weight="700">2. Emotional Resilience</text>
    <text x="12" y="125" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10">Quick bounce-back from setbacks.</text>

    <text x="12" y="155" fill="#6ee7b7" font-family="system-ui, sans-serif" font-size="11" font-weight="700">3. Stronger Friendships</text>
    <text x="12" y="170" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10">Expressing sincere thanks to peers.</text>

    <text x="12" y="200" fill="#6ee7b7" font-family="system-ui, sans-serif" font-size="11" font-weight="700">4. Spiritual Joy &amp; Peace</text>
    <text x="12" y="215" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10">Unshakable trust in God's goodness.</text>
  </g>

  <!-- Bottom Banner -->
  <rect x="30" y="360" width="740" height="56" rx="8" fill="#1e293b" stroke="#334155" stroke-width="1"/>
  <text x="400" y="384" fill="#34d399" font-family="system-ui, sans-serif" font-size="12" font-weight="700" text-anchor="middle">GRATITUDE IS A SPIRITUAL WEAPON AND AN EMOTIONAL FORTRESS</text>
  <text x="400" y="402" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="11" text-anchor="middle">Choosing to thank God before complaining rewires the teenage brain for joy, resilience, and supernatural peace.</text>
</svg>"""


def get_svg_lesson6():
    return """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 450" width="100%" height="100%">
  <defs>
    <linearGradient id="bgGrad6" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#0f172a"/>
      <stop offset="50%" stop-color="#1e293b"/>
      <stop offset="100%" stop-color="#0f172a"/>
    </linearGradient>
    <linearGradient id="h1Grad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#0284c7"/>
      <stop offset="100%" stop-color="#0369a1"/>
    </linearGradient>
    <linearGradient id="h2Grad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#059669"/>
      <stop offset="100%" stop-color="#047857"/>
    </linearGradient>
    <linearGradient id="h3Grad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#d97706"/>
      <stop offset="100%" stop-color="#b45309"/>
    </linearGradient>
    <linearGradient id="h4Grad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#7c3aed"/>
      <stop offset="100%" stop-color="#6d28d9"/>
    </linearGradient>
    <linearGradient id="h5Grad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#e11d48"/>
      <stop offset="100%" stop-color="#be123c"/>
    </linearGradient>
  </defs>

  <rect width="800" height="450" fill="url(#bgGrad6)" rx="14"/>
  <rect x="15" y="15" width="770" height="420" fill="none" stroke="#334155" stroke-width="1.5" stroke-dasharray="6 4" rx="10"/>

  <text x="400" y="44" fill="#38bdf8" font-family="system-ui, -apple-system, sans-serif" font-size="18" font-weight="800" text-anchor="middle" letter-spacing="0.5">THE 5 HABITS OF DAILY GRATITUDE &amp; THE FORGIVENESS LOOP</text>
  <text x="400" y="66" fill="#94a3b8" font-family="system-ui, -apple-system, sans-serif" font-size="12" text-anchor="middle">Practical Rhythms from Colossians 3:15-17 to Anchor Thanksgiving into Teenage Life</text>

  <!-- 5 Habit Cards -->
  <!-- 1: Blessing Journal -->
  <g transform="translate(25, 95)">
    <rect width="138" height="240" rx="8" fill="#1e293b" stroke="#38bdf8" stroke-width="1.5"/>
    <rect width="138" height="32" rx="8" fill="url(#h1Grad)"/>
    <text x="69" y="21" fill="#ffffff" font-family="system-ui, sans-serif" font-size="11" font-weight="700" text-anchor="middle">1. JOURNALING</text>
    <text x="10" y="55" fill="#7dd3fc" font-family="system-ui, sans-serif" font-size="10" font-weight="700">Blessing Book:</text>
    <text x="10" y="72" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="9.5">Write 3 specific</text>
    <text x="10" y="86" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="9.5">blessings every night</text>
    <text x="10" y="100" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="9.5">before sleeping.</text>
    <text x="10" y="130" fill="#7dd3fc" font-family="system-ui, sans-serif" font-size="10" font-weight="700">Impact:</text>
    <text x="10" y="147" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="9.5">Trains the mind to</text>
    <text x="10" y="161" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="9.5">spot God's hand in</text>
    <text x="10" y="175" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="9.5">ordinary events.</text>
  </g>

  <!-- 2: Morning/Evening Rhythms -->
  <g transform="translate(178, 95)">
    <rect width="138" height="240" rx="8" fill="#1e293b" stroke="#34d399" stroke-width="1.5"/>
    <rect width="138" height="32" rx="8" fill="url(#h2Grad)"/>
    <text x="69" y="21" fill="#ffffff" font-family="system-ui, sans-serif" font-size="11" font-weight="700" text-anchor="middle">2. PRAYER RHYTHM</text>
    <text x="10" y="55" fill="#6ee7b7" font-family="system-ui, sans-serif" font-size="10" font-weight="700">Psalm 92:1-2:</text>
    <text x="10" y="72" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="9.5">Morning praise for</text>
    <text x="10" y="86" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="9.5">God's loving-kindness;</text>
    <text x="10" y="100" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="9.5">Evening for faithfulness.</text>
    <text x="10" y="130" fill="#6ee7b7" font-family="system-ui, sans-serif" font-size="10" font-weight="700">Impact:</text>
    <text x="10" y="147" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="9.5">Bookends the day</text>
    <text x="10" y="161" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="9.5">with Christ at the</text>
    <text x="10" y="175" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="9.5">center of focus.</text>
  </g>

  <!-- 3: Gratitude Alarm -->
  <g transform="translate(331, 95)">
    <rect width="138" height="240" rx="8" fill="#1e293b" stroke="#f59e0b" stroke-width="1.5"/>
    <rect width="138" height="32" rx="8" fill="url(#h3Grad)"/>
    <text x="69" y="21" fill="#ffffff" font-family="system-ui, sans-serif" font-size="11" font-weight="700" text-anchor="middle">3. HOURLY PAUSE</text>
    <text x="10" y="55" fill="#fde68a" font-family="system-ui, sans-serif" font-size="10" font-weight="700">Gratitude Alarm:</text>
    <text x="10" y="72" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="9.5">Set a midday prompt</text>
    <text x="10" y="86" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="9.5">to pause for 30s</text>
    <text x="10" y="100" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="9.5">and thank God.</text>
    <text x="10" y="130" fill="#fde68a" font-family="system-ui, sans-serif" font-size="10" font-weight="700">Impact:</text>
    <text x="10" y="147" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="9.5">Interrupts complaint</text>
    <text x="10" y="161" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="9.5">cycles and restores</text>
    <text x="10" y="175" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="9.5">calm composure.</text>
  </g>

  <!-- 4: Worship Music -->
  <g transform="translate(484, 95)">
    <rect width="138" height="240" rx="8" fill="#1e293b" stroke="#a78bfa" stroke-width="1.5"/>
    <rect width="138" height="32" rx="8" fill="url(#h4Grad)"/>
    <text x="69" y="21" fill="#ffffff" font-family="system-ui, sans-serif" font-size="11" font-weight="700" text-anchor="middle">4. WORSHIP SONGS</text>
    <text x="10" y="55" fill="#c4b5fd" font-family="system-ui, sans-serif" font-size="10" font-weight="700">Spiritual Songs:</text>
    <text x="10" y="72" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="9.5">Singing psalms &amp;</text>
    <text x="10" y="86" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="9.5">hymns with grace</text>
    <text x="10" y="100" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="9.5">in hearts (Col 3:16).</text>
    <text x="10" y="130" fill="#c4b5fd" font-family="system-ui, sans-serif" font-size="10" font-weight="700">Impact:</text>
    <text x="10" y="147" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="9.5">Fills thoughts with</text>
    <text x="10" y="161" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="9.5">truth and dispels</text>
    <text x="10" y="175" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="9.5">negative emotions.</text>
  </g>

  <!-- 5: Forgiveness Loop -->
  <g transform="translate(637, 95)">
    <rect width="138" height="240" rx="8" fill="#1e293b" stroke="#f43f5e" stroke-width="1.5"/>
    <rect width="138" height="32" rx="8" fill="url(#h5Grad)"/>
    <text x="69" y="21" fill="#ffffff" font-family="system-ui, sans-serif" font-size="11" font-weight="700" text-anchor="middle">5. FORGIVENESS</text>
    <text x="10" y="55" fill="#fda4af" font-family="system-ui, sans-serif" font-size="10" font-weight="700">Grace Cycle:</text>
    <text x="10" y="72" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="9.5">Recognizing Christ's</text>
    <text x="10" y="86" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="9.5">forgiveness empowers</text>
    <text x="10" y="100" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="9.5">us to pardon others.</text>
    <text x="10" y="130" fill="#fda4af" font-family="system-ui, sans-serif" font-size="10" font-weight="700">Impact:</text>
    <text x="10" y="147" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="9.5">Breaks cycles of</text>
    <text x="10" y="161" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="9.5">grudge-holding</text>
    <text x="10" y="175" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="9.5">in school &amp; family.</text>
  </g>

  <!-- Bottom Banner -->
  <rect x="25" y="360" width="750" height="56" rx="8" fill="#1e293b" stroke="#334155" stroke-width="1"/>
  <text x="400" y="384" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="12" font-weight="700" text-anchor="middle">COLOSSIANS 3:17 — 'WHATEVER YOU DO, DO ALL IN THE NAME OF THE LORD JESUS, GIVING THANKS'</text>
  <text x="400" y="402" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="11" text-anchor="middle">Daily gratitude transforms routine obligations into acts of worship and builds a joyful, forgiving community.</text>
</svg>"""


# ─── LESSONS CONFIGURATION DATA (6 LESSONS) ───────────────────────────────────

LESSONS_DATA = [
    # ─── LESSON 1 ─────────────────────────────────────────────────────────────
    {
        "unit_order": 1,
        "unit_name": "Understanding Leprosy and Social Outcasts",
        "unit_description": "Analyze the physical reality of leprosy in biblical antiquity and examine the social, legal, and religious quarantine imposed by Levitical law.",
        "lesson_title": "Understanding Leprosy and Social Outcasts",
        "image": {
            "url": "https://upload.wikimedia.org/wikipedia/commons/thumb/6/69/Ottheinrich_Folio_251v_Luk17.jpg/800px-Ottheinrich_Folio_251v_Luk17.jpg",
            "title": "Visual Hook: Lepers Outside the City Gate",
            "author": "Ottheinrich Folio Master (Matthias Gerung)",
            "licensing": "Public Domain",
            "source": "Wikimedia Commons",
            "caption": "A 16th-century illuminated biblical manuscript showing afflicted lepers standing outside the settlement, banned by quarantine laws and crying out for help."
        },
        "youtube": {
            "youtube_id": "26z_Khwaxyg",
            "title": "BibleProject: Luke 9-19 Overview",
            "description": "Explores Jesus' journey to Jerusalem, highlighting His mission to seek and save the lost, the sick, and marginalized social outcasts."
        },
        "svg_fn": get_svg_lesson1,
        "goals": [
            "Describe the physical pathology, symptoms, and severe suffering caused by leprosy (Hansen's disease) in biblical times.",
            "Explain the social, legal, and religious quarantine laws governing lepers under Leviticus 13-14 and Luke 17:11-12.",
            "Evaluate contemporary forms of social stigmatization in Kenyan schools and formulate empathetic Christian responses to marginalized peers."
        ],
        "intro": "Have you ever had a highly contagious illness—such as chickenpox, measles, or pink eye—where the school nurse or your parents told you: 'You must stay in your room. Do not play with other children until you are completely well'? It feels incredibly lonely to be separated from your friends for just a few days.\n\nIn biblical times, if you were diagnosed with leprosy, you faced a life sentence of absolute isolation. You were banned from your family, your village, and the temple forever, with no medical hope of a cure. Understanding the terrifying reality of leprosy helps us appreciate the desperation and courage of the ten lepers who encountered Jesus.",
        "core_scripture": "### Biblical Foundations of Leprosy Quarantine\n\n#### Leviticus 13:45-46 — The Law Concerning Leprosy\n> *\"Anyone with such a defiling disease must wear torn clothes, let their hair be unkempt, cover the lower part of their face and cry out, 'Unclean! Unclean!' As long as they have the disease they remain unclean. They must live alone; they must live outside the camp.\"*\n\n#### Luke 17:11-12 — The Meeting at the Border\n> *\"Now on his way to Jerusalem, Jesus traveled along the border between Samaria and Galilee. As he was going into a village, ten men who had leprosy met him. They stood at a distance.\"*\n\nThese biblical passages illustrate both the severe legal quarantine established in the Old Testament and the obedience of the ten lepers who kept the required distance while seeking Jesus' intervention.",
        "theological_pillars": "### Theological & Medical Dimensions of Biblical Leprosy\n\n1. **The Physical Horror of Hansen's Disease:** Leprosy is a chronic bacterial infection attacking peripheral nerves, skin, respiratory mucosa, and eyes. In the ancient world, it caused loss of physical sensation, secondary infections, bone resorption, gangrene, and visible physical disfigurement.\n2. **Ritual Uncleanliness under Levitical Law:** Under the Mosaic covenant (Leviticus 13-14), leprosy rendered a person ritually *tamei* (unclean). It was not merely viewed as a physical pathology, but as a condition that barred the sufferer from approaching the Holy Sanctuary and participating in Israel's worship.\n3. **Total Social Death:** A diagnosed leper was evicted from city gates, forced to live in caves or desolate wilderness camps, wear mourning garments (torn robes, unkempt hair), and loudly shout 'Unclean! Unclean!' whenever a healthy traveler approached. They were regarded as 'the living dead.'",
        "deep_dive": "### Deep Dive: Quarantine, Stigma, and Common Bond in Suffering\n\nTo fully grasp Luke 17:11-12, we must analyze the social dynamics of the ancient borderlands:\n\n- **The Border Region:** Jesus was traveling along the border between Samaria and Galilee—a no-man's-land where normal social structures broke down. It was here that outcasts congregated.\n- **Shared Misery Overcoming Ancient Hatred:** Under normal circumstances, Jews and Samaritans despised one another and refused to associate. However, their shared affliction with leprosy destroyed their ethnic divisions. The leper colony included both Jews and at least one Samaritan.\n- **Standing at a Distance:** Even in their desperation, the ten lepers respected the legal quarantine. They did not rush to touch Jesus or crowd Him, but stood at least 100 paces away, demonstrating both social awareness and respect for the Law of Moses.\n- **Sin and Restoration Symbolism:** Throughout Scripture, leprosy serves as a vivid metaphor for the devastating alienating power of sin: it numbs moral sensitivity, separates humanity from God's presence, and requires supernatural divine cleansing.",
        "practical": {
            "title": "Action Framework: Overcoming Social Stigma and Marginalization",
            "steps": [
                "Step 1: Identify Modern Stigmas — Recognize peers in your school who are isolated due to disability, poverty, academic struggles, or background.",
                "Step 2: Resist Bullying & Exclusion — Refuse to participate in jokes, gossip, or social exclusion that pushes classmates into modern 'leper camps.'",
                "Step 3: Extend Intentional Friendship — Follow Christ's example by actively greeting, sitting with, and including those whom others avoid.",
                "Step 4: Advocate for Fair Treatment — Speak up for vulnerable students in class and school clubs, affirming their God-given dignity as image-bearers."
            ]
        },
        "kenyan_context": "In Kenyan society today, physical leprosy is treatable with modern multidrug therapy (MDT), but social 'leprosy' persists through the stigmatization of people living with HIV/AIDS, mental illness, physical disabilities, or marginalized ethnic identities. Christian teenagers in Kenya are called by CBC values to champion inclusivity, social cohesion, and the constitutional dignity of every person regardless of their health or economic status.",
        "reflection": "### Personal Reflection & Empathy Challenge\n\nImagine receiving a medical diagnosis that meant you could never hug your parents again, never sit in a classroom with your friends, and had to spend the rest of your life shouting 'Unclean!' whenever someone walked past.\n\n- How does this background heighten the immense emotional desperation of the ten men who cried out to Jesus?\n- Who in your school community feels isolated like a modern-day leper, and how can you show them Christ's love this week?",
        "takeaways": [
            "Leprosy in biblical times caused severe physical deformity, nerve death, and lifelong ritual uncleanness (Leviticus 13:45-46).",
            "Lepers suffered total social and religious quarantine, forced to live outside settlements and shout 'Unclean! Unclean!'",
            "Shared suffering united Jewish and Samaritan lepers across bitter ethnic barriers along the border region (Luke 17:11-12).",
            "Christians are called to dismantle social stigmas and actively embrace marginalized and vulnerable individuals in their communities."
        ],
        "mcq": {
            "question": "Under the Law of Moses (Leviticus 13:45), what was a person afflicted with leprosy legally required to do when a healthy person approached?",
            "options": [
                "A) Offer a financial sacrifice to the town magistrates immediately.",
                "B) Run away and hide behind the nearest rocks or trees.",
                "C) Tear their clothes, let their hair be unkempt, cover their mouth, and shout 'Unclean! Unclean!'",
                "D) Demand food and medical herbs from the travelers."
            ],
            "answer": "C",
            "explanation": "Leviticus 13:45 mandated that lepers wear torn clothes, keep unkempt hair, cover their upper lip/mouth, and shout 'Unclean! Unclean!' to warn others and prevent ritual defilement."
        }
    },

    # ─── LESSON 2 ─────────────────────────────────────────────────────────────
    {
        "unit_order": 2,
        "unit_name": "The Cry for Mercy and the Command of Faith",
        "unit_description": "Examine the united cry of the ten lepers, Jesus' response, and the profound test of faith embedded in His command to show themselves to the priests.",
        "lesson_title": "The Cry for Mercy and the Command of Faith",
        "image": {
            "url": "https://upload.wikimedia.org/wikipedia/commons/thumb/3/36/Healing_of_ten_lepers.jpg/800px-Healing_of_ten_lepers.jpg",
            "title": "Visual Hook: The Ten Lepers Calling Out to Jesus",
            "author": "Unknown Byzantine Master (Visoki Dečani Monastery)",
            "licensing": "Public Domain",
            "source": "Wikimedia Commons",
            "caption": "A 14th-century Byzantine fresco depicting the ten lepers standing at a distance, raising their voices in prayer and receiving Christ's testing command."
        },
        "youtube": {
            "youtube_id": "xmFPS0445X4",
            "title": "BibleProject: Gospel of the Kingdom",
            "description": "Explores how Jesus inaugurated the Kingdom of God by confronting sickness, restoring outcasts, and demanding active obedience in faith."
        },
        "svg_fn": get_svg_lesson2,
        "goals": [
            "Analyze why the ten lepers raised their voices in a coordinated cry and the theological significance of calling Jesus 'Master' (Epistates).",
            "Explain how Jesus' command to 'go show yourselves to the priests' tested their faith and obedience while they were still physically diseased.",
            "Apply the biblical principle of active faith to personal academic, moral, and emotional challenges in daily student life."
        ],
        "intro": "If you were desperately ill and saw the most renowned doctor walking along the road, your first instinct would be to run up to them, grab their sleeve, and plead for immediate help. But the ten lepers could not do that; they had to obey the quarantine boundary.\n\nInstead of running, they pooled their strength and raised a single, thunderous cry of faith across the open fields. Notice how Jesus responded: He did not touch them, lay hands on them, or say 'You are cured.' Instead, He gave them an instruction that required them to walk forward in pure trust before seeing any physical change.",
        "core_scripture": "### Biblical Passage: The Cry and The Testing Command\n\n#### Luke 17:12-14\n> *\"As he was going into a village, ten men who had leprosy met him. They stood at a distance and called out in a loud voice, 'Jesus, Master, have pity on us!' When he saw them, he said, 'Go, show yourselves to the priests.' And as they went, they were cleansed.\"*\n\nThis Scripture reveals the dynamic interaction between human desperation, respectful prayer, divine instruction, and the physical miracle that unfolds through obedient action.",
        "theological_pillars": "### Theological Insights: The Dynamics of Faith and Authority\n\n1. **The Title 'Master' (*Epistates*):** In Luke's Gospel, the Greek term *Epistates* (Chief Commander / Sovereign Master) is used exclusively by disciples who recognize Jesus' absolute authority over nature and circumstances. The lepers acknowledged Christ's divine power.\n2. **The Cry for Mercy (*Eleison*):** They did not demand their rights, ask for alms, or bargain. They asked for *mercy* (pity/grace). In biblical theology, grace is unearned divine favor bestowed upon the completely helpless.\n3. **The Counter-Intuitive Command:** Under Leviticus 14, priests did not cure leprosy; they only verified cures that had already occurred. By telling them to go to the priests while their sores were still bleeding and active, Jesus demanded that they act as though the healing were already an established reality.",
        "deep_dive": "### Deep Dive: Faith as Obedient Movement\n\nExamining the tension between what the lepers saw and what Jesus commanded reveals the essence of biblical faith:\n\n- **The Risk of Looking Foolish:** Imagine walking into a temple or village to present yourself to a priest while still covered in white sores. The lepers risked public ridicule and severe punishment for breaking quarantine.\n- **Decision at the Crossroads:** The ten men had to choose: stay where they were and complain that Jesus hadn't healed them on the spot, or turn their backs and start walking toward the priests in Jerusalem. They chose obedience.\n- **Blessing Follows the Step:** Luke notes: *\"And as they went, they were cleansed.\"* The miraculous healing power of God was not released while they stood debating; it was unleashed in the rhythm of their obedient footsteps.\n- **Hebrews 11 Connection:** *\"Now faith is confidence in what we hope for and assurance about what we do not see\"* (Hebrews 11:1). Active faith always moves forward on the promise of God's Word.",
        "practical": {
            "title": "Action Framework: Stepping Out in Active Faith",
            "steps": [
                "Step 1: Acknowledge Your Need — Honestly present your academic, personal, or family struggles to God in prayer without pretending.",
                "Step 2: Align with God's Commands — Identify what the Scriptures and moral conscience instruct you to do in your current challenge.",
                "Step 3: Take Concrete Action — Begin studying, seeking counsel, or reconciling with someone before you feel an emotional breakthrough.",
                "Step 4: Trust God with the Outcome — Persevere in daily obedience, confident that God's power accompanies faithful action."
            ]
        },
        "kenyan_context": "In Kenya, students often face daunting challenges such as preparing for national exams (KJSEA/KCSE), financial constraints for school fees, or peer temptation. Waiting passively for a miracle without studying or working hard is not biblical faith. Like the lepers who walked toward the priests before their skin changed, Kenyan youth are called to combine earnest prayer with diligent study, trusting God to crown their disciplined efforts with success.",
        "reflection": "### Personal Reflection: Stepping onto the Road\n\nPut yourself in the sandals of one of the ten lepers when Jesus said, 'Go, show yourselves to the priests.'\n\n- You look down at your bandaged hands, and the leprosy is still there. What thoughts would battle in your mind at that precise moment?\n- In what area of your life is God calling you to take an obedient step of faith today before you see the full solution?",
        "takeaways": [
            "The lepers addressed Jesus as 'Master' (*Epistates*), acknowledging His supreme authority and seeking divine mercy rather than material alms.",
            "Jesus tested their faith by commanding them to go to the priests before their physical healing was visibly evident (Luke 17:14).",
            "The miracle occurred mid-journey: *'And as they went, they were cleansed,'* demonstrating that blessings accompany obedient action.",
            "Biblical faith is never passive; it requires taking active, trusting steps in accordance with God's Word."
        ],
        "mcq": {
            "question": "Why was Jesus' command, 'Go, show yourselves to the priests,' a profound test of faith for the ten lepers?",
            "options": [
                "A) Because priests were doctors who charged expensive fees to heal leprosy.",
                "B) Because they were still visibly covered in leprosy when Jesus commanded them to start walking.",
                "C) Because the priests had issued a warrant for Jesus' arrest.",
                "D) Because Samaritans were legally forbidden from ever walking on public roads."
            ],
            "answer": "B",
            "explanation": "When Jesus gave the command, their skin had not yet changed. They had to obey and start walking to the priests—who only inspected healed persons—trusting Jesus' word before seeing physical evidence."
        }
    },

    # ─── LESSON 3 ─────────────────────────────────────────────────────────────
    {
        "unit_order": 3,
        "unit_name": "The Miracle of Healing and the Outcast's Return",
        "unit_description": "Analyze the miraculous cleansing on the road, the historical hostility between Jews and Samaritans, and the radical return of the single grateful Samaritan.",
        "lesson_title": "The Miracle of Healing and the Outcast's Return",
        "image": {
            "url": "https://upload.wikimedia.org/wikipedia/commons/thumb/e/ee/Gebhard_Fugel_Heilung_der_zehn_Auss%C3%A4tzigen_c1920.jpg/800px-Gebhard_Fugel_Heilung_der_zehn_Auss%C3%A4tzigen_c1920.jpg",
            "title": "Visual Hook: The Grateful Samaritan Falling at Jesus' Feet",
            "author": "Gebhard Fugel (c. 1920)",
            "licensing": "Public Domain",
            "source": "Wikimedia Commons",
            "caption": "A vivid 20th-century painting depicting the lone Samaritan returning with tears of gratitude, falling prostrate at Jesus' feet while nine others rush ahead."
        },
        "youtube": {
            "youtube_id": "62CliEkRCso",
            "title": "BibleProject: Compassion and Gracious Character",
            "description": "Explores how God's gracious love reaches beyond cultural, religious, and ethnic divides to embrace the humble and thankful outcast."
        },
        "svg_fn": get_svg_lesson3,
        "goals": [
            "Describe the moment of physical healing as the ten lepers journeyed toward the priests (Luke 17:14-15).",
            "Explain the deep historical, ethnic, and theological hostility between Jews and Samaritans in the first century.",
            "Analyze why the return and prostration of the Samaritan was culturally shocking and spiritually exemplary."
        ],
        "intro": "Imagine you and nine classmates are in trouble, facing suspension from school. A teacher steps forward, defends you before the principal, and gets all of you completely exonerated. All ten of you walk out of the principal's office celebrating. Nine of your classmates immediately run off to the canteen and soccer field. But you stop in your tracks, walk back to the teacher's office, knock on the door, and say: 'Teacher, thank you with all my heart for saving my future.'\n\nHow would that teacher feel? That is what happened on the dusty road between Samaria and Galilee. Ten men received a life-transforming miracle, but only one returned to say thank you—and he was the person society least expected.",
        "core_scripture": "### Biblical Passage: The Miraculous Cleansing and The Return\n\n#### Luke 17:14-16\n> *\"And as they went, they were cleansed. One of them, when he saw he was healed, came back, praising God in a loud voice. He threw himself at Jesus’ feet and thanked him—and he was a Samaritan.\"*\n\nThis passage contrasts the rushing departure of the nine with the spontaneous, passionate, and humble return of the solitary Samaritan foreigner.",
        "theological_pillars": "### Theological Insights: The Radical Return of the Samaritan\n\n1. **The Sudden Cleansing (*Ekatharisthesan*):** As they walked, their decaying skin, dead nerve endings, and open sores suddenly regenerated. Skin became smooth, healthy, and whole. The power of Christ operated at a distance.\n2. **The Historical Jew-Samaritan Hostility:** Ever since the Assyrian exile (722 BC), Jews regarded Samaritans as theological heretics and ethnic half-breeds who corrupted pure worship on Mount Gerizim. Jews avoided traveling through Samaria, avoided sharing eating vessels, and considered Samaritans permanently unclean (John 4:9).\n3. **Prostration and True Worship:** When the Samaritan realized he was cured, he did not just whisper a polite 'thanks.' He returned shouting praises to God at the top of his lungs, falling face down (*epesen epi prosopon*) at Jesus' dusty feet. In biblical gesture, prostration is an act of supreme worship reserved for God alone.",
        "deep_dive": "### Deep Dive: Why Did the Nine Keep Going?\n\nTo understand human nature, we must examine why ninety percent of the beneficiaries failed to return:\n\n- **Legalism Over Relationship:** The nine Jewish lepers were technically obeying Jesus' instruction to show themselves to the priests. However, they became so obsessed with following the legal procedure to regain their civil privileges that they forgot the Lord who gave them the miracle.\n- **The Seduction of the Gift:** The nine were so thrilled by the gift (their new skin, the prospect of seeing family, returning to business) that they bypassed the Giver. They took God's blessing for granted as their entitled right as Abraham's descendants.\n- **The Samaritan's Theological Insight:** The Samaritan realized something deeper: if Jesus possessed the divine power to cleanse incurable leprosy, then Jesus Himself was greater than the temple priests in Jerusalem or Mount Gerizim! Going back to worship Jesus took precedence over any ritual clearance certificate.",
        "practical": {
            "title": "Action Framework: Breaking Cultural Barriers with Gratitude",
            "steps": [
                "Step 1: Stop and Recognize God's Hand — When good things happen (passing exams, recovery from illness), pause immediately before rushing into celebrations.",
                "Step 2: Give Verbal and Public Thanks — Express your gratitude aloud to God in prayer and verbally thank the people who supported you.",
                "Step 3: Practice Humility — Guard against pride or entitlement by acknowledging that every talent and blessing is an unearned gift of grace.",
                "Step 4: Cross Ethnic and Social Divides — Treat people from every ethnic group, religion, and social background in Kenya with honor and Christian love."
            ]
        },
        "kenyan_context": "Kenya is a rich tapestry of over 40 ethnic communities. Unfortunately, ethnic prejudice and tribal stereotypes have sometimes fueled political tension and social friction. The story of the grateful Samaritan teaches Kenyan youth that God does not judge people by tribe or background. Sincere Christian character, gratitude, and moral integrity matter infinitely more than ethnic affiliation.",
        "reflection": "### Personal Reflection: Checking Our Motives\n\nWhen God answers a major prayer in your life—such as passing your end-of-term exams or healing a sick family member—what is your immediate reaction?\n\n- Do you run off to celebrate and brag on social media like the nine, or do you take time to kneel in private thanksgiving before God?\n- Have you ever looked down on someone because of their tribe or background, only to see them demonstrate greater character and kindness than others?",
        "takeaways": [
            "All ten lepers were miraculously cleansed of their disease as they journeyed in obedience (Luke 17:14).",
            "Nine lepers rushed ahead to the priests, prioritizing legal clearance and social restoration over thanking Christ.",
            "The lone leper who returned was a Samaritan—a member of a despised group in first-century Jewish society (Luke 17:16).",
            "The Samaritan fell prostrate at Jesus' feet, demonstrating that genuine gratitude is an act of humble, passionate worship."
        ],
        "mcq": {
            "question": "What was culturally and historically astonishing about the one healed leper who returned to thank Jesus?",
            "options": [
                "A) He was a Roman centurion with high political authority.",
                "B) He was a Samaritan, a group fiercely despised and treated as religious outcasts by the Jews.",
                "C) He was a Pharisee from the Sanhedrin council.",
                "D) He refused to accept his physical healing until Jesus touched him."
            ],
            "answer": "B",
            "explanation": "Jews and Samaritans harbored centuries of mutual hatred. The fact that the nine Jewish lepers ran off without a word while the despised Samaritan returned to worship Jesus was a shocking cultural reversal."
        }
    },

    # ─── LESSON 4 ─────────────────────────────────────────────────────────────
    {
        "unit_order": 4,
        "unit_name": "Jesus' Profound Questions and Teachings",
        "unit_description": "Analyze Jesus' three probing questions in Luke 17:17-18, the sensitivity of God's heart, and the vital theological distinction between physical cleansing and spiritual salvation.",
        "lesson_title": "Jesus' Profound Questions and Teachings",
        "image": {
            "url": "https://upload.wikimedia.org/wikipedia/commons/thumb/4/4c/Christ_and_the_Samaritan_Woman_by_Stefano_Erardi.jpg/800px-Christ_and_the_Samaritan_Woman_by_Stefano_Erardi.jpg",
            "title": "Visual Hook: Jesus Welcoming the Outsider",
            "author": "Stefano Erardi (National Museum of Fine Arts, Malta)",
            "licensing": "Public Domain",
            "source": "Wikimedia Commons",
            "caption": "A 17th-century masterpiece depicting Christ engaging deeply with the Samaritan, illustrating God's sovereign valuation and restoration of the marginalized."
        },
        "youtube": {
            "youtube_id": "oLYORLZOaZE",
            "title": "BibleProject: Shalom (Wholeness & Peace)",
            "description": "Explores the biblical meaning of Shalom and Sozo—how God restores broken bodies, broken hearts, and broken communities into complete wholeness."
        },
        "svg_fn": get_svg_lesson4,
        "goals": [
            "Analyze Jesus' three probing questions in Luke 17:17-18 and evaluate what they reveal about God's heart and sensitivity to ingratitude.",
            "Distinguish between physical cleansing (*catharizo*) and holistic spiritual salvation (*sozo*) in Jesus' pronouncement to the Samaritan.",
            "Formulate principles for guarding against spiritual entitlement, presumption, and religious complacency in daily Christian life."
        ],
        "intro": "Have you ever spent your own hard-earned pocket money to buy a special gift for a friend, wrapped it carefully, and handed it to them with excitement, only for them to grab it, say nothing, and walk away without even looking at you? You would feel deeply hurt. That hurt does not mean you are weak; it shows that you value relationships and love.\n\nSince Jesus came to reveal God the Father to us, His response to the ungrateful lepers gives us a stunning window into the heart of God: God notices when we thank Him, and He genuinely grieves when we treat His blessings with cold indifference.",
        "core_scripture": "### Biblical Passage: Jesus' Questions and The Pronouncement of Salvation\n\n#### Luke 17:17-19\n> *\"Jesus asked, 'Were not all ten cleansed? Where are the other nine? Has no one returned to give praise to God except this foreigner?' Then he said to him, 'Rise and go; your faith has made you well.'\"*\n\nIn these verses, Jesus addresses the crowd with three searching rhetorical questions before bestowing the highest gift of spiritual wholeness upon the kneeling Samaritan.",
        "theological_pillars": "### Theological Insights: The Heart of God & Dimensions of Salvation\n\n1. **The Three Questions of Divine Disappointment:**\n   - *\"Were not all ten cleansed?\"* — Jesus is fully aware of every miracle He performs; none is hidden.\n   - *\"Where are the other nine?\"* — Christ feels their absence. God is not an unfeeling machine; He desires relationship.\n   - *\"Has no one returned except this foreigner (*allogenes*)?\"* — The Greek term *allogenes* denotes an outsider. The religious insiders took God's mercy for granted, while the outsider recognized God's glory.\n2. **Physical Cleansing (*Catharizo*) vs. Wholeness (*Sozo*):**\n   - In verse 14, all ten were *cleansed* (*ekatharisthesan* — bodily skin healed).\n   - In verse 19, Jesus tells the Samaritan: *\"He pistis sou sesoken se\"* — *\"Your faith has saved / made you whole!\"* The verb *sozo* is the biblical word for complete salvation: forgiveness of sins, peace with God, and eternal life.",
        "deep_dive": "### Deep Dive: Entitlement vs. Grace\n\nThis passage delivers a piercing warning to anyone who grows up around religion:\n\n- **The Danger of Familiarity:** The nine Jewish lepers grew up hearing about God's covenant with Abraham. They assumed that healing was their natural birthright. Familiarity with religious concepts can breed callous spiritual entitlement.\n- **The Humility of the Foreigner:** The Samaritan knew he had no covenant claims, no standing before the God of Israel, and no right to mercy. Therefore, when he received healing, his heart erupted in uncontrollable praise. He understood that everything was pure, unmerited grace.\n- **The Ultimate Miracle:** Physical health is temporary; all ten healed men eventually aged and died. But the Samaritan received an eternal blessing: he looked into the eyes of Christ, heard the words of salvation, and left in reconciled fellowship with the Creator.",
        "practical": {
            "title": "Action Framework: Guarding Against Spiritual Entitlement",
            "steps": [
                "Step 1: Conduct a Daily Blessing Audit — List at least five unearned blessings you enjoy daily (air, health, family, food, schooling).",
                "Step 2: Renounce the 'Entitlement Trap' — Recognize that neither God nor your parents owe you luxury, gadgets, or unearned privileges.",
                "Step 3: Respond to Answered Prayers — Whenever God helps you overcome a difficulty, immediately set aside time for private praise and dedication.",
                "Step 4: Seek Spiritual Wholeness Above Earthly Gains — Prioritize growing in Christlike character over merely asking God for material success."
            ]
        },
        "kenyan_context": "In Kenyan schools and churches, many students are raised in religious environments where praying before meals, attending chapel, and singing hymns are routine. It is very easy to fall into the trap of the 'other nine'—participating in religious rituals while having hearts cold to God's daily goodness. Jesus calls Kenyan youth to authentic, heartfelt discipleship where thanksgiving is a continuous lifestyle rather than a weekly formality.",
        "reflection": "### Personal Reflection: What Does God Hear from You?\n\nIf Jesus were to review your prayers over the last month, what would He find?\n\n- Is 90% of your prayer time spent asking for things (help in exams, pocket money, good health) with only 10% spent thanking Him for what He has already done?\n- How can you transform your prayer life so that thanksgiving becomes the loudest voice in your conversation with God?",
        "takeaways": [
            "Jesus asked three searching questions showing that God is emotionally sensitive to human ingratitude (Luke 17:17-18).",
            "The religious insiders took their healing for granted, while the Samaritan foreigner recognized God's sovereign grace.",
            "All ten men received physical cleansing (*catharizo*), but only the grateful Samaritan received spiritual salvation (*sozo*) (Luke 17:19).",
            "True discipleship goes beyond consuming God's blessings to establishing a loving, thankful relationship with Christ."
        ],
        "mcq": {
            "question": "What is the profound theological difference between what the nine lepers received and what the one Samaritan leper received?",
            "options": [
                "A) The nine were healed permanently, but the Samaritan's leprosy returned after three days.",
                "B) All ten received physical bodily cleansing, but only the grateful Samaritan received spiritual salvation and wholeness (Sozo).",
                "C) The nine received priesthood positions, while the Samaritan became a soldier.",
                "D) The Samaritan was excused from paying Roman taxes."
            ],
            "answer": "B",
            "explanation": "While all ten experienced bodily healing (*catharizo*), only the grateful Samaritan who returned to worship at Jesus' feet received the crown of complete spiritual salvation (*sozo*) and personal relationship with Christ."
        }
    },

    # ─── LESSON 5 ─────────────────────────────────────────────────────────────
    {
        "unit_order": 5,
        "unit_name": "Faith and Gratitude: Lessons for Teenagers",
        "unit_description": "Explore the psychological, emotional, and spiritual power of gratitude, examining biblical mandates (1 Thess 5:16-18, Ps 103:1-5) and resilience against adolescent stress.",
        "lesson_title": "Faith and Gratitude: Lessons for Teenagers",
        "image": {
            "url": "https://upload.wikimedia.org/wikipedia/commons/thumb/e/eb/Kenyan_Samburu_children_in_a_classroom.jpg/800px-Kenyan_Samburu_children_in_a_classroom.jpg",
            "title": "Visual Hook: Joy and Gratitude in Youth Community",
            "author": "UNESCO / Wikimedia Commons",
            "licensing": "CC BY-SA 3.0",
            "source": "Wikimedia Commons",
            "caption": "Young Kenyan students radiating joy, mutual respect, and contentment in their school environment, illustrating the mental resilience cultivated by thanksgiving."
        },
        "youtube": {
            "youtube_id": "d4qC7qHj3pU",
            "title": "BibleProject: Generosity and Thanksgiving",
            "description": "Explores how experiencing God's abundant grace naturally produces a lifestyle of generous gratitude and unshakable joy in biblical literature."
        },
        "svg_fn": get_svg_lesson5,
        "goals": [
            "Explain how biblical faith and gratitude operate as spiritual weapons against anxiety, envy, and adolescent depression.",
            "Analyze 1 Thessalonians 5:16-18 and Psalm 103:1-5 in relation to developing a resilient, thankful mindset in modern society.",
            "Evaluate scientific and psychological research demonstrating the positive impact of gratitude on teenage brain health and emotional well-being."
        ],
        "intro": "Have you ever met someone who is always smiling, encouraging others, and full of energy, even though they don't have the newest sneakers or the most expensive smartphone? On the other hand, you probably know students who have wealthy families, top grades, and the latest gadgets, but are constantly grumpy, cynical, and complaining about everything.\n\nWhat makes the difference? The answer is not money, looks, or popularity; the answer is **gratitude**. Gratitude is a spiritual choice that completely changes the way you experience the world. In this lesson, we will see how faith and thanksgiving protect your mental, emotional, and spiritual health.",
        "core_scripture": "### Biblical Foundations of Continuous Gratitude\n\n#### 1 Thessalonians 5:16-18 — The Triad of Christian Living\n> *\"Rejoice always, pray continually, give thanks in all circumstances; for this is God’s will for you in Christ Jesus.\"*\n\n#### Psalm 103:1-2 — Blessing the Lord\n> *\"Praise the Lord, my soul; all my inmost being, praise his holy name. Praise the Lord, my soul, and forget not all his benefits.\"*\n\nThese Scriptures reveal that gratitude is not a conditional reaction when everything goes perfectly; it is an unconditional command and spiritual anchor in all circumstances.",
        "theological_pillars": "### Theological & Psychological Dimensions of Adolescent Gratitude\n\n1. **Gratitude as God's Will (1 Thess 5:18):** Notice that Paul does not say *for* all circumstances, but *in* all circumstances. Even when facing difficult exams, family tension, or financial strain, believers can thank God for His unchanging love, presence, and eternal salvation.\n2. **The Battle Against Forgetfulness (Psalm 103:2):** Human nature tends to remember insults, failures, and hardships while quickly forgetting thousands of daily blessings. David commands his own soul: *'Forget not all His benefits!'* Cultivating gratitude requires deliberate remembrance.\n3. **The Neurological Benefits of Thanksgiving:** Modern neuroscience confirms that when adolescents actively practice gratitude, the brain releases dopamine and serotonin—neurotransmitters that reduce stress, combat depression, improve sleep quality, and enhance academic focus.",
        "deep_dive": "### Deep Dive: The Adolescent Gratitude Shield\n\nDuring the teenage years, youth face intense peer pressure, body image concerns, and comparison on social media. Gratitude acts as a protective shield:\n\n- **Shield Against Envy & FOMO (Fear of Missing Out):** When you scroll through social media and see peers displaying expensive clothes or trips, envy whispers: *'Your life is terrible.'* Gratitude responds: *'I thank God for the family, health, and opportunities I have.'* It kills envy at the root.\n- **Shield Against Anxiety & Academic Panic:** When exam anxiety builds up, thanksgiving shifts your focus from panic to God's past faithfulness. Reminding yourself of how God helped you in past terms calms your nervous system.\n- **Shield Against Toxic Cynicism:** Cynical students think complaining makes them look cool or mature. In reality, constant complaining poisons friendships and breeds bitterness. A thankful student radiates hope, draws authentic friends, and inspires the classroom.",
        "practical": {
            "title": "Action Framework: Building the Gratitude Habit in School",
            "steps": [
                "Step 1: The 'Three Good Things' Nightly Ritual — Before sleeping, write down three specific positive things that happened during the school day.",
                "Step 2: Verbalize Appreciation to School Staff — Make a point to thank the school cooks, cleaners, drivers, and teachers who serve behind the scenes.",
                "Step 3: Replace Complaints with Praise — Whenever you catch yourself complaining about homework or school food, immediately state two blessings you are grateful for.",
                "Step 4: Create a Gratitude WhatsApp / SMS Culture — Send a weekly message of encouragement and thanks to a parent, sibling, or friend."
            ]
        },
        "kenyan_context": "In Kenya, junior secondary school learners are navigating the transition to Grade 9 under CBC, with new subjects, project assessments, and career pathways. This transition can sometimes feel overwhelming. By embracing the biblical virtue of gratitude, Kenyan teenagers build emotional resilience, respect their teachers and parents, and contribute to a supportive, uplifting school atmosphere.",
        "reflection": "### Personal Reflection: Shifting Your Mental Lens\n\nTake a minute to think about your biggest frustration at school or home right now (e.g., tough math homework, waking up early, doing chores).\n\n- How can you reframe this frustration through the lens of thanksgiving? (e.g., 'Waking up early means I have the gift of life and the privilege of education').\n- How would your mood and relationships change if you chose to complain 50% less and thank God 50% more this week?",
        "takeaways": [
            "Giving thanks in all circumstances is God's direct will for believers in Christ Jesus (1 Thessalonians 5:18).",
            "Psalm 103:2 teaches us to actively fight spiritual amnesia by deliberately remembering God's daily benefits.",
            "Gratitude acts as an adolescent shield against envy, peer pressure, exam panic, and depressive thoughts.",
            "Practicing daily thanksgiving rewires brain chemistry for joy, reduces cortisol (stress), and deepens friendships."
        ],
        "mcq": {
            "question": "According to 1 Thessalonians 5:18, under what circumstances are Christians commanded to give thanks?",
            "options": [
                "A) Only when they win a sports competition or score top marks.",
                "B) Only during church services on Sundays.",
                "C) In all circumstances, because this is God's will in Christ Jesus.",
                "D) Only when their parents buy them expensive presents."
            ],
            "answer": "C",
            "explanation": "1 Thessalonians 5:18 clearly commands: 'Give thanks in all circumstances; for this is God's will for you in Christ Jesus.' Christian gratitude is rooted in God's eternal love, not merely pleasant external conditions."
        }
    },

    # ─── LESSON 6 ─────────────────────────────────────────────────────────────
    {
        "unit_order": 6,
        "unit_name": "Practicing Gratitude in Daily Life",
        "unit_description": "Equip learners with practical daily habits, worship music practices, and the profound theological connection between thanksgiving and forgiving others (Colossians 3:15-17).",
        "lesson_title": "Practicing Gratitude in Daily Life",
        "image": {
            "url": "https://upload.wikimedia.org/wikipedia/commons/thumb/1/17/Community_health_worker_counseling_young_people.jpg/800px-Community_health_worker_counseling_young_people.jpg",
            "title": "Visual Hook: Practicing Compassion and Thanksgiving Daily",
            "author": "USAID / Wikimedia Commons",
            "licensing": "Public Domain",
            "source": "Wikimedia Commons",
            "caption": "Mentorship and youth fellowship in East Africa where young people actively share testimonies, resolve conflicts, and cultivate daily habits of gratitude."
        },
        "youtube": {
            "youtube_id": "Ufe_hOfl4_w",
            "title": "BibleProject: The Character of God - Loving-Kindness (Hesed)",
            "description": "Explores how God's loyal, covenantal love (Hesed) anchors our daily worship, empowers mutual forgiveness, and sustains lifelong gratitude."
        },
        "svg_fn": get_svg_lesson6,
        "goals": [
            "Formulate five practical daily habits to anchor gratitude into teenage life based on Colossians 3:15-17 and Psalm 92:1-2.",
            "Explain the powerful theological loop connecting sincere gratitude to God with the ability to forgive peers and family members.",
            "Design an actionable personal and family gratitude plan (including a blessing journal and gratitude letters) for implementation in the Kenyan community."
        ],
        "intro": "Have you ever tried to learn an instrument like the piano or guitar, or master a sport like basketball or swimming? On your first day, it feels awkward and difficult. But if you practice every single day for thirty minutes, it eventually becomes second nature.\n\nGratitude is like a muscle: if you only use it once a year on your birthday, it remains weak. But if you exercise it daily through intentional habits, it becomes an unshakeable character trait. In this final lesson, we examine concrete, practical habits you can start tonight to live as a modern-day grateful Samaritan.",
        "core_scripture": "### Biblical Passage: The Rhythm of Christian Gratitude\n\n#### Colossians 3:15-17 — Peace, Praise, and Thanksgiving\n> *\"Let the peace of Christ rule in your hearts, since as members of one body you were called to peace. And be thankful. Let the message of Christ dwell among you richly as you teach and admonish one another with all wisdom through psalms, hymns, and songs from the Spirit, singing to God with gratitude in your hearts. And whatever you do, whether in word or deed, do it all in the name of the Lord Jesus, giving thanks to God the Father through him.\"*\n\n#### Psalm 92:1-2 — Morning and Evening Praise\n> *\"It is good to praise the Lord and make music to your name, O Most High, proclaiming your love in the morning and your faithfulness at night.\"*\n\nThese Scriptures provide the divine blueprint for integrating thankfulness into every conversation, song, decision, and relationship in daily life.",
        "theological_pillars": "### Five Practical Habits of Daily Gratitude\n\n1. **The Blessing Journal:** Keep a notebook beside your bed. Every evening before sleeping, record three specific blessings from your day (e.g., 'A friend shared their textbook, I understood chemistry, mother prepared a delicious dinner').\n2. **Morning and Evening Prayer Rhythms (Psalm 92:1-2):** Bookend your day with God. In the morning, thank Him for His steadfast love and the gift of life. In the evening, thank Him for His faithfulness throughout the day's trials.\n3. **The Hourly Gratitude Pause:** Set a quiet timer on your watch or phone. When it chimes, pause for 30 seconds to breathe, step back from busyness, and name one thing you are grateful for.\n4. **Worship Music as a Spiritual Prompt (Col 3:16):** Use Christ-centered worship music (such as 'How Good He Is', '10,000 Reasons', or Swahili hymns like 'Bwana U Sehemu Yangu') to direct your thoughts away from anxiety and toward God's goodness.\n5. **The Gratitude-Forgiveness Loop:** When your heart overflows with gratitude for Christ forgiving your sins, the toxic desire for revenge melts away. Thanksgiving empowers you to forgive classmates who offend you.",
        "deep_dive": "### Deep Dive: The Gratitude-Forgiveness Loop\n\nWhy is forgiveness so closely tied to thanksgiving in Colossians 3?\n\n- **The Root of Bitterness:** An ungrateful person focuses entirely on what they have been denied, what they have lost, or how someone offended them. This builds a wall of bitterness and resentment.\n- **The Transforming Perspective of Grace:** When a Christian looks at the Cross and realizes: *'God forgave all my countless sins through Christ's sacrifice, completely free of charge,'* they are overwhelmed by gratitude.\n- **Releasing the Debtor:** From a heart full of thanksgiving, you can say: *'Because God has been so overwhelmingly generous and merciful to me, I choose to forgive my classmate and release my grudge.'* Gratitude breaks the cycle of anger and brings Christ's peace into your school.",
        "practical": {
            "title": "Action Framework: Writing a Sincere Gratitude Letter",
            "steps": [
                "Step 1: Select a Recipient — Identify a parent, teacher, pastor, school cook, or classmate who has made a positive impact on your life.",
                "Step 2: Be Specific About Their Contribution — Mention concrete actions they took (e.g., 'Thank you for patiently explaining mathematics after class when I was confused').",
                "Step 3: Express the Emotional Impact — Share how their kindness encouraged you, gave you hope, or helped you grow.",
                "Step 4: Deliver the Letter — Hand the handwritten note to them in person. A sincere letter of appreciation will bring immense joy to their heart."
            ]
        },
        "kenyan_context": "In Kenyan boarding and day schools, harmonious community living requires deliberate effort. Conflict among roommates, academic competition, and misunderstandings often create tension. Implementing daily gratitude practices—such as sharing one blessing during dorm devotions, writing thank-you notes to teachers on Teacher Appreciation Day, and resolving disagreements through forgiveness—fosters national cohesion and Christian values as envisioned in Kenya's CBC framework.",
        "reflection": "### Personal Reflection & Commitment\n\nAs we conclude this topic on the Healing of the Ten Lepers:\n\n- Which of the five daily gratitude habits will you commit to starting tonight?\n- Who is the first person in your family or school to whom you will write a handwritten gratitude letter this week?",
        "takeaways": [
            "Colossians 3:15-17 commands believers to let the peace of Christ rule in their hearts and do everything with thanksgiving.",
            "Five practical habits anchor gratitude: keeping a blessing journal, morning/evening prayer, hourly pauses, worship music, and forgiveness.",
            "There is an inseparable theological loop between gratitude for God's mercy and our ability to forgive others who offend us.",
            "Writing specific, handwritten gratitude letters blesses mentors and builds a culture of appreciation in Kenyan communities."
        ],
        "mcq": {
            "question": "How does cultivating a grateful heart toward God practically empower a teenager to forgive classmates who offend them?",
            "options": [
                "A) By allowing them to ignore school rules entirely.",
                "B) By helping them remember how much mercy God has freely forgiven them, melting bitterness and empowering them to release grudges.",
                "C) By proving to everyone that they are morally superior to others.",
                "D) By forcing the offender to pay a financial fine."
            ],
            "answer": "B",
            "explanation": "Recognizing the overwhelming grace and forgiveness God has shown us in Christ fills our hearts with gratitude, making it natural and necessary to extend that same grace and forgiveness to others (Colossians 3:13-15)."
        }
    }
]


# ─── MAIN TOPIC INGESTION FUNCTION ───────────────────────────────────────────

def ingest_cbc_grade9_cre_topic6():
    print("=" * 80)
    print("VLEARN CBC GRADE 9 CRE — TOPIC 6: HEALING OF THE TEN LEPERS INGESTION")
    print("=" * 80)

    with transaction.atomic():
        # 1. Resolve Grade 9 (ID: 18) and Subject CRE (ID: 50)
        grade = Grade.objects.get(id=18)
        subject = Subject.objects.get(id=50, grade=grade)

        print(f"[*] Grade  : {grade.name} (ID: {grade.id})")
        print(f"[*] Subject: {subject.name} (ID: {subject.id})")

        # 2. Resolve/Create Topic 6 under Subject 50
        topic_name = "Healing of the Ten Lepers"
        topic_desc = (
            "The miracle of Jesus Christ healing ten men afflicted with leprosy along the border of Samaria "
            "and Galilee. Explores the medical and social reality of biblical leprosy, the cry for mercy, "
            "the command of faith, the dramatic healing on the journey, the return of the thankful Samaritan outcast, "
            "and practical daily habits for cultivating lifelong gratitude and forgiveness."
        )

        topic, created = Topic.objects.get_or_create(
            subject=subject,
            order=6,
            defaults={
                "name": topic_name,
                "description": clean_text(topic_desc),
            }
        )
        if not created:
            topic.name = topic_name
            topic.description = clean_text(topic_desc)
            topic.save()
            print(f"[*] Resolved existing Topic ID: {topic.id} (Order: {topic.order}, Name: '{topic.name}')")
        else:
            print(f"[+] Created new Topic ID: {topic.id} (Order: {topic.order}, Name: '{topic.name}')")

        total_lessons_ingested = 0
        total_blocks_created = 0
        total_assets_created = 0

        # 3. Iterate over all 6 lessons
        for lesson_idx, cfg in enumerate(LESSONS_DATA, start=1):
            print("\n" + "-" * 70)
            print(f"INGESTING LESSON {lesson_idx}/6: {cfg['lesson_title']}")
            print("-" * 70)

            u_order = cfg["unit_order"]
            u_name = cfg["unit_name"]
            l_title = cfg["lesson_title"]

            # Remove existing learning unit with this order under this topic
            existing_units = LearningUnit.objects.filter(topic=topic, order=u_order)
            if existing_units.exists():
                for eu in existing_units:
                    print(f"[*] Cleaning up existing LearningUnit order={u_order} (ID: {eu.id})")
                    eu.delete()

            # Create LearningUnit
            unit = LearningUnit.objects.create(
                topic=topic,
                order=u_order,
                name=clean_text(u_name),
                description=clean_text(cfg["unit_description"])
            )
            print(f"[+] Created LearningUnit ID: {unit.id} ('{unit.name}', order={unit.order})")

            # Create Published Lesson
            lesson = Lesson.objects.create(
                topic=topic,
                learning_unit=unit,
                title=clean_text(l_title),
                status="published",
                version=1,
                immutable_metadata={
                    "grade": "Grade 9",
                    "subject": "CRE",
                    "topic_order": 6,
                    "topic_name": topic.name,
                    "unit_order": u_order,
                    "lesson_order": lesson_idx,
                    "author": "VLearn Grade 9 CRE Pedagogical Ingestion Engine",
                    "curriculum_framework": "CBC Kenya",
                    "enrichment_version": "v3_pedagogical_standard"
                }
            )
            print(f"[+] Created Lesson ID: {lesson.id} ('{lesson.title}', status={lesson.status})")

            # ─── CREATE 3 LESSON ASSETS ───────────────────────────────────────
            # Asset 1: Image
            img_info = cfg["image"]
            img_asset = LessonAsset.objects.create(
                lesson=lesson,
                asset_type="image",
                source_type="external",
                storage_type="url",
                status="attached",
                title=clean_text(img_info["title"]),
                description=clean_text(img_info["caption"]),
                url=img_info["url"],
                metadata={
                    "author": img_info["author"],
                    "licensing": img_info["licensing"],
                    "source": img_info["source"],
                    "caption": clean_text(img_info["caption"])
                }
            )

            # Asset 2: Responsive Vector SVG Diagram
            svg_content = cfg["svg_fn"]()
            svg_asset = LessonAsset.objects.create(
                lesson=lesson,
                asset_type="diagram",
                source_type="ai_generated",
                storage_type="url",
                status="attached",
                title=f"Diagram: {l_title}",
                description=f"Responsive pedagogical vector SVG diagram illustrating {l_title}.",
                url=f"https://vlearn.africa/assets/diagrams/cre/grade9_topic_6_lesson_{lesson_idx}.svg",
                metadata={
                    "svg_xml": svg_content,
                    "viewBox": "0 0 800 450",
                    "theme": "#0f172a"
                }
            )

            # Asset 3: YouTube Video
            yt_info = cfg["youtube"]
            yt_asset = LessonAsset.objects.create(
                lesson=lesson,
                asset_type="youtube",
                source_type="external",
                storage_type="url",
                status="attached",
                title=clean_text(yt_info["title"]),
                description=clean_text(yt_info["description"]),
                url=f"https://www.youtube.com/watch?v={yt_info['youtube_id']}",
                metadata={
                    "youtube_id": yt_info["youtube_id"],
                    "embed_url": f"https://www.youtube.com/embed/{yt_info['youtube_id']}"
                }
            )
            total_assets_created += 3
            print(f"[+] Created & Attached 3 LessonAssets (Image, SVG Diagram, YouTube Video)")

            # ─── CREATE 6 CARDS / PAGES WITH 13 LESSON BLOCKS ─────────────────

            # CARD 1 (Page 1): Discovery & Objectives (3 blocks)
            # Block 1: suggested_image
            b1 = LessonBlock.objects.create(
                lesson=lesson, page_number=1, page_title="Discovery & Objectives",
                order=10, component_order=1,
                block_type="suggested_image", component_type="suggested_image",
                title=clean_text(img_info["title"]),
                content={
                    "title": clean_text(img_info["title"]),
                    "url": img_info["url"],
                    "resolved_image_url": img_info["url"],
                    "caption": clean_text(img_info["caption"]),
                    "author": img_info["author"],
                    "licensing": img_info["licensing"],
                    "source": img_info["source"]
                }
            )
            b1.assets.add(img_asset)

            # Block 2: learning_goal (3 Bloom's goals)
            LessonBlock.objects.create(
                lesson=lesson, page_number=1, page_title="Discovery & Objectives",
                order=20, component_order=2,
                block_type="learning_goal", component_type="learning_goal",
                title="Lesson Objectives",
                content={"goals": clean_dict(cfg["goals"])}
            )

            # Block 3: concept_explanation (engaging hook)
            LessonBlock.objects.create(
                lesson=lesson, page_number=1, page_title="Discovery & Objectives",
                order=30, component_order=3,
                block_type="concept_explanation", component_type="concept_explanation",
                title="Sharing Experiences & Familiar Connection",
                content={"markdown": clean_text(cfg["intro"])}
            )

            # CARD 2 (Page 2): Scriptural Exegesis (2 blocks)
            # Block 4: concept_explanation (Scripture passage)
            LessonBlock.objects.create(
                lesson=lesson, page_number=2, page_title="Scriptural Exegesis",
                order=40, component_order=1,
                block_type="concept_explanation", component_type="concept_explanation",
                title="Core Biblical Foundations",
                content={"markdown": clean_text(cfg["core_scripture"])}
            )

            # Block 5: concept_explanation (Theological exegesis)
            LessonBlock.objects.create(
                lesson=lesson, page_number=2, page_title="Scriptural Exegesis",
                order=45, component_order=2,
                block_type="concept_explanation", component_type="concept_explanation",
                title="Theological Dimensions & Spiritual Pillars",
                content={"markdown": clean_text(cfg["theological_pillars"])}
            )

            # CARD 3 (Page 3): Pedagogical Diagram & Deep Dive (2 blocks)
            # Block 6: suggested_diagram
            b6 = LessonBlock.objects.create(
                lesson=lesson, page_number=3, page_title="Vector SVG Diagram & Deep Dive",
                order=50, component_order=1,
                block_type="suggested_diagram", component_type="suggested_diagram",
                title=f"Diagram: {l_title}",
                content={
                    "title": f"Pedagogical Diagram: {l_title}",
                    "caption": f"Responsive vector diagram illustrating key theological and moral concepts for {l_title}.",
                    "svg": svg_content,
                    "svg_xml": svg_content
                }
            )
            b6.assets.add(svg_asset)

            # Block 7: concept_explanation (Deep dive analysis)
            LessonBlock.objects.create(
                lesson=lesson, page_number=3, page_title="Vector SVG Diagram & Deep Dive",
                order=60, component_order=2,
                block_type="concept_explanation", component_type="concept_explanation",
                title="Deep Dive Analysis & Biblical Context",
                content={"markdown": clean_text(cfg["deep_dive"])}
            )

            # CARD 4 (Page 4): Practical Application & Context (2 blocks)
            # Block 8: step_process (4-step actionable framework)
            LessonBlock.objects.create(
                lesson=lesson, page_number=4, page_title="Practical Application",
                order=70, component_order=1,
                block_type="step_process", component_type="step_process",
                title=clean_text(cfg["practical"]["title"]),
                content=clean_dict(cfg["practical"])
            )

            # Block 9: concept_explanation (Kenyan context & breaking barriers)
            LessonBlock.objects.create(
                lesson=lesson, page_number=4, page_title="Practical Application",
                order=75, component_order=2,
                block_type="concept_explanation", component_type="concept_explanation",
                title="Kenyan Real-World Context & Overcoming Division",
                content={"markdown": clean_text(cfg["kenyan_context"])}
            )

            # CARD 5 (Page 5): Multimedia & Reflection (2 blocks)
            # Block 10: suggested_video
            b10 = LessonBlock.objects.create(
                lesson=lesson, page_number=5, page_title="Multimedia & Reflection",
                order=80, component_order=1,
                block_type="suggested_video", component_type="suggested_video",
                title=clean_text(yt_info["title"]),
                content={
                    "title": clean_text(yt_info["title"]),
                    "url": f"https://www.youtube.com/watch?v={yt_info['youtube_id']}",
                    "youtube_id": yt_info["youtube_id"],
                    "description": clean_text(yt_info["description"])
                }
            )
            b10.assets.add(yt_asset)

            # Block 11: concept_explanation (Spiritual reflection)
            LessonBlock.objects.create(
                lesson=lesson, page_number=5, page_title="Multimedia & Reflection",
                order=90, component_order=2,
                block_type="concept_explanation", component_type="concept_explanation",
                title="Spiritual Reflection & Personal Examination",
                content={"markdown": clean_text(cfg["reflection"])}
            )

            # CARD 6 (Page 6): Mastery Check (2 blocks)
            # Block 12: summary (Key takeaways)
            LessonBlock.objects.create(
                lesson=lesson, page_number=6, page_title="Mastery Check",
                order=100, component_order=1,
                block_type="summary", component_type="summary",
                title="Summary & Core Takeaways",
                content={
                    "title": f"Key Takeaways: {l_title}",
                    "takeaways": clean_dict(cfg["takeaways"])
                }
            )

            # Block 13: knowledge_check (4-option MCQ)
            LessonBlock.objects.create(
                lesson=lesson, page_number=6, page_title="Mastery Check",
                order=110, component_order=2,
                block_type="knowledge_check", component_type="knowledge_check",
                title="Mastery Assessment",
                content=clean_dict(cfg["mcq"])
            )

            lesson_blocks_count = lesson.blocks.count()
            total_blocks_created += lesson_blocks_count
            total_lessons_ingested += 1

            print(f"[+] Successfully Created 6 Cards / {lesson_blocks_count} Blocks for Lesson {lesson_idx}")

        print("\n" + "=" * 80)
        print("TOPIC 6 INGESTION SUMMARY & METRICS")
        print("=" * 80)
        print(f"• Grade               : {grade.name} (ID: {grade.id})")
        print(f"• Subject             : {subject.name} (ID: {subject.id})")
        print(f"• Topic               : {topic.name} (ID: {topic.id}, Order: {topic.order})")
        print(f"• Learning Units Count: {topic.learning_units.count()}")
        print(f"• Lessons Ingested    : {total_lessons_ingested}")
        print(f"• Total Cards / Pages : {total_lessons_ingested * 6}")
        print(f"• Total Blocks Created: {total_blocks_created} (13 blocks/lesson)")
        print(f"• Total Assets Created: {total_assets_created} (3 assets/lesson)")
        print("=" * 80)


if __name__ == "__main__":
    ingest_cbc_grade9_cre_topic6()
