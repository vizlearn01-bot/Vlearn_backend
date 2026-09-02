"""
VLearn CBC Grade 9 CRE — Topic 8: Nicodemus' Encounter with Jesus Christ
Production-Ready Ingestion & Visual Enrichment Engine

Curriculum: CBC
Grade: Grade 9 (ID: 18)
Subject: CRE (ID: 50)
Topic: Topic 8: Nicodemus' Encounter with Jesus Christ (Order: 8)

6 Discrete Units / Published Lessons:
  1. The Identity of Nicodemus (John 3:1-2)
  2. Born Again: Rebirth of Water and the Spirit (John 3:3-8)
  3. The Bronze Serpent and Jesus' Mission (Numbers 21:4-9, John 3:14-15)
  4. God's Perfect Gift of Love (John 3:16-21)
  5. Nicodemus' Transformation (John 7:50-52, John 19:38-42)
  6. Overcoming Spiritual Pride and Showmanship Today (Matthew 6:1-6, James 4:6)

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
    <linearGradient id="blueGrad1" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#0284c7"/>
      <stop offset="100%" stop-color="#0369a1"/>
    </linearGradient>
  </defs>
  <rect width="800" height="450" fill="url(#bg1)" rx="14"/>
  <rect x="15" y="15" width="770" height="420" fill="none" stroke="#334155" stroke-width="1.5" stroke-dasharray="6 4" rx="10"/>

  <text x="400" y="45" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="17" font-weight="700" text-anchor="middle">THE WORLD &amp; IDENTITY OF NICODEMUS (JOHN 3:1-2)</text>
  <text x="400" y="68" fill="#94a3b8" font-family="system-ui, sans-serif" font-size="12" text-anchor="middle">Analyzing High Social Status, Religious Power, and the Sincere Night Encounter</text>

  <!-- Central Hub: Nicodemus -->
  <rect x="290" y="92" width="220" height="68" rx="12" fill="url(#goldGrad1)" stroke="#fbbf24" stroke-width="2"/>
  <text x="400" y="120" fill="#0f172a" font-family="system-ui, sans-serif" font-size="15" font-weight="800" text-anchor="middle">NICODEMUS</text>
  <text x="400" y="140" fill="#1e293b" font-family="system-ui, sans-serif" font-size="11.5" font-weight="600" text-anchor="middle">Pharisee &amp; Ruler of the Jews</text>

  <!-- Connecting Lines -->
  <line x1="320" y1="160" x2="155" y2="200" stroke="#38bdf8" stroke-width="2" stroke-dasharray="4 3"/>
  <line x1="400" y1="160" x2="400" y2="200" stroke="#38bdf8" stroke-width="2" stroke-dasharray="4 3"/>
  <line x1="480" y1="160" x2="645" y2="200" stroke="#38bdf8" stroke-width="2" stroke-dasharray="4 3"/>

  <!-- 3 Facets of Nicodemus -->
  <!-- Pillar 1: Religious & Political Rank -->
  <g transform="translate(40, 200)">
    <rect width="230" height="195" rx="10" fill="#1e293b" stroke="#38bdf8" stroke-width="1.5"/>
    <rect width="230" height="34" rx="10" fill="#0284c7"/>
    <text x="115" y="22" fill="#ffffff" font-family="system-ui, sans-serif" font-size="12" font-weight="700" text-anchor="middle">1. HIGH SOCIAL RANK</text>
    <text x="15" y="58" fill="#f8fafc" font-family="system-ui, sans-serif" font-size="11" font-weight="700">• Member of Sanhedrin</text>
    <text x="15" y="74" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10">Part of the supreme 71-member</text>
    <text x="15" y="88" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10">Jewish council of elders.</text>
    <text x="15" y="112" fill="#f8fafc" font-family="system-ui, sans-serif" font-size="11" font-weight="700">• Respected Pharisee</text>
    <text x="15" y="128" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10">Strict observer and teacher of</text>
    <text x="15" y="142" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10">the Mosaic Law and oral code.</text>
    <text x="15" y="166" fill="#7dd3fc" font-family="system-ui, sans-serif" font-size="10" font-weight="600">High prestige at stake!</text>
  </g>

  <!-- Pillar 2: The Night Visit Dynamics -->
  <g transform="translate(285, 200)">
    <rect width="230" height="195" rx="10" fill="#1e293b" stroke="#f59e0b" stroke-width="1.5"/>
    <rect width="230" height="34" rx="10" fill="#d97706"/>
    <text x="115" y="22" fill="#ffffff" font-family="system-ui, sans-serif" font-size="12" font-weight="700" text-anchor="middle">2. THE NIGHT VISIT</text>
    <text x="15" y="58" fill="#f8fafc" font-family="system-ui, sans-serif" font-size="11" font-weight="700">• Fear of Peers</text>
    <text x="15" y="74" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10">Avoided hostility &amp; mockery</text>
    <text x="15" y="88" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10">from anti-Jesus Pharisees.</text>
    <text x="15" y="112" fill="#f8fafc" font-family="system-ui, sans-serif" font-size="11" font-weight="700">• Quiet Dialogue</text>
    <text x="15" y="128" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10">Escaped bustling crowds to</text>
    <text x="15" y="142" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10">have deep private discussion.</text>
    <text x="15" y="166" fill="#fde68a" font-family="system-ui, sans-serif" font-size="10" font-weight="600">Privacy for honest questions</text>
  </g>

  <!-- Pillar 3: Respect & Sincerity -->
  <g transform="translate(530, 200)">
    <rect width="230" height="195" rx="10" fill="#1e293b" stroke="#34d399" stroke-width="1.5"/>
    <rect width="230" height="34" rx="10" fill="#059669"/>
    <text x="115" y="22" fill="#ffffff" font-family="system-ui, sans-serif" font-size="12" font-weight="700" text-anchor="middle">3. SINCERE APPROACH</text>
    <text x="15" y="58" fill="#f8fafc" font-family="system-ui, sans-serif" font-size="11" font-weight="700">• Called Him "Rabbi"</text>
    <text x="15" y="74" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10">Acknowledged Jesus as an</text>
    <text x="15" y="88" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10">authentic Teacher from God.</text>
    <text x="15" y="112" fill="#f8fafc" font-family="system-ui, sans-serif" font-size="11" font-weight="700">• Recognized Signs</text>
    <text x="15" y="128" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10">Admitted no one could do</text>
    <text x="15" y="142" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10">such miracles without God.</text>
    <text x="15" y="166" fill="#a7f3d0" font-family="system-ui, sans-serif" font-size="10" font-weight="600">Sincerity over cynicism</text>
  </g>

  <text x="400" y="422" fill="#64748b" font-family="system-ui, sans-serif" font-size="10" text-anchor="middle">LESSON AXIOM: GENUINE SEARCH FOR TRUTH OVERCOMES SOCIAL PRESTIGE AND PEER PRESSURE</text>
</svg>"""


def get_svg_lesson_2():
    return """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 450" width="100%" height="100%">
  <defs>
    <linearGradient id="bg2" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#0f172a"/>
      <stop offset="50%" stop-color="#1e293b"/>
      <stop offset="100%" stop-color="#0f172a"/>
    </linearGradient>
    <linearGradient id="waterGrad2" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#0284c7"/>
      <stop offset="100%" stop-color="#06b6d4"/>
    </linearGradient>
    <linearGradient id="spiritGrad2" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#8b5cf6"/>
      <stop offset="100%" stop-color="#ec4899"/>
    </linearGradient>
  </defs>
  <rect width="800" height="450" fill="url(#bg2)" rx="14"/>
  <rect x="15" y="15" width="770" height="420" fill="none" stroke="#334155" stroke-width="1.5" stroke-dasharray="6 4" rx="10"/>

  <text x="400" y="45" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="17" font-weight="700" text-anchor="middle">BORN AGAIN: REBIRTH OF WATER AND THE SPIRIT (JOHN 3:3-8)</text>
  <text x="400" y="68" fill="#94a3b8" font-family="system-ui, sans-serif" font-size="12" text-anchor="middle">Contrasting Physical Birth (Flesh) with Spiritual Regeneration (Pneuma)</text>

  <!-- Left: Physical Birth (Flesh) -->
  <g transform="translate(40, 95)">
    <rect width="210" height="295" rx="10" fill="#1e293b" stroke="#ef4444" stroke-width="1.5"/>
    <rect width="210" height="34" rx="10" fill="#dc2626"/>
    <text x="105" y="23" fill="#ffffff" font-family="system-ui, sans-serif" font-size="12" font-weight="700" text-anchor="middle">PHYSICAL BIRTH (FLESH)</text>

    <text x="15" y="62" fill="#fca5a5" font-family="system-ui, sans-serif" font-size="11" font-weight="700">• Biological Origin</text>
    <text x="15" y="80" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10">Born from human parents</text>
    <text x="15" y="95" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10">into earthly realm.</text>

    <text x="15" y="125" fill="#fca5a5" font-family="system-ui, sans-serif" font-size="11" font-weight="700">• Inherited Sin Nature</text>
    <text x="15" y="143" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10">Subject to decay, moral</text>
    <text x="15" y="158" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10">weakness, and death.</text>

    <text x="15" y="188" fill="#fca5a5" font-family="system-ui, sans-serif" font-size="11" font-weight="700">• Literal Misunderstanding</text>
    <text x="15" y="206" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10">Nicodemus asked: "Can one</text>
    <text x="15" y="221" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10">re-enter mother's womb?"</text>

    <rect x="15" y="245" width="180" height="32" rx="6" fill="#0f172a" stroke="#ef4444" stroke-width="1"/>
    <text x="105" y="265" fill="#fca5a5" font-family="system-ui, sans-serif" font-size="10" font-weight="700" text-anchor="middle">Flesh produces flesh (v.6)</text>
  </g>

  <!-- Center: The Divine Agent (Water & Spirit) -->
  <g transform="translate(265, 95)">
    <rect width="240" height="295" rx="10" fill="#1e293b" stroke="#38bdf8" stroke-width="1.5"/>
    <rect width="240" height="34" rx="10" fill="#0284c7"/>
    <text x="120" y="23" fill="#ffffff" font-family="system-ui, sans-serif" font-size="12" font-weight="700" text-anchor="middle">WATER &amp; THE SPIRIT</text>

    <!-- Water Box -->
    <rect x="15" y="50" width="210" height="95" rx="8" fill="url(#waterGrad2)"/>
    <text x="120" y="73" fill="#ffffff" font-family="system-ui, sans-serif" font-size="12" font-weight="800" text-anchor="middle">💧 BORN OF WATER</text>
    <text x="25" y="94" fill="#f0f9ff" font-family="system-ui, sans-serif" font-size="10.5">• Outward cleansing of sins</text>
    <text x="25" y="112" fill="#f0f9ff" font-family="system-ui, sans-serif" font-size="10.5">• Repentance &amp; Baptism</text>
    <text x="25" y="130" fill="#f0f9ff" font-family="system-ui, sans-serif" font-size="10.5">• Washing of renewal (Titus 3:5)</text>

    <!-- Spirit Box -->
    <rect x="15" y="155" width="210" height="125" rx="8" fill="url(#spiritGrad2)"/>
    <text x="120" y="178" fill="#ffffff" font-family="system-ui, sans-serif" font-size="12" font-weight="800" text-anchor="middle">🕊️ BORN OF SPIRIT</text>
    <text x="25" y="198" fill="#fdf2f8" font-family="system-ui, sans-serif" font-size="10.5">• Inward regeneration of heart</text>
    <text x="25" y="216" fill="#fdf2f8" font-family="system-ui, sans-serif" font-size="10.5">• Divine life &amp; Holy Spirit</text>
    <text x="25" y="234" fill="#fdf2f8" font-family="system-ui, sans-serif" font-size="10.5">• Wind metaphor: Invisible cause,</text>
    <text x="25" y="252" fill="#fdf2f8" font-family="system-ui, sans-serif" font-size="10.5">visible moral effects!</text>
  </g>

  <!-- Right: Spiritual Rebirth (Kingdom Life) -->
  <g transform="translate(520, 95)">
    <rect width="240" height="295" rx="10" fill="#1e293b" stroke="#34d399" stroke-width="1.5"/>
    <rect width="240" height="34" rx="10" fill="#059669"/>
    <text x="120" y="23" fill="#ffffff" font-family="system-ui, sans-serif" font-size="12" font-weight="700" text-anchor="middle">KINGDOM REBIRTH</text>

    <text x="15" y="62" fill="#6ee7b7" font-family="system-ui, sans-serif" font-size="11" font-weight="700">• New Spiritual Identity</text>
    <text x="15" y="80" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10">Adopted child of God;</text>
    <text x="15" y="95" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10">new creation in Christ.</text>

    <text x="15" y="125" fill="#6ee7b7" font-family="system-ui, sans-serif" font-size="11" font-weight="700">• Transformed Mind &amp; Will</text>
    <text x="15" y="143" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10">Desires shifted from sin</text>
    <text x="15" y="158" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10">to righteousness and love.</text>

    <text x="15" y="188" fill="#6ee7b7" font-family="system-ui, sans-serif" font-size="11" font-weight="700">• Entry into God's Kingdom</text>
    <text x="15" y="206" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10">Ability to see, enter, and</text>
    <text x="15" y="221" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10">enjoy eternal life now.</text>

    <rect x="15" y="245" width="210" height="32" rx="6" fill="#0f172a" stroke="#34d399" stroke-width="1"/>
    <text x="120" y="265" fill="#6ee7b7" font-family="system-ui, sans-serif" font-size="10" font-weight="700" text-anchor="middle">Spirit produces spirit (v.6)</text>
  </g>

  <text x="400" y="422" fill="#64748b" font-family="system-ui, sans-serif" font-size="10" text-anchor="middle">THEOLOGICAL TRUTH: SALVATION REQUIRES A COMPLETE SUPERNATURAL REBIRTH BY GOD'S SPIRIT</text>
</svg>"""


def get_svg_lesson_3():
    return """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 450" width="100%" height="100%">
  <defs>
    <linearGradient id="bg3" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#0f172a"/>
      <stop offset="50%" stop-color="#1e293b"/>
      <stop offset="100%" stop-color="#0f172a"/>
    </linearGradient>
    <linearGradient id="bronzeGrad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#b45309"/>
      <stop offset="100%" stop-color="#78350f"/>
    </linearGradient>
    <linearGradient id="crossGrad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#0284c7"/>
      <stop offset="100%" stop-color="#1e40af"/>
    </linearGradient>
  </defs>
  <rect width="800" height="450" fill="url(#bg3)" rx="14"/>
  <rect x="15" y="15" width="770" height="420" fill="none" stroke="#334155" stroke-width="1.5" stroke-dasharray="6 4" rx="10"/>

  <text x="400" y="45" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="17" font-weight="700" text-anchor="middle">TYPOLOGY OF DELIVERANCE: BRONZE SERPENT &amp; THE CROSS</text>
  <text x="400" y="68" fill="#94a3b8" font-family="system-ui, sans-serif" font-size="12" text-anchor="middle">Comparing Numbers 21:4-9 (Old Testament Shadow) with John 3:14-15 (New Covenant Substance)</text>

  <!-- Left: The Old Testament Shadow (Wilderness) -->
  <g transform="translate(40, 95)">
    <rect width="330" height="295" rx="10" fill="#1e293b" stroke="#f59e0b" stroke-width="1.5"/>
    <rect width="330" height="34" rx="10" fill="url(#bronzeGrad)"/>
    <text x="165" y="23" fill="#ffffff" font-family="system-ui, sans-serif" font-size="12.5" font-weight="700" text-anchor="middle">OLD COVENANT: MOSES &amp; BRONZE SERPENT</text>

    <!-- Point 1: Crisis -->
    <text x="15" y="60" fill="#fde68a" font-family="system-ui, sans-serif" font-size="11" font-weight="700">1. Deadly Crisis (Numbers 21:4-6)</text>
    <text x="15" y="76" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10">Rebellion, complaining; venomous snakes bit</text>
    <text x="15" y="90" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10">the people resulting in widespread physical death.</text>

    <!-- Point 2: Lifted Up -->
    <text x="15" y="118" fill="#fde68a" font-family="system-ui, sans-serif" font-size="11" font-weight="700">2. Raised on a Wooden Pole (Numbers 21:8-9)</text>
    <text x="15" y="134" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10">Moses cast a bronze snake (image of curse) and</text>
    <text x="15" y="148" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10">lifted it up high in the center of the camp.</text>

    <!-- Point 3: Simple Act of Faith -->
    <text x="15" y="176" fill="#fde68a" font-family="system-ui, sans-serif" font-size="11" font-weight="700">3. Simple Act of Obedient Faith</text>
    <text x="15" y="192" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10">Anyone who looked upon the bronze serpent</text>
    <text x="15" y="206" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10">believing God's promise was healed physically.</text>

    <!-- Result Banner -->
    <rect x="15" y="235" width="300" height="42" rx="6" fill="#0f172a" stroke="#f59e0b" stroke-width="1"/>
    <text x="165" y="253" fill="#fbbf24" font-family="system-ui, sans-serif" font-size="10.5" font-weight="700" text-anchor="middle">Physical Deliverance from Snake Venom</text>
    <text x="165" y="268" fill="#94a3b8" font-family="system-ui, sans-serif" font-size="9.5" text-anchor="middle">Temporary preservation of mortal earthly life</text>
  </g>

  <!-- Center Arrow -->
  <g transform="translate(378, 220)">
    <path d="M 0 15 L 30 15 L 30 5 L 45 20 L 30 35 L 30 25 L 0 25 Z" fill="#38bdf8"/>
    <text x="22" y="50" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="9" font-weight="700" text-anchor="middle">PROPHETIC</text>
    <text x="22" y="62" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="9" font-weight="700" text-anchor="middle">FULFILLMENT</text>
  </g>

  <!-- Right: The New Covenant Substance (Calvary) -->
  <g transform="translate(430, 95)">
    <rect width="330" height="295" rx="10" fill="#1e293b" stroke="#38bdf8" stroke-width="1.5"/>
    <rect width="330" height="34" rx="10" fill="url(#crossGrad)"/>
    <text x="165" y="23" fill="#ffffff" font-family="system-ui, sans-serif" font-size="12.5" font-weight="700" text-anchor="middle">NEW COVENANT: JESUS &amp; THE CROSS</text>

    <!-- Point 1: Universal Crisis -->
    <text x="15" y="60" fill="#7dd3fc" font-family="system-ui, sans-serif" font-size="11" font-weight="700">1. Universal Fatal Poison of Sin (Rom 3:23)</text>
    <text x="15" y="76" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10">All humanity bitten by the poison of sin,</text>
    <text x="15" y="90" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10">facing eternal spiritual separation from God.</text>

    <!-- Point 2: Lifted Up -->
    <text x="15" y="118" fill="#7dd3fc" font-family="system-ui, sans-serif" font-size="11" font-weight="700">2. Lifted Up on the Cross (John 3:14)</text>
    <text x="15" y="134" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10">Jesus, who knew no sin, became sin for us and</text>
    <text x="15" y="148" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10">was lifted up on the cross outside Jerusalem.</text>

    <!-- Point 3: Saving Faith -->
    <text x="15" y="176" fill="#7dd3fc" font-family="system-ui, sans-serif" font-size="11" font-weight="700">3. Spiritual Faith in Jesus Christ</text>
    <text x="15" y="192" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10">Whoever turns their heart to Jesus in trusting faith</text>
    <text x="15" y="206" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10">is cleansed, forgiven, and granted eternal life.</text>

    <!-- Result Banner -->
    <rect x="15" y="235" width="300" height="42" rx="6" fill="#0f172a" stroke="#38bdf8" stroke-width="1"/>
    <text x="165" y="253" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="10.5" font-weight="700" text-anchor="middle">Eternal Spiritual Deliverance from Sin</text>
    <text x="165" y="268" fill="#6ee7b7" font-family="system-ui, sans-serif" font-size="9.5" text-anchor="middle">Permanent eternal life and fellowship with God</text>
  </g>

  <text x="400" y="422" fill="#64748b" font-family="system-ui, sans-serif" font-size="10" text-anchor="middle">JOHN 3:14-15: "JUST AS MOSES LIFTED UP THE SNAKE IN THE WILDERNESS, SO THE SON OF MAN MUST BE LIFTED UP"</text>
</svg>"""


def get_svg_lesson_4():
    return """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 450" width="100%" height="100%">
  <defs>
    <linearGradient id="bg4" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#0f172a"/>
      <stop offset="50%" stop-color="#1e293b"/>
      <stop offset="100%" stop-color="#0f172a"/>
    </linearGradient>
    <linearGradient id="goldPillar" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#f59e0b"/>
      <stop offset="100%" stop-color="#d97706"/>
    </linearGradient>
  </defs>
  <rect width="800" height="450" fill="url(#bg4)" rx="14"/>
  <rect x="15" y="15" width="770" height="420" fill="none" stroke="#334155" stroke-width="1.5" stroke-dasharray="6 4" rx="10"/>

  <text x="400" y="44" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="17" font-weight="700" text-anchor="middle">ANATOMY OF JOHN 3:16: GOD'S PERFECT GIFT OF LOVE</text>
  <text x="400" y="66" fill="#94a3b8" font-family="system-ui, sans-serif" font-size="12" text-anchor="middle">Deconstructing the Four Life-Giving Pillars of the Gospel in Miniature</text>

  <!-- 4 Quadrants/Pillars of John 3:16 -->
  <!-- Pillar 1: The Divine Motivation -->
  <g transform="translate(35, 90)">
    <rect width="170" height="295" rx="10" fill="#1e293b" stroke="#ec4899" stroke-width="1.5"/>
    <rect width="170" height="34" rx="10" fill="#db2777"/>
    <text x="85" y="22" fill="#ffffff" font-family="system-ui, sans-serif" font-size="11.5" font-weight="700" text-anchor="middle">1. MOTIVATION</text>

    <text x="12" y="60" fill="#f472b6" font-family="system-ui, sans-serif" font-size="11" font-weight="700">"For God so loved..."</text>
    <text x="12" y="82" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10">• **Agape Love:**</text>
    <text x="12" y="98" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10">Unconditional, active,</text>
    <text x="12" y="112" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10">sacrificial commitment.</text>

    <text x="12" y="138" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10">• **The World (Kosmos):**</text>
    <text x="12" y="154" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10">Not just one tribe or race;</text>
    <text x="12" y="168" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10">embraces all humanity.</text>

    <rect x="10" y="200" width="150" height="75" rx="6" fill="#0f172a" stroke="#db2777" stroke-width="1"/>
    <text x="85" y="220" fill="#f472b6" font-family="system-ui, sans-serif" font-size="10" font-weight="700" text-anchor="middle">CORE ATTRIBUTE</text>
    <text x="85" y="240" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="9.5" text-anchor="middle">God initiates salvation</text>
    <text x="85" y="255" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="9.5" text-anchor="middle">out of pure grace</text>
  </g>

  <!-- Pillar 2: The Sacrificial Action -->
  <g transform="translate(220, 90)">
    <rect width="170" height="295" rx="10" fill="#1e293b" stroke="#f59e0b" stroke-width="1.5"/>
    <rect width="170" height="34" rx="10" fill="#d97706"/>
    <text x="85" y="22" fill="#ffffff" font-family="system-ui, sans-serif" font-size="11.5" font-weight="700" text-anchor="middle">2. ACTION</text>

    <text x="12" y="60" fill="#fde68a" font-family="system-ui, sans-serif" font-size="11" font-weight="700">"...that He gave His Son"</text>
    <text x="12" y="82" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10">• **Ultimate Sacrifice:**</text>
    <text x="12" y="98" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10">Gave His only begotten</text>
    <text x="12" y="112" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10">Son (Monogenes).</text>

    <text x="12" y="138" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10">• **Generosity in Deed:**</text>
    <text x="12" y="154" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10">Not empty words, but</text>
    <text x="12" y="168" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10">costly demonstration.</text>

    <rect x="10" y="200" width="150" height="75" rx="6" fill="#0f172a" stroke="#d97706" stroke-width="1"/>
    <text x="85" y="220" fill="#fbbf24" font-family="system-ui, sans-serif" font-size="10" font-weight="700" text-anchor="middle">DIVINE COST</text>
    <text x="85" y="240" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="9.5" text-anchor="middle">The cross proves the</text>
    <text x="85" y="255" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="9.5" text-anchor="middle">depth of God's love</text>
  </g>

  <!-- Pillar 3: The Universal Condition -->
  <g transform="translate(405, 90)">
    <rect width="170" height="295" rx="10" fill="#1e293b" stroke="#38bdf8" stroke-width="1.5"/>
    <rect width="170" height="34" rx="10" fill="#0284c7"/>
    <text x="85" y="22" fill="#ffffff" font-family="system-ui, sans-serif" font-size="11.5" font-weight="700" text-anchor="middle">3. CONDITION</text>

    <text x="12" y="60" fill="#7dd3fc" font-family="system-ui, sans-serif" font-size="11" font-weight="700">"...whoever believes"</text>
    <text x="12" y="82" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10">• **Open to Whoever:**</text>
    <text x="12" y="98" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10">No tribal, social, or</text>
    <text x="12" y="112" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10">economic barriers.</text>

    <text x="12" y="138" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10">• **Faith (Pistis):**</text>
    <text x="12" y="154" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10">Trusting Jesus as Lord</text>
    <text x="12" y="168" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10">and personal Savior.</text>

    <rect x="10" y="200" width="150" height="75" rx="6" fill="#0f172a" stroke="#0284c7" stroke-width="1"/>
    <text x="85" y="220" fill="#7dd3fc" font-family="system-ui, sans-serif" font-size="10" font-weight="700" text-anchor="middle">UNIVERSAL INVITATION</text>
    <text x="85" y="240" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="9.5" text-anchor="middle">Salvation through faith,</text>
    <text x="85" y="255" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="9.5" text-anchor="middle">not legalistic ritual</text>
  </g>

  <!-- Pillar 4: The Promise -->
  <g transform="translate(590, 90)">
    <rect width="175" height="295" rx="10" fill="#1e293b" stroke="#34d399" stroke-width="1.5"/>
    <rect width="175" height="34" rx="10" fill="#059669"/>
    <text x="87" y="22" fill="#ffffff" font-family="system-ui, sans-serif" font-size="11.5" font-weight="700" text-anchor="middle">4. PROMISE</text>

    <text x="12" y="60" fill="#6ee7b7" font-family="system-ui, sans-serif" font-size="11" font-weight="700">"...have eternal life"</text>
    <text x="12" y="82" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10">• **Not Perishing:**</text>
    <text x="12" y="98" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10">Rescued from judgment</text>
    <text x="12" y="112" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10">and eternal death.</text>

    <text x="12" y="138" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10">• **Zoe Aionios:**</text>
    <text x="12" y="154" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10">Qualitative life of joy,</text>
    <text x="12" y="168" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10">peace, and eternal hope.</text>

    <rect x="10" y="200" width="155" height="75" rx="6" fill="#0f172a" stroke="#059669" stroke-width="1"/>
    <text x="87" y="220" fill="#6ee7b7" font-family="system-ui, sans-serif" font-size="10" font-weight="700" text-anchor="middle">ASSURANCE &amp; PEACE</text>
    <text x="87" y="240" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="9.5" text-anchor="middle">Sent not to condemn,</text>
    <text x="87" y="255" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="9.5" text-anchor="middle">but to save the world!</text>
  </g>

  <text x="400" y="422" fill="#64748b" font-family="system-ui, sans-serif" font-size="10" text-anchor="middle">JOHN 3:17: "FOR GOD DID NOT SEND HIS SON INTO THE WORLD TO CONDEMN THE WORLD, BUT TO SAVE THE WORLD THROUGH HIM"</text>
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

  <text x="400" y="44" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="17" font-weight="700" text-anchor="middle">THE 3-STAGE TRANSFORMATION OF NICODEMUS: FROM NIGHT TO DAYLIGHT</text>
  <text x="400" y="66" fill="#94a3b8" font-family="system-ui, sans-serif" font-size="12" text-anchor="middle">Tracing Spiritual Growth and Courage in the Gospel of John</text>

  <!-- Connecting Journey Arrow / Timeline Line -->
  <line x1="145" y1="210" x2="655" y2="210" stroke="#475569" stroke-width="3" stroke-dasharray="6 4"/>

  <!-- Stage 1: The Secret Seeker -->
  <g transform="translate(35, 95)">
    <rect width="220" height="285" rx="10" fill="#1e293b" stroke="#64748b" stroke-width="1.5"/>
    <rect width="220" height="34" rx="10" fill="#334155"/>
    <text x="110" y="23" fill="#ffffff" font-family="system-ui, sans-serif" font-size="12" font-weight="700" text-anchor="middle">STAGE 1: SECRET INQUIRER</text>

    <!-- Badge -->
    <rect x="35" y="45" width="150" height="22" rx="11" fill="#0f172a" stroke="#64748b" stroke-width="1"/>
    <text x="110" y="60" fill="#94a3b8" font-family="system-ui, sans-serif" font-size="10.5" font-weight="600" text-anchor="middle">John 3:1-2 • Night Shadows</text>

    <text x="15" y="95" fill="#f8fafc" font-family="system-ui, sans-serif" font-size="11" font-weight="700">• Spiritual Posture:</text>
    <text x="15" y="112" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10">Curious and sincere, but</text>
    <text x="15" y="126" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10">held back by fear of peers.</text>

    <text x="15" y="152" fill="#f8fafc" font-family="system-ui, sans-serif" font-size="11" font-weight="700">• Setting &amp; Risk:</text>
    <text x="15" y="169" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10">Visits Jesus under cover</text>
    <text x="15" y="183" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10">of darkness to protect rank.</text>

    <text x="15" y="210" fill="#f8fafc" font-family="system-ui, sans-serif" font-size="11" font-weight="700">• Key Virtue:</text>
    <text x="15" y="227" fill="#94a3b8" font-family="system-ui, sans-serif" font-size="10">Openness to seek the truth.</text>

    <rect x="15" y="245" width="190" height="24" rx="4" fill="#0f172a"/>
    <text x="110" y="261" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="9.5" text-anchor="middle">"Came to Jesus at night"</text>
  </g>

  <!-- Stage 2: The Fair Defender -->
  <g transform="translate(290, 95)">
    <rect width="220" height="285" rx="10" fill="#1e293b" stroke="#f59e0b" stroke-width="1.5"/>
    <rect width="220" height="34" rx="10" fill="#d97706"/>
    <text x="110" y="23" fill="#ffffff" font-family="system-ui, sans-serif" font-size="12" font-weight="700" text-anchor="middle">STAGE 2: LEGAL DEFENDER</text>

    <!-- Badge -->
    <rect x="35" y="45" width="150" height="22" rx="11" fill="#0f172a" stroke="#f59e0b" stroke-width="1"/>
    <text x="110" y="60" fill="#fde68a" font-family="system-ui, sans-serif" font-size="10.5" font-weight="600" text-anchor="middle">John 7:50-52 • The Sanhedrin</text>

    <text x="15" y="95" fill="#f8fafc" font-family="system-ui, sans-serif" font-size="11" font-weight="700">• Spiritual Posture:</text>
    <text x="15" y="112" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10">Growing confidence; stands</text>
    <text x="15" y="126" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10">up for fairness and justice.</text>

    <text x="15" y="152" fill="#f8fafc" font-family="system-ui, sans-serif" font-size="11" font-weight="700">• Setting &amp; Risk:</text>
    <text x="15" y="169" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10">Challenges illegal plots;</text>
    <text x="15" y="183" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10">endures mockery from council.</text>

    <text x="15" y="210" fill="#f8fafc" font-family="system-ui, sans-serif" font-size="11" font-weight="700">• Key Virtue:</text>
    <text x="15" y="227" fill="#fbbf24" font-family="system-ui, sans-serif" font-size="10">Moral courage for justice.</text>

    <rect x="15" y="245" width="190" height="24" rx="4" fill="#0f172a"/>
    <text x="110" y="261" fill="#fde68a" font-family="system-ui, sans-serif" font-size="9.5" text-anchor="middle">"Does law judge without hearing?"</text>
  </g>

  <!-- Stage 3: The Bold Disciple -->
  <g transform="translate(545, 95)">
    <rect width="220" height="285" rx="10" fill="#1e293b" stroke="#34d399" stroke-width="2"/>
    <rect width="220" height="34" rx="10" fill="#059669"/>
    <text x="110" y="23" fill="#ffffff" font-family="system-ui, sans-serif" font-size="12" font-weight="700" text-anchor="middle">STAGE 3: BOLD DISCIPLE</text>

    <!-- Badge -->
    <rect x="35" y="45" width="150" height="22" rx="11" fill="#0f172a" stroke="#34d399" stroke-width="1"/>
    <text x="110" y="60" fill="#6ee7b7" font-family="system-ui, sans-serif" font-size="10.5" font-weight="600" text-anchor="middle">John 19:38-42 • Broad Daylight</text>

    <text x="15" y="95" fill="#f8fafc" font-family="system-ui, sans-serif" font-size="11" font-weight="700">• Spiritual Posture:</text>
    <text x="15" y="112" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10">Full public loyalty and</text>
    <text x="15" y="126" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10">devotion to the crucified King.</text>

    <text x="15" y="152" fill="#f8fafc" font-family="system-ui, sans-serif" font-size="11" font-weight="700">• Setting &amp; Risk:</text>
    <text x="15" y="169" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10">Brings 75 lbs of royal spices;</text>
    <text x="15" y="183" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10">honors Jesus when others fled.</text>

    <text x="15" y="210" fill="#f8fafc" font-family="system-ui, sans-serif" font-size="11" font-weight="700">• Key Virtue:</text>
    <text x="15" y="227" fill="#34d399" font-family="system-ui, sans-serif" font-size="10">Extravagant, fearless love.</text>

    <rect x="15" y="245" width="190" height="24" rx="4" fill="#0f172a"/>
    <text x="110" y="261" fill="#6ee7b7" font-family="system-ui, sans-serif" font-size="9.5" text-anchor="middle">"Brought myrrh &amp; aloes for burial"</text>
  </g>

  <text x="400" y="422" fill="#64748b" font-family="system-ui, sans-serif" font-size="10" text-anchor="middle">DISCIPLESHIP TRUTH: TRUE FAITH IS A PROGRESSIVE JOURNEY THAT MATURES FROM FEAR INTO PUBLIC COURAGE</text>
</svg>"""


def get_svg_lesson_6():
    return """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 450" width="100%" height="100%">
  <defs>
    <linearGradient id="bg6" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#0f172a"/>
      <stop offset="50%" stop-color="#1e293b"/>
      <stop offset="100%" stop-color="#0f172a"/>
    </linearGradient>
  </defs>
  <rect width="800" height="450" fill="url(#bg6)" rx="14"/>
  <rect x="15" y="15" width="770" height="420" fill="none" stroke="#334155" stroke-width="1.5" stroke-dasharray="6 4" rx="10"/>

  <text x="400" y="44" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="17" font-weight="700" text-anchor="middle">SPIRITUAL SHOWMANSHIP VS SINCERE HUMILITY</text>
  <text x="400" y="66" fill="#94a3b8" font-family="system-ui, sans-serif" font-size="12" text-anchor="middle">Matthew 6:1-6 &amp; James 4:6 — Cultivating Heart Integrity and Secret Service</text>

  <!-- Left: Spiritual Pride & Showmanship (Hypocrisy) -->
  <g transform="translate(40, 95)">
    <rect width="335" height="295" rx="10" fill="#1e293b" stroke="#ef4444" stroke-width="1.5"/>
    <rect width="335" height="34" rx="10" fill="#dc2626"/>
    <text x="167" y="23" fill="#ffffff" font-family="system-ui, sans-serif" font-size="12" font-weight="700" text-anchor="middle">SPIRITUAL PRIDE &amp; SHOWMANSHIP</text>

    <!-- Point 1: Motivation -->
    <text x="15" y="62" fill="#fca5a5" font-family="system-ui, sans-serif" font-size="11" font-weight="700">• Motivation: Seeking Human Applause</text>
    <text x="15" y="78" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10">Performing prayers, charity, or leadership duties</text>
    <text x="15" y="92" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10">primarily to be seen, praised, and admired by others.</text>

    <!-- Point 2: Behavior -->
    <text x="15" y="120" fill="#fca5a5" font-family="system-ui, sans-serif" font-size="11" font-weight="700">• Attitude: Self-Righteous Judgment</text>
    <text x="15" y="136" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10">Believing one is spiritually superior; looking</text>
    <text x="15" y="150" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10">down on struggling classmates or moral failures.</text>

    <!-- Point 3: Reward -->
    <text x="15" y="178" fill="#fca5a5" font-family="system-ui, sans-serif" font-size="11" font-weight="700">• Spiritual Reality: Hollow &amp; Temporary</text>
    <text x="15" y="194" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10">"They have received their reward in full" (Matt 6:2).</text>
    <text x="15" y="208" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10">God opposes the proud (James 4:6).</text>

    <rect x="15" y="240" width="305" height="36" rx="6" fill="#0f172a" stroke="#ef4444" stroke-width="1"/>
    <text x="167" y="262" fill="#fca5a5" font-family="system-ui, sans-serif" font-size="10" font-weight="700" text-anchor="middle">❌ "Beware of practicing your righteousness to be seen"</text>
  </g>

  <!-- Right: Sincere Humility & Secret Service (Integrity) -->
  <g transform="translate(425, 95)">
    <rect width="335" height="295" rx="10" fill="#1e293b" stroke="#34d399" stroke-width="1.5"/>
    <rect width="335" height="34" rx="10" fill="#059669"/>
    <text x="167" y="23" fill="#ffffff" font-family="system-ui, sans-serif" font-size="12" font-weight="700" text-anchor="middle">SINCERE HUMILITY &amp; SECRET SERVICE</text>

    <!-- Point 1: Motivation -->
    <text x="15" y="62" fill="#6ee7b7" font-family="system-ui, sans-serif" font-size="11" font-weight="700">• Motivation: Pleasing God in Secret</text>
    <text x="15" y="78" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10">Serving others quietly without blowing trumpets</text>
    <text x="15" y="92" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10">or boasting on social media (Matthew 6:3-4).</text>

    <!-- Point 2: Behavior -->
    <text x="15" y="120" fill="#6ee7b7" font-family="system-ui, sans-serif" font-size="11" font-weight="700">• Attitude: Honest Brokenness &amp; Grace</text>
    <text x="15" y="136" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10">Acknowledging personal flaws; showing empathy,</text>
    <text x="15" y="150" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10">mercy, and support to struggling peers.</text>

    <!-- Point 3: Reward -->
    <text x="15" y="178" fill="#6ee7b7" font-family="system-ui, sans-serif" font-size="11" font-weight="700">• Spiritual Reality: Eternal Divine Favor</text>
    <text x="15" y="194" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10">"Your Father who sees in secret will reward you."</text>
    <text x="15" y="208" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10">God gives grace to the humble (James 4:6).</text>

    <rect x="15" y="240" width="305" height="36" rx="6" fill="#0f172a" stroke="#34d399" stroke-width="1"/>
    <text x="167" y="262" fill="#6ee7b7" font-family="system-ui, sans-serif" font-size="10" font-weight="700" text-anchor="middle">✓ "Your Father who sees what is done in secret will reward you"</text>
  </g>

  <text x="400" y="422" fill="#64748b" font-family="system-ui, sans-serif" font-size="10" text-anchor="middle">CHRISTIAN VIRTUE: INTEGRITY IS BEING THE EXACT SAME RIGHTEOUS PERSON IN THE SECRET DARK AS IN THE LIGHT</text>
</svg>"""


# ─── LESSON DATA CONFIGURATIONS (6 LESSONS) ───────────────────────────────────

LESSONS_DATA = [
    # ─── LESSON 1 ────────────────────────────────────────────────────────────
    {
        "unit_order": 1,
        "unit_name": "The Identity of Nicodemus",
        "unit_description": "Examine Nicodemus' background, his political and religious status in the Sanhedrin, and analyze why he chose to visit Jesus under the cover of night.",
        "lesson_title": "The Identity of Nicodemus",
        "image": {
            "url": "https://upload.wikimedia.org/wikipedia/commons/thumb/e/e4/William_Hole_Nicodemus_comes_to_Jesus_by_night.jpg/800px-William_Hole_Nicodemus_comes_to_Jesus_by_night.jpg",
            "title": "Visual Hook: Nicodemus Comes to Jesus by Night",
            "author": "William Hole (1846–1917)",
            "licensing": "Public Domain",
            "source": "Wikimedia Commons",
            "caption": "Nicodemus visiting Jesus secretly at night in Jerusalem, seeking spiritual truth while wrestling with the fear of his fellow Sanhedrin authorities."
        },
        "youtube": {
            "youtube_id": "G-2e9mMf7E8",
            "title": "BibleProject: Gospel of John (Part 1 - John 1-12)",
            "description": "An animated overview of John chapters 1-12, exploring Jesus' identity, His signs, and His intimate dialogue with Nicodemus about the Kingdom of God."
        },
        "svg_fn": get_svg_lesson_1,
        "goals": [
            "Describe the religious and political background of Nicodemus as a Pharisee and member of the Sanhedrin.",
            "Analyze the reasons why Nicodemus chose to visit Jesus secretly at night rather than in broad daylight.",
            "Evaluate the difference between peer pressure and sincere truth-seeking in personal and school life."
        ],
        "intro": "Have you ever wanted to ask a teacher, parent, or elder a very serious question, but hesitated because you feared your classmates might laugh at you, mock your questions, or label you a 'know-it-all'? You probably waited until after class when everyone had gone home to approach the teacher in private.\n\nNicodemus, a highly respected, powerful, and wealthy leader in first-century Jerusalem, experienced this exact inner conflict. He desperately wanted to know the truth about Jesus' divine authority, but his high reputation, social standing, and political career were all on the line.",
        "core_scripture": "### Scriptural Passage: John 3:1-2\n\n> *\"Now there was a Pharisee, a man named Nicodemus who was a member of the Jewish ruling council. He came to Jesus at night and said, 'Rabbi, we know that you are a teacher who has come from God. For no one could perform the signs you are doing if God were not with him.'\"*\n\nThis passage introduces Nicodemus as both a Pharisee and a prominent ruler of the Jews. His title and opening greeting reveal both his high social standing and his profound curiosity regarding Jesus' miracles.",
        "theological_pillars": "### Theological & Historical Dimensions of Nicodemus' Identity\n\n1. **Pharisee and Legal Expert:** The Pharisees were an influential religious party renowned for their meticulous, strict adherence to the Mosaic Law and oral traditions. While many Pharisees opposed Jesus, Nicodemus demonstrated genuine intellectual and spiritual curiosity.\n2. **Member of the Sanhedrin:** The Sanhedrin was the supreme Jewish religious, legislative, and judicial council consisting of 71 elders, chief priests, and scribes. Membership conferred immense prestige, judicial power, and social honor in Roman Judea.\n3. **The Nighttime Encounter:** Night represented both a physical concealment from hostile peers who sought to destroy Jesus, and a quiet, uninterrupted space for deep theological dialogue away from daytime crowds.\n4. **Respectful Recognition of Christ:** Nicodemus addressed Jesus as *'Rabbi'* (Master/Teacher) and acknowledged His miracles (*signs*) as undeniable proof of God's presence, distinguishing himself from religious leaders who accused Jesus of demonic sorcery.",
        "deep_dive": "### Deep Dive: Social Pressure vs Sincere Seeking\n\nNicodemus lived in a high-stakes honour-shame culture where public perception dictated a leader's survival:\n\n- **The Danger of Excommunication:** Associating with an unauthorized, itinerant teacher like Jesus could result in being expelled from the synagogue and stripped of Sanhedrin office (John 9:22).\n- **The Search for Truth:** Despite severe social risks, Nicodemus took proactive steps to investigate Christ for himself rather than relying on hearsay or prejudice.\n- **Sincerity over Cynicism:** Unlike the Pharisees who questioned Jesus to entrap Him on legal technicalities (e.g., paying taxes to Caesar or healing on the Sabbath), Nicodemus arrived with genuine questions about God's kingdom.",
        "practical": {
            "title": "Action Framework: Overcoming Peer Pressure in the Search for Truth",
            "steps": [
                "Step 1: Identify the Fear — Recognize when fear of mockery, judgment, or social isolation is stopping you from doing what is right.",
                "Step 2: Seek Truth Sincerely — Take intentional, practical steps to investigate the truth, ask questions, and seek guidance from trustworthy mentors.",
                "Step 3: Value God's Approval Above Human Applause — Shift your focus from seeking popularity to pursuing righteous character and divine integrity.",
                "Step 4: Speak Up Courageously — Progressively build the moral courage to defend the truth and protect others, even when your peers disagree."
            ]
        },
        "kenyan_context": "In Kenyan schools and youth fellowships, young people often face intense peer pressure regarding study habits, moral integrity, drug avoidance, and social media behavior. Like Nicodemus, students may initially feel intimidated to stand out from the crowd. Christian teaching encourages learners to value truth and integrity above fleeting popularity.",
        "reflection": "### Reflection on Sincerity and Peer Pressure\n\nReflect on the choices you make every day:\n- Have you ever hidden your Christian values or stayed silent when a classmate was being mistreated because you feared being excluded by the 'popular' group?\n- How does Nicodemus' courage to approach Jesus secretly at night show that God patiently welcomes all sincere seekers, even when their faith is just beginning?",
        "takeaways": [
            "Nicodemus was a prominent Pharisee and ruler of the Jews sitting on the 71-member Sanhedrin court (John 3:1).",
            "He visited Jesus at night to avoid social conflict with hostile religious peers and to secure uninterrupted dialogue with Christ.",
            "He approached Jesus respectfully as 'Rabbi' and acknowledged His miracles as divine signs (John 3:2).",
            "True discipleship begins with sincere seeking, which God nurtures and transforms into bold, public courage."
        ],
        "mcq": {
            "question": "Why did Nicodemus choose to visit Jesus at night rather than during the day?",
            "options": [
                "A) He was busy fulfilling legal court duties at the Sanhedrin all day",
                "B) He feared the hostility of fellow Jewish authorities and sought a private, quiet dialogue",
                "C) He wanted to catch Jesus while He was sleeping to surprise Him",
                "D) He did not know where Jesus resided during the daytime"
            ],
            "answer": "B",
            "explanation": "John 3:1-2 indicates that Nicodemus came at night primarily to avoid being seen by his fellow Sanhedrin members who were hostile to Jesus, while also securing a quiet environment for deep theological discussion."
        }
    },

    # ─── LESSON 2 ────────────────────────────────────────────────────────────
    {
        "unit_order": 2,
        "unit_name": "Born Again: Rebirth of Water and the Spirit",
        "unit_description": "Explain the spiritual meaning of being 'born again' of water and the Spirit, and analyze Nicodemus' literalist misunderstanding versus Jesus' spiritual teaching.",
        "lesson_title": "Born Again: Rebirth of Water and the Spirit",
        "image": {
            "url": "https://upload.wikimedia.org/wikipedia/commons/thumb/c/cd/Christ_and_Nicodemus_by_Fritz_von_Uhde.jpg/800px-Christ_and_Nicodemus_by_Fritz_von_Uhde.jpg",
            "title": "Visual Hook: Christ and Nicodemus in Theological Discussion",
            "author": "Fritz von Uhde (1848–1911)",
            "licensing": "Public Domain",
            "source": "Wikimedia Commons",
            "caption": "Jesus explaining the mystery of spiritual rebirth of water and the Spirit to Nicodemus, contrasting physical lineage with supernatural renewal."
        },
        "youtube": {
            "youtube_id": "oNNZO9i1Gjc",
            "title": "BibleProject: Holy Spirit (Ruakh)",
            "description": "Explores the biblical concept of the Holy Spirit as God's breath and wind (Ruakh / Pneuma) that brings new life, recreation, and moral transformation to humanity."
        },
        "svg_fn": get_svg_lesson_2,
        "goals": [
            "Define the theological concept of being 'born again' (spiritual regeneration) according to John 3:3-8.",
            "Explain the dual significance of being born of 'water' and the 'Spirit' in Christian theology.",
            "Contrast physical birth with spiritual rebirth using Jesus' metaphor of the wind."
        ],
        "intro": "Have you ever played a digital video game or sports match where you made so many disastrous mistakes that you desperately wished you could hit a 'Restart' or 'Reset' button to begin the entire match fresh from score zero?\n\nJesus offers the ultimate reset button for human life. When Nicodemus arrived to discuss religious scholarship, Jesus interrupted him and stated: 'You must start your entire life completely over.' Jesus revealed that entry into God's Kingdom requires an inward, spiritual rebirth rather than external heritage or legalistic perfection.",
        "core_scripture": "### Scriptural Passage: John 3:3-8\n\n> *\"Jesus replied, 'Very truly I tell you, no one can see the kingdom of God unless they are born again.'\n> 'How can someone be born when they are old?' Nicodemus asked. 'Surely they cannot enter a second time into their mother's womb to be born!'\n> Jesus answered, 'Very truly I tell you, no one can enter the kingdom of God unless they are born of water and the Spirit. Flesh gives birth to flesh, but the Spirit gives birth to spirit. You should not be surprised at my saying, \"You must be born again.\" The wind blows wherever it pleases. You hear its sound, but you cannot tell where it comes from or where it is going. So it is with everyone born of the Spirit.'\"*",
        "theological_pillars": "### Theological Foundations of Spiritual Regeneration\n\n1. **Born Again (*Anothen*):** The Greek term *anothen* carries a rich double meaning: *'born from above'* (divine origin) and *'born anew'* (spiritual restart). It signifies total regeneration of the heart.\n2. **Nicodemus' Literalist Trap:** Despite his vast scholarship, Nicodemus interpreted Jesus' metaphor strictly physically, wondering how an aged man could re-enter his mother's womb. Jesus clarified that physical lineage cannot produce spiritual life.\n3. **Born of Water:** Refers to outward repentance, moral cleansing of sins, and the Sacrament of Baptism, echoing Ezekiel 36:25 (*\"I will sprinkle clean water on you, and you will be clean\"*).\n4. **Born of the Spirit:** Refers to the inward, supernatural renewal accomplished solely by the Holy Spirit (Titus 3:5), granting believers a new heart, righteous desires, and eternal life.\n5. **The Metaphor of the Wind (*Pneuma*):** In Greek and Hebrew, *pneuma / ruakh* means breath, wind, and spirit. Like the wind, the Holy Spirit's movement is invisible to human eyes, yet His transformative power is unmistakably visible through changed lives and righteous fruit.",
        "deep_dive": "### Deep Dive: Flesh vs Spirit in Christian Living\n\nJesus clearly divided existence into two distinct realms:\n\n- **The Realm of Flesh (*Sarx*):** Natural human abilities, biological pedigree, social status, and human effort. These are mortal, limited, and cannot inherit the eternal Kingdom of God.\n- **The Realm of Spirit (*Pneuma*):** Divine grace, supernatural transformation, love, and eternal fellowship with God. Rebirth cannot be earned by observing rituals; it is received as a gift of divine grace through faith.",
        "practical": {
            "title": "Action Framework: Living Out the Reality of Spiritual Rebirth",
            "steps": [
                "Step 1: Repent Sincerely — Acknowledge past sins, selfish habits, and wrong attitudes, asking God for forgiveness and cleansing.",
                "Step 2: Surrender to the Holy Spirit — Invite the Holy Spirit to guide your daily thoughts, speech, and moral choices at home and school.",
                "Step 3: Put on the New Self — Replace destructive behaviors (gossip, cheating, laziness) with the fruits of the Spirit (love, patience, integrity).",
                "Step 4: Cultivate Spiritual Growth — Nurture your spiritual life daily through prayer, scripture study, and active fellowship in the Christian community."
            ]
        },
        "kenyan_context": "In many Kenyan communities, people often base their identity on family ancestry, clan status, or ethnic origin. Jesus' teaching on being born again reminds us that our primary and eternal identity is found in Christ. Every young person, regardless of background, has the opportunity to experience a fresh start through the Holy Spirit.",
        "reflection": "### Reflection on the Transformative Wind of the Spirit\n\nConsider how the wind works in nature:\n- You cannot touch or see the wind, but you easily see tall trees swaying, windmills turning, and dust moving. How do people around you notice the 'movement' of the Holy Spirit in your words, kindness, and actions?",
        "takeaways": [
            "Being 'born again' (born from above) is essential for seeing and entering the Kingdom of God (John 3:3, 5).",
            "Nicodemus mistakenly thought Jesus meant re-entering his mother's womb physically, missing the spiritual metaphor (John 3:4).",
            "'Born of water' represents repentance and cleansing, while 'born of the Spirit' represents supernatural heart transformation.",
            "The Holy Spirit is like the wind: invisible in operation, but unmistakably evident through righteous fruit and moral transformation."
        ],
        "mcq": {
            "question": "What did Jesus mean when He told Nicodemus that one must be 'born of water and the Spirit'?",
            "options": [
                "A) One must swim across a sacred river before participating in prayer",
                "B) One must experience biological rebirth in an earthly womb followed by physical death",
                "C) One requires spiritual cleansing through repentance/baptism and inward renewal by the Holy Spirit",
                "D) One must become a sailor and study meteorology to understand the wind"
            ],
            "answer": "C",
            "explanation": "In John 3:5, 'water' signifies repentance, cleansing of sins, and baptism, while 'Spirit' signifies the inward regeneration of the human heart and character by the Holy Spirit."
        }
    },

    # ─── LESSON 3 ────────────────────────────────────────────────────────────
    {
        "unit_order": 3,
        "unit_name": "The Bronze Serpent and Jesus' Mission",
        "unit_description": "Explain the Old Testament background of the Bronze Serpent from Numbers 21:4-9 and relate its typological significance to Jesus' crucifixion and saving mission.",
        "lesson_title": "The Bronze Serpent and Jesus' Mission",
        "image": {
            "url": "https://upload.wikimedia.org/wikipedia/commons/thumb/3/36/The_Brazen_Serpent_by_Sebastiano_Bourdon.jpg/800px-The_Brazen_Serpent_by_Sebastiano_Bourdon.jpg",
            "title": "Visual Hook: Moses and the Brazen Serpent",
            "author": "Sébastien Bourdon (1616–1671)",
            "licensing": "Public Domain",
            "source": "Wikimedia Commons",
            "caption": "Moses lifting the bronze serpent on a pole in the wilderness so that bitten, dying Israelites who look upon it in faith are healed."
        },
        "youtube": {
            "youtube_id": "tp5MI_UC6mg",
            "title": "BibleProject: The Book of Numbers",
            "description": "An animated overview of Israel's wilderness wanderings, the rebellion that brought venomous snakes, and God's provision of the bronze serpent on the pole."
        },
        "svg_fn": get_svg_lesson_3,
        "goals": [
            "Retell the historical account of the bronze serpent in the wilderness from Numbers 21:4-9.",
            "Explain the typological connection between the lifted bronze serpent and the crucifixion of Jesus Christ (John 3:14-15).",
            "Analyze how obedient faith in God brings healing and deliverance from the deadly power of sin."
        ],
        "intro": "Have you ever looked closely at an ambulance, hospital emblem, or pharmacy sign? You will often notice a serpent coiled around a wooden staff (the Rod of Asclepius). Have you ever wondered why a deadly, frightening creature like a snake is globally recognized as a symbol of healing and medicine?\n\nThis iconic imagery has profound biblical roots. During His nighttime dialogue with Nicodemus, Jesus pointed back to a dramatic Old Testament historical event in the desert to explain the very purpose of His coming sacrifice on the cross.",
        "core_scripture": "### Scriptural Passages: Numbers 21:4-9 & John 3:14-15\n\n#### Numbers 21:8-9 — The Wilderness Provision\n> *\"The Lord said to Moses, 'Make a snake and put it up on a pole; anyone who is bitten can look at it and live.' So Moses made a bronze snake and put it up on a pole. Then when anyone was bitten by a snake and looked at the bronze snake, they lived.\"*\n\n#### John 3:14-15 — The New Covenant Fulfillment\n> *\"Just as Moses lifted up the snake in the wilderness, so the Son of Man must be lifted up, that everyone who believes may have eternal life in him.\"*",
        "theological_pillars": "### The Typology of Deliverance: Shadow vs Substance\n\n1. **The Poisonous Crisis:** In Numbers 21, the Israelites rebelled against God, complaining bitterly about food and water. God sent venomous serpents as a consequence of their sin. Similarly, all humanity suffers from the fatal spiritual 'bite' of sin (Romans 3:23).\n2. **The Lifted Representation:** Moses fashioned a bronze serpent—the exact likeness of the creature that brought death—and raised it on a wooden pole. On the cross, Jesus, who was entirely sinless, took upon Himself the likeness of sinful flesh and bore our curse (2 Corinthians 5:21, Galatians 3:13).\n3. **The Simple Look of Faith:** Bitten Israelites did not have to manufacture medicines, climb the pole, or perform complex rituals. They simply had to look at the bronze serpent with trusting obedience to God's promise and live.\n4. **Spiritual Salvation & Eternal Life:** In John 3:14-15, Jesus reveals that whoever looks to Him on the cross in faith is saved from eternal death and granted eternal life.",
        "deep_dive": "### Deep Dive: Biblical Typology\n\nIn Christian theology, **typology** is the study of how Old Testament persons, events, or objects (*types*) foreshadow and find their ultimate fulfillment in Jesus Christ (*antitypes*):\n\n- **The Type (Shadow):** The bronze serpent in the wilderness saved Israelites from physical, temporal death.\n- **The Antitype (Substance):** Jesus Christ lifted on the cross delivers all humanity from eternal spiritual separation from God.\n- **Healing Power in the Word:** The bronze itself possessed no magical healing properties; healing flowed directly from God in response to faith and obedience.",
        "practical": {
            "title": "Action Framework: Turning Eyes of Faith to Christ in Times of Crisis",
            "steps": [
                "Step 1: Guard Against Ingratitude — Avoid chronic grumbling and complaining about daily challenges; practice daily thanksgiving to God.",
                "Step 2: Recognize the Poison of Sin — Promptly admit when sinful attitudes (anger, deceit, bitterness) begin to poison your heart and relationships.",
                "Step 3: Fix Your Eyes on Jesus — Turn your focus away from despair and look to Christ's sacrifice through earnest prayer and faith.",
                "Step 4: Walk in Wholeness and Hope — Receive God's forgiveness and live confidently as a healed, restored child of God."
            ]
        },
        "kenyan_context": "When facing difficult socioeconomic hardships, exam anxiety, or family sickness in Kenya, people can easily fall into complaining and despair. The lesson of the bronze serpent reminds learners that focusing solely on problems increases despair, but lifting our eyes to Jesus brings divine hope, healing, and peace.",
        "reflection": "### Reflection on Obedient Faith\n\nReflect on God's method of healing:\n- Why did God command Moses to raise a bronze serpent rather than immediately removing all living snakes from the camp? How does this teach us that God uses trials to teach us obedient faith?",
        "takeaways": [
            "In Numbers 21, God provided healing to snake-bitten Israelites through a bronze serpent lifted on a pole.",
            "Jesus identified the bronze serpent as a prophetic type of His own crucifixion on the cross (John 3:14).",
            "Healing did not come from the metal, but from faith and obedience to God's promise.",
            "Looking to Jesus in faith delivers believers from the fatal curse of sin and imparts eternal life (John 3:15)."
        ],
        "mcq": {
            "question": "How did Jesus connect the Old Testament story of the bronze serpent in Numbers 21 to His mission on earth?",
            "options": [
                "A) He instructed His disciples to craft bronze statues of serpents in Christian churches",
                "B) He explained that just as the bronze serpent was lifted up on a pole, the Son of Man must be lifted up on the cross",
                "C) He commanded believers to handle venomous serpents to prove their faith",
                "D) He claimed that bronze is a sacred metal capable of curing all physical diseases"
            ],
            "answer": "B",
            "explanation": "In John 3:14-15, Jesus stated that just as Moses lifted up the bronze serpent in the wilderness, the Son of Man must be lifted up on the cross so that everyone who believes in Him may receive eternal life."
        }
    },

    # ─── LESSON 4 ────────────────────────────────────────────────────────────
    {
        "unit_order": 4,
        "unit_name": "God's Perfect Gift of Love",
        "unit_description": "Analyze John 3:16-21, focusing on God's motivation of Agape love, the sacrificial gift of His Son, and the promise of eternal life over condemnation.",
        "lesson_title": "God's Perfect Gift of Love",
        "image": {
            "url": "https://upload.wikimedia.org/wikipedia/commons/thumb/2/23/Light_over_Jerusalem_Hills.jpg/800px-Light_over_Jerusalem_Hills.jpg",
            "title": "Visual Hook: Radiant Light Piercing Darkness over Jerusalem",
            "author": "Wikimedia Public Domain Archive",
            "licensing": "Public Domain",
            "source": "Wikimedia Commons",
            "caption": "Golden sunbeams breaking through dark clouds over Jerusalem, symbolizing God's unconditional love and light sent into a broken world to redeem humanity."
        },
        "youtube": {
            "youtube_id": "slyevQ1LWmv",
            "title": "BibleProject: Agape (Unconditional Love)",
            "description": "Explores the biblical meaning of Agape love — not simply a fleeting feeling, but an active, costly commitment to seek the highest well-being of others."
        },
        "svg_fn": get_svg_lesson_4,
        "goals": [
            "Recite and explain the four foundational components of John 3:16.",
            "Differentiate between eternal life and condemnation according to John 3:16-21.",
            "Demonstrate how God's universal love inspires active compassion, generosity, and non-discrimination in daily life."
        ],
        "intro": "What is the most valuable gift you have ever received? Think of something precious given to you by someone who loved you dearly. Now imagine sacrificing your most cherished possession for someone who did not appreciate you or even treated you as an enemy.\n\nJohn 3:16 is celebrated as 'the Gospel in miniature' because in a single sentence, it captures the greatest sacrifice ever made, motivated by the purest, most unconditional love in history. Jesus revealed to Nicodemus that God's heart toward the world is not wrath and condemnation, but redemption and eternal life.",
        "core_scripture": "### Scriptural Passage: John 3:16-17\n\n> *\"For God so loved the world that he gave his one and only Son, that whoever believes in him shall not perish but have eternal life. For God did not send his Son into the world to condemn the world, but to save the world through him.\"*\n\nThis core biblical passage outlines the universal scope of divine love, the depth of divine sacrifice, the simplicity of faith, and the promise of salvation.",
        "theological_pillars": "### Deconstructing John 3:16: Four Pillars of Divine Grace\n\n1. **The Motivation (*Love / Agape*):** *'For God so loved the world...'* God's love is unconditional, active, and impartial. It transcends ethnic boundaries, social class, and moral pedigree, embracing all humanity (*kosmos*).\n2. **The Action (*Sacrificial Generosity*):** *'...that He gave His only Son...'* Divine love is demonstrated through tangible, costly action. God gave His uniquely beloved Son (*monogenes*) to die on behalf of sinners (Romans 5:8).\n3. **The Condition (*Universal Faith*):** *'...that whoever believes in Him...'* The invitation is fully inclusive (*'whoever'*). Salvation is not restricted by race or wealth, but received through personal, trusting faith in Jesus Christ.\n4. **The Promise (*Eternal Life over Condemnation*):** *'...shall not perish but have eternal life.'* Believers are delivered from spiritual ruin (*perishing*) and given *Zoe Aionios*—eternal life of peace, fellowship with God, and everlasting joy.",
        "deep_dive": "### Deep Dive: Light vs Darkness (John 3:19-21)\n\nJesus expanded on the human response to divine love:\n\n- **The Verdict on Light and Darkness:** Light has entered the world, but people often love darkness because their deeds are evil. Unbelief is not merely an intellectual problem, but a moral resistance to having one's deeds exposed.\n- **Walking into the Light:** The person who loves truth comes openly into the light, so that it may be clearly seen that their deeds are performed in obedience to God.\n- **The Purpose of Christ's Mission:** John 3:17 emphatically confirms that Jesus was sent not to condemn the world, but that the world through Him might be saved.",
        "practical": {
            "title": "Action Framework: Practicing Sacrificial Agape Love",
            "steps": [
                "Step 1: Receive God's Unconditional Love — Accept that God loves you deeply and unconditionally, freeing you from guilt and self-condemnation.",
                "Step 2: Eliminate Favoritism — Treat all classmates, neighbors, and strangers with dignity, rejecting tribalism, racism, and social bias.",
                "Step 3: Practice Costly Generosity — Share your resources, time, and academic assistance with those in need without expecting repayment.",
                "Step 4: Walk in the Light of Truth — Live honestly, confessing mistakes promptly and maintaining moral integrity in private and public."
            ]
        },
        "kenyan_context": "In Kenyan communities, sacrificial love is often demonstrated during times of hardship (Harambee spirit), when neighbors contribute to help orphans, pay medical bills, or support education. John 3:16 elevates this cultural value to a spiritual peak, showing that true love willingly sacrifices for the well-being of others.",
        "reflection": "### Reflection on God's Heart of Mercy\n\nReflect on John 3:17:\n- How does knowing that 'God did not send His Son to condemn the world, but to save it' transform your personal understanding of God's character and His desire for your life?",
        "takeaways": [
            "John 3:16 summarizes the core message of Christianity: God's universal love, sacrificial gift, and promise of eternal life.",
            "God's love (*Agape*) is demonstrated through costly action: giving His only Son for the salvation of the world.",
            "Salvation is universally available to 'whoever believes' regardless of social background or past mistakes.",
            "Jesus came not to condemn humanity, but to rescue all who turn to Him in faith (John 3:17)."
        ],
        "mcq": {
            "question": "According to John 3:16-17, what was God's primary motivation for sending His only Son into the world?",
            "options": [
                "A) To establish an earthly political empire and overthrow Roman governors",
                "B) Because He loved the world and desired to save humanity from perishing",
                "C) To punish and condemn sinners immediately for their wickedness",
                "D) To enforce mandatory financial taxation on all religious citizens"
            ],
            "answer": "B",
            "explanation": "John 3:16-17 clearly states that God sent His Son because He 'so loved the world' and desired that believers should not perish but have eternal life, not to condemn the world but to save it."
        }
    },

    # ─── LESSON 5 ────────────────────────────────────────────────────────────
    {
        "unit_order": 5,
        "unit_name": "Nicodemus' Transformation",
        "unit_description": "Trace Nicodemus' spiritual journey across the Gospel of John, showing how he grew from a fearful nighttime inquirer into a bold, public follower of Jesus Christ.",
        "lesson_title": "Nicodemus' Transformation",
        "image": {
            "url": "https://upload.wikimedia.org/wikipedia/commons/thumb/5/5e/The_Burial_of_Christ_by_Caravaggio.jpg/800px-The_Burial_of_Christ_by_Caravaggio.jpg",
            "title": "Visual Hook: The Entombment and Burial of Christ",
            "author": "Michelangelo Merisi da Caravaggio (1571–1610)",
            "licensing": "Public Domain",
            "source": "Wikimedia Commons",
            "caption": "Nicodemus and Joseph of Arimathea boldly and tenderly caring for the body of Jesus Christ, honoring Him with royal spices after the crucifixion."
        },
        "youtube": {
            "youtube_id": "RUfh_527kac",
            "title": "BibleProject: Gospel of John (Part 2 - John 13-21)",
            "description": "Explores the climax of the Gospel of John, the crucifixion, the bold devotion of secret disciples, and the victory of Jesus' resurrection."
        },
        "svg_fn": get_svg_lesson_5,
        "goals": [
            "Trace Nicodemus' spiritual transformation across three distinct passages in John's Gospel (John 3, 7, and 19).",
            "Analyze how true Christian faith overcomes fear of peer pressure and produces outward moral courage.",
            "Develop personal commitments to stand up courageously for justice, fairness, and Christian values in school and society."
        ],
        "intro": "Have you ever seen a quiet, timid student sitting at the back of the classroom who initially seemed afraid to speak up, but over time gained confidence and eventually became a bold school leader advocating for others?\n\nSpiritual growth takes time, patience, and courage. Nicodemus underwent one of the most remarkable transformations recorded in the Bible. He began in the dark shadows of fear, cautiously asking questions at night. Yet when the ultimate crisis arrived, he stepped into broad daylight to honor Jesus when almost everyone else had fled.",
        "core_scripture": "### Scriptural Passages: Tracing Nicodemus in John's Gospel\n\n#### Stage 1: The Night Inquirer (John 3:1-2)\n> *\"He came to Jesus at night and said, 'Rabbi, we know that you are a teacher who has come from God.'\"*\n\n#### Stage 2: The Legal Defender (John 7:50-51)\n> *\"Nicodemus, who had gone to Jesus earlier and who was one of their own number, asked, 'Does our law condemn a man without first hearing him to find out what he has been doing?'\"*\n\n#### Stage 3: The Bold Disciple (John 19:39-40)\n> *\"He was accompanied by Nicodemus, the man who earlier had visited Jesus at night. Nicodemus brought a mixture of myrrh and aloes, about seventy-five pounds. Taking Jesus' body, the two of them wrapped it, with the spices, in strips of linen. This was in accordance with Jewish burial customs.\"*",
        "theological_pillars": "### The 3-Stage Progression of Nicodemus' Faith\n\n1. **Stage 1 — The Secret Seeker (John 3):** Nicodemus began with curiosity mixed with fear. He came under the cover of night to protect his status as a Sanhedrin ruler, yet his questions were sincere and humble.\n2. **Stage 2 — The Courageous Defender (John 7):** When the Sanhedrin plotted to arrest and execute Jesus without a legal trial, Nicodemus stood up in the council and demanded procedural justice: *'Does our law judge a man without first giving him a hearing?'* He endured fierce mockery from his fellow rulers for defending Christ.\n3. **Stage 3 — The Royal Mourner and Bold Disciple (John 19):** After Jesus was crucified, when the 12 disciples had scattered in terror, Nicodemus stepped openly into the light. He joined Joseph of Arimathea, approached Pontius Pilate, and brought 75 pounds (about 100 Roman pounds) of fragrant myrrh and aloes to give Jesus a king's burial.\n4. **Extravagant Love and Public Loyalty:** Nicodemus' lavish gift of 75 pounds of spices was fit for royalty, demonstrating that he recognized Jesus as the true King of Israel and was willing to sacrifice his career and social standing for Him.",
        "deep_dive": "### Deep Dive: Lessons from Nicodemus' Transformation\n\nNicodemus' life provides a powerful model of discipleship:\n\n- **Faith is a Growing Process:** God does not demand instantaneous perfection; He welcomes sincere seekers and patiently guides them toward maturity.\n- **Love Casts Out Fear:** As Nicodemus understood the depth of Jesus' love and witnessed His sacrifice, his fear of peer pressure was replaced by bold devotion (1 John 4:18).\n- **Courage in Times of Crisis:** True character is tested not in times of ease, but when following the truth is unpopular, dangerous, and costly.",
        "practical": {
            "title": "Action Framework: Growing from Timid Faith to Bold Christian Witness",
            "steps": [
                "Step 1: Start with Honest Inquiries — Never be afraid to bring your sincere questions, doubts, and struggles to God in prayer and study.",
                "Step 2: Defend Justice in Small Moments — Speak up when a classmate is being falsely accused, gossiped about, or unfairly punished.",
                "Step 3: Overcome Fear of Disapproval — Remind yourself that God's eternal truth matters far more than the temporary opinions of peers.",
                "Step 4: Practice Extravagant Commitment — Dedicate your best talents, resources, and public witness to honoring Christ and serving your community."
            ]
        },
        "kenyan_context": "In Kenyan schools, standing up for an innocent classmate who is being bullied or refusing to participate in exam cheating requires immense moral courage. Nicodemus teaches Kenyan youths that true Christian leadership means standing for truth and justice even when one stands alone.",
        "reflection": "### Reflection on Growth and Public Courage\n\nReflect on your personal spiritual journey:\n- When Jesus died on the cross, His closest disciples fled in fear, yet Nicodemus stepped forward publicly to bury Him. What gave Nicodemus such extraordinary courage at that critical moment?",
        "takeaways": [
            "Nicodemus appears in three pivotal moments in John's Gospel: John 3 (night seeker), John 7 (legal defender), and John 19 (bold disciple).",
            "In John 7, Nicodemus courageously stood against his fellow Sanhedrin rulers to demand a fair legal trial for Jesus.",
            "In John 19, he publicly joined Joseph of Arimathea to provide an honorable, royal burial for Jesus with 75 pounds of spices.",
            "True faith matures over time, overcoming the fear of human disapproval to produce bold public action and sacrificial loyalty."
        ],
        "mcq": {
            "question": "How did Nicodemus demonstrate his bold, public devotion to Jesus following the crucifixion?",
            "options": [
                "A) He fled into the wilderness of Galilee to hide with the other disciples",
                "B) He delivered a loud political speech in the marketplace against Pontius Pilate",
                "C) He partnered with Joseph of Arimathea to bury Jesus, bringing 75 pounds of royal spices",
                "D) He returned to the Sanhedrin and renounced his belief in Jesus Christ"
            ],
            "answer": "C",
            "explanation": "John 19:39-40 records that Nicodemus boldly came forward with Joseph of Arimathea, bringing approximately 75 pounds of expensive myrrh and aloes to wrap and bury Jesus' body according to royal customs."
        }
    },

    # ─── LESSON 6 ────────────────────────────────────────────────────────────
    {
        "unit_order": 6,
        "unit_name": "Overcoming Spiritual Pride and Showmanship Today",
        "unit_description": "Apply the lessons of Nicodemus' encounter to contemporary youth life, warning against spiritual pride, hypocrisy, and religious showmanship while cultivating genuine humility.",
        "lesson_title": "Overcoming Spiritual Pride and Showmanship Today",
        "image": {
            "url": "https://upload.wikimedia.org/wikipedia/commons/thumb/9/93/The_Pharisee_and_the_Publican_by_Bida.jpg/800px-The_Pharisee_and_the_Publican_by_Bida.jpg",
            "title": "Visual Hook: The Pharisee and the Tax Collector",
            "author": "Alexandre Bida (1813–1895)",
            "licensing": "Public Domain",
            "source": "Wikimedia Commons",
            "caption": "Jesus' parable contrasting the self-righteous Pharisee boasting loudly in public with the humble tax collector crying out for God's mercy in secret."
        },
        "youtube": {
            "youtube_id": "P03kI3qK8z4",
            "title": "BibleProject: The Sermon on the Mount (Matthew 6)",
            "description": "Jesus' radical instructions on secret generosity, private prayer, fasting without showmanship, and seeking the approval of God rather than human praise."
        },
        "svg_fn": get_svg_lesson_6,
        "goals": [
            "Define 'spiritual pride' and 'religious showmanship' (hypocrisy) in light of Matthew 6:1-6 and James 4:6.",
            "Analyze why Jesus severely warned against performing righteous deeds solely to receive human admiration.",
            "Formulate practical strategies for practicing secret service, sincere humility, and heart integrity in daily life."
        ],
        "intro": "Have you ever observed someone perform a good deed—like picking up litter, donating food, or helping a needy person—only when a teacher was watching or so they could record a video to post on TikTok and Instagram for likes and comments?\n\nThat behavior is known as 'showmanship' or religious hypocrisy. When people perform good acts to gain human applause, their focus is on self-glory rather than loving God or neighbor. Jesus warned that true righteousness is nurtured in the quiet, secret places of the heart, not on a public stage.",
        "core_scripture": "### Scriptural Passages: Matthew 6:1-4 & James 4:6\n\n#### Matthew 6:1-4 — Beware of Practicing Righteousness for Show\n> *\"Be careful not to practice your righteousness in front of others to be seen by them. If you do, you will have no reward from your Father in heaven. So when you give to the needy, do not announce it with trumpets, as the hypocrites do in the synagogues and on the streets, to be honored by others. Truly I tell you, they have received their reward in full. But when you give to the needy, do not let your left hand know what your right hand is doing, so that your giving may be in secret. Then your Father, who sees what is done in secret, will reward you.\"*\n\n#### James 4:6 — God's Favor to the Humble\n> *\"God opposes the proud but shows favor to the humble.\"*",
        "theological_pillars": "### Theological Analysis: Hypocrisy vs Sincere Humility\n\n1. **Spiritual Pride Defined:** The dangerous spiritual attitude of believing oneself to be morally superior or more deserving of God's favor than others, leading to arrogance and contempt for struggling peers.\n2. **Religious Showmanship (Hypocrisy):** Derived from the Greek theatrical term *hypokrites* (stage actor wearing a mask). It refers to putting on a righteous public performance while the private heart is cold, selfish, and unrepentant.\n3. **Why Jesus Condemned Showmanship:**\n   - **It is Deceitful:** It misrepresents God's character and turns holy worship into personal vanity.\n   - **It Earns No Divine Reward:** Jesus warned that those who seek human praise have already received their reward in full (the fleeting applause of people).\n   - **It Prevents Genuine Repentance:** The self-righteous person cannot see their own need for God's grace and forgiveness.\n4. **The Power of Secret Service:** Jesus taught that prayer, fasting, and giving should be performed quietly before the Father who sees in secret and rewards openly.",
        "deep_dive": "### Deep Dive: Nicodemus vs the Showman Pharisees\n\nNicodemus' journey provides a vivid contrast with religious showmen of his era:\n\n- **The Showman Pharisees:** Prayed loudly on street corners, wore ostentatious phylacteries, and blew trumpets during almsgiving, yet their hearts plotted violence against Jesus.\n- **Nicodemus:** Started with quiet, humble questions in private (John 3), defended justice legally (John 7), and offered an extravagant 75-pound royal gift at Christ's tomb without seeking popularity (John 19).\n- **Integrity Defined:** Christian integrity means being the exact same righteous, compassionate person in the dark when nobody is watching as in the public light.",
        "practical": {
            "title": "Action Framework: Cultivating Sincere Humility and Silent Service",
            "steps": [
                "Step 1: Check Your Motives — Before praying, singing, or helping others, ask yourself: 'Am I doing this to honor God or to impress people?'",
                "Step 2: Practice Silent Service — Regularly perform helpful tasks (cleaning classrooms, helping siblings, tutoring peers) without telling anyone.",
                "Step 3: Guard Your Private Prayer Life — Spend focused, private time communicating with God where no one else can see or praise you.",
                "Step 4: Be Quick to Repent — Acknowledge mistakes openly, ask for forgiveness, and celebrate the accomplishments of your peers with genuine joy."
            ]
        },
        "kenyan_context": "In Kenyan schools, churches, and Christian Union (CU) fellowships, students are often elected to leadership positions (prefects, CU officials). True Christian leadership is demonstrated not through pride or looking down on others, but through servant leadership, quiet kindness, and helping vulnerable learners.",
        "reflection": "### Reflection on Humility and Integrity\n\nReflect on your daily habits:\n- How can you maintain the balance between 'letting your light shine' (Matthew 5:16) through good works while strictly avoiding the trap of doing good deeds just to boast on social media or get praise from teachers?",
        "takeaways": [
            "Spiritual pride is the dangerous attitude of believing oneself morally superior to others, which God actively opposes (James 4:6).",
            "Religious showmanship (hypocrisy) involves performing spiritual acts for the praise and admiration of human audiences (Matthew 6:1-2).",
            "Jesus commanded secret generosity, private prayer, and quiet fasting, promising that the Father who sees in secret will reward openly.",
            "Christian integrity means being genuinely righteous, humble, and faithful in private, seeking God's approval above human applause."
        ],
        "mcq": {
            "question": "What is 'spiritual pride,' and why did Jesus strongly warn His followers against it?",
            "options": [
                "A) Feeling proud when your school sports team wins a regional championship",
                "B) The dangerous belief that one is morally superior to others, leading to hypocrisy and seeking human applause rather than God's approval",
                "C) Maintaining high self-esteem and working diligently to excel in academic examinations",
                "D) Singing loudly and enthusiastically during a church or Christian Union choir session"
            ],
            "answer": "B",
            "explanation": "Spiritual pride is believing that one is more holy or righteous than others, which breeds hypocrisy and superficial showmanship. Jesus warned that God opposes the proud and desires sincere, secret humility (Matthew 6:1-4, James 4:6)."
        }
    }
]


# ─── INGESTION RUNNER ─────────────────────────────────────────────────────────

def ingest_grade9_cre_topic8():
    print("=" * 80)
    print("VLEARN INGESTION ENGINE: GRADE 9 CRE — TOPIC 8: NICODEMUS' ENCOUNTER WITH JESUS CHRIST")
    print("=" * 80)

    with transaction.atomic():
        # 1. Resolve Target Hierarchy
        curriculum = Curriculum.objects.get(id=5) # CBC
        grade = Grade.objects.get(id=18)          # Grade 9
        subject = Subject.objects.get(id=50, grade=grade) # CRE

        print(f"[✓] Target Hierarchy Verified: {curriculum.name} -> {grade.name} (ID: {grade.id}) -> {subject.name} (ID: {subject.id})")

        # 2. Get or Create Topic 8
        topic, created = Topic.objects.get_or_create(
            subject=subject,
            order=8,
            defaults={
                "name": "Nicodemus' Encounter with Jesus Christ",
                "description": "Explores Nicodemus' nighttime visit to Jesus Christ (John 3:1-21), the theological meaning of being born again of water and the Spirit, the historical significance of the Bronze Serpent, God's perfect gift of love, Nicodemus' spiritual transformation, and overcoming spiritual pride."
            }
        )
        if not created:
            topic.name = "Nicodemus' Encounter with Jesus Christ"
            topic.description = "Explores Nicodemus' nighttime visit to Jesus Christ (John 3:1-21), the theological meaning of being born again of water and the Spirit, the historical significance of the Bronze Serpent, God's perfect gift of love, Nicodemus' spiritual transformation, and overcoming spiritual pride."
            topic.save()
            print(f"[✓] Updated existing Topic: Order {topic.order} — '{topic.name}' (ID: {topic.id})")
        else:
            print(f"[✓] Created Topic: Order {topic.order} — '{topic.name}' (ID: {topic.id})")

        # Clean existing units/lessons under topic 8 for clean idempotent rebuild
        existing_units = LearningUnit.objects.filter(topic=topic)
        for unit in existing_units:
            for lsn in unit.lessons.all():
                lsn.blocks.all().delete()
                lsn.assets.all().delete()
                lsn.delete()
            unit.delete()
        print("[✓] Cleared previous units and lessons under Topic 8 for clean idempotent rebuild.")

        total_units = 0
        total_lessons = 0
        total_pages = 0
        total_blocks = 0
        total_assets = 0

        # 3. Ingest 6 Lessons
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
                    "topic_order": 8,
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
                url=f"https://vlearn.africa/assets/diagrams/cre/grade9_topic_8_lesson_{u_order}.svg",
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
        print("INGESTION SUMMARY FOR GRADE 9 CRE TOPIC 8:")
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
    ingest_grade9_cre_topic8()
