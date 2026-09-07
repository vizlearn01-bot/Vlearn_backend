"""
VLearn CBC Grade 9 IRE — Topic 19: Unity of Muslims
Production Ingestion and Enrichment Script for all 4 Lessons

Target Topic in DB: Topic ID 359 (Subject: IRE ID 53, Grade: Grade 9 ID 18)
Source Markdown: /home/jason-bitega/Desktop/VL/vlearn_repositories/Grade 9 IRE/unity-of-muslims.md

4 Lessons Ingested & Fully Enriched:
  1. Lesson 7.2.1: Meaning and importance of Muslim unity
  2. Lesson 7.2.2: Factors that enhance Muslim unity in Kenya
  3. Lesson 7.2.3: Challenges that undermine Muslim unity in Kenya
  4. Lesson 7.2.4: Practising unity and building a harmonious society
"""

import os
import sys
import re
import xml.etree.ElementTree as ET
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
    """Removes bracket citations and internal pedagogical tags while preserving markdown."""
    if not text:
        return ""
    text = re.sub(r'\[(?:\d+(?:\.\d+)?(?:,\s*\d+(?:\.\d+)?)*|image_\d+|S\d+.*?|[\d,\s]{2,})\]', '', text)
    text = re.sub(
        r'\[(VISUAL|QURAN REFERENCE|HADITH REFERENCE|BIBLE PASSAGE|BIBLE REFERENCE|CRITICAL THINKING|VALUES|'
        r'MISCONCEPTION|MISCONCEPTION CHECK|INTERACTION|ETHICAL SCENARIO|KEY VERSE|'
        r'REAL WORLD APPLICATION|PEDAGOGICAL ARCHITECTURE|PROJECT TITLE|REFLECTION|'
        r'COMPARISON TABLE|INFOGRAPHIC|SVG|DIAGRAM)[^\]]*\]',
        '',
        text,
        flags=re.IGNORECASE
    )
    text = re.sub(r'\[Source:[^\]]*\]', '', text, flags=re.IGNORECASE)
    text = re.sub(r'^[ \t]*[•\u2022][ \t]*', '- ', text, flags=re.MULTILINE)
    text = re.sub(r'([^\n])[ \t]+[•\u2022][ \t]+', r'\1\n- ', text)
    return text.strip()


# ─────────────────────────────────────────────────────────────────────────────
# 4 DEDICATED RESPONSIVE PEDAGOGICAL VECTOR SVGS (#0f172a theme, viewBox 880x440)
# ─────────────────────────────────────────────────────────────────────────────

def get_svg_lesson_1():
    """Lesson 7.2.1: The Rope of Allah (Hablullah) Binding the One Body (Ummah)"""
    return """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 880 440" width="100%" height="100%">
  <defs>
    <linearGradient id="bg191" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#0f172a"/>
      <stop offset="50%" stop-color="#1e293b"/>
      <stop offset="100%" stop-color="#0f172a"/>
    </linearGradient>
  </defs>

  <rect width="880" height="440" rx="14" fill="url(#bg191)"/>
  <rect x="2" y="2" width="876" height="436" rx="12" fill="none" stroke="#334155" stroke-width="1.5"/>

  <!-- Header -->
  <text x="440" y="38" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="16" font-weight="700" text-anchor="middle">THE FOUNDATION OF MUSLIM UNITY: HABLULLAH &amp; THE ONE BODY</text>
  <text x="440" y="58" fill="#94a3b8" font-family="system-ui, sans-serif" font-size="12" text-anchor="middle">How Faith in the Qur'an and Sunnah Unites Diverse Peoples into an Inseparable Ummah</text>

  <!-- Central Anchor Box: The Rope of Allah -->
  <g transform="translate(320, 80)">
    <rect width="240" height="110" rx="10" fill="#1e293b" stroke="#fbbf24" stroke-width="2"/>
    <circle cx="120" cy="38" r="22" fill="#78350f" stroke="#fbbf24" stroke-width="1.5"/>
    <text x="120" y="45" fill="#fef08a" font-family="system-ui, sans-serif" font-size="16" font-weight="bold" text-anchor="middle">⚓</text>
    <text x="120" y="76" fill="#f8fafc" font-family="system-ui, sans-serif" font-size="13" font-weight="700" text-anchor="middle">THE ROPE OF ALLAH</text>
    <text x="120" y="94" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="11" font-weight="600" text-anchor="middle">Hablullah: Qur'an &amp; Sunnah</text>
  </g>

  <!-- 4 Radiating Community Strands -->
  <!-- Strand 1: Coastal Swahili -->
  <g transform="translate(45, 220)">
    <rect width="180" height="150" rx="8" fill="#1e293b" stroke="#0284c7" stroke-width="1.5"/>
    <text x="90" y="26" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="12" font-weight="700" text-anchor="middle">COASTAL SWAHILI</text>
    <text x="12" y="52" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="11">
      <tspan x="12" dy="0">• Maritime trade heritage</tspan>
      <tspan x="12" dy="18">• Kiswahili literature</tspan>
      <tspan x="12" dy="18">• Stone town mosques</tspan>
      <tspan x="12" dy="18">• Bound by Hablullah</tspan>
    </text>
    <rect x="12" y="112" width="156" height="24" rx="4" fill="#0f172a"/>
    <text x="90" y="128" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="10" font-weight="600" text-anchor="middle">One Faith</text>
  </g>

  <!-- Strand 2: Western Kenya -->
  <g transform="translate(245, 220)">
    <rect width="180" height="150" rx="8" fill="#1e293b" stroke="#10b981" stroke-width="1.5"/>
    <text x="90" y="26" fill="#34d399" font-family="system-ui, sans-serif" font-size="12" font-weight="700" text-anchor="middle">WESTERN KENYA</text>
    <text x="12" y="52" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="11">
      <tspan x="12" dy="0">• Mumias royal heritage</tspan>
      <tspan x="12" dy="18">• Nabongo Mumia legacy</tspan>
      <tspan x="12" dy="18">• Agricultural &amp; trade ties</tspan>
      <tspan x="12" dy="18">• Bound by Hablullah</tspan>
    </text>
    <rect x="12" y="112" width="156" height="24" rx="4" fill="#0f172a"/>
    <text x="90" y="128" fill="#34d399" font-family="system-ui, sans-serif" font-size="10" font-weight="600" text-anchor="middle">One Ummah</text>
  </g>

  <!-- Strand 3: Central Kenya -->
  <g transform="translate(455, 220)">
    <rect width="180" height="150" rx="8" fill="#1e293b" stroke="#a855f7" stroke-width="1.5"/>
    <text x="90" y="26" fill="#c084fc" font-family="system-ui, sans-serif" font-size="12" font-weight="700" text-anchor="middle">CENTRAL URBAN</text>
    <text x="12" y="52" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="11">
      <tspan x="12" dy="0">• Pumwani &amp; Kibera</tspan>
      <tspan x="12" dy="18">• Railway history hubs</tspan>
      <tspan x="12" dy="18">• Jamia Mosque civic center</tspan>
      <tspan x="12" dy="18">• Bound by Hablullah</tspan>
    </text>
    <rect x="12" y="112" width="156" height="24" rx="4" fill="#0f172a"/>
    <text x="90" y="128" fill="#c084fc" font-family="system-ui, sans-serif" font-size="10" font-weight="600" text-anchor="middle">One Qiblah</text>
  </g>

  <!-- Strand 4: North Eastern -->
  <g transform="translate(655, 220)">
    <rect width="180" height="150" rx="8" fill="#1e293b" stroke="#f59e0b" stroke-width="1.5"/>
    <text x="90" y="26" fill="#fbbf24" font-family="system-ui, sans-serif" font-size="12" font-weight="700" text-anchor="middle">NORTH EASTERN</text>
    <text x="12" y="52" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="11">
      <tspan x="12" dy="0">• Pastoralist resilience</tspan>
      <tspan x="12" dy="18">• Duksi Quran schools</tspan>
      <tspan x="12" dy="18">• Maslah reconciliation</tspan>
      <tspan x="12" dy="18">• Bound by Hablullah</tspan>
    </text>
    <rect x="12" y="112" width="156" height="24" rx="4" fill="#0f172a"/>
    <text x="90" y="128" fill="#fbbf24" font-family="system-ui, sans-serif" font-size="10" font-weight="600" text-anchor="middle">One Heart</text>
  </g>

  <!-- Connecting Ropes from Anchor to Boxes -->
  <path d="M360,190 L135,220" stroke="#fbbf24" stroke-width="2.5" stroke-dasharray="6 4"/>
  <path d="M410,190 L335,220" stroke="#fbbf24" stroke-width="2.5" stroke-dasharray="6 4"/>
  <path d="M470,190 L545,220" stroke="#fbbf24" stroke-width="2.5" stroke-dasharray="6 4"/>
  <path d="M520,190 L745,220" stroke="#fbbf24" stroke-width="2.5" stroke-dasharray="6 4"/>

  <!-- Footer Banner -->
  <rect x="45" y="390" width="790" height="30" rx="6" fill="#1e293b" stroke="#475569" stroke-width="1"/>
  <text x="440" y="410" fill="#34d399" font-family="system-ui, sans-serif" font-size="12" font-weight="600" text-anchor="middle">"The believers, in their mutual love, are like a single body: when one limb aches, the whole body responds." — Sahih Muslim 2586</text>
</svg>"""


def get_svg_lesson_2():
    """Lesson 7.2.2: The Keystone Architecture of Muslim Unity in Kenya"""
    return """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 880 440" width="100%" height="100%">
  <defs>
    <linearGradient id="bg192" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#0f172a"/>
      <stop offset="50%" stop-color="#1e293b"/>
      <stop offset="100%" stop-color="#0f172a"/>
    </linearGradient>
  </defs>

  <rect width="880" height="440" rx="14" fill="url(#bg192)"/>
  <rect x="2" y="2" width="876" height="436" rx="12" fill="none" stroke="#334155" stroke-width="1.5"/>

  <!-- Header -->
  <text x="440" y="38" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="16" font-weight="700" text-anchor="middle">THE KEYSTONE ARCH OF MUSLIM UNITY IN KENYA</text>
  <text x="440" y="58" fill="#94a3b8" font-family="system-ui, sans-serif" font-size="12" text-anchor="middle">Four Interlocking Blocks Supporting Community Strength, Harmony and Collective Development</text>

  <!-- Keystone at Top Center -->
  <g transform="translate(340, 75)">
    <polygon points="20,0 180,0 160,80 40,80" fill="#b45309" stroke="#fbbf24" stroke-width="2"/>
    <text x="100" y="35" fill="#ffffff" font-family="system-ui, sans-serif" font-size="12" font-weight="800" text-anchor="middle">KEYSTONE: TAQWA</text>
    <text x="100" y="55" fill="#fef08a" font-family="system-ui, sans-serif" font-size="10.5" font-weight="600" text-anchor="middle">Universal Moral Equality</text>
    <text x="100" y="70" fill="#ffffff" font-family="system-ui, sans-serif" font-size="9.5" text-anchor="middle">(Surah Al-Hujurat 49:13)</text>
  </g>

  <!-- 4 Supporting Arch Blocks -->
  <!-- Block 1: Shared Worship -->
  <g transform="translate(50, 165)">
    <rect width="180" height="195" rx="8" fill="#1e293b" stroke="#38bdf8" stroke-width="1.5"/>
    <rect width="180" height="32" rx="8" fill="#0284c7"/>
    <text x="90" y="21" fill="#ffffff" font-family="system-ui, sans-serif" font-size="11.5" font-weight="700" text-anchor="middle">1. SHARED WORSHIP</text>
    <text x="12" y="54" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10.5">
      <tspan x="12" dy="0">• Daily 5 Salat in Jam'ah</tspan>
      <tspan x="12" dy="18">• Friday Jumu'ah leveling</tspan>
      <tspan x="12" dy="18">• Fasting in Ramadan</tspan>
      <tspan x="12" dy="18">• Shared Eid gatherings</tspan>
      <tspan x="12" dy="18">• Single Qiblah facing</tspan>
      <tspan x="12" dy="18">• Erases wealth classes</tspan>
    </text>
    <rect x="12" y="160" width="156" height="22" rx="4" fill="#0f172a"/>
    <text x="90" y="175" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="10" font-weight="600" text-anchor="middle">Ritual Social Leveler</text>
  </g>

  <!-- Block 2: Inclusive Institutions -->
  <g transform="translate(245, 165)">
    <rect width="180" height="195" rx="8" fill="#1e293b" stroke="#10b981" stroke-width="1.5"/>
    <rect width="180" height="32" rx="8" fill="#059669"/>
    <text x="90" y="21" fill="#ffffff" font-family="system-ui, sans-serif" font-size="11.5" font-weight="700" text-anchor="middle">2. INCLUSIVE ORGS</text>
    <text x="12" y="54" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10.5">
      <tspan x="12" dy="0">• SUPKEM coordination</tspan>
      <tspan x="12" dy="18">• Council of Imams (CIPK)</tspan>
      <tspan x="12" dy="18">• Kenya Muslim Youth Alliance</tspan>
      <tspan x="12" dy="18">• Joint moon-sighting</tspan>
      <tspan x="12" dy="18">• Unified national voice</tspan>
      <tspan x="12" dy="18">• National advocacy</tspan>
    </text>
    <rect x="12" y="160" width="156" height="22" rx="4" fill="#0f172a"/>
    <text x="90" y="175" fill="#34d399" font-family="system-ui, sans-serif" font-size="10" font-weight="600" text-anchor="middle">National Umbrella</text>
  </g>

  <!-- Block 3: Pooled Charity -->
  <g transform="translate(455, 165)">
    <rect width="180" height="195" rx="8" fill="#1e293b" stroke="#a855f7" stroke-width="1.5"/>
    <rect width="180" height="32" rx="8" fill="#7e22ce"/>
    <text x="90" y="21" fill="#ffffff" font-family="system-ui, sans-serif" font-size="11.5" font-weight="700" text-anchor="middle">3. POOLED CHARITY</text>
    <text x="12" y="54" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10.5">
      <tspan x="12" dy="0">• Zakat collection trusts</tspan>
      <tspan x="12" dy="18">• Drought relief to North</tspan>
      <tspan x="12" dy="18">• Orphan sponsorships</tspan>
      <tspan x="12" dy="18">• Education bursary funds</tspan>
      <tspan x="12" dy="18">• Jamia Mosque aid</tspan>
      <tspan x="12" dy="18">• Eliminates poverty</tspan>
    </text>
    <rect x="12" y="160" width="156" height="22" rx="4" fill="#0f172a"/>
    <text x="90" y="175" fill="#c084fc" font-family="system-ui, sans-serif" font-size="10" font-weight="600" text-anchor="middle">Economic Solidarity</text>
  </g>

  <!-- Block 4: Intra-faith Dialogue -->
  <g transform="translate(650, 165)">
    <rect width="180" height="195" rx="8" fill="#1e293b" stroke="#f59e0b" stroke-width="1.5"/>
    <rect width="180" height="32" rx="8" fill="#d97706"/>
    <text x="90" y="21" fill="#ffffff" font-family="system-ui, sans-serif" font-size="11.5" font-weight="700" text-anchor="middle">4. DIALOGUE &amp; ADAB</text>
    <text x="12" y="54" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10.5">
      <tspan x="12" dy="0">• Respecting Madhahib</tspan>
      <tspan x="12" dy="18">• Adab al-Ikhtilaf (etiquette)</tspan>
      <tspan x="12" dy="18">• No excommunication</tspan>
      <tspan x="12" dy="18">• Interfaith relations</tspan>
      <tspan x="12" dy="18">• Peaceful coexistence</tspan>
      <tspan x="12" dy="18">• Celebrating diversity</tspan>
    </text>
    <rect x="12" y="160" width="156" height="22" rx="4" fill="#0f172a"/>
    <text x="90" y="175" fill="#fbbf24" font-family="system-ui, sans-serif" font-size="10" font-weight="600" text-anchor="middle">Respectful Adab</text>
  </g>

  <!-- Footer Banner -->
  <rect x="50" y="385" width="780" height="30" rx="6" fill="#1e293b" stroke="#475569" stroke-width="1"/>
  <text x="440" y="405" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="11.5" font-weight="600" text-anchor="middle">"An Arab has no superiority over a non-Arab... except by piety and good action." — The Prophet's Last Sermon</text>
</svg>"""


def get_svg_lesson_3():
    """Lesson 7.2.3: The Termites of Division vs The Tabayyun Verification Shield"""
    return """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 880 440" width="100%" height="100%">
  <defs>
    <linearGradient id="bg193" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#0f172a"/>
      <stop offset="50%" stop-color="#1e293b"/>
      <stop offset="100%" stop-color="#0f172a"/>
    </linearGradient>
  </defs>

  <rect width="880" height="440" rx="14" fill="url(#bg193)"/>
  <rect x="2" y="2" width="876" height="436" rx="12" fill="none" stroke="#334155" stroke-width="1.5"/>

  <!-- Header -->
  <text x="440" y="38" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="16" font-weight="700" text-anchor="middle">CHALLENGES TO MUSLIM UNITY: THE TERMITES OF DIVISION</text>
  <text x="440" y="58" fill="#94a3b8" font-family="system-ui, sans-serif" font-size="12" text-anchor="middle">Halting the Destructive Cycle of Sectarianism, Tribalism, and Unverified Digital Gossip</text>

  <!-- Left: The 3 Termites of Division -->
  <g transform="translate(45, 85)">
    <rect width="375" height="285" rx="10" fill="#1e293b" stroke="#ef4444" stroke-width="2"/>
    <rect width="375" height="40" rx="10" fill="#991b1b"/>
    <text x="187" y="26" fill="#ffffff" font-family="system-ui, sans-serif" font-size="13.5" font-weight="700" text-anchor="middle">THE THREE TERMITES OF FRAGMENTATION</text>

    <g transform="translate(20, 55)">
      <text x="0" y="16" fill="#fca5a5" font-family="system-ui, sans-serif" font-size="12" font-weight="bold">1. Sectarianism (Tawa'ifiyyah):</text>
      <text x="0" y="34" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="11">Rigid intolerance over secondary Fiqh issues; excommunicating peers.</text>
    </g>

    <g transform="translate(20, 115)">
      <text x="0" y="16" fill="#fca5a5" font-family="system-ui, sans-serif" font-size="12" font-weight="bold">2. Tribal Prejudice (Asabiyyah):</text>
      <text x="0" y="34" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="11">Favoring one's clan over qualifications; excluding minority groups.</text>
    </g>

    <g transform="translate(20, 175)">
      <text x="0" y="16" fill="#fca5a5" font-family="system-ui, sans-serif" font-size="12" font-weight="bold">3. Digital Gossip &amp; Rumors:</text>
      <text x="0" y="34" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="11">Forwarding unverified WhatsApp audio/text slandering leaders without Tabayyun.</text>
    </g>

    <rect x="20" y="240" width="335" height="30" rx="6" fill="#450a0a"/>
    <text x="187" y="260" fill="#fca5a5" font-family="system-ui, sans-serif" font-size="11" font-weight="600" text-anchor="middle">Quran 8:46: "Lest you lose courage &amp; strength depart"</text>
  </g>

  <!-- Right: The Tabayyun Defense Shield -->
  <g transform="translate(460, 85)">
    <rect width="375" height="285" rx="10" fill="#1e293b" stroke="#10b981" stroke-width="2"/>
    <rect width="375" height="40" rx="10" fill="#065f46"/>
    <text x="187" y="26" fill="#ffffff" font-family="system-ui, sans-serif" font-size="13.5" font-weight="700" text-anchor="middle">THE PROPHETIC TABAYYUN SHIELD</text>

    <g transform="translate(20, 55)">
      <text x="0" y="16" fill="#6ee7b7" font-family="system-ui, sans-serif" font-size="12" font-weight="bold">1. Verify Before Forwarding:</text>
      <text x="0" y="34" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="11">Stop rumors at your screen. Delete sensational group messages.</text>
    </g>

    <g transform="translate(20, 115)">
      <text x="0" y="16" fill="#6ee7b7" font-family="system-ui, sans-serif" font-size="12" font-weight="bold">2. Merit &amp; Taqwa Over Tribe:</text>
      <text x="0" y="34" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="11">Appoint committee and club leaders based on Amanah, not ethnic ties.</text>
    </g>

    <g transform="translate(20, 175)">
      <text x="0" y="16" fill="#6ee7b7" font-family="system-ui, sans-serif" font-size="12" font-weight="bold">3. Broad-Minded Adab al-Ikhtilaf:</text>
      <text x="0" y="34" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="11">Respect legitimate scholarly diversity without attacking character.</text>
    </g>

    <rect x="20" y="240" width="335" height="30" rx="6" fill="#064e3b"/>
    <text x="187" y="260" fill="#6ee7b7" font-family="system-ui, sans-serif" font-size="11" font-weight="600" text-anchor="middle">Quran 49:6: "Investigate, lest you harm people in ignorance"</text>
  </g>

  <!-- Footer -->
  <rect x="45" y="390" width="790" height="30" rx="6" fill="#1e293b" stroke="#475569" stroke-width="1"/>
  <text x="440" y="410" fill="#fbbf24" font-family="system-ui, sans-serif" font-size="12" font-weight="600" text-anchor="middle">Disputes eat away at communal strength just like termites eat away at a bridge.</text>
</svg>"""


def get_svg_lesson_4():
    """Lesson 7.2.4: The Four-Step Unity Cultivator Protocol"""
    return """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 880 440" width="100%" height="100%">
  <defs>
    <linearGradient id="bg194" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#0f172a"/>
      <stop offset="50%" stop-color="#1e293b"/>
      <stop offset="100%" stop-color="#0f172a"/>
    </linearGradient>
  </defs>

  <rect width="880" height="440" rx="14" fill="url(#bg194)"/>
  <rect x="2" y="2" width="876" height="436" rx="12" fill="none" stroke="#334155" stroke-width="1.5"/>

  <!-- Header -->
  <text x="440" y="38" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="16" font-weight="700" text-anchor="middle">THE FOUR-STEP UNITY CULTIVATOR PROTOCOL</text>
  <text x="440" y="58" fill="#94a3b8" font-family="system-ui, sans-serif" font-size="12" text-anchor="middle">Actionable Daily Protocol for Students to Foster Peace, Resolve Conflict (Islaah) &amp; Cooperate (Ta'awun)</text>

  <!-- 4 Process Steps Flowing Horizontally -->
  <!-- Step 1: Spread Salam -->
  <g transform="translate(45, 85)">
    <rect width="180" height="285" rx="8" fill="#1e293b" stroke="#38bdf8" stroke-width="1.5"/>
    <rect width="180" height="36" rx="8" fill="#0284c7"/>
    <text x="90" y="23" fill="#ffffff" font-family="system-ui, sans-serif" font-size="12" font-weight="700" text-anchor="middle">STEP 1: SINCERE SALAM</text>
    
    <circle cx="90" cy="72" r="22" fill="#0c4a6e" stroke="#38bdf8" stroke-width="1.5"/>
    <text x="90" y="79" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="16" font-weight="bold" text-anchor="middle">1</text>
    
    <text x="90" y="118" fill="#f8fafc" font-family="system-ui, sans-serif" font-size="12" font-weight="600" text-anchor="middle">Greeting &amp; Warmth</text>
    <text x="12" y="145" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="11">
      <tspan x="12" dy="0">• Greet with peace first</tspan>
      <tspan x="12" dy="18">• Smile is charity (Sadaqah)</tspan>
      <tspan x="12" dy="18">• Greet known and unknown</tspan>
      <tspan x="12" dy="18">• Melts social coldness</tspan>
      <tspan x="12" dy="18">• Hadith: "Spread Salam"</tspan>
    </text>
    <rect x="12" y="238" width="156" height="24" rx="4" fill="#0f172a"/>
    <text x="90" y="254" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="10" font-weight="600" text-anchor="middle">Builds Mutual Love</text>
  </g>

  <!-- Step 2: Active Inclusion -->
  <g transform="translate(245, 85)">
    <rect width="180" height="285" rx="8" fill="#1e293b" stroke="#10b981" stroke-width="1.5"/>
    <rect width="180" height="36" rx="8" fill="#059669"/>
    <text x="90" y="23" fill="#ffffff" font-family="system-ui, sans-serif" font-size="12" font-weight="700" text-anchor="middle">STEP 2: INCLUSION</text>
    
    <circle cx="90" cy="72" r="22" fill="#064e3b" stroke="#10b981" stroke-width="1.5"/>
    <text x="90" y="79" fill="#34d399" font-family="system-ui, sans-serif" font-size="16" font-weight="bold" text-anchor="middle">2</text>
    
    <text x="90" y="118" fill="#f8fafc" font-family="system-ui, sans-serif" font-size="12" font-weight="600" text-anchor="middle">Welcoming the Quiet</text>
    <text x="12" y="145" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="11">
      <tspan x="12" dy="0">• Notice isolated peers</tspan>
      <tspan x="12" dy="18">• Invite to lunch or sport</tspan>
      <tspan x="12" dy="18">• Break tribal cliques</tspan>
      <tspan x="12" dy="18">• Value diverse voices</tspan>
      <tspan x="12" dy="18">• Empathy for newcomers</tspan>
    </text>
    <rect x="12" y="238" width="156" height="24" rx="4" fill="#0f172a"/>
    <text x="90" y="254" fill="#34d399" font-family="system-ui, sans-serif" font-size="10" font-weight="600" text-anchor="middle">Eliminates Loneliness</text>
  </g>

  <!-- Step 3: Conflict Islaah -->
  <g transform="translate(450, 85)">
    <rect width="180" height="285" rx="8" fill="#1e293b" stroke="#fbbf24" stroke-width="1.5"/>
    <rect width="180" height="36" rx="8" fill="#b45309"/>
    <text x="90" y="23" fill="#ffffff" font-family="system-ui, sans-serif" font-size="12" font-weight="700" text-anchor="middle">STEP 3: ISLAAH</text>
    
    <circle cx="90" cy="72" r="22" fill="#78350f" stroke="#fbbf24" stroke-width="1.5"/>
    <text x="90" y="79" fill="#fbbf24" font-family="system-ui, sans-serif" font-size="16" font-weight="bold" text-anchor="middle">3</text>
    
    <text x="90" y="118" fill="#f8fafc" font-family="system-ui, sans-serif" font-size="12" font-weight="600" text-anchor="middle">Reconciliation</text>
    <text x="12" y="145" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="11">
      <tspan x="12" dy="0">• Intervene in arguments</tspan>
      <tspan x="12" dy="18">• Listen without bias</tspan>
      <tspan x="12" dy="18">• Encourage apologies</tspan>
      <tspan x="12" dy="18">• Forgive past grudges</tspan>
      <tspan x="12" dy="18">• Quran 49:10 mandate</tspan>
    </text>
    <rect x="12" y="238" width="156" height="24" rx="4" fill="#0f172a"/>
    <text x="90" y="254" fill="#fbbf24" font-family="system-ui, sans-serif" font-size="10" font-weight="600" text-anchor="middle">Restores Peace</text>
  </g>

  <!-- Step 4: Joint Ta'awun -->
  <g transform="translate(655, 85)">
    <rect width="180" height="285" rx="8" fill="#1e293b" stroke="#a855f7" stroke-width="1.5"/>
    <rect width="180" height="36" rx="8" fill="#7e22ce"/>
    <text x="90" y="23" fill="#ffffff" font-family="system-ui, sans-serif" font-size="12" font-weight="700" text-anchor="middle">STEP 4: TA'AWUN</text>
    
    <circle cx="90" cy="72" r="22" fill="#581c87" stroke="#a855f7" stroke-width="1.5"/>
    <text x="90" y="79" fill="#c084fc" font-family="system-ui, sans-serif" font-size="16" font-weight="bold" text-anchor="middle">4</text>
    
    <text x="90" y="118" fill="#f8fafc" font-family="system-ui, sans-serif" font-size="12" font-weight="600" text-anchor="middle">Righteous Teamwork</text>
    <text x="12" y="145" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="11">
      <tspan x="12" dy="0">• Community cleaning days</tspan>
      <tspan x="12" dy="18">• Shared study groups</tspan>
      <tspan x="12" dy="18">• Charity fundraisers</tspan>
      <tspan x="12" dy="18">• Tree planting initiatives</tspan>
      <tspan x="12" dy="18">• Quran 5:2 mandate</tspan>
    </text>
    <rect x="12" y="238" width="156" height="24" rx="4" fill="#0f172a"/>
    <text x="90" y="254" fill="#c084fc" font-family="system-ui, sans-serif" font-size="10" font-weight="600" text-anchor="middle">National Flourishing</text>
  </g>

  <!-- Footer -->
  <rect x="45" y="390" width="790" height="30" rx="6" fill="#1e293b" stroke="#475569" stroke-width="1"/>
  <text x="440" y="410" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="12" font-weight="600" text-anchor="middle">"The believers are but brothers, so make peace between your brothers." — Surah Al-Hujurat 49:10</text>
</svg>"""


# ─────────────────────────────────────────────────────────────────────────────
# LESSON DATA SPECIFICATION (4 Lessons, 7 Cards Each)
# ─────────────────────────────────────────────────────────────────────────────

TOPIC_19_LESSONS = [
    {
        "unit_order": 1,
        "lesson_title": "Meaning and importance of Muslim unity",
        "inquiry": "What is the meaning of the Muslim Ummah, and why is unity considered a fundamental obligation in Islam?",
        "hook": "Picture a synchronized team of rowers racing along the Tana River. If each rower paddles in a different direction, at an irregular tempo, or according to their own personal whim, the boat spins helplessly, loses momentum, and capsizes. But when all rowers pull in unison, responsive to the coxswain, the shell glides effortlessly and swiftly toward victory. In the identical manner, the Muslim community is designed to function as an interdependent, unified crew. In Islam, unity is not a casual social ideal; it is a sacred, non-negotiable spiritual obligation.",
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/7/7b/The_Kaaba_during_Hajj.jpg/800px-The_Kaaba_during_Hajj.jpg",
        "image_title": "The Kaaba: Universal Center of Muslim Unity",
        "image_caption": "Millions of pilgrims from every nation and race circumambulating the Kaaba in Mecca, symbolizing the absolute unity and equality of the global Ummah.",
        "concept_name": "The Ummah: One Universal Body Bound by Hablullah",
        "concept_explanation": "The Ummah is the worldwide community of believers united by shared faith in the Oneness of Allah (Tawheed) and the finality of the Prophethood of Muhammad (PBUH), dissolving all barriers of race, language, social class, and geographic origin. Islam establishes communal unity as a mandatory religious duty commanded in Surah Ali 'Imran (3:103), likening the believers to a single physiological body.",
        "scripture_quran": "And hold firmly to the rope of Allah all together and do not become divided. And remember the favor of Allah upon you – when you were enemies and He brought your hearts together and you became, by His favor, brothers...",
        "scripture_quran_ref": "Surah Ali 'Imran 3:103",
        "scripture_hadith": "The believers, in their mutual love, mercy, and compassion, are like a single body. When any limb of it aches, the whole body responds with sleeplessness and fever.",
        "scripture_hadith_ref": "Sahih Muslim 2586",
        "deep_explanation": "The theology of Islamic unity rests upon three foundational pillars:\n1. The Anchor of Hablullah: The 'Rope of Allah' in Surah Ali 'Imran signifies the Holy Qur'an and authentic Sunnah. True unity is anchored in divine revelation rather than temporary political treaties or ethnic pacts.\n2. Physiological Empathy: The Prophetic body metaphor mandates that the distress of any believer—such as pastoralists facing drought in Garissa or a classmate enduring bullying—must provoke active, collective mobilization from the entire community.\n3. Universal Brotherhood (Ukhuwwah): Faith creates an indissoluble spiritual kinship that takes precedence over tribal loyalties, uniting Kenyan Muslims of Bantu, Cushitic, Nilotic, and Asian descent.",
        "diagram_title": "The Foundation of Muslim Unity: Hablullah & The One Body",
        "svg_func": get_svg_lesson_1,
        "table_title": "Foundations of Islamic Unity: Secular Coalitions vs Islamic Ukhuwwah",
        "table_headers": ["Dimension", "Secular / Political Coalitions", "Islamic Faith-Based Unity (Ukhuwwah)"],
        "table_rows": [
            ["Core Anchor", "Temporary political interest, territory, or financial gain", "The eternal 'Rope of Allah' (Qur'an and authentic Sunnah)"],
            ["Ethnic Diversity", "Often fractures along tribal, racial, and national borders", "Embraces racial diversity as intentional divine beauty (49:13)"],
            ["Response to Crisis", "Conditional upon strategic utility or diplomatic advantage", "Visceral, mandatory response: 'When one limb aches, all ache'"],
            ["Enduring Nature", "Dissolves when individual or group interests diverge", "Eternal covenant continuing into the life of the Hereafter"]
        ],
        "scenario": "At Sabaki Junior School, a new student named Yusuf transfers from a school in Lamu. He speaks with a distinct coastal Swahili accent and feels socially alienated. During lunch breaks, students divide themselves into exclusive neighborhood cliques, leaving Yusuf to eat alone. Hussein recalls the 'single body' Hadith from IRE class. Realizing that leaving Yusuf isolated wounds the unity of the entire class, Hussein leaves his friends, greets Yusuf with a warm Salam, shares lunch, and introduces him to the school football captain. Within days, Yusuf is thriving academically and socially.",
        "real_world": "Apply the 'One-Body Empathy Protocol' in your school this week. Observe your classmates and identify anyone who seems withdrawn, lonely, or struggling with studies. Proactively approach them with a cheerful Salam, sit beside them in class, and invite them into your revision group. Small daily gestures of brotherhood fulfill the prophetic command to heal aching limbs.",
        "reflection": "How does the 'single body' analogy reshape how we should react when we witness poverty or distress in remote Kenyan counties? Why is holding onto the Qur'an and Sunnah the only permanent guarantee against communal division?",
        "misconception": "Misconception: Believing that Islamic unity requires robotic uniformity where everyone must have identical opinions on every matter. Islam accommodates respectful diversity in secondary legal applications (Fiqh), while strictly demanding unity in core creed, brotherhood, and mutual affection.",
        "yt_id": "8G8_9V1q5cQ",
        "yt_title": "The Meaning of the Ummah and the Obligation of Unity",
        "yt_desc": "Scholarly overview of Surah Ali 'Imran 3:103, the 'single body' Hadith, and Islamic brotherhood.",
        "mcq": {
            "question": "According to Surah Ali 'Imran (3:103), what is the 'Rope of Allah' that Muslims are divinely commanded to hold firmly together to prevent division?",
            "options": [
                "A. The geographic borders and national constitutions of various countries.",
                "B. The cultural traditions and dialects of local ethnic tribes.",
                "C. The divine revelation of the Holy Qur'an and the authentic Sunnah.",
                "D. Commercial trade pacts and international economic alliances."
            ],
            "answer": "C",
            "explanation": "The 'Rope of Allah' (Hablullah) is the authoritative metaphor for the Qur'an and the Sunnah, serving as the immutable divine anchor that keeps the global Ummah united."
        },
        "summary_content": "The Ummah is a trans-national family of believers united by Tawheed. Surah Ali 'Imran (3:103) establishes unity as a mandatory religious duty, while the Prophet (PBUH) likened the community to a single body where every member feels and relieves the pain of another.",
        "key_points": [
            "The Ummah is the universal community of believers bound by faith across all worldly divisions.",
            "Holding firmly to Hablullah (the Qur'an and Sunnah) is an explicit divine command.",
            "The Prophet (PBUH) likened the Ummah to a single physiological body requiring active empathy.",
            "Differences in secondary opinions must never degenerate into tribalism or hatred."
        ],
        "exit_ticket": "State one practical way you can demonstrate the 'single body' concept to support a struggling classmate this week."
    },
    {
        "unit_order": 2,
        "lesson_title": "Factors that enhance Muslim unity in Kenya",
        "inquiry": "What are the key factors that can strengthen and enhance the unity of Muslims in Kenya today?",
        "hook": "Consider a towering Swahili coral-stone archway standing in Lamu for over four centuries. It is composed of dozens of individual stones of differing dimensions and colors. None of those stones could suspend itself in mid-air alone. Yet when carefully assembled, leaning against one another and locked together by a central, wedge-shaped keystone at the apex, they form an indestructible arch capable of carrying tons of weight. Kenya's multi-ethnic Muslim community is that archway. In this lesson, we explore the essential pillars and the divine keystone that preserve our national unity.",
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/c/cd/Jamia_Mosque_Nairobi.jpg/800px-Jamia_Mosque_Nairobi.jpg",
        "image_title": "Jamia Mosque Nairobi: National Institutional Anchor",
        "image_caption": "Iconic minarets and domes of Jamia Mosque Nairobi, representing central coordination, national welfare relief, and unity for Kenyan Muslims.",
        "concept_name": "The Four Enhancing Factors of Kenyan Muslim Cohesion",
        "concept_explanation": "Muslim cohesion in Kenya is enhanced by four foundational factors: shared congregational rituals (the Five Pillars of Islam), the divine standard of Taqwa (righteousness over tribe), national umbrella leadership institutions (such as SUPKEM and CIPK), and pooled socioeconomic welfare programs (Zakat, disaster relief, and Waqf trusts).",
        "scripture_quran": "O mankind, indeed We have created you from male and female and made you peoples and tribes that you may know one another. Indeed, the most noble of you in the sight of Allah is the most righteous of you...",
        "scripture_quran_ref": "Surah Al-Hujurat 49:13",
        "scripture_hadith": "An Arab has no superiority over a non-Arab, nor does a non-Arab have any superiority over an Arab; also a white has no superiority over a black, nor does a black have any superiority over a white except by piety and good action.",
        "scripture_hadith_ref": "The Prophet's Last Sermon (Musnad Ahmad 22978)",
        "deep_explanation": "Four practical engines cement Muslim solidarity across Kenya:\n1. Shared Rituals as Social Levelers: Standing shoulder to shoulder in Jumu'ah prayers, observing the dawn-to-dusk fast of Ramadan, and facing the identical Qiblah dissolves artificial barriers of wealth, social status, and regional origin.\n2. The Keystone of Taqwa: Implementing Surah Al-Hujurat (49:13) ensures that ethnic diversity (Bantu, Cushitic, Nilotic, Nubian, Asian) is celebrated as intentional divine design, repudiating tribal arrogance.\n3. National Umbrella Organizations: Bodies such as the Supreme Council of Kenya Muslims (SUPKEM) and the Council of Imams and Preachers of Kenya (CIPK) provide centralized coordination for moon-sighting, education policy, and civic representation.\n4. Cooperative Welfare & Relief: Centralized Zakat trusts and relief initiatives channel humanitarian assistance from affluent urban centers to remote drought-stricken pastoralist regions, ensuring tangible economic brotherhood.",
        "diagram_title": "The Keystone Arch of Muslim Unity in Kenya",
        "svg_func": get_svg_lesson_2,
        "table_title": "Practical Pillars Enhancing Muslim Unity Across Kenya",
        "table_headers": ["Unifying Factor", "Religious & Institutional Mechanism", "Concrete Social Impact in Kenya"],
        "table_rows": [
            ["Shared Rituals", "5 Daily Prayers, Friday Jumu'ah, Ramadan & Eid", "Eliminates social stratification; unites worshippers in single rows"],
            ["Taqwa Standard", "Surah Al-Hujurat 49:13 and the Farewell Sermon", "Eradicates tribal superiority and fosters inter-ethnic respect"],
            ["Umbrella Leadership", "SUPKEM, CIPK, Jamia Mosque Committee", "Unifies dates of Eid, coordinates education and national advocacy"],
            ["Coordinated Relief", "Zakat distribution funds & disaster relief networks", "Delivers clean water, food aid & education bursaries to remote areas"]
        ],
        "scenario": "During an acute drought affecting northern pastoralist counties, a youth association from a Nairobi mosque takes decisive action. Rather than operating in isolation, they partner with a coastal relief trust and a local mobile Duksi school network in Garissa to establish the 'United Water Relief Caravan.' Nairobi youth raise 500,000 shillings in urban donations, coastal logistics teams supply water tankers, and local Garissa elders identify 500 vulnerable pastoralist households. This collaborative endeavor saves hundreds of families, demonstrating the power of unified institutional brotherhood.",
        "real_world": "Participate in a school-wide 'Ta'awun Service Project.' Team up with classmates from diverse ethnic and religious backgrounds to organize a campus environmental cleanup, a shared textbook-donation drive, or a revision circle for peers struggling with mathematics. Practical, cooperative service breaks down social divisions and builds enduring cohesion.",
        "reflection": "How does standing shoulder to shoulder in Friday Jumu'ah prayers serve as a powerful weekly lesson in human equality? How does coordinated Zakat distribution bridge economic inequality across Kenyan counties?",
        "misconception": "Misconception: Believing that tribal loyalty should dictate whom we assist. In authentic Islam, charity and solidarity are universal—commanded to help any human being in distress, regardless of their clan, ethnicity, or region.",
        "yt_id": "z9Qp8X7K2vY",
        "yt_title": "Strengthening Muslim Cohesion and Social Action in Kenya",
        "yt_desc": "Overview of umbrella bodies like SUPKEM, shared worship, and pooled humanitarian relief across Kenyan counties.",
        "mcq": {
            "question": "According to the Farewell Sermon of the Prophet Muhammad (PBUH) and Surah Al-Hujurat (49:13), what is the ONLY metric that determines honor and status in the sight of Allah?",
            "options": [
                "A. The extent of material wealth, land, and business enterprises owned.",
                "B. Ancestral lineage, royal blood, and prominent tribal clan affiliations.",
                "C. Taqwa (God-consciousness, piety, and moral righteousness).",
                "D. Fluency in multiple languages and political influence."
            ],
            "answer": "C",
            "explanation": "Both the Qur'an (49:13) and the Prophet's Farewell Sermon explicitly declare that worldly distinctions like wealth and tribe carry zero weight with Allah; only Taqwa (piety) determines true nobility."
        },
        "summary_content": "Muslim unity in Kenya is sustained by shared congregational worship, the divine standard of Taqwa over tribalism, representative umbrella organizations (SUPKEM, CIPK), and pooled socioeconomic welfare programs that channel humanitarian relief to vulnerable communities.",
        "key_points": [
            "Shared rituals (Salat, Ramadan, Hajj) dissolve artificial social hierarchies.",
            "Surah Al-Hujurat (49:13) establishes Taqwa as the sole measure of human worth.",
            "Umbrella bodies like SUPKEM provide a unified voice and institutional leadership.",
            "Pooled charity networks ensure wealth circulates to alleviate poverty across all counties."
        ],
        "exit_ticket": "Identify two practical factors that can unite Muslims from different counties of Kenya for community development."
    },
    {
        "unit_order": 3,
        "lesson_title": "Challenges that undermine Muslim unity in Kenya",
        "inquiry": "What are the key social and ideological challenges that threaten the unity of Muslims in Kenya, and how can we identify them?",
        "hook": "Imagine an elegant suspension footbridge spanning a deep river canyon, enabling villagers to cross safely to market, school, and clinics. From a distance, the bridge appears solid and stable. However, microscopic wood-boring termites have silently infested the primary timber support beams, eating away the structural core. If left untreated, the bridge will suddenly fracture and collapse under pressure. Social and ideological vices are the 'termites' that undermine our communal bridge of unity. To safeguard our society, we must learn to identify and eradicate these termites before catastrophe strikes.",
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/6/6d/Cracked_earth_in_drought.jpg/800px-Cracked_earth_in_drought.jpg",
        "image_title": "Fissures of Division",
        "image_caption": "Deep fissures in dry earth illustrating how sectarianism, tribalism, and gossip crack and fragment community cohesion.",
        "concept_name": "The Three Termites of Division & The Tabayyun Shield",
        "concept_explanation": "Communal cohesion in Kenya is threatened by three primary divisive vices: Sectarianism (Tawa'ifiyyah)—rigid, intolerant excommunication over secondary jurisprudence differences; Tribalism and Cultural Bias (Asabiyyah)—favoring one's ethnic clan over justice; and Unverified Digital Gossip—the irresponsible spread of rumors on social media without scriptural verification (Tabayyun).",
        "scripture_quran": "And obey Allah and His Messenger, and do not dispute, lest you lose courage and your strength depart; and be patient. Indeed, Allah is with the patient.",
        "scripture_quran_ref": "Surah Al-Anfal 8:46",
        "scripture_hadith": "Whoever calls to tribalism ('Asabiyyah) is not one of us; whoever fights for tribalism is not one of us; and whoever dies for tribalism is not one of us.",
        "scripture_hadith_ref": "Sunan Abu Dawood 5121",
        "deep_explanation": "Three structural vulnerabilities undermine unity in Kenya:\n1. The Menace of Sectarianism (Tawa'ifiyyah): Legitimate diversity in legal schools (Madhahib) is transformed by rigid partisans into mutual excommunication (Takfir), boycotting mosques, and refusing to pray behind scholars of differing legal interpretations.\n2. The Disease of Tribalism ('Asabiyyah): A remnant of pre-Islamic ignorance (Jahiliyyah) where mosque committees, school boards, or bursary funds are mismanaged to benefit specific clans rather than being distributed based on merit and integrity (Amanah).\n3. Digital Misinformation & Slander: The instant forwarding of unverified voice notes, sensational video clips, and slanderous claims in WhatsApp community groups spreads suspicion (Zann) and inflames communal passions, directly violating Surah Al-Hujurat (49:6).",
        "diagram_title": "Challenges to Muslim Unity: The Termites of Division",
        "svg_func": get_svg_lesson_3,
        "table_title": "Challenges Undermining Unity vs Islamic Countermeasures",
        "table_headers": ["Divisive Challenge", "Root Behavioral Cause", "Direct Harm to Society", "Prescribed Shariah Solution"],
        "table_rows": [
            ["Sectarianism (Tawa'ifiyyah)", "Rigid fanaticism over secondary Fiqh issues", "Splits mosques, fosters hatred & confuses youth", "Adab al-Ikhtilaf (etiquette of disagreement) & moderation"],
            ["Tribalism ('Asabiyyah)", "Blind ethnic favoritism and clan arrogance", "Corruption, nepotism in boards & excluded minorities", "Taqwa meritocracy & appointment based on Amanah"],
            ["Digital Gossip & Slander", "Sensationalism & forwarding without verification", "Slanders reputable leaders & breeds paranoia", "Tabayyun protocol (Quran 49:6: Verify all news)"],
            ["Political Rivalry", "Partisan manipulation during national elections", "Divides communities along political party lines", "Holding firmly to universal Islamic ethics above party politics"]
        ],
        "scenario": "A sensational voice note is shared in a school student chat group claiming that the local mosque management committee misappropriated charity funds to exclusively sponsor students from one specific clan. Several students become enraged and begin posting inflammatory insults against the Imam. Faruq intervenes: 'Classmates, let us halt immediately. We have zero evidence for this claim. Spreading rumors without verification destroys our communal peace and makes us lose moral strength, exactly as Allah warns in Surah Al-Anfal (8:46). Let us delete these defamatory messages and request our IRE teacher to verify the facts transparently.' The group calms down and removes the harmful posts.",
        "real_world": "Adopt the 'Seven-Day Zero-Gossip Digital Pledge.' If you receive a social media message, voice note, or meme that mocks another student, insults an Islamic scholar, or attacks a specific ethnic group, do not forward it. Delete it immediately and politely remind the sender: 'Spreading unverified rumors destroys our unity; let us verify before we share.' Protecting digital spaces is an act of Islamic worship.",
        "reflection": "Why does persistent internal fighting cause a community to 'lose courage and strength' as warned in Surah Al-Anfal (8:46)? How does tribalism in religious institutions directly violate the Islamic concept of justice (Adl)?",
        "misconception": "Misconception: Assuming that forwarding an unverified message with a disclaimer ('forwarded as received') clears the sender of guilt. In Islamic ethics, transmitting unverified rumors makes the sender an active accomplice in spreading falsehood.",
        "yt_id": "T0r3N_xY7dU",
        "yt_title": "The Dangers of Sectarianism and Tribalism in Modern Communities",
        "yt_desc": "Analysis of Surah Al-Anfal 8:46, the prohibition of 'Asabiyyah, and verifying information in the digital age.",
        "mcq": {
            "question": "Which of the following is defined in Islamic ethics as the rigid, uncompromising division of the community into hostile factions over secondary differences in religious interpretation?",
            "options": [
                "A. Tawheed (Monotheism)",
                "B. Sectarianism (Tawa'ifiyyah)",
                "C. Ta'awun (Mutual Cooperation)",
                "D. Islah (Reconciliation)"
            ],
            "answer": "B",
            "explanation": "Sectarianism (Tawa'ifiyyah) is the fanatical division of the community into hostile factions over secondary interpretations, directly contradicting the Quranic command to preserve unity."
        },
        "summary_content": "Sectarianism, tribalism ('Asabiyyah), and unverified digital rumors represent destructive 'termites' that weaken Muslim cohesion. Surah Al-Anfal (8:46) warns that disputing leads to loss of strength, mandating the application of the Tabayyun verification protocol to protect communal peace.",
        "key_points": [
            "Sectarianism turns secondary differences in Fiqh into destructive hostility.",
            "Tribalism ('Asabiyyah) is a pre-Islamic evil that corrupts institutional appointments.",
            "Unverified rumors and digital slander destroy social trust and community courage.",
            "Applying the Tabayyun protocol (Surah Al-Hujurat 49:6) stops the cycle of division."
        ],
        "exit_ticket": "List two negative effects of ethnic or tribal prejudice on a school student association."
    },
    {
        "unit_order": 4,
        "lesson_title": "Practising unity and building a harmonious society",
        "inquiry": "How can we actively practice unity and conflict resolution to build a cohesive and peaceful society in Kenya?",
        "hook": "Imagine being entrusted with a rare, delicate seed of a majestic fruit tree. If you seal that seed inside a glass jar on your study desk, it will remain dormant and never produce fruit. To reap its shade and sweet harvest, you must physically plant it in rich soil, water it daily, guard it against weeds, and protect it from pests. Practicing unity follows the identical law: it is not a passive sentiment. Unity requires intentional daily cultivation, active conflict resolution (Islaah), and righteous collaborative effort (Ta'awun).",
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/8/87/Students_in_classroom_Kenya.jpg/800px-Students_in_classroom_Kenya.jpg",
        "image_title": "Kenyan Students Cooperating in Learning",
        "image_caption": "Kenyan Junior School students working collaboratively in a diverse classroom, demonstrating the living practice of Islaah, Ta'awun, and social cohesion.",
        "concept_name": "The Four-Step Unity Cultivator Protocol (Islaah & Ta'awun)",
        "concept_explanation": "Practicing unity in daily life transforms Islamic theory into social reality through the 'Four-Step Unity Cultivator Protocol': Spreading sincere greeting (Salam), practicing active inclusion of marginalized peers, executing impartial conflict resolution (Islaah) as commanded in Surah Al-Hujurat (49:10), and collaborating on righteous community projects (Ta'awun) as commanded in Surah Al-Ma'idah (5:2).",
        "scripture_quran": "The believers are but brothers, so make peace between your brothers. And fear Allah that you may receive mercy.",
        "scripture_quran_ref": "Surah Al-Hujurat 49:10",
        "scripture_hadith": "Shall I not inform you of something better in degree than fasting, prayer, and charity? They said: 'Yes.' He said: 'Reconciling between people (Islaah dhat al-bayn)...'",
        "scripture_hadith_ref": "Sunan Abu Dawood 4919",
        "deep_explanation": "The operational blueprint for active peacebuilding encompasses four steps:\n1. Step 1: Sincere Greeting (Salam): The Prophet (PBUH) taught that spreading Salam dissolves social coldness and cultivates mutual affection. Offering a heartfelt greeting to all classmates removes cliquish barriers.\n2. Step 2: Active Inclusion: Welcoming quiet, economically disadvantaged, or minority peers into study groups and recreational games ensures no student is left vulnerable to loneliness.\n3. Step 3: Conflict Interception (Islaah): When disagreements occur, believers must not spectate or incite anger. They must intervene as fair mediators, hearing both sides without tribal bias, encouraging apologies, and restoring friendship.\n4. Step 4: Righteous Collaboration (Ta'awun): Uniting diverse students on constructive community service learning (CSL) projects—such as cleaning playgrounds, planting trees, and tutoring younger peers—builds shared national pride.",
        "diagram_title": "The Four-Step Unity Cultivator Protocol",
        "svg_func": get_svg_lesson_4,
        "table_title": "The Four Steps of Active Peacemaking in Daily School Life",
        "table_headers": ["Protocol Step", "Actionable Student Practice", "Target Outcome in School Environment"],
        "table_rows": [
            ["1. Sincere Salam", "Greeting peers with a smile and sincere prayer for peace", "Melts social tension and cultivates mutual affection"],
            ["2. Active Inclusion", "Inviting quiet or new students to lunch and sports", "Eliminates isolation and breaks exclusive tribal cliques"],
            ["3. Fair Islaah", "Impartially mediating disputes without favoritism (49:10)", "Restores brotherhood and halts destructive bullying"],
            ["4. Joint Ta'awun", "Partnering on school cleanups, tree-planting & tutoring", "Fosters collective accomplishment and national pride"]
        ],
        "scenario": "At Sabaki Junior School, the Grade 9 class prepares for their annual Community Service Learning (CSL) project. Two student groups engage in an intense dispute: one group demands cleaning the urban marketplace, while the other insists on planting seedlings at the public medical dispensary. The argument becomes bitter, with students threatening to boycott the project. Amina steps forward, applying the principles of Islaah: 'Colleagues, fighting over good deeds causes our entire class to fail. Let us harmonize our goals: we will dedicate Saturday morning to sanitizing the market, and Saturday afternoon to planting the clinic seedlings. This way, we accomplish both noble deeds as one united class.' The students shake hands and execute both projects with resounding success.",
        "real_world": "Establish a 'Unity and Service Team' with two peers from different cultural or religious backgrounds. Identify an urgent need in your school or neighborhood—such as repairing damaged classroom library books, picking up plastic litter, or assisting an elderly neighbor. Document your collaborative effort and present your experience during class assembly to inspire your peers.",
        "reflection": "Why did the Prophet (PBUH) declare that reconciling between people (Islaah) ranks higher in degree than supererogatory fasting and prayer? How does resolving a dispute between two peers protect the safety of the entire school?",
        "misconception": "Misconception: Assuming that making peace (Islaah) means siding with your friend even when they are in the wrong. In authentic Islamic jurisprudence, true loyalty requires helping a friend who is wrong by gently correcting them and upholding impartial justice.",
        "yt_id": "r1vJ9R2Q8Y0",
        "yt_title": "The Art of Islaah: Peacemaking and Mediation in Islam",
        "yt_desc": "Practical strategies for peer mediation, conflict resolution, and collaborative service based on Surah Al-Hujurat 49:10.",
        "mcq": {
            "question": "A heated dispute erupts between two classmates over a borrowed library textbook. Applying the direct command of Surah Al-Hujurat (49:10), what is the most responsible action for a Muslim student to take?",
            "options": [
                "A. Remain silent and watch the quarrel so as not to get involved in trouble.",
                "B. Automatically support the student who shares your ethnic background or neighborhood.",
                "C. Actively intervene as an impartial mediator, facilitate reconciliation (Islaah), and restore peace.",
                "D. Record the altercation on a smartphone to publish on social media."
            ],
            "answer": "C",
            "explanation": "Surah Al-Hujurat 49:10 commands believers that 'the believers are but brothers, so make peace (Islaah) between your brothers,' establishing conflict mediation as an obligatory communal duty."
        },
        "summary_content": "Practicing unity requires daily action through the Four-Step Protocol: spreading Salam, practicing active inclusion, mediating disputes with impartial fairness (Islaah), and collaborating on righteous community projects (Ta'awun) to establish a peaceful, flourishing society.",
        "key_points": [
            "Unity is an active discipline cultivated through daily practice, not a passive feeling.",
            "Surah Al-Hujurat (49:10) commands believers to actively mediate conflicts (Islaah).",
            "Reconciling between people ranks higher in degree than non-obligatory fasting and prayer.",
            "Righteous cooperation (Ta'awun) on community projects unites diverse youth in shared purpose."
        ],
        "exit_ticket": "Write down one concrete commitment you will fulfill this week to promote unity and resolve conflict in your classroom."
    }
]


# ─────────────────────────────────────────────────────────────────────────────
# INGESTION & AUDIT EXECUTION ENGINE
# ─────────────────────────────────────────────────────────────────────────────

@transaction.atomic
def ingest_topic_19():
    print("================================================================================")
    print("STARTING PRODUCTION INGESTION: GRADE 9 IRE — TOPIC 19")
    print("Topic: Unity of Muslims (Topic ID 359)")
    print("================================================================================")

    topic = Topic.objects.get(id=359)
    print(f"Target Topic: {topic.id} - {topic.name}")

    # Clean existing units for idempotent ingestion
    existing_units = LearningUnit.objects.filter(topic=topic)
    if existing_units.exists():
        print(f"Cleaning up {existing_units.count()} existing LearningUnits for clean idempotent ingestion...")
        existing_units.delete()

    created_units = 0
    created_lessons = 0
    created_blocks = 0
    created_assets = 0

    for ldata in TOPIC_19_LESSONS:
        order = ldata["unit_order"]
        title = ldata["lesson_title"]
        print(f"\nIngesting Lesson {order}/4: {title}...")

        # 1. Create LearningUnit
        unit = LearningUnit.objects.create(
            topic=topic,
            name=f"Lesson 7.2.{order}: {title}",
            order=order,
            description=clean_text(ldata["concept_explanation"][:250] + "...")
        )
        created_units += 1

        # 2. Create Published Lesson
        lesson = Lesson.objects.create(
            topic=topic,
            learning_unit=unit,
            title=clean_text(title),
            version=1,
            status="published"
        )
        created_lessons += 1

        # 3. Create Pedagogical Vector SVG Asset
        svg_xml = ldata["svg_func"]()
        try:
            ET.fromstring(svg_xml)
        except ET.ParseError as e:
            raise ValueError(f"Invalid SVG XML generated for Lesson {order}: {e}")

        diagram_asset = LessonAsset.objects.create(
            lesson=lesson,
            asset_type="image",
            title=ldata["diagram_title"],
            url="",
            metadata={
                "svg_xml": svg_xml,
                "svg_content": svg_xml,
                "format": "svg",
                "theme": "dark",
                "viewBox": "0 0 880 440"
            }
        )
        created_assets += 1

        # 4. Create Wikimedia Asset
        wiki_asset = LessonAsset.objects.create(
            lesson=lesson,
            asset_type="image",
            title=ldata["image_title"],
            url=ldata["image_url"],
            metadata={
                "caption": ldata["image_caption"],
                "source": "Wikimedia Commons"
            }
        )
        created_assets += 1

        # 5. Create Educational Video Asset
        video_asset = LessonAsset.objects.create(
            lesson=lesson,
            asset_type="video",
            title=ldata["yt_title"],
            url=f"https://www.youtube.com/watch?v={ldata['yt_id']}",
            metadata={
                "youtube_id": ldata["yt_id"],
                "description": ldata["yt_desc"]
            }
        )
        created_assets += 1

        # ─────────────────────────────────────────────────────────────────────
        # 7 ATOMIC CARDS (PAGES 1 TO 7)
        # ─────────────────────────────────────────────────────────────────────

        # CARD 1 (Page 1): Orientation & Hook
        b1_img = LessonBlock.objects.create(
            lesson=lesson,
            block_type="suggested_image",
            page_number=1,
            order=1,
            content={"caption": ldata["image_caption"], "title": ldata["image_title"], "url": ldata["image_url"]},
            metadata={"source": "Wikimedia Commons"}
        )
        b1_img.assets.add(wiki_asset)
        created_blocks += 1

        LessonBlock.objects.create(
            lesson=lesson,
            block_type="learning_goal",
            page_number=1,
            order=2,
            content={
                "inquiry_question": clean_text(ldata["inquiry"]),
                "hook": clean_text(ldata["hook"])
            },
            metadata={"focus": "orientation_and_connection"}
        )
        created_blocks += 1

        # CARD 2 (Page 2): Core Teaching & Scripture Panel
        LessonBlock.objects.create(
            lesson=lesson,
            block_type="concept_explanation",
            page_number=2,
            order=1,
            content={
                "concept_name": clean_text(ldata["concept_name"]),
                "text": clean_text(ldata["concept_explanation"])
            },
            metadata={"depth": "core_concept"}
        )
        created_blocks += 1

        LessonBlock.objects.create(
            lesson=lesson,
            block_type="callout",
            page_number=2,
            order=2,
            content={
                "title": "Scripture Evidence Panel",
                "quran_verse": clean_text(ldata["scripture_quran"]),
                "quran_reference": clean_text(ldata["scripture_quran_ref"]),
                "hadith_text": clean_text(ldata["scripture_hadith"]),
                "hadith_reference": clean_text(ldata["scripture_hadith_ref"])
            },
            metadata={"style": "scripture_panel"}
        )
        created_blocks += 1

        # CARD 3 (Page 3): Deep Explanation, Pedagogical Diagram & Comparison Table
        LessonBlock.objects.create(
            lesson=lesson,
            block_type="concept_explanation",
            page_number=3,
            order=1,
            content={
                "text": clean_text(ldata["deep_explanation"])
            },
            metadata={"depth": "elaborated_analysis"}
        )
        created_blocks += 1

        b3_diag = LessonBlock.objects.create(
            lesson=lesson,
            block_type="suggested_diagram",
            page_number=3,
            order=2,
            content={
                "title": ldata["diagram_title"],
                "svg_xml": svg_xml,
                "svg_content": svg_xml
            },
            metadata={"format": "svg", "viewBox": "0 0 880 440", "svg_content": svg_xml}
        )
        b3_diag.assets.add(diagram_asset)
        created_blocks += 1

        LessonBlock.objects.create(
            lesson=lesson,
            block_type="comparison_table",
            page_number=3,
            order=3,
            content={
                "title": ldata["table_title"],
                "headers": ldata["table_headers"],
                "rows": ldata["table_rows"]
            },
            metadata={"structure": "matrix"}
        )
        created_blocks += 1

        # CARD 4 (Page 4): Relatable Student Scenario
        LessonBlock.objects.create(
            lesson=lesson,
            block_type="worked_example",
            page_number=4,
            order=1,
            content={
                "title": "Relatable Student Scenario & Analysis",
                "scenario": clean_text(ldata["scenario"])
            },
            metadata={"context": "student_daily_life"}
        )
        created_blocks += 1

        # CARD 5 (Page 5): Real-World Application, Reflection & Video
        LessonBlock.objects.create(
            lesson=lesson,
            block_type="real_world_example",
            page_number=5,
            order=1,
            content={
                "application": clean_text(ldata["real_world"]),
                "reflection_prompts": clean_text(ldata["reflection"]),
                "misconception_check": clean_text(ldata["misconception"])
            },
            metadata={"focus": "authentic_application"}
        )
        created_blocks += 1

        b5_vid = LessonBlock.objects.create(
            lesson=lesson,
            block_type="suggested_video",
            page_number=5,
            order=2,
            content={
                "title": ldata["yt_title"],
                "youtube_id": ldata["yt_id"],
                "url": f"https://www.youtube.com/watch?v={ldata['yt_id']}",
                "description": ldata["yt_desc"]
            },
            metadata={"type": "educational_multimedia"}
        )
        b5_vid.assets.add(video_asset)
        created_blocks += 1

        # CARD 6 (Page 6): Verified Interactive MCQ
        mcq_data = ldata["mcq"]
        LessonBlock.objects.create(
            lesson=lesson,
            block_type="knowledge_check",
            page_number=6,
            order=1,
            content={
                "question": mcq_data["question"],
                "options": mcq_data["options"],
                "answer": mcq_data["answer"],
                "explanation": mcq_data["explanation"]
            },
            metadata={"assessment_type": "mcq"}
        )
        created_blocks += 1

        # CARD 7 (Page 7): Summary, Key Points & Exit Ticket
        LessonBlock.objects.create(
            lesson=lesson,
            block_type="summary",
            page_number=7,
            order=1,
            content={
                "summary": clean_text(ldata["summary_content"]),
                "key_points": [clean_text(kp) for kp in ldata["key_points"]],
                "exit_ticket": clean_text(ldata["exit_ticket"])
            },
            metadata={"review_type": "synthesis"}
        )
        created_blocks += 1

    print("\n================================================================================")
    print("INGESTION COMPLETE FOR TOPIC 19!")
    print(f"Created Units: {created_units}")
    print(f"Created Lessons: {created_lessons}")
    print(f"Created Blocks: {created_blocks}")
    print(f"Created Assets: {created_assets}")
    print("================================================================================")


if __name__ == "__main__":
    ingest_topic_19()
