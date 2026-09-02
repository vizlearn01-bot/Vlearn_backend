"""
CBC Grade 9 CRE — Topic 4: Kings David and Solomon
Production-Ready Ingestion & Visual Enrichment Engine (All 8 Lessons)

Target Scope:
  - Curriculum: CBC (ID: 5)
  - Grade: Grade 9 (ID: 18)
  - Subject: CRE (ID: 50)
  - Topic: Kings David and Solomon (Order: 4, ID: 325)

8 Lessons:
  1. Lesson 1: The Demand for a King in Israel (1 Samuel 8:1-22)
  2. Lesson 2: Saul's Rise, Achievements, and Failures (1 Samuel 9-11, 13, 15)
  3. Lesson 3: David's Calling and Anointing (1 Samuel 16:1-13)
  4. Lesson 4: King David's Achievements and Failures (2 Samuel 5-7, 11-12, Psalm 51)
  5. Lesson 5: David as an Ancestor of Jesus Christ (2 Samuel 7:12-16, Matthew 1:1, Luke 1:32-33)
  6. Lesson 6: Solomon's Accession, Request for Wisdom, and Achievements (1 Kings 3, 4, 6)
  7. Lesson 7: Solomon's Failures and the Temple's Importance (1 Kings 6-8, 11)
  8. Lesson 8: Choosing Leaders of Integrity Today (1 Timothy 3:1-7, Titus 1:5-9)

Standardized Block Structure per Lesson (6 Cards/Pages, 13 Blocks, 3 Assets):
  - Card 1 (Discovery & Objectives): suggested_image, learning_goal, concept_explanation
  - Card 2 (Scriptural Exegesis): concept_explanation, concept_explanation
  - Card 3 (Pedagogical Diagram & Deep Dive): suggested_diagram, concept_explanation
  - Card 4 (Practical Application & Context): step_process, concept_explanation
  - Card 5 (Multimedia & Reflection): suggested_video, concept_explanation
  - Card 6 (Mastery Check): summary, knowledge_check
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
    # Strip bracket citations e.g. [796, 797], [801]
    text = re.sub(r'\[(?:\d+(?:\.\d+)?(?:,\s*\d+(?:\.\d+)?)*|image_\d+|S\d+.*?|[\d,\s]{2,})\]', '', text)
    # Strip internal pedagogical tags
    text = re.sub(r'\[(VISUAL|BIBLE REFERENCE|BIBLE PASSAGE|REAL WORLD APPLICATION|REFLECTION|CRITICAL THINKING|VALUES|MISCONCEPTION|INTERACTION|ETHICAL SCENARIO|KEY VERSE|BIBLICAL CONTEXT|PEDAGOGICAL ARCHITECTURE|PROJECT TITLE)[^\]]*\]', '', text, flags=re.IGNORECASE)
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


# ─────────────────────────────────────────────────────────────────────────────
# 8 CUSTOM RESPONSIVE VECTOR SVGS (viewBox="0 0 800 450", #0f172a theme)
# ─────────────────────────────────────────────────────────────────────────────

def get_svg_lesson_1():
    return """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 450" width="100%" height="100%">
  <defs>
    <linearGradient id="bgGrad1" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#0f172a"/>
      <stop offset="50%" stop-color="#1e293b"/>
      <stop offset="100%" stop-color="#0f172a"/>
    </linearGradient>
    <linearGradient id="amberGrad1" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#f59e0b"/>
      <stop offset="100%" stop-color="#d97706"/>
    </linearGradient>
    <linearGradient id="redGrad1" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#ef4444"/>
      <stop offset="100%" stop-color="#b91c1c"/>
    </linearGradient>
  </defs>
  <rect width="800" height="450" fill="url(#bgGrad1)" rx="14"/>
  <rect x="15" y="15" width="770" height="420" fill="none" stroke="#334155" stroke-width="1.5" stroke-dasharray="6 4" rx="10"/>

  <text x="400" y="45" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="18" font-weight="700" text-anchor="middle">THE DEMAND FOR A KING: THEOCRACY VS. MONARCHY</text>
  <text x="400" y="68" fill="#94a3b8" font-family="system-ui, sans-serif" font-size="12" text-anchor="middle">1 Samuel 8: Causes of Israel's Demand &amp; Samuel's Prophetic Warnings</text>

  <!-- Left Column: Causes of Demand -->
  <g transform="translate(35, 90)">
    <rect width="345" height="320" rx="10" fill="#1e293b" stroke="#f59e0b" stroke-width="1.5"/>
    <rect width="345" height="38" rx="10" fill="url(#amberGrad1)"/>
    <text x="172" y="24" fill="#0f172a" font-family="system-ui, sans-serif" font-size="14" font-weight="800" text-anchor="middle">CAUSES OF ISRAEL'S DEMAND</text>

    <text x="18" y="70" fill="#f8fafc" font-family="system-ui, sans-serif" font-size="12" font-weight="700">1. Corruption of Samuel's Sons</text>
    <text x="28" y="90" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="11">Joel &amp; Abijah took bribes and perverted justice.</text>

    <text x="18" y="125" fill="#f8fafc" font-family="system-ui, sans-serif" font-size="12" font-weight="700">2. Philistine Threat &amp; Military Need</text>
    <text x="28" y="145" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="11">Desire for a permanent warrior general.</text>

    <text x="18" y="180" fill="#f8fafc" font-family="system-ui, sans-serif" font-size="12" font-weight="700">3. Conformity to Surrounding Nations</text>
    <text x="28" y="200" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="11">Envy of pagan monarchies ("Like other nations").</text>

    <text x="18" y="235" fill="#f8fafc" font-family="system-ui, sans-serif" font-size="12" font-weight="700">4. Rejection of Invisible Sovereignty</text>
    <text x="28" y="255" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="11">Preferred visible human ruler over God's rule.</text>

    <text x="18" y="290" fill="#f8fafc" font-family="system-ui, sans-serif" font-size="12" font-weight="700">5. Quest for Centralized Law Courts</text>
  </g>

  <!-- Right Column: Samuel's Prophetic Warnings -->
  <g transform="translate(420, 90)">
    <rect width="345" height="320" rx="10" fill="#1e293b" stroke="#ef4444" stroke-width="1.5"/>
    <rect width="345" height="38" rx="10" fill="url(#redGrad1)"/>
    <text x="172" y="24" fill="#ffffff" font-family="system-ui, sans-serif" font-size="14" font-weight="800" text-anchor="middle">SAMUEL'S PROPHETIC WARNINGS</text>

    <text x="18" y="70" fill="#f8fafc" font-family="system-ui, sans-serif" font-size="12" font-weight="700">• Forced Military Conscription</text>
    <text x="28" y="90" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="11">Sons drafted to run before royal chariots.</text>

    <text x="18" y="125" fill="#f8fafc" font-family="system-ui, sans-serif" font-size="12" font-weight="700">• Exploitation of Labor &amp; Daughters</text>
    <text x="28" y="145" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="11">Daughters taken as cooks, bakers, perfumers.</text>

    <text x="18" y="180" fill="#f8fafc" font-family="system-ui, sans-serif" font-size="12" font-weight="700">• Property Grabbing &amp; Confiscation</text>
    <text x="28" y="200" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="11">Best vineyards and olive groves seized for officials.</text>

    <text x="18" y="235" fill="#f8fafc" font-family="system-ui, sans-serif" font-size="12" font-weight="700">• Heavy Royal Taxation (Tithe on Grain/Flocks)</text>
    <text x="28" y="255" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="11">10% tax on harvest to sustain lavish royal courts.</text>

    <text x="18" y="290" fill="#fca5a5" font-family="system-ui, sans-serif" font-size="12" font-weight="700">• State Enslavement &amp; Loss of Freedom</text>
  </g>
</svg>"""


def get_svg_lesson_2():
    return """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 450" width="100%" height="100%">
  <defs>
    <linearGradient id="bgGrad2" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#0f172a"/>
      <stop offset="50%" stop-color="#1e293b"/>
      <stop offset="100%" stop-color="#0f172a"/>
    </linearGradient>
  </defs>
  <rect width="800" height="450" fill="url(#bgGrad2)" rx="14"/>
  <rect x="15" y="15" width="770" height="420" fill="none" stroke="#334155" stroke-width="1.5" stroke-dasharray="6 4" rx="10"/>

  <text x="400" y="42" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="18" font-weight="700" text-anchor="middle">THE DOWNWARD SPIRAL OF KING SAUL</text>
  <text x="400" y="64" fill="#94a3b8" font-family="system-ui, sans-serif" font-size="12" text-anchor="middle">From Divine Anointing to Apostasy: The Peril of Rationalized Disobedience</text>

  <!-- Step 1: Humility & Anointing -->
  <g transform="translate(30, 85)">
    <rect width="130" height="300" rx="8" fill="#1e293b" stroke="#10b981" stroke-width="1.5"/>
    <rect width="130" height="32" rx="8" fill="#059669"/>
    <text x="65" y="21" fill="#ffffff" font-family="system-ui, sans-serif" font-size="12" font-weight="700" text-anchor="middle">1. ANOINTING</text>
    <text x="10" y="60" fill="#f8fafc" font-family="system-ui, sans-serif" font-size="11" font-weight="700">• Divine Choice</text>
    <text x="10" y="80" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10">Tall, handsome</text>
    <text x="10" y="95" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10">from Benjamin.</text>
    <text x="10" y="125" fill="#f8fafc" font-family="system-ui, sans-serif" font-size="11" font-weight="700">• Early Humility</text>
    <text x="10" y="145" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10">Hid among baggage.</text>
    <text x="10" y="175" fill="#f8fafc" font-family="system-ui, sans-serif" font-size="11" font-weight="700">• Victory</text>
    <text x="10" y="195" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10">Unified tribes</text>
    <text x="10" y="210" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10">against Ammonites.</text>
  </g>

  <!-- Step 2: Presumptuous Sacrifice -->
  <g transform="translate(180, 85)">
    <rect width="130" height="300" rx="8" fill="#1e293b" stroke="#3b82f6" stroke-width="1.5"/>
    <rect width="130" height="32" rx="8" fill="#2563eb"/>
    <text x="65" y="21" fill="#ffffff" font-family="system-ui, sans-serif" font-size="11" font-weight="700" text-anchor="middle">2. IMPATIENCE</text>
    <text x="10" y="60" fill="#f8fafc" font-family="system-ui, sans-serif" font-size="11" font-weight="700">• Gilgal Crisis</text>
    <text x="10" y="80" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10">Troops scattering</text>
    <text x="10" y="95" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10">before Philistines.</text>
    <text x="10" y="125" fill="#f8fafc" font-family="system-ui, sans-serif" font-size="11" font-weight="700">• Ritual Breach</text>
    <text x="10" y="145" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10">Offered sacrifice</text>
    <text x="10" y="160" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10">without Samuel.</text>
    <text x="10" y="190" fill="#93c5fd" font-family="system-ui, sans-serif" font-size="10" font-weight="600">Dynasty forfeited.</text>
  </g>

  <!-- Step 3: Amalekite Disobedience -->
  <g transform="translate(330, 85)">
    <rect width="130" height="300" rx="8" fill="#1e293b" stroke="#f59e0b" stroke-width="1.5"/>
    <rect width="130" height="32" rx="8" fill="#d97706"/>
    <text x="65" y="21" fill="#0f172a" font-family="system-ui, sans-serif" font-size="11" font-weight="800" text-anchor="middle">3. COMPROMISE</text>
    <text x="10" y="60" fill="#f8fafc" font-family="system-ui, sans-serif" font-size="11" font-weight="700">• Spared Agag</text>
    <text x="10" y="80" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10">Kept fat livestock.</text>
    <text x="10" y="110" fill="#f8fafc" font-family="system-ui, sans-serif" font-size="11" font-weight="700">• Shifted Blame</text>
    <text x="10" y="130" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10">Blamed soldiers.</text>
    <text x="10" y="160" fill="#fef08a" font-family="system-ui, sans-serif" font-size="10" font-weight="700">"To obey is</text>
    <text x="10" y="175" fill="#fef08a" font-family="system-ui, sans-serif" font-size="10" font-weight="700">better than</text>
    <text x="10" y="190" fill="#fef08a" font-family="system-ui, sans-serif" font-size="10" font-weight="700">sacrifice."</text>
    <text x="10" y="220" fill="#fca5a5" font-family="system-ui, sans-serif" font-size="10">Kingship rejected.</text>
  </g>

  <!-- Step 4: Jealousy & Paranoia -->
  <g transform="translate(480, 85)">
    <rect width="130" height="300" rx="8" fill="#1e293b" stroke="#ea580c" stroke-width="1.5"/>
    <rect width="130" height="32" rx="8" fill="#c2410c"/>
    <text x="65" y="21" fill="#ffffff" font-family="system-ui, sans-serif" font-size="11" font-weight="700" text-anchor="middle">4. PARANOIA</text>
    <text x="10" y="60" fill="#f8fafc" font-family="system-ui, sans-serif" font-size="11" font-weight="700">• Jealousy</text>
    <text x="10" y="80" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10">Enraged by song:</text>
    <text x="10" y="95" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10">"David tens of</text>
    <text x="10" y="110" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10">thousands."</text>
    <text x="10" y="140" fill="#f8fafc" font-family="system-ui, sans-serif" font-size="11" font-weight="700">• Murderous plots</text>
    <text x="10" y="160" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10">Hunted David</text>
    <text x="10" y="175" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10">in wilderness.</text>
    <text x="10" y="205" fill="#f8fafc" font-family="system-ui, sans-serif" font-size="11" font-weight="700">• Nob Massacre</text>
  </g>

  <!-- Step 5: Occult & Tragic Fall -->
  <g transform="translate(630, 85)">
    <rect width="130" height="300" rx="8" fill="#1e293b" stroke="#ef4444" stroke-width="1.5"/>
    <rect width="130" height="32" rx="8" fill="#b91c1c"/>
    <text x="65" y="21" fill="#ffffff" font-family="system-ui, sans-serif" font-size="11" font-weight="700" text-anchor="middle">5. APOSTASY</text>
    <text x="10" y="60" fill="#f8fafc" font-family="system-ui, sans-serif" font-size="11" font-weight="700">• Witch of Endor</text>
    <text x="10" y="80" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10">Consulted medium</text>
    <text x="10" y="95" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10">in disguise.</text>
    <text x="10" y="125" fill="#f8fafc" font-family="system-ui, sans-serif" font-size="11" font-weight="700">• Total Silence</text>
    <text x="10" y="145" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10">God answered not.</text>
    <text x="10" y="175" fill="#fca5a5" font-family="system-ui, sans-serif" font-size="11" font-weight="700">• Mount Gilboa</text>
    <text x="10" y="195" fill="#fca5a5" font-family="system-ui, sans-serif" font-size="10">Defeat &amp; suicide.</text>
  </g>
</svg>"""


def get_svg_lesson_3():
    return """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 450" width="100%" height="100%">
  <defs>
    <linearGradient id="bgGrad3" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#0f172a"/>
      <stop offset="50%" stop-color="#1e293b"/>
      <stop offset="100%" stop-color="#0f172a"/>
    </linearGradient>
    <linearGradient id="goldGrad3" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#fbbf24"/>
      <stop offset="100%" stop-color="#d97706"/>
    </linearGradient>
  </defs>
  <rect width="800" height="450" fill="url(#bgGrad3)" rx="14"/>
  <rect x="15" y="15" width="770" height="420" fill="none" stroke="#334155" stroke-width="1.5" stroke-dasharray="6 4" rx="10"/>

  <text x="400" y="42" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="18" font-weight="700" text-anchor="middle">DIVINE ELECTION: GOD LOOKS AT THE HEART</text>
  <text x="400" y="64" fill="#94a3b8" font-family="system-ui, sans-serif" font-size="12" text-anchor="middle">1 Samuel 16:7 — "People look at the outward appearance, but the Lord looks at the heart."</text>

  <!-- Left: Human Criteria (Eliab & Brothers) -->
  <g transform="translate(45, 90)">
    <rect width="325" height="315" rx="10" fill="#1e293b" stroke="#94a3b8" stroke-width="1.5"/>
    <rect width="325" height="38" rx="10" fill="#475569"/>
    <text x="162" y="24" fill="#ffffff" font-family="system-ui, sans-serif" font-size="13" font-weight="700" text-anchor="middle">HUMAN PERSPECTIVE (ELIAB &amp; BROTHERS)</text>

    <text x="18" y="70" fill="#f8fafc" font-family="system-ui, sans-serif" font-size="12" font-weight="700">• Physical Stature &amp; Height</text>
    <text x="28" y="90" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="11">Samuel judged Eliab by impressive looks.</text>

    <text x="18" y="125" fill="#f8fafc" font-family="system-ui, sans-serif" font-size="12" font-weight="700">• Seniority &amp; Birthright Position</text>
    <text x="28" y="145" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="11">7 elder sons paraded first before prophet.</text>

    <text x="18" y="180" fill="#f8fafc" font-family="system-ui, sans-serif" font-size="12" font-weight="700">• Visible Military Muscle</text>
    <text x="28" y="200" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="11">Soldiers with armor, training, and rank.</text>

    <text x="18" y="240" fill="#fca5a5" font-family="system-ui, sans-serif" font-size="12" font-weight="700">VERDICT: "The Lord has not chosen these."</text>
    <text x="28" y="260" fill="#94a3b8" font-family="system-ui, sans-serif" font-size="11">Outward charisma cannot replace inward integrity.</text>
  </g>

  <!-- Right: Divine Criteria (David the Shepherd) -->
  <g transform="translate(430, 90)">
    <rect width="325" height="315" rx="10" fill="#1e293b" stroke="#fbbf24" stroke-width="1.5"/>
    <rect width="325" height="38" rx="10" fill="url(#goldGrad3)"/>
    <text x="162" y="24" fill="#0f172a" font-family="system-ui, sans-serif" font-size="13" font-weight="800" text-anchor="middle">GOD'S PERSPECTIVE (DAVID THE SHEPHERD)</text>

    <text x="18" y="70" fill="#f8fafc" font-family="system-ui, sans-serif" font-size="12" font-weight="700">• Faith &amp; Spiritual Alignment</text>
    <text x="28" y="90" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="11">A heart entirely devoted to Yahweh.</text>

    <text x="18" y="125" fill="#f8fafc" font-family="system-ui, sans-serif" font-size="12" font-weight="700">• Tested Faithfulness in Obscurity</text>
    <text x="28" y="145" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="11">Defended flock from lion and bear.</text>

    <text x="18" y="180" fill="#f8fafc" font-family="system-ui, sans-serif" font-size="12" font-weight="700">• Humility in Waiting &amp; Service</text>
    <text x="28" y="200" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="11">Returned to sheep; soothed Saul with harp.</text>

    <text x="18" y="240" fill="#86efac" font-family="system-ui, sans-serif" font-size="12" font-weight="700">VERDICT: "Rise and anoint him; this is the one!"</text>
    <text x="28" y="260" fill="#93c5fd" font-family="system-ui, sans-serif" font-size="11">Spirit of the Lord rushed upon David.</text>
  </g>
</svg>"""


def get_svg_lesson_4():
    return """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 450" width="100%" height="100%">
  <defs>
    <linearGradient id="bgGrad4" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#0f172a"/>
      <stop offset="50%" stop-color="#1e293b"/>
      <stop offset="100%" stop-color="#0f172a"/>
    </linearGradient>
    <linearGradient id="blueGrad4" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#38bdf8"/>
      <stop offset="100%" stop-color="#0284c7"/>
    </linearGradient>
    <linearGradient id="purpleGrad4" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#a855f7"/>
      <stop offset="100%" stop-color="#7e22ce"/>
    </linearGradient>
  </defs>
  <rect width="800" height="450" fill="url(#bgGrad4)" rx="14"/>
  <rect x="15" y="15" width="770" height="420" fill="none" stroke="#334155" stroke-width="1.5" stroke-dasharray="6 4" rx="10"/>

  <text x="400" y="42" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="18" font-weight="700" text-anchor="middle">KING DAVID: ACHIEVEMENTS VS. MORAL RECKONING</text>
  <text x="400" y="64" fill="#94a3b8" font-family="system-ui, sans-serif" font-size="12" text-anchor="middle">Golden Age Governance, Grievous Fall (Bathsheba/Uriah), and True Repentance (Psalm 51)</text>

  <!-- Left: Achievements -->
  <g transform="translate(40, 90)">
    <rect width="335" height="315" rx="10" fill="#1e293b" stroke="#38bdf8" stroke-width="1.5"/>
    <rect width="335" height="38" rx="10" fill="url(#blueGrad4)"/>
    <text x="167" y="24" fill="#0f172a" font-family="system-ui, sans-serif" font-size="13" font-weight="800" text-anchor="middle">MAJOR ACHIEVEMENTS</text>

    <text x="16" y="70" fill="#f8fafc" font-family="system-ui, sans-serif" font-size="12" font-weight="700">1. Military &amp; Territorial Expansion</text>
    <text x="26" y="88" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="11">Subdued Philistines, Moabites, Ammonites.</text>

    <text x="16" y="120" fill="#f8fafc" font-family="system-ui, sans-serif" font-size="12" font-weight="700">2. Jerusalem as Capital City</text>
    <text x="26" y="138" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="11">Captured Zion; neutralized tribal rivalry.</text>

    <text x="16" y="170" fill="#f8fafc" font-family="system-ui, sans-serif" font-size="12" font-weight="700">3. Spiritual Centralization</text>
    <text x="26" y="188" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="11">Brought Ark of the Covenant to Jerusalem.</text>

    <text x="16" y="220" fill="#f8fafc" font-family="system-ui, sans-serif" font-size="12" font-weight="700">4. Musical &amp; Worship Legacy (Psalms)</text>

    <text x="16" y="260" fill="#f8fafc" font-family="system-ui, sans-serif" font-size="12" font-weight="700">5. Covenant Justice &amp; Kindness</text>
    <text x="26" y="278" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="11">Honored Jonathan via Mephibosheth.</text>
  </g>

  <!-- Right: Moral Reckoning & Repentance -->
  <g transform="translate(425, 90)">
    <rect width="335" height="315" rx="10" fill="#1e293b" stroke="#a855f7" stroke-width="1.5"/>
    <rect width="335" height="38" rx="10" fill="url(#purpleGrad4)"/>
    <text x="167" y="24" fill="#ffffff" font-family="system-ui, sans-serif" font-size="13" font-weight="800" text-anchor="middle">FALL, CONFRONTATION &amp; REPENTANCE</text>

    <text x="16" y="70" fill="#fca5a5" font-family="system-ui, sans-serif" font-size="12" font-weight="700">1. Complacency &amp; Adultery</text>
    <text x="26" y="88" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="11">Stayed in Jerusalem; sin with Bathsheba.</text>

    <text x="16" y="120" fill="#fca5a5" font-family="system-ui, sans-serif" font-size="12" font-weight="700">2. Cover-up Murder of Uriah</text>
    <text x="26" y="138" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="11">Abused royal power; ordered front-line death.</text>

    <text x="16" y="170" fill="#fef08a" font-family="system-ui, sans-serif" font-size="12" font-weight="700">3. Nathan's Prophetic Rebukes</text>
    <text x="26" y="188" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="11">Parable of the ewe lamb: "You are the man!"</text>

    <text x="16" y="225" fill="#86efac" font-family="system-ui, sans-serif" font-size="12" font-weight="700">4. Brokenness &amp; Sincere Confession</text>
    <text x="26" y="243" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="11">"I have sinned against the Lord." (Psalm 51)</text>

    <text x="16" y="275" fill="#e2e8f0" font-family="system-ui, sans-serif" font-size="11" font-style="italic">"Create in me a clean heart, O God."</text>
  </g>
</svg>"""


def get_svg_lesson_5():
    return """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 450" width="100%" height="100%">
  <defs>
    <linearGradient id="bgGrad5" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#0f172a"/>
      <stop offset="50%" stop-color="#1e293b"/>
      <stop offset="100%" stop-color="#0f172a"/>
    </linearGradient>
    <linearGradient id="goldGrad5" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#f59e0b"/>
      <stop offset="100%" stop-color="#b45309"/>
    </linearGradient>
  </defs>
  <rect width="800" height="450" fill="url(#bgGrad5)" rx="14"/>
  <rect x="15" y="15" width="770" height="420" fill="none" stroke="#334155" stroke-width="1.5" stroke-dasharray="6 4" rx="10"/>

  <text x="400" y="42" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="18" font-weight="700" text-anchor="middle">THE DAVIDIC COVENANT &amp; MESSIANIC FULFILLMENT</text>
  <text x="400" y="64" fill="#94a3b8" font-family="system-ui, sans-serif" font-size="12" text-anchor="middle">2 Samuel 7: God Promises an Everlasting House Fulfilled in Jesus Christ</text>

  <!-- Flow Boxes -->
  <!-- Box 1: David's Desire -->
  <g transform="translate(35, 95)">
    <rect width="210" height="130" rx="8" fill="#1e293b" stroke="#38bdf8" stroke-width="1.5"/>
    <rect width="210" height="30" rx="8" fill="#0284c7"/>
    <text x="105" y="20" fill="#ffffff" font-family="system-ui, sans-serif" font-size="12" font-weight="700" text-anchor="middle">DAVID'S DESIRE</text>
    <text x="12" y="55" fill="#f8fafc" font-family="system-ui, sans-serif" font-size="11" font-weight="600">• Cedar Palace vs Tent</text>
    <text x="12" y="72" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10">Wished to build a</text>
    <text x="12" y="87" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10">brick temple for Ark.</text>
    <text x="12" y="110" fill="#94a3b8" font-family="system-ui, sans-serif" font-size="10">God said: "Not you."</text>
  </g>

  <!-- Arrow 1 -->
  <polygon points="285,160 275,155 275,165" fill="#fbbf24"/>

  <!-- Box 2: God's Covenant Promise -->
  <g transform="translate(295, 95)">
    <rect width="210" height="130" rx="8" fill="#1e293b" stroke="#f59e0b" stroke-width="1.5"/>
    <rect width="210" height="30" rx="8" fill="url(#goldGrad5)"/>
    <text x="105" y="20" fill="#0f172a" font-family="system-ui, sans-serif" font-size="12" font-weight="800" text-anchor="middle">GOD'S COVENANT</text>
    <text x="12" y="55" fill="#f8fafc" font-family="system-ui, sans-serif" font-size="11" font-weight="600">• Dynasty ("House")</text>
    <text x="12" y="72" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10">God builds David an</text>
    <text x="12" y="87" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10">everlasting royal line.</text>
    <text x="12" y="110" fill="#fde68a" font-family="system-ui, sans-serif" font-size="10">Throne forever.</text>
  </g>

  <!-- Arrow 2 -->
  <polygon points="545,160 535,155 535,165" fill="#fbbf24"/>

  <!-- Box 3: Physical vs Spiritual House -->
  <g transform="translate(555, 95)">
    <rect width="210" height="130" rx="8" fill="#1e293b" stroke="#10b981" stroke-width="1.5"/>
    <rect width="210" height="30" rx="8" fill="#059669"/>
    <text x="105" y="20" fill="#ffffff" font-family="system-ui, sans-serif" font-size="12" font-weight="700" text-anchor="middle">SOLOMON'S ROLE</text>
    <text x="12" y="55" fill="#f8fafc" font-family="system-ui, sans-serif" font-size="11" font-weight="600">• Man of Peace</text>
    <text x="12" y="72" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10">Solomon built the</text>
    <text x="12" y="87" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10">physical Jerusalem temple.</text>
    <text x="12" y="110" fill="#a7f3d0" font-family="system-ui, sans-serif" font-size="10">Shadow of eternal house.</text>
  </g>

  <!-- Bottom: Messianic Climax in Jesus Christ -->
  <g transform="translate(70, 255)">
    <rect width="660" height="150" rx="10" fill="#1e293b" stroke="#38bdf8" stroke-width="2"/>
    <rect width="660" height="32" rx="10" fill="#0284c7"/>
    <text x="330" y="21" fill="#ffffff" font-family="system-ui, sans-serif" font-size="13" font-weight="800" text-anchor="middle">NEW TESTAMENT FULFILLMENT IN JESUS CHRIST</text>

    <text x="25" y="60" fill="#f8fafc" font-family="system-ui, sans-serif" font-size="12" font-weight="700">• Genealogy (Matthew 1:1):</text>
    <text x="210" y="60" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="11">"Jesus Christ, the Son of David, the Son of Abraham."</text>

    <text x="25" y="88" fill="#f8fafc" font-family="system-ui, sans-serif" font-size="12" font-weight="700">• Annunciation (Luke 1:32-33):</text>
    <text x="210" y="88" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="11">"God will give him the throne of his father David; kingdom will never end."</text>

    <text x="25" y="116" fill="#f8fafc" font-family="system-ui, sans-serif" font-size="12" font-weight="700">• Birthplace (Luke 2:4):</text>
    <text x="210" y="116" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="11">Born in Bethlehem, the City of David.</text>

    <text x="25" y="138" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="11" font-weight="600">• Blind Bartimaeus (Luke 18:38): "Jesus, Son of David, have mercy on me!"</text>
  </g>
</svg>"""


def get_svg_lesson_6():
    return """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 450" width="100%" height="100%">
  <defs>
    <linearGradient id="bgGrad6" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#0f172a"/>
      <stop offset="50%" stop-color="#1e293b"/>
      <stop offset="100%" stop-color="#0f172a"/>
    </linearGradient>
    <linearGradient id="goldGrad6" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#f59e0b"/>
      <stop offset="100%" stop-color="#d97706"/>
    </linearGradient>
  </defs>
  <rect width="800" height="450" fill="url(#bgGrad6)" rx="14"/>
  <rect x="15" y="15" width="770" height="420" fill="none" stroke="#334155" stroke-width="1.5" stroke-dasharray="6 4" rx="10"/>

  <text x="400" y="42" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="18" font-weight="700" text-anchor="middle">KING SOLOMON: DIVINE WISDOM &amp; GOLDEN AGE ACHIEVEMENTS</text>
  <text x="400" y="64" fill="#94a3b8" font-family="system-ui, sans-serif" font-size="12" text-anchor="middle">1 Kings 3-6: The Prayer at Gibeon, Famous Judgment, and Global Trade</text>

  <!-- 4 Pillars of Solomon's Reign -->
  <!-- Pillar 1: Divine Wisdom -->
  <g transform="translate(30, 90)">
    <rect width="170" height="315" rx="8" fill="#1e293b" stroke="#fbbf24" stroke-width="1.5"/>
    <rect width="170" height="34" rx="8" fill="url(#goldGrad6)"/>
    <text x="85" y="22" fill="#0f172a" font-family="system-ui, sans-serif" font-size="12" font-weight="800" text-anchor="middle">1. DIVINE WISDOM</text>
    <text x="12" y="60" fill="#f8fafc" font-family="system-ui, sans-serif" font-size="11" font-weight="700">• Prayer at Gibeon</text>
    <text x="12" y="76" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10">Asked for discerning</text>
    <text x="12" y="90" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10">heart, not riches.</text>
    <text x="12" y="120" fill="#f8fafc" font-family="system-ui, sans-serif" font-size="11" font-weight="700">• Proverbial Genius</text>
    <text x="12" y="136" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10">3,000 proverbs &amp;</text>
    <text x="12" y="150" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10">1,005 songs.</text>
    <text x="12" y="180" fill="#f8fafc" font-family="system-ui, sans-serif" font-size="11" font-weight="700">• Natural Sciences</text>
    <text x="12" y="196" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10">Botany &amp; Zoology.</text>
  </g>

  <!-- Pillar 2: Judicial Discernment -->
  <g transform="translate(220, 90)">
    <rect width="170" height="315" rx="8" fill="#1e293b" stroke="#38bdf8" stroke-width="1.5"/>
    <rect width="170" height="34" rx="8" fill="#0284c7"/>
    <text x="85" y="22" fill="#ffffff" font-family="system-ui, sans-serif" font-size="12" font-weight="700" text-anchor="middle">2. JUSTICE &amp; RULING</text>
    <text x="12" y="60" fill="#f8fafc" font-family="system-ui, sans-serif" font-size="11" font-weight="700">• Two Mothers Case</text>
    <text x="12" y="76" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10">Dispute over one</text>
    <text x="12" y="90" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10">living baby boy.</text>
    <text x="12" y="120" fill="#f8fafc" font-family="system-ui, sans-serif" font-size="11" font-weight="700">• The Sword Test</text>
    <text x="12" y="136" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10">Exposed true mother's</text>
    <text x="12" y="150" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10">unselfish compassion.</text>
    <text x="12" y="180" fill="#f8fafc" font-family="system-ui, sans-serif" font-size="11" font-weight="700">• National Awe</text>
    <text x="12" y="196" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10">God's justice visible.</text>
  </g>

  <!-- Pillar 3: Temple Construction -->
  <g transform="translate(410, 90)">
    <rect width="170" height="315" rx="8" fill="#1e293b" stroke="#10b981" stroke-width="1.5"/>
    <rect width="170" height="34" rx="8" fill="#059669"/>
    <text x="85" y="22" fill="#ffffff" font-family="system-ui, sans-serif" font-size="12" font-weight="700" text-anchor="middle">3. TEMPLE BUILDER</text>
    <text x="12" y="60" fill="#f8fafc" font-family="system-ui, sans-serif" font-size="11" font-weight="700">• 7-Year Construction</text>
    <text x="12" y="76" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10">On Mount Moriah</text>
    <text x="12" y="90" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10">in Jerusalem.</text>
    <text x="12" y="120" fill="#f8fafc" font-family="system-ui, sans-serif" font-size="11" font-weight="700">• Finest Materials</text>
    <text x="12" y="136" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10">Lebanese cedar,</text>
    <text x="12" y="150" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10">Ophir gold, bronze.</text>
    <text x="12" y="180" fill="#f8fafc" font-family="system-ui, sans-serif" font-size="11" font-weight="700">• Ark Enthroned</text>
    <text x="12" y="196" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10">Glory cloud filled it.</text>
  </g>

  <!-- Pillar 4: International Trade -->
  <g transform="translate(600, 90)">
    <rect width="170" height="315" rx="8" fill="#1e293b" stroke="#a855f7" stroke-width="1.5"/>
    <rect width="170" height="34" rx="8" fill="#7e22ce"/>
    <text x="85" y="22" fill="#ffffff" font-family="system-ui, sans-serif" font-size="12" font-weight="700" text-anchor="middle">4. GLOBAL TRADE</text>
    <text x="12" y="60" fill="#f8fafc" font-family="system-ui, sans-serif" font-size="11" font-weight="700">• Hiram of Tyre</text>
    <text x="12" y="76" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10">Timber &amp; maritime</text>
    <text x="12" y="90" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10">merchant fleets.</text>
    <text x="12" y="120" fill="#f8fafc" font-family="system-ui, sans-serif" font-size="11" font-weight="700">• Queen of Sheba</text>
    <text x="12" y="136" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10">Global prestige</text>
    <text x="12" y="150" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10">&amp; diplomacy.</text>
    <text x="12" y="180" fill="#f8fafc" font-family="system-ui, sans-serif" font-size="11" font-weight="700">• 12 Districts</text>
    <text x="12" y="196" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10">Administrative grid.</text>
  </g>
</svg>"""


def get_svg_lesson_7():
    return """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 450" width="100%" height="100%">
  <defs>
    <linearGradient id="bgGrad7" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#0f172a"/>
      <stop offset="50%" stop-color="#1e293b"/>
      <stop offset="100%" stop-color="#0f172a"/>
    </linearGradient>
    <linearGradient id="emeraldGrad7" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#10b981"/>
      <stop offset="100%" stop-color="#047857"/>
    </linearGradient>
    <linearGradient id="roseGrad7" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#f43f5e"/>
      <stop offset="100%" stop-color="#be123c"/>
    </linearGradient>
  </defs>
  <rect width="800" height="450" fill="url(#bgGrad7)" rx="14"/>
  <rect x="15" y="15" width="770" height="420" fill="none" stroke="#334155" stroke-width="1.5" stroke-dasharray="6 4" rx="10"/>

  <text x="400" y="42" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="18" font-weight="700" text-anchor="middle">SOLOMON'S PARADOX: SACRED TEMPLE VS. SPIRITUAL COMPROMISE</text>
  <text x="400" y="64" fill="#94a3b8" font-family="system-ui, sans-serif" font-size="12" text-anchor="middle">1 Kings 6-8, 11: The Sacred Centrality of the Temple &amp; The Tragic Cost of Idolatry</text>

  <!-- Left: Importance of Temple -->
  <g transform="translate(40, 90)">
    <rect width="335" height="315" rx="10" fill="#1e293b" stroke="#10b981" stroke-width="1.5"/>
    <rect width="335" height="38" rx="10" fill="url(#emeraldGrad7)"/>
    <text x="167" y="24" fill="#ffffff" font-family="system-ui, sans-serif" font-size="13" font-weight="800" text-anchor="middle">FUNCTIONS OF THE JERUSALEM TEMPLE</text>

    <text x="16" y="70" fill="#f8fafc" font-family="system-ui, sans-serif" font-size="12" font-weight="700">• Center of Worship &amp; Sacrifices</text>
    <text x="26" y="88" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="11">National altar for atonement and praise.</text>

    <text x="16" y="120" fill="#f8fafc" font-family="system-ui, sans-serif" font-size="12" font-weight="700">• Symbol of God's Dwelling Presence</text>
    <text x="26" y="138" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="11">Housed Ark of Covenant in Holy of Holies.</text>

    <text x="16" y="170" fill="#f8fafc" font-family="system-ui, sans-serif" font-size="12" font-weight="700">• Pillar of National Unity</text>
    <text x="26" y="188" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="11">3 yearly pilgrimage festivals (Passover, etc.).</text>

    <text x="16" y="220" fill="#f8fafc" font-family="system-ui, sans-serif" font-size="12" font-weight="700">• Supreme Judicial Court &amp; School</text>
    <text x="26" y="238" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="11">Interpreted Law of Moses; scribal education.</text>

    <text x="16" y="270" fill="#f8fafc" font-family="system-ui, sans-serif" font-size="12" font-weight="700">• Sacred Life Ceremonies</text>
    <text x="26" y="288" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="11">Purification, dedication, infant presentation.</text>
  </g>

  <!-- Right: Solomon's Downfall -->
  <g transform="translate(425, 90)">
    <rect width="335" height="315" rx="10" fill="#1e293b" stroke="#f43f5e" stroke-width="1.5"/>
    <rect width="335" height="38" rx="10" fill="url(#roseGrad7)"/>
    <text x="167" y="24" fill="#ffffff" font-family="system-ui, sans-serif" font-size="13" font-weight="800" text-anchor="middle">THE ANATOMY OF SOLOMON'S DOWNFALL</text>

    <text x="16" y="70" fill="#fca5a5" font-family="system-ui, sans-serif" font-size="12" font-weight="700">• 1,000 Wives &amp; Concubines</text>
    <text x="26" y="88" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="11">Forbidden alliances with pagan nations.</text>

    <text x="16" y="120" fill="#fca5a5" font-family="system-ui, sans-serif" font-size="12" font-weight="700">• High Places for Molech &amp; Ashtoreth</text>
    <text x="26" y="138" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="11">Built pagan altars on Mount of Olives.</text>

    <text x="16" y="170" fill="#fca5a5" font-family="system-ui, sans-serif" font-size="12" font-weight="700">• Heavy Taxation &amp; Forced Labor</text>
    <text x="26" y="188" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="11">Oppressed Israelites; fueled tribal bitterness.</text>

    <text x="16" y="220" fill="#fca5a5" font-family="system-ui, sans-serif" font-size="12" font-weight="700">• Misplaced Priorities</text>
    <text x="26" y="238" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="11">13 years on palace vs. 7 years on temple.</text>

    <text x="16" y="270" fill="#fecdd3" font-family="system-ui, sans-serif" font-size="12" font-weight="700">• Consequence: Kingdom Divided</text>
    <text x="26" y="288" fill="#fca5a5" font-family="system-ui, sans-serif" font-size="11">Torn away from Rehoboam (North vs. South).</text>
  </g>
</svg>"""


def get_svg_lesson_8():
    return """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 450" width="100%" height="100%">
  <defs>
    <linearGradient id="bgGrad8" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#0f172a"/>
      <stop offset="50%" stop-color="#1e293b"/>
      <stop offset="100%" stop-color="#0f172a"/>
    </linearGradient>
    <linearGradient id="goldGrad8" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#f59e0b"/>
      <stop offset="100%" stop-color="#d97706"/>
    </linearGradient>
  </defs>
  <rect width="800" height="450" fill="url(#bgGrad8)" rx="14"/>
  <rect x="15" y="15" width="770" height="420" fill="none" stroke="#334155" stroke-width="1.5" stroke-dasharray="6 4" rx="10"/>

  <text x="400" y="42" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="18" font-weight="700" text-anchor="middle">THE FIVE PILLARS OF ETHICAL LEADERSHIP</text>
  <text x="400" y="64" fill="#94a3b8" font-family="system-ui, sans-serif" font-size="12" text-anchor="middle">Biblical Framework for Choosing Leaders of Integrity in School, Church &amp; Society</text>

  <!-- Central Hub: INTEGRITY -->
  <circle cx="400" cy="230" r="62" fill="url(#goldGrad8)" stroke="#fbbf24" stroke-width="2"/>
  <text x="400" y="226" fill="#0f172a" font-family="system-ui, sans-serif" font-size="14" font-weight="800" text-anchor="middle">LEADER OF</text>
  <text x="400" y="244" fill="#0f172a" font-family="system-ui, sans-serif" font-size="14" font-weight="800" text-anchor="middle">INTEGRITY</text>

  <!-- Connecting Lines -->
  <line x1="400" y1="168" x2="400" y2="115" stroke="#38bdf8" stroke-width="2" stroke-dasharray="4 3"/>
  <line x1="455" y1="195" x2="620" y2="140" stroke="#38bdf8" stroke-width="2" stroke-dasharray="4 3"/>
  <line x1="445" y1="275" x2="590" y2="345" stroke="#38bdf8" stroke-width="2" stroke-dasharray="4 3"/>
  <line x1="355" y1="275" x2="210" y2="345" stroke="#38bdf8" stroke-width="2" stroke-dasharray="4 3"/>
  <line x1="345" y1="195" x2="180" y2="140" stroke="#38bdf8" stroke-width="2" stroke-dasharray="4 3"/>

  <!-- 5 Surrounding Nodes -->
  <!-- Node 1: Fear of God (Top) -->
  <g transform="translate(300, 75)">
    <rect width="200" height="55" rx="8" fill="#1e293b" stroke="#38bdf8" stroke-width="1.5"/>
    <text x="100" y="22" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="12" font-weight="700" text-anchor="middle">1. FEAR OF GOD</text>
    <text x="100" y="40" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10" text-anchor="middle">Divine accountability &amp; reverence</text>
  </g>

  <!-- Node 2: Servant Heart (Top Right) -->
  <g transform="translate(560, 115)">
    <rect width="200" height="55" rx="8" fill="#1e293b" stroke="#10b981" stroke-width="1.5"/>
    <text x="100" y="22" fill="#10b981" font-family="system-ui, sans-serif" font-size="12" font-weight="700" text-anchor="middle">2. SERVANT HEART</text>
    <text x="100" y="40" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10" text-anchor="middle">Selfless service, not exploitation</text>
  </g>

  <!-- Node 3: Justice & Fairness (Bottom Right) -->
  <g transform="translate(530, 320)">
    <rect width="210" height="55" rx="8" fill="#1e293b" stroke="#a855f7" stroke-width="1.5"/>
    <text x="105" y="22" fill="#a855f7" font-family="system-ui, sans-serif" font-size="12" font-weight="700" text-anchor="middle">3. JUSTICE &amp; FAIRNESS</text>
    <text x="105" y="40" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10" text-anchor="middle">No tribalism, bribery, or favoritism</text>
  </g>

  <!-- Node 4: Diligence & Stewardship (Bottom Left) -->
  <g transform="translate(60, 320)">
    <rect width="210" height="55" rx="8" fill="#1e293b" stroke="#f59e0b" stroke-width="1.5"/>
    <text x="105" y="22" fill="#f59e0b" font-family="system-ui, sans-serif" font-size="12" font-weight="700" text-anchor="middle">4. DILIGENCE &amp; STEWARD</text>
    <text x="105" y="40" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10" text-anchor="middle">Wise management of public resources</text>
  </g>

  <!-- Node 5: Humility & Repentance (Top Left) -->
  <g transform="translate(40, 115)">
    <rect width="200" height="55" rx="8" fill="#1e293b" stroke="#ef4444" stroke-width="1.5"/>
    <text x="100" y="22" fill="#ef4444" font-family="system-ui, sans-serif" font-size="12" font-weight="700" text-anchor="middle">5. HUMILITY &amp; REPENTANCE</text>
    <text x="100" y="40" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10" text-anchor="middle">Teachable; admits and corrects errors</text>
  </g>
</svg>"""


# ─────────────────────────────────────────────────────────────────────────────
# LESSON CONFIGURATIONS (ALL 8 LESSONS)
# ─────────────────────────────────────────────────────────────────────────────

LESSONS_DATA = [
    # ── LESSON 1 ──
    {
        "unit_order": 1,
        "lesson_order": 1,
        "title": "The Demand for a King in Israel",
        "biblical_source": "1 Samuel 8:1-22, 10:17-25",
        "image": {
            "title": "Visual Hook: Samuel Anointing Saul and the Assembly of Israel",
            "url": "https://upload.wikimedia.org/wikipedia/commons/4/4b/Samuel_anoints_Saul.jpg",
            "caption": "The prophet Samuel gathers the tribes of Israel to inaugurate the monarchy after the elders demanded a visible earthly king.",
            "author": "Julius Schnorr von Carolsfeld",
            "licensing": "Public Domain",
            "source": "Wikimedia Commons"
        },
        "goals": [
            "Outline the historical factors and social pressures that led the Israelites to demand a king",
            "Examine Samuel's solemn prophetic warnings regarding the heavy cost of human monarchy",
            "Evaluate how Christians can resist negative peer pressure and remain faithful to divine authority"
        ],
        "intro": """### Sharing Experiences & Familiar Connection

Imagine you are attending a school where there are no permanent school prefects or classroom captains. Instead, whenever a dispute arises or a classroom chore needs coordination, a student is appointed on the spot to handle the situation. Over time, you observe that neighboring schools have smart, uniformed school presidents who lead morning assemblies, direct student councils, and represent their institutions with great fanfare. You and your classmates might begin pleading with the principal: *"We want to be like other schools! Appoint a permanent school president to lead us face-to-face and make us look organized!"*

This scenario captures exactly how the Israelites felt during the era of the Judges. Looking at the powerful, centralized monarchies surrounding them, they clamored for an earthly, visible warrior king they could see, rather than placing their faith in their invisible, sovereign King—Yahweh God.""",
        "core_scripture": """### Biblical Foundation: 1 Samuel 8:4-9 & 8:19-20

> "So all the elders of Israel gathered together and came to Samuel at Ramah. They said to him, 'You are old, and your sons do not follow your ways; now appoint a king to lead us, such as all the other nations have.'
>
> But when they said, 'Give us a king to lead us,' this displeased Samuel; so he prayed to the Lord. And the Lord told him: 'Listen to all that the people are saying to you; it is not you they have rejected, but they have rejected me as their king. As they have done from the day I brought them up out of Egypt until this day, forsaking me and serving other gods, so they are doing to you. Now listen to them; but warn them solemnly and let them know what the king who will reign over them will claim as his rights.' ...
>
> But the people refused to listen to Samuel. 'No!' they said. 'We want a king over us. Then we will be like all the other nations, with a king to lead us and to go out before us and fight our battles.'" (1 Samuel 8:4-9, 19-20)""",
        "theological_pillars": """### Theological Dimensions: Theocracy vs. Monarchy

1. **The Nature of Israel's Theocracy:** For over two centuries following their settlement in Canaan, Israel functioned as a tribal confederacy under direct divine sovereignty (**Theocracy**). God raised charismatic **Judges** (such as Deborah, Gideon, and Samson) during national crises to deliver the people from oppression.
2. **The Spiritual Breach of Conformity:** Israel's primary spiritual failure was not merely administrative; it was an abandonment of their unique covenant identity. Demanding a king to be *"like all the other nations"* violated God's command for Israel to remain a distinct, holy nation consecrated to the Lord (Exodus 19:5-6).
3. **The Root of Rejection:** God revealed to Samuel that the demand for a human king represented a direct rejection of Yahweh's invisible reign. The people traded reliance on divine protection for the false security of human armor, chariots, and earthly generals.
4. **Prophetic Accountability:** Even when permitting the monarchy, God established that Israel's king would not be an absolute despot like pagan monarchs. The king remained a subordinate vassal subject to God's Torah and accountable to God's prophets.""",
        "svg_func": get_svg_lesson_1,
        "deep_dive": """### Deep Dive: Historical Context & Samuel's Prophetic Warnings

The transition from the Judges to the Monarchy was accelerated by five major historical factors:

#### 1. The Corruption of Samuel's Sons
Samuel appointed his sons, **Joel** and **Abijah**, as judges in Beersheba. Unlike their godly father, they were greedy for dishonest gain, accepted bribes, and perverted justice, destroying public confidence in hereditary leadership.

#### 2. The Philistine Military Threat
The Philistines possessed iron weapons, disciplined standing armies, and war chariots. Israel's decentralized tribal militia felt vulnerable and demanded a permanent commander-in-chief to lead them into battle.

#### 3. Geopolitical Pressure & Envy of Surrounding Monarchies
Israel was encircled by centralized kingdoms (Philistia, Moab, Edom, Ammon). The Israelites envied the outward prestige, royal courts, and visible pomp of these pagan nations.

#### 4. The Price of Monarchy (Samuel's Warnings)
Samuel faithfully laid out the oppressive reality of royal governance (1 Samuel 8:10-18):
- **Military Draft:** Forcible conscription of Israel's sons to serve in cavalry, infantry, and weapon manufacturing.
- **Forced Labor:** Exploitation of daughters as royal bakers, perfumers, and palace cooks.
- **Land Seizure (Eminent Domain):** Confiscation of citizens' prime vineyards, olive groves, and fields to reward royal favorites.
- **Heavy Taxation:** Imposition of a 10% tithe on grain, vineyards, and livestock to sustain the extravagant court.
- **Loss of Liberty:** The eventual transformation of free covenant citizens into state servants and laborers.""",
        "practical": {
            "title": "Action Framework: Resisting Conformity & Standing for Values",
            "steps": [
                "Identify areas of subtle peer pressure where the crowd urges you to compromise your moral standards.",
                "Discern the hidden long-term costs of compromising your faith to fit in with popular trends.",
                "Seek wise spiritual counsel from trusted parents, pastors, or mentors before making life-altering choices.",
                "Commit daily to God's sovereign authority over your academic, social, and personal life."
            ]
        },
        "kenyan_context": """### Kenyan Real-World Context: Peer Pressure & Youth Leadership

In modern Kenyan secondary schools and communities, young people constantly face intense pressure to conform to popular secular subcultures—such as experimenting with substance abuse, cheating in national examinations, or engaging in cyberbullying simply to look "cool" or fit in with influential cliques. 

Just as the ancient elders of Israel ignored Samuel's clear warnings because they were captivated by the outward glamor of pagan nations, youth today often trade their moral integrity for temporary social validation. As CBC Grade 9 learners, upholding Christian values requires courage. True leadership does not mean blindly copying what everyone else is doing, but having the conviction to stand up for righteousness, honesty, and divine truth in your school and neighborhood.""",
        "youtube": {
            "title": "BibleProject: 1 Samuel — The Rise of Israel's Monarchy",
            "youtube_id": "QkJ431smxG4",
            "description": "An insightful exploration of 1 Samuel, examining Israel's demand for a king, Samuel's warnings, and the transition from theocracy to monarchy."
        },
        "reflection": """### Spiritual Reflection & Ethical Application

- **Self-Examination:** In what areas of your daily school routine do you feel tempted to say, *"I want to do this because everyone else is doing it"*?
- **True Security:** Are you trusting in visible, human solutions (popularity, wealth, powerful connections) rather than placing your ultimate confidence in God's guidance?
- **Prayer:** *Lord God, You are my true King and Guide. Grant me the discernment to recognize dangerous worldly pressures and the moral courage to obey Your Word even when the crowd walks in the opposite direction. Amen.*""",
        "takeaways": [
            "Israel demanded a king due to the corruption of Samuel's sons, Philistine military aggression, and a desire to be like surrounding pagan nations.",
            "Demanding a human monarch constituted a direct spiritual rejection of Yahweh's sovereign theocratic rule over Israel.",
            "Samuel warned that a human king would impose forced conscription, exploit labor, seize private property, and levy heavy taxes.",
            "Christian learners must resist conformity and peer pressure, prioritizing God's enduring truth over transient social popularity."
        ],
        "mcq": {
            "question": "What was the primary spiritual failure of the Israelites when they demanded a human king in 1 Samuel 8?",
            "options": [
                "A. They refused to build a tabernacle in Shiloh.",
                "B. They rejected God as their sovereign King to conform to pagan nations.",
                "C. They wanted to reinstate the sacrificial laws of Egypt.",
                "D. They sought to abolish the Levitical priesthood completely."
            ],
            "answer": "B",
            "correct_answer": "B",
            "explanation": "By demanding a visible king to be 'like all the other nations,' Israel rejected Yahweh's direct, sovereign rule over them as a holy, consecrated covenant people."
        }
    },

    # ── LESSON 2 ──
    {
        "unit_order": 2,
        "lesson_order": 2,
        "title": "Saul's Rise, Achievements, and Failures",
        "biblical_source": "1 Samuel 9-11, 13, 15, 28, 31",
        "image": {
            "title": "Visual Hook: Samuel Rebuking King Saul",
            "url": "https://upload.wikimedia.org/wikipedia/commons/e/e0/Samuel_and_Saul_by_John_Sargent.jpg",
            "caption": "The prophet Samuel solemnly rebukes King Saul after his selective obedience regarding the Amalekites, proclaiming that obedience is better than sacrifice.",
            "author": "John Singer Sargent",
            "licensing": "Public Domain",
            "source": "Wikimedia Commons"
        },
        "goals": [
            "Analyze the military and political achievements of King Saul as Israel's first monarch",
            "Explain the spiritual causes of Saul's rejection by God, focusing on impatience and rationalized disobedience",
            "Apply the principle that obedience is better than sacrifice to everyday Christian moral decision-making"
        ],
        "intro": """### Sharing Experiences & Familiar Connection

Have you ever been given a clear, direct instruction by your parent or teacher—such as *"Wait here until I return with the keys"* or *"Do not open this laboratory cabinet"*—but because you felt impatient, anxious, or pressured by classmates, you decided to take matters into your own hands? You might have rationalized: *"I'm doing this for a good cause, so nobody will mind."* Yet when the authority figure returned, your actions caused serious trouble.

King Saul made this fatal spiritual mistake. Endowed with great physical stature, charismatic leadership, and military victories, he repeatedly substituted his personal convenience and public opinion for God's exact commands, discovering that outward religious rituals can never substitute for inward obedience.""",
        "core_scripture": """### Biblical Foundation: 1 Samuel 15:22-23

> "But Samuel replied:
> 'Does the Lord delight in burnt offerings and sacrifices as much as in obeying the Lord?
> To obey is better than sacrifice, and to heed is better than the fat of rams.
> For rebellion is like the sin of divination, and arrogance like the evil of idolatry.
> Because you have rejected the word of the Lord, he has rejected you as king.'" (1 Samuel 15:22-23)""",
        "theological_pillars": """### Theological Dimensions: The Downfall of Self-Willed Leadership

1. **Divine Calling vs. Human Presumption:** Saul was divinely chosen and anointed by the Holy Spirit. However, holding sacred office does not exempt a leader from absolute submission to God's moral law.
2. **The Danger of Impatience (Gilgal):** When faced with a crisis, taking matters into one's own hands instead of waiting on God demonstrates a lack of genuine faith. Saul usurped the priestly office by offering burnt sacrifices at Gilgal.
3. **Rationalized Disobedience (The Amalekites):** Partial obedience is complete disobedience in God's sight. Sparing King Agag and the finest livestock while claiming they were kept "for sacrifices" proved that Saul feared his soldiers' opinions more than God's command.
4. **The Peril of Apostasy (Endor):** When God withdrew His presence due to unrepented rebellion, Saul fell into occult consultation with a medium at Endor, directly violating the Torah (Deuteronomy 18:10-12).""",
        "svg_func": get_svg_lesson_2,
        "deep_dive": """### Deep Dive: Saul's Successes, Tragic Errors, and Lessons

#### Saul's Notable Achievements
- **Divine Anointing & Tribe Elevation:** Divinely anointed from the smallest tribe (Benjamin), Saul unified Israel's fractured tribes under a single command.
- **Military Victories:** He successfully liberated Jabesh Gilead from the brutal Ammonites (1 Samuel 11) and repelled Philistine incursions, securing national borders.
- **Personal Courage:** He demonstrated exceptional battlefield bravery during the early years of his reign.

#### The Three Fatal Failures
1. **Presumptuous Sacrifice at Gilgal (1 Samuel 13:8-14):** Terrified by deserting soldiers and an advancing Philistine army, Saul refused to wait for Samuel's arrival on the seventh day and offered the burnt offering himself. Samuel declared that Saul's dynasty would not endure.
2. **Selective Obedience with the Amalekites (1 Samuel 15:1-26):** Saul spared King Agag and the best sheep and cattle, blaming his troops when confronted. Samuel delivered the landmark verdict: *"To obey is better than sacrifice."* God rejected Saul as king.
3. **Consultation of the Medium of Endor (1 Samuel 28:3-25):** Plagued by terror and abandoned by God's Spirit, Saul disguised himself to consult a necromancer, sealing his tragic doom on Mount Gilboa (1 Samuel 31).

#### Core Moral Lessons
- **Inward Integrity vs. Outward Show:** Performing religious acts cannot compensate for a rebellious heart.
- **Patience in Crisis:** True character is tested when circumstances look desperate.
- **Shunning the Occult:** Christians must stay completely away from witchcraft, horoscopes, and mediums.""",
        "practical": {
            "title": "Action Framework: Practicing Wholehearted Obedience",
            "steps": [
                "Examine your actions to ensure you are not practicing partial obedience or making excuses for known wrongs.",
                "Refuse to rationalize shortcuts or dishonesty under the pretext of achieving good academic results.",
                "Practice patience when facing anxiety or pressure, waiting actively on God's guidance and timing.",
                "Cultivate genuine humility by admitting faults immediately without shifting blame to classmates or friends."
            ]
        },
        "kenyan_context": """### Kenyan Real-World Context: Integrity Over Outward Religious Pomp

In Kenyan society, people frequently observe leaders or public figures who attend lavish church fundraisers, give massive donations, and display outward piety, yet engage in corrupt practices, embezzlement of public funds, or tribal nepotism during working hours. 

King Saul represents this very trap: attempting to use animal sacrifices to mask active defiance of God's commands. For CBC Grade 9 learners, genuine Christian living is not measured by merely singing in the school choir or attending Christian Union meetings, but by demonstrating honesty in examinations, respecting school rules when teachers are absent, and treating every classmate with dignity and justice.""",
        "youtube": {
            "title": "BibleProject: 1 Samuel — The Tragedy of King Saul",
            "youtube_id": "QkJ431smxG4",
            "description": "An exploration of Saul's character flaws, his fear of people, and the tragic consequences of his pride and disobedience."
        },
        "reflection": """### Spiritual Reflection & Ethical Application

- **Heart Check:** Have you ever obeyed a school rule or parental instruction halfway, while secretly keeping what you wanted for yourself?
- **Accountability:** When corrected by an authority figure, do you react with defensiveness and blame-shifting like Saul, or with humble acknowledgment?
- **Prayer:** *Heavenly Father, cleanse my heart of pride, impatience, and self-justification. Teach me to value wholehearted obedience to Your commandments above public praise or empty rituals. Amen.*""",
        "takeaways": [
            "Saul began his reign with humility and achieved significant military victories over the Ammonites and Philistines.",
            "Saul forfeited his dynasty at Gilgal by offering sacrifices presumptuously rather than waiting for the prophet Samuel.",
            "Saul was rejected as king after sparing Agag and the Amalekite livestock, proving that partial obedience is disobedience.",
            "The golden biblical principle stands: To obey the Lord is far better than religious sacrifices and empty rituals."
        ],
        "mcq": {
            "question": "Why did God reject Saul as king of Israel following the military campaign against the Amalekites in 1 Samuel 15?",
            "options": [
                "A. Saul refused to construct a monument in Carmel.",
                "B. Saul spared King Agag and the best livestock, disobeying God's explicit command.",
                "C. Saul lost the Ark of the Covenant to the Philistines.",
                "D. Saul failed to pay wages to his standing army."
            ],
            "answer": "B",
            "correct_answer": "B",
            "explanation": "Saul selectively obeyed God's command by sparing Agag and the prime livestock, then rationalized his disobedience by blaming his soldiers."
        }
    },

    # ── LESSON 3 ──
    {
        "unit_order": 3,
        "lesson_order": 3,
        "title": "David's Calling and Anointing",
        "biblical_source": "1 Samuel 16:1-23, 17:1-58",
        "image": {
            "title": "Visual Hook: Samuel Anointing the Shepherd Boy David",
            "url": "https://upload.wikimedia.org/wikipedia/commons/c/c2/Samuel_anointing_David%2C_by_Julius_Schnorr_von_Carolsfeld.jpg",
            "caption": "The venerable prophet Samuel pours oil over the youthful shepherd David in Bethlehem as his father Jesse and brothers look on in amazement.",
            "author": "Julius Schnorr von Carolsfeld",
            "licensing": "Public Domain",
            "source": "Wikimedia Commons"
        },
        "goals": [
            "Describe the narrative of Samuel's mission to Jesse's home in Bethlehem and the divine selection of David",
            "Explain the theological principle that God looks at inner character and faith rather than outward physical appearance",
            "Examine how David practiced humble service, patience, and courage in obscurity before his public elevation"
        ],
        "intro": """### Sharing Experiences & Familiar Connection

Have you ever witnessed sports captains or class leaders picking team members for an inter-house football match or a school debate? Almost instinctively, they select the tallest, strongest, most athletic, or most vocal students first. If you are small, quiet, or reserved, you might be left standing on the sidelines, feeling overlooked and undervalued.

In this lesson, we discover that God operates by a completely different standard. While human beings are easily dazzled by height, muscular build, and outward swagger, the Creator looks straight into the human heart. When the prophet Samuel went to Bethlehem to anoint Israel's next king, God bypassed seven tall, handsome brothers and chose a forgotten young shepherd boy tending sheep in the wilderness!""",
        "core_scripture": """### Biblical Foundation: 1 Samuel 16:6-13

> "When they arrived, Samuel saw Eliab and thought, 'Surely the Lord’s anointed stands here before the Lord.'
>
> But the Lord said to Samuel, 'Do not consider his appearance or his height, for I have rejected him. The Lord does not look at the things people look at. People look at the outward appearance, but the Lord looks at the heart.'
>
> Then Jesse called Abinadab and had him pass in front of Samuel. But Samuel said, 'The Lord has not chosen this one either.' ... Jesse had seven of his sons pass before Samuel, but Samuel said to him, 'The Lord has not chosen these.' So he asked Jesse, 'Are these all the sons you have?'
>
> 'There is still the youngest,' Jesse answered. 'He is tending the sheep.' Samuel said, 'Send for him; we will not sit down until he arrives.'
>
> So he sent for him and had him brought in. He was glowing with health and had a fine appearance and handsome features. Then the Lord said, 'Rise and anoint him; this is the one.' So Samuel took the horn of oil and anointed him in the presence of his brothers, and from that day on the Spirit of the Lord came powerfully upon David." (1 Samuel 16:6-13)""",
        "theological_pillars": """### Theological Dimensions: Divine Election & Character Formation

1. **Sovereign Divine Election:** God chooses leaders based on spiritual suitability and heart alignment, not human social hierarchies, age privilege, or physical intimidation.
2. **Heart vs. Appearance (1 Samuel 16:7):** Human perspective is inherently superficial, evaluating people by height, wealth, and charisma. God searches the inner motives, humility, and steadfast faith of the soul.
3. **Preparation in the Secret Place:** David's spiritual stamina was forged in solitude—defending his father's sheep from lions and bears, communing with God through the lyre/harp, and writing Psalms.
4. **Patience Under Anointing:** Even after being anointed king, David did not scheme to depose Saul. He returned to his sheep, served Saul humbly in the royal court, and trusted God's timing.""",
        "svg_func": get_svg_lesson_3,
        "deep_dive": """### Deep Dive: From Bethlehem's Pastures to Saul's Palace & Elah's Valley

#### 1. The Anointing in Bethlehem (1 Samuel 16:1-13)
God instructed Samuel to fill his horn with oil and travel to Bethlehem. Jesse paraded seven impressive sons:
- **Eliab (The Eldest):** Possessed tall stature and commanding presence, but his heart lacked the humility required for divine leadership.
- **The Seven Passed Over:** Each was presented, but God spoke clearly: *"The Lord has not chosen these."*
- **David the Youngest:** Overlooked even by his family, David was summoned from the pasture. God confirmed: *"Rise and anoint him; this is the one."*

#### 2. Humble Service in Saul's Court (1 Samuel 16:14-23)
When an distressing spirit tormented Saul, David was brought to court as a skilled lyre musician. David's anointed music brought spiritual relief to Saul, and David became Saul's trusted armor-bearer, serving with loyalty.

#### 3. Faith and Courage Against Goliath (1 Samuel 17)
While Saul and Israel's veteran army trembled before the Philistine champion Goliath for 40 days, David arrived with food for his brothers. Moved by righteous zeal for God's honor, David declared: *"The battle is the Lord's!"* Armed with only a sling, five smooth stones, and unwavering faith, David defeated Goliath, demonstrating that God delivers not with sword and spear, but by His Spirit.""",
        "practical": {
            "title": "Action Framework: Cultivating Inner Character in Obscurity",
            "steps": [
                "Focus on cultivating unseen virtues—honesty, prayerfulness, and kindness—rather than chasing shallow popularity.",
                "Excel in small, unglamorous duties at home and school (cleaning, chores, private study) with diligence.",
                "Rely on God's strength when facing intimidating challenges or 'giants' in your academics or personal life.",
                "Serve those in authority over you with respect and loyalty, trusting God to elevate you in His perfect timing."
            ]
        },
        "kenyan_context": """### Kenyan Real-World Context: Overcoming Stereotypes & Discovering Hidden Potential

In Kenyan society, young people often face prejudice based on background, socioeconomic status, family lineage, or physical appearance. A student from an underprivileged rural school or an informal urban settlement may feel they cannot achieve greatness or lead effectively compared to affluent peers.

David's calling reminds us that God's assessment does not depend on outward privilege or social standing. In Kenya today, many renowned innovators, athletes, community champions, and spiritual leaders began in humble, overlooked environments. What qualifies a young person before God is not social status, but a heart rich in integrity, hard work, fear of God, and perseverance.""",
        "youtube": {
            "title": "BibleProject: 1 Samuel — David the Anointed King",
            "youtube_id": "QkJ431smxG4",
            "description": "An overview of David's election, his character of radical trust in God, and his humble rise through suffering and exile."
        },
        "reflection": """### Spiritual Reflection & Ethical Application

- **Introspection:** If God were to examine your inner thoughts, motivations, and secret habits right now, what qualities of honesty, humility, and faith would He find?
- **Judging Others:** Do you tend to judge your fellow learners by their uniforms, shoes, speech, or outward appearance rather than their character?
- **Prayer:** *Lord God, You look at the heart. Cleanse my inner thoughts, purify my motives, and mold me into a servant of integrity, patience, and courage for Your kingdom. Amen.*""",
        "takeaways": [
            "God rejected Jesse's seven elder sons and chose the youngest, David the shepherd, establishing that God looks at the heart.",
            "David's courage and spiritual character were forged in solitude while tending sheep and defending them from predators.",
            "After his anointing, David demonstrated humility by returning to his flock and serving King Saul faithfully with harp music.",
            "David defeated the giant Goliath through unwavering faith in God's power, declaring that the battle belongs to the Lord."
        ],
        "mcq": {
            "question": "What fundamental principle did God declare to Samuel when evaluating Jesse's eldest son Eliab in 1 Samuel 16:7?",
            "options": [
                "A. Anointed leaders must always belong to the tribe of Benjamin.",
                "B. Only the firstborn son possesses the spiritual right to inherit royal office.",
                "C. People look at the outward appearance, but the Lord looks at the heart.",
                "D. Physical height and military combat experience are the primary qualifications for kingship."
            ],
            "answer": "C",
            "correct_answer": "C",
            "explanation": "God explicitly corrected Samuel's human bias toward physical stature, teaching that inner character and heart alignment are God's true criteria for leadership."
        }
    },

    # ── LESSON 4 ──
    {
        "unit_order": 4,
        "lesson_order": 4,
        "title": "King David's Achievements and Failures",
        "biblical_source": "2 Samuel 5-7, 11-12, Psalm 51",
        "image": {
            "title": "Visual Hook: The Prophet Nathan Confronting King David",
            "url": "https://upload.wikimedia.org/wikipedia/commons/e/ea/Nathan_and_David.jpg",
            "caption": "The prophet Nathan points an accusing finger at King David after recounting the parable of the poor man's lamb, declaring 'You are the man!'",
            "author": "Julius Schnorr von Carolsfeld",
            "licensing": "Public Domain",
            "source": "Wikimedia Commons"
        },
        "goals": [
            "Evaluate the major military, political, and religious achievements of King David's 40-year reign",
            "Analyze David's moral failures concerning Bathsheba and Uriah the Hittite, and trace the consequences of unchecked power",
            "Contrast David's broken, sincere repentance in Psalm 51 with Saul's defensive blame-shifting"
        ],
        "intro": """### Sharing Experiences & Familiar Connection

Have you ever witnessed a highly admired school leader, an acclaimed athlete, or an esteemed community role model make a devastating moral mistake that shocked everyone? It is deeply sobering when someone blessed with immense talents falls into serious wrongdoing.

King David is celebrated as Israel's greatest earthly monarch—a courageous warrior, gifted poet, and *"a man after God's own heart."* Yet at the peak of his power, he committed shocking sins of adultery and murder. However, what distinguished David from Saul was not that David was sinless, but how he responded when confronted: with shattered, authentic repentance before God rather than self-justifying excuses.""",
        "core_scripture": """### Biblical Foundation: 2 Samuel 12:7-13 & Psalm 51:1-4

> "Then Nathan said to David, 'You are the man! This is what the Lord, the God of Israel, says: I anointed you king over Israel, and I delivered you from the hand of Saul... Why did you despise the word of the Lord by doing what is evil in his eyes? You struck down Uriah the Hittite with the sword and took his wife to be your own.' ...
>
> Then David said to Nathan, 'I have sinned against the Lord.' Nathan replied, 'The Lord has taken away your sin. You are not going to die.' (2 Samuel 12:7-9, 13)
>
> Have mercy on me, O God, according to your unfailing love; according to your great compassion blot out my transgressions. Wash away all my iniquity and cleanse me from my sin. For I know my transgressions, and my sin is always before me. Against you, you only, have I sinned and done what is evil in your sight." (Psalm 51:1-4)""",
        "theological_pillars": """### Theological Dimensions: Power, Accountability & Authentic Repentance

1. **The Trap of Complacency:** Spiritual drift often occurs during times of ease and success rather than hardship. David stayed home in palace comfort when kings went out to battle (2 Samuel 11:1).
2. **The Progression of Sin:** Unchecked lust led to adultery with Bathsheba, deceitful cover-up schemes, abuse of military authority, and the cold-blooded murder of faithful soldier Uriah.
3. **Prophetic Confrontation & Law Supremacy:** Israel's king was not above the law. God dispatched Nathan the prophet to hold the monarch accountable through the brilliant parable of the stolen ewe lamb.
4. **The Anatomy of True Repentance (Psalm 51):** Unlike Saul who defended himself to preserve public reputation, David accepted full responsibility, acknowledged his guilt against God, and cried out for inward cleansing and renewal.""",
        "svg_func": get_svg_lesson_4,
        "deep_dive": """### Deep Dive: David's Golden Achievements vs. The Bathsheba Scandal

#### 1. David's Remarkable Achievements
- **National Unification & Expansion:** Reigned 40 years (7 in Hebron, 33 in Jerusalem), defeating the Philistines, Moabites, Ammonites, and Edomites to secure Israel's promised borders.
- **Jerusalem as Capital:** Captured the neutral Jebusite stronghold of Zion, naming it the *City of David* and overcoming tribal jealousies.
- **Religious Centralization:** Brought the **Ark of the Covenant** to Jerusalem with great rejoicing, making the capital both the political and spiritual center of worship.
- **Literary & Liturgical Legacy:** Composed numerous Psalms that became the foundation for temple hymnody and modern Christian devotion.
- **Covenant Loyalty & Kindness:** Honored his covenant with Jonathan by seeking out and caring for Saul's crippled grandson, Mephibosheth (2 Samuel 9).

#### 2. The Grave Moral Fall (2 Samuel 11)
- Stayed behind in Jerusalem while General Joab besieged Rabbah.
- Saw Bathsheba bathing, inquired about her, and committed adultery with her.
- When Bathsheba became pregnant, David summoned Uriah from the battlefield to cover up the scandal. When Uriah loyally refused to sleep at home while his comrades camped in open fields, David ordered Joab to place Uriah at the front line to be killed.

#### 3. Nathan's Parable and Sincere Repentance (2 Samuel 12, Psalm 51)
Nathan exposed David's conscience with the story of a wealthy man stealing a poor man's only pet lamb. David confessed without excuses: *"I have sinned against the Lord."* Though God extended forgiveness, severe consequences followed, including sword, rebellion (Absalom), and turmoil within his household.""",
        "practical": {
            "title": "Action Framework: Practicing Radical Accountability & Repentance",
            "steps": [
                "Guard against complacency and idleness during times of leisure or academic success.",
                "Take immediate responsibility for mistakes without shifting blame, making excuses, or covering up.",
                "Welcome constructive correction from teachers, parents, and spiritual mentors with a teachable spirit.",
                "Seek daily spiritual renewal through sincere confession and prayer, asking God to create in you a clean heart."
            ]
        },
        "kenyan_context": """### Kenyan Real-World Context: Leadership Accountability & Ethical Transparency

In Kenyan public life, corruption, abuse of office, and misuse of state resources frequently occur when leaders view themselves as untouchable and unaccountable to the public or the law. When scandals are uncovered, many leaders resort to denials, legal technicalities, or tribal mobilization to evade responsibility.

King David's response to Nathan provides a powerful leadership model for Kenya. A true leader does not claim moral perfection, but demonstrates transparency, accepts accountability when wrong, and seeks genuine restitution. For Grade 9 learners aspiring to student council leadership or community roles, integrity means leading with an open conscience and taking personal responsibility for your actions.""",
        "youtube": {
            "title": "BibleProject: 2 Samuel — The Golden Age & The Fall of David",
            "youtube_id": "YvoWDXNDJgs",
            "description": "An overview of 2 Samuel, tracing David's political rise, the Davidic covenant, his moral failure with Bathsheba, and family fallout."
        },
        "reflection": """### Spiritual Reflection & Ethical Application

- **Self-Examination:** When you hurt a classmate, tell a lie, or break a school regulation, do you try to cover it up with more lies, or do you confess honestly?
- **Grace and Consequences:** Why does God forgive the repentant sinner while still allowing natural consequences to unfold?
- **Prayer:** *Create in me a clean heart, O God, and renew a steadfast spirit within me. Do not cast me from Your presence or take Your Holy Spirit from me. Restore to me the joy of Your salvation. Amen.*""",
        "takeaways": [
            "David unified Israel, established Jerusalem as the political and spiritual capital, and brought the Ark of the Covenant to the city.",
            "At the height of ease, David fell into adultery with Bathsheba and orchestrated the murder of Uriah the Hittite.",
            "God sent the prophet Nathan to confront David using the powerful parable of the stolen ewe lamb.",
            "David accepted full personal responsibility and repented brokenly in Psalm 51, modeling true accountability before God."
        ],
        "mcq": {
            "question": "Which prophet did God send to confront King David after his sins of adultery with Bathsheba and the murder of Uriah?",
            "options": [
                "A. Prophet Samuel",
                "B. Prophet Elijah",
                "C. Prophet Nathan",
                "D. Prophet Ahijah"
            ],
            "answer": "C",
            "correct_answer": "C",
            "explanation": "God dispatched Nathan, who used the convicting parable of the poor man's pet ewe lamb to bring King David to genuine confession and repentance."
        }
    },

    # ── LESSON 5 ──
    {
        "unit_order": 5,
        "lesson_order": 5,
        "title": "David as an Ancestor of Jesus Christ",
        "biblical_source": "2 Samuel 7:12-16, Matthew 1:1, Luke 1:32-33",
        "image": {
            "title": "Visual Hook: The Jesse Tree & Messianic Lineage of David",
            "url": "https://upload.wikimedia.org/wikipedia/commons/3/36/Jesse_tree_from_the_Scherenberg_Psalter.jpg",
            "caption": "A medieval illumination of the Tree of Jesse, depicting the genealogical lineage connecting King David directly to Jesus Christ.",
            "author": "Scherenberg Psalter Master",
            "licensing": "Public Domain",
            "source": "Wikimedia Commons"
        },
        "goals": [
            "Explain the theological significance of the unconditional Davidic Covenant in 2 Samuel 7",
            "Analyze the reasons why God did not permit David to construct the physical temple in Jerusalem",
            "Demonstrate how the New Testament records the fulfillment of God's promises to David in the person and eternal reign of Jesus Christ"
        ],
        "intro": """### Sharing Experiences & Familiar Connection

Have you ever wanted to undertake a grand project for your parents or school—such as building a new house or purchasing an expensive gift—but they lovingly told you: *"Thank you for your generous heart, but that is not your task right now. Focus on your studies and let us care for you."*

When King David settled into his luxurious cedar palace in Jerusalem, he felt convicted that the Ark of God remained in a humble goat-skin tent (Tabernacle). He desired to build a magnificent brick temple for God. But God responded through Nathan with an extraordinary covenant promise: *"You will not build Me a house; instead, I will build you a 'house'—an everlasting dynasty that will culminate in the Savior of the world!"*""",
        "core_scripture": """### Biblical Foundation: 2 Samuel 7:12-16 & Luke 1:31-33

> "When your days are over and you rest with your ancestors, I will raise up your offspring to succeed you, your own flesh and blood, and I will establish his kingdom. He is the one who will build a house for my Name, and I will establish the throne of his kingdom forever. I will be his father, and he will be my son... Your house and your kingdom will endure forever before me; your throne will be established forever." (2 Samuel 7:12-14, 16)
>
> "You will conceive and give birth to a son, and you are to call him Jesus. He will be great and will be called the Son of the Most High. The Lord God will give him the throne of his father David, and he will reign over Jacob’s descendants forever; his kingdom will never end." (Luke 1:31-33)""",
        "theological_pillars": """### Theological Dimensions: The Davidic Covenant & Messianic Hope

1. **The Unconditional Davidic Covenant:** Unlike the conditional Mosaic covenant based on legal obedience, God's covenant with David was a gracious, unconditional promise of an eternal dynasty, throne, and kingdom.
2. **Physical Temple vs. Eternal Dynasty:** God redirected David's attention from a temporary brick building to an eternal spiritual legacy. David's son Solomon would build the physical temple, but God would build David an everlasting house.
3. **Why David Could Not Build the Temple:** David was a warrior who had fought many wars and shed much blood (1 Chronicles 22:8). God reserved the temple construction for a man of peace (Solomon).
4. **The Ultimate Messianic Fulfillment:** The Davidic Covenant finds its eternal climax in **Jesus Christ**, who was born of David's line according to the flesh and whose spiritual kingdom transcends all earthly boundaries forever.""",
        "svg_func": get_svg_lesson_5,
        "deep_dive": """### Deep Dive: Tracing the Messianic Lineage & New Testament Fulfillment

#### 1. Key Promises of the Davidic Covenant (2 Samuel 7)
- **A Renowned Name:** God promised to make David's name great among all the leaders of the earth.
- **Peace & Security for Israel:** A permanent dwelling place free from oppression.
- **An Everlasting Royal Line:** An unbroken dynasty leading to an eternal King.
- **Father-Son Relationship:** God promised special fatherly fellowship with David's royal heir.

#### 2. Reasons God Reserved Temple Building for Solomon
- **Man of Bloodshed vs. Man of Peace:** David's reign was characterized by military warfare, whereas Solomon's reign represented shalom (peace).
- **God's Omnipresence:** God reminded David that He had never requested a cedar house; the Almighty cannot be confined to physical walls.
- **Divine Timing:** God prioritizes the building of spiritual character and kingdom foundations before physical structures.

#### 3. New Testament Proofs of Messianic Fulfillment
- **Gospel Genealogies:** Matthew opens his gospel with: *"This is the genealogy of Jesus the Messiah the son of David, the son of Abraham"* (Matthew 1:1). Luke traces Mary's lineage back to David (Luke 3:23-38).
- **The Angelic Annunciation:** Gabriel declared to Mary that God would give Jesus the throne of His father David (Luke 1:32-33).
- **Birthplace:** Jesus was born in Bethlehem, the ancient City of David (Luke 2:4-7).
- **Messianic Titles:** Hailed by blind Bartimaeus (*"Jesus, Son of David, have mercy on me!"* - Mark 10:47) and celebrated by crowds during the Triumphal Entry (Matthew 21:9).""",
        "practical": {
            "title": "Action Framework: Submitting Personal Ambition to God's Purpose",
            "steps": [
                "Recognize that God's plans for your future are far greater and more enduring than your immediate desires.",
                "Accept God's redirects and 'No' answers in prayer with trust, humility, and peace.",
                "Anchor your daily hope and loyalty in Jesus Christ, the eternal King whose kingdom never ends.",
                "Invest your talents in building people and spiritual character rather than focusing solely on material accumulation."
            ]
        },
        "kenyan_context": """### Kenyan Real-World Context: Enduring Legacy & Spiritual Heritage

In Kenya, families and communities place immense value on ancestral inheritance, family names, and long-lasting generational legacies. Many parents work tirelessly to leave behind land, businesses, and family houses for their children.

The Davidic Covenant reminds Grade 9 learners that the greatest legacy one can inherit or pass on is not physical buildings or wealth, but a steadfast spiritual foundation of faith in Jesus Christ. Earthly political regimes and physical properties decay over time, but the spiritual kingdom of Jesus Christ provides eternal salvation, moral purpose, and hope for every Kenyan family and community.""",
        "youtube": {
            "title": "BibleProject: 2 Samuel — The Davidic Covenant",
            "youtube_id": "YvoWDXNDJgs",
            "description": "An exploration of God's covenant with David in 2 Samuel 7 and how it points forward to the eternal reign of Jesus Christ."
        },
        "reflection": """### Spiritual Reflection & Ethical Application

- **Trusting God's 'No':** Have you ever experienced disappointment when a plan you prayed for did not work out? How does David's reaction teach you to trust God's greater plan?
- **Kingdom Allegiance:** Is Jesus Christ truly the King and Lord over your private thoughts, friendships, and daily ambitions?
- **Prayer:** *Lord Jesus Christ, eternal Son of David, You reign forever over all creation. I submit my personal plans, academic ambitions, and life dreams into Your sovereign hands. Establish Your kingdom in my heart today. Amen.*""",
        "takeaways": [
            "David desired to build a physical temple, but God covenanted to build David an eternal spiritual house and dynasty.",
            "God rejected David's offer to build the temple because David was a warrior who had shed much blood in warfare.",
            "Solomon was chosen as a man of peace to construct the physical temple on Mount Moriah in Jerusalem.",
            "Jesus Christ fulfilled the Davidic Covenant as the Son of David whose resurrection established an eternal, unending kingdom."
        ],
        "mcq": {
            "question": "Why did God decline King David's offer to build a physical temple in Jerusalem according to 1 Chronicles 22:8 and 2 Samuel 7?",
            "options": [
                "A. David did not possess sufficient gold and cedar timber.",
                "B. David had been a warrior who shed much blood, so the task was reserved for Solomon, a man of peace.",
                "C. The elders of the northern tribes objected to the temple location.",
                "D. David was not an anointed descendant of the tribe of Levi."
            ],
            "answer": "B",
            "correct_answer": "B",
            "explanation": "God explicitly explained that because David had engaged in extensive military warfare and shed blood, the temple construction was reserved for his son Solomon, whose reign was marked by peace."
        }
    },

    # ── LESSON 6 ──
    {
        "unit_order": 6,
        "lesson_order": 6,
        "title": "Solomon's Accession, Request for Wisdom, and Achievements",
        "biblical_source": "1 Kings 3:1-28, 4:29-34, 5:1-18, 6:1-38",
        "image": {
            "title": "Visual Hook: The Judgment of King Solomon",
            "url": "https://upload.wikimedia.org/wikipedia/commons/e/e6/The_Judgment_of_Solomon_by_Peter_Paul_Rubens.jpg",
            "caption": "Peter Paul Rubens' masterpiece depicting King Solomon commanding a soldier to divide the disputed child, revealing the true mother through her selfless love.",
            "author": "Peter Paul Rubens",
            "licensing": "Public Domain",
            "source": "Wikimedia Commons"
        },
        "goals": [
            "Explain the narrative of Solomon's dream at Gibeon and his humble prayer for divine wisdom",
            "Demonstrate how Solomon exercised judicial discernment in the famous dispute between the two mothers",
            "Summarize Solomon's economic, architectural, and literary achievements during Israel's Golden Age"
        ],
        "intro": """### Sharing Experiences & Familiar Connection

If the Almighty God appeared to you tonight in a dream and said: *"Ask for whatever you want Me to give you,"* what would be your immediate request? Most people would instinctively ask for billions of shillings, luxury sports cars, fame, long life, or top grades without studying.

When young King Solomon was offered this incredible choice at Gibeon, he did not ask for wealth, military conquest, or personal glory. Instead, recognizing his youth and inexperience, he asked for a discerning heart to govern God's people with justice and distinguish between right and wrong. God was so pleased with this humble, selfless prayer that He granted him unmatched wisdom along with the riches and honor he never requested!""",
        "core_scripture": """### Biblical Foundation: 1 Kings 3:7-12 & 3:24-28

> "'Now, Lord my God, you have made your servant king in place of my father David. But I am only a little child and do not know how to carry out my duties. Your servant is here among the people you have chosen, a great people, too numerous to count or number. So give your servant a discerning heart to govern your people and to distinguish between right and wrong. For who is able to govern this great people of yours?'
>
> The Lord was pleased that Solomon had asked for this. So God said to him, 'Since you have asked for this and not for long life or wealth for yourself, nor have asked for the death of your enemies, but for discernment in administering justice, I will do what you have asked. I will give you a wise and discerning heart... Moreover, I will give you what you have not asked for—both wealth and honor.' (1 Kings 3:7-13)
>
> Then the king said, 'Bring me a sword.' So they brought a sword for the king. He then gave an order: 'Cut the living child in two and give half to one and half to the other.' The woman whose son was alive was deeply moved out of love for her son and said to the king, 'Please, my lord, give her the living baby! Don’t kill him!' But the other said, 'Neither I nor you shall have him. Cut him in two!' Then the king gave his ruling: 'Give the living baby to the first woman. Do not kill him; she is his mother.' (1 Kings 3:24-27)""",
        "theological_pillars": """### Theological Dimensions: The Priority of Divine Wisdom

1. **Wisdom vs. Mere Knowledge:** Knowledge is the accumulation of facts; **Biblical Wisdom (Chokhmah)** is the ability to apply God's truth to make righteous, life-affirming choices.
2. **The Humility of True Leadership:** Solomon acknowledged his personal inadequacy (*"I am only a little child"*), establishing that the fear of the Lord is the true beginning of wisdom (Proverbs 9:10).
3. **Justice as the Fruit of Wisdom:** Divine wisdom is not theoretical; it actively defends the vulnerable, unravels complex human deceptions, and establishes fairness in society.
4. **The Principle of Divine Provision (Matthew 6:33):** Seeking God's righteous kingdom and wisdom first results in God adding all other necessary blessings according to His will.""",
        "svg_func": get_svg_lesson_6,
        "deep_dive": """### Deep Dive: The Golden Age of Solomon's Monarchy

#### 1. The Famous Judicial Ruling (1 Kings 3:16-28)
Two women living in the same house gave birth. One baby died during the night due to suffocation, and its mother swapped the corpses. When both claimed the living infant before the royal court with no witnesses, Solomon applied brilliant psychological discernment by ordering a sword to divide the child. The false mother indifferently agreed (*"Cut him in two"*), while the true mother pleaded to surrender her child to preserve his life. Solomon restored the baby to his real mother, filling the nation with awe at God's wisdom.

#### 2. Architectural & Economic Achievements
- **Construction of the Temple (1 Kings 6):** A 7-year magnificent project on Mount Moriah utilizing prefabricated Lebanese cedar beams, bronze pillars (Jachin and Boaz), and pure Ophir gold overlays.
- **International Commerce & Trade Fleets:** Formed commercial alliances with King Hiram of Tyre, operating merchant fleets from Ezion-Geber trading in spices, timber, gold, silver, horses, and copper.
- **Administrative Precision:** Divided Israel into twelve administrative districts, each governed by an officer responsible for provisioning the royal court for one month annually.
- **Literary & Scientific Output (1 Kings 4:32-34):** Authored 3,000 proverbs and 1,005 songs; renowned as a naturalist and scholar of plants, beasts, birds, and fish.
- **International Diplomacy:** Received foreign monarchs, notably the Queen of Sheba, who marveled at his wisdom and statecraft.""",
        "practical": {
            "title": "Action Framework: Seeking Divine Wisdom in Daily Decisions",
            "steps": [
                "Ask God daily in prayer for wisdom to navigate complex academic and relational situations (James 1:5).",
                "Value character development and moral discernment above the pursuit of material possessions or exam shortcuts.",
                "Practice empathetic listening and discernment when mediating disagreements among classmates.",
                "Steward your talents and academic opportunities diligently to contribute positively to your community."
            ]
        },
        "kenyan_context": """### Kenyan Real-World Context: Academic Excellence & Moral Discernment

In the Kenyan education system under the CBC framework, learners are encouraged to develop critical thinking, problem-solving skills, and ethical values. However, many students mistakenly equate success purely with obtaining high marks by rote memorization, sometimes resorting to dishonest shortcuts.

Solomon's prayer highlights that intellectual capability without moral wisdom and the fear of God is dangerous. True success for a Kenyan Grade 9 learner lies in cultivating a discerning conscience—knowing how to choose trustworthy friends, resolving playground conflicts peacefully, using digital technology responsibly, and using knowledge to serve society with integrity.""",
        "youtube": {
            "title": "BibleProject: 1 & 2 Kings — Solomon's Wisdom & Reign",
            "youtube_id": "bVFW3wbi9pk",
            "description": "An exploration of Solomon's accession, his gift of divine wisdom, the glorious building of the temple, and the roots of his later compromise."
        },
        "reflection": """### Spiritual Reflection & Ethical Application

- **Priorities in Prayer:** When you pray before exams or daily studies, do you ask God primarily for wisdom, discernment, and integrity, or merely for high grades and material rewards?
- **Conflict Resolution:** How can you apply Solomon's empathetic understanding of human nature when solving disputes in your classroom or family?
- **Prayer:** *Lord God of all wisdom, grant me a discerning heart. Help me to distinguish between right and wrong, to choose truth over falsehood, and to honor You in all my academic pursuits. Amen.*""",
        "takeaways": [
            "Solomon asked God for a discerning heart to govern Israel rather than seeking riches, long life, or military conquest.",
            "God granted Solomon unmatched wisdom, accompanied by wealth, international honor, and national peace.",
            "Solomon demonstrated judicial discernment in the dispute between the two mothers, exposing the true mother through her selfless love.",
            "Solomon constructed the temple in Jerusalem, composed 3,000 proverbs, and expanded international trade networks."
        ],
        "mcq": {
            "question": "What did King Solomon ask of God during his dream encounter at Gibeon in 1 Kings 3?",
            "options": [
                "A. Unlimited gold and vast chariot armies.",
                "B. Long life and the complete destruction of all foreign enemies.",
                "C. A discerning heart (wisdom) to govern God's people with justice.",
                "D. Authorization to build a royal palace larger than the temple."
            ],
            "answer": "C",
            "correct_answer": "C",
            "explanation": "Solomon humbly recognized his inexperience and requested a discerning heart to administer justice and govern God's people wisely, pleasing God greatly."
        }
    },

    # ── LESSON 7 ──
    {
        "unit_order": 7,
        "lesson_order": 7,
        "title": "Solomon's Failures and the Temple's Importance",
        "biblical_source": "1 Kings 6-8, 11:1-43, 2 Chronicles 5-7",
        "image": {
            "title": "Visual Hook: Solomon's Temple in Ancient Jerusalem",
            "url": "https://upload.wikimedia.org/wikipedia/commons/5/5a/Solomon%27s_temple.jpg",
            "caption": "An architectural model of King Solomon's Temple in Jerusalem, illustrating the Holy of Holies, the Holy Place, and the surrounding courts of worship.",
            "author": "Phillip Medhurst Collection",
            "licensing": "CC BY-SA 3.0",
            "source": "Wikimedia Commons"
        },
        "goals": [
            "Analyze the critical spiritual, social, and judicial functions of the Temple constructed by Solomon in Jerusalem",
            "Examine the causes and progression of Solomon's spiritual apostasy in his later years (1 Kings 11)",
            "Evaluate how unchecked compromise, idolatry, and oppressive policies lead to spiritual ruin and national division"
        ],
        "intro": """### Sharing Experiences & Familiar Connection

Have you ever seen a brilliant, top-performing student who started high school with stellar grades and strong discipline, but gradually began hanging out with reckless friends, ignoring advice, and making small compromises until their performance collapsed completely? It is a sobering truth that a glorious start in life does not guarantee a successful finish unless you remain disciplined and faithful to the end.

King Solomon began his reign as the wisest monarch on earth, dedicating the magnificent Temple of God amidst heavenly glory. Yet in his later years, unchecked wealth, excessive foreign marriages, and pride caused his heart to turn away from God, leading him to construct pagan altars for horrific idols right on the hills overlooking Jerusalem!""",
        "core_scripture": """### Biblical Foundation: 1 Kings 11:1-4 & 11:9-11

> "King Solomon, however, loved many foreign women besides Pharaoh’s daughter—Moabites, Ammonites, Edomites, Sidonians and Hittites. They were from nations about which the Lord had told the Israelites, 'You must not intermarry with them, because they will surely turn your hearts after their gods.' Nevertheless, Solomon held fast to them in love. He had seven hundred wives of royal birth and three hundred concubines, and his wives turned his heart after other gods. As Solomon grew old, his wives turned his heart after other gods, and his heart was not fully devoted to the Lord his God, as the heart of David his father had been...
>
> The Lord became angry with Solomon because his heart had turned away from the Lord, the God of Israel, who had appeared to him twice. Although he had forbidden Solomon to follow other gods, Solomon did not keep the Lord’s command. So the Lord said to Solomon, 'Since this is your attitude and you have not kept my covenant and my decrees, which I commanded you, I will most certainly tear the kingdom away from you and give it to one of your subordinates.'" (1 Kings 11:1-4, 9-11)""",
        "theological_pillars": """### Theological Dimensions: Compromise, Torah Violation & Sacred Space

1. **The Functions of the Sacred Temple:** The Temple was not a magical talisman, but a consecrated sanctuary symbolizing God's covenant presence among His people, the central altar for atonement, and the focal point of national unity.
2. **The Direct Violation of Torah Commands:** Deuteronomy 17:16-17 explicitly forbade Israel's kings from accumulating excessive horses (military reliance), multiplying wives (foreign idolatrous treaties), or amassing excessive silver and gold (greed). Solomon violated all three prohibitions.
3. **The Gradual Creep of Compromise:** Solomon did not renounce God overnight. It began with diplomatic marriages, followed by accommodating his wives' foreign shrines, and culminated in actively worshipping pagan deities (**Molech** and **Ashtoreth**).
4. **Sovereign Judgment & Division:** God's covenant faithfulness remains unshakable, but human rebellion invites severe judgment. God decreed the tearing away of ten tribes from Solomon's son (Rehoboam), birthing the Divided Kingdom.""",
        "svg_func": get_svg_lesson_7,
        "deep_dive": """### Deep Dive: The Importance of the Temple vs. Solomon's Spiritual Collapse

#### 1. Key Functions and Importance of the Temple in Israel
- **Central Place of Worship & Atonement:** The exclusive sanctuary where morning and evening sacrifices, sin offerings, and national feasts were presented.
- **Sanctuary of God's Dwelling Presence:** Housed the Ark of the Covenant within the Holy of Holies; at dedication, the Shekinah glory cloud filled the house (1 Kings 8:10-11).
- **Symbol of National Cohesion:** Unifying center where all Israelite males gathered thrice annually (Passover, Pentecost/Weeks, Tabernacles).
- **Supreme Court & Education:** Seat of the high priestly court interpreting Mosaic law; center for training scribes and preserving sacred scrolls.
- **Rites of Passage:** Location for purification, infant presentations, tithe presentations, and national prayer in times of famine or warfare.

#### 2. The Five Pillars of Solomon's Downfall (1 Kings 11)
1. **Unchecked Polygamy & Forbidden Marriages:** 700 royal wives and 300 concubines from prohibited pagan nations.
2. **Gross Idolatry & Religious Syncretism:** Built high places for **Chemosh** (god of Moab) and **Molech** (the Ammonite deity associated with child sacrifice) on the Mount of Olives.
3. **Oppressive Forced Labor & Crushing Taxes:** Enslaved labor forces and levied exorbitant taxes to finance his 13-year palace construction, breeding tribal resentment.
4. **Misplaced Priorities:** Spent 13 years building his personal palace, but only 7 years on God's Temple.
5. **Covenant Rupture:** Resulted in God raising adversaries (Hadad the Edomite, Rezon of Damascus, Jeroboam son of Nebat) and decreeing the division of the kingdom.""",
        "practical": {
            "title": "Action Framework: Guarding Your Heart Against Spiritual Drift",
            "steps": [
                "Guard against 'small' moral compromises in academics, entertainment, and speech that erode your conscience.",
                "Choose close friends whose character, faith, and values draw you closer to God rather than pull you away.",
                "Keep your priorities aligned with God's Word, ensuring academic and personal ambitions do not become modern idols.",
                "Cultivate daily prayer and scripture reading to maintain a heart wholly devoted to God throughout your life."
            ]
        },
        "kenyan_context": """### Kenyan Real-World Context: Misplaced Priorities, Taxation & National Cohesion

In Kenyan history and contemporary governance, citizens often express deep frustration when government projects impose heavy taxation and national debt to fund extravagant executive lifestyles and non-essential luxuries, while ordinary citizens struggle with basic living costs.

Solomon's oppressive labor policies and heavy taxation created the deep-seated grievances that eventually tore Israel apart under his successor Rehoboam. For young Kenyans, this history demonstrates that true leadership requires empathy, economic justice, and moderation. Furthermore, in personal life, allowing modern idols (money, materialism, corrupt peer groups) to compromise your Christian walk will inevitably fracture your future and relationships.""",
        "youtube": {
            "title": "BibleProject: 1 & 2 Kings — Solomon's Downfall & The Divided Kingdom",
            "youtube_id": "bVFW3wbi9pk",
            "description": "An analysis of Solomon's idolatry, the oppressive taxation that alienated the northern tribes, and the fracture into two kingdoms."
        },
        "reflection": """### Spiritual Reflection & Ethical Application

- **Heart Allegiance:** Solomon was the wisest man alive, yet wisdom alone did not prevent his moral collapse. Why is daily obedience more vital than mere intellectual brilliance?
- **Modern Idols:** What subtle influences (social media obsession, materialism, ungodly peer groups) threaten to turn your heart away from God?
- **Prayer:** *Lord God, keep my heart wholly devoted to You. Guard me against pride, greed, and moral compromise. Help me not only to start well, but to finish my life's race with faithfulness and integrity. Amen.*""",
        "takeaways": [
            "Solomon's Temple served as Israel's central place of sacrifice, God's dwelling presence, national unity, and judicial interpretation.",
            "Solomon violated the Torah by multiplying foreign wives, excessive wealth, and chariots, leading his heart into gross idolatry.",
            "Solomon constructed pagan high places for Ashtoreth, Chemosh, and Molech, bringing severe divine anger upon his reign.",
            "Because of Solomon's covenant unfaithfulness and oppressive taxation, God decreed that ten tribes would be torn away from his dynasty."
        ],
        "mcq": {
            "question": "What was the primary spiritual consequence of King Solomon marrying hundreds of foreign women in 1 Kings 11?",
            "options": [
                "A. Israel was immediately conquered by the Pharaoh of Egypt.",
                "B. His foreign wives turned his heart away from God to worship pagan idols like Ashtoreth and Molech.",
                "C. The Phoenicians terminated all cedar trade agreements with Israel.",
                "D. The Ark of the Covenant was permanently removed from the Temple."
            ],
            "answer": "B",
            "correct_answer": "B",
            "explanation": "Solomon's foreign marriages violated God's explicit command, leading him directly into religious compromise and the worship of pagan detestable deities."
        }
    },

    # ── LESSON 8 ──
    {
        "unit_order": 8,
        "lesson_order": 8,
        "title": "Choosing Leaders of Integrity Today",
        "biblical_source": "1 Timothy 3:1-7, Titus 1:5-9, Deuteronomy 17:14-20",
        "image": {
            "title": "Visual Hook: Moses and the Elders of Integrity",
            "url": "https://upload.wikimedia.org/wikipedia/commons/e/eb/Moses_and_the_Seventy_Elders.jpg",
            "caption": "Moses selects capable, God-fearing men of truth who hate dishonest gain to serve as judges and leaders over Israel.",
            "author": "Julius Schnorr von Carolsfeld",
            "licensing": "Public Domain",
            "source": "Wikimedia Commons"
        },
        "goals": [
            "Synthesize the comparative leadership styles, strengths, and downfalls of King Saul, King David, and King Solomon",
            "Identify the five biblical pillars of ethical leadership outlined in the Old and New Testaments",
            "Apply biblical leadership criteria when electing student council leaders, voting in church, and engaging in civic duties"
        ],
        "intro": """### Sharing Experiences & Familiar Connection

Consider student council elections at your school. When candidates stand on the assembly podium to campaign, how do you decide who gets your vote? Do you vote for the classmate who distributes free sweets, makes loud and unrealistic promises, or wears the most fashionable clothes? Or do you vote for the student who is consistently honest in exams, responsible in daily duties, respectful to everyone, and genuinely concerned about learners' welfare?

Throughout our study of Israel's early monarchy, we have observed three distinct leadership profiles: Saul (insecure, excuse-making, people-pleaser), David (flawed yet deeply repentant, humble, God-focused), and Solomon (brilliant yet compromised by greed and idolatry). In this final lesson, we synthesize these timeless biblical lessons to establish how to choose and become leaders of genuine integrity today.""",
        "core_scripture": """### Biblical Foundation: 1 Timothy 3:1-7 & Titus 1:7-9

> "Now the overseer is to be above reproach, faithful to his wife, temperate, self-controlled, respectable, hospitable, able to teach, not given to drunkenness, not violent but gentle, not quarrelsome, not a lover of money. He must manage his own family well and see that his children obey him, and he must do so in a manner worthy of full respect... He must also have a good reputation with outsiders, so that he will not fall into disgrace and into the devil’s trap." (1 Timothy 3:2-4, 7)
>
> "Since an overseer manages God’s household, he must be blameless—not overbearing, not quick-tempered, not given to drunkenness, not violent, not pursuing dishonest gain. Rather, he must be hospitable, one who loves what is good, who is self-controlled, upright, holy and disciplined." (Titus 1:7-8)""",
        "theological_pillars": """### Theological Dimensions: Biblical Standards for Servant Leadership

1. **Character Precedes Competence:** In God's economy, a leader's moral integrity, self-control, and fear of God far outweigh external charm, oratory skills, or personal wealth.
2. **Servant Leadership (Mark 10:42-45):** Biblical leadership is not about dominating or exploiting subordinates, but humbly serving others for the common good, modeled perfectly by Jesus Christ.
3. **Justice and Impartiality (Mishpat):** A leader of integrity administers rules and resources fairly, without tribalism, nepotism, bribery, or favoritism.
4. **Stewardship & Financial Integrity:** Leaders must hate dishonest gain, manage community and school resources transparently, and practice moderation rather than extravagance.""",
        "svg_func": get_svg_lesson_8,
        "deep_dive": """### Deep Dive: Comprehensive Leadership Synthesis & The Five Pillars

#### 1. Comparative Leadership Matrix
| Leader | Core Strengths | Critical Downfall | Response to Confrontation | Key Takeaway for Today |
| :--- | :--- | :--- | :--- | :--- |
| **King Saul** | Physical stature, battlefield courage, initial humility | Impatience, selective obedience, fear of public opinion, consulting medium | Deflected blame to troops; sought public honor from Samuel | Religious show cannot compensate for inward disobedience. |
| **King David** | Absolute faith in God, brave, worshipful, centralized justice | Complacency, adultery with Bathsheba, murder of Uriah | Sincere, broken repentance (*"I have sinned against the Lord"* - Ps 51) | Integrity means taking total responsibility for one's failures. |
| **King Solomon** | Extraordinary wisdom, architectural mastery, global commerce | 1,000 wives/concubines, idolatry, heavy taxation, forced labor | Ignored divine warnings; defensiveness led to kingdom division | Intellectual genius without moral discipline leads to ruin. |

#### 2. The Five Pillars of Ethical Leadership
1. **The Fear of God:** Acknowledging accountability to divine authority, which fosters humility, honesty, and reverent living.
2. **Servant Heart:** Prioritizing the welfare, growth, and empowerment of the community over personal power or enrichment.
3. **Justice & Impartiality:** Administering rules, duties, and opportunities with uncompromising fairness, free from ethnic or social bias.
4. **Diligence & Financial Stewardship:** Managing public or school funds with meticulous transparency and abhorring all forms of corruption or bribery.
5. **Humility & Teachability:** Readily accepting constructive correction, admitting mistakes, and actively seeking wise counsel.""",
        "practical": {
            "title": "Action Framework: Evaluating and Practicing Ethical Leadership",
            "steps": [
                "Evaluate leadership candidates in school or community based on demonstrated character, honesty, and service, not bribery or popularity.",
                "Refuse to participate in electoral malpractices, gossip campaigns, or tribal voting blocs during student elections.",
                "Exemplify servant leadership in your current responsibilities (class monitor, dormitory prefect, group leader) by helping others.",
                "Cultivate personal accountability by inviting honest feedback from teachers, mentors, and trustworthy peers."
            ]
        },
        "kenyan_context": """### Kenyan Real-World Context: Transformative Leadership & Chapter Six of the Constitution

Article 10 (National Values and Principles of Governance) and Chapter Six (Leadership and Integrity) of the Constitution of Kenya 2010 establish high ethical standards for public leaders: integrity, competence, transparency, accountability, and selfless service. Unfortunately, electoral cycles are still frequently tainted by vote-buying, handouts, inflammatory tribal rhetoric, and broken campaign promises.

As Grade 9 CBC learners preparing to be future civic leaders, teachers, doctors, and innovators, internalizing biblical leadership principles is vital for the transformation of Kenya. When you vote in school elections or choose club executives, rejecting bribery and selecting candidates of proven moral integrity helps build a culture of honesty and good governance for the entire nation.""",
        "youtube": {
            "title": "BibleProject: Biblical Character — Justice & Servant Leadership",
            "youtube_id": "A14THPoc4-4",
            "description": "An exploration of biblical justice (mishpat and tzedakah) and how leaders are called to embody God's righteousness and service."
        },
        "reflection": """### Spiritual Reflection & Ethical Application

- **Self-Assessment:** If your classmates were to evaluate your leadership potential based on honesty, humility, and fairness, what would they say?
- **Civic Responsibility:** How can you actively encourage your peers to reject handouts and popularity contests in school elections, choosing leaders based on character?
- **Prayer:** *Almighty God, righteous Judge of all the earth, raise up leaders of integrity, humility, and justice in our schools, churches, and nation. Mold me into a servant leader who honors Your name and serves others with a pure heart. Amen.*""",
        "takeaways": [
            "Saul failed through excuse-making, David modeled broken repentance, and Solomon showed the danger of compromise despite immense wisdom.",
            "Biblical leadership demands leaders who are above reproach, temperate, self-controlled, hospitable, and not lovers of money.",
            "The five pillars of ethical leadership are the fear of God, servant heart, justice, financial stewardship, and teachability.",
            "Christian learners must reject superficial popularity and electoral bribery, selecting and embodying leaders of genuine moral integrity."
        ],
        "mcq": {
            "question": "Which crucial leadership quality distinguished King David from King Saul when confronted by a prophet regarding their sins?",
            "options": [
                "A. David blamed his commanding generals to protect royal prestige.",
                "B. David immediately accepted personal responsibility and repented with a broken heart before God.",
                "C. David offered double the required animal sacrifices to appease the public.",
                "D. David exiled the prophet Nathan from the royal court of Jerusalem."
            ],
            "answer": "B",
            "correct_answer": "B",
            "explanation": "While Saul repeatedly rationalized his disobedience and blamed his soldiers, David demonstrated authentic integrity by confessing 'I have sinned against the Lord' with deep, broken repentance (Psalm 51)."
        }
    }
]


# ─────────────────────────────────────────────────────────────────────────────
# INGESTION ENGINE
# ─────────────────────────────────────────────────────────────────────────────

def ingest_cbc_grade9_cre_topic4():
    print("=" * 80)
    print("STARTING INGESTION FOR GRADE 9 CRE TOPIC 4: 'Kings David and Solomon'")
    print("=" * 80)

    # 1. Resolve Hierarchy
    curriculum = Curriculum.objects.filter(name__icontains="CBC").first()
    if not curriculum:
        curriculum = Curriculum.objects.first()

    grade = Grade.objects.get(id=18)
    subject = Subject.objects.get(id=50)

    print(f"Target Curriculum : {curriculum.name} (ID: {curriculum.id})")
    print(f"Target Grade      : {grade.name} (ID: {grade.id})")
    print(f"Target Subject    : {subject.name} (ID: {subject.id})")

    with transaction.atomic():
        # Resolve Topic 4
        topic, t_created = Topic.objects.get_or_create(
            subject=subject,
            order=4,
            defaults={"name": "Kings David and Solomon"}
        )
        if not t_created and topic.name != "Kings David and Solomon":
            topic.name = "Kings David and Solomon"
            topic.save()

        print(f"Target Topic      : Order {topic.order} — {topic.name} (ID: {topic.id}) [Created: {t_created}]")

        # Clean existing units under Topic 4 to ensure clean state
        existing_units = LearningUnit.objects.filter(topic=topic)
        if existing_units.exists():
            print(f"[*] Cleaning {existing_units.count()} existing LearningUnits under Topic 4...")
            existing_units.delete()

        total_units = 0
        total_lessons = 0
        total_pages = 0
        total_blocks = 0
        total_assets = 0

        for cfg in LESSONS_DATA:
            u_order = cfg["unit_order"]
            l_title = cfg["title"]

            # Create LearningUnit
            unit = LearningUnit.objects.create(
                topic=topic,
                order=u_order,
                name=f"4.{u_order} {l_title}",
                description=f"Curriculum unit {u_order} covering {l_title} in Grade 9 CRE Topic 4."
            )
            total_units += 1

            # Create Lesson
            lesson = Lesson.objects.create(
                topic=topic,
                learning_unit=unit,
                title=l_title,
                status="published",
                version=1,
                immutable_metadata={
                    "grade": "Grade 9",
                    "subject": "CRE",
                    "topic_order": 4,
                    "topic_name": topic.name,
                    "unit_order": u_order,
                    "lesson_order": cfg["lesson_order"],
                    "curriculum_framework": "CBC Kenya"
                }
            )
            total_lessons += 1

            # ─── ASSETS (3 per lesson) ───
            # Asset 1: Curated Wikimedia Visual Image Hook
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
                    "resolved_image_url": img_info["url"]
                }
            )
            total_assets += 1

            # Asset 2: Custom Responsive Vector SVG Diagram
            svg_content = cfg["svg_func"]()
            svg_asset = LessonAsset.objects.create(
                lesson=lesson,
                asset_type="diagram",
                source_type="generated",
                storage_type="url",
                status="attached",
                title=f"Diagram: {l_title}",
                description=f"Responsive pedagogical vector SVG diagram illustrating {l_title}.",
                url=f"https://vlearn.africa/assets/diagrams/cre/grade9_topic_4_lesson_{u_order}.svg",
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

            # ─── 13 BLOCKS ACROSS 6 CARDS/PAGES ───

            # ── CARD 1 (Page 1): Discovery & Objectives (3 blocks) ──
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
                title="Sharing Experiences & Familiar Connection",
                content={"markdown": clean_text(cfg["intro"])}
            )

            # ── CARD 2 (Page 2): Scriptural Exegesis (2 blocks) ──
            LessonBlock.objects.create(
                lesson=lesson, page_number=2, page_title="Scriptural Exegesis",
                order=40, component_order=1,
                block_type="concept_explanation", component_type="concept_explanation",
                title="Core Biblical Foundation",
                content={"markdown": clean_text(cfg["core_scripture"])}
            )

            LessonBlock.objects.create(
                lesson=lesson, page_number=2, page_title="Scriptural Exegesis",
                order=45, component_order=2,
                block_type="concept_explanation", component_type="concept_explanation",
                title="Theological Foundations & Principles",
                content={"markdown": clean_text(cfg["theological_pillars"])}
            )

            # ── CARD 3 (Page 3): Pedagogical Diagram & Deep Dive (2 blocks) ──
            b5 = LessonBlock.objects.create(
                lesson=lesson, page_number=3, page_title="Pedagogical Diagram",
                order=50, component_order=1,
                block_type="suggested_diagram", component_type="suggested_diagram",
                title=f"Visual Architecture: {l_title}",
                content={
                    "title": f"Pedagogical Blueprint: {l_title}",
                    "caption": f"Comprehensive architectural vector diagram illustrating {l_title}.",
                    "svg": svg_content,
                    "svg_xml": svg_content
                }
            )
            b5.assets.add(svg_asset)

            LessonBlock.objects.create(
                lesson=lesson, page_number=3, page_title="Pedagogical Diagram",
                order=60, component_order=2,
                block_type="concept_explanation", component_type="concept_explanation",
                title="Historical Context & Theological Deep Dive",
                content={"markdown": clean_text(cfg["deep_dive"])}
            )

            # ── CARD 4 (Page 4): Practical Application & Context (2 blocks) ──
            LessonBlock.objects.create(
                lesson=lesson, page_number=4, page_title="Practical Application",
                order=70, component_order=1,
                block_type="step_process", component_type="step_process",
                title=clean_text(cfg["practical"]["title"]),
                content=clean_dict(cfg["practical"])
            )

            LessonBlock.objects.create(
                lesson=lesson, page_number=4, page_title="Practical Application",
                order=75, component_order=2,
                block_type="concept_explanation", component_type="concept_explanation",
                title="Kenyan Real-World Context & Youth Leadership",
                content={"markdown": clean_text(cfg["kenyan_context"])}
            )

            # ── CARD 5 (Page 5): Multimedia & Reflection (2 blocks) ──
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
                title="Spiritual Reflection & Ethical Values",
                content={"markdown": clean_text(cfg["reflection"])}
            )

            # ── CARD 6 (Page 6): Mastery Check & Key Takeaways (2 blocks) ──
            LessonBlock.objects.create(
                lesson=lesson, page_number=6, page_title="Mastery Check",
                order=100, component_order=1,
                block_type="summary", component_type="summary",
                title="Summary & Core Principles",
                content={
                    "title": f"Key Takeaways: {l_title}",
                    "takeaways": clean_dict(cfg["takeaways"])
                }
            )

            LessonBlock.objects.create(
                lesson=lesson, page_number=6, page_title="Mastery Check",
                order=110, component_order=2,
                block_type="knowledge_check", component_type="knowledge_check",
                title="Mastery Assessment",
                content=clean_dict(cfg["mcq"])
            )

            total_pages += 6
            total_blocks += 13
            print(f"  [+] Ingested Lesson {u_order:02d}/8: '{l_title}' (6 cards, 13 blocks, 3 assets)")

        print("=" * 80)
        print("INGESTION SUMMARY FOR GRADE 9 CRE TOPIC 4:")
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
    ingest_cbc_grade9_cre_topic4()
