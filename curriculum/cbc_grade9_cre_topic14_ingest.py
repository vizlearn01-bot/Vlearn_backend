"""
VLearn CBC Grade 9 CRE — Topic 14: Responsible Parenthood
Production-Ready Ingestion & Visual Enrichment Engine

Curriculum: CBC
Grade: Grade 9 (ID: 18)
Subject: CRE (ID: 50)
Topic: Topic 14: Responsible Parenthood (Order: 14)

6 Discrete Units / Published Lessons:
  1. Lesson 1: Understanding Family Types and Values (Psalm 127:3-5, Proverbs 22:6)
  2. Lesson 2: Responsible Parenthood and Parenting Styles (Proverbs 22:6, Proverbs 29:15)
  3. Lesson 3: Biblical Teachings on Parenting and Children's Roles (Ephesians 6:1-4, Colossians 3:20-21)
  4. Lesson 4: Problems Facing Family Life Today (Ephesians 4:31-32, Proverbs 15:18)
  5. Lesson 5: Resolving Family Conflicts: Traditional African vs. Christian Approaches (Matthew 18:15-17, Galatians 6:1-2)
  6. Lesson 6: Avoiding Unplanned Families (1 Corinthians 6:18-20, Proverbs 4:23, Proverbs 24:3-4)

Every Lesson contains:
  - 6 Cards / Pages (Discovery & Objectives, Scriptural Exegesis, Pedagogical Diagram, Practical Application, Multimedia & Reflection, Mastery Check)
  - 13 Blocks (standardized block_types: suggested_image, learning_goal, concept_explanation, suggested_diagram, step_process, suggested_video, summary, knowledge_check)
  - 3 Assets (LessonAsset objects: Image, Diagram, YouTube)
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
    Curriculum, Grade, Subject, Topic, LearningUnit, Lesson, LessonBlock, LessonAsset
)


def clean_text(text: str) -> str:
    """Removes bracket citations and internal meta tags."""
    if not text:
        return ""
    # Strip bracket citations e.g. [1], [298], [1, 2], [72, 238]
    text = re.sub(r'\[(?:\d+(?:\.\d+)?(?:,\s*\d+(?:\.\d+)?)*|image_\d+|S\d+.*?|[\d,\s]{2,})\]', '', text)
    # Strip internal pedagogical tags
    text = re.sub(r'\[(VISUAL|BIBLE PASSAGE|BIBLE REFERENCE|CRITICAL THINKING|VALUES|MISCONCEPTION|INTERACTION|ETHICAL SCENARIO|KEY VERSE|REAL WORLD APPLICATION|BIBLICAL CONTEXT|PEDAGOGICAL ARCHITECTURE|PROJECT TITLE|REFLECTION|BIBLE VERSE|RECALL|COMPREHENSION|APPLICATION)[^\]]*\]', '', text, flags=re.IGNORECASE)
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


# ─── 6 CUSTOM RESPONSIVE VECTOR SVGS (viewBox="0 0 800 450", #0f172a theme) ─────

def get_svg_lesson_1():
    return """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 450" width="100%" height="100%">
  <defs>
    <linearGradient id="bg1" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#0f172a"/>
      <stop offset="50%" stop-color="#1e293b"/>
      <stop offset="100%" stop-color="#0f172a"/>
    </linearGradient>
    <linearGradient id="goldGrad1" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#f59e0b"/>
      <stop offset="100%" stop-color="#d97706"/>
    </linearGradient>
  </defs>
  <rect width="800" height="450" fill="url(#bg1)" rx="14"/>
  <rect x="15" y="15" width="770" height="420" fill="none" stroke="#334155" stroke-width="1.5" stroke-dasharray="6 4" rx="10"/>

  <text x="400" y="45" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="17" font-weight="700" text-anchor="middle">CONTEMPORARY &amp; TRADITIONAL FAMILY STRUCTURES</text>
  <text x="400" y="68" fill="#94a3b8" font-family="system-ui, sans-serif" font-size="12" text-anchor="middle">Understanding Diverse Family Types and Communal Values in Kenya</text>

  <!-- Left Column: Core Family Structures -->
  <g transform="translate(35, 95)">
    <rect width="345" height="270" rx="10" fill="#1e293b" stroke="#38bdf8" stroke-width="1.5"/>
    <rect width="345" height="34" rx="10" fill="#0284c7"/>
    <text x="172" y="22" fill="#ffffff" font-family="system-ui, sans-serif" font-size="12" font-weight="700" text-anchor="middle">CONTEMPORARY FAMILY STRUCTURES</text>
    
    <text x="15" y="62" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="11" font-weight="700">• Nuclear Family:</text>
    <text x="15" y="78" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10">Father, mother, and biological/adopted children.</text>
    
    <text x="15" y="105" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="11" font-weight="700">• Extended Family:</text>
    <text x="15" y="121" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10">Parents, children, grandparents, uncles, aunts &amp; cousins.</text>
    
    <text x="15" y="148" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="11" font-weight="700">• Single-Parent Family:</text>
    <text x="15" y="164" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10">One parent caring for children (death, divorce, choice).</text>

    <text x="15" y="191" fill="#fbbf24" font-family="system-ui, sans-serif" font-size="11" font-weight="700">• Grandparent-Headed Family:</text>
    <text x="15" y="207" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10">Elderly grandparents raising orphaned grandchildren.</text>

    <text x="15" y="234" fill="#f43f5e" font-family="system-ui, sans-serif" font-size="11" font-weight="700">• Child-Led Family:</text>
    <text x="15" y="250" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10">Oldest sibling heading home following parents' demise.</text>
  </g>

  <!-- Right Column: Traditional African Family Values -->
  <g transform="translate(420, 95)">
    <rect width="345" height="270" rx="10" fill="#1e293b" stroke="#f59e0b" stroke-width="1.5"/>
    <rect width="345" height="34" rx="10" fill="#d97706"/>
    <text x="172" y="22" fill="#ffffff" font-family="system-ui, sans-serif" font-size="12" font-weight="700" text-anchor="middle">TRADITIONAL AFRICAN FAMILY VALUES</text>

    <text x="15" y="62" fill="#fbbf24" font-family="system-ui, sans-serif" font-size="11" font-weight="700">• Three-Dimensional Boundary:</text>
    <text x="15" y="78" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10">Encompasses the Living, the Unborn, and Ancestors.</text>

    <text x="15" y="105" fill="#fbbf24" font-family="system-ui, sans-serif" font-size="11" font-weight="700">• Communal Parenting:</text>
    <text x="15" y="121" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10">"It takes a village to raise a child" — shared guidance.</text>

    <text x="15" y="148" fill="#fbbf24" font-family="system-ui, sans-serif" font-size="11" font-weight="700">• Collective Social Security:</text>
    <text x="15" y="164" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10">Widows and orphans absorbed into clan care networks.</text>

    <text x="15" y="191" fill="#fbbf24" font-family="system-ui, sans-serif" font-size="11" font-weight="700">• Age-Based Division of Labour:</text>
    <text x="15" y="207" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10">Shared responsibilities according to maturity and strength.</text>

    <text x="15" y="234" fill="#34d399" font-family="system-ui, sans-serif" font-size="11" font-weight="700">• Sacred Continuity of Life:</text>
    <text x="15" y="250" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10">Children viewed as divine blessings preserving clan heritage.</text>
  </g>

  <rect x="150" y="380" width="500" height="32" rx="6" fill="#0f172a" stroke="#475569" stroke-width="1"/>
  <text x="400" y="401" fill="#7dd3fc" font-family="system-ui, sans-serif" font-size="11" font-weight="600" text-anchor="middle">"Children are a heritage from the Lord, offspring a reward from Him." (Psalm 127:3)</text>
</svg>"""


def get_svg_lesson_2():
    return """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 450" width="100%" height="100%">
  <defs>
    <linearGradient id="bg2" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#0f172a"/>
      <stop offset="50%" stop-color="#1e293b"/>
      <stop offset="100%" stop-color="#0f172a"/>
    </linearGradient>
  </defs>
  <rect width="800" height="450" fill="url(#bg2)" rx="14"/>
  <rect x="15" y="15" width="770" height="420" fill="none" stroke="#334155" stroke-width="1.5" stroke-dasharray="6 4" rx="10"/>

  <text x="400" y="42" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="17" font-weight="700" text-anchor="middle">THE PARENTING STYLES MATRIX &amp; DEVELOPMENTAL IMPACT</text>
  <text x="400" y="64" fill="#94a3b8" font-family="system-ui, sans-serif" font-size="12" text-anchor="middle">Balancing Parental Demandingness (Control) vs Parental Responsiveness (Warmth)</text>

  <!-- 2x2 Grid -->
  <!-- Top-Left: Authoritative / Democratic -->
  <g transform="translate(35, 85)">
    <rect width="350" height="135" rx="8" fill="#1e293b" stroke="#34d399" stroke-width="2"/>
    <rect width="350" height="28" rx="8" fill="#059669"/>
    <text x="175" y="19" fill="#ffffff" font-family="system-ui, sans-serif" font-size="12" font-weight="700" text-anchor="middle">AUTHORITATIVE / DEMOCRATIC (IDEAL)</text>
    <text x="15" y="48" fill="#34d399" font-family="system-ui, sans-serif" font-size="10.5" font-weight="700">High Warmth + High Demandingness / Standards</text>
    <text x="15" y="66" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10">• Sets clear boundaries, explains the reason behind rules.</text>
    <text x="15" y="82" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10">• Listens to children's opinions and fosters open dialogue.</text>
    <text x="15" y="100" fill="#7dd3fc" font-family="system-ui, sans-serif" font-size="10" font-weight="600">Outcome: Confident, self-disciplined, high academic achievement.</text>
    <text x="15" y="118" fill="#6ee7b7" font-family="system-ui, sans-serif" font-size="9.5">✓ Recommended Biblical &amp; Pedagogical Model</text>
  </g>

  <!-- Top-Right: Authoritarian / Autocratic -->
  <g transform="translate(415, 85)">
    <rect width="350" height="135" rx="8" fill="#1e293b" stroke="#f43f5e" stroke-width="1.5"/>
    <rect width="350" height="28" rx="8" fill="#be123c"/>
    <text x="175" y="19" fill="#ffffff" font-family="system-ui, sans-serif" font-size="12" font-weight="700" text-anchor="middle">AUTHORITARIAN / AUTOCRATIC</text>
    <text x="15" y="48" fill="#fca5a5" font-family="system-ui, sans-serif" font-size="10.5" font-weight="700">Low Warmth + High Demandingness / Control</text>
    <text x="15" y="66" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10">• Imposes strict rules without explanation; "Because I said so!"</text>
    <text x="15" y="82" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10">• Relies heavily on punishment and demands blind obedience.</text>
    <text x="15" y="100" fill="#fca5a5" font-family="system-ui, sans-serif" font-size="10" font-weight="600">Outcome: Anxious, low self-esteem, rebellion outside home.</text>
    <text x="15" y="118" fill="#f87171" font-family="system-ui, sans-serif" font-size="9.5">⚠️ Provokes resentment and discouragement (Col 3:21)</text>
  </g>

  <!-- Bottom-Left: Permissive / Indulgent -->
  <g transform="translate(35, 235)">
    <rect width="350" height="135" rx="8" fill="#1e293b" stroke="#f59e0b" stroke-width="1.5"/>
    <rect width="350" height="28" rx="8" fill="#d97706"/>
    <text x="175" y="19" fill="#ffffff" font-family="system-ui, sans-serif" font-size="12" font-weight="700" text-anchor="middle">PERMISSIVE / INDULGENT (LAISSEZ-FAIRE)</text>
    <text x="15" y="48" fill="#fde68a" font-family="system-ui, sans-serif" font-size="10.5" font-weight="700">High Warmth + Low Demandingness / Boundaries</text>
    <text x="15" y="66" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10">• Very lenient with few rules, avoids confrontation or discipline.</text>
    <text x="15" y="82" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10">• Acts like a peer rather than an authoritative parent.</text>
    <text x="15" y="100" fill="#fde68a" font-family="system-ui, sans-serif" font-size="10" font-weight="600">Outcome: Poor self-regulation, entitlement, impulse control issues.</text>
    <text x="15" y="118" fill="#fbbf24" font-family="system-ui, sans-serif" font-size="9.5">⚠️ "A child left undisciplined disgraces its mother" (Prov 29:15)</text>
  </g>

  <!-- Bottom-Right: Neglectful / Uninvolved -->
  <g transform="translate(415, 235)">
    <rect width="350" height="135" rx="8" fill="#1e293b" stroke="#64748b" stroke-width="1.5"/>
    <rect width="350" height="28" rx="8" fill="#475569"/>
    <text x="175" y="19" fill="#ffffff" font-family="system-ui, sans-serif" font-size="12" font-weight="700" text-anchor="middle">NEGLECTFUL / UNINVOLVED</text>
    <text x="15" y="48" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10.5" font-weight="700">Low Warmth + Low Demandingness (Absence)</text>
    <text x="15" y="66" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10">• Emotionally or physically absent, detached from child's life.</text>
    <text x="15" y="82" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10">• Provides minimal basic needs with no emotional support.</text>
    <text x="15" y="100" fill="#fca5a5" font-family="system-ui, sans-serif" font-size="10" font-weight="600">Outcome: Severe behavioral issues, depression, substance risk.</text>
    <text x="15" y="118" fill="#94a3b8" font-family="system-ui, sans-serif" font-size="9.5">❌ Complete failure of responsible parenthood mandate</text>
  </g>

  <rect x="150" y="385" width="500" height="32" rx="6" fill="#0f172a" stroke="#475569" stroke-width="1"/>
  <text x="400" y="406" fill="#7dd3fc" font-family="system-ui, sans-serif" font-size="11" font-weight="600" text-anchor="middle">"Start children off on the way they should go, and when they are old they will not turn." (Prov 22:6)</text>
</svg>"""


def get_svg_lesson_3():
    return """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 450" width="100%" height="100%">
  <defs>
    <linearGradient id="bg3" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#0f172a"/>
      <stop offset="50%" stop-color="#1e293b"/>
      <stop offset="100%" stop-color="#0f172a"/>
    </linearGradient>
    <linearGradient id="covenantGrad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#38bdf8"/>
      <stop offset="100%" stop-color="#0284c7"/>
    </linearGradient>
  </defs>
  <rect width="800" height="450" fill="url(#bg3)" rx="14"/>
  <rect x="15" y="15" width="770" height="420" fill="none" stroke="#334155" stroke-width="1.5" stroke-dasharray="6 4" rx="10"/>

  <text x="400" y="45" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="17" font-weight="700" text-anchor="middle">THE RECIPROCAL BIBLICAL COVENANT OF FAMILY LIFE</text>
  <text x="400" y="68" fill="#94a3b8" font-family="system-ui, sans-serif" font-size="12" text-anchor="middle">Ephesians 6:1-4 &amp; Colossians 3:20-21 — Mutual Duties Grounded in God's Grace</text>

  <!-- Left: Parent's Biblical Mandate -->
  <g transform="translate(35, 95)">
    <rect width="335" height="265" rx="10" fill="#1e293b" stroke="#38bdf8" stroke-width="1.5"/>
    <rect width="335" height="34" rx="10" fill="#0284c7"/>
    <text x="167" y="22" fill="#ffffff" font-family="system-ui, sans-serif" font-size="12" font-weight="700" text-anchor="middle">PARENTAL RESPONSIBILITIES (Eph 6:4)</text>

    <text x="15" y="62" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="11" font-weight="700">1. Spiritual Nurture &amp; Catechesis:</text>
    <text x="15" y="78" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10">Teach God's commandments diligently (Deut 11:19).</text>

    <text x="15" y="108" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="11" font-weight="700">2. Loving, Constructive Discipline:</text>
    <text x="15" y="124" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10">Correct behavior in love without wrath or abuse.</text>

    <text x="15" y="154" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="11" font-weight="700">3. Providing Holistic Needs:</text>
    <text x="15" y="170" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10">Food, clothing, shelter, healthcare, and education.</text>

    <text x="15" y="200" fill="#f43f5e" font-family="system-ui, sans-serif" font-size="11" font-weight="700">4. Avoiding Provocation &amp; Bitterness:</text>
    <text x="15" y="216" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10">Never discourage or embitter children harshly (Col 3:21).</text>

    <text x="15" y="246" fill="#34d399" font-family="system-ui, sans-serif" font-size="10.5" font-weight="600">✓ Stewardship of God's Trust</text>
  </g>

  <!-- Right: Child's Biblical Mandate -->
  <g transform="translate(430, 95)">
    <rect width="335" height="265" rx="10" fill="#1e293b" stroke="#f59e0b" stroke-width="1.5"/>
    <rect width="335" height="34" rx="10" fill="#d97706"/>
    <text x="167" y="22" fill="#ffffff" font-family="system-ui, sans-serif" font-size="12" font-weight="700" text-anchor="middle">CHILDREN'S RESPONSIBILITIES (Eph 6:1-3)</text>

    <text x="15" y="62" fill="#fbbf24" font-family="system-ui, sans-serif" font-size="11" font-weight="700">1. Obedience in the Lord:</text>
    <text x="15" y="78" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10">Obey parents in all things, for this pleases God.</text>

    <text x="15" y="108" fill="#fbbf24" font-family="system-ui, sans-serif" font-size="11" font-weight="700">2. Honor and Reverence:</text>
    <text x="15" y="124" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10">Treat parents with dignity, politeness, and high esteem.</text>

    <text x="15" y="154" fill="#fbbf24" font-family="system-ui, sans-serif" font-size="11" font-weight="700">3. Active Household Cooperation:</text>
    <text x="15" y="170" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10">Perform household chores faithfully without grumbling.</text>

    <text x="15" y="200" fill="#fbbf24" font-family="system-ui, sans-serif" font-size="11" font-weight="700">4. Support in Aging &amp; Vulnerability:</text>
    <text x="15" y="216" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10">Care for elderly parents physically and financially.</text>

    <text x="15" y="246" fill="#34d399" font-family="system-ui, sans-serif" font-size="10.5" font-weight="600">✓ First Commandment with a Promise: Long Life</text>
  </g>

  <!-- Central Bridge -->
  <path d="M 370 230 L 430 230" stroke="#38bdf8" stroke-width="3" stroke-dasharray="4 2"/>

  <rect x="150" y="380" width="500" height="32" rx="6" fill="#0f172a" stroke="#475569" stroke-width="1"/>
  <text x="400" y="401" fill="#7dd3fc" font-family="system-ui, sans-serif" font-size="11" font-weight="600" text-anchor="middle">"Honor your father and mother — that it may go well with you and you may enjoy long life." (Eph 6:2-3)</text>
</svg>"""


def get_svg_lesson_4():
    return """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 450" width="100%" height="100%">
  <defs>
    <linearGradient id="bg4" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#0f172a"/>
      <stop offset="50%" stop-color="#1e293b"/>
      <stop offset="100%" stop-color="#0f172a"/>
    </linearGradient>
  </defs>
  <rect width="800" height="450" fill="url(#bg4)" rx="14"/>
  <rect x="15" y="15" width="770" height="420" fill="none" stroke="#334155" stroke-width="1.5" stroke-dasharray="6 4" rx="10"/>

  <text x="400" y="42" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="17" font-weight="700" text-anchor="middle">MODERN FAMILY PRESSURES &amp; CHRISTIAN RESILIENCE</text>
  <text x="400" y="64" fill="#94a3b8" font-family="system-ui, sans-serif" font-size="12" text-anchor="middle">Overcoming Contemporary Social, Economic, and Psychological Challenges (Ephesians 4:31-32)</text>

  <!-- Left: Threat Vectors -->
  <g transform="translate(35, 85)">
    <rect width="345" height="280" rx="10" fill="#1e293b" stroke="#f43f5e" stroke-width="1.5"/>
    <rect width="345" height="32" rx="10" fill="#be123c"/>
    <text x="172" y="21" fill="#ffffff" font-family="system-ui, sans-serif" font-size="11.5" font-weight="700" text-anchor="middle">CONTEMPORARY CHALLENGES / PRESSURES</text>

    <text x="15" y="56" fill="#fca5a5" font-family="system-ui, sans-serif" font-size="10.5" font-weight="700">• Economic Crisis &amp; Retrenchment:</text>
    <text x="15" y="70" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="9.5">Unemployment, inflation, inability to pay school fees.</text>

    <text x="15" y="96" fill="#fca5a5" font-family="system-ui, sans-serif" font-size="10.5" font-weight="700">• Substance &amp; Alcohol Abuse:</text>
    <text x="15" y="110" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="9.5">Squandering household wealth, triggering domestic violence.</text>

    <text x="15" y="136" fill="#fca5a5" font-family="system-ui, sans-serif" font-size="10.5" font-weight="700">• Domestic Violence &amp; Child Abuse:</text>
    <text x="15" y="150" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="9.5">Physical battering, emotional cruelty, and exploitation.</text>

    <text x="15" y="176" fill="#fca5a5" font-family="system-ui, sans-serif" font-size="10.5" font-weight="700">• Generation Gap &amp; Digital Friction:</text>
    <text x="15" y="190" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="9.5">Misunderstandings over tech, values, and peer pressure.</text>

    <text x="15" y="216" fill="#fca5a5" font-family="system-ui, sans-serif" font-size="10.5" font-weight="700">• Chronic Illness &amp; Infertility:</text>
    <text x="15" y="230" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="9.5">HIV/AIDS stigma, medical bills, childlessness tensions.</text>

    <text x="15" y="256" fill="#fca5a5" font-family="system-ui, sans-serif" font-size="10.5" font-weight="700">• In-Law &amp; Relatives Interference:</text>
    <text x="15" y="270" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="9.5">Unsolicited meddling destabilizing marital harmony.</text>
  </g>

  <!-- Right: Protective Pillars of Resilience -->
  <g transform="translate(420, 85)">
    <rect width="345" height="280" rx="10" fill="#1e293b" stroke="#34d399" stroke-width="1.5"/>
    <rect width="345" height="32" rx="10" fill="#059669"/>
    <text x="172" y="21" fill="#ffffff" font-family="system-ui, sans-serif" font-size="11.5" font-weight="700" text-anchor="middle">CHRISTIAN PILLARS OF FAMILY RESILIENCE</text>

    <text x="15" y="56" fill="#6ee7b7" font-family="system-ui, sans-serif" font-size="10.5" font-weight="700">• Radical Forgiveness (Eph 4:32):</text>
    <text x="15" y="70" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="9.5">Renouncing bitterness, rage, slander, and malicious vengeance.</text>

    <text x="15" y="96" fill="#6ee7b7" font-family="system-ui, sans-serif" font-size="10.5" font-weight="700">• Mutual Patience &amp; Tolerance:</text>
    <text x="15" y="110" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="9.5">Bearing with each other during financial and emotional crises.</text>

    <text x="15" y="136" fill="#6ee7b7" font-family="system-ui, sans-serif" font-size="10.5" font-weight="700">• Transparent Financial Stewardship:</text>
    <text x="15" y="150" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="9.5">Joint budgeting, eliminating secrecy, prioritizing essentials.</text>

    <text x="15" y="176" fill="#6ee7b7" font-family="system-ui, sans-serif" font-size="10.5" font-weight="700">• Open Empathetic Communication:</text>
    <text x="15" y="190" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="9.5">Bridging generational gaps through dialogue, not shouting.</text>

    <text x="15" y="216" fill="#6ee7b7" font-family="system-ui, sans-serif" font-size="10.5" font-weight="700">• Community &amp; Church Support:</text>
    <text x="15" y="230" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="9.5">Seeking pastoral counseling, support groups, and prayer.</text>

    <text x="15" y="256" fill="#6ee7b7" font-family="system-ui, sans-serif" font-size="10.5" font-weight="700">• Legal &amp; Institutional Safeguards:</text>
    <text x="15" y="270" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="9.5">Legal protection against violence and drafting valid wills.</text>
  </g>

  <rect x="150" y="382" width="500" height="32" rx="6" fill="#0f172a" stroke="#475569" stroke-width="1"/>
  <text x="400" y="403" fill="#7dd3fc" font-family="system-ui, sans-serif" font-size="11" font-weight="600" text-anchor="middle">"Be kind and compassionate to one another, forgiving each other, as in Christ God forgave you." (Eph 4:32)</text>
</svg>"""


def get_svg_lesson_5():
    return """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 450" width="100%" height="100%">
  <defs>
    <linearGradient id="bg5" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#0f172a"/>
      <stop offset="50%" stop-color="#1e293b"/>
      <stop offset="100%" stop-color="#0f172a"/>
    </linearGradient>
  </defs>
  <rect width="800" height="450" fill="url(#bg5)" rx="14"/>
  <rect x="15" y="15" width="770" height="420" fill="none" stroke="#334155" stroke-width="1.5" stroke-dasharray="6 4" rx="10"/>

  <text x="400" y="45" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="17" font-weight="700" text-anchor="middle">RESOLVING FAMILY CONFLICTS: DUAL PATHWAYS TO PEACE</text>
  <text x="400" y="68" fill="#94a3b8" font-family="system-ui, sans-serif" font-size="12" text-anchor="middle">Traditional African Arbitration vs Christian Ministry &amp; Legal Resolution Models</text>

  <!-- Left Column: Traditional African Model -->
  <g transform="translate(35, 95)">
    <rect width="345" height="265" rx="10" fill="#1e293b" stroke="#f59e0b" stroke-width="1.5"/>
    <rect width="345" height="34" rx="10" fill="#d97706"/>
    <text x="172" y="22" fill="#ffffff" font-family="system-ui, sans-serif" font-size="12" font-weight="700" text-anchor="middle">TRADITIONAL AFRICAN PATHWAY</text>

    <text x="15" y="62" fill="#fbbf24" font-family="system-ui, sans-serif" font-size="11" font-weight="700">• Clan Elders Arbitration:</text>
    <text x="15" y="78" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10">Respected uncles, aunts, and elders hear disputes.</text>

    <text x="15" y="108" fill="#fbbf24" font-family="system-ui, sans-serif" font-size="11" font-weight="700">• Customary Mediation &amp; Fines:</text>
    <text x="15" y="124" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10">Reconciliatory rituals, shared meals, and symbolic fines.</text>

    <text x="15" y="154" fill="#fbbf24" font-family="system-ui, sans-serif" font-size="11" font-weight="700">• Early Initiation Preparation:</text>
    <text x="15" y="170" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10">Teaching conflict resolution skills prior to marriage.</text>

    <text x="15" y="200" fill="#fbbf24" font-family="system-ui, sans-serif" font-size="11" font-weight="700">• Communal Safety Net:</text>
    <text x="15" y="216" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10">Widow support and extended family collective care.</text>

    <text x="15" y="246" fill="#34d399" font-family="system-ui, sans-serif" font-size="10.5" font-weight="600">Goal: Clan Solidarity &amp; Communal Harmony</text>
  </g>

  <!-- Right Column: Christian Ministry & Legal Model -->
  <g transform="translate(420, 95)">
    <rect width="345" height="265" rx="10" fill="#1e293b" stroke="#38bdf8" stroke-width="1.5"/>
    <rect width="345" height="34" rx="10" fill="#0284c7"/>
    <text x="172" y="22" fill="#ffffff" font-family="system-ui, sans-serif" font-size="12" font-weight="700" text-anchor="middle">CHRISTIAN &amp; LEGAL PATHWAY</text>

    <text x="15" y="62" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="11" font-weight="700">• Biblical Peacemaking (Matt 18:15):</text>
    <text x="15" y="78" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10">Private confrontation → Trusted mediators → Church counsel.</text>

    <text x="15" y="108" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="11" font-weight="700">• Professional Pastoral Counseling:</text>
    <text x="15" y="124" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10">Pre-marital and marriage seminars, youth mentorship.</text>

    <text x="15" y="154" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="11" font-weight="700">• Church Fellowship Support:</text>
    <text x="15" y="170" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10">Mothers' Union, Men's Guild, and youth fellowships.</text>

    <text x="15" y="200" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="11" font-weight="700">• Legal Protection &amp; Written Wills:</text>
    <text x="15" y="216" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10">Court intervention for abuse; wills to avert inheritance feuds.</text>

    <text x="15" y="246" fill="#34d399" font-family="system-ui, sans-serif" font-size="10.5" font-weight="600">Goal: Spiritual Healing, Justice &amp; Reconciliation</text>
  </g>

  <rect x="150" y="380" width="500" height="32" rx="6" fill="#0f172a" stroke="#475569" stroke-width="1"/>
  <text x="400" y="401" fill="#7dd3fc" font-family="system-ui, sans-serif" font-size="11" font-weight="600" text-anchor="middle">"Carry each other's burdens, and in this way you will fulfill the law of Christ." (Galatians 6:2)</text>
</svg>"""


def get_svg_lesson_6():
    return """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 450" width="100%" height="100%">
  <defs>
    <linearGradient id="bg6" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#0f172a"/>
      <stop offset="50%" stop-color="#1e293b"/>
      <stop offset="100%" stop-color="#0f172a"/>
    </linearGradient>
    <linearGradient id="shieldGrad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#0284c7"/>
      <stop offset="100%" stop-color="#0369a1"/>
    </linearGradient>
  </defs>
  <rect width="800" height="450" fill="url(#bg6)" rx="14"/>
  <rect x="15" y="15" width="770" height="420" fill="none" stroke="#334155" stroke-width="1.5" stroke-dasharray="6 4" rx="10"/>

  <text x="400" y="42" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="17" font-weight="700" text-anchor="middle">THE PURITY SHIELD &amp; LIFE DECISION BLUEPRINT</text>
  <text x="400" y="64" fill="#94a3b8" font-family="system-ui, sans-serif" font-size="12" text-anchor="middle">Guarding Your Heart, Practicing Self-Control, and Securing Your Future (1 Cor 6:18-20)</text>

  <!-- Left: Threat Inflows Deflected -->
  <g transform="translate(35, 90)">
    <rect width="210" height="270" rx="8" fill="#1e293b" stroke="#f43f5e" stroke-width="1.5"/>
    <rect width="210" height="28" rx="8" fill="#be123c"/>
    <text x="105" y="19" fill="#ffffff" font-family="system-ui, sans-serif" font-size="11" font-weight="700" text-anchor="middle">DEFLECTED PRESSURES</text>

    <text x="12" y="55" fill="#fca5a5" font-family="system-ui, sans-serif" font-size="10.5" font-weight="700">❌ Negative Peer Pressure</text>
    <text x="12" y="70" fill="#94a3b8" font-family="system-ui, sans-serif" font-size="9.5">"Everyone is doing it"</text>

    <text x="12" y="100" fill="#fca5a5" font-family="system-ui, sans-serif" font-size="10.5" font-weight="700">❌ Uncontrolled Media</text>
    <text x="12" y="115" fill="#94a3b8" font-family="system-ui, sans-serif" font-size="9.5">Pornography &amp; toxic music</text>

    <text x="12" y="145" fill="#fca5a5" font-family="system-ui, sans-serif" font-size="10.5" font-weight="700">❌ Premature Romance</text>
    <text x="12" y="160" fill="#94a3b8" font-family="system-ui, sans-serif" font-size="9.5">Early sexual compromise</text>

    <text x="12" y="190" fill="#fca5a5" font-family="system-ui, sans-serif" font-size="10.5" font-weight="700">❌ Idleness &amp; Boredom</text>
    <text x="12" y="205" fill="#94a3b8" font-family="system-ui, sans-serif" font-size="9.5">Vulnerability to bad company</text>

    <text x="12" y="235" fill="#fca5a5" font-family="system-ui, sans-serif" font-size="10.5" font-weight="700">❌ Unplanned Pregnancy</text>
    <text x="12" y="250" fill="#94a3b8" font-family="system-ui, sans-serif" font-size="9.5">Disrupted school &amp; career</text>
  </g>

  <!-- Center: The Core Purity Shield -->
  <g transform="translate(265, 80)">
    <!-- Shield Shape -->
    <path d="M 135 15 L 250 50 L 250 180 C 250 250, 135 290, 135 290 C 135 290, 20 250, 20 180 L 20 50 Z" fill="url(#shieldGrad)" stroke="#38bdf8" stroke-width="2.5"/>
    <text x="135" y="65" fill="#ffffff" font-family="system-ui, sans-serif" font-size="13" font-weight="800" text-anchor="middle">PURITY SHIELD</text>
    <text x="135" y="85" fill="#bae6fd" font-family="system-ui, sans-serif" font-size="10" font-weight="600" text-anchor="middle">Core Virtues &amp; Life Skills</text>

    <rect x="40" y="105" width="190" height="24" rx="4" fill="#0f172a"/>
    <text x="135" y="121" fill="#34d399" font-family="system-ui, sans-serif" font-size="10" font-weight="700" text-anchor="middle">1. SELF-CONTROL (Gal 5:23)</text>

    <rect x="40" y="135" width="190" height="24" rx="4" fill="#0f172a"/>
    <text x="135" y="151" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="10" font-weight="700" text-anchor="middle">2. ASSERTIVENESS ("NO!")</text>

    <rect x="40" y="165" width="190" height="24" rx="4" fill="#0f172a"/>
    <text x="135" y="181" fill="#fbbf24" font-family="system-ui, sans-serif" font-size="10" font-weight="700" text-anchor="middle">3. HIGH SELF-ESTEEM</text>

    <rect x="40" y="195" width="190" height="24" rx="4" fill="#0f172a"/>
    <text x="135" y="211" fill="#e2e8f0" font-family="system-ui, sans-serif" font-size="10" font-weight="700" text-anchor="middle">4. CRITICAL THINKING</text>

    <rect x="40" y="225" width="190" height="24" rx="4" fill="#0f172a"/>
    <text x="135" y="241" fill="#f43f5e" font-family="system-ui, sans-serif" font-size="10" font-weight="700" text-anchor="middle">5. SEXUAL ABSTINENCE</text>
  </g>

  <!-- Right: Future Promised Pathway -->
  <g transform="translate(555, 90)">
    <rect width="210" height="270" rx="8" fill="#1e293b" stroke="#34d399" stroke-width="1.5"/>
    <rect width="210" height="28" rx="8" fill="#059669"/>
    <text x="105" y="19" fill="#ffffff" font-family="system-ui, sans-serif" font-size="11" font-weight="700" text-anchor="middle">FUTURE PROMISES</text>

    <text x="12" y="55" fill="#6ee7b7" font-family="system-ui, sans-serif" font-size="10.5" font-weight="700">✓ Academic Excellence</text>
    <text x="12" y="70" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="9.5">Uninterrupted learning</text>

    <text x="12" y="100" fill="#6ee7b7" font-family="system-ui, sans-serif" font-size="10.5" font-weight="700">✓ Career Fulfillment</text>
    <text x="12" y="115" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="9.5">Achieving life dreams</text>

    <text x="12" y="145" fill="#6ee7b7" font-family="system-ui, sans-serif" font-size="10.5" font-weight="700">✓ Emotional Wholeness</text>
    <text x="12" y="160" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="9.5">Free from guilt and regrets</text>

    <text x="12" y="190" fill="#6ee7b7" font-family="system-ui, sans-serif" font-size="10.5" font-weight="700">✓ Responsible Parenthood</text>
    <text x="12" y="205" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="9.5">Prepared marriage in God's timing</text>

    <text x="12" y="235" fill="#6ee7b7" font-family="system-ui, sans-serif" font-size="10.5" font-weight="700">✓ God's Eternal Favor</text>
    <text x="12" y="250" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="9.5">Body honored as Temple</text>
  </g>

  <rect x="150" y="382" width="500" height="32" rx="6" fill="#0f172a" stroke="#475569" stroke-width="1"/>
  <text x="400" y="403" fill="#7dd3fc" font-family="system-ui, sans-serif" font-size="11" font-weight="600" text-anchor="middle">"Above all else, guard your heart, for everything you do flows from it." (Proverbs 4:23)</text>
</svg>"""


# ─── LESSON DATA CONFIGURATIONS (6 LESSONS) ───────────────────────────────────

LESSONS_DATA = [
    # ─── LESSON 1 ────────────────────────────────────────────────────────────
    {
        "unit_order": 1,
        "unit_name": "Understanding Family Types and Values",
        "unit_description": "Examine contemporary family structures including nuclear, extended, single-parent, grandparent-headed, and child-led units, contrasting them with traditional African communal values.",
        "lesson_title": "Understanding Family Types and Values",
        "image": {
            "url": "https://upload.wikimedia.org/wikipedia/commons/thumb/c/c5/Cornelis_de_Vos_-_Family_portrait.jpg/1280px-Cornelis_de_Vos_-_Family_portrait.jpg",
            "title": "Visual Hook: Multi-Generational Family Portrait",
            "author": "Cornelis de Vos (Royal Museum of Fine Arts Antwerp)",
            "licensing": "Public Domain",
            "source": "Wikimedia Commons",
            "caption": "A portrait illustrating the family unit as the foundational building block of society, uniting generations in shared love, identity, and moral responsibility."
        },
        "youtube": {
            "youtube_id": "k1nLzR9k45c",
            "title": "BibleProject: The Meaning of Blessing & Family in Scripture",
            "description": "An engaging biblical overview of how God established families to reflect His covenant love, nurture future generations, and extend blessings across clans."
        },
        "goals": [
            "Identify and distinguish between modern family structures (nuclear, extended, single-parent, grandparent-headed, child-led).",
            "Explain the three-dimensional boundary and communal parenting values in Traditional African Society.",
            "Demonstrate practical empathy, solidarity, and responsibility toward peers from vulnerable or non-traditional family setups."
        ],
        "intro": """Think about the people who share your home every day. Do you live with your father, mother, and siblings? Or do you share your compound with grandparents, aunts, uncles, and cousins? In Kenya today, many young people live in single-parent homes, are raised with deep devotion by elderly grandparents, or bravely head households as older siblings.

The family is the foundational building block of human society. Across history, families have evolved in structure due to urbanization, economic shifts, and medical challenges like HIV/AIDS. Despite these structural changes, the underlying spiritual calling of the family remains constant: to provide unconditional love, moral identity, protection, and mutual support.""",
        "core_scripture": """### Psalm 127:3-5 & Ephesians 3:14-15 (NIV)

> **Psalm 127:3-5:**
> "Children are a heritage from the Lord, offspring a reward from him. Like arrows in the hands of a warrior are children born in one’s youth. Blessed is the man whose quiver is full of them. They will not be put to shame when they contend with their opponents in court."
>
> **Ephesians 3:14-15:**
> "For this reason I kneel before the Father, from whom every family in heaven and on earth derives its name."
>
> **Psalms 103:13:**
> "As a father has compassion on his children, so the Lord has compassion on those who fear him." """,
        "theological_pillars": """### Theological Exegesis & Analysis

1. **Children as a Divine Heritage (Psalm 127:3):**
   Scripture unequivocally establishes that children are not economic commodities, personal trophies, or accidental burdens. They are a *heritage* (*nachalah*)—a sacred divine trust entrusted to parents by God.

2. **The Warrior's Arrows (Psalm 127:4-5):**
   The metaphor of arrows in a warrior's hand underscores intentionality in parenting. An arrow must be carefully shaped, feathered, and aimed with precision. Parents are called to aim their children toward righteousness, moral courage, and public justice.

3. **The Ultimate Source of Family Identity (Ephesians 3:14-15):**
   Paul reveals that all human fatherhood and family structures derive their name and authentic purpose from God the Father. Every earthly family is called to mirror God's compassionate, steadfast, and protective character.""",
        "svg_fn": get_svg_lesson_1,
        "deep_dive": """### Deep Dive: Contemporary Family Structures vs. Traditional African Values

#### 1. Contemporary Family Typology
- **Nuclear Family:** Comprises two parents (father and mother) and their biological or legally adopted children. Predominant in urban centres due to housing constraints and high living costs.
- **Extended Family:** Encompasses parents, children, grandparents, uncles, aunts, in-laws, and cousins. Historically the bedrock of communal African life.
- **Single-Parent Family:** Headed by one parent caring for children, arising from bereavement, separation, divorce, or intentional single parenthood.
- **Grandparent-Headed Family:** Elderly grandparents stepping in to raise grandchildren. Highly prevalent in sub-Saharan Africa due to the impact of the HIV/AIDS epidemic and parental migration.
- **Child-Led Family:** A household where both parents are deceased, and the eldest sibling (often an adolescent) assumes parental responsibility over younger brothers and sisters.

#### 2. Traditional African Family Values
In Traditional African Society, the family was a sacred, eternal institution defined across three dimensions:
1. **The Living:** Current household and clan members interacting daily.
2. **The Unborn:** Future generations whose continuity depends on honorable marriages and moral preservation.
3. **The Living-Dead (Ancestors):** Revered forebears who guard cultural norms and spiritual balance.

**Key Traditional Pillars:**
- **Communal Parenting:** *"It takes a whole village to raise a child."* Every adult in the community exercised parental authority, instilling discipline, ethical values, and craftsmanship.
- **Shared Economic Solidarity:** Age-based division of labour ensured food security, livestock protection, and mutual survival without leaving vulnerable members destitute.""",
        "practical": {
            "title": "Action Framework: Practicing Solidarity with Diverse Families",
            "steps": [
                {
                    "step": 1,
                    "title": "Acknowledge and Respect Diversity",
                    "description": "Recognize that God loves and values every family setup regardless of whether it is nuclear, single-parent, grandparent-headed, or child-led."
                },
                {
                    "step": 2,
                    "title": "Eliminate Stigma and Exclusion",
                    "description": "Never tease, isolate, or look down upon peers whose families have suffered loss, divorce, or financial distress."
                },
                {
                    "step": 3,
                    "title": "Extend Practical Material Support",
                    "description": "Share school stationery, textbooks, and extra food with classmates from vulnerable households or child-led homes."
                },
                {
                    "step": 4,
                    "title": "Build Study and Emotional Support Networks",
                    "description": "Invite peers from struggling households into collaborative group revisions and spiritual fellowships to foster belonging."
                }
            ]
        },
        "kenyan_context": """### Kenyan Real-World Context & Cultural Integration

In Kenya, social transformations—including rapid rural-to-urban migration, industrialization, and medical crises—have altered the traditional extended family safety net. In many informal urban settlements and rural villages, grandparent-headed and child-led households face acute economic hardship.

CBC values call on learners to revive the core traditional ethos of *Utu* (human dignity) and Christian charity. In Kenyan schools, Christian Unions and guidance clubs actively provide peer mentoring, communal welfare drives, and academic assistance to ensure no child is left behind due to family vulnerability.""",
        "reflection": """### Spiritual Reflection & Values

God did not design us to exist in isolation. Whether your family is large or small, complete or experiencing loss, God's promise is to be "a father to the fatherless and a defender of widows" (Psalm 68:5). 

Take a moment to thank God for the guardians, parents, or mentors who have provided for you. How can you demonstrate genuine gratitude today by lifting household burdens and respecting your elders?""",
        "takeaways": [
            "The family is the fundamental building block of society established by God to provide love, nurture, and moral instruction.",
            "Contemporary family setups include nuclear, extended, single-parent, grandparent-headed, and child-led families.",
            "In Traditional African Society, family boundaries encompassed the living, the unborn, and ancestors under a communal parenting model.",
            "HIV/AIDS and socioeconomic migration have increased the prevalence of grandparent-headed and child-led households in Kenya.",
            "Christian discipleship requires showing active empathy, responsibility, and material solidarity with vulnerable family structures."
        ],
        "mcq": {
            "question": "Which type of family structure has become significantly prevalent in Kenya due to the devastating loss of parents to terminal illnesses like HIV/AIDS?",
            "options": [
                "Polygamous family",
                "Grandparent-headed family",
                "Nuclear family",
                "Monastic family"
            ],
            "correct_answer": "Grandparent-headed family",
            "explanation": "The HIV/AIDS pandemic and other terminal illnesses left many children orphaned, prompting resilient grandparents to step in as primary caregivers to head households and raise their grandchildren."
        }
    },

    # ─── LESSON 2 ────────────────────────────────────────────────────────────
    {
        "unit_order": 2,
        "unit_name": "Responsible Parenthood and Parenting Styles",
        "unit_description": "Define responsible parenthood and evaluate the four major parenting styles—authoritative/democratic, authoritarian/autocratic, permissive/indulgent, and neglectful—analyzing their developmental outcomes.",
        "lesson_title": "Responsible Parenthood and Parenting Styles",
        "image": {
            "url": "https://upload.wikimedia.org/wikipedia/commons/thumb/4/4b/Mary_Cassatt_-_Mother_and_Child_%281890%29.jpg/800px-Mary_Cassatt_-_Mother_and_Child_%281890%29.jpg",
            "title": "Visual Hook: Nurturing Mother and Child",
            "author": "Mary Cassatt (Wichita Art Museum Collection)",
            "licensing": "Public Domain",
            "source": "Wikimedia Commons",
            "caption": "A classic artistic depiction of parental tenderness, vigilance, and moral guidance in early childhood development."
        },
        "youtube": {
            "youtube_id": "az_EI9kZ_18",
            "title": "BibleProject: Wisdom & The Book of Proverbs",
            "description": "An exploration of how biblical wisdom in Proverbs provides timeless principles for intentional parenting, discipline, and character formation."
        },
        "goals": [
            "Define responsible parenthood across physical, spiritual, intellectual, emotional, and social dimensions.",
            "Compare and contrast the four primary parenting styles (Authoritative, Authoritarian, Permissive, Neglectful).",
            "Assess the developmental and psychological outcomes of different parenting approaches on adolescent behavior."
        ],
        "intro": """Consider how decisions and rules are established in your home. When you wish to visit friends or attend an extracurricular event, does your parent discuss the expectations with you, or are you met with an unexplained 'No!'? Do some homes have no rules at all where teenagers do whatever they wish?

Parenting is never an accidental undertaking. It is a deliberate, lifelong commitment that shapes the moral conscience, emotional stability, and intellectual growth of children. Today, we investigate what constitutes responsible parenthood and evaluate the distinct parenting styles that influence child development.""",
        "core_scripture": """### Proverbs 22:6 & Proverbs 29:15-17 (NIV)

> **Proverbs 22:6:**
> "Start children off on the way they should go, and even when they are old they will not turn from it."
>
> **Proverbs 29:15:**
> "A rod and a reprimand impart wisdom, but a child left undisciplined disgraces its mother."
>
> **Proverbs 29:17:**
> "Discipline your children, and they will give you peace; they will bring you the delights you desire." """,
        "theological_pillars": """### Theological Exegesis & Analysis

1. **Intentional Foundation (Proverbs 22:6):**
   The Hebrew idiom *chanokh lanna'ar* ('train up' or 'dedicate') implies intentional consecration and personalized training. Responsible parents recognize a child's unique gifts, temperament, and spiritual calling, instilling godly habits early.

2. **The Dual Instruments of Wisdom (Proverbs 29:15):**
   Scripture couples corrective boundaries ('rod') with verbal guidance and reasoned rebuke ('reprimand'). Discipline without verbal explanation breeds resentment, while instruction without boundaries breeds lawlessness.

3. **The Fruit of Proactive Guidance (Proverbs 29:17):**
   Consistent, loving discipline produces enduring family peace (*shalom*). Responsible parenthood is an investment that safeguards the family against future disgrace and moral ruin.""",
        "svg_fn": get_svg_lesson_2,
        "deep_dive": """### Deep Dive: Comprehensive Analysis of Parenting Styles

#### 1. Defining Responsible Parenthood
Responsible parenthood is the conscious, continuous commitment by parents/guardians to provide:
- **Physical care:** Nutritious food, clean shelter, clothing, and access to medical care.
- **Spiritual guidance:** Imparting Scripture, praying together, and modeling Christian integrity.
- **Intellectual stimulation:** Financing education, monitoring academic progress, and encouraging curiosity.
- **Emotional & Social stability:** Providing unconditional love, affirming self-worth, and teaching social etiquette.

#### 2. The Four Major Parenting Styles (Baumrind Framework)

| Parenting Style | Demand / Control | Warmth / Responsiveness | Characteristics & Discipline Approach | Adolescent Outcome |
| :--- | :--- | :--- | :--- | :--- |
| **Authoritative (Democratic)** | **High** | **High** | Sets clear standards; explains rationale; listens to child's feedback; praises good conduct. | Confident, self-disciplined, high academic performance, resilient. |
| **Authoritarian (Autocratic)** | **High** | **Low** | Strict unbending rules; demands unquestioning obedience; relies on harsh punishment. | Anxious, low self-esteem, rebellious outside home, poor communication. |
| **Permissive (Indulgent)** | **Low** | **High** | Very few boundaries; avoids confrontation; indulges every whim; behaves like a peer. | Poor impulse control, entitled attitude, struggles with authority. |
| **Neglectful (Uninvolved)** | **Low** | **Low** | Emotionally detached; physically absent; provides bare minimal survival needs. | Severe emotional distress, delinquency, high risk of substance abuse. |

#### 3. Why the Democratic / Authoritative Style is Optimal
The democratic approach mirrors God's covenantal relationship with humanity—combining absolute holiness and righteous standards with boundless grace, active listening, and loving patience.""",
        "practical": {
            "title": "Action Framework: Constructive Engagement in Family Dialogue",
            "steps": [
                {
                    "step": 1,
                    "title": "Practice Active and Respectful Listening",
                    "description": "When parents or guardians communicate household rules, listen attentively without interrupting or reacting defensively."
                },
                {
                    "step": 2,
                    "title": "Articulate Thoughts with Humility",
                    "description": "Express your feelings, academic challenges, and personal goals politely using respectful and calm language."
                },
                {
                    "step": 3,
                    "title": "Embrace Parental Corrections Positively",
                    "description": "Accept constructive reprimands and curfew boundaries as expressions of protective love and character building."
                },
                {
                    "step": 4,
                    "title": "Honor Final Family Decisions",
                    "description": "Once discussions conclude, support the final guidance of parents with a willing, cheerful attitude."
                }
            ]
        },
        "kenyan_context": """### Kenyan Real-World Context & Democratic Parenting

In traditional setups, parenting was predominantly authoritative and communal, with children rarely questioning adult decisions. In contemporary Kenya, educated parents increasingly adopt democratic approaches, holding regular family meetings to discuss household budgeting, school choices, and holiday schedules.

However, challenges arise when parents misunderstand modern democracy as permissive indulgence, failing to enforce disciplinary boundaries. Kenyan youth are encouraged to actively participate in family discussions while maintaining the deeply rooted cultural and biblical value of absolute respect (*Heshima*) toward parents.""",
        "reflection": """### Spiritual Reflection & Values

God is our Heavenly Father who models perfect authoritative parenting: He establishes righteous boundaries for our protection and surrounds us with everlasting mercy. 

Reflect on your attitude toward parental guidance. Do you view family rules as a prison or as a protective hedge? Ask God to grant you a teachable heart that welcomes godly discipline.""",
        "takeaways": [
            "Responsible parenthood encompasses holistic physical, spiritual, intellectual, social, and emotional care.",
            "The authoritative (democratic) parenting style balances high standards with warmth, yielding the healthiest developmental outcomes.",
            "Authoritarian parenting relies on rigid control without warmth, often producing anxious or rebellious adolescents.",
            "Permissive parenting lacks boundaries and leads to poor self-regulation, while neglectful parenting constitutes total failure of parental duty.",
            "Proverbs 22:6 underscores the lifelong impact of early, intentional moral and spiritual training."
        ],
        "mcq": {
            "question": "Which parenting style is universally recognized by psychologists and Christian educators as the most effective because it combines high standards with open dialogue and warmth?",
            "options": [
                "Autocratic parenting style",
                "Democratic (Authoritative) parenting style",
                "Permissive (Laissez-faire) parenting style",
                "Neglectful (Uninvolved) parenting style"
            ],
            "correct_answer": "Democratic (Authoritative) parenting style",
            "explanation": "The democratic/authoritative parenting style is optimal because it sets clear, reasonable expectations while maintaining warmth, open communication, and mutual respect."
        }
    },

    # ─── LESSON 3 ────────────────────────────────────────────────────────────
    {
        "unit_order": 3,
        "unit_name": "Biblical Teachings on Parenting and Children's Roles",
        "unit_description": "Analyze key biblical mandates regarding parental duty to nurture and instruct children, alongside the reciprocal obligation of children to honor and obey their parents.",
        "lesson_title": "Biblical Teachings on Parenting and Children's Roles",
        "image": {
            "url": "https://upload.wikimedia.org/wikipedia/commons/thumb/8/87/Rembrandt_Harmensz._van_Rijn_-_The_Holy_Family_-_WGA19139.jpg/1280px-Rembrandt_Harmensz._van_Rijn_-_The_Holy_Family_-_WGA19139.jpg",
            "title": "Visual Hook: The Holy Family at Nazareth",
            "author": "Rembrandt van Rijn (Hermitage Museum)",
            "licensing": "Public Domain",
            "source": "Wikimedia Commons",
            "caption": "Rembrandt's depiction of the Holy Family, capturing the biblical environment of humble labour, divine instruction, and mutual family devotion."
        },
        "youtube": {
            "youtube_id": "Y71r-T98E2Q",
            "title": "BibleProject: Ephesians Overview",
            "description": "A comprehensive walk-through of Paul's letter to the Ephesians, focusing on Chapter 6 and the revolutionary household code for Christian families."
        },
        "goals": [
            "Examine biblical mandates for parents regarding spiritual education, compassionate discipline, and avoiding provocation.",
            "Explain children's scriptural obligations of honor, obedience, and reciprocal care for aging parents.",
            "Evaluate the Fifth Commandment as the foundational commandment carrying a divine promise of long life and prosperity."
        ],
        "intro": """Whenever you purchase an intricate mechanical device—such as a motorcycle, generator, or smartphone—it comes with an official manufacturer's handbook explaining exactly how to operate it safely. For Christian believers, the Holy Scriptures serve as the ultimate operational manual for family life.

God did not leave family dynamics to guesswork. Through the Law, Wisdom Literature, and apostolic epistles, God designed a balanced, reciprocal covenant: parents are given sacred authority to nurture and protect, while children are commanded to honor and obey. Let us examine these divine instructions.""",
        "core_scripture": """### Ephesians 6:1-4 & Colossians 3:20-21 (NIV)

> **Ephesians 6:1-4:**
> "Children, obey your parents in the Lord, for this is right. 'Honor your father and mother'—which is the first commandment with a promise—'so that it may go well with you and that you may enjoy long life on the earth.' Fathers, do not exasperate your children; instead, bring them up in the training and instruction of the Lord."
>
> **Colossians 3:20-21:**
> "Children, obey your parents in everything, for this pleases the Lord. Fathers, do not embitter your children, or they will become discouraged."
>
> **Exodus 20:12:**
> "Honor your father and your mother, so that you may live long in the land the Lord your God is giving you." """,
        "theological_pillars": """### Theological Exegesis & Analysis

1. **Obedience 'In the Lord' (Ephesians 6:1):**
   Children are instructed to obey their parents because parental authority is ordained by God. The phrase *'in the Lord'* indicates that obedience is an act of direct worship and submission to Christ Himself.

2. **The Promise of the Fifth Commandment (Exodus 20:12 / Ephesians 6:2-3):**
   Honoring parents (*kavod* — giving weight, high esteem, and reverence) is the first commandment accompanied by a specific covenantal blessing: societal stability, personal well-being, and longevity.

3. **Parental Restraint Against Exasperation (Ephesians 6:4 / Colossians 3:21):**
   In Roman antiquity, the *paterfamilias* held absolute life-and-death power over children. Paul radically subverted this cultural cruelty by commanding fathers never to exasperate (*parorgizo*) or embitter their children through harsh, unfair, or humiliating treatment.""",
        "svg_fn": get_svg_lesson_3,
        "deep_dive": """### Deep Dive: The Reciprocal Biblical Blueprint for Family Harmony

```
               ┌────────────────────────────────────────────────────────┐
               │              GOD'S COVENANTAL FOUNDATION               │
               └───────────────────────────┬────────────────────────────┘
                                           │
            ┌──────────────────────────────┴─────────────────────────────┐
            ▼                                                            ▼
┌───────────────────────────────────────┐    ┌───────────────────────────────────────┐
│        DUTIES OF GODLY PARENTS        │    │         DUTIES OF GODLY CHILDREN      │
├───────────────────────────────────────┤    ├───────────────────────────────────────┤
│ 1. Diligent Scripture Instruction     │    │ 1. Cheerful, Complete Obedience       │
│    (Deuteronomy 11:18-21)             │    │    (Colossians 3:20)                  │
│ 2. Providing Basic Holistic Needs     │    │ 2. Honor, Respect & High Esteem       │
│    (1 Timothy 5:8)                    │    │    (Exodus 20:12)                     │
│ 3. Loving, Corrective Discipline      │    │ 3. Diligent Household Cooperation     │
│    (Proverbs 13:24)                   │    │    (Proverbs 10:5)                    │
│ 4. Restraint from Harsh Provocation   │    │ 4. Lifelong Support for Aging Parents │
│    (Colossians 3:21)                  │    │    (1 Timothy 5:4)                    │
└───────────────────────────────────────┘    └───────────────────────────────────────┘
            │                                                            │
            └──────────────────────────────┬─────────────────────────────┘
                                           ▼
               ┌────────────────────────────────────────────────────────┐
               │    FAMILY HARMONY, PROSPERITY & DIVINE BLESSING        │
               └────────────────────────────────────────────────────────┘
```

#### 1. What Scripture Demands of Parents
- **Catechesis & Spiritual Legacy:** Deuteronomy 11:19 commands parents to talk about God's words when sitting at home, walking along the road, lying down, and getting up.
- **Holistic Provision:** 1 Timothy 5:8 warns that anyone who fails to provide for relatives, especially immediate family, has denied the faith.
- **Encouragement and Dignity:** Parents must build up a child's moral courage rather than crushing their spirit through sarcastic or demeaning insults.

#### 2. What Scripture Demands of Children
- **Reverence (*Kabod*):** Valuing parental sacrifice and speaking of them with profound dignity.
- **Prompt Execution of Guidance:** Following directives regarding education, chores, and moral boundaries without rebellion.
- **Reciprocal Care in Old Age:** Caring for elderly parents when they can no longer care for themselves, fulfilling our moral debt of gratitude.""",
        "practical": {
            "title": "Action Framework: Daily Demonstration of Biblical Honor",
            "steps": [
                {
                    "step": 1,
                    "title": "Perform Chores Without Grumbling",
                    "description": "Execute daily tasks like washing dishes, fetching water, or tidying the living room promptly and cheerfully."
                },
                {
                    "step": 2,
                    "title": "Demonstrate Polite Speech and Demeanor",
                    "description": "Use courteous words ('Thank you', 'Excuse me') and eliminate eye-rolling, slamming doors, or insolent replies."
                },
                {
                    "step": 3,
                    "title": "Commit to Academic Excellence",
                    "description": "Study diligently and protect school materials, recognizing the immense financial sacrifice parents make for your fees."
                },
                {
                    "step": 4,
                    "title": "Pray Daily for Parental Protection",
                    "description": "Intercede for your parents and guardians, asking God to grant them health, financial provision, and divine wisdom."
                }
            ]
        },
        "kenyan_context": """### Kenyan Real-World Context & Cultural Integration

In Kenyan society, honoring parents is deeply embedded in both Christian doctrine and African customary ethics. A child who openly disrespects or insults parents is culturally seen as attracting a generational curse, whereas a child who serves parents brings honor to the entire clan.

Many Kenyan youth express this honor practically during school holidays by assisting with agricultural work (shamba cultivation, caring for cattle) or helping in family retail businesses. When teenagers treat their homes as cooperative team units, family cohesion flourishes.""",
        "reflection": """### Spiritual Reflection & Values

The Fifth Commandment is the only commandment with a promise: that your days may be long and that it may go well with you. 

Examine how you treat your parents or guardians when they correct you. Do you respond with humility or anger? Ask the Lord to give you the grace to obey and honor them in all circumstances.""",
        "takeaways": [
            "God's Word provides a reciprocal framework for parents and children to maintain peace and spiritual health.",
            "Parents are commanded to teach Scripture, provide basic needs, and avoid provoking or embittering their children.",
            "Children are commanded to obey their parents in the Lord and honor them with lifelong respect.",
            "Honoring parents is the first commandment with a promise of longevity and divine favor.",
            "Adult children retain a moral and biblical obligation to support and care for their aging parents."
        ],
        "mcq": {
            "question": "According to Colossians 3:21 and Ephesians 6:4, what specific danger must Christian parents avoid when disciplining their children?",
            "options": [
                "Teaching them to perform household chores",
                "Embittering, exasperating, or discouraging them through harshness",
                "Taking them to church on Sundays",
                "Requiring them to study hard for examinations"
            ],
            "correct_answer": "Embittering, exasperating, or discouraging them through harshness",
            "explanation": "Paul explicitly instructs parents not to exasperate, embitter, or provoke their children with unreasonable harshness, which can crush their spirit and cause them to become discouraged."
        }
    },

    # ─── LESSON 4 ────────────────────────────────────────────────────────────
    {
        "unit_order": 4,
        "unit_name": "Problems Facing Family Life Today",
        "unit_description": "Identify and analyze the modern social, economic, psychological, and medical challenges destabilizing family life, exploring Christian strategies for resilience and healing.",
        "lesson_title": "Problems Facing Family Life Today",
        "image": {
            "url": "https://upload.wikimedia.org/wikipedia/commons/thumb/d/d7/Lange-MigrantMother02.jpg/800px-Lange-MigrantMother02.jpg",
            "title": "Visual Hook: Family Resiliency in Hardship",
            "author": "Dorothea Lange (Library of Congress Collection)",
            "licensing": "Public Domain",
            "source": "Wikimedia Commons",
            "caption": "Dorothea Lange's iconic portrait of a mother protecting her children amidst severe economic displacement, symbolizing the struggle and resilience of families facing hardship."
        },
        "youtube": {
            "youtube_id": "1p4fW6j6H68",
            "title": "BibleProject: Compassion & Grace in Broken Situations",
            "description": "A theological reflection on how God's character of compassion, patience, and forgiveness anchors families experiencing crisis, stress, and brokenness."
        },
        "goals": [
            "Identify major contemporary threats to family stability (economic strain, substance abuse, domestic violence, generation gap).",
            "Examine the root causes and indicators of family breakdown in contemporary Kenya.",
            "Apply Christian moral principles of tolerance, self-control, and forgiveness to withstand domestic adversity."
        ],
        "intro": """Imagine constructing a sturdy brick home on a hillside. Suddenly, an intense tropical storm arrives with howling gale-force winds, torrential downpours, and rushing floodwaters. If the foundation was built on sand, the house will fracture and collapse.

Today, the family institution is navigating an unprecedented storm of social, economic, and cultural pressures. High living costs, substance addiction, unaddressed domestic conflicts, and generational friction threaten family stability. How can families identify these threats early and build an unshakeable foundation of faith and resilience?""",
        "core_scripture": """### Ephesians 4:31-32 & Proverbs 15:1-4, 18 (NIV)

> **Ephesians 4:31-32:**
> "Get rid of all bitterness, rage and anger, brawling and slander, along with every form of malice. Be kind and compassionate to one another, forgiving each other, just as in Christ God forgave you."
>
> **Proverbs 15:1:**
> "A gentle answer turns away wrath, but a harsh word stirs up anger."
>
> **Proverbs 15:18:**
> "A hot-tempered person stirs up conflict, but the one who is patient calms a quarrel." """,
        "theological_pillars": """### Theological Exegesis & Analysis

1. **Renouncing Destructive Emotional Patterns (Ephesians 4:31):**
   Paul catalogs six toxic behaviors that poison family life: internal bitterness (*pikria*), volcanic rage (*thymos*), chronic anger (*orge*), public shouting/brawling (*krauge*), verbal slander (*blasphemia*), and calculated ill-will (*kakia*). Families must actively purge these vices.

2. **The Law of Reciprocal Forgiveness (Ephesians 4:32):**
   Christian forgiveness within a family is not based on whether the offending member deserves it, but on the standard of how God forgave us in Christ—freely, lavishly, and unconditionally.

3. **De-escalation Through Gentle Speech (Proverbs 15:1):**
   Biblical wisdom highlights the power of verbal restraint. Gentle words diffuse emotional tension, whereas provocative, sarcastic retorts ignite destructive domestic fires.""",
        "svg_fn": get_svg_lesson_4,
        "deep_dive": """### Deep Dive: Comprehensive Catalog of Contemporary Family Problems

#### 1. Economic Strain & Retrenchment
- **Unemployment & High Cost of Living:** Inability to afford rent, nutritious food, or school fees causes chronic anxiety and marital finger-pointing.
- **Retrenchment:** Sudden job redundancy strips breadwinners of financial security, often triggering acute depression or loss of self-worth.

#### 2. Substance Addiction & Alcohol Abuse
- **Resource Depletion:** Household income is diverted toward alcohol and drugs.
- **Domestic Turbulence:** Substance abuse is the leading catalyst for domestic violence, emotional trauma, and parental neglect.

#### 3. Domestic Violence & Child Abuse
- **Physical, Verbal & Emotional Assault:** Battering and demeaning language inflict lasting psychological trauma on spouses and children.
- **Child Exploitation:** Forcing underage children into child labour, hawking, or commercial exploitation violates basic human rights.

#### 4. The Generation Gap & Digital Friction
- **Technological Disconnect:** Disagreements between parents and tech-savvy teenagers over social media, smartphone usage, clothing trends, and peer culture.
- **Breakdown of Dialogue:** Failure to listen creates feelings of alienation and teenage withdrawal into secret online spaces.

#### 5. Health Crises & Chronic Illness
- **HIV/AIDS & Terminal Illnesses:** Depletion of family savings on medical management and stigmatization by uninformed relatives.
- **Caring for Children with Special Needs:** Lack of specialized educational and healthcare support can place severe emotional strain on parents.

#### 6. Childlessness & In-Law Interference
- **Infertility Stigma:** Inability to conceive often leads to unfair blame, societal pressure, and marital dissolution.
- **Meddling Relatives:** In-laws dictating domestic affairs or attempting to disinherit widows.""",
        "practical": {
            "title": "Action Framework: Managing Domestic Stress and Conflict",
            "steps": [
                {
                    "step": 1,
                    "title": "Apply Verbal De-escalation",
                    "description": "When tension rises, lower your voice tone and respond calmly rather than shouting or slamming doors."
                },
                {
                    "step": 2,
                    "title": "Practice Empathy Toward Stressed Parents",
                    "description": "Understand that parental irritability is often caused by heavy workplace stress or unpaid bills; offer practical help."
                },
                {
                    "step": 3,
                    "title": "Protect Personal and Sibling Safety",
                    "description": "In situations of severe domestic violence or abuse, seek immediate help from trusted teachers, pastors, or child protection helplines."
                },
                {
                    "step": 4,
                    "title": "Foster Family Prayer and Unity",
                    "description": "Encourage brief family devotions to bring economic and health burdens before God in prayer."
                }
            ]
        },
        "kenyan_context": """### Kenyan Real-World Context & Social Interventions

In Kenya, economic challenges—such as agricultural droughts, inflation, and urban un-employment—have placed severe strain on families. Organizations like the National Council for Children's Services (NCCS), Childline Kenya (116 helpline), and faith-based community groups provide legal, psychological, and material support to distressed families.

Kenyan youth are taught that facing hardship is not a sign of failure, but a call for resilient solidarity. Sharing scarce resources, supporting parents during retrenchment, and rejecting substance abuse protect the family from disintegrating.""",
        "reflection": """### Spiritual Reflection & Values

No earthly family is immune to trials, but God's grace is sufficient in our weakness. "The Lord is close to the brokenhearted and saves those who are crushed in spirit" (Psalm 34:18).

Think about any pain or frustration currently affecting your home. Have you brought it to God in prayer? Ask Him to fill your home with His supernatural peace and reconciliation.""",
        "takeaways": [
            "Modern families confront complex economic, social, medical, and psychological challenges.",
            "Retrenchment and inflation place immense pressure on breadwinners, often creating domestic friction.",
            "Substance abuse, domestic violence, and child abuse severely undermine the safety and sanctity of the home.",
            "The generation gap can be bridged through patient, empathetic, and respectful communication.",
            "Ephesians 4:31-32 commands family members to eliminate bitterness and cultivate Christ-like forgiveness."
        ],
        "mcq": {
            "question": "Which of the following describes an economic crisis where an organization formally terminates an employee's contract to reduce operational costs, suddenly cutting off family income?",
            "options": [
                "The generation gap",
                "Retrenchment",
                "In-law arbitration",
                "Communal parenting"
            ],
            "correct_answer": "Retrenchment",
            "explanation": "Retrenchment is the layoff of employees by companies to reduce operating expenses, which suddenly strips the family breadwinner of income and creates severe financial distress."
        }
    },

    # ─── LESSON 5 ────────────────────────────────────────────────────────────
    {
        "unit_order": 5,
        "unit_name": "Resolving Family Conflicts: Traditional African vs. Christian Approaches",
        "unit_description": "Compare and evaluate how family disputes are resolved through traditional African clan arbitration versus Christian pastoral ministry, counseling, and legal frameworks.",
        "lesson_title": "Resolving Family Conflicts: Traditional African vs. Christian Approaches",
        "image": {
            "url": "https://upload.wikimedia.org/wikipedia/commons/thumb/9/93/Rembrandt_Harmensz_van_Rijn_-_Return_of_the_Prodigal_Son_-_Google_Art_Project.jpg/1280px-Rembrandt_Harmensz_van_Rijn_-_Return_of_the_Prodigal_Son_-_Google_Art_Project.jpg",
            "title": "Visual Hook: The Return of the Prodigal Son",
            "author": "Rembrandt van Rijn (Hermitage Museum)",
            "licensing": "Public Domain",
            "source": "Wikimedia Commons",
            "caption": "Rembrandt's masterpiece capturing the climax of biblical reconciliation: an embracing father extending unconditional grace and restorative forgiveness to his repentant child."
        },
        "youtube": {
            "youtube_id": "v_o_wA9hHms",
            "title": "BibleProject: Forgiveness and Peacemaking",
            "description": "An insightful exploration of biblical peacemaking, tracing how genuine reconciliation heals human relationships and honors God's redemptive work."
        },
        "goals": [
            "Compare traditional African mechanisms of family dispute resolution with Christian pastoral approaches.",
            "Outline the steps of biblical reconciliation taught by Jesus in Matthew 18:15-17 and Galatians 6:1-2.",
            "Explain the importance of legal protections, counseling seminars, and written wills in averting property conflicts."
        ],
        "intro": """Imagine two farmers arguing over a boundary line between their crops. If they choose to shout insults and throw stones, the dispute escalates until crops are destroyed and lives are endangered. However, if they invite respected village elders to measure the boundary peacefully, order and friendship are restored.

Conflict is an inevitable reality in human relationships, but the mechanisms we use to address dispute determine whether a family heals or fractures. Both our African cultural heritage and the Christian Church provide powerful, structured frameworks for resolving disputes. Let us explore these pathways to peace.""",
        "core_scripture": """### Matthew 18:15-17, Galatians 6:1-2 & Colossians 3:12-14 (NIV)

> **Matthew 18:15-17:**
> "If your brother or sister sins, go and point out their fault, just between the two of you. If they listen to you, you have won them over. But if they will not listen, take one or two others along... If they still refuse to listen, tell it to the church."
>
> **Galatians 6:1-2:**
> "Brothers and sisters, if someone is caught in a sin, you who live by the Spirit should restore that person gently. But watch yourselves, or you also may be tempted. Carry each other’s burdens, and in this way you will fulfill the law of Christ."
>
> **Colossians 3:12-13:**
> "Therefore, as God's chosen people, holy and dearly loved, clothe yourselves with compassion, kindness, humility, gentleness and patience. Bear with each other and forgive one another." """,
        "theological_pillars": """### Theological Exegesis & Analysis

1. **The Principle of Graduated Reconciliation (Matthew 18:15-17):**
   Jesus outlines a three-stage restorative protocol:
   - *Stage 1:* Private, one-on-one dialogue to protect dignity and prevent gossip.
   - *Stage 2:* Involving one or two trusted mediators to establish objective facts.
   - *Stage 3:* Submitting the matter to the wider church leadership for formal mediation.

2. **Gentle Restoration over Vengeance (Galatians 6:1-2):**
   The Greek term *katartizo* ('restore') was used by ancient physicians to describe setting a broken bone. Confronting wrongdoing must never aim to humiliate or destroy, but to heal and realign the offender with love.

3. **Bearing Burdens (*Barē*):**
   Fulfilling the law of Christ means sharing emotional weights, helping family members overcome financial distress, and providing mutual accountability.""",
        "svg_fn": get_svg_lesson_5,
        "deep_dive": """### Deep Dive: Comparative Models of Family Dispute Resolution

| Dimension | Traditional African Approach | Christian & Legal Approach |
| :--- | :--- | :--- |
| **Primary Mediators** | Clan elders, maternal uncles, grandmothers, village chiefs. | Pastors, professional counselors, Christian elders, family courts. |
| **Guiding Principles** | Customary law, ancestral taboos, clan solidarity, preserving lineage. | Holy Scripture, Christ-like forgiveness, civil and family law. |
| **Key Mechanisms** | Reconciliatory gatherings, animal sacrifices, shared meals, symbolic fines. | Pastoral counseling, marriage seminars, joint prayer, civil mediation. |
| **Role of Women** | Senior aunts and grandmothers advised young wives privately. | Fellowships like Mothers' Union and Women's Guild provide mentorship. |
| **Property & Inheritance** | Oral declarations before clan witnesses; customary land distribution. | Legally drafted and registered **Written Wills**, preventing family disinheritance. |
| **Extreme Cases** | Temporary separation to clan home; cleansing rituals. | Legal protection orders, formal civil court intervention for abuse. |

#### Why Drafting a Written Will is Essential Today
In contemporary Kenya, property disputes frequently erupt after the sudden death of a family breadwinner, leaving widows and orphans disinherited by opportunistic relatives. A legally valid, witnessed **Written Will** clearly articulates asset distribution, protecting the family's financial future and preserving peace.""",
        "practical": {
            "title": "Action Framework: Becoming a Peacemaker in Family Disputes",
            "steps": [
                {
                    "step": 1,
                    "title": "Adopt a Non-Judgmental Stance",
                    "description": "Refuse to take partisan sides or fuel gossip when parents or siblings experience disagreements."
                },
                {
                    "step": 2,
                    "title": "Initiate Private, Gentle Dialogue",
                    "description": "If a sibling or family member offends you, address the issue calmly in private without broadcasting it publicly."
                },
                {
                    "step": 3,
                    "title": "Seek Wise Spiritual Mediation",
                    "description": "When conflicts persist, suggest consulting a trusted church leader, school counselor, or respected relative."
                },
                {
                    "step": 4,
                    "title": "Extend Forgiveness and Let Go of Grudges",
                    "description": "Choose to forgive past offenses as Christ forgave you, actively rebuilding trust through acts of kindness."
                }
            ]
        },
        "kenyan_context": """### Kenyan Real-World Context & Church Fellowships

In Kenya, churches play a pivotal role in maintaining family stability through organized ministries:
- **Mothers' Union / Women's Guild:** Provide holistic mentorship on marriage management, child rearing, and financial entrepreneurship.
- **Men's Fellowship (KAMA / PCMF):** Train fathers to be responsible spiritual leaders, loving spouses, and positive role models.
- **Youth & Pre-Marital Seminars:** Equip young couples with communication, budgeting, and conflict resolution skills before marriage.

When combined with modern legal instruments (such as registering land title deeds and writing wills), these ministries provide robust protection against family breakdown.""",
        "reflection": """### Spiritual Reflection & Values

Jesus declared: "Blessed are the peacemakers, for they will be called children of God" (Matthew 5:9). Peacemaking is not passive avoidance of conflict; it is the courageous work of building bridges of truth, justice, and forgiveness.

Are you harboring resentment toward any family member? Ask God for the courage and humility to initiate reconciliation and restore peace today.""",
        "takeaways": [
            "Conflict is inevitable, but mature families use structured, peaceful mechanisms to achieve reconciliation.",
            "Traditional African dispute resolution relied on clan elders, customary mediation, and shared reconciliatory meals.",
            "Christian resolution centers on biblical peacemaking (Matthew 18), gentle restoration, prayer, and pastoral counseling.",
            "Church ministries like Mothers' Union and Men's Guild provide ongoing mentorship for family harmony.",
            "Drafting a legally binding written will prevents bitter property and inheritance conflicts after a breadwinner's passing."
        ],
        "mcq": {
            "question": "Which church-supported fellowship provides practical mentorship and spiritual guidance for Christian women in managing households and mentoring youth in Kenya?",
            "options": [
                "The Local Law Society",
                "Mothers' Union / Women's Guild",
                "School Board of Management",
                "The County Land Registry"
            ],
            "correct_answer": "Mothers' Union / Women's Guild",
            "explanation": "Organizations like the Mothers' Union and Women's Guild are established church ministries where women fellowship, study Scripture, and mentor younger women and wives on family stewardship and parenting."
        }
    },

    # ─── LESSON 6 ────────────────────────────────────────────────────────────
    {
        "unit_order": 6,
        "unit_name": "Avoiding Unplanned Families",
        "unit_description": "Examine the moral values and critical life skills needed to prevent premature sexual activity and avoid unplanned teenage pregnancies, securing academic and career aspirations.",
        "lesson_title": "Avoiding Unplanned Families",
        "image": {
            "url": "https://upload.wikimedia.org/wikipedia/commons/thumb/b/b3/Guido_Reni_-_Joseph_and_Potiphar%27s_Wife_-_WGA19297.jpg/1280px-Guido_Reni_-_Joseph_and_Potiphar%27s_Wife_-_WGA19297.jpg",
            "title": "Visual Hook: Joseph Resisting Temptation",
            "author": "Guido Reni (Pushkin State Museum of Fine Arts)",
            "licensing": "Public Domain",
            "source": "Wikimedia Commons",
            "caption": "Guido Reni's dramatic portrayal of young Joseph fleeing from Potiphar's wife, exemplifying biblical moral courage, integrity, and self-control."
        },
        "youtube": {
            "youtube_id": "V7Q_R8yX198",
            "title": "BibleProject: The Wisdom Books & Guarding the Heart",
            "description": "An overview of how biblical wisdom in Proverbs guides young people to govern their desires, practice self-control, and build an honorable future."
        },
        "goals": [
            "Define an unplanned family and analyze the socioeconomic and educational risks of premature teenage parenting.",
            "Identify essential Christian moral values (Self-Control, Chastity, Integrity, Responsibility) that protect youth.",
            "Apply practical life skills (Assertiveness, High Self-Esteem, Critical Thinking, Decision-Making) to resist peer pressure."
        ],
        "intro": """Think about a high-performance, expensive sports car equipped with a massive engine capable of incredible speed. What happens if you drive that car at top speed on a steep mountain road without brakes, steering control, or headlights? You will inevitably crash, destroying both the vehicle and yourself.

Human sexuality and fertility are powerful, sacred gifts given by God. However, without the 'brakes' of self-control, moral values, and life skills, premature sexual indulgence leads to catastrophic consequences: sexually transmitted infections, disrupted education, and unplanned teenage pregnancies that derail your future. Let us examine how to construct a strong shield of purity.""",
        "core_scripture": """### 1 Corinthians 6:18-20, Proverbs 4:23 & Proverbs 24:3-4 (NIV)

> **1 Corinthians 6:18-20:**
> "Flee from sexual immorality. All other sins a person commits are outside the body, but whoever sins sexually, sins against their own body. Do you not know that your bodies are temples of the Holy Spirit, who is in you, whom you have received from God? You are not your own; you were bought at a price. Therefore honor God with your bodies."
>
> **Proverbs 4:23:**
> "Above all else, guard your heart, for everything you do flows from it."
>
> **Proverbs 24:3-4:**
> "By wisdom a house is built, and through understanding it is established; through knowledge its rooms are filled with rare and beautiful treasures." """,
        "theological_pillars": """### Theological Exegesis & Analysis

1. **The Mandate to Flee Immorality (1 Corinthians 6:18):**
   Paul does not tell believers to debate, negotiate with, or casually withstand sexual temptation; he commands them to *flee* (*pheugete*), just as Joseph ran from Potiphar's house (Genesis 39:12). Sexual sin uniquely compromises bodily and spiritual integrity.

2. **The Body as the Temple of the Holy Spirit (1 Corinthians 6:19-20):**
   A Christian's body is not private property for casual physical pleasure. It is a consecrated sanctuary (*naos*) purchased by the blood of Christ. Purity is an act of honoring God's ownership.

3. **Guarding the Inner Sanctuary (Proverbs 4:23):**
   In Hebrew thought, the *lev* (heart) represents the command centre of thoughts, desires, and decisions. Guarding the heart means controlling what we watch, listen to, and dwell on in our minds.""",
        "svg_fn": get_svg_lesson_6,
        "deep_dive": """### Deep Dive: Values and Life Skills for Preventing Unplanned Families

#### 1. What is an Unplanned Family?
An unplanned family is created prematurely when teenagers or unprepared individuals engage in unprotected premarital sexual activity, resulting in pregnancy without emotional maturity, financial stability, or marriage commitment.

#### 2. Consequences of Premature Teenage Parenting
- **Educational Disruption:** School dropout or prolonged academic deferral, severely limiting career prospects.
- **Economic Vulnerability:** Inability to provide food, housing, healthcare, and education for the baby, entrenching cycles of poverty.
- **Psychological & Emotional Trauma:** Guilt, depression, social stigmatization, and parental disappointment.
- **Health Complications:** Higher medical risks during adolescent pregnancy and childbirth.

#### 3. Core Christian Moral Virtues
1. **Self-Control (Temperance):** The spiritual power (Fruit of the Spirit, Galatians 5:23) to govern bodily passions and delay gratification.
2. **Chastity (Sexual Purity):** Preserving sexual intimacy exclusively for holy marriage.
3. **Integrity:** Making righteous moral choices even when unmonitored by parents or teachers.
4. **Responsibility:** Acknowledging that every action carries lifelong consequences.

#### 4. Critical Life Skills for Adolescents
- **High Self-Esteem:** Recognizing your identity as God's precious creation; refusing to seek validation through unhealthy relationships.
- **Assertiveness:** Communicating firm boundaries clearly without fear: *"NO! My future and education come first."*
- **Critical Thinking:** Pausing to evaluate long-term outcomes: *"If I compromise now, where will I be in 12 months?"*
- **Constructive Leisure Utilization:** Channeling energy into sports, church youth fellowship, reading, and creative arts to prevent idle vulnerability.""",
        "practical": {
            "title": "Action Framework: Goal-Setting and Boundary Defense",
            "steps": [
                {
                    "step": 1,
                    "title": "Write Down Clear Academic & Career Goals",
                    "description": "Document your dream career on a revision card and place it where you see it daily as a constant reminder."
                },
                {
                    "step": 2,
                    "title": "Establish Strict Physical & Social Boundaries",
                    "description": "Avoid isolated situations, unchaperoned parties, and compromising peer gatherings where sexual pressure occurs."
                },
                {
                    "step": 3,
                    "title": "Filter Digital and Media Content",
                    "description": "Unfollow social media accounts and delete apps or music promoting pornography, vulgarity, and immorality."
                },
                {
                    "step": 4,
                    "title": "Seek Godly Accountability",
                    "description": "Partner with trustworthy Christian friends, Sunday School teachers, or parents who encourage your walk of purity."
                }
            ]
        },
        "kenyan_context": """### Kenyan Real-World Context & Youth Empowerment

In Kenya, teenage pregnancies present a major challenge to adolescent education, particularly in secondary schools. The Ministry of Education, in partnership with religious organizations, champions values-based education, life skills coaching, and Christian Union guidance.

Kenyan students are encouraged to embrace the national motto of youth empowerment: *'Abstinence is the ultimate mark of strength and self-respect.'* By focusing on academic completion and vocational training, young people lay a solid foundation for future planned, thriving families.""",
        "reflection": """### Spiritual Reflection & Values

Your life is a masterpiece in progress. God has plans to prosper you and not to harm you, plans to give you hope and a future (Jeremiah 29:11). 

Do not allow a fleeting moment of peer pressure or physical curiosity to steal your destiny. Ask God to fortify your spirit with unwavering self-control, assertiveness, and moral courage.""",
        "takeaways": [
            "An unplanned family created through teenage pregnancy brings severe educational, economic, and emotional disruptions.",
            "1 Corinthians 6:18-20 commands believers to flee sexual immorality because our bodies are temples of the Holy Spirit.",
            "Proverbs 4:23 reminds youth that guarding their heart and thought-life is essential for moral preservation.",
            "Self-control, chastity, integrity, and responsibility are indispensable Christian virtues for protecting your future.",
            "Assertiveness and critical thinking empower young people to say 'No' to peer pressure and pursue their dreams."
        ],
        "mcq": {
            "question": "Which spiritual virtue, classified as a Fruit of the Holy Spirit in Galatians 5:22-23, empowers young people to govern physical desires and maintain sexual purity?",
            "options": [
                "Impatience",
                "Self-Control",
                "Idleness",
                "Complacency"
            ],
            "correct_answer": "Self-Control",
            "explanation": "Self-control (temperance) is the spiritual virtue and fruit of the Spirit that enables an individual to master their physical appetites, resist temptation, and honor God with their body."
        }
    }
]


# ─── INGESTION RUNNER ────────────────────────────────────────────────────────

def ingest_grade9_cre_topic14():
    print("=" * 80)
    print("STARTING INGESTION FOR GRADE 9 CRE TOPIC 14: RESPONSIBLE PARENTHOOD")
    print("=" * 80)

    with transaction.atomic():
        # 1. Resolve Grade 9
        try:
            grade = Grade.objects.get(id=18)
            print(f"[✓] Resolved Grade: {grade.name} (ID: {grade.id})")
        except Grade.DoesNotExist:
            print("[X] ERROR: Grade ID 18 does not exist!")
            return

        # 2. Resolve Curriculum
        curriculum = grade.curriculum
        print(f"[✓] Resolved Curriculum: {curriculum.name} (ID: {curriculum.id})")

        # 3. Resolve Subject CRE (ID: 50)
        try:
            subject = Subject.objects.get(id=50, grade=grade)
            print(f"[✓] Resolved Subject: {subject.name} (ID: {subject.id})")
        except Subject.DoesNotExist:
            print("[X] ERROR: Subject ID 50 under Grade 18 does not exist!")
            return

        # 4. Resolve or Create Topic 14
        topic, created = Topic.objects.get_or_create(
            subject=subject,
            order=14,
            defaults={
                "name": "Responsible Parenthood",
                "description": clean_text(
                    "This topic explores the family as the basic unit of society, examining different "
                    "family structures, traditional African and Christian family values, parenting styles, "
                    "conflict resolution mechanisms, and avoiding unplanned families."
                )
            }
        )
        if created:
            print(f"[✓] Created Topic 14: '{topic.name}' (ID: {topic.id})")
        else:
            topic.name = "Responsible Parenthood"
            topic.description = clean_text(
                "This topic explores the family as the basic unit of society, examining different "
                "family structures, traditional African and Christian family values, parenting styles, "
                "conflict resolution mechanisms, and avoiding unplanned families."
            )
            topic.save()
            print(f"[✓] Resolved existing Topic 14: '{topic.name}' (ID: {topic.id})")

        # Clean existing units and lessons under Topic 14 for clean idempotent execution
        existing_units = LearningUnit.objects.filter(topic=topic)
        for unit in existing_units:
            for lsn in unit.lessons.all():
                lsn.blocks.all().delete()
                lsn.assets.all().delete()
                lsn.delete()
            unit.delete()

        # Clean any orphaned lessons directly under topic
        for lsn in Lesson.objects.filter(topic=topic):
            lsn.blocks.all().delete()
            lsn.assets.all().delete()
            lsn.delete()
        print("[✓] Cleared previous units and lessons under Topic 14 for clean idempotent rebuild.")

        total_units = 0
        total_lessons = 0
        total_pages = 0
        total_blocks = 0
        total_assets = 0

        # 5. Ingest 6 Lessons
        for cfg in LESSONS_DATA:
            u_order = cfg["unit_order"]
            u_name = cfg["unit_name"]
            l_title = cfg["lesson_title"]

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
                    "grade": "Grade 9",
                    "subject": "CRE",
                    "topic_order": 14,
                    "topic_name": topic.name,
                    "unit_order": u_order,
                    "author": "VLearn Grade 9 CRE Ingestion Engine",
                    "curriculum_framework": "CBC Kenya",
                    "enrichment_version": "v3_pedagogical"
                }
            )
            total_lessons += 1

            # Prepare Assets (3 Assets per Lesson)
            # Asset 1: Image Visual Hook
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

            # Asset 2: Pedagogical Vector SVG Diagram
            svg_content = cfg["svg_fn"]()
            svg_asset = LessonAsset.objects.create(
                lesson=lesson,
                asset_type="diagram",
                source_type="ai_generated",
                storage_type="url",
                status="attached",
                title=f"Diagram: {l_title}",
                description=f"Responsive pedagogical vector SVG diagram illustrating {l_title}.",
                url=f"https://vlearn.africa/assets/diagrams/cre/grade9_topic_14_lesson_{u_order}.svg",
                metadata={
                    "svg_xml": svg_content,
                    "viewBox": "0 0 800 450",
                    "theme": "#0f172a"
                }
            )
            total_assets += 1

            # Asset 3: Curated Educational YouTube Video
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
            total_assets += 1

            # ───────────────────────────────────────────────────────────────────
            # CARD 1 (Page 1): Discovery & Objectives (3 blocks)
            # ───────────────────────────────────────────────────────────────────
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

            LessonBlock.objects.create(
                lesson=lesson, page_number=1, page_title="Discovery & Objectives",
                order=20, component_order=2,
                block_type="learning_goal", component_type="learning_goal",
                title="Lesson Objectives",
                content={"goals": clean_dict(cfg["goals"])}
            )

            LessonBlock.objects.create(
                lesson=lesson, page_number=1, page_title="Discovery & Objectives",
                order=30, component_order=3,
                block_type="concept_explanation", component_type="concept_explanation",
                title="Introduction & Familiar Connection",
                content={"markdown": clean_text(cfg["intro"])}
            )

            # ───────────────────────────────────────────────────────────────────
            # CARD 2 (Page 2): Scriptural Exegesis (2 blocks)
            # ───────────────────────────────────────────────────────────────────
            LessonBlock.objects.create(
                lesson=lesson, page_number=2, page_title="Scriptural Exegesis",
                order=40, component_order=1,
                block_type="concept_explanation", component_type="concept_explanation",
                title="Scripture Passage",
                content={"markdown": clean_text(cfg["core_scripture"])}
            )

            LessonBlock.objects.create(
                lesson=lesson, page_number=2, page_title="Scriptural Exegesis",
                order=45, component_order=2,
                block_type="concept_explanation", component_type="concept_explanation",
                title="Theological Exegesis & Analysis",
                content={"markdown": clean_text(cfg["theological_pillars"])}
            )

            # ───────────────────────────────────────────────────────────────────
            # CARD 3 (Page 3): Pedagogical Diagram & Deep Dive (2 blocks)
            # ───────────────────────────────────────────────────────────────────
            b5 = LessonBlock.objects.create(
                lesson=lesson, page_number=3, page_title="Pedagogical Diagram & Deep Dive",
                order=50, component_order=1,
                block_type="suggested_diagram", component_type="suggested_diagram",
                title=f"Diagram: {l_title}",
                content={
                    "title": f"Pedagogical Blueprint: {l_title}",
                    "caption": f"Comprehensive architectural diagram illustrating {l_title}.",
                    "svg": svg_content,
                    "svg_xml": svg_content
                }
            )
            b5.assets.add(svg_asset)

            LessonBlock.objects.create(
                lesson=lesson, page_number=3, page_title="Pedagogical Diagram & Deep Dive",
                order=60, component_order=2,
                block_type="concept_explanation", component_type="concept_explanation",
                title="Theological Deep Dive",
                content={"markdown": clean_text(cfg["deep_dive"])}
            )

            # ───────────────────────────────────────────────────────────────────
            # CARD 4 (Page 4): Practical Application & Context (2 blocks)
            # ───────────────────────────────────────────────────────────────────
            LessonBlock.objects.create(
                lesson=lesson, page_number=4, page_title="Practical Application & Context",
                order=70, component_order=1,
                block_type="step_process", component_type="step_process",
                title=clean_text(cfg["practical"]["title"]),
                content=clean_dict(cfg["practical"])
            )

            LessonBlock.objects.create(
                lesson=lesson, page_number=4, page_title="Practical Application & Context",
                order=75, component_order=2,
                block_type="concept_explanation", component_type="concept_explanation",
                title="Kenyan Real-World Context & Integration",
                content={"markdown": clean_text(cfg["kenyan_context"])}
            )

            # ───────────────────────────────────────────────────────────────────
            # CARD 5 (Page 5): Multimedia & Reflection (2 blocks)
            # ───────────────────────────────────────────────────────────────────
            b8 = LessonBlock.objects.create(
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
            b8.assets.add(yt_asset)

            LessonBlock.objects.create(
                lesson=lesson, page_number=5, page_title="Multimedia & Reflection",
                order=90, component_order=2,
                block_type="concept_explanation", component_type="concept_explanation",
                title="Spiritual Reflection & Values",
                content={"markdown": clean_text(cfg["reflection"])}
            )

            # ───────────────────────────────────────────────────────────────────
            # CARD 6 (Page 6): Mastery Check (2 blocks)
            # ───────────────────────────────────────────────────────────────────
            LessonBlock.objects.create(
                lesson=lesson, page_number=6, page_title="Mastery Check",
                order=100, component_order=1,
                block_type="summary", component_type="summary",
                title="Summary & Key Takeaways",
                content={
                    "title": f"Key Takeaways: {l_title}",
                    "takeaways": clean_dict(cfg["takeaways"])
                }
            )

            LessonBlock.objects.create(
                lesson=lesson, page_number=6, page_title="Mastery Check",
                order=110, component_order=2,
                block_type="knowledge_check", component_type="knowledge_check",
                title="Mastery Knowledge Check",
                content=clean_dict(cfg["mcq"])
            )

            total_pages += 6
            total_blocks += 13
            print(f"  [+] Ingested Lesson {u_order:02d}/6: '{l_title}' (6 cards/pages, 13 blocks, 3 LessonAssets)")

        print("=" * 80)
        print("INGESTION SUMMARY FOR GRADE 9 CRE TOPIC 14:")
        print(f"  - Curriculum       : {curriculum.name} (ID: {curriculum.id})")
        print(f"  - Grade            : {grade.name} (ID: {grade.id}, Level: {grade.level})")
        print(f"  - Subject          : {subject.name} (ID: {subject.id})")
        print(f"  - Topic            : Order {topic.order} — {topic.name} (ID: {topic.id})")
        print(f"  - Learning Units   : {total_units}")
        print(f"  - Published Lessons: {total_lessons}")
        print(f"  - Total Pages/Cards: {total_pages}")
        print(f"  - Total Blocks     : {total_blocks}")
        print(f"  - Total Assets     : {total_assets}")
        print("=" * 80)


if __name__ == "__main__":
    ingest_grade9_cre_topic14()
