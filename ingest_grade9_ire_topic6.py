"""
VLearn CBC Grade 9 IRE — Topic 6: Belief in Qadar (Divine Decree)
Production Ingestion and Enrichment Script for all 4 Lessons

Target Topic in DB: Topic ID 346 (Subject: IRE ID 53, Grade: Grade 9 ID 18)
Source Markdown: /home/jason-bitega/Desktop/VL/vlearn_repositories/Grade 9 IRE/belief-in-qadar.md

4 Lessons Ingested & Fully Enriched:
  1. Lesson 3.2.1: Key terms and belief
  2. Lesson 3.2.2: Effects of belief
  3. Lesson 3.2.3: Significance and acceptance
  4. Lesson 3.2.4: Unit synthesis

Standardized 7-Card Architecture per Lesson:
  Card 1 (page 1): suggested_image (Wikimedia asset) + learning_goal (Inquiry question + Connection hook)
  Card 2 (page 2): concept_explanation (Authoritative concept) + callout (Scripture Panel)
  Card 3 (page 3): concept_explanation (Deep explanation) + suggested_diagram (Full vector SVG + LessonAsset) + comparison_table / step_process
  Card 4 (page 4): worked_example (Relatable student scenario with analysis & takeaway)
  Card 5 (page 5): suggested_video (Yaqeen Institute YouTube video) + real_world_example + reflection + common_misconception
  Card 6 (page 6): knowledge_check (Interactive MCQ: question, options, answer, explanation)
  Card 7 (page 7): summary (Key points + Vocabulary review) + mini_activity (Exit ticket)
"""

import os
import sys
import re
import django
from django.db import transaction
from django.utils import timezone

# Setup Django Environment
sys.path.append("/home/jason-bitega/Desktop/VL/vlearn_repositories/Vlearn_backend")
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "Nexus_backend.settings")
django.setup()

from curriculum.models import (
    Topic, LearningUnit, Lesson, LessonBlock, LessonAsset
)


def clean_text(text: str) -> str:
    """Removes bracket citations and internal pedagogical tags while preserving markdown."""
    if not text:
        return ""
    text = re.sub(r'\[(?:\d+(?:\.\d+)?(?:,\s*\d+(?:\.\d+)?)*|image_\d+|S\d+.*?|[\d,\s]{2,})\]', '', text)
    text = re.sub(
        r'\[(VISUAL|QURAN REFERENCE|HADITH REFERENCE|BIBLE REFERENCE|REAL WORLD APPLICATION|'
        r'REFLECTION|CRITICAL THINKING|VALUES|MISCONCEPTION|INTERACTION|ETHICAL SCENARIO|'
        r'KEY VERSE|HISTORICAL CONTEXT|PEDAGOGICAL ARCHITECTURE|PROJECT TITLE|MAP|TIMELINE|'
        r'COMPARISON|INFOGRAPHIC|SVG)[^\]]*\]',
        '', text, flags=re.IGNORECASE
    )
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


# ─── 4 PEDAGOGICAL VECTOR SVGS (viewBox="0 0 880 440", theme #0f172a) ─────────

def get_svg_lesson_1():
    """Lesson 3.2.1: The Four Pillars of Qadar & Qadar vs Qadha Framework"""
    return """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 880 440" width="100%" height="100%">
  <defs>
    <linearGradient id="bg1" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#0f172a"/>
      <stop offset="50%" stop-color="#1e293b"/>
      <stop offset="100%" stop-color="#0f172a"/>
    </linearGradient>
    <linearGradient id="ilmGrad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#0284c7"/>
      <stop offset="100%" stop-color="#0369a1"/>
    </linearGradient>
    <linearGradient id="kitabahGrad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#10b981"/>
      <stop offset="100%" stop-color="#047857"/>
    </linearGradient>
    <linearGradient id="masheeahGrad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#f59e0b"/>
      <stop offset="100%" stop-color="#b45309"/>
    </linearGradient>
    <linearGradient id="khalqGrad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#8b5cf6"/>
      <stop offset="100%" stop-color="#6d28d9"/>
    </linearGradient>
    <filter id="shadow1" x="-10%" y="-10%" width="120%" height="120%">
      <feDropShadow dx="0" dy="4" stdDeviation="5" flood-color="#000000" flood-opacity="0.4"/>
    </filter>
  </defs>

  <rect width="880" height="440" fill="url(#bg1)" rx="14"/>
  <rect x="15" y="15" width="850" height="410" fill="none" stroke="#334155" stroke-width="1.5" stroke-dasharray="6 4" rx="10"/>

  <!-- Title & Subtitle -->
  <text x="440" y="42" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="17" font-weight="800" text-anchor="middle" letter-spacing="0.5">THE ARCHITECTURE OF BELIEF IN QADAR (DIVINE DECREE)</text>
  <text x="440" y="63" fill="#94a3b8" font-family="system-ui, sans-serif" font-size="12" text-anchor="middle">The Four Foundational Pillars of Decree &amp; The Theological Bridge Between Qadar and Qadha</text>

  <!-- TOP SECTION: THE FOUR PILLARS (Y: 80 to 235) -->
  <!-- Pillar 1: Knowledge ('Ilm) -->
  <g transform="translate(35, 80)" filter="url(#shadow1)">
    <rect width="190" height="155" rx="10" fill="#1e293b" stroke="#0284c7" stroke-width="1.5"/>
    <rect width="190" height="32" rx="10" fill="url(#ilmGrad)"/>
    <text x="95" y="21" fill="#ffffff" font-family="system-ui, sans-serif" font-size="12" font-weight="700" text-anchor="middle">1. AL-'ILM (KNOWLEDGE)</text>
    <text x="15" y="55" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="10.5" font-weight="700">• Absolute Foreknowledge</text>
    <text x="15" y="75" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10">• Covers past, present &amp; future</text>
    <text x="15" y="95" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10">• Not a leaf falls without it</text>
    <text x="15" y="115" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10">• Knows every human choice</text>
    <rect x="15" y="125" width="160" height="22" rx="4" fill="#0f172a"/>
    <text x="95" y="140" fill="#94a3b8" font-family="system-ui, sans-serif" font-size="9" text-anchor="middle">Surah Fatir 35:38</text>
  </g>

  <!-- Pillar 2: Writing (Kitabah) -->
  <g transform="translate(240, 80)" filter="url(#shadow1)">
    <rect width="190" height="155" rx="10" fill="#1e293b" stroke="#10b981" stroke-width="1.5"/>
    <rect width="190" height="32" rx="10" fill="url(#kitabahGrad)"/>
    <text x="95" y="21" fill="#ffffff" font-family="system-ui, sans-serif" font-size="12" font-weight="700" text-anchor="middle">2. AL-KITABAH (WRITING)</text>
    <text x="15" y="55" fill="#34d399" font-family="system-ui, sans-serif" font-size="10.5" font-weight="700">• Al-Lawh al-Mahfuz</text>
    <text x="15" y="75" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10">• Preserved celestial tablet</text>
    <text x="15" y="95" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10">• Inscribed 50,000 yrs prior</text>
    <text x="15" y="115" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10">• Descriptive, not coercive</text>
    <rect x="15" y="125" width="160" height="22" rx="4" fill="#0f172a"/>
    <text x="95" y="140" fill="#94a3b8" font-family="system-ui, sans-serif" font-size="9" text-anchor="middle">Surah Al-Hadid 57:22</text>
  </g>

  <!-- Pillar 3: Will (Mashee'ah) -->
  <g transform="translate(445, 80)" filter="url(#shadow1)">
    <rect width="190" height="155" rx="10" fill="#1e293b" stroke="#f59e0b" stroke-width="1.5"/>
    <rect width="190" height="32" rx="10" fill="url(#masheeahGrad)"/>
    <text x="95" y="21" fill="#ffffff" font-family="system-ui, sans-serif" font-size="12" font-weight="700" text-anchor="middle">3. AL-MASHEE'AH (WILL)</text>
    <text x="15" y="55" fill="#fbbf24" font-family="system-ui, sans-serif" font-size="10.5" font-weight="700">• Supreme Universal Will</text>
    <text x="15" y="75" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10">• What Allah wills happens</text>
    <text x="15" y="95" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10">• What He wills not cannot be</text>
    <text x="15" y="115" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10">• Encompasses all existence</text>
    <rect x="15" y="125" width="160" height="22" rx="4" fill="#0f172a"/>
    <text x="95" y="140" fill="#94a3b8" font-family="system-ui, sans-serif" font-size="9" text-anchor="middle">Surah At-Takwir 81:29</text>
  </g>

  <!-- Pillar 4: Creation (Khalq) -->
  <g transform="translate(650, 80)" filter="url(#shadow1)">
    <rect width="195" height="155" rx="10" fill="#1e293b" stroke="#8b5cf6" stroke-width="1.5"/>
    <rect width="195" height="32" rx="10" fill="url(#khalqGrad)"/>
    <text x="97" y="21" fill="#ffffff" font-family="system-ui, sans-serif" font-size="12" font-weight="700" text-anchor="middle">4. AL-KHALQ (CREATION)</text>
    <text x="15" y="55" fill="#c084fc" font-family="system-ui, sans-serif" font-size="10.5" font-weight="700">• Sole Creator of Realities</text>
    <text x="15" y="75" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10">• Creator of all entities</text>
    <text x="15" y="95" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10">• Creates human agency</text>
    <text x="15" y="115" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10">• Brings decree into time</text>
    <rect x="15" y="125" width="165" height="22" rx="4" fill="#0f172a"/>
    <text x="97" y="140" fill="#94a3b8" font-family="system-ui, sans-serif" font-size="9" text-anchor="middle">Surah Az-Zumar 39:62</text>
  </g>

  <!-- BOTTOM SECTION: QADAR VS QADHA BRIDGE (Y: 255 to 415) -->
  <g transform="translate(35, 255)" filter="url(#shadow1)">
    <rect width="365" height="155" rx="10" fill="#1e293b" stroke="#0ea5e9" stroke-width="1.5"/>
    <rect width="365" height="32" rx="10" fill="#0369a1"/>
    <text x="182" y="21" fill="#ffffff" font-family="system-ui, sans-serif" font-size="13" font-weight="700" text-anchor="middle">QADAR (THE ETERNAL BLUEPRINT)</text>
    <text x="20" y="55" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="11" font-weight="700">Divine Determination &amp; Pre-Measurement</text>
    <text x="20" y="77" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10.5">• The eternal decree inscribed in the Preserved Tablet</text>
    <text x="20" y="97" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10.5">• Allah's perfect foreknowledge of every outcome</text>
    <text x="20" y="117" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10.5">• Analogy: The complete master code designed by the creator</text>
    <rect x="20" y="128" width="325" height="20" rx="4" fill="#0f172a"/>
    <text x="182" y="142" fill="#fbbf24" font-family="system-ui, sans-serif" font-size="9.5" text-anchor="middle">Example: Allah knew and wrote that it would rain on Monday</text>
  </g>

  <!-- Center Transformation Bridge -->
  <g transform="translate(410, 305)">
    <circle cx="30" cy="25" r="24" fill="#0f172a" stroke="#f59e0b" stroke-width="1.8"/>
    <text x="30" y="21" fill="#fbbf24" font-family="system-ui, sans-serif" font-size="8.5" font-weight="700" text-anchor="middle">EXECUTION</text>
    <text x="30" y="33" fill="#94a3b8" font-family="system-ui, sans-serif" font-size="8" text-anchor="middle">IN TIME</text>
  </g>

  <g transform="translate(480, 255)" filter="url(#shadow1)">
    <rect width="365" height="155" rx="10" fill="#1e293b" stroke="#10b981" stroke-width="1.5"/>
    <rect width="365" height="32" rx="10" fill="#047857"/>
    <text x="182" y="21" fill="#ffffff" font-family="system-ui, sans-serif" font-size="13" font-weight="700" text-anchor="middle">QADHA (THE TEMPORAL MANIFESTATION)</text>
    <text x="20" y="55" fill="#34d399" font-family="system-ui, sans-serif" font-size="11" font-weight="700">The Divine Decision Brought into Physical Reality</text>
    <text x="20" y="77" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10.5">• The actual occurrence of the decreed event in history</text>
    <text x="20" y="97" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10.5">• Brings the written plan into visible physical existence</text>
    <text x="20" y="117" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10.5">• Analogy: The player pressing the button and event taking place</text>
    <rect x="20" y="128" width="325" height="20" rx="4" fill="#0f172a"/>
    <text x="182" y="142" fill="#34d399" font-family="system-ui, sans-serif" font-size="9.5" text-anchor="middle">Example: Rain physically pouring at your school at 10:00 AM</text>
  </g>
</svg>"""


def get_svg_lesson_2():
    """Lesson 3.2.2: The Psychological Shield of Qadar"""
    return """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 880 440" width="100%" height="100%">
  <defs>
    <linearGradient id="bg2" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#0f172a"/>
      <stop offset="50%" stop-color="#1e293b"/>
      <stop offset="100%" stop-color="#0f172a"/>
    </linearGradient>
    <linearGradient id="shieldGrad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#38bdf8"/>
      <stop offset="50%" stop-color="#0284c7"/>
      <stop offset="100%" stop-color="#0369a1"/>
    </linearGradient>
    <linearGradient id="successGrad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#10b981"/>
      <stop offset="100%" stop-color="#059669"/>
    </linearGradient>
    <linearGradient id="trialGrad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#f59e0b"/>
      <stop offset="100%" stop-color="#d97706"/>
    </linearGradient>
    <filter id="shadow2" x="-10%" y="-10%" width="120%" height="120%">
      <feDropShadow dx="0" dy="4" stdDeviation="6" flood-color="#000000" flood-opacity="0.45"/>
    </filter>
  </defs>

  <rect width="880" height="440" fill="url(#bg2)" rx="14"/>
  <rect x="15" y="15" width="850" height="410" fill="none" stroke="#334155" stroke-width="1.5" stroke-dasharray="6 4" rx="10"/>

  <text x="440" y="42" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="17" font-weight="800" text-anchor="middle" letter-spacing="0.5">THE PSYCHOLOGICAL SHIELD OF BELIEF IN QADAR</text>
  <text x="440" y="63" fill="#94a3b8" font-family="system-ui, sans-serif" font-size="12" text-anchor="middle">How Sincere Faith in Divine Decree Transforms All Life Events into Spiritual Elevation (Sahih Muslim 2999)</text>

  <!-- LEFT COLUMN: LIFE EVENTS (INPUTS) -->
  <!-- Success Card -->
  <g transform="translate(35, 85)" filter="url(#shadow2)">
    <rect width="235" height="140" rx="10" fill="#1e293b" stroke="#10b981" stroke-width="1.5"/>
    <rect width="235" height="30" rx="10" fill="url(#successGrad)"/>
    <text x="117" y="20" fill="#ffffff" font-family="system-ui, sans-serif" font-size="12" font-weight="700" text-anchor="middle">LIFE EVENT: SUCCESS &amp; EASE</text>
    <text x="15" y="52" fill="#34d399" font-family="system-ui, sans-serif" font-size="11" font-weight="600">• Academic Excellence &amp; Top Grades</text>
    <text x="15" y="72" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10">• Material Wealth &amp; Health</text>
    <text x="15" y="92" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10">• Athletic Victory &amp; Praise</text>
    <rect x="15" y="105" width="205" height="24" rx="4" fill="#0f172a"/>
    <text x="117" y="121" fill="#ef4444" font-family="system-ui, sans-serif" font-size="9" text-anchor="middle">⚠️ Danger Without Qadar: Arrogance (Kibr)</text>
  </g>

  <!-- Adversity Card -->
  <g transform="translate(35, 245)" filter="url(#shadow2)">
    <rect width="235" height="140" rx="10" fill="#1e293b" stroke="#f59e0b" stroke-width="1.5"/>
    <rect width="235" height="30" rx="10" fill="url(#trialGrad)"/>
    <text x="117" y="20" fill="#ffffff" font-family="system-ui, sans-serif" font-size="12" font-weight="700" text-anchor="middle">LIFE EVENT: ADVERSITY &amp; LOSS</text>
    <text x="15" y="52" fill="#fbbf24" font-family="system-ui, sans-serif" font-size="11" font-weight="600">• Unexpected Illness &amp; Injury</text>
    <text x="15" y="72" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10">• Academic Failure or Misfortune</text>
    <text x="15" y="92" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10">• Loss of Wealth or Plans</text>
    <rect x="15" y="105" width="205" height="24" rx="4" fill="#0f172a"/>
    <text x="117" y="121" fill="#ef4444" font-family="system-ui, sans-serif" font-size="9" text-anchor="middle">⚠️ Danger Without Qadar: Despair (Qu'nut)</text>
  </g>

  <!-- CENTER COLUMN: THE SHIELD FILTER -->
  <g transform="translate(310, 85)" filter="url(#shadow2)">
    <rect width="260" height="300" rx="16" fill="#1e293b" stroke="#38bdf8" stroke-width="2"/>
    <rect width="260" height="36" rx="16" fill="url(#shieldGrad)"/>
    <text x="130" y="24" fill="#ffffff" font-family="system-ui, sans-serif" font-size="13" font-weight="800" text-anchor="middle">THE COGNITIVE SHIELD OF QADAR</text>

    <!-- Center Emblem / Graphic -->
    <circle cx="130" cy="90" r="36" fill="#0f172a" stroke="#f59e0b" stroke-width="2"/>
    <path d="M 130 65 L 155 78 L 155 102 L 130 115 L 105 102 L 105 78 Z" fill="#0284c7" stroke="#38bdf8" stroke-width="1.5"/>
    <text x="130" y="94" fill="#ffffff" font-family="system-ui, sans-serif" font-size="10" font-weight="800" text-anchor="middle">IMAN</text>

    <text x="130" y="145" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="11.5" font-weight="700" text-anchor="middle">Core Paradigm of Faith:</text>
    <text x="130" y="168" fill="#f8fafc" font-family="system-ui, sans-serif" font-size="10.5" text-anchor="middle">"What hit you could never miss you;</text>
    <text x="130" y="184" fill="#f8fafc" font-family="system-ui, sans-serif" font-size="10.5" text-anchor="middle">what missed you could never hit you."</text>

    <line x1="25" y1="202" x2="235" y2="202" stroke="#334155" stroke-width="1"/>

    <text x="130" y="222" fill="#fbbf24" font-family="system-ui, sans-serif" font-size="11" font-weight="700" text-anchor="middle">Mental Health Benefits:</text>
    <text x="25" y="244" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10">✓ Eradicates existential dread &amp; anxiety</text>
    <text x="25" y="262" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10">✓ Replaces regret with purposeful striving</text>
    <text x="25" y="280" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10">✓ Grounds self-worth in Allah's pleasure</text>
  </g>

  <!-- Connective Lines -->
  <line x1="270" y1="155" x2="310" y2="155" stroke="#10b981" stroke-width="2.5" stroke-dasharray="4 2"/>
  <line x1="270" y1="315" x2="310" y2="315" stroke="#f59e0b" stroke-width="2.5" stroke-dasharray="4 2"/>
  <line x1="570" y1="155" x2="610" y2="155" stroke="#34d399" stroke-width="2.5" stroke-dasharray="4 2"/>
  <line x1="570" y1="315" x2="610" y2="315" stroke="#38bdf8" stroke-width="2.5" stroke-dasharray="4 2"/>

  <!-- RIGHT COLUMN: SPIRITUAL TRANSFORMATION (OUTPUTS) -->
  <!-- Shukr Card -->
  <g transform="translate(610, 85)" filter="url(#shadow2)">
    <rect width="235" height="140" rx="10" fill="#1e293b" stroke="#34d399" stroke-width="1.5"/>
    <rect width="235" height="30" rx="10" fill="url(#successGrad)"/>
    <text x="117" y="20" fill="#ffffff" font-family="system-ui, sans-serif" font-size="12" font-weight="700" text-anchor="middle">SHUKR &amp; HUMILITY</text>
    <text x="15" y="52" fill="#34d399" font-family="system-ui, sans-serif" font-size="11" font-weight="600">• Attributing success to Allah</text>
    <text x="15" y="72" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10">• "Alhamdulillah for this blessing"</text>
    <text x="15" y="92" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10">• Generosity toward the needy</text>
    <rect x="15" y="105" width="205" height="24" rx="4" fill="#0f172a"/>
    <text x="117" y="121" fill="#34d399" font-family="system-ui, sans-serif" font-size="9" font-weight="600" text-anchor="middle">🛡️ Shielded from Pride &amp; Ego</text>
  </g>

  <!-- Sabr Card -->
  <g transform="translate(610, 245)" filter="url(#shadow2)">
    <rect width="235" height="140" rx="10" fill="#1e293b" stroke="#38bdf8" stroke-width="1.5"/>
    <rect width="235" height="30" rx="10" fill="url(#shieldGrad)"/>
    <text x="117" y="20" fill="#ffffff" font-family="system-ui, sans-serif" font-size="12" font-weight="700" text-anchor="middle">SABR &amp; TRANQUILITY</text>
    <text x="15" y="52" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="11" font-weight="600">• Peaceful acceptance of the trial</text>
    <text x="15" y="72" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10">• "Qaddarallahu wa ma sha'a fa'al"</text>
    <text x="15" y="92" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10">• Searching for hidden wisdom &amp; reward</text>
    <rect x="15" y="105" width="205" height="24" rx="4" fill="#0f172a"/>
    <text x="117" y="121" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="9" font-weight="600" text-anchor="middle">🛡️ Shielded from Depression &amp; Rage</text>
  </g>

  <!-- Bottom Synthesis Footer -->
  <rect x="35" y="398" width="810" height="24" rx="6" fill="#0f172a" stroke="#334155" stroke-width="1"/>
  <text x="440" y="414" fill="#fbbf24" font-family="system-ui, sans-serif" font-size="10.5" font-weight="700" text-anchor="middle">Hadith: "How amazing is the affair of the believer! All of it is good for him: in ease he gives thanks, and in hardship he shows patience." (Sahih Muslim)</text>
</svg>"""


def get_svg_lesson_3():
    """Lesson 3.2.3: The Trap of "If Only" (Law) vs Sincere Acceptance (Rida)"""
    return """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 880 440" width="100%" height="100%">
  <defs>
    <linearGradient id="bg3" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#0f172a"/>
      <stop offset="50%" stop-color="#1e293b"/>
      <stop offset="100%" stop-color="#0f172a"/>
    </linearGradient>
    <linearGradient id="crimsonGrad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#ef4444"/>
      <stop offset="100%" stop-color="#b91c1c"/>
    </linearGradient>
    <linearGradient id="ridaGrad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#10b981"/>
      <stop offset="100%" stop-color="#047857"/>
    </linearGradient>
    <linearGradient id="triggerGrad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#3b82f6"/>
      <stop offset="100%" stop-color="#1d4ed8"/>
    </linearGradient>
    <filter id="shadow3" x="-10%" y="-10%" width="120%" height="120%">
      <feDropShadow dx="0" dy="4" stdDeviation="5" flood-color="#000000" flood-opacity="0.4"/>
    </filter>
  </defs>

  <rect width="880" height="440" fill="url(#bg3)" rx="14"/>
  <rect x="15" y="15" width="850" height="410" fill="none" stroke="#334155" stroke-width="1.5" stroke-dasharray="6 4" rx="10"/>

  <text x="440" y="42" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="17" font-weight="800" text-anchor="middle" letter-spacing="0.5">THE TRAP OF "IF ONLY" (LAW) VS. SINCERE ACCEPTANCE (RIDA)</text>
  <text x="440" y="63" fill="#94a3b8" font-family="system-ui, sans-serif" font-size="12" text-anchor="middle">Prophetic Cognitive Emotional Intelligence and Theological Resilience (Sahih Muslim 2664)</text>

  <!-- TOP TRIGGER: UNEXPECTED CALAMITY / DISRUPTION -->
  <g transform="translate(240, 78)" filter="url(#shadow3)">
    <rect width="400" height="48" rx="10" fill="#1e293b" stroke="#60a5fa" stroke-width="1.5"/>
    <rect width="400" height="24" rx="10" fill="url(#triggerGrad)"/>
    <text x="200" y="17" fill="#ffffff" font-family="system-ui, sans-serif" font-size="11.5" font-weight="700" text-anchor="middle">TRIGGER EVENT: UNEXPECTED LOSS / PLAN DISRUPTION</text>
    <text x="200" y="39" fill="#e2e8f0" font-family="system-ui, sans-serif" font-size="10.5" text-anchor="middle">Example: Heavy downpour ruins outdoor plans, missed bus, or damaged project</text>
  </g>

  <!-- Diverging Flow Lines -->
  <path d="M 330 126 L 330 148 L 220 148 L 220 160" stroke="#ef4444" stroke-width="2.5" fill="none"/>
  <path d="M 550 126 L 550 148 L 660 148 L 660 160" stroke="#10b981" stroke-width="2.5" fill="none"/>

  <!-- LEFT COLUMN: PATH A — THE TRAP OF "IF ONLY" (LAW) -->
  <g transform="translate(45, 160)" filter="url(#shadow3)">
    <rect width="360" height="225" rx="12" fill="#1e293b" stroke="#ef4444" stroke-width="1.8"/>
    <rect width="360" height="34" rx="12" fill="url(#crimsonGrad)"/>
    <text x="180" y="23" fill="#ffffff" font-family="system-ui, sans-serif" font-size="13" font-weight="800" text-anchor="middle">PATH A: THE TRAP OF "IF ONLY" (LAW)</text>

    <!-- Sub-boxes of Consequences -->
    <rect x="15" y="46" width="330" height="34" rx="6" fill="#0f172a" stroke="#7f1d1d" stroke-width="1"/>
    <text x="25" y="62" fill="#f87171" font-family="system-ui, sans-serif" font-size="10.5" font-weight="700">Utterance:</text>
    <text x="90" y="62" fill="#fecaca" font-family="system-ui, sans-serif" font-size="10.5" font-style="italic">"If only I had done X, this wouldn't have happened!"</text>
    <text x="25" y="74" fill="#94a3b8" font-family="system-ui, sans-serif" font-size="9">Opens the gateway to Satanic whispering (Amal ash-Shaytan)</text>

    <rect x="15" y="88" width="330" height="38" rx="6" fill="#0f172a"/>
    <text x="25" y="104" fill="#f87171" font-family="system-ui, sans-serif" font-size="10" font-weight="600">1. Chronic Regret &amp; Self-Blame</text>
    <text x="25" y="118" fill="#94a3b8" font-family="system-ui, sans-serif" font-size="9">Dwelling on what cannot be changed; cognitive exhaustion</text>

    <rect x="15" y="132" width="330" height="38" rx="6" fill="#0f172a"/>
    <text x="25" y="148" fill="#f87171" font-family="system-ui, sans-serif" font-size="10" font-weight="600">2. Resentment &amp; Projection</text>
    <text x="25" y="162" fill="#94a3b8" font-family="system-ui, sans-serif" font-size="9">Blaming classmates, weather, or circumstances; bitter heart</text>

    <rect x="15" y="176" width="330" height="38" rx="6" fill="#0f172a"/>
    <text x="25" y="192" fill="#f87171" font-family="system-ui, sans-serif" font-size="10" font-weight="600">3. Spiritual Paralysis</text>
    <text x="25" y="206" fill="#94a3b8" font-family="system-ui, sans-serif" font-size="9">Inability to take proactive steps; feeling doomed to fail</text>
  </g>

  <!-- RIGHT COLUMN: PATH B — SINCERE ACCEPTANCE (RIDA) -->
  <g transform="translate(475, 160)" filter="url(#shadow3)">
    <rect width="360" height="225" rx="12" fill="#1e293b" stroke="#10b981" stroke-width="1.8"/>
    <rect width="360" height="34" rx="12" fill="url(#ridaGrad)"/>
    <text x="180" y="23" fill="#ffffff" font-family="system-ui, sans-serif" font-size="13" font-weight="800" text-anchor="middle">PATH B: SINCERE ACCEPTANCE (RIDA)</text>

    <!-- Sub-boxes of Positive Transformation -->
    <rect x="15" y="46" width="330" height="34" rx="6" fill="#0f172a" stroke="#064e3b" stroke-width="1"/>
    <text x="25" y="62" fill="#34d399" font-family="system-ui, sans-serif" font-size="10.5" font-weight="700">Utterance:</text>
    <text x="90" y="62" fill="#a7f3d0" font-family="system-ui, sans-serif" font-size="10.5" font-weight="700">"Qaddarallahu wa ma sha'a fa'al"</text>
    <text x="25" y="74" fill="#94a3b8" font-family="system-ui, sans-serif" font-size="9">"Allah has decreed, and what He wills, He does." (Muslim)</text>

    <rect x="15" y="88" width="330" height="38" rx="6" fill="#0f172a"/>
    <text x="25" y="104" fill="#34d399" font-family="system-ui, sans-serif" font-size="10" font-weight="600">1. Instant Emotional Serenity (Sakinah)</text>
    <text x="25" y="118" fill="#94a3b8" font-family="system-ui, sans-serif" font-size="9">Shuts the door to Satan; heart remains completely calm</text>

    <rect x="15" y="132" width="330" height="38" rx="6" fill="#0f172a"/>
    <text x="25" y="148" fill="#34d399" font-family="system-ui, sans-serif" font-size="10" font-weight="600">2. Objective &amp; Calm Assessment</text>
    <text x="25" y="162" fill="#94a3b8" font-family="system-ui, sans-serif" font-size="9">Analyzes facts without panic; seeks lessons with clarity</text>

    <rect x="15" y="176" width="330" height="38" rx="6" fill="#0f172a"/>
    <text x="25" y="192" fill="#34d399" font-family="system-ui, sans-serif" font-size="10" font-weight="600">3. Constructive Forward Action</text>
    <text x="25" y="206" fill="#94a3b8" font-family="system-ui, sans-serif" font-size="9">Quickly adapts, problem-solves, and executes the next best step</text>
  </g>

  <!-- Bottom Synthesis Bar -->
  <rect x="45" y="395" width="790" height="26" rx="6" fill="#0f172a" stroke="#334155" stroke-width="1"/>
  <text x="440" y="412" fill="#fbbf24" font-family="system-ui, sans-serif" font-size="10.5" font-weight="700" text-anchor="middle">Golden Principle: The past belongs to Allah's decree — The present and future belong to your sincere effort!</text>
</svg>"""


def get_svg_lesson_4():
    """Lesson 3.2.4: Master Synthesis Shield of Divine Decree & Human Agency"""
    return """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 880 440" width="100%" height="100%">
  <defs>
    <linearGradient id="bg4" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#0f172a"/>
      <stop offset="50%" stop-color="#1e293b"/>
      <stop offset="100%" stop-color="#0f172a"/>
    </linearGradient>
    <linearGradient id="rimGrad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#f59e0b"/>
      <stop offset="100%" stop-color="#b45309"/>
    </linearGradient>
    <linearGradient id="coreGrad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#10b981"/>
      <stop offset="100%" stop-color="#047857"/>
    </linearGradient>
    <filter id="shadow4" x="-10%" y="-10%" width="120%" height="120%">
      <feDropShadow dx="0" dy="4" stdDeviation="6" flood-color="#000000" flood-opacity="0.4"/>
    </filter>
  </defs>

  <rect width="880" height="440" fill="url(#bg4)" rx="14"/>
  <rect x="15" y="15" width="850" height="410" fill="none" stroke="#334155" stroke-width="1.5" stroke-dasharray="6 4" rx="10"/>

  <text x="440" y="40" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="17" font-weight="800" text-anchor="middle" letter-spacing="0.5">MASTER SYNTHESIS: THE SHIELD OF DIVINE DECREE &amp; HUMAN AGENCY</text>
  <text x="440" y="60" fill="#94a3b8" font-family="system-ui, sans-serif" font-size="12" text-anchor="middle">Harmonizing Absolute Divine Sovereignty, Human Striving (Tawakkul), and Peaceful Acceptance (Rida)</text>

  <!-- LEFT WING: DEFLECTING CALAMITY -->
  <g transform="translate(35, 80)" filter="url(#shadow4)">
    <rect width="220" height="300" rx="12" fill="#1e293b" stroke="#f59e0b" stroke-width="1.5"/>
    <rect width="220" height="34" rx="12" fill="url(#rimGrad)"/>
    <text x="110" y="22" fill="#ffffff" font-family="system-ui, sans-serif" font-size="12" font-weight="700" text-anchor="middle">INCOMING CALAMITY</text>

    <!-- Arrow striking shield -->
    <path d="M 30 75 L 180 75" stroke="#ef4444" stroke-width="2.5" stroke-dasharray="4 2"/>
    <polygon points="190,75 178,70 178,80" fill="#ef4444"/>
    <text x="110" y="65" fill="#f87171" font-family="system-ui, sans-serif" font-size="10" font-weight="600" text-anchor="middle">Trial, Loss, Injury, Setback</text>

    <!-- Deflection Arc -->
    <rect x="15" y="95" width="190" height="85" rx="8" fill="#0f172a" stroke="#334155" stroke-width="1"/>
    <text x="95" y="115" fill="#34d399" font-family="system-ui, sans-serif" font-size="11" font-weight="700" text-anchor="middle">DEFLECTED AS SABR</text>
    <text x="25" y="135" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="9.5">• No despair or bitter rage</text>
    <text x="25" y="152" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="9.5">• "Qaddarallahu wa ma sha'a fa'al"</text>
    <text x="25" y="169" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="9.5">• Reward for patience earned</text>

    <!-- Summary Box -->
    <rect x="15" y="195" width="190" height="90" rx="8" fill="#0f172a"/>
    <text x="95" y="215" fill="#fbbf24" font-family="system-ui, sans-serif" font-size="10.5" font-weight="700" text-anchor="middle">No "If Only" (Law)</text>
    <text x="25" y="235" fill="#94a3b8" font-family="system-ui, sans-serif" font-size="9">• Shuts the door to Satan</text>
    <text x="25" y="252" fill="#94a3b8" font-family="system-ui, sans-serif" font-size="9">• Protects mental well-being</text>
    <text x="25" y="269" fill="#94a3b8" font-family="system-ui, sans-serif" font-size="9">• Refocuses on forward steps</text>
  </g>

  <!-- CENTER: THE INTEGRATED SHIELD EMBLEM -->
  <g transform="translate(280, 75)" filter="url(#shadow4)">
    <!-- Outer Shield Frame (Divine Sovereignty) -->
    <path d="M 160 10 C 260 10 310 40 310 120 C 310 220 220 280 160 310 C 100 280 10 220 10 120 C 10 40 60 10 160 10 Z" fill="#1e293b" stroke="#f59e0b" stroke-width="3"/>

    <!-- Outer Rim Layer -->
    <text x="160" y="45" fill="#fbbf24" font-family="system-ui, sans-serif" font-size="11" font-weight="800" text-anchor="middle">OUTER RIM: DIVINE SOVEREIGNTY</text>
    <text x="160" y="62" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="9.5" text-anchor="middle">'Ilm (Knowledge) &amp; Kitabah (Preserved Tablet)</text>

    <!-- Middle Field (Human Agency & Tawakkul) -->
    <path d="M 160 75 C 235 75 270 95 270 150 C 270 215 205 255 160 275 C 115 255 50 215 50 150 C 50 95 85 75 160 75 Z" fill="#0f172a" stroke="#0284c7" stroke-width="2"/>
    <text x="160" y="102" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="10.5" font-weight="800" text-anchor="middle">HANDLES: HUMAN AGENCY</text>
    <text x="160" y="118" fill="#94a3b8" font-family="system-ui, sans-serif" font-size="9" text-anchor="middle">Effort, Choice &amp; Accountability</text>

    <!-- Inner Core (Rida & Tuman'ninah) -->
    <circle cx="160" cy="180" r="50" fill="url(#coreGrad)" stroke="#34d399" stroke-width="2"/>
    <text x="160" y="168" fill="#ffffff" font-family="system-ui, sans-serif" font-size="13" font-weight="800" text-anchor="middle">RIDA</text>
    <text x="160" y="184" fill="#a7f3d0" font-family="system-ui, sans-serif" font-size="9" font-weight="700" text-anchor="middle">ACCEPTANCE</text>
    <text x="160" y="198" fill="#ffffff" font-family="system-ui, sans-serif" font-size="8.5" text-anchor="middle">Tuman'ninah</text>

    <text x="160" y="250" fill="#f8fafc" font-family="system-ui, sans-serif" font-size="9" font-weight="700" text-anchor="middle">"Tie Your Camel First, Then Trust Allah"</text>
  </g>

  <!-- RIGHT WING: ABSORBING SUCCESS -->
  <g transform="translate(625, 80)" filter="url(#shadow4)">
    <rect width="220" height="300" rx="12" fill="#1e293b" stroke="#10b981" stroke-width="1.5"/>
    <rect width="220" height="34" rx="12" fill="url(#coreGrad)"/>
    <text x="110" y="22" fill="#ffffff" font-family="system-ui, sans-serif" font-size="12" font-weight="700" text-anchor="middle">INCOMING BLESSING</text>

    <!-- Ray entering shield -->
    <path d="M 190 75 L 40 75" stroke="#34d399" stroke-width="2.5" stroke-dasharray="4 2"/>
    <polygon points="30,75 42,70 42,80" fill="#34d399"/>
    <text x="110" y="65" fill="#34d399" font-family="system-ui, sans-serif" font-size="10" font-weight="600" text-anchor="middle">High Score, Award, Wealth</text>

    <!-- Absorption Arc -->
    <rect x="15" y="95" width="190" height="85" rx="8" fill="#0f172a" stroke="#334155" stroke-width="1"/>
    <text x="95" y="115" fill="#fbbf24" font-family="system-ui, sans-serif" font-size="11" font-weight="700" text-anchor="middle">ABSORBED AS SHUKR</text>
    <text x="25" y="135" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="9.5">• No boastful arrogance (Kibr)</text>
    <text x="25" y="152" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="9.5">• "All praise is due to Allah alone"</text>
    <text x="25" y="169" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="9.5">• Modesty &amp; service to others</text>

    <!-- Summary Box -->
    <rect x="15" y="195" width="190" height="90" rx="8" fill="#0f172a"/>
    <text x="95" y="215" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="10.5" font-weight="700" text-anchor="middle">Tawakkul (Active Trust)</text>
    <text x="25" y="235" fill="#94a3b8" font-family="system-ui, sans-serif" font-size="9">• 100% effort &amp; study</text>
    <text x="25" y="252" fill="#94a3b8" font-family="system-ui, sans-serif" font-size="9">• Zero reliance on self alone</text>
    <text x="25" y="269" fill="#94a3b8" font-family="system-ui, sans-serif" font-size="9">• Full surrender to the outcome</text>
  </g>

  <!-- Bottom Synthesis Banner -->
  <rect x="35" y="395" width="810" height="26" rx="6" fill="#0f172a" stroke="#334155" stroke-width="1"/>
  <text x="440" y="412" fill="#fbbf24" font-family="system-ui, sans-serif" font-size="10.5" font-weight="700" text-anchor="middle">Belief in Qadar = Maximum Ethical Effort (Tawakkul) + Complete Inner Peace (Rida) + Unshakable Character</text>
</svg>"""


# ─── MASTER ENRICHMENT DATA FOR TOPIC 6 (4 LESSONS) ───────────────────────────

LESSONS_DATA = [
    # =========================================================================
    # LESSON 1: Key terms and belief (3.2.1)
    # =========================================================================
    {
        "unit_order": 1,
        "unit_name": "Lesson 3.2.1: Key terms and belief",
        "unit_description": (
            "Exposition of the foundational theological definitions of Qadar (Divine Decree), "
            "Qadha (Divine Decision), and Al-Lawh al-Mahfuz (The Preserved Tablet), alongside "
            "the Four Pillars of Qadar and the harmony between divine decree and human free will."
        ),
        "lesson_title": "Lesson 3.2.1: Key terms and belief",
        "diagram_title": "The Four Pillars of Qadar & Theological Qadar vs Qadha Framework",
        "svg_fn": get_svg_lesson_1,
        "image": {
            "title": "Early Qur'anic Manuscript — Record of Divine Revelation",
            "url": "https://upload.wikimedia.org/wikipedia/commons/5/50/Birmingham_Quran_manuscript.jpg",
            "caption": "An ancient manuscript of the Holy Qur'an, embodying the eternal revealed words of Allah and the recording of divine decrees in Al-Lawh al-Mahfuz.",
            "author": "Classical Islamic Calligrapher",
            "licensing": "Public Domain",
            "source": "Wikimedia Commons"
        },
        "youtube": {
            "title": "Where Was I Before I Was Born? | Why Me? Ep 1 | Dr. Omar Suleiman",
            "youtube_id": "uzE5j2qkFA0",
            "description": "Dr. Omar Suleiman explores the pre-existence of souls, divine knowledge, and how Allah's eternal decree shapes human existence."
        },
        "inquiry_question": "What are the definitions of Qadar and Qadha, and how do we balance divine decree with human free will?",
        "connection": (
            "Imagine a master programmer who designs a highly advanced adventure game. "
            "The programmer writes the entire code, knows every possible path, and has designed "
            "the physical rules of the game (gravity, obstacles, terrain). Yet, when you pick up the "
            "controller, you have the complete freedom to choose where to run, which door to open, "
            "and how to play. You are responsible for your score. This is a helpful analogy for Qadar. "
            "Allah, in His absolute knowledge, has decreed and written everything, yet we retain "
            "free will and are fully responsible for our choices."
        ),
        "goals": [
            "Define the theological terms Qadar, Qadha, and Al-Lawh al-Mahfuz in Islamic belief.",
            "Explain the Four Pillars of Qadar: Knowledge ('Ilm), Writing (Kitabah), Will (Mashee'ah), and Creation (Khalq).",
            "Differentiate between divine pre-recording and human moral accountability."
        ],
        "authoritative_concept": """### Foundational Theological Definitions of Divine Decree

Belief in *Qadar* (Divine Decree) is the Sixth Pillar of *Iman* (Faith) in Islam. It encompasses three interrelated theological realities:

1. **Qadar (Divine Decree):**
   Allah's eternal, timeless knowledge and determination of all events, actions, circumstances, and outcomes in the universe before they occur. Allah has measured and designed everything with perfect proportion (*Taqdir*).

2. **Qadha (Divine Decision / Execution):**
   The actual execution, realization, or physical occurrence of those decreed events in historical time according to Allah's sovereign will. While *Qadar* is the eternal design, *Qadha* is its physical manifestation.

3. **The Preserved Tablet (*Al-Lawh al-Mahfuz*):**
   The sacred, incorruptible celestial record in the heavens where Allah commanded the Pen (*Al-Qalam*) to write everything that will ever transpire across the entire expanse of creation, fifty thousand years before the creation of the heavens and earth.""",
        "scripture_panel": """### Primary Scriptural Foundations for Belief in Qadar

> *"Indeed, Allah is the Knower of the unseen of the heavens and the earth. Indeed, He is Knowing of that within the breasts."*
> — **Surah Fatir (35:38)**

> *"No calamity strikes upon the earth or among yourselves except that it is in a Book before We bring it into being. Indeed that, for Allah, is easy."*
> — **Surah Al-Hadid (57:22)**

> *"The first thing Allah created was the Pen. He said to it: 'Write!' It said: 'What shall I write, my Lord?' He said: 'Write the destinies of all things until the Hour is established.'"*
> — **Prophetic Hadith (Sunan Abu Dawood 4700, Authenticated by Al-Albani)**""",
        "deep_explanation": """### The Four Pillars of Qadar (*Arkan al-Qadar*)

Sunni Islamic orthodoxy identifies four essential, interdependent components that constitute sound belief in *Qadar*:

1. **Knowledge (*Al-'Ilm*):**
   Believing firmly that Allah possesses absolute, all-encompassing knowledge covering the past, present, future, and what never was and how it would have been had it occurred. Nothing in the heavens or earth escapes His infinite awareness.

2. **Writing (*Al-Kitabah*):**
   Believing that Allah recorded all knowledge, lifespans, provisions, deeds, and destinies in the Preserved Tablet (*Al-Lawh al-Mahfuz*). This recording is descriptive—documenting what humans would freely choose—rather than coercive compulsion.

3. **Will (*Al-Mashee'ah*):**
   Believing that Allah's sovereign universal will is absolute: whatever Allah wills comes to pass without delay, and whatever He does not will can never exist. Human free will operates within the overarching domain of Allah's sovereign permission.

4. **Creation (*Al-Khalq*):**
   Believing that Allah is the sole, undisputed Creator of all things, including physical entities, the laws of nature, and the human capacity to intend, choose, and execute actions.""",
        "comparison_table": {
            "title": "Comparative Theological Analysis: Qadar vs Qadha",
            "headers": ["Dimension", "Qadar (The Eternal Blueprint)", "Qadha (The Execution in Time)"],
            "rows": [
                ["Theological Definition", "Allah's eternal pre-measurement, determination, and knowledge before creation", "The physical bringing into existence and execution of that decree in time"],
                ["Temporal Aspect", "Eternal, timeless, inscribed before the creation of the universe", "Historical, temporal, occurring at a specific moment in space and time"],
                ["Celestial Record", "Inscribed upon Al-Lawh al-Mahfuz (The Preserved Tablet)", "Manifested in the created physical realm and historical events"],
                ["Pedagogical Analogy", "The master architectural blueprint and structural specifications", "The actual construction and physical standing of the completed building"],
                ["Concrete Example", "Allah knew and recorded that rain would fall on your school on Monday", "The raindrops physically falling on the school courtyard at 10:00 AM on Monday"]
            ]
        },
        "worked_example": {
            "title": "Relatable Student Scenario: Yusuf and the Studying Dilemma",
            "scenario": (
                "During a lively classroom discussion on predestination, a student named Yusuf raises his hand "
                "and poses an honest question to his teacher, Mr. Bilal: 'If Allah has already written whether I will pass "
                "or fail my final Grade 9 examinations in the Preserved Tablet, why should I spend late nights revising "
                "and studying? Isn't my final grade already predetermined?'"
            ),
            "analysis": (
                "Mr. Bilal offers a profound, clarifying response: 'Yusuf, this is among the most widespread misunderstandings "
                "about Qadar. Allah's pre-writing represents His infinite, perfect foreknowledge of your future choices—not coercive force. "
                "If you decide to neglect your books, sleep through your classes, and fail, that failure is the direct consequence "
                "of your free choice, for which you are accountable. If you choose to study diligently, review past papers, and pass "
                "with honors, that was also your choice. Allah recorded the outcome because He knew in advance what you would freely choose, "
                "not because He forced you. Therefore, study with maximum dedication and choose academic excellence!'"
            ),
            "takeaway": "Divine pre-recording is descriptive of human choices, not a constraint that robs us of moral agency. Human effort is the means through which Allah decrees success."
        },
        "real_world_application": (
            "Never use Qadar as a philosophical excuse for laziness, undisciplined habits, or bad choices. "
            "When faced with academic tasks or personal responsibilities, exercise your full free will and moral agency. "
            "If you make an error or fall short, do not deflect responsibility by saying 'It was my Qadar to fail.' "
            "Instead, take full ownership, seek Allah's forgiveness (Tawbah), analyze your missteps, and resolve to make "
            "disciplined, righteous choices moving forward."
        ),
        "reflection": (
            "How does knowing that Allah possesses perfect foreknowledge of your entire future protect you from "
            "debilitating anxiety about tomorrow? Why is genuine human free will essential for the justice of the Day of Judgment?"
        ),
        "misconception": {
            "misconception": "Because Allah wrote all destinies in advance in Al-Lawh al-Mahfuz, humans are merely helpless puppets forced to commit sins or experience failures against their will.",
            "correction": "Allah's writing reflects His eternal foreknowledge of what we would freely choose with our own volition. A teacher who knows an unprepared student will fail an exam does not cause the failure; similarly, Allah's knowledge records our voluntary actions without coercing them."
        },
        "mcq": {
            "question": "What is the correct theological definition of the term Al-Lawh al-Mahfuz in Islamic belief?",
            "options": [
                "A) The physical scale (Mizan) used to weigh deeds on the Day of Resurrection.",
                "B) The traverse bridge (As-Sirat) spanning over Hellfire leading into Paradise.",
                "C) The Preserved Tablet in the heavens where Allah wrote all decrees and destinies before creation.",
                "D) The assembly plain (Al-Mahshar) where all of humanity gathers for judgment."
            ],
            "answer": "C",
            "correct_answer": "C",
            "explanation": "Al-Lawh al-Mahfuz is the sacred Preserved Tablet in the heavens in which Allah recorded the divine decree, measures, and destinies of all created entities before creating the universe."
        },
        "summary": {
            "key_points": [
                "Qadar is Allah's eternal decree and foreknowledge; Qadha is the temporal execution and occurrence of that decree.",
                "Sound belief in Qadar rests upon four indispensable pillars: Knowledge ('Ilm), Writing (Kitabah), Will (Mashee'ah), and Creation (Khalq).",
                "Divine pre-recording in Al-Lawh al-Mahfuz is descriptive foreknowledge and does not negate human free will or personal accountability."
            ],
            "vocabulary": [
                {"term": "Qadar", "definition": "Allah's eternal decree, measure, and foreknowledge of all things before they exist."},
                {"term": "Qadha", "definition": "The execution, implementation, or physical occurrence of the decreed event in time."},
                {"term": "Al-Lawh al-Mahfuz", "definition": "The celestial Preserved Tablet containing the comprehensive written record of creation."},
                {"term": "Al-Mashee'ah", "definition": "Allah's absolute, sovereign universal will that governs all reality."}
            ]
        },
        "exit_ticket": "State the four foundational pillars of belief in Qadar in your own words and explain how human free will remains intact alongside divine decree."
    },

    # =========================================================================
    # LESSON 2: Effects of belief (3.2.2)
    # =========================================================================
    {
        "unit_order": 2,
        "unit_name": "Lesson 3.2.2: Effects of belief",
        "unit_description": (
            "Investigation of the profound psychological and spiritual benefits of believing in Qadar, "
            "specifically analyzing how it cultivates patience in adversity (Sabr), humility in success (Shukr), "
            "and emotional tranquility while guarding against arrogance (Kibr) and despair (Qu'nut)."
        ),
        "lesson_title": "Lesson 3.2.2: Effects of belief",
        "diagram_title": "The Psychological Shield of Qadar: Cognitive Filter of Faith",
        "svg_fn": get_svg_lesson_2,
        "image": {
            "title": "Pilgrims at the Sacred Kaaba in Mecca",
            "url": "https://upload.wikimedia.org/wikipedia/commons/7/79/The_Kaaba_during_Hajj.jpg",
            "caption": "Believers gathered at the Holy Kaaba in Mecca, demonstrating spiritual surrender, patience, and gratitude in every life condition.",
            "author": "Classical Heritage",
            "licensing": "Creative Commons Attribution-Share Alike",
            "source": "Wikimedia Commons"
        },
        "youtube": {
            "title": "Why Did Allah Choose This Time for Me? | Why Me? Ep 2 | Dr. Omar Suleiman",
            "youtube_id": "5hDUB6yFwBQ",
            "description": "Dr. Omar Suleiman explains how trusting divine decree removes existential envy and despair, helping believers recognize the wisdom in their personal life circumstances."
        },
        "inquiry_question": "What are the psychological and spiritual benefits of believing in Qadar, and how does it prevent arrogance and despair?",
        "connection": (
            "Imagine a ship sailing across a vast, unpredictable ocean. Suddenly, a massive storm hits, "
            "with giant waves crashing against the deck. A passenger who does not trust the captain will panic, "
            "scream, and fall into deep despair. But a passenger who knows that the captain is highly experienced, "
            "has a perfect nautical map, and is fully in control of the ship will remain calm, patient, and helpful, "
            "trusting that they will reach the harbor safely. In our lives, believing in Qadar is what keeps our hearts "
            "calm and steady through the storms of life."
        ),
        "goals": [
            "Analyze the twin psychological fruits of Qadar: Patience in adversity (Sabr) and Humility in success (Shukr).",
            "Explain how belief in divine decree shields the mind from destructive pride (Kibr) and hopeless despair (Qu'nut).",
            "Implement the practical 'Decree Protocol' (Qaddarallahu wa ma sha'a fa'al) in response to unexpected daily disruptions."
        ],
        "authoritative_concept": """### The Psychological & Spiritual Transformation of Qadar

Belief in *Qadar* is not merely an intellectual creed; it is a profound cognitive and spiritual defense mechanism that shapes human temperament and mental health:

1. **Patience in Adversity (*Sabr*):**
   When facing grief, illness, financial loss, or personal setbacks, the believer does not succumb to existential rage or depression. Knowing that trials are decreed by Allah with infinite underlying wisdom enables the heart to maintain emotional composure, resilience, and hope.

2. **Humility in Success (*Tawadu'* & *Shukr*):**
   When achieving extraordinary academic, athletic, or social success, the believer is protected from arrogance (*Kibr*). Recognizing that intelligence, health, and favorable circumstances are divine gifts keeps the soul humble, attributing all blessings to Allah (*Alhamdulillah*).

3. **Emotional Stability (*Sakinah*):**
   By anchoring the self to divine wisdom, the believer experiences deep tranquility, immune to the wild oscillations between manic arrogance in ease and suicidal despair in hardship.""",
        "scripture_panel": """### Scriptural Foundations for Patience and Gratitude

> *"And We will surely test you with something of fear and hunger and a loss of wealth and lives and fruits, but give good tidings to the patient—who, when disaster strikes them, say, 'Indeed we belong to Allah, and indeed to Him we will return.'"*
> — **Surah Al-Baqarah (2:155–156)**

> *"How amazing is the affair of the believer! Verily, all of his affairs are good for him, and this is for none except a believer. If something pleasant befalls him, he is grateful (Shukr), and that is good for him; and if something harmful befalls him, he is patient (Sabr), and that is good for him."*
> — **Prophetic Hadith (Sahih Muslim, 2999)**""",
        "deep_explanation": """### Three Major Mental Health & Spiritual Shields of Qadar

The cognitive filter of *Qadar* produces three transformative mental outcomes:

1. **Protection from Arrogance (*Kibr*):**
   When a student scores top grades, the unanchored mindset often thinks, *"I achieved this solely through my superior brilliance and work ethic."* This arrogance breeds condescension toward others. In contrast, the believer says, *"Alhamdulillah! Allah blessed me with memory, health, supportive teachers, and clarity on exam day."* This produces humility, empathy, and social gratitude.

2. **Protection from Hopeless Despair (*Qu'nut*):**
   When sudden tragedies or failures occur, the secular mindset often spirals into nihilism: *"Why me? Why is the world so cruel and meaningless?"* The believer recognizes that this world is a testing ground (*Dar al-Ibtila*), and that every difficulty carries expiation of sins, character refinement, and future reward that far exceeds the temporary pain.

3. **High Hope & Fearless Endeavor:**
   Knowing that sustenance (*Rizq*) and lifespan (*Ajal*) are decreed entirely by Allah frees the believer from debilitating fear of people, poverty, or future uncertainties. One works with 100% courage, focusing on ethical striving while leaving the ultimate outcome in the hands of the Most Merciful.""",
        "comparison_table": {
            "title": "Cognitive Response Matrix: Secular Mindset vs Mindset Grounded in Qadar",
            "headers": ["Life Circumstance", "Secular / Unanchored Mindset", "Mindset Grounded in Qadar (Shield of Iman)", "Spiritual & Psychological Fruit"],
            "rows": [
                ["Outstanding Achievement / Wealth", "Arrogance & Vanity: 'I earned this by my own power and genius.'", "Gratitude & Humility: 'This is an unearned blessing from Allah's grace.'", "Modesty, generosity, and protection from pride (Kibr)"],
                ["Sudden Failure / Serious Injury", "Existential Despair: 'My life is ruined; why did fate curse me?'", "Patience & Trust: 'Allah decreed this with wisdom; my effort is rewarded.'", "Resilience, emotional calm, and expiation of sins"],
                ["Uncertain Future / Upcoming Crisis", "Paralyzing Anxiety: Constantly dreading uncontrollable variables", "Active Tawakkul: 'I prepare my best; what Allah wills is best for me.'", "Fearless purpose, focused action, and inner peace (Sakinah)"]
            ]
        },
        "worked_example": {
            "title": "Relatable Student Scenario: Zainab's Championship Fall",
            "scenario": (
                "Zainab has trained rigorously for three grueling months for the inter-school athletics championship. "
                "During the final 100-meter sprint, with the finish line in sight, she slips on a patch of wet grass, "
                "severely spraining her ankle and crossing the line in last place. Devastated, in tears and physical pain, "
                "she cries out: 'All my sweat, discipline, and training were completely wasted!' Her friend Halima sits beside "
                "her, wraps a comforting arm around her, and says: 'Zainab, please do not say your effort was wasted. "
                "In the sight of Allah, every stride of your training and every ounce of your dedication was recorded and rewarded. "
                "Slipping on the grass was decreed by Allah in Al-Lawh al-Mahfuz, containing a wisdom and protection we cannot "
                "currently perceive. Be patient, say Alhamdulillah, and trust His plan. Your hard work built your character, "
                "and Allah will elevate your rank for your Sabr.'"
            ),
            "analysis": (
                "Halima applies the Islamic cognitive reframe of Qadar to a sudden crisis. By separating human striving "
                "(which is never lost before Allah) from worldly outcomes (which are governed by divine decree), she transforms "
                "a devastating athletic defeat from meaningless misery into a spiritually enriching crucible for patience "
                "and character refinement."
            ),
            "takeaway": "No sincere striving is ever wasted. When unexpected physical setbacks disrupt our goals, Sabr reframes the loss into spiritual elevation and enduring strength."
        },
        "real_world_application": (
            "Implement the 'Decree Protocol' this week. Whenever any disruption, setback, or irritation occurs—whether you "
            "miss a bus, misplace your favorite pen, receive a disappointing mark on an assignment, or have weekend sports "
            "canceled by rain—strictly prohibit yourself from complaining, venting anger, or cursing time. Instantly whisper "
            "the prophetic phrase: 'Qaddarallahu wa ma sha'a fa'al' (Allah has decreed, and what He wills, He does). "
            "Observe how this cognitive affirmation instantly arrests stress hormones, steadies your heartbeat, and restores mental clarity."
        ),
        "reflection": (
            "Why do individuals who lack belief in divine decree frequently suffer from debilitating anxiety regarding "
            "future events? How does practicing active gratitude during times of success protect you from looking down on peers who struggle?"
        ),
        "misconception": {
            "misconception": "Believing in Qadar breeds a passive, indifferent personality that lacks competitive drive or passion for excellence.",
            "correction": "Belief in Qadar produces the most resilient, courageous strivers. Knowing that failure cannot destroy one's ultimate destiny removes the paralyzing fear of failure, liberating the believer to pursue noble goals with total dedication."
        },
        "mcq": {
            "question": "According to the authentic Hadith in Sahih Muslim (2999), why is the overall situation of a believer uniquely described as 'amazing'?",
            "options": [
                "A) Because believers are completely exempted from experiencing any illness, poverty, or worldly trials.",
                "B) Because believers are miraculously guaranteed immediate worldly wealth whenever they make supplication.",
                "C) Because believers respond to prosperity with gratitude (Shukr) and adversity with patience (Sabr), making every outcome beneficial.",
                "D) Because believers possess supernatural insight allowing them to foresee future decrees in advance."
            ],
            "answer": "C",
            "correct_answer": "C",
            "explanation": "The Prophet (PBUH) explained that the affair of the believer is extraordinary because they derive spiritual benefit and reward from every life situation: blessings inspire gratitude, while hardship inspires patience."
        },
        "summary": {
            "key_points": [
                "Belief in Qadar acts as a psychological shield, preventing arrogance during success and despair during trials.",
                "The believer navigates life through twin spiritual responses: Gratitude (Shukr) in prosperity and Patience (Sabr) in adversity.",
                "Trusting that all occurrences unfold according to divine wisdom provides profound psychological resilience and mental peace."
            ],
            "vocabulary": [
                {"term": "Sabr", "definition": "Patience, fortitude, and emotional restraint in the face of difficulties."},
                {"term": "Shukr", "definition": "Gratitude and thanksgiving expressed to Allah in heart, speech, and deeds."},
                {"term": "Kibr", "definition": "Arrogance and excessive pride in oneself, looking down upon others."},
                {"term": "Qu'nut", "definition": "Despair and loss of hope in Allah's mercy and wisdom."}
            ]
        },
        "exit_ticket": "Recall a time in your life when an unexpected setback or disappointment occurred, which later revealed itself to be a blessing in disguise. Explain how that experience illustrates belief in Qadar."
    },

    # =========================================================================
    # LESSON 3: Significance and acceptance (3.2.3)
    # =========================================================================
    {
        "unit_order": 3,
        "unit_name": "Lesson 3.2.3: Significance and acceptance",
        "unit_description": (
            "Examination of the theological and psychological significance of accepting divine will (Rida), "
            "analyzing the spiritual dangers of saying 'If only' (Law), and studying the prophetic remedy for regret."
        ),
        "lesson_title": "Lesson 3.2.3: Significance and acceptance",
        "diagram_title": "The Trap of 'If Only' (Law) vs Sincere Acceptance (Rida)",
        "svg_fn": get_svg_lesson_3,
        "image": {
            "title": "Tranquil Courtyard of the Prophet's Mosque in Medina",
            "url": "https://upload.wikimedia.org/wikipedia/commons/c/c6/Al_Masjid_An_Nabawi.jpg",
            "caption": "The serene, light-filled courtyard of Al-Masjid an-Nabawi in Medina, embodying the tranquility (Sakinah) and spiritual contentment (Rida) born of trust in Allah.",
            "author": "Wikimedia Commons Contributor",
            "licensing": "Creative Commons Attribution-Share Alike",
            "source": "Wikimedia Commons"
        },
        "youtube": {
            "title": "What If I Could've Changed Things? | Why Me? Ep 18 | Dr. Omar Suleiman",
            "youtube_id": "c-ppIM94ilw",
            "description": "Dr. Omar Suleiman addresses the paralyzing trap of counterfactual regret ('What if?'), teaching how to find peace through Islamic acceptance and forward-focused striving."
        },
        "inquiry_question": "How does accepting the Will of Allah bring complete peace of mind, and what is the danger of saying 'If only'?",
        "connection": (
            "Have you ever spent days planning a beautiful outdoor picnic or sports tournament, only for a massive, "
            "unpredicted thunderstorm to pour torrential rain the moment you arrive? No matter how loudly you scream, "
            "how angry you become, or how hard you stamp your feet, you cannot order the clouds to stop raining. "
            "You have two distinct choices: spend your day soaked, furious, and bitter, ruining the day for yourself "
            "and everyone around you, or accept the rain as Allah's decree, smile, move your gathering indoors, "
            "and enjoy the unexpected blessings of the moment. In this lesson, we discover the profound spiritual power "
            "of Acceptance (*Rida*) and the dangerous psychological trap of dwelling on 'If only'."
        ),
        "goals": [
            "Define the station of Acceptance (*Rida*) and differentiate it from defeatist passivity.",
            "Identify the spiritual and cognitive dangers of uttering 'If only' (*Law*) after an event has passed.",
            "Internalize the prophetic guidance on maintaining emotional peace and constructive problem-solving."
        ],
        "authoritative_concept": """### The Spiritual Station of Acceptance (*Rida*) and the Trap of *Law*

In Islamic spirituality, emotional serenity in the face of uncontrollable circumstances rests upon two key principles:

1. **Acceptance (*Rida bi-Qada'illah*):**
   *Rida* is the sublime spiritual state wherein the believer's heart is completely at peace with Allah's decree. Rather than merely enduring hardship with clenched teeth, the person possessing *Rida* rests in the certainty that Allah is the All-Wise (*Al-Hakim*) and the Most Merciful (*Ar-Rahim*), knowing that behind every apparent misfortune lies divine benevolence.

2. **The Hazard of Counterfactual Regret (*Law* / 'If Only'):**
   In Arabic, using the particle *Law* ('If only I had done such-and-such...') to express sorrow or defiance over a completed event is spiritually destructive. It implies the irrational belief that human maneuvering could have overturned divine destiny, which opens the psychological gateway to Satanic whispering (*Waswas*), chronic self-torment, and bitterness.""",
        "scripture_panel": """### Scriptural Foundations for Contentment and Avoiding 'If Only'

> *"Say, 'Indeed, my prayer, my rites of sacrifice, my living and my dying are for Allah, Lord of the worlds. No partner has He. And this I have been commanded, and I am the first of the Muslims.'"*
> — **Surah Al-An'am (6:162–163)**

> *"Strive for that which benefits you, seek help from Allah, and do not lose heart. If something befalls you, do not say: 'If only I had done such-and-such, then such-and-such would have happened!' Rather, say: 'Qaddarallahu wa ma sha'a fa'al' (Allah has decreed, and what He wills, He does). For indeed, saying 'If only' (Law) opens the work of Satan."*
> — **Prophetic Hadith (Sahih Muslim, 2664)**""",
        "deep_explanation": """### Why 'If Only' Is a Mental and Spiritual Poison

Islamic pedagogy identifies three critical reasons why dwelling on 'If only' harms the human mind and soul:

1. **Closing the Door to Satan (*Bab ash-Shaytan*):**
   Satan exploits regret to drive human beings toward despair and defiance against Allah. By repeatedly replaying counterfactual fantasies (*'If only I hadn't taken that street...', 'If only I hadn't answered that question differently...'*), Satan whispers that Allah's decree was flawed or cruel, poisoning the believer's love for their Creator.

2. **Active Acceptance vs Fatalistic Passivity:**
   *Rida* does **not** mean being passive or refusing to take precautions. The Islamic model demands 100% lawful planning, preparation, and striving *before* an event occurs. However, once an outcome is finalized and outside human control, energy must immediately shift from regret to serene acceptance.

3. **The Neurological Power of 'Qaddarallahu':**
   Uttering the prophetic formula, *"Allah has decreed, and what He wills, He does,"* halts the destructive cognitive loop of rumination. It grounds the conscious mind in present reality, releasing emotional stress and liberating cognitive resources for proactive problem-solving.""",
        "comparison_table": {
            "title": "Behavioral Breakdown: The Trap of 'If Only' vs The Sanctuary of Rida",
            "headers": ["Evaluation Metric", "Reaction A: The Trap of 'If Only' (Law)", "Reaction B: Sincere Acceptance (Rida)"],
            "rows": [
                ["Initial Verbal Formula", "'If only I had taken that other bus / revised that topic!'", "'Qaddarallahu wa ma sha'a fa'al (Allah has decreed; His will is done).'"],
                ["Cognitive Focus", "Trapped in an unchangeable past; endless self-blame and 'what ifs'", "Firmly anchored in the present reality and future constructive actions"],
                ["Satanic Vulnerability", "Opens wide the door for Satanic whisperings, bitterness, and anger", "Slams shut the door to Satan; envelops the heart in divine tranquility"],
                ["Interpersonal Impact", "Blames partners, family, or teachers; projects frustration onto others", "Remains pleasant, forgiving, and supportive toward peers and family"],
                ["Long-Term Mindset", "Chronic cynicism, resentment, and fear of making future decisions", "Continuous spiritual growth, emotional resilience, and deep optimism"]
            ]
        },
        "worked_example": {
            "title": "Relatable Student Scenario: Ibrahim, Hussein, and the Sudden Downpour",
            "scenario": (
                "Ibrahim and Hussein are walking home together from school carrying their backpacks and homework folders. "
                "Without any warning, dark storm clouds roll in and a heavy tropical downpour begins, soaking their uniforms "
                "within seconds. Hussein is enraged; he stamps his feet in puddles, throws his hands up, and angrily shouts: "
                "'If only we had walked out five minutes earlier! If only we hadn't stopped to chat with Faruq! Now our "
                "afternoon is completely ruined and our books are wet!' Ibrahim laughs gently, takes Hussein by the arm, "
                "and leads him under a large shop awning: 'Hussein, my dear brother, shouting at the rain will not dry our "
                "uniforms. Neither you nor I could see the future five minutes ago. Say: Qaddarallahu wa ma sha'a fa'al. "
                "Look how fresh the air smells, and how the plants are drinking the water. Getting angry at the weather "
                "is like getting angry at Allah's plan. Let's dry our folders, enjoy the breeze, and head home once the rain eases.' "
                "Hussein chuckles, takes a deep breath, and admits: 'You are right, Ibrahim. Alhamdulillah.'"
            ),
            "analysis": (
                "Hussein's instinctive reaction demonstrates the spiral of 'If only'—pointless counterfactual regret that generates "
                "anger and blames innocent events. Ibrahim exemplifies Rida: immediate acceptance of divine decree, reframing the disruption "
                "with positivity, and taking practical shelter without emotional distress."
            ),
            "takeaway": "Regret over what has already occurred cannot alter past events; it only robs you of present peace. Sincere acceptance restores joy and clarity."
        },
        "real_world_application": (
            "Undertake the '48-Hour No \"If Only\" Challenge.' Over the next two days, banish the phrases 'If only...', "
            "'I should have...', and 'Why did this have to happen?' entirely from your vocabulary. Whenever an unexpected mishap "
            "occurs—a broken glass, a canceled plan, a dropped score, or a sprained finger—immediately recite aloud: "
            "'Qaddarallahu wa ma sha'a fa'al.' Consciously observe how this single conscious habit protects your emotional calm "
            "and boosts your mental clarity."
        ),
        "reflection": (
            "Why does the phrase 'If only' act as an invitation for Satanic whisperings? In what ways does dedicating our entire "
            "living and dying to Allah (as stated in Surah Al-An'am) make unexpected life changes easier to embrace?"
        ),
        "misconception": {
            "misconception": "Saying 'If only' is a harmless, normal human reaction that simply demonstrates that you care about high standards.",
            "correction": "While analyzing errors to plan future improvements is healthy, using 'If only' with emotional bitterness implies that you believe human effort could have thwarted Allah's decree. Islam teaches constructive forward reflection ('Next time I will...') rather than bitter backward lamentation."
        },
        "mcq": {
            "question": "What did Prophet Muhammad (PBUH) specifically command believers to say when an unexpected difficulty or trial strikes, rather than saying 'If only'?",
            "options": [
                "A) 'This is completely unfair and my hard work has been ruined forever.'",
                "B) 'If only I had planned more carefully, this trial would have been averted.'",
                "C) 'Qaddarallahu wa ma sha'a fa'al (Allah has decreed, and what He wills, He does).'",
                "D) 'I renounce this action and will never undertake another effort of this kind.'"
            ],
            "answer": "C",
            "correct_answer": "C",
            "explanation": "In Sahih Muslim (2664), the Prophet (PBUH) commanded believers to avoid saying 'If only' and instead declare: 'Qaddarallahu wa ma sha'a fa'al' to terminate regret and affirm trust in Allah's sovereignty."
        },
        "summary": {
            "key_points": [
                "Sincere acceptance (*Rida*) brings complete tranquility, emotional balance, and spiritual contentment.",
                "Saying 'If only' (*Law*) is a spiritual hazard that invites Satanic whisperings, despair, and futile bitterness.",
                "True acceptance balances proactive, lawful human striving before the event with peaceful surrender to the outcome after it occurs."
            ],
            "vocabulary": [
                {"term": "Rida", "definition": "Complete spiritual contentment and peace of heart with Allah's divine decree."},
                {"term": "Law", "definition": "The Arabic conditional 'If' or 'If only', prohibited when used to express regret over decrees."},
                {"term": "Qaddarallahu wa ma sha'a fa'al", "definition": "'Allah has decreed, and what He wills, He does' — the prophetic shield against regret."},
                {"term": "Waswas", "definition": "Subtle evil whisperings and doubts cast into the heart by Satan."}
            ]
        },
        "exit_ticket": "In one concise sentence, explain why saying 'If only' cannot reverse past occurrences and how the prophetic phrase restores immediate mental peace."
    },

    # =========================================================================
    # LESSON 4: Unit synthesis (3.2.4)
    # =========================================================================
    {
        "unit_order": 4,
        "unit_name": "Lesson 3.2.4: Unit synthesis",
        "unit_description": (
            "Master consolidation of Strand 3.2 on Belief in Qadar, synthesizing the Four Pillars, "
            "human moral agency, the psychological Shield of Qadar, and practical integration in daily character."
        ),
        "lesson_title": "Lesson 3.2.4: Unit synthesis",
        "diagram_title": "Master Synthesis Shield: Divine Decree, Human Agency & Tawakkul",
        "svg_fn": get_svg_lesson_4,
        "image": {
            "title": "Historic Carved Portal of the Prophet's Mosque",
            "url": "https://upload.wikimedia.org/wikipedia/commons/7/73/Al-Masjid_AL-Nabawi_Door.jpg",
            "caption": "The magnificent, fortified portal of the Prophet's Mosque in Medina, symbolizing the spiritual fortress and enduring shield of faith in Allah's decree.",
            "author": "Wikimedia Commons Contributor",
            "licensing": "Creative Commons Attribution-Share Alike",
            "source": "Wikimedia Commons"
        },
        "youtube": {
            "title": "Do Good Deeds Extend My Life? | Divine Decree & Human Action | Dr. Omar Suleiman",
            "youtube_id": "ojt8FtaSVr4",
            "description": "Dr. Omar Suleiman explains the synthesis of divine pre-recording, supplication (Dua), and human action, clarifying how deeds harmonize with eternal decree."
        },
        "inquiry_question": "How do we consolidate our understanding of Qadar, Qadha, and their practical implications on our character?",
        "connection": (
            "Imagine you have spent weeks in a master forge crafting a custom-built, heavy-duty shield. "
            "You have forged the strong iron rim, shaped the protective midfield, polished the bronze emblem at the core, "
            "and attached comfortable, durable leather straps for your forearm. In this final capstone lesson of our unit, "
            "we strap this spiritual 'Shield of Qadar' securely onto our arms. We consolidate the definitions, the Four Pillars, "
            "the psychological defenses of Sabr and Shukr, and the dismissal of regret, ensuring we are fully prepared "
            "to navigate any storm life sends our way with unshakeable dignity and peace."
        ),
        "goals": [
            "Synthesize all core concepts: Qadar, Qadha, Al-Lawh al-Mahfuz, and the Four Pillars of Decree.",
            "Harmonize absolute divine sovereignty with genuine human moral responsibility and free will.",
            "Embody the comprehensive character fruits of Qadar: Humility in triumph, resilience in calamity, and deep inner peace (Tuman'ninah)."
        ],
        "authoritative_concept": """### Master Synthesis: The Complete Architecture of Faith in Qadar

Sound Islamic theology integrates divine sovereignty with human agency into a seamless, unified worldview:

1. **The Shield of Qadar:**
   The spiritual and psychological armor that protects the believer on all sides. It deflects the arrows of calamity as patient perseverance (*Sabr*), and absorbs the light of triumph as grateful humility (*Shukr*), preventing both pride and despair.

2. **Inner Tranquility (*Tuman'ninah*):**
   The profound stillness of heart that arises when an individual knows with certainty that the universe is not random chaos, but a meticulously governed creation where every hardship has purpose and every blessing carries responsibility.

3. **Authentic Tawakkul (Trust with Striving):**
   The indispensable balance between tying one's camel (exerting maximum lawful human effort) and placing ultimate reliance in Allah (surrendering the final result to divine will).""",
        "scripture_panel": """### Master Scriptural Anchor for the Synthesis of Qadar

> *"Say, 'Indeed, my prayer, my rites of sacrifice, my living and my dying are for Allah, Lord of the worlds. No partner has He. And this I have been commanded, and I am the first of the Muslims.'"*
> — **Surah Al-An'am (6:162–163)**

> *"A man asked the Prophet (PBUH): 'O Messenger of Allah, should I tie my camel and rely upon Allah, or should I leave it loose and rely upon Allah?' The Prophet (PBUH) replied: 'Tie your camel first, then rely upon Allah (Tawakkul).'"*
> — **Prophetic Hadith (Sunan at-Tirmidhi, 2517, Hasan)**""",
        "deep_explanation": """### The Comprehensive Synthesis Map of Belief in Qadar

To achieve mastery in this unit, remember the four harmonized dimensions of the Shield:

1. **The Divine Grounding (The Four Pillars):**
   - **Knowledge (*'Ilm*):** Allah eternally knows all things.
   - **Writing (*Kitabah*):** Recorded in the Preserved Tablet (*Al-Lawh al-Mahfuz*).
   - **Will (*Mashee'ah*):** Nothing exists except by Allah's sovereign will.
   - **Creation (*Khalq*):** Allah alone brings every entity and action into existence.

2. **The Human Operational Dimension (Agency & Accountability):**
   Allah granted humans intellect, conscience, and free will. We choose our actions and bear full responsibility. Qadar is never a defense for crime, sin, or academic laziness.

3. **The Cognitive Deflector (No 'If Only'):**
   When uncontrollable setbacks strike, the believer instantly shuts the door to Satan by reciting *Qaddarallahu wa ma sha'a fa'al*, preserving emotional energy for proactive adaptation.

4. **The Character Outcomes (Sabr, Shukr, & Tuman'ninah):**
   Life's dual currents—prosperity and adversity—both yield spiritual victory, making the believer mentally invincible and spiritually serene.""",
        "step_process": {
            "title": "The Four Integrated Steps to Mastering the Shield of Qadar",
            "steps": [
                {"step": 1, "title": "Divine Grounding", "description": "Anchor your worldview in the Four Pillars of Qadar, recognizing Allah's absolute knowledge, pre-recording, will, and creation."},
                {"step": 2, "title": "Disciplined Agency", "description": "Exert 100% lawful effort in school, moral conduct, and daily tasks, living the principle of 'Tie your camel first' (Authentic Tawakkul)."},
                {"step": 3, "title": "Emotional Fortification", "description": "When unexpected adversity hits, banish 'If only', speak the prophetic formula (Qaddarallahu), and embrace peaceful Rida."},
                {"step": 4, "title": "Enduring Character Fruit", "description": "Cultivate lifelong humility in times of triumph (Shukr) and unshakable fortitude in times of difficulty (Sabr), attaining Tuman'ninah."}
            ]
        },
        "worked_example": {
            "title": "Interactive Conceptual Matching & Synthesis",
            "scenario": (
                "During a comprehensive unit review, students are presented with four distinct real-life situations "
                "and asked to identify which foundational concept of Qadar each situation represents:\n"
                "1. Knowing that Allah has written your lifespan and provisions fifty thousand years ago.\n"
                "2. The rain falling on your school campus exactly at noon as Allah knew it would.\n"
                "3. Feeling peaceful and grateful when your outdoor plans are unexpectedly disrupted, trusting Allah's wiser plan.\n"
                "4. Preparing with maximum effort for an examination while sincerely praying to Allah for success."
            ),
            "analysis": (
                "• Situation 1 illustrates Al-Lawh al-Mahfuz (The Preserved Tablet) — Allah's eternal, comprehensive record written before creation.\n"
                "• Situation 2 illustrates Qadha — the temporal execution and physical occurrence of decreed reality in time.\n"
                "• Situation 3 illustrates Rida (Acceptance) — the highest spiritual station where the heart embraces divine will with peace and tranquility.\n"
                "• Situation 4 illustrates Tawakkul (Trust & Effort) — the authentic balance where human moral agency and lawful striving accompany trust in Allah."
            ),
            "takeaway": "Belief in Qadar is not an abstract riddle; it directly translates into purposeful effort (Tawakkul), peaceful acceptance (Rida), and recognition of divine order (Qadar & Qadha)."
        },
        "real_world_application": (
            "Design a personal 'Resilience & Character Poster' for your study room or digital notebook. "
            "In the center, write the Hadith 'Qaddarallahu wa ma sha'a fa'al' in bold lettering. "
            "Around it, illustrate the three pillars of character resilience: (1) Humility and Shukr during success, "
            "(2) Patience and Sabr during adversity, and (3) Freedom from anxiety through Tawakkul. "
            "Whenever you experience pre-exam stress or personal difficulty, review your poster to re-center your heart on divine wisdom."
        ),
        "reflection": (
            "How does a deep belief in Qadar empower you to forgive individuals who have accidentally ruined your plans "
            "or caused you unintended harm? What is the practical difference in daily life between authentic active trust "
            "(*Tawakkul*) and lazy passive resignation (*Tawaakul*)?"
        ),
        "misconception": {
            "misconception": "Tawakkul means sitting passively at home, neither studying nor taking medication when ill, expecting Allah to grant success and cure solely through divine decree.",
            "correction": "This attitude is fatalistic laziness (Tawaakul), which the Prophet (PBUH) condemned. Authentic Tawakkul requires actively utilizing all lawful physical means ('Tie your camel') while relying with your heart entirely upon Allah for the ultimate result."
        },
        "mcq": {
            "question": "Amina worked hard for months to qualify for the national science fair, but her project model was damaged during road transit, and she was unable to participate. Applying the full synthesis of our unit on Qadar, what is the most balanced, spiritually mature response Amina should make?",
            "options": [
                "A) Cry and proclaim 'If only I had traveled by bus instead of truck, this would never have happened!' and refuse to build any science models in the future.",
                "B) Accept that the transit damage was decreed by Allah, remain patient (Sabr), and resolve to use her skills to build an even better project for next year, knowing her past effort was rewarded.",
                "C) Declare 'It was clearly my Qadar to fail in life, so studying science or putting effort into school competitions is entirely pointless.'",
                "D) File an aggressive lawsuit against the transportation driver, furiously demanding that they compensate her for stolen potential."
            ],
            "answer": "B",
            "correct_answer": "B",
            "explanation": "Option B represents the mature, complete synthesis of Islamic belief in Qadar: peaceful acceptance of what is outside human control (Rida), perseverance through trial (Sabr), recognition that effort is rewarded by Allah, and continued active striving without despair."
        },
        "summary": {
            "key_points": [
                "Belief in Qadar is a holistic pillar of Iman that balances absolute divine sovereignty with human agency and accountability.",
                "Sincere acceptance (*Rida*) and the phrase *Qaddarallahu* shut the door to anxiety, regret, and the whisperings of Satan.",
                "The Shield of Qadar fosters an invincible, balanced character: humble in success, resilient in trial, and perpetually at peace."
            ],
            "vocabulary": [
                {"term": "Tawakkul", "definition": "Sincere reliance and trust upon Allah while actively taking all necessary lawful means."},
                {"term": "Tawaakul", "definition": "Passive, fatalistic neglect of effort under the false guise of relying upon Allah."},
                {"term": "Tuman'ninah", "definition": "Deep tranquility, stability, and peaceful contentment of the soul."},
                {"term": "Dar al-Ibtila", "definition": "The worldly life viewed as an arena of trials, refinement, and examination."}
            ]
        },
        "exit_ticket": "In two sentences, formulate a personal plan for how you will use the 'Shield of Qadar' to manage exam anxiety and maintain focus during your upcoming national evaluations."
    }
]


# ─── INGESTION RUNNER ─────────────────────────────────────────────────────────

def ingest_grade9_ire_topic6():
    print("=" * 80)
    print("VLEARN INGESTION ENGINE: GRADE 9 IRE — TOPIC 6: BELIEF IN QADAR")
    print("Target Topic ID: 346 | Strict Subject & Topic Isolation")
    print("=" * 80)

    with transaction.atomic():
        # Retrieve target topic 346
        topic = Topic.objects.select_related("subject", "subject__grade", "subject__grade__curriculum").get(id=346)
        subject = topic.subject
        grade = subject.grade
        curriculum = grade.curriculum

        print(f"Curriculum : {curriculum.name}")
        print(f"Grade      : {grade.name} (ID: {grade.id})")
        print(f"Subject    : {subject.name} (ID: {subject.id})")
        print(f"Topic      : {topic.name} (ID: {topic.id}, Order: {topic.order})")
        print("-" * 80)

        # Update topic metadata
        topic.name = "Belief in Qadar (Divine Decree)"
        topic.description = (
            "Comprehensive study of Belief in Qadar (Divine Decree) as the Sixth Pillar of Iman: "
            "definitions of Qadar and Qadha, Al-Lawh al-Mahfuz, the Four Pillars of Qadar, "
            "the balance between divine sovereignty and human moral agency, psychological benefits "
            "of Sabr (patience) and Shukr (gratitude), avoidance of 'If only' (Law), and cultivation "
            "of spiritual contentment (Rida) and inner tranquility (Tuman'ninah)."
        )
        topic.save()

        # Clean existing units under topic 346 (Strictly isolated to Topic 346)
        existing_units = LearningUnit.objects.filter(topic=topic)
        if existing_units.exists():
            print(f"[*] Removing {existing_units.count()} existing LearningUnits under Topic 346...")
            existing_units.delete()

        # Clean any orphan lessons under topic 346
        orphan_lessons = Lesson.objects.filter(topic=topic)
        if orphan_lessons.exists():
            print(f"[*] Removing {orphan_lessons.count()} orphan Lessons under Topic 346...")
            orphan_lessons.delete()

        total_units_created = 0
        total_lessons_created = 0
        total_blocks_created = 0
        total_assets_created = 0

        for cfg in LESSONS_DATA:
            u_order = cfg["unit_order"]
            u_name = cfg["unit_name"]
            l_title = cfg["lesson_title"]

            print(f"\n>>> [Unit {u_order}/4] Ingesting: '{l_title}'")

            # 1. Create LearningUnit
            unit = LearningUnit.objects.create(
                topic=topic,
                order=u_order,
                name=u_name,
                description=clean_text(cfg["unit_description"])
            )
            total_units_created += 1

            # 2. Create Published Lesson
            lesson = Lesson.objects.create(
                topic=topic,
                learning_unit=unit,
                title=clean_text(l_title),
                status="published",
                version=1,
                published_at=timezone.now(),
                immutable_metadata={
                    "grade": "Grade 9",
                    "grade_id": grade.id,
                    "subject": "IRE",
                    "subject_id": subject.id,
                    "topic_id": topic.id,
                    "topic_order": topic.order,
                    "topic_name": topic.name,
                    "unit_order": u_order,
                    "unit_name": u_name,
                    "author": "VLearn Senior Curriculum Ingestion Specialist",
                    "curriculum_framework": "CBC Kenya Grade 9 IRE Strand 3 Sub-strand 3.2",
                    "enrichment_version": "v3_pedagogical_7cards",
                    "diagram_title": cfg["diagram_title"]
                }
            )
            total_lessons_created += 1

            # 3. Create LessonAssets
            # Asset 1: Authentic Wikimedia Commons Image
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
                    "author": img_info.get("author", "Classical Heritage"),
                    "licensing": img_info.get("licensing", "Public Domain"),
                    "source": img_info.get("source", "Wikimedia Commons"),
                    "caption": clean_text(img_info["caption"])
                }
            )

            # Asset 2: Dedicated Vector SVG Diagram
            svg_content = cfg["svg_fn"]()
            svg_asset = LessonAsset.objects.create(
                lesson=lesson,
                asset_type="diagram",
                source_type="ai_generated",
                storage_type="url",
                status="attached",
                title=clean_text(cfg["diagram_title"]),
                description=f"High-quality pedagogical vector SVG diagram illustrating {l_title}.",
                url=f"https://vlearn.africa/assets/diagrams/ire/grade9_topic_6_lesson_{u_order}.svg",
                metadata={
                    "svg_content": svg_content,
                    "svg_xml": svg_content,
                    "viewBox": "0 0 880 440",
                    "theme": "#0f172a"
                }
            )

            # Asset 3: Educational YouTube Video
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

            # 4. Build 7 Cards / Pages (Standardized Pedagogical Blocks)

            # ───────────────────────────────────────────────────────────────────
            # CARD 1 (Page 1): Orientation & Inquiry
            # ───────────────────────────────────────────────────────────────────
            b_p1_img = LessonBlock.objects.create(
                lesson=lesson, page_number=1, page_title="Orientation & Inquiry",
                order=10, component_order=1,
                block_type="suggested_image", component_type="suggested_image",
                title=clean_text(img_info["title"]),
                content={
                    "title": clean_text(img_info["title"]),
                    "url": img_info["url"],
                    "caption": clean_text(img_info["caption"]),
                    "author": img_info.get("author", "Classical Heritage"),
                    "licensing": img_info.get("licensing", "Public Domain"),
                    "source": img_info.get("source", "Wikimedia Commons")
                }
            )
            b_p1_img.assets.add(img_asset)

            LessonBlock.objects.create(
                lesson=lesson, page_number=1, page_title="Orientation & Inquiry",
                order=20, component_order=2,
                block_type="learning_goal", component_type="learning_goal",
                title="Lesson Objectives & Inquiry Hook",
                content={
                    "inquiry_question": clean_text(cfg["inquiry_question"]),
                    "connection": clean_text(cfg["connection"]),
                    "goals": clean_dict(cfg["goals"]),
                    "markdown": f"### Inquiry Question\n\n**{clean_text(cfg['inquiry_question'])}**\n\n### Connection & Hook\n\n{clean_text(cfg['connection'])}\n\n### Learning Goals\n\n" + "\n".join([f"- {g}" for g in cfg["goals"]])
                }
            )

            # ───────────────────────────────────────────────────────────────────
            # CARD 2 (Page 2): Core Concept & Scripture Panel
            # ───────────────────────────────────────────────────────────────────
            LessonBlock.objects.create(
                lesson=lesson, page_number=2, page_title="Core Concept & Scripture",
                order=30, component_order=1,
                block_type="concept_explanation", component_type="concept_explanation",
                title="Authoritative Concept",
                content={
                    "title": "Authoritative Concept",
                    "markdown": clean_text(cfg["authoritative_concept"]),
                    "text": clean_text(cfg["authoritative_concept"])
                }
            )

            LessonBlock.objects.create(
                lesson=lesson, page_number=2, page_title="Core Concept & Scripture",
                order=40, component_order=2,
                block_type="callout", component_type="callout",
                title="Scripture & Sources Panel",
                content={
                    "title": "Scripture & Sources Panel",
                    "text": clean_text(cfg["scripture_panel"]),
                    "markdown": clean_text(cfg["scripture_panel"])
                }
            )

            # ───────────────────────────────────────────────────────────────────
            # CARD 3 (Page 3): Deep Explanation & Architecture Diagram
            # ───────────────────────────────────────────────────────────────────
            LessonBlock.objects.create(
                lesson=lesson, page_number=3, page_title="Deep Explanation & Diagram",
                order=50, component_order=1,
                block_type="concept_explanation", component_type="concept_explanation",
                title="In-Depth Analysis & Exposition",
                content={
                    "title": "In-Depth Analysis & Exposition",
                    "markdown": clean_text(cfg["deep_explanation"]),
                    "text": clean_text(cfg["deep_explanation"])
                }
            )

            b_p3_diag = LessonBlock.objects.create(
                lesson=lesson, page_number=3, page_title="Deep Explanation & Diagram",
                order=60, component_order=2,
                block_type="suggested_diagram", component_type="suggested_diagram",
                title=f"Diagram: {clean_text(cfg['diagram_title'])}",
                metadata={
                    "svg_content": svg_content,
                    "svg_xml": svg_content,
                    "viewBox": "0 0 880 440",
                    "theme": "#0f172a"
                },
                content={
                    "title": f"Diagram: {clean_text(cfg['diagram_title'])}",
                    "caption": f"Pedagogical vector SVG architecture for {l_title}.",
                    "svg": svg_content,
                    "svg_xml": svg_content,
                    "svg_content": svg_content,
                    "url": svg_asset.url
                }
            )
            b_p3_diag.assets.add(svg_asset)

            # Structured comparison table or step process on Card 3
            if "comparison_table" in cfg:
                LessonBlock.objects.create(
                    lesson=lesson, page_number=3, page_title="Deep Explanation & Diagram",
                    order=70, component_order=3,
                    block_type="comparison_table", component_type="comparison_table",
                    title=clean_text(cfg["comparison_table"]["title"]),
                    content=clean_dict(cfg["comparison_table"])
                )
            elif "step_process" in cfg:
                LessonBlock.objects.create(
                    lesson=lesson, page_number=3, page_title="Deep Explanation & Diagram",
                    order=70, component_order=3,
                    block_type="step_process", component_type="step_process",
                    title=clean_text(cfg["step_process"]["title"]),
                    content=clean_dict(cfg["step_process"])
                )

            # ───────────────────────────────────────────────────────────────────
            # CARD 4 (Page 4): Worked Example & Relatable Scenario
            # ───────────────────────────────────────────────────────────────────
            LessonBlock.objects.create(
                lesson=lesson, page_number=4, page_title="Worked Example & Scenario",
                order=80, component_order=1,
                block_type="worked_example", component_type="worked_example",
                title=clean_text(cfg["worked_example"].get("title", "Relatable Student Scenario & Analysis")),
                content={
                    "title": clean_text(cfg["worked_example"].get("title", "Relatable Student Scenario & Analysis")),
                    "scenario": clean_text(cfg["worked_example"]["scenario"]),
                    "analysis": clean_text(cfg["worked_example"]["analysis"]),
                    "takeaway": clean_text(cfg["worked_example"]["takeaway"]),
                    "markdown": (
                        f"### Student Scenario\n\n{clean_text(cfg['worked_example']['scenario'])}\n\n"
                        f"### Analytical Breakdown\n\n{clean_text(cfg['worked_example']['analysis'])}\n\n"
                        f"### Core Takeaway\n\n**{clean_text(cfg['worked_example']['takeaway'])}**"
                    )
                }
            )

            # ───────────────────────────────────────────────────────────────────
            # CARD 5 (Page 5): Suggested Video, Real-World Application, Reflection & Misconception
            # ───────────────────────────────────────────────────────────────────
            b_p5_vid = LessonBlock.objects.create(
                lesson=lesson, page_number=5, page_title="Real-World Application & Reflection",
                order=90, component_order=1,
                block_type="suggested_video", component_type="suggested_video",
                title=clean_text(yt_info["title"]),
                content={
                    "title": clean_text(yt_info["title"]),
                    "url": f"https://www.youtube.com/watch?v={yt_info['youtube_id']}",
                    "youtube_id": yt_info["youtube_id"],
                    "embed_url": f"https://www.youtube.com/embed/{yt_info['youtube_id']}",
                    "description": clean_text(yt_info["description"])
                }
            )
            b_p5_vid.assets.add(yt_asset)

            LessonBlock.objects.create(
                lesson=lesson, page_number=5, page_title="Real-World Application & Reflection",
                order=100, component_order=2,
                block_type="real_world_example", component_type="real_world_example",
                title="Actionable Real-World Application",
                content={
                    "title": "Actionable Real-World Application",
                    "application": clean_text(cfg["real_world_application"]),
                    "markdown": f"### Real-World Application\n\n{clean_text(cfg['real_world_application'])}"
                }
            )

            LessonBlock.objects.create(
                lesson=lesson, page_number=5, page_title="Real-World Application & Reflection",
                order=110, component_order=3,
                block_type="reflection", component_type="reflection",
                title="Pause & Reflect",
                content={
                    "title": "Pause & Reflect",
                    "prompt": clean_text(cfg["reflection"]),
                    "markdown": f"### Pause & Reflect\n\n{clean_text(cfg['reflection'])}"
                }
            )

            if "misconception" in cfg:
                LessonBlock.objects.create(
                    lesson=lesson, page_number=5, page_title="Real-World Application & Reflection",
                    order=120, component_order=4,
                    block_type="common_misconception", component_type="common_misconception",
                    title="Common Misconception & Correction",
                    content={
                        "title": "Common Misconception & Correction",
                        "misconception": clean_text(cfg["misconception"]["misconception"]),
                        "correction": clean_text(cfg["misconception"]["correction"]),
                        "reality": clean_text(cfg["misconception"]["correction"]),
                        "markdown": (
                            f"### Common Misconception\n\n❌ *{clean_text(cfg['misconception']['misconception'])}*\n\n"
                            f"### Factual Correction\n\n✓ **{clean_text(cfg['misconception']['correction'])}**"
                        )
                    }
                )

            # ───────────────────────────────────────────────────────────────────
            # CARD 6 (Page 6): Interactive Assessment / Knowledge Check
            # ───────────────────────────────────────────────────────────────────
            LessonBlock.objects.create(
                lesson=lesson, page_number=6, page_title="Knowledge Check & Assessment",
                order=130, component_order=1,
                block_type="knowledge_check", component_type="knowledge_check",
                title=f"Concept Diagnostic: {l_title}",
                content=clean_dict(cfg["mcq"])
            )

            # ───────────────────────────────────────────────────────────────────
            # CARD 7 (Page 7): Summary, Key Points & Mini-Activity (Exit Ticket)
            # ───────────────────────────────────────────────────────────────────
            LessonBlock.objects.create(
                lesson=lesson, page_number=7, page_title="Summary & Exit Ticket",
                order=140, component_order=1,
                block_type="summary", component_type="summary",
                title="Unit Principles & Vocabulary Review",
                content={
                    "title": f"Summary: {l_title}",
                    "key_points": clean_dict(cfg["summary"]["key_points"]),
                    "vocabulary": clean_dict(cfg["summary"]["vocabulary"]),
                    "markdown": (
                        f"### Key Principles\n\n"
                        + "\n".join([f"- {kp}" for kp in cfg["summary"]["key_points"]])
                        + "\n\n### Vocabulary Review\n\n"
                        + "\n".join([f"- **{v['term']}**: {v['definition']}" for v in cfg["summary"]["vocabulary"]])
                    )
                }
            )

            LessonBlock.objects.create(
                lesson=lesson, page_number=7, page_title="Summary & Exit Ticket",
                order=150, component_order=2,
                block_type="mini_activity", component_type="mini_activity",
                title="Exit Ticket Challenge",
                content={
                    "title": "Exit Ticket Challenge",
                    "activity": clean_text(cfg["exit_ticket"]),
                    "prompt": clean_text(cfg["exit_ticket"]),
                    "markdown": f"### Exit Ticket Challenge\n\n📝 **{clean_text(cfg['exit_ticket'])}**"
                }
            )

            blocks_count = lesson.blocks.count()
            total_blocks_created += blocks_count
            print(f"  [+] Created 7 Cards / Pages with {blocks_count} Blocks and 3 LessonAssets")

        print("\n" + "=" * 80)
        print("TOPIC 346 INGESTION & ENRICHMENT COMPLETE!")
        print(f"  - Subject           : {subject.name} (ID: {subject.id})")
        print(f"  - Topic             : {topic.name} (ID: {topic.id}, Order: {topic.order})")
        print(f"  - LearningUnits     : {total_units_created}")
        print(f"  - Lessons Published : {total_lessons_created}")
        print(f"  - LessonBlocks      : {total_blocks_created}")
        print(f"  - LessonAssets      : {total_assets_created}")
        print("=" * 80)


if __name__ == "__main__":
    ingest_grade9_ire_topic6()
