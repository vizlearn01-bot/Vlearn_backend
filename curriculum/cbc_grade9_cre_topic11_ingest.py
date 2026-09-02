"""
VLearn CBC Grade 9 CRE — Topic 11: The Early Church
Production-Ready Ingestion & Visual Enrichment Engine

Curriculum: CBC
Grade: Grade 9 (ID: 18)
Subject: CRE (ID: 50)
Topic: Topic 11: The Early Church (Order: 11)

8 Discrete Units / Published Lessons:
  1. The Day of Pentecost: Birth of the Church (Acts 2:1-13, Joel 2:28-29)
  2. Characteristics of the Early Church (Acts 2:42-47, Acts 4:32-37)
  3. Miracles in the Early Church (Acts 3:1-10, Acts 5:12-16)
  4. Paul and Silas: The Prison Context (Acts 16:16-24)
  5. Paul and Silas: Praise in the Prison (Acts 16:25-28, Psalm 34:1)
  6. The Conversion of the Jailer (Acts 16:29-34, Romans 10:9)
  7. Characteristics of the Modern Church (1 Peter 2:9-10, Ephesians 4:11-16)
  8. The Call to Salvation Today (Romans 10:8-13, 2 Corinthians 5:17-20)

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
    # Strip bracket citations e.g. [1], [223], [1, 2], [72, 238]
    text = re.sub(r'\[(?:\d+(?:\.\d+)?(?:,\s*\d+(?:\.\d+)?)*|image_\d+|S\d+.*?|[\d,\s]{2,})\]', '', text)
    # Strip internal pedagogical tags
    text = re.sub(r'\[(VISUAL|BIBLE PASSAGE|BIBLE REFERENCE|CRITICAL THINKING|VALUES|MISCONCEPTION|INTERACTION|ETHICAL SCENARIO|KEY VERSE|REAL WORLD APPLICATION|BIBLICAL CONTEXT|PEDAGOGICAL ARCHITECTURE|PROJECT TITLE|REFLECTION)[^\]]*\]', '', text, flags=re.IGNORECASE)
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


# ─── 8 CUSTOM RESPONSIVE VECTOR SVGS (viewBox="0 0 800 450", #0f172a theme) ─────

def get_svg_lesson_1():
    return """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 450" width="100%" height="100%">
  <defs>
    <linearGradient id="bg1" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#0f172a"/>
      <stop offset="50%" stop-color="#1e293b"/>
      <stop offset="100%" stop-color="#0f172a"/>
    </linearGradient>
    <linearGradient id="fireGrad1" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#f59e0b"/>
      <stop offset="100%" stop-color="#ef4444"/>
    </linearGradient>
    <linearGradient id="windGrad1" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#0284c7"/>
      <stop offset="100%" stop-color="#38bdf8"/>
    </linearGradient>
    <linearGradient id="spiritGrad1" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#8b5cf6"/>
      <stop offset="100%" stop-color="#ec4899"/>
    </linearGradient>
  </defs>
  <rect width="800" height="450" fill="url(#bg1)" rx="14"/>
  <rect x="15" y="15" width="770" height="420" fill="none" stroke="#334155" stroke-width="1.5" stroke-dasharray="6 4" rx="10"/>

  <text x="400" y="45" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="17" font-weight="700" text-anchor="middle">THE DAY OF PENTECOST: BIRTH OF THE CHURCH (ACTS 2:1-13)</text>
  <text x="400" y="68" fill="#94a3b8" font-family="system-ui, sans-serif" font-size="12" text-anchor="middle">The Holy Spirit Outpouring, Prophetic Fulfillment, and the Global Apostolic Mission</text>

  <!-- Central Hub: Outpouring -->
  <rect x="280" y="90" width="240" height="65" rx="12" fill="url(#fireGrad1)" stroke="#fbbf24" stroke-width="2"/>
  <text x="400" y="118" fill="#0f172a" font-family="system-ui, sans-serif" font-size="14.5" font-weight="800" text-anchor="middle">HOLY SPIRIT OUTPOURING</text>
  <text x="400" y="138" fill="#1e293b" font-family="system-ui, sans-serif" font-size="11.5" font-weight="600" text-anchor="middle">Fulfillment of Joel 2:28-29</text>

  <!-- Connecting Lines -->
  <line x1="310" y1="155" x2="155" y2="195" stroke="#38bdf8" stroke-width="2" stroke-dasharray="4 3"/>
  <line x1="400" y1="155" x2="400" y2="195" stroke="#38bdf8" stroke-width="2" stroke-dasharray="4 3"/>
  <line x1="490" y1="155" x2="645" y2="195" stroke="#38bdf8" stroke-width="2" stroke-dasharray="4 3"/>

  <!-- 3 Pillars -->
  <!-- Pillar 1: Supernatural Manifestations -->
  <g transform="translate(40, 195)">
    <rect width="230" height="200" rx="10" fill="#1e293b" stroke="#38bdf8" stroke-width="1.5"/>
    <rect width="230" height="34" rx="10" fill="url(#windGrad1)"/>
    <text x="115" y="22" fill="#ffffff" font-family="system-ui, sans-serif" font-size="12" font-weight="700" text-anchor="middle">1. SUPERNATURAL SIGNS</text>
    <text x="15" y="58" fill="#f8fafc" font-family="system-ui, sans-serif" font-size="11" font-weight="700">• Violent Rushing Wind</text>
    <text x="15" y="74" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10">Divine breath of God filling</text>
    <text x="15" y="88" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10">the entire upper room.</text>
    <text x="15" y="112" fill="#f8fafc" font-family="system-ui, sans-serif" font-size="11" font-weight="700">• Tongues of Fire</text>
    <text x="15" y="128" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10">Individual flames resting on</text>
    <text x="15" y="142" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10">each disciple (purity &amp; power).</text>
    <text x="15" y="170" fill="#7dd3fc" font-family="system-ui, sans-serif" font-size="10" font-weight="600">Visible &amp; Audible Reality</text>
  </g>

  <!-- Pillar 2: Miracle of Human Tongues -->
  <g transform="translate(285, 195)">
    <rect width="230" height="200" rx="10" fill="#1e293b" stroke="#f59e0b" stroke-width="1.5"/>
    <rect width="230" height="34" rx="10" fill="#d97706"/>
    <text x="115" y="22" fill="#ffffff" font-family="system-ui, sans-serif" font-size="12" font-weight="700" text-anchor="middle">2. HUMAN TONGUES</text>
    <text x="15" y="58" fill="#f8fafc" font-family="system-ui, sans-serif" font-size="11" font-weight="700">• Native Languages</text>
    <text x="15" y="74" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10">Spoke existing dialects of</text>
    <text x="15" y="88" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10">pilgrims from 15+ nations.</text>
    <text x="15" y="112" fill="#f8fafc" font-family="system-ui, sans-serif" font-size="11" font-weight="700">• Reversal of Babel</text>
    <text x="15" y="128" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10">Overcoming language barriers</text>
    <text x="15" y="142" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10">to unite humanity in Christ.</text>
    <text x="15" y="170" fill="#fde68a" font-family="system-ui, sans-serif" font-size="10" font-weight="600">Universal Gospel Mission</text>
  </g>

  <!-- Pillar 3: Bold Preaching & 3,000 Converts -->
  <g transform="translate(530, 195)">
    <rect width="230" height="200" rx="10" fill="#1e293b" stroke="#34d399" stroke-width="1.5"/>
    <rect width="230" height="34" rx="10" fill="#059669"/>
    <text x="115" y="22" fill="#ffffff" font-family="system-ui, sans-serif" font-size="12" font-weight="700" text-anchor="middle">3. BOLD PREACHING</text>
    <text x="15" y="58" fill="#f8fafc" font-family="system-ui, sans-serif" font-size="11" font-weight="700">• Peter's Transformed Courage</text>
    <text x="15" y="74" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10">Proclaimed Jesus' death,</text>
    <text x="15" y="88" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10">resurrection, and Lordship.</text>
    <text x="15" y="112" fill="#f8fafc" font-family="system-ui, sans-serif" font-size="11" font-weight="700">• 3,000 Baptized in 1 Day</text>
    <text x="15" y="128" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10">Massive spiritual harvest</text>
    <text x="15" y="142" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10">marking Church's birthday.</text>
    <text x="15" y="170" fill="#a7f3d0" font-family="system-ui, sans-serif" font-size="10" font-weight="600">Power for Global Witness</text>
  </g>

  <text x="400" y="422" fill="#64748b" font-family="system-ui, sans-serif" font-size="10" text-anchor="middle">THEOLOGICAL TRUTH: THE HOLY SPIRIT EMPOWERS ORDINARY BELIEVERS FOR COURAGEOUS GLOBAL WITNESS</text>
</svg>"""


def get_svg_lesson_2():
    return """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 450" width="100%" height="100%">
  <defs>
    <linearGradient id="bg2" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#0f172a"/>
      <stop offset="50%" stop-color="#1e293b"/>
      <stop offset="100%" stop-color="#0f172a"/>
    </linearGradient>
    <linearGradient id="goldGrad2" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#f59e0b"/>
      <stop offset="100%" stop-color="#d97706"/>
    </linearGradient>
  </defs>
  <rect width="800" height="450" fill="url(#bg2)" rx="14"/>
  <rect x="15" y="15" width="770" height="420" fill="none" stroke="#334155" stroke-width="1.5" stroke-dasharray="6 4" rx="10"/>

  <text x="400" y="45" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="17" font-weight="700" text-anchor="middle">THE FIVE PILLARS OF THE EARLY CHURCH (ACTS 2:42-47)</text>
  <text x="400" y="68" fill="#94a3b8" font-family="system-ui, sans-serif" font-size="12" text-anchor="middle">The Structural Rhythm of Apostolic Doctrine, Koinonia, Sacrament, Worship, and Generosity</text>

  <!-- Pillar 1: Apostles' Teaching -->
  <g transform="translate(30, 95)">
    <rect width="135" height="295" rx="8" fill="#1e293b" stroke="#38bdf8" stroke-width="1.5"/>
    <rect width="135" height="34" rx="8" fill="#0284c7"/>
    <text x="67" y="22" fill="#ffffff" font-family="system-ui, sans-serif" font-size="11" font-weight="700" text-anchor="middle">1. DOCTRINE</text>
    <text x="10" y="60" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="10" font-weight="700">Apostles' Teaching</text>
    <text x="10" y="80" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="9.5">Grounded in the</text>
    <text x="10" y="96" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="9.5">words of Christ.</text>
    <text x="10" y="125" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="9.5">Studied daily to</text>
    <text x="10" y="141" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="9.5">prevent heresy &amp;</text>
    <text x="10" y="157" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="9.5">false teaching.</text>
    <rect x="10" y="235" width="115" height="38" rx="5" fill="#0f172a" stroke="#38bdf8" stroke-width="1"/>
    <text x="67" y="258" fill="#7dd3fc" font-family="system-ui, sans-serif" font-size="9" font-weight="700" text-anchor="middle">Spiritual Root</text>
  </g>

  <!-- Pillar 2: Fellowship (Koinonia) -->
  <g transform="translate(180, 95)">
    <rect width="135" height="295" rx="8" fill="#1e293b" stroke="#8b5cf6" stroke-width="1.5"/>
    <rect width="135" height="34" rx="8" fill="#7c3aed"/>
    <text x="67" y="22" fill="#ffffff" font-family="system-ui, sans-serif" font-size="11" font-weight="700" text-anchor="middle">2. KOINONIA</text>
    <text x="10" y="60" fill="#c084fc" font-family="system-ui, sans-serif" font-size="10" font-weight="700">Deep Fellowship</text>
    <text x="10" y="80" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="9.5">Egalitarian union</text>
    <text x="10" y="96" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="9.5">across rich, poor,</text>
    <text x="10" y="112" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="9.5">Jews &amp; Gentiles.</text>
    <text x="10" y="141" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="9.5">Mutual emotional</text>
    <text x="10" y="157" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="9.5">&amp; physical bond.</text>
    <rect x="10" y="235" width="115" height="38" rx="5" fill="#0f172a" stroke="#8b5cf6" stroke-width="1"/>
    <text x="67" y="258" fill="#d8b4fe" font-family="system-ui, sans-serif" font-size="9" font-weight="700" text-anchor="middle">Social Unity</text>
  </g>

  <!-- Pillar 3: Breaking of Bread -->
  <g transform="translate(330, 95)">
    <rect width="135" height="295" rx="8" fill="#1e293b" stroke="#f59e0b" stroke-width="1.5"/>
    <rect width="135" height="34" rx="8" fill="#d97706"/>
    <text x="67" y="22" fill="#ffffff" font-family="system-ui, sans-serif" font-size="11" font-weight="700" text-anchor="middle">3. BREAD</text>
    <text x="10" y="60" fill="#fbbf24" font-family="system-ui, sans-serif" font-size="10" font-weight="700">Breaking of Bread</text>
    <text x="10" y="80" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="9.5">Communal meals</text>
    <text x="10" y="96" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="9.5">in family homes.</text>
    <text x="10" y="125" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="9.5">Sacrament of the</text>
    <text x="10" y="141" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="9.5">Lord's Supper in</text>
    <text x="10" y="157" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="9.5">Jesus' memory.</text>
    <rect x="10" y="235" width="115" height="38" rx="5" fill="#0f172a" stroke="#f59e0b" stroke-width="1"/>
    <text x="67" y="258" fill="#fde68a" font-family="system-ui, sans-serif" font-size="9" font-weight="700" text-anchor="middle">Sacramental Life</text>
  </g>

  <!-- Pillar 4: Prayer & Praise -->
  <g transform="translate(480, 95)">
    <rect width="135" height="295" rx="8" fill="#1e293b" stroke="#ec4899" stroke-width="1.5"/>
    <rect width="135" height="34" rx="8" fill="#db2777"/>
    <text x="67" y="22" fill="#ffffff" font-family="system-ui, sans-serif" font-size="11" font-weight="700" text-anchor="middle">4. PRAYER</text>
    <text x="10" y="60" fill="#f472b6" font-family="system-ui, sans-serif" font-size="10" font-weight="700">Prayer &amp; Praise</text>
    <text x="10" y="80" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="9.5">Daily gatherings</text>
    <text x="10" y="96" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="9.5">in temple courts.</text>
    <text x="10" y="125" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="9.5">Passionate praise</text>
    <text x="10" y="141" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="9.5">and corporate</text>
    <text x="10" y="157" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="9.5">intercession.</text>
    <rect x="10" y="235" width="115" height="38" rx="5" fill="#0f172a" stroke="#ec4899" stroke-width="1"/>
    <text x="67" y="258" fill="#fbcfe8" font-family="system-ui, sans-serif" font-size="9" font-weight="700" text-anchor="middle">Devotional Power</text>
  </g>

  <!-- Pillar 5: Radical Generosity -->
  <g transform="translate(630, 95)">
    <rect width="135" height="295" rx="8" fill="#1e293b" stroke="#34d399" stroke-width="1.5"/>
    <rect width="135" height="34" rx="8" fill="#059669"/>
    <text x="67" y="22" fill="#ffffff" font-family="system-ui, sans-serif" font-size="11" font-weight="700" text-anchor="middle">5. GENEROSITY</text>
    <text x="10" y="60" fill="#6ee7b7" font-family="system-ui, sans-serif" font-size="10" font-weight="700">Shared Wealth</text>
    <text x="10" y="80" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="9.5">Sold land/houses;</text>
    <text x="10" y="96" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="9.5">shared resources.</text>
    <text x="10" y="125" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="9.5">No needy person</text>
    <text x="10" y="141" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="9.5">among them.</text>
    <text x="10" y="157" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="9.5">(Acts 4:34)</text>
    <rect x="10" y="235" width="115" height="38" rx="5" fill="#0f172a" stroke="#34d399" stroke-width="1"/>
    <text x="67" y="258" fill="#a7f3d0" font-family="system-ui, sans-serif" font-size="9" font-weight="700" text-anchor="middle">Mutual Aid</text>
  </g>

  <text x="400" y="422" fill="#64748b" font-family="system-ui, sans-serif" font-size="10" text-anchor="middle">OUTCOME: THE EARLY CHURCH ENJOYED FAVOR WITH ALL PEOPLE AND THE LORD ADDED DAILY THOSE BEING SAVED</text>
</svg>"""


def get_svg_lesson_3():
    return """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 450" width="100%" height="100%">
  <defs>
    <linearGradient id="bg3" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#0f172a"/>
      <stop offset="50%" stop-color="#1e293b"/>
      <stop offset="100%" stop-color="#0f172a"/>
    </linearGradient>
    <linearGradient id="miracleGrad3" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#0284c7"/>
      <stop offset="100%" stop-color="#38bdf8"/>
    </linearGradient>
  </defs>
  <rect width="800" height="450" fill="url(#bg3)" rx="14"/>
  <rect x="15" y="15" width="770" height="420" fill="none" stroke="#334155" stroke-width="1.5" stroke-dasharray="6 4" rx="10"/>

  <text x="400" y="45" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="17" font-weight="700" text-anchor="middle">MIRACLES AT THE BEAUTIFUL GATE: POWER &amp; HUMILITY (ACTS 3:1-16)</text>
  <text x="400" y="68" fill="#94a3b8" font-family="system-ui, sans-serif" font-size="12" text-anchor="middle">Apostolic Authority, Immediate Physical Restoration, and Absolute Deflection of Glory to Jesus</text>

  <!-- Left: The Physical Beggar -->
  <g transform="translate(40, 95)">
    <rect width="215" height="295" rx="10" fill="#1e293b" stroke="#f59e0b" stroke-width="1.5"/>
    <rect width="215" height="34" rx="10" fill="#d97706"/>
    <text x="107" y="22" fill="#ffffff" font-family="system-ui, sans-serif" font-size="11.5" font-weight="700" text-anchor="middle">1. EXPECTATION: ALMS</text>
    <text x="15" y="60" fill="#fde68a" font-family="system-ui, sans-serif" font-size="11" font-weight="700">• Crippled from Birth</text>
    <text x="15" y="78" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10">Carried daily to the temple</text>
    <text x="15" y="93" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10">gate called 'Beautiful'.</text>
    <text x="15" y="123" fill="#fde68a" font-family="system-ui, sans-serif" font-size="11" font-weight="700">• Seeking Silver &amp; Gold</text>
    <text x="15" y="141" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10">Expected temporary coins</text>
    <text x="15" y="156" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10">to survive one more day.</text>
    <rect x="15" y="235" width="185" height="42" rx="6" fill="#0f172a" stroke="#f59e0b" stroke-width="1"/>
    <text x="107" y="253" fill="#fbbf24" font-family="system-ui, sans-serif" font-size="10.5" font-weight="700" text-anchor="middle">Human Limitation</text>
    <text x="107" y="268" fill="#94a3b8" font-family="system-ui, sans-serif" font-size="9" text-anchor="middle">Money cannot restore broken legs</text>
  </g>

  <!-- Center: The Divine Miracle -->
  <g transform="translate(280, 95)">
    <rect width="240" height="295" rx="10" fill="#1e293b" stroke="#38bdf8" stroke-width="1.5"/>
    <rect width="240" height="34" rx="10" fill="#0284c7"/>
    <text x="120" y="22" fill="#ffffff" font-family="system-ui, sans-serif" font-size="11.5" font-weight="700" text-anchor="middle">2. THE DIVINE COMMAND</text>
    <text x="15" y="60" fill="#7dd3fc" font-family="system-ui, sans-serif" font-size="11" font-weight="700">• "In Jesus' Name, Walk!"</text>
    <text x="15" y="78" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10">Peter gave what he had:</text>
    <text x="15" y="93" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10">supernatural authority.</text>
    <text x="15" y="123" fill="#7dd3fc" font-family="system-ui, sans-serif" font-size="11" font-weight="700">• Instant Restoration</text>
    <text x="15" y="141" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10">Feet and ankle bones</text>
    <text x="15" y="156" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10">received instant strength.</text>
    <rect x="15" y="235" width="210" height="42" rx="6" fill="#0f172a" stroke="#38bdf8" stroke-width="1"/>
    <text x="120" y="253" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="10.5" font-weight="700" text-anchor="middle">Walking, Leaping &amp; Praising</text>
    <text x="120" y="268" fill="#94a3b8" font-family="system-ui, sans-serif" font-size="9" text-anchor="middle">Encountering Living God</text>
  </g>

  <!-- Right: Deflection of Glory -->
  <g transform="translate(545, 95)">
    <rect width="215" height="295" rx="10" fill="#1e293b" stroke="#34d399" stroke-width="1.5"/>
    <rect width="215" height="34" rx="10" fill="#059669"/>
    <text x="107" y="22" fill="#ffffff" font-family="system-ui, sans-serif" font-size="11.5" font-weight="700" text-anchor="middle">3. HUMILITY &amp; FAITH</text>
    <text x="15" y="60" fill="#6ee7b7" font-family="system-ui, sans-serif" font-size="11" font-weight="700">• No Human Pride</text>
    <text x="15" y="78" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10">"Why stare at us as though</text>
    <text x="15" y="93" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10">by our power we did this?"</text>
    <text x="15" y="123" fill="#6ee7b7" font-family="system-ui, sans-serif" font-size="11" font-weight="700">• Glory to Christ</text>
    <text x="15" y="141" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10">Faith in the resurrected</text>
    <text x="15" y="156" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10">Jesus gave complete wholeness.</text>
    <rect x="15" y="235" width="185" height="42" rx="6" fill="#0f172a" stroke="#34d399" stroke-width="1"/>
    <text x="107" y="253" fill="#34d399" font-family="system-ui, sans-serif" font-size="10.5" font-weight="700" text-anchor="middle">Apostolic Integrity</text>
    <text x="107" y="268" fill="#94a3b8" font-family="system-ui, sans-serif" font-size="9" text-anchor="middle">Redirecting all worship to God</text>
  </g>

  <text x="400" y="422" fill="#64748b" font-family="system-ui, sans-serif" font-size="10" text-anchor="middle">CORE LESSON: TRUE SPIRITUAL POWER GLORIFIES JESUS CHRIST AND RESTORES HUMAN DIGNITY</text>
</svg>"""


def get_svg_lesson_4():
    return """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 450" width="100%" height="100%">
  <defs>
    <linearGradient id="bg4" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#0f172a"/>
      <stop offset="50%" stop-color="#1e293b"/>
      <stop offset="100%" stop-color="#0f172a"/>
    </linearGradient>
    <linearGradient id="explGrad4" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#dc2626"/>
      <stop offset="100%" stop-color="#991b1b"/>
    </linearGradient>
  </defs>
  <rect width="800" height="450" fill="url(#bg4)" rx="14"/>
  <rect x="15" y="15" width="770" height="420" fill="none" stroke="#334155" stroke-width="1.5" stroke-dasharray="6 4" rx="10"/>

  <text x="400" y="45" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="17" font-weight="700" text-anchor="middle">PAUL &amp; SILAS IN PHILIPPI: SPIRITUAL DELIVERANCE VS EXPLOITATION</text>
  <text x="400" y="68" fill="#94a3b8" font-family="system-ui, sans-serif" font-size="12" text-anchor="middle">Analyzing Acts 16:16-24: Demonic Bondage, Economic Greed, False Charges, and Unjust Imprisonment</text>

  <!-- Flowchart Stages -->
  <!-- Stage 1: Bondage & Greed -->
  <g transform="translate(30, 95)">
    <rect width="165" height="295" rx="8" fill="#1e293b" stroke="#ef4444" stroke-width="1.5"/>
    <rect width="165" height="34" rx="8" fill="url(#explGrad4)"/>
    <text x="82" y="22" fill="#ffffff" font-family="system-ui, sans-serif" font-size="10.5" font-weight="700" text-anchor="middle">1. EXPLOITATION</text>
    <text x="10" y="60" fill="#fca5a5" font-family="system-ui, sans-serif" font-size="10" font-weight="700">• Demonic Spirit</text>
    <text x="10" y="78" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="9">Slave girl possessed by</text>
    <text x="10" y="93" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="9">spirit of divination.</text>
    <text x="10" y="120" fill="#fca5a5" font-family="system-ui, sans-serif" font-size="10" font-weight="700">• Greedy Masters</text>
    <text x="10" y="138" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="9">Used fortune-telling</text>
    <text x="10" y="153" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="9">to make huge profits.</text>
    <rect x="10" y="235" width="145" height="38" rx="5" fill="#0f172a" stroke="#ef4444" stroke-width="1"/>
    <text x="82" y="258" fill="#fca5a5" font-family="system-ui, sans-serif" font-size="8.5" font-weight="700" text-anchor="middle">Human Bondage</text>
  </g>

  <!-- Stage 2: Deliverance -->
  <g transform="translate(225, 95)">
    <rect width="165" height="295" rx="8" fill="#1e293b" stroke="#38bdf8" stroke-width="1.5"/>
    <rect width="165" height="34" rx="8" fill="#0284c7"/>
    <text x="82" y="22" fill="#ffffff" font-family="system-ui, sans-serif" font-size="10.5" font-weight="700" text-anchor="middle">2. DELIVERANCE</text>
    <text x="10" y="60" fill="#7dd3fc" font-family="system-ui, sans-serif" font-size="10" font-weight="700">• Discernment</text>
    <text x="10" y="78" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="9">Paul refused demonic</text>
    <text x="10" y="93" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="9">association / mockery.</text>
    <text x="10" y="120" fill="#7dd3fc" font-family="system-ui, sans-serif" font-size="10" font-weight="700">• Authority in Jesus</text>
    <text x="10" y="138" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="9">Commanded demon to</text>
    <text x="10" y="153" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="9">leave her instantly.</text>
    <rect x="10" y="235" width="145" height="38" rx="5" fill="#0f172a" stroke="#38bdf8" stroke-width="1"/>
    <text x="82" y="258" fill="#7dd3fc" font-family="system-ui, sans-serif" font-size="8.5" font-weight="700" text-anchor="middle">Freedom Restored</text>
  </g>

  <!-- Stage 3: Backlash & Lies -->
  <g transform="translate(420, 95)">
    <rect width="165" height="295" rx="8" fill="#1e293b" stroke="#f59e0b" stroke-width="1.5"/>
    <rect width="165" height="34" rx="8" fill="#d97706"/>
    <text x="82" y="22" fill="#ffffff" font-family="system-ui, sans-serif" font-size="10.5" font-weight="700" text-anchor="middle">3. GREEDY RETALIATION</text>
    <text x="10" y="60" fill="#fde68a" font-family="system-ui, sans-serif" font-size="10" font-weight="700">• Lost Revenue</text>
    <text x="10" y="78" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="9">Owners furious because</text>
    <text x="10" y="93" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="9">profit stream died.</text>
    <text x="10" y="120" fill="#fde68a" font-family="system-ui, sans-serif" font-size="10" font-weight="700">• Fabricated Charges</text>
    <text x="10" y="138" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="9">Accused Jews of civil</text>
    <text x="10" y="153" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="9">unrest &amp; illegal customs.</text>
    <rect x="10" y="235" width="145" height="38" rx="5" fill="#0f172a" stroke="#f59e0b" stroke-width="1"/>
    <text x="82" y="258" fill="#fde68a" font-family="system-ui, sans-serif" font-size="8.5" font-weight="700" text-anchor="middle">False Accusation</text>
  </g>

  <!-- Stage 4: Unjust Prison -->
  <g transform="translate(615, 95)">
    <rect width="155" height="295" rx="8" fill="#1e293b" stroke="#8b5cf6" stroke-width="1.5"/>
    <rect width="155" height="34" rx="8" fill="#7c3aed"/>
    <text x="77" y="22" fill="#ffffff" font-family="system-ui, sans-serif" font-size="10.5" font-weight="700" text-anchor="middle">4. INNER PRISON</text>
    <text x="10" y="60" fill="#c084fc" font-family="system-ui, sans-serif" font-size="10" font-weight="700">• Severe Flogging</text>
    <text x="10" y="78" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="9">Beaten with rods</text>
    <text x="10" y="93" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="9">without fair trial.</text>
    <text x="10" y="120" fill="#c084fc" font-family="system-ui, sans-serif" font-size="10" font-weight="700">• Wooden Stocks</text>
    <text x="10" y="138" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="9">Locked in deepest</text>
    <text x="10" y="153" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="9">darkest dungeon.</text>
    <rect x="10" y="235" width="135" height="38" rx="5" fill="#0f172a" stroke="#8b5cf6" stroke-width="1"/>
    <text x="77" y="258" fill="#d8b4fe" font-family="system-ui, sans-serif" font-size="8.5" font-weight="700" text-anchor="middle">Unjust Suffering</text>
  </g>

  <text x="400" y="422" fill="#64748b" font-family="system-ui, sans-serif" font-size="10" text-anchor="middle">INTEGRITY LESSON: STANDING UP FOR THE MARGINALIZED OFTEN PROVOKES RETALIATION FROM EXPLOITERS</text>
</svg>"""


def get_svg_lesson_5():
    return """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 450" width="100%" height="100%">
  <defs>
    <linearGradient id="bg5" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#0f172a"/>
      <stop offset="50%" stop-color="#1e293b"/>
      <stop offset="100%" stop-color="#0f172a"/>
    </linearGradient>
    <linearGradient id="praiseGrad5" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#f59e0b"/>
      <stop offset="100%" stop-color="#ec4899"/>
    </linearGradient>
    <linearGradient id="quakeGrad5" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#0284c7"/>
      <stop offset="100%" stop-color="#38bdf8"/>
    </linearGradient>
  </defs>
  <rect width="800" height="450" fill="url(#bg5)" rx="14"/>
  <rect x="15" y="15" width="770" height="420" fill="none" stroke="#334155" stroke-width="1.5" stroke-dasharray="6 4" rx="10"/>

  <text x="400" y="45" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="17" font-weight="700" text-anchor="middle">PRAISE IN THE PRISON: MIDNIGHT BREAKTHROUGH (ACTS 16:25-28)</text>
  <text x="400" y="68" fill="#94a3b8" font-family="system-ui, sans-serif" font-size="12" text-anchor="middle">Suffering Transformed: Authentic Worship, Divine Intervention, and Shattered Chains</text>

  <!-- Left: Midnight Suffering -->
  <g transform="translate(40, 95)">
    <rect width="220" height="295" rx="10" fill="#1e293b" stroke="#ef4444" stroke-width="1.5"/>
    <rect width="220" height="34" rx="10" fill="#dc2626"/>
    <text x="110" y="22" fill="#ffffff" font-family="system-ui, sans-serif" font-size="11.5" font-weight="700" text-anchor="middle">1. CRUEL CIRCUMSTANCES</text>
    <text x="15" y="60" fill="#fca5a5" font-family="system-ui, sans-serif" font-size="11" font-weight="700">• Bleeding Open Wounds</text>
    <text x="15" y="78" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10">Severe rod beating left</text>
    <text x="15" y="93" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10">deep untreated lacerations.</text>
    <text x="15" y="123" fill="#fca5a5" font-family="system-ui, sans-serif" font-size="11" font-weight="700">• Feet Locked in Stocks</text>
    <text x="15" y="141" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10">Cramped agonizing position</text>
    <text x="15" y="156" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10">in pitch dark inner cell.</text>
    <rect x="15" y="235" width="190" height="42" rx="6" fill="#0f172a" stroke="#ef4444" stroke-width="1"/>
    <text x="110" y="253" fill="#fca5a5" font-family="system-ui, sans-serif" font-size="10" font-weight="700" text-anchor="middle">Physical Torment</text>
    <text x="110" y="268" fill="#94a3b8" font-family="system-ui, sans-serif" font-size="9" text-anchor="middle">Refusal to despair or curse</text>
  </g>

  <!-- Center: Midnight Worship -->
  <g transform="translate(285, 95)">
    <rect width="230" height="295" rx="10" fill="#1e293b" stroke="#f59e0b" stroke-width="1.5"/>
    <rect width="230" height="34" rx="10" fill="url(#praiseGrad5)"/>
    <text x="115" y="22" fill="#ffffff" font-family="system-ui, sans-serif" font-size="11.5" font-weight="700" text-anchor="middle">2. MIDNIGHT PRAISE</text>
    <text x="15" y="60" fill="#fde68a" font-family="system-ui, sans-serif" font-size="11" font-weight="700">• Praying &amp; Singing Hymns</text>
    <text x="15" y="78" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10">Chose joyful worship</text>
    <text x="15" y="93" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10">over self-pity or revenge.</text>
    <text x="15" y="123" fill="#fde68a" font-family="system-ui, sans-serif" font-size="11" font-weight="700">• Prisoners Listening</text>
    <text x="15" y="141" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10">Radiant faith served as</text>
    <text x="15" y="156" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10">powerful audible witness.</text>
    <rect x="15" y="235" width="200" height="42" rx="6" fill="#0f172a" stroke="#f59e0b" stroke-width="1"/>
    <text x="115" y="253" fill="#fbbf24" font-family="system-ui, sans-serif" font-size="10" font-weight="700" text-anchor="middle">Spiritual Sovereignty</text>
    <text x="115" y="268" fill="#94a3b8" font-family="system-ui, sans-serif" font-size="9" text-anchor="middle">Worship rooted in eternal joy</text>
  </g>

  <!-- Right: Supernatural Earthquake -->
  <g transform="translate(540, 95)">
    <rect width="220" height="295" rx="10" fill="#1e293b" stroke="#38bdf8" stroke-width="1.5"/>
    <rect width="220" height="34" rx="10" fill="url(#quakeGrad5)"/>
    <text x="110" y="22" fill="#ffffff" font-family="system-ui, sans-serif" font-size="11.5" font-weight="700" text-anchor="middle">3. CHAINS SHATTERED</text>
    <text x="15" y="60" fill="#7dd3fc" font-family="system-ui, sans-serif" font-size="11" font-weight="700">• Great Earthquake</text>
    <text x="15" y="78" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10">Prison foundations shook;</text>
    <text x="15" y="93" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10">all locked doors flew open.</text>
    <text x="15" y="123" fill="#7dd3fc" font-family="system-ui, sans-serif" font-size="11" font-weight="700">• All Chains Loosed</text>
    <text x="15" y="141" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10">Supernatural release for</text>
    <text x="15" y="156" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10">every prisoner present.</text>
    <rect x="15" y="235" width="190" height="42" rx="6" fill="#0f172a" stroke="#38bdf8" stroke-width="1"/>
    <text x="110" y="253" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="10.5" font-weight="700" text-anchor="middle">Supernatural Deliverance</text>
    <text x="110" y="268" fill="#94a3b8" font-family="system-ui, sans-serif" font-size="9" text-anchor="middle">God answers faith in darkness</text>
  </g>

  <text x="400" y="422" fill="#64748b" font-family="system-ui, sans-serif" font-size="10" text-anchor="middle">THEOLOGICAL TRUTH: AUTHENTIC PRAISE IN SUFFERING RELEASES DIVINE POWER AND UNLOCKS PRISONS</text>
</svg>"""


def get_svg_lesson_6():
    return """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 450" width="100%" height="100%">
  <defs>
    <linearGradient id="bg6" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#0f172a"/>
      <stop offset="50%" stop-color="#1e293b"/>
      <stop offset="100%" stop-color="#0f172a"/>
    </linearGradient>
    <linearGradient id="salvGrad6" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#059669"/>
      <stop offset="100%" stop-color="#10b981"/>
    </linearGradient>
  </defs>
  <rect width="800" height="450" fill="url(#bg6)" rx="14"/>
  <rect x="15" y="15" width="770" height="420" fill="none" stroke="#334155" stroke-width="1.5" stroke-dasharray="6 4" rx="10"/>

  <text x="400" y="45" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="17" font-weight="700" text-anchor="middle">THE PHILIPPIAN JAILER: FROM DESPAIR TO HOUSEHOLD SALVATION</text>
  <text x="400" y="68" fill="#94a3b8" font-family="system-ui, sans-serif" font-size="12" text-anchor="middle">Acts 16:27-34: Mercy Restraining Suicide, The Great Question, and Immediate Practical Fruit</text>

  <!-- 3 Stages -->
  <!-- Stage 1: Despair & Mercy -->
  <g transform="translate(40, 95)">
    <rect width="220" height="295" rx="10" fill="#1e293b" stroke="#ef4444" stroke-width="1.5"/>
    <rect width="220" height="34" rx="10" fill="#dc2626"/>
    <text x="110" y="22" fill="#ffffff" font-family="system-ui, sans-serif" font-size="11.5" font-weight="700" text-anchor="middle">1. DESPAIR &amp; MERCY</text>
    <text x="15" y="60" fill="#fca5a5" font-family="system-ui, sans-serif" font-size="11" font-weight="700">• Facing Roman Penalty</text>
    <text x="15" y="78" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10">Execution awaited jailers</text>
    <text x="15" y="93" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10">who let prisoners flee.</text>
    <text x="15" y="123" fill="#fca5a5" font-family="system-ui, sans-serif" font-size="11" font-weight="700">• "Do Not Harm Yourself!"</text>
    <text x="15" y="141" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10">Paul stayed to save his life</text>
    <text x="15" y="156" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10">rather than escape.</text>
    <rect x="15" y="235" width="190" height="42" rx="6" fill="#0f172a" stroke="#ef4444" stroke-width="1"/>
    <text x="110" y="253" fill="#fca5a5" font-family="system-ui, sans-serif" font-size="10" font-weight="700" text-anchor="middle">Suicide Averted</text>
    <text x="110" y="268" fill="#94a3b8" font-family="system-ui, sans-serif" font-size="9" text-anchor="middle">Christian love protects enemy</text>
  </g>

  <!-- Stage 2: The Way of Salvation -->
  <g transform="translate(285, 95)">
    <rect width="230" height="295" rx="10" fill="#1e293b" stroke="#38bdf8" stroke-width="1.5"/>
    <rect width="230" height="34" rx="10" fill="#0284c7"/>
    <text x="115" y="22" fill="#ffffff" font-family="system-ui, sans-serif" font-size="11.5" font-weight="700" text-anchor="middle">2. "WHAT MUST I DO?"</text>
    <text x="15" y="60" fill="#7dd3fc" font-family="system-ui, sans-serif" font-size="11" font-weight="700">• The Great Question</text>
    <text x="15" y="78" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10">Kneeling in trembling awe</text>
    <text x="15" y="93" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10">before the servants of God.</text>
    <text x="15" y="123" fill="#7dd3fc" font-family="system-ui, sans-serif" font-size="11" font-weight="700">• "Believe in the Lord Jesus"</text>
    <text x="15" y="141" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10">Simple, direct promise of</text>
    <text x="15" y="156" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10">salvation for his household.</text>
    <rect x="15" y="235" width="200" height="42" rx="6" fill="#0f172a" stroke="#38bdf8" stroke-width="1"/>
    <text x="115" y="253" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="10" font-weight="700" text-anchor="middle">Gospel Invitation</text>
    <text x="115" y="268" fill="#94a3b8" font-family="system-ui, sans-serif" font-size="9" text-anchor="middle">Faith in Christ alone saves</text>
  </g>

  <!-- Stage 3: Immediate Transformation -->
  <g transform="translate(540, 95)">
    <rect width="220" height="295" rx="10" fill="#1e293b" stroke="#34d399" stroke-width="1.5"/>
    <rect width="220" height="34" rx="10" fill="url(#salvGrad6)"/>
    <text x="110" y="22" fill="#ffffff" font-family="system-ui, sans-serif" font-size="11.5" font-weight="700" text-anchor="middle">3. PRACTICAL FRUIT</text>
    <text x="15" y="60" fill="#6ee7b7" font-family="system-ui, sans-serif" font-size="11" font-weight="700">• Washed Their Wounds</text>
    <text x="15" y="78" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10">Tender medical compassion</text>
    <text x="15" y="93" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10">replacing cruelty.</text>
    <text x="15" y="123" fill="#6ee7b7" font-family="system-ui, sans-serif" font-size="11" font-weight="700">• Baptism &amp; Great Joy</text>
    <text x="15" y="141" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10">Entire family baptized;</text>
    <text x="15" y="156" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10">shared midnight meal.</text>
    <rect x="15" y="235" width="190" height="42" rx="6" fill="#0f172a" stroke="#34d399" stroke-width="1"/>
    <text x="110" y="253" fill="#34d399" font-family="system-ui, sans-serif" font-size="10.5" font-weight="700" text-anchor="middle">Household Transformed</text>
    <text x="110" y="268" fill="#94a3b8" font-family="system-ui, sans-serif" font-size="9" text-anchor="middle">Faith demonstrated in deeds</text>
  </g>

  <text x="400" y="422" fill="#64748b" font-family="system-ui, sans-serif" font-size="10" text-anchor="middle">CONVERSION PRINCIPLE: GENUINE FAITH IMMEDIATELY PRODUCES MERCY, HOSPITALITY, AND PROFOUND JOY</text>
</svg>"""


def get_svg_lesson_7():
    return """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 450" width="100%" height="100%">
  <defs>
    <linearGradient id="bg7" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#0f172a"/>
      <stop offset="50%" stop-color="#1e293b"/>
      <stop offset="100%" stop-color="#0f172a"/>
    </linearGradient>
    <linearGradient id="bridgeGrad7" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#0284c7"/>
      <stop offset="100%" stop-color="#10b981"/>
    </linearGradient>
  </defs>
  <rect width="800" height="450" fill="url(#bg7)" rx="14"/>
  <rect x="15" y="15" width="770" height="420" fill="none" stroke="#334155" stroke-width="1.5" stroke-dasharray="6 4" rx="10"/>

  <text x="400" y="45" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="17" font-weight="700" text-anchor="middle">THE CONTINUITY BRIDGE: EARLY CHURCH (A.D. 33) TO MODERN CHURCH TODAY</text>
  <text x="400" y="68" fill="#94a3b8" font-family="system-ui, sans-serif" font-size="12" text-anchor="middle">Preserving Apostolic DNA Across Two Millennia of Christian Fellowship &amp; Ministry</text>

  <!-- Left Box: Early Church (Acts 2 & 4) -->
  <g transform="translate(40, 95)">
    <rect width="320" height="295" rx="10" fill="#1e293b" stroke="#f59e0b" stroke-width="1.5"/>
    <rect width="320" height="34" rx="10" fill="#d97706"/>
    <text x="160" y="22" fill="#ffffff" font-family="system-ui, sans-serif" font-size="12" font-weight="700" text-anchor="middle">EARLY CHURCH PATTERN (A.D. 33)</text>

    <text x="15" y="65" fill="#fde68a" font-family="system-ui, sans-serif" font-size="11" font-weight="700">1. Apostles' Doctrine:</text>
    <text x="15" y="82" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10">Devoted daily to teaching of Christ.</text>

    <text x="15" y="112" fill="#fde68a" font-family="system-ui, sans-serif" font-size="11" font-weight="700">2. Organic Koinonia:</text>
    <text x="15" y="129" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10">Shared life, homes, and personal wealth.</text>

    <text x="15" y="159" fill="#fde68a" font-family="system-ui, sans-serif" font-size="11" font-weight="700">3. Breaking of Bread:</text>
    <text x="15" y="176" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10">Agape love feasts &amp; Lord's Supper.</text>

    <text x="15" y="206" fill="#fde68a" font-family="system-ui, sans-serif" font-size="11" font-weight="700">4. Radical Charity:</text>
    <text x="15" y="223" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10">No needy person in the entire assembly.</text>

    <rect x="15" y="245" width="290" height="32" rx="6" fill="#0f172a" stroke="#f59e0b" stroke-width="1"/>
    <text x="160" y="266" fill="#fbbf24" font-family="system-ui, sans-serif" font-size="10" font-weight="700" text-anchor="middle">Apostolic Foundation</text>
  </g>

  <!-- Center Bridge Arrows -->
  <g transform="translate(372, 215)">
    <path d="M 0 15 L 40 15 L 40 5 L 55 20 L 40 35 L 40 25 L 0 25 Z" fill="#38bdf8"/>
    <text x="27" y="52" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="9" font-weight="700" text-anchor="middle">DNA</text>
  </g>

  <!-- Right Box: Modern Church Expression -->
  <g transform="translate(440, 95)">
    <rect width="320" height="295" rx="10" fill="#1e293b" stroke="#34d399" stroke-width="1.5"/>
    <rect width="320" height="34" rx="10" fill="#059669"/>
    <text x="160" y="22" fill="#ffffff" font-family="system-ui, sans-serif" font-size="12" font-weight="700" text-anchor="middle">MODERN CHURCH EXPRESSION (TODAY)</text>

    <text x="15" y="65" fill="#6ee7b7" font-family="system-ui, sans-serif" font-size="11" font-weight="700">1. Sunday Sermons &amp; Bible Study:</text>
    <text x="15" y="82" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10">Exposition of Scripture in local parishes.</text>

    <text x="15" y="112" fill="#6ee7b7" font-family="system-ui, sans-serif" font-size="11" font-weight="700">2. Small Groups &amp; Youth Fellowships:</text>
    <text x="15" y="129" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10">Cell groups, youth rallies, prayer cells.</text>

    <text x="15" y="159" fill="#6ee7b7" font-family="system-ui, sans-serif" font-size="11" font-weight="700">3. Holy Communion (Eucharist):</text>
    <text x="15" y="176" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10">Sacramental remembrance of the Cross.</text>

    <text x="15" y="206" fill="#6ee7b7" font-family="system-ui, sans-serif" font-size="11" font-weight="700">4. Community Outreach &amp; Welfare:</text>
    <text x="15" y="223" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10">Food drives, medical camps, children's homes.</text>

    <rect x="15" y="245" width="290" height="32" rx="6" fill="#0f172a" stroke="#34d399" stroke-width="1"/>
    <text x="160" y="266" fill="#34d399" font-family="system-ui, sans-serif" font-size="10" font-weight="700" text-anchor="middle">Contemporary Execution</text>
  </g>

  <text x="400" y="422" fill="#64748b" font-family="system-ui, sans-serif" font-size="10" text-anchor="middle">CHALLENGE TODAY: OVERCOMING INDIVIDUALISM TO EMBODY RADICAL APOSTOLIC GENEROSITY</text>
</svg>"""


def get_svg_lesson_8():
    return """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 450" width="100%" height="100%">
  <defs>
    <linearGradient id="bg8" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#0f172a"/>
      <stop offset="50%" stop-color="#1e293b"/>
      <stop offset="100%" stop-color="#0f172a"/>
    </linearGradient>
    <linearGradient id="stepGrad8" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#0284c7"/>
      <stop offset="100%" stop-color="#8b5cf6"/>
    </linearGradient>
  </defs>
  <rect width="800" height="450" fill="url(#bg8)" rx="14"/>
  <rect x="15" y="15" width="770" height="420" fill="none" stroke="#334155" stroke-width="1.5" stroke-dasharray="6 4" rx="10"/>

  <text x="400" y="45" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="17" font-weight="700" text-anchor="middle">THE 4 STEPS OF THE CALL TO SALVATION (ROMANS 10:8-13)</text>
  <text x="400" y="68" fill="#94a3b8" font-family="system-ui, sans-serif" font-size="12" text-anchor="middle">God's Grace, Heart Faith, Bold Confession, and Transformation as a New Creation</text>

  <!-- Step 1: Acknowledge Need -->
  <g transform="translate(30, 95)">
    <rect width="165" height="295" rx="8" fill="#1e293b" stroke="#ef4444" stroke-width="1.5"/>
    <rect width="165" height="34" rx="8" fill="#dc2626"/>
    <text x="82" y="22" fill="#ffffff" font-family="system-ui, sans-serif" font-size="10.5" font-weight="700" text-anchor="middle">1. ACKNOWLEDGE</text>
    <text x="10" y="60" fill="#fca5a5" font-family="system-ui, sans-serif" font-size="10" font-weight="700">• Human Limitation</text>
    <text x="10" y="78" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="9">All have sinned and</text>
    <text x="10" y="93" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="9">fall short of glory.</text>
    <text x="10" y="120" fill="#fca5a5" font-family="system-ui, sans-serif" font-size="10" font-weight="700">• Need for Savior</text>
    <text x="10" y="138" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="9">Good works cannot</text>
    <text x="10" y="153" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="9">erase sin debt.</text>
    <rect x="10" y="235" width="145" height="38" rx="5" fill="#0f172a" stroke="#ef4444" stroke-width="1"/>
    <text x="82" y="258" fill="#fca5a5" font-family="system-ui, sans-serif" font-size="8.5" font-weight="700" text-anchor="middle">Humility &amp; Repentance</text>
  </g>

  <!-- Step 2: Believe in Heart -->
  <g transform="translate(225, 95)">
    <rect width="165" height="295" rx="8" fill="#1e293b" stroke="#f59e0b" stroke-width="1.5"/>
    <rect width="165" height="34" rx="8" fill="#d97706"/>
    <text x="82" y="22" fill="#ffffff" font-family="system-ui, sans-serif" font-size="10.5" font-weight="700" text-anchor="middle">2. BELIEVE</text>
    <text x="10" y="60" fill="#fde68a" font-family="system-ui, sans-serif" font-size="10" font-weight="700">• Faith in Jesus</text>
    <text x="10" y="78" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="9">Trusting Christ's</text>
    <text x="10" y="93" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="9">death on the Cross.</text>
    <text x="10" y="120" fill="#fde68a" font-family="system-ui, sans-serif" font-size="10" font-weight="700">• Resurrection</text>
    <text x="10" y="138" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="9">Believing God raised</text>
    <text x="10" y="153" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="9">Him from the dead.</text>
    <rect x="10" y="235" width="145" height="38" rx="5" fill="#0f172a" stroke="#f59e0b" stroke-width="1"/>
    <text x="82" y="258" fill="#fde68a" font-family="system-ui, sans-serif" font-size="8.5" font-weight="700" text-anchor="middle">Inward Justification</text>
  </g>

  <!-- Step 3: Confess with Mouth -->
  <g transform="translate(420, 95)">
    <rect width="165" height="295" rx="8" fill="#1e293b" stroke="#38bdf8" stroke-width="1.5"/>
    <rect width="165" height="34" rx="8" fill="#0284c7"/>
    <text x="82" y="22" fill="#ffffff" font-family="system-ui, sans-serif" font-size="10.5" font-weight="700" text-anchor="middle">3. CONFESS</text>
    <text x="10" y="60" fill="#7dd3fc" font-family="system-ui, sans-serif" font-size="10" font-weight="700">• "Jesus is Lord"</text>
    <text x="10" y="78" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="9">Verbal allegiance</text>
    <text x="10" y="93" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="9">before humanity.</text>
    <text x="10" y="120" fill="#7dd3fc" font-family="system-ui, sans-serif" font-size="10" font-weight="700">• Bold Witness</text>
    <text x="10" y="138" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="9">Living without fear</text>
    <text x="10" y="153" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="9">or shame of Gospel.</text>
    <rect x="10" y="235" width="145" height="38" rx="5" fill="#0f172a" stroke="#38bdf8" stroke-width="1"/>
    <text x="82" y="258" fill="#7dd3fc" font-family="system-ui, sans-serif" font-size="8.5" font-weight="700" text-anchor="middle">Outward Allegiance</text>
  </g>

  <!-- Step 4: Walk in Newness -->
  <g transform="translate(615, 95)">
    <rect width="155" height="295" rx="8" fill="#1e293b" stroke="#34d399" stroke-width="1.5"/>
    <rect width="155" height="34" rx="8" fill="#059669"/>
    <text x="77" y="22" fill="#ffffff" font-family="system-ui, sans-serif" font-size="10.5" font-weight="700" text-anchor="middle">4. NEW CREATION</text>
    <text x="10" y="60" fill="#6ee7b7" font-family="system-ui, sans-serif" font-size="10" font-weight="700">• 2 Cor 5:17</text>
    <text x="10" y="78" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="9">Old has gone, new</text>
    <text x="10" y="93" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="9">life has begun.</text>
    <text x="10" y="120" fill="#6ee7b7" font-family="system-ui, sans-serif" font-size="10" font-weight="700">• Ambassador</text>
    <text x="10" y="138" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="9">Representing Christ</text>
    <text x="10" y="153" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="9">in daily lifestyle.</text>
    <rect x="10" y="235" width="135" height="38" rx="5" fill="#0f172a" stroke="#34d399" stroke-width="1"/>
    <text x="77" y="258" fill="#a7f3d0" font-family="system-ui, sans-serif" font-size="8.5" font-weight="700" text-anchor="middle">Transformed Life</text>
  </g>

  <text x="400" y="422" fill="#64748b" font-family="system-ui, sans-serif" font-size="10" text-anchor="middle">PROMISE: EVERYONE WHO CALLS ON THE NAME OF THE LORD WILL BE SAVED (ROMANS 10:13)</text>
</svg>"""


# ─── 8 LESSON CONFIGURATION DEFINITIONS ────────────────────────────────────────

LESSONS_DATA = [
    # ─── LESSON 1 ─────────────────────────────────────────────────────────────
    {
        "order": 1,
        "title": "The Day of Pentecost: Birth of the Church",
        "description": "Examine the outpouring of the Holy Spirit on Pentecost, analyze Peter's bold sermon, and explain the significance of the event for the universal spread of the Gospel.",
        "goals": [
            "Recount the chronological events and supernatural signs of the Day of Pentecost (Acts 2:1-13).",
            "Analyze Peter's sermon and explain how speaking in diverse human languages demonstrated the universality of the Gospel.",
            "Apply the boldness of the Holy Spirit to stand up for truth and overcome peer pressure in daily life."
        ],
        "image": {
            "title": "Pentecost: Outpouring of the Holy Spirit",
            "caption": "Historical depiction of the descent of the Holy Spirit upon the Apostles on Pentecost with tongues of fire.",
            "url": "https://upload.wikimedia.org/wikipedia/commons/thumb/6/6b/Pentecost_-_Jean_Restout_II.jpg/800px-Pentecost_-_Jean_Restout_II.jpg",
            "author": "Jean Restout II (1732)",
            "licensing": "Public Domain",
            "source": "Wikimedia Commons"
        },
        "intro": """Have you ever struggled to communicate with someone because you spoke completely different languages? Language barriers can divide communities and create misunderstandings. 

On the Day of Pentecost, God performed a spectacular miracle of language to do the exact opposite—uniting thousands of pilgrims from diverse nations, tribes, and tongues under one single message of redemption and hope. This miraculous event marked the official birthday of the global Christian Church.""",
        "core_scripture": """### Acts 2:1-4 (NIV)
> "When the day of Pentecost came, they were all together in one place. Suddenly a sound like the blowing of a violent wind came from heaven and filled the whole house where they were sitting. They saw what seemed to be tongues of fire that separated and came to rest on each of them. All of them were filled with the Holy Spirit and began to speak in other tongues as the Spirit enabled them."

### Joel 2:28-29 (NIV)
> "And afterward, I will pour out my Spirit on all people. Your sons and daughters will prophesy, your old men will dream dreams, your young men will see visions. Even on my servants, both men and women, I will pour out my Spirit in those days."

### Acts 2:38 (NIV)
> "Peter replied, 'Repent and be baptized, every one of you, in the name of Jesus Christ for the forgiveness of your sins. And you will receive the gift of the Holy Spirit.'" """,
        "theological_pillars": """### Exegetical Pillars of Pentecost

1. **The Jewish Feast of Pentecost (*Shavuot*):**
   Pentecost (from the Greek word for 'fiftieth') was a major Jewish harvest festival celebrated 50 days after Passover, commemorating the giving of the Law on Mount Sinai. Devout Jews from every nation under heaven were gathered in Jerusalem, creating the ideal international audience for the launch of the global Church.

2. **The Three Supernatural Phenomena:**
   - **Audible Wind:** The sound like a violent rushing wind symbolized the divine breath (*Pneuma* / *Ruach*) of God, breathing supernatural life into the newly formed Body of Christ.
   - **Visible Fire:** Tongues of fire resting on each individual symbolized spiritual cleansing, divine presence, and the empowerment of every believer, not just a high priest.
   - **Linguistic Miracle (Glossolalia / Xenolalia):** Disciples spoke in real, existing human foreign dialects (from Parthia, Media, Elam, Mesopotamia, Egypt, Rome, and Crete).

3. **Peter's Bold Apologetic Sermon:**
   Peter, who had cowardly denied Jesus weeks prior, stood boldly and explained:
   - This was the fulfillment of the Prophet Joel's prophecy (Joel 2:28-32).
   - Jesus of Nazareth was accredited by God through miracles, crucified by lawless hands, and resurrected according to divine sovereignty.
   - He called the crowd to repentance and baptism, resulting in 3,000 souls being added in a single day.""",
        "svg_fn": get_svg_lesson_1,
        "deep_dive": """### Theological Deep Dive: The Reversal of Babel

In Genesis 11, humanity attempted to build the Tower of Babel out of pride to make a name for themselves. God scattered them by confusing their languages, creating division and cultural fragmentation.

At Pentecost (Acts 2), God reversed the curse of Babel. Rather than eliminating human cultural diversity, the Holy Spirit consecrated all human languages by communicating the wonders of God in every native tongue. This demonstrates:
- **Universal Inclusion:** No single human language or culture is superior in God's eyes.
- **The Global Commission:** The Gospel is designed to cross every ethnic, tribal, and national boundary.
- **Transformational Boldness:** The Holy Spirit transforms timid, hiding disciples into fearless ambassadors of divine truth.""",
        "practical": {
            "title": "4-Step Framework for Living with Holy Spirit Boldness",
            "steps": [
                {
                    "step_number": 1,
                    "name": "Acknowledge Your Fears",
                    "description": "Identify situations at school or in your peer group where peer pressure causes you to stay silent about truth or justice."
                },
                {
                    "step_number": 2,
                    "name": "Pray for Spiritual Courage",
                    "description": "Ask the Holy Spirit daily for wisdom, discernment, and moral courage before facing challenging social situations."
                },
                {
                    "step_number": 3,
                    "name": "Speak Truth with Grace",
                    "description": "Speak up respectfully when others spread gossip, bully classmates, or cheat, using words that heal and protect."
                },
                {
                    "step_number": 4,
                    "name": "Embrace Cultural and Tribal Diversity",
                    "description": "Actively build friendships with peers from different tribal, ethnic, and socio-economic backgrounds, reflecting Pentecost's unity."
                }
            ]
        },
        "kenyan_context": """### Kenyan Real-World Context & Church Fellowship

In Kenya, national unity across our 40+ diverse ethnic communities is essential for peace and development. Pentecost reminds Kenyan youth that tribalism and ethnic prejudice have no place in the Body of Christ. 

During national holidays, inter-denominational youth conferences, and school Christian Union (C.U.) rallies, students from every county worship together, mirroring the diverse gathering in Jerusalem on Pentecost. Living out Pentecost means rejecting tribal stereotypes and championing national brotherhood in our schools and neighborhoods.""",
        "youtube": {
            "title": "BibleProject: Acts 1-12 (The Holy Spirit & The Early Church)",
            "youtube_id": "CGbNw855Bsw",
            "description": "Watch how the Holy Spirit empowers the early disciples to spread the Good News from Jerusalem to Judea and Samaria."
        },
        "reflection": """### Spiritual Reflection & Core Values

- **Boldness:** Peter did not let his past denial of Jesus define his future. When empowered by the Holy Spirit, he stepped forward courageously. Are you letting past failures stop you from serving God?
- **Inclusivity:** God spoke to pilgrims in their own mother tongues. How can you ensure that newcomers or quiet students in your school feel welcomed and valued?""",
        "takeaways": [
            "Pentecost occurred 50 days after Passover and marked the birth of the Christian Church.",
            "The Holy Spirit descended with three signs: rushing wind, tongues of fire, and speaking in diverse human languages.",
            "Peter boldly preached Christ's resurrection and called for repentance, leading to 3,000 new believers being baptized in one day.",
            "Pentecost reversed the division of Babel, showing that the Gospel is universal for all tribes, tongues, and nations."
        ],
        "mcq": {
            "question": "Why did the Holy Spirit enable the disciples to speak in existing foreign human languages on the Day of Pentecost?",
            "options": [
                "A. To confuse the Roman authorities and prevent them from understanding the Apostles' plans.",
                "B. To prove that Greek and Latin were the only holy languages approved for Christian worship.",
                "C. To demonstrate that the Gospel is universal for every tribe, nation, and tongue, allowing pilgrims to hear God's wonders in their native dialects.",
                "D. To give the disciples a secret commercial advantage in trade with foreign merchants."
            ],
            "correct_answer": "C",
            "explanation": "Speaking in diverse human languages demonstrated that God embraces all cultures and tongues equally, initiating the universal mission of the Church to proclaim redemption to all nations."
        }
    },

    # ─── LESSON 2 ─────────────────────────────────────────────────────────────
    {
        "order": 2,
        "title": "Characteristics of the Early Church",
        "description": "Examine the communal lifestyle, spiritual devotion, and radical generosity of the first Christian community in Jerusalem (Acts 2:42-47, Acts 4:32-37).",
        "goals": [
            "List and explain the five core characteristics and daily rhythms of the Early Church in Jerusalem.",
            "Analyze the theological and practical significance of Koinonia and shared possessions.",
            "Develop practical ways modern school and church fellowships can emulate the early church's unity and care for the needy."
        ],
        "image": {
            "title": "Early Christian Fellowship and Shared Meals",
            "caption": "Depiction of the early Christian community gathering in fellowship, breaking bread, and sharing resources.",
            "url": "https://upload.wikimedia.org/wikipedia/commons/thumb/e/e0/Early_Christian_Agape_Feast.jpg/800px-Early_Christian_Agape_Feast.jpg",
            "author": "Historical Fresco (Catacombs)",
            "licensing": "Public Domain",
            "source": "Wikimedia Commons"
        },
        "intro": """Imagine a community where no one was homeless, no one went to bed hungry, and wealthy individuals voluntarily sold their extra houses and lands to support struggling neighbors. 

This was not a fantasy; it was the everyday reality of the Early Church in Jerusalem. Following Pentecost, the first 3,000 believers formed a radical, loving family that shocked the Roman Empire and drew thousands of new seekers daily. What made their lifestyle so powerful?""",
        "core_scripture": """### Acts 2:42-47 (NIV)
> "They devoted themselves to the apostles’ teaching and to fellowship, to the breaking of bread and to prayer. Everyone was filled with awe at the many wonders and signs performed by the apostles. All the believers were together and had everything in common. They sold property and possessions to give to anyone who had need. Every day they continued to meet together in the temple courts. They broke bread in their homes and ate together with glad and sincere hearts, praising God and enjoying the favor of all the people. And the Lord added to their number daily those who were being saved."

### Acts 4:32-35 (NIV)
> "All the believers were one in heart and mind. No one claimed that any of their possessions was their own, but they shared everything they had... God’s grace was so powerfully at work in them all that there were no needy persons among them." """,
        "theological_pillars": """### The Five Pillars of Early Church Life

1. **Devotion to Apostolic Teaching (*Didache*):**
   The believers spent extensive time daily studying the teachings of Jesus through the eyewitness testimony of the Apostles, establishing sound doctrinal foundations that resisted surrounding pagan and legalistic pressures.

2. **Radical Fellowship (*Koinonia*):**
   *Koinonia* signifies intimate communion, joint partnership, and mutual responsibility. Believers demolished social barriers between rich and poor, masters and slaves, forming a unified spiritual family.

3. **Breaking of Bread (*Klasis tou Artou*):**
   They combined ordinary fellowship dinners in homes with the celebration of the Lord's Supper (Holy Communion), remembering Christ's sacrifice with glad and sincere hearts.

4. **Constant Corporate Prayer and Praise:**
   Gathering daily in both the public temple courts and private households, their lives were saturated with passionate intercession, thanksgiving, and worship.

5. **Shared Possessions and Radical Generosity:**
   Wealthy members sold assets (such as Barnabas selling a field in Acts 4:36-37) and placed the proceeds at the Apostles' feet to distribute to anyone facing financial hardship, ensuring zero poverty within the church.""",
        "svg_fn": get_svg_lesson_2,
        "deep_dive": """### Deep Dive: Voluntary Generosity vs. Forced Collectivism

The early church's practice of 'having everything in common' was distinct from modern political systems:
- **Voluntary Love:** It was motivated by the inward grace of the Holy Spirit, not government coercion (Acts 5:4 confirms property was under personal control before being sold).
- **Needs-Based Distribution:** Funds were distributed specifically to eliminate poverty and physical suffering (*'as anyone had need'*).
- **Spiritual Favor:** Their selfless love won the genuine respect (*charis*) of the entire city, serving as the greatest evangelistic magnet for new converts.""",
        "practical": {
            "title": "4-Step Blueprint for Creating a Caring School Fellowship",
            "steps": [
                {
                    "step_number": 1,
                    "name": "Identify Hidden Needs",
                    "description": "Notice classmates who lack revision materials, school fees, stationery, or decent meals without embarrassing them."
                },
                {
                    "step_number": 2,
                    "name": "Pool Resources Creatively",
                    "description": "Organize peer study groups where textbooks, revision notes, and revision time are shared generously among all students."
                },
                {
                    "step_number": 3,
                    "name": "Practice Inclusive Hospitality",
                    "description": "Invite introverted, struggling, or marginalized classmates to join your lunch table and discussion circles."
                },
                {
                    "step_number": 4,
                    "name": "Maintain Corporate Prayer",
                    "description": "Commit to regular prayer sessions with friends for personal integrity, family peace, and academic excellence."
                }
            ]
        },
        "kenyan_context": """### Kenyan Real-World Context & Church Fellowship

In Kenya, the traditional spirit of *Harambee* (pulling together) and community welfare groups like *Chamas* mirror the early church's collective care. 

Modern Kenyan churches demonstrate this through welfare funds, disaster relief, school sponsorships, and medical camps. When youth actively contribute to church charity drives or organize community clean-ups, they bring the authentic *Koinonia* of Acts 2 to life in their local estates and villages.""",
        "youtube": {
            "title": "BibleProject: The Early Church & Koinonia (Acts)",
            "youtube_id": "tp--5JU4-3c",
            "description": "Explore how the early Christian movement turned Roman social hierarchies upside down through radical generosity and love."
        },
        "reflection": """### Spiritual Reflection & Core Values

- **Selflessness:** The first Christians did not cling possessively to their wealth. How tightly are you holding onto your resources, time, and talents?
- **Community:** Spiritual growth happens best in genuine community, not in isolated individualism. Are you actively plugged into a healthy faith fellowship?""",
        "takeaways": [
            "The Early Church was grounded in five daily pillars: Apostles' teaching, Koinonia, breaking of bread, prayer, and radical generosity.",
            "Believers were 'one in heart and mind', holding possessions in common so that no needy person existed among them.",
            "Fellowship occurred both in large corporate gatherings (temple courts) and intimate home settings.",
            "Their radical love and integrity resulted in favor with the entire public and daily church growth."
        ],
        "mcq": {
            "question": "Which Greek term describes the deep, practical communion, mutual partnership, and shared life of the Early Church?",
            "options": [
                "A. Koinonia",
                "B. Diaspora",
                "C. Synagogue",
                "D. Apologetics"
            ],
            "correct_answer": "A",
            "explanation": "Koinonia refers to intimate spiritual communion, shared life, and practical generosity where believers support each other spiritually, emotionally, and materially."
        }
    },

    # ─── LESSON 3 ─────────────────────────────────────────────────────────────
    {
        "order": 3,
        "title": "Miracles in the Early Church",
        "description": "Analyze the miracles performed by the Apostles, focusing on the healing of the lame man at the Beautiful Gate (Acts 3:1-10) and apostolic humility (Acts 3:11-16, Acts 5:12-16).",
        "goals": [
            "Recount the miracle of the healing of the lame beggar at the Beautiful Gate in detail.",
            "Analyze why Peter and John refused to accept personal credit or worship for the miracle.",
            "Demonstrate Christian compassion and humility by using personal talents to support marginalized individuals today."
        ],
        "image": {
            "title": "Peter and John Healing the Lame Man",
            "caption": "Raphael's depiction of Peter and John healing the crippled beggar at the Beautiful Gate in the name of Jesus Christ.",
            "url": "https://upload.wikimedia.org/wikipedia/commons/thumb/9/91/Raphael_-_The_Healing_of_the_Lame_Man.jpg/800px-Raphael_-_The_Healing_of_the_Lame_Man.jpg",
            "author": "Raphael (1515)",
            "licensing": "Public Domain",
            "source": "Wikimedia Commons"
        },
        "intro": """Imagine sitting on cold stone steps every single day from childhood to adulthood, begging for small copper coins just to buy bread. You watch thousands of wealthy worshippers pass by, looking down with pity or disgust. 

One afternoon, two men stop, look directly into your eyes, and say: 'Look at us!' You expect a valuable gold coin. Instead, they offer you something money could never buy—instant, complete physical restoration! Let's explore the miraculous power and genuine humility of the Apostles.""",
        "core_scripture": """### Acts 3:1-8 (NIV)
> "One day Peter and John were going up to the temple at the time of prayer—at three in the afternoon. Now a man who was lame from birth was being carried to the temple gate called Beautiful, where he was put every day to beg from those going into the temple courts. When he saw Peter and John about to enter, he asked them for money. Peter looked straight at him, as did John. Then Peter said, 'Look at us!' So the man gave them his attention, expecting to get something from them.
> 
> Then Peter said, 'Silver or gold I do not have, but what I do have I give you. In the name of Jesus Christ of Nazareth, walk.' Taking him by the right hand, he helped him up, and instantly the man’s feet and ankles became strong. He jumped to his feet and began to walk. Then he went with them into the temple courts, walking and jumping, and praising God."

### Acts 3:12, 16 (NIV)
> "When Peter saw this, he said to them: 'Fellow Israelites, why does this surprise you? Why do you stare at us as if by our own power or godliness we had made this man walk?... By faith in the name of Jesus, this man whom you see and know was made strong. It is Jesus’ name and the faith that comes through him that has completely healed him, as you can all see.'" """,
        "theological_pillars": """### Theological Insights into Apostolic Miracles

1. **The Purpose of Apostolic Miracles:**
   Miracles in Acts were never mere magic tricks or human entertainment. They served as divine signposts (*semeia*) validating that Jesus Christ was resurrected and alive, confirming the divine authority of the Gospel message.

2. **Personal Dignity & Direct Eye Contact:**
   Peter and John did not carelessly toss a coin. By saying *'Look at us!'*, they restored the beggar's human dignity, looking past his physical handicap to minister to his whole person.

3. **Authority in the Name of Jesus:**
   Peter declared: *'Silver or gold I do not have, but what I do have I give you.'* Divine healing flowed not from apostolic wealth or ritual herbs, but exclusively through the sovereign name of Jesus Christ of Nazareth.

4. **Absolute Refusal of Human Glory:**
   When the astonished crowd gathered at Solomon's Colonnade to idolize the Apostles, Peter immediately corrected them. He deflected all praise, teaching that human godliness has zero healing power—Jesus alone restores.""" ,
        "svg_fn": get_svg_lesson_3,
        "deep_dive": """### Deep Dive: Physical Healing and Spiritual Worship

Notice the sequence of the healed man's response:
- **Instant Strength:** Feet and ankle bones received immediate physiological strength.
- **Joyful Movement:** He jumped up, walked, and leaped into the temple courts.
- **Uninhibited Praise:** Under Jewish law, physically disabled individuals were restricted from entering inner sacred spaces. Now fully healed, his first action was entering God's courts praising God publicly.

This demonstrates that God's miracles restore people physically, socially, and spiritually, bringing the excluded into full fellowship with God and community.""",
        "practical": {
            "title": "4-Step Framework for Offering What You Have",
            "steps": [
                {
                    "step_number": 1,
                    "name": "Look Beyond Physical Limitations",
                    "description": "Treat persons with disabilities and marginalized individuals with deep respect, honor, and direct attentiveness."
                },
                {
                    "step_number": 2,
                    "name": "Give Your Best Resources",
                    "description": "Even when you have no financial wealth to give, offer your time, prayers, encouragement, and practical assistance."
                },
                {
                    "step_number": 3,
                    "name": "Maintain Extreme Humility",
                    "description": "Whenever you achieve academic success, leadership honor, or athletic victory, redirect all praise to God."
                },
                {
                    "step_number": 4,
                    "name": "Point Others to Christ",
                    "description": "Use every platform and opportunity to explain that your moral strength and talents come from faith in Jesus."
                }
            ]
        },
        "kenyan_context": """### Kenyan Real-World Context & Church Fellowship

In Kenya, many persons living with disabilities face social stigmatization, lack of accessibility infrastructure, and economic hardship. 

Christian institutions and schools have historically led the way in establishing special schools (such as Joytown in Thika) and empowerment programs. As young believers, we are called to stand against discrimination, advocate for disability access in our schools and churches, and show Christlike compassion to all.""",
        "youtube": {
            "title": "BibleProject: Miracles in Acts & The Power of Jesus' Name",
            "youtube_id": "CGbNw855Bsw",
            "description": "Examine how signs and wonders confirmed the resurrection of Jesus and catalyzed rapid church growth in Jerusalem."
        },
        "reflection": """### Spiritual Reflection & Core Values

- **Humility:** The Apostles boldly rejected human applause. When you do something commendable, do you crave praise on social media, or do you seek God's approval in secret?
- **Active Faith:** Peter took the lame man by the hand before his legs had visibly changed. True faith steps out boldly in obedience to God's Word.""",
        "takeaways": [
            "Peter and John healed a man crippled from birth at the Beautiful Gate in the powerful name of Jesus Christ.",
            "The Apostles possessed no silver or gold, but gave supernatural restoration through faith in Christ.",
            "Peter rebuked the crowd for idolizing them, insisting that Jesus alone was the source of healing power.",
            "Miracles validated apostolic preaching and led to thousands of new believers coming to repentance."
        ],
        "mcq": {
            "question": "What did Peter state was the sole reason the lame beggar at the Beautiful Gate was completely healed?",
            "options": [
                "A. Peter and John's personal piety and lengthy spiritual fasting.",
                "B. The special medical properties of the dust near Solomon's Colonnade.",
                "C. Faith in the authoritative, resurrected name of Jesus Christ of Nazareth.",
                "D. The generous financial contributions of the worshippers entering the temple."
            ],
            "correct_answer": "C",
            "explanation": "Peter explicitly told the crowd that human power and piety had nothing to do with the miracle; complete physical restoration occurred solely through faith in the name of Jesus Christ."
        }
    },

    # ─── LESSON 4 ─────────────────────────────────────────────────────────────
    {
        "order": 4,
        "title": "Paul and Silas: The Prison Context",
        "description": "Explore the historical, cultural, and spiritual background leading to the arrest and imprisonment of Paul and Silas in Philippi (Acts 16:16-24).",
        "goals": [
            "Explain the spiritual deliverance of the fortune-telling slave girl in Philippi (Acts 16:16-18).",
            "Analyze the economic and political motivations behind the false charges brought against Paul and Silas.",
            "Evaluate modern forms of human exploitation and formulate principled Christian responses to injustice."
        ],
        "image": {
            "title": "Paul and Silas Arrested in Philippi",
            "caption": "Depiction of Paul and Silas being seized in the marketplace of Philippi and brought before Roman magistrates.",
            "url": "https://upload.wikimedia.org/wikipedia/commons/thumb/d/d4/Paul_and_Silas_in_Prison_Philippi.jpg/800px-Paul_and_Silas_in_Prison_Philippi.jpg",
            "author": "Historical Engraving",
            "licensing": "Public Domain",
            "source": "Wikimedia Commons"
        },
        "intro": """Have you ever witnessed someone in power exploiting vulnerable people—such as greedy employers underpaying domestic workers or traffickers forcing children into street begging? 

In ancient Philippi, a young slave girl was trapped in double bondage: possessed by a demonic spirit and exploited by ruthless owners who used her fortune-telling to amass personal wealth. When the Apostle Paul set her free in Jesus' name, her masters did not celebrate her deliverance—they launched a furious, violent retaliation.""",
        "core_scripture": """### Acts 16:16-19 (NIV)
> "Once when we were going to the place of prayer, we were met by a female slave who had a spirit by which she predicted the future. She earned a great deal of money for her owners by fortune-telling. She followed Paul and the rest of us, shouting, 'These men are servants of the Most High God, who are telling you the way to be saved.' She kept this up for many days. Finally Paul became so annoyed that he turned around and said to the spirit, 'In the name of Jesus Christ I command you to come out of her!' At that moment the spirit left her.
> 
> When her owners realized that their hope of making money was gone, they seized Paul and Silas and dragged them into the marketplace to face the authorities."

### Acts 16:20-24 (NIV)
> "They brought them before the magistrates and said, 'These men are Jews, and are throwing our city into an uproar by advocating customs unlawful for us Romans to accept or practice.' The crowd joined in the attack against them, and the magistrates ordered them to be stripped and beaten with rods. After they had been severely flogged, they were thrown into prison, and the jailer was commanded to guard them carefully. When he received these orders, he put them in the inner cell and fastened their feet in the stocks." """,
        "theological_pillars": """### Exegetical Analysis: Deliverance vs. Exploitation

1. **The Spirit of Divination (*Pythona*):**
   The slave girl was possessed by a demonic spirit associated with the Greek oracle at Delphi. Although her words were factually true (*'servants of the Most High God'*), her source was demonic, seeking to associate the Gospel with occult practices.

2. **Spiritual Discernment in Action:**
   Paul exercised spiritual discernment. True ministers of God refuse endorsements from demonic or ungodly sources. In the sovereign authority of Jesus Christ, Paul commanded the spirit to depart immediately.

3. **The Root of Persecution: Economic Greed:**
   The slave owners' fury was not driven by religious zeal, but financial loss: *'their hope of making money was gone'*. Greed often masks itself behind patriotic or cultural outrage.

4. **False Political Accusations & Roman Xenophobia:**
   To incite the Philippian magistrates, the owners hid their financial loss and played the ethnic card, accusing Paul and Silas of being *'Jews advocating unlawful customs for Romans'*.

5. **Unjust Punishment:**
   Without a formal trial, Paul and Silas were stripped, severely beaten with wooden rods, thrown into the dark inner dungeon, and had their feet locked in agonizing wooden stocks.""",
        "svg_fn": get_svg_lesson_4,
        "deep_dive": """### Deep Dive: Human Dignity Over Economic Profit

The confrontation in Philippi highlights the clash between two worldviews:
- **The World's Exploitative Economy:** Treats vulnerable human beings as commercial assets to be used, monetized, and discarded for selfish profit.
- **The Gospel's Redemptive Economy:** Treats every individual as an image-bearer of God (*Imago Dei*), worthy of freedom, dignity, and spiritual deliverance.

Paul chose to liberate the oppressed girl knowing full well that doing so would invite severe personal persecution. Christian integrity requires standing up for human dignity even when it disrupts corrupt economic systems.""",
        "practical": {
            "title": "4-Step Strategy for Standing Against Exploitation",
            "steps": [
                {
                    "step_number": 1,
                    "name": "Recognize Exploitative Patterns",
                    "description": "Learn to identify child labor, academic bullying (forcing others to do assignments), and commercial exploitation."
                },
                {
                    "step_number": 2,
                    "name": "Exercise Spiritual Discernment",
                    "description": "Never compromise Christian values for easy money, flattery, or popularity that comes from unethical sources."
                },
                {
                    "step_number": 3,
                    "name": "Advocate for the Vulnerable",
                    "description": "Report cases of abuse, exploitation, or harassment in your school or neighborhood to responsible authorities."
                },
                {
                    "step_number": 4,
                    "name": "Expect and Endure Opposition",
                    "description": "Understand that doing what is right may provoke anger from those who benefit from injustice, but God remains faithful."
                }
            ]
        },
        "kenyan_context": """### Kenyan Real-World Context & Church Fellowship

In Kenya, issues of child labor, human trafficking, and exploitation of vulnerable domestic workers remain critical challenges. 

The Constitution of Kenya (Article 30) explicitly prohibits slavery, servitude, and forced labor. The Church plays a leading role in rescuing street children, operating rescue centers, and providing vocational training to restore dignity to the exploited, continuing Paul's legacy of deliverance.""",
        "youtube": {
            "title": "BibleProject: Acts 13-28 (Paul's Missionary Journeys & Persecution)",
            "youtube_id": "fo_pTt_g-pQ",
            "description": "Follow Paul and Silas on their mission across the Roman Empire as the Gospel challenges political and economic empires."
        },
        "reflection": """### Spiritual Reflection & Core Values

- **Integrity:** Paul refused to let an evil spirit act as a free publicity agent for the Gospel. How careful are you to maintain absolute purity and integrity in your spiritual walk?
- **Courage:** Doing the right thing cost Paul and Silas severe physical pain. Are you willing to endure unpopularity to defend someone who is being mistreated?""",
        "takeaways": [
            "Paul cast out a spirit of divination from an exploited slave girl in the name of Jesus Christ.",
            "The owners attacked Paul and Silas because their lucrative fortune-telling revenue stream was destroyed.",
            "The owners disguised their greed behind false charges of civil disturbance and anti-Roman customs.",
            "Paul and Silas were illegally beaten with rods and locked in stocks in the inner prison."
        ],
        "mcq": {
            "question": "What was the real reason the masters of the slave girl dragged Paul and Silas before the magistrates in Philippi?",
            "options": [
                "A. They wanted to protect Roman traditional religion from foreign philosophies.",
                "B. They were angry because Paul's deliverance of the girl destroyed their profitable fortune-telling business.",
                "C. They wanted to demand that Paul teach them how to perform miracles.",
                "D. They were defending the slave girl from being harmed by the Apostles."
            ],
            "correct_answer": "B",
            "explanation": "The biblical text notes that 'when her owners realized that their hope of making money was gone, they seized Paul and Silas'. Greed was the underlying motive, disguised as civic patriotism."
        }
    },

    # ─── LESSON 5 ─────────────────────────────────────────────────────────────
    {
        "order": 5,
        "title": "Paul and Silas: Praise in the Prison",
        "description": "Analyze the response of Paul and Silas during intense suffering, exploring the transformative power of authentic worship at midnight (Acts 16:25-28, Psalm 34:1).",
        "goals": [
            "Describe the midnight prayer, hymn singing, and earthquake in the Philippian jail (Acts 16:25-26).",
            "Analyze the spiritual, psychological, and evangelical impact of praising God during severe suffering.",
            "Cultivate the discipline of maintaining joy, patience, and worship during personal adversity and academic stress."
        ],
        "image": {
            "title": "Paul and Silas Singing Praises in the Philippian Jail",
            "caption": "Dramatic representation of Paul and Silas in the inner dungeon praying and singing hymns at midnight as prisoners listen.",
            "url": "https://upload.wikimedia.org/wikipedia/commons/thumb/c/c5/Paul_and_Silas_Praying_in_Prison.jpg/800px-Paul_and_Silas_Praying_in_Prison.jpg",
            "author": "Historical Illustration",
            "licensing": "Public Domain",
            "source": "Wikimedia Commons"
        },
        "intro": """If you were unjustly arrested, severely flogged until your back was bleeding, and locked into painful wooden stocks inside a damp, foul-smelling dungeon, what would you do at midnight? 

Most humans would drown in bitterness, weeping, or plans of vengeance. But around midnight, the deep chambers of the Philippian jail began to echo with a sound never before heard in that dungeon—not groans of agony, but triumphant, melodic songs of praise to the Almighty God!""",
        "core_scripture": """### Acts 16:25-28 (NIV)
> "About midnight Paul and Silas were praying and singing hymns to God, and the other prisoners were listening to them. Suddenly there was such a violent earthquake that the foundations of the prison were shaken. At once all the prison doors flew open, and everyone’s chains came loose.
> 
> The jailer woke up, and when he saw the prison doors open, he drew his sword and was about to kill himself because he thought the prisoners had escaped. But Paul shouted, 'Don’t harm yourself! We are all here!'"

### Psalm 34:1 (NIV)
> "I will extol the Lord at all times; his praise will always be on my lips." """,
        "theological_pillars": """### The Dynamics of Midnight Worship

1. **Worship as a Spiritual Choice, Not an Emotion:**
   Paul and Silas did not praise God because their physical bodies felt comfortable. They praised God because His character and faithfulness remain unchanged regardless of human circumstances.

2. **The Audible Witness to Fellow Prisoners:**
   *‘And the other prisoners were listening to them.’* In ancient Greek, the verb (*epakroōmai*) implies intense, attentive listening. The authentic, joyful faith of Paul and Silas in extreme pain spoke louder than any sermon.

3. **The Divine Interruption: The Supernatural Earthquake:**
   God responded to their praise with a localized, violent earthquake that shook the foundations, burst open every locked iron door, and unfastened the chains of *every* prisoner present.

4. **Universal Release:**
   God's intervention was not just for the Apostles; the chains of all prisoners were loosed, demonstrating God's boundless grace to all captives.""",
        "svg_fn": get_svg_lesson_5,
        "deep_dive": """### Deep Dive: The Power of Praise in Adversity

Praise during suffering achieves three profound spiritual breakthroughs:
- **Reframing Reality:** It shifts focus from the temporary physical cage to the eternal sovereignty of God.
- **Shattering Internal Bonds:** Long before the physical chains fell off the wall, Paul and Silas were already spiritually free from fear, bitterness, and despair.
- **Evangelistic Magnet:** Hardened criminals and prison guards are drawn to Christ when they witness believers displaying supernatural peace and resilience under trial.""",
        "practical": {
            "title": "4-Step Guide to Praising God During Personal Crises",
            "steps": [
                {
                    "step_number": 1,
                    "name": "Refuse the Trap of Bitterness",
                    "description": "When faced with disappointment, unfair blame, or loss, deliberately reject feelings of anger and victimhood."
                },
                {
                    "step_number": 2,
                    "name": "Initiate Intentional Praise",
                    "description": "Play uplifting worship music or recite Psalms of thanksgiving even when you do not feel like it."
                },
                {
                    "step_number": 3,
                    "name": "Remember God's Past Faithfulness",
                    "description": "List specific times God helped you and your family overcome difficult situations in the past."
                },
                {
                    "step_number": 4,
                    "name": "Be a Calming Influence for Others",
                    "description": "Show peaceful courage during stressful family or school moments, encouraging those around you who are anxious."
                }
            ]
        },
        "kenyan_context": """### Kenyan Real-World Context & Church Fellowship

In Kenya, gospel worship music is a central pillar of daily life. Whether in public transport (*matatus*), school assemblies, or hospital wards, Kenyans turn to praise during economic hardship, grief, and national challenges. 

Our resilience as a nation is deeply anchored in faith. When Kenyan youth sing praises amidst academic pressure or financial constraints, they embody the midnight faith of Paul and Silas.""",
        "youtube": {
            "title": "BibleProject: Acts 13-28 (Paul in Prison & Global Mission)",
            "youtube_id": "fo_pTt_g-pQ",
            "description": "Witness how prison doors and chains could not stop the unstoppable advance of God's Kingdom."
        },
        "reflection": """### Spiritual Reflection & Core Values

- **Resilience:** Joy is not the absence of trouble, but the presence of Christ in the middle of trouble. What is your automatic reaction when plans go wrong?
- **Impact:** People watch how Christians behave during adversity. Does your reaction to stress draw others closer to God or drive them away?""",
        "takeaways": [
            "At midnight, despite severe wounds and stocks, Paul and Silas were praying and singing hymns to God.",
            "The other prisoners listened intently to their authentic worship in suffering.",
            "A violent earthquake shook the foundations, opening all doors and loosening everyone's chains.",
            "Authentic praise in trials releases divine power and breaks both physical and spiritual bondage."
        ],
        "mcq": {
            "question": "What key detail does Luke include about the response of the other prisoners while Paul and Silas were singing at midnight?",
            "options": [
                "A. The prisoners shouted angrily at them to be quiet so they could sleep.",
                "B. The prisoners were listening attentively to their prayers and hymns.",
                "C. The prisoners plotted an immediate armed mutiny against the jailer.",
                "D. The prisoners laughed and mocked the Apostles' God."
            ],
            "correct_answer": "B",
            "explanation": "Acts 16:25 specifically records that 'the other prisoners were listening to them', showing how their joyful worship in pain served as a compelling witness to everyone in the jail."
        }
    },

    # ─── LESSON 6 ─────────────────────────────────────────────────────────────
    {
        "order": 6,
        "title": "The Conversion of the Jailer",
        "description": "Examine the dramatic conversion of the Philippian jailer, analyze Paul's mercy, and explain the steps to Christian salvation (Acts 16:29-34, Romans 10:9).",
        "goals": [
            "Describe the jailer's crisis, suicide attempt, and Paul's life-saving intervention (Acts 16:27-28).",
            "Explain Paul's answer to the question 'What must I do to be saved?' (Acts 16:30-31).",
            "Analyze the immediate practical transformation in the jailer's life and apply Christian mercy to personal relationships."
        ],
        "image": {
            "title": "The Conversion of the Philippian Jailer",
            "caption": "Depiction of the Philippian jailer falling on his knees before Paul and Silas inside the shattered prison.",
            "url": "https://upload.wikimedia.org/wikipedia/commons/thumb/1/1a/Philippian_Jailer_Conversion.jpg/800px-Philippian_Jailer_Conversion.jpg",
            "author": "Historical Painting",
            "licensing": "Public Domain",
            "source": "Wikimedia Commons"
        },
        "intro": """Have you ever found yourself in a catastrophic crisis where you thought your life, career, or reputation was completely ruined? 

The Philippian jailer woke up to open prison doors. Under Roman military law, a guard whose prisoners escaped suffered the exact death penalties of those prisoners. Overcome with absolute terror, he drew his sword to commit suicide. But just before the blade struck, a compassionate voice called out from the dark, altering his eternal destiny!""",
        "core_scripture": """### Acts 16:29-34 (NIV)
> "The jailer called for lights, rushed in and fell trembling before Paul and Silas. He then brought them out and asked, 'Sirs, what must I do to be saved?'
> 
> They replied, 'Believe in the Lord Jesus, and you will be saved—you and your household.' Then they spoke the word of the Lord to him and to all the others in his house.
> 
> At that hour of the night the jailer took them and washed their wounds; then immediately he and all his household were baptized. The jailer brought them into his house and set a meal before them; he was filled with joy because he had come to believe in God—he and his whole household."

### Romans 10:9 (NIV)
> "If you declare with your mouth, 'Jesus is Lord,' and believe in your heart that God raised him from the dead, you will be saved." """,
        "theological_pillars": """### Exegetical Highlights: Grace Over Retaliation

1. **Valuing the Enemy's Life:**
   Paul and Silas possessed a golden opportunity to flee. Instead, they stayed behind to save the physical life of their cruel jailer. They valued his immortal soul far more than their own physical comfort.

2. **The Fundamental Human Question:**
   Trembling with awe at the miracle and the Apostles' selfless love, the jailer asked the ultimate question: *'Sirs, what must I do to be saved?'* He recognized that his deepest need was not merely escaping Roman execution, but spiritual salvation from sin.

3. **The Simple, Uncompromising Gospel:**
   Paul did not burden him with complex rituals or legalistic demands. The answer was direct and universal: *'Believe in the Lord Jesus, and you will be saved—you and your household.'*

4. **The Immediate Evidences of Authentic Regeneration:**
   - **Tender Compassion:** He washed their bleeding, flogged backs.
   - **Public Obedience:** He and his entire family were baptized immediately at midnight.
   - **Joyful Hospitality:** He brought them into his home, prepared a celebratory meal, and rejoiced in his new faith.""",
        "svg_fn": get_svg_lesson_6,
        "deep_dive": """### Deep Dive: Household Salvation in the New Testament

The conversion of the Philippian jailer is one of several household conversions in Acts (including Cornelius in Acts 10 and Lydia in Acts 16):
- **Covenantal Influence:** When the head of a home embraces Christ, his transformed character creates an atmosphere where his entire family hears and embraces the Gospel.
- **Holistic Renewal:** Faith in Christ immediately transformed this Roman prison official from a hardened, callous instrument of violence into a gentle, hospitable servant of God.""",
        "practical": {
            "title": "4-Step Blueprint for Responding with Christlike Mercy",
            "steps": [
                {
                    "step_number": 1,
                    "name": "Choose Mercy Over Revenge",
                    "description": "When someone who has wronged you falls into trouble, resist the urge to celebrate their misfortune."
                },
                {
                    "step_number": 2,
                    "name": "Step In to Protect and Help",
                    "description": "Offer practical help, kindness, or a listening ear to those who are going through severe personal crises."
                },
                {
                    "step_number": 3,
                    "name": "Share the Gospel Simply",
                    "description": "Explain clearly to friends that salvation is received through faith in Jesus Christ, not by earning it through works."
                },
                {
                    "step_number": 4,
                    "name": "Demonstrate Faith in Practical Deeds",
                    "description": "Let your faith be seen through acts of service, reconciliation in your family, and caring for those in pain."
                }
            ]
        },
        "kenyan_context": """### Kenyan Real-World Context & Church Fellowship

In Kenya, Prison Chaplaincy ministries (such as Prison Fellowship Kenya) minister to thousands of inmates and prison wardens across facilities like Kamiti, Shimo la Tewa, and Lang'ata. 

Many former inmates and officers have experienced dramatic conversions like the Philippian jailer, proving that God's grace reaches into the darkest prison cells to transform lives and restore families.""",
        "youtube": {
            "title": "BibleProject: Acts 13-28 (The Philippian Jailer & The Roman World)",
            "youtube_id": "fo_pTt_g-pQ",
            "description": "Watch how the Gospel crossed ethnic and cultural barriers to transform Roman households in Philippi."
        },
        "reflection": """### Spiritual Reflection & Core Values

- **Compassion:** Paul and Silas showed intense love for a man who had hours earlier fastened their feet in stocks. Can you pray sincerely for someone who has hurt you?
- **Transformation:** The jailer's life changed completely in a single night. Have you allowed God's love to soften your attitudes toward difficult people?""",
        "takeaways": [
            "Paul prevented the terrified jailer from committing suicide by assuring him that all prisoners were present.",
            "The jailer asked: 'Sirs, what must I do to be saved?' and Paul answered: 'Believe in the Lord Jesus, and you will be saved.'",
            "The jailer's genuine conversion was shown immediately by washing their wounds, being baptized, and feeding the Apostles.",
            "Salvation brings profound joy and moral transformation to individuals and entire households."
        ],
        "mcq": {
            "question": "What immediate practical actions demonstrated that the Philippian jailer had genuinely experienced salvation?",
            "options": [
                "A. He locked the Apostles back in the inner dungeon and reported the earthquake to the emperor.",
                "B. He resigned from his military job and fled to Athens with his savings.",
                "C. He washed the Apostles' wounds, was baptized with his household, and joyfully served them a meal.",
                "D. He filed a formal lawsuit against the magistrates for unlawful imprisonment."
            ],
            "correct_answer": "C",
            "explanation": "True repentance produces immediate fruit: the jailer washed their wounds (compassion), was baptized (obedience), and fed them in his home with great joy (hospitality)."
        }
    },

    # ─── LESSON 7 ─────────────────────────────────────────────────────────────
    {
        "order": 7,
        "title": "Characteristics of the Modern Church",
        "description": "Compare the contemporary Christian Church with the Early Church, exploring apostolic continuity, modern worship, and youth stewardship (1 Peter 2:9-10, Ephesians 4:11-16).",
        "goals": [
            "Identify the continuities between early apostolic practices and contemporary church life.",
            "Analyze challenges facing the modern church, including individualism and religious showmanship.",
            "Formulate actionable ways Christian youth can actively contribute to church worship, outreach, and stewardship."
        ],
        "image": {
            "title": "The Contemporary Church in Worship and Fellowship",
            "caption": "A vibrant modern Christian congregation gathering in corporate worship, prayer, and community ministry.",
            "url": "https://upload.wikimedia.org/wikipedia/commons/thumb/c/ca/Contemporary_Christian_Church_Worship.jpg/800px-Contemporary_Christian_Church_Worship.jpg",
            "author": "Church Media Archives",
            "licensing": "CC-BY-SA",
            "source": "Wikimedia Commons"
        },
        "intro": """If an early Christian believer from Jerusalem in A.D. 33 walked into your local church this Sunday, would they recognize what was happening? 

Despite our digital screens, modern sound systems, and musical instruments, the essential heartbeat of the Church remains identical across 2,000 years! In this lesson, we examine how the genetic DNA of the Early Church continues in our local parishes today and discover how you are an indispensable part of that ongoing story.""",
        "core_scripture": """### 1 Peter 2:9-10 (NIV)
> "But you are a chosen people, a royal priesthood, a holy nation, God’s special possession, that you may declare the praises of him who called you out of darkness into his wonderful light. Once you were not a people, but now you are the people of God; once you had not received mercy, but now you have received mercy."

### Ephesians 4:11-13 (NIV)
> "So Christ himself gave the apostles, the prophets, the evangelists, the pastors and teachers, to equip his people for works of service, so that the body of Christ may be built up until we all reach unity in the faith and in the knowledge of the Son of God and become mature, attaining to the whole measure of the fullness of Christ." """,
        "theological_pillars": """### Apostolic Continuities in the Modern Church

1. **Apostolic Continuity (*Traditio*):**
   The modern church preserves the core message of the Apostles: the authority of Scripture, the deity and resurrection of Jesus Christ, salvation by grace through faith, and the fellowship of the Holy Spirit.

2. **Structural Continuities with Acts 2:42:**
   - **Sermons & Bible Study:** Continues devotion to the Apostles' teaching.
   - **Holy Communion (Eucharist):** Continues the sacramental breaking of bread in remembrance of Christ.
   - **Corporate Worship & Midweek Prayers:** Continues daily prayer and praise in the temple courts.
   - **Church Charities & Food Drives:** Continues radical generosity and care for widows, orphans, and the needy.

3. **Key Challenges Facing the Modern Church:**
   - **Individualism & Consumerism:** Treating church as an entertainment venue rather than a sacrificial community.
   - **Religious Showmanship:** Seeking social media popularity or financial gain rather than humble service.""",
        "svg_fn": get_svg_lesson_7,
        "deep_dive": """### Deep Dive: The Priesthood of All Believers

1 Peter 2:9 declares that *every* Christian is part of a 'royal priesthood'. This means:
- **No Passive Spectators:** Ministry is not reserved solely for ordained clergy; every believer is gifted by the Holy Spirit to build up the Church.
- **Youth Leadership:** Young people are not merely the 'church of tomorrow'—they are active ministers today through choirs, ushering, multimedia teams, intercession, and community outreach.""",
        "practical": {
            "title": "4-Step Framework for Active Youth Stewardship in Church",
            "steps": [
                {
                    "step_number": 1,
                    "name": "Join a Service Department",
                    "description": "Volunteer your talents in the youth choir, praise & worship band, audio-visual team, or ushering department."
                },
                {
                    "step_number": 2,
                    "name": "Practice Faithful Giving",
                    "description": "Honor God with your tithes and offerings from pocket money or gifts, supporting church outreach projects."
                },
                {
                    "step_number": 3,
                    "name": "Engage in Community Outreach",
                    "description": "Participate actively in church visits to children's homes, elderly care centers, and prison ministries."
                },
                {
                    "step_number": 4,
                    "name": "Keep a Spiritual Journal",
                    "description": "Record sermon notes, Bible study reflections, and answered prayers to foster consistent spiritual growth."
                }
            ]
        },
        "kenyan_context": """### Kenyan Real-World Context & Church Fellowship

In Kenya, churches are central pillars of national life, operating thousands of schools, hospitals, universities, and vocational training institutes. 

Youth make up over 60% of many Kenyan congregations. Programs like Brigade, Christian Youth Fellowship (PCEA), Anglican Youth Fellowship (KAYO), and Catholic Youth Movement (CYM) equip students with leadership skills, entrepreneurship mentorship, and moral integrity to impact society.""",
        "youtube": {
            "title": "BibleProject: The Church (Body of Christ)",
            "youtube_id": "CGbNw855Bsw",
            "description": "Discover how Jesus designed the Church to be a multi-ethnic community of love, worship, and service to the world."
        },
        "reflection": """### Spiritual Reflection & Core Values

- **Stewardship:** God has endowed you with unique energy, digital skills, and talents. Are you using them to build God's Kingdom or only for personal entertainment?
- **Unity:** The modern church is called to be 'one body'. How can you foster unity among classmates from different Christian denominations?""",
        "takeaways": [
            "The modern church continues the core apostolic practices: Scripture teaching, Holy Communion, prayer, and charity.",
            "1 Peter 2:9 establishes the 'priesthood of all believers', calling every Christian to active service.",
            "Modern challenges include consumerism, individualism, and religious showmanship.",
            "Youth have a vital responsibility to participate in worship, stewardship, and community outreach."
        ],
        "mcq": {
            "question": "Which modern church practice directly continues the Early Church practice of 'breaking bread' established by Jesus?",
            "options": [
                "A. Printing weekly church announcements and calendars.",
                "B. Celebrating Holy Communion (the Lord's Supper) and hosting charity fellowship meals.",
                "C. Upgrading the church electronic sound and lighting equipment.",
                "D. Electing members to church administrative boards."
            ],
            "correct_answer": "B",
            "explanation": "Holy Communion (the Eucharist) is the direct continuation of the Last Supper and the early church practice of breaking bread, symbolizing spiritual unity and remembrance of Christ."
        }
    },

    # ─── LESSON 8 ─────────────────────────────────────────────────────────────
    {
        "order": 8,
        "title": "The Call to Salvation Today",
        "description": "Explain the concept of salvation, explore the biblical steps to receiving God's grace, and guide learners in their personal response to Christ (Romans 10:8-13, 2 Corinthians 5:17-20).",
        "goals": [
            "Define biblical salvation (*Soteria*) and explain the role of divine grace versus human works.",
            "Outline the four biblical steps of salvation: Acknowledge, Believe, Confess, and Walk in New Life.",
            "Draft a personal commitment to live as an ambassador for Christ with integrity and moral courage."
        ],
        "image": {
            "title": "The Call to Salvation: A New Creation in Christ",
            "caption": "Symbolic representation of transformation and new spiritual life through faith in Jesus Christ.",
            "url": "https://upload.wikimedia.org/wikipedia/commons/thumb/3/36/Transfiguration_of_Jesus_-_Bloch.jpg/800px-Transfiguration_of_Jesus_-_Bloch.jpg",
            "author": "Carl Bloch (1872)",
            "licensing": "Public Domain",
            "source": "Wikimedia Commons"
        },
        "intro": """Have you ever played a video game where your character got completely trapped, made fatal mistakes, and you desperately needed to press the 'Reset' button to start fresh? 

Salvation is God's ultimate spiritual reset for the human soul! No matter how heavy your past mistakes, bad habits, or guilt may feel, God offers complete forgiveness, a clean slate, and eternal life through Jesus Christ. Let's discover what it practically means to accept His life-transforming gift today.""",
        "core_scripture": """### Romans 10:8-13 (NIV)
> "The word is near you; it is in your mouth and in your heart,” that is, the message concerning faith that we proclaim: If you declare with your mouth, 'Jesus is Lord,' and believe in your heart that God raised him from the dead, you will be saved. For it is with your heart that you believe and are justified, and it is with your mouth that you profess your faith and are saved.
> 
> As Scripture says, 'Anyone who believes in him will never be put to shame.' For there is no difference between Jew and Gentile—the same Lord is Lord of all and richly blesses all who call on him, for, 'Everyone who calls on the name of the Lord will be saved.'"

### 2 Corinthians 5:17-20 (NIV)
> "Therefore, if anyone is in Christ, the new creation has come: The old has gone, the new is here! All this is from God, who reconciled us to himself through Christ and gave us the ministry of reconciliation... We are therefore Christ’s ambassadors, as though God were making his appeal through us." """,
        "theological_pillars": """### The Architecture of Salvation (*Soteriology*)

1. **Definition of Salvation (*Soteria*):**
   Salvation means complete deliverance from the penalty of sin (justification), the ongoing power of sin (sanctification), and the future presence of sin (glorification).

2. **Grace vs. Human Works (Ephesians 2:8-9):**
   Salvation is an unmerited gift of divine grace (*Charis*). No human being can earn salvation through good works, wealth, or ancestry; good deeds are the joyful fruit of salvation, not the purchase price.

3. **The Four Biblical Steps of Salvation:**
   - **Acknowledge Need:** Admitting that we are sinners incapable of saving ourselves (Romans 3:23).
   - **Believe in Heart:** Trusting fully in the sacrificial death and physical resurrection of Jesus Christ.
   - **Confess with Mouth:** Declaring publicly that Jesus is Lord and Master of our lives.
   - **Walk in New Life:** Living daily as a 'New Creation' guided by the Holy Spirit.

4. **Christ's Ambassadors (2 Corinthians 5:20):**
   Saved believers receive a sacred mission: representing the Kingdom of God in their schools, families, and society with integrity and love.""",
        "svg_fn": get_svg_lesson_8,
        "deep_dive": """### Deep Dive: Justification and Sanctification

Understanding the two essential dimensions of salvation:
- **Justification (Instantaneous Legal Verdict):** The moment you place faith in Christ, God declares you legally righteous, wiping away all guilt based on Jesus' blood.
- **Sanctification (Lifelong Transformational Journey):** The Holy Spirit works continuously in your heart, empowering you to conquer negative habits, resist temptations, and grow in Christlike character daily.""",
        "practical": {
            "title": "4-Step Action Plan for Walking as a New Creation",
            "steps": [
                {
                    "step_number": 1,
                    "name": "Make a Sincere Decision",
                    "description": "Pray sincerely, repenting of your sins and inviting Jesus Christ to be your personal Lord and Savior."
                },
                {
                    "step_number": 2,
                    "name": "Break Away from Destructive Habits",
                    "description": "Deliberately turn away from cheating, dishonest language, sexual immorality, and negative peer pressure."
                },
                {
                    "step_number": 3,
                    "name": "Feed Your Spirit Daily",
                    "description": "Establish a consistent daily habit of reading the Bible and spending quiet time in prayer every morning."
                },
                {
                    "step_number": 4,
                    "name": "Stand as an Ambassador for Christ",
                    "description": "Represent Christian integrity in your classroom, sports field, and home, sharing God's love with friends."
                }
            ]
        },
        "kenyan_context": """### Kenyan Real-World Context & Church Fellowship

In Kenyan schools, Christian Unions (C.U.), Young Christian Students (YCS), and Seventh-day Adventist student associations provide regular weekend rallies, missions, and mentorship. 

Many national leaders, teachers, and professionals point to decisions made during their high school C.U. days as the foundation of their ethical character, proving that accepting Christ in youth sets the trajectory for a life of purpose and integrity.""",
        "youtube": {
            "title": "BibleProject: Grace and the Gospel of Salvation",
            "youtube_id": "slyevQ1LW7A",
            "description": "Understand how God's unmerited favor transforms guilty sinners into beloved children and ambassadors of His Kingdom."
        },
        "reflection": """### Spiritual Reflection & Core Values

- **Personal Commitment:** Salvation is not an inherited family tradition; it is a personal heart decision. Have you consciously responded to Christ's invitation?
- **Ambassadorship:** As Christ's ambassador, do your words, online posts, and treatment of classmates accurately reflect the loving character of Jesus?""",
        "takeaways": [
            "Salvation is God's free gift of grace received through faith in Jesus Christ, not earned through good works.",
            "Romans 10:9-10 teaches that believing in the heart and confessing with the mouth leads to justification and salvation.",
            "In Christ, believers become a 'New Creation' (2 Cor 5:17) and are appointed as His ambassadors.",
            "Salvation results in ongoing moral transformation, integrity, and joyful service in community."
        ],
        "mcq": {
            "question": "Why is biblical salvation described as a 'free gift of grace' rather than something earned through good works?",
            "options": [
                "A. Because God encourages humans to avoid hard work and discipline.",
                "B. Because no amount of human effort can erase sin; salvation is an unmerited gift of God's love received through faith in Christ.",
                "C. Because Roman law forbade citizens from paying money for religious rituals.",
                "D. Because the Apostles wanted to lower standards so that everyone would join the Church."
            ],
            "correct_answer": "B",
            "explanation": "Ephesians 2:8-9 and Romans 10:8-13 emphasize that salvation is by grace through faith so that no one can boast. Good deeds are the fruit of salvation, not its purchase price."
        }
    }
]


# ─── MAIN INGESTION WORKFLOW ──────────────────────────────────────────────────

def ingest_grade9_cre_topic11():
    print("=" * 80)
    print("STARTING INGESTION: GRADE 9 CRE — TOPIC 11: THE EARLY CHURCH")
    print("=" * 80)

    with transaction.atomic():
        # 1. Resolve Target Hierarchy
        grade = Grade.objects.get(id=18)          # Grade 9
        curriculum = grade.curriculum
        subject = Subject.objects.get(id=50, grade=grade) # CRE

        print(f"[+] Target Hierarchy Verified: {curriculum.name} (ID: {curriculum.id}) -> {grade.name} (ID: {grade.id}) -> {subject.name} (ID: {subject.id})")

        # 2. Resolve / Create Topic 11
        topic, created = Topic.objects.get_or_create(
            subject=subject,
            order=11,
            defaults={
                "name": "The Early Church",
                "description": "Examine the birth and expansion of the Early Church, apostolic miracles, persecutions, and the contemporary call to salvation."
            }
        )
        if not created and topic.name != "The Early Church":
            topic.name = "The Early Church"
            topic.description = "Examine the birth and expansion of the Early Church, apostolic miracles, persecutions, and the contemporary call to salvation."
            topic.save()

        print(f"[+] Target Topic  : Order {topic.order} — '{topic.name}' (ID: {topic.id})")

        # 3. Clean existing LearningUnits/Lessons under Topic 11 for idempotent ingestion
        existing_units = LearningUnit.objects.filter(topic=topic)
        print(f"[*] Found {existing_units.count()} existing Learning Units under Topic 11. Purging for clean ingestion...")
        for u in existing_units:
            # Delete lessons and blocks
            for l in u.lessons.all():
                l.blocks.all().delete()
                l.assets.all().delete()
                l.delete()
            u.delete()

        # 4. Ingest all 8 Lessons
        total_units = 0
        total_lessons = 0
        total_pages = 0
        total_blocks = 0
        total_assets = 0

        for cfg in LESSONS_DATA:
            u_order = cfg["order"]
            l_title = cfg["title"]
            l_desc = cfg["description"]

            # Create LearningUnit
            unit = LearningUnit.objects.create(
                topic=topic,
                order=u_order,
                name=f"Unit {u_order}: {l_title}",
                description=clean_text(l_desc)
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
                    "topic_order": 11,
                    "topic_name": topic.name,
                    "unit_order": u_order,
                    "author": "VLearn Grade 9 CRE Ingestion Engine",
                    "curriculum_framework": "CBC Kenya",
                    "enrichment_version": "v3_pedagogical"
                }
            )
            total_lessons += 1

            # ───────────────────────────────────────────────────────────────────
            # LESSON ASSETS (3 Assets: Image, Diagram, YouTube)
            # ───────────────────────────────────────────────────────────────────
            # Asset 1: Curated Wikimedia Visual Hook Image
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
                url=f"https://vlearn.africa/assets/diagrams/cre/grade9_topic_11_lesson_{u_order}.svg",
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
            print(f"  [+] Ingested Lesson {u_order:02d}/8: '{l_title}' (6 cards/pages, 13 blocks, 3 LessonAssets)")

        print("=" * 80)
        print("INGESTION SUMMARY FOR GRADE 9 CRE TOPIC 11:")
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
    ingest_grade9_cre_topic11()
