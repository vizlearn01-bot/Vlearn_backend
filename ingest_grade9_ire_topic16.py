"""
VLearn CBC Grade 9 IRE — Topic 16: Trade and Financial Transactions in Islam
Production Ingestion and Enrichment Script for all 6 Lessons

Target Topic in DB: Topic ID 356 (Subject: IRE ID 53, Grade: Grade 9 ID 18)
Source Markdown: /home/jason-bitega/Desktop/VL/vlearn_repositories/Grade 9 IRE/trade-and-finance.md

6 Lessons Ingested & Fully Enriched:
  1. Lesson 6.5.1: Ethical finance
  2. Lesson 6.5.2: Rules of borrowing
  3. Lesson 6.5.3: Rules of lending
  4. Lesson 6.5.4: Consumer rights and protection
  5. Lesson 6.5.5: Practice: a fair agreement
  6. Lesson 6.5.6: Unit synthesis
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
# 6 DEDICATED RESPONSIVE PEDAGOGICAL VECTOR SVGS (#0f172a theme, viewBox 880x440)
# ─────────────────────────────────────────────────────────────────────────────

def get_svg_lesson_1():
    """Lesson 6.5.1: The Three Pillars of Islamic Ethical Finance"""
    return """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 880 440" width="100%" height="100%">
  <defs>
    <linearGradient id="bg161" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#0f172a"/>
      <stop offset="50%" stop-color="#1e293b"/>
      <stop offset="100%" stop-color="#0f172a"/>
    </linearGradient>
    <linearGradient id="p1Grad" x1="0%" y1="0%" x2="0%" y2="100%">
      <stop offset="0%" stop-color="#10b981"/>
      <stop offset="100%" stop-color="#047857"/>
    </linearGradient>
    <linearGradient id="p2Grad" x1="0%" y1="0%" x2="0%" y2="100%">
      <stop offset="0%" stop-color="#ef4444"/>
      <stop offset="100%" stop-color="#b91c1c"/>
    </linearGradient>
    <linearGradient id="p3Grad" x1="0%" y1="0%" x2="0%" y2="100%">
      <stop offset="0%" stop-color="#38bdf8"/>
      <stop offset="100%" stop-color="#0284c7"/>
    </linearGradient>
  </defs>

  <rect width="880" height="440" rx="14" fill="url(#bg161)"/>
  <rect x="2" y="2" width="876" height="436" rx="12" fill="none" stroke="#334155" stroke-width="1.5"/>

  <!-- Header -->
  <text x="440" y="38" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="16" font-weight="700" text-anchor="middle">THE THREE PILLARS OF ISLAMIC ETHICAL FINANCE</text>
  <text x="440" y="58" fill="#94a3b8" font-family="system-ui, sans-serif" font-size="12" text-anchor="middle">Wealth as a Sacred Trust (Amanah) Governed by Divine Justice, Mutual Consent &amp; Risk-Sharing</text>

  <!-- Pillar 1: Halal Earnings -->
  <g transform="translate(50, 85)">
    <rect width="235" height="300" rx="10" fill="#1e293b" stroke="#10b981" stroke-width="2"/>
    <rect width="235" height="48" rx="10" fill="url(#p1Grad)"/>
    <text x="117" y="30" fill="#ffffff" font-family="system-ui, sans-serif" font-size="14" font-weight="700" text-anchor="middle">1. HALAL EARNINGS</text>
    
    <circle cx="117" cy="95" r="28" fill="#064e3b" stroke="#10b981" stroke-width="2"/>
    <text x="117" y="102" fill="#10b981" font-family="system-ui, sans-serif" font-size="20" font-weight="bold" text-anchor="middle">✓</text>
    
    <text x="117" y="150" fill="#f8fafc" font-family="system-ui, sans-serif" font-size="13" font-weight="600" text-anchor="middle">Lawful &amp; Wholesome (Tayyib)</text>
    <text x="18" y="180" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="11.5" line-height="1.4">
      <tspan x="18" dy="0">• No fraud, cheating, or deceit</tspan>
      <tspan x="18" dy="20">• Prohibited commodities banned</tspan>
      <tspan x="18" dy="16">  (alcohol, gambling, pork)</tspan>
      <tspan x="18" dy="20">• Mutual consent (Taradin)</tspan>
      <tspan x="18" dy="20">• Transparent product disclosure</tspan>
    </text>
    <rect x="20" y="255" width="195" height="30" rx="6" fill="#0f172a"/>
    <text x="117" y="275" fill="#34d399" font-family="system-ui, sans-serif" font-size="11" font-weight="600" text-anchor="middle">Barakah in Pure Livelihood</text>
  </g>

  <!-- Pillar 2: Prohibition of Usury (Riba) -->
  <g transform="translate(322, 85)">
    <rect width="235" height="300" rx="10" fill="#1e293b" stroke="#ef4444" stroke-width="2"/>
    <rect width="235" height="48" rx="10" fill="url(#p2Grad)"/>
    <text x="117" y="30" fill="#ffffff" font-family="system-ui, sans-serif" font-size="14" font-weight="700" text-anchor="middle">2. PROHIBITION OF RIBA</text>
    
    <circle cx="117" cy="95" r="28" fill="#7f1d1d" stroke="#ef4444" stroke-width="2"/>
    <text x="117" y="102" fill="#ef4444" font-family="system-ui, sans-serif" font-size="20" font-weight="bold" text-anchor="middle">✕</text>
    
    <text x="117" y="150" fill="#f8fafc" font-family="system-ui, sans-serif" font-size="13" font-weight="600" text-anchor="middle">Zero Interest / Usury</text>
    <text x="18" y="180" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="11.5">
      <tspan x="18" dy="0">• Money cannot spawn money</tspan>
      <tspan x="18" dy="20">• No guaranteed risk-free gain</tspan>
      <tspan x="18" dy="20">• Protects borrowers from debt trap</tspan>
      <tspan x="18" dy="20">• Eliminates economic tyranny</tspan>
      <tspan x="18" dy="20">• Surah Al-Baqarah 2:275</tspan>
    </text>
    <rect x="20" y="255" width="195" height="30" rx="6" fill="#0f172a"/>
    <text x="117" y="275" fill="#f87171" font-family="system-ui, sans-serif" font-size="11" font-weight="600" text-anchor="middle">Defends Vulnerable from Ruin</text>
  </g>

  <!-- Pillar 3: Social Equity & Risk-Sharing -->
  <g transform="translate(595, 85)">
    <rect width="235" height="300" rx="10" fill="#1e293b" stroke="#38bdf8" stroke-width="2"/>
    <rect width="235" height="48" rx="10" fill="url(#p3Grad)"/>
    <text x="117" y="30" fill="#ffffff" font-family="system-ui, sans-serif" font-size="14" font-weight="700" text-anchor="middle">3. SOCIAL EQUITY</text>
    
    <circle cx="117" cy="95" r="28" fill="#0c4a6e" stroke="#38bdf8" stroke-width="2"/>
    <text x="117" y="102" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="18" font-weight="bold" text-anchor="middle">⚖</text>
    
    <text x="117" y="150" fill="#f8fafc" font-family="system-ui, sans-serif" font-size="13" font-weight="600" text-anchor="middle">Risk-Sharing &amp; Circulation</text>
    <text x="18" y="180" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="11.5">
      <tspan x="18" dy="0">• Mudarabah &amp; Musharakah</tspan>
      <tspan x="18" dy="16">  (Profit &amp; Loss sharing)</tspan>
      <tspan x="18" dy="20">• Zakat (2.5% wealth redistribution)</tspan>
      <tspan x="18" dy="20">• Sadaqah &amp; Waqf endowments</tspan>
      <tspan x="18" dy="20">• Anti-hoarding (Kanz) safeguards</tspan>
    </text>
    <rect x="20" y="255" width="195" height="30" rx="6" fill="#0f172a"/>
    <text x="117" y="275" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="11" font-weight="600" text-anchor="middle">Universal Socio-Economic Justice</text>
  </g>

  <!-- Bottom Banner -->
  <rect x="50" y="398" width="780" height="28" rx="6" fill="#1e293b" stroke="#475569" stroke-width="1"/>
  <text x="440" y="417" fill="#fbbf24" font-family="system-ui, sans-serif" font-size="11.5" font-weight="600" text-anchor="middle">"Allah has permitted trade and has forbidden interest (usury)." — Surah Al-Baqarah 2:275</text>
</svg>"""


def get_svg_lesson_2():
    """Lesson 6.5.2: The Islamic Borrower's Protocol & Debt Checklist"""
    return """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 880 440" width="100%" height="100%">
  <defs>
    <linearGradient id="bg162" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#0f172a"/>
      <stop offset="50%" stop-color="#1e293b"/>
      <stop offset="100%" stop-color="#0f172a"/>
    </linearGradient>
  </defs>

  <rect width="880" height="440" rx="14" fill="url(#bg162)"/>
  <rect x="2" y="2" width="876" height="436" rx="12" fill="none" stroke="#334155" stroke-width="1.5"/>

  <!-- Header -->
  <text x="440" y="38" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="16" font-weight="700" text-anchor="middle">THE ISLAMIC BORROWER'S PROTOCOL (AYAT AL-DAYN)</text>
  <text x="440" y="58" fill="#94a3b8" font-family="system-ui, sans-serif" font-size="12" text-anchor="middle">Step-by-Step Shariah Guidelines for Ethical Borrowing (Surah Al-Baqarah 2:282)</text>

  <!-- Step 1 -->
  <g transform="translate(40, 85)">
    <rect width="185" height="290" rx="8" fill="#1e293b" stroke="#38bdf8" stroke-width="1.5"/>
    <rect width="185" height="38" rx="8" fill="#0284c7"/>
    <text x="92" y="24" fill="#ffffff" font-family="system-ui, sans-serif" font-size="13" font-weight="700" text-anchor="middle">STEP 1: GENUINE NEED</text>
    
    <circle cx="92" cy="72" r="22" fill="#0c4a6e" stroke="#38bdf8" stroke-width="1.5"/>
    <text x="92" y="79" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="16" font-weight="bold" text-anchor="middle">1</text>
    
    <text x="92" y="118" fill="#f8fafc" font-family="system-ui, sans-serif" font-size="12.5" font-weight="600" text-anchor="middle">Need vs Luxury</text>
    <text x="14" y="145" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="11">
      <tspan x="14" dy="0">• Only for necessities</tspan>
      <tspan x="14" dy="18">  (medicine, food, education)</tspan>
      <tspan x="14" dy="20">• Not for showing off</tspan>
      <tspan x="14" dy="18">  or luxury consumption</tspan>
      <tspan x="14" dy="20">• Debt is a heavy burden</tspan>
      <tspan x="14" dy="18">  in Dunya &amp; Akhirah</tspan>
    </text>
    <rect x="14" y="240" width="157" height="26" rx="4" fill="#0f172a"/>
    <text x="92" y="257" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="10.5" font-weight="600" text-anchor="middle">Spiritual Restraint</text>
  </g>

  <!-- Step 2 -->
  <g transform="translate(245, 85)">
    <rect width="185" height="290" rx="8" fill="#1e293b" stroke="#a855f7" stroke-width="1.5"/>
    <rect width="185" height="38" rx="8" fill="#7e22ce"/>
    <text x="92" y="24" fill="#ffffff" font-family="system-ui, sans-serif" font-size="13" font-weight="700" text-anchor="middle">STEP 2: WRITING (KITABAH)</text>
    
    <circle cx="92" cy="72" r="22" fill="#581c87" stroke="#a855f7" stroke-width="1.5"/>
    <text x="92" y="79" fill="#c084fc" font-family="system-ui, sans-serif" font-size="16" font-weight="bold" text-anchor="middle">2</text>
    
    <text x="92" y="118" fill="#f8fafc" font-family="system-ui, sans-serif" font-size="12.5" font-weight="600" text-anchor="middle">Formal Documentation</text>
    <text x="14" y="145" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="11">
      <tspan x="14" dy="0">• State exact principal sum</tspan>
      <tspan x="14" dy="20">• Fix clear repayment date</tspan>
      <tspan x="14" dy="20">• Debtor dictates terms</tspan>
      <tspan x="14" dy="20">• Two trustworthy witnesses</tspan>
      <tspan x="14" dy="20">• Longest Quranic verse</tspan>
    </text>
    <rect x="14" y="240" width="157" height="26" rx="4" fill="#0f172a"/>
    <text x="92" y="257" fill="#c084fc" font-family="system-ui, sans-serif" font-size="10.5" font-weight="600" text-anchor="middle">Prevents Misunderstandings</text>
  </g>

  <!-- Step 3 -->
  <g transform="translate(450, 85)">
    <rect width="185" height="290" rx="8" fill="#1e293b" stroke="#f59e0b" stroke-width="1.5"/>
    <rect width="185" height="38" rx="8" fill="#d97706"/>
    <text x="92" y="24" fill="#ffffff" font-family="system-ui, sans-serif" font-size="13" font-weight="700" text-anchor="middle">STEP 3: PURE INTENTION</text>
    
    <circle cx="92" cy="72" r="22" fill="#78350f" stroke="#f59e0b" stroke-width="1.5"/>
    <text x="92" y="79" fill="#fbbf24" font-family="system-ui, sans-serif" font-size="16" font-weight="bold" text-anchor="middle">3</text>
    
    <text x="92" y="118" fill="#f8fafc" font-family="system-ui, sans-serif" font-size="12.5" font-weight="600" text-anchor="middle">Intention to Pay (Niyyah)</text>
    <text x="14" y="145" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="11">
      <tspan x="14" dy="0">• Intend full repayment</tspan>
      <tspan x="14" dy="20">• Allah aids sincere debtors</tspan>
      <tspan x="14" dy="20">• Borrowing to squander</tspan>
      <tspan x="14" dy="18">  leads to destruction</tspan>
      <tspan x="14" dy="20">• Pray for debt liberation</tspan>
    </text>
    <rect x="14" y="240" width="157" height="26" rx="4" fill="#0f172a"/>
    <text x="92" y="257" fill="#fbbf24" font-family="system-ui, sans-serif" font-size="10.5" font-weight="600" text-anchor="middle">Divine Assistance</text>
  </g>

  <!-- Step 4 -->
  <g transform="translate(655, 85)">
    <rect width="185" height="290" rx="8" fill="#1e293b" stroke="#10b981" stroke-width="1.5"/>
    <rect width="185" height="38" rx="8" fill="#059669"/>
    <text x="92" y="24" fill="#ffffff" font-family="system-ui, sans-serif" font-size="13" font-weight="700" text-anchor="middle">STEP 4: PROMPT PAYMENT</text>
    
    <circle cx="92" cy="72" r="22" fill="#064e3b" stroke="#10b981" stroke-width="1.5"/>
    <text x="92" y="79" fill="#34d399" font-family="system-ui, sans-serif" font-size="16" font-weight="bold" text-anchor="middle">4</text>
    
    <text x="92" y="118" fill="#f8fafc" font-family="system-ui, sans-serif" font-size="12.5" font-weight="600" text-anchor="middle">Honoring the Due Date</text>
    <text x="14" y="145" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="11">
      <tspan x="14" dy="0">• Pay on or before due date</tspan>
      <tspan x="14" dy="20">• Delaying when able is</tspan>
      <tspan x="14" dy="18">  injustice (Zulm)</tspan>
      <tspan x="14" dy="20">• Communicate early if hard</tspan>
      <tspan x="14" dy="20">• Debt cleared before estate</tspan>
    </text>
    <rect x="14" y="240" width="157" height="26" rx="4" fill="#0f172a"/>
    <text x="92" y="257" fill="#34d399" font-family="system-ui, sans-serif" font-size="10.5" font-weight="600" text-anchor="middle">Preserves Trust &amp; Honor</text>
  </g>

  <!-- Bottom Banner -->
  <rect x="40" y="395" width="800" height="30" rx="6" fill="#1e293b" stroke="#475569" stroke-width="1"/>
  <text x="440" y="415" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="12" font-weight="600" text-anchor="middle">"Procrastination in paying debts by a wealthy person is an act of injustice." — Sahih al-Bukhari 2287</text>
</svg>"""


def get_svg_lesson_3():
    """Lesson 6.5.3: The Ethical Lender's Framework: Qard Hasan vs Usury"""
    return """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 880 440" width="100%" height="100%">
  <defs>
    <linearGradient id="bg163" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#0f172a"/>
      <stop offset="50%" stop-color="#1e293b"/>
      <stop offset="100%" stop-color="#0f172a"/>
    </linearGradient>
  </defs>

  <rect width="880" height="440" rx="14" fill="url(#bg163)"/>
  <rect x="2" y="2" width="876" height="436" rx="12" fill="none" stroke="#334155" stroke-width="1.5"/>

  <!-- Header -->
  <text x="440" y="38" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="16" font-weight="700" text-anchor="middle">RULES OF LENDING: CONVENTIONAL USURY VS ISLAMIC QARD HASAN</text>
  <text x="440" y="58" fill="#94a3b8" font-family="system-ui, sans-serif" font-size="12" text-anchor="middle">Transforming Financial Aid from Merciless Exploitation into a Sanctuary of Divine Reward</text>

  <!-- Left: Conventional Exploitative Lending -->
  <g transform="translate(45, 80)">
    <rect width="375" height="300" rx="10" fill="#1e293b" stroke="#ef4444" stroke-width="2"/>
    <rect width="375" height="42" rx="10" fill="#991b1b"/>
    <text x="187" y="27" fill="#ffffff" font-family="system-ui, sans-serif" font-size="14" font-weight="700" text-anchor="middle">CONVENTIONAL COMMERCIAL LENDING</text>
    
    <text x="24" y="70" fill="#fca5a5" font-family="system-ui, sans-serif" font-size="12" font-weight="bold">Core Philosophy: Extraction &amp; Profit</text>
    <text x="24" y="96" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="11.5">
      <tspan x="24" dy="0">❌ Charges guaranteed interest (Riba) on principal</tspan>
      <tspan x="24" dy="24">❌ Profits directly from the borrower's hardship</tspan>
      <tspan x="24" dy="24">❌ Compounding late fees &amp; extortionate penalties</tspan>
      <tspan x="24" dy="24">❌ Aggressive repossession &amp; public humiliation</tspan>
      <tspan x="24" dy="24">❌ Traps poor families into lifelong debt slavery</tspan>
      <tspan x="24" dy="24">❌ Severe sin in Islam; war declared by Allah (2:279)</tspan>
    </text>
    
    <rect x="20" y="250" width="335" height="36" rx="6" fill="#450a0a" stroke="#ef4444" stroke-width="1"/>
    <text x="187" y="273" fill="#fca5a5" font-family="system-ui, sans-serif" font-size="11" font-weight="600" text-anchor="middle">Outcome: Social Division &amp; Economic Oppression</text>
  </g>

  <!-- Right: Islamic Qard Hasan -->
  <g transform="translate(460, 80)">
    <rect width="375" height="300" rx="10" fill="#1e293b" stroke="#10b981" stroke-width="2"/>
    <rect width="375" height="42" rx="10" fill="#065f46"/>
    <text x="187" y="27" fill="#ffffff" font-family="system-ui, sans-serif" font-size="14" font-weight="700" text-anchor="middle">ISLAMIC ETHICAL LENDING (QARD HASAN)</text>
    
    <text x="24" y="70" fill="#6ee7b7" font-family="system-ui, sans-serif" font-size="12" font-weight="bold">Core Philosophy: Worship, Compassion &amp; Solidarity</text>
    <text x="24" y="96" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="11.5">
      <tspan x="24" dy="0">✓ 100% Interest-free loan seeking only Allah's pleasure</tspan>
      <tspan x="24" dy="24">✓ Lenders forbidden from extracting gifts or benefits</tspan>
      <tspan x="24" dy="24">✓ Granting respite (Inzar) when borrower faces hardship</tspan>
      <tspan x="24" dy="24">✓ Voluntary debt remission converted to high Sadaqah</tspan>
      <tspan x="24" dy="24">✓ Prophet (PBUH): Reward of loan is 18-fold vs charity 10-fold</tspan>
      <tspan x="24" dy="24">✓ Surah Al-Baqarah 2:280 commands ease for the debtor</tspan>
    </text>
    
    <rect x="20" y="250" width="335" height="36" rx="6" fill="#064e3b" stroke="#10b981" stroke-width="1"/>
    <text x="187" y="273" fill="#6ee7b7" font-family="system-ui, sans-serif" font-size="11" font-weight="600" text-anchor="middle">Outcome: Communal Harmony, Dignity &amp; Barakah</text>
  </g>

  <!-- Footer -->
  <rect x="45" y="394" width="790" height="30" rx="6" fill="#1e293b" stroke="#475569" stroke-width="1"/>
  <text x="440" y="414" fill="#fbbf24" font-family="system-ui, sans-serif" font-size="12" font-weight="600" text-anchor="middle">"If the debtor is in difficulty, grant him time till it is easy for him to repay." — Surah Al-Baqarah 2:280</text>
</svg>"""


def get_svg_lesson_4():
    """Lesson 6.5.4: Consumer Rights Shield & Fair Market Principles"""
    return """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 880 440" width="100%" height="100%">
  <defs>
    <linearGradient id="bg164" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#0f172a"/>
      <stop offset="50%" stop-color="#1e293b"/>
      <stop offset="100%" stop-color="#0f172a"/>
    </linearGradient>
  </defs>

  <rect width="880" height="440" rx="14" fill="url(#bg164)"/>
  <rect x="2" y="2" width="876" height="436" rx="12" fill="none" stroke="#334155" stroke-width="1.5"/>

  <!-- Header -->
  <text x="440" y="38" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="16" font-weight="700" text-anchor="middle">CONSUMER RIGHTS SHIELD &amp; ETHICAL MARKETPLACE PRINCIPLES</text>
  <text x="440" y="58" fill="#94a3b8" font-family="system-ui, sans-serif" font-size="12" text-anchor="middle">Integrating Islamic Commercial Jurisprudence (Fiqh al-Muamalat) with Kenyan Consumer Protections (KEBS &amp; CAK)</text>

  <!-- 4 Quadrants -->
  <!-- Quadrant 1: Right to Full Disclosure -->
  <g transform="translate(45, 80)">
    <rect width="380" height="135" rx="8" fill="#1e293b" stroke="#38bdf8" stroke-width="1.5"/>
    <circle cx="45" cy="45" r="20" fill="#0c4a6e" stroke="#38bdf8" stroke-width="1.5"/>
    <text x="45" y="52" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="16" font-weight="bold" text-anchor="middle">1</text>
    <text x="80" y="40" fill="#f8fafc" font-family="system-ui, sans-serif" font-size="13" font-weight="700">Right to Truth &amp; Disclosure (Nasiha)</text>
    <text x="80" y="58" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="11" font-weight="600">Ban on Tadlis (Concealing Defects)</text>
    <text x="20" y="85" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="11">
      <tspan x="20" dy="0">• Seller must reveal all known defects and damages</tspan>
      <tspan x="20" dy="18">• Hadith of damp grain: "Whoever deceives us is not of us"</tspan>
      <tspan x="20" dy="18">• Clear price tags, honest weights &amp; accurate measures</tspan>
    </text>
  </g>

  <!-- Quadrant 2: Right to Safety & Quality Standards -->
  <g transform="translate(455, 80)">
    <rect width="380" height="135" rx="8" fill="#1e293b" stroke="#10b981" stroke-width="1.5"/>
    <circle cx="45" cy="45" r="20" fill="#064e3b" stroke="#10b981" stroke-width="1.5"/>
    <text x="45" y="52" fill="#10b981" font-family="system-ui, sans-serif" font-size="16" font-weight="bold" text-anchor="middle">2</text>
    <text x="80" y="40" fill="#f8fafc" font-family="system-ui, sans-serif" font-size="13" font-weight="700">Right to Safety &amp; Wholesomeness (Tayyib)</text>
    <text x="80" y="58" fill="#10b981" font-family="system-ui, sans-serif" font-size="11" font-weight="600">Compliance with KEBS &amp; Halal Verification</text>
    <text x="20" y="85" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="11">
      <tspan x="20" dy="0">• Products must not harm health, environment, or intellect</tspan>
      <tspan x="20" dy="18">• Valid expiry dates, clear ingredient listing &amp; safety marks</tspan>
      <tspan x="20" dy="18">• KEBS quality certification &amp; Halal compliance checks</tspan>
    </text>
  </g>

  <!-- Quadrant 3: Right to Cancellation & Redress -->
  <g transform="translate(45, 230)">
    <rect width="380" height="135" rx="8" fill="#1e293b" stroke="#f59e0b" stroke-width="1.5"/>
    <circle cx="45" cy="45" r="20" fill="#78350f" stroke="#f59e0b" stroke-width="1.5"/>
    <text x="45" y="52" fill="#fbbf24" font-family="system-ui, sans-serif" font-size="16" font-weight="bold" text-anchor="middle">3</text>
    <text x="80" y="40" fill="#f8fafc" font-family="system-ui, sans-serif" font-size="13" font-weight="700">Right to Redress (Khiyar al-Ayb)</text>
    <text x="80" y="58" fill="#fbbf24" font-family="system-ui, sans-serif" font-size="11" font-weight="600">Option of Defect Refund or Replacement</text>
    <text x="20" y="85" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="11">
      <tspan x="20" dy="0">• Absolute right to return goods if hidden flaws exist</tspan>
      <tspan x="20" dy="18">• "No refunds/No returns" signs cannot override fraud</tspan>
      <tspan x="20" dy="18">• Supported by Competition Authority of Kenya (CAK)</tspan>
    </text>
  </g>

  <!-- Quadrant 4: Fair Pricing & Anti-Monopoly -->
  <g transform="translate(455, 230)">
    <rect width="380" height="135" rx="8" fill="#1e293b" stroke="#a855f7" stroke-width="1.5"/>
    <circle cx="45" cy="45" r="20" fill="#581c87" stroke="#a855f7" stroke-width="1.5"/>
    <text x="45" y="52" fill="#c084fc" font-family="system-ui, sans-serif" font-size="16" font-weight="bold" text-anchor="middle">4</text>
    <text x="80" y="40" fill="#f8fafc" font-family="system-ui, sans-serif" font-size="13" font-weight="700">Protection Against Hoarding (Ihtikar)</text>
    <text x="80" y="58" fill="#c084fc" font-family="system-ui, sans-serif" font-size="11" font-weight="600">Fair Market Competition &amp; Anti-Price-Gouging</text>
    <text x="20" y="85" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="11">
      <tspan x="20" dy="0">• Hoarding food to artificially spike prices is cursed</tspan>
      <tspan x="20" dy="18">• Ban on artificial bidding (Najash) and price collusion</tspan>
      <tspan x="20" dy="18">• Open market equilibrium governed by justice and equity</tspan>
    </text>
  </g>

  <!-- Footer -->
  <rect x="45" y="380" width="790" height="32" rx="6" fill="#1e293b" stroke="#475569" stroke-width="1"/>
  <text x="440" y="401" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="12" font-weight="600" text-anchor="middle">"Whoever deceives us is not one of us." — Sahih Muslim 102</text>
</svg>"""


def get_svg_lesson_5():
    """Lesson 6.5.5: Anatomy of a Valid Islamic Contract (Aqad al-Dayn)"""
    return """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 880 440" width="100%" height="100%">
  <defs>
    <linearGradient id="bg165" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#0f172a"/>
      <stop offset="50%" stop-color="#1e293b"/>
      <stop offset="100%" stop-color="#0f172a"/>
    </linearGradient>
  </defs>

  <rect width="880" height="440" rx="14" fill="url(#bg165)"/>
  <rect x="2" y="2" width="876" height="436" rx="12" fill="none" stroke="#334155" stroke-width="1.5"/>

  <!-- Header -->
  <text x="440" y="36" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="16" font-weight="700" text-anchor="middle">ANATOMY OF A VALID ISLAMIC LOAN CONTRACT (AQAD AL-DAYN)</text>
  <text x="440" y="56" fill="#94a3b8" font-family="system-ui, sans-serif" font-size="12" text-anchor="middle">Contractual Blueprint Derived Directly from the Longest Verse of the Holy Qur'an (2:282)</text>

  <!-- Certificate Box -->
  <g transform="translate(60, 75)">
    <rect width="760" height="310" rx="10" fill="#1e293b" stroke="#fbbf24" stroke-width="1.5"/>
    <rect x="6" y="6" width="748" height="298" rx="8" fill="none" stroke="#475569" stroke-width="1" stroke-dasharray="4 3"/>

    <!-- Document Title -->
    <rect x="220" y="14" width="320" height="30" rx="6" fill="#78350f" stroke="#fbbf24" stroke-width="1"/>
    <text x="380" y="34" fill="#fef08a" font-family="system-ui, sans-serif" font-size="13" font-weight="700" text-anchor="middle">DEED OF ETHICAL LOAN (QARD HASAN)</text>

    <!-- Field 1 & 2: Parties -->
    <rect x="25" y="56" width="345" height="46" rx="6" fill="#0f172a" stroke="#334155" stroke-width="1"/>
    <text x="35" y="74" fill="#94a3b8" font-family="system-ui, sans-serif" font-size="10">CREDITOR / LENDER (DA'IN)</text>
    <text x="35" y="93" fill="#f8fafc" font-family="system-ui, sans-serif" font-size="12" font-weight="600">Yusuf Ibrahim (Full Legal Capacity &amp; Consent)</text>

    <rect x="390" y="56" width="345" height="46" rx="6" fill="#0f172a" stroke="#334155" stroke-width="1"/>
    <text x="400" y="74" fill="#94a3b8" font-family="system-ui, sans-serif" font-size="10">DEBTOR / BORROWER (MADIN)</text>
    <text x="400" y="93" fill="#f8fafc" font-family="system-ui, sans-serif" font-size="12" font-weight="600">Amina Hussein (Dictates Terms Freely)</text>

    <!-- Field 3 & 4: Principal & Repayment Date -->
    <rect x="25" y="112" width="345" height="46" rx="6" fill="#0f172a" stroke="#334155" stroke-width="1"/>
    <text x="35" y="130" fill="#94a3b8" font-family="system-ui, sans-serif" font-size="10">PRINCIPAL SUM (MAL AL-DAYN)</text>
    <text x="35" y="149" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="12" font-weight="700">KES 1,500 (One Thousand Five Hundred Shillings)</text>

    <rect x="390" y="112" width="345" height="46" rx="6" fill="#0f172a" stroke="#334155" stroke-width="1"/>
    <text x="400" y="130" fill="#94a3b8" font-family="system-ui, sans-serif" font-size="10">MATURITY DATE (AJAL AL-DAYN)</text>
    <text x="400" y="149" fill="#34d399" font-family="system-ui, sans-serif" font-size="12" font-weight="700">December 15, 2026 (Unambiguous Term)</text>

    <!-- Special Clause: Riba Free -->
    <rect x="25" y="168" width="710" height="44" rx="6" fill="#0f172a" stroke="#10b981" stroke-width="1.5"/>
    <text x="380" y="186" fill="#34d399" font-family="system-ui, sans-serif" font-size="11" font-weight="700" text-anchor="middle">MANDATORY SHARIAH CLAUSE: ZERO USURY (RIBA)</text>
    <text x="380" y="202" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10.5" text-anchor="middle">"This loan is strictly interest-free for the sake of Allah. No gifts, fees, or extra financial benefit may be attached."</text>

    <!-- Signatures & Witnesses -->
    <g transform="translate(25, 222)">
      <rect width="345" height="74" rx="6" fill="#0f172a" stroke="#334155" stroke-width="1"/>
      <text x="172" y="20" fill="#94a3b8" font-family="system-ui, sans-serif" font-size="10" text-anchor="middle">CONTRACTING PARTIES' SIGNATURES</text>
      <line x1="20" y1="52" x2="160" y2="52" stroke="#64748b" stroke-width="1"/>
      <text x="90" y="66" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10" text-anchor="middle">Lender Signature</text>
      <line x1="185" y1="52" x2="325" y2="52" stroke="#64748b" stroke-width="1"/>
      <text x="255" y="66" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10" text-anchor="middle">Borrower Signature</text>
    </g>

    <g transform="translate(390, 222)">
      <rect width="345" height="74" rx="6" fill="#0f172a" stroke="#334155" stroke-width="1"/>
      <text x="172" y="20" fill="#94a3b8" font-family="system-ui, sans-serif" font-size="10" text-anchor="middle">TWO TRUSTWORTHY WITNESSES (SHAHIDAN)</text>
      <line x1="20" y1="52" x2="160" y2="52" stroke="#64748b" stroke-width="1"/>
      <text x="90" y="66" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10" text-anchor="middle">Witness 1: Mr. Bilal (Teacher)</text>
      <line x1="185" y1="52" x2="325" y2="52" stroke="#64748b" stroke-width="1"/>
      <text x="255" y="66" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10" text-anchor="middle">Witness 2: Zainab (Rep)</text>
    </g>
  </g>

  <!-- Footer Banner -->
  <text x="440" y="415" fill="#fbbf24" font-family="system-ui, sans-serif" font-size="12" font-weight="600" text-anchor="middle">"And let a scribe write it between you in justice..." — Surah Al-Baqarah 2:282</text>
</svg>"""


def get_svg_lesson_6():
    """Lesson 6.5.6: Master Architecture of Islamic Economics & Trade"""
    return """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 880 440" width="100%" height="100%">
  <defs>
    <linearGradient id="bg166" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#0f172a"/>
      <stop offset="50%" stop-color="#1e293b"/>
      <stop offset="100%" stop-color="#0f172a"/>
    </linearGradient>
    <linearGradient id="roofGrad" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#0284c7"/>
      <stop offset="50%" stop-color="#38bdf8"/>
      <stop offset="100%" stop-color="#0284c7"/>
    </linearGradient>
  </defs>

  <rect width="880" height="440" rx="14" fill="url(#bg166)"/>
  <rect x="2" y="2" width="876" height="436" rx="12" fill="none" stroke="#334155" stroke-width="1.5"/>

  <!-- Header -->
  <text x="440" y="34" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="16" font-weight="700" text-anchor="middle">MASTER ARCHITECTURE: THE ISLAMIC ECONOMIC SANCTUARY</text>
  <text x="440" y="52" fill="#94a3b8" font-family="system-ui, sans-serif" font-size="11.5" text-anchor="middle">Synthesizing Muamalat: Divine Accountability, Transparent Commerce &amp; Social Cohesion</text>

  <!-- Roof: Social Harmony & Prosperity -->
  <polygon points="120,110 440,65 760,110" fill="url(#roofGrad)" stroke="#38bdf8" stroke-width="1.5"/>
  <text x="440" y="98" fill="#0f172a" font-family="system-ui, sans-serif" font-size="13" font-weight="800" text-anchor="middle">COMMUNAL PROSPERITY, EQUITY &amp; DIVINE BARAKAH</text>

  <!-- 4 Pillars -->
  <!-- Pillar 1 -->
  <g transform="translate(130, 115)">
    <rect width="140" height="205" rx="6" fill="#1e293b" stroke="#10b981" stroke-width="1.5"/>
    <rect width="140" height="32" rx="6" fill="#065f46"/>
    <text x="70" y="21" fill="#ffffff" font-family="system-ui, sans-serif" font-size="11" font-weight="700" text-anchor="middle">ETHICAL FINANCE</text>
    <text x="12" y="54" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10.5">
      <tspan x="12" dy="0">• Wealth is Amanah</tspan>
      <tspan x="12" dy="18">• Halal earning only</tspan>
      <tspan x="12" dy="18">• Strict Riba ban</tspan>
      <tspan x="12" dy="18">• Zakat circulation</tspan>
      <tspan x="12" dy="18">• Risk sharing</tspan>
      <tspan x="12" dy="18">• No gambling</tspan>
      <tspan x="12" dy="18">• Pure sustenance</tspan>
    </text>
  </g>

  <!-- Pillar 2 -->
  <g transform="translate(285, 115)">
    <rect width="140" height="205" rx="6" fill="#1e293b" stroke="#a855f7" stroke-width="1.5"/>
    <rect width="140" height="32" rx="6" fill="#6b21a8"/>
    <text x="70" y="21" fill="#ffffff" font-family="system-ui, sans-serif" font-size="11" font-weight="700" text-anchor="middle">BORROWING RULES</text>
    <text x="12" y="54" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10.5">
      <tspan x="12" dy="0">• Genuine need only</tspan>
      <tspan x="12" dy="18">• Written contract</tspan>
      <tspan x="12" dy="18">• Sincere intention</tspan>
      <tspan x="12" dy="18">• Prompt payment</tspan>
      <tspan x="12" dy="18">• Prioritize debt</tspan>
      <tspan x="12" dy="18">• Clear witnesses</tspan>
      <tspan x="12" dy="18">• Avoid Zulm</tspan>
    </text>
  </g>

  <!-- Pillar 3 -->
  <g transform="translate(440, 115)">
    <rect width="140" height="205" rx="6" fill="#1e293b" stroke="#f59e0b" stroke-width="1.5"/>
    <rect width="140" height="32" rx="6" fill="#b45309"/>
    <text x="70" y="21" fill="#ffffff" font-family="system-ui, sans-serif" font-size="11" font-weight="700" text-anchor="middle">LENDING MERCY</text>
    <text x="12" y="54" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10.5">
      <tspan x="12" dy="0">• Qard Hasan</tspan>
      <tspan x="12" dy="18">• Zero interest</tspan>
      <tspan x="12" dy="18">• Patience in delay</tspan>
      <tspan x="12" dy="18">• Inzar respite</tspan>
      <tspan x="12" dy="18">• Forgive as Sadaqah</tspan>
      <tspan x="12" dy="18">• 18-fold reward</tspan>
      <tspan x="12" dy="18">• Solves hardship</tspan>
    </text>
  </g>

  <!-- Pillar 4 -->
  <g transform="translate(595, 115)">
    <rect width="140" height="205" rx="6" fill="#1e293b" stroke="#38bdf8" stroke-width="1.5"/>
    <rect width="140" height="32" rx="6" fill="#0369a1"/>
    <text x="70" y="21" fill="#ffffff" font-family="system-ui, sans-serif" font-size="11" font-weight="700" text-anchor="middle">CONSUMER SHIELD</text>
    <text x="12" y="54" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10.5">
      <tspan x="12" dy="0">• Reveal defects</tspan>
      <tspan x="12" dy="18">• Khiyar al-Ayb refund</tspan>
      <tspan x="12" dy="18">• No hoarding</tspan>
      <tspan x="12" dy="18">• Accurate scales</tspan>
      <tspan x="12" dy="18">• KEBS safety</tspan>
      <tspan x="12" dy="18">• CAK redress</tspan>
      <tspan x="12" dy="18">• Anti-deception</tspan>
    </text>
  </g>

  <!-- Foundation: Iman, Taqwa & Akhlaq -->
  <rect x="110" y="325" width="660" height="50" rx="8" fill="#1e293b" stroke="#e2e8f0" stroke-width="2"/>
  <text x="440" y="347" fill="#f8fafc" font-family="system-ui, sans-serif" font-size="13" font-weight="700" text-anchor="middle">FOUNDATION: IMAN, TAQWA &amp; SACRED TRUST (AMANAH)</text>
  <text x="440" y="365" fill="#94a3b8" font-family="system-ui, sans-serif" font-size="11" text-anchor="middle">Every Shilling Earned, Spent or Lent is Accountable Before Allah on the Day of Judgment</text>

  <!-- Footer -->
  <rect x="80" y="388" width="720" height="28" rx="6" fill="#0f172a" stroke="#334155" stroke-width="1"/>
  <text x="440" y="407" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="11.5" font-weight="600" text-anchor="middle">"O you who have believed, fulfill your contracts." — Surah Al-Ma'idah 5:1</text>
</svg>"""


# ─────────────────────────────────────────────────────────────────────────────
# LESSON DATA SPECIFICATION (6 Lessons, 7 Cards Each)
# ─────────────────────────────────────────────────────────────────────────────

TOPIC_16_LESSONS = [
    {
        "unit_order": 1,
        "lesson_title": "Ethical finance",
        "inquiry": "Why does Islam regulate financial transactions, and what makes wealth 'ethical'?",
        "hook": "Imagine playing a game of Monopoly where one player is allowed to make up their own rules, steal money from the bank, and charge double rent to players who land on their properties. The game would quickly become frustrating, unfair, and make everyone angry. In real life, money is a powerful tool, but without fair rules, it can lead to greed, cheating, and the rich exploiting the poor. In this lesson, we will explore why Islam has established strict ethical rules for trade and finance to ensure fairness, equity, and peace in society.",
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/6/65/Dinar_Al-Mu%27izz_Cairo_358AH.jpg/800px-Dinar_Al-Mu%27izz_Cairo_358AH.jpg",
        "image_title": "Historical Islamic Currency: Gold Dinar",
        "image_caption": "Historic Islamic gold dinar coin symbolizing tangible, asset-backed wealth and the preservation of real economic value in Islamic trade.",
        "concept_name": "The Three Pillars of Islamic Ethical Wealth",
        "concept_explanation": "In Islam, wealth is not absolute personal property to be hoarded or exploited at will; it is an Amanah (sacred trust) from Allah (S.W.T.) that must be earned through lawful (Halal) means and spent constructively. Islamic jurisprudence strictly bans Usury (Riba)—the practice of charging interest—and instead fosters asset-backed commerce, transparent partnerships (Mudarabah), and mandatory wealth redistribution (Zakat) to protect the vulnerable from economic subjugation.",
        "scripture_quran": "Those who consume interest cannot stand [on the Day of Judgment] except as one stands who is being beaten by Satan into insanity. That is because they say, 'Trade is just like interest.' But Allah has permitted trade and has forbidden interest...",
        "scripture_quran_ref": "Surah Al-Baqarah 2:275",
        "scripture_hadith": "Indeed, Allah is pure and He accepts only that which is pure...",
        "scripture_hadith_ref": "Sahih Muslim 1015",
        "deep_explanation": "The Islamic financial paradigm rests upon three structural realities:\n1. Sanctity of Property & Effort: Every person has an inviolable right to private property earned through productive labor, skill, or legitimate trade, while gaining money through bribery, theft, or gambling is strictly forbidden.\n2. Risk-and-Profit Sharing: Unlike conventional systems where lenders shift all market risk onto debtors through fixed interest rates, Islam promotes equity partnerships where capital owners and entrepreneurs share actual market risks and profits.\n3. Socio-Economic Circulation: Wealth must circulate dynamically to alleviate poverty through Zakat and charitable endowments (Waqf), ensuring that national assets do not concentrate solely within an elite minority.",
        "diagram_title": "The Three Pillars of Islamic Ethical Finance",
        "svg_func": get_svg_lesson_1,
        "table_title": "Conventional Interest-Based Finance vs. Islamic Ethical Finance",
        "table_headers": ["Feature", "Conventional Financial System", "Islamic Financial System (Shariah)"],
        "table_rows": [
            ["Earning Method", "Allows interest (Riba), speculation, and high-risk derivatives", "Strictly asset-backed, Halal goods, and productive trade"],
            ["Risk Allocation", "Debtor absorbs risk; lender receives guaranteed interest", "Symmetrical risk-sharing (Mudarabah / Musharakah)"],
            ["Handling Hardship", "Imposes compounding penalties and foreclosure on defaulting debtors", "Mandates payment extensions (Inzar) or debt forgiveness (Sadaqah)"],
            ["Social Purpose", "Maximizing individual shareholder profit regardless of social harm", "Promoting public welfare (Maslahah) and preventing wealth hoarding"]
        ],
        "scenario": "Yusuf and his friend Amina decide to start a small enterprise selling handmade keychains at their school's entrepreneurship exhibition. Yusuf has the funds to purchase raw materials, while Amina possesses the artistic talent to design them. Yusuf proposes: 'I will lend you the cash, but you must repay me the capital plus a guaranteed 20% interest regardless of our sales.' Amina counters: 'That is Riba, Yusuf. If the keychains do not sell, I fall into debt while you risk nothing. Instead, let us enter a Mudarabah partnership: you supply capital, I contribute labor, and we split net profits equally. If we experience a loss, you lose financial capital, and I lose my time and craftsmanship.' Yusuf immediately agrees, recognizing this as the just, Islamic pathway.",
        "real_world": "Adopt the 'Ethical Earner' code in your personal life. When selling items, washing cars, or doing part-time chores, ensure complete honesty. Never conceal defects, never exaggerate item quality, and never shortchange customers on measurements. Earning even a modest amount through lawful, honest effort infuses divine Barakah (blessings) into your sustenance.",
        "reflection": "How does the prohibition of interest protect economically vulnerable families from predatory debt cycles? Why must we view wealth as a temporary trust from the Creator rather than absolute personal entitlement?",
        "misconception": "Misconception: Believing that because trade and interest both generate profit, they are identical. The Qur'an explicitly debunks this fallacy: trade involves mutual exchange and real business risk, whereas interest guarantees risk-free profit for the creditor while exploiting the borrower's distress.",
        "yt_id": "cQ8zT2H2_dY",
        "yt_title": "Introduction to Islamic Ethical Finance & Economics",
        "yt_desc": "Overview of how Islamic finance eliminates exploitation, bans usury, and fosters shared community prosperity.",
        "mcq": {
            "question": "Which of the following statements correctly distinguishes trade from interest (Riba) according to Islamic economic principles?",
            "options": [
                "A. Trade involves exchanging goods and sharing commercial risks, whereas interest guarantees profit for the lender without bearing risk.",
                "B. Trade is prohibited in Islam, while interest is highly recommended.",
                "C. Interest deals only with physical commodities, while trade only uses digital money.",
                "D. Both are legally identical under Shariah jurisprudence."
            ],
            "answer": "A",
            "explanation": "Trade involves legitimate commerce with symmetrical exposure to potential profit and loss, which is lawful (Halal). Interest (Riba) guarantees risk-free monetary expansion for the lender at the sole expense of the borrower, making it exploitative and strictly forbidden (Haram)."
        },
        "summary_content": "Islamic finance governs wealth as an Amanah from Allah, strictly outlawing Riba (usury/interest) to prevent economic exploitation. It mandates that wealth be generated through Halal trade, equitable risk-sharing partnerships, and dynamic community circulation via Zakat.",
        "key_points": [
            "Wealth is a sacred trust (Amanah) requiring lawful (Halal) earning and ethical spending.",
            "Riba (interest/usury) is strictly prohibited as an exploitative and unjust practice.",
            "Islamic economics prioritizes risk-sharing partnerships (Mudarabah) over debt servitude.",
            "Wealth must actively circulate to protect the vulnerable rather than being hoarded by elites."
        ],
        "exit_ticket": "State one reason why a profit-and-loss sharing partnership is ethically superior to an interest-based loan."
    },
    {
        "unit_order": 2,
        "lesson_title": "Rules of borrowing",
        "inquiry": "What are the spiritual and legal obligations of a borrower in Islam?",
        "hook": "Imagine you borrow your classmate's favorite fountain pen for an important exam, promising to return it by the end of the day. After the exam, you get distracted, put the pen in your pocket, go home, and lose it. When your classmate asks for it the next morning, you shrug and say, 'It's just a cheap pen, don't worry about it.' Your classmate feels betrayed and hurt. In Islam, borrowing is a solemn legal and moral covenant. Whether you borrow a simple pen or a substantial sum of money, you are fully accountable before Allah to fulfill your agreement.",
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/8/87/Folio_from_the_Blue_Qur%27an_%28Surah_2_verses_120-124%29.jpg/800px-Folio_from_the_Blue_Qur%27an_%28Surah_2_verses_120-124%29.jpg",
        "image_title": "Ayat al-Dayn: Classical Manuscript Heritage",
        "image_caption": "Historic Quranic manuscript tradition preserving Surah Al-Baqarah, which contains the foundational Ayat al-Dayn on debt documentation.",
        "concept_name": "The Sanctity of Debt (Dayn) and the Borrower's Covenant",
        "concept_explanation": "Borrowing in Islam is a concession permitted solely under genuine necessity, never for vanity or luxury. Under Islamic law, contracting a debt creates an unbreakable legal covenant that demands meticulous written documentation, witness verification, sincere intent to pay, and prompt repayment on the agreed date.",
        "scripture_quran": "O you who have believed, when you contract a debt for a specified term, write it down. Let a scribe write it between you in justice...",
        "scripture_quran_ref": "Surah Al-Baqarah 2:282",
        "scripture_hadith": "Procrastination (delaying payment) by a wealthy debtor is an injustice...",
        "scripture_hadith_ref": "Sahih al-Bukhari 2287",
        "deep_explanation": "The jurisprudence of borrowing incorporates four fundamental pillars:\n1. Ayat al-Dayn Mandate: The longest single verse in the entire Qur'an (2:282) mandates that credit agreements be formally recorded in writing with exact repayment timelines and witnessed by two trustworthy individuals.\n2. Spiritual Intent (Niyyah): The Prophet (PBUH) affirmed that whoever takes people's money with sincere intention to repay, Allah will facilitate repayment; but whoever takes it with intention to squander, Allah will bring about their ruin.\n3. Absolute Priority of Debt Settlement: When a Muslim passes away, their outstanding debts must be fully liquidated from their estate before any inheritance can be distributed or voluntary bequests honored.",
        "diagram_title": "The Islamic Borrower's Protocol Checklist",
        "svg_func": get_svg_lesson_2,
        "table_title": "The Borrower's Ethical Code: Right Actions vs Injustices",
        "table_headers": ["Stage of Borrowing", "Ethical Conduct (Sunnah & Fiqh)", "Prohibited Injustice (Zulm)"],
        "table_rows": [
            ["Initiation", "Borrowing solely for real emergencies or essential needs", "Borrowing for status symbols, luxury parties, or gambling"],
            ["Contracting", "Insisting on a detailed written agreement with two witnesses", "Relying on vague oral promises or hiding terms"],
            ["During Debt", "Living frugally and budgeting strictly to save for repayment", "Spending carelessly while ignoring debt obligations"],
            ["Maturity Date", "Paying immediately or communicating proactively if in hardship", "Procrastinating, hiding, or dodging creditor calls (Zulm)"]
        ],
        "scenario": "Hussein requires 1,500 Kenyan Shillings to acquire prescribed reference textbooks for his Grade 9 national examinations. Having no personal savings, he approaches his older cousin Ali. Following Islamic borrowing etiquette, they draft a clear written covenant: 'Hussein borrows 1,500 KES from Ali on September 6, 2026, to be repaid in full by December 6, 2026.' Both parties sign the agreement, and Hussein's elder brother signs as an independent witness. Hussein saves 500 KES each month from his allowance. On November 30—a week ahead of schedule—Hussein settles the debt in full with sincere gratitude.",
        "real_world": "Perform an immediate personal debt audit. If you have borrowed a textbook, sports kit, bicycle, or pocket money from a friend, formulate an actionable plan to return it promptly. If facing genuine financial hardship, approach the lender honestly and negotiate a realistic, formal extension rather than avoiding them.",
        "reflection": "Why does delaying debt repayment when one possesses the money constitute an act of tyranny (Zulm)? How does writing down agreements protect long-term friendships from destructive disputes?",
        "misconception": "Misconception: Thinking that small personal loans among close friends or relatives do not need to be documented. The Qur'an commands documentation regardless of whether the loan is small or large, explicitly to prevent forgetfulness, doubts, and suspicion.",
        "yt_id": "r1vJ9R2Q8Y0",
        "yt_title": "Islamic Rules and Etiquette of Borrowing and Debts",
        "yt_desc": "Detailed analysis of Ayat al-Dayn and the grave spiritual accountability associated with unpaid debts.",
        "mcq": {
            "question": "According to the Quranic mandate in Ayat al-Dayn (Surah Al-Baqarah 2:282), what is the primary obligation when entering into a debt contract?",
            "options": [
                "A. To keep the financial transaction completely secret from relatives.",
                "B. To formally document the agreement in writing in the presence of witnesses.",
                "C. To attach a guaranteed interest markup to ensure prompt repayment.",
                "D. To only borrow from foreign institutions, never from community members."
            ],
            "answer": "B",
            "explanation": "Surah Al-Baqarah 2:282 strictly instructs believers to record all credit agreements in writing and secure two reliable witnesses to guarantee clarity, prevent conflict, and uphold social justice."
        },
        "summary_content": "Borrowing is a serious financial and moral responsibility reserved for genuine necessities. Shariah mandates thorough written documentation with witnesses, sincere intent to settle debts, and immediate repayment without unjust procrastination.",
        "key_points": [
            "Borrowing should only occur for genuine needs, not conspicuous consumerism.",
            "Surah Al-Baqarah 2:282 commands writing down debts with clear timelines and witnesses.",
            "Sincere intention to repay unlocks divine assistance; intending fraud leads to ruin.",
            "Delaying debt payment when having financial capacity is categorized as injustice (Zulm)."
        ],
        "exit_ticket": "Explain why the Prophet (PBUH) characterized the delay of debt repayment by an able debtor as an act of injustice."
    },
    {
        "unit_order": 3,
        "lesson_title": "Rules of lending",
        "inquiry": "How does Islam encourage lending as an act of charity, and what are the duties of a lender?",
        "hook": "Imagine you see a classmate sitting alone and hungry during lunchtime because they forgot their meal voucher. You have extra pocket money. You could say: 'I will lend you 50 shillings for lunch, but tomorrow you must buy me a 100-shilling snack as interest.' Or you could say: 'Take 50 shillings, pay me back whenever your parents send your allowance, and if you cannot, don't worry about it.' The first option is predatory exploitation; the second is a sublime act of mercy. In Islam, lending to someone in need is not a commercial enterprise to extract profit—it is a beloved act of worship.",
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/c/c2/Al-Baqara_282.jpg/800px-Al-Baqara_282.jpg",
        "image_title": "Ayat al-Dayn Calligraphic Panel",
        "image_caption": "Calligraphic illumination of Surah Al-Baqarah verse 280, commanding patience, compassion, and debt relief for struggling debtors.",
        "concept_name": "Qard Hasan: The Sanctuary of Interest-Free Lending",
        "concept_explanation": "Islamic jurisprudence establishes Qard Hasan (the beautiful loan) as an interest-free loan extended exclusively to relieve human distress for the pleasure of Allah. Shariah commands lenders to practice absolute empathy, strictly forbidding the extraction of gifts or services, and requiring lenders to extend deadlines or forgive debts when borrowers encounter severe hardship.",
        "scripture_quran": "If someone is in difficulty, then let there be a delay until a time of ease. But if you give [it] as charity, that is better for you if you only knew.",
        "scripture_quran_ref": "Surah Al-Baqarah 2:280",
        "scripture_hadith": "Whoever helps a debtor in difficulty, Allah will make it easy for him in this world and the Hereafter...",
        "scripture_hadith_ref": "Sahih Muslim 2699",
        "deep_explanation": "The jurisprudence of Islamic lending is structured around three ethical cornerstones:\n1. Absolute Ban on Benefit-Extraction: Lenders are forbidden from demanding or accepting any unilateral gifts, favors, or financial additions connected to a loan. The legal maxim states: 'Every loan that draws a conditional benefit is a form of Riba.'\n2. Mandatory Respite (Inzar): If a debtor encounters genuine insolvency, the lender is legally and spiritually bound to extend the maturity term without attaching late payment fines or penalties.\n3. The Supreme Virtue of Debt Remission: Converting unpayable debt into voluntary charity (Sadaqah) earns unmatched divine honor. The Prophet (PBUH) taught that whoever relieves a distressed debtor will be sheltered beneath Allah's throne on the Day of Judgment.",
        "diagram_title": "Conventional Usury vs Islamic Qard Hasan",
        "svg_func": get_svg_lesson_3,
        "table_title": "The Ethical Lender's Code: Islamic Virtues vs Un-Islamic Practices",
        "table_headers": ["Dimension", "Islamic Ethical Lending (Qard Hasan)", "Un-Islamic / Usurious Lending"],
        "table_rows": [
            ["Profit Motive", "Zero financial gain; seeks divine reward and community welfare", "Extracts maximum interest profit from the borrower's plight"],
            ["Additional Benefits", "Lender rejects gifts, favors, or conditional markups", "Demands processing fees, compounding interest, and gifts"],
            ["Debtor in Crisis", "Mandatory deadline extension (Inzar) without extra cost", "Imposes heavy penal interest and aggressive repossession"],
            ["Final Recourse", "Encouraged to forgive part or all of the debt as Sadaqah", "Enforces civil imprisonment and bankruptcy auctions"]
        ],
        "scenario": "Zainab lends her neighbor Halima 2,000 Kenyan Shillings to purchase emergency prescription medicine for her sick daughter, agreeing to a one-month repayment window. At month's end, Halima approaches Zainab in tears, explaining that her tailoring machine broke down and she has had zero income. Zainab recalls Surah Al-Baqarah (2:280). She consoles Halima: 'Do not grieve, my sister. I grant you another two months to repair your machine and pay when comfortable. If difficulties persist, consider half the amount a gift for Allah's sake.' Halima feels immense relief and prays for Zainab's household.",
        "real_world": "Exercise forbearance when lending personal property to peers or siblings. If a friend accidentally damages or misplaces a borrowed item and shows genuine remorse, choose patience and gracious pardon rather than rage. Practicing compassion in small matters nurtures a resilient, peaceful school community.",
        "reflection": "Why does Allah reward extending time to an insolvent debtor with greater spiritual merit than ordinary charity? How would our national economy change if interest-free microloans replaced predatory digital lending apps?",
        "misconception": "Misconception: Believing that a lender is weak or losing money when granting payment extensions. The Prophet (PBUH) clarified that for every day a creditor grants respite to a struggling debtor, they are credited with the spiritual reward of giving that entire sum as daily charity.",
        "yt_id": "V2fD1hY-3wE",
        "yt_title": "The Virtues of Qard Hasan and Forgiving Debts in Islam",
        "yt_desc": "Spiritual and communal benefits of interest-free lending and treating insolvent debtors with mercy.",
        "mcq": {
            "question": "What is an Islamic creditor commanded to do under Surah Al-Baqarah (2:280) when a debtor faces extreme financial destitution at the maturity date?",
            "options": [
                "A. Confiscate the debtor's personal household belongings by force.",
                "B. Double the loan repayment amount as a punitive deterrent.",
                "C. Grant a payment extension until a time of ease, or forgive the debt as charity.",
                "D. Publicly humiliate the debtor before community leaders."
            ],
            "answer": "C",
            "explanation": "Surah Al-Baqarah 2:280 explicitly mandates granting delay until a time of ease, further noting that forgiving the debt entirely as charity yields immense divine reward."
        },
        "summary_content": "Lending in Islam is an act of high worship governed by Qard Hasan (interest-free loans). Shariah strictly forbids deriving any personal profit from loans, mandating patience, extension of deadlines for insolvent debtors, and voluntary debt forgiveness as an act of supreme charity.",
        "key_points": [
            "Qard Hasan is an interest-free loan extended solely for the sake of Allah's pleasure.",
            "Lenders cannot demand gifts, interest, or favors from the borrower.",
            "Surah Al-Baqarah 2:280 commands granting respite (Inzar) to insolvent debtors.",
            "Forgiving a debt for a person in severe hardship earns divine shade on the Day of Judgment."
        ],
        "exit_ticket": "State two spiritual rewards promised to a creditor who shows patience and grants respite to an impoverished debtor."
    },
    {
        "unit_order": 4,
        "lesson_title": "Consumer rights and protection",
        "inquiry": "How does Islam protect consumers from exploitation, and what is the role of consumer protection agencies?",
        "hook": "Imagine you save your pocket money for months to buy a brand-new scientific calculator for your mathematics lessons. When you open the package at home, the display is cracked and key function buttons fail to register. You return to the retail shop, but the vendor laughs and gestures to a sign: 'Goods once sold cannot be returned or refunded.' You feel cheated, outraged, and powerless. In this lesson, we will examine how Islamic jurisprudence established robust consumer protection over 1,400 years ago, and how modern statutory bodies like KEBS and CAK enforce these identical rights in Kenya today.",
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/e/e5/Scales_of_Justice.svg/800px-Scales_of_Justice.svg.png",
        "image_title": "Scales of Commercial Justice",
        "image_caption": "The scales of balance symbolizing truthful measurement, honest disclosure, and fair market pricing commanded in Islamic law.",
        "concept_name": "Khiyar al-Ayb & the Consumer Protection Mandate",
        "concept_explanation": "Islamic commercial law protects buyers through statutory rights of inspection and cancellation, particularly Khiyar al-Ayb (the right of return due to hidden defects). Shariah strictly outlaws commercial fraud (Tadlis), counterfeit goods, hoarding (Ihtikar), and misleading claims, while aligning seamlessly with statutory bodies like the Kenya Bureau of Standards (KEBS) and Competition Authority of Kenya (CAK).",
        "scripture_quran": "O you who have believed, do not consume one another's wealth unjustly but only [in lawful] business by mutual consent...",
        "scripture_quran_ref": "Surah An-Nisa 4:29",
        "scripture_hadith": "The Prophet (PBUH) passed by a pile of grain. He inserted his hand into it and his fingers felt dampness. He asked: 'What is this, O seller of food?' The man replied: 'It was caught by the rain, O Messenger of Allah.' The Prophet said: 'Why did you not place it on top so that people could see it? Whoever deceives us is not one of us.'",
        "scripture_hadith_ref": "Sahih Muslim 102",
        "deep_explanation": "Islamic consumer protection functions across four foundational quadrants:\n1. Absolute Transparency (Nasiha): Vendors must disclose every known physical or operational defect before accepting payment. Concealing damp grain, expired dates, or damaged parts is categorized as theft.\n2. Right of Repudiation (Khiyar): When a consumer discovers an undisclosed flaw, Shariah guarantees them the irrevocable legal option to return the merchandise for a 100% refund or accept a price adjustment.\n3. Prohibition of Market Manipulation: Practices such as hoarding essential foodstuffs (Ihtikar) to drive up prices during shortages, collusive price-fixing, and false bidding (Najash) are cursed.\n4. Modern Civic Synergy: In Kenya, the Competition Authority of Kenya (CAK) and KEBS protect citizens from defective products and predatory trade, giving modern institutional teeth to Islamic consumer rights.",
        "diagram_title": "Consumer Rights Shield & Fair Marketplace Principles",
        "svg_func": get_svg_lesson_4,
        "table_title": "Consumer Protection Rights: Islamic Jurisprudence vs Modern Kenyan Law",
        "table_headers": ["Consumer Right", "Islamic Shariah Jurisprudence (Fiqh)", "Modern Kenyan Legal Framework"],
        "table_rows": [
            ["Full Information", "Mandatory disclosure of flaws; Hadith on wet food", "CAK rules on truthful product labeling and advertising"],
            ["Safety & Standards", "Tayyib standard; prohibition of harmful/toxic goods", "KEBS Standardization Mark of Quality and safety checks"],
            ["Right of Return", "Khiyar al-Ayb grants automatic refund for hidden defects", "Consumer Protection Act 2012 warranties and refund rights"],
            ["Fair Competition", "Strict ban on hoarding (Ihtikar) and fake bidding (Najash)", "Competition Act provisions against monopolies and price-fixing"]
        ],
        "scenario": "Ali purchases a second-hand bicycle from an urban marketplace. The shopkeeper assures him: 'This bicycle is in flawless mechanical condition, lightly ridden.' Ten minutes into his ride home, the brake cables snap completely, nearly causing a severe traffic collision. Inspecting the bicycle, Ali finds the cables were corroded and patched with cheap black electrical tape. Ali returns to the shop. When the seller points to a 'No Returns' notice, Ali politely asserts: 'In Islamic law, concealing a perilous defect is deceit (Ghash), which invalidates the sale. Under the Kenyan Consumer Protection Act, I am entitled to a safe product and an immediate refund.' Recognizing his moral and legal liability, the shopkeeper apologizes, refunds the full amount, and replaces the braking assembly.",
        "real_world": "Practice vigilant and responsible consumption. Always inspect manufactured food and personal items for the KEBS mark of quality and valid expiration dates. When buying second-hand electronics or study materials, examine them carefully. If sold a defective item, calmly demand a repair or refund, and report persistent fraudulent vendors to school administrators or consumer protection desks.",
        "reflection": "Why does Islamic law declare that 'Whoever deceives us is not one of us'? How does commercial honesty foster economic growth and foreign investment in Kenya?",
        "misconception": "Misconception: Believing that 'Buyer Beware' (Caveat Emptor) relieves a vendor of moral guilt if a customer fails to detect a flaw. In Islam, the primary burden of disclosure rests entirely upon the seller; intentionally staying silent about a defect is an act of deceit and unlawful consumption.",
        "yt_id": "8r6hX_W9qKM",
        "yt_title": "Consumer Protection & Fair Trade in Islamic Jurisprudence",
        "yt_desc": "Analysis of consumer rights, seller duties of disclosure, and the prohibition of fraud in Islamic marketplaces.",
        "mcq": {
            "question": "When the Prophet Muhammad (PBUH) discovered damp grain hidden beneath dry grain in the marketplace, what legal command did he establish?",
            "options": [
                "A. He purchased all the damp grain to compensate the merchant.",
                "B. He advised the seller to keep it hidden so market prices would not drop.",
                "C. He commanded the seller to put the wet grain on top for all buyers to see, declaring that deceivers are not true believers.",
                "D. He instructed buyers to inspect every single grain before paying."
            ],
            "answer": "C",
            "explanation": "The Prophet (PBUH) insisted on total transparency, commanding that the wet grain be placed in plain view and declaring that anyone who deceives consumers is not part of the righteous community."
        },
        "summary_content": "Islam guarantees comprehensive consumer rights, prohibiting fraud (Tadlis), defect concealment, and hoarding (Ihtikar). The doctrine of Khiyar al-Ayb gives buyers the legal right to full refunds for hidden flaws, harmonizing directly with modern Kenyan consumer protection bodies such as KEBS and CAK.",
        "key_points": [
            "Sellers have a religious duty to disclose all known product defects openly.",
            "Khiyar al-Ayb provides buyers an absolute right to return defective goods for a full refund.",
            "Signs reading 'Goods once sold cannot be returned' cannot legally cover up fraud or deception.",
            "Kenyan agencies like KEBS and CAK uphold the same principles of consumer safety and transparency."
        ],
        "exit_ticket": "Explain why selling a defective product without informing the buyer is considered equivalent to theft in Islamic ethics."
    },
    {
        "unit_order": 5,
        "lesson_title": "Practice: a fair agreement",
        "inquiry": "How do we write a legally and spiritually valid loan agreement under Islamic law?",
        "hook": "Imagine you and your close friend decide to pool funds to register for a school robotics competition. You lend your friend 1,000 shillings for their entry fee, with an informal verbal understanding to repay 'sometime next term.' When next term arrives, you need your money to pay for exam supplies, but your friend claims: 'I thought you said I could repay you at the end of the year!' Misunderstandings, hurt feelings, and fractured friendships occur when financial agreements remain unwritten. In this lesson, we will master the art of drafting a clear, ethical, and legally binding loan contract based on Islamic law.",
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/d/d4/Ottoman_Firmans.jpg/800px-Ottoman_Firmans.jpg",
        "image_title": "Historical Islamic Legal Contracts",
        "image_caption": "Archival Islamic legal agreements demonstrating centuries of rigorous documentation, formal witnessing, and legal clarity in trade.",
        "concept_name": "Kitabah: The Architectural Blueprint of a Debt Agreement",
        "concept_explanation": "Kitabah (contract drafting) is a direct Quranic command from Surah Al-Baqarah (2:282) designed to eliminate ambiguity, preserve social trust, and protect both contracting parties. A valid Islamic loan contract requires precise identification of parties, the exact principal amount, an unambiguous repayment date, a strict zero-interest clause, and verified signatures of two trustworthy witnesses.",
        "scripture_quran": "...And let a scribe write it between you in justice. Let no scribe refuse to write as Allah has taught him. So let him write and let the one who has the obligation dictate...",
        "scripture_quran_ref": "Surah Al-Baqarah 2:282",
        "scripture_hadith": "Muslims are bound by their conditions, except a condition that makes the lawful unlawful or the unlawful lawful.",
        "scripture_hadith_ref": "Sunan at-Tirmidhi 1352",
        "deep_explanation": "Drafting an authentic Islamic debt instrument incorporates five structural components:\n1. The Debtor Dictates: Shariah requires the borrower (who carries the financial obligation) to dictate the agreement's terms, ensuring they act under free will without coercion.\n2. Temporal & Financial Specificity: The contract must record the precise sum and an unmistakable maturity calendar date (e.g., December 15, 2026), rejecting vague phrases like 'soon' or 'after the harvest.'\n3. The Qard Hasan Inscription: The agreement must explicitly prohibit interest, late charges, or gifts, certifying it as an act of pure financial assistance.\n4. Dual Independent Witnesses: Two trustworthy adult witnesses must verify and sign the document, serving as an impartial safeguard in case of future disputes or memory lapses.",
        "diagram_title": "Anatomy of a Valid Islamic Loan Contract",
        "svg_func": get_svg_lesson_5,
        "table_title": "Key Elements of a Standard Shariah-Compliant Loan Agreement",
        "table_headers": ["Clause / Component", "Description & Legal Purpose", "Sample Text in Practice"],
        "table_rows": [
            ["Identification of Parties", "Specifies full legal names and addresses of creditor and debtor", "'Lender: Yusuf Ibrahim | Borrower: Amina Hussein'"],
            ["Principal Amount", "Exact monetary sum spelled out in words and numbers", "'KES 1,500 (One Thousand Five Hundred Kenyan Shillings)'"],
            ["Maturity Date", "Definite calendar date on which the principal falls due", "'Repayment Due Date: December 15, 2026'"],
            ["Zero-Interest Term", "Explicit certification that no Riba or late fees will be assessed", "'This loan is Qard Hasan; zero interest or late fees shall apply'"],
            ["Signatures & Witnesses", "Signatures of lender, borrower, and two impartial witnesses", "'Signed by both parties in presence of Witness 1 & Witness 2'"]
        ],
        "scenario": "Review the following model contract drafted by Junior School students during an IRE practical session:\n\nDEED OF FRIENDLY LOAN (QARD HASAN)\nDate: September 6, 2026\nLender: Yusuf Ibrahim (Grade 9)\nBorrower: Amina Hussein (Grade 9)\nPrincipal: KES 500 (Five Hundred Kenyan Shillings)\nDue Date: November 6, 2026\nTerms: This is an interest-free loan (Qard Hasan) given out of solidarity. No additional interest, penalties, or gifts shall be charged.\nSignatures: Yusuf Ibrahim (Lender) | Amina Hussein (Borrower)\nWitnesses: Mr. Bilal John (IRE Instructor) | Zainab Ali (Class Secretary)\n\nThrough this clear agreement, both students enjoy peace of mind, knowing their rights and duties are protected.",
        "real_world": "Draft a practice loan covenant with your desk partner. Imagine one of you is borrowing a textbook or 200 shillings for a bus fare. Draft a clean agreement incorporating the five essential elements: party names, sum, exact repayment date, zero-interest declaration, and two peer witness signatures. Keep this model in your portfolio as a lifelong reference.",
        "reflection": "Why does the Qur'an instruct that the debtor—not the creditor—dictate the loan terms to the scribe? How does written documentation preserve brotherly love and kinship during commercial deals?",
        "misconception": "Misconception: Assuming that requesting a written contract implies a lack of trust in a friend. In Islam, writing contracts is an act of religious obedience to Allah that protects both parties' honor, eliminates forgetfulness, and prevents shaytan from sowing seeds of doubt.",
        "yt_id": "T0r3N_xY7dU",
        "yt_title": "How to Draft a Halal Written Agreement in Islamic Law",
        "yt_desc": "Practical guide to drafting valid debt agreements, witness requirements, and avoiding ambiguous contract terms.",
        "mcq": {
            "question": "Why does Islamic jurisprudence require that two trustworthy witnesses sign a debt agreement?",
            "options": [
                "A. To allow the witnesses to claim a percentage of the loan as a commission.",
                "B. To provide an independent, verifiable record that resolves misunderstandings and protects both parties.",
                "C. To make the borrower liable to pay interest if the witnesses demand it.",
                "D. To keep the agreement hidden from judicial courts."
            ],
            "answer": "B",
            "explanation": "Trustworthy witnesses provide objective, independent confirmation of the transaction, ensuring that neither party's rights are violated and resolving any potential future disputes."
        },
        "summary_content": "Writing loan contracts (Kitabah) is a sacred command from Surah Al-Baqarah (2:282). A valid agreement must state exact names, principal amount, definitive due date, zero-interest terms, and contain signatures of the parties and two trustworthy witnesses.",
        "key_points": [
            "Contract documentation prevents ambiguity, memory lapses, and social friction.",
            "The borrower must freely dictate the terms of the debt to the recording scribe.",
            "Exact repayment dates and principal amounts must be recorded without vagueness.",
            "Two trustworthy witnesses must verify and sign the loan covenant."
        ],
        "exit_ticket": "List the five essential components that must be present in a valid Islamic debt contract."
    },
    {
        "unit_order": 6,
        "lesson_title": "Unit synthesis",
        "inquiry": "How do we synthesize the Islamic principles of trade, lending, and consumer protection into a unified ethical lifestyle?",
        "hook": "Imagine walking through a bustling urban market in Nairobi. In some alleyways, sellers use altered scales, hide rotten fruit beneath fresh produce, and loan sharks trap poor stall owners in compounding interest. But in other stalls, traders smile warmly, weigh goods with absolute precision, extend generous interest-free credit, and point out minor defects before accepting payment. Which marketplace would you want to live in? In this final synthesis lesson, we unite all strands of ethical finance, borrowing, lending, and consumer rights into a comprehensive blueprint for an ethical economic life.",
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/6/6b/Islamic_Cairo_Market.jpg/800px-Islamic_Cairo_Market.jpg",
        "image_title": "Historic Islamic Marketplace",
        "image_caption": "Centuries of traditional Islamic market architecture where trade, morality, and community cohesion merged into daily life.",
        "concept_name": "The Master Sanctuary of Islamic Economic Muamalat",
        "concept_explanation": "Islamic Muamalat (social and commercial jurisprudence) integrates faith, law, and morality into a cohesive economic sanctuary. By uniting ethical wealth generation, disciplined borrowing, merciful interest-free lending (Qard Hasan), and rigorous consumer protection, Islam ensures that money serves as an engine of universal prosperity and peace rather than greed and exploitation.",
        "scripture_quran": "Indeed, Allah commands you to render trusts to whom they are due and when you judge between people to judge with justice...",
        "scripture_quran_ref": "Surah An-Nisa 4:58",
        "scripture_hadith": "The truthful, trustworthy merchant is with the Prophets, the truthful ones, and the martyrs.",
        "scripture_hadith_ref": "Sunan at-Tirmidhi 1209",
        "deep_explanation": "Synthesizing the unit reveals four interconnected pillars supporting the Islamic economic house:\n1. The Foundation of Amanah: Wealth is a divine trust. Every shilling earned or spent will be audited on Yawm al-Qiyamah, demanding Halal sources and ethical expenditure.\n2. The Pillar of Fair Commerce: Trade is permitted and blessed, while usury (Riba), price manipulation, and deception are outlawed to safeguard public welfare.\n3. The Pillar of Solidarity: Borrowing is disciplined and documented, while lending is transformed into Qard Hasan—mercy-driven financial assistance that extends relief to struggling debtors.\n4. The Consumer Shield: Transparency, quality standards (KEBS), and the doctrine of Khiyar al-Ayb empower buyers and ensure fair competition across the national economy.",
        "diagram_title": "Master Architecture of the Islamic Economic Sanctuary",
        "svg_func": get_svg_lesson_6,
        "table_title": "Master Unit Synthesis Framework: Islamic Commercial Jurisprudence",
        "table_headers": ["Economic Dimension", "Core Islamic Legal Mandate", "Civic & Commercial Practice", "Spiritual & Social Outcome"],
        "table_rows": [
            ["Earning Wealth", "Halal trade; absolute ban on Riba (2:275)", "Asset-backed trade & risk-sharing partnerships", "Economic equity & divine Barakah"],
            ["Borrowing Funds", "Ayat al-Dayn (2:282) written contract & intent", "Clear terms, due dates & two independent witnesses", "Prevention of conflict & preserved trust"],
            ["Lending Capital", "Qard Hasan; respite for insolvent debtors (2:280)", "Zero-interest credit; forgiving debts in hardship", "Social safety net & immense divine rewards"],
            ["Consumer Protection", "Khiyar al-Ayb; disclosure of defects (Sahih Muslim 102)", "Accurate weights, safety marks & refund options", "Marketplace integrity & protected buyers"]
        ],
        "scenario": "Amina operates a school supply cooperative. A shipment of geometry sets arrives with 10% having slightly cracked plastic compasses. Applying the complete synthesis of Islamic trade and consumer ethics, Amina refuses to hide the damaged sets or discard them deceitfully. Instead, she sorts the stock into two clearly marked sections: 'First-Quality Sets (Standard Price)' and 'Discounted Sets: Compass Flawed (Half Price).' She explains the flaws openly to every student buyer. Her classmates praise her honesty, her stock sells out rapidly, and the school administration commends her enterprise as a model of business integrity.",
        "real_world": "Design an 'Ethical Code of Commerce' for your class entrepreneurship project or family business. Draft three golden rules: 1. Absolute transparency in disclosing item flaws, 2. Zero tolerance for usury or hidden fees, and 3. Allocating a fixed percentage of net profits to charitable community initiatives. Display your charter on your school bulletin board.",
        "reflection": "How does conducting trade with impeccable honesty bring peace of mind and divine Barakah to our families? What is the difference between accumulating wealth through cunning deceit versus earning modest profit through truthful labor?",
        "misconception": "Misconception: Assuming that following strict Islamic commercial ethics makes a business less profitable. In reality, ethical businesses build enduring customer loyalty, superior brand trust, and avoid catastrophic legal liabilities, while earning divine Barakah that sustains long-term prosperity.",
        "yt_id": "z9Qp8X7K2vY",
        "yt_title": "Comprehensive Synthesis: Islamic Economics and Trade Ethics",
        "yt_desc": "Unit synthesis reviewing ethical finance, loan drafting, debt relief, and fair consumer protection in Islam.",
        "mcq": {
            "question": "A merchant receives a shipment of rulers where several items have minor manufacturing scratches. Applying the comprehensive synthesis of Islamic trade ethics, what is the correct action for the merchant to take?",
            "options": [
                "A. Pack the scratched rulers beneath perfect items so customers do not notice them before purchasing.",
                "B. Sell the scratched rulers at an honest discount while openly informing customers about the defect before purchase.",
                "C. Falsely claim the rulers were stolen to fraudulently collect insurance compensation.",
                "D. Sell them at full retail price with an aggressive 'No Refund' policy."
            ],
            "answer": "B",
            "explanation": "This demonstrates total transparency, defect disclosure, and fair pricing, embodying the complete synthesis of Islamic consumer protection and honest commerce."
        },
        "summary_content": "Islamic economics synthesizes spiritual integrity and commercial jurisprudence into a unified lifestyle. Wealth is an Amanah; trade must be transparent and interest-free; borrowing requires written documentation; lending demands mercy (Qard Hasan); and consumer rights are guarded by Khiyar al-Ayb.",
        "key_points": [
            "Commercial trade conducted with honesty is an act of high worship (Ibadah).",
            "Ethical finance eliminates usury (Riba) and safeguards families from debt traps.",
            "Written contracts (Kitabah) and witnesses preserve community trust and brotherhood.",
            "Consumer protection guarantees fair pricing, truthful disclosure, and refund rights."
        ],
        "exit_ticket": "Write down the single most vital lesson you learned in this unit and explain how it will guide your future financial decisions."
    }
]


# ─────────────────────────────────────────────────────────────────────────────
# INGESTION & AUDIT EXECUTION ENGINE
# ─────────────────────────────────────────────────────────────────────────────

@transaction.atomic
def ingest_topic_16():
    print("================================================================================")
    print("STARTING PRODUCTION INGESTION: GRADE 9 IRE — TOPIC 16")
    print("Topic: Trade and Financial Transactions in Islam (Topic ID 356)")
    print("================================================================================")

    topic = Topic.objects.get(id=356)
    print(f"Target Topic: {topic.id} - {topic.name}")

    # Remove any existing units for this topic to ensure clean, idempotent ingestion
    existing_units = LearningUnit.objects.filter(topic=topic)
    if existing_units.exists():
        print(f"Cleaning up {existing_units.count()} existing LearningUnits for clean idempotent ingestion...")
        existing_units.delete()

    created_units = 0
    created_lessons = 0
    created_blocks = 0
    created_assets = 0

    for ldata in TOPIC_16_LESSONS:
        order = ldata["unit_order"]
        title = ldata["lesson_title"]
        print(f"\nIngesting Lesson {order}/6: {title}...")

        # 1. Create LearningUnit
        unit = LearningUnit.objects.create(
            topic=topic,
            name=f"Lesson 6.5.{order}: {title}",
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
        # Verify SVG XML validity
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
    print("INGESTION COMPLETE FOR TOPIC 16!")
    print(f"Created Units: {created_units}")
    print(f"Created Lessons: {created_lessons}")
    print(f"Created Blocks: {created_blocks}")
    print(f"Created Assets: {created_assets}")
    print("================================================================================")


if __name__ == "__main__":
    ingest_topic_16()
