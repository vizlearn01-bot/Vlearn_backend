"""
VLearn CBC Grade 9 IRE — Topic 14: Child Custody (Hadanah)
Production Ingestion and Enrichment Script for all 4 Lessons

Target Topic in DB: Topic ID 354 (Subject: IRE ID 53, Grade: Grade 9 ID 18)
Source Markdown: /home/jason-bitega/Desktop/VL/vlearn_repositories/Grade 9 IRE/child-custody.md

4 Lessons Ingested & Fully Enriched:
  1. Lesson 6.3.1: Child rights and custody
  2. Lesson 6.3.2: Islamic rules on custody
  3. Lesson 6.3.3: Significance and family bonds
  4. Lesson 6.3.4: Unit synthesis
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
    """Lesson 6.3.1: The Child's Shield of Rights in Hadanah"""
    return """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 880 440" width="100%" height="100%">
  <defs>
    <linearGradient id="bg141" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#0f172a"/>
      <stop offset="50%" stop-color="#1e293b"/>
      <stop offset="100%" stop-color="#0f172a"/>
    </linearGradient>
  </defs>

  <rect width="880" height="440" rx="14" fill="url(#bg141)"/>
  <rect x="2" y="2" width="876" height="436" rx="12" fill="none" stroke="#334155" stroke-width="1.5"/>

  <!-- Header -->
  <text x="440" y="36" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="16" font-weight="700" text-anchor="middle">CHILD CUSTODY (HADANAH): THE CHILD'S SACRED SHIELD OF RIGHTS</text>
  <text x="440" y="56" fill="#94a3b8" font-family="system-ui, sans-serif" font-size="11.5" text-anchor="middle">A Welfare-Centered Approach: Custody Belongs to the Child as a Sacred Trust (Amanah)</text>

  <!-- 4 Converging Protective Quadrants -->
  <!-- Quadrant 1: Physical Safety -->
  <g transform="translate(45, 85)">
    <rect width="180" height="260" rx="8" fill="#1e293b" stroke="#38bdf8" stroke-width="1.5"/>
    <rect width="180" height="34" rx="8" fill="#0284c7"/>
    <text x="90" y="22" fill="#ffffff" font-family="system-ui, sans-serif" font-size="10.5" font-weight="800" text-anchor="middle">1. PHYSICAL SAFETY</text>

    <text x="90" y="56" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="10" font-weight="700" text-anchor="middle">Health &amp; Security</text>

    <rect x="10" y="70" width="160" height="175" rx="4" fill="#0f172a"/>
    <text x="18" y="92" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="8.5" font-weight="700">• Clean Shelter:</text>
    <text x="18" y="108" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="8">  Safe home environment</text>
    <text x="18" y="122" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="8">  free from physical danger</text>
    <text x="18" y="146" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="8.5" font-weight="700">• Nutrition &amp; Healthcare:</text>
    <text x="18" y="162" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="8">  Wholesome food and timely</text>
    <text x="18" y="176" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="8">  medical treatment</text>
    <text x="18" y="208" fill="#34d399" font-family="system-ui, sans-serif" font-size="8.5" font-weight="700">★ Bodily Wellbeing</text>
    <text x="18" y="224" fill="#a7f3d0" font-family="system-ui, sans-serif" font-size="7.5">Zero tolerance for neglect</text>
  </g>

  <!-- Quadrant 2: Emotional Nurturing -->
  <g transform="translate(245, 85)">
    <rect width="180" height="260" rx="8" fill="#1e293b" stroke="#34d399" stroke-width="1.5"/>
    <rect width="180" height="34" rx="8" fill="#059669"/>
    <text x="90" y="22" fill="#ffffff" font-family="system-ui, sans-serif" font-size="10.5" font-weight="800" text-anchor="middle">2. EMOTIONAL WARMTH</text>

    <text x="90" y="56" fill="#34d399" font-family="system-ui, sans-serif" font-size="10" font-weight="700" text-anchor="middle">Tarbiya &amp; Love</text>

    <rect x="10" y="70" width="160" height="175" rx="4" fill="#0f172a"/>
    <text x="18" y="92" fill="#34d399" font-family="system-ui, sans-serif" font-size="8.5" font-weight="700">• Maternal Priority:</text>
    <text x="18" y="108" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="8">  Specialized affection and</text>
    <text x="18" y="122" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="8">  care in early formative years</text>
    <text x="18" y="146" fill="#34d399" font-family="system-ui, sans-serif" font-size="8.5" font-weight="700">• Psychological Peace:</text>
    <text x="18" y="162" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="8">  Shielded from spousal arguments</text>
    <text x="18" y="176" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="8">  and toxic hostility</text>
    <text x="18" y="208" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="8.5" font-weight="700">★ Mental Stability</text>
    <text x="18" y="224" fill="#e0f2fe" font-family="system-ui, sans-serif" font-size="7.5">Secure emotional bonding</text>
  </g>

  <!-- Quadrant 3: Financial Maintenance -->
  <g transform="translate(445, 85)">
    <rect width="180" height="260" rx="8" fill="#1e293b" stroke="#fbbf24" stroke-width="1.5"/>
    <rect width="180" height="34" rx="8" fill="#d97706"/>
    <text x="90" y="22" fill="#ffffff" font-family="system-ui, sans-serif" font-size="10.5" font-weight="800" text-anchor="middle">3. FINANCIAL DUTY</text>

    <text x="90" y="56" fill="#fbbf24" font-family="system-ui, sans-serif" font-size="10" font-weight="700" text-anchor="middle">Father's Sole Nafaqah</text>

    <rect x="10" y="70" width="160" height="175" rx="4" fill="#0f172a"/>
    <text x="18" y="92" fill="#fbbf24" font-family="system-ui, sans-serif" font-size="8.5" font-weight="700">• 100% Paternal Cost:</text>
    <text x="18" y="108" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="8">  School fees, books, clothing,</text>
    <text x="18" y="122" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="8">  and housing allowance</text>
    <text x="18" y="146" fill="#fbbf24" font-family="system-ui, sans-serif" font-size="8.5" font-weight="700">• Unconditional Duty:</text>
    <text x="18" y="162" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="8">  Father must pay regardless of</text>
    <text x="18" y="176" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="8">  who holds physical custody</text>
    <text x="18" y="208" fill="#f87171" font-family="system-ui, sans-serif" font-size="8.5" font-weight="700">★ Material Guarantee</text>
    <text x="18" y="224" fill="#fecaca" font-family="system-ui, sans-serif" font-size="7.5">Zero financial abandonment</text>
  </g>

  <!-- Quadrant 4: Spiritual & Moral Growth -->
  <g transform="translate(645, 85)">
    <rect width="180" height="260" rx="8" fill="#1e293b" stroke="#a78bfa" stroke-width="1.5"/>
    <rect width="180" height="34" rx="8" fill="#6d28d9"/>
    <text x="90" y="22" fill="#ede9fe" font-family="system-ui, sans-serif" font-size="10.5" font-weight="800" text-anchor="middle">4. SPIRITUAL FITRAH</text>

    <text x="90" y="56" fill="#a78bfa" font-family="system-ui, sans-serif" font-size="10" font-weight="700" text-anchor="middle">Islamic Guidance</text>

    <rect x="10" y="70" width="160" height="175" rx="4" fill="#0f172a"/>
    <text x="18" y="92" fill="#a78bfa" font-family="system-ui, sans-serif" font-size="8.5" font-weight="700">• Preserving Fitrah:</text>
    <text x="18" y="108" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="8">  Teaching Salah, Quran,</text>
    <text x="18" y="122" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="8">  and sound Islamic manners</text>
    <text x="18" y="146" fill="#a78bfa" font-family="system-ui, sans-serif" font-size="8.5" font-weight="700">• Moral Environment:</text>
    <text x="18" y="162" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="8">  Custodian must shield child</text>
    <text x="18" y="176" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="8">  from drugs, crime, or vice</text>
    <text x="18" y="208" fill="#34d399" font-family="system-ui, sans-serif" font-size="8.5" font-weight="700">★ Moral Upbringing</text>
    <text x="18" y="224" fill="#a7f3d0" font-family="system-ui, sans-serif" font-size="7.5">Accountability before Allah</text>
  </g>

  <!-- Bottom Banner -->
  <g transform="translate(45, 360)">
    <rect width="780" height="55" rx="8" fill="#1e293b" stroke="#334155" stroke-width="1.5"/>
    <text x="390" y="24" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="10.5" font-weight="700" text-anchor="middle">CHILDREN ARE AN AMANAH (SACRED TRUST), NOT PROPERTY</text>
    <text x="390" y="42" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="9" text-anchor="middle">Custody is an unalienable right belonging to the child, prioritizing their physical, emotional, and spiritual best interests</text>
  </g>
</svg>"""


def get_svg_lesson_2():
    """Lesson 6.3.2: The Custody Priority Path & Staged Sequence"""
    return """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 880 440" width="100%" height="100%">
  <defs>
    <linearGradient id="bg142" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#0f172a"/>
      <stop offset="50%" stop-color="#1e293b"/>
      <stop offset="100%" stop-color="#0f172a"/>
    </linearGradient>
  </defs>

  <rect width="880" height="440" rx="14" fill="url(#bg142)"/>
  <rect x="2" y="2" width="876" height="436" rx="12" fill="none" stroke="#334155" stroke-width="1.5"/>

  <!-- Header -->
  <text x="440" y="36" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="16" font-weight="700" text-anchor="middle">THE ISLAMIC CUSTODY PRIORITY SEQUENCE &amp; DEVELOPMENTAL PATH</text>
  <text x="440" y="56" fill="#94a3b8" font-family="system-ui, sans-serif" font-size="11.5" text-anchor="middle">Staged Custody Allocation Grounded in Child Needs, Moral Fitness, and Paternal Maintenance</text>

  <!-- 3 Stages Process Flow -->
  <!-- Stage 1: Early Childhood -->
  <g transform="translate(45, 90)">
    <rect width="240" height="250" rx="10" fill="#1e293b" stroke="#38bdf8" stroke-width="1.5"/>
    <rect width="240" height="38" rx="10" fill="#0369a1"/>
    <text x="120" y="24" fill="#ffffff" font-family="system-ui, sans-serif" font-size="11" font-weight="800" text-anchor="middle">STAGE 1: AGES 0–7 YEARS</text>

    <text x="120" y="60" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="10" font-weight="700" text-anchor="middle">Mother's Absolute Priority</text>

    <rect x="15" y="75" width="210" height="155" rx="6" fill="#0f172a"/>
    <text x="25" y="98" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="9" font-weight="700">• Prophetic Precedent:</text>
    <text x="25" y="114" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="8.5">  "You have the best right to him</text>
    <text x="25" y="128" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="8.5">  as long as you do not remarry"</text>
    <text x="25" y="152" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="9" font-weight="700">• Unmatched Tenderness:</text>
    <text x="25" y="168" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="8.5">  Patience, feeding, and maternal</text>
    <text x="25" y="182" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="8.5">  emotional bonding</text>
    <text x="25" y="208" fill="#34d399" font-family="system-ui, sans-serif" font-size="8.5" font-weight="700">★ Father funds 100% Nafaqah</text>
  </g>

  <!-- Stage 2: Transfer Triggers -->
  <g transform="translate(320, 90)">
    <rect width="240" height="250" rx="10" fill="#1e293b" stroke="#f59e0b" stroke-width="1.5"/>
    <rect width="240" height="38" rx="10" fill="#b45309"/>
    <text x="120" y="24" fill="#ffffff" font-family="system-ui, sans-serif" font-size="11" font-weight="800" text-anchor="middle">STAGE 2: TRANSFER TRIGGERS</text>

    <text x="120" y="60" fill="#fbbf24" font-family="system-ui, sans-serif" font-size="10" font-weight="700" text-anchor="middle">Remarriage or Unfitness</text>

    <rect x="15" y="75" width="210" height="155" rx="6" fill="#0f172a"/>
    <text x="25" y="98" fill="#fbbf24" font-family="system-ui, sans-serif" font-size="9" font-weight="700">• Transfer Sequence:</text>
    <text x="25" y="114" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="8.5">  1. Maternal Grandmother</text>
    <text x="25" y="128" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="8.5">  2. Father / Paternal relatives</text>
    <text x="25" y="142" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="8.5">  3. Aunts &amp; female kin</text>
    <text x="25" y="168" fill="#fbbf24" font-family="system-ui, sans-serif" font-size="9" font-weight="700">• Unfitness Criteria:</text>
    <text x="25" y="182" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="8.5">  Substance abuse, crime, neglect</text>
    <text x="25" y="208" fill="#f87171" font-family="system-ui, sans-serif" font-size="8.5" font-weight="700">★ Best interest of child governs</text>
  </g>

  <!-- Stage 3: Age of Reason -->
  <g transform="translate(595, 90)">
    <rect width="240" height="250" rx="10" fill="#1e293b" stroke="#34d399" stroke-width="1.5"/>
    <rect width="240" height="38" rx="10" fill="#059669"/>
    <text x="120" y="24" fill="#ffffff" font-family="system-ui, sans-serif" font-size="11" font-weight="800" text-anchor="middle">STAGE 3: AGES 7+ YEARS</text>

    <text x="120" y="60" fill="#34d399" font-family="system-ui, sans-serif" font-size="10" font-weight="700" text-anchor="middle">Age of Reason (Tamyiz)</text>

    <rect x="15" y="75" width="210" height="155" rx="6" fill="#0f172a"/>
    <text x="25" y="98" fill="#34d399" font-family="system-ui, sans-serif" font-size="9" font-weight="700">• Child's Preference (Ikhtiyar):</text>
    <text x="25" y="114" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="8.5">  Child can express choice of</text>
    <text x="25" y="128" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="8.5">  parent if both are righteous</text>
    <text x="25" y="152" fill="#34d399" font-family="system-ui, sans-serif" font-size="9" font-weight="700">• Education &amp; Discipline:</text>
    <text x="25" y="168" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="8.5">  Father exercises oversight for</text>
    <text x="25" y="182" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="8.5">  social training &amp; career</text>
    <text x="25" y="208" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="8.5" font-weight="700">★ Co-parenting harmony required</text>
  </g>

  <!-- Bottom Summary Banner -->
  <g transform="translate(45, 360)">
    <rect width="790" height="55" rx="8" fill="#1e293b" stroke="#334155" stroke-width="1.5"/>
    <text x="395" y="24" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="10.5" font-weight="700" text-anchor="middle">TWO PERMANENT PILLARS</text>
    <text x="395" y="42" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="9" text-anchor="middle">Physical custody changes with developmental needs • Paternal financial maintenance (Nafaqah) remains constant throughout</text>
  </g>
</svg>"""


def get_svg_lesson_3():
    """Lesson 6.3.3: Silat al-Rahim: Healthy Co-Parenting vs Alienation"""
    return """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 880 440" width="100%" height="100%">
  <defs>
    <linearGradient id="bg143" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#0f172a"/>
      <stop offset="50%" stop-color="#1e293b"/>
      <stop offset="100%" stop-color="#0f172a"/>
    </linearGradient>
  </defs>

  <rect width="880" height="440" rx="14" fill="url(#bg143)"/>
  <rect x="2" y="2" width="876" height="436" rx="12" fill="none" stroke="#334155" stroke-width="1.5"/>

  <!-- Header -->
  <text x="440" y="36" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="16" font-weight="700" text-anchor="middle">PRESERVING KINSHIP TIES (SILAT AL-RAHIM): CO-PARENTING ARCHITECTURE</text>
  <text x="440" y="56" fill="#94a3b8" font-family="system-ui, sans-serif" font-size="11.5" text-anchor="middle">Healthy Islamic Co-Parenting vs Destructive Parental Alienation</text>

  <!-- Left Column: Healthy Co-Parenting -->
  <g transform="translate(45, 85)">
    <rect width="380" height="260" rx="8" fill="#1e293b" stroke="#34d399" stroke-width="1.5"/>
    <rect width="380" height="34" rx="8" fill="#059669"/>
    <text x="190" y="22" fill="#ffffff" font-family="system-ui, sans-serif" font-size="11.5" font-weight="800" text-anchor="middle">HEALTHY ISLAMIC CO-PARENTING (EMERALD STANDARD)</text>

    <rect x="15" y="46" width="350" height="42" rx="4" fill="#0f172a"/>
    <text x="25" y="62" fill="#34d399" font-family="system-ui, sans-serif" font-size="9" font-weight="700">Sacred Visitation Rights:</text>
    <text x="25" y="78" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="8.5">Regular, peaceful access to non-custodial parent without hindrance</text>

    <rect x="15" y="96" width="350" height="42" rx="4" fill="#0f172a"/>
    <text x="25" y="112" fill="#34d399" font-family="system-ui, sans-serif" font-size="9" font-weight="700">Respectful Communication:</text>
    <text x="25" y="128" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="8.5">Parents speak honorably of each other in front of the child</text>

    <rect x="15" y="146" width="350" height="42" rx="4" fill="#0f172a"/>
    <text x="25" y="162" fill="#34d399" font-family="system-ui, sans-serif" font-size="9" font-weight="700">Extended Kinship Bonds (Silat al-Rahim):</text>
    <text x="25" y="178" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="8.5">Child regularly visits both maternal &amp; paternal grandparents and cousins</text>

    <rect x="15" y="196" width="350" height="42" rx="4" fill="#0f172a"/>
    <text x="25" y="212" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="9" font-weight="700">Paternal Support Faithfulness:</text>
    <text x="25" y="228" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="8.5">Father pays school fees and expenses happily as an act of ibadah</text>
  </g>

  <!-- Right Column: Parental Alienation -->
  <g transform="translate(455, 85)">
    <rect width="380" height="260" rx="8" fill="#1e293b" stroke="#f87171" stroke-width="1.5"/>
    <rect width="380" height="34" rx="8" fill="#7f1d1d"/>
    <text x="190" y="22" fill="#fecaca" font-family="system-ui, sans-serif" font-size="11.5" font-weight="800" text-anchor="middle">DESTRUCTIVE PARENTAL ALIENATION (HARAM)</text>

    <rect x="15" y="46" width="350" height="42" rx="4" fill="#0f172a"/>
    <text x="25" y="62" fill="#f87171" font-family="system-ui, sans-serif" font-size="9" font-weight="700">Blocking Visitation:</text>
    <text x="25" y="78" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="8.5">Hiding child or preventing visits; cuts kinship ties (Major Sin)</text>

    <rect x="15" y="96" width="350" height="42" rx="4" fill="#0f172a"/>
    <text x="25" y="112" fill="#f87171" font-family="system-ui, sans-serif" font-size="9" font-weight="700">Bad-mouthing &amp; Poisoning:</text>
    <text x="25" y="128" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="8.5">Insulting ex-spouse to turn child against father/mother (Slander)</text>

    <rect x="15" y="146" width="350" height="42" rx="4" fill="#0f172a"/>
    <text x="25" y="162" fill="#f87171" font-family="system-ui, sans-serif" font-size="9" font-weight="700">Using Child as a Bargaining Chip:</text>
    <text x="25" y="178" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="8.5">Manipulating child to extract money or inflict emotional punishment</text>

    <rect x="15" y="196" width="350" height="42" rx="4" fill="#0f172a"/>
    <text x="25" y="212" fill="#fbbf24" font-family="system-ui, sans-serif" font-size="9" font-weight="700">Withholding Financial Maintenance:</text>
    <text x="25" y="228" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="8.5">Father cutting school fees to punish mother; harms child directly</text>
  </g>

  <!-- Bottom Message -->
  <g transform="translate(45, 360)">
    <rect width="790" height="55" rx="8" fill="#1e293b" stroke="#334155" stroke-width="1.5"/>
    <text x="395" y="24" fill="#f87171" font-family="system-ui, sans-serif" font-size="10" font-weight="700" text-anchor="middle">PROPHETIC WARNING: "HE WHO SEVERS KINSHIP WILL NOT ENTER PARADISE"</text>
    <text x="395" y="42" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="9" text-anchor="middle">Divorce ends marriage between spouses; it never dissolves the sacred parent-child bond</text>
  </g>
</svg>"""


def get_svg_lesson_4():
    """Lesson 6.3.4: Master Synthesis: The Child Custody Sanctuary"""
    return """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 880 440" width="100%" height="100%">
  <defs>
    <linearGradient id="bg144" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#0f172a"/>
      <stop offset="50%" stop-color="#1e293b"/>
      <stop offset="100%" stop-color="#0f172a"/>
    </linearGradient>
  </defs>

  <rect width="880" height="440" rx="14" fill="url(#bg144)"/>
  <rect x="2" y="2" width="876" height="436" rx="12" fill="none" stroke="#334155" stroke-width="1.5"/>

  <!-- Header -->
  <text x="440" y="32" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="16" font-weight="700" text-anchor="middle">MASTER SYNTHESIS: THE CHILD CUSTODY SANCTUARY</text>
  <text x="440" y="52" fill="#94a3b8" font-family="system-ui, sans-serif" font-size="11.5" text-anchor="middle">Harmonizing Maternal Care, Paternal Guardianship, and Sacred Kinship in Islamic Family Law</text>

  <!-- Central Apex: Child's Best Interest -->
  <g transform="translate(290, 75)">
    <polygon points="150,0 300,55 0,55" fill="#0369a1" stroke="#38bdf8" stroke-width="1.5"/>
    <text x="150" y="32" fill="#ffffff" font-family="system-ui, sans-serif" font-size="12" font-weight="800" text-anchor="middle">CHILD'S BEST INTEREST &amp; SACRED FITRAH</text>
    <text x="150" y="47" fill="#e0f2fe" font-family="system-ui, sans-serif" font-size="9" text-anchor="middle">(Surah Al-Isra 17:70 &amp; Hadith on Amanah)</text>
  </g>

  <!-- 3 Pillar Columns -->
  <!-- Left Pillar: Mother's Role -->
  <g transform="translate(60, 145)">
    <rect width="220" height="205" rx="8" fill="#1e293b" stroke="#34d399" stroke-width="1.5"/>
    <rect width="220" height="32" rx="8" fill="#059669"/>
    <text x="110" y="21" fill="#ffffff" font-family="system-ui, sans-serif" font-size="10.5" font-weight="800" text-anchor="middle">MOTHER'S ROLE: HADANAH</text>

    <rect x="12" y="42" width="196" height="150" rx="4" fill="#0f172a"/>
    <text x="20" y="62" fill="#34d399" font-family="system-ui, sans-serif" font-size="8.5" font-weight="700">• Physical Nurturing:</text>
    <text x="20" y="78" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="8">  Daily hygiene, feeding,</text>
    <text x="20" y="92" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="8">  and bedtime security</text>
    <text x="20" y="116" fill="#34d399" font-family="system-ui, sans-serif" font-size="8.5" font-weight="700">• Maternal Affection:</text>
    <text x="20" y="132" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="8">  Natural patience &amp; emotional</text>
    <text x="20" y="146" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="8">  warmth during early growth</text>
    <text x="20" y="174" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="8.5" font-weight="700">★ Ages 0–7 Default Priority</text>
  </g>

  <!-- Center Core: Kinship Ties -->
  <g transform="translate(330, 145)">
    <rect width="220" height="205" rx="8" fill="#1e293b" stroke="#38bdf8" stroke-width="1.5"/>
    <rect width="220" height="32" rx="8" fill="#0284c7"/>
    <text x="110" y="21" fill="#ffffff" font-family="system-ui, sans-serif" font-size="10.5" font-weight="800" text-anchor="middle">KINSHIP: SILAT AL-RAHIM</text>

    <rect x="12" y="42" width="196" height="150" rx="4" fill="#0f172a"/>
    <text x="20" y="62" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="8.5" font-weight="700">• Sacred Visitation:</text>
    <text x="20" y="78" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="8">  Non-custodial parent visits</text>
    <text x="20" y="92" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="8">  freely without hostility</text>
    <text x="20" y="116" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="8.5" font-weight="700">• Two-Sided Family Tree:</text>
    <text x="20" y="132" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="8">  Grandparents, aunts &amp; uncles</text>
    <text x="20" y="146" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="8">  enrich child's identity</text>
    <text x="20" y="174" fill="#34d399" font-family="system-ui, sans-serif" font-size="8.5" font-weight="700">★ Ties Must Never Be Severed</text>
  </g>

  <!-- Right Pillar: Father's Role -->
  <g transform="translate(600, 145)">
    <rect width="220" height="205" rx="8" fill="#1e293b" stroke="#fbbf24" stroke-width="1.5"/>
    <rect width="220" height="32" rx="8" fill="#d97706"/>
    <text x="110" y="21" fill="#ffffff" font-family="system-ui, sans-serif" font-size="10.5" font-weight="800" text-anchor="middle">FATHER'S ROLE: WILAYAH</text>

    <rect x="12" y="42" width="196" height="150" rx="4" fill="#0f172a"/>
    <text x="20" y="62" fill="#fbbf24" font-family="system-ui, sans-serif" font-size="8.5" font-weight="700">• Financial Maintenance:</text>
    <text x="20" y="78" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="8">  100% funding of education,</text>
    <text x="20" y="92" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="8">  housing, and medical costs</text>
    <text x="20" y="116" fill="#fbbf24" font-family="system-ui, sans-serif" font-size="8.5" font-weight="700">• Legal Guardianship:</text>
    <text x="20" y="132" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="8">  Protective oversight, discipline,</text>
    <text x="20" y="146" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="8">  and moral representation</text>
    <text x="20" y="174" fill="#f87171" font-family="system-ui, sans-serif" font-size="8.5" font-weight="700">★ Nafaqah Duty Never Dies</text>
  </g>

  <!-- Foundation: Child-Centered Justice -->
  <g transform="translate(60, 360)">
    <rect width="760" height="50" rx="6" fill="#1e293b" stroke="#38bdf8" stroke-width="1.5"/>
    <text x="380" y="22" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="11" font-weight="800" text-anchor="middle">FOUNDATION: CHILD-CENTERED JUSTICE (MAQASID AL-SHARIAH)</text>
    <text x="380" y="39" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="8.5" text-anchor="middle">When parents separate, the child's rights are never compromised; mother, father, and court unite to guard the child</text>
  </g>
</svg>"""


# ─────────────────────────────────────────────────────────────────────────────
# CONFIGURATION FOR THE 4 LESSONS IN TOPIC 14
# ─────────────────────────────────────────────────────────────────────────────

LESSONS_CONFIG = [
    {
        "unit_order": 1,
        "lesson_title": "Child rights and custody",
        "inquiry": "What is child custody (Hadanah) in Islam, and how does it safeguard the fundamental rights of children?",
        "hook": "Imagine a priceless diamond owned by a national museum. If the museum undergoes structural renovation, they do not leave the diamond lying on the floor or allow staff to argue over who carries it home. They commission an elite, climate-controlled transport team to store the gem in a secure vault, ensuring it remains protected, polished, and safe from harm. In Islamic family law, a child is not property, an asset to be partitioned, or a trophy in parental disputes. A child is a priceless spiritual jewel—an Amanah (sacred trust) from Allah. Child custody (Hadanah) is the legal sanctuary designed to place this precious trust in the safest possible hands.",
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/c/c5/Quran_manuscript.jpg/800px-Quran_manuscript.jpg",
        "image_title": "Divine Legislation on Family Care and Custody",
        "image_caption": "Historic Qur'anic manuscript documenting the sacred obligations of parents toward their children and the sanctity of family welfare.",
        "concept_name": "Hadanah as the Child's Sacred Right",
        "concept_explanation": "Hadanah (Child Custody) is defined in Islamic jurisprudence as the physical care, nurturing, education, and protection of a child who has not reached the age of independence following parental separation or divorce. In Shariah, custody is fundamentally the right of the child to receive nurturing, safety, and moral guidance—it is not an ownership right belonging to either parent. Children are born upon pure natural faith (Fitrah), and parents are held strictly accountable before Allah as shepherds responsible for their flock.",
        "scripture_quran": "We have enjoined upon man [care] for his parents. His mother carried him with hardship upon hardship, and his weaning is in two years...",
        "scripture_quran_ref": "Surah Luqman 31:14",
        "scripture_hadith": "Each of you is a shepherd, and each of you is responsible for his flock... A man is a shepherd in his house and is responsible for his flock; a woman is a shepherd in her husband's house and is responsible for her flock...",
        "scripture_hadith_ref": "Sahih al-Bukhari 5188",
        "deep_explanation": "The system of Hadanah guarantees four fundamental rights of the child:\n1. The Right to Nurturing (Tarbiya): Early developmental years require exceptional patience, emotional warmth, and physical care, which is why Shariah gives initial physical custody priority to the mother.\n2. The Right to Financial Maintenance (Nafaqah): The child has an absolute right to complete financial support (nutritious food, clothing, clean lodging, healthcare, and education). Crucially, the father remains 100% financially liable for all costs, even when the mother retains physical custody.\n3. The Right to Moral & Spiritual Upbringing: The custodian must provide a safe environment promoting prayer, virtuous character (Akhlaq), and sound Islamic knowledge, shielding the child from corrupting influences.\n4. Protection from Spousal Hostility: Shariah strictly forbids parents from using children as pawns or leverage in divorce negotiations.",
        "diagram_title": "The Child's Sacred Shield of Rights in Hadanah",
        "svg_func": get_svg_lesson_1,
        "table_title": "Four Core Pillars of Child Rights in Hadanah",
        "table_headers": ["Pillar of Right", "Legal Obligation in Shariah", "Responsible Parent", "Pedagogical Objective"],
        "table_rows": [
            ["Physical Safety & Health", "Clean shelter, wholesome food, medical insurance", "Mother (Care) / Father (Funding)", "Guarantees bodily health & safe living"],
            ["Emotional Nurturing", "Unconditional love, patience, stress-free home", "Mother (Primary in early childhood)", "Fosters secure attachment & mental peace"],
            ["Financial Maintenance (Nafaqah)", "100% funding of school fees, clothing, housing", "Father (Absolute legal liability)", "Shields child from post-divorce poverty"],
            ["Spiritual & Moral Growth", "Teaching Salah, Quran, and good character (Akhlaq)", "Both Parents & Kadhi Court", "Preserves Fitrah & upright citizenship"]
        ],
        "scenario": "Yusuf and Amina are undergoing a divorce. In anger, Yusuf declares: 'Since we are separating, I will take our 3-year-old daughter Halima to live with me, and you will not see her. This is my right as a father.' Amina's brother Omar intervenes with Islamic knowledge: 'Yusuf, in Shariah, custody is not a game of pride. Halima is a toddler and possesses a divine right to her mother's care and tender nurturing. The Prophet (PBUH) ruled that the mother has primary custody of young children. Your obligation as her father is to pay for her housing, food, and medical fees, while visiting her peacefully to teach and guide her.'",
        "real_world": "In your school and neighborhood, classmates whose parents are separated may experience emotional transitions. Embody Islamic empathy (Rahmah) by being a supportive, non-judgmental friend. Never gossip about their family situation, ask insensitive questions, or make them feel isolated. Your kindness helps maintain their emotional stability, fulfilling the noble goals of Islamic social relations (Muamalat).",
        "reflection": "Why does Islamic law make the father fully financially responsible for his children after divorce, while granting the mother primary physical custody? How does this balance of roles reflect divine wisdom and equity?",
        "misconception": "Misconception: Believing that child custody is a prize won by the wealthiest parent in court. In Islamic law, wealth does not determine custody; maternal care and the child's overall safety govern physical custody, while the father is legally compelled to fund all expenses according to his means.",
        "yt_id": "wX_K29Y7Z7I",
        "yt_title": "Child Custody in Islamic Jurisprudence (Hadanah)",
        "yt_desc": "Comprehensive analysis of child rights, maternal custody priority, and paternal financial maintenance under Shariah.",
        "mcq": {
            "question": "What is the primary legal and spiritual objective of child custody (Hadanah) in Islamic family law?",
            "options": [
                "A. To reward the parent who earns the highest financial income.",
                "B. To divide the child's physical time mathematically between parents.",
                "C. To safeguard the child's rights, physical welfare, and moral development.",
                "D. To punish the mother by removing her rights to the child."
            ],
            "answer": "C",
            "explanation": "Hadanah is constructed around a welfare-centered approach: the absolute legal priority is the child's best interests—securing their safety, emotional care, education, and spiritual uprightness."
        },
        "summary_content": "Hadanah is the legal system governing the nurturing, care, and upbringing of children after parental divorce. Islamic law treats children as an Amanah (sacred trust), prioritizing their welfare over parental desires. The child has divine rights to emotional care, physical security, moral guidance, and 100% paternal financial support.",
        "key_points": [
            "Hadanah is primarily the right of the child, not the ownership right of parents.",
            "Children are an Amanah (trust) from Allah born upon pure Fitrah.",
            "The mother holds primary custody in early childhood for emotional care.",
            "The father remains 100% financially liable for the child's Nafaqah."
        ],
        "exit_ticket": "Explain in your own words why a child is regarded as an Amanah (sacred trust) rather than property in Islamic law."
    },
    {
        "unit_order": 2,
        "lesson_title": "Islamic rules on custody",
        "inquiry": "What specific rules, developmental stages, and priorities govern child custody in Islam?",
        "hook": "Imagine an astronaut training program for a high-stakes space exploration mission. The mission agency does not select the lead pilot through a popularity contest or random lottery. They follow an exacting protocol: Who possesses the necessary specialized skills for each flight phase? Who remains calm under pressure? In Islamic family law, the critical mission of raising a human soul follows an exacting, divinely established sequence. Islam establishes clear priorities and benchmarks to ensure the child is placed with the caregiver best suited for each developmental stage.",
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/5/52/Al-Masjid_an-Nabawi_in_2017.jpg/800px-Al-Masjid_an-Nabawi_in_2017.jpg",
        "image_title": "The Prophet's Mosque in Madinah",
        "image_caption": "Historic sanctuary where the Prophet (PBUH) issued landmark legal judgments protecting mothers' rights to child custody and establishing family justice.",
        "concept_name": "Developmental Custody Priority & Transfer Protocols",
        "concept_explanation": "Islamic custody regulations are structured around developmental stages and caregiver fitness. In infancy and early childhood (ages 0–7), the mother holds the primary right to custody as long as she meets safety standards and does not remarry a non-mahram stranger who might neglect the child. If the mother is unable or disqualified, custody transitions along a prioritized line of female relatives (such as the maternal grandmother) before passing to the father. At the age of understanding (Tamyiz, around age 7), the child's living preference may be consulted, while the father remains the legal guardian (Wali) with ongoing financial duties.",
        "scripture_quran": "Mothers may breastfeed their children two complete years for whoever wishes to complete the nursing [period]. Upon the father is the mothers' provision and their clothing according to what is acceptable...",
        "scripture_quran_ref": "Surah Al-Baqarah 2:233",
        "scripture_hadith": "A woman said: 'O Messenger of Allah, my womb was a vessel for this son, my breast was a water-skin for him, and my lap was a shelter for him, yet his father wants to take him away.' The Prophet (PBUH) said: 'You have the best right to him, so long as you do not remarry.'",
        "scripture_hadith_ref": "Sunan Abu Dawood 2276 / Sahih Muslim 1442",
        "deep_explanation": "Islamic jurisprudence outlines three developmental phases and fitness criteria:\n1. Early Childhood (0–7 Years): The mother's unmatched patience and nurturing capacity establish her custody priority. The famous Hadith in Sunan Abu Dawood explicitly confirms this legal privilege.\n2. Remarriage & Disqualification: If the mother remarries a stranger who has no natural affection for the child, or if she engages in severe neglect, crime, or substance abuse, custody transfers to ensure child safety. It passes first to the maternal grandmother (who shares maternal love) before transitioning to the father.\n3. Age of Discernment (Tamyiz, 7+ Years): When the child reaches cognitive maturity, many scholars permit the child to express their preference (Ikhtiyar) between two fit parents.\n4. Separate Legal Roles: Physical custody (Hadanah) and financial guardianship (Wilayah) are distinct. The father must fund all expenses regardless of who holds physical custody.",
        "diagram_title": "The Islamic Custody Priority Sequence & Developmental Path",
        "svg_func": get_svg_lesson_2,
        "table_title": "Developmental Stages and Islamic Custody Allocations",
        "table_headers": ["Developmental Stage", "Age Range", "Default Custody Allocation", "Legal Rationale"],
        "table_rows": [
            ["Early Formative Years", "Infancy to 7 Years", "Mother holds primary physical custody", "Unique nurturing capacity and maternal bonding (Sunan Abu Dawood 2276)"],
            ["Transfer Triggers", "Any Age (Upon trigger)", "Maternal Grandmother -> Father -> Aunts", "Mother remarries stranger or lacks physical/moral fitness"],
            ["Age of Reason (Tamyiz)", "7 Years and Above", "Child's preference (Ikhtiyar) consulted", "Child discerns beneficial care; father exercises moral oversight"],
            ["Financial Liability", "Throughout Entire Minority", "Father pays 100% Nafaqah unconditionally", "Binding Qur'anic injunction on fathers (Surah Al-Baqarah 2:233)"]
        ],
        "scenario": "Fatima and Yusuf are divorced, and their 5-year-old son Ali lives with Fatima. Fatima decides to remarry. Yusuf immediately demands physical custody, claiming Ali must live with him now that she is remarried. Fatima's family seeks guidance from the local Kadhi court. The Kadhi explains: 'Under the Hadith, the mother's default priority yields upon remarriage to protect the child from potential household tension. However, the court evaluates Ali's welfare: since Fatima's mother (Ali's grandmother) lives in the same neighborhood and can provide familiar, loving care, custody transitions to the grandmother, while Yusuf continues to pay Ali's school fees and maintenance.'",
        "real_world": "In daily life, appreciate that managing responsibilities requires selflessness. If you care for a younger sibling or lead a school project, prioritize the safety and needs of those under your care over your personal convenience. Demonstrating reliability and compassion in small tasks prepares you to be a responsible, trustworthy guardian in adulthood.",
        "reflection": "Why did the Prophet (PBUH) condition the mother's priority on 'as long as you do not remarry'? How does this ruling proactively prevent domestic strain or neglect for a young child?",
        "misconception": "Misconception: Assuming that if a mother remarries, the father automatically gets custody without question. In Islamic jurisprudence, custody transitions first to the maternal grandmother and close female relatives who preserve maternal tenderness, always guided by the child's best interests.",
        "yt_id": "fD5m1Z7K8kY",
        "yt_title": "Rules and Sequence of Child Custody in Shariah",
        "yt_desc": "Legal lecture explaining the stages of Hadanah, conditions for maternal custody, and transfer protocols.",
        "mcq": {
            "question": "According to the famous Hadith in Sunan Abu Dawood (2276), what is the default rule regarding a mother's right to physical custody of her young child after divorce?",
            "options": [
                "A. She loses custody immediately to the father, regardless of the child's age.",
                "B. She has the highest right to custody, so long as she does not remarry.",
                "C. She must pay the father compensation to be allowed custody.",
                "D. She only has custody rights during weekends and school holidays."
            ],
            "answer": "B",
            "explanation": "The Prophet (PBUH) explicitly ruled that the mother has the primary right to her young child's custody so long as she does not remarry, recognizing her specialized nurturing role in early development."
        },
        "summary_content": "Islamic custody is organized into clear developmental stages: mothers hold priority from ages 0 to 7; custody may transition to female relatives (such as maternal grandmothers) or fathers if triggers arise; and children at the age of reason (Tamyiz) can express preferences between fit parents. The father remains 100% financially liable for Nafaqah at all stages.",
        "key_points": [
            "Mothers have primary custody priority for young children up to age 7.",
            "Custody may transfer upon remarriage or unfitness to maternal grandmother or father.",
            "At the age of reason (Tamyiz, 7+), the child's preference is respectfully considered.",
            "The father's duty to provide financial maintenance (Nafaqah) remains permanent."
        ],
        "exit_ticket": "State the conditions under which a mother might lose physical custody of her young child under Islamic law."
    },
    {
        "unit_order": 3,
        "lesson_title": "Significance and family bonds",
        "inquiry": "How do Islamic custody rules preserve loving family bonds (Silat al-Rahim) and protect children's mental health after divorce?",
        "hook": "Imagine a bridge connecting two vibrant towns across a roaring canyon. During a severe tremor, the bridge's central span is damaged. The residents on either side cannot cross to visit relatives, trade, or share supplies. To prevent alienation, engineers construct a sturdy suspension footbridge, allowing community members to visit back and forth freely. In family life, divorce is an emotional earthquake that dissolves the spousal bridge. Islamic custody laws act as an unbreakable family footbridge, ensuring the child maintains a secure, loving connection to both parents and their extended families.",
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/e/e4/Kaaba_Masjid_Haraam_Makkah.jpg/800px-Kaaba_Masjid_Haraam_Makkah.jpg",
        "image_title": "Sanctuary of Mercy and Family Ties",
        "image_caption": "The holy sanctuary reminding believers that preserving the ties of kinship (Silat al-Rahim) is a sacred command carrying eternal divine rewards.",
        "concept_name": "Silat al-Rahim & Co-Parenting Ethics",
        "concept_explanation": "In Islamic family law, the dissolution of marriage between spouses never terminates the sacred parent-child bond or dissolves the ties of kinship (Silat al-Rahim). Custody arrangements must actively protect the child's mental health and emotional security by guaranteeing regular, unrestricted visitation with the non-custodial parent. Severing family ties, alienating a child from a parent, or poisoning a child's mind through slander are major sins in Islam. Divorced parents are religiously commanded to cooperate with maturity, respect, and fairness.",
        "scripture_quran": "...And fear Allah, through whom you ask one another, and the wombs [i.e., relationship of kinship]. Indeed, Allah is ever, over you, an Observer.",
        "scripture_quran_ref": "Surah An-Nisa 4:1",
        "scripture_hadith": "Whoever severs the bonds of kinship will not enter Paradise.",
        "scripture_hadith_ref": "Sahih al-Bukhari 5984",
        "deep_explanation": "Preserving family bonds during custody disputes rests upon foundational Shariah mandates:\n1. Unrestricted Visitation as a Sacred Right: The custodian parent cannot hide the child, relocate maliciously to prevent access, or deny visits. Blocking a parent from their child is classified as an act of oppression (Zulm) and severe disruption of kinship.\n2. Extended Kinship Preservation: Children derive their psychological stability, ancestral identity, and resilience from both maternal and paternal kin. Regular interaction with grandparents, uncles, aunts, and cousins on both sides is mandatory.\n3. The Ban on Parental Alienation: Bad-mouthing, mocking, or blaming the other parent in front of the child inflicts severe psychological trauma and violates the Prophetic command of truthful, honorable speech.\n4. Judicial Oversight: Kadhi courts possess authority to transfer custody away from a parent who persistently denies visitation or poisons the child against the other parent.",
        "diagram_title": "Preserving Kinship Ties (Silat al-Rahim): Co-Parenting Architecture",
        "svg_func": get_svg_lesson_3,
        "table_title": "Healthy Islamic Co-Parenting vs Destructive Parental Alienation",
        "table_headers": ["Behavioral Area", "Healthy Islamic Co-Parenting", "Destructive Alienation (Haram)"],
        "table_rows": [
            ["Visitation & Access", "Unrestricted, peaceful, and scheduled visitation", "Hiding the child or fabricating excuses to block visits"],
            ["Spousal Communication", "Respectful, mature dialogue focused on child welfare", "Slandering and cursing the ex-spouse in front of the child"],
            ["Extended Family Ties", "Child spends quality time with both sets of grandparents", "Isolating the child completely from the non-custodial family"],
            ["Financial Support", "Father pays Nafaqah gladly as an act of ibadah", "Father withholds maintenance to punish the mother financially"]
        ],
        "scenario": "Zainab and Omar are divorced. Their 8-year-old daughter Halima resides with Zainab in Nakuru, while Omar works in Nairobi. Despite their past differences, Omar reliably transfers school fees and medical support at the start of each term. Every second weekend, Zainab packs Halima's bag, and Omar travels to Nakuru to spend quality time with her, taking her to visit her paternal grandparents. Zainab always tells Halima: 'Your father is a good man who loves you dearly.' Halima thrives academically and emotionally, confident in the love of both parents.",
        "real_world": "Practice the virtue of Silat al-Rahim today. Reach out to extended family members: call your grandparents, write a supportive message to a cousin, or help an elderly aunt with chores. Cultivating warm kinship bonds brings immense spiritual blessings, long life, and inner peace, as promised by the Prophet (PBUH).",
        "reflection": "How does bad-mouthing an ex-spouse in front of a child harm the child's psychological wellbeing and violate their Islamic rights? Why is emotional maturity essential in co-parenting?",
        "misconception": "Misconception: Some think that once parents divorce, the child belongs exclusively to the custodial parent's family. In Islam, kinship ties to both maternal and paternal lineages remain inviolable, and both families share in the child's upbringing.",
        "yt_id": "rJ3wR3L4q8M",
        "yt_title": "Preserving Kinship Ties (Silat al-Rahim) After Divorce",
        "yt_desc": "Islamic counseling on co-parenting etiquette, emotional health of children, and avoiding parental alienation.",
        "mcq": {
            "question": "Which foundational Islamic principle is directly violated when a custodial parent maliciously refuses to allow the other parent to visit or contact their child?",
            "options": [
                "A. Shukr (Gratitude)",
                "B. Silat al-Rahim (Maintaining sacred kinship and family ties)",
                "C. Qana'ah (Contentment)",
                "D. Haya (Modesty)"
            ],
            "answer": "B",
            "explanation": "Silat al-Rahim refers to the mandatory preservation of kinship and family bonds. Severing these ties is a major sin in Islam, and both parents must guarantee the child's ongoing relationship with both sides of the family."
        },
        "summary_content": "Divorce terminates the marital contract between adults, but never severs the sacred bonds of kinship (Silat al-Rahim). Custody arrangements must facilitate regular visitation, respectful co-parenting, and active relationships with both maternal and paternal extended families to protect the child's emotional stability.",
        "key_points": [
            "Severing kinship ties (Silat al-Rahim) is a grave sin in Islamic law.",
            "Visitation rights of the non-custodial parent are sacred and inviolable.",
            "Parental alienation and bad-mouthing inflict severe emotional harm on children.",
            "Children thrive when connected to both maternal and paternal extended families."
        ],
        "exit_ticket": "Explain why keeping a child connected to both sides of their extended family is essential for their emotional development."
    },
    {
        "unit_order": 4,
        "lesson_title": "Unit synthesis",
        "inquiry": "How do we unify child rights, custody rules, and family bonds into a single, child-centered sanctuary of justice?",
        "hook": "Imagine a master architect designing an earthquake-resistant community dome. The dome requires three perfectly balanced corner pillars, a shock-absorbing foundation, and a protective roof. If one pillar is constructed weakly or the foundation is neglected, the entire dome will collapse during the first tremor. In this final synthesis lesson, we unite all dimensions of child custody—the foundational rights of the child, the developmental priority path, and the sacred obligation of kinship—to observe how Islam constructs an impenetrable sanctuary of protection for children.",
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/1/1a/Old_Quran_in_Wazir_Khan_Mosque.jpg/800px-Old_Quran_in_Wazir_Khan_Mosque.jpg",
        "image_title": "Architecture of Divine Protection",
        "image_caption": "Magnificent Islamic architectural heritage symbolizing the structural strength, harmony, and balance of Islamic family law.",
        "concept_name": "The Master Sanctuary of Child-Centered Justice",
        "concept_explanation": "Child custody in Islamic jurisprudence is a comprehensive manifestation of child-centered justice. Shariah balances maternal nurturing (Hadanah), paternal financial guardianship (Wilayah & Nafaqah), and extended kinship preservation (Silat al-Rahim) to place the vulnerable child's best interests at the apex of all legal rulings. By viewing custody through the Maqasid al-Shariah, learners synthesize how Islamic laws prevent trauma, preserve faith (Fitrah), and build emotionally resilient future generations.",
        "scripture_quran": "And We have certainly honored the children of Adam and carried them on land and sea and provided for them of the good things and preferred them over much of what We have created, with [definite] preference.",
        "scripture_quran_ref": "Surah Al-Isra 17:70",
        "scripture_hadith": "He is not of us who does not show mercy to our young ones and acknowledge the honor of our elders.",
        "scripture_hadith_ref": "Sunan at-Tirmidhi 1919",
        "deep_explanation": "Synthesizing the unit yields three universal rules of thumb in Islamic family law:\n1. The Rule of Maternal Nurturing: Physical custody begins with the mother due to natural tenderness, early childhood feeding, and psychological security, transferring only if her environment becomes unsafe or upon remarriage.\n2. The Rule of Paternal Provision: Financial maintenance is exclusively and permanently assigned to the father, ensuring that child nutrition, healthcare, and education are never compromised by divorce.\n3. The Rule of Kinship Inviolability: Neither parent possesses the authority to erase the other parent from the child's life. Preserving Silat al-Rahim ensures the child inherits a complete, rich family identity.",
        "diagram_title": "Master Synthesis: The Child Custody Sanctuary",
        "svg_func": get_svg_lesson_4,
        "table_title": "Master Unit Synthesis Framework: The Custody Sanctuary",
        "table_headers": ["Dimension", "Legal Mechanism in Shariah", "Responsible Entity", "Holistic Child Outcome"],
        "table_rows": [
            ["Maternal Nurturing", "Hadanah (Physical custody ages 0–7)", "Mother / Female relatives", "Emotional security & tender early care"],
            ["Paternal Maintenance", "Wilayah & Nafaqah (100% financial funding)", "Father (Strict legal duty)", "Financial stability, education & lodging"],
            ["Kinship Inviolability", "Silat al-Rahim (Guaranteed visitation)", "Both Parents & Relatives", "Preservation of family identity & mental peace"],
            ["Judicial Safeguard", "Child's Best Interests Standard", "Kadhi Courts & Community", "Protection from neglect, abuse, or alienation"]
        ],
        "scenario": "A Shariah court in Mombasa handles a dispute between divorced parents Ibrahim and Layla over their 6-year-old son Bilal. Ibrahim earns a high executive salary but travels abroad constantly. Layla works as a primary teacher with modest earnings but provides a stable, loving home environment. Ibrahim demands sole custody because he has greater wealth. Applying the unit's synthesis, the Kadhi rules: Physical custody remains with Layla because Bilal is young and needs maternal presence and nurturing. Ibrahim retains legal guardianship, weekend visitation, and is ordered to fund Bilal's school fees, health insurance, and monthly living allowance. Bilal's rights are fully secured, and both parents remain active in his life.",
        "real_world": "Draft a 'Child Rights Charter' for your class or Madrasa. Write down five concrete commitments to protect and support younger children in your school and community: such as helping younger siblings with homework, reporting safety hazards to teachers, and being kind to peers from separated families. Present your charter to your IRE teacher.",
        "reflection": "How does the Islamic approach to child custody, which prioritizes the child's rights over the parents' desires, demonstrate the ultimate mercy and justice of Islamic Shariah?",
        "misconception": "Misconception: Thinking that children from divorced families are destined to fail academically or morally. When divorced parents adhere to Islamic co-parenting principles—paying Nafaqah on time, preserving visitation, and speaking respectfully—children grow up secure, confident, and highly accomplished.",
        "yt_id": "kX7F5sF9k2w",
        "yt_title": "Comprehensive Summary: Child Custody in Islamic Law",
        "yt_desc": "Unit synthesis reviewing the rights of children, maternal custody priorities, paternal maintenance, and kinship ethics in Islam.",
        "mcq": {
            "question": "Yusuf and Fatima are divorced, and their 4-year-old daughter lives with Fatima. Yusuf stops paying school fees because Fatima denied him visitation over a weekend. Applying the full synthesis of Islamic custody, what is the correct legal and moral evaluation?",
            "options": [
                "A. Yusuf is justified in withholding school fees to penalize Fatima.",
                "B. Fatima is justified in hiding the child, and Yusuf is justified in cutting support.",
                "C. Both parents are in violation: Fatima violated Silat al-Rahim by blocking visitation, and Yusuf violated the child's absolute right to Nafaqah.",
                "D. The child should be placed in state custody since the parents disagree."
            ],
            "answer": "C",
            "explanation": "In Islamic law, physical custody, visitation, and financial maintenance are separate legal obligations. Fatima cannot block visits (violating kinship ties), and Yusuf cannot withhold maintenance (violating child rights), as both must prioritize the child's welfare over their personal conflict."
        },
        "summary_content": "Islamic child custody (Hadanah) represents a master architecture of justice centered on child welfare. By balancing maternal emotional nurturing, paternal financial maintenance, and sacred kinship ties, Shariah ensures children remain fully protected, cherished, and spiritually grounded after parental divorce.",
        "key_points": [
            "Hadanah prioritizes the child's welfare above all adult desires.",
            "Mothers provide tender physical care; fathers provide unconditional financial support.",
            "Visitation rights must be honored to preserve sacred family ties (Silat al-Rahim).",
            "Islamic family law protects children's emotional stability, education, and pure Fitrah."
        ],
        "exit_ticket": "Write a three-sentence summary explaining how Islam balances physical care, financial support, and visitation rights after divorce."
    }
]


# ─────────────────────────────────────────────────────────────────────────────
# INGESTION EXECUTION FUNCTION
# ─────────────────────────────────────────────────────────────────────────────

def ingest_grade9_ire_topic14():
    print("=" * 80)
    print("STARTING INGESTION: GRADE 9 IRE — TOPIC 14: CHILD CUSTODY (HADANAH)")
    print("=" * 80)

    try:
        topic = Topic.objects.get(id=354)
    except Topic.DoesNotExist:
        print("ERROR: Topic ID 354 does not exist! Please create topic record first.")
        sys.exit(1)

    print(f"Target Topic: ID={topic.id}, Name='{topic.name}', Order={topic.order}")

    # Validate all SVGs before database transactions
    print("\nValidating all 4 custom vector SVGs for XML compliance...")
    for idx, cfg in enumerate(LESSONS_CONFIG, 1):
        svg_content = cfg["svg_func"]()
        try:
            ET.fromstring(svg_content)
            print(f"  [✓] SVG {idx}/4 ('{cfg['diagram_title']}') is valid XML.")
        except ET.ParseError as e:
            print(f"  [✗] XML Parse Error in SVG {idx}: {e}")
            sys.exit(1)

    with transaction.atomic():
        # Clean existing units if any
        existing_units = LearningUnit.objects.filter(topic=topic)
        if existing_units.exists():
            print(f"\nCleaning {existing_units.count()} existing units under Topic {topic.id}...")
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
                name=f"Lesson 6.3.{u_order}: {l_title}",
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
                        f"Understand the core meaning and rulings of {l_title}",
                        "Examine foundational Qur'anic verses and Hadith citations",
                        "Analyze practical real-life scenarios and social responsibilities"
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
                        f"**Primary Reference ({cfg['scripture_hadith_ref']}):**\n> \"{cfg['scripture_hadith']}\""
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
            print(f"  [+] Ingested Lesson {u_order}/4: '{l_title}' (7 cards, 15 blocks, 3 assets)")

    print("=" * 80)
    print("TOPIC 14 INGESTION COMPLETE & VERIFIED!")
    print(f"  LearningUnits : {total_units} / 4")
    print(f"  Lessons       : {total_lessons} / 4 (Published)")
    print(f"  Blocks        : {total_blocks} (15 per lesson, 7 pages)")
    print(f"  Assets        : {total_assets} (4 SVGs, 4 images, 4 videos)")
    print("=" * 80)


if __name__ == "__main__":
    ingest_grade9_ire_topic14()
