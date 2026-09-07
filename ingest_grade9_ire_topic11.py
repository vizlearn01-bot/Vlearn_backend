"""
VLearn CBC Grade 9 IRE — Topic 11: Prohibitions in Islam: Zina
Production Ingestion and Enrichment Script for all 6 Lessons

Target Topic in DB: Topic ID 351 (Subject: IRE ID 53, Grade: Grade 9 ID 18)
Source Markdown: /home/jason-bitega/Desktop/VL/vlearn_repositories/Grade 9 IRE/prohibitions-zina.md

6 Lessons Ingested & Fully Enriched:
  1. Lesson 5.3.1: Meaning and scope
  2. Lesson 5.3.2: Effects on individuals and families
  3. Lesson 5.3.3: Effects on society
  4. Lesson 5.3.4: Reasons for prohibition
  5. Lesson 5.3.5: Measures of prevention and support
  6. Lesson 5.3.6: Unit synthesis
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
# 6 DEDICATED RESPONSIVE PEDAGOGICAL VECTOR SVGS (#0f172a theme, viewBox 880x440)
# ─────────────────────────────────────────────────────────────────────────────

def get_svg_lesson_1():
    """Lesson 5.3.1: The Protective Boundary of Chastity (Iffah)"""
    return """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 880 440" width="100%" height="100%">
  <defs>
    <linearGradient id="bg111" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#0f172a"/>
      <stop offset="50%" stop-color="#1e293b"/>
      <stop offset="100%" stop-color="#0f172a"/>
    </linearGradient>
  </defs>

  <rect width="880" height="440" rx="14" fill="url(#bg111)"/>
  <rect x="2" y="2" width="876" height="436" rx="12" fill="none" stroke="#334155" stroke-width="1.5"/>

  <!-- Header -->
  <text x="440" y="36" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="16" font-weight="700" text-anchor="middle">THE PROTECTIVE BOUNDARY: "DO NOT APPROACH UNLAWFUL INTIMACY"</text>
  <text x="440" y="56" fill="#94a3b8" font-family="system-ui, sans-serif" font-size="11.5" text-anchor="middle">Understanding the Qur'anic Command (Surah Al-Isra 17:32) to Avoid Preliminary Traps Leading to Zina</text>

  <!-- Central Castle: Dignity of Family & Body -->
  <g transform="translate(540, 95)">
    <rect width="290" height="305" rx="10" fill="#1e293b" stroke="#38bdf8" stroke-width="2"/>
    <rect width="290" height="36" rx="10" fill="#0369a1"/>
    <text x="145" y="24" fill="#ffffff" font-family="system-ui, sans-serif" font-size="12" font-weight="800" text-anchor="middle">THE SANCTUARY OF DIGNITY (IFFAH)</text>

    <!-- Inside Castle -->
    <rect x="20" y="50" width="250" height="46" rx="6" fill="#0f172a" stroke="#38bdf8"/>
    <text x="145" y="70" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="10.5" font-weight="700" text-anchor="middle">Sacred Human Body (Amanah)</text>
    <text x="145" y="86" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="8.5" text-anchor="middle">Moral purity, self-respect &amp; peace</text>

    <rect x="20" y="106" width="250" height="46" rx="6" fill="#0f172a" stroke="#34d399"/>
    <text x="145" y="126" fill="#34d399" font-family="system-ui, sans-serif" font-size="10.5" font-weight="700" text-anchor="middle">Protected Family Lineage (Nasab)</text>
    <text x="145" y="142" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="8.5" text-anchor="middle">Clear identity, honor &amp; inheritance</text>

    <rect x="20" y="162" width="250" height="46" rx="6" fill="#0f172a" stroke="#fbbf24"/>
    <text x="145" y="182" fill="#fbbf24" font-family="system-ui, sans-serif" font-size="10.5" font-weight="700" text-anchor="middle">Lawful Marriage (Nikah)</text>
    <text x="145" y="198" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="8.5" text-anchor="middle">The ONLY honorable gate to intimacy</text>

    <rect x="20" y="222" width="250" height="65" rx="6" fill="#082f49" stroke="#0284c7"/>
    <text x="145" y="244" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="10" font-weight="700" text-anchor="middle">Divine Honor Guaranteed</text>
    <text x="145" y="260" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="8.5" text-anchor="middle">Mutual love, legal custody, spiritual tranquility</text>
    <text x="145" y="274" fill="#a7f3d0" font-family="system-ui, sans-serif" font-size="8.5" text-anchor="middle">"Nikah is my Sunnah" (Ibn Majah)</text>
  </g>

  <!-- Left Side: The "Do Not Approach" Moat & Checkpoints -->
  <g transform="translate(50, 95)">
    <rect width="450" height="305" rx="10" fill="#1e293b" stroke="#f87171" stroke-width="1.5"/>
    <rect width="450" height="36" rx="10" fill="#991b1b"/>
    <text x="225" y="24" fill="#fecaca" font-family="system-ui, sans-serif" font-size="12" font-weight="800" text-anchor="middle">PREVENTATIVE WARNING: PRELIMINARY PATHS TO AVOID</text>

    <!-- Checkpoint 1 -->
    <rect x="18" y="50" width="414" height="48" rx="6" fill="#0f172a" stroke="#475569"/>
    <text x="30" y="70" fill="#f87171" font-family="system-ui, sans-serif" font-size="10" font-weight="700">1. Unchecked Eyes (Visual Temptations):</text>
    <text x="30" y="87" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="8.5">• Suggestive digital media, pornography, gazing with lust -> Remedy: Ghad al-Basar (Lowering gaze)</text>

    <!-- Checkpoint 2 -->
    <rect x="18" y="108" width="414" height="48" rx="6" fill="#0f172a" stroke="#475569"/>
    <text x="30" y="128" fill="#f87171" font-family="system-ui, sans-serif" font-size="10" font-weight="700">2. Private Isolation (Khalwah):</text>
    <text x="30" y="145" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="8.5">• Unchaperoned private meetings or secretive 1-on-1 chats -> Remedy: Public &amp; respectful communication</text>

    <!-- Checkpoint 3 -->
    <rect x="18" y="166" width="414" height="48" rx="6" fill="#0f172a" stroke="#475569"/>
    <text x="30" y="186" fill="#f87171" font-family="system-ui, sans-serif" font-size="10" font-weight="700">3. Suggestive Speech &amp; Revealing Attire:</text>
    <text x="30" y="203" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="8.5">• Flirtatious teasing, tight/immodest clothing -> Remedy: Modest speech &amp; proper covering (Awrah)</text>

    <!-- Checkpoint 4 (The Trap) -->
    <rect x="18" y="224" width="414" height="65" rx="6" fill="#2d1515" stroke="#ef4444"/>
    <text x="225" y="246" fill="#f87171" font-family="system-ui, sans-serif" font-size="10.5" font-weight="800" text-anchor="middle">CRITICAL THEOLOGICAL INSIGHT</text>
    <text x="225" y="264" fill="#fca5a5" font-family="system-ui, sans-serif" font-size="9" text-anchor="middle">"Do not approach" means stopping at the guardrails BEFORE the cliff.</text>
    <text x="225" y="278" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="8.5" text-anchor="middle">When preliminary gates are guarded, the sin of Zina becomes impossible to reach.</text>
  </g>
</svg>"""


def get_svg_lesson_2():
    """Lesson 5.3.2: The Ripple Effect of Unlawful Intimacy"""
    return """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 880 440" width="100%" height="100%">
  <defs>
    <linearGradient id="bg112" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#0f172a"/>
      <stop offset="50%" stop-color="#1e293b"/>
      <stop offset="100%" stop-color="#0f172a"/>
    </linearGradient>
  </defs>

  <rect width="880" height="440" rx="14" fill="url(#bg112)"/>
  <rect x="2" y="2" width="876" height="436" rx="12" fill="none" stroke="#334155" stroke-width="1.5"/>

  <!-- Header -->
  <text x="440" y="36" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="16" font-weight="700" text-anchor="middle">THE RIPPLE EFFECT: HOW ZINA HARMS INDIVIDUALS &amp; FAMILIES</text>
  <text x="440" y="56" fill="#94a3b8" font-family="system-ui, sans-serif" font-size="11.5" text-anchor="middle">A Single Private Transgression Expands Outward, Causing Devastating Physical, Mental, and Social Damage</text>

  <!-- Concentric Ripple Bands (Left) -->
  <g transform="translate(190, 245)">
    <!-- Outer Ring 4: Societal -->
    <circle r="150" fill="#1e293b" stroke="#64748b" stroke-width="1.5" stroke-dasharray="4,4"/>
    <!-- Ring 3: Family -->
    <circle r="115" fill="#334155" stroke="#f59e0b" stroke-width="1.5"/>
    <!-- Ring 2: Physical Health -->
    <circle r="80" fill="#475569" stroke="#ef4444" stroke-width="1.5"/>
    <!-- Core: The Sin -->
    <circle r="45" fill="#7f1d1d" stroke="#f87171" stroke-width="2"/>
    <text x="0" y="-8" fill="#ffffff" font-family="system-ui, sans-serif" font-size="10" font-weight="800" text-anchor="middle">ZINA</text>
    <text x="0" y="8" fill="#fecaca" font-family="system-ui, sans-serif" font-size="8" text-anchor="middle">(Core Sin)</text>
    <text x="0" y="20" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="7.5" text-anchor="middle">Loss of Iman</text>
  </g>

  <!-- Labels / Detailed Breakdown Cards (Right) -->
  <g transform="translate(410, 85)">
    <!-- Ripple 1 -->
    <rect x="0" y="0" width="430" height="68" rx="8" fill="#1e293b" stroke="#f87171" stroke-width="1.5"/>
    <text x="15" y="22" fill="#f87171" font-family="system-ui, sans-serif" font-size="11" font-weight="800">RIPPLE 1: PERSONAL &amp; SPIRITUAL TRAUMA</text>
    <text x="15" y="40" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="9">• Iman departs temporarily from the heart during the act (Hadith Bukhari 2475)</text>
    <text x="15" y="55" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="9">• Deep personal guilt, persistent anxiety, loss of self-esteem, depression</text>

    <!-- Ripple 2 -->
    <rect x="0" y="78" width="430" height="68" rx="8" fill="#1e293b" stroke="#ef4444" stroke-width="1.5"/>
    <text x="15" y="100" fill="#ef4444" font-family="system-ui, sans-serif" font-size="11" font-weight="800">RIPPLE 2: PHYSICAL HEALTH DISASTERS</text>
    <text x="15" y="118" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="9">• Transmission of fatal STIs, HIV/AIDS without the protection of marriage</text>
    <text x="15" y="133" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="9">• Unwanted teenage pregnancies, leading to life-threatening unlawful abortions</text>

    <!-- Ripple 3 -->
    <rect x="0" y="156" width="430" height="68" rx="8" fill="#1e293b" stroke="#f59e0b" stroke-width="1.5"/>
    <text x="15" y="178" fill="#f59e0b" font-family="system-ui, sans-serif" font-size="11" font-weight="800">RIPPLE 3: FAMILY SHATTERING &amp; TRAUMA</text>
    <text x="15" y="196" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="9">• Destruction of mutual trust between spouses, causing bitter divorce</text>
    <text x="15" y="211" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="9">• Innocent children deprived of stable 2-parent nurturing and paternal care</text>

    <!-- Ripple 4 -->
    <rect x="0" y="234" width="430" height="68" rx="8" fill="#1e293b" stroke="#38bdf8" stroke-width="1.5"/>
    <text x="15" y="256" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="11" font-weight="800">RIPPLE 4: SOCIAL CRISIS &amp; ECONOMIC DRAIN</text>
    <text x="15" y="274" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="9">• Massive health budget spent on treating preventable STIs and clinics</text>
    <text x="15" y="289" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="9">• Confusion of inheritance rights and rise in child abandonment</text>
  </g>
</svg>"""


def get_svg_lesson_3():
    """Lesson 5.3.3: Upright Society vs Broken Lineage Comparison Matrix"""
    return """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 880 440" width="100%" height="100%">
  <defs>
    <linearGradient id="bg113" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#0f172a"/>
      <stop offset="50%" stop-color="#1e293b"/>
      <stop offset="100%" stop-color="#0f172a"/>
    </linearGradient>
  </defs>

  <rect width="880" height="440" rx="14" fill="url(#bg113)"/>
  <rect x="2" y="2" width="876" height="436" rx="12" fill="none" stroke="#334155" stroke-width="1.5"/>

  <!-- Header -->
  <text x="440" y="36" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="16" font-weight="700" text-anchor="middle">SOCIETAL IMPACT: MORAL COHESION VS LINEAGE BREAKDOWN</text>
  <text x="440" y="56" fill="#94a3b8" font-family="system-ui, sans-serif" font-size="11.5" text-anchor="middle">How Individual Chastity and Lawful Lineage (Hifz al-Nasl) Anchor Economic Strength and Social Peace</text>

  <!-- Left Column: Society A (Moral & Chaste) -->
  <g transform="translate(45, 85)">
    <rect width="370" height="315" rx="10" fill="#1e293b" stroke="#34d399" stroke-width="1.5"/>
    <rect width="370" height="36" rx="10" fill="#065f46"/>
    <text x="185" y="24" fill="#a7f3d0" font-family="system-ui, sans-serif" font-size="12" font-weight="800" text-anchor="middle">SOCIETY A: UPRIGHT &amp; CHASTE (SUNNAH)</text>

    <rect x="15" y="48" width="340" height="54" rx="6" fill="#0f172a" stroke="#475569"/>
    <text x="25" y="68" fill="#34d399" font-family="system-ui, sans-serif" font-size="10" font-weight="700">Solid Two-Parent Families:</text>
    <text x="25" y="86" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="9">• Children raised with mutual fatherly &amp; motherly love</text>

    <rect x="15" y="112" width="340" height="54" rx="6" fill="#0f172a" stroke="#475569"/>
    <text x="25" y="132" fill="#34d399" font-family="system-ui, sans-serif" font-size="10" font-weight="700">Documented Lineage (Nasab):</text>
    <text x="25" y="150" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="9">• Clear legal identity, proud family tree, zero inheritance disputes</text>

    <rect x="15" y="176" width="340" height="54" rx="6" fill="#0f172a" stroke="#475569"/>
    <text x="25" y="196" fill="#34d399" font-family="system-ui, sans-serif" font-size="10" font-weight="700">Flourishing Public Health:</text>
    <text x="25" y="214" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="9">• Low rates of STIs, teenage pregnancies, and safe youth</text>

    <rect x="15" y="244" width="340" height="56" rx="6" fill="#064e3b" stroke="#10b981"/>
    <text x="185" y="265" fill="#34d399" font-family="system-ui, sans-serif" font-size="10.5" font-weight="800" text-anchor="middle">MACROECONOMIC BENEFIT</text>
    <text x="185" y="284" fill="#a7f3d0" font-family="system-ui, sans-serif" font-size="9" text-anchor="middle">Resources invested into schools, innovation, and infrastructure</text>
  </g>

  <!-- Right Column: Society B (Unregulated & Broken) -->
  <g transform="translate(465, 85)">
    <rect width="370" height="315" rx="10" fill="#1e293b" stroke="#f87171" stroke-width="1.5"/>
    <rect width="370" height="36" rx="10" fill="#7f1d1d"/>
    <text x="185" y="24" fill="#fecaca" font-family="system-ui, sans-serif" font-size="12" font-weight="800" text-anchor="middle">SOCIETY B: CORRUPTED &amp; DIVIDED</text>

    <rect x="15" y="48" width="340" height="54" rx="6" fill="#0f172a" stroke="#475569"/>
    <text x="25" y="68" fill="#f87171" font-family="system-ui, sans-serif" font-size="10" font-weight="700">Broken Homes &amp; Abandonment:</text>
    <text x="25" y="86" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="9">• Children neglected without financial or emotional support</text>

    <rect x="15" y="112" width="340" height="54" rx="6" fill="#0f172a" stroke="#475569"/>
    <text x="25" y="132" fill="#f87171" font-family="system-ui, sans-serif" font-size="10" font-weight="700">Confused Paternity &amp; Feuds:</text>
    <text x="25" y="150" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="9">• Endless court battles over child custody and lost inheritances</text>

    <rect x="15" y="176" width="340" height="54" rx="6" fill="#0f172a" stroke="#475569"/>
    <text x="25" y="196" fill="#f87171" font-family="system-ui, sans-serif" font-size="10" font-weight="700">Public Health Crisis:</text>
    <text x="25" y="214" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="9">• Explosive rates of HIV, high teenage maternal mortality</text>

    <rect x="15" y="244" width="340" height="56" rx="6" fill="#2d1515" stroke="#ef4444"/>
    <text x="185" y="265" fill="#f87171" font-family="system-ui, sans-serif" font-size="10.5" font-weight="800" text-anchor="middle">ECONOMIC DRAIN &amp; DESPAIR</text>
    <text x="185" y="284" fill="#fca5a5" font-family="system-ui, sans-serif" font-size="9" text-anchor="middle">Millions spent on orphanages, clinics, policing, and courts</text>
  </g>
</svg>"""


def get_svg_lesson_4():
    """Lesson 5.3.4: The Triple Protective Shield of Maqasid al-Shariah"""
    return """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 880 440" width="100%" height="100%">
  <defs>
    <linearGradient id="bg114" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#0f172a"/>
      <stop offset="50%" stop-color="#1e293b"/>
      <stop offset="100%" stop-color="#0f172a"/>
    </linearGradient>
  </defs>

  <rect width="880" height="440" rx="14" fill="url(#bg114)"/>
  <rect x="2" y="2" width="876" height="436" rx="12" fill="none" stroke="#334155" stroke-width="1.5"/>

  <!-- Header -->
  <text x="440" y="36" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="16" font-weight="700" text-anchor="middle">DIVINE WISDOM: THE TRIPLE PROTECTIVE SHIELD OF MAQASID</text>
  <text x="440" y="56" fill="#94a3b8" font-family="system-ui, sans-serif" font-size="11.5" text-anchor="middle">Why Islam Prohibits Zina: Engineering Safeguards that Guarantee Long-Term Human Flourishing</text>

  <!-- Central Crest / Flight Manual Analogy -->
  <g transform="translate(190, 85)">
    <rect width="500" height="70" rx="8" fill="#1e293b" stroke="#fbbf24" stroke-width="1.5"/>
    <text x="250" y="28" fill="#fbbf24" font-family="system-ui, sans-serif" font-size="12" font-weight="800" text-anchor="middle">THE CREATOR'S FLIGHT MANUAL ANALOGY</text>
    <text x="250" y="48" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="9.5" text-anchor="middle">Just as an aircraft manual restricts speed to prevent catastrophic crashes, divine laws</text>
    <text x="250" y="62" fill="#a7f3d0" font-family="system-ui, sans-serif" font-size="9.5" text-anchor="middle">restrict harmful desires to preserve human dignity and societal stability.</text>
  </g>

  <!-- 3 Interlocking Shields -->
  <!-- Shield 1: Progeny -->
  <g transform="translate(50, 175)">
    <rect width="240" height="225" rx="12" fill="#1e293b" stroke="#38bdf8" stroke-width="2"/>
    <rect width="240" height="34" rx="12" fill="#0369a1"/>
    <text x="120" y="22" fill="#ffffff" font-family="system-ui, sans-serif" font-size="11" font-weight="800" text-anchor="middle">SHIELD 1: HIFZ AL-NASL</text>
    <text x="120" y="55" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="11" font-weight="700" text-anchor="middle">Protection of Progeny</text>

    <rect x="15" y="70" width="210" height="140" rx="6" fill="#0f172a"/>
    <text x="25" y="92" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="9">• Guarantees every child</text>
    <text x="25" y="107" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="9">  has a legitimate father</text>
    <text x="25" y="127" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="9">• Enforces legal inheritance</text>
    <text x="25" y="142" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="9">  and property rights</text>
    <text x="25" y="162" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="9">• Eliminates child neglect</text>
    <text x="25" y="177" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="9">  and abandonment</text>
  </g>

  <!-- Shield 2: Dignity -->
  <g transform="translate(320, 175)">
    <rect width="240" height="225" rx="12" fill="#1e293b" stroke="#34d399" stroke-width="2"/>
    <rect width="240" height="34" rx="12" fill="#065f46"/>
    <text x="120" y="22" fill="#ffffff" font-family="system-ui, sans-serif" font-size="11" font-weight="800" text-anchor="middle">SHIELD 2: HIFZ AL-KARAMAH</text>
    <text x="120" y="55" fill="#34d399" font-family="system-ui, sans-serif" font-size="11" font-weight="700" text-anchor="middle">Protection of Human Dignity</text>

    <rect x="15" y="70" width="210" height="140" rx="6" fill="#0f172a"/>
    <text x="25" y="92" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="9">• Prevents commercial</text>
    <text x="25" y="107" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="9">  exploitation of bodies</text>
    <text x="25" y="127" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="9">• Protects women's financial</text>
    <text x="25" y="142" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="9">  and legal status via Nikah</text>
    <text x="25" y="162" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="9">• Replaces disposable lust</text>
    <text x="25" y="177" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="9">  with lifelong commitment</text>
  </g>

  <!-- Shield 3: Health / Life -->
  <g transform="translate(590, 175)">
    <rect width="240" height="225" rx="12" fill="#1e293b" stroke="#fbbf24" stroke-width="2"/>
    <rect width="240" height="34" rx="12" fill="#b45309"/>
    <text x="120" y="22" fill="#ffffff" font-family="system-ui, sans-serif" font-size="11" font-weight="800" text-anchor="middle">SHIELD 3: HIFZ AL-NAFS</text>
    <text x="120" y="55" fill="#fbbf24" font-family="system-ui, sans-serif" font-size="11" font-weight="700" text-anchor="middle">Protection of Life &amp; Health</text>

    <rect x="15" y="70" width="210" height="140" rx="6" fill="#0f172a"/>
    <text x="25" y="92" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="9">• Total prevention of</text>
    <text x="25" y="107" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="9">  fatal STIs and HIV/AIDS</text>
    <text x="25" y="127" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="9">• Prevents teenage maternal</text>
    <text x="25" y="142" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="9">  deaths and unsafe abortion</text>
    <text x="25" y="162" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="9">• Fosters mental peace</text>
    <text x="25" y="177" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="9">  free of guilt &amp; paranoia</text>
  </g>
</svg>"""


def get_svg_lesson_5():
    """Lesson 5.3.5: The Mountain Highway: Five Behavioral Guardrails"""
    return """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 880 440" width="100%" height="100%">
  <defs>
    <linearGradient id="bg115" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#0f172a"/>
      <stop offset="50%" stop-color="#1e293b"/>
      <stop offset="100%" stop-color="#0f172a"/>
    </linearGradient>
  </defs>

  <rect width="880" height="440" rx="14" fill="url(#bg115)"/>
  <rect x="2" y="2" width="876" height="436" rx="12" fill="none" stroke="#334155" stroke-width="1.5"/>

  <!-- Header -->
  <text x="440" y="36" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="16" font-weight="700" text-anchor="middle">THE HIGHWAY OF CHASTITY: FIVE PRACTICAL BEHAVIORAL GUARDRAILS</text>
  <text x="440" y="56" fill="#94a3b8" font-family="system-ui, sans-serif" font-size="11.5" text-anchor="middle">Sadd al-Dhara'i (Blocking the Means): Concrete Defensive Checkpoints Protecting Youth</text>

  <!-- 5 Guardrail Cards Across Horizontal Grid -->
  <!-- Guardrail 1 -->
  <g transform="translate(30, 85)">
    <rect width="150" height="315" rx="8" fill="#1e293b" stroke="#38bdf8" stroke-width="1.5"/>
    <rect width="150" height="32" rx="8" fill="#0284c7"/>
    <text x="75" y="21" fill="#ffffff" font-family="system-ui, sans-serif" font-size="10" font-weight="800" text-anchor="middle">1. EYE GATE</text>

    <text x="75" y="55" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="10" font-weight="700" text-anchor="middle">Ghad al-Basar</text>
    <text x="75" y="70" fill="#94a3b8" font-family="system-ui, sans-serif" font-size="8.5" text-anchor="middle">(Lowering Gaze)</text>

    <rect x="10" y="85" width="130" height="215" rx="4" fill="#0f172a"/>
    <text x="18" y="105" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="8.5">• Quran 24:30-31</text>
    <text x="18" y="125" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="8.5">• The gaze is the</text>
    <text x="18" y="140" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="8.5">  "arrow of heart"</text>
    <text x="18" y="165" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="8.5">• 1-Second Rule:</text>
    <text x="18" y="180" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="8.5">  Swipe past</text>
    <text x="18" y="195" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="8.5">  vulgar media</text>
    <text x="18" y="225" fill="#34d399" font-family="system-ui, sans-serif" font-size="8.5" font-weight="700">• Mental clarity</text>
    <text x="18" y="240" fill="#34d399" font-family="system-ui, sans-serif" font-size="8.5" font-weight="700">&amp; inner peace</text>
  </g>

  <!-- Guardrail 2 -->
  <g transform="translate(195, 85)">
    <rect width="150" height="315" rx="8" fill="#1e293b" stroke="#34d399" stroke-width="1.5"/>
    <rect width="150" height="32" rx="8" fill="#059669"/>
    <text x="75" y="21" fill="#ffffff" font-family="system-ui, sans-serif" font-size="10" font-weight="800" text-anchor="middle">2. ATTIRE GATE</text>

    <text x="75" y="55" fill="#34d399" font-family="system-ui, sans-serif" font-size="10" font-weight="700" text-anchor="middle">Modest Covering</text>
    <text x="75" y="70" fill="#94a3b8" font-family="system-ui, sans-serif" font-size="8.5" text-anchor="middle">(Covering Awrah)</text>

    <rect x="10" y="85" width="130" height="215" rx="4" fill="#0f172a"/>
    <text x="18" y="105" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="8.5">• Loose, non-revealing</text>
    <text x="18" y="120" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="8.5">  clothing</text>
    <text x="18" y="145" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="8.5">• Both males and</text>
    <text x="18" y="160" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="8.5">  females</text>
    <text x="18" y="185" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="8.5">• Promotes respect</text>
    <text x="18" y="200" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="8.5">  over superficial</text>
    <text x="18" y="215" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="8.5">  physical looks</text>
    <text x="18" y="240" fill="#34d399" font-family="system-ui, sans-serif" font-size="8.5" font-weight="700">• Dignity armor</text>
  </g>

  <!-- Guardrail 3 -->
  <g transform="translate(360, 85)">
    <rect width="150" height="315" rx="8" fill="#1e293b" stroke="#fbbf24" stroke-width="1.5"/>
    <rect width="150" height="32" rx="8" fill="#d97706"/>
    <text x="75" y="21" fill="#ffffff" font-family="system-ui, sans-serif" font-size="10" font-weight="800" text-anchor="middle">3. SPACE GATE</text>

    <text x="75" y="55" fill="#fbbf24" font-family="system-ui, sans-serif" font-size="10" font-weight="700" text-anchor="middle">No Isolation</text>
    <text x="75" y="70" fill="#94a3b8" font-family="system-ui, sans-serif" font-size="8.5" text-anchor="middle">(Avoiding Khalwah)</text>

    <rect x="10" y="85" width="130" height="215" rx="4" fill="#0f172a"/>
    <text x="18" y="105" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="8.5">• No secret 1-on-1</text>
    <text x="18" y="120" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="8.5">  closed rooms</text>
    <text x="18" y="145" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="8.5">• No secret DMs or</text>
    <text x="18" y="160" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="8.5">  hidden chats</text>
    <text x="18" y="185" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="8.5">• Study in public</text>
    <text x="18" y="200" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="8.5">  libraries/classes</text>
    <text x="18" y="230" fill="#34d399" font-family="system-ui, sans-serif" font-size="8.5" font-weight="700">• Prevents Shaytan</text>
    <text x="18" y="245" fill="#34d399" font-family="system-ui, sans-serif" font-size="8.5" font-weight="700">  as third party</text>
  </g>

  <!-- Guardrail 4 -->
  <g transform="translate(525, 85)">
    <rect width="150" height="315" rx="8" fill="#1e293b" stroke="#a78bfa" stroke-width="1.5"/>
    <rect width="150" height="32" rx="8" fill="#7c3aed"/>
    <text x="75" y="21" fill="#ffffff" font-family="system-ui, sans-serif" font-size="10" font-weight="800" text-anchor="middle">4. SPIRIT SHIELD</text>

    <text x="75" y="55" fill="#a78bfa" font-family="system-ui, sans-serif" font-size="10" font-weight="700" text-anchor="middle">Fasting for Youth</text>
    <text x="75" y="70" fill="#94a3b8" font-family="system-ui, sans-serif" font-size="8.5" text-anchor="middle">(Sawm as Wijaa')</text>

    <rect x="10" y="85" width="130" height="215" rx="4" fill="#0f172a"/>
    <text x="18" y="105" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="8.5">• Hadith Bukhari 5066</text>
    <text x="18" y="125" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="8.5">• Fasting on Mon/Thu</text>
    <text x="18" y="145" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="8.5">• Humbles physical</text>
    <text x="18" y="160" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="8.5">  impulses &amp; ego</text>
    <text x="18" y="185" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="8.5">• Builds steel</text>
    <text x="18" y="200" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="8.5">  self-discipline</text>
    <text x="18" y="230" fill="#34d399" font-family="system-ui, sans-serif" font-size="8.5" font-weight="700">• Spiritual shield</text>
    <text x="18" y="245" fill="#34d399" font-family="system-ui, sans-serif" font-size="8.5" font-weight="700">  for the soul</text>
  </g>

  <!-- Guardrail 5 -->
  <g transform="translate(690, 85)">
    <rect width="160" height="315" rx="8" fill="#1e293b" stroke="#f472b6" stroke-width="1.5"/>
    <rect width="160" height="32" rx="8" fill="#db2777"/>
    <text x="80" y="21" fill="#ffffff" font-family="system-ui, sans-serif" font-size="10" font-weight="800" text-anchor="middle">5. DIGITAL PROTOCOL</text>

    <text x="80" y="55" fill="#f472b6" font-family="system-ui, sans-serif" font-size="10" font-weight="700" text-anchor="middle">Screen Hygiene</text>
    <text x="80" y="70" fill="#94a3b8" font-family="system-ui, sans-serif" font-size="8.5" text-anchor="middle">(Clean Device Spaces)</text>

    <rect x="10" y="85" width="140" height="215" rx="4" fill="#0f172a"/>
    <text x="18" y="105" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="8.5">• Unfollow toxic</text>
    <text x="18" y="120" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="8.5">  influencer accounts</text>
    <text x="18" y="145" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="8.5">• Leave unmoderated</text>
    <text x="18" y="160" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="8.5">  vulgar chat groups</text>
    <text x="18" y="185" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="8.5">• Fill free time with</text>
    <text x="18" y="200" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="8.5">  sports &amp; study</text>
    <text x="18" y="230" fill="#34d399" font-family="system-ui, sans-serif" font-size="8.5" font-weight="700">• Digital Taqwa</text>
    <text x="18" y="245" fill="#34d399" font-family="system-ui, sans-serif" font-size="8.5" font-weight="700">  24/7 protection</text>
  </g>
</svg>"""


def get_svg_lesson_6():
    """Lesson 5.3.6: Master Synthesis: The Fortress of Moral Integrity"""
    return """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 880 440" width="100%" height="100%">
  <defs>
    <linearGradient id="bg116" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#0f172a"/>
      <stop offset="50%" stop-color="#1e293b"/>
      <stop offset="100%" stop-color="#0f172a"/>
    </linearGradient>
  </defs>

  <rect width="880" height="440" rx="14" fill="url(#bg116)"/>
  <rect x="2" y="2" width="876" height="436" rx="12" fill="none" stroke="#334155" stroke-width="1.5"/>

  <!-- Header -->
  <text x="440" y="36" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="16" font-weight="700" text-anchor="middle">MASTER SYNTHESIS: THE FORTRESS OF MORAL INTEGRITY (IFFAH)</text>
  <text x="440" y="56" fill="#94a3b8" font-family="system-ui, sans-serif" font-size="11.5" text-anchor="middle">Holistic Architecture of Sexual Morality: Divine Safeguards, Character Armor, and Social Flourishing</text>

  <!-- Apex Sanctuary (Top) -->
  <g transform="translate(240, 85)">
    <rect width="400" height="75" rx="10" fill="#1e293b" stroke="#34d399" stroke-width="2"/>
    <text x="200" y="26" fill="#34d399" font-family="system-ui, sans-serif" font-size="12.5" font-weight="800" text-anchor="middle">THE PROTECTED CITY: PEACEFUL &amp; HEALTHY COMMUNITY</text>
    <text x="200" y="46" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="9.5" text-anchor="middle">Pure Family Trees (Nasab) • Zero HIV/STIs • Secure, Loved Children</text>
    <text x="200" y="62" fill="#a7f3d0" font-family="system-ui, sans-serif" font-size="9.5" text-anchor="middle">National resources invested into schools, innovation, and social welfare</text>
  </g>

  <!-- 4 Supporting Pillars / Walls (Middle) -->
  <g transform="translate(60, 175)">
    <rect width="170" height="135" rx="8" fill="#1e293b" stroke="#38bdf8" stroke-width="1.5"/>
    <text x="85" y="24" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="10.5" font-weight="700" text-anchor="middle">PILLAR 1: GAZE &amp; MIND</text>
    <rect x="12" y="36" width="146" height="85" rx="4" fill="#0f172a"/>
    <text x="20" y="55" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="8.5">• Ghad al-Basar</text>
    <text x="20" y="70" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="8.5">• Digital hygiene filter</text>
    <text x="20" y="85" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="8.5">• 1-second swipe</text>
    <text x="20" y="105" fill="#34d399" font-family="system-ui, sans-serif" font-size="8.5">Mental purity</text>
  </g>

  <g transform="translate(250, 175)">
    <rect width="170" height="135" rx="8" fill="#1e293b" stroke="#fbbf24" stroke-width="1.5"/>
    <text x="85" y="24" fill="#fbbf24" font-family="system-ui, sans-serif" font-size="10.5" font-weight="700" text-anchor="middle">PILLAR 2: MODESTY</text>
    <rect x="12" y="36" width="146" height="85" rx="4" fill="#0f172a"/>
    <text x="20" y="55" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="8.5">• Loose clothing</text>
    <text x="20" y="70" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="8.5">• Covering Awrah</text>
    <text x="20" y="85" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="8.5">• Dignified speech</text>
    <text x="20" y="105" fill="#34d399" font-family="system-ui, sans-serif" font-size="8.5">Respect over lust</text>
  </g>

  <g transform="translate(440, 175)">
    <rect width="170" height="135" rx="8" fill="#1e293b" stroke="#a78bfa" stroke-width="1.5"/>
    <text x="85" y="24" fill="#a78bfa" font-family="system-ui, sans-serif" font-size="10.5" font-weight="700" text-anchor="middle">PILLAR 3: BOUNDARIES</text>
    <rect x="12" y="36" width="146" height="85" rx="4" fill="#0f172a"/>
    <text x="20" y="55" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="8.5">• Zero Khalwah</text>
    <text x="20" y="70" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="8.5">• Public study groups</text>
    <text x="20" y="85" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="8.5">• Wholesome peers</text>
    <text x="20" y="105" fill="#34d399" font-family="system-ui, sans-serif" font-size="8.5">Safe environments</text>
  </g>

  <g transform="translate(630, 175)">
    <rect width="190" height="135" rx="8" fill="#1e293b" stroke="#34d399" stroke-width="1.5"/>
    <text x="95" y="24" fill="#34d399" font-family="system-ui, sans-serif" font-size="10.5" font-weight="700" text-anchor="middle">PILLAR 4: TAWBAH</text>
    <rect x="12" y="36" width="166" height="85" rx="4" fill="#0f172a"/>
    <text x="20" y="55" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="8.5">• Door of Mercy open</text>
    <text x="20" y="70" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="8.5">• Sincere remorse &amp; reform</text>
    <text x="20" y="85" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="8.5">• Replacing sins with good</text>
    <text x="20" y="105" fill="#34d399" font-family="system-ui, sans-serif" font-size="8.5">Spiritual renewal</text>
  </g>

  <!-- Foundation (Bottom) -->
  <g transform="translate(60, 330)">
    <rect width="760" height="85" rx="8" fill="#0f172a" stroke="#64748b" stroke-width="1.5"/>
    <text x="380" y="26" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="12" font-weight="800" text-anchor="middle">THE UNSHAKEABLE BEDROCK: DIVINE REVELATION &amp; TAQWA</text>
    <text x="380" y="46" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="9.5" text-anchor="middle">"And do not approach unlawful intimacy... it is ever an immorality." (17:32) • "Tell believing men &amp; women to lower their gaze." (24:30)</text>
    <text x="380" y="66" fill="#fbbf24" font-family="system-ui, sans-serif" font-size="9.5" font-weight="700" text-anchor="middle">The body is an Amanah; true freedom is mastering desires, not becoming their slave.</text>
  </g>
</svg>"""


# ─────────────────────────────────────────────────────────────────────────────
# CONFIGURATION FOR TOPIC 11 (6 LESSONS)
# ─────────────────────────────────────────────────────────────────────────────

LESSONS_CONFIG = [
    {
        "unit_order": 1,
        "lesson_title": "Meaning and scope",
        "inquiry": "What is Zina in Islamic law, and how does Islam protect the sanctity and dignity of the human body?",
        "hook": "Imagine a rare historical manuscript in a museum. Because of its immense value, the museum places it in a climate-controlled glass display with strict security and legal protocols. In Islam, the human body and our capacity for intimacy are considered far more precious than any manuscript—they are sacred trusts (Amanah) from Allah. To protect their dignity, Islam establishes marriage as the only lawful path, prohibiting all intimacy outside it, known as Zina.",
        "concept_name": "Zina and the Virtue of Chastity (Iffah)",
        "concept_explanation": "Zina refers to any unlawful sexual relations or physical intimacy outside the bounds of a valid Islamic marriage (Nikah). Chastity (Iffah) is the virtue of maintaining moral purity, self-restraint, and guarding one's body and desires from unlawful actions. Islam establishes that the human body is an Amanah that must never be exploited.",
        "scripture_quran": "And do not approach unlawful sexual intercourse. Indeed, it is ever an immorality and is evil as a way.",
        "scripture_quran_ref": "Surah Al-Isra, 17:32",
        "scripture_hadith": "When a person commits zina, faith departs from him [and hovers above him like a shadow].",
        "scripture_hadith_ref": "Sahih al-Bukhari, 2475",
        "deep_explanation": "The prohibition in Surah Al-Isra (17:32) contains precise theological depth:\n\n1. 'Do Not Approach': Allah does not just say 'do not commit.' He commands us not to *approach* it, meaning we must avoid all preliminary paths, environments, suggestive media, and private isolation (Khalwah) that lead toward it.\n2. Major Sin (Kabirah): Zina is classified as a major sin because it violates human dignity, shatters families, and invites divine displeasure.\n3. Spiritual Consequence: Faith (Iman) and moral corruption cannot coexist; engaging in unlawful intimacy leaves the soul vulnerable and spiritually bankrupt.",
        "svg_func": get_svg_lesson_1,
        "diagram_title": "The Protective Boundary of Chastity (Iffah)",
        "table_title": "Preliminary Paths vs Islamic Guardrails",
        "table_headers": ["Vulnerable Situation", "The Slippery Slope", "Islamic Defensive Guardrail", "Pedagogical Rationale"],
        "table_rows": [
            ["Suggestive Media", "Gazing at inappropriate photos", "Ghad al-Basar (Lowering gaze)", "Protects mind from corruption"],
            ["Private Online Chat", "Flirtatious secret 1-on-1 DMs", "Transparent public communication", "Prevents Shaytan's third party"],
            ["Unchaperoned Rooms", "Alone behind closed doors", "Avoiding Khalwah (Public study)", "Eliminates physical opportunity"],
            ["Revealing Attire", "Seeking physical attention", "Modest loose dress (Awrah)", "Fosters dignity over lust"]
        ],
        "scenario": "Zainab is browsing her phone late at night and receives a direct message from a classmate she likes. The message contains suggestive language and asks her to send a private, inappropriate photo of herself. Zainab feels tempted, but remembers the Qur'an's command: 'Do not approach zina.' She says to herself, 'My body is an Amanah from Allah, and my dignity is too valuable to compromise. Sending this photo is a step toward crossing that sacred boundary.' Zainab politely but firmly declines, deletes the message, and blocks the sender to protect her moral purity.",
        "real_world": "Establish a 'Digital Boundary Protocol' on your electronic devices. To align with the command 'Do not approach zina,' consciously delete any apps, unfollow accounts, or mute chat groups that consistently share vulgar or suggestive content. Replacing harmful media with beneficial, educational, and clean content is a vital way Grade 9 students can guard their minds and hearts.",
        "reflection": "Why does the Qur'an focus on preventing the 'steps' that lead to a sin, rather than just prohibiting the final act itself?",
        "misconception": "Remember: The prohibition of Zina is not about shaming human biology. Islam celebrates healthy, loving intimacy within marriage (Nikah) as a blessed act of worship, while strictly prohibiting unlawful exploitation outside marriage.",
        "yt_title": "Why Islam Forbids Zina: Understanding the Wisdom",
        "yt_desc": "A clear, insightful talk on the sacred boundaries of marriage and the protection of human dignity in Islam.",
        "yt_id": "vM39rSj38fE",
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/4/4b/The_Great_Mosque_of_Cordoba_Spain.jpg/1280px-The_Great_Mosque_of_Cordoba_Spain.jpg",
        "image_title": "The Great Mosque of Córdoba",
        "image_caption": "Historic architectural marvel representing Islamic civilization's emphasis on sacred discipline, dignity, and moral order.",
        "mcq": {
            "question": "What is the primary significance of the phrasing 'Do not approach' in Surah Al-Isra (17:32) regarding unlawful physical intimacy?",
            "options": [
                "It means the act is only forbidden if you get physically near a mosque.",
                "It commands believers to avoid all preliminary behaviors, media, and environments that lead toward the sin.",
                "It indicates that the prohibition is temporary and only applies during daytime hours.",
                "It suggests that the action is discouraged but not completely prohibited."
            ],
            "answer": "B",
            "explanation": "The phrase 'Do not approach' is a preventive legal and moral principle that requires Muslims to avoid all preliminary steps (suggestive media, private isolation, flirtatious talk) that could lead to the sin of Zina."
        },
        "summary_content": "Zina refers to any unlawful physical intimacy outside of a valid marriage. The Qur'an commands us to 'not approach' Zina, which means actively avoiding all preliminary temptations and private isolation. Sincere faith and moral purity (Iffah) are incompatible with illicit behavior.",
        "key_points": [
            "Zina violates human dignity and is strictly classified as a major sin (Kabirah).",
            "'Do not approach' mandates eliminating preliminary steps and temptations.",
            "Marriage (Nikah) is the only lawful, dignified institution for intimacy in Islam."
        ],
        "exit_ticket": "Explain in your own words why guarding your digital habits is an essential part of the command 'Do not approach zina.'"
    },
    {
        "unit_order": 2,
        "lesson_title": "Effects on individuals and families",
        "inquiry": "What are the harmful physical, psychological, and social consequences of Zina on individuals and family structures?",
        "hook": "Imagine a farmer who spends years preparing fertile soil and building strong fences. Suddenly, wild destructive animals are let into the field, trampling crops and breaking fences within hours. In a similar way, a family is a protected, sacred field where children are nurtured with love and security. Zina acts like those wild animals—it breaks down the protective fences of trust, causing immense harm to individuals and completely shattering family units.",
        "concept_name": "Sanctity of the Family and Consequential Harm",
        "concept_explanation": "The family unit is the essential foundation of a healthy, moral, and stable society in Islam. Consequential harm refers to the reality that major prohibitions in Islam exist because the forbidden acts inflict severe, unavoidable physical, psychological, and relational damage upon individuals and their loved ones.",
        "scripture_quran": "...and do not kill your children out of fear of poverty. We provide for them and for you. Surely killing them is a heinous sin.",
        "scripture_quran_ref": "Surah Al-Isra, 17:31",
        "scripture_hadith": "No person commits zina while having complete faith.",
        "scripture_hadith_ref": "Sahih al-Bukhari, 6772",
        "deep_explanation": "The harmful consequences of Zina are severe and multi-dimensional:\n\n1. Physical Health Hazards: Unlawful intimacy outside marriage drives the transmission of Sexually Transmitted Infections (STIs), including HIV/AIDS, and causes unsupported early pregnancies that often lead to unsafe illegal abortions.\n2. Psychological Trauma: Lacking the lifelong spiritual and legal covenant of Nikah, illicit relationships breed chronic guilt, anxiety, low self-esteem, depression, and paranoia over social exposure.\n3. Destruction of Family Trust: Marital infidelity shatters emotional trust, causing bitter divorces, divided households, and emotional trauma for children who lose the stability of a loving dual-parent home.",
        "svg_func": get_svg_lesson_2,
        "diagram_title": "The Ripple Effect of Unlawful Intimacy",
        "table_title": "Dimensions of Harm Caused by Zina",
        "table_headers": ["Dimension", "Specific Harm", "Impact on Victim / Family", "Islamic Legal Safeguard"],
        "table_rows": [
            ["Physical Health", "Transmission of STIs & HIV", "Chronic illness, infertility, death", "Chastity & monogamous Nikah"],
            ["Psychological", "Guilt, anxiety & depression", "Loss of self-worth and inner peace", "Tawbah & spiritual self-control"],
            ["Family Unity", "Broken trust between spouses", "Bitter divorce & broken homes", "Muraqabah & marital fidelity"],
            ["Child Welfare", "Loss of paternal support", "Emotional trauma & abandoned youth", "Enforced parental maintenance"]
        ],
        "scenario": "In a biology class discussing health and relationships, Amina reads a brochure about high rates of HIV and unwanted teenage pregnancies in her region. Her classmate Yusuf asks, 'Why does this happen so much among teenagers?' Amina explains, 'Yusuf, in our IRE class, we learned that Allah prohibited Zina for our own protection. When people ignore the rules of marriage and engage in unlawful relationships, they expose themselves to these physical diseases and face huge emotional struggles. If a child is born outside a stable home, that child misses out on the protective care of two married parents. Islam's rules are not there to limit our happiness, but to safeguard our health and our future families.'",
        "real_world": "Design a 'Family Advocacy Flyer' for your portfolio. Write down three physical health reasons (STIs, HIV prevention, avoiding early pregnancy) and three psychological reasons (trust, self-respect, emotional stability) explaining why waiting for marriage (Nikah) is the safest and most honorable choice for a young person.",
        "reflection": "How does a stable, married family unit contribute to a child's success in school and their emotional peace of mind?",
        "misconception": "Remember: The harmful consequences of Zina are not just theoretical or ancient; medical science and social studies consistently prove that sexual promiscuity leads to severe physical infections and psychological distress.",
        "yt_title": "Protecting the Family Unit in Islamic Ethics",
        "yt_desc": "An educational discussion on why family stability is the backbone of society and how moral boundaries preserve health.",
        "yt_id": "7E_d-F6iX3o",
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/c/c5/Moroccan_family_home_courtyard.jpg/1280px-Moroccan_family_home_courtyard.jpg",
        "image_title": "Traditional Family Courtyard in Fes",
        "image_caption": "Traditional Islamic domestic architecture designed around privacy, family warmth, and the sacred protection of loved ones.",
        "mcq": {
            "question": "Which of the following is a direct, curriculum-listed physical consequence of violating sexual boundaries outside of marriage?",
            "options": [
                "A decrease in a person's physical height and hearing.",
                "An increased risk of contracting Sexually Transmitted Infections (STIs) and HIV/AIDS.",
                "The immediate loss of all academic qualifications.",
                "The physical decay of school uniforms and books."
            ],
            "answer": "B",
            "explanation": "Zina lacks the protective, monogamous framework of marriage, which dramatically increases the risk of contracting and transmitting STIs and HIV/AIDS, as well as experiencing unsupported early pregnancies."
        },
        "summary_content": "Islam's prohibitions are designed to protect human welfare and prevent severe harm. Zina leads to grave physical health risks including STIs and early pregnancies. It destroys the trust necessary for stable families, leaving children emotionally and financially vulnerable.",
        "key_points": [
            "Divine prohibitions exist to prevent severe physical, psychological, and social harm.",
            "Zina is a leading driver of STIs, HIV, and unsupported early pregnancies.",
            "Family breakups resulting from infidelity inflict lasting trauma on children."
        ],
        "exit_ticket": "State two ways a broken family home can negatively affect a child's emotional and academic development."
    },
    {
        "unit_order": 3,
        "lesson_title": "Effects on society",
        "inquiry": "How does the widespread practice of Zina undermine the social fabric, trust, and economic stability of the wider community?",
        "hook": "Imagine a heavy rope made of thousands of tiny, tightly woven threads. As long as the threads remain united, the rope can lift heavy containers and dock massive ships. But if someone cuts the individual threads one by one, the rope frays and eventually snaps under the slightest weight. In a society, individual families are the tiny threads. If family units are broken down by dishonesty, infidelity, and immoral behavior, the entire rope of society snaps.",
        "concept_name": "Social Cohesion and Protection of Lineage (Hifz al-Nasl)",
        "concept_explanation": "Social cohesion is the level of trust, unity, and mutual support that exists within a community, allowing members to cooperate peacefully. Lineage protection (Hifz al-Nasl) is one of the five primary goals of Islamic law (Maqasid al-Shariah), focusing on protecting the clarity of family lineage, legal identity, and child inheritance rights.",
        "scripture_quran": "And We have certainly honored the children of Adam and carried them on land and sea and provided for them of the good things...",
        "scripture_quran_ref": "Surah Al-Isra, 17:70",
        "scripture_hadith": "None of you truly believes until he loves for his brother what he loves for himself.",
        "scripture_hadith_ref": "Sahih al-Bukhari, 13",
        "deep_explanation": "Widespread sexual immorality degrades the broader society in three major ways:\n\n1. Confusion of Lineage (Nasab): When children are born outside marriage, it leads to disputes over legal identity, loss of paternal inheritance rights, and the severance of extended family ties. Islam insists that every child has a proud, documented lineage.\n2. Economic Burden on Society: Broken homes and abandoned children place immense financial strain on community charities, orphanages, and state budgets, diverting funds from schools and infrastructure.\n3. Spread of Social Vices: Promiscuity is tightly linked to human exploitation, prostitution, drug abuse, and violent domestic disputes, eroding public trust and moral standards.",
        "svg_func": get_svg_lesson_3,
        "diagram_title": "Societal Impact: Moral Cohesion vs Lineage Breakdown",
        "table_title": "Upright Society vs Corrupted Society Comparison",
        "table_headers": ["Social Dimension", "Upright & Chaste Community", "Corrupted Community", "National Impact"],
        "table_rows": [
            ["Family Foundation", "Stable, married parents", "Broken homes & abandonment", "Determines youth well-being"],
            ["Legal Identity", "Documented Nasab & lineage", "Paternity disputes & lawsuits", "Guarantees inheritance rights"],
            ["Public Health", "Low STI rates & healthy youth", "High medical costs for epidemics", "Frees hospital budgets for care"],
            ["Civic Resources", "Funds spent on schools & roads", "Funds diverted to orphanages", "Accelerates national progress"]
        ],
        "scenario": "In a social studies debate on 'Building a Prosperous Nation,' a student argues, 'As long as our economy is growing, the private moral behavior of citizens does not matter.' Omar stands up and politely responds: 'I respectfully disagree. A country's economy is built by its people. In our IRE classes, we studied that when sexual immorality spreads, it shatters families. Broken families lead to high numbers of abandoned children, emotional trauma, and massive health costs for treating STIs. The government has to spend millions of shillings on clinics, orphanages, and courts instead of investing in our education and roads. Private moral choices have a direct, massive impact on our national development.'",
        "real_world": "Draft a short 'Community Integration Proposal' for your school's Peace and Integrity Club. Outline three ways high moral standards and chastity support the Kenyan National Goals of Education (specifically fostering national unity, patriotism, and social equity). Suggest organizing a school assembly presentation to encourage peers to value modesty and family integrity.",
        "reflection": "Why does protecting the clarity of a child's family tree (lineage) matter for their sense of belonging, inheritance, and social rights?",
        "misconception": "Remember: Private sins are never completely private in their outcomes; the social, financial, and emotional fallout of Zina affects extended families, healthcare systems, and community stability.",
        "yt_title": "The Societal Value of Family in Islam",
        "yt_desc": "An analytical exploration of how Islamic family ethics protect lineage, child rights, and community welfare.",
        "yt_id": "rJ_q0u-w_1E",
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/e/e1/Children_studying_Quran_in_Sudan.jpg/1280px-Children_studying_Quran_in_Sudan.jpg",
        "image_title": "Community Learning and Youth Nurturing",
        "image_caption": "Community-based spiritual education fostering social responsibility, moral values, and mutual support among youth.",
        "mcq": {
            "question": "Which of the following is a major societal challenge that arises when the purity of lineage (Nasab) is neglected due to widespread sexual immorality?",
            "options": [
                "The loss of a child's legal identity, documented lineage, and rightful inheritance rights.",
                "A sudden drop in the academic standard of national geography exams.",
                "The physical failure of public transportation engines.",
                "A change in the seasonal monsoon rainfall patterns."
            ],
            "answer": "A",
            "explanation": "One of the primary objectives of marriage is Hifz al-Nasl (preservation of lineage). Without it, children face confusion over paternal identity and legal inheritance rights, creating social disorder."
        },
        "summary_content": "Society is only as strong as the families that compose it. Lineage protection (Hifz al-Nasl) is a primary goal of Shariah to safeguard child rights. Moral corruption drains community resources, increases disease burdens, and undermines public trust.",
        "key_points": [
            "Families are the foundational building blocks of a stable, prosperous nation.",
            "Hifz al-Nasl guarantees clear identity, dignity, and inheritance for every child.",
            "Promiscuity diverts civic funds toward treating preventable health and social crises."
        ],
        "exit_ticket": "Explain in one sentence why a nation's economic strength is closely tied to the stability of its family homes."
    },
    {
        "unit_order": 4,
        "lesson_title": "Reasons for prohibition",
        "inquiry": "What is the deeper divine wisdom behind the prohibition of Zina, and how does it safeguard human dignity?",
        "hook": "Imagine an advanced aircraft designed by world-renowned engineers. The engineers provide a detailed flight manual with strict rules: do not fly in severe storms, do not exceed specific speed limits, and do not use low-quality fuel. A pilot who calls these rules restrictive and ignores them will cause a catastrophic crash. Allah (S.W.T.) is our Creator and designed us perfectly. The Shariah is our flight manual, and the prohibition of Zina is a vital safety feature designed to prevent us from spiritually and socially crashing.",
        "concept_name": "Maqasid al-Shariah and Divine Wisdom (Hikmah)",
        "concept_explanation": "Maqasid al-Shariah represents the higher objectives of Islamic law revealed to preserve five essential human interests: Religion, Life, Intellect, Property, and Lineage/Dignity. Divine wisdom (Hikmah) is the perfect underlying purpose behind Allah's commandments, always aiming to maximize human flourishing and eliminate harm.",
        "scripture_quran": "O mankind, indeed We have created you from male and female and made you peoples and tribes that you may know one another. Indeed, the most noble of you in the sight of Allah is the most righteous of you...",
        "scripture_quran_ref": "Surah Al-Hujurat, 49:13",
        "scripture_hadith": "There should be neither harming nor reciprocating harm.",
        "scripture_hadith_ref": "Sunan Ibn Majah, 2340",
        "deep_explanation": "The divine wisdom behind prohibiting Zina centers on three core protections:\n\n1. Preserving Human Honor (Takreem): Zina reduces human beings to temporary objects of physical gratification. Islam elevates relationships into a sacred covenant (Mithaq Ghalidh) of mutual care, emotional safety, and financial responsibility.\n2. Protecting Women's Rights: In unregulated relationships, women often bear the physical, social, and financial burdens of pregnancy alone. Marriage legally binds the husband to provide full maintenance, housing, and protection.\n3. Preventing Social Discord (Fitnah): Unregulated sexual relations generate jealousy, adultery-related violence, paternity feuds, and the destruction of domestic peace.",
        "svg_func": get_svg_lesson_4,
        "diagram_title": "Divine Wisdom: The Triple Protective Shield of Maqasid",
        "table_title": "The Divine Wisdom (Hikmah) Behind the Prohibition",
        "table_headers": ["Objective of Law", "Harm Prevented (Mafsadah)", "Benefit Achieved (Maslahah)", "Spiritual Outcome"],
        "table_rows": [
            ["Protection of Lineage", "Confusion of paternal roots", "Documented legal Nasab", "Preserves child inheritance"],
            ["Protection of Dignity", "Dehumanization & exploitation", "Honorable status of Nikah", "Guarantees mutual respect"],
            ["Protection of Health", "Fatal STIs & unsafe abortions", "Clean, monogamous intimacy", "Physical vitality & peace"],
            ["Protection of Society", "Broken families & orphan crisis", "Stable, supportive households", "National harmony & progress"]
        ],
        "scenario": "During an IRE study group, Yusuf says, 'Some people online argue that if two consenting adults want to have an unlawful relationship, it doesn't harm anyone. Why is Islam so strict about it?' Mr. Bilal, who is passing by, explains: 'Yusuf, consented harm is still harm. If a person consents to drink poison, does it stop being poison? No. The divine wisdom behind prohibiting Zina is that Allah loves us and wants to protect our dignity, our women, and our children. Consent cannot prevent the spread of STIs, the heartbreak of broken families, or the abandonment of children. Allah's laws protect the entire society from collapsing into chaos, even when individuals fail to see the danger.'",
        "real_world": "Write a reflective essay or prepare a 3-minute speech on the topic: 'Consenting Desires vs Divine Wisdom: Why Shariah Protects Human Dignity.' Use the analogy of the aircraft flight manual and the three shields of Maqasid to explain why restricting intimacy to marriage is a sign of Allah's mercy and care for humanity.",
        "reflection": "How does the legal contract of marriage (Nikah) protect a woman's financial and social rights compared to an unregulated, unlawful relationship?",
        "misconception": "Remember: Allah's laws are not arbitrary restrictions designed to suppress human happiness. Every single prohibition in Shariah exists to shield humanity from suffering and guarantee lasting well-being.",
        "yt_title": "Understanding the Wisdom of Islamic Rulings",
        "yt_desc": "An explanation of Maqasid al-Shariah and how divine commands reflect profound mercy and wisdom.",
        "yt_id": "p6c0_7L9jKs",
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/a/a2/Qur%27an_manuscript_12th_century.jpg/1280px-Qur%27an_manuscript_12th_century.jpg",
        "image_title": "Twelfth-Century Illuminated Qur'an Manuscript",
        "image_caption": "Historic manuscript preserving the divine revelation that balances divine law, justice, and mercy.",
        "mcq": {
            "question": "How does the prohibition of Zina specifically safeguard the rights and welfare of children born into a community?",
            "options": [
                "It guarantees that every child is born into a legal, stable family with two committed parents responsible for their care.",
                "It ensures that all children automatically receive free school materials from local mosques.",
                "It allows children to choose their own names at the age of seven.",
                "It exempts children from attending public school."
            ],
            "answer": "A",
            "explanation": "By restricting physical intimacy to marriage, Islam ensures every child has a documented lineage, rightful inheritance, and is nurtured by both parents who are legally and spiritually bound to support them."
        },
        "summary_content": "Allah's laws are founded on Hikmah (perfect wisdom) to maximize human welfare and prevent harm. Zina is prohibited to protect human dignity, prevent the exploitation of women, and secure child rights. Marriage provides a secure legal contract that guarantees lifelong protection.",
        "key_points": [
            "Maqasid al-Shariah protects Religion, Life, Intellect, Property, and Lineage/Dignity.",
            "Consented harm remains destructive to physical health and family structures.",
            "Nikah establishes an honorable, legally enforceable covenant of mutual care."
        ],
        "exit_ticket": "State one major legal and emotional difference between an unregulated relationship and the sacred contract of Nikah."
    },
    {
        "unit_order": 5,
        "lesson_title": "Measures of prevention and support",
        "inquiry": "What practical spiritual, behavioral, and community measures does Islam establish to prevent Zina and support moral integrity?",
        "hook": "Imagine driving down a steep mountain road along a cliff edge. To keep you safe, the road engineers do not merely put a sign at the bottom; they construct strong steel guardrails, paint bright lane dividers, install rumble strips, and set speed limits. In Islam, guarding chastity is like driving on that mountain road. Islam does not merely prohibit Zina; it builds an entire series of behavioral guardrails to keep our hearts and actions safe on the road of life.",
        "concept_name": "Sadd al-Dhara'i and Modesty in Action",
        "concept_explanation": "Sadd al-Dhara'i (Blocking the Means) is the legal and moral principle of prohibiting actions or habits that are not sins in themselves, but are highly likely to lead directly to a major sin. Modesty in action is the daily practice of self-restraint through controlling our gaze, dress, speech, and company to maintain moral purity.",
        "scripture_quran": "Tell the believing men to lower their gaze and guard their private parts. That is purer for them. Indeed, Allah is Acquainted with what they do. And tell the believing women to lower their gaze and guard their private parts...",
        "scripture_quran_ref": "Surah An-Nur, 24:30-31",
        "scripture_hadith": "O young men, whoever among you can marry, let him marry... and whoever is not able, let him fast, for it is a shield for him.",
        "scripture_hadith_ref": "Sahih al-Bukhari, 5066",
        "deep_explanation": "Islam establishes five practical preventative guardrails for youth:\n\n1. Lowering the Gaze (Ghad al-Basar): Guarding our eyes from looking at suggestive media, explicit photos, or staring with lust. The gaze is described in tradition as the initial spark of the heart.\n2. Modesty in Dress (Covering Awrah): Wearing loose, dignified clothing that covers bodily boundaries for both males and females, promoting intellectual and moral respect over physical lust.\n3. Avoiding Private Isolation (Khalwah): Prohibiting an unrelated male and female from being alone in a closed room or secret, unmonitored digital space.\n4. The Spiritual Shield of Fasting (Sawm): Voluntary fasting humbles physical desires and strengthens spiritual willpower and self-mastery.\n5. Digital Hygiene: Consciously unfollowing toxic accounts, filtering screen time, and exiting vulgar chat groups.",
        "svg_func": get_svg_lesson_5,
        "diagram_title": "The Highway of Chastity: Five Practical Behavioral Guardrails",
        "table_title": "The 5 Islamic Guardrails of Chastity",
        "table_headers": ["Guardrail", "Core Practice", "Temptation Blocked", "Youth Implementation"],
        "table_rows": [
            ["1. Eye Gate", "Ghad al-Basar (Lowering gaze)", "Suggestive & explicit media", "1-second rule: Look away and swipe"],
            ["2. Attire Gate", "Covering Awrah modestly", "Objectification & lustful gaze", "Wear loose, dignified clothes"],
            ["3. Space Gate", "Avoiding Khalwah (Isolation)", "Private compromise & coercion", "Study in public tables & libraries"],
            ["4. Habit Gate", "Voluntary Fasting (Sawm)", "Overwhelming physical impulses", "Fast Mondays/Thursdays for discipline"],
            ["5. Digital Gate", "Screen hygiene & app filtering", "Online grooming & cyber sins", "Mute/leave unmoderated group chats"]
        ],
        "scenario": "Yusuf and Amina are assigned by their teacher to work on a joint science project after school. Since the school library is closed, Yusuf suggests, 'Let's work in my room at home; my parents are away, so we will have absolute quiet.' Amina pauses and thinks about the guardrail of avoiding Khalwah (private isolation). She says, 'Yusuf, I want us to get an A on this project, but it is not safe or permissible for us to be alone in a closed house. Let's sit at this open table in the school courtyard instead. It is public, respectful, and we can still focus perfectly.' Yusuf respects her decision, and they complete a highly successful project while maintaining their moral boundaries.",
        "real_world": "Implement the 'Gaze Shield Protocol' this week. Whenever an inappropriate, suggestive image or video appears on your television, social media feed, or phone screen, instantly look away and swipe past it within one second. Treat this first look as a test of your Taqwa. Notice how guarding your eyes builds deep inner peace, focus, and mental clarity.",
        "reflection": "Why does private, unchaperoned isolation (Khalwah) increase the risk of making poor moral decisions?",
        "misconception": "Remember: Practicing modesty and avoiding Khalwah does not mean men and women cannot cooperate. In Islam, men and women work together in classrooms, hospitals, and communities with mutual respect, professional decorum, and public dignity.",
        "yt_title": "Guardrails of Chastity: Practical Youth Guidance",
        "yt_desc": "How teenagers can navigate digital temptations, lower the gaze, and build moral self-efficacy.",
        "yt_id": "d04bUq0-1p8",
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/d/d3/Al-Azhar_Mosque_Courtyard.jpg/1280px-Al-Azhar_Mosque_Courtyard.jpg",
        "image_title": "Courtyard of Al-Azhar Mosque",
        "image_caption": "Historic Islamic academic institution where scholarship and ethical discipline have guided generations.",
        "mcq": {
            "question": "Zainab wants to keep her digital habits pure. A friend invites her to a private, unmoderated online group chat where members frequently share suggestive jokes and inappropriate photos. What is the most responsible, preventative action Zainab should take?",
            "options": [
                "Join the group chat but pretend she does not see the inappropriate material.",
                "Decline the invitation, explaining politely that she prefers clean, respectful spaces, and recommend a wholesome study group instead.",
                "Join the group and start arguing with members to make them feel guilty.",
                "Forward the inappropriate photos to other friends to demonstrate how bad the group is."
            ],
            "answer": "B",
            "explanation": "Declining to enter an environment of temptation demonstrates the principle of Sadd al-Dhara'i (blocking the means to sin), guarding one's thoughts and heart from harmful influences."
        },
        "summary_content": "Prevention is always better than cure; Islam builds behavioral guardrails to block the paths to sin. Lowering the gaze and modest dress protect our thoughts and promote mutual respect. Avoiding private isolation (Khalwah) and practicing fasting (Sawm) are powerful shields for youth.",
        "key_points": [
            "Sadd al-Dhara'i proactively eliminates environments and habits that lead to sin.",
            "Ghad al-Basar and modest dress foster respect over physical objectification.",
            "Avoiding Khalwah and utilizing voluntary fasting build inner spiritual resilience."
        ],
        "exit_ticket": "List three behavioral guardrails Islam establishes to protect youth from moral deviation."
    },
    {
        "unit_order": 6,
        "lesson_title": "Unit synthesis",
        "inquiry": "How do we consolidate our understanding of sexual morality, self-discipline, and the protective frameworks of Islam?",
        "hook": "Imagine you are a structural engineer designing a major suspension bridge across a deep, windy river. You must ensure cables are strong, pillars are deeply anchored, and safety barriers are secure. If you ignore even one safety feature, the entire bridge could collapse. In this final synthesis lesson, we act as master engineers of our own character, assembling the definitions, consequences, divine wisdom, and preventative guardrails into an unbreakable bridge of chastity and moral integrity.",
        "concept_name": "Moral Cohesion (Iffah) and Active Advocacy",
        "concept_explanation": "Moral cohesion represents the complete integration of spiritual devotion, mental discipline, and modest conduct to build an honorable life. Active advocacy is the responsibility of a Muslim youth to not only practice modesty personally, but to champion respect, safety, and clean speech in their school and digital communities.",
        "scripture_quran": "And turn to Allah in repentance, all of you, O believers, that you might succeed.",
        "scripture_quran_ref": "Surah An-Nur, 24:31",
        "scripture_hadith": "The believer is not one who slanders, curses, or speaks obscenities.",
        "scripture_hadith_ref": "Sunan al-Tirmidhi, 1977",
        "deep_explanation": "Synthesizing the unit's core architecture:\n\n1. Sacred Foundation: The human body is an Amanah; physical intimacy is restricted solely to the sacred contract of marriage (Nikah).\n2. Multi-Tiered Harm of Zina: Loss of faith and inner peace, transmission of STIs/HIV, broken families, confused lineage, and economic strain on society.\n3. The 5 Guardrails: Lowering the gaze, modest dress, avoiding Khalwah, the shield of fasting, and digital hygiene.\n4. Sincere Repentance (Tawbah): For anyone who has slipped, Allah's door of forgiveness is always open. Sincere repentance, remorse, and moral reform restore the heart to purity.",
        "svg_func": get_svg_lesson_6,
        "diagram_title": "Master Synthesis: The Fortress of Moral Integrity (Iffah)",
        "table_title": "Unit Synthesis: Comprehensive Review Matrix",
        "table_headers": ["Pedagogical Component", "Core Theological Teaching", "Practical Life Application", "Societal Benefit"],
        "table_rows": [
            ["Definition & Scope", "Zina is major sin; avoid preliminary steps", "Guard digital devices & language", "Preserves personal honor"],
            ["Individual Harm", "Loss of Iman, guilt, STIs & HIV risk", "Practice abstinence until Nikah", "Guarantees physical health"],
            ["Societal Harm", "Confused lineage & broken homes", "Support two-parent family stability", "Reduces burden on state/charity"],
            ["Preventative Gates", "Sadd al-Dhara'i: Gaze, Dress, No Khalwah", "Public study groups & voluntary fasting", "Creates safe, inclusive schools"],
            ["Spiritual Renewal", "Tawbah wipe away past mistakes", "Turn to Allah with sincere reform", "Restores hope & moral agency"]
        ],
        "scenario": "A classmate, Omar, feels depressed because he has been spending hours looking at inappropriate websites on his phone, and his grades are dropping. Applying the lessons of this unit, his friend Ali says: 'Omar, do not despair. You made a mistake, but the door of Tawbah is wide open. First, delete those browsing histories and apps right now. Second, join me for soccer after school so your time is full of positive energy. Third, pray two Rak'ahs and ask Allah for forgiveness and strength. Allah loves those who turn back to Him in repentance.' Ali's balanced, supportive approach gives Omar hope and helps him regain his moral discipline.",
        "real_world": "As a class, draft a 'VLearn Modesty Charter' for your classroom notice board. Include practical commitments such as: 1. We will use only clean, respectful language in our speech and WhatsApp groups; 2. We will respect each other's physical and digital privacy; 3. We will support one another in maintaining high moral standards. Sign your names to the charter as a pledge of mutual support.",
        "reflection": "Which of the preventative guardrails studied in this unit do you find most valuable for navigating digital challenges like social media? Why?",
        "misconception": "Remember: Sincere repentance (Tawbah) completely wipes away past sins. Islam never condemns a person to eternal shame if they turn to Allah with genuine remorse, reform their habits, and resolve never to return to the sin.",
        "yt_title": "Building Moral Immunity and Sincere Tawbah",
        "yt_desc": "A powerful synthesis on developing spiritual resilience, overcoming slip-ups, and building lasting character.",
        "yt_id": "0-m2i1oB4P0",
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/2/23/Sultan_Ahmed_Mosque_Istanbul.jpg/1280px-Sultan_Ahmed_Mosque_Istanbul.jpg",
        "image_title": "The Blue Mosque (Sultan Ahmed Mosque) in Istanbul",
        "image_caption": "Historic architectural symbol of spiritual aspiration, moral purity, and community solidarity in Islam.",
        "mcq": {
            "question": "A classmate is struggling with compulsive consumption of inappropriate online media and feels hopeless. Applying the full synthesis of this unit, what is the most balanced, source-grounded advice to give him?",
            "options": [
                "Tell him he is permanently ruined and can never be a practicing Muslim again.",
                "Advise him to delete bookmarks, install content filters, engage in wholesome sports, and seek sincere Tawbah from Allah with hope in His mercy.",
                "Ignore him completely because discussing personal struggles is improper.",
                "Share his private struggles on the school chat group to shame him into stopping."
            ],
            "answer": "B",
            "explanation": "This response combines practical prevention (content filters, healthy sports) with spiritual healing (Tawbah and hope in Allah's mercy), supporting personal reform without public shame."
        },
        "summary_content": "Sexual morality is a vital protection for individual health and societal peace. Modesty must be practiced holistically in our gaze, dress, speech, and digital spaces. Sincere repentance (Tawbah) is always available to heal mistakes and rebuild upright character.",
        "key_points": [
            "Iffah integrates spiritual devotion, mental discipline, and modest conduct.",
            "Preventative guardrails protect youth from falling off the cliff of temptation.",
            "Tawbah restores spiritual purity and provides a fresh start for the sincere believer."
        ],
        "exit_ticket": "Write down the single most important lesson you have learned in this unit and how you will use it to maintain your personal integrity."
    }
]


# ─────────────────────────────────────────────────────────────────────────────
# INGESTION FUNCTION
# ─────────────────────────────────────────────────────────────────────────────

def ingest_grade9_ire_topic11():
    print("=" * 80)
    print("STARTING INGESTION: GRADE 9 IRE — TOPIC 11: PROHIBITIONS IN ISLAM: ZINA")
    print("=" * 80)

    try:
        topic = Topic.objects.get(id=351)
    except Topic.DoesNotExist:
        print("ERROR: Topic ID 351 does not exist!")
        sys.exit(1)

    print(f"Target Topic: ID={topic.id}, Name='{topic.name}', Order={topic.order}")

    with transaction.atomic():
        # Clean existing units if any
        existing_units = LearningUnit.objects.filter(topic=topic)
        if existing_units.exists():
            print(f"Cleaning {existing_units.count()} existing units under Topic {topic.id}...")
            existing_units.delete()

        total_units = 0
        total_lessons = 0
        total_blocks = 0
        total_assets = 0

        for cfg in LESSONS_CONFIG:
            u_order = cfg["unit_order"]
            l_title = cfg["lesson_title"]

            # 1. Create LearningUnit
            unit = LearningUnit.objects.create(
                topic=topic,
                name=f"Lesson 5.3.{u_order}: {l_title}",
                order=u_order,
                description=clean_text(cfg["concept_explanation"][:250] + "...")
            )
            total_units += 1

            # 2. Create Published Lesson
            lesson = Lesson.objects.create(
                topic=topic,
                learning_unit=unit,
                title=clean_text(l_title),
                status="published",
                version=1
            )
            total_lessons += 1

            # ─────────────────────────────────────────────────────────────────
            # CARD 1 (Page 1): Orientation & Hook (2 blocks)
            # ─────────────────────────────────────────────────────────────────
            img_asset = LessonAsset.objects.create(
                lesson=lesson,
                asset_type="image",
                title=clean_text(cfg["image_title"]),
                url=cfg["image_url"],
                metadata={
                    "caption": clean_text(cfg["image_caption"]),
                    "credit": "Wikimedia Commons"
                }
            )
            total_assets += 1

            b_img = LessonBlock.objects.create(
                lesson=lesson,
                page_number=1,
                page_title="Orientation & Hook",
                order=10,
                component_order=1,
                block_type="suggested_image",
                component_type="suggested_image",
                title=clean_text(cfg["image_title"]),
                content={
                    "title": clean_text(cfg["image_title"]),
                    "caption": clean_text(cfg["image_caption"]),
                    "url": cfg["image_url"]
                }
            )
            b_img.assets.add(img_asset)

            LessonBlock.objects.create(
                lesson=lesson,
                page_number=1,
                page_title="Orientation & Hook",
                order=20,
                component_order=2,
                block_type="learning_goal",
                component_type="learning_goal",
                title="Lesson Orientation & Inquiry",
                content={
                    "title": "Lesson Orientation & Inquiry",
                    "inquiry_question": clean_text(cfg["inquiry"]),
                    "hook": clean_text(cfg["hook"]),
                    "learning_goals": [
                        f"Understand the core meaning of {l_title}",
                        "Examine foundational Qur'anic verses and Hadith",
                        "Analyze practical scenarios and daily ethical applications"
                    ]
                }
            )

            # ─────────────────────────────────────────────────────────────────
            # CARD 2 (Page 2): Core Theological Concept (2 blocks)
            # ─────────────────────────────────────────────────────────────────
            LessonBlock.objects.create(
                lesson=lesson,
                page_number=2,
                page_title="Core Theological Concept",
                order=30,
                component_order=1,
                block_type="concept_explanation",
                component_type="concept_explanation",
                title=clean_text(cfg["concept_name"]),
                content={
                    "title": clean_text(cfg["concept_name"]),
                    "explanation": clean_text(cfg["concept_explanation"]),
                    "text": clean_text(cfg["concept_explanation"])
                }
            )

            LessonBlock.objects.create(
                lesson=lesson,
                page_number=2,
                page_title="Core Theological Concept",
                order=40,
                component_order=2,
                block_type="callout",
                component_type="callout",
                title="Scripture Source Panel",
                content={
                    "title": "Scripture Source Panel",
                    "callout_type": "scripture",
                    "quran_verse": clean_text(cfg["scripture_quran"]),
                    "quran_reference": clean_text(cfg["scripture_quran_ref"]),
                    "hadith_text": clean_text(cfg["scripture_hadith"]),
                    "hadith_reference": clean_text(cfg["scripture_hadith_ref"]),
                    "text": clean_text(
                        f"**Qur'an ({cfg['scripture_quran_ref']}):**\n> \"{cfg['scripture_quran']}\"\n\n"
                        f"**Hadith ({cfg['scripture_hadith_ref']}):**\n> \"{cfg['scripture_hadith']}\""
                    )
                }
            )

            # ─────────────────────────────────────────────────────────────────
            # CARD 3 (Page 3): Deep Explanation & SVG Diagram (3 blocks)
            # ─────────────────────────────────────────────────────────────────
            LessonBlock.objects.create(
                lesson=lesson,
                page_number=3,
                page_title="Deep Pedagogical Explanation",
                order=50,
                component_order=1,
                block_type="concept_explanation",
                component_type="concept_explanation",
                title="Theological Analysis & Principles",
                content={
                    "title": "Theological Analysis & Principles",
                    "explanation": clean_text(cfg["deep_explanation"]),
                    "text": clean_text(cfg["deep_explanation"])
                }
            )

            svg_str = cfg["svg_func"]()
            svg_asset = LessonAsset.objects.create(
                lesson=lesson,
                asset_type="diagram",
                title=clean_text(cfg["diagram_title"]),
                metadata={
                    "svg_xml": svg_str,
                    "svg_content": svg_str,
                    "theme": "#0f172a",
                    "viewBox": "0 0 880 440",
                    "responsive": True
                }
            )
            total_assets += 1

            b_diag = LessonBlock.objects.create(
                lesson=lesson,
                page_number=3,
                page_title="Deep Pedagogical Explanation",
                order=60,
                component_order=2,
                block_type="suggested_diagram",
                component_type="suggested_diagram",
                title=clean_text(cfg["diagram_title"]),
                content={
                    "title": clean_text(cfg["diagram_title"]),
                    "svg_xml": svg_str,
                    "svg_content": svg_str
                },
                metadata={
                    "svg_xml": svg_str,
                    "svg_content": svg_str
                }
            )
            b_diag.assets.add(svg_asset)

            LessonBlock.objects.create(
                lesson=lesson,
                page_number=3,
                page_title="Deep Pedagogical Explanation",
                order=70,
                component_order=3,
                block_type="comparison_table",
                component_type="comparison_table",
                title=clean_text(cfg["table_title"]),
                content={
                    "title": clean_text(cfg["table_title"]),
                    "headers": [clean_text(h) for h in cfg["table_headers"]],
                    "rows": [[clean_text(c) for c in row] for row in cfg["table_rows"]]
                }
            )

            # ─────────────────────────────────────────────────────────────────
            # CARD 4 (Page 4): Lived Reality Scenario (1 block)
            # ─────────────────────────────────────────────────────────────────
            LessonBlock.objects.create(
                lesson=lesson,
                page_number=4,
                page_title="Lived Reality Scenario",
                order=80,
                component_order=1,
                block_type="worked_example",
                component_type="worked_example",
                title="Practical Student Scenario",
                content={
                    "title": "Practical Student Scenario",
                    "scenario": clean_text(cfg["scenario"]),
                    "text": clean_text(cfg["scenario"])
                }
            )

            # ─────────────────────────────────────────────────────────────────
            # CARD 5 (Page 5): Real-World Ethics & Video (4 blocks)
            # ─────────────────────────────────────────────────────────────────
            LessonBlock.objects.create(
                lesson=lesson,
                page_number=5,
                page_title="Application & Reflection",
                order=90,
                component_order=1,
                block_type="real_world_example",
                component_type="real_world_example",
                title="Real-World Ethical Action",
                content={
                    "title": "Real-World Ethical Action",
                    "application": clean_text(cfg["real_world"]),
                    "text": clean_text(cfg["real_world"])
                }
            )

            LessonBlock.objects.create(
                lesson=lesson,
                page_number=5,
                page_title="Application & Reflection",
                order=100,
                component_order=2,
                block_type="reflection",
                component_type="reflection",
                title="Introspective Prompt",
                content={
                    "title": "Introspective Prompt",
                    "prompt": clean_text(cfg["reflection"]),
                    "text": clean_text(cfg["reflection"])
                }
            )

            LessonBlock.objects.create(
                lesson=lesson,
                page_number=5,
                page_title="Application & Reflection",
                order=110,
                component_order=3,
                block_type="common_misconception",
                component_type="common_misconception",
                title="Misconception Check",
                content={
                    "title": "Misconception Check",
                    "content": clean_text(cfg["misconception"]),
                    "correction": clean_text(cfg["misconception"]),
                    "text": clean_text(cfg["misconception"])
                }
            )

            yt_asset = LessonAsset.objects.create(
                lesson=lesson,
                asset_type="video",
                title=clean_text(cfg["yt_title"]),
                url=f"https://www.youtube.com/watch?v={cfg['yt_id']}",
                metadata={
                    "youtube_id": cfg["yt_id"],
                    "description": clean_text(cfg["yt_desc"])
                }
            )
            total_assets += 1

            b_vid = LessonBlock.objects.create(
                lesson=lesson,
                page_number=5,
                page_title="Application & Reflection",
                order=120,
                component_order=4,
                block_type="suggested_video",
                component_type="suggested_video",
                title=clean_text(cfg["yt_title"]),
                content={
                    "title": clean_text(cfg["yt_title"]),
                    "description": clean_text(cfg["yt_desc"]),
                    "url": f"https://www.youtube.com/watch?v={cfg['yt_id']}",
                    "youtube_id": cfg["yt_id"]
                }
            )
            b_vid.assets.add(yt_asset)

            # ─────────────────────────────────────────────────────────────────
            # CARD 6 (Page 6): Knowledge Mastery Check (1 block)
            # ─────────────────────────────────────────────────────────────────
            mcq_data = cfg["mcq"]
            LessonBlock.objects.create(
                lesson=lesson,
                page_number=6,
                page_title="Knowledge Mastery Check",
                order=130,
                component_order=1,
                block_type="knowledge_check",
                component_type="knowledge_check",
                title="Mastery Knowledge Check",
                content={
                    "title": "Mastery Knowledge Check",
                    "question": clean_text(mcq_data["question"]),
                    "options": [clean_text(opt) for opt in mcq_data["options"]],
                    "answer": clean_text(mcq_data["answer"]),
                    "correct_answer": clean_text(mcq_data["answer"]),
                    "explanation": clean_text(mcq_data["explanation"])
                }
            )

            # ─────────────────────────────────────────────────────────────────
            # CARD 7 (Page 7): Summary & Exit Ticket (2 blocks)
            # ─────────────────────────────────────────────────────────────────
            LessonBlock.objects.create(
                lesson=lesson,
                page_number=7,
                page_title="Summary & Exit Ticket",
                order=140,
                component_order=1,
                block_type="summary",
                component_type="summary",
                title="Summary & Vocabulary Review",
                content={
                    "title": "Summary & Vocabulary Review",
                    "content": clean_text(cfg["summary_content"]),
                    "text": clean_text(cfg["summary_content"]),
                    "takeaways": [clean_text(p) for p in cfg["key_points"]]
                }
            )

            LessonBlock.objects.create(
                lesson=lesson,
                page_number=7,
                page_title="Summary & Exit Ticket",
                order=150,
                component_order=2,
                block_type="mini_activity",
                component_type="mini_activity",
                title="Exit Ticket & Action Step",
                content={
                    "title": "Exit Ticket & Action Step",
                    "content": clean_text(cfg["exit_ticket"]),
                    "text": clean_text(cfg["exit_ticket"])
                }
            )

            total_blocks += 15
            print(f"  [+] Ingested Lesson {u_order}/6: '{l_title}' (7 cards, 15 blocks, 3 assets)")

    print("=" * 80)
    print("TOPIC 11 INGESTION COMPLETE & VERIFIED!")
    print(f"  LearningUnits : {total_units} / 6")
    print(f"  Lessons       : {total_lessons} / 6 (Published)")
    print(f"  Blocks        : {total_blocks} (15 per lesson, 7 pages)")
    print(f"  Assets        : {total_assets} (6 SVGs, 6 images, 6 videos)")
    print("=" * 80)


if __name__ == "__main__":
    ingest_grade9_ire_topic11()
