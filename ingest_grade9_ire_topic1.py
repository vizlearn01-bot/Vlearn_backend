"""
VLearn CBC Grade 9 IRE — Topic 1: Ulum al-Qur'an (The Sciences of the Qur'an)
Production Ingestion & Pedagogical Enrichment Engine

Target Topic: Topic ID 341 (CBC -> Grade 9 -> IRE -> Ulum al-Qur'an (The Sciences of the Qur'an))
Source File: /home/jason-bitega/Desktop/VL/vlearn_repositories/Grade 9 IRE/ulum-al-quran.md

7 Lessons Ingested & Fully Enriched:
  1. Lesson 1.1.1: What makes a miracle?
  2. Lesson 1.1.2: The miraculous nature of the Qur’an
  3. Lesson 1.1.3: The language of the Qur’an
  4. Lesson 1.1.4: Styles of the Qur’an
  5. Lesson 1.1.5: Reading for meaning and interpretation
  6. Lesson 1.1.6: Research and presentation
  7. Lesson 1.1.7: Unit synthesis: the Qur’an as guidance

Card Structure (7 Cards per Lesson):
  Card 1 (page 1): learning_goal (Inquiry question + Connection hook + Objectives)
  Card 2 (page 2): concept_explanation (Authoritative concept) + callout (Scripture Panel: Surah & verse with translation)
  Card 3 (page 3): concept_explanation (Deep explanation) + suggested_diagram (Full vector SVG + LessonAsset) + comparison_table / step_process
  Card 4 (page 4): worked_example (Relatable student scenario with analysis)
  Card 5 (page 5): real_world_example (Actionable real-world application) + reflection (Pause & reflect prompt) + common_misconception
  Card 6 (page 6): knowledge_check (Interactive MCQ: question, options, answer, explanation)
  Card 7 (page 7): summary (Key points + Vocabulary review) + mini_activity (Exit ticket)
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
    Topic, LearningUnit, Lesson, LessonBlock, LessonAsset
)


def clean_text(text: str) -> str:
    """Removes bracket citations and internal meta tags while preserving markdown."""
    if not text:
        return ""
    # Strip bracket citations e.g. [1], [223], [1, 2]
    text = re.sub(r'\[(?:\d+(?:\.\d+)?(?:,\s*\d+(?:\.\d+)?)*)\]', '', text)
    # Strip internal pedagogical tags
    text = re.sub(
        r'\[(VISUAL|QURAN REFERENCE|CRITICAL THINKING|VALUES|MISCONCEPTION|INTERACTION|'
        r'ETHICAL SCENARIO|KEY VERSE|REAL WORLD APPLICATION|PEDAGOGICAL ARCHITECTURE|'
        r'PROJECT TITLE|REFLECTION|COMPARISON TABLE|MISCONCEPTION CHECK)[^\]]*\]',
        '', text, flags=re.IGNORECASE
    )
    # Normalize list bullet points
    text = re.sub(r'^[ \t]*[•\u2022][ \t]*', '- ', text, flags=re.MULTILINE)
    text = re.sub(r'([^\n])[ \t]+[•\u2022][ \t]+', r'\1\n- ', text)
    return text.strip()


def clean_dict(data):
    if isinstance(data, str):
        return clean_text(data)
    elif isinstance(data, dict):
        return {k: clean_dict(v) for k, v in data.items()}
    elif isinstance(data, list):
        return [clean_dict(item) for item in data]
    return data


TOPIC_1_VIDEOS = {
    1: {
        "title": "Understanding Miracles (Mu'jizah) in Islamic Theology",
        "yt_id": "8VfK-3qYtX8",
        "description": "An educational breakdown of the definition, conditions, and purpose of divine miracles granted to the Prophets."
    },
    2: {
        "title": "The Miraculous Inimitability (I'jaz) of the Qur'an",
        "yt_id": "2M0H6p8V3jA",
        "description": "Exploration of the literary and intellectual challenge of the Qur'an to humanity throughout the centuries."
    },
    3: {
        "title": "The Linguistic Architecture of the Holy Qur'an",
        "yt_id": "sZ9B5e7pW4M",
        "description": "How classical Arabic morphology, rhythm, and syntax combine to create the unique text of the Qur'an."
    },
    4: {
        "title": "Literary Styles and Parables of the Qur'an",
        "yt_id": "eJ4X7t9V1uL",
        "description": "Understanding divine storytelling, oaths, allegories, and rhetorical questions across Meccan and Medinan Surahs."
    },
    5: {
        "title": "Principles of Qur'anic Interpretation (Usul al-Tafsir)",
        "yt_id": "fW8G3r5Y7nM",
        "description": "A guide to reading the Qur'an with understanding, context (Asbab al-Nuzul), and classical Tafsir methodologies."
    },
    6: {
        "title": "Effective Research and Thematic Presentation in Islamic Studies",
        "yt_id": "hB3P7t1Z9qR",
        "description": "Developing critical inquiry, source-validation, and academic communication skills for religious education."
    },
    7: {
        "title": "The Qur'an: The Ultimate Blueprint for Living",
        "yt_id": "jN2T8w4X6pY",
        "description": "Synthesis of Strand 1.0 on how the Qur'an guides individual morality, social justice, and civic responsibility."
    }
}


# ─────────────────────────────────────────────────────────────────────────────
# 7 CUSTOM RESPONSIVE VECTOR SVGS (viewBox="0 0 880 480", #0f172a theme)
# ─────────────────────────────────────────────────────────────────────────────

def get_svg_lesson_1():
    return """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 880 480" width="100%" height="100%">
  <defs>
    <linearGradient id="bg1" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#0f172a"/>
      <stop offset="50%" stop-color="#1e293b"/>
      <stop offset="100%" stop-color="#0f172a"/>
    </linearGradient>
    <linearGradient id="blueGrad1" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#0284c7"/>
      <stop offset="100%" stop-color="#0369a1"/>
    </linearGradient>
    <linearGradient id="emeraldGrad1" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#10b981"/>
      <stop offset="100%" stop-color="#059669"/>
    </linearGradient>
    <filter id="glow1" x="-10%" y="-10%" width="120%" height="120%">
      <feDropShadow dx="0" dy="4" stdDeviation="6" flood-color="#000000" flood-opacity="0.4"/>
    </filter>
  </defs>

  <rect width="880" height="480" fill="url(#bg1)" rx="14"/>
  <rect x="15" y="15" width="850" height="450" fill="none" stroke="#334155" stroke-width="1.5" stroke-dasharray="6 4" rx="10"/>

  <text x="440" y="46" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="17" font-weight="800" text-anchor="middle" letter-spacing="1">HUMAN ACHIEVEMENT VS. DIVINE MIRACLE (MU‘JIZAH)</text>
  <text x="440" y="68" fill="#94a3b8" font-family="system-ui, sans-serif" font-size="12" text-anchor="middle">Distinguishing Progressive Scientific Innovation from Supernatural Prophetic Authentication</text>

  <!-- Left Card: Human Achievement -->
  <g transform="translate(45, 90)" filter="url(#glow1)">
    <rect width="370" height="305" rx="12" fill="#1e293b" stroke="#0284c7" stroke-width="1.5"/>
    <rect width="370" height="42" rx="12" fill="url(#blueGrad1)"/>
    <rect x="0" y="30" width="370" height="12" fill="url(#blueGrad1)"/>
    <text x="185" y="27" fill="#ffffff" font-family="system-ui, sans-serif" font-size="14" font-weight="800" text-anchor="middle">HUMAN ACHIEVEMENT</text>
    
    <rect x="25" y="55" width="135" height="20" rx="4" fill="#082f49"/>
    <text x="92" y="69" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="10" font-weight="700" text-anchor="middle">SCIENTIFIC PROGRESS</text>

    <circle cx="32" cy="98" r="4" fill="#38bdf8"/>
    <text x="44" y="96" fill="#f8fafc" font-family="system-ui, sans-serif" font-size="11.5" font-weight="700">Origin &amp; Power:</text>
    <text x="44" y="112" fill="#94a3b8" font-family="system-ui, sans-serif" font-size="11">Human intellect, research &amp; iterative trial-and-error.</text>

    <circle cx="32" cy="140" r="4" fill="#38bdf8"/>
    <text x="44" y="138" fill="#f8fafc" font-family="system-ui, sans-serif" font-size="11.5" font-weight="700">Natural Law Relation:</text>
    <text x="44" y="154" fill="#94a3b8" font-family="system-ui, sans-serif" font-size="11">Operates strictly within natural physical laws.</text>

    <circle cx="32" cy="182" r="4" fill="#38bdf8"/>
    <text x="44" y="180" fill="#f8fafc" font-family="system-ui, sans-serif" font-size="11.5" font-weight="700">Reproducibility:</text>
    <text x="44" y="196" fill="#94a3b8" font-family="system-ui, sans-serif" font-size="11">Can be copied and improved by any trained team.</text>

    <circle cx="32" cy="224" r="4" fill="#38bdf8"/>
    <text x="44" y="222" fill="#f8fafc" font-family="system-ui, sans-serif" font-size="11.5" font-weight="700">Primary Purpose:</text>
    <text x="44" y="238" fill="#94a3b8" font-family="system-ui, sans-serif" font-size="11">Material utility, commercial ease &amp; exploration.</text>

    <rect x="20" y="258" width="330" height="34" rx="6" fill="#0f172a" stroke="#1e3a5f" stroke-width="1"/>
    <text x="185" y="280" fill="#7dd3fc" font-family="system-ui, sans-serif" font-size="11" font-weight="600" text-anchor="middle">Example: Rocketry, Delivery Drones, Supercomputers</text>
  </g>

  <!-- Center 'VS' Circle -->
  <g transform="translate(440, 242)">
    <circle cx="0" cy="0" r="26" fill="#0f172a" stroke="#f59e0b" stroke-width="2"/>
    <text x="0" y="6" fill="#f59e0b" font-family="system-ui, sans-serif" font-size="14" font-weight="900" text-anchor="middle">VS</text>
  </g>

  <!-- Right Card: Divine Miracle -->
  <g transform="translate(465, 90)" filter="url(#glow1)">
    <rect width="370" height="305" rx="12" fill="#1e293b" stroke="#10b981" stroke-width="1.5"/>
    <rect width="370" height="42" rx="12" fill="url(#emeraldGrad1)"/>
    <rect x="0" y="30" width="370" height="12" fill="url(#emeraldGrad1)"/>
    <text x="185" y="27" fill="#ffffff" font-family="system-ui, sans-serif" font-size="14" font-weight="800" text-anchor="middle">DIVINE MIRACLE (MU‘JIZAH)</text>

    <rect x="25" y="55" width="145" height="20" rx="4" fill="#064e3b"/>
    <text x="97" y="69" fill="#34d399" font-family="system-ui, sans-serif" font-size="10" font-weight="700" text-anchor="middle">SUPERNATURAL EVIDENCE</text>

    <circle cx="32" cy="98" r="4" fill="#34d399"/>
    <text x="44" y="96" fill="#f8fafc" font-family="system-ui, sans-serif" font-size="11.5" font-weight="700">Origin &amp; Power:</text>
    <text x="44" y="112" fill="#94a3b8" font-family="system-ui, sans-serif" font-size="11">Direct command and sole permission of Allah (S.W.T.).</text>

    <circle cx="32" cy="140" r="4" fill="#34d399"/>
    <text x="44" y="138" fill="#f8fafc" font-family="system-ui, sans-serif" font-size="11.5" font-weight="700">Natural Law Relation:</text>
    <text x="44" y="154" fill="#94a3b8" font-family="system-ui, sans-serif" font-size="11">Suspends natural laws (Kharq al-‘Adah) instantaneously.</text>

    <circle cx="32" cy="182" r="4" fill="#34d399"/>
    <text x="44" y="180" fill="#f8fafc" font-family="system-ui, sans-serif" font-size="11.5" font-weight="700">Reproducibility:</text>
    <text x="44" y="196" fill="#94a3b8" font-family="system-ui, sans-serif" font-size="11">Impossible to replicate (I‘jaz) by human effort or magic.</text>

    <circle cx="32" cy="224" r="4" fill="#34d399"/>
    <text x="44" y="222" fill="#f8fafc" font-family="system-ui, sans-serif" font-size="11.5" font-weight="700">Primary Purpose:</text>
    <text x="44" y="238" fill="#94a3b8" font-family="system-ui, sans-serif" font-size="11">Proves prophet's truthfulness &amp; solidifies faith (Iman).</text>

    <rect x="20" y="258" width="330" height="34" rx="6" fill="#0f172a" stroke="#065f46" stroke-width="1"/>
    <text x="185" y="280" fill="#a7f3d0" font-family="system-ui, sans-serif" font-size="11" font-weight="600" text-anchor="middle">Example: Parting Red Sea, Staff of Musa, Water from Fingers</text>
  </g>

  <!-- Bottom Core Insight Banner -->
  <g transform="translate(45, 410)">
    <rect width="790" height="42" rx="8" fill="#1e293b" stroke="#475569" stroke-width="1"/>
    <text x="395" y="26" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="11.5" font-weight="600" text-anchor="middle">
      <tspan fill="#38bdf8" font-weight="700">Key Distinguishing Rule: </tspan>Human tools harness creation's laws; Divine miracles suspend creation's laws by the Creator's will.
    </text>
  </g>
</svg>"""


def get_svg_lesson_2():
    return """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 880 480" width="100%" height="100%">
  <defs>
    <linearGradient id="bg2" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#0f172a"/>
      <stop offset="50%" stop-color="#1e293b"/>
      <stop offset="100%" stop-color="#0f172a"/>
    </linearGradient>
    <linearGradient id="goldGrad2" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#f59e0b"/>
      <stop offset="100%" stop-color="#b45309"/>
    </linearGradient>
    <filter id="glow2" x="-10%" y="-10%" width="120%" height="120%">
      <feDropShadow dx="0" dy="4" stdDeviation="6" flood-color="#000000" flood-opacity="0.4"/>
    </filter>
  </defs>

  <rect width="880" height="480" fill="url(#bg2)" rx="14"/>
  <rect x="15" y="15" width="850" height="450" fill="none" stroke="#334155" stroke-width="1.5" stroke-dasharray="6 4" rx="10"/>

  <text x="440" y="44" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="17" font-weight="800" text-anchor="middle" letter-spacing="1">THE FOUR PILLARS OF I‘JAZ AL-QUR'AN</text>
  <text x="440" y="66" fill="#94a3b8" font-family="system-ui, sans-serif" font-size="12" text-anchor="middle">The Multi-Faceted Inimitability and Enduring Nature of the Holy Qur'an</text>

  <!-- Connecting Lines from Center -->
  <line x1="440" y1="240" x2="215" y2="155" stroke="#38bdf8" stroke-width="2" stroke-dasharray="4 3" opacity="0.6"/>
  <line x1="440" y1="240" x2="665" y2="155" stroke="#f59e0b" stroke-width="2" stroke-dasharray="4 3" opacity="0.6"/>
  <line x1="440" y1="240" x2="215" y2="330" stroke="#10b981" stroke-width="2" stroke-dasharray="4 3" opacity="0.6"/>
  <line x1="440" y1="240" x2="665" y2="330" stroke="#a855f7" stroke-width="2" stroke-dasharray="4 3" opacity="0.6"/>

  <!-- Center Hub -->
  <g transform="translate(440, 240)">
    <circle cx="0" cy="0" r="70" fill="#0f172a" stroke="#f59e0b" stroke-width="3"/>
    <circle cx="0" cy="0" r="62" fill="#1e293b" stroke="#334155" stroke-width="1"/>
    <text x="0" y="-18" fill="#fbbf24" font-family="system-ui, sans-serif" font-size="13" font-weight="800" text-anchor="middle">I‘JAZ</text>
    <text x="0" y="0" fill="#f8fafc" font-family="system-ui, sans-serif" font-size="12" font-weight="700" text-anchor="middle">AL-QUR'AN</text>
    <text x="0" y="18" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="9.5" font-weight="600" text-anchor="middle">LIVING MIRACLE</text>
    <text x="0" y="32" fill="#94a3b8" font-family="system-ui, sans-serif" font-size="8.5" text-anchor="middle">For All Generations</text>
  </g>

  <!-- Pillar 1: Top-Left (Literary Perfection) -->
  <g transform="translate(45, 90)" filter="url(#glow2)">
    <rect width="330" height="130" rx="10" fill="#1e293b" stroke="#38bdf8" stroke-width="1.5"/>
    <rect width="330" height="28" rx="10" fill="#0284c7"/>
    <rect x="0" y="20" width="330" height="8" fill="#0284c7"/>
    <text x="165" y="19" fill="#ffffff" font-family="system-ui, sans-serif" font-size="11.5" font-weight="800" text-anchor="middle">1. LITERARY PERFECTION</text>
    <text x="16" y="52" fill="#f8fafc" font-family="system-ui, sans-serif" font-size="10.5" font-weight="600">• Neither Poetry nor Prose:</text>
    <text x="24" y="68" fill="#94a3b8" font-family="system-ui, sans-serif" font-size="10">Unique rhythm, sublime eloquence &amp; pristine style.</text>
    <text x="16" y="90" fill="#f8fafc" font-family="system-ui, sans-serif" font-size="10.5" font-weight="600">• Linguistic Inimitability:</text>
    <text x="24" y="106" fill="#94a3b8" font-family="system-ui, sans-serif" font-size="10">Flawless word choice and precise grammatical harmony.</text>
  </g>

  <!-- Pillar 2: Top-Right (Divine Challenge) -->
  <g transform="translate(505, 90)" filter="url(#glow2)">
    <rect width="330" height="130" rx="10" fill="#1e293b" stroke="#f59e0b" stroke-width="1.5"/>
    <rect width="330" height="28" rx="10" fill="#d97706"/>
    <rect x="0" y="20" width="330" height="8" fill="#d97706"/>
    <text x="165" y="19" fill="#ffffff" font-family="system-ui, sans-serif" font-size="11.5" font-weight="800" text-anchor="middle">2. DIVINE CHALLENGE (TAHADDI)</text>
    <text x="16" y="52" fill="#f8fafc" font-family="system-ui, sans-serif" font-size="10.5" font-weight="600">• The Standing Challenge:</text>
    <text x="24" y="68" fill="#94a3b8" font-family="system-ui, sans-serif" font-size="10">"Produce a surah the like thereof" (Q 2:23).</text>
    <text x="16" y="90" fill="#f8fafc" font-family="system-ui, sans-serif" font-size="10.5" font-weight="600">• Unmet Across History:</text>
    <text x="24" y="106" fill="#94a3b8" font-family="system-ui, sans-serif" font-size="10">Pre-Islamic master poets failed to match even one short surah.</text>
  </g>

  <!-- Pillar 3: Bottom-Left (Perfect Preservation) -->
  <g transform="translate(45, 265)" filter="url(#glow2)">
    <rect width="330" height="130" rx="10" fill="#1e293b" stroke="#10b981" stroke-width="1.5"/>
    <rect width="330" height="28" rx="10" fill="#059669"/>
    <rect x="0" y="20" width="330" height="8" fill="#059669"/>
    <text x="165" y="19" fill="#ffffff" font-family="system-ui, sans-serif" font-size="11.5" font-weight="800" text-anchor="middle">3. PERFECT PRESERVATION</text>
    <text x="16" y="52" fill="#f8fafc" font-family="system-ui, sans-serif" font-size="10.5" font-weight="600">• Divine Protection Promise:</text>
    <text x="24" y="68" fill="#94a3b8" font-family="system-ui, sans-serif" font-size="10">"We sent down the Qur'an and We will guard it" (Q 15:9).</text>
    <text x="16" y="90" fill="#f8fafc" font-family="system-ui, sans-serif" font-size="10.5" font-weight="600">• Dual Transmission:</text>
    <text x="24" y="106" fill="#94a3b8" font-family="system-ui, sans-serif" font-size="10">Millions of Huffaz memorizers + ancient manuscript codices.</text>
  </g>

  <!-- Pillar 4: Bottom-Right (Universal Guidance) -->
  <g transform="translate(505, 265)" filter="url(#glow2)">
    <rect width="330" height="130" rx="10" fill="#1e293b" stroke="#a855f7" stroke-width="1.5"/>
    <rect width="330" height="28" rx="10" fill="#7c3aed"/>
    <rect x="0" y="20" width="330" height="8" fill="#7c3aed"/>
    <text x="165" y="19" fill="#ffffff" font-family="system-ui, sans-serif" font-size="11.5" font-weight="800" text-anchor="middle">4. COMPREHENSIVE GUIDANCE</text>
    <text x="16" y="52" fill="#f8fafc" font-family="system-ui, sans-serif" font-size="10.5" font-weight="600">• Complete Human Blueprint:</text>
    <text x="24" y="68" fill="#94a3b8" font-family="system-ui, sans-serif" font-size="10">Spiritual, moral, economic &amp; social justice frameworks.</text>
    <text x="16" y="90" fill="#f8fafc" font-family="system-ui, sans-serif" font-size="10.5" font-weight="600">• Societal Transformation:</text>
    <text x="24" y="106" fill="#94a3b8" font-family="system-ui, sans-serif" font-size="10">Elevated tribal society into a global intellectual civilization.</text>
  </g>

  <!-- Bottom Banner -->
  <g transform="translate(45, 415)">
    <rect width="790" height="38" rx="8" fill="#1e293b" stroke="#334155" stroke-width="1"/>
    <text x="395" y="24" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="11" font-weight="600" text-anchor="middle">
      <tspan fill="#f59e0b" font-weight="700">The Living Miracle: </tspan>Physical miracles ended with their witnesses; the Qur'an remains open, audible, and testable today.
    </text>
  </g>
</svg>"""


def get_svg_lesson_3():
    return """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 880 480" width="100%" height="100%">
  <defs>
    <linearGradient id="bg3" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#0f172a"/>
      <stop offset="50%" stop-color="#1e293b"/>
      <stop offset="100%" stop-color="#0f172a"/>
    </linearGradient>
    <filter id="glow3" x="-10%" y="-10%" width="120%" height="120%">
      <feDropShadow dx="0" dy="4" stdDeviation="6" flood-color="#000000" flood-opacity="0.4"/>
    </filter>
  </defs>

  <rect width="880" height="480" fill="url(#bg3)" rx="14"/>
  <rect x="15" y="15" width="850" height="450" fill="none" stroke="#334155" stroke-width="1.5" stroke-dasharray="6 4" rx="10"/>

  <text x="440" y="44" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="17" font-weight="800" text-anchor="middle" letter-spacing="1">3-TIER FRAMEWORK: TEXT, TRANSLATION &amp; TAFSIR</text>
  <text x="440" y="66" fill="#94a3b8" font-family="system-ui, sans-serif" font-size="12" text-anchor="middle">Preserving Sacred Divine Revelation While Navigating Language and Meaning</text>

  <!-- Tier 1: Original Arabic Text -->
  <g transform="translate(50, 85)" filter="url(#glow3)">
    <rect width="780" height="92" rx="10" fill="#1e293b" stroke="#f59e0b" stroke-width="2"/>
    <rect width="780" height="28" rx="10" fill="#d97706"/>
    <rect x="0" y="20" width="780" height="8" fill="#d97706"/>
    <text x="25" y="19" fill="#ffffff" font-family="system-ui, sans-serif" font-size="12" font-weight="800">TIER 1: THE SACRED ARABIC REVELATION (KALAMULLAH)</text>
    <rect x="635" y="4" width="130" height="20" rx="4" fill="#451a03"/>
    <text x="700" y="18" fill="#fef3c7" font-family="system-ui, sans-serif" font-size="10" font-weight="700" text-anchor="middle">LITERAL WORD OF ALLAH</text>
    
    <text x="20" y="50" fill="#fef3c7" font-family="system-ui, sans-serif" font-size="11" font-weight="600">• Revealed Verbatim in Clear Arabic (Lisan 'Arabi Mubin — Q 12:2, 26:195) to Prophet Muhammad (PBUH).</text>
    <text x="20" y="70" fill="#94a3b8" font-family="system-ui, sans-serif" font-size="10.5">• The only text recited in Salah. Inimitable (Mu‘jiz), divine, and preserved without a single syllable changed.</text>
  </g>

  <!-- Connecting Arrow 1 -->
  <g transform="translate(440, 182)">
    <polygon points="-8,-4 0,4 8,-4" fill="#38bdf8"/>
  </g>

  <!-- Tier 2: Translation of Meanings -->
  <g transform="translate(50, 192)" filter="url(#glow3)">
    <rect width="780" height="92" rx="10" fill="#1e293b" stroke="#0284c7" stroke-width="1.5"/>
    <rect width="780" height="28" rx="10" fill="#0284c7"/>
    <rect x="0" y="20" width="780" height="8" fill="#0284c7"/>
    <text x="25" y="19" fill="#ffffff" font-family="system-ui, sans-serif" font-size="12" font-weight="800">TIER 2: TRANSLATION OF MEANINGS (TARJAMAT AL-MA‘ANI)</text>
    <rect x="630" y="4" width="135" height="20" rx="4" fill="#082f49"/>
    <text x="697" y="18" fill="#bae6fd" font-family="system-ui, sans-serif" font-size="10" font-weight="700" text-anchor="middle">HUMAN APPROXIMATION</text>
    
    <text x="20" y="50" fill="#e0f2fe" font-family="system-ui, sans-serif" font-size="11" font-weight="600">• Human effort to convey Arabic meaning into English, Swahili, or other languages.</text>
    <text x="20" y="70" fill="#94a3b8" font-family="system-ui, sans-serif" font-size="10.5">• Cannot capture Arabic root depth, acoustic rhythm, or divine perfection. Serves as a guide, NOT the Qur'an itself.</text>
  </g>

  <!-- Connecting Arrow 2 -->
  <g transform="translate(440, 289)">
    <polygon points="-8,-4 0,4 8,-4" fill="#a855f7"/>
  </g>

  <!-- Tier 3: Scholarly Tafsir -->
  <g transform="translate(50, 299)" filter="url(#glow3)">
    <rect width="780" height="92" rx="10" fill="#1e293b" stroke="#a855f7" stroke-width="1.5"/>
    <rect width="780" height="28" rx="10" fill="#7c3aed"/>
    <rect x="0" y="20" width="780" height="8" fill="#7c3aed"/>
    <text x="25" y="19" fill="#ffffff" font-family="system-ui, sans-serif" font-size="12" font-weight="800">TIER 3: SCHOLARLY EXEGESIS (TAFSIR)</text>
    <rect x="615" y="4" width="150" height="20" rx="4" fill="#3b0764"/>
    <text x="690" y="18" fill="#f3e8ff" font-family="system-ui, sans-serif" font-size="10" font-weight="700" text-anchor="middle">CONTEXTUAL EXPLANATION</text>
    
    <text x="20" y="50" fill="#f3e8ff" font-family="system-ui, sans-serif" font-size="11" font-weight="600">• In-depth scholarly discipline exploring historical context (Asbab al-Nuzul) and Prophetic Hadith.</text>
    <text x="20" y="70" fill="#94a3b8" font-family="system-ui, sans-serif" font-size="10.5">• Clarifies legal rulings, metaphors, and ethical principles to prevent misunderstandings.</text>
  </g>

  <!-- Bottom Rule Banner -->
  <g transform="translate(50, 410)">
    <rect width="780" height="42" rx="8" fill="#1e293b" stroke="#475569" stroke-width="1"/>
    <text x="390" y="26" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="11" font-weight="600" text-anchor="middle">
      <tspan fill="#38bdf8" font-weight="700">Golden Academic Rule: </tspan>Say "The translation of the meaning is..." rather than "The Qur'an says in English."
    </text>
  </g>
</svg>"""


def get_svg_lesson_4():
    return """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 880 480" width="100%" height="100%">
  <defs>
    <linearGradient id="bg4" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#0f172a"/>
      <stop offset="50%" stop-color="#1e293b"/>
      <stop offset="100%" stop-color="#0f172a"/>
    </linearGradient>
    <filter id="glow4" x="-10%" y="-10%" width="120%" height="120%">
      <feDropShadow dx="0" dy="4" stdDeviation="6" flood-color="#000000" flood-opacity="0.4"/>
    </filter>
  </defs>

  <rect width="880" height="480" fill="url(#bg4)" rx="14"/>
  <rect x="15" y="15" width="850" height="450" fill="none" stroke="#334155" stroke-width="1.5" stroke-dasharray="6 4" rx="10"/>

  <text x="440" y="44" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="17" font-weight="800" text-anchor="middle" letter-spacing="1">USLUB AL-QUR'AN: DIVERSE COMMUNICATION STYLES</text>
  <text x="440" y="66" fill="#94a3b8" font-family="system-ui, sans-serif" font-size="12" text-anchor="middle">Engaging Intellect, Emotion, and Conscience Across Diverse Human Faculties (Surah Al-Kahf 18:54)</text>

  <!-- Connecting Lines -->
  <line x1="440" y1="240" x2="225" y2="155" stroke="#38bdf8" stroke-width="2" stroke-dasharray="4 3" opacity="0.6"/>
  <line x1="440" y1="240" x2="655" y2="155" stroke="#10b981" stroke-width="2" stroke-dasharray="4 3" opacity="0.6"/>
  <line x1="440" y1="240" x2="225" y2="325" stroke="#f59e0b" stroke-width="2" stroke-dasharray="4 3" opacity="0.6"/>
  <line x1="440" y1="240" x2="655" y2="325" stroke="#a855f7" stroke-width="2" stroke-dasharray="4 3" opacity="0.6"/>

  <!-- Center Circle -->
  <g transform="translate(440, 240)">
    <circle cx="0" cy="0" r="66" fill="#0f172a" stroke="#38bdf8" stroke-width="3"/>
    <circle cx="0" cy="0" r="58" fill="#1e293b" stroke="#334155" stroke-width="1"/>
    <text x="0" y="-14" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="12" font-weight="800" text-anchor="middle">USLUB</text>
    <text x="0" y="4" fill="#ffffff" font-family="system-ui, sans-serif" font-size="11" font-weight="700" text-anchor="middle">AL-QUR'AN</text>
    <text x="0" y="20" fill="#94a3b8" font-family="system-ui, sans-serif" font-size="9" text-anchor="middle">Diverse Styles</text>
  </g>

  <!-- Branch 1: Top-Left (Legislative) -->
  <g transform="translate(45, 90)" filter="url(#glow4)">
    <rect width="340" height="125" rx="10" fill="#1e293b" stroke="#38bdf8" stroke-width="1.5"/>
    <rect width="340" height="26" rx="10" fill="#0284c7"/>
    <rect x="0" y="18" width="340" height="8" fill="#0284c7"/>
    <text x="170" y="18" fill="#ffffff" font-family="system-ui, sans-serif" font-size="11" font-weight="800" text-anchor="middle">1. LEGISLATIVE STYLE (AMR &amp; NAHY)</text>
    <text x="14" y="50" fill="#f8fafc" font-family="system-ui, sans-serif" font-size="10.5" font-weight="600">• Commands &amp; Prohibitions:</text>
    <text x="22" y="66" fill="#94a3b8" font-family="system-ui, sans-serif" font-size="10">Direct, authoritative rules establishing justice (e.g. "Establish prayer").</text>
    <text x="14" y="88" fill="#f8fafc" font-family="system-ui, sans-serif" font-size="10.5" font-weight="600">• Purpose:</text>
    <text x="22" y="104" fill="#94a3b8" font-family="system-ui, sans-serif" font-size="10">Defines clear moral obligations (Fard) and boundaries (Haram).</text>
  </g>

  <!-- Branch 2: Top-Right (Narratives) -->
  <g transform="translate(495, 90)" filter="url(#glow4)">
    <rect width="340" height="125" rx="10" fill="#1e293b" stroke="#10b981" stroke-width="1.5"/>
    <rect width="340" height="26" rx="10" fill="#059669"/>
    <rect x="0" y="18" width="340" height="8" fill="#059669"/>
    <text x="170" y="18" fill="#ffffff" font-family="system-ui, sans-serif" font-size="11" font-weight="800" text-anchor="middle">2. NARRATIVE STYLE (QASAS)</text>
    <text x="14" y="50" fill="#f8fafc" font-family="system-ui, sans-serif" font-size="10.5" font-weight="600">• Historical Prophetic Accounts:</text>
    <text x="22" y="66" fill="#94a3b8" font-family="system-ui, sans-serif" font-size="10">Vivid stories of Musa, Ibrahim, Yusuf, and Maryam.</text>
    <text x="14" y="88" fill="#f8fafc" font-family="system-ui, sans-serif" font-size="10.5" font-weight="600">• Purpose:</text>
    <text x="22" y="104" fill="#94a3b8" font-family="system-ui, sans-serif" font-size="10">Extracts timeless ethical lessons and touches human emotions.</text>
  </g>

  <!-- Branch 3: Bottom-Left (Parables) -->
  <g transform="translate(45, 265)" filter="url(#glow4)">
    <rect width="340" height="125" rx="10" fill="#1e293b" stroke="#f59e0b" stroke-width="1.5"/>
    <rect width="340" height="26" rx="10" fill="#d97706"/>
    <rect x="0" y="18" width="340" height="8" fill="#d97706"/>
    <text x="170" y="18" fill="#ffffff" font-family="system-ui, sans-serif" font-size="11" font-weight="800" text-anchor="middle">3. PARABOLIC STYLE (AMTHAL)</text>
    <text x="14" y="50" fill="#f8fafc" font-family="system-ui, sans-serif" font-size="10.5" font-weight="600">• Metaphors &amp; Similes:</text>
    <text x="22" y="66" fill="#94a3b8" font-family="system-ui, sans-serif" font-size="10">Connecting spiritual truths to tangible physical realities.</text>
    <text x="14" y="88" fill="#f8fafc" font-family="system-ui, sans-serif" font-size="10.5" font-weight="600">• Example:</text>
    <text x="22" y="104" fill="#94a3b8" font-family="system-ui, sans-serif" font-size="10">Charity compared to a grain yielding seven ears of wheat (Q 2:261).</text>
  </g>

  <!-- Branch 4: Bottom-Right (Dialogue & Questions) -->
  <g transform="translate(495, 265)" filter="url(#glow4)">
    <rect width="340" height="125" rx="10" fill="#1e293b" stroke="#a855f7" stroke-width="1.5"/>
    <rect width="340" height="26" rx="10" fill="#7c3aed"/>
    <rect x="0" y="18" width="340" height="8" fill="#7c3aed"/>
    <text x="170" y="18" fill="#ffffff" font-family="system-ui, sans-serif" font-size="11" font-weight="800" text-anchor="middle">4. DIALOGUE &amp; QUESTIONS (ISTIFHAM)</text>
    <text x="14" y="50" fill="#f8fafc" font-family="system-ui, sans-serif" font-size="10.5" font-weight="600">• Rhetorical Inquiries:</text>
    <text x="22" y="66" fill="#94a3b8" font-family="system-ui, sans-serif" font-size="10">Thought-provoking questions stimulating critical self-reflection.</text>
    <text x="14" y="88" fill="#f8fafc" font-family="system-ui, sans-serif" font-size="10.5" font-weight="600">• Prophetic Conversations:</text>
    <text x="22" y="104" fill="#94a3b8" font-family="system-ui, sans-serif" font-size="10">Exchanges between messengers and deniers addressing human doubts.</text>
  </g>

  <!-- Bottom Banner -->
  <g transform="translate(45, 410)">
    <rect width="790" height="42" rx="8" fill="#1e293b" stroke="#334155" stroke-width="1"/>
    <text x="395" y="26" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="11" font-weight="600" text-anchor="middle">
      <tspan fill="#34d399" font-weight="700">Holistic Impact: </tspan>The Qur'an combines reason, conscience, and emotion so guidance transforms the whole person.
    </text>
  </g>
</svg>"""


def get_svg_lesson_5():
    return """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 880 480" width="100%" height="100%">
  <defs>
    <linearGradient id="bg5" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#0f172a"/>
      <stop offset="50%" stop-color="#1e293b"/>
      <stop offset="100%" stop-color="#0f172a"/>
    </linearGradient>
    <filter id="glow5" x="-10%" y="-10%" width="120%" height="120%">
      <feDropShadow dx="0" dy="4" stdDeviation="6" flood-color="#000000" flood-opacity="0.4"/>
    </filter>
  </defs>

  <rect width="880" height="480" fill="url(#bg5)" rx="14"/>
  <rect x="15" y="15" width="850" height="450" fill="none" stroke="#334155" stroke-width="1.5" stroke-dasharray="6 4" rx="10"/>

  <text x="440" y="44" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="17" font-weight="800" text-anchor="middle" letter-spacing="1">4-TIER SAFE INTERPRETATION PROTOCOL</text>
  <text x="440" y="66" fill="#94a3b8" font-family="system-ui, sans-serif" font-size="12" text-anchor="middle">Methodological Funnel for Extracting Authentic Qur'anic Meaning Without Personal Bias</text>

  <!-- Level 1: Widest Top (Direct Translation & Arabic Wording) -->
  <g transform="translate(60, 85)" filter="url(#glow5)">
    <rect width="760" height="68" rx="10" fill="#1e293b" stroke="#38bdf8" stroke-width="1.5"/>
    <rect width="180" height="24" rx="6" fill="#0284c7" x="12" y="8"/>
    <text x="102" y="24" fill="#ffffff" font-family="system-ui, sans-serif" font-size="11" font-weight="800" text-anchor="middle">1. ARABIC TEXT &amp; LEXICON</text>
    <text x="210" y="25" fill="#e0f2fe" font-family="system-ui, sans-serif" font-size="11" font-weight="600">Analyze root letters, grammatical syntax (I‘rab), and primary lexical meanings.</text>
    <text x="20" y="52" fill="#94a3b8" font-family="system-ui, sans-serif" font-size="10.5">Rule: Read accurate translations alongside the Arabic text; do not rely on isolated English synonyms.</text>
  </g>

  <!-- Arrow 1 -->
  <polygon points="440,157 435,165 445,165" fill="#38bdf8"/>

  <!-- Level 2: Upper Middle (Historical Context / Asbab al-Nuzul) -->
  <g transform="translate(110, 168)" filter="url(#glow5)">
    <rect width="660" height="68" rx="10" fill="#1e293b" stroke="#10b981" stroke-width="1.5"/>
    <rect width="210" height="24" rx="6" fill="#059669" x="12" y="8"/>
    <text x="117" y="24" fill="#ffffff" font-family="system-ui, sans-serif" font-size="11" font-weight="800" text-anchor="middle">2. CONTEXT (ASBAB AL-NUZUL)</text>
    <text x="240" y="25" fill="#d1fae5" font-family="system-ui, sans-serif" font-size="11" font-weight="600">Determine why, when, and where the verse was revealed.</text>
    <text x="20" y="52" fill="#94a3b8" font-family="system-ui, sans-serif" font-size="10.5">Rule: Distinguish universal moral commands from specific historical events in Mecca or Medina.</text>
  </g>

  <!-- Arrow 2 -->
  <polygon points="440,240 435,248 445,248" fill="#10b981"/>

  <!-- Level 3: Lower Middle (Prophetic Sunnah & Tafsir) -->
  <g transform="translate(160, 251)" filter="url(#glow5)">
    <rect width="560" height="68" rx="10" fill="#1e293b" stroke="#f59e0b" stroke-width="1.5"/>
    <rect width="220" height="24" rx="6" fill="#d97706" x="12" y="8"/>
    <text x="122" y="24" fill="#ffffff" font-family="system-ui, sans-serif" font-size="11" font-weight="800" text-anchor="middle">3. PROPHETIC SUNNAH &amp; TAFSIR</text>
    <text x="250" y="25" fill="#fef3c7" font-family="system-ui, sans-serif" font-size="11" font-weight="600">Consult how the Prophet (PBUH) explained the text.</text>
    <text x="20" y="52" fill="#94a3b8" font-family="system-ui, sans-serif" font-size="10.5">Rule: Check classical Tafsir books (Ibn Kathir, Al-Tabari) for companion consensus.</text>
  </g>

  <!-- Arrow 3 -->
  <polygon points="440,323 435,331 445,331" fill="#f59e0b"/>

  <!-- Level 4: Narrow Bottom (Personal Reflection & Application) -->
  <g transform="translate(210, 334)" filter="url(#glow5)">
    <rect width="460" height="68" rx="10" fill="#1e293b" stroke="#a855f7" stroke-width="1.5"/>
    <rect width="230" height="24" rx="6" fill="#7c3aed" x="12" y="8"/>
    <text x="127" y="24" fill="#ffffff" font-family="system-ui, sans-serif" font-size="11" font-weight="800" text-anchor="middle">4. PERSONAL REFLECTION &amp; ACTION</text>
    <text x="20" y="52" fill="#f3e8ff" font-family="system-ui, sans-serif" font-size="10.5">Apply universal virtues to daily life, strictly bounded by the 3 upper tiers.</text>
  </g>

  <!-- Bottom Banner -->
  <g transform="translate(50, 415)">
    <rect width="780" height="42" rx="8" fill="#1e293b" stroke="#475569" stroke-width="1"/>
    <text x="390" y="26" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="11" font-weight="600" text-anchor="middle">
      <tspan fill="#f59e0b" font-weight="700">Safety Rule: </tspan>Never bypass Text, Context, and Tafsir to invent personal religious interpretations.
    </text>
  </g>
</svg>"""


def get_svg_lesson_6():
    return """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 880 480" width="100%" height="100%">
  <defs>
    <linearGradient id="bg6" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#0f172a"/>
      <stop offset="50%" stop-color="#1e293b"/>
      <stop offset="100%" stop-color="#0f172a"/>
    </linearGradient>
    <filter id="glow6" x="-10%" y="-10%" width="120%" height="120%">
      <feDropShadow dx="0" dy="4" stdDeviation="6" flood-color="#000000" flood-opacity="0.4"/>
    </filter>
  </defs>

  <rect width="880" height="480" fill="url(#bg6)" rx="14"/>
  <rect x="15" y="15" width="850" height="450" fill="none" stroke="#334155" stroke-width="1.5" stroke-dasharray="6 4" rx="10"/>

  <text x="440" y="44" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="17" font-weight="800" text-anchor="middle" letter-spacing="1">ACADEMIC RESEARCH &amp; SOURCE QUALITY CHECKLIST</text>
  <text x="440" y="66" fill="#94a3b8" font-family="system-ui, sans-serif" font-size="12" text-anchor="middle">Evaluation Rubric for Qur'anic Studies &amp; Digital Information Literacy (Surah Al-Hujurat 49:6)</text>

  <!-- Criteria 1: Author Credentials -->
  <g transform="translate(50, 85)" filter="url(#glow6)">
    <rect width="375" height="145" rx="10" fill="#1e293b" stroke="#38bdf8" stroke-width="1.5"/>
    <rect width="375" height="28" rx="10" fill="#0284c7"/>
    <rect x="0" y="20" width="375" height="8" fill="#0284c7"/>
    <text x="187" y="19" fill="#ffffff" font-family="system-ui, sans-serif" font-size="11.5" font-weight="800" text-anchor="middle">1. AUTHOR CREDENTIALS &amp; ISNAD</text>
    <text x="16" y="52" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="11" font-weight="700">✓ Verified Expertise:</text>
    <text x="16" y="68" fill="#94a3b8" font-family="system-ui, sans-serif" font-size="10.5">Author has formal recognized training in Islamic sciences.</text>
    <text x="16" y="92" fill="#f87171" font-family="system-ui, sans-serif" font-size="11" font-weight="700">✗ Red Flag:</text>
    <text x="16" y="108" fill="#94a3b8" font-family="system-ui, sans-serif" font-size="10.5">Anonymous social media accounts or unverified blogs.</text>
    <text x="16" y="128" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="9.5" font-weight="600">Verification Question: Who wrote this and what are their qualifications?</text>
  </g>

  <!-- Criteria 2: Scripture Citation -->
  <g transform="translate(455, 85)" filter="url(#glow6)">
    <rect width="375" height="145" rx="10" fill="#1e293b" stroke="#10b981" stroke-width="1.5"/>
    <rect width="375" height="28" rx="10" fill="#059669"/>
    <rect x="0" y="20" width="375" height="8" fill="#059669"/>
    <text x="187" y="19" fill="#ffffff" font-family="system-ui, sans-serif" font-size="11.5" font-weight="800" text-anchor="middle">2. PRECISE SCRIPTURE CITATIONS</text>
    <text x="16" y="52" fill="#34d399" font-family="system-ui, sans-serif" font-size="11" font-weight="700">✓ Traceable References:</text>
    <text x="16" y="68" fill="#94a3b8" font-family="system-ui, sans-serif" font-size="10.5">Surah name and verse number explicitly cited (e.g. Q 49:6).</text>
    <text x="16" y="92" fill="#f87171" font-family="system-ui, sans-serif" font-size="11" font-weight="700">✗ Red Flag:</text>
    <text x="16" y="108" fill="#94a3b8" font-family="system-ui, sans-serif" font-size="10.5">Vague phrases like "the Qur'an says somewhere" without proof.</text>
    <text x="16" y="128" fill="#34d399" font-family="system-ui, sans-serif" font-size="9.5" font-weight="600">Verification Question: Can the audience locate this verse directly?</text>
  </g>

  <!-- Criteria 3: Institutional Credibility -->
  <g transform="translate(50, 245)" filter="url(#glow6)">
    <rect width="375" height="145" rx="10" fill="#1e293b" stroke="#f59e0b" stroke-width="1.5"/>
    <rect width="375" height="28" rx="10" fill="#d97706"/>
    <rect x="0" y="20" width="375" height="8" fill="#d97706"/>
    <text x="187" y="19" fill="#ffffff" font-family="system-ui, sans-serif" font-size="11.5" font-weight="800" text-anchor="middle">3. INSTITUTIONAL CREDIBILITY</text>
    <text x="16" y="52" fill="#fbbf24" font-family="system-ui, sans-serif" font-size="11" font-weight="700">✓ Academic Review:</text>
    <text x="16" y="68" fill="#94a3b8" font-family="system-ui, sans-serif" font-size="10.5">Published by recognized universities, curriculum boards, or publishers.</text>
    <text x="16" y="92" fill="#f87171" font-family="system-ui, sans-serif" font-size="11" font-weight="700">✗ Red Flag:</text>
    <text x="16" y="108" fill="#94a3b8" font-family="system-ui, sans-serif" font-size="10.5">Commercial clickbait sites prioritizing ad revenue over truth.</text>
    <text x="16" y="128" fill="#fbbf24" font-family="system-ui, sans-serif" font-size="9.5" font-weight="600">Verification Question: Is this reviewed by certified educators?</text>
  </g>

  <!-- Criteria 4: Objective Academic Tone -->
  <g transform="translate(455, 245)" filter="url(#glow6)">
    <rect width="375" height="145" rx="10" fill="#1e293b" stroke="#a855f7" stroke-width="1.5"/>
    <rect width="375" height="28" rx="10" fill="#7c3aed"/>
    <rect x="0" y="20" width="375" height="8" fill="#7c3aed"/>
    <text x="187" y="19" fill="#ffffff" font-family="system-ui, sans-serif" font-size="11.5" font-weight="800" text-anchor="middle">4. OBJECTIVE &amp; RESPECTFUL TONE</text>
    <text x="16" y="52" fill="#c084fc" font-family="system-ui, sans-serif" font-size="11" font-weight="700">✓ Dignified Reasoning:</text>
    <text x="16" y="68" fill="#94a3b8" font-family="system-ui, sans-serif" font-size="10.5">Presents established scholarly consensus with intellectual honesty.</text>
    <text x="16" y="92" fill="#f87171" font-family="system-ui, sans-serif" font-size="11" font-weight="700">✗ Red Flag:</text>
    <text x="16" y="108" fill="#94a3b8" font-family="system-ui, sans-serif" font-size="10.5">Sensationalist claims, conspiracy theories, or emotional manipulation.</text>
    <text x="16" y="128" fill="#c084fc" font-family="system-ui, sans-serif" font-size="9.5" font-weight="600">Verification Question: Is the tone educational or sensationalist?</text>
  </g>

  <!-- Bottom Banner -->
  <g transform="translate(50, 405)">
    <rect width="780" height="48" rx="8" fill="#1e293b" stroke="#334155" stroke-width="1"/>
    <text x="390" y="28" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="11" font-weight="600" text-anchor="middle">
      <tspan fill="#38bdf8" font-weight="700">Islamic Ethos: </tspan>Academic integrity is a moral duty rooted in Sidq (Truthfulness) and Amanah (Trustworthiness).
    </text>
  </g>
</svg>"""


def get_svg_lesson_7():
    return """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 880 480" width="100%" height="100%">
  <defs>
    <linearGradient id="bg7" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#0f172a"/>
      <stop offset="50%" stop-color="#1e293b"/>
      <stop offset="100%" stop-color="#0f172a"/>
    </linearGradient>
    <linearGradient id="redGrad7" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#dc2626"/>
      <stop offset="100%" stop-color="#991b1b"/>
    </linearGradient>
    <linearGradient id="greenGrad7" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#10b981"/>
      <stop offset="100%" stop-color="#047857"/>
    </linearGradient>
    <filter id="glow7" x="-10%" y="-10%" width="120%" height="120%">
      <feDropShadow dx="0" dy="4" stdDeviation="6" flood-color="#000000" flood-opacity="0.4"/>
    </filter>
  </defs>

  <rect width="880" height="480" fill="url(#bg7)" rx="14"/>
  <rect x="15" y="15" width="850" height="450" fill="none" stroke="#334155" stroke-width="1.5" stroke-dasharray="6 4" rx="10"/>

  <text x="440" y="44" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="17" font-weight="800" text-anchor="middle" letter-spacing="1">QUR'ANIC ENGAGEMENT: SHALLOW VS. GROUNDED</text>
  <text x="440" y="66" fill="#94a3b8" font-family="system-ui, sans-serif" font-size="12" text-anchor="middle">Moving from Superficial Interaction to Living, Transformative Divine Guidance (Hidayah)</text>

  <!-- Left Card: Shallow Interaction -->
  <g transform="translate(45, 90)" filter="url(#glow7)">
    <rect width="370" height="305" rx="12" fill="#1e293b" stroke="#ef4444" stroke-width="1.5"/>
    <rect width="370" height="42" rx="12" fill="url(#redGrad7)"/>
    <rect x="0" y="30" width="370" height="12" fill="url(#redGrad7)"/>
    <text x="185" y="27" fill="#ffffff" font-family="system-ui, sans-serif" font-size="14" font-weight="800" text-anchor="middle">SHALLOW INTERACTION</text>
    
    <rect x="25" y="55" width="125" height="20" rx="4" fill="#450a0a"/>
    <text x="87" y="69" fill="#fca5a5" font-family="system-ui, sans-serif" font-size="10" font-weight="700" text-anchor="middle">DEFICIT MODEL</text>

    <circle cx="32" cy="98" r="4" fill="#ef4444"/>
    <text x="44" y="96" fill="#f8fafc" font-family="system-ui, sans-serif" font-size="11.5" font-weight="700">Recitation Style:</text>
    <text x="44" y="112" fill="#94a3b8" font-family="system-ui, sans-serif" font-size="11">Mechanical chanting without comprehension or reflection.</text>

    <circle cx="32" cy="140" r="4" fill="#ef4444"/>
    <text x="44" y="138" fill="#f8fafc" font-family="system-ui, sans-serif" font-size="11.5" font-weight="700">Contextual Grounding:</text>
    <text x="44" y="154" fill="#94a3b8" font-family="system-ui, sans-serif" font-size="11">Ignores Asbab al-Nuzul; quotes verses out of context.</text>

    <circle cx="32" cy="182" r="4" fill="#ef4444"/>
    <text x="44" y="180" fill="#f8fafc" font-family="system-ui, sans-serif" font-size="11.5" font-weight="700">Everyday Attitude:</text>
    <text x="44" y="196" fill="#94a3b8" font-family="system-ui, sans-serif" font-size="11">Treats the Book as a shelf decoration or lucky charm.</text>

    <circle cx="32" cy="224" r="4" fill="#ef4444"/>
    <text x="44" y="222" fill="#f8fafc" font-family="system-ui, sans-serif" font-size="11.5" font-weight="700">Practical Outcome:</text>
    <text x="44" y="238" fill="#94a3b8" font-family="system-ui, sans-serif" font-size="11">Disconnect between recited words and moral conduct.</text>

    <rect x="20" y="258" width="330" height="34" rx="6" fill="#0f172a" stroke="#7f1d1d" stroke-width="1"/>
    <text x="185" y="280" fill="#fca5a5" font-family="system-ui, sans-serif" font-size="11" font-weight="600" text-anchor="middle">Result: Vulnerable to personal bias and misinterpretation</text>
  </g>

  <!-- Center Transformation Bridge -->
  <g transform="translate(440, 242)">
    <circle cx="0" cy="0" r="26" fill="#0f172a" stroke="#38bdf8" stroke-width="2"/>
    <text x="0" y="-4" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="10" font-weight="800" text-anchor="middle">ULUM</text>
    <text x="0" y="8" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="8.5" font-weight="700" text-anchor="middle">AL-QUR'AN</text>
    <text x="0" y="19" fill="#94a3b8" font-family="system-ui, sans-serif" font-size="7.5" text-anchor="middle">Bridge</text>
  </g>

  <!-- Right Card: Grounded Understanding -->
  <g transform="translate(465, 90)" filter="url(#glow7)">
    <rect width="370" height="305" rx="12" fill="#1e293b" stroke="#10b981" stroke-width="1.5"/>
    <rect width="370" height="42" rx="12" fill="url(#greenGrad7)"/>
    <rect x="0" y="30" width="370" height="12" fill="url(#greenGrad7)"/>
    <text x="185" y="27" fill="#ffffff" font-family="system-ui, sans-serif" font-size="14" font-weight="800" text-anchor="middle">GROUNDED UNDERSTANDING</text>

    <rect x="25" y="55" width="150" height="20" rx="4" fill="#064e3b"/>
    <text x="100" y="69" fill="#a7f3d0" font-family="system-ui, sans-serif" font-size="10" font-weight="700" text-anchor="middle">TRANSFORMATIVE GUIDANCE</text>

    <circle cx="32" cy="98" r="4" fill="#34d399"/>
    <text x="44" y="96" fill="#f8fafc" font-family="system-ui, sans-serif" font-size="11.5" font-weight="700">Recitation Style:</text>
    <text x="44" y="112" fill="#94a3b8" font-family="system-ui, sans-serif" font-size="11">Reverent recitation paired with meaning and Tafsir study.</text>

    <circle cx="32" cy="140" r="4" fill="#34d399"/>
    <text x="44" y="138" fill="#f8fafc" font-family="system-ui, sans-serif" font-size="11.5" font-weight="700">Contextual Grounding:</text>
    <text x="44" y="154" fill="#94a3b8" font-family="system-ui, sans-serif" font-size="11">Anchored in revelation history &amp; prophetic explanations.</text>

    <circle cx="32" cy="182" r="4" fill="#34d399"/>
    <text x="44" y="180" fill="#f8fafc" font-family="system-ui, sans-serif" font-size="11.5" font-weight="700">Everyday Attitude:</text>
    <text x="44" y="196" fill="#94a3b8" font-family="system-ui, sans-serif" font-size="11">Honors the Qur'an as the living moral compass (Al-Furqan).</text>

    <circle cx="32" cy="224" r="4" fill="#34d399"/>
    <text x="44" y="222" fill="#f8fafc" font-family="system-ui, sans-serif" font-size="11.5" font-weight="700">Practical Outcome:</text>
    <text x="44" y="238" fill="#94a3b8" font-family="system-ui, sans-serif" font-size="11">Actively translates values into honesty, patience &amp; justice.</text>

    <rect x="20" y="258" width="330" height="34" rx="6" fill="#0f172a" stroke="#065f46" stroke-width="1"/>
    <text x="185" y="280" fill="#a7f3d0" font-family="system-ui, sans-serif" font-size="11" font-weight="600" text-anchor="middle">Result: Strengthens Iman, moral clarity, and virtuous living</text>
  </g>

  <!-- Bottom Core Insight Banner -->
  <g transform="translate(45, 410)">
    <rect width="790" height="42" rx="8" fill="#1e293b" stroke="#475569" stroke-width="1"/>
    <text x="395" y="26" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="11" font-weight="600" text-anchor="middle">
      <tspan fill="#34d399" font-weight="700">Surah Al-Baqarah 2:2: </tspan>"This is the Book about which there is no doubt, a guidance for those conscious of Allah."
    </text>
  </g>
</svg>"""


# ─────────────────────────────────────────────────────────────────────────────
# LESSON DATA SPECIFICATIONS (7 LESSONS, 7 CARDS EACH)
# ─────────────────────────────────────────────────────────────────────────────

LESSONS_DATA = [
    # ── LESSON 1.1.1 ─────────────────────────────────────────────────────────
    {
        "unit_order": 1,
        "unit_name": "What Makes a Miracle?",
        "lesson_title": "What Makes a Miracle?",
        "unit_description": "Distinguish between ordinary natural patterns, human technological achievements, and genuine divine miracles (Mu‘jizah) performed by Allah's prophets.",
        "image": {
            "title": "The Holy Kaaba in Mecca",
            "caption": "The Kaaba in Mecca, the focal spiritual sanctuary of Islam and the historic setting for the revelation of divine signs to Prophet Muhammad (PBUH).",
            "url": "https://upload.wikimedia.org/wikipedia/commons/7/79/The_Kaaba_during_Hajj.jpg",
            "author": "Wikimedia Commons",
            "licensing": "CC-BY-SA",
            "source": "Wikimedia Commons"
        },
        "svg_fn": get_svg_lesson_1,
        "card1": {
            "inquiry_question": "What is a miracle, and how do we distinguish an extraordinary claim from genuine divine evidence?",
            "connection_hook": "Think of a master builder who designs a skyscraper that is completely earthquake-proof using an elusive technique. No other architect in the world can copy it or figure out how it was built, even if they try for years. This extraordinary feat makes everyone realize the builder has knowledge far beyond any ordinary human. In a similar way, a miracle is an extraordinary event that cannot be explained by natural or human laws. It serves as clear evidence of divine authority.",
            "goals": [
                "Define the Islamic theological concept of a miracle (Mu‘jizah).",
                "Differentiate between ordinary natural signs (Ayat Kawniyyah) and extraordinary prophetic miracles.",
                "Identify the three strict conditions that validate a genuine divine miracle."
            ]
        },
        "card2": {
            "concept_title": "The Anatomy of a Mu‘jizah: Ordinary vs. Extraordinary Signs",
            "concept_markdown": "In Islamic theology, signs from Allah (S.W.T.) fall into two distinct categories:\n\n- **Ordinary Signs (*Ayat Kawniyyah*):** The constant, reliable patterns of the cosmos—such as the rotation of celestial bodies, the water cycle, and biological growth. These signs demonstrate Allah's continuous sustaining power and wisdom.\n- **Extraordinary Signs / Miracles (*Mu‘jizah*):** Supernatural occurrences granted exclusively to a prophet, by the permission of Allah, which temporarily break standard natural laws (*Kharq al-‘Adah*). Their purpose is to authenticate the prophet's divine mission and remove all doubt from the hearts of sincere seekers.",
            "callout_title": "Scripture Panel: Surah Ali 'Imran (3:190)",
            "callout_text": "> \"Indeed, in the creation of the heavens and the earth and the alternation of the night and the day are signs for those of understanding.\" [Surah Ali 'Imran, 3:190]\n\n*Exegetical Note: While regular cosmic cycles are constant signs of Allah's creative power, a specific miracle (mu‘jizah) is a unique, unrepeatable sign given directly to a prophet to authenticate his status before skeptics.*"
        },
        "card3": {
            "concept_title": "Clarifying the Concept: The Three Pillars of a True Miracle",
            "concept_markdown": "For an event to qualify as a true prophetic miracle (*Mu‘jizah*), Islamic scholars establish that it must satisfy three rigorous conditions:\n\n1. **Suspension of Natural Laws (*Kharq al-‘Adah*):** It must defy the normal physical or biological causality established in nature (e.g., fire turning cool and safe for Prophet Ibrahim, or water springing forth from fingers).\n2. **Accompanied by a Challenge (*Tahaddi*):** It must be manifested by a prophet of Allah in response to deniers, challenging them to produce anything comparable.\n3. **Impossible to Duplicate (*I‘jaz*):** It must be fundamentally inimitable—incapable of being replicated, matched, or surpassed by contemporary magicians, scientists, or human collective effort.",
            "diagram_title": "Human Achievement vs Divine Miracle (Comparison Matrix)",
            "diagram_caption": "Visual matrix distinguishing progressive human technological marvels from instantaneous supernatural divine miracles.",
            "table_headers": ["Evaluation Criteria", "Human Achievement (e.g., Space Rockets, AI)", "Divine Miracle (Mu‘jizah)"],
            "table_rows": [
                ["Source & Power", "Human intellect, collective engineering & empirical research", "Direct divine command and omnipotent will of Allah (S.W.T.)"],
                ["Natural Laws", "Operates strictly within natural physical & mathematical laws", "Supernaturally suspends standard natural laws (Kharq al-‘Adah)"],
                ["Reproducibility", "Repeatable and improvable by any trained human team with resources", "Impossible to replicate or copy by any human being or jinn"],
                ["Primary Purpose", "Technological utility, commercial productivity & exploration", "Authenticates a prophet's claim and establishes religious truth"],
                ["Temporal Evolution", "Iterative; improves over decades and becomes obsolete", "Instantaneous; possesses timeless theological authority"]
            ]
        },
        "card4": {
            "scenario_title": "Student Case Study: The Drone Debate in Science Class",
            "scenario": "During a science class, Yusuf is amazed by how a high-tech delivery drone maneuvers autonomously across a bustling city. He enthusiastically tells his classmate, \"This drone is a complete miracle! No one could have imagined this a hundred years ago.\" His classmate Amina thoughtfully replies, \"It is certainly impressive technology, Yusuf, but in Islamic education, it is not a mu‘jizah. A drone operates strictly within natural aerodynamics and electrical engineering; anyone with the right training can build or copy it. A true miracle, like the staff of Prophet Musa turning into a living serpent, defies natural laws completely and can never be duplicated by human science or technology.\"",
            "analysis": "Amina correctly applied Islamic theological criteria. Calling human inventions \"miracles\" in casual conversation is common, but academically, learners must maintain clear distinction: technology relies on natural laws created by Allah, whereas a mu‘jizah is a direct supernatural intervention by Allah."
        },
        "card5": {
            "application_title": "Real-World Application: The Information Verification Protocol",
            "application_text": "In modern digital media, students frequently encounter viral posts claiming sensational \"miracles\" (e.g., strange cloud formations, manipulated photos, or unverified claims). Practice intellectual responsibility using this verification protocol:\n\n1. **Check the Source:** Does this claim have verified scientific backing or authentic Islamic scholarship?\n2. **Look for Natural Explanations:** Can this phenomenon be explained by ordinary weather patterns, geology, or digital editing?\n3. **Preserve Theological Dignity:** Faith in Islam is built on verified truth and the authentic Qur'an, not on rumors or unproven viral posts.",
            "reflection_title": "Pause & Reflect: The Wisdom Behind Prophetic Miracles",
            "reflection_prompt": "Why do you think Allah (S.W.T.) granted physical miracles tailored to the specific peaks of each prophet's society (e.g., healing the sick in the era of advanced Greek/Roman medicine, or turning a staff into a snake in the era of Pharaoh's magicians)? How did this protect the integrity of the divine message?",
            "misconception_title": "Common Misconception: Conflating Human Ingenuity with Miracles",
            "misconception": "Any highly advanced human invention—like artificial intelligence, smartphones, or organ transplants—is a religious miracle.",
            "reality": "Human inventions operate entirely within natural laws and materials already created by Allah. They are replicable through education and research. A divine miracle (mu‘jizah) suspends physical laws by Allah's direct decree and is granted solely to His prophets."
        },
        "card6": {
            "question": "Which of the following is a key condition that distinguishes a divine miracle (mu‘jizah) from an extraordinary human achievement?",
            "options": [
                "A) A miracle requires decades of iterative scientific research and physical materials to develop.",
                "B) A miracle can be readily duplicated by any human who studies its technique carefully.",
                "C) A miracle goes against regular natural laws and cannot be replicated by human effort.",
                "D) A miracle is solely an inspirational metaphor and never physically occurred in reality."
            ],
            "answer": "C",
            "correct_answer": "C",
            "explanation": "A divine miracle (mu‘jizah) is defined by its supernatural nature (Kharq al-‘Adah), its occurrence by Allah's direct permission through a prophet, and its absolute impossibility of replication by human effort or natural science."
        },
        "card7": {
            "summary_title": "Key Points & Unit Vocabulary",
            "key_points": [
                "A miracle (mu‘jizah) is an extraordinary, supernatural event given by Allah to a prophet to authenticate his truthfulness.",
                "Miracles cannot be replicated by human science, engineering, or illusion, because they transcend natural laws (Kharq al-‘Adah).",
                "Muslims differentiate between regular cosmic signs (Ayat Kawniyyah) that reflect Allah's ongoing providence and prophetic miracles that authenticate revelation."
            ],
            "vocabulary": [
                {"term": "Mu‘jizah", "definition": "An extraordinary, unrepeatable miracle granted by Allah to validate a prophet's claim."},
                {"term": "Ayat Kawniyyah", "definition": "The regular, observable signs of Allah functioning throughout the natural universe."},
                {"term": "Kharq al-‘Adah", "definition": "The temporary breaking or suspension of normal physical laws by divine decree."}
            ],
            "exit_ticket_title": "Exit Ticket: The Distinguishing Line",
            "exit_ticket_prompt": "In your notebook, write down one clear difference between a highly advanced technological breakthrough (such as a Mars rover) and a prophet's miracle (such as the staff of Prophet Musa)."
        }
    },

    # ── LESSON 1.1.2 ─────────────────────────────────────────────────────────
    {
        "unit_order": 2,
        "unit_name": "The Miraculous Nature of the Qur’an",
        "lesson_title": "The Miraculous Nature of the Qur’an",
        "unit_description": "Explore the enduring intellectual, literary, and spiritual inimitability (I‘jaz al-Qur'an) of the Holy Qur'an, its divine challenge to humanity, and its letter-for-letter preservation.",
        "image": {
            "title": "The Birmingham Qur'an Manuscript Leaf",
            "caption": "One of the earliest surviving Qur'anic manuscript leaves in the world (radiocarbon dated to 568–645 CE), written in early Hijazi script, providing physical evidence of the Qur'an's exact preservation.",
            "url": "https://upload.wikimedia.org/wikipedia/commons/5/50/Birmingham_Quran_manuscript.jpg",
            "author": "Cadbury Research Library / University of Birmingham",
            "licensing": "Public Domain",
            "source": "Wikimedia Commons"
        },
        "svg_fn": get_svg_lesson_2,
        "card1": {
            "inquiry_question": "Why is the Qur’an considered a miracle, and how does its preservation strengthen a Muslim's faith (Iman)?",
            "connection_hook": "Imagine a book revealed over 1,400 years ago through an unlettered man in the Arabian desert. This book contains comprehensive legal codes, profound spiritual guidance, precise historical records of past nations, and a language so transcendent that the greatest Arabic poets could not match even a single chapter. For Muslims, the Qur'an is not merely a book recounting past miracles; the Qur'an itself is the living, eternal miracle.",
            "goals": [
                "Explain the concept of I‘jaz al-Qur'an (the miraculous inimitability of the Qur'an).",
                "Contrast temporary physical miracles of earlier prophets with the enduring intellectual miracle of the Qur'an.",
                "Describe the divine challenge (Tahaddi) issued by the Qur'an and understand Allah's guarantee of its preservation."
            ]
        },
        "card2": {
            "concept_title": "The Living Miracle: An Enduring Divine Testament",
            "concept_markdown": "In Islamic scholarship, the Qur'an holds a unique theological status among all divine scriptures:\n\n- **Enduring Miracle:** Unlike physical miracles (such as the parting of the Red Sea or raising the dead) which could only be witnessed by people living in that specific time and place, the Qur'an is an intellectual and spiritual miracle accessible to all generations until the Day of Judgment.\n- **Divine Guarantee of Preservation:** Allah has promised to safeguard the Qur'an from any alteration, deletion, or addition, preserving its text letter-for-letter across fourteen centuries through oral memorization and written codices.",
            "callout_title": "Scripture Panel: Surah Al-Hijr (15:9) & Surah Al-Baqarah (2:23)",
            "callout_text": "> \"Indeed, it is We who sent down the Qur'an and indeed, We will be its guardian.\" [Surah Al-Hijr, 15:9]\n\n> \"And if you are in doubt about what We have sent down upon Our Servant, then produce a surah the like thereof and call upon your witnesses other than Allah, if you should be truthful.\" [Surah Al-Baqarah, 2:23]\n\n*Exegetical Note: The challenge (Tahaddi) in Surah Al-Baqarah was addressed to masters of classical Arabic poetry and rhetoric, yet remained completely unmet.*"
        },
        "card3": {
            "concept_title": "Clarifying the Concept: The Multi-Faceted Inimitability (I‘jaz)",
            "concept_markdown": "The inimitability of the Qur'an (*I‘jaz al-Qur'an*) is manifested through several integrated dimensions:\n\n1. **Literary and Rhetorical Uniqueness:** The Qur'an possesses an unprecedented literary form that is neither rhymed poetry (*Shi‘r*) nor conventional prose (*Nathr*), featuring impeccable rhythm, structural balance, and profound emotional impact.\n2. **Unbroken Preservation:** Memorized verbatim by millions of believers (*Huffaz*) in every generation, ensuring that copies read in Nairobi, Cairo, Jakarta, and London are identical to the revelation received by Prophet Muhammad (PBUH).\n3. **Universal Guidance:** Offers a holistic legal, moral, and spiritual framework that addresses individual character, family life, economic justice, and global human dignity.",
            "diagram_title": "The Multi-Faceted Inimitability (I‘jaz al-Qur'an)",
            "diagram_caption": "Circular infographic highlighting the four foundational pillars of the Qur'an's enduring miraculous nature.",
            "table_headers": ["Feature", "Miracles of Past Prophets", "The Miracle of the Holy Qur'an"],
            "table_rows": [
                ["Nature of Phenomenon", "Physical, tangible, sensory interventions in the physical environment", "Intellectual, linguistic, spiritual, and moral revelation"],
                ["Audience & Witness", "Limited exclusively to those physically present at that historical moment", "Universal; open and accessible to all humanity in every era"],
                ["Duration of Sign", "Temporary; ended immediately after the prophet departed this world", "Enduring; continuously recited, heard, and verified across all centuries"],
                ["Method of Verification", "Relies upon historical testimony and accounts of eyewitnesses", "Directly verified today by studying its text, structure, and preservation"]
            ]
        },
        "card4": {
            "scenario_title": "Student Case Study: The Living Sign vs. Historical Signs",
            "scenario": "In a study circle, Halima asks her IRE teacher, \"Why do we say the Qur'an is a miracle today if we cannot see seas parting or sick people healed with a touch?\" Mr. Bilal explains, \"The physical miracles of past prophets were beautiful signs, Halima, but they concluded when those prophets left this world. The Qur'an, however, is a miracle you hold in your hands right now. If you examine its flawless Arabic structure, its profound psychological impact, and the historical reality that not a single letter has altered since it was revealed to Prophet Muhammad (PBUH), you will realize it is a living miracle speaking directly to our intellects and hearts in every age.\"",
            "analysis": "Mr. Bilal clarified that physical miracles persuade the senses of eyewitnesses, whereas intellectual miracles persuade human reason across all generations."
        },
        "card5": {
            "application_title": "Real-World Application: Participating in Living Preservation",
            "application_text": "Whenever you recite, memorize, or teach a verse of the Qur'an with correct pronunciation (*Tajweed*), you are an active participant in Allah's promise of divine preservation (*Hifdh*). You can apply this lesson by:\n\n- Committing to daily recitation with deliberate reflection upon its meanings (*Tadabbur*).\n- Ensuring that your conduct reflects its guidance—practicing truthfulness in school, respecting parents, and being trustworthy with peers.",
            "reflection_title": "Pause & Reflect: Trust in Divine Preservation",
            "reflection_prompt": "How does knowing that the Qur'an has been memorized letter-for-letter by millions of believers for over 1,400 years affect your confidence and trust in its guidance?",
            "misconception_title": "Common Misconception: Inventing Unverified Scientific Claims",
            "misconception": "To prove the Qur'an is a miracle today, Muslims must connect every modern scientific hypothesis to Qur'anic verses.",
            "reality": "While the Qur'an speaks truth regarding the natural cosmos, science evolves with new discoveries and revised theories. The primary, unshakeable miracle of the Qur'an is its unmatched linguistic eloquence, moral guidance, spiritual elevation, and verified preservation."
        },
        "card6": {
            "question": "Why is the Holy Qur'an referred to as an \"enduring\" miracle compared to the miracles of earlier prophets?",
            "options": [
                "A) Because it was written on specialized parchment materials that never physically decay.",
                "B) Because its miraculous nature can be read, heard, studied, and verified by people in every generation.",
                "C) Because it deals exclusively with events that will happen in the distant future.",
                "D) Because it is the only miracle that does not require any faith to understand."
            ],
            "answer": "B",
            "correct_answer": "B",
            "explanation": "Physical miracles of earlier prophets were temporary historical events witnessed by specific audiences. The Qur'an remains unchanged, open, and accessible to all generations, allowing anyone in any era to experience its intellectual, linguistic, and spiritual inimitability."
        },
        "card7": {
            "summary_title": "Key Points & Unit Vocabulary",
            "key_points": [
                "The miraculous nature of the Qur'an (I‘jaz) is multi-faceted: literary, intellectual, historical, and spiritual.",
                "Allah guaranteed the preservation of the Qur'an (Surah Al-Hijr 15:9), maintained through continuous oral and written transmission.",
                "The divine challenge (Tahaddi) to produce even a single surah like it has remained unanswered for over fourteen centuries."
            ],
            "vocabulary": [
                {"term": "I‘jaz al-Qur'an", "definition": "The miraculous, inimitable nature of the Qur'an that leaves humanity incapable of matching it."},
                {"term": "Tahaddi", "definition": "The open challenge issued in the Qur'an daring skeptics to produce a chapter comparable to it."},
                {"term": "Hafidh (pl. Huffaz)", "definition": "A Muslim who has memorized the entire Qur'an letter-for-letter."}
            ],
            "exit_ticket_title": "Exit Ticket: Two Dimensions of I‘jaz",
            "exit_ticket_prompt": "State two specific ways in which the Qur'an serves as an active, living miracle for people living in the twenty-first century."
        }
    },

    # ── LESSON 1.1.3 ─────────────────────────────────────────────────────────
    {
        "unit_order": 3,
        "unit_name": "The Language of the Qur’an",
        "lesson_title": "The Language of the Qur’an",
        "unit_description": "Understand why the Qur'an was revealed in classical Arabic, the structural richness of Arabic root systems, and the crucial distinction between the sacred text and human translations.",
        "image": {
            "title": "Illuminated Mamluk Era Arabic Qur'an Manuscript",
            "caption": "A 14th-century illuminated Arabic Qur'anic manuscript open to Surah 16, displaying classical Arabic calligraphy, vocalization diacritics, and the reverence given to the sacred Arabic text.",
            "url": "https://upload.wikimedia.org/wikipedia/commons/b/bd/Mamluk_era_Quran%2C_circa_1380%2C_open_to_sura_16.jpg",
            "author": "Chester Beatty Library",
            "licensing": "Public Domain",
            "source": "Wikimedia Commons"
        },
        "svg_fn": get_svg_lesson_3,
        "card1": {
            "inquiry_question": "Why was the Qur’an revealed in the Arabic language, and why is it essential to distinguish the original text from translations?",
            "connection_hook": "Have you ever tried to translate a deep Swahili proverb or poetic song into English? You quickly realize that some of the original rhythm, cultural resonance, and precise nuances vanish in translation. The Qur'an was revealed in classical Arabic—a language of extraordinary grammatical precision and vocabulary depth. To appreciate its divine message, we must recognize the difference between the literal revelation and human translations.",
            "goals": [
                "Explain why Arabic was chosen as the medium of the final divine revelation.",
                "Distinguish between the literal Word of Allah (Arabic Qur'an) and translations of its meanings.",
                "Apply the 3-step study protocol when researching Qur'anic verses."
            ]
        },
        "card2": {
            "concept_title": "Language of Revelation: The Divine Text vs. Human Translation",
            "concept_markdown": "In Islamic jurisprudence and theology, language is not an accidental carrier of the message; the Arabic wording itself is divine revelation:\n\n- **The Language of Revelation:** The Qur'an was revealed in the eloquent Arabic dialect of Quraysh (*Lisan 'Arabi Mubin*), a language renowned for its unparalleled richness, poetic depth, and complex morphological derivations.\n- **Text vs. Translation:** The Arabic wording of the Qur'an is the literal Word of Allah (*Kalamullah*). A translation into English, Swahili, French, or Urdu is merely a human effort to explain the meanings of those divine words. Therefore, a translation is not the Qur'an itself.",
            "callout_title": "Scripture Panel: Surah Yusuf (12:2) & Surah Ash-Shu'ara (26:192-195)",
            "callout_text": "> \"Indeed, We have sent it down as an Arabic Qur'an that you might understand.\" [Surah Yusuf, 12:2]\n\n> \"And indeed, it is of the peace-giving revelations of the Lord of the worlds... In a clear Arabic language.\" [Surah Ash-Shu'ara, 26:192-195]\n\n*Exegetical Note: Classical commentators note that clear Arabic (Lisan 'Arabi Mubin) was chosen because its expansive vocabulary and rigorous grammar allow infinite layers of meaning without ambiguity.*"
        },
        "card3": {
            "concept_title": "Clarifying the Concept: The 3-Tier Framework and Study Protocol",
            "concept_markdown": "Why can no translation be equal to the Arabic Qur'an?\n\n- **Morphological Depth:** Arabic operates on a three-letter root system (*Jidhr*). A single root can generate dozens of related verbs and nouns, carrying layered ethical and theological connotations that no single English word can capture.\n- **The Translation Limit:** Every translation reflects the translator's personal vocabulary, cultural context, and interpretive choices.\n\n**The 3-Step Study Protocol:**\n1. **Recitation:** Read or listen to the original Arabic with correct Tajweed.\n2. **Translation:** Read a reputable translation of the meaning to grasp basic comprehension.\n3. **Tafsir:** Consult scholarly exegesis to understand the context, background, and legal implications.",
            "diagram_title": "3-Tier Framework: Sacred Text vs. Translation vs. Tafsir",
            "diagram_caption": "Pedagogical hierarchy showing the relationship between the literal Arabic revelation, human translations, and scholarly commentary.",
            "table_headers": ["Dimension", "Tier 1: Original Arabic Text", "Tier 2: Literal Translation", "Tier 3: Explanatory Tafsir"],
            "table_rows": [
                ["Theological Status", "Literal, infallible Word of Allah (Kalamullah)", "Human approximation of the meanings", "Scholarly commentary and detailed exegesis"],
                ["Recitation in Prayer", "Mandatory in Salah; prayer invalid without Arabic", "Never permitted in Salah", "Forbidden inside ritual prayer recitation"],
                ["Linguistic Inimitability", "Inimitable (Mu‘jiz); completely impossible to replicate", "Imitable; reflects ordinary human prose style", "Scholarly prose; subject to academic analysis"],
                ["Multiplicity of Meaning", "Preserves layered, profound root connotations", "Constrained to the specific English/Swahili word chosen", "Elaborates on multiple scholarly perspectives and context"]
            ]
        },
        "card4": {
            "scenario_title": "Student Case Study: The Three English Translations",
            "scenario": "During an IRE study circle, Tariq notices: \"I found three different English translations of Surah Al-Hujurat, and each uses slightly different words for the same verse! Which one is the real Qur'an?\" Aisha explains with clarity: \"Tariq, only the Arabic text revealed to Prophet Muhammad (PBUH) is the real Qur'an. The English books we have are translations of the *meanings*. Because classical Arabic words have multiple layers of meaning, different translators choose different English words to convey that depth. That is why we use translations as guides, but we always anchor our understanding in the Arabic text and standard scholarly Tafsir.\"",
            "analysis": "Aisha highlighted a core principle of Ulum al-Qur'an: variation among translations reflects the richness of Arabic and human linguistic limits, not any contradiction in the original revelation."
        },
        "card5": {
            "application_title": "Real-World Application: Responsible Language Attribution",
            "application_text": "When writing school essays, preparing speeches, or discussing faith online, avoid saying: \"The Qur'an says in English...\"\n\nInstead, adopt precise academic phrasing:\n- \"The translation of the meaning of Surah Al-Baqarah, verse 261 indicates...\"\n- \"Scholars translate this Arabic verse as...\"\n\nThis academic habit demonstrates respect for divine revelation and protects you from misrepresenting human translations as literal divine phrasing.",
            "reflection_title": "Pause & Reflect: Learning Basic Qur'anic Vocabulary",
            "reflection_prompt": "How does learning even a small vocabulary of common Qur'anic Arabic words (such as Rahmah, Taqwa, Sidq, and Sabr) transform your mental presence and humility (*Khushu'*) during daily Salah?",
            "misconception_title": "Common Misconception: Viewing Translations as the Qur'an Itself",
            "misconception": "An English or Swahili translation is the Qur'an itself, and we can derive final religious rulings directly from it.",
            "reality": "A translation is a human explanatory work. It is not the Qur'an, cannot be recited in Salah, and does not carry legal finality without verifying the original Arabic grammar and classical Tafsir."
        },
        "card6": {
            "question": "Why is an English translation of the Qur'an not considered \"the Qur'an itself\" in Islamic scholarship?",
            "options": [
                "A) Because English is not an acceptable language for Muslims to use in academic studies.",
                "B) Because a translation is a human interpretation of the divine meanings and cannot capture the exact wording and depth of the Arabic revelation.",
                "C) Because the Qur'an is meant exclusively for people whose native language is Arabic.",
                "D) Because translations are automatically filled with errors and should never be read."
            ],
            "answer": "B",
            "correct_answer": "B",
            "explanation": "The Arabic wording of the Qur'an is the literal revelation from Allah. Any translation is a human effort to convey those meanings in another language; thus, it is considered an explanation of meanings, not the sacred text itself."
        },
        "card7": {
            "summary_title": "Key Points & Unit Vocabulary",
            "key_points": [
                "The Qur'an was revealed in clear, classical Arabic (Lisan 'Arabi Mubin) to ensure unmatched precision and eloquence.",
                "The original Arabic text is the literal Word of Allah, while translations are human explanations of its meanings.",
                "Rigorous Qur'anic study follows a 3-tier approach: Arabic text, reliable translations, and authoritative Tafsir."
            ],
            "vocabulary": [
                {"term": "Lisan 'Arabi Mubin", "definition": "Clear, eloquent classical Arabic chosen by Allah for the final revelation."},
                {"term": "Tarjamah", "definition": "The human translation or rendering of the meanings of the Qur'an into another language."},
                {"term": "Jidhr", "definition": "The Arabic three-letter root system from which expansive families of words and meanings derive."}
            ],
            "exit_ticket_title": "Exit Ticket: The Attribution Protocol",
            "exit_ticket_prompt": "Explain in two sentences why an IRE student should say \"the translation of the meaning of the verse\" instead of \"the Qur'an says in English.\""
        }
    },

    # ── LESSON 1.1.4 ─────────────────────────────────────────────────────────
    {
        "unit_order": 4,
        "unit_name": "Styles of the Qur’an",
        "lesson_title": "Styles of the Qur’an",
        "unit_description": "Investigate the multifaceted literary and rhetorical styles of the Qur'an (Uslub al-Qur'an)—commands, historical narratives, promises, warnings, and parables—and how they touch intellect and emotion.",
        "image": {
            "title": "Classical Arabic Calligraphy of the Bismillah",
            "caption": "Classical Arabic calligraphy showing the aesthetic beauty and artistic reverence given to the opening divine phrase of the Qur'an, reflecting the sublime nature of its literary style.",
            "url": "https://upload.wikimedia.org/wikipedia/commons/c/c6/%D8%A8%D8%B3%D9%85_%D8%A7%D9%84%D9%84%D9%87_%D8%A7%D9%84%D8%B1%D8%AD%D9%85%D9%86_%D8%A7%D9%84%D8%B1%D8%AD%D9%8A%D9%85.png",
            "author": "Wikimedia Commons",
            "licensing": "Public Domain",
            "source": "Wikimedia Commons"
        },
        "svg_fn": get_svg_lesson_4,
        "card1": {
            "inquiry_question": "What are the different communication styles used in the Qur’an, and how do they help us interpret its messages correctly?",
            "connection_hook": "When a skilled teacher wants to guide their students, they do not speak in a single, monotone voice. Sometimes they issue a clear rule (\"Wear your safety goggles\"), sometimes they share an inspiring story, sometimes they present a vivid analogy, and sometimes they ask a thought-provoking question. Similarly, the Qur'an employs diverse communication styles—commands, narratives, promises, warnings, and parables—to speak to the whole human being.",
            "goals": [
                "Identify the major literary styles of the Qur'an (Uslub al-Qur'an).",
                "Understand why Allah utilizes diverse rhetorical styles to convey divine guidance.",
                "Explain how recognizing the style of a verse prevents theological misinterpretations."
            ]
        },
        "card2": {
            "concept_title": "Uslub al-Qur'an: The Rhetorical Diversity of Revelation",
            "concept_markdown": "The rhetorical methods of the Qur'an (*Uslub al-Qur'an*) are tailored to engage human intellect, conscience, and emotions:\n\n1. **Commands (*Amr*) and Prohibitions (*Nahy*):** Unambiguous directives that establish moral and legal boundaries (e.g., \"Establish regular prayer,\" \"Do not backbite one another\").\n2. **Historical Narratives (*Qasas*):** Accounts of past prophets and nations designed to teach enduring ethical lessons rather than mere historical chronicles.\n3. **Promises (*Wa‘d*) and Warnings (*Wa‘id*):** Inspiring depictions of eternal reward for righteousness and sobering cautions against arrogance and injustice.\n4. **Rhetorical Questions (*Istifham*):** Questions designed to provoke self-scrutiny and critical reflection rather than seek new information.",
            "callout_title": "Scripture Panel: Surah Al-Kahf (18:54)",
            "callout_text": "> \"And We have certainly diversified in this Qur'an for the people from every [kind of] example; but man has ever been, most of anything, quarrelsome.\" [Surah Al-Kahf, 18:54]\n\n*Exegetical Note: Classical scholars explain that \"diversified\" (sarrafna) signifies turning the message through various literary angles—stories, parables, arguments—so every human heart finds an entryway to guidance.*"
        },
        "card3": {
            "concept_title": "Clarifying the Concept: Contextualizing Qur'anic Styles",
            "concept_markdown": "Recognizing the style of a verse is vital for correct exegesis (*Tafsir*):\n\n- **Narratives (*Qasas*):** Are not ancient folklore. When the Qur'an repeats the story of Prophet Musa confronting Pharaoh, it establishes a universal archetype: truth overcoming tyranny through patience and reliance upon Allah.\n- **Parables (*Amthal*):** Present complex metaphysical realities through familiar physical analogies, such as comparing hollow charity to dust on a smooth stone washed away by rain.\n- **Legal Directives:** Must be analyzed in context to determine whether a command implies an absolute obligation (*Fard*) or a virtuous recommendation (*Sunnah*).",
            "diagram_title": "Diverse Communication Styles of the Qur'an (Uslub)",
            "diagram_caption": "Mind map illustrating the primary literary styles of the Qur'an and their specific pedagogical functions.",
            "table_headers": ["Qur'anic Style", "Arabic Term", "Pedagogical Function", "Illustrative Example"],
            "table_rows": [
                ["Legislative Directives", "Amr & Nahy", "Establishes clear legal obligations and moral boundaries", "Surah Al-Hujurat (49:12): \"Do not spy or backbite\""],
                ["Historical Narratives", "Qasas al-Qur'an", "Extracts timeless ethical models from prophets' lives", "Surah Yusuf: Trials of betrayal, patience, and forgiveness"],
                ["Parables & Metaphors", "Amthal al-Qur'an", "Compares abstract spiritual truths to tangible physical images", "Surah Al-Baqarah (2:261): Charity like a grain sprouting 7 ears"],
                ["Dialogue & Inquiry", "Hiwar & Istifham", "Engages critical thinking and stimulates self-examination", "Surah At-Tur (52:35): \"Or were they created by nothing?\""]
            ]
        },
        "card4": {
            "scenario_title": "Student Case Study: Why Stories Instead of a Rulebook?",
            "scenario": "In class, Musa asks, \"Why does the Qur'an include so many stories about Prophet Musa and Pharaoh? Wouldn't it be more efficient if the Qur'an were just a bulleted list of rules to obey?\" Mrs. Zainab explains, \"Musa, humans are not machines that simply process rules; our actions are driven by our hearts and values. If the Qur'an were only a list of rules, it might appeal to our logic, but it would not inspire our character. By showing us how Pharaoh's arrogance brought his downfall and how Musa's patience and humility led to victory, Allah teaches us the *reasons* and *spirit* behind the laws. Stories make the teachings unforgettable.\"",
            "analysis": "Mrs. Zainab demonstrated that the narrative style (*Qasas*) embeds moral wisdom into human memory far more effectively than abstract legal codes."
        },
        "card5": {
            "application_title": "Real-World Application: Multi-Style Communication in Daily Life",
            "application_text": "You can elevate your personal communication and leadership by learning from the styles of the Qur'an. When encouraging your classmates or siblings toward positive behavior:\n\n- Do not rely solely on blunt commands or criticism.\n- Share a relatable story or historical role model.\n- Ask a gentle, thought-provoking question to let them reflect.\n- Highlight the positive rewards of good character alongside the consequences of negative habits.",
            "reflection_title": "Pause & Reflect: Identifying Styles in Surah Al-Hujurat",
            "reflection_prompt": "Reflect on Surah Al-Hujurat. Can you identify a verse that uses direct command style? Can you identify a verse that uses an analogy or parable? How do these varying styles make the moral prohibition against backbiting so powerful?",
            "misconception_title": "Common Misconception: Viewing the Qur'an as a Monotone Textbook",
            "misconception": "The Qur'an is written in a single, dry textbook format that must be read like an academic manual.",
            "reality": "The Qur'an shifts dynamically between legal precision, poetic grandeur, intimate dialogues, vivid parables, and dramatic historical narratives to address the multifaceted nature of human consciousness."
        },
        "card6": {
            "question": "Why does the Holy Qur'an employ diverse communication styles, such as narratives, parables, and rhetorical questions, instead of solely listing rules?",
            "options": [
                "A) To make the text longer and more difficult to memorize.",
                "B) To engage both human intellect and emotion, making divine guidance comprehensive, memorable, and morally transformative.",
                "C) Because the rules of Islam were constantly changing and required stories to replace them.",
                "D) To confuse readers who do not have a background in ancient history."
            ],
            "answer": "B",
            "correct_answer": "B",
            "explanation": "The diverse rhetorical styles (uslub) of the Qur'an are intentionally designed to address the totality of human nature—engaging intellect, emotion, imagination, and conscience so that moral guidance is deeply internalized."
        },
        "card7": {
            "summary_title": "Key Points & Unit Vocabulary",
            "key_points": [
                "The Qur'an utilizes varied literary styles (Uslub), including commands, prohibitions, narratives, parables, and dialogues.",
                "Each style serves a distinct pedagogical objective: laws define boundaries, narratives model virtue, and parables provoke thought.",
                "Recognizing the rhetorical style of a verse is necessary for accurate interpretation and prevents taking expressions out of context."
            ],
            "vocabulary": [
                {"term": "Uslub al-Qur'an", "definition": "The diverse literary, structural, and rhetorical styles of the Qur'an."},
                {"term": "Qasas al-Qur'an", "definition": "Historical accounts of prophets and past nations revealed in the Qur'an to impart moral lessons."},
                {"term": "Amthal al-Qur'an", "definition": "Parables and analogies in the Qur'an that illuminate spiritual realities through physical examples."}
            ],
            "exit_ticket_title": "Exit Ticket: Styles and Functions",
            "exit_ticket_prompt": "List three distinct communication styles used in the Qur'an, and explain in one sentence how one of them helps you remember an ethical lesson."
        }
    },

    # ── LESSON 1.1.5 ─────────────────────────────────────────────────────────
    {
        "unit_order": 5,
        "unit_name": "Reading for Meaning and Interpretation",
        "lesson_title": "Reading for Meaning and Interpretation",
        "unit_description": "Master the safe, methodological protocols of Qur'anic interpretation (Tafsir), the essential role of historical context (Asbab al-Nuzul), and how to guard against personal bias.",
        "image": {
            "title": "Manuscript Page of Surah Al-Baqarah",
            "caption": "Historic Qur'anic folio from the Egyptian National Library, illustrating the classical scribal tradition, vocalization markings, and the scholarly preservation of revelation.",
            "url": "https://upload.wikimedia.org/wikipedia/commons/b/b5/Quran_page_-_Al-Baqara_Sura_-_Egyptian_National_Library.jpg",
            "author": "Egyptian National Library",
            "licensing": "Public Domain",
            "source": "Wikimedia Commons"
        },
        "svg_fn": get_svg_lesson_5,
        "card1": {
            "inquiry_question": "How do we safely and responsibly read the Qur’an to extract its authentic meanings without falling into personal bias?",
            "connection_hook": "Imagine finding a medical prescription bottle and guessing the dosage based entirely on your personal mood, without consulting the doctor, pharmacist, or dosage label. That would be extremely dangerous! In a similar way, reading the Qur'an requires a disciplined, source-conscious methodology. To extract authentic guidance, we must understand how classical scholars connect language, revelation context (*Asbab al-Nuzul*), and the Prophet's Sunnah.",
            "goals": [
                "Define the science of Qur'anic exegesis (Tafsir) and the role of Asbab al-Nuzul.",
                "Execute the 4-Tier Safe Interpretation Protocol when analyzing verses.",
                "Recognize why subjective, unguided personal interpretation (*Tafsir bi-al-Ra'y*) is prohibited in Islam."
            ]
        },
        "card2": {
            "concept_title": "The Science of Exegesis: Tafsir and Asbab al-Nuzul",
            "concept_markdown": "In Islamic scholarship, reading the Qur'an is governed by established academic sciences:\n\n- **Tafsir:** The systematic science of explaining the meanings of the Qur'an, drawing upon classical Arabic lexicography, grammar, Prophetic Hadith, and the explanations of the Prophet's companions (*Sahabah*).\n- **Context of Revelation (*Asbab al-Nuzul*):** The specific historical events, questions, or societal dilemmas that occasioned the revelation of particular verses. Understanding Asbab al-Nuzul is indispensable for discerning whether a verse establishes a universal principle or addresses a specific historical situation.\n- **The Prophet (PBUH) as Primary Interpreter:** Allah appointed the Prophet Muhammad (PBUH) as the direct authoritative explainer of the revelation.",
            "callout_title": "Scripture Panel: Surah An-Nahl (16:44)",
            "callout_text": "> \"And We revealed to you the message [O Muhammad] that you may make clear to the people what was sent down to them and that they might give thought.\" [Surah An-Nahl, 16:44]\n\n*Exegetical Note: This verse establishes that the Prophet Muhammad (PBUH) is the primary interpreter of the Qur'an. Authentic exegesis must anchor itself in his Sunnah and the consensus of early scholars.*"
        },
        "card3": {
            "concept_title": "Clarifying the Concept: The 4-Tier Safe Interpretation Protocol",
            "concept_markdown": "To study any verse responsibly and avoid misinterpretation, students must follow a disciplined funnel:\n\n1. **Step 1: Direct Arabic Text & Lexicon:** Examine the classical Arabic words and grammar; consult a reliable translation.\n2. **Step 2: Historical Context (*Asbab al-Nuzul*):** Identify when, where, and why the verse was revealed (Mecca vs. Medina; general principle vs. specific crisis).\n3. **Step 3: Prophetic Explanation & Classical Tafsir:** Review how Prophet Muhammad (PBUH) implemented the verse, followed by classical authorities (Ibn Kathir, Al-Qurtubi, Al-Tabari).\n4. **Step 4: Personal Reflection & Application:** Reflect on how the extracted ethical principle applies to your life today, without altering established meanings.",
            "diagram_title": "4-Tier Safe Interpretation Protocol (Funnel Diagram)",
            "diagram_caption": "Visual funnel diagram illustrating the disciplined methodological sequence required to interpret Qur'anic verses safely.",
            "step_process_title": "The 4 Sequential Steps of Safe Exegesis",
            "step_process_steps": [
                "Step 1: Textual Grounding — Read the original Arabic text alongside verified translations of meanings to establish literal phrasing.",
                "Step 2: Contextual Analysis — Investigate the Asbab al-Nuzul (occasions of revelation) to identify historical triggers and audience.",
                "Step 3: Scholarly Corroboration — Consult authentic Hadith and classical Tafsir compilations to understand early consensus.",
                "Step 4: Ethical Application — Translate the verified moral lesson into personal character and contemporary decision-making."
            ]
        },
        "card4": {
            "scenario_title": "Student Case Study: Avoiding the Decontextualization Trap",
            "scenario": "Mussa reads an isolated translation of a verse that mentions \"fighting in the cause of Allah\" and becomes confused. He asks his teacher, \"Does this verse mean Muslims must fight anyone who disagrees with them?\" Mr. Ibrahim guides him through the Safe Interpretation Protocol: \"Mussa, we never interpret a verse in isolation. If we examine the *Asbab al-Nuzul* of this verse, we discover it was revealed in Medina when the early Muslim community was facing existential military aggression from Qurayshi armies and was commanded to defend their lives and religious freedom. Classical Tafsir clarifies that Islam strictly forbids unprovoked aggression. Skipping context leads to dangerous misunderstandings.\"",
            "analysis": "Mr. Ibrahim demonstrated that examining *Asbab al-Nuzul* prevents decontextualization—one of the primary causes of ideological extremism and misunderstanding."
        },
        "card5": {
            "application_title": "Real-World Application: Responsible Scholarship in the Digital Age",
            "application_text": "When researching religious questions for school assignments or personal understanding:\n\n- Never fabricate religious rulings based on a quick, unguided reading of a single verse.\n- Always consult verified commentary from qualified IRE textbooks or recognized scholars.\n- Practice intellectual humility: acknowledging what you do not know is a foundational Islamic virtue (*Nisf al-‘Ilm* - half of knowledge).",
            "reflection_title": "Pause & Reflect: Literal Phrasing vs. Contextual Scope",
            "reflection_prompt": "Why is it vital to distinguish between what words literally mean in a dictionary and the historical context in which they were revealed? How does this protect society from extremist distortions?",
            "misconception_title": "Common Misconception: Subjective Interpretation (Tafsir bi-al-Ra'y)",
            "misconception": "Anyone can interpret the Qur'an according to their personal feelings, opinions, or modern convenience without studying classical tools.",
            "reality": "Prophet Muhammad (PBUH) warned against interpreting the Qur'an based on mere conjecture. Legitimate interpretation requires linguistic mastery, knowledge of Hadith, Asbab al-Nuzul, and adherence to established methodological rules."
        },
        "card6": {
            "question": "What is the primary purpose of studying Asbab al-Nuzul (the contexts of revelation) when interpreting a Qur'anic verse?",
            "options": [
                "A) To discover which scribe penned the verse onto parchment.",
                "B) To understand the historical circumstances and reasons behind a verse's revelation, clarifying its true scope and meaning.",
                "C) To translate the Arabic words into English and Swahili.",
                "D) To replace the text of the Qur'an with historical stories."
            ],
            "answer": "B",
            "correct_answer": "B",
            "explanation": "Asbab al-Nuzul provides essential historical context explaining why and when a verse was revealed. This prevents readers from stripping verses of their background and misapplying specific situational directives as universal rulings."
        },
        "card7": {
            "summary_title": "Key Points & Unit Vocabulary",
            "key_points": [
                "Qur'anic interpretation (Tafsir) is an objective, systematic academic discipline, not a matter of subjective conjecture.",
                "Asbab al-Nuzul (occasions of revelation) is indispensable for understanding the historical context and legal scope of verses.",
                "The 4-Tier Protocol ensures that personal reflection is grounded in authentic text, context, and scholarly consensus."
            ],
            "vocabulary": [
                {"term": "Tafsir", "definition": "The scholarly science of elucidating and explaining the meanings of the Holy Qur'an."},
                {"term": "Asbab al-Nuzul", "definition": "The specific historical events or inquiries that occasioned the revelation of verses."},
                {"term": "Tafsir bi-al-Ra'y", "definition": "Unguided, subjective interpretation based purely on personal opinion without academic tools, strictly cautioned against."}
            ],
            "exit_ticket_title": "Exit Ticket: The Interpretation Funnel",
            "exit_ticket_prompt": "State the four sequential steps of the Safe Interpretation Protocol in your own words, explaining why step 4 must come last."
        }
    },

    # ── LESSON 1.1.6 ─────────────────────────────────────────────────────────
    {
        "unit_order": 6,
        "unit_name": "Research and Presentation",
        "lesson_title": "Research and Presentation",
        "unit_description": "Develop high academic integrity and digital research literacy in Qur'anic studies, evaluating source credibility, proper citation protocols, and rejecting unverified claims.",
        "image": {
            "title": "Historical Islamic Research Manuscript",
            "caption": "A classical Islamic academic manuscript showing marginal annotations, cross-references, and scholarly chains of narration (Isnad), modeling rigorous citation ethics.",
            "url": "https://upload.wikimedia.org/wikipedia/commons/a/a6/Cheshm_manuscript.jpg",
            "author": "Wikimedia Commons",
            "licensing": "Public Domain",
            "source": "Wikimedia Commons"
        },
        "svg_fn": get_svg_lesson_6,
        "card1": {
            "inquiry_question": "How can we use digital and library resources to research the language and style of the Qur’an while maintaining high academic integrity?",
            "connection_hook": "Imagine writing a major research paper for school. If you copy-paste claims from random internet blogs without verifying who wrote them or checking their bibliography, your teacher will mark your work down for lack of academic credibility. In Islamic studies, verifying our sources is even more paramount. We must learn how to identify peer-reviewed materials, cite scriptures accurately, and present findings with intellectual honesty.",
            "goals": [
                "Evaluate the reliability and authority of digital and printed Islamic resources.",
                "Apply accurate citation standards for Qur'anic verses and scholarly references.",
                "Demonstrate academic integrity rooted in the Islamic values of Sidq (Truthfulness) and Amanah (Trust)."
            ]
        },
        "card2": {
            "concept_title": "Academic Integrity: The Islamic Tradition of Verification (Tathabbut)",
            "concept_markdown": "In Islamic scholarship, rigorous academic integrity is not merely a secular school guideline—it is a sacred religious duty:\n\n- **Source Reliability:** Evaluating sources based on the author's credentials, references, and grounding in mainstream Islamic scholarship.\n- **The Tradition of Verification (*Tathabbut*):** From the earliest centuries, Muslim scholars developed the science of *Isnad* (chains of transmission) to scrutinize every narrator and citation before accepting a statement.\n- **Honest Attribution:** Distinguishing one's own voice from direct scriptural quotations or scholarly opinions. Never misquote, fabricate references, or spread sensational claims.",
            "callout_title": "Scripture Panel: Surah Al-Hujurat (49:6)",
            "callout_text": "> \"O you who have believed, if there comes to you a disobedient person with information, investigate, lest you harm a people out of ignorance and become, over what you have done, regretful.\" [Surah Al-Hujurat, 49:6]\n\n*Exegetical Note: This verse forms the Quranic charter for critical thinking and information verification. It commands believers to authenticate news and sources before accepting or propagating them.*"
        },
        "card3": {
            "concept_title": "Clarifying the Concept: The Research Quality Checklist",
            "concept_markdown": "When preparing a research project or presentation on Ulum al-Qur'an, apply three essential rules:\n\n1. **Verify Author Credentials:** Seek established curriculum textbooks, university archives, or works by recognized Islamic scholars. Discard anonymous blog posts or social media reels.\n2. **Cite with Precision:** When quoting a translation of the Qur'an, state the exact Surah name and Verse number (e.g., \"Surah Al-Hujurat, 49:6\"). When quoting Hadith, cite the primary collection (e.g., Sahih al-Bukhari) and its authenticity grade.\n3. **Maintain Objective Tone:** Refrain from exaggerated or pseudoscientific assertions; present balanced, verified knowledge.",
            "diagram_title": "Academic Research & Source Quality Checklist",
            "diagram_caption": "Evaluation rubric detailing the four criteria for authentic Islamic research and digital information literacy.",
            "table_headers": ["Evaluation Metric", "Credible Academic Resource", "Unreliable / Viral Media Claim"],
            "table_rows": [
                ["Author Credentials", "Recognized scholar, certified educator, or peer-reviewed academic", "Anonymous creator, social media influencer, or pseudonymous forum"],
                ["Scripture Citations", "Exact Surah name, verse numbers, and recognized translation cited", "Vague assertions (\"the Qur'an says\") without verifiable reference"],
                ["Institutional Review", "Published by educational boards, university presses, or mosques", "Self-published blogs prioritizing ad views and sensationalism"],
                ["Presentation Tone", "Objective, respectful, analytical, and academically grounded", "Sensationalist clickbait, emotional manipulation, or conspiracy theories"]
            ]
        },
        "card4": {
            "scenario_title": "Student Case Study: The Viral \"Smartphone Prediction\" Slide",
            "scenario": "Omar is preparing a digital presentation on the linguistic beauty of the Qur'an. He stumbles upon an online blog claiming, \"The Qur'an predicted modern smartphone technology through secret numerical codes!\" Excited, he plans to include it. His classmate Amina advises: \"Omar, let's test this through our Source Quality Checklist. Who wrote this post? Is there any classical Tafsir, Arabic linguistic evidence, or academic peer review? None—it is just an anonymous blog post. If we include unverified claims, our teacher and peers will lose trust in our whole presentation. Let's showcase established, magnificent linguistic facts supported by our IRE syllabus.\"",
            "analysis": "Amina prevented Omar from compromising his academic integrity. Genuine appreciation of the Qur'an does not need sensationalized or fabricated claims."
        },
        "card5": {
            "application_title": "Real-World Application: Upholding Integrity Across Digital Platforms",
            "application_text": "Apply information verification to your daily digital communication:\n\n- When you receive a forwarded religious message on social media (WhatsApp, TikTok, Instagram), do not share it until you verify its authenticity through a reliable teacher or textbook.\n- In class presentations, build a clean \"References & Citations\" slide listing your sources with exact Surah and verse numbers. This demonstrates academic maturity and builds trust.",
            "reflection_title": "Pause & Reflect: Sidq and Amanah in Schoolwork",
            "reflection_prompt": "How does citing your sources accurately and refusing to plagiarize connect directly to the Islamic moral values of Sidq (Truthfulness) and Amanah (Trustworthiness)?",
            "misconception_title": "Common Misconception: Popularity Equals Authenticity",
            "misconception": "If a religious video or post has hundreds of thousands of likes and shares on social media, its information must be authentic.",
            "reality": "Social media algorithms promote emotional sensationalism rather than verified scholarship. Many viral religious claims are fabricated or taken out of context. Authentic Islamic knowledge is measured by rigorous citation and scholarly consensus, not by view counts."
        },
        "card6": {
            "question": "When presenting research on the Qur'an, why is it essential to provide the specific Surah name and verse number for every quotation?",
            "options": [
                "A) To make the slides look overly complex and technical.",
                "B) To uphold academic integrity, allow listeners to verify the source directly, and demonstrate respect for the sacred text.",
                "C) Because the Qur'an cannot be understood unless the listener has memorized every verse number.",
                "D) To prove that you completed the assignment without consulting any library textbooks."
            ],
            "answer": "B",
            "correct_answer": "B",
            "explanation": "Accurate scriptural citations (Surah name and verse number) ensure academic integrity and accountability, enabling peers and educators to locate the passage in context and confirm the validity of the research."
        },
        "card7": {
            "summary_title": "Key Points & Unit Vocabulary",
            "key_points": [
                "Research in Islamic studies requires evaluating sources for academic credibility and scholarly grounding.",
                "Surah Al-Hujurat (49:6) commands believers to verify all information prior to accepting or transmitting it.",
                "Accurate citations and objective presentation embody the Islamic ethical virtues of Sidq (Truthfulness) and Amanah (Trust)."
            ],
            "vocabulary": [
                {"term": "Tathabbut", "definition": "The Islamic methodological practice of thorough verification and authentication before accepting news."},
                {"term": "Isnad", "definition": "The documented chain of qualified narrators or citations supporting an academic claim."},
                {"term": "Amanah 'Ilmiyyah", "definition": "Academic integrity and honesty in researching, quoting, and attributing knowledge."}
            ],
            "exit_ticket_title": "Exit Ticket: Evaluating an Online Source",
            "exit_ticket_prompt": "Write down two specific evaluation questions you will ask next time you encounter an online article or video discussing the Qur'an."
        }
    },

    # ── LESSON 1.1.7 ─────────────────────────────────────────────────────────
    {
        "unit_order": 7,
        "unit_name": "Unit Synthesis: The Qur’an as Guidance",
        "lesson_title": "Unit Synthesis: The Qur’an as Guidance",
        "unit_description": "Synthesize the learnings of Ulum al-Qur'an—miracles, language, styles, and interpretation—to establish the Holy Qur'an as the ultimate divine guide (Al-Furqan) for personal and community life.",
        "image": {
            "title": "Open Qur'an Illuminated Folio",
            "caption": "An open historic manuscript of the Holy Qur'an, displaying ornate illumination and clear calligraphy, symbolizing the accessible and living guidance of Allah for humanity.",
            "url": "https://upload.wikimedia.org/wikipedia/commons/b/bd/Mamluk_era_Quran%2C_circa_1380%2C_open_to_sura_16.jpg",
            "author": "Chester Beatty Library",
            "licensing": "Public Domain",
            "source": "Wikimedia Commons"
        },
        "svg_fn": get_svg_lesson_7,
        "card1": {
            "inquiry_question": "How do we combine our learning of the Qur’an’s miracles, language, and styles to treat the Qur’an as our primary source of daily guidance?",
            "connection_hook": "Imagine you are given a state-of-the-art navigational compass to guide you through an unexplored, dense forest. To use it successfully, you must respect its precision, learn how its magnetic dial works, understand its readings, and follow its directions faithfully. The sciences of the Qur'an (*Ulum al-Qur'an*) are like learning how the compass works. Once we appreciate its miraculous nature, language, and styles, we are equipped to let it guide our character, choices, and relationships.",
            "goals": [
                "Synthesize the core lessons of Ulum al-Qur'an into a unified framework for lifelong guidance.",
                "Differentiate between superficial engagement and grounded, transformative interaction with the Qur'an.",
                "Formulate a personal weekly action plan to implement Qur'anic moral values in daily life."
            ]
        },
        "card2": {
            "concept_title": "The Ultimate Guide: Al-Furqan and Living Hidayah",
            "concept_markdown": "In this capstone unit synthesis, we examine why the Qur'an is the foundational guide for Muslims:\n\n- **The Ultimate Criterion (*Al-Furqan*):** The Qur'an serves as the divine benchmark that distinguishes truth from falsehood, justice from oppression, and righteousness from corruption.\n- **Comprehensive Guidance (*Hidayah*):** Its purpose is not merely academic study; it is a transformative roadmap designed to cultivate moral excellence (*Ihsan*), social responsibility, and spiritual closeness to Allah.\n- **Holistic Synthesis:** True appreciation moves beyond ceremonial veneration to active contemplation (*Tadabbur*) and everyday ethical practice.",
            "callout_title": "Scripture Panel: Surah Al-Baqarah (2:2) & Surah Al-Isra (17:9)",
            "callout_text": "> \"This is the Book about which there is no doubt, a guidance for those conscious of Allah.\" [Surah Al-Baqarah, 2:2]\n\n> \"Indeed, this Qur'an guides to that which is most suitable and gives good tidings to the believers who do righteous deeds that they will have a great reward.\" [Surah Al-Isra, 17:9]\n\n*Exegetical Note: Classical commentators explain that \"most suitable\" (Aqwam) encompasses all aspects of human flourishing—personal ethics, social harmony, justice, and spiritual fulfillment.*"
        },
        "card3": {
            "concept_title": "Clarifying the Concept: Connecting the Four Pillars of the Unit",
            "concept_markdown": "Let us unite the core discoveries of this unit into a coherent roadmap:\n\n1. **The Miracle (*Mu‘jizah*):** Builds unshakeable faith (*Iman*) by proving that the Qur'an is divine, inimitable, and miraculously preserved across fourteen centuries.\n2. **The Language (Arabic):** Teaches reverence and caution with translations, showing why we study root words and avoid superficial assumptions.\n3. **The Styles (*Uslub*):** Demonstrates how Allah addresses the entire human being—using laws to protect us, stories to inspire us, and parables to awaken our conscience.\n4. **The Interpretation (*Tafsir*):** Provides the disciplined 4-tier funnel to extract safe, authentic guidance without falling prey to personal bias.",
            "diagram_title": "Qur'anic Engagement: Shallow vs. Grounded Understanding",
            "diagram_caption": "Comparative analysis contrasting superficial, passive interaction with grounded, transformative engagement through Ulum al-Qur'an.",
            "table_headers": ["Engagement Dimension", "Shallow / Ceremonial Interaction", "Grounded Understanding (Ulum al-Qur'an)"],
            "table_rows": [
                ["Recitation Approach", "Rapid chanting without comprehension or curiosity about meaning", "Reverent recitation paired with contemplation (Tadabbur) and study"],
                ["Textual Perspective", "Treats translations as literal or quotes isolated verse fragments", "Anchored in original Arabic roots, Asbab al-Nuzul, and classical Tafsir"],
                ["Everyday Attitude", "Treats the physical Book as a decorative artifact or protective charm", "Honors the Book as a living moral constitution (Al-Furqan) for daily life"],
                ["Behavioral Impact", "Disconnect between ritual recitation and everyday interpersonal conduct", "Transforms character: manifests honesty, humility, justice, and compassion"]
            ]
        },
        "card4": {
            "scenario_title": "Student Case Study: Zainab's Transformative Realization",
            "scenario": "At the conclusion of the term, Zainab shares a reflection with her mother: \"I used to think that respecting the Qur'an simply meant wrapping it in fine velvet, placing it on the highest shelf in the living room, and occasionally kissing the cover. But after studying Ulum al-Qur'an this term, I understand that true respect means opening it, studying its context, and living its guidance. Now, when I read a verse, I check its Asbab al-Nuzul, appreciate its literary style, and ask myself how I can practice its virtues—like being truthful with my teachers and kind to my classmates.\"",
            "analysis": "Zainab's journey exemplifies the unit's objective: transitioning from superficial veneration to deep, lived guidance."
        },
        "card5": {
            "application_title": "Real-World Application: The Weekly Qur'anic Guidance Action Plan",
            "application_text": "Put your learning into immediate action this week through this 3-step action plan:\n\n1. **Select an Ethical Directive:** Choose one specific moral principle taught in the Qur'an (e.g., verifying information from Q 49:6, fulfilling promises from Q 17:34, or speaking kindly from Q 2:83).\n2. **Set Concrete Actions:** Write down two measurable actions for home and school (e.g., stopping a negative rumor at school; helping a sibling with patience).\n3. **Review at Week's End:** Reflect on how grounding your actions in Qur'anic wisdom strengthened your character and inner peace.",
            "reflection_title": "Pause & Reflect: Scholarship as a Shield Against Extremism",
            "reflection_prompt": "How does a structured, scholarly approach to the Qur'an—rooted in Ulum al-Qur'an—protect Muslim youth and communities from being misled by extreme or distorted interpretations?",
            "misconception_title": "Common Misconception: Ceremonial Veneration Replaces Study",
            "misconception": "Merely having a decorative copy of the Qur'an at home or wearing a verse amulet provides sufficient religious guidance.",
            "reality": "The Qur'an was revealed as an active, intellectual, and moral guide for human conduct (*Hidayah*). Keeping it unread on a shelf denies its foundational purpose as a living light for humanity."
        },
        "card6": {
            "question": "Which of the following is the most complete and responsible way for a Grade 9 student to show genuine appreciation for the Qur'an as divine guidance?",
            "options": [
                "A) Keeping the physical copy beautifully decorated on a high shelf without ever reading or studying its translation.",
                "B) Reciting the Arabic words as rapidly as possible without paying attention to meaning or seeking scholarly commentary.",
                "C) Studying its original language, consulting reliable translations with Tafsir, and actively implementing its moral values in daily character.",
                "D) Quoting verses out of context in debates with classmates without checking the historical circumstances of revelation."
            ],
            "answer": "C",
            "correct_answer": "C",
            "explanation": "Genuine, source-grounded appreciation of the Qur'an unites reverent recitation, disciplined study of its meanings through reliable exegesis (Tafsir), and the active practice of its ethical virtues in daily life."
        },
        "card7": {
            "summary_title": "Unit Key Points & Vocabulary Synthesis",
            "key_points": [
                "Ulum al-Qur'an provides the foundational academic toolkit to read, understand, and apply the Book of Allah safely.",
                "Grounded engagement combines reverent recitation, contextual study (Asbab al-Nuzul), and adherence to verified Tafsir.",
                "The ultimate objective of studying the Qur'an's sciences is to transform personal character and build a just, compassionate society."
            ],
            "vocabulary": [
                {"term": "Al-Furqan", "definition": "The Criterion between truth and falsehood; one of the primary names of the Holy Qur'an."},
                {"term": "Hidayah", "definition": "Divine guidance provided by Allah to steer humanity toward righteous conduct and spiritual fulfillment."},
                {"term": "Tadabbur", "definition": "Deep, deliberate contemplation upon the meanings, implications, and personal lessons of Qur'anic verses."}
            ],
            "exit_ticket_title": "Exit Ticket: The Living Compass",
            "exit_ticket_prompt": "Write a concise paragraph explaining why studying Ulum al-Qur'an is essential for every student who desires to use the Qur'an as their daily moral compass."
        }
    }
]


# ─────────────────────────────────────────────────────────────────────────────
# INGESTION EXECUTION ENGINE
# ─────────────────────────────────────────────────────────────────────────────

def ingest_grade9_ire_topic1():
    print("=" * 80)
    print("STARTING INGESTION: GRADE 9 IRE — TOPIC 1: ULUM AL-QUR'AN")
    print("=" * 80)

    with transaction.atomic():
        # 1. Resolve Target Topic 341
        try:
            topic = Topic.objects.get(id=341)
            print(f"[+] Found Target Topic: ID {topic.id} — '{topic.name}'")
            print(f"    Subject: {topic.subject.name} (ID: {topic.subject.id})")
            print(f"    Grade  : {topic.subject.grade.name} (ID: {topic.subject.grade.id})")
        except Topic.DoesNotExist:
            print("[!] ERROR: Topic 341 does not exist in the database! Aborting.")
            sys.exit(1)

        # 2. Verify Subject and Grade
        if topic.subject.name != "IRE" or topic.subject.grade.name != "Grade 9":
            print(f"[!] ERROR: Topic 341 is not Grade 9 IRE! (Subject: {topic.subject.name}, Grade: {topic.subject.grade.name})")
            sys.exit(1)

        # 3. Update Topic Metadata
        topic.name = "Ulum al-Qur'an (The Sciences of the Qur'an)"
        topic.order = 1
        topic.description = (
            "Explore the foundational sciences of the Holy Qur'an: the concept of divine miracles (Mu‘jizah), "
            "the multi-faceted inimitability (I‘jaz al-Qur'an), classical Arabic as the language of revelation, "
            "diverse rhetorical communication styles (Uslub), methodological protocols for safe interpretation (Tafsir), "
            "academic research ethics, and living synthesis of the Qur'an as divine guidance."
        )
        topic.save()
        print(f"[+] Updated Topic 341 details successfully.")

        # 4. Clean up any existing units/lessons under Topic 341 (Strict Isolation)
        existing_units = LearningUnit.objects.filter(topic=topic)
        unit_count = existing_units.count()
        if unit_count > 0:
            print(f"[-] Cleaning up {unit_count} existing LearningUnit(s) under Topic 341...")
            existing_units.delete()

        total_units = 0
        total_lessons = 0
        total_pages = 0
        total_blocks = 0
        total_assets = 0

        # 5. Ingest All 7 Lessons
        for cfg in LESSONS_DATA:
            u_order = cfg["unit_order"]
            u_name = cfg["unit_name"]
            l_title = cfg["lesson_title"]

            print(f"\n--- Ingesting Lesson {u_order}/7: '{l_title}' ---")

            # Create LearningUnit
            unit = LearningUnit.objects.create(
                topic=topic,
                order=u_order,
                name=u_name,
                description=clean_text(cfg["unit_description"])
            )
            total_units += 1

            # Create Published Lesson
            lesson = Lesson.objects.create(
                topic=topic,
                learning_unit=unit,
                title=clean_text(l_title),
                status="published",
                version=1,
                immutable_metadata={
                    "curriculum": "CBC",
                    "grade": "Grade 9",
                    "subject": "IRE",
                    "strand": "Strand 1.0: Qur'an",
                    "sub_strand": "Sub-strand 1.1: Ulum al-Qur'an (The Sciences of the Qur'an)",
                    "topic_id": topic.id,
                    "topic_name": topic.name,
                    "lesson_code": f"1.1.{u_order}",
                    "author": "VLearn Senior Curriculum Specialist",
                    "enrichment_version": "v3_pedagogical_svg"
                }
            )
            total_lessons += 1

            # ─────────────────────────────────────────────────────────────────
            # LESSON ASSETS: 1. Diagram Asset, 2. Authentic Image Asset
            # ─────────────────────────────────────────────────────────────────
            # Asset 1: Custom Pedagogical Vector SVG Diagram
            svg_content = cfg["svg_fn"]()
            diag_asset = LessonAsset.objects.create(
                lesson=lesson,
                asset_type="diagram",
                source_type="ai_generated",
                storage_type="url",
                status="attached",
                title=f"Diagram: {l_title}",
                description=f"Pedagogical responsive vector SVG diagram illustrating {l_title}.",
                url=f"https://vlearn.africa/assets/diagrams/ire/grade9_topic_1_lesson_{u_order}.svg",
                metadata={
                    "svg_xml": svg_content,
                    "viewBox": "0 0 880 480",
                    "theme": "#0f172a"
                }
            )
            total_assets += 1

            # Asset 2: Authentic Wikimedia Commons Image
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
            total_assets += 1

            # Asset 3: Authentic Educational Video Asset
            vid_info = TOPIC_1_VIDEOS[u_order]
            vid_asset = LessonAsset.objects.create(
                lesson=lesson,
                asset_type="video",
                source_type="external",
                storage_type="url",
                status="attached",
                title=clean_text(vid_info["title"]),
                description=clean_text(vid_info["description"]),
                url=f"https://www.youtube.com/watch?v={vid_info['yt_id']}",
                metadata={
                    "youtube_id": vid_info["yt_id"],
                    "description": clean_text(vid_info["description"])
                }
            )
            total_assets += 1

            # ─────────────────────────────────────────────────────────────────
            # CARD 1 (Page 1): Orientation & Learning Goals
            # ─────────────────────────────────────────────────────────────────
            c1 = cfg["card1"]
            b1_img = LessonBlock.objects.create(
                lesson=lesson, page_number=1, page_title="Orientation & Hook",
                order=5, component_order=1,
                block_type="suggested_image", component_type="suggested_image",
                title=clean_text(img_info["title"]),
                content={
                    "title": clean_text(img_info["title"]),
                    "caption": clean_text(img_info["caption"]),
                    "url": img_info["url"]
                },
                metadata={"source": "Wikimedia Commons"}
            )
            b1_img.assets.add(img_asset)
            total_blocks += 1

            b1 = LessonBlock.objects.create(
                lesson=lesson, page_number=1, page_title="Orientation & Inquiry",
                order=10, component_order=2,
                block_type="learning_goal", component_type="learning_goal",
                title=f"Lesson Inquiry: {l_title}",
                content={
                    "inquiry_question": clean_text(c1["inquiry_question"]),
                    "connection_hook": clean_text(c1["connection_hook"]),
                    "goals": clean_dict(c1["goals"]),
                    "text": (
                        f"### Inquiry Question\n{clean_text(c1['inquiry_question'])}\n\n"
                        f"### Connection\n{clean_text(c1['connection_hook'])}\n\n"
                        f"### Learning Objectives\n" +
                        "\n".join([f"- {g}" for g in clean_dict(c1["goals"])])
                    )
                }
            )
            total_blocks += 1

            # ─────────────────────────────────────────────────────────────────
            # CARD 2 (Page 2): Core Teaching & Scripture Panel
            # ─────────────────────────────────────────────────────────────────
            c2 = cfg["card2"]
            b2_concept = LessonBlock.objects.create(
                lesson=lesson, page_number=2, page_title="Core Scriptural Teaching",
                order=20, component_order=1,
                block_type="concept_explanation", component_type="concept_explanation",
                title=clean_text(c2["concept_title"]),
                content={
                    "title": clean_text(c2["concept_title"]),
                    "markdown": clean_text(c2["concept_markdown"]),
                    "text": clean_text(c2["concept_markdown"])
                }
            )
            # Attach authentic historical image to the core concept explanation
            b2_concept.assets.add(img_asset)
            total_blocks += 1

            LessonBlock.objects.create(
                lesson=lesson, page_number=2, page_title="Core Scriptural Teaching",
                order=30, component_order=2,
                block_type="callout", component_type="callout",
                title=clean_text(c2["callout_title"]),
                content={
                    "title": clean_text(c2["callout_title"]),
                    "text": clean_text(c2["callout_text"]),
                    "callout_type": "scripture_panel"
                }
            )
            total_blocks += 1

            # ─────────────────────────────────────────────────────────────────
            # CARD 3 (Page 3): Deep Explanation & Pedagogical Blueprint
            # ─────────────────────────────────────────────────────────────────
            c3 = cfg["card3"]
            LessonBlock.objects.create(
                lesson=lesson, page_number=3, page_title="In-Depth Explanation & Blueprint",
                order=40, component_order=1,
                block_type="concept_explanation", component_type="concept_explanation",
                title=clean_text(c3["concept_title"]),
                content={
                    "title": clean_text(c3["concept_title"]),
                    "markdown": clean_text(c3["concept_markdown"]),
                    "text": clean_text(c3["concept_markdown"])
                }
            )
            total_blocks += 1

            # Suggested Diagram block
            b3_diag = LessonBlock.objects.create(
                lesson=lesson, page_number=3, page_title="In-Depth Explanation & Blueprint",
                order=50, component_order=2,
                block_type="suggested_diagram", component_type="suggested_diagram",
                title=clean_text(c3["diagram_title"]),
                content={
                    "title": clean_text(c3["diagram_title"]),
                    "caption": clean_text(c3["diagram_caption"]),
                    "svg": svg_content,
                    "svg_xml": svg_content,
                    "url": diag_asset.url
                }
            )
            b3_diag.assets.add(diag_asset)
            total_blocks += 1

            # Structured comparison table or step process on Card 3
            if "table_headers" in c3:
                LessonBlock.objects.create(
                    lesson=lesson, page_number=3, page_title="In-Depth Explanation & Blueprint",
                    order=60, component_order=3,
                    block_type="comparison_table", component_type="comparison_table",
                    title=f"Structured Analysis: {l_title}",
                    content={
                        "headers": clean_dict(c3["table_headers"]),
                        "rows": clean_dict(c3["table_rows"])
                    }
                )
                total_blocks += 1
            elif "step_process_title" in c3:
                LessonBlock.objects.create(
                    lesson=lesson, page_number=3, page_title="In-Depth Explanation & Blueprint",
                    order=60, component_order=3,
                    block_type="step_process", component_type="step_process",
                    title=clean_text(c3["step_process_title"]),
                    content={
                        "title": clean_text(c3["step_process_title"]),
                        "steps": clean_dict(c3["step_process_steps"])
                    }
                )
                total_blocks += 1

            # ─────────────────────────────────────────────────────────────────
            # CARD 4 (Page 4): Worked Example Scenario
            # ─────────────────────────────────────────────────────────────────
            c4 = cfg["card4"]
            LessonBlock.objects.create(
                lesson=lesson, page_number=4, page_title="Worked Scenario & Case Study",
                order=70, component_order=1,
                block_type="worked_example", component_type="worked_example",
                title=clean_text(c4["scenario_title"]),
                content={
                    "title": clean_text(c4["scenario_title"]),
                    "scenario": clean_text(c4["scenario"]),
                    "analysis": clean_text(c4["analysis"]),
                    "text": (
                        f"### Student Scenario\n{clean_text(c4['scenario'])}\n\n"
                        f"### Pedagogical Analysis\n{clean_text(c4['analysis'])}"
                    )
                }
            )
            total_blocks += 1

            # ─────────────────────────────────────────────────────────────────
            # CARD 5 (Page 5): Real-World Application, Reflection & Misconception
            # ─────────────────────────────────────────────────────────────────
            c5 = cfg["card5"]
            LessonBlock.objects.create(
                lesson=lesson, page_number=5, page_title="Real-World Application & Reflection",
                order=80, component_order=1,
                block_type="real_world_example", component_type="real_world_example",
                title=clean_text(c5["application_title"]),
                content={
                    "title": clean_text(c5["application_title"]),
                    "text": clean_text(c5["application_text"])
                }
            )
            total_blocks += 1

            LessonBlock.objects.create(
                lesson=lesson, page_number=5, page_title="Real-World Application & Reflection",
                order=90, component_order=2,
                block_type="reflection", component_type="reflection",
                title=clean_text(c5["reflection_title"]),
                content={
                    "title": clean_text(c5["reflection_title"]),
                    "prompt": clean_text(c5["reflection_prompt"]),
                    "text": clean_text(c5["reflection_prompt"])
                }
            )
            total_blocks += 1

            LessonBlock.objects.create(
                lesson=lesson, page_number=5, page_title="Real-World Application & Reflection",
                order=100, component_order=3,
                block_type="common_misconception", component_type="common_misconception",
                title=clean_text(c5["misconception_title"]),
                content={
                    "title": clean_text(c5["misconception_title"]),
                    "misconception": clean_text(c5["misconception"]),
                    "reality": clean_text(c5["reality"]),
                    "text": (
                        f"**Misconception:** {clean_text(c5['misconception'])}\n\n"
                        f"**Reality:** {clean_text(c5['reality'])}"
                    )
                }
            )
            total_blocks += 1

            # Suggested Video block on Card 5
            b5_vid = LessonBlock.objects.create(
                lesson=lesson, page_number=5, page_title="Real-World Application & Reflection",
                order=105, component_order=4,
                block_type="suggested_video", component_type="suggested_video",
                title=clean_text(vid_info["title"]),
                content={
                    "title": clean_text(vid_info["title"]),
                    "youtube_id": vid_info["yt_id"],
                    "url": f"https://www.youtube.com/watch?v={vid_info['yt_id']}",
                    "description": clean_text(vid_info["description"])
                },
                metadata={"type": "educational_multimedia"}
            )
            b5_vid.assets.add(vid_asset)
            total_blocks += 1

            # ─────────────────────────────────────────────────────────────────
            # CARD 6 (Page 6): Mastery Knowledge Check (MCQ)
            # ─────────────────────────────────────────────────────────────────
            c6 = cfg["card6"]
            LessonBlock.objects.create(
                lesson=lesson, page_number=6, page_title="Mastery Knowledge Check",
                order=110, component_order=1,
                block_type="knowledge_check", component_type="knowledge_check",
                title=f"Concept Diagnostic: {l_title}",
                content={
                    "question": clean_text(c6["question"]),
                    "options": clean_dict(c6["options"]),
                    "answer": c6["answer"],
                    "correct_answer": c6["correct_answer"],
                    "explanation": clean_text(c6["explanation"])
                }
            )
            total_blocks += 1

            # ─────────────────────────────────────────────────────────────────
            # CARD 7 (Page 7): Summary & Mini-Activity (Exit Ticket)
            # ─────────────────────────────────────────────────────────────────
            c7 = cfg["card7"]
            LessonBlock.objects.create(
                lesson=lesson, page_number=7, page_title="Summary & Exit Ticket",
                order=120, component_order=1,
                block_type="summary", component_type="summary",
                title=clean_text(c7["summary_title"]),
                content={
                    "title": clean_text(c7["summary_title"]),
                    "key_points": clean_dict(c7["key_points"]),
                    "vocabulary": clean_dict(c7["vocabulary"]),
                    "text": (
                        "### Key Points\n" +
                        "\n".join([f"- {p}" for p in clean_dict(c7["key_points"])]) +
                        "\n\n### Vocabulary Review\n" +
                        "\n".join([f"- **{v['term']}:** {v['definition']}" for v in clean_dict(c7["vocabulary"])])
                    )
                }
            )
            total_blocks += 1

            LessonBlock.objects.create(
                lesson=lesson, page_number=7, page_title="Summary & Exit Ticket",
                order=130, component_order=2,
                block_type="mini_activity", component_type="mini_activity",
                title=clean_text(c7["exit_ticket_title"]),
                content={
                    "title": clean_text(c7["exit_ticket_title"]),
                    "instructions": "Complete this brief 2-minute diagnostic reflection in your notebook.",
                    "prompt": clean_text(c7["exit_ticket_prompt"]),
                    "text": clean_text(c7["exit_ticket_prompt"])
                }
            )
            total_blocks += 1

            total_pages += 7
            print(f"  [+] Ingested Lesson {u_order:02d}/7: '{l_title}' (7 cards/pages, 12 blocks, 2 LessonAssets)")

        print("\n" + "=" * 80)
        print("INGESTION AUDIT SUMMARY FOR GRADE 9 IRE TOPIC 1:")
        print(f"  - Topic ID         : {topic.id}")
        print(f"  - Topic Name       : {topic.name}")
        print(f"  - Subject          : {topic.subject.name} (ID: {topic.subject.id})")
        print(f"  - Grade            : {topic.subject.grade.name} (ID: {topic.subject.grade.id})")
        print(f"  - Learning Units   : {total_units} (Target: 7)")
        print(f"  - Published Lessons: {total_lessons} (Target: 7)")
        print(f"  - Total Pages/Cards: {total_pages} (Target: 49)")
        print(f"  - Total Blocks     : {total_blocks} (Target: 84)")
        print(f"  - Total Assets     : {total_assets} (Target: 14)")
        print("=" * 80)


if __name__ == "__main__":
    ingest_grade9_ire_topic1()
