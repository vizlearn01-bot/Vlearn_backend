"""
VLearn CBC Grade 9 IRE — Topic 3: Ulum al-Hadith (The Sciences of Hadith)
Production Ingestion and Enrichment Script for all 10 Lessons

Target Topic in DB: Topic ID 343 (Subject: IRE ID 53, Grade: Grade 9 ID 18)
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
    """Removes bracket citations and internal pedagogical tags."""
    if not text:
        return ""
    text = re.sub(r'\[(?:\d+(?:\.\d+)?(?:,\s*\d+(?:\.\d+)?)*|image_\d+|S\d+.*?|[\d,\s]{2,})\]', '', text)
    text = re.sub(
        r'\[(VISUAL|QURAN REFERENCE|HADITH REFERENCE|BIBLE REFERENCE|REAL WORLD APPLICATION|REFLECTION|CRITICAL THINKING|VALUES|MISCONCEPTION|INTERACTION|ETHICAL SCENARIO|KEY VERSE|HISTORICAL CONTEXT|PEDAGOGICAL ARCHITECTURE|PROJECT TITLE|MAP|TIMELINE|COMPARISON|INFOGRAPHIC|SVG)[^\]]*\]',
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


# ─── 10 PEDAGOGICAL VECTOR SVGS (viewBox="0 0 880 440", theme #0f172a) ───────

def get_svg_lesson_1():
    """Lesson 2.1.1: Qur'an and Sunnah Complementary Relationship Architecture"""
    return """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 880 440" width="100%" height="100%">
  <defs>
    <linearGradient id="bg1" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#0f172a"/>
      <stop offset="50%" stop-color="#1e293b"/>
      <stop offset="100%" stop-color="#0f172a"/>
    </linearGradient>
    <linearGradient id="quranGrad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#0284c7"/>
      <stop offset="100%" stop-color="#0369a1"/>
    </linearGradient>
    <linearGradient id="sunnahGrad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#10b981"/>
      <stop offset="100%" stop-color="#047857"/>
    </linearGradient>
    <linearGradient id="apexGrad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#f59e0b"/>
      <stop offset="100%" stop-color="#d97706"/>
    </linearGradient>
    <filter id="shadow1" x="-10%" y="-10%" width="120%" height="120%">
      <feDropShadow dx="0" dy="4" stdDeviation="6" flood-color="#000000" flood-opacity="0.5"/>
    </filter>
  </defs>

  <rect width="880" height="440" fill="url(#bg1)" rx="14"/>
  <rect x="15" y="15" width="850" height="410" fill="none" stroke="#334155" stroke-width="1.5" stroke-dasharray="6 4" rx="10"/>

  <text x="440" y="42" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="17" font-weight="800" text-anchor="middle" letter-spacing="0.5">THE ARCHITECTURE OF ISLAMIC GUIDANCE</text>
  <text x="440" y="64" fill="#94a3b8" font-family="system-ui, sans-serif" font-size="12" text-anchor="middle">Complementary Relationship Between the Holy Qur'an and the Prophetic Sunnah (Hadith)</text>

  <!-- Left Pillar: The Qur'an -->
  <g transform="translate(45, 90)" filter="url(#shadow1)">
    <rect width="250" height="310" rx="12" fill="#1e293b" stroke="#0284c7" stroke-width="1.8"/>
    <rect width="250" height="42" rx="12" fill="url(#quranGrad)"/>
    <text x="125" y="27" fill="#ffffff" font-family="system-ui, sans-serif" font-size="14" font-weight="700" text-anchor="middle">THE HOLY QUR'AN</text>
    <text x="125" y="65" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="11" font-weight="700" text-anchor="middle">PRIMARY DIVINE SOURCE</text>
    <text x="20" y="95" fill="#f8fafc" font-family="system-ui, sans-serif" font-size="11" font-weight="600">• Literal Word of Allah (SWT)</text>
    <text x="20" y="125" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10.5">• Revealed verbatim in Arabic</text>
    <text x="20" y="155" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10.5">• Universal ethical principles</text>
    <text x="20" y="185" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10.5">• Broad commands: "Establish Salah"</text>
    <text x="20" y="215" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10.5">• Foundation of Islamic law</text>
    <rect x="20" y="245" width="210" height="45" rx="8" fill="#0f172a" stroke="#0369a1" stroke-width="1"/>
    <text x="125" y="264" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="10" font-weight="600" text-anchor="middle">Surah An-Nahl 16:44</text>
    <text x="125" y="280" fill="#94a3b8" font-family="system-ui, sans-serif" font-size="9" text-anchor="middle">"...that you make clear what was revealed"</text>
  </g>

  <!-- Right Pillar: The Hadith / Sunnah -->
  <g transform="translate(585, 90)" filter="url(#shadow1)">
    <rect width="250" height="310" rx="12" fill="#1e293b" stroke="#10b981" stroke-width="1.8"/>
    <rect width="250" height="42" rx="12" fill="url(#sunnahGrad)"/>
    <text x="125" y="27" fill="#ffffff" font-family="system-ui, sans-serif" font-size="14" font-weight="700" text-anchor="middle">HADITH &amp; SUNNAH</text>
    <text x="125" y="65" fill="#34d399" font-family="system-ui, sans-serif" font-size="11" font-weight="700" text-anchor="middle">SECONDARY EXPLANATORY SOURCE</text>
    <text x="20" y="95" fill="#f8fafc" font-family="system-ui, sans-serif" font-size="11" font-weight="600">• Living Model of Prophet (PBUH)</text>
    <text x="20" y="125" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10.5">• Words (Qawl), Actions (Fi'l)</text>
    <text x="20" y="155" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10.5">• Silent Approvals (Taqrir)</text>
    <text x="20" y="185" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10.5">• Mechanics: Units &amp; times of Salah</text>
    <text x="20" y="215" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10.5">• "Pray as you have seen me pray"</text>
    <rect x="20" y="245" width="210" height="45" rx="8" fill="#0f172a" stroke="#047857" stroke-width="1"/>
    <text x="125" y="264" fill="#34d399" font-family="system-ui, sans-serif" font-size="10" font-weight="600" text-anchor="middle">Surah An-Nisa 4:80</text>
    <text x="125" y="280" fill="#94a3b8" font-family="system-ui, sans-serif" font-size="9" text-anchor="middle">"He who obeys Messenger has obeyed Allah"</text>
  </g>

  <!-- Center Connecting Arch / Functions -->
  <g transform="translate(315, 90)">
    <!-- Function 1: Clarification -->
    <rect x="0" y="10" width="250" height="75" rx="10" fill="#1e293b" stroke="#f59e0b" stroke-width="1.2"/>
    <text x="125" y="32" fill="#fbbf24" font-family="system-ui, sans-serif" font-size="12" font-weight="700" text-anchor="middle">1. BAYAN (EXPLANATION)</text>
    <text x="125" y="52" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10" text-anchor="middle">Explains general verses with</text>
    <text x="125" y="68" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10" text-anchor="middle">practical timings &amp; rituals (Salah, Zakah)</text>

    <!-- Function 2: Specification -->
    <rect x="0" y="100" width="250" height="75" rx="10" fill="#1e293b" stroke="#38bdf8" stroke-width="1.2"/>
    <text x="125" y="122" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="12" font-weight="700" text-anchor="middle">2. TAKHSIS (SPECIFICATION)</text>
    <text x="125" y="142" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10" text-anchor="middle">Specifies broad trade laws,</text>
    <text x="125" y="158" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10" text-anchor="middle">prohibiting deceit &amp; usurious clauses</text>

    <!-- Function 3: Legislation -->
    <rect x="0" y="190" width="250" height="75" rx="10" fill="#1e293b" stroke="#a855f7" stroke-width="1.2"/>
    <text x="125" y="212" fill="#c084fc" font-family="system-ui, sans-serif" font-size="12" font-weight="700" text-anchor="middle">3. TASHRI' IDAPHI (SUPPLEMENT)</text>
    <text x="125" y="232" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10" text-anchor="middle">Provides secondary moral rulings &amp;</text>
    <text x="125" y="248" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10" text-anchor="middle">daily etiquettes not explicitly in Qur'an</text>

    <!-- Bottom Synergy Pill -->
    <rect x="15" y="278" width="220" height="30" rx="15" fill="url(#apexGrad)"/>
    <text x="125" y="298" fill="#0f172a" font-family="system-ui, sans-serif" font-size="11" font-weight="800" text-anchor="middle">INDISPENSABLE HARMONY</text>
  </g>

  <!-- Connective Arrows -->
  <line x1="295" y1="140" x2="315" y2="140" stroke="#38bdf8" stroke-width="2"/>
  <line x1="565" y1="140" x2="585" y2="140" stroke="#34d399" stroke-width="2"/>
</svg>"""


def get_svg_lesson_2():
    """Lesson 2.1.2: The Kutub al-Sittah (Six Books) Classification Hierarchy"""
    return """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 880 440" width="100%" height="100%">
  <defs>
    <linearGradient id="bg2" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#0f172a"/>
      <stop offset="50%" stop-color="#1e293b"/>
      <stop offset="100%" stop-color="#0f172a"/>
    </linearGradient>
    <linearGradient id="goldTop" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#f59e0b"/>
      <stop offset="100%" stop-color="#b45309"/>
    </linearGradient>
    <linearGradient id="silverSunan" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#0ea5e9"/>
      <stop offset="100%" stop-color="#0369a1"/>
    </linearGradient>
    <filter id="shadow2" x="-10%" y="-10%" width="120%" height="120%">
      <feDropShadow dx="0" dy="4" stdDeviation="5" flood-color="#000000" flood-opacity="0.4"/>
    </filter>
  </defs>

  <rect width="880" height="440" fill="url(#bg2)" rx="14"/>
  <rect x="15" y="15" width="850" height="410" fill="none" stroke="#334155" stroke-width="1.5" stroke-dasharray="6 4" rx="10"/>

  <text x="440" y="42" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="17" font-weight="800" text-anchor="middle">AL-KUTUB AL-SITTAH (THE SIX AUTHENTIC HADITH BOOKS)</text>
  <text x="440" y="64" fill="#94a3b8" font-family="system-ui, sans-serif" font-size="12" text-anchor="middle">Canonical 3rd Century A.H. Compilations and Their Hierarchical Authentication Tiers</text>

  <!-- TIER 1: AL-SAHIHAYN (Gold Tier) -->
  <g transform="translate(45, 85)" filter="url(#shadow2)">
    <rect width="790" height="135" rx="12" fill="#1e293b" stroke="#f59e0b" stroke-width="1.8"/>
    <rect width="790" height="34" rx="12" fill="url(#goldTop)"/>
    <text x="395" y="23" fill="#0f172a" font-family="system-ui, sans-serif" font-size="13" font-weight="800" text-anchor="middle">TIER 1: AL-SAHIHAYN (THE TWO UNANIMOUSLY AUTHENTIC COMPILATIONS)</text>

    <!-- Sahih al-Bukhari -->
    <rect x="25" y="46" width="355" height="75" rx="8" fill="#0f172a" stroke="#d97706" stroke-width="1.2"/>
    <text x="40" y="68" fill="#fbbf24" font-family="system-ui, sans-serif" font-size="13" font-weight="700">1. Sahih al-Bukhari</text>
    <text x="40" y="86" fill="#f8fafc" font-family="system-ui, sans-serif" font-size="10.5">Compiler: Imam Muhammad ibn Isma'il al-Bukhari (d. 256 AH)</text>
    <text x="40" y="104" fill="#94a3b8" font-family="system-ui, sans-serif" font-size="9.5">• Absolute strictest verification criteria; most authentic book after Qur'an</text>

    <!-- Sahih Muslim -->
    <rect x="410" y="46" width="355" height="75" rx="8" fill="#0f172a" stroke="#d97706" stroke-width="1.2"/>
    <text x="425" y="68" fill="#fbbf24" font-family="system-ui, sans-serif" font-size="13" font-weight="700">2. Sahih Muslim</text>
    <text x="425" y="86" fill="#f8fafc" font-family="system-ui, sans-serif" font-size="10.5">Compiler: Imam Muslim ibn al-Hajjaj (d. 261 AH)</text>
    <text x="425" y="104" fill="#94a3b8" font-family="system-ui, sans-serif" font-size="9.5">• Exceptional thematic coherence &amp; precise chain variations comparison</text>
  </g>

  <!-- TIER 2: AL-SUNAN AL-ARBA'AH (Silver/Cyan Tier) -->
  <g transform="translate(45, 235)" filter="url(#shadow2)">
    <rect width="790" height="175" rx="12" fill="#1e293b" stroke="#0ea5e9" stroke-width="1.8"/>
    <rect width="790" height="34" rx="12" fill="url(#silverSunan)"/>
    <text x="395" y="23" fill="#ffffff" font-family="system-ui, sans-serif" font-size="13" font-weight="800" text-anchor="middle">TIER 2: AL-SUNAN AL-ARBA'AH (THE FOUR LEGAL &amp; ETHICAL SUNAN)</text>

    <!-- Sunan Abu Dawood -->
    <rect x="20" y="46" width="175" height="115" rx="8" fill="#0f172a" stroke="#0369a1" stroke-width="1"/>
    <text x="30" y="68" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="11" font-weight="700">3. Sunan Abu Dawood</text>
    <text x="30" y="85" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="9.5">Imam Abu Dawood</text>
    <text x="30" y="100" fill="#94a3b8" font-family="system-ui, sans-serif" font-size="8.5">(d. 275 AH)</text>
    <text x="30" y="120" fill="#f8fafc" font-family="system-ui, sans-serif" font-size="8.5">• Focus: Legal rulings (Ahkam)</text>
    <text x="30" y="135" fill="#94a3b8" font-family="system-ui, sans-serif" font-size="8.5">• Essential for jurists</text>

    <!-- Jami' at-Tirmidhi -->
    <rect x="210" y="46" width="175" height="115" rx="8" fill="#0f172a" stroke="#0369a1" stroke-width="1"/>
    <text x="220" y="68" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="11" font-weight="700">4. Jami' at-Tirmidhi</text>
    <text x="220" y="85" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="9.5">Imam Abu Isa at-Tirmidhi</text>
    <text x="220" y="100" fill="#94a3b8" font-family="system-ui, sans-serif" font-size="8.5">(d. 279 AH)</text>
    <text x="220" y="120" fill="#f8fafc" font-family="system-ui, sans-serif" font-size="8.5">• Pioneer in Hadith grading</text>
    <text x="220" y="135" fill="#94a3b8" font-family="system-ui, sans-serif" font-size="8.5">• Lists madhhab opinions</text>

    <!-- Sunan an-Nasa'i -->
    <rect x="400" y="46" width="175" height="115" rx="8" fill="#0f172a" stroke="#0369a1" stroke-width="1"/>
    <text x="410" y="68" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="11" font-weight="700">5. Sunan an-Nasa'i</text>
    <text x="410" y="85" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="9.5">Imam Ahmad an-Nasa'i</text>
    <text x="410" y="100" fill="#94a3b8" font-family="system-ui, sans-serif" font-size="8.5">(d. 303 AH)</text>
    <text x="410" y="120" fill="#f8fafc" font-family="system-ui, sans-serif" font-size="8.5">• Very strict narrator criteria</text>
    <text x="410" y="135" fill="#94a3b8" font-family="system-ui, sans-serif" font-size="8.5">• Highlights hidden defects</text>

    <!-- Sunan Ibn Majah -->
    <rect x="590" y="46" width="180" height="115" rx="8" fill="#0f172a" stroke="#0369a1" stroke-width="1"/>
    <text x="600" y="68" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="11" font-weight="700">6. Sunan Ibn Majah</text>
    <text x="600" y="85" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="9.5">Imam Ibn Majah</text>
    <text x="600" y="100" fill="#94a3b8" font-family="system-ui, sans-serif" font-size="8.5">(d. 273 AH)</text>
    <text x="600" y="120" fill="#f8fafc" font-family="system-ui, sans-serif" font-size="8.5">• Broad topical arrangement</text>
    <text x="600" y="135" fill="#94a3b8" font-family="system-ui, sans-serif" font-size="8.5">• Contains unique narrations</text>
  </g>
</svg>"""


def get_svg_lesson_3():
    """Lesson 2.1.3: Three Historical Phases of Hadith Preservation Timeline"""
    return """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 880 440" width="100%" height="100%">
  <defs>
    <linearGradient id="bg3" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#0f172a"/>
      <stop offset="50%" stop-color="#1e293b"/>
      <stop offset="100%" stop-color="#0f172a"/>
    </linearGradient>
    <linearGradient id="p1" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#10b981"/>
      <stop offset="100%" stop-color="#047857"/>
    </linearGradient>
    <linearGradient id="p2" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#f59e0b"/>
      <stop offset="100%" stop-color="#b45309"/>
    </linearGradient>
    <linearGradient id="p3" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#38bdf8"/>
      <stop offset="100%" stop-color="#0284c7"/>
    </linearGradient>
    <filter id="shadow3" x="-10%" y="-10%" width="120%" height="120%">
      <feDropShadow dx="0" dy="4" stdDeviation="5" flood-color="#000000" flood-opacity="0.4"/>
    </filter>
  </defs>

  <rect width="880" height="440" fill="url(#bg3)" rx="14"/>
  <rect x="15" y="15" width="850" height="410" fill="none" stroke="#334155" stroke-width="1.5" stroke-dasharray="6 4" rx="10"/>

  <text x="440" y="42" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="17" font-weight="800" text-anchor="middle">THREE HISTORICAL PHASES OF HADITH PRESERVATION</text>
  <text x="440" y="64" fill="#94a3b8" font-family="system-ui, sans-serif" font-size="12" text-anchor="middle">How the Sunnah Transitioned from Rigorous Oral Custody to Canonical Scientific Compilations</text>

  <!-- Central Connecting Timeline Axis -->
  <line x1="80" y1="110" x2="800" y2="110" stroke="#475569" stroke-width="4" stroke-linecap="round"/>
  <circle cx="180" cy="110" r="10" fill="#10b981" stroke="#f8fafc" stroke-width="2"/>
  <circle cx="440" cy="110" r="10" fill="#f59e0b" stroke="#f8fafc" stroke-width="2"/>
  <circle cx="700" cy="110" r="10" fill="#38bdf8" stroke="#f8fafc" stroke-width="2"/>

  <!-- PHASE 1: 1st Century AH (Prophetic & Sahabah Era) -->
  <g transform="translate(45, 140)" filter="url(#shadow3)">
    <rect width="250" height="265" rx="10" fill="#1e293b" stroke="#10b981" stroke-width="1.5"/>
    <rect width="250" height="34" rx="10" fill="url(#p1)"/>
    <text x="125" y="22" fill="#ffffff" font-family="system-ui, sans-serif" font-size="12" font-weight="700" text-anchor="middle">PHASE 1: 1st CENTURY A.H.</text>
    <text x="125" y="55" fill="#34d399" font-family="system-ui, sans-serif" font-size="11" font-weight="700" text-anchor="middle">ORAL MEMORIZATION &amp; SUHUF</text>
    <text x="20" y="85" fill="#f8fafc" font-family="system-ui, sans-serif" font-size="10.5">• Direct transmission from Prophet</text>
    <text x="20" y="110" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10">• Prodigious Arabian memory power</text>
    <text x="20" y="135" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10">• Private notebooks (al-Sahifah al-Sadiqah)</text>
    <text x="20" y="160" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10">• Priority on Qur'anic compilation</text>
    <rect x="20" y="190" width="210" height="60" rx="6" fill="#0f172a" stroke="#047857" stroke-width="1"/>
    <text x="125" y="210" fill="#f87171" font-family="system-ui, sans-serif" font-size="9.5" font-weight="700" text-anchor="middle">TRIGGER FOR FORMALIZATION:</text>
    <text x="125" y="228" fill="#94a3b8" font-family="system-ui, sans-serif" font-size="8.5" text-anchor="middle">Passing away of eyewitness Sahabah</text>
    <text x="125" y="242" fill="#94a3b8" font-family="system-ui, sans-serif" font-size="8.5" text-anchor="middle">and rapid geographical expansion</text>
  </g>

  <!-- PHASE 2: 2nd Century AH (Tabi'un Era) -->
  <g transform="translate(315, 140)" filter="url(#shadow3)">
    <rect width="250" height="265" rx="10" fill="#1e293b" stroke="#f59e0b" stroke-width="1.5"/>
    <rect width="250" height="34" rx="10" fill="url(#p2)"/>
    <text x="125" y="22" fill="#0f172a" font-family="system-ui, sans-serif" font-size="12" font-weight="800" text-anchor="middle">PHASE 2: 2nd CENTURY A.H.</text>
    <text x="125" y="55" fill="#fbbf24" font-family="system-ui, sans-serif" font-size="11" font-weight="700" text-anchor="middle">OFFICIAL STATE INITIATIVE</text>
    <text x="20" y="85" fill="#f8fafc" font-family="system-ui, sans-serif" font-size="10.5">• Caliph Umar ibn Abdul Aziz decree</text>
    <text x="20" y="110" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10">• "Search for Hadiths &amp; record them"</text>
    <text x="20" y="135" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10">• Ibn Shihab al-Zuhri leads gathering</text>
    <text x="20" y="160" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10">• Early thematic books (Imam Malik's Muwatta)</text>
    <rect x="20" y="190" width="210" height="60" rx="6" fill="#0f172a" stroke="#b45309" stroke-width="1"/>
    <text x="125" y="210" fill="#fbbf24" font-family="system-ui, sans-serif" font-size="9.5" font-weight="700" text-anchor="middle">CRUCIAL MILESTONE:</text>
    <text x="125" y="228" fill="#94a3b8" font-family="system-ui, sans-serif" font-size="8.5" text-anchor="middle">Transition from personal notebooks</text>
    <text x="125" y="242" fill="#94a3b8" font-family="system-ui, sans-serif" font-size="8.5" text-anchor="middle">to institutional archives</text>
  </g>

  <!-- PHASE 3: 3rd Century AH (Compilers Era) -->
  <g transform="translate(585, 140)" filter="url(#shadow3)">
    <rect width="250" height="265" rx="10" fill="#1e293b" stroke="#38bdf8" stroke-width="1.5"/>
    <rect width="250" height="34" rx="10" fill="url(#p3)"/>
    <text x="125" y="22" fill="#ffffff" font-family="system-ui, sans-serif" font-size="12" font-weight="700" text-anchor="middle">PHASE 3: 3rd CENTURY A.H.</text>
    <text x="125" y="55" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="11" font-weight="700" text-anchor="middle">CANONICAL VERIFICATION</text>
    <text x="20" y="85" fill="#f8fafc" font-family="system-ui, sans-serif" font-size="10.5">• Golden age of Hadith scholarship</text>
    <text x="20" y="110" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10">• Transcontinental journeys (Rihlah)</text>
    <text x="20" y="135" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10">• Rigorous narrator audit (Jarh &amp; Ta'dil)</text>
    <text x="20" y="160" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10">• Compilation of Kutub al-Sittah</text>
    <rect x="20" y="190" width="210" height="60" rx="6" fill="#0f172a" stroke="#0284c7" stroke-width="1"/>
    <text x="125" y="210" fill="#34d399" font-family="system-ui, sans-serif" font-size="9.5" font-weight="700" text-anchor="middle">ENDURING RESULT:</text>
    <text x="125" y="228" fill="#94a3b8" font-family="system-ui, sans-serif" font-size="8.5" text-anchor="middle">Peer-reviewed, graded reference</text>
    <text x="125" y="242" fill="#94a3b8" font-family="system-ui, sans-serif" font-size="8.5" text-anchor="middle">corpora preserved for all time</text>
  </g>
</svg>"""


def get_svg_lesson_4():
    """Lesson 2.1.4: The Three Blessed Generations of Transmission Tree"""
    return """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 880 440" width="100%" height="100%">
  <defs>
    <linearGradient id="bg4" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#0f172a"/>
      <stop offset="50%" stop-color="#1e293b"/>
      <stop offset="100%" stop-color="#0f172a"/>
    </linearGradient>
    <linearGradient id="gen1" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#f59e0b"/>
      <stop offset="100%" stop-color="#d97706"/>
    </linearGradient>
    <linearGradient id="gen2" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#10b981"/>
      <stop offset="100%" stop-color="#047857"/>
    </linearGradient>
    <linearGradient id="gen3" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#0ea5e9"/>
      <stop offset="100%" stop-color="#0369a1"/>
    </linearGradient>
  </defs>

  <rect width="880" height="440" fill="url(#bg4)" rx="14"/>
  <rect x="15" y="15" width="850" height="410" fill="none" stroke="#334155" stroke-width="1.5" stroke-dasharray="6 4" rx="10"/>

  <text x="440" y="40" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="17" font-weight="800" text-anchor="middle">SANAD AL-HADITH: THE THREE BLESSED GENERATIONS</text>
  <text x="440" y="60" fill="#94a3b8" font-family="system-ui, sans-serif" font-size="12" text-anchor="middle">The Unbroken Human Conduit from the Prophet Muhammad (PBUH) to the Canonical Compilers</text>

  <!-- Prophet Muhammad (PBUH) - The Root -->
  <g transform="translate(240, 75)">
    <rect width="400" height="45" rx="8" fill="#1e293b" stroke="#e2e8f0" stroke-width="2"/>
    <text x="200" y="28" fill="#f8fafc" font-family="system-ui, sans-serif" font-size="13" font-weight="800" text-anchor="middle">THE PROPHET MUHAMMAD (PBUH) — SOURCE OF GUIDANCE</text>
  </g>

  <!-- Conduit Line 1 -->
  <line x1="440" y1="120" x2="440" y2="140" stroke="#f59e0b" stroke-width="3"/>

  <!-- Level 1: Sahabah -->
  <g transform="translate(60, 140)">
    <rect width="760" height="70" rx="10" fill="#1e293b" stroke="#f59e0b" stroke-width="1.5"/>
    <rect width="180" height="70" rx="10" fill="url(#gen1)"/>
    <text x="90" y="32" fill="#0f172a" font-family="system-ui, sans-serif" font-size="13" font-weight="800" text-anchor="middle">1st GENERATION</text>
    <text x="90" y="52" fill="#0f172a" font-family="system-ui, sans-serif" font-size="11" font-weight="700" text-anchor="middle">AS-SAHABAH</text>
    <text x="200" y="30" fill="#fbbf24" font-family="system-ui, sans-serif" font-size="12" font-weight="700">The Companions of the Prophet (Met him in faith and died as Muslims)</text>
    <text x="200" y="50" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10.5">Role: Direct witnesses who heard his words, memorized them, and exemplified his character.</text>
    <text x="640" y="42" fill="#94a3b8" font-family="system-ui, sans-serif" font-size="9.5" text-anchor="middle">Abu Huraira, Aisha, Ibn Umar</text>
  </g>

  <!-- Conduit Line 2 -->
  <line x1="440" y1="210" x2="440" y2="230" stroke="#10b981" stroke-width="3"/>

  <!-- Level 2: Tabi'un -->
  <g transform="translate(60, 230)">
    <rect width="760" height="70" rx="10" fill="#1e293b" stroke="#10b981" stroke-width="1.5"/>
    <rect width="180" height="70" rx="10" fill="url(#gen2)"/>
    <text x="90" y="32" fill="#ffffff" font-family="system-ui, sans-serif" font-size="13" font-weight="800" text-anchor="middle">2nd GENERATION</text>
    <text x="90" y="52" fill="#ffffff" font-family="system-ui, sans-serif" font-size="11" font-weight="700" text-anchor="middle">AT-TABI'UN</text>
    <text x="200" y="30" fill="#34d399" font-family="system-ui, sans-serif" font-size="12" font-weight="700">The Successors (Met the Sahabah, but did not see the Prophet)</text>
    <text x="200" y="50" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10.5">Role: Gathered narrations from dispersing Sahabah; started official statewide compilation.</text>
    <text x="640" y="42" fill="#94a3b8" font-family="system-ui, sans-serif" font-size="9.5" text-anchor="middle">Said ibn al-Musayyib, Zuhri</text>
  </g>

  <!-- Conduit Line 3 -->
  <line x1="440" y1="300" x2="440" y2="320" stroke="#0ea5e9" stroke-width="3"/>

  <!-- Level 3: Atba' al-Tabi'in -->
  <g transform="translate(60, 320)">
    <rect width="760" height="70" rx="10" fill="#1e293b" stroke="#0ea5e9" stroke-width="1.5"/>
    <rect width="180" height="70" rx="10" fill="url(#gen3)"/>
    <text x="90" y="30" fill="#ffffff" font-family="system-ui, sans-serif" font-size="12" font-weight="800" text-anchor="middle">3rd GENERATION</text>
    <text x="90" y="50" fill="#ffffff" font-family="system-ui, sans-serif" font-size="10.5" font-weight="700" text-anchor="middle">ATBA' AL-TABI'IN</text>
    <text x="200" y="30" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="12" font-weight="700">Successors of the Successors (Learned directly from Tabi'un)</text>
    <text x="200" y="50" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10.5">Role: Developed narrator science (Jarh wa Ta'dil), classified Sahih vs Dha'if, wrote books.</text>
    <text x="640" y="42" fill="#94a3b8" font-family="system-ui, sans-serif" font-size="9.5" text-anchor="middle">Imam Malik, Sufyan al-Thawri</text>
  </g>

  <!-- Bottom Proof Banner -->
  <text x="440" y="415" fill="#f59e0b" font-family="system-ui, sans-serif" font-size="11" font-weight="600" text-anchor="middle">Hadith: "The best of people are my generation, then those who follow them, then those who follow them." (Sahih al-Bukhari)</text>
</svg>"""


def get_svg_lesson_5():
    """Lesson 2.1.5: The 5-Key Padlock of Sahih Hadith Authenticity"""
    return """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 880 440" width="100%" height="100%">
  <defs>
    <linearGradient id="bg5" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#0f172a"/>
      <stop offset="50%" stop-color="#1e293b"/>
      <stop offset="100%" stop-color="#0f172a"/>
    </linearGradient>
    <linearGradient id="lockGrad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#10b981"/>
      <stop offset="100%" stop-color="#047857"/>
    </linearGradient>
    <linearGradient id="goldKey" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#fbbf24"/>
      <stop offset="100%" stop-color="#d97706"/>
    </linearGradient>
    <filter id="shadow5" x="-10%" y="-10%" width="120%" height="120%">
      <feDropShadow dx="0" dy="4" stdDeviation="6" flood-color="#000000" flood-opacity="0.5"/>
    </filter>
  </defs>

  <rect width="880" height="440" fill="url(#bg5)" rx="14"/>
  <rect x="15" y="15" width="850" height="410" fill="none" stroke="#334155" stroke-width="1.5" stroke-dasharray="6 4" rx="10"/>

  <text x="440" y="42" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="17" font-weight="800" text-anchor="middle">THE 5-KEY PADLOCK OF SAHIH HADITH AUTHENTICITY</text>
  <text x="440" y="64" fill="#94a3b8" font-family="system-ui, sans-serif" font-size="12" text-anchor="middle">All 5 Conditions Must Simultaneously Turn for a Hadith to be Pronounced Sahih</text>

  <!-- Center Vault / Padlock -->
  <g transform="translate(340, 110)" filter="url(#shadow5)">
    <!-- Shackle -->
    <path d="M 50 80 A 50 50 0 0 1 150 80 L 150 110 L 125 110 L 125 80 A 25 25 0 0 0 75 80 L 75 110 L 50 110 Z" fill="#94a3b8" stroke="#cbd5e1" stroke-width="1.5"/>
    <!-- Body -->
    <rect x="25" y="105" width="150" height="150" rx="16" fill="url(#lockGrad)" stroke="#34d399" stroke-width="2"/>
    <circle cx="100" cy="165" r="16" fill="#0f172a"/>
    <polygon points="94,170 106,170 102,195 98,195" fill="#0f172a"/>
    <text x="100" y="225" fill="#ffffff" font-family="system-ui, sans-serif" font-size="12" font-weight="800" text-anchor="middle">SAHIH VAULT</text>
    <text x="100" y="240" fill="#a7f3d0" font-family="system-ui, sans-serif" font-size="9" text-anchor="middle">UNLOCKED ONLY WITH 5/5</text>
  </g>

  <!-- Left Side: Keys 1 and 2 -->
  <g transform="translate(45, 100)" filter="url(#shadow5)">
    <!-- Key 1: Connected Chain -->
    <rect width="265" height="100" rx="10" fill="#1e293b" stroke="#fbbf24" stroke-width="1.4"/>
    <rect width="40" height="100" rx="10" fill="url(#goldKey)"/>
    <text x="20" y="58" fill="#0f172a" font-family="system-ui, sans-serif" font-size="16" font-weight="900" text-anchor="middle">1</text>
    <text x="55" y="28" fill="#fbbf24" font-family="system-ui, sans-serif" font-size="12" font-weight="700">ITTISAL AL-ISNAD</text>
    <text x="55" y="46" fill="#f8fafc" font-family="system-ui, sans-serif" font-size="10.5" font-weight="600">Fully Connected Chain</text>
    <text x="55" y="65" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="9.5">• Every narrator directly met &amp; heard</text>
    <text x="55" y="80" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="9.5">• Zero chronological or geographic gaps</text>

    <!-- Key 2: Upright Character -->
    <g transform="translate(0, 120)">
      <rect width="265" height="100" rx="10" fill="#1e293b" stroke="#fbbf24" stroke-width="1.4"/>
      <rect width="40" height="100" rx="10" fill="url(#goldKey)"/>
      <text x="20" y="58" fill="#0f172a" font-family="system-ui, sans-serif" font-size="16" font-weight="900" text-anchor="middle">2</text>
      <text x="55" y="28" fill="#fbbf24" font-family="system-ui, sans-serif" font-size="12" font-weight="700">'ADALAT AL-RUWAT</text>
      <text x="55" y="46" fill="#f8fafc" font-family="system-ui, sans-serif" font-size="10.5" font-weight="600">Pious Moral Integrity</text>
      <text x="55" y="65" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="9.5">• Pious, honest, mature Muslims</text>
      <text x="55" y="80" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="9.5">• Never caught lying in any aspect of life</text>
    </g>
  </g>

  <!-- Right Side: Keys 3 and 4 -->
  <g transform="translate(570, 100)" filter="url(#shadow5)">
    <!-- Key 3: Perfect Memory -->
    <rect width="265" height="100" rx="10" fill="#1e293b" stroke="#fbbf24" stroke-width="1.4"/>
    <rect width="40" height="100" rx="10" fill="url(#goldKey)"/>
    <text x="20" y="58" fill="#0f172a" font-family="system-ui, sans-serif" font-size="16" font-weight="900" text-anchor="middle">3</text>
    <text x="55" y="28" fill="#fbbf24" font-family="system-ui, sans-serif" font-size="12" font-weight="700">TAMM AL-DABT</text>
    <text x="55" y="46" fill="#f8fafc" font-family="system-ui, sans-serif" font-size="10.5" font-weight="600">Flawless Memory Precision</text>
    <text x="55" y="65" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="9.5">• Precise mental recall or written notes</text>
    <text x="55" y="80" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="9.5">• Word-for-word accuracy under audit</text>

    <!-- Key 4: No Contradiction -->
    <g transform="translate(0, 120)">
      <rect width="265" height="100" rx="10" fill="#1e293b" stroke="#fbbf24" stroke-width="1.4"/>
      <rect width="40" height="100" rx="10" fill="url(#goldKey)"/>
      <text x="20" y="58" fill="#0f172a" font-family="system-ui, sans-serif" font-size="16" font-weight="900" text-anchor="middle">4</text>
      <text x="55" y="28" fill="#fbbf24" font-family="system-ui, sans-serif" font-size="12" font-weight="700">'ADAM AL-SHUDHUDH</text>
      <text x="55" y="46" fill="#f8fafc" font-family="system-ui, sans-serif" font-size="10.5" font-weight="600">Absence of Anomaly</text>
      <text x="55" y="65" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="9.5">• Text does not contradict stronger</text>
      <text x="55" y="80" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="9.5">• reports from more reliable narrators</text>
    </g>
  </g>

  <!-- Bottom Center: Key 5 -->
  <g transform="translate(240, 345)" filter="url(#shadow5)">
    <rect width="400" height="65" rx="10" fill="#1e293b" stroke="#fbbf24" stroke-width="1.4"/>
    <rect width="45" height="65" rx="10" fill="url(#goldKey)"/>
    <text x="22" y="40" fill="#0f172a" font-family="system-ui, sans-serif" font-size="18" font-weight="900" text-anchor="middle">5</text>
    <text x="60" y="25" fill="#fbbf24" font-family="system-ui, sans-serif" font-size="12" font-weight="700">'ADAM AL-'ILLAH (NO HIDDEN DEFECTS)</text>
    <text x="60" y="42" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10">Completely free from subtle, hidden flaws in chain or text detectable only by master critics.</text>
    <text x="60" y="55" fill="#34d399" font-family="system-ui, sans-serif" font-size="9" font-weight="700">Result: If 1 key fails → Hadith is NOT graded Sahih.</text>
  </g>
</svg>"""


def get_svg_lesson_6():
    """Lesson 2.1.6: Sahih vs Hasan Precision & Memory Gauge"""
    return """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 880 440" width="100%" height="100%">
  <defs>
    <linearGradient id="bg6" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#0f172a"/>
      <stop offset="50%" stop-color="#1e293b"/>
      <stop offset="100%" stop-color="#0f172a"/>
    </linearGradient>
    <linearGradient id="sahihCard" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#10b981"/>
      <stop offset="100%" stop-color="#047857"/>
    </linearGradient>
    <linearGradient id="hasanCard" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#0284c7"/>
      <stop offset="100%" stop-color="#0369a1"/>
    </linearGradient>
    <filter id="shadow6" x="-10%" y="-10%" width="120%" height="120%">
      <feDropShadow dx="0" dy="4" stdDeviation="6" flood-color="#000000" flood-opacity="0.4"/>
    </filter>
  </defs>

  <rect width="880" height="440" fill="url(#bg6)" rx="14"/>
  <rect x="15" y="15" width="850" height="410" fill="none" stroke="#334155" stroke-width="1.5" stroke-dasharray="6 4" rx="10"/>

  <text x="440" y="42" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="17" font-weight="800" text-anchor="middle">AUTHENTICITY GAUGE: SAHIH VS. HASAN HADITH</text>
  <text x="440" y="64" fill="#94a3b8" font-family="system-ui, sans-serif" font-size="12" text-anchor="middle">The Single Difference: Level of Narrator Memory Precision (Dabt Tamm vs. Dabt Khafif)</text>

  <!-- Left Column: Sahih -->
  <g transform="translate(45, 85)" filter="url(#shadow6)">
    <rect width="375" height="260" rx="12" fill="#1e293b" stroke="#10b981" stroke-width="1.8"/>
    <rect width="375" height="40" rx="12" fill="url(#sahihCard)"/>
    <text x="187" y="26" fill="#ffffff" font-family="system-ui, sans-serif" font-size="14" font-weight="800" text-anchor="middle">SAHIH (AUTHENTIC — GRADE 1)</text>

    <text x="25" y="65" fill="#34d399" font-family="system-ui, sans-serif" font-size="11" font-weight="700">✓ Connected Chain:</text>
    <text x="160" y="65" fill="#f8fafc" font-family="system-ui, sans-serif" font-size="11">Continuous (Ittisal al-Isnad)</text>

    <text x="25" y="95" fill="#34d399" font-family="system-ui, sans-serif" font-size="11" font-weight="700">✓ Moral Character:</text>
    <text x="160" y="95" fill="#f8fafc" font-family="system-ui, sans-serif" font-size="11">Flawless Piety ('Adalah)</text>

    <rect x="15" y="115" width="345" height="45" rx="6" fill="#0f172a" stroke="#10b981" stroke-width="1.2"/>
    <text x="25" y="133" fill="#fbbf24" font-family="system-ui, sans-serif" font-size="10.5" font-weight="800">★ MEMORY PRECISION (DABT):</text>
    <text x="25" y="148" fill="#34d399" font-family="system-ui, sans-serif" font-size="10" font-weight="700">DABT TAMM (100% Perfect, Flawless Retention)</text>

    <text x="25" y="185" fill="#34d399" font-family="system-ui, sans-serif" font-size="11" font-weight="700">✓ No Contradictions:</text>
    <text x="160" y="185" fill="#f8fafc" font-family="system-ui, sans-serif" font-size="11">Free from Shudhudh</text>

    <text x="25" y="215" fill="#34d399" font-family="system-ui, sans-serif" font-size="11" font-weight="700">✓ No Hidden Defects:</text>
    <text x="160" y="215" fill="#f8fafc" font-family="system-ui, sans-serif" font-size="11">Free from 'Illah</text>

    <rect x="25" y="232" width="325" height="20" rx="4" fill="#064e3b"/>
    <text x="187" y="246" fill="#a7f3d0" font-family="system-ui, sans-serif" font-size="9.5" font-weight="700" text-anchor="middle">LEGAL STATUS: INDISPUTABLE HIGHEST AUTHORITY</text>
  </g>

  <!-- Right Column: Hasan -->
  <g transform="translate(460, 85)" filter="url(#shadow6)">
    <rect width="375" height="260" rx="12" fill="#1e293b" stroke="#0284c7" stroke-width="1.8"/>
    <rect width="375" height="40" rx="12" fill="url(#hasanCard)"/>
    <text x="187" y="26" fill="#ffffff" font-family="system-ui, sans-serif" font-size="14" font-weight="800" text-anchor="middle">HASAN (GOOD — GRADE 2)</text>

    <text x="25" y="65" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="11" font-weight="700">✓ Connected Chain:</text>
    <text x="160" y="65" fill="#f8fafc" font-family="system-ui, sans-serif" font-size="11">Continuous (Ittisal al-Isnad)</text>

    <text x="25" y="95" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="11" font-weight="700">✓ Moral Character:</text>
    <text x="160" y="95" fill="#f8fafc" font-family="system-ui, sans-serif" font-size="11">Flawless Piety ('Adalah)</text>

    <rect x="15" y="115" width="345" height="45" rx="6" fill="#0f172a" stroke="#0284c7" stroke-width="1.2"/>
    <text x="25" y="133" fill="#fbbf24" font-family="system-ui, sans-serif" font-size="10.5" font-weight="800">★ MEMORY PRECISION (DABT):</text>
    <text x="25" y="148" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="10" font-weight="700">DABT KHAfif (Good/Slightly Lighter Precision)</text>

    <text x="25" y="185" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="11" font-weight="700">✓ No Contradictions:</text>
    <text x="160" y="185" fill="#f8fafc" font-family="system-ui, sans-serif" font-size="11">Free from Shudhudh</text>

    <text x="25" y="215" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="11" font-weight="700">✓ No Hidden Defects:</text>
    <text x="160" y="215" fill="#f8fafc" font-family="system-ui, sans-serif" font-size="11">Free from 'Illah</text>

    <rect x="25" y="232" width="325" height="20" rx="4" fill="#0c4a6e"/>
    <text x="187" y="246" fill="#bae6fd" font-family="system-ui, sans-serif" font-size="9.5" font-weight="700" text-anchor="middle">LEGAL STATUS: FULLY AUTHENTIC &amp; ACTIONABLE</text>
  </g>

  <!-- Bottom Commonality Anchor -->
  <g transform="translate(100, 360)">
    <rect width="680" height="50" rx="10" fill="#0f172a" stroke="#f59e0b" stroke-width="1.4"/>
    <text x="340" y="24" fill="#fbbf24" font-family="system-ui, sans-serif" font-size="12" font-weight="800" text-anchor="middle">CRITICAL JURISPRUDENTIAL PRINCIPLE (CONSENSUS OF SCHOLARS)</text>
    <text x="340" y="41" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10.5" text-anchor="middle">Both Sahih and Hasan Hadiths are 100% reliable for establishing Islamic Laws, Beliefs, and Ethics.</text>
  </g>
</svg>"""


def get_svg_lesson_7():
    """Lesson 2.1.7: Hadith Reliability & Usage Traffic Light System"""
    return """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 880 440" width="100%" height="100%">
  <defs>
    <linearGradient id="bg7" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#0f172a"/>
      <stop offset="50%" stop-color="#1e293b"/>
      <stop offset="100%" stop-color="#0f172a"/>
    </linearGradient>
    <linearGradient id="greenGrad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#10b981"/>
      <stop offset="100%" stop-color="#047857"/>
    </linearGradient>
    <linearGradient id="yellowGrad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#f59e0b"/>
      <stop offset="100%" stop-color="#b45309"/>
    </linearGradient>
    <linearGradient id="redGrad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#ef4444"/>
      <stop offset="100%" stop-color="#b91c1c"/>
    </linearGradient>
    <filter id="shadow7" x="-10%" y="-10%" width="120%" height="120%">
      <feDropShadow dx="0" dy="4" stdDeviation="5" flood-color="#000000" flood-opacity="0.4"/>
    </filter>
  </defs>

  <rect width="880" height="440" fill="url(#bg7)" rx="14"/>
  <rect x="15" y="15" width="850" height="410" fill="none" stroke="#334155" stroke-width="1.5" stroke-dasharray="6 4" rx="10"/>

  <text x="440" y="42" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="17" font-weight="800" text-anchor="middle">HADITH RELIABILITY &amp; USAGE: TRAFFIC LIGHT SYSTEM</text>
  <text x="440" y="64" fill="#94a3b8" font-family="system-ui, sans-serif" font-size="12" text-anchor="middle">Legal Framework for When and How Muslims May Apply Different Grades of Hadith</text>

  <!-- GREEN LIGHT: Sahih & Hasan -->
  <g transform="translate(45, 90)" filter="url(#shadow7)">
    <rect width="250" height="315" rx="12" fill="#1e293b" stroke="#10b981" stroke-width="1.8"/>
    <rect width="250" height="40" rx="12" fill="url(#greenGrad)"/>
    <circle cx="35" cy="20" r="12" fill="#22c55e" stroke="#ffffff" stroke-width="1.5"/>
    <text x="140" y="25" fill="#ffffff" font-family="system-ui, sans-serif" font-size="13" font-weight="800">GREEN: GO AHEAD</text>

    <text x="20" y="65" fill="#34d399" font-family="system-ui, sans-serif" font-size="12" font-weight="700">SAHIH &amp; HASAN</text>
    <text x="20" y="85" fill="#f8fafc" font-family="system-ui, sans-serif" font-size="10.5">• 100% Verified authenticity</text>
    <text x="20" y="110" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10">• Connected chain &amp; reliable memory</text>

    <rect x="15" y="130" width="220" height="90" rx="6" fill="#0f172a" stroke="#047857" stroke-width="1"/>
    <text x="125" y="150" fill="#34d399" font-family="system-ui, sans-serif" font-size="10" font-weight="700" text-anchor="middle">AUTHORIZED USES:</text>
    <text x="25" y="170" fill="#f8fafc" font-family="system-ui, sans-serif" font-size="9.5">1. Core Creed (Aqeedah)</text>
    <text x="25" y="188" fill="#f8fafc" font-family="system-ui, sans-serif" font-size="9.5">2. Legal Rulings (Halal / Haram)</text>
    <text x="25" y="206" fill="#f8fafc" font-family="system-ui, sans-serif" font-size="9.5">3. All Moral &amp; Ethical Directives</text>

    <rect x="15" y="240" width="220" height="55" rx="6" fill="#064e3b"/>
    <text x="125" y="260" fill="#a7f3d0" font-family="system-ui, sans-serif" font-size="9.5" font-weight="700" text-anchor="middle">Consensus of Ummah:</text>
    <text x="125" y="278" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="9" text-anchor="middle">Binding upon all Muslims</text>
  </g>

  <!-- YELLOW LIGHT: Dha'if (Weak) -->
  <g transform="translate(315, 90)" filter="url(#shadow7)">
    <rect width="250" height="315" rx="12" fill="#1e293b" stroke="#f59e0b" stroke-width="1.8"/>
    <rect width="250" height="40" rx="12" fill="url(#yellowGrad)"/>
    <circle cx="35" cy="20" r="12" fill="#fbbf24" stroke="#ffffff" stroke-width="1.5"/>
    <text x="140" y="25" fill="#0f172a" font-family="system-ui, sans-serif" font-size="13" font-weight="800">YELLOW: CAUTION</text>

    <text x="20" y="65" fill="#fbbf24" font-family="system-ui, sans-serif" font-size="12" font-weight="700">DHA'IF (WEAK)</text>
    <text x="20" y="85" fill="#f8fafc" font-family="system-ui, sans-serif" font-size="10.5">• Fails 1+ condition of Sahih</text>
    <text x="20" y="110" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10">• Broken chain or poor memory</text>

    <rect x="15" y="130" width="220" height="90" rx="6" fill="#0f172a" stroke="#b45309" stroke-width="1"/>
    <text x="125" y="150" fill="#fbbf24" font-family="system-ui, sans-serif" font-size="10" font-weight="700" text-anchor="middle">STRICT CONDITIONS FOR USE:</text>
    <text x="25" y="170" fill="#f87171" font-family="system-ui, sans-serif" font-size="9.5">✗ FORBIDDEN for Laws &amp; Creed</text>
    <text x="25" y="188" fill="#fcd34d" font-family="system-ui, sans-serif" font-size="9.5">✓ Permitted for Virtues (Fada'il)</text>
    <text x="25" y="206" fill="#94a3b8" font-family="system-ui, sans-serif" font-size="9">   (Only if weakness is minor)</text>

    <rect x="15" y="240" width="220" height="55" rx="6" fill="#451a03"/>
    <text x="125" y="260" fill="#fde68a" font-family="system-ui, sans-serif" font-size="9.5" font-weight="700" text-anchor="middle">Warning Note:</text>
    <text x="125" y="278" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="9" text-anchor="middle">Do not state "Prophet definitely said"</text>
  </g>

  <!-- RED LIGHT: Mawdu' (Fabricated) -->
  <g transform="translate(585, 90)" filter="url(#shadow7)">
    <rect width="250" height="315" rx="12" fill="#1e293b" stroke="#ef4444" stroke-width="1.8"/>
    <rect width="250" height="40" rx="12" fill="url(#redGrad)"/>
    <circle cx="35" cy="20" r="12" fill="#dc2626" stroke="#ffffff" stroke-width="1.5"/>
    <text x="140" y="25" fill="#ffffff" font-family="system-ui, sans-serif" font-size="13" font-weight="800">RED: STOP!</text>

    <text x="20" y="65" fill="#f87171" font-family="system-ui, sans-serif" font-size="12" font-weight="700">MAWDU' (FABRICATED)</text>
    <text x="20" y="85" fill="#f8fafc" font-family="system-ui, sans-serif" font-size="10.5">• Intentionally invented lies</text>
    <text x="20" y="110" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10">• Attributed falsely to Prophet</text>

    <rect x="15" y="130" width="220" height="90" rx="6" fill="#0f172a" stroke="#b91c1c" stroke-width="1"/>
    <text x="125" y="150" fill="#f87171" font-family="system-ui, sans-serif" font-size="10" font-weight="700" text-anchor="middle">ABSOLUTE PROHIBITION:</text>
    <text x="25" y="170" fill="#f87171" font-family="system-ui, sans-serif" font-size="9.5">✗ FORBIDDEN to practice</text>
    <text x="25" y="188" fill="#f87171" font-family="system-ui, sans-serif" font-size="9.5">✗ FORBIDDEN to quote or share</text>
    <text x="25" y="206" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="9.5">✓ ONLY allowed to warn people</text>

    <rect x="15" y="240" width="220" height="55" rx="6" fill="#450a0a"/>
    <text x="125" y="260" fill="#fca5a5" font-family="system-ui, sans-serif" font-size="9.5" font-weight="700" text-anchor="middle">Severe Prophetic Warning:</text>
    <text x="125" y="278" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="8.5" text-anchor="middle">"Whoever lies about me, takes seat in Fire"</text>
  </g>
</svg>"""


def get_svg_lesson_8():
    """Lesson 2.1.8: The Compiler's 4-Step Verification Journey"""
    return """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 880 440" width="100%" height="100%">
  <defs>
    <linearGradient id="bg8" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#0f172a"/>
      <stop offset="50%" stop-color="#1e293b"/>
      <stop offset="100%" stop-color="#0f172a"/>
    </linearGradient>
    <linearGradient id="stepGrad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#0284c7"/>
      <stop offset="100%" stop-color="#0369a1"/>
    </linearGradient>
    <filter id="shadow8" x="-10%" y="-10%" width="120%" height="120%">
      <feDropShadow dx="0" dy="4" stdDeviation="5" flood-color="#000000" flood-opacity="0.4"/>
    </filter>
  </defs>

  <rect width="880" height="440" fill="url(#bg8)" rx="14"/>
  <rect x="15" y="15" width="850" height="410" fill="none" stroke="#334155" stroke-width="1.5" stroke-dasharray="6 4" rx="10"/>

  <text x="440" y="42" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="17" font-weight="800" text-anchor="middle">THE COMPILER'S 4-STEP VERIFICATION METHODOLOGY</text>
  <text x="440" y="64" fill="#94a3b8" font-family="system-ui, sans-serif" font-size="12" text-anchor="middle">The Rigorous Scientific Pipeline Created by Classical Scholars (e.g. Imam al-Bukhari)</text>

  <!-- Step 1: Rihlah -->
  <g transform="translate(45, 95)" filter="url(#shadow8)">
    <rect width="185" height="300" rx="10" fill="#1e293b" stroke="#38bdf8" stroke-width="1.5"/>
    <rect width="185" height="34" rx="10" fill="url(#stepGrad)"/>
    <text x="92" y="22" fill="#ffffff" font-family="system-ui, sans-serif" font-size="12" font-weight="800" text-anchor="middle">STEP 1: AL-RIHLAH</text>
    <text x="92" y="52" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="10.5" font-weight="700" text-anchor="middle">TRANSCONTINENTAL TRAVEL</text>
    <text x="15" y="80" fill="#f8fafc" font-family="system-ui, sans-serif" font-size="10">• Traveling thousands of</text>
    <text x="15" y="96" fill="#f8fafc" font-family="system-ui, sans-serif" font-size="10">  miles on foot/camels</text>
    <text x="15" y="118" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="9.5">• Medina, Kufa, Basra,</text>
    <text x="15" y="134" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="9.5">  Damascus, Cairo, Makkah</text>
    <text x="15" y="156" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="9.5">• Rejecting hearsay: only</text>
    <text x="15" y="172" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="9.5">  direct face-to-face hearing</text>

    <rect x="12" y="210" width="160" height="75" rx="6" fill="#0f172a" stroke="#0369a1" stroke-width="1"/>
    <text x="92" y="230" fill="#fbbf24" font-family="system-ui, sans-serif" font-size="9.5" font-weight="700" text-anchor="middle">Famous Criterion:</text>
    <text x="92" y="248" fill="#94a3b8" font-family="system-ui, sans-serif" font-size="8.5" text-anchor="middle">Bukhari required proven</text>
    <text x="92" y="262" fill="#94a3b8" font-family="system-ui, sans-serif" font-size="8.5" text-anchor="middle">physical meeting (Liqa')</text>
  </g>

  <!-- Step 2: Jarh wa Ta'dil -->
  <g transform="translate(245, 95)" filter="url(#shadow8)">
    <rect width="185" height="300" rx="10" fill="#1e293b" stroke="#f59e0b" stroke-width="1.5"/>
    <rect width="185" height="34" rx="10" fill="#b45309"/>
    <text x="92" y="22" fill="#ffffff" font-family="system-ui, sans-serif" font-size="12" font-weight="800" text-anchor="middle">STEP 2: BIOGRAPHY</text>
    <text x="92" y="52" fill="#fbbf24" font-family="system-ui, sans-serif" font-size="10.5" font-weight="700" text-anchor="middle">JARH WA AL-TA'DIL</text>
    <text x="15" y="80" fill="#f8fafc" font-family="system-ui, sans-serif" font-size="10">• Rigorous narrator audit</text>
    <text x="15" y="100" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="9.5">• Interviewing neighbors,</text>
    <text x="15" y="116" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="9.5">  peers, and family</text>
    <text x="15" y="138" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="9.5">• Checking piety ('Adalah)</text>
    <text x="15" y="154" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="9.5">  and memory (Dabt)</text>
    <text x="15" y="176" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="9.5">• Horse deception test:</text>
    <text x="15" y="192" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="9.5">  zero tolerance for tricks</text>

    <rect x="12" y="210" width="160" height="75" rx="6" fill="#0f172a" stroke="#b45309" stroke-width="1"/>
    <text x="92" y="230" fill="#fbbf24" font-family="system-ui, sans-serif" font-size="9.5" font-weight="700" text-anchor="middle">Dual Verdict:</text>
    <text x="92" y="248" fill="#34d399" font-family="system-ui, sans-serif" font-size="8.5" text-anchor="middle">Ta'dil (Declared Trustworthy)</text>
    <text x="92" y="262" fill="#f87171" font-family="system-ui, sans-serif" font-size="8.5" text-anchor="middle">Jarh (Discredited/Rejected)</text>
  </g>

  <!-- Step 3: Textual Cross-Check -->
  <g transform="translate(445, 95)" filter="url(#shadow8)">
    <rect width="185" height="300" rx="10" fill="#1e293b" stroke="#10b981" stroke-width="1.5"/>
    <rect width="185" height="34" rx="10" fill="#047857"/>
    <text x="92" y="22" fill="#ffffff" font-family="system-ui, sans-serif" font-size="12" font-weight="800" text-anchor="middle">STEP 3: CROSS-CHECK</text>
    <text x="92" y="52" fill="#34d399" font-family="system-ui, sans-serif" font-size="10.5" font-weight="700" text-anchor="middle">MATN VERIFICATION</text>
    <text x="15" y="80" fill="#f8fafc" font-family="system-ui, sans-serif" font-size="10">• Gathering multiple chains</text>
    <text x="15" y="96" fill="#f8fafc" font-family="system-ui, sans-serif" font-size="10">  for the exact same text</text>
    <text x="15" y="118" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="9.5">• Word-by-word alignment</text>
    <text x="15" y="134" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="9.5">  across different regions</text>
    <text x="15" y="156" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="9.5">• Checking consistency with</text>
    <text x="15" y="172" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="9.5">  clear Qur'anic verses</text>

    <rect x="12" y="210" width="160" height="75" rx="6" fill="#0f172a" stroke="#047857" stroke-width="1"/>
    <text x="92" y="230" fill="#fbbf24" font-family="system-ui, sans-serif" font-size="9.5" font-weight="700" text-anchor="middle">Anomaly Detection:</text>
    <text x="92" y="248" fill="#94a3b8" font-family="system-ui, sans-serif" font-size="8.5" text-anchor="middle">Exposes accidental word</text>
    <text x="92" y="262" fill="#94a3b8" font-family="system-ui, sans-serif" font-size="8.5" text-anchor="middle">substitutions or slips</text>
  </g>

  <!-- Step 4: The Compilation -->
  <g transform="translate(645, 95)" filter="url(#shadow8)">
    <rect width="190" height="300" rx="10" fill="#1e293b" stroke="#a855f7" stroke-width="1.5"/>
    <rect width="190" height="34" rx="10" fill="#6d28d9"/>
    <text x="95" y="22" fill="#ffffff" font-family="system-ui, sans-serif" font-size="12" font-weight="800" text-anchor="middle">STEP 4: TADWIN</text>
    <text x="95" y="52" fill="#c084fc" font-family="system-ui, sans-serif" font-size="10.5" font-weight="700" text-anchor="middle">STRUCTURED PUBLISHING</text>
    <text x="15" y="80" fill="#f8fafc" font-family="system-ui, sans-serif" font-size="10">• Subject categorization</text>
    <text x="15" y="96" fill="#f8fafc" font-family="system-ui, sans-serif" font-size="10">  (Iman, Salah, Trade, etc.)</text>
    <text x="15" y="118" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="9.5">• Complete Sanad listed</text>
    <text x="15" y="134" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="9.5">  before every single report</text>
    <text x="15" y="156" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="9.5">• Bukhari filtered 600,000</text>
    <text x="15" y="172" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="9.5">  narrations to ~7,500</text>

    <rect x="12" y="210" width="166" height="75" rx="6" fill="#0f172a" stroke="#7e22ce" stroke-width="1"/>
    <text x="95" y="230" fill="#fbbf24" font-family="system-ui, sans-serif" font-size="9.5" font-weight="700" text-anchor="middle">Pious Practice:</text>
    <text x="95" y="248" fill="#94a3b8" font-family="system-ui, sans-serif" font-size="8.5" text-anchor="middle">Prayed Istikharah &amp; ghusl</text>
    <text x="95" y="262" fill="#94a3b8" font-family="system-ui, sans-serif" font-size="8.5" text-anchor="middle">before writing each Hadith</text>
  </g>
</svg>"""


def get_svg_lesson_9():
    """Lesson 2.1.9: Digital Hadith Source Check & Verification Form Mockup"""
    return """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 880 440" width="100%" height="100%">
  <defs>
    <linearGradient id="bg9" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#0f172a"/>
      <stop offset="50%" stop-color="#1e293b"/>
      <stop offset="100%" stop-color="#0f172a"/>
    </linearGradient>
    <linearGradient id="headerUi" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#0284c7"/>
      <stop offset="100%" stop-color="#0f766e"/>
    </linearGradient>
    <filter id="shadow9" x="-10%" y="-10%" width="120%" height="120%">
      <feDropShadow dx="0" dy="4" stdDeviation="6" flood-color="#000000" flood-opacity="0.5"/>
    </filter>
  </defs>

  <rect width="880" height="440" fill="url(#bg9)" rx="14"/>
  <rect x="15" y="15" width="850" height="410" fill="none" stroke="#334155" stroke-width="1.5" stroke-dasharray="6 4" rx="10"/>

  <text x="440" y="42" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="17" font-weight="800" text-anchor="middle">DIGITAL HADITH SOURCE VERIFICATION PROTOCOL</text>
  <text x="440" y="64" fill="#94a3b8" font-family="system-ui, sans-serif" font-size="12" text-anchor="middle">Standard 4-Point Source Audit Required Before Quoting or Sharing Religious Reports Online</text>

  <!-- Form Container UI Mockup -->
  <g transform="translate(100, 85)" filter="url(#shadow9)">
    <rect width="680" height="325" rx="12" fill="#1e293b" stroke="#38bdf8" stroke-width="1.6"/>
    <rect width="680" height="38" rx="12" fill="url(#headerUi)"/>
    <circle cx="25" cy="19" r="5" fill="#ef4444"/>
    <circle cx="42" cy="19" r="5" fill="#f59e0b"/>
    <circle cx="59" cy="19" r="5" fill="#10b981"/>
    <text x="340" y="24" fill="#ffffff" font-family="system-ui, sans-serif" font-size="12" font-weight="700" text-anchor="middle">VLearn Digital Hadith Validator — Online Source Sincerity</text>

    <!-- Field 1: Matn (Text) -->
    <g transform="translate(30, 52)">
      <text x="0" y="14" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="11" font-weight="700">1. QUOTED STATEMENT (MATN):</text>
      <rect x="0" y="22" width="620" height="32" rx="6" fill="#0f172a" stroke="#475569" stroke-width="1"/>
      <text x="15" y="43" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="11" font-style="italic">"None of you truly believes until he loves for his brother what he loves for himself."</text>
      <text x="600" y="43" fill="#10b981" font-family="system-ui, sans-serif" font-size="14" font-weight="900" text-anchor="end">✓</text>
    </g>

    <!-- Field 2: Source Book -->
    <g transform="translate(30, 118)">
      <rect width="195" height="75" rx="8" fill="#0f172a" stroke="#10b981" stroke-width="1.2"/>
      <text x="15" y="22" fill="#94a3b8" font-family="system-ui, sans-serif" font-size="9.5" font-weight="700">SOURCE COMPILATION:</text>
      <text x="15" y="42" fill="#f8fafc" font-family="system-ui, sans-serif" font-size="12" font-weight="800">Sahih al-Bukhari</text>
      <text x="15" y="60" fill="#34d399" font-family="system-ui, sans-serif" font-size="10">Hadith #13 (Book of Iman)</text>
      <circle cx="175" cy="20" r="8" fill="#10b981"/>
      <text x="175" y="24" fill="#ffffff" font-family="system-ui, sans-serif" font-size="9" font-weight="900" text-anchor="middle">✓</text>
    </g>

    <!-- Field 3: Primary Narrator -->
    <g transform="translate(242, 118)">
      <rect width="195" height="75" rx="8" fill="#0f172a" stroke="#10b981" stroke-width="1.2"/>
      <text x="15" y="22" fill="#94a3b8" font-family="system-ui, sans-serif" font-size="9.5" font-weight="700">PRIMARY NARRATOR:</text>
      <text x="15" y="42" fill="#f8fafc" font-family="system-ui, sans-serif" font-size="12" font-weight="800">Anas ibn Malik (RA)</text>
      <text x="15" y="60" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="10">Direct eyewitness Sahabi</text>
      <circle cx="175" cy="20" r="8" fill="#10b981"/>
      <text x="175" y="24" fill="#ffffff" font-family="system-ui, sans-serif" font-size="9" font-weight="900" text-anchor="middle">✓</text>
    </g>

    <!-- Field 4: Grading -->
    <g transform="translate(455, 118)">
      <rect width="195" height="75" rx="8" fill="#0f172a" stroke="#10b981" stroke-width="1.2"/>
      <text x="15" y="22" fill="#94a3b8" font-family="system-ui, sans-serif" font-size="9.5" font-weight="700">SCHOLARLY GRADING:</text>
      <text x="15" y="42" fill="#34d399" font-family="system-ui, sans-serif" font-size="12" font-weight="800">SAHIH (Muttafaqun 'Alayh)</text>
      <text x="15" y="60" fill="#a7f3d0" font-family="system-ui, sans-serif" font-size="10">Highest possible consensus</text>
      <circle cx="175" cy="20" r="8" fill="#10b981"/>
      <text x="175" y="24" fill="#ffffff" font-family="system-ui, sans-serif" font-size="9" font-weight="900" text-anchor="middle">✓</text>
    </g>

    <!-- Validation Status Banner -->
    <g transform="translate(30, 208)">
      <rect width="620" height="50" rx="8" fill="#064e3b" stroke="#10b981" stroke-width="1.2"/>
      <text x="310" y="24" fill="#34d399" font-family="system-ui, sans-serif" font-size="12" font-weight="800" text-anchor="middle">STATUS: ALL 4 VERIFICATION FIELDS CONFIRMED</text>
      <text x="310" y="40" fill="#a7f3d0" font-family="system-ui, sans-serif" font-size="10" text-anchor="middle">This Hadith meets authentic standards and is approved for citing, quoting, and sharing.</text>
    </g>

    <!-- Golden Action Rule -->
    <text x="340" y="285" fill="#f59e0b" font-family="system-ui, sans-serif" font-size="10.5" font-weight="700" text-anchor="middle">GOLDEN RULE: If Source, Narrator, or Grading is UNKNOWN or 'NOT SUPPLIED' → DO NOT FORWARD!</text>
  </g>
</svg>"""


def get_svg_lesson_10():
    """Lesson 2.1.10: Master Comprehensive Architecture of Ulum al-Hadith"""
    return """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 880 440" width="100%" height="100%">
  <defs>
    <linearGradient id="bg10" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#0f172a"/>
      <stop offset="50%" stop-color="#1e293b"/>
      <stop offset="100%" stop-color="#0f172a"/>
    </linearGradient>
    <linearGradient id="centerPillar" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#f59e0b"/>
      <stop offset="100%" stop-color="#d97706"/>
    </linearGradient>
    <filter id="shadow10" x="-10%" y="-10%" width="120%" height="120%">
      <feDropShadow dx="0" dy="4" stdDeviation="6" flood-color="#000000" flood-opacity="0.5"/>
    </filter>
  </defs>

  <rect width="880" height="440" fill="url(#bg10)" rx="14"/>
  <rect x="15" y="15" width="850" height="410" fill="none" stroke="#334155" stroke-width="1.5" stroke-dasharray="6 4" rx="10"/>

  <text x="440" y="40" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="17" font-weight="800" text-anchor="middle">MASTER ARCHITECTURE OF ULUM AL-HADITH</text>
  <text x="440" y="60" fill="#94a3b8" font-family="system-ui, sans-serif" font-size="12" text-anchor="middle">Comprehensive Synthesis of Sciences, Classifications, and Modern Custody Responsibilities</text>

  <!-- Quadrant 1: Definition & Anatomy (Top Left) -->
  <g transform="translate(45, 80)" filter="url(#shadow10)">
    <rect width="250" height="150" rx="10" fill="#1e293b" stroke="#0ea5e9" stroke-width="1.5"/>
    <text x="125" y="24" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="12" font-weight="700" text-anchor="middle">1. ANATOMY OF A HADITH</text>
    <line x1="20" y1="34" x2="230" y2="34" stroke="#334155"/>
    <text x="15" y="55" fill="#f8fafc" font-family="system-ui, sans-serif" font-size="11" font-weight="700">• ISNAD (The Chain):</text>
    <text x="25" y="72" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10">Sequence of narrators back to Prophet</text>
    <text x="15" y="95" fill="#f8fafc" font-family="system-ui, sans-serif" font-size="11" font-weight="700">• MATN (The Text):</text>
    <text x="25" y="112" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10">Actual words, actions, or silent approval</text>
    <text x="15" y="134" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="9.5">Both parts audited independently</text>
  </g>

  <!-- Quadrant 2: The Three Generations (Bottom Left) -->
  <g transform="translate(45, 245)" filter="url(#shadow10)">
    <rect width="250" height="150" rx="10" fill="#1e293b" stroke="#10b981" stroke-width="1.5"/>
    <text x="125" y="24" fill="#34d399" font-family="system-ui, sans-serif" font-size="12" font-weight="700" text-anchor="middle">2. BLESSED GENERATIONS</text>
    <line x1="20" y1="34" x2="230" y2="34" stroke="#334155"/>
    <text x="15" y="55" fill="#fbbf24" font-family="system-ui, sans-serif" font-size="10.5" font-weight="700">1. AS-SAHABAH (Companions)</text>
    <text x="25" y="70" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="9.5">Direct eyewitnesses &amp; memorizers</text>
    <text x="15" y="90" fill="#34d399" font-family="system-ui, sans-serif" font-size="10.5" font-weight="700">2. AT-TABI'UN (Successors)</text>
    <text x="25" y="105" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="9.5">Official written compilation begun</text>
    <text x="15" y="125" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="10.5" font-weight="700">3. ATBA' AL-TABI'IN</text>
    <text x="25" y="140" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="9.5">Standardized sciences and early books</text>
  </g>

  <!-- Center Core Pillar: Kutub al-Sittah (The Six Books) -->
  <g transform="translate(315, 80)" filter="url(#shadow10)">
    <rect width="250" height="315" rx="12" fill="#1e293b" stroke="#f59e0b" stroke-width="1.8"/>
    <rect width="250" height="36" rx="12" fill="url(#centerPillar)"/>
    <text x="125" y="24" fill="#0f172a" font-family="system-ui, sans-serif" font-size="13" font-weight="800" text-anchor="middle">AL-KUTUB AL-SITTAH</text>

    <text x="15" y="58" fill="#fbbf24" font-family="system-ui, sans-serif" font-size="11" font-weight="700">THE TWO SAHIHS (Gold Standard):</text>
    <text x="20" y="76" fill="#f8fafc" font-family="system-ui, sans-serif" font-size="10.5">• Sahih al-Bukhari (d. 256 AH)</text>
    <text x="20" y="94" fill="#f8fafc" font-family="system-ui, sans-serif" font-size="10.5">• Sahih Muslim (d. 261 AH)</text>

    <line x1="20" y1="110" x2="230" y2="110" stroke="#334155"/>

    <text x="15" y="132" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="11" font-weight="700">THE FOUR SUNAN (Legal/Moral):</text>
    <text x="20" y="152" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10">• Sunan Abu Dawood (Ahkam)</text>
    <text x="20" y="170" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10">• Jami' at-Tirmidhi (Gradings)</text>
    <text x="20" y="188" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10">• Sunan an-Nasa'i (Strictness)</text>
    <text x="20" y="206" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10">• Sunan Ibn Majah (Comprehensiveness)</text>

    <rect x="15" y="225" width="220" height="75" rx="8" fill="#0f172a" stroke="#d97706" stroke-width="1"/>
    <text x="125" y="245" fill="#fbbf24" font-family="system-ui, sans-serif" font-size="10" font-weight="700" text-anchor="middle">ACADEMIC METHODOLOGY:</text>
    <text x="20" y="265" fill="#94a3b8" font-family="system-ui, sans-serif" font-size="9">• Transcontinental Rihlah (travel)</text>
    <text x="20" y="280" fill="#94a3b8" font-family="system-ui, sans-serif" font-size="9">• Jarh wa Ta'dil (character audit)</text>
    <text x="20" y="294" fill="#94a3b8" font-family="system-ui, sans-serif" font-size="9">• Cross-checking multiple variants</text>
  </g>

  <!-- Quadrant 3: 3-Tier Classification (Top Right) -->
  <g transform="translate(585, 80)" filter="url(#shadow10)">
    <rect width="250" height="150" rx="10" fill="#1e293b" stroke="#a855f7" stroke-width="1.5"/>
    <text x="125" y="24" fill="#c084fc" font-family="system-ui, sans-serif" font-size="12" font-weight="700" text-anchor="middle">3. THREE AUTHENTICITY TIERS</text>
    <line x1="20" y1="34" x2="230" y2="34" stroke="#334155"/>
    <text x="15" y="55" fill="#34d399" font-family="system-ui, sans-serif" font-size="10.5" font-weight="700">1. SAHIH (5/5 Conditions Met):</text>
    <text x="25" y="70" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="9.5">Highest grade; binding on law &amp; creed</text>
    <text x="15" y="90" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="10.5" font-weight="700">2. HASAN (Good / Reliable):</text>
    <text x="25" y="105" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="9.5">Lighter memory precision; fully valid</text>
    <text x="15" y="125" fill="#f87171" font-family="system-ui, sans-serif" font-size="10.5" font-weight="700">3. DHA'IF (Weak):</text>
    <text x="25" y="140" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="9.5">Lacks conditions; strictly not for law/creed</text>
  </g>

  <!-- Quadrant 4: Modern Responsible Custody (Bottom Right) -->
  <g transform="translate(585, 245)" filter="url(#shadow10)">
    <rect width="250" height="150" rx="10" fill="#1e293b" stroke="#f59e0b" stroke-width="1.5"/>
    <text x="125" y="24" fill="#fbbf24" font-family="system-ui, sans-serif" font-size="12" font-weight="700" text-anchor="middle">4. DIGITAL RESPONSIBILITY</text>
    <line x1="20" y1="34" x2="230" y2="34" stroke="#334155"/>
    <text x="15" y="55" fill="#f8fafc" font-family="system-ui, sans-serif" font-size="10.5" font-weight="700">• Check 4 Mandatory Fields:</text>
    <text x="25" y="72" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="9.5">Source book, Narrator, Matn, Grading</text>
    <text x="15" y="95" fill="#f87171" font-family="system-ui, sans-serif" font-size="10.5" font-weight="700">• Reject Chain Messages:</text>
    <text x="25" y="112" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="9.5">Never forward unverified claims</text>
    <text x="15" y="135" fill="#34d399" font-family="system-ui, sans-serif" font-size="10" font-weight="700">Core Value: Amanah (Integrity)</text>
  </g>
</svg>"""


# ─── DATA MATRIX FOR ALL 10 LESSONS ───────────────────────────────────────────

LESSONS_DATA = [
    # ─── LESSON 2.1.1 ───────────────────────────────────────────────────────────
    {
        "unit_order": 1,
        "unit_name": "Lesson 2.1.1: Hadith as guidance",
        "unit_description": "Examines the nature of Hadith, its vital complementary role alongside the Qur'an, and its legal authority as a source of Islamic guidance.",
        "lesson_title": "Hadith as Guidance",
        "diagram_title": "Qur'an and Sunnah Complementary Relationship Architecture",
        "svg_fn": get_svg_lesson_1,
        "image": {
            "title": "Historical Manuscript of Hadith Transmission",
            "url": "https://upload.wikimedia.org/wikipedia/commons/f/f4/A_manuscript_about_hadiths%2C_in_nasta%27liq%2C_1559.jpg",
            "caption": "Classical 16th-century manuscript illustrating preserved Hadith traditions and textual transmission chains.",
            "author": "Persian Calligrapher (1559 CE)",
            "licensing": "Public Domain",
            "source": "Wikimedia Commons"
        },
        "youtube": {
            "title": "Introduction to the Sciences of Hadith (Class 1)",
            "youtube_id": "ddorxxHB62w",
            "description": "Comprehensive pedagogical introduction to Hadith sciences and the foundational collections of the Sunnah."
        },
        "inquiry_question": "What is Hadith, and what is its role as a source of Islamic guidance alongside the Qur'an?",
        "connection": "Imagine buying a highly advanced camera. It comes with a primary manual (which explains what the camera does) and a practical quick-start video guide (which shows you exactly how a professional photographer holds the camera, presses the buttons, and takes beautiful photos in real life). In Islam, the Qur'an is the primary divine manual of guidance, and the Hadith of the Prophet Muhammad (PBUH) is the practical, living demonstration of how to implement those divine teachings in our daily lives.",
        "goals": [
            "Define the terms Hadith and Sunnah and differentiate between their forms (words, actions, silent approvals, characteristics).",
            "Explain the three vital functions of Hadith in relation to the Qur'an (Bayan, Takhsis, Tashri' Idaphi).",
            "Demonstrate why religious duties like Salah (daily prayer) cannot be practiced without the Hadith."
        ],
        "authoritative_concept": """### Authoritative Concepts: Hadith and Sunnah

- **Hadith (حديث):** A reported transmission of the sayings (*qawl*), physical actions (*fi'l*), silent approvals (*taqrir*), or noble physical and moral characteristics (*sifah*) of the Prophet Muhammad (PBUH).
- **Sunnah (سنة):** The actual established lifestyle, model practices, and lived tradition of the Prophet Muhammad (PBUH). The Hadith is the recorded, textual medium through which the Sunnah is transmitted to subsequent generations.
- **Secondary Source of Islamic Law:** Hadith stands as the second supreme authority in Islamic jurisprudence (*Shariah*), immediately following the Holy Qur'an. It possesses legal authority (*hujjiyyah*) by divine decree, serving to clarify, elaborate, and implement divine revelation in human history.""",
        "scripture_panel": """### Scripture & Sources Panel

> *"And We revealed to you the message [O Muhammad] that you may make clear to the people what was sent down to them and that they might give thought."*
> — **Surah An-Nahl (16:44)**

> *"He who obeys the Messenger has obeyed Allah; but those who turn away - We have not sent you over them as a guardian."*
> — **Surah An-Nisa (4:80)**

> The Prophet Muhammad (PBUH) stated:
> *"Pray as you have seen me praying."*
> — **Sahih al-Bukhari (631)**""",
        "deep_explanation": """### The Threefold Functional Relationship of Hadith to the Qur'an

Islamic jurists categorize the explanatory authority of Hadith into three indispensable functions:

1. **Clarification and Elaboration (*Bayan al-Mujmal*):**
   - The Qur'an issues universal legal commands without detailing their exact mechanical procedures. For instance, the Qur'an repeatedly commands believers to "establish prayer" (*Aqim al-Salah*) and "pay zakah" (*Atu al-Zakah*).
   - However, the Qur'an does not specify the five daily prayer times, the exact number of units (*rak'ahs*), the recitation procedures, the bows (*ruku'*), or prostrations (*sujud*).
   - The Hadith provides the exhaustive, living demonstration: the Prophet's instruction, *"Pray as you have seen me praying"* (Sahih al-Bukhari).

2. **Specification of the General (*Takhsis al-'Amm*):**
   - The Qur'an frequently establishes general legal principles. For example, it permits commerce and forbids usury (*riba*).
   - The Hadith specifies which precise trade contracts are permissible and which constitute deceit (*gharar*), monopolies (*ihtikar*), or unjust exploitation.

3. **Autonomous Supplementary Rulings (*Tashri' Idaphi*):**
   - The Hadith establishes secondary ethical directives, dietary boundaries, and social decencies not explicitly detailed in the Qur'an, such as the prohibition of wearing silk and gold for men, and detailed manners of eating and neighborliness.""",
        "comparison_table": {
            "title": "Comparative Analysis: The Holy Qur'an vs. The Prophetic Hadith",
            "headers": ["Dimension", "The Holy Qur'an", "The Prophetic Hadith"],
            "rows": [
                ["Source & Nature", "Direct literal Word of Allah (Kalamullah)", "Words, actions, and approvals of Prophet Muhammad (PBUH)"],
                ["Language & Wording", "Miraculous, inimitable divine Arabic phrasing", "Prophetic phrasing expressing divinely guided wisdom"],
                ["Jurisprudential Role", "Primary, supreme constitutional source", "Secondary, indispensable explanatory and specifying source"],
                ["Recitation in Rituals", "Recited verbatim as worship in Salah", "Studied for guidance; not recited in place of Qur'an in Salah"],
                ["Practical Scope", "Universal theological, moral, and legal principles", "Concrete real-life application, details, and behavioral demonstrations"]
            ]
        },
        "worked_example": {
            "scenario": "In an online forum, a user writes: 'We only need to follow the Qur'an. It is the perfect word of Allah. We don't need Hadith books.' Halima, reading this, discusses it with her teacher, Mr. Khalid. Mr. Khalid says, 'Halima, ask them: how do they perform Salah? The Qur'an commands us to pray, but the steps, times, and words of the prayer are not written in the Qur'an. They are only preserved in the Hadith. The Prophet (PBUH) said, \"Pray as you have seen me praying.\" To follow the Qur'an's command to pray, we must look to the Hadith for the practical steps. The Hadith is indispensable for living as a Muslim.'",
            "analysis": "This scenario demonstrates that the Qur'an and Hadith are inseparable. Rejecting Hadith makes it impossible to implement the Qur'an's explicit commands.",
            "takeaway": "The Hadith is not an optional extra; it is the practical key that unlocks the execution of Qur'anic commands."
        },
        "real_world_application": "When studying Islamic practices, always connect the rule to its prophetic model. For example, when you learn about the importance of good character or hygiene, look up how the Prophet (PBUH) smiled, cleaned his teeth with the miswak, and spoke kindly to children. Emulating these specific practices turns your daily routines into rewarding acts of worship.",
        "reflection": "Why did Allah send a human messenger to deliver His book instead of just sending down a written book from heaven? How does a living role model help us practice moral values far more effectively than abstract text alone?",
        "misconception": {
            "misconception": "Some people believe that Muslims can practice Islam completely by reading only the Qur'an and ignoring the Hadith.",
            "correction": "The Qur'an itself commands believers to obey the Prophet (4:80) and informs us that his role is to make clear what was revealed (16:44). Without Hadith, fundamental pillars like Salah, Sawm, Zakah, and Hajj cannot be performed."
        },
        "mcq": {
            "question": "What is the primary relationship between the Qur'an and the Hadith in Islamic law and practice?",
            "options": [
                "A) The Hadith replaces the Qur'an as the primary source of law",
                "B) The Hadith provides the practical explanation, details, and real-life demonstration of the general principles revealed in the Qur'an",
                "C) The Hadith is only a collection of Arabian historical poetry without legal authority",
                "D) The Hadith is identical to the Qur'an in its literal divine Arabic wording"
            ],
            "answer": "B",
            "explanation": "The Hadith is the secondary, authoritative source of Islamic law that clarifies, specifies, and demonstrates how to implement the divine principles of the Qur'an in daily life."
        },
        "summary": {
            "key_points": [
                "Hadith refers to the recorded sayings, actions, silent approvals, and characteristics of the Prophet Muhammad (PBUH).",
                "Sunnah represents the living model of the Prophet; Hadith is its textual documentation.",
                "Hadith serves three critical roles: Bayan (explanation), Takhsis (specification), and Tashri' Idaphi (supplementary rulings).",
                "The Qur'an and Hadith are complementary and inseparable; essential worship like Salah cannot be performed without Hadith."
            ],
            "vocabulary": [
                {"term": "Hadith (حديث)", "definition": "A recorded report of the Prophet's words, actions, approvals, or qualities."},
                {"term": "Sunnah (سنة)", "definition": "The practical lifestyle, traditions, and exemplary path of the Prophet."},
                {"term": "Bayan (بيان)", "definition": "The explanatory function of Hadith clarifying ambiguous or general Qur'anic verses."},
                {"term": "Taqrir (تقرير)", "definition": "Silent approval granted by the Prophet when witnessing a companion's action."}
            ]
        },
        "exit_ticket": "State one major reason why it is impossible for a Muslim to perform daily prayers (Salah) without relying upon the Hadith."
    },

    # ─── LESSON 2.1.2 ───────────────────────────────────────────────────────────
    {
        "unit_order": 2,
        "unit_name": "Lesson 2.1.2: The six authentic Books (Kutub al-Sittah)",
        "unit_description": "Explores the canonical Kutub al-Sittah compilations of the 3rd century AH, their compilers, structural differences, and classification tiers.",
        "lesson_title": "The Six Authentic Books (Kutub al-Sittah)",
        "diagram_title": "The Kutub al-Sittah (Six Books) Classification Hierarchy",
        "svg_fn": get_svg_lesson_2,
        "image": {
            "title": "Classical Printed Edition of Sahih al-Bukhari",
            "url": "https://upload.wikimedia.org/wikipedia/commons/8/80/Sahih_al-Bukhari%2C_1890s_%282024-04-02%29.jpg",
            "caption": "An authentic historical 1890s print edition of Sahih al-Bukhari displaying organized chapters and narrator chains.",
            "author": "Ottoman Publisher (1890s)",
            "licensing": "Public Domain",
            "source": "Wikimedia Commons"
        },
        "youtube": {
            "title": "Most Authentic Books of Hadith | Al Kutub As Sittah",
            "youtube_id": "ddorxxHB62w",
            "description": "In-depth overview of the Six Canonical Books of Hadith, their author biographies, and criteria of authenticity."
        },
        "inquiry_question": "What are the six authentic collections of Hadith (Kutub al-Sittah), and why are they regarded as the highest reference works in Islamic scholarship?",
        "connection": "Imagine you are a medical researcher searching for the most reliable, peer-reviewed, and rigorously audited scientific findings. You would consult the world's most prestigious medical journals because their editors apply the most uncompromising standards before publishing any discovery. In Hadith studies, scholars recorded tens of thousands of narrations, but six books stand out as the most authentic, verified, and systematically organized compendiums in Islamic history. Knowing these 'Six Books' is foundational to understanding authentic Islamic guidance.",
        "goals": [
            "Identify the titles and compilers of the Kutub al-Sittah (Six Books).",
            "Distinguish between Al-Sahihayn (The Two Sahihs) and Al-Sunan al-Arba'ah (The Four Sunan).",
            "Appreciate the lifelong dedication of classical scholars in preserving the authentic Sunnah."
        ],
        "authoritative_concept": """### The Six Canonical Compilations (Al-Kutub al-Sittah)

During the 3rd Century of the Islamic Hijrah calendar—known as the Golden Age of Hadith scholarship—six eminent scholars compiled definitive compendiums:

1. **Sahih al-Bukhari:** Compiled by Imam Muhammad ibn Isma'il al-Bukhari (194–256 AH / 810–870 CE). Universally recognized by Islamic consensus as the most authentic book after the Qur'an.
2. **Sahih Muslim:** Compiled by Imam Muslim ibn al-Hajjaj al-Qushayri (204–261 AH / 820–875 CE). Celebrated for its rigorous thematic organization and preservation of chain variations.
3. **Sunan Abu Dawood:** Compiled by Imam Abu Dawood Sulayman ibn al-Ash'ath (202–275 AH). Focuses primarily on legal narrations (*ahkam*) foundational to jurisprudence.
4. **Jami' at-Tirmidhi:** Compiled by Imam Abu Isa Muhammad at-Tirmidhi (209–279 AH). Famous for pioneered grading notations (Sahih, Hasan, Gharib) and comparative juristic rulings.
5. **Sunan an-Nasa'i (Al-Mujtaba):** Compiled by Imam Ahmad ibn Shu'ayb an-Nasa'i (215–303 AH). Noted for its exceedingly strict standards in narrator vetting.
6. **Sunan Ibn Majah:** Compiled by Imam Muhammad ibn Yazid Ibn Majah (209–273 AH). Renowned for its comprehensive chapter arrangement and unique narrations.""",
        "scripture_panel": """### Classical Scholarly Consensus on Kutub al-Sittah

> *"The scholars of Islam are united in consensus that Sahih al-Bukhari and Sahih Muslim are the two soundest and most authentic books after the Book of Allah the Almighty."*
> — **Imam an-Nawawi (Introduction to Sharh Sahih Muslim)**

> *"I did not include any hadith in my Sahih except that I first took a bath (ghusl) and prayed two rak'ahs of Istikharah (prayer seeking divine guidance)."*
> — **Imam Muhammad ibn Isma'il al-Bukhari**""",
        "deep_explanation": """### The Two Structural Tiers of Kutub al-Sittah

The Six Books are fundamentally organized into two distinct methodological tiers:

1. **Tier 1: Al-Sahihayn (The Two Sahihs — Bukhari & Muslim):**
   - **Exclusive Authenticity Mandate:** Both Imam al-Bukhari and Imam Muslim committed themselves to recording *only* Hadiths meeting the highest threshold of authenticity (*Sahih*).
   - **Flawless Sanad:** Every narrator in their chains possessed impeccable moral integrity (*'adalah*) and flawless memory (*dabt tamm*), with verified chronological and geographical connection.
   - **Scholarly Authority:** Every single Hadith in these two works is accepted as definitive legal and theological evidence.

2. **Tier 2: Al-Sunan al-Arba'ah (The Four Sunan — Abu Dawood, Tirmidhi, Nasa'i, Ibn Majah):**
   - **Focus on Legal Traditions (*Ahkam*):** These scholars aimed to provide comprehensive compendiums for Islamic judges and muftis dealing with practical law, contracts, and worship.
   - **Broader Grading Spectrum:** In addition to *Sahih* reports, they deliberately included *Hasan* (good) narrations, and occasionally *Dha'if* (weak) reports while explicitly highlighting their chain weaknesses for academic scrutiny.
   - **Distinction:** A narration appearing in one of the Sunan is not automatically 100% Sahih; it requires verifying the compiler's or later critics' specific grading.""",
        "comparison_table": {
            "title": "Summary Matrix: The Canonical Six Books (Al-Kutub al-Sittah)",
            "headers": ["Book Title", "Compiler", "Lifespan (AH)", "Primary Thematic Focus", "Authenticity Level"],
            "rows": [
                ["Sahih al-Bukhari", "Imam al-Bukhari", "194–256 AH", "Beliefs, Law, Ethics, History", "100% Sahih (Highest in Islam)"],
                ["Sahih Muslim", "Imam Muslim", "204–261 AH", "Faith, Legal Rulings, Ethics", "100% Sahih (Unanimous Consensus)"],
                ["Sunan Abu Dawood", "Imam Abu Dawood", "202–275 AH", "Jurisprudence & Legal Judgments", "Predominantly Sahih & Hasan"],
                ["Jami' at-Tirmidhi", "Imam at-Tirmidhi", "209–279 AH", "Hadith Gradings & Madhhab Opinions", "Sahih, Hasan, and noted Weak"],
                ["Sunan an-Nasa'i", "Imam an-Nasa'i", "215–303 AH", "Strict Legal Rulings & Flaw Checks", "Very High Authenticity standard"],
                ["Sunan Ibn Majah", "Imam Ibn Majah", "209–273 AH", "General Legal & Practical Chapters", "Sahih, Hasan, and some Weak"]
            ]
        },
        "worked_example": {
            "scenario": "Zainab is writing an essay on Islamic ethics and wants to quote a Hadith about honesty. She finds a quote on a social media page that says, 'Be honest even if it harms you.' She wants to use it but doesn't know if it's reliable. Her older brother, who studies Islamic law, says, 'Zainab, look at the citation of the Hadith. Does it say it was compiled in Sahih al-Bukhari or Sahih Muslim, or one of the Sunan books? Yes, it says: \"Recorded in Sahih al-Bukhari, Book of Good Manners.\" This means it has passed through the rigorous verification of the greatest Hadith compilers, and you can quote it with absolute confidence.'",
            "analysis": "Citing the canonical source book provides verifiable provenance and guarantees that the report is anchored in peer-reviewed classical scholarship.",
            "takeaway": "Always look for canonical compilation citations (Bukhari, Muslim, etc.) before sharing or relying on religious quotes."
        },
        "real_world_application": "Whenever you prepare a religious speech, write a school paper, or study a moral topic, practice 'Source Sincerity.' Look up the compilation name. Citing recognized works like Bukhari, Muslim, Abu Dawood, or Tirmidhi demonstrates academic integrity, protects you from fabricated quotes, and commands intellectual respect.",
        "reflection": "Why did classical compilers like Imam al-Bukhari travel thousands of miles on foot and by camel across deserts to verify single Hadiths? What does their sacrifice teach us about the value of truthfulness and academic responsibility?",
        "misconception": {
            "misconception": "Some people believe that every single Hadith found in all six books is of identical authenticity to Sahih al-Bukhari.",
            "correction": "While Sahih al-Bukhari and Sahih Muslim contain exclusively authentic (Sahih) reports, the four Sunan books contain Sahih, Hasan, and some Dha'if reports accompanied by critical commentary."
        },
        "mcq": {
            "question": "Which of the following books is unanimously regarded by Islamic scholars as the most authentic collection of Hadith, applying the strictest verification criteria?",
            "options": [
                "A) Sunan Ibn Majah",
                "B) Sahih al-Bukhari",
                "C) Sunan Abu Dawood",
                "D) Jami' at-Tirmidhi"
            ],
            "answer": "B",
            "explanation": "Sahih al-Bukhari, compiled by Imam al-Bukhari, is recognized by unanimous scholarly consensus as the most authentic and rigorously verified book after the Holy Qur'an."
        },
        "summary": {
            "key_points": [
                "The Kutub al-Sittah are the six premier Hadith collections compiled during the 3rd century AH.",
                "Al-Sahihayn (Bukhari and Muslim) represent the gold standard of 100% authentic narrations.",
                "The Four Sunan (Abu Dawood, Tirmidhi, Nasa'i, Ibn Majah) focus on legal rulings and include both Sahih and Hasan narrations with critical scholarly notes.",
                "Knowing the Six Books enables Muslims to practice source verification and distinguish authentic reports from unverified claims."
            ],
            "vocabulary": [
                {"term": "Al-Kutub al-Sittah (الكتب الستة)", "definition": "The six canonical Sunni Hadith compilations."},
                {"term": "Al-Sahihayn (الصحيحان)", "definition": "The 'Two Sahihs' of Imam al-Bukhari and Imam Muslim."},
                {"term": "Sunan (سنن)", "definition": "Hadith collections arranged specifically around chapters of jurisprudence (fiqh)."},
                {"term": "Ahkam (أحكام)", "definition": "Practical legal rulings defining obligatory, permissible, and prohibited actions."}
            ]
        },
        "exit_ticket": "Name the compilers of the 'Two Sahihs' (Al-Sahihayn) and state in one sentence why their works hold the highest authority."
    },

    # ─── LESSON 2.1.3 ───────────────────────────────────────────────────────────
    {
        "unit_order": 3,
        "unit_name": "Lesson 2.1.3: Why Hadith was collected",
        "unit_description": "Analyzes the historical imperatives that necessitated the written collection and compilation of Hadith, including demographic changes and preservation needs.",
        "lesson_title": "Why Hadith Was Collected",
        "diagram_title": "Three Historical Phases of Hadith Preservation Timeline",
        "svg_fn": get_svg_lesson_3,
        "image": {
            "title": "Historical Mosque of the Prophet in Medina",
            "url": "https://upload.wikimedia.org/wikipedia/commons/0/0a/Abu_Bakr_Mosque%2C_Medina_%28Interior%29.jpg",
            "caption": "Historic prayer hall in Medina, the epicenter where the Prophet's companions originally gathered and memorized the Sunnah.",
            "author": "Islamic Heritage Archive",
            "licensing": "Creative Commons Attribution-ShareAlike",
            "source": "Wikimedia Commons"
        },
        "youtube": {
            "title": "How The First Hadith Book Was Compiled | Dr. Omar Suleiman",
            "youtube_id": "Rywpb0ZYR3c",
            "description": "Historical exploration of the factors that triggered the written compilation of Hadith from the Sahabah through the early Caliphates."
        },
        "inquiry_question": "Why was it necessary for the Muslim community to transition from oral memory to systematic written Hadith collections?",
        "connection": "Imagine a revered grandmother who is the sole living guardian of your family's centuries-old history and recipes. As long as she lives in the family house, anyone can ask her directly. But as generations grow, family branches migrate to distant continents, and the grandmother advances in years, everyone realizes: 'If we do not record her exact words into a permanent book, our ancestral heritage will be distorted or lost forever.' When the Prophet (PBUH) was alive, Muslims asked him directly. But as companions passed away and Islam crossed three continents, systematic compilation became an urgent spiritual and cultural necessity.",
        "goals": [
            "Explain the three historical factors that necessitated the written compilation of Hadith.",
            "Describe the chronological evolution from oral memorization to written archives.",
            "Identify the role of the pious Caliph Umar ibn Abdul Aziz in formalizing statewide compilation."
        ],
        "authoritative_concept": """### Factors Necessitating the Compilation of Hadith

The transition from individual oral retention to systematic, codified written books was driven by three urgent historical realities:

1. **The Demise of Key Eyewitness Companions:**
   - In the initial decades, thousands of companions who had heard the Prophet firsthand began passing away through age and battles. With their demise came the alarming danger of oral knowledge disappearing (*Dhihab al-'Ilm*).

2. **Rapid Geographical Expansion Across Continents:**
   - Within 50 years of the Prophet's death, the Islamic state encompassed Arabia, Egypt, Syria, North Africa, and Persia.
   - Millions of non-Arab converts entered Islam without ever seeing the Prophet or knowing the cultural nuances of Medina. Written, verified reference manuals were urgently required to standardize worship and legal adjudications.

3. **The Emergence of Political Sects and Fabrications (*Mawdu'at*):**
   - After the political conflicts during the Caliphates of Uthman and Ali (RA), deviating groups began inventing false statements and attributing them to the Prophet to bolster political factions.
   - Scholars recognized that an uncompromising, documented paper trail (*Isnad*) was essential to isolate and eliminate fabrications.""",
        "scripture_panel": """### The Historic Decree of Caliph Umar ibn Abdul Aziz (d. 101 AH)

> Caliph Umar ibn Abdul Aziz issued an official imperial directive to Abu Bakr ibn Muhammad ibn Hazm, Governor of Medina:
> *"Search for the Hadiths of the Messenger of Allah (PBUH) and write them down, for I fear the disappearance of religious knowledge and the passing away of the scholars."*
> — **Sahih al-Bukhari, Book of Knowledge**

> The Prophet Muhammad (PBUH) stated:
> *"May Allah brighten the face of a person who hears a statement from us, memorizes it, understands it, and conveys it to others just as he heard it."*
> — **Jami' at-Tirmidhi (2658)**""",
        "deep_explanation": """### The Three Progressive Eras of Preservation

1. **The Prophetic Era & Early Sahabah (1st Century AH): Memory First, Selective Writing:**
   - The primary focus was memorizing and compiling the Qur'an to ensure zero conflation between Allah's revelation and the Prophet's personal words.
   - Despite this, prominent Sahabah maintained private personal notebooks (*Suhuf*), such as Abdullah ibn 'Amr ibn al-'As (*Al-Sahifah al-Sadiqah*) and Ali ibn Abi Talib.

2. **The Era of the Tabi'un (Late 1st – 2nd Century AH): Official State Initiative:**
   - Guided by Caliph Umar ibn Abdul Aziz's decree, master scholars like Ibn Shihab al-Zuhri began gathering narrations into centralized regional archives.
   - The first themed compendiums were produced, most notably the *Muwatta* of Imam Malik ibn Anas in Medina.

3. **The Era of the Compilers (3rd Century AH): Golden Scientific Standardization:**
   - Scholars traversed thousands of miles, interviewing narrators and establishing the sciences of *Isnad* analysis.
   - The *Kutub al-Sittah* were authored, creating a definitive, authenticated corpus that has endured unchanged for over twelve centuries.""",
        "comparison_table": {
            "title": "Evolutionary Stages of Hadith Preservation",
            "headers": ["Historical Stage", "Primary Custodians", "Method of Preservation", "Primary Motivation"],
            "rows": [
                ["Prophetic Era (1st Century AH)", "Companions (Sahabah)", "Oral memory, living practice, private notes (Suhuf)", "Preserving Qur'an distinctly; direct living access"],
                ["Successors Era (Late 1st-2nd AH)", "Tabi'un & Caliph Umar II", "First official state gathering into regional texts", "Death of memorizers; geographical spread"],
                ["Golden Age (3rd Century AH)", "Compilers of Kutub al-Sittah", "Rigorous critical compilation & biographical auditing", "Eradicating fabrications; establishing definitive canon"]
            ]
        },
        "worked_example": {
            "scenario": "In a history class, a student asks: 'If Hadith books were written down decades after the Prophet's death, how do we know they are not just made-up stories?' Mr. Rashid explains: 'Think of it this way: if your father tells you a family event, and you tell your son, and everyone in the town records this with exact names, and later a scholar comes and checks the memory and honesty of every single person in that line of storytellers before recording it, that is a scientific audit. Early Muslims did not just write stories; they engineered a rigorous oral-to-written verification science that filtered out falsehoods and preserved authentic truth.'",
            "analysis": "This scenario demonstrates that Hadith compilation was not an afterthought, but an unbroken, rigorous transition from oral to written custody.",
            "takeaway": "The written compilation was the natural, scientific culmination of disciplined oral preservation."
        },
        "real_world_application": "Apply the value of 'Preservation' to your academic career. Just as early scholars recognized the vulnerability of unwritten memory and committed the Sunnah to parchment, you should cultivate the habit of organized, dated, and structured note-taking in every class. Relying purely on memory causes knowledge to evaporate; written notes with clear references guarantee long-term retention and academic success.",
        "reflection": "What would have happened to the religion of Islam if early scholars had not made the immense effort to collect and verify the Hadiths? How does their commitment reflect profound love and responsibility for their faith?",
        "misconception": {
            "misconception": "Some assume that Hadiths were entirely oral and that no writing of Hadith occurred during the lifetime of the Prophet (PBUH).",
            "correction": "Several companions wrote down Hadiths during the Prophet's lifetime with his explicit permission, such as Abdullah ibn 'Amr ibn al-'As in his notebook called *Al-Sahifah al-Sadiqah*."
        },
        "mcq": {
            "question": "Which of the following was a primary catalyst that necessitated the systematic written collection of Hadith after the era of the companions?",
            "options": [
                "A) The Qur'an was lost and needed to be substituted by Hadith books",
                "B) The death of companion memorizers, global expansion, and the rise of political fabrications",
                "C) The desire of compilers to sell manuscripts for commercial profit in marketplaces",
                "D) A prophetic command prohibiting Muslims from ever memorizing oral statements"
            ],
            "answer": "B",
            "explanation": "The loss of living memorizers, the spread of Islam to diverse non-Arabic cultures, and the threat of political fabrications made written, authenticated records essential."
        },
        "summary": {
            "key_points": [
                "Hadith was initially preserved through disciplined oral memorization and selected private notebooks (Suhuf).",
                "Key catalysts for compilation were the demise of Sahabah, territorial expansion, and sectarian fabrications.",
                "Caliph Umar ibn Abdul Aziz formalized the first statewide collection under scholars like Ibn Shihab al-Zuhri.",
                "The 3rd century AH completed the transition with the creation of the canonical Kutub al-Sittah."
            ],
            "vocabulary": [
                {"term": "Suhuf (صحف)", "definition": "Early private written manuscripts and notebooks kept by individual Sahabah."},
                {"term": "Tadwin (تدوين)", "definition": "The formal, official written recording and codification of Hadith."},
                {"term": "Mawdu' (موضوع)", "definition": "Fabricated or forged reports falsely attributed to the Prophet."},
                {"term": "Dhihab al-'Ilm (ذهاب العلم)", "definition": "The loss of sacred knowledge caused by the death of qualified scholars."}
            ]
        },
        "exit_ticket": "Identify two major historical events or pressures that led Caliph Umar ibn Abdul Aziz to order the official compilation of Hadith."
    },

    # ─── LESSON 2.1.4 ───────────────────────────────────────────────────────────
    {
        "unit_order": 4,
        "unit_name": "Lesson 2.1.4: Tabi‘in and Tabi‘i-Tabi‘in",
        "unit_description": "Examines the three blessed generations of Hadith transmission: Sahabah, Tabi'un, and Atba' al-Tabi'in, and their roles as links in the golden chain.",
        "lesson_title": "Tabi‘in and Tabi‘i-Tabi‘in",
        "diagram_title": "The Three Blessed Generations of Transmission Tree",
        "svg_fn": get_svg_lesson_4,
        "image": {
            "title": "Classical Calligraphic Inscription of Hadith Transmission",
            "url": "https://upload.wikimedia.org/wikipedia/commons/3/38/Hadith_in_Persian_Calligraphy.jpg",
            "caption": "Artistic classical manuscript demonstrating the honor accorded to the chain of narrators across the blessed generations.",
            "author": "Islamic Calligraphy Master",
            "licensing": "Public Domain",
            "source": "Wikimedia Commons"
        },
        "youtube": {
            "title": "What The Tabi'in Say About The Ahli Sunnah",
            "youtube_id": "sKZpWByFQYU",
            "description": "Explores the generational characteristics, piety, and transmission accuracy of the Tabi'un and their successors."
        },
        "inquiry_question": "Who were the Tabi'un and Atba' al-Tabi'in, and how did these two generations guarantee the unbroken chain of prophetic teachings?",
        "connection": "Imagine an Olympic torch relay where an eternal flame must travel from the mountaintop to a grand stadium thousands of miles away without being extinguished. The runner at the summit is the Prophet (PBUH), who passes the flame to his Companions. But who received the flame from the Companions, and who carried it safely until it was enclosed within the lamps of the great Hadith books? These second and third generations of Muslims are the unsung heroes who preserved the sacred flame with absolute integrity and meticulous discipline.",
        "goals": [
            "Define the three generations: Sahabah, Tabi'un, and Atba' al-Tabi'in.",
            "Explain how the master-disciple relationship formed an unbroken chain of custody (Sanad).",
            "Appreciate the moral and intellectual qualifications demanded of narrators in the early generations."
        ],
        "authoritative_concept": """### The Three Blessed Generations (Qurun al-Fadilah)

The science of Hadith transmission rests upon three foundational generations praised by the Prophet Muhammad (PBUH):

1. **As-Sahabah (The Companions — 1st Generation):**
   - Defined as any person who met the Prophet Muhammad (PBUH) while believing in him and died as a Muslim.
   - Primary role: Direct eye and ear witnesses who absorbed the Qur'an and Sunnah directly from the Prophet's speech and daily conduct.

2. **At-Tabi'un (The Successors — 2nd Generation):**
   - Defined as the generation of Muslims who met one or more of the Sahabah in a state of faith and died as Muslims, but did not see the Prophet (PBUH).
   - Primary role: Inherited the oral traditions from dispersing companions, organized the first formal schools of Hadith (in Medina, Kufa, Basra), and carried out official written recordings under Caliph Umar II.

3. **Atba' al-Tabi'in (The Successors of the Successors — 3rd Generation):**
   - Defined as Muslims who met one or more of the Tabi'un, but did not meet any Sahabah.
   - Primary role: Standardized the rules of Hadith criticism (*Jarh wa Ta'dil*), developed classification terminologies, and authored the earliest structured thematic books (e.g., Imam Malik's *Muwatta*, Sufyan al-Thawri's compilations).""",
        "scripture_panel": """### Prophetic Commendation of the Three Generations

> The Prophet Muhammad (PBUH) said:
> *"The best of my people are my generation, then those who follow them, then those who follow them."*
> — **Sahih al-Bukhari (2651), Sahih Muslim (2533)**

> Allah (SWT) declared in the Qur'an:
> *"And the first forerunners [in the faith] among the Muhajireen and the Ansar and those who followed them with good conduct - Allah is pleased with them and they are pleased with Him..."*
> — **Surah At-Tawbah (9:100)**""",
        "deep_explanation": """### The Educational Conduit: Master to Disciple

1. **The Human Conduit (*Isnad*):**
   - The classical scholars understood that written pages alone can be corrupted or misinterpreted without an unbroken chain of living human teachers.
   - Every single narration in the canonical books is preceded by a list of names tracing back generation by generation:
     `Compiler (3rd AH) → Teacher (Atba' al-Tabi'in) → Mentor (Tabi'un) → Companion (Sahabi) → Prophet (PBUH)`.

2. **Rigorous Biographical Tracking (*'Ilm al-Rijal*):**
   - Scholars documented the birth years, death dates, journeys, teachers, students, memory strength, and moral character of tens of thousands of narrators.
   - If a scholar claimed to narrate from a companion but historical records showed the companion died before the scholar was born, the narration was instantly exposed as broken (*munqati'*) and unauthentic.

3. **Transmission Integrity:**
   - The Tabi'un treated learning Hadith with profound reverence. Scholars like Sa'id ibn al-Musayyib and Al-Hasan al-Basri would travel for days across deserts to confirm a single word transmitted by a Sahabi.""",
        "comparison_table": {
            "title": "Comparison of the Three Primary Generations of Hadith Custody",
            "headers": ["Generation", "Arabic Name", "Defining Criterion", "Prominent Exemplars", "Core Historical Contribution"],
            "rows": [
                ["1st Generation", "As-Sahabah", "Met the Prophet (PBUH) in faith and died as Muslims", "Abu Huraira, Aisha, Ibn Umar, Anas ibn Malik", "Direct eyewitness testimony; established oral and practical baseline"],
                ["2nd Generation", "At-Tabi'un", "Met the Sahabah in faith, but never met the Prophet", "Sa'id ibn al-Musayyib, Urwah ibn al-Zubayr, Hasan al-Basri", "Gathered narrations from diverse provinces; initiated statewide codification"],
                ["3rd Generation", "Atba' al-Tabi'in", "Met the Tabi'un in faith, but never met any Sahabi", "Imam Malik, Sufyan al-Thawri, Hammad ibn Zayd", "Formulated narrator criticism rules; authored early structured compendiums"]
            ]
        },
        "worked_example": {
            "scenario": "During an IRE quiz, the teacher asks: 'If Imam al-Bukhari lived in the 3rd century AH, how could he record a Hadith from the Prophet (PBUH) who lived two hundred years earlier?' Mussa answers: 'Imam al-Bukhari did not hear the Prophet directly. He received the Hadith through a documented, verified human chain: his teacher (an Atba' al-Tabi'i) heard it from a master of the Tabi'un generation, who heard it from a Companion (Sahabi) who sat with the Prophet and heard him speak. This chain of custody connects Imam al-Bukhari directly to the Prophet's mouth.' The teacher gives Mussa top marks.",
            "analysis": "This scenario demonstrates how the Isnad bridges the historical timeline through direct teacher-student lineages.",
            "takeaway": "The chain of narrators is the historical bridge connecting classical books directly to prophetic revelation."
        },
        "real_world_application": "Practice 'Chain Respect' within your family, school, and community. Just as the Tabi'un honored and learned from the elder Sahabah, you should demonstrate immense reverence for your grandparents, parents, and veteran teachers. Inquire about their life lessons, listen patiently to their wisdom, and recognize yourself as the next link in the chain responsible for carrying upright moral values into the future.",
        "reflection": "Why did early scholars invest lifetimes writing detailed biographies of thousands of ordinary men and women who transmitted Hadith? What does this teach us about the importance of personal credibility and accountability?",
        "misconception": {
            "misconception": "Some think that anyone who lived during the era of the Prophet was a Sahabi.",
            "correction": "To be a Sahabi, a person must have met the Prophet (PBUH) while believing in him and died as a Muslim. Opponents like Abu Jahl met the Prophet but were not believers, so they are not Sahabah."
        },
        "mcq": {
            "question": "Which of the following statements accurately defines the generation of the 'Tabi'un' in Hadith sciences?",
            "options": [
                "A) The companions who migrated with the Prophet from Makkah to Medina",
                "B) The generation of Muslims who met the Companions (Sahabah) in faith, but did not see the Prophet directly",
                "C) Modern translators who render classical Arabic Hadiths into English",
                "D) The political governors appointed by the Abbasid Caliphs in Baghdad"
            ],
            "answer": "B",
            "explanation": "The Tabi'un (Successors) are the second blessed generation who learned directly from the Sahabah, serving as the pivotal link between eyewitness companions and later compilers."
        },
        "summary": {
            "key_points": [
                "The preservation of Hadith relies upon three blessed generations: Sahabah, Tabi'un, and Atba' al-Tabi'in.",
                "The Isnad (chain of transmission) connects each compiler directly to the Prophet through verified teacher-student relationships.",
                "The science of biographies ('Ilm al-Rijal) verified birth and death dates to ensure zero historical gaps.",
                "The early generations modeled unparalleled dedication, traveling across deserts to confirm individual narrations."
            ],
            "vocabulary": [
                {"term": "Sahabah (الصحابة)", "definition": "The companions who met the Prophet (PBUH) in faith and died as Muslims."},
                {"term": "Tabi'un (التابعون)", "definition": "The Successors who met the Sahabah in faith and transmitted their knowledge."},
                {"term": "Atba' al-Tabi'in (أتباع التابعين)", "definition": "The Successors of the Successors who formalized Hadith sciences."},
                {"term": "'Ilm al-Rijal (علم الرجال)", "definition": "The biographical science evaluating the integrity and timelines of Hadith transmitters."}
            ]
        },
        "exit_ticket": "Define the terms 'Sahabah' and 'Tabi'un', highlighting the single key difference between them."
    },

    # ─── LESSON 2.1.5 ───────────────────────────────────────────────────────────
    {
        "unit_order": 5,
        "unit_name": "Lesson 2.1.5: Classification: sahih",
        "unit_description": "Analyzes the definition of a Sahih (authentic) Hadith and its five indispensable conditions of authentication.",
        "lesson_title": "Classification: Sahih",
        "diagram_title": "The 5-Key Padlock of Sahih Hadith Authenticity",
        "svg_fn": get_svg_lesson_5,
        "image": {
            "title": "Folio from an Ancient Copy of Sahih al-Bukhari",
            "url": "https://upload.wikimedia.org/wikipedia/commons/8/80/Sahih_al-Bukhari%2C_1890s_%282024-04-02%29.jpg",
            "caption": "Pristine historical manuscript text showing the uninterrupted chain of narrators preceding every Sahih hadith.",
            "author": "Islamic Classical Scribe",
            "licensing": "Public Domain",
            "source": "Wikimedia Commons"
        },
        "youtube": {
            "title": "The Five Conditions Of A Saheeh Hadith",
            "youtube_id": "7knWxIHX3sM",
            "description": "Clear and detailed breakdown of the five necessary and sufficient conditions for grading a Hadith as Sahih."
        },
        "inquiry_question": "What makes a Hadith sahih (authentic), and what five rigorous criteria must it satisfy to achieve this highest classification?",
        "connection": "Imagine a bullion bank evaluating a shipment of gold bars. The bank vault does not open for just any shiny metal. An assayer runs five separate tests: 1) Is the courier certified? 2) Is the bar stamped with verified provenance? 3) Is the weight exactly 1,000.0 grams without loss? 4) Is the metal free of alloys? 5) Is it free from hidden internal fissures under X-ray? In Hadith sciences, a Sahih Hadith is like that certified pure gold bar. It must pass through five rigorous security tests before scholars declare it authentic and binding.",
        "goals": [
            "Define the technical classification of a Sahih Hadith.",
            "List and explain each of the five mandatory conditions of authenticity.",
            "Understand why all five conditions must be simultaneously present for a Hadith to be Sahih."
        ],
        "authoritative_concept": """### Definition of Sahih Hadith (الحديث الصحيح)

In the definitive terminology established by master scholars like Ibn al-Salah (d. 643 AH) and Ibn Hajar al-Asqalani:

> **Sahih Hadith:** A narration transmitted through an unbroken, continuous chain of narrators (*ittisal al-isnad*), where every single narrator possesses upright moral character (*'adalah*) and flawless memory precision (*dabt tamm*), completely free from any irregularity (*shudhudh*) and free from any hidden defect (*'illah*).

A Sahih Hadith represents the pinnacle of historical and legal certainty in Islamic scholarship and serves as an absolute proof (*hujjah*) for Islamic creed (*Aqeedah*), laws (*Ahkam*), and morals (*Akhlaq*).""",
        "scripture_panel": """### The Five Classical Conditions Defined

> *"A Sahih hadith is a connected-chain narration transmitted by an upright, fully precise narrator from one like him up to its end, without being anomalous or defective."*
> — **Imam Ibn al-Salah (Muqaddimah fi 'Ulum al-Hadith)**

> *"O you who have believed, if there comes to you a disobedient one with information, investigate, lest you harm a people out of ignorance and become, over what you have done, regretful."*
> — **Surah Al-Hujurat (49:6)**""",
        "deep_explanation": """### Exhaustive Examination of the Five Conditions

1. **Unbroken Chain Connection (*Ittisal al-Isnad*):**
   - Every transmitter in the Sanad must have received the Hadith directly through a verified face-to-face meeting with their teacher.
   - If there is even one missing person or chronological gap, the chain is broken (*munqati'*), and the Hadith is automatically disqualified from being Sahih.

2. **Upright Moral Character (*'Adalat al-Ruwat*):**
   - Every narrator must be a sane, mature Muslim known for piety, truthfulness, and integrity.
   - Anyone convicted of a major sin, persistent minor sins, or caught in even a single casual lie in daily life was permanently disqualified.

3. **Flawless Memory Precision (*Tamm al-Dabt*):**
   - Narrators must possess extraordinary retentive memory (*Dabt al-Sadr*) or meticulously kept, cross-checked written records (*Dabt al-Kitab*).
   - Their narrations were regularly audited by comparing them with other scholars to verify they never added, omitted, or confused words.

4. **Absence of Irregularity (*'Adam al-Shudhudh*):**
   - The text (*Matn*) must not contradict a narration transmitted by a more trustworthy narrator or a stronger consensus of scholars.

5. **Absence of Subtle Hidden Defects (*'Adam al-'Illah*):**
   - The Hadith must be free from obscure, hidden flaws that appear outwardly sound but are uncovered through expert comparative analysis (such as misattributing a Companion's saying to the Prophet).""",
        "comparison_table": {
            "title": "The 5-Condition Security Matrix of a Sahih Hadith",
            "headers": ["Key Condition", "Arabic Term", "Target of Audit", "Failure Consequence"],
            "rows": [
                ["1. Continuous Chain", "Ittisal al-Isnad", "Chronological & geographic link between each narrator", "Hadith becomes Broken (Munqati'/Mu'allaq) → Disqualified"],
                ["2. Moral Character", "'Adalah", "Personal piety, truthfulness, and ethical adherence", "Hadith becomes Suspect or Fabricated (Mawdu') → Rejected"],
                ["3. Flawless Memory", "Tamm al-Dabt", "Exact textual recall under rigorous comparative testing", "Hadith drops to Hasan (lighter memory) or Dha'if (poor memory)"],
                ["4. Absence of Anomaly", "'Adam al-Shudhudh", "Textual alignment with more established narrations", "Hadith classified as Anomalous (Shadhdh) → Rejected"],
                ["5. Absence of Hidden Flaw", "'Adam al-'Illah", "Subtle technical errors in chain or text attribution", "Hadith classified as Defective (Mu'allal) → Rejected"]
            ]
        },
        "worked_example": {
            "scenario": "Amina finds a Hadith in a library book and wants to verify if it is Sahih. Her teacher shows her the chain of narrators written before the text: 'Imam al-Bukhari heard from Al-Humaydi, who heard from Sufyan ibn Uyaynah, who heard from Yahya ibn Sa'id, who heard from Muhammad ibn Ibrahim, who heard from Alqamah, who heard Umar ibn al-Khattab, who heard the Prophet (PBUH) say: \"Actions are judged by intentions...\"' The teacher explains: 'Amina, scholars examined all six individuals. Every single one met the person before them, lived with upright moral character, possessed extraordinary memory, and their text matches the consensus without subtle defects. Because it meets all five conditions, this Hadith is unconditionally Sahih.'",
            "analysis": "This scenario demonstrates how real Hadith chains are evaluated by applying all five conditions simultaneously.",
            "takeaway": "Authenticity is not an arbitrary label; it is a verifiable verdict derived from testing all five conditions."
        },
        "real_world_application": "Apply the principles of *Dabt* (precision) and *'Adalah* (integrity) to your personal reputation. Be a student whose word is an ironclad bond: never cheat in exams, never exaggerate stories to gain popularity, and when carrying messages between teachers, parents, and friends, communicate facts with exact precision. Cultivating uprightness and precision will make you a pillar of trust in your school and society.",
        "reflection": "Why did Hadith scholars reject a narrator who was caught lying in ordinary worldly matters, even if he never lied about a Hadith? How does this standard safeguard divine religion?",
        "misconception": {
            "misconception": "Some think that if a Hadith has a beautiful, inspiring message, it is automatically Sahih.",
            "correction": "A beautiful message does not make a Hadith authentic. It must satisfy all five rigorous conditions regarding its chain of narrators and lack of hidden defects before being graded Sahih."
        },
        "mcq": {
            "question": "Which of the following is NOT one of the five essential conditions required for a Hadith to be classified as Sahih (authentic)?",
            "options": [
                "A) The chain of narrators must be fully continuous without any missing links",
                "B) Every narrator must possess precise memory (Dabt)",
                "C) The narration must be composed in rhyming Arabic poetic verse",
                "D) The Hadith must be completely free from hidden defects ('Illah)"
            ],
            "answer": "C",
            "explanation": "Poetic style is never a requirement for Hadith authenticity. Authenticity depends strictly on chain connection, narrator uprightness, memory precision, absence of anomalies, and absence of hidden defects."
        },
        "summary": {
            "key_points": [
                "Sahih is the highest classification of Hadith authenticity in Islamic scholarship.",
                "It requires all five conditions: continuous chain, upright character, flawless memory, absence of anomaly, and absence of hidden defect.",
                "If even one condition fails, the Hadith cannot be graded as Sahih.",
                "Sahih Hadiths provide definitive legal, theological, and moral proof in Islam."
            ],
            "vocabulary": [
                {"term": "Sahih (صحيح)", "definition": "Sound, authentic; meeting all five criteria of flawless transmission."},
                {"term": "Ittisal (اتصال)", "definition": "The unbroken continuity of transmission from compiler to Prophet."},
                {"term": "Dabt (ضبط)", "definition": "Accuracy, precision, and retention power of a narrator's memory or written book."},
                {"term": "'Illah (علة)", "definition": "A subtle, hidden defect that damages a Hadith's authenticity despite outward soundness."}
            ]
        },
        "exit_ticket": "Recite or write down from memory the five mandatory conditions of a Sahih Hadith."
    },

    # ─── LESSON 2.1.6 ───────────────────────────────────────────────────────────
    {
        "unit_order": 6,
        "unit_name": "Lesson 2.1.6: Classification: hasan",
        "unit_description": "Examines the Hasan (good/sound) Hadith classification, its relationship to Sahih, and its authority in Islamic jurisprudence.",
        "lesson_title": "Classification: Hasan",
        "diagram_title": "Sahih vs Hasan Precision & Memory Gauge",
        "svg_fn": get_svg_lesson_6,
        "image": {
            "title": "Classical Folio from Jami' at-Tirmidhi",
            "url": "https://upload.wikimedia.org/wikipedia/commons/f/f4/A_manuscript_about_hadiths%2C_in_nasta%27liq%2C_1559.jpg",
            "caption": "Historical manuscript of Jami' at-Tirmidhi, the pioneering compilation that established the technical classification of Hasan hadiths.",
            "author": "At-Tirmidhi Manuscript Heritage",
            "licensing": "Public Domain",
            "source": "Wikimedia Commons"
        },
        "youtube": {
            "title": "Difference between Sahih Hadith and Hasan Hadith",
            "youtube_id": "_EdJtaw3Ni4",
            "description": "Explains how the Hasan classification operates, its slight memory nuance compared to Sahih, and why it is fully binding."
        },
        "inquiry_question": "What is a hasan (good) Hadith, and how does it differ from a sahih Hadith while remaining fully authoritative in Islamic law?",
        "connection": "Imagine a national high school examination grading system. An 'A+' student scores 98-100%, consistently produces immaculate work, and makes zero calculation errors (analogous to a Sahih narrator with Dabt Tamm). An 'A' or 'B+' student is also deeply honest, conscientious, and highly knowledgeable, scoring 85-92%, but occasionally makes a tiny slip or exhibits slightly less speed under pressure (analogous to a Hasan narrator with Dabt Khafif). Their work is still thoroughly excellent, trusted by universities, and fully approved. In Hadith science, a Hasan Hadith is like that A-student—completely authentic and authoritative.",
        "goals": [
            "Define the technical meaning of a Hasan Hadith.",
            "Identify the single criterion that distinguishes a Hasan Hadith from a Sahih Hadith.",
            "Explain the pioneering contribution of Imam at-Tirmidhi in standardizing the Hasan classification."
        ],
        "authoritative_concept": """### Definition of Hasan Hadith (الحديث الحسن)

In Islamic Hadith terminology, formalized by Imam Abu Isa at-Tirmidhi and defined by classical master Ibn Hajar:

> **Hasan Hadith:** A narration that satisfies all the conditions of a *Sahih* Hadith—possessing an unbroken chain (*ittisal*), upright and pious narrators (*'adalah*), absence of irregularity (*shudhudh*), and absence of hidden defects (*'illah*)—**EXCEPT** that one or more narrators in its chain have a slightly lighter or less precise level of retentive memory (*khiffat al-dabt*) compared to the flawless memory (*dabt tamm*) demanded for Sahih.

Despite this minor distinction in memory rating, scholars are in unanimous agreement that a Hasan Hadith is **completely authentic, legally binding (*hujjah*), and fully actionable** in deriving Islamic laws and ethical principles.""",
        "scripture_panel": """### Classical Formulation of the Hasan Classification

> *"A Hasan hadith is one whose chain is connected, its narrators are upright, but its precision is lighter than that of a Sahih hadith, and it is free from anomaly and defect."*
> — **Imam Ibn Hajar al-Asqalani (Nukhbat al-Fikar)**

> Imam at-Tirmidhi stated in his *Al-Jami'*:
> *"What we intend by 'Hadith Hasan' in our book is a hadith whose chain does not contain anyone accused of lying, its text is not anomalous, and it is reported through more than one route."*
> — **Imam Abu Isa at-Tirmidhi**""",
        "deep_explanation": """### Comparing Sahih and Hasan: The Four Shared Pillars vs. The Single Variant

To understand the precision of Hadith scholars, observe that a Hasan Hadith must maintain 4 out of 5 conditions at the absolute maximum standard:

1. **Unbroken Chain Connection:** Must be 100% continuous. If there is a missing link, it is instantly demoted to Dha'if (Weak).
2. **Moral Uprightness (*'Adalah*):** The narrator must be 100% pious, honest, and morally blameless. If their honesty is questioned, the report is rejected.
3. **Absence of Irregularity (*Shudhudh*):** The text must not conflict with stronger narrations.
4. **Absence of Hidden Flaws (*'Illah*):** The text and chain must be free of covert defects.

**The ONLY Difference: Retentive Memory (*Dabt*):**
- **Sahih:** Narrators possess *Dabt Tamm* (maximum retention, virtually zero memory lapses across thousands of narrations).
- **Hasan:** Narrator possesses *Dabt Khafif* (high competence and reliability, but audited to have occasional minor memory slips).
- Because their integrity (*'adalah*) is beyond doubt, the meaning of their report is intact, and scholars accept it as reliable proof.""",
        "comparison_table": {
            "title": "Head-to-Head Comparison: Sahih vs. Hasan Hadith",
            "headers": ["Authenticity Element", "Sahih Hadith (Grade 1)", "Hasan Hadith (Grade 2)", "Jurisprudential Impact"],
            "rows": [
                ["Chain Continuity", "100% Unbroken (Ittisal)", "100% Unbroken (Ittisal)", "Identical strict requirement"],
                ["Narrator Character", "Pious, upright ('Adalah)", "Pious, upright ('Adalah)", "Identical moral threshold"],
                ["Memory Precision", "Dabt Tamm (Flawless precision)", "Dabt Khafif (Slightly lighter precision)", "The ONLY distinguishing factor"],
                ["Anomaly / Flaws", "Free from Shudhudh & 'Illah", "Free from Shudhudh & 'Illah", "Identical textual safety standard"],
                ["Legal Authority", "Absolute, primary evidence", "Fully authoritative & binding", "Both are accepted sources of law"]
            ]
        },
        "worked_example": {
            "scenario": "During an exam revision group, Omar says: 'I found a Hadith regarding manners of visiting neighbors, but the book states its grading is Hasan. Does this mean we should disregard it because it isn't graded Sahih?' His study partner Halima replies: 'No, Omar! A Hasan Hadith is completely authentic, reliable, and binding. The only reason it is termed Hasan rather than Sahih is that one narrator in the chain had a slightly less extraordinary memory, but was still deeply honest, upright, and God-fearing. Islamic scholars unanimously accept Hasan Hadiths as proof for laws and manners, exactly like Sahih reports.'",
            "analysis": "This scenario clears the pervasive misconception that Hasan means 'weak' or 'inferior'.",
            "takeaway": "Hasan Hadiths are fully authentic and legally actionable in Islamic jurisprudence."
        },
        "real_world_application": "Apply the wisdom of 'Reasonable Tolerances' in your collaborative schoolwork. Do not reject a teammate's essay, a classmate's contribution, or a younger sibling's assistance simply because it is not 100% flawless (like a Sahih). If they are sincere, honest, diligent, and generally accurate (like a Hasan narrator), appreciate and accept their work. Mutual encouragement builds stronger communities than hypercritical perfectionism.",
        "reflection": "Why did Hadith scholars introduce the intermediary classification of 'Hasan' rather than forcing every narration into either '100% perfect' or 'worthless'? How does this demonstrate their scientific balance?",
        "misconception": {
            "misconception": "Some learners believe that a Hasan Hadith is weak or questionable and cannot be used to establish Islamic practices.",
            "correction": "A Hasan Hadith is an authentic narration. Islamic jurists are in full consensus that Hasan Hadiths are authoritative proofs for deriving Islamic rulings and daily religious duties."
        },
        "mcq": {
            "question": "What is the single difference between a Sahih Hadith and a Hasan Hadith according to classical Hadith science?",
            "options": [
                "A) A Hasan Hadith has gaps in its chain of narrators, while a Sahih chain is unbroken",
                "B) A Hasan Hadith contains fabricated phrases inserted by later storytellers",
                "C) A Hasan Hadith has one or more narrators with slightly lighter memory precision (Dabt Khafif), while a Sahih requires flawless memory",
                "D) A Hasan Hadith is rejected by scholars, while a Sahih Hadith is accepted"
            ],
            "answer": "C",
            "explanation": "A Hasan Hadith satisfies all the strict conditions of a Sahih Hadith, differing only in that a narrator's memory precision is slightly lighter (Dabt Khafif) than the absolute perfection of a Sahih narrator."
        },
        "summary": {
            "key_points": [
                "Hasan is the second tier of authentic Hadith, fully reliable and authoritative in Islamic law.",
                "It meets every condition of a Sahih Hadith except that a narrator has slightly lighter memory precision (Dabt Khafif).",
                "Imam at-Tirmidhi played a monumental role in formalizing and popularizing the Hasan designation.",
                "Both Sahih and Hasan Hadiths form the authentic textual foundation for Islamic belief and practice."
            ],
            "vocabulary": [
                {"term": "Hasan (حسن)", "definition": "Good, sound; an authentic narration whose narrator has slightly lighter memory precision."},
                {"term": "Dabt Khafif (ضبط خفيف)", "definition": "Slightly lighter precision; reliable retention that falls short of absolute perfection."},
                {"term": "Hujjah (حجة)", "definition": "Binding proof or authoritative legal evidence in Islamic jurisprudence."},
                {"term": "Hasan li-Dhatihi (حسن لذاته)", "definition": "A Hadith that is Hasan in its own right based on its own chain of narrators."}
            ]
        },
        "exit_ticket": "State in your own words why scholars consider a Hasan Hadith to be fully acceptable for deriving Islamic laws."
    },

    # ─── LESSON 2.1.7 ───────────────────────────────────────────────────────────
    {
        "unit_order": 7,
        "unit_name": "Lesson 2.1.7: Classification: dha‘if",
        "unit_description": "Examines the causes of weakness in Hadith (Dha'if), the categories of flaws, and the strict scholarly rules governing their conditional use.",
        "lesson_title": "Classification: Dha‘if",
        "diagram_title": "Hadith Reliability & Usage Traffic Light System",
        "svg_fn": get_svg_lesson_7,
        "image": {
            "title": "Classical Arabic Manuscript Demonstrating Textual Criticism",
            "url": "https://upload.wikimedia.org/wikipedia/commons/f/f4/A_manuscript_about_hadiths%2C_in_nasta%27liq%2C_1559.jpg",
            "caption": "Scholarly annotations in a historical Hadith codex marking weak transmitters and questionable reports.",
            "author": "Hadith Critic Tradition",
            "licensing": "Public Domain",
            "source": "Wikimedia Commons"
        },
        "youtube": {
            "title": "Can We Follow Weak or Da'if Hadith?",
            "youtube_id": "EodcnGjGspo",
            "description": "Comprehensive explanation of what causes a Hadith to be graded Dha'if and the conditions under which scholars permit or ban its usage."
        },
        "inquiry_question": "What causes a Hadith to be classified as dha'if (weak), and why must it never be used to establish Islamic beliefs or laws?",
        "connection": "Imagine receiving a forwarded WhatsApp message from an unsaved number stating: 'The Ministry of Education has cancelled all upcoming national exams starting tomorrow!' If you trace where the message came from, you find that person #3 in the chain is known for spreading pranks, and person #5 is completely anonymous. Would you stop studying based on that message? Of course not! Because the chain has unreliable links and unknown sources, the message lacks credibility. A Dha'if (weak) Hadith is like that unverified message—it contains defects in its transmission that prevent scholars from trusting it as the authentic speech of the Prophet.",
        "goals": [
            "Define a Dha'if (weak) Hadith and differentiate it from Mawdu' (fabricated).",
            "Identify the two primary causes of weakness: broken chains and narrator defects.",
            "State the strict conditions under which some scholars permit quoting mildly weak Hadiths."
        ],
        "authoritative_concept": """### Definition of Dha'if Hadith (الحديث الضعيف)

In the taxonomy of Hadith sciences:

> **Dha'if Hadith:** Any narration that fails to satisfy one or more of the five mandatory conditions required for authenticity (*Sahih* or *Hasan*).

### Two Primary Roots of Weakness:

1. **A Break in the Chain (*Inqita' al-Sanad*):**
   - A missing link where a narrator could not have met or heard from the person they claim to narrate from.
   - Subtypes include: *Mu'allaq* (suspended at beginning), *Mursal* (missing the companion link), *Mu'dal* (two consecutive missing narrators), and *Munqati'* (a single missing narrator in the middle).

2. **Defect in the Narrator (*Ta'n fi al-Rawi*):**
   - **Moral Defect:** Known for unreliability, innovation, or impiety.
   - **Memory Defect:** Frequent errors (*Fahsh al-Ghalat*), extreme carelessness, or being unknown (*Majhul*).
   - **Fabrication (*Mawdu'*):** The most severe subcategory, where a narrator deliberately invents a lie and falsely claims the Prophet said it. A fabricated report is completely rejected.""",
        "scripture_panel": """### Scholarly Guidelines on Weak Hadiths

> *"A weak hadith is that which does not reach the rank of Hasan through the absence of its conditions."*
> — **Imam al-Bayquni (Al-Manzumah al-Bayquniyyah)**

> Master Hadith scholar Imam Ibn Hajar al-Asqalani established three strict conditions for using mildly weak Hadiths:
> 1. The weakness must not be severe (no liars or fabricators in chain).
> 2. It must fall under a general principle already established in the Qur'an or Sahih Hadith.
> 3. One must not believe with certainty that the Prophet actually said it, but act on it only out of caution for noble virtues.""",
        "deep_explanation": """### Legal and Theological Boundaries for Using Weak Hadiths

Scholars established strict rules regarding what weak Hadiths can and cannot be used for:

1. **Strictly Forbidden in Creed (*Aqeedah*):**
   - Islamic beliefs regarding the attributes of Allah, the unseen (*Ghayb*), the Day of Judgment, and angels must be established *only* on definitive, authentic evidence (Qur'an and Sahih/Hasan Hadith). A weak Hadith has zero authority in theology.

2. **Strictly Forbidden in Core Rulings (*Ahkam*):**
   - Making an action obligatory (*Wajib*), forbidden (*Haram*), or valid in contracts cannot be based on a weak report.

3. **Conditionally Allowed in Virtues (*Fada'il al-A'mal*):**
   - Some classical jurists permitted quoting mildly weak narrations to encourage voluntary good deeds (e.g., extra remembrance, voluntary fasting, showing kindness to parents), provided:
     - The hadith is not severely weak (*dha'if jiddan*).
     - It does not introduce brand new rituals not grounded in authentic Sunnah.
     - The speaker clarifies its grading rather than claiming certainty.""",
        "comparison_table": {
            "title": "Categorization of Hadith Weakness & Scholarly Ruling",
            "headers": ["Classification", "Nature of Defect", "Scholarly Ruling", "Permissible Use"],
            "rows": [
                ["Dha'if (Mildly Weak)", "Minor memory lapses or single hidden gap in chain", "Unreliable for legal rulings or theology", "Permitted strictly for encouraging virtues (Fada'il)"],
                ["Dha'if Jiddan (Severely Weak)", "Narrator accused of deceit or flagrant errors", "Completely disqualified from proof", "Prohibited from usage; disregarded"],
                ["Mawdu' (Fabricated Lie)", "Deliberately invented lie attributed to Prophet", "Completely rejected and cursed", "Prohibited to quote EXCEPT to expose its falsehood"]
            ]
        },
        "worked_example": {
            "scenario": "Farhan finds an article online that quotes a Hadith saying: 'If you sleep after the Asr (afternoon) prayer, you will lose your mental sanity.' He is terrified and vows never to take an afternoon nap. His father, consulting a scholarly database, explains: 'Farhan, this report is classified by Hadith critics as Dha'if Jiddan (severely weak) and some scholars categorized it as Mawdu' (fabricated). Its chain contains an unreliable transmitter. In Islam, we never build our daily lifestyles, fears, or religious rulings on weak reports. The authentic Sunnah actually encourages wholesome rest, and sleeping after Asr is medically and religiously permissible.'",
            "analysis": "This scenario illustrates how relying on weak Hadiths leads to groundless fears and baseless religious restrictions.",
            "takeaway": "Islamic rulings and lifestyle practices must never be constructed upon weak or fabricated narrations."
        },
        "real_world_application": "Apply 'Verification Discipline' to your digital media habits. Just as Hadith scholars reject weak reports to protect religious truth, you should refuse to believe, like, or retweet unverified news, gossip, and shocking claims on social media. When someone shares an alarming rumor, ask: 'What is the original source? Who verified this?' Fostering an investigative mindset protects your mind from deception.",
        "reflection": "Why is it an act of moral courage and academic integrity for a scholar to openly declare a Hadith 'weak', even if the Hadith promotes a nice moral message? How does intellectual honesty protect religion?",
        "misconception": {
            "misconception": "Some think that a Dha'if Hadith is a fabricated lie created by enemies of Islam.",
            "correction": "A Dha'if Hadith is not necessarily an intentional lie. Most weak Hadiths arose from well-meaning narrators who suffered from poor memory or lost notes. An intentional lie is categorized separately as Mawdu' (fabricated)."
        },
        "mcq": {
            "question": "Why are Dha'if (weak) Hadiths strictly prohibited by Islamic scholars from being used to derive core beliefs (Aqeedah) or legal rulings (Ahkam)?",
            "options": [
                "A) Because they were composed in languages other than Arabic",
                "B) Because their transmission lacks the historical certainty and narrator reliability necessary to guarantee they are the authentic words of the Prophet",
                "C) Because weak Hadiths are reserved exclusively for advanced university professors",
                "D) Because any Hadith not compiled by Imam al-Bukhari is automatically judged as false"
            ],
            "answer": "B",
            "explanation": "Due to gaps in the chain or narrators with deficient memory, weak Hadiths lack the historical certainty required to establish mandatory laws or theological creed."
        },
        "summary": {
            "key_points": [
                "A Dha'if Hadith fails to meet one or more conditions of Sahih or Hasan authenticity.",
                "Weakness arises primarily from broken chains (Inqita') or narrator deficiencies in memory or character.",
                "Weak Hadiths cannot be used to establish Islamic beliefs (Aqeedah) or legal prohibitions (Ahkam).",
                "Fabricated Hadiths (Mawdu') are outright lies and are completely forbidden to share except to expose their falsehood."
            ],
            "vocabulary": [
                {"term": "Dha'if (ضعيف)", "definition": "Weak; a Hadith that does not fulfill the criteria of authenticity."},
                {"term": "Mawdu' (موضوع)", "definition": "Fabricated; an invented report falsely ascribed to the Prophet."},
                {"term": "Inqita' (انقطاع)", "definition": "A break or gap in the chain of narrators."},
                {"term": "Fada'il al-A'mal (فضائل الأعمال)", "definition": "Virtues of good deeds and voluntary acts of worship."}
            ]
        },
        "exit_ticket": "State two reasons why a Hadith might be graded as Dha'if (weak), and name one realm where weak Hadiths can never be used."
    },

    # ─── LESSON 2.1.8 ───────────────────────────────────────────────────────────
    {
        "unit_order": 8,
        "unit_name": "Lesson 2.1.8: Collection and compilation process",
        "unit_description": "Examines the methodology of classical compilers, the science of Jarh wa al-Ta'dil, and the transcontinental journeys undertaken to verify Hadith.",
        "lesson_title": "Collection and Compilation Process",
        "diagram_title": "The Compiler's 4-Step Verification Journey",
        "svg_fn": get_svg_lesson_8,
        "image": {
            "title": "Classical Center of Islamic Manuscript Compilation",
            "url": "https://upload.wikimedia.org/wikipedia/commons/8/80/Sahih_al-Bukhari%2C_1890s_%282024-04-02%29.jpg",
            "caption": "Manuscript archive representing the rigorous compilation methodology of classical scholars during the Golden Age of Islam.",
            "author": "Historical Compilation Archive",
            "licensing": "Public Domain",
            "source": "Wikimedia Commons"
        },
        "youtube": {
            "title": "How Were The Hadith Collected and Written Down?",
            "youtube_id": "AWqQ0OxZGkY",
            "description": "Exploration of the travel (Rihlah), cross-referencing, and verification methodology utilized by classical Hadith compilers."
        },
        "inquiry_question": "How did classical compilers travel, cross-check, and filter thousands of reports to assemble verified Hadith compendiums?",
        "connection": "Imagine an investigative journalist spending twenty years traveling on foot through ten countries to interview living eyewitnesses of a world-changing event. Before writing down a single quote, the journalist interviews the eyewitness's neighbors, checks their financial honesty, examines their memory, and compares their statement with independent versions recorded thousands of miles away. This is not fiction. This was the daily reality of classical Hadith compilers like Imam al-Bukhari, who spent decades traversing deserts to preserve the Sunnah with unmatched scientific precision.",
        "goals": [
            "Explain the concept of Al-Rihlah (travel in pursuit of Hadith verification).",
            "Define the science of 'Ilm al-Jarh wa al-Ta'dil (criticism and validation of narrators).",
            "Describe the 4-step pipeline used by compilers to verify and compile Hadiths."
        ],
        "authoritative_concept": """### The Compiler's Verification Methodology

The classical compilation of Hadith was characterized by two extraordinary scholarly disciplines:

1. **Al-Rihlah fi Talab al-Hadith (الرحلة في طلب الحديث):**
   - Compilers refused to rely on second-hand letters or rumors. They traveled on foot and by animal across vast distances—from Central Asia (Bukhara, Samarkand) to Iraq, Syria, Egypt, Yemen, and the Hijaz—to sit face-to-face with transmitters and hear narrations directly.

2. **'Ilm al-Jarh wa al-Ta'dil (علم الجرح والتعديل):**
   - The definitive biographical science developed to evaluate the reliability and credibility of narrators:
     - **Ta'dil (تعديل - Validation):** Declaring a narrator upright (*'Adl*), reliable, and truthful based on rigorous investigation.
     - **Jarh (جرح - Discrediting):** Exposing a narrator's flaws (e.g., poor memory, dishonesty, sectarian bias) to protect the Sunnah from corruption.
   - Scholars declared that critical evaluation of narrators is a religious obligation (*Fard Kifayah*) to safeguard the purity of Islam.""",
        "scripture_panel": """### Classical Compilers on the Rigor of Verification

> Imam al-Bukhari stated:
> *"I compiled my book 'Al-Sahih' from among 600,000 hadiths over sixteen years. I made it an argument between myself and Allah the Almighty."*
> — **Tarikh Baghdad by Al-Khatib al-Baghdadi**

> Great Hadith master Yahya ibn Ma'in was asked:
> *"Are you not afraid that these people whom you discredit will be your opponents on the Day of Judgment?"*
> He replied: *"That they should be my opponents is far better to me than having the Prophet (PBUH) be my opponent, saying: 'Why did you not defend my Sunnah from lies?'"*""",
        "deep_explanation": """### The Compilers' 4-Step Verification Pipeline

1. **Step 1: The Personal Journey (*Al-Rihlah*):**
   - Meeting the living transmitter in person to verify their existence, sanity, and actual possession of original written manuscripts or verified chains.

2. **Step 2: The Narrator Audit (*Jarh wa Ta'dil*):**
   - Investigating the transmitter's daily reputation. Did they practice honest business? Were they ever caught exaggerating? Did their memory remain stable in old age?
   - In a legendary incident, Imam al-Bukhari traveled weeks to meet a narrator. Upon arrival, he saw the man tricking his escaped horse with an empty feed bag. Bukhari immediately left without taking a single Hadith, stating: *"One who lies to an animal cannot be trusted with the words of the Prophet of Allah."*

3. **Step 3: Textual Cross-Auditing (*Mu'aradah al-Mutun*):**
   - Compiling all independent versions of the same Hadith recorded across different cities (Kufa, Basra, Medina, Damascus) and comparing word variations to detect slips.

4. **Step 4: Systematic Codification (*Tadwin Mubawwab*):**
   - Organizing verified narrations into topical books (*Kutub*) and specific legal chapters (*Abwab*) preceded by complete chains.""",
        "comparison_table": {
            "title": "The Four Pillars of the Classical Hadith Ingestion Pipeline",
            "headers": ["Pipeline Stage", "Methodology", "Objective", "Modern Equivalent"],
            "rows": [
                ["1. Transcontinental Travel (Rihlah)", "Traveling thousands of miles to meet living narrators", "Eliminating hearsay; verifying direct custody", "Investigative field journalism & primary source vetting"],
                ["2. Biographical Audit (Jarh wa Ta'dil)", "Vetting personal morals, honesty, and memory recall", "Validating (Ta'dil) or discrediting (Jarh) transmitters", "Peer-review background vetting & character reference"],
                ["3. Cross-Checking (Mu'aradah)", "Comparing regional copies from Medina, Syria, Iraq", "Isolating textual slips, anomalies, and insertions", "Data triangulation and multi-source cross-verification"],
                ["4. Systematic Codification (Tadwin)", "Thematic chaptering with full Sanad documentation", "Publishing permanent canonical reference corpora", "Publishing peer-reviewed academic encyclopedia"]
            ]
        },
        "worked_example": {
            "scenario": "During an IRE class, the teacher recounts the story of Imam al-Bukhari and the man with the escaped horse. A student, Zahra, asks: 'Was tricking a horse really that serious? Why did Imam al-Bukhari reject the hadith immediately?' The teacher replies: 'Zahra, this story illustrates the uncompromising standard of Jarh wa Ta'dil. If a person is willing to employ deception in daily life—even toward an animal—scholars could never guarantee that he wouldn't employ exaggeration or carelessness when quoting the Prophet of Allah. This extreme standard is why we can trust Sahih al-Bukhari with absolute certainty today.'",
            "analysis": "This scenario demonstrates the extreme moral threshold required by classical Hadith auditors.",
            "takeaway": "Integrity cannot be compartmentalized; moral character in daily life directly determines academic credibility."
        },
        "real_world_application": "Incorporate the ethics of *Jarh wa Ta'dil* into your own research and reporting. Before you quote an article on the internet, cite a scientific claim in biology, or share breaking news, examine the credentials and motives of the author. Are they a recognized expert in their field? Do they have a commercial or political conflict of interest? Evaluating source credibility is the hallmark of an educated, critical mind.",
        "reflection": "What lessons of perseverance, patience, and sacrifice can modern students draw from the lives of Hadith compilers who walked thousands of miles in the desert heat to verify a single truth?",
        "misconception": {
            "misconception": "Some think that evaluating narrators in Jarh wa Ta'dil was a form of forbidden backbiting (Gheebah).",
            "correction": "Scholars unanimously established that Jarh wa Ta'dil is not backbiting, but a mandatory religious duty to protect divine religion from falsehood, exactly like giving honest testimony in a court of law."
        },
        "mcq": {
            "question": "In the science of Hadith authentication, what does the technical term 'Jarh wa al-Ta'dil' refer to?",
            "options": [
                "A) The artistic ornamentation of Hadith manuscript bindings",
                "B) The systematic evaluation of narrators' moral characters and memories to declare them either unreliable (Jarh) or trustworthy (Ta'dil)",
                "C) The memorization of the Holy Qur'an within a thirty-day period",
                "D) The translation of Hadith collections from Arabic into Persian and Urdu"
            ],
            "answer": "B",
            "explanation": "Jarh wa al-Ta'dil is the specialized biographical science of auditing narrators to determine who is trustworthy (Ta'dil) and who is unreliable (Jarh)."
        },
        "summary": {
            "key_points": [
                "Compiling Hadith involved extensive physical travel (Al-Rihlah) to verify direct oral reception.",
                "The science of Jarh wa al-Ta'dil audited the personal integrity and memory of every transmitter.",
                "Compilers like Imam al-Bukhari filtered hundreds of thousands of narrations through cross-referencing and textual comparison.",
                "The rigorous methodology created by Hadith compilers predated modern peer-review by nearly a millennium."
            ],
            "vocabulary": [
                {"term": "Al-Rihlah (الرحلة)", "definition": "Journeys undertaken across continents specifically to collect and verify Hadith."},
                {"term": "Jarh (جرح)", "definition": "Discrediting a narrator due to moral flaws, carelessness, or poor memory."},
                {"term": "Ta'dil (تعديل)", "definition": "Validating and declaring a narrator upright, trustworthy, and precise."},
                {"term": "Thiqah (ثقة)", "definition": "A trustworthy narrator who combines upright moral character with precise memory."}
            ]
        },
        "exit_ticket": "Explain in two sentences what Imam al-Bukhari's famous incident with the horse demonstrates about the standards of Hadith compilation."
    },

    # ─── LESSON 2.1.9 ───────────────────────────────────────────────────────────
    {
        "unit_order": 9,
        "unit_name": "Lesson 2.1.9: Authenticity and responsible use",
        "unit_description": "Establishes a practical 4-point verification protocol for digital literacy, ethical quoting, and preventing the spread of fabricated Hadiths.",
        "lesson_title": "Authenticity and Responsible Use",
        "diagram_title": "Digital Hadith Source Check & Verification Form Mockup",
        "svg_fn": get_svg_lesson_9,
        "image": {
            "title": "Historical Illuminated Hadith Manuscript Page",
            "url": "https://upload.wikimedia.org/wikipedia/commons/f/f4/A_manuscript_about_hadiths%2C_in_nasta%27liq%2C_1559.jpg",
            "caption": "An illuminated classical manuscript showcasing the care and reverence given to recording authenticated Hadith text.",
            "author": "Islamic Classical Scribe",
            "licensing": "Public Domain",
            "source": "Wikimedia Commons"
        },
        "youtube": {
            "title": "What Criteria Are Used to Verify the Authenticity of a Hadith?",
            "youtube_id": "x68lzICLATk",
            "description": "Practical educational guidance on verifying Hadith citations, checking authenticity gradings, and ethical digital sharing."
        },
        "inquiry_question": "How do we responsibly verify, quote, and share Hadiths on digital platforms and in our daily lives?",
        "connection": "Have you ever encountered a viral social media message that claims: 'Forward this Hadith to 10 friends, and you will receive miraculous good news in an hour; if you ignore it, tragedy will strike!'? Thousands of people share these messages because they sound pious, unaware that they are participating in the circulation of invented fabrications or superstitions. In our digital era, every smartphone user is a publisher. Learning a rigorous, source-conscious protocol to verify Hadiths before hitting 'forward' is both an academic duty and a sacred religious responsibility.",
        "goals": [
            "Demonstrate the 4-Point Digital Hadith Verification Protocol (Source, Narrator, Matn, Grading).",
            "Recognize the severe spiritual and moral consequences of attributing unverified statements to the Prophet.",
            "Apply digital literacy skills to identify and debunk online chain messages and religious hoaxes."
        ],
        "authoritative_concept": """### The Ethics of Quoting the Prophet (PBUH)

Attributing a statement to the Prophet Muhammad (PBUH) is a profound moral act that carries severe religious responsibility. The Prophet delivered an explicit, unequivocal warning against careless attribution:

> *"Whoever tells a lie about me deliberately, let him take his place in the Hellfire."*
> — **Sahih al-Bukhari (110), Sahih Muslim (3)**

> *"It is enough of a lie for a person to narrate everything that he hears."*
> — **Sahih Muslim (Introduction)**

### The 4-Point Verification Protocol

Before quoting, writing, or forwarding any Hadith, a responsible student must verify four essential fields:
1. **The Source Compilation (*Al-Masdar*):** Exactly which recognized book records it (e.g., Sahih al-Bukhari, Sahih Muslim, Sunan Abi Dawood).
2. **The Primary Narrator (*Al-Rawi al-A'la*):** The specific Sahabi who witnessed and narrated the statement (e.g., Abu Huraira, Aisha, Anas ibn Malik).
3. **The Exact Text (*Al-Matn*):** The verified wording, avoiding paraphrase or sensationalized embellishments.
4. **The Scholarly Grading (*Al-Hukm*):** The authenticity grade (Sahih, Hasan, or Dha'if) rendered by qualified Hadith scholars. If unknown, it must be labeled **'Source Not Supplied / Unverified'**.""",
        "scripture_panel": """### Foundational Rules for Digital Hadith Transmission

> *"Do not pursue that of which you have no knowledge. Indeed, the hearing, the sight and the heart - about all those one will be questioned."*
> — **Surah Al-Isra (17:36)**

> *"He who speaks of me with a narration which he suspects is a lie, then he is one of the liars."*
> — **Sahih Muslim (Introduction)**""",
        "deep_explanation": """### Practical Steps to Audit a Hadith in the Digital Age

When you encounter a religious quote on social media or in an essay, apply this practical checklist:

1. **Step 1: Check for Specific Attribution:**
   - Red Flag: The post says merely "The Prophet said..." with no book name, no chapter, and no hadith number.
   - Good Practice: Look for exact citations (e.g., *Sahih al-Bukhari, Book of Good Manners, Hadith #6011*).

2. **Step 2: Cross-Check with Searchable Databases:**
   - Use recognized online Hadith archives (such as Sunnah.com) to look up the English keywords or Arabic text.
   - Confirm that the hadith actually exists in the cited collection and review the grading given by classical or recognized contemporary scholars.

3. **Step 3: Screen for Superstitious 'Chain Message' Language:**
   - Any message promising specific worldly wealth for forwarding to X people, or threatening misfortune for deleting it, is 100% fabricated.

4. **Step 4: Practice Digital Restraint:**
   - If you cannot locate the source, or if the report is graded Dha'if Jiddan or Mawdu', immediately halt the transmission. Delete the message and politely inform the sender.""",
        "comparison_table": {
            "title": "The Digital Hadith Verification Protocol Matrix",
            "headers": ["Verification Field", "Unverified / Careless Example", "Verified / Responsible Standard", "Action Required"],
            "rows": [
                ["1. Source Book", "'The Prophet said somewhere...'", "Sahih al-Bukhari, Hadith #13", "Verify book name and reference number"],
                ["2. Primary Narrator", "Anonymous / 'A wise man said...'", "Narrated by Anas ibn Malik (RA)", "Confirm eyewitness companion is named"],
                ["3. Authentic Text", "Emotional paraphrase with superstitious claims", "Exact preserved wording of the Hadith", "Strip modern sensationalism or chain threats"],
                ["4. Scholarly Grading", "Unchecked / 'Sounds inspiring'", "Graded: Sahih (Unanimous Consensus)", "If unverified, mark 'Not Supplied' & do not share"]
            ]
        },
        "worked_example": {
            "scenario": "Tariq receives a broadcast message on his class WhatsApp group stating: 'The Prophet said that whoever fails to brush their teeth before sleeping will have angels cursing them until morning. Forward this to 10 friends to be blessed.' Tariq is tempted to share it, but remembers the 4-Point Protocol. He asks the sender: 'Which book is this from? Who is the narrator? What is the grading?' The sender replies: 'I don't know, my cousin sent it to me.' Tariq checks a verified database, finds no such hadith, and replies politely: 'In Islam, the Prophet warned against attributing unverified sayings to him. Let's delete this message, and instead share the authentic Hadith from Sahih al-Bukhari where the Prophet simply says: \"Using the miswak is a purification for the mouth and pleasing to the Lord.\"'",
            "analysis": "Tariq exercised digital responsibility by stopping an unverified rumor and replacing it with an authentic, verified Hadith.",
            "takeaway": "Never forward unverified religious messages; replace false claims with authentic prophetic guidance."
        },
        "real_world_application": "Become a champion of truth in your school and family group chats. When classmates or family members post unverified quotes, superstitions, or chain messages attributing claims to the Prophet, respond gently: 'This is a beautiful reminder, but let's locate its source collection and authenticity grade before sharing it, so we protect our religion from unverified claims.' Promoting source verification elevates the intellectual and spiritual health of your entire community.",
        "reflection": "How does knowing the Prophet's warning—'Whoever lies about me deliberately, let him take his seat in the Fire'—transform your sense of responsibility when tapping 'share' on your phone?",
        "misconception": {
            "misconception": "Some people believe that sharing a fabricated Hadith is harmless as long as the message encourages people to be good.",
            "correction": "Inventing or sharing lies about the Prophet is a grave sin regardless of good intentions. Islam is already complete; it does not need manufactured lies to inspire righteousness."
        },
        "mcq": {
            "question": "What is the most responsible action you should take if you receive an inspiring online post quoting a Hadith, but it lacks a source book, narrator, or authenticity grading?",
            "options": [
                "A) Forward it immediately to all your contacts to gain quick spiritual rewards",
                "B) Assume it is authentic because it sounds beautiful and encourages moral behavior",
                "C) Stop and investigate its source using reliable databases; if it cannot be verified, do not share it",
                "D) Translate it into multiple languages and post it on your personal blog"
            ],
            "answer": "C",
            "explanation": "Responsible use of Hadith requires verifying the source collection, narrator, and scholarly grading. If these fields cannot be verified, the report must not be shared."
        },
        "summary": {
            "key_points": [
                "Muslims bear a serious spiritual responsibility to ensure Hadith authenticity before sharing.",
                "The 4-Point Protocol requires verifying: Source Collection, Primary Narrator, Exact Text, and Scholarly Grading.",
                "Fabricating or carelessly spreading unverified claims about the Prophet is severely condemned.",
                "Digital literacy and source sincerity protect the Muslim community from superstitions and fabricated rumors."
            ],
            "vocabulary": [
                {"term": "Amanah (أمانة)", "definition": "Moral integrity, trustworthiness, and intellectual honesty."},
                {"term": "Masdar (مصدر)", "definition": "The original primary source collection where a Hadith is documented."},
                {"term": "Al-Rawi al-A'la (الراوي الأعلى)", "definition": "The top companion narrator who directly witnessed the Prophet."},
                {"term": "Chain Message (رسالة متسلسلة)", "definition": "Superstitious messages demanding forwards under threat of misfortune."}
            ]
        },
        "exit_ticket": "List the four mandatory fields of the Digital Hadith Verification Protocol and state what you should do if a field is unknown."
    },

    # ─── LESSON 2.1.10 ──────────────────────────────────────────────────────────
    {
        "unit_order": 10,
        "unit_name": "Lesson 2.1.10: Unit review and presentation",
        "unit_description": "Synthesizes the complete sub-strand on Ulum al-Hadith, unifying definitions, collections, classifications, and modern verification ethics.",
        "lesson_title": "Unit Review and Presentation",
        "diagram_title": "Master Comprehensive Architecture of Ulum al-Hadith",
        "svg_fn": get_svg_lesson_10,
        "image": {
            "title": "Master Archival Codex of Classical Hadith Sciences",
            "url": "https://upload.wikimedia.org/wikipedia/commons/8/80/Sahih_al-Bukhari%2C_1890s_%282024-04-02%29.jpg",
            "caption": "A master historical Hadith compilation codex embodying the comprehensive architectural preservation of the Sunnah.",
            "author": "Islamic Classical Scholars Consortium",
            "licensing": "Public Domain",
            "source": "Wikimedia Commons"
        },
        "youtube": {
            "title": "Course | Explore Sciences of Hadith (Uloom Ul Hadith)",
            "youtube_id": "2_JKqnIQRZI",
            "description": "Comprehensive summary review of Hadith sciences, terminologies, and the historical methodology of authentication."
        },
        "inquiry_question": "How do we synthesize our knowledge of Ulum al-Hadith into a unified framework of academic integrity and responsible citizenship?",
        "connection": "Imagine completing an intensive course in architectural engineering. You now know how to test soil foundations, calculate structural load limits, inspect steel joints, and read master blueprints. Your capstone project is to present your knowledge to a civic council so that every building constructed in your city is safe, durable, and sound. In this final unit review, we assemble all the pillars we have mastered—definitions, Kutub al-Sittah, the three generations, authenticity classifications, and digital verification—to create an inspiring presentation that champions truth and integrity in our school.",
        "goals": [
            "Synthesize the core principles of Ulum al-Hadith into a unified conceptual framework.",
            "Demonstrate mastery of Hadith terminology through definitions and matching assessments.",
            "Design and present a 3-minute peer presentation on digital Hadith verification and academic integrity."
        ],
        "authoritative_concept": """### Master Synthesis of Ulum al-Hadith

The Sciences of Hadith (*Ulum al-Hadith*) constitute a unique, groundbreaking historical methodology developed by classical Muslim scholars to preserve divine revelation.

### Core Pillars Mastered in Topic 3:
1. **The Dual Foundations:** The Qur'an (primary divine scripture) and the Sunnah/Hadith (indispensable explanatory and living demonstration).
2. **The Canonical Compendiums (Kutub al-Sittah):**
   - *Al-Sahihayn:* Sahih al-Bukhari and Sahih Muslim (Gold Standard, 100% authentic).
   - *Al-Sunan al-Arba'ah:* Abu Dawood, Tirmidhi, Nasa'i, and Ibn Majah (Focused on jurisprudence; graded narrations).
3. **The Unbroken Chain of Custody:** Transmitted across the Three Blessed Generations: Sahabah → Tabi'un → Atba' al-Tabi'in.
4. **The Authenticity Spectrum:**
   - **Sahih:** Meets all 5 conditions with perfect memory (*Dabt Tamm*).
   - **Hasan:** Meets all conditions with lighter memory precision (*Dabt Khafif*); fully authentic and binding.
   - **Dha'if:** Deficient in chain continuity or narrator reliability; barred from creed and legal rulings.
   - **Mawdu':** Fabricated lies; completely prohibited.
5. **Modern Stewardship (*Amanah*):** Applying the 4-Point Protocol (Source, Narrator, Matn, Grading) in digital media.""",
        "scripture_panel": """### The Noble Heritage of Amanah (Trust)

> *"Indeed, Allah commands you to render trusts to whom they are due and when you judge between people to judge with justice..."*
> — **Surah An-Nisa (4:58)**

> The Prophet Muhammad (PBUH) stated:
> *"The believer is not one who slanders, curses, or speaks obscene and vulgar words."*
> — **Jami' at-Tirmidhi (1977)**""",
        "deep_explanation": """### Comprehensive Review Framework: From Ancient Manuscripts to Modern Screens

1. **The Scientific Anatomy:**
   - Every Hadith has two distinct components: the **Sanad / Isnad** (the chain of human transmitters) and the **Matn** (the actual text). Scholars audited both dimensions independently.

2. **The Moral Dimension of Research:**
   - Hadith scholars proved that factual accuracy cannot be separated from moral character. A person who lacked personal integrity (*'adalah*) in daily dealings was rejected as a reliable witness of truth.
   - This standard is the greatest gift of Islamic scholarship to global research ethics.

3. **Your Capstone Responsibility as a Grade 9 Student:**
   - In Kenya today, CBC education emphasizes *Integrity, Critical Thinking, and Digital Literacy*.
   - By mastering Ulum al-Hadith, you possess the tools to combat fake news, question unverified rumors, honor historical truth, and champion academic excellence.""",
        "comparison_table": {
            "title": "Master Synthesis Review Matrix: Ulum al-Hadith",
            "headers": ["Science Domain", "Core Concepts Mastered", "Primary Standard Applied", "Contemporary Value Developed"],
            "rows": [
                ["Terminology & Sources", "Hadith vs. Sunnah; Bayan, Takhsis, Tashri'", "Complementary authority with Qur'an", "Holistic understanding of religious law"],
                ["Canonical Compilations", "Kutub al-Sittah (Sahihayn & 4 Sunan)", "Strictest authentication in Bukhari & Muslim", "Source citation and bibliographical respect"],
                ["Historical Transmission", "Sahabah, Tabi'un, Atba' al-Tabi'in", "Continuous master-disciple chain (Isnad)", "Honoring mentors and generational wisdom"],
                ["Classification Spectrum", "Sahih, Hasan, Dha'if, Mawdu'", "The 5-condition padlock of authenticity", "Scientific precision and intellectual nuance"],
                ["Digital Application", "4-Point Verification Protocol", "Source, Narrator, Matn, Grading", "Combating online rumors & academic honesty"]
            ]
        },
        "worked_example": {
            "scenario": "As a capstone unit project, Mr. Khalid divides the Grade 9 IRE class into groups to present 'Hadith Literacy' to the junior secondary students. Halima's group creates a multimedia presentation titled: 'The Original Peer-Review: How Classical Scholars Protected Truth.' They use diagrams showing the Rihlah travels, the five conditions of Sahih, and the modern 4-point digital checklist. The junior students are amazed to learn that Hadith preservation was a scientific, evidence-based discipline. The school principal commends the Grade 9 students for their clarity, research rigor, and presentation poise.",
            "analysis": "Communicating knowledge through structured presentations cements deep understanding and empowers students as educational leaders.",
            "takeaway": "True mastery of knowledge is demonstrated when you can explain it simply and inspire others to value the truth."
        },
        "real_world_application": "Design a 3-minute oral presentation or a mini-poster for your school's noticeboard or Islamic Society assembly. Your theme: 'Think Before You Forward: A Student Guide to Hadith Verification Online.' Use the 4-Point Protocol to teach your peers how to identify unverified posts and uphold academic and religious integrity in WhatsApp and social media spaces.",
        "reflection": "How has your understanding of Islamic knowledge and the credibility of Hadith changed from Lesson 1 to Lesson 10? What does the concept of Amanah (trustworthiness) mean to you personally as an aspiring scholar?",
        "misconception": {
            "misconception": "Some think that Ulum al-Hadith is merely an ancient history subject with no practical relevance to modern life.",
            "correction": "Ulum al-Hadith is the ultimate masterclass in critical thinking, source criticism, and information verification—skills that are urgently needed to navigate today's internet, combat misinformation, and uphold personal integrity."
        },
        "matching_exercise": {
            "title": "Interactive Terminology Mastery Assessment",
            "instructions": "Match each Hadith concept (1-4) with its correct definition (A-D):",
            "pairs": [
                {"number": "1", "term": "Isnad (إسناد)", "letter": "D", "definition": "The continuous chain of narrators transmitting the report from compiler to the Prophet."},
                {"number": "2", "term": "Matn (متن)", "letter": "B", "definition": "The actual text or wording of the prophetic statement or action."},
                {"number": "3", "term": "Tabi'un (تابعون)", "letter": "A", "definition": "The second generation of Muslims who learned directly from the Sahabah."},
                {"number": "4", "term": "'Adalah (عدالة)", "letter": "C", "definition": "The upright moral character, piety, and integrity of a transmitter."}
            ],
            "correct_mapping": "1-D, 2-B, 3-A, 4-C",
            "explanation": "Isnad is the chain of transmitters; Matn is the textual statement; Tabi'un are the Successors of the Companions; and 'Adalah represents narrator moral integrity."
        },
        "summary": {
            "key_points": [
                "Ulum al-Hadith is a comprehensive, scientific discipline safeguarding prophetic guidance across history.",
                "The Kutub al-Sittah represent centuries of rigorous scholarship and peer-reviewed verification.",
                "Authenticity grading into Sahih, Hasan, and Dha'if protects Islamic law and creed from corruption.",
                "Modern Muslims must practice Amanah by verifying sources before quoting or forwarding religious information online."
            ],
            "vocabulary": [
                {"term": "Ulum al-Hadith (علوم الحديث)", "definition": "The specialized sciences and methodologies governing Hadith transmission and verification."},
                {"term": "Muttafaqun 'Alayh (متفق عليه)", "definition": "Agreed upon; a Hadith recorded in both Sahih al-Bukhari and Sahih Muslim."},
                {"term": "Amanah al-'Ilmiyyah (الأمانة العلمية)", "definition": "Academic integrity and scrupulous honesty in research and attribution."},
                {"term": "Hukm al-Hadith (حكم الحديث)", "definition": "The definitive critical grading of a Hadith's authenticity rendered by scholars."}
            ]
        },
        "exit_ticket": "Write one clear, persuasive sentence explaining to a friend why we can place absolute confidence in an authenticated Sahih Hadith."
    }
]


# ─── INGESTION RUNNER ─────────────────────────────────────────────────────────

def ingest_grade9_ire_topic3():
    print("=" * 80)
    print("VLEARN INGESTION ENGINE: GRADE 9 IRE — TOPIC 3: ULUM AL-HADITH")
    print("Target Topic ID: 343 | Strict Subject & Topic Isolation")
    print("=" * 80)

    with transaction.atomic():
        # Retrieve target topic 343
        topic = Topic.objects.select_related("subject", "subject__grade", "subject__grade__curriculum").get(id=343)
        subject = topic.subject
        grade = subject.grade
        curriculum = grade.curriculum

        print(f"Curriculum : {curriculum.name}")
        print(f"Grade      : {grade.name} (ID: {grade.id})")
        print(f"Subject    : {subject.name} (ID: {subject.id})")
        print(f"Topic      : {topic.name} (ID: {topic.id}, Order: {topic.order})")
        print("-" * 80)

        # Update topic metadata
        topic.name = "Ulum al-Hadith (The Sciences of Hadith)"
        topic.description = (
            "Comprehensive study of Ulum al-Hadith: definition and role as guidance alongside the Qur'an, "
            "Kutub al-Sittah collections, preservation factors, transmission through Tabi'un and Atba' al-Tabi'in, "
            "authenticity classifications (Sahih, Hasan, Dha'if), compilation processes, and digital verification ethics."
        )
        topic.save()

        # Clean existing units under topic 343 (Strictly isolated to Topic 343)
        existing_units = LearningUnit.objects.filter(topic=topic)
        if existing_units.exists():
            print(f"[*] Removing {existing_units.count()} existing LearningUnits under Topic 343...")
            existing_units.delete()

        # Clean any orphan lessons under topic 343
        orphan_lessons = Lesson.objects.filter(topic=topic)
        if orphan_lessons.exists():
            print(f"[*] Removing {orphan_lessons.count()} orphan Lessons under Topic 343...")
            orphan_lessons.delete()

        total_units_created = 0
        total_lessons_created = 0
        total_blocks_created = 0
        total_assets_created = 0

        for cfg in LESSONS_DATA:
            u_order = cfg["unit_order"]
            u_name = cfg["unit_name"]
            l_title = cfg["lesson_title"]

            print(f"\n>>> [Unit {u_order}/10] Ingesting: '{l_title}'")

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
                    "curriculum_framework": "CBC Kenya Grade 9 IRE Strand 2",
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
                url=f"https://vlearn.africa/assets/diagrams/ire/grade9_topic_3_lesson_{u_order}.svg",
                metadata={
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
                content={"markdown": clean_text(cfg["authoritative_concept"])}
            )

            LessonBlock.objects.create(
                lesson=lesson, page_number=2, page_title="Core Concept & Scripture",
                order=40, component_order=2,
                block_type="callout", component_type="callout",
                title="Scripture & Sources Panel",
                content={
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
                content={"markdown": clean_text(cfg["deep_explanation"])}
            )

            b_p3_diag = LessonBlock.objects.create(
                lesson=lesson, page_number=3, page_title="Deep Explanation & Diagram",
                order=60, component_order=2,
                block_type="suggested_diagram", component_type="suggested_diagram",
                title=f"Diagram: {clean_text(cfg['diagram_title'])}",
                content={
                    "title": f"Diagram: {clean_text(cfg['diagram_title'])}",
                    "caption": f"Pedagogical vector SVG architecture for {l_title}.",
                    "svg": svg_content,
                    "svg_xml": svg_content
                }
            )
            b_p3_diag.assets.add(svg_asset)

            # Comparison table on Card 3
            if "comparison_table" in cfg:
                LessonBlock.objects.create(
                    lesson=lesson, page_number=3, page_title="Deep Explanation & Diagram",
                    order=70, component_order=3,
                    block_type="comparison_table", component_type="comparison_table",
                    title=clean_text(cfg["comparison_table"]["title"]),
                    content=clean_dict(cfg["comparison_table"])
                )

            # ───────────────────────────────────────────────────────────────────
            # CARD 4 (Page 4): Worked Example & Relatable Scenario
            # ───────────────────────────────────────────────────────────────────
            LessonBlock.objects.create(
                lesson=lesson, page_number=4, page_title="Worked Example & Scenario",
                order=80, component_order=1,
                block_type="worked_example", component_type="worked_example",
                title="Relatable Student Scenario & Analysis",
                content={
                    "scenario": clean_text(cfg["worked_example"]["scenario"]),
                    "analysis": clean_text(cfg["worked_example"]["analysis"]),
                    "takeaway": clean_text(cfg["worked_example"]["takeaway"]),
                    "markdown": f"### Scenario\n\n{clean_text(cfg['worked_example']['scenario'])}\n\n### Analytical Breakdown\n\n{clean_text(cfg['worked_example']['analysis'])}\n\n### Core Takeaway\n\n**{clean_text(cfg['worked_example']['takeaway'])}**"
                }
            )

            # ───────────────────────────────────────────────────────────────────
            # CARD 5 (Page 5): Real-World Application, Reflection & Misconception
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
                        "misconception": clean_text(cfg["misconception"]["misconception"]),
                        "correction": clean_text(cfg["misconception"]["correction"]),
                        "markdown": f"### Common Misconception\n\n❌ *{clean_text(cfg['misconception']['misconception'])}*\n\n### Factual Correction\n\n✓ **{clean_text(cfg['misconception']['correction'])}**"
                    }
                )

            # ───────────────────────────────────────────────────────────────────
            # CARD 6 (Page 6): Interactive Assessment / Knowledge Check
            # ───────────────────────────────────────────────────────────────────
            if "mcq" in cfg:
                LessonBlock.objects.create(
                    lesson=lesson, page_number=6, page_title="Knowledge Check & Assessment",
                    order=130, component_order=1,
                    block_type="knowledge_check", component_type="knowledge_check",
                    title="Interactive Knowledge Check",
                    content=clean_dict(cfg["mcq"])
                )
            elif "matching_exercise" in cfg:
                LessonBlock.objects.create(
                    lesson=lesson, page_number=6, page_title="Knowledge Check & Assessment",
                    order=130, component_order=1,
                    block_type="knowledge_check", component_type="knowledge_check",
                    title="Interactive Terminology Matching",
                    content=clean_dict(cfg["matching_exercise"])
                )

            # ───────────────────────────────────────────────────────────────────
            # CARD 7 (Page 7): Summary, Key Points & Mini-Activity
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
                    "markdown": f"### Key Principles\n\n" + "\n".join([f"- {kp}" for kp in cfg["summary"]["key_points"]]) + "\n\n### Vocabulary Review\n\n" + "\n".join([f"- **{v['term']}**: {v['definition']}" for v in cfg["summary"]["vocabulary"]])
                }
            )

            LessonBlock.objects.create(
                lesson=lesson, page_number=7, page_title="Summary & Exit Ticket",
                order=150, component_order=2,
                block_type="mini_activity", component_type="mini_activity",
                title="Exit Ticket Challenge",
                content={
                    "activity": clean_text(cfg["exit_ticket"]),
                    "prompt": clean_text(cfg["exit_ticket"]),
                    "markdown": f"### Exit Ticket Challenge\n\n📝 **{clean_text(cfg['exit_ticket'])}**"
                }
            )

            blocks_count = lesson.blocks.count()
            total_blocks_created += blocks_count
            print(f"  [+] Created 7 Cards / Pages with {blocks_count} Blocks and 3 LessonAssets")

        print("\n" + "=" * 80)
        print("TOPIC 343 INGESTION & ENRICHMENT COMPLETE!")
        print(f"  - Subject           : {subject.name} (ID: {subject.id})")
        print(f"  - Topic             : {topic.name} (ID: {topic.id}, Order: {topic.order})")
        print(f"  - LearningUnits     : {total_units_created}")
        print(f"  - Lessons Published : {total_lessons_created}")
        print(f"  - LessonBlocks      : {total_blocks_created}")
        print(f"  - LessonAssets      : {total_assets_created}")
        print("=" * 80)


if __name__ == "__main__":
    ingest_grade9_ire_topic3()
